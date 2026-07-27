#!/usr/bin/env python3
"""Offline unit tests for the CE-G7 release-control primitives."""

from __future__ import annotations

import hashlib
import importlib.util
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parent


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


control = load_module("ce_g7_release_control", ROOT / "ce_g7_release_control.py")


class ReleaseControlTests(unittest.TestCase):
    def test_validate_file_accepts_exact_bytes_and_hash(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            release = Path(directory)
            value = b"exact-ce-g7-fixture"
            (release / "fixture").write_bytes(value)
            control.validate_file(
                release,
                "fixture",
                len(value),
                hashlib.sha256(value).hexdigest(),
            )

    def test_validate_file_rejects_hash_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            release = Path(directory)
            (release / "fixture").write_bytes(b"changed")
            with self.assertRaises(control.GateFailure):
                control.validate_file(release, "fixture", 7, "0" * 64)

    def test_atomic_switch_requires_exact_current_and_is_atomic(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            old = root / "old"
            new = root / "new"
            old.mkdir()
            new.mkdir()
            current = root / "current"
            temp = root / ".current-temp"
            current.symlink_to(old)
            control.atomic_switch(current, old, new, temp)
            self.assertEqual(current.readlink(), new)
            self.assertFalse(temp.exists())

    def test_atomic_switch_rejects_unexpected_current(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            old = root / "old"
            other = root / "other"
            target = root / "target"
            for path in (old, other, target):
                path.mkdir()
            current = root / "current"
            current.symlink_to(other)
            with self.assertRaises(control.GateFailure):
                control.atomic_switch(
                    current, old, target, root / ".current-temp"
                )
            self.assertEqual(current.readlink(), other)


if __name__ == "__main__":
    unittest.main()
