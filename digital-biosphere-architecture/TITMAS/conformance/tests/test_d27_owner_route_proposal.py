from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PROPOSAL_ROOT = ROOT / "architecture" / "proposals"
ASSESSMENT_PATH = PROPOSAL_ROOT / "d27-owner-route-coverage-assessment.json"
NORMALIZATION_PATH = PROPOSAL_ROOT / "d27-owner-route-normalization-proposal.json"
DBA_MAP_PATH = ROOT / "TITMAS" / "agent-native" / "evolution" / "canonical-owner-map.json"
PROJECTION_PATH = ROOT / "cockpit" / "projections" / "titmac-scout.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class D27OwnerRouteProposalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.assessment = load(ASSESSMENT_PATH)
        cls.proposal = load(NORMALIZATION_PATH)
        cls.owner_map = load(DBA_MAP_PATH)
        cls.projection = load(PROJECTION_PATH)

    def test_d27_r01_all_d26_problem_types_are_classified(self) -> None:
        rows = self.assessment["assessments"]
        self.assertEqual(10, len(rows))
        self.assertEqual(10, len({row["d26_problem_type"] for row in rows}))
        self.assertEqual(0, self.assessment["unclassified_types"])

    def test_d27_r02_exact_routes_remain_unchanged(self) -> None:
        digest = hashlib.sha256(DBA_MAP_PATH.read_bytes()).hexdigest()
        self.assertEqual(
            self.assessment["source_baselines"]["dba_normative_owner_map_sha256"],
            digest,
        )
        self.assertFalse(self.assessment["owner_map_changed"])

    def test_d27_r03_aliases_cannot_change_owner(self) -> None:
        routes = {
            problem_type: route["canonical_owner_repository"]
            for route in self.owner_map["routes"]
            for problem_type in route["problem_types"]
        }
        for alias in self.proposal["conditional_exact_alias_candidates"]:
            self.assertEqual(routes[alias["normalized_type"]], alias["existing_owner"])
            self.assertTrue(alias["owner_unchanged"])
            self.assertTrue(alias["routing_result_unchanged"])

    def test_d27_r04_ambiguous_routes_fail_closed(self) -> None:
        rows = [
            row for row in self.assessment["assessments"]
            if row["classification"] == "AMBIGUOUS_OWNER"
        ]
        self.assertEqual(4, len(rows))
        self.assertTrue(all(row["candidate_owner"] == "HOLD_OWNER_REVIEW_REQUIRED" for row in rows))
        self.assertEqual(
            "HOLD_OWNER_REVIEW_REQUIRED",
            self.proposal["failure_behavior"]["ambiguous_type"],
        )

    def test_d27_r05_unknown_routes_fail_closed(self) -> None:
        self.assertEqual(
            "HOLD_OWNER_REVIEW_REQUIRED",
            self.proposal["failure_behavior"]["unknown_type"],
        )

    def test_d27_r06_agent_cannot_handwrite_owner(self) -> None:
        self.assertFalse(self.proposal["failure_behavior"]["agent_can_handwrite_owner"])
        self.assertEqual([], self.proposal["new_owner_assignments"])

    def test_d27_r07_no_default_dba_route(self) -> None:
        self.assertFalse(self.proposal["failure_behavior"]["default_route_to_dba"])

    def test_d27_r08_no_default_scout_route(self) -> None:
        self.assertFalse(self.proposal["failure_behavior"]["default_route_to_scout"])

    def test_d27_r09_normalization_precedes_owner_resolution(self) -> None:
        self.assertEqual(
            [
                "RAW_OBSERVATION_TYPE",
                "CONTEXT_BOUND_EXACT_NORMALIZATION",
                "CANONICAL_PROBLEM_TYPE",
                "CANONICAL_OWNER_RESOLVER",
            ],
            self.proposal["design"]["pipeline"],
        )
        self.assertTrue(self.proposal["design"]["normalization_precedes_owner_resolution"])

    def test_d27_r10_proposal_modifies_no_executable_map(self) -> None:
        self.assertFalse(self.proposal["owner_map_changed"])
        self.assertFalse(self.proposal["owner_resolver_changed"])
        self.assertFalse(self.proposal["implementation_authorized"])
        self.assertEqual("2.1.0", self.owner_map["version"])

    def test_d27_r11_authority_route_change_is_er3_candidate(self) -> None:
        self.assertEqual(
            "ER-3_CANDIDATE",
            self.proposal["authority_and_risk"]["proposed_change_risk"],
        )
        self.assertTrue(
            self.proposal["authority_and_risk"]["new_owner_assignment_is_authority_routing_change"]
        )

    def test_d27_r12_d26_negative_evidence_is_retained(self) -> None:
        summary = self.projection["summary"]
        self.assertEqual(
            "evolution-runs/D26-SECOND-INDEPENDENT-ER1",
            summary["latest_evolution_run"],
        )
        self.assertEqual(
            "NO_ELIGIBLE_INDEPENDENT_ER1_FOUND",
            summary["latest_evolution_result"],
        )
        self.assertTrue(
            any(
                "D24-DBA-ER1-001 remains the last retained self-healing run" in item
                for item in summary["known_limitations"]
            )
        )


if __name__ == "__main__":
    unittest.main()
