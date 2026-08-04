from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
GATEWAY_REVISION = "e200ea0f00d9d948c3b6dbf7058e08489dea1ccd"


def load(relative: str):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


class D29CurrentImplementationProjectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.projection = load("commercial/discovery/d29-reference-implementation.json")
        cls.status = load("commercial/discovery/status.json")
        cls.offerings = load("commercial/discovery/commercial-offerings.json")
        cls.limitations = load("commercial/discovery/known-limitations.json")
        cls.repositories = load("commercial/discovery/canonical-repositories.json")
        cls.program = load("commercial-program-state.json")
        cls.readiness = load("commercial-readiness.json")
        cls.agent_index = load("agent-index.json")

    def test_source_is_exact_canonical_gateway_main(self):
        source = self.projection["source"]
        self.assertEqual("joy7758/titmas-sandbox-gateway", source["repository"])
        self.assertEqual("main", source["branch"])
        self.assertEqual(GATEWAY_REVISION, source["revision"])
        self.assertEqual("MERGED_ON_CANONICAL_MAIN", source["source_status"])
        self.assertEqual(GATEWAY_REVISION, self.repositories["commercial_platform"]["observed_main_head"])
        self.assertEqual(GATEWAY_REVISION, self.program["source_commits"]["data_plane"])

    def test_reference_capabilities_do_not_become_offerings(self):
        self.assertTrue(self.status["observer_runtime_implemented"])
        self.assertTrue(self.status["console_implemented"])
        self.assertTrue(self.status["synthetic_first_value_implemented"])
        self.assertTrue(self.status["software_delivery_proof_implemented"])
        for key in (
            "observer_runtime_status",
            "console_status",
            "synthetic_first_value_status",
        ):
            self.assertEqual("IMPLEMENTED_REFERENCE_NOT_DEPLOYED", self.status[key])
        self.assertEqual(0, self.status["available_offering_count"])
        self.assertFalse(self.status["currently_achieved"])
        self.assertFalse(self.status["deployment_executed"])
        self.assertFalse(self.status["paid_monitor_pilot_available"])
        self.assertFalse(self.status["customer_specific_enforce_authorized"])
        self.assertFalse(self.status["public_launch_authorized"])
        self.assertFalse(self.status["commercial_customer_created"])
        self.assertEqual(0, self.offerings["available_offering_count"])
        self.assertTrue(all(not item.get("currently_available_offering", False) for item in self.offerings["offerings"]))

    def test_durable_read_projections_retain_bounded_audit_boundary(self):
        capabilities = self.projection["capabilities"]
        boundaries = self.projection["retained_fail_closed_boundaries"]
        self.assertEqual(
            "IMPLEMENTED_REFERENCE_NOT_DEPLOYED",
            capabilities["durable_receipt_read_projection"],
        )
        self.assertEqual(
            "PASS_SOURCE_AND_EPHEMERAL_POSTGRES_CI_COMPLETE_DECLARED_WORKSPACE_SCOPE_NOT_DEPLOYED",
            capabilities["durable_audit_export_projection"],
        )
        self.assertEqual(
            "IMPLEMENTED_REFERENCE_AUDIT_COMPLETE_FOR_DECLARED_WORKSPACE_SCOPE_NOT_DEPLOYED",
            capabilities["durable_health_projection"],
        )
        self.assertTrue(
            boundaries[
                "postgres_audit_projection_chain_complete_for_declared_workspace_scope"
            ]
        )
        self.assertEqual(
            "COMMERCIAL_TENANT_WORKSPACE_EXPORT_V1",
            boundaries["postgres_audit_projection_profile"],
        )
        self.assertFalse(boundaries["canonical_tenant_event_content_complete"])
        self.assertFalse(
            boundaries["offline_scope_non_membership_cryptographic_proof"]
        )
        self.assertFalse(boundaries["external_cryptographic_anchor"])
        self.assertFalse(self.projection["availability"]["deployed"])

    def test_security_engineering_gate_fails_closed_with_exact_counts(self):
        gate = self.projection["security_engineering_gate"]
        self.assertEqual("FAIL_CLOSED", gate["status"])
        self.assertEqual(20, gate["control_count"])
        self.assertEqual(16, gate["pass"])
        self.assertEqual(1, gate["partial"])
        self.assertEqual(1, gate["fail_retained"])
        self.assertEqual(1, gate["not_assessed"])
        self.assertEqual(1, gate["not_applicable"])
        self.assertEqual(1, gate["blocker_findings_open"])
        self.assertEqual(2, gate["high_findings_open"])
        self.assertEqual("NOT_RECOMMENDED", gate["agent_recommendation"])
        self.assertFalse(gate["independent_security_evaluation_executed"])
        self.assertFalse(gate["d04_reopened"])
        self.assertEqual("NONE", gate["commercial_effect"])
        self.assertEqual(
            "FAIL_CLOSED_ONE_BLOCKER_TWO_HIGH",
            self.status["security_engineering_gate"],
        )

    def test_workspace_data_lifecycle_is_source_only_and_not_deployed(self):
        capabilities = self.projection["capabilities"]
        for key in ("workspace_deletion_lifecycle", "workspace_retention_lifecycle"):
            self.assertEqual(
                "PASS_SOURCE_AND_EPHEMERAL_POSTGRES_CI_NOT_DEPLOYED",
                capabilities[key],
            )
            self.assertEqual(capabilities[key], self.status[key])
        self.assertFalse(self.projection["availability"]["deployed"])
        self.assertFalse(self.status["deployment_executed"])

    def test_security_drill_is_prepared_but_not_authorized_or_executed(self):
        drill = self.projection["security_drill_readiness"]
        self.assertEqual(
            "PASS_PREPARATION_ONLY_EXECUTION_NOT_AUTHORIZED", drill["status"]
        )
        self.assertFalse(drill["incident_drill_executed"])
        self.assertFalse(drill["formal_rollback_drill_executed"])
        self.assertFalse(drill["incident_drill_authorized"])
        self.assertFalse(drill["rollback_drill_authorized"])
        self.assertEqual(0, drill["security_findings_closed"])
        self.assertEqual("NONE", drill["commercial_effect"])
        self.assertEqual(
            "PASS_PREPARATION_ONLY_EXECUTION_NOT_AUTHORIZED",
            self.status["security_drill_readiness"],
        )
        self.assertFalse(self.status["incident_drill_executed"])
        self.assertFalse(self.status["formal_rollback_drill_executed"])

    def test_synthetic_measurements_retain_scope_and_non_claims(self):
        measured = self.projection["measured_synthetic_reference"]
        self.assertEqual(0, measured["customer_data_count"])
        self.assertEqual(0, measured["real_external_action_count"])
        self.assertEqual(0, measured["production_permission_count"])
        self.assertEqual("PASS", measured["first_value"]["receipt_verification"])
        self.assertEqual(
            "SYNTHETIC_ZERO_DATA_BENCHMARK_NOT_PRODUCTION_PERFORMANCE",
            measured["measurement_classification"],
        )
        self.assertFalse(measured["latency_is_slo"])
        self.assertFalse(measured["result_is_customer_evidence"])
        self.assertEqual(
            "NON_BINDING_SYNTHETIC_PROOF_ONLY_NO_CUSTOMER_AUTHORIZATION_OR_RELEASE_ACTION",
            measured["software_delivery_proof_disclaimer"],
        )
        self.assertFalse(measured["software_delivery_proof"]["release_or_merge_executed"])
        self.assertEqual(0, measured["software_delivery_proof"]["external_network_call_count"])

    def test_fail_closed_commercial_boundaries_are_retained(self):
        availability = self.projection["availability"]
        boundaries = self.projection["retained_fail_closed_boundaries"]
        self.assertFalse(availability["deployed"])
        self.assertFalse(availability["commercial_offering_available"])
        self.assertFalse(availability["paid_monitor_pilot_available"])
        self.assertFalse(availability["customer_specific_enforce_authorized"])
        self.assertEqual(0, availability["customer_count"])
        self.assertFalse(availability["production_ready"])
        self.assertEqual("CLOSED_FAILED_RETAINED", boundaries["d04_status"])
        self.assertFalse(boundaries["p0_10_agent_first_acceptance"])
        self.assertFalse(boundaries["receipt_pass_is_truth"])
        self.assertFalse(boundaries["verification_is_authorization"])
        self.assertFalse(boundaries["gate_decision_is_execution"])
        self.assertFalse(boundaries["synthetic_authorization_is_customer_authorization"])
        self.assertFalse(self.readiness["commercial_technical_ready"])
        self.assertFalse(self.readiness["paid_beta_ready"])
        self.assertFalse(self.readiness["production_ready"])

    def test_agent_entry_exposes_one_projection_without_copying_child_truth(self):
        surface = self.agent_index["machine_surfaces"]["commercial_d29_reference_implementation"]
        self.assertEqual("commercial/discovery/d29-reference-implementation.json", surface)
        self.assertTrue((ROOT / surface).is_file())
        current = self.agent_index["commercialization_boundary"]["d29_customer_entry_reference"]
        self.assertEqual(GATEWAY_REVISION, current["source_revision"])
        self.assertFalse(current["commercial_offering_available"])
        self.assertFalse(current["production_ready"])
        self.assertEqual(
            "READ_ONLY_DBA_SOURCE_PIN_NO_CHILD_STATUS_WRITE",
            self.projection["projection_effect"],
        )

    def test_current_limitations_replace_stale_missing_claims(self):
        limitations = set(self.limitations["limitations"])
        self.assertIn("D29_REFERENCE_IMPLEMENTATION_NOT_DEPLOYED", limitations)
        self.assertIn("OBSERVER_FIRST_VALUE_SYNTHETIC_ONLY", limitations)
        self.assertIn("CONSOLE_REFERENCE_NOT_DEPLOYED", limitations)
        self.assertIn("PAID_MONITOR_PILOT_NOT_AVAILABLE", limitations)
        self.assertNotIn("OBSERVER_RUNTIME_NOT_IMPLEMENTED", limitations)
        self.assertNotIn("CONSOLE_NOT_IMPLEMENTED", limitations)


if __name__ == "__main__":
    unittest.main()
