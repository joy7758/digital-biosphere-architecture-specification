#!/usr/bin/env python3

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]
TRIAL_ROOT = PROJECT_ROOT / "TITMAS" / "private-stage5-1-trial"
sys.path.insert(0, str(TRIAL_ROOT))

import build_trial_repository
import validate_trial_repository


def revision() -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"],
        cwd=PROJECT_ROOT,
        text=True,
    ).strip()


class TrialReconstructionTests(unittest.TestCase):
    def test_reconstruction_is_manifest_complete_and_zero_finding(self):
        with tempfile.TemporaryDirectory(
            prefix="titmas-stage51-build-"
        ) as raw:
            root = Path(raw) / "trial"
            manifest = build_trial_repository.build(root, revision())
            result = validate_trial_repository.validate(root)
            self.assertEqual("PASS", result["status"])
            self.assertEqual(len(manifest["files"]), result["files_checked"])
            self.assertEqual(3, result["trial_tasks_checked"])
            self.assertEqual(0, result["core_access_count"])
            self.assertEqual(0, result["real_model_call_count"])
            self.assertFalse(manifest["public_release_allowed"])
            self.assertFalse(manifest["git_history_copied"])

    def test_unmanifested_file_fails_closed(self):
        with tempfile.TemporaryDirectory(
            prefix="titmas-stage51-extra-"
        ) as raw:
            root = Path(raw) / "trial"
            build_trial_repository.build(root, revision())
            (root / "unexpected.txt").write_text("unexpected", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "manifest differ"):
                validate_trial_repository.validate(root)

    def test_modified_file_hash_fails_closed(self):
        with tempfile.TemporaryDirectory(
            prefix="titmas-stage51-hash-"
        ) as raw:
            root = Path(raw) / "trial"
            build_trial_repository.build(root, revision())
            (root / "README.md").write_text("changed", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "hash mismatch"):
                validate_trial_repository.validate(root)

    def test_symlink_fails_closed(self):
        with tempfile.TemporaryDirectory(
            prefix="titmas-stage51-symlink-"
        ) as raw:
            root = Path(raw) / "trial"
            build_trial_repository.build(root, revision())
            target = root / "trial" / "linked.md"
            target.symlink_to(root / "README.md")
            manifest_path = root / "trial-source-manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["files"].append({
                "source_repository":
                    build_trial_repository.SOURCE_REPOSITORY,
                "source_commit": revision(),
                "source_path": build_trial_repository.BUILDER_REF,
                "source_blob_sha": "0" * 40,
                "classification": "COMMERCIAL_CUSTOMER_ONLY",
                "trial_output_path": "trial/linked.md",
                "trial_output_sha256": "0" * 64,
                "security_scan_status": "PASS_ZERO_FINDINGS",
                "commercial_review_status": "PRIVATE_TRIAL_D01_APPROVED",
                "trial_release_status": "PRIVATE_TRIAL_ONLY",
                "public_release_allowed": False,
            })
            manifest_path.write_text(
                json.dumps(manifest, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            with self.assertRaises(ValueError):
                validate_trial_repository.validate(root)


if __name__ == "__main__":
    unittest.main()
