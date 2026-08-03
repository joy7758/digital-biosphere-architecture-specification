from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def load_json(relative: str):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


class CommercialPrivateConstitutionTests(unittest.TestCase):
    def test_current_constitution_and_decision_are_present(self):
        constitution = (ROOT / "architecture/commercial-private-infrastructure-strategy-constitution.md").read_text(encoding="utf-8")
        decision = (ROOT / "architecture/ADR-042-commercial-private-infrastructure-direction.md").read_text(encoding="utf-8")
        self.assertIn("COMMERCIAL_PRIVATE_INFRASTRUCTURE_FIRST=true", constitution)
        self.assertIn("PRIVATE_CORE_IS_CANONICAL=true", constitution)
        self.assertIn("PUBLIC_SURFACE_NE_OPEN_SOURCE_CORE=true", constitution)
        self.assertIn("Status: `ACCEPTED`", decision)

    def test_agent_entry_uses_current_commercial_identity(self):
        index = load_json("agent-index.json")
        self.assertEqual("3.0.0", index["format_version"])
        self.assertEqual("TITMAS Commercial Agent Infrastructure", index["canonical_program_name"])
        self.assertEqual("COMMERCIAL_PRIVATE_AGENT_INFRASTRUCTURE", index["product_category"])
        self.assertNotIn("canonical_community_name", index)
        self.assertEqual("NONE", index["historical_community_identity"]["current_authority_effect"])

    def test_public_surface_does_not_imply_open_core_or_community(self):
        constitution = (ROOT / "architecture/commercial-private-infrastructure-strategy-constitution.md").read_text(encoding="utf-8")
        for invariant in (
            "PUBLIC_SURFACE_NE_OPEN_SOURCE_CORE=true",
            "PUBLIC_SDK_NE_PUBLIC_COMMUNITY=true",
            "PUBLIC_CONTRIBUTION_ROUTE_ACTIVE=false",
            "COMMUNITY_ESTABLISHED=false",
        ):
            self.assertIn(invariant, constitution)

    def test_historical_community_record_is_fail_closed(self):
        status = load_json("TITMAS/community/community-status.json")
        self.assertTrue(status["historical_record"])
        self.assertFalse(status["current_route_active"])
        self.assertEqual("NONE", status["current_authority_effect"])
        self.assertFalse(status["public_contribution_surface"]["active"])
        self.assertFalse(status["public_contribution_surface"]["authorized"])
        self.assertFalse(status["community_established"])

    def test_historical_open_constitution_has_no_current_authority(self):
        historical = (ROOT / "architecture/open-infrastructure-strategy-constitution.md").read_text(encoding="utf-8")
        self.assertIn("Status: `SUPERSEDED_HISTORICAL_STRATEGY`", historical)
        self.assertIn("Current authority effect: `NONE`", historical)
        self.assertIn("ADR-042", historical)

    def test_strategy_change_creates_no_operational_authority(self):
        decision = (ROOT / "architecture/ADR-042-commercial-private-infrastructure-direction.md").read_text(encoding="utf-8")
        for boundary in (
            "IMPLEMENTATION_AUTHORIZED=false",
            "RELEASE_AUTHORIZED=false",
            "DEPLOYMENT_AUTHORIZED=false",
            "COMMERCIAL_OFFER_AUTHORIZED=false",
            "CORE_SOURCE_PUBLICATION_AUTHORIZED=false",
            "PUBLIC_CONTRIBUTION_AUTHORIZED=false",
        ):
            self.assertIn(boundary, decision)


if __name__ == "__main__":
    unittest.main()
