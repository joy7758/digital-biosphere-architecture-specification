import importlib.util
import json
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path

EVOLUTION_PATH = (
    Path(__file__).resolve().parents[1] / "evolution" / "evolution.py"
)
SPEC = importlib.util.spec_from_file_location("titmas_evolution", EVOLUTION_PATH)
assert SPEC and SPEC.loader
EVOLUTION = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(EVOLUTION)


class EvolutionD19Tests(unittest.TestCase):
    def setUp(self):
        self.bundle = EVOLUTION.run_demo()

    def test_ev_t01_problem_evidence_schema(self):
        EVOLUTION.validate_object("problem_evidence", self.bundle["problem_evidence"])
        broken = deepcopy(self.bundle["problem_evidence"])
        del broken["evidence_references"]
        with self.assertRaisesRegex(EVOLUTION.EvolutionRejected, "SCHEMA_INVALID"):
            EVOLUTION.validate_object("problem_evidence", broken)

    def test_ev_t02_canonical_owner_resolution(self):
        route = EVOLUTION.resolve_owner("STALE_TASK_REGISTRY")
        self.assertEqual(
            "joy7758/digital-biosphere-architecture-specification",
            route["canonical_owner_repository"],
        )
        with self.assertRaisesRegex(EVOLUTION.EvolutionRejected, "OWNER_UNRESOLVED"):
            EVOLUTION.resolve_owner("UNKNOWN_PROBLEM")

    def test_ev_t03_duplicate_semantic_object_rejected(self):
        item = self.bundle["variants"][0]
        with self.assertRaisesRegex(EVOLUTION.EvolutionRejected, "DUPLICATE"):
            EVOLUTION.assert_unique_semantic_objects([item, item], "variant_id")

    def test_ev_t04_maximum_three_variants(self):
        limits = EVOLUTION.load_json(EVOLUTION.LIMITS_PATH)
        self.assertLessEqual(len(self.bundle["variants"]), limits["max_patch_variants_per_problem"])
        self.assertEqual(3, len(self.bundle["variants"]))

    def test_ev_t05_no_change_baseline_required(self):
        variants = [
            item for item in self.bundle["variants"]
            if item["variant_kind"] != "NO_CHANGE_BASELINE"
        ]
        evaluations = [
            item for item in self.bundle["fitness_evaluations"]
            if not item["variant_id"].endswith("-V0")
        ]
        with self.assertRaisesRegex(EVOLUTION.EvolutionRejected, "REQUIRED_VARIANT"):
            EVOLUTION.select_variant("D19-ER1-DEMO-001", variants, evaluations)

    def test_ev_t06_risk_class_assignment(self):
        self.assertEqual(
            "ER-1",
            EVOLUTION.classify_risk(deterministic_derived_repair=True),
        )
        self.assertEqual("ER-3", EVOLUTION.classify_risk(semantic_change=True))
        self.assertEqual(
            "ER-4",
            EVOLUTION.classify_risk(irreversible_external_effect=True),
        )

    def test_ev_t07_er3_cannot_auto_merge(self):
        model = EVOLUTION.load_json(EVOLUTION.ROOT / "risk-classification.json")
        er3 = next(item for item in model["classes"] if item["id"] == "ER-3")
        self.assertFalse(er3["autonomous_merge"])
        self.assertTrue(er3["human_authorization_required"])

    def test_ev_t08_er4_cannot_auto_activate(self):
        model = EVOLUTION.load_json(EVOLUTION.ROOT / "risk-classification.json")
        er4 = next(item for item in model["classes"] if item["id"] == "ER-4")
        self.assertFalse(er4["automatic_activation"])
        self.assertTrue(er4["independent_agent_review_required"])

    def test_ev_t09_constitutional_invariant_immutable(self):
        with self.assertRaisesRegex(EVOLUTION.EvolutionRejected, "IMMUTABLE"):
            EVOLUTION.assert_constitution_preserved(["FAIL_CLOSED"])

    def test_ev_t10_no_self_granted_credential(self):
        capability = EVOLUTION.load_json(EVOLUTION.ROOT / "evolution-capability.json")
        self.assertIn("DISCOVERY_LAYER_NE_AUTHORITY", capability["authority_boundaries"])
        policy = EVOLUTION.load_json(EVOLUTION.POLICY_PATH)
        self.assertIn("NO_SELF_GRANTED_CREDENTIAL", policy["constitutional_invariants"])

    def test_ev_t11_no_self_granted_authority(self):
        policy = EVOLUTION.load_json(EVOLUTION.POLICY_PATH)
        self.assertIn("NO_SELF_GRANTED_AUTHORITY", policy["constitutional_invariants"])
        self.assertFalse(
            self.bundle["authorization_reference"]["production_activation_authorized"]
        )

    def test_ev_t12_raw_secret_disclosure_rejected(self):
        with self.assertRaisesRegex(EVOLUTION.EvolutionRejected, "RAW_SECRET"):
            EVOLUTION.assert_no_secret_disclosure(
                {"header": "Authorization: Bearer abcdefghijklmnopqrstuvwxyz"}
            )

    def test_ev_t13_fitness_is_multi_objective(self):
        profile = EVOLUTION.load_json(EVOLUTION.FITNESS_PATH)
        self.assertTrue(profile["multi_objective"])
        self.assertGreaterEqual(len(profile["dimensions"]), 10)
        self.assertFalse(profile["opaque_universal_score"])

    def test_ev_t14_safety_threshold_cannot_be_offset(self):
        failed = deepcopy(self.bundle["fitness_evaluations"][0])
        failed["security_results"] = "FAIL"
        failed["confidence"] = 1.0
        self.assertFalse(EVOLUTION.hard_gates_pass(failed))
        profile = EVOLUTION.load_json(EVOLUTION.FITNESS_PATH)
        self.assertFalse(profile["hard_gate_compensation_allowed"])

    def test_ev_t15_mutation_retry_bounded(self):
        limits = EVOLUTION.load_json(EVOLUTION.LIMITS_PATH)
        self.assertEqual(2, limits["max_discovery_retries"])
        self.assertEqual(2, limits["max_reproduction_attempts"])
        self.assertEqual(1, limits["max_variant_generation_rounds"])
        self.assertEqual("BLOCKED_LIMIT_REACHED", limits["limit_reached_status"])

    def test_ev_t16_sandbox_required(self):
        self.assertTrue(
            EVOLUTION.state_transition_allowed("VARIANTS_GENERATED", "SANDBOXED")
        )
        self.assertFalse(
            EVOLUTION.state_transition_allowed("VARIANTS_GENERATED", "EVALUATED")
        )

    def test_ev_t17_rollback_reference_required(self):
        for variant in self.bundle["variants"]:
            self.assertTrue(variant["rollback_reference"])
        broken = deepcopy(self.bundle["variants"][0])
        del broken["rollback_reference"]
        with self.assertRaisesRegex(EVOLUTION.EvolutionRejected, "SCHEMA_INVALID"):
            EVOLUTION.validate_object("patch_variant", broken)

    def test_ev_t18_failed_mutation_retained(self):
        rollback = self.bundle["rollback_evidence"]
        self.assertTrue(rollback["failed_mutation_retained"])
        EVOLUTION.validate_object("rollback_evidence", rollback)

    def test_ev_t19_lineage_parent_child_binding(self):
        lineage = self.bundle["lineage"]
        self.assertNotEqual(lineage["parent_revision"], lineage["child_revision"])
        self.assertEqual(
            self.bundle["selection_record"]["selected_variant"],
            lineage["selected_variant"],
        )
        EVOLUTION.validate_object("evolution_lineage", lineage)

    def test_ev_t20_independent_review_required(self):
        capability = EVOLUTION.load_json(EVOLUTION.ROOT / "evolution-capability.json")
        roles = set(capability["roles"])
        self.assertIn("VARIANT_BUILDER_AGENT", roles)
        self.assertIn("FITNESS_EVALUATOR_AGENT", roles)
        self.assertFalse(
            capability["role_separation"]["variant_builder_is_sole_evaluator"]
        )

    def test_ev_t21_p0_10_cannot_auto_reopen(self):
        p0 = EVOLUTION.load_json(EVOLUTION.POLICY_PATH)["p0_10"]
        self.assertFalse(p0["automatic_reopen"])
        self.assertEqual(
            "NOT_ASSESSED_DIAGNOSTIC_LIMIT_REACHED",
            p0["final_disposition"],
        )

    def test_ev_t22_community_evidence_intake_valid(self):
        registry = EVOLUTION.load_json(
            EVOLUTION.DBA_ROOT / "TITMAS" / "agent-native" / "tasks" / "task-registry.json"
        )
        evolution_tasks = [
            item for item in registry["tasks"]
            if item["task_id"].startswith("AN-EV-")
        ]
        self.assertEqual(8, len(evolution_tasks))
        for task in evolution_tasks:
            self.assertIn("canonical_owner", task)
            self.assertIn("auto_repair_eligibility", task)
            self.assertIn("fitness_dimensions", task)

    def test_ev_t23_fixture_self_healing_end_to_end(self):
        self.assertEqual(
            "CURRENT",
            self.bundle["repaired_registry"]["status"],
        )
        self.assertTrue(
            self.bundle["outcome_evidence"]["deterministic_source_match"]
        )
        self.assertEqual(
            "D19-ER1-DEMO-001-V1",
            self.bundle["selection_record"]["selected_variant"],
        )

    def test_ev_t24_deterministic_replay(self):
        first = EVOLUTION.digest(EVOLUTION.run_demo())
        second = EVOLUTION.digest(EVOLUTION.run_demo())
        self.assertEqual(first, second)
        with tempfile.TemporaryDirectory(dir=Path("/tmp").resolve()) as directory:
            output = Path(directory) / "run"
            EVOLUTION.write_demo_run(output)
            first_files = {
                path.relative_to(output): path.read_bytes()
                for path in output.rglob("*.json")
            }
            EVOLUTION.write_demo_run(output)
            second_files = {
                path.relative_to(output): path.read_bytes()
                for path in output.rglob("*.json")
            }
            self.assertEqual(first_files, second_files)

    def test_ev_t25_no_production_side_effect(self):
        outcome = self.bundle["outcome_evidence"]
        self.assertFalse(outcome["real_runtime_changed"])
        self.assertFalse(outcome["production_deployment"])
        self.assertFalse(outcome["database_changed"])
        self.assertFalse(outcome["credential_created"])
        self.assertFalse(outcome["p0_10_reopened"])


if __name__ == "__main__":
    unittest.main()
