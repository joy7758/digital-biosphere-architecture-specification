from __future__ import annotations

import hashlib
import json
import subprocess
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path


COCKPIT = Path(__file__).resolve().parents[1]
ROOT = COCKPIT.parent

import sys

sys.path.insert(0, str(COCKPIT))
from read_only_status_adapter import CockpitSourceError, ReadOnlyStatusAdapter, canonical_json


class TitmacScoutBridgeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.scout = Path(self.temporary_directory.name) / "titmac-scout-fixture"
        (self.scout / "governance").mkdir(parents=True)
        status = self.fixture_status()
        status_bytes = canonical_json(status).encode("utf-8")
        (self.scout / "governance" / "project-status.json").write_bytes(status_bytes)
        schema = {
            "type": "object",
            "required": sorted(status.keys()),
            "properties": {key: {} for key in status},
        }
        (self.scout / "governance" / "project-status.schema.json").write_text(
            canonical_json(schema), encoding="utf-8"
        )
        self.git("init", "-b", "main")
        self.git("config", "user.name", "D20 Test Fixture")
        self.git("config", "user.email", "d20-fixture@example.invalid")
        self.git("add", "governance")
        self.git("commit", "-m", "fixture")
        self.git("branch", "codex/titmac-scout-status-contract-d20")
        self.expected_revision = self.git("rev-parse", "HEAD")
        self.expected_tree = self.git("rev-parse", "HEAD^{tree}")
        self.expected_digest = hashlib.sha256(status_bytes).hexdigest()

        registry = json.loads((COCKPIT / "source-registry.json").read_text(encoding="utf-8"))
        entry = registry["sources"][0]
        entry["candidate_source_revision"] = self.expected_revision
        entry["candidate_source_tree_digest"] = self.expected_tree
        entry["candidate_status_digest"] = self.expected_digest
        self.registry_path = Path(self.temporary_directory.name) / "source-registry.json"
        self.registry_path.write_text(canonical_json(registry), encoding="utf-8")
        self.adapter = ReadOnlyStatusAdapter(self.registry_path)
        self.at = datetime(2026, 8, 2, 8, 0, tzinfo=timezone.utc)

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def test_sc_d20_t06_source_revision_verified(self) -> None:
        projection = self.adapter.fetch_local_git("titmac-scout", self.scout, candidate=True, retrieved_at=self.at)
        self.assertEqual(self.expected_revision, projection["source_revision"])
        self.assertTrue(projection["source_revision_match"])
        mismatched = self.adapter_with_registry_override(candidate_source_revision="0" * 40)
        with self.assertRaisesRegex(CockpitSourceError, "SOURCE_DRIFT:REVISION_MISMATCH"):
            mismatched.fetch_local_git("titmac-scout", self.scout, candidate=True, retrieved_at=self.at)

    def test_sc_d20_t07_source_digest_verified(self) -> None:
        projection = self.adapter.fetch_local_git("titmac-scout", self.scout, candidate=True, retrieved_at=self.at)
        self.assertEqual(self.expected_digest, projection["status_source_digest"])
        self.assertEqual("PASS", projection["source_integrity"])
        mismatched = self.adapter_with_registry_override(candidate_status_digest="0" * 64)
        with self.assertRaisesRegex(CockpitSourceError, "SOURCE_INVALID:DIGEST_MISMATCH"):
            mismatched.fetch_local_git("titmac-scout", self.scout, candidate=True, retrieved_at=self.at)

    def test_sc_d20_t08_stale_status_fails_closed(self) -> None:
        with self.assertRaisesRegex(CockpitSourceError, "SOURCE_STALE"):
            self.adapter.fetch_local_git(
                "titmac-scout",
                self.scout,
                candidate=True,
                retrieved_at=datetime(2026, 8, 6, tzinfo=timezone.utc),
            )

    def test_sc_d20_t09_unavailable_source_fails_closed(self) -> None:
        with self.assertRaisesRegex(CockpitSourceError, "SOURCE_UNAVAILABLE"):
            self.adapter.fetch_local_git(
                "titmac-scout", Path("/definitely/not/a/repository"), candidate=True, retrieved_at=self.at
            )

    def test_sc_d20_t12_cockpit_adapter_is_read_only(self) -> None:
        public_methods = {name for name in dir(self.adapter) if not name.startswith("_")}
        forbidden = {"write", "push", "merge", "open_pr", "trigger_repair", "issue_credential", "activate_mutation"}
        self.assertTrue(forbidden.isdisjoint(public_methods))
        self.assertEqual("READ_ONLY", self.adapter.source("titmac-scout")["access_mode"])

    def test_sc_d20_t13_no_raw_run_is_copied_to_dba(self) -> None:
        projection = self.adapter.fetch_local_git("titmac-scout", self.scout, candidate=True, retrieved_at=self.at)
        serialized = canonical_json(projection)
        for forbidden in ("raw evolution run", "raw patch variant", "raw sandbox output", "raw model output", "credential"):
            self.assertNotIn(forbidden, serialized.lower())
        self.assertFalse(projection["projection_boundaries"]["raw_run_copied"])
        self.assertFalse(projection["projection_boundaries"]["cockpit_stores_canonical_run"])

    def test_sc_d20_t16_p0_10_remains_closed(self) -> None:
        projection = self.adapter.fetch_local_git("titmac-scout", self.scout, candidate=True, retrieved_at=self.at)
        self.assertFalse(projection["summary"]["p0_10_reopened"])

    def test_sc_d20_t17_pr105_remains_draft(self) -> None:
        snapshot = json.loads((COCKPIT / "external-pr-boundaries.json").read_text(encoding="utf-8"))
        item = next(item for item in snapshot["pull_requests"] if item["number"] == 105)
        self.assertEqual("OPEN", item["state"])
        self.assertTrue(item["is_draft"])
        self.assertEqual("PENDING", item["ownership_review"])

    def test_sc_d20_t18_pr106_remains_draft(self) -> None:
        snapshot = json.loads((COCKPIT / "external-pr-boundaries.json").read_text(encoding="utf-8"))
        item = next(item for item in snapshot["pull_requests"] if item["number"] == 106)
        self.assertEqual("OPEN", item["state"])
        self.assertTrue(item["is_draft"])
        self.assertEqual("PENDING", item["migration_review"])

    def test_sc_d20_t20_clean_refresh_replay(self) -> None:
        first = self.adapter.fetch_local_git("titmac-scout", self.scout, candidate=True, retrieved_at=self.at)
        second = self.adapter.fetch_local_git("titmac-scout", self.scout, candidate=True, retrieved_at=self.at)
        self.assertEqual(canonical_json(first), canonical_json(second))

    def git(self, *arguments: str) -> str:
        result = subprocess.run(
            ["git", "-C", str(self.scout), *arguments],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()

    def adapter_with_registry_override(self, **overrides: object) -> ReadOnlyStatusAdapter:
        registry = json.loads(self.registry_path.read_text(encoding="utf-8"))
        registry["sources"][0].update(overrides)
        path = Path(self.temporary_directory.name) / f"registry-{len(overrides)}-{next(iter(overrides))}.json"
        path.write_text(canonical_json(registry), encoding="utf-8")
        return ReadOnlyStatusAdapter(path)

    @staticmethod
    def fixture_status() -> dict[str, object]:
        progress = {
            stage: {
                "status": "NOT_ASSESSED",
                "updated_at": None,
                "evidence_reference": None,
                "source_revision": "SELF",
                "limitations": ["Synthetic adapter test fixture only."],
            }
            for stage in (
                "OBSERVE DISCOVER EVIDENCE REPRODUCE CLASSIFY_RISK RESOLVE_OWNER "
                "GENERATE_VARIANTS IMPLEMENT_IN_SANDBOX EVALUATE_FITNESS SELECT "
                "AWAIT_AUTHORIZATION APPLY OBSERVE_OUTCOME RETAIN_OR_ROLLBACK RECORD_LINEAGE"
            ).split()
        }
        return {
            "status_contract_version": "0.1",
            "project_id": "titmac-scout",
            "project_name": "titmac-scout",
            "conversation_aliases": ["tiamas-scout"],
            "repository": "joy7758/titmac-scout",
            "repository_visibility": "PRIVATE",
            "canonical_branch": "main",
            "source_revision": "SELF",
            "source_tree_digest": "SELF_TREE",
            "architecture_owner": "joy7758/digital-biosphere-architecture-specification",
            "implementation_owner": "joy7758/titmac-scout",
            "evidence_semantics_owner": "TITMAS_EVIDENCE_ARCHITECTURE",
            "lifecycle_status": "IMPLEMENTING",
            "development_phase": "D20_STATUS_CONTRACT",
            "implementation_status": "IMPLEMENTATION_EXISTS_READY_FOR_HUMAN_REVIEW",
            "discovery_layer_status": "CANDIDATE",
            "self_observation_status": "CANDIDATE",
            "problem_evidence_status": "CANDIDATE",
            "canonical_owner_resolution_status": "NOT_ASSESSED",
            "patch_variant_status": "NOT_ASSESSED",
            "sandbox_implementation_status": "NOT_ASSESSED",
            "fitness_evaluation_status": "NOT_ASSESSED",
            "selection_status": "NOT_ASSESSED",
            "rollback_status": "NOT_ASSESSED",
            "lineage_status": "NOT_ASSESSED",
            "self_healing_status": "NOT_ASSESSED",
            "self_evolution_status": "NOT_ASSESSED",
            "autonomous_risk_classes": [],
            "human_authorization_risk_classes": [],
            "latest_evolution_run": None,
            "latest_run_result": None,
            "latest_run_digest": None,
            "latest_outcome_evidence": None,
            "latest_rollback_evidence": None,
            "test_summary": {"status": "PASS"},
            "ci_summary": {"status": "NOT_ASSESSED"},
            "open_pull_requests": [],
            "blocking_issues": [],
            "blocking_decisions": ["D20_DRAFT_PRS_REQUIRE_HUMAN_REVIEW"],
            "next_human_decision": "REVIEW_TITMAC_SCOUT_AND_COCKPIT_BRIDGE_DRAFT_PRS",
            "known_limitations": ["Synthetic adapter test fixture only."],
            "authority_boundaries": ["COCKPIT_PULL_ONLY"],
            "security_boundaries": ["P0_10_CLOSED"],
            "evolution_progress": progress,
            "progress_percent": 0,
            "p0_10_reopened": False,
            "production_runtime_changed": False,
            "database_changed": False,
            "production_credential_created": False,
            "generated_at": "2026-08-02T07:15:47Z",
            "fresh_until": "2026-08-05T07:15:47Z",
        }


if __name__ == "__main__":
    unittest.main()
