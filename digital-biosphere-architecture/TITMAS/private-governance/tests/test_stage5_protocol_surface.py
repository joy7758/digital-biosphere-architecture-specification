#!/usr/bin/env python3
"""Private Stage 5 protocol-surface reconstruction tests."""

from __future__ import annotations

import importlib.util
import json
import os
import stat
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "build_stage5_protocol_surface.py"
SPEC = importlib.util.spec_from_file_location("stage5_surface_builder", MODULE_PATH)
assert SPEC and SPEC.loader
BUILDER = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BUILDER
SPEC.loader.exec_module(BUILDER)


class Stage5ProtocolSurfaceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.tracked_output_root = BUILDER.OUTPUT_ROOT
        cls.temporary_directory = tempfile.TemporaryDirectory(
            prefix="titmas-stage5-protocol-surface-"
        )
        BUILDER.OUTPUT_ROOT = (
            Path(cls.temporary_directory.name) / "private-stage5-protocol-surface"
        )
        cls.manifest = BUILDER.build()

    @classmethod
    def tearDownClass(cls) -> None:
        BUILDER.OUTPUT_ROOT = cls.tracked_output_root
        cls.temporary_directory.cleanup()

    def test_generated_surface_matches_tracked_expected_bytes(self) -> None:
        generated_files = {
            path.relative_to(BUILDER.OUTPUT_ROOT)
            for path in BUILDER.OUTPUT_ROOT.rglob("*")
            if path.is_file()
        }
        tracked_files = {
            path.relative_to(self.tracked_output_root)
            for path in self.tracked_output_root.rglob("*")
            if path.is_file()
        }
        self.assertEqual(tracked_files, generated_files)
        for relative in sorted(generated_files):
            self.assertEqual(
                (self.tracked_output_root / relative).read_bytes(),
                (BUILDER.OUTPUT_ROOT / relative).read_bytes(),
                str(relative),
            )

    def test_manifest_is_private_and_default_deny(self) -> None:
        self.assertFalse(self.manifest["public_release_allowed"])
        self.assertTrue(self.manifest["private_stage_5_use_allowed"])
        self.assertFalse(self.manifest["git_tracking_default"])

    def test_every_payload_is_hash_and_source_bound(self) -> None:
        for entry in self.manifest["files"]:
            path = BUILDER.OUTPUT_ROOT / entry["path"]
            self.assertEqual(
                entry["output_sha256"], BUILDER.sha256_bytes(path.read_bytes())
            )
            self.assertRegex(entry["source_blob_sha"], r"^[0-9a-f]{40}$")
            self.assertFalse(entry["public_release_allowed"])

    def test_surface_contains_only_allowed_extensions(self) -> None:
        for path in BUILDER.OUTPUT_ROOT.rglob("*"):
            if path.is_file():
                self.assertIn(path.suffix, {".json", ".md"})
                self.assertFalse(path.is_symlink())

    def test_surface_scans_are_zero(self) -> None:
        self.assertEqual(
            {
                "protocol_surface_core_source_findings": 0,
                "protocol_surface_private_path_findings": 0,
                "protocol_surface_secret_findings": 0,
                "protocol_surface_symlink_findings": 0,
            },
            self.manifest["findings"],
        )

    def test_generated_permissions_are_private(self) -> None:
        self.assertEqual(
            0o700, stat.S_IMODE(BUILDER.OUTPUT_ROOT.stat().st_mode)
        )
        for path in BUILDER.OUTPUT_ROOT.rglob("*"):
            expected = 0o700 if path.is_dir() else 0o600
            self.assertEqual(expected, stat.S_IMODE(path.stat().st_mode))

    def test_no_private_implementation_payload(self) -> None:
        names = {
            path.name for path in BUILDER.OUTPUT_ROOT.rglob("*") if path.is_file()
        }
        self.assertNotIn("harness.py", names)
        self.assertNotIn("response_capture.py", names)
        self.assertNotIn("service.py", names)


if __name__ == "__main__":
    unittest.main()
