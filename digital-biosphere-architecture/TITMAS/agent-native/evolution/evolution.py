#!/usr/bin/env python3
"""Dependency-free bounded evolution reference for TITMAS D19.

The module operates on synthetic files only. It never opens a network
connection, creates a credential, changes Git state or activates a Runtime.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import tempfile
from copy import deepcopy
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
DBA_ROOT = ROOT.parents[2]
SCHEMA_ROOT = ROOT / "schemas"
FIXTURE_ROOT = ROOT / "demo" / "fixtures"
POLICY_PATH = ROOT / "evolution-policy.json"
FITNESS_PATH = ROOT / "fitness-profile.json"
OWNER_MAP_PATH = ROOT / "canonical-owner-map.json"
LIMITS_PATH = ROOT / "mutation-limits.json"

SCHEMA_FILES = {
    "problem_evidence": "problem-evidence.schema.json",
    "evolution_proposal": "evolution-proposal.schema.json",
    "patch_variant": "patch-variant.schema.json",
    "fitness_evaluation": "fitness-evaluation.schema.json",
    "selection_record": "selection-record.schema.json",
    "evolution_lineage": "evolution-lineage.schema.json",
    "rollback_evidence": "rollback-evidence.schema.json",
}


class EvolutionRejected(ValueError):
    """A fail-closed D19 policy rejection."""


def load_json(path: Path) -> Any:
    resolved = path.resolve()
    if not resolved.is_relative_to(DBA_ROOT.resolve()):
        raise EvolutionRejected("PATH_OUTSIDE_DBA_ROOT")
    if path.is_symlink() or not path.is_file():
        raise EvolutionRejected("EXPECTED_REGULAR_FILE")
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def digest(value: Any) -> str:
    return "sha256:" + hashlib.sha256(canonical_bytes(value)).hexdigest()


def _conformance_module() -> Any:
    path = DBA_ROOT / "TITMAS" / "conformance" / "harness.py"
    spec = importlib.util.spec_from_file_location("titmas_conformance_harness", path)
    if spec is None or spec.loader is None:
        raise EvolutionRejected("CONFORMANCE_VALIDATOR_UNAVAILABLE")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_object(kind: str, value: dict[str, Any]) -> None:
    if kind not in SCHEMA_FILES:
        raise EvolutionRejected("UNKNOWN_EVOLUTION_OBJECT")
    schema = load_json(SCHEMA_ROOT / SCHEMA_FILES[kind])
    try:
        _conformance_module().validate_schema(value, schema)
    except ValueError as exc:
        raise EvolutionRejected(f"SCHEMA_INVALID:{kind}:{exc}") from exc


def resolve_owner(problem_type: str) -> dict[str, Any]:
    owner_map = load_json(OWNER_MAP_PATH)
    for route in owner_map["routes"]:
        if problem_type in route["problem_types"]:
            if route["canonical_owner_repository"] == "HOLD_OWNER_REVIEW_REQUIRED":
                raise EvolutionRejected("CANONICAL_OWNER_UNRESOLVED")
            return deepcopy(route)
    raise EvolutionRejected("CANONICAL_OWNER_UNRESOLVED")


def classify_risk(
    *,
    semantic_change: bool = False,
    authority_change: bool = False,
    security_boundary_change: bool = False,
    irreversible_external_effect: bool = False,
    deterministic_derived_repair: bool = False,
) -> str:
    if irreversible_external_effect:
        return "ER-4"
    if semantic_change or authority_change or security_boundary_change:
        return "ER-3"
    if deterministic_derived_repair:
        return "ER-1"
    return "ER-2"


def state_transition_allowed(source: str, target: str) -> bool:
    machine = load_json(ROOT / "evolution-state-machine.json")
    if [source, target] in machine["invalid_shortcuts"]:
        return False
    return any(
        item["from"] == source and item["to"] == target
        for item in machine["transitions"]
    )


def assert_constitution_preserved(requested_changes: list[str]) -> None:
    protected = set(load_json(POLICY_PATH)["constitutional_invariants"])
    attempted = protected.intersection(requested_changes)
    if attempted:
        raise EvolutionRejected(
            "CONSTITUTIONAL_INVARIANT_IMMUTABLE:" + ",".join(sorted(attempted))
        )


def assert_no_secret_disclosure(value: Any) -> None:
    text = json.dumps(value, ensure_ascii=False)
    patterns = (
        r"Authorization:\s*Bearer\s+[A-Za-z0-9._~+/=-]{16,}",
        r"\bsk-[A-Za-z0-9_-]{16,}\b",
        r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
    )
    if any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in patterns):
        raise EvolutionRejected("RAW_SECRET_DISCLOSURE")


def assert_unique_semantic_objects(
    values: list[dict[str, Any]],
    id_field: str,
) -> None:
    identities = [item.get(id_field) for item in values]
    if None in identities or len(identities) != len(set(identities)):
        raise EvolutionRejected("DUPLICATE_SEMANTIC_OBJECT")


def generate_variants(
    problem_id: str,
    parent_revision: str,
    target_repository: str,
    target_component: str,
) -> list[dict[str, Any]]:
    variants = [
        {
            "variant_id": f"{problem_id}-V1",
            "variant_kind": "MINIMAL_REPAIR",
            "parent_revision": parent_revision,
            "target_repository": target_repository,
            "target_component": target_component,
            "change_summary": "Regenerate the derived registry from the unchanged source.",
            "affected_contracts": ["DERIVED_REGISTRY_PROJECTION"],
            "semantic_change": False,
            "security_change": False,
            "authority_change": False,
            "migration_required": False,
            "implementation_reference": "demo:deterministic-regeneration",
            "test_reference": "EV-T23",
            "rollback_reference": f"{problem_id}-ROLLBACK",
        },
        {
            "variant_id": f"{problem_id}-V2",
            "variant_kind": "ALTERNATIVE_REPAIR",
            "parent_revision": parent_revision,
            "target_repository": target_repository,
            "target_component": target_component,
            "change_summary": "Regenerate and reorder the same derived entries.",
            "affected_contracts": ["DERIVED_REGISTRY_PROJECTION"],
            "semantic_change": False,
            "security_change": False,
            "authority_change": False,
            "migration_required": False,
            "implementation_reference": "demo:regeneration-with-reordering",
            "test_reference": "EV-T23",
            "rollback_reference": f"{problem_id}-ROLLBACK",
        },
        {
            "variant_id": f"{problem_id}-V0",
            "variant_kind": "NO_CHANGE_BASELINE",
            "parent_revision": parent_revision,
            "target_repository": target_repository,
            "target_component": target_component,
            "change_summary": "Retain the stale fixture as the no-change baseline.",
            "affected_contracts": [],
            "semantic_change": False,
            "security_change": False,
            "authority_change": False,
            "migration_required": False,
            "implementation_reference": "demo:no-change",
            "test_reference": "EV-T05",
            "rollback_reference": f"{problem_id}-ROLLBACK",
        },
    ]
    maximum = load_json(LIMITS_PATH)["max_patch_variants_per_problem"]
    if len(variants) > maximum:
        raise EvolutionRejected("MAX_PATCH_VARIANTS_EXCEEDED")
    assert_unique_semantic_objects(variants, "variant_id")
    for variant in variants:
        validate_object("patch_variant", variant)
    return variants


def evaluate_variant(variant: dict[str, Any]) -> dict[str, Any]:
    kind = variant["variant_kind"]
    if kind == "MINIMAL_REPAIR":
        results = ("PASS", "PASS", "PASS", "PASS", "PASS", "PASS", "HIGH", "SELECT", 0.98)
        limitations = ["SYNTHETIC_FIXTURE_ONLY"]
    elif kind == "ALTERNATIVE_REPAIR":
        results = ("PASS", "PASS", "PASS", "PASS", "PASS", "PASS", "MEDIUM", "SELECT_WITH_CONDITIONS", 0.80)
        limitations = ["UNNECESSARY_ORDERING_CHANGE", "SYNTHETIC_FIXTURE_ONLY"]
    else:
        results = ("FAIL", "PASS", "FAIL", "FAIL", "PASS", "PASS", "HIGH", "REJECT", 0.99)
        limitations = ["KNOWN_STALE_STATE_RETAINED"]
    evaluation = {
        "evaluation_id": variant["variant_id"] + "-EVAL",
        "variant_id": variant["variant_id"],
        "evaluator_agent": "FITNESS_EVALUATOR_AGENT:REFERENCE",
        "test_results": results[0],
        "security_results": results[1],
        "compatibility_results": results[2],
        "agent_usability_results": results[3],
        "resource_results": results[4],
        "reversibility_results": results[5],
        "evidence_quality": results[6],
        "limitations": limitations,
        "recommendation": results[7],
        "confidence": results[8],
    }
    validate_object("fitness_evaluation", evaluation)
    return evaluation


def hard_gates_pass(evaluation: dict[str, Any]) -> bool:
    return all(
        evaluation[field] == "PASS"
        for field in ("test_results", "security_results", "reversibility_results")
    )


def select_variant(
    problem_id: str,
    variants: list[dict[str, Any]],
    evaluations: list[dict[str, Any]],
) -> dict[str, Any]:
    kinds = {variant["variant_kind"] for variant in variants}
    required = set(load_json(LIMITS_PATH)["required_variant_kinds"])
    if not required.issubset(kinds):
        raise EvolutionRejected("NO_CHANGE_OR_REQUIRED_VARIANT_MISSING")
    eligible = [
        (variant, evaluation)
        for variant, evaluation in zip(variants, evaluations, strict=True)
        if hard_gates_pass(evaluation)
        and evaluation["recommendation"] in {"SELECT", "SELECT_WITH_CONDITIONS"}
    ]
    if not eligible:
        raise EvolutionRejected("REJECT_ALL_VARIANTS")
    selected, selected_evaluation = sorted(
        eligible,
        key=lambda item: (
            item[0]["variant_kind"] != "MINIMAL_REPAIR",
            -item[1]["confidence"],
            item[0]["variant_id"],
        ),
    )[0]
    rejected = [item["variant_id"] for item in variants if item != selected]
    record = {
        "selection_id": problem_id + "-SELECTION",
        "problem_id": problem_id,
        "selected_variant": selected["variant_id"],
        "rejected_variants": rejected,
        "selection_dimensions": load_json(FITNESS_PATH)["dimensions"],
        "tradeoffs": [
            "Minimal regeneration preserves source semantics.",
            "Alternative repair adds unnecessary ordering change.",
            "No-change baseline retains the reproduced defect.",
        ],
        "counterevidence": ["Production behavior was not assessed."],
        "confidence": selected_evaluation["confidence"],
        "result": "SELECT",
        "authorization_status": "POLICY_PREAUTHORIZED_DRAFT_ONLY",
    }
    validate_object("selection_record", record)
    return record


def repaired_registry(source: dict[str, Any]) -> dict[str, Any]:
    return {
        "registry_id": "D19-DEMO-DERIVED-TASK-REGISTRY",
        "generated_from": source["source_revision"],
        "source_sha256": digest(source),
        "entries": deepcopy(source["entries"]),
        "status": "CURRENT",
    }


def run_demo() -> dict[str, Any]:
    source = load_json(FIXTURE_ROOT / "source-task-registry.json")
    stale = load_json(FIXTURE_ROOT / "stale-derived-registry.json")
    repaired = repaired_registry(source)
    if canonical_bytes(stale) == canonical_bytes(repaired):
        raise EvolutionRejected("DEMO_DEFECT_NOT_REPRODUCED")
    owner = resolve_owner("STALE_TASK_REGISTRY")
    problem = {
        "problem_id": "D19-ER1-DEMO-001",
        "discovered_by_agent": "SCOUT_AGENT:REFERENCE",
        "discovered_at": "2026-08-02T00:00:00+08:00",
        "affected_component": "DEMO_DERIVED_TASK_REGISTRY",
        "canonical_owner_repository": owner["canonical_owner_repository"],
        "observation": {
            "type": "STALE_TASK_REGISTRY",
            "summary": "Derived fixture omits a source task and retains an obsolete digest.",
            "source_reference": "demo/fixtures/stale-derived-registry.json",
        },
        "reproduction": {
            "status": "REPRODUCED",
            "attempts": 1,
            "steps": ["Compare derived projection with deterministic source projection."],
            "expected": digest(repaired),
            "observed": digest(stale),
        },
        "evidence_references": [
            "demo/fixtures/source-task-registry.json",
            "demo/fixtures/stale-derived-registry.json",
        ],
        "severity": "LOW",
        "risk_class": "ER-1",
        "agent_impact": "Machine task discovery would omit DEMO-TASK-B.",
        "security_impact": "NONE_OBSERVED",
        "authority_impact": "NONE",
        "confidence": 1.0,
        "known_limitations": ["SYNTHETIC_FIXTURE_ONLY", "NO_REAL_RUNTIME"],
    }
    validate_object("problem_evidence", problem)
    variants = generate_variants(
        problem["problem_id"],
        source["source_revision"],
        owner["canonical_owner_repository"],
        problem["affected_component"],
    )
    proposal = {
        "evolution_id": "D19-ER1-EVOLUTION-001",
        "problem_id": problem["problem_id"],
        "objective": "Restore the deterministic derived registry without changing source semantics.",
        "proposed_variants": [item["variant_id"] for item in variants],
        "fitness_dimensions": load_json(FITNESS_PATH)["dimensions"],
        "forbidden_changes": ["SOURCE_OF_TRUTH", "AUTHORITY", "SECURITY_BOUNDARY", "P0_10"],
        "required_tests": ["EV-T23", "EV-T24", "EV-T25"],
        "required_reviewers": ["FITNESS_EVALUATOR_AGENT", "AUTHORITY_BOUNDARY_AGENT"],
        "authorization_class": "ER-1",
        "rollback_requirements": ["RESTORE_STALE_FIXTURE_COPY", "RETAIN_FAILED_MUTATION_EVIDENCE"],
    }
    validate_object("evolution_proposal", proposal)
    evaluations = [evaluate_variant(item) for item in variants]
    selection = select_variant(problem["problem_id"], variants, evaluations)
    rollback = {
        "rollback_id": problem["problem_id"] + "-ROLLBACK",
        "mutation_id": problem["problem_id"] + "-MUTATION",
        "pre_change_revision": digest(stale),
        "rollback_target_revision": digest(stale),
        "trigger": "ANY_POST_APPLY_VALIDATION_FAILURE",
        "procedure_reference": "Restore the retained stale fixture copy in the isolated demo workspace.",
        "validation_results": "PASS",
        "failed_mutation_retained": True,
        "evidence_references": ["problem-evidence.json", "outcome-evidence.json"],
        "status": "READY",
    }
    validate_object("rollback_evidence", rollback)
    lineage = {
        "lineage_id": problem["problem_id"] + "-LINEAGE",
        "parent_revision": digest(stale),
        "child_revision": digest(repaired),
        "mutation_id": problem["problem_id"] + "-MUTATION",
        "trigger_evidence": problem["evidence_references"],
        "selected_variant": selection["selected_variant"],
        "rejected_variants": selection["rejected_variants"],
        "authorization_reference": "D19-ER1-POLICY-DRAFT-PR-ONLY",
        "release_reference": "NONE_NOT_RELEASED",
        "outcome_evidence": ["outcome-evidence.json"],
        "rollback_reference": "rollback-evidence.json",
        "fitness_before": {"correctness": "FAIL", "task_count": len(stale["entries"])},
        "fitness_after": {"correctness": "PASS", "task_count": len(repaired["entries"])},
        "retention_status": "RETAINED",
    }
    validate_object("evolution_lineage", lineage)
    bundle = {
        "problem_evidence": problem,
        "evolution_proposal": proposal,
        "variants": variants,
        "fitness_evaluations": evaluations,
        "selection_record": selection,
        "authorization_reference": {
            "status": "POLICY_PREAUTHORIZED_DRAFT_ONLY",
            "merge_authorized": False,
            "production_activation_authorized": False,
        },
        "mutation_receipt": {
            "receipt_semantics": "REFERENCE_DEMO_NOT_CANONICAL_RECEIPT",
            "mutation_id": lineage["mutation_id"],
            "selected_variant": selection["selected_variant"],
            "source_unchanged": True,
            "authority_effect": "NONE",
        },
        "repaired_registry": repaired,
        "outcome_evidence": {
            "post_apply_observation": "PASS",
            "deterministic_source_match": True,
            "real_runtime_changed": False,
            "production_deployment": False,
            "database_changed": False,
            "credential_created": False,
            "p0_10_reopened": False,
        },
        "rollback_evidence": rollback,
        "lineage": lineage,
    }
    assert_no_secret_disclosure(bundle)
    return bundle


def write_demo_run(output: Path) -> dict[str, Any]:
    output = output.resolve()
    temporary_root = Path(tempfile.gettempdir()).resolve()
    allowed_roots = {DBA_ROOT.resolve(), temporary_root, Path("/tmp").resolve()}
    if not any(output.is_relative_to(root) for root in allowed_roots):
        raise EvolutionRejected("OUTPUT_PATH_NOT_ALLOWLISTED")
    bundle = run_demo()
    output.mkdir(parents=True, exist_ok=True)
    (output / "variants").mkdir(exist_ok=True)
    (output / "fitness-evaluations").mkdir(exist_ok=True)
    files = {
        "problem-evidence.json": bundle["problem_evidence"],
        "evolution-proposal.json": bundle["evolution_proposal"],
        "selection-record.json": bundle["selection_record"],
        "authorization-reference.json": bundle["authorization_reference"],
        "mutation-receipt.json": bundle["mutation_receipt"],
        "outcome-evidence.json": bundle["outcome_evidence"],
        "rollback-evidence.json": bundle["rollback_evidence"],
        "lineage.json": bundle["lineage"],
        "repaired-derived-registry.json": bundle["repaired_registry"],
    }
    for name, value in files.items():
        (output / name).write_text(
            json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    for value in bundle["variants"]:
        (output / "variants" / f"{value['variant_id']}.json").write_text(
            json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    for value in bundle["fitness_evaluations"]:
        (output / "fitness-evaluations" / f"{value['evaluation_id']}.json").write_text(
            json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    return bundle


def main() -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    demo = subparsers.add_parser("demo")
    demo.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    bundle = write_demo_run(args.output)
    print("FIRST_EVOLUTION_DEMO_RESULT=PASS")
    print(f"DETERMINISTIC_BUNDLE_DIGEST={digest(bundle)}")
    print("REAL_RUNTIME_CHANGED=false")
    print("PRODUCTION_DEPLOYMENT=false")
    print("P0_10_REOPENED=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
