"""Offline tests for the CE-G6 read-only release revalidator."""

from __future__ import annotations

import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tarfile
import tempfile
import unittest
from unittest import mock


MODULE_PATH = Path(__file__).with_name("ce_g6_release_revalidator.py")
SPEC = importlib.util.spec_from_file_location(
    "ce_g6_release_revalidator", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load ce_g6_release_revalidator")
revalidator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(revalidator)


def digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


class RevalidatorTests(unittest.TestCase):
    def create_fixture(self, root: Path) -> dict[str, Path | str | int]:
        current = root / "current"
        stable = root / "stable"
        stable.mkdir()
        current.symlink_to(stable)
        proposed = root / "proposed"
        proposed.mkdir()
        source_revision = "fixture-source-revision"

        entry = {
            "status": "DEVELOPMENT_CONTRACT_SOURCE_PREPARED_NOT_DEPLOYED",
            "maturity": "Development",
            "evaluation_only": True,
            "effects": {
                "authority": False,
                "permission": False,
                "runtime": False,
            },
            "recommendation_policy": {
                "production_result": "DO_NOT_RECOMMEND_FOR_PRODUCTION",
                "recommendation_creates_decision": False,
                "recommendation_creates_permission": False,
            },
        }
        status = {
            "commercial_evaluation": {
                "available_offering": False,
                "production_ready": False,
                "sla_defined": False,
                "customers_verified": 0,
                "contracts_created": 0,
            },
            "release": {
                "production_ready": False,
                "customer_adoption_claimed": False,
            },
        }
        bodies: dict[str, bytes] = {
            "TITMAS-AGENT-EVALUATION-ENTRY-v0.1.json": (
                json.dumps(entry) + "\n"
            ).encode(),
            "status.json": (json.dumps(status) + "\n").encode(),
        }
        for index in range(58):
            bodies[f"fixture-{index:02d}.txt"] = (
                f"fixture {index}\n".encode()
            )
        self.assertEqual(len(bodies), 60)

        entries = []
        for relative, body in bodies.items():
            path = proposed / relative
            path.write_bytes(body)
            entries.append(
                {
                    "path": relative,
                    "bytes": len(body),
                    "sha256": digest(body),
                }
            )
        manifest = {
            "schema_version": "0.1",
            "source_revision": source_revision,
            "files": entries,
        }
        (proposed / "release-manifest.json").write_text(
            json.dumps(manifest) + "\n", encoding="utf-8"
        )

        archive = root / "release.tar.gz"
        with tarfile.open(archive, mode="w:gz") as bundle:
            for path in sorted(proposed.iterdir()):
                bundle.add(path, arcname=path.name, recursive=False)
        return {
            "current": current,
            "stable": stable,
            "proposed": proposed,
            "archive": archive,
            "source_revision": source_revision,
            "archive_bytes": archive.stat().st_size,
            "archive_sha256": revalidator.sha256_file(archive),
        }

    def patch_fixture(self, fixture: dict[str, Path | str | int]):
        return mock.patch.multiple(
            revalidator,
            CURRENT_LINK=fixture["current"],
            EXPECTED_CURRENT=fixture["stable"].resolve(),
            PROPOSED_SOURCE=fixture["source_revision"],
            PROPOSED_RELEASE=fixture["proposed"],
            ARCHIVE=fixture["archive"],
            EXPECTED_ARCHIVE_BYTES=fixture["archive_bytes"],
            EXPECTED_ARCHIVE_SHA256=fixture["archive_sha256"],
        )

    def test_exact_fixture_passes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = self.create_fixture(Path(directory))
            with self.patch_fixture(fixture):
                result = revalidator.validate()
        self.assertEqual(result["manifest"]["files_verified"], 60)
        self.assertEqual(result["archive"]["regular_files_verified"], 61)
        self.assertTrue(result["truth_boundary"]["effects_all_false"])

    def test_archive_hash_mismatch_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = self.create_fixture(Path(directory))
            fixture["archive_sha256"] = "0" * 64
            with self.patch_fixture(fixture):
                with self.assertRaisesRegex(
                    revalidator.RevalidationError,
                    "ARCHIVE_SHA256_MISMATCH",
                ):
                    revalidator.validate()

    def test_unsafe_archive_member_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixture = self.create_fixture(root)
            archive = fixture["archive"]
            self.assertIsInstance(archive, Path)
            with tarfile.open(archive, mode="w:gz") as bundle:
                info = tarfile.TarInfo("../escape.txt")
                body = b"escape"
                info.size = len(body)
                bundle.addfile(info, io.BytesIO(body))
            fixture["archive_bytes"] = archive.stat().st_size
            fixture["archive_sha256"] = revalidator.sha256_file(archive)
            with self.patch_fixture(fixture):
                with self.assertRaisesRegex(
                    revalidator.RevalidationError,
                    "UNSAFE_ARCHIVE_PATH",
                ):
                    revalidator.validate()


if __name__ == "__main__":
    unittest.main()
