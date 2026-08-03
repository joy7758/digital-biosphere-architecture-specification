from __future__ import annotations

import json
import unittest
from pathlib import Path

from TITMAS.conformance.harness import validate_schema


ROOT = Path(__file__).resolve().parents[3]


def load(relative: str):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


class FdoPvs0CockpitProjectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.projection = load("cockpit/projections/titmas-fdo-pvs0.json")
        cls.schema = load("cockpit/fdo-pvs0-projection.schema.json")

    def test_projection_matches_schema(self):
        validate_schema(self.projection, self.schema)

    def test_exact_public_evidence_is_pinned(self):
        source = self.projection["public_source"]
        self.assertEqual("1dcca69d0bcc2ee94b7e3ef0c80f21536cd39d1c", source["revision"])
        self.assertEqual(43, source["file_count"])
        self.assertEqual(10, source["tests"]["passed"])
        self.assertEqual(0, source["tests"]["failed"])
        self.assertEqual("10.5281/zenodo.21778954", self.projection["archive"]["record_doi"])
        self.assertEqual("10.5281/zenodo.21778953", self.projection["archive"]["concept_doi"])
        self.assertEqual("09defa9345bf5ff6c766c5efa88130e0", self.projection["archive"]["file_md5"])
        self.assertEqual(43, self.projection["archive"]["archive_file_count"])
        self.assertTrue(self.projection["archive"]["matches_public_commit_tree"])

    def test_five_record_types_remain_distinct(self):
        records = self.projection["records"]
        counts = {name: sum(item["classification"] == name for item in records) for name in ("FdoProfile", "BasicInfoType", "FdoService")}
        self.assertEqual({"FdoProfile": 2, "BasicInfoType": 2, "FdoService": 1}, counts)
        service = next(item for item in records if item["identifier"].endswith("aro-audit-demo-do-1"))
        self.assertEqual("FdoService", service["classification"])

    def test_candidates_and_demo_assets_are_not_normative(self):
        records = self.projection["records"]
        self.assertTrue(all(not item["normative"] for item in records))
        self.assertEqual(2, sum(item["target_disposition"] == "STANDARDIZATION_CANDIDATE_ASSET" for item in records))
        self.assertEqual(3, sum(item["target_disposition"] == "NON_NORMATIVE_DEMO_AND_HISTORICAL_EVIDENCE" for item in records))

    def test_migration_waits_for_external_confirmation(self):
        migration = self.projection["migration"]
        self.assertEqual("WAITING_FOR_GWDG_RESPONSE", migration["status"])
        self.assertEqual("NOT_YET_RECEIVED", migration["external_confirmation"])
        self.assertTrue(migration["forbidden_reclassification"])

    def test_stale_embedded_status_is_not_silently_rewritten(self):
        consistency = self.projection["source_consistency"]
        self.assertEqual("PASS_WITH_STALE_EMBEDDED_STATUS_RECORDED", consistency["result"])
        self.assertGreaterEqual(len(consistency["conflicts"]), 4)

    def test_no_authority_runtime_standard_or_adoption_is_created(self):
        boundaries = self.projection["boundaries"]
        self.assertTrue(all(value is False for value in boundaries.values()))
        self.assertEqual("FROZEN_MAINTENANCE_MODE", self.projection["line_status"])


if __name__ == "__main__":
    unittest.main()
