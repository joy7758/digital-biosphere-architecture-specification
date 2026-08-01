from __future__ import annotations

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[3]
PROJECTION = ROOT / "TITMAS/specifications/portfolio/agent-action-gate.json"
PROPOSAL = ROOT / "TITMAS/specifications/proposals/titmas-agent-action-gate-admission-v0.1.md"


class AgentActionGatePortfolioTests(unittest.TestCase):
    def setUp(self) -> None:
        self.projection = json.loads(PROJECTION.read_text(encoding="utf-8"))
        self.proposal = PROPOSAL.read_text(encoding="utf-8")

    def test_public_reference_implementation_source_is_exactly_pinned(self) -> None:
        self.assertEqual(
            self.projection["canonical_remote_repository"],
            "https://github.com/joy7758/titmas-agent-action-gate",
        )
        self.assertEqual(self.projection["observed_branch"], "agent/implement-action-gate-runtime")
        self.assertEqual(
            self.projection["observed_commit"],
            "27ccf953421e1491177c7946a31296a1e1eabe29",
        )
        self.assertEqual(
            self.projection["contract_ci"]["head_sha"],
            self.projection["observed_commit"],
        )
        self.assertEqual(self.projection["contract_ci"]["conclusion"], "SUCCESS")

    def test_existence_and_management_do_not_elevate_authority(self) -> None:
        self.assertFalse(self.projection["portfolio_admission"])
        self.assertTrue(self.projection["dba_management_policy_granted"])
        self.assertFalse(self.projection["github_acl_changed"])
        self.assertFalse(self.projection["runtime_permission_created"])
        self.assertTrue(self.projection["implementation_started"])
        self.assertTrue(self.projection["action_gate_implemented"])
        self.assertTrue(self.projection["mcp_server_implemented"])
        self.assertFalse(self.projection["live_agentteams_deployed"])
        self.assertFalse(self.projection["competition_submission"])

    def test_gates_preserve_reference_and_non_release_boundaries(self) -> None:
        gates = self.projection["gates"]
        self.assertEqual(gates["G0"], "REVIEW_REQUIRED_READY_FOR_HUMAN_DECISION")
        self.assertEqual(gates["G1"], "PASS_PUBLIC_DRAFT_PR_SOURCE_PINNED")
        self.assertIn("REFERENCE_IMPLEMENTATION", gates["G3"])
        self.assertIn("NOT_INDEPENDENT", gates["G4"])
        self.assertIn("RUNTIME_PERMISSION_NOT_CREATED", gates["G5"])
        self.assertIn("NO_MERGE", gates["G6"])
        self.assertEqual(gates["G8"], "NOT_RELEASED_NOT_ADOPTED_NOT_SUBMITTED")

    def test_proposal_is_review_ready_but_not_admitted(self) -> None:
        self.assertIn("status: READY_FOR_REVIEW", self.proposal)
        self.assertIn("PORTFOLIO_ADMISSION_GRANTED=false", self.proposal)
        self.assertIn("ACTION_GATE_REFERENCE_IMPLEMENTED=true", self.proposal)
        self.assertIn("LIVE_AGENTTEAMS_DEPLOYED=false", self.proposal)
        self.assertIn("COMPETITION_SUBMITTED=false", self.proposal)


if __name__ == "__main__":
    unittest.main()
