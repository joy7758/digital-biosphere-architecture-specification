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

    def test_agent_native_surfaces_pass(self):
        details = HARNESS.check_agent_native_surfaces()
        self.assertEqual(12, details["agent_tasks_checked"])
        self.assertEqual(1, details["canonical_machine_entries"])

    def test_agent_native_adversarial_coverage(self):
        details = HARNESS.check_agent_native_adversarial()
        self.assertEqual(22, details["adversarial_cases_rejected"])
        self.assertEqual(22, details["adversarial_cases_executed"])

    def test_agent_native_value_gate_preserves_negative_result(self):
        details = HARNESS.check_agent_native_value_gate()
        self.assertEqual(6, details["frozen_counts_checked"])

    def test_agent_native_reviews_preserve_real_independence(self):
        details = HARNESS.check_agent_native_reviews()
        self.assertEqual(14, details["review_sessions_checked"])
        self.assertEqual(1, details["independent_model_lineages"])


if __name__ == "__main__":
    unittest.main()
