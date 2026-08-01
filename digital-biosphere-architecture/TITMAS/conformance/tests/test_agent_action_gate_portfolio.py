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

    def test_public_m1_source_is_exactly_pinned(self) -> None:
        self.assertEqual(
            self.projection["canonical_remote_repository"],
            "https://github.com/joy7758/titmas-agent-action-gate",
        )
        self.assertEqual(self.projection["observed_branch"], "main")
        self.assertEqual(
            self.projection["observed_commit"],
            "626388124dd97853f2e6c08429dd6024ff0b981c",
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
        self.assertFalse(self.projection["implementation_started"])
        self.assertFalse(self.projection["competition_submission"])

    def test_gates_preserve_unimplemented_and_unassessed_states(self) -> None:
        gates = self.projection["gates"]
        self.assertEqual(gates["G0"], "REVIEW_REQUIRED_READY_FOR_HUMAN_DECISION")
        self.assertEqual(gates["G1"], "PASS_PUBLIC_M1_SOURCE_PINNED")
        self.assertEqual(gates["G3"], "NOT_STARTED")
        self.assertEqual(gates["G4"], "NOT_ASSESSED_CONTRACT_FIXTURES_ONLY")
        self.assertEqual(gates["G5"], "NOT_AUTHORIZED")
        self.assertEqual(gates["G6"], "NOT_EXECUTED")
        self.assertEqual(gates["G8"], "NOT_RELEASED_NOT_ADOPTED")

    def test_proposal_is_review_ready_but_not_admitted(self) -> None:
        self.assertIn("status: READY_FOR_REVIEW", self.proposal)
        self.assertIn("PORTFOLIO_ADMISSION_GRANTED=false", self.proposal)
        self.assertIn("ACTION_GATE_RUNTIME_CREATED=false", self.proposal)
        self.assertIn("COMPETITION_SUBMITTED=false", self.proposal)


if __name__ == "__main__":
    unittest.main()
