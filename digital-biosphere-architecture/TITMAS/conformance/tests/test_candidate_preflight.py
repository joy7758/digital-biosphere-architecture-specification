#!/usr/bin/env python3

import sys
import unittest
import hashlib
from pathlib import Path

DBA_ROOT = Path(__file__).resolve().parents[3]
GROUNDING_ROOT = DBA_ROOT / "TITMAS" / "conformance" / "grounding"
sys.path.insert(0, str(GROUNDING_ROOT))

from candidate_preflight import canonical, candidate_hash

class TestCandidatePreflightHash(unittest.TestCase):
    def test_canonical_simple_types(self):
        self.assertEqual(canonical("test"), '"test"')
        self.assertEqual(canonical(123), '123')
        self.assertEqual(canonical(True), 'true')
        self.assertEqual(canonical(False), 'false')
        self.assertEqual(canonical(None), 'null')

    def test_canonical_dict_ordering(self):
        d1 = {"b": 2, "a": 1, "c": 3}
        self.assertEqual(canonical(d1), '{"a":1,"b":2,"c":3}')

        # Nested ordering
        d2 = {"z": {"b": 2, "a": 1}, "y": 1}
        self.assertEqual(canonical(d2), '{"y":1,"z":{"a":1,"b":2}}')

    def test_canonical_list(self):
        l1 = [3, 1, 2]
        self.assertEqual(canonical(l1), '[3,1,2]')

        # Nested dicts in list
        l2 = [{"b": 2, "a": 1}, {"c": 3}]
        self.assertEqual(canonical(l2), '[{"a":1,"b":2},{"c":3}]')

    def test_canonical_unicode(self):
        # ensure_ascii=False
        u1 = {"name": "你好"}
        self.assertEqual(canonical(u1), '{"name":"你好"}')

    def test_candidate_hash_deterministic(self):
        d1 = {"b": 2, "a": 1, "c": 3}
        d2 = {"c": 3, "b": 2, "a": 1}

        h1 = candidate_hash(d1)
        h2 = candidate_hash(d2)

        self.assertEqual(h1, h2)
        self.assertTrue(h1.startswith("sha256:"))
        self.assertEqual(len(h1), 7 + 64) # "sha256:" + 64 char hex string

    def test_candidate_hash_value(self):
        d = {"a": 1}
        expected_digest = hashlib.sha256(b'{"a":1}').hexdigest()
        expected_hash = f"sha256:{expected_digest}"
        self.assertEqual(candidate_hash(d), expected_hash)

if __name__ == '__main__':
    unittest.main()
