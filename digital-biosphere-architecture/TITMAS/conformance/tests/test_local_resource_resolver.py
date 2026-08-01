#!/usr/bin/env python3
"""Tests for local_resource_resolver.py."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

DBA_ROOT = Path(__file__).resolve().parents[3]
GROUNDING_ROOT = DBA_ROOT / "TITMAS" / "conformance" / "grounding"
sys.path.insert(0, str(GROUNDING_ROOT))

from local_resource_resolver import canonical

class TestCanonical(unittest.TestCase):
    def test_canonical_primitive_types(self):
        """Test that primitive types are serialized correctly."""
        self.assertEqual(canonical("string"), '"string"')
        self.assertEqual(canonical(123), "123")
        self.assertEqual(canonical(12.3), "12.3")
        self.assertEqual(canonical(True), "true")
        self.assertEqual(canonical(False), "false")
        self.assertEqual(canonical(None), "null")

    def test_canonical_special_floats(self):
        """Test special float values."""
        self.assertEqual(canonical(float("inf")), "Infinity")
        self.assertEqual(canonical(float("-inf")), "-Infinity")
        self.assertEqual(canonical(float("nan")), "NaN")

    def test_canonical_list(self):
        """Test that lists are serialized correctly."""
        self.assertEqual(canonical([3, 1, 2]), "[3,1,2]")
        self.assertEqual(canonical([]), "[]")
        self.assertEqual(canonical([None, True, False, "test"]), '[null,true,false,"test"]')

    def test_canonical_dict(self):
        """Test that dicts are sorted and serialized correctly."""
        self.assertEqual(canonical({"b": 2, "a": 1}), '{"a":1,"b":2}')
        self.assertEqual(canonical({}), "{}")

    def test_canonical_nested(self):
        """Test that nested structures are serialized correctly."""
        self.assertEqual(
            canonical({"a": [2, 1], "b": {"d": 4, "c": 3}}),
            '{"a":[2,1],"b":{"c":3,"d":4}}'
        )

if __name__ == "__main__":
    unittest.main()
