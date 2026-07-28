import copy
import importlib.util
import json
import unittest
from pathlib import Path

HARNESS_PATH = Path(__file__).resolve().parents[1] / "harness.py"
SPEC = importlib.util.spec_from_file_location("titmas_harness", HARNESS_PATH)
assert SPEC and SPEC.loader
HARNESS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(HARNESS)


class HarnessTests(unittest.TestCase):
    def test_full_harness_passes(self):
        report = HARNESS.run_all(write_report=False)
        self.assertEqual("PASS", report["status"], report)

    def test_all_required_negative_cases_are_rejected(self):
        path = HARNESS.TITMAS_ROOT / "conformance" / "fixtures" / "negative" / "semantic-elevation-cases.json"
        cases = json.loads(path.read_text(encoding="utf-8"))["cases"]
        self.assertEqual(8, len(cases))
        for case in cases:
            self.assertIn(case["expected_error"], HARNESS.semantic_errors(case["payload"]))

    def test_community_status_schema_fails_closed(self):
        status_path = HARNESS.TITMAS_ROOT / "community" / "community-status.json"
        status = json.loads(status_path.read_text(encoding="utf-8"))
        unsafe = copy.deepcopy(status)
        unsafe["public_launch_authorized"] = True
        self.assertTrue(unsafe["public_launch_authorized"])
        self.assertFalse(status["public_launch_authorized"])

    def test_schema_depth_fails_closed(self):
        schema = {"type": "object", "properties": {}}
        instance = {}
        cursor_schema = schema
        cursor_instance = instance
        for index in range(HARNESS.MAX_SCHEMA_DEPTH + 2):
            cursor_schema["properties"] = {"nested": {"type": "object", "properties": {}}}
            cursor_schema = cursor_schema["properties"]["nested"]
            cursor_instance["nested"] = {}
            cursor_instance = cursor_instance["nested"]
        with self.assertRaises(HARNESS.ConformanceError):
            HARNESS.validate_schema(instance, schema)

    def test_json_path_escape_fails_closed(self):
        with self.assertRaises(HARNESS.ConformanceError):
            HARNESS.load_json(Path("/tmp/not-a-titmas-input.json"))

    def test_number_schema_rejects_boolean(self):
        with self.assertRaises(HARNESS.ConformanceError):
            HARNESS.validate_schema(True, {"type": "number"})

    def test_number_schema_enforces_minimum(self):
        with self.assertRaises(HARNESS.ConformanceError):
            HARNESS.validate_schema(-1, {"type": "integer", "minimum": 0})

    def test_agent_native_surfaces_pass(self):
        details = HARNESS.check_agent_native_surfaces()
        self.assertEqual(12, details["agent_tasks_checked"])
        self.assertEqual(1, details["canonical_machine_entries"])

    def test_bilingual_brand_identity_passes(self):
        details = HARNESS.check_bilingual_brand_identity()
        self.assertEqual(1, details["canonical_machine_entries"])
        self.assertEqual(1, details["brand_identity_projections"])
        self.assertEqual(2, details["positive_cases_passed"])
        self.assertEqual(5, details["negative_cases_rejected"])

    def test_bilingual_brand_identity_fails_closed(self):
        path = (
            HARNESS.TITMAS_ROOT / "conformance" / "fixtures" / "brand"
            / "titmas-xiarizhihai-brand-cases.json"
        )
        cases = json.loads(path.read_text(encoding="utf-8"))["negative_cases"]
        self.assertEqual(5, len(cases))
        for case in cases:
            self.assertIn(
                case["expected_error"],
                HARNESS.brand_identity_errors(case["payload"]),
            )

    def test_agent_native_adversarial_coverage(self):
        details = HARNESS.check_agent_native_adversarial()
        self.assertEqual(22, details["adversarial_cases_rejected"])
        self.assertEqual(22, details["adversarial_cases_executed"])

    def test_agent_native_value_gate_preserves_negative_result(self):
        details = HARNESS.check_agent_native_value_gate()
        self.assertEqual(6, details["frozen_counts_checked"])

    def test_agent_native_value_validation_framework_passes(self):
        details = HARNESS.check_agent_native_value_validation_framework()
        self.assertEqual(10, details["ecology_box_tasks_checked"])
        self.assertEqual(9, details["security_cases_rejected"])
        self.assertEqual(0, details["independent_lineage_count"])

    def test_value_validation_security_cases_fail_closed(self):
        path = (
            HARNESS.TITMAS_ROOT / "agent-native" / "value-validation"
            / "security-negative-cases.v0.1.json"
        )
        cases = json.loads(path.read_text(encoding="utf-8"))["cases"]
        self.assertEqual(9, len(cases))
        for case in cases:
            self.assertEqual(
                {
                    "decision": "REJECT",
                    "reason_code": case["reason_code"],
                },
                HARNESS.value_validation_rejection(case["attack"]),
            )

    def test_value_validation_lineage_inflation_fails_closed(self):
        path = (
            HARNESS.TITMAS_ROOT / "agent-native" / "value-validation"
            / "not-executed-record.v0.1.json"
        )
        record = json.loads(path.read_text(encoding="utf-8"))
        inflated = copy.deepcopy(record)
        inflated["lineage"]["independent_lineage_count"] = 2
        with self.assertRaises(HARNESS.ConformanceError):
            HARNESS.validate_value_lineage(inflated["lineage"])
        self.assertEqual(0, record["lineage"]["independent_lineage_count"])

    def test_ecology_box_001_package_passes_without_execution(self):
        details = HARNESS.check_agent_native_ecology_box_001_package()
        self.assertEqual(8, details["role_definitions_checked"])
        self.assertEqual(10, details["task_contracts_checked"])
        self.assertEqual(10, details["failure_scenarios_checked"])
        self.assertEqual(9, details["security_cases_rejected"])
        self.assertEqual(0, details["participant_instances"])
        self.assertFalse(details["experiment_executed"])

    def test_ecology_box_001_security_cases_fail_closed(self):
        self.assertEqual(9, len(HARNESS.ECOLOGY_BOX_001_REJECTIONS))
        for attack, reason_code in HARNESS.ECOLOGY_BOX_001_REJECTIONS.items():
            self.assertEqual(
                {"decision": "REJECT", "reason_code": reason_code},
                HARNESS.ecology_box_001_rejection(attack),
            )

    def test_ecology_box_001_unknown_security_case_is_not_assessed(self):
        self.assertEqual(
            {"decision": "NOT_ASSESSED", "reason_code": "UNKNOWN_CASE"},
            HARNESS.ecology_box_001_rejection("UNFROZEN_CASE"),
        )

    def test_ecology_box_001_manifest_tamper_is_detectable(self):
        root = HARNESS.TITMAS_ROOT / "agent-native" / "ecology-box-001"
        manifest = json.loads((root / "freeze-manifest.yaml").read_text(encoding="utf-8"))
        task_hash = f"sha256:{HARNESS.sha256_file(root / 'tasks' / 'task-registry.yaml')}"
        self.assertEqual(task_hash, manifest["task_set_hash"])
        tampered = copy.deepcopy(manifest)
        tampered["task_set_hash"] = "sha256:" + ("0" * 64)
        self.assertNotEqual(task_hash, tampered["task_set_hash"])

    def test_ecology_box_001_contains_no_run_record(self):
        run_root = (
            HARNESS.TITMAS_ROOT / "agent-native" / "ecology-box-001" / "runs"
        )
        records = [
            path for path in run_root.iterdir()
            if path.is_file() and path.name != "README.md"
        ]
        self.assertEqual([], records)

    def test_ecology_box_001_preregistration_passes_without_execution(self):
        details = HARNESS.check_agent_native_ecology_box_001_preregistration()
        self.assertEqual("REQUIRES_CORRECTION", details["fairness_review_status"])
        self.assertEqual(5, details["transition_cases_rejected"])
        self.assertEqual(10, details["human_decisions_undecided"])
        self.assertFalse(details["execution_authorized"])
        self.assertFalse(details["experiment_executed"])
        self.assertFalse(details["value_proven"])

    def test_ecology_box_001_ready_cannot_auto_become_executed(self):
        self.assertEqual(
            {"decision": "REJECT", "reason_code": "READY_NE_EXECUTED"},
            HARNESS.ecology_box_001_preregistration_rejection(
                "READY_TO_EXECUTED"
            ),
        )

    def test_ecology_box_001_result_cannot_auto_become_value_proven(self):
        self.assertEqual(
            {"decision": "REJECT", "reason_code": "RESULT_NE_VALUE_PROVEN"},
            HARNESS.ecology_box_001_preregistration_rejection(
                "RESULT_TO_VALUE_PROVEN"
            ),
        )

    def test_ecology_box_001_agent_activity_cannot_prove_community_value(self):
        self.assertEqual(
            {
                "decision": "REJECT",
                "reason_code": "AGENT_ACTIVITY_NE_COMMUNITY_VALUE",
            },
            HARNESS.ecology_box_001_preregistration_rejection(
                "ACTIVITY_TO_COMMUNITY_VALUE"
            ),
        )

    def test_ecology_box_001_sessions_cannot_be_lineages(self):
        root = HARNESS.TITMAS_ROOT / "agent-native" / "ecology-box-001"
        lineage = json.loads((root / "agent-lineage-plan.yaml").read_text())
        self.assertEqual(
            1,
            lineage["counting_rules"][
                "single_model_multiple_sessions_multiple_roles"
            ]["independent_lineage_count"],
        )
        inflated = copy.deepcopy(lineage)
        inflated["current_counts"]["MODEL_COUNT"] = 1
        inflated["current_counts"]["SESSION_COUNT"] = 8
        inflated["current_counts"]["ROLE_COUNT"] = 8
        inflated["current_counts"]["INDEPENDENT_LINEAGE_COUNT"] = 8
        with self.assertRaises(HARNESS.ConformanceError):
            HARNESS.validate_ecology_box_001_preregistration_lineage(inflated)
        self.assertEqual(
            {
                "decision": "REJECT",
                "reason_code": "SESSION_COUNT_NE_INDEPENDENT_LINEAGE_COUNT",
            },
            HARNESS.ecology_box_001_preregistration_rejection(
                "SESSION_TO_LINEAGE"
            ),
        )

    def test_ecology_box_001_pilot_pass_cannot_prove_commercial_value(self):
        self.assertEqual(
            {
                "decision": "REJECT",
                "reason_code": "PILOT_PASS_NE_COMMERCIAL_VALUE",
            },
            HARNESS.ecology_box_001_preregistration_rejection(
                "PILOT_PASS_TO_COMMERCIAL_VALUE"
            ),
        )

    def test_ecology_box_001_unknown_transition_is_not_assessed(self):
        self.assertEqual(
            {"decision": "NOT_ASSESSED", "reason_code": "UNKNOWN_CASE"},
            HARNESS.ecology_box_001_preregistration_rejection(
                "UNFROZEN_TRANSITION"
            ),
        )

    def test_agent_native_reviews_preserve_real_independence(self):
        details = HARNESS.check_agent_native_reviews()
        self.assertEqual(14, details["review_sessions_checked"])
        self.assertEqual(1, details["independent_model_lineages"])


if __name__ == "__main__":
    unittest.main()
