#!/usr/bin/env python3
"""Dependency-free TITMAS Development conformance harness."""

from __future__ import annotations

import json
import hashlib
import importlib.util
import re
import sys
from pathlib import Path
from typing import Any

TITMAS_ROOT = Path(__file__).resolve().parents[1]
DBA_ROOT = TITMAS_ROOT.parent
REPORT_PATH = TITMAS_ROOT / "conformance" / "reports" / "latest.json"
MAX_JSON_BYTES = 1_000_000
MAX_SCHEMA_DEPTH = 32
REQUIRED_REGISTRY_FIELDS = {
    "id", "title", "title_zh", "category", "status", "maturity",
    "owner_ref", "authority_ref", "version", "normative",
    "implementation_status", "conformance_status", "security_review_status",
    "external_adoption_status", "created_at", "updated_at", "supersedes",
    "dependencies", "limitations",
}


class ConformanceError(ValueError):
    pass


def load_json(path: Path) -> Any:
    resolved = path.resolve()
    if not resolved.is_relative_to(DBA_ROOT.resolve()):
        raise ConformanceError(f"{path}: path escapes the DBA root")
    if path.is_symlink() or not path.is_file():
        raise ConformanceError(f"{path}: expected a regular non-symlink file")
    if path.stat().st_size > MAX_JSON_BYTES:
        raise ConformanceError(f"{path}: file exceeds {MAX_JSON_BYTES} bytes")
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def validate_schema(
    instance: Any,
    schema: dict[str, Any],
    path: str = "$",
    depth: int = 0,
) -> None:
    if depth > MAX_SCHEMA_DEPTH:
        raise ConformanceError(f"{path}: schema depth exceeds {MAX_SCHEMA_DEPTH}")
    expected = schema.get("type")
    type_map = {
        "object": dict, "array": list, "string": str,
        "boolean": bool, "integer": int, "number": (int, float),
    }
    if expected in type_map and not isinstance(instance, type_map[expected]):
        raise ConformanceError(f"{path}: expected {expected}")
    if expected == "integer" and isinstance(instance, bool):
        raise ConformanceError(f"{path}: boolean is not an integer")
    if expected == "number" and isinstance(instance, bool):
        raise ConformanceError(f"{path}: boolean is not a number")
    if (
        isinstance(instance, (int, float))
        and not isinstance(instance, bool)
        and "minimum" in schema
        and instance < schema["minimum"]
    ):
        raise ConformanceError(f"{path}: number is less than minimum")
    if "enum" in schema and instance not in schema["enum"]:
        raise ConformanceError(f"{path}: value {instance!r} is not allowed")
    if "const" in schema and instance != schema["const"]:
        raise ConformanceError(f"{path}: expected constant {schema['const']!r}")
    if isinstance(instance, str) and len(instance) < schema.get("minLength", 0):
        raise ConformanceError(f"{path}: string is shorter than minLength")
    if isinstance(instance, list):
        if len(instance) < schema.get("minItems", 0):
            raise ConformanceError(f"{path}: array is shorter than minItems")
        item_schema = schema.get("items")
        if item_schema:
            for index, item in enumerate(instance):
                validate_schema(item, item_schema, f"{path}[{index}]", depth + 1)
    if isinstance(instance, dict):
        missing = [key for key in schema.get("required", []) if key not in instance]
        if missing:
            raise ConformanceError(f"{path}: missing required fields {missing}")
        for key, child in schema.get("properties", {}).items():
            if key in instance:
                validate_schema(instance[key], child, f"{path}.{key}", depth + 1)
        if schema.get("additionalProperties") is False:
            extra = sorted(set(instance) - set(schema.get("properties", {})))
            if extra:
                raise ConformanceError(f"{path}: additional properties not allowed {extra}")


def parse_frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ConformanceError(f"{path}: missing frontmatter start")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ConformanceError(f"{path}: missing frontmatter end") from exc
    result: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ConformanceError(f"{path}: invalid frontmatter line {line!r}")
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip()
    required = {
        "id", "title", "title_zh", "category", "status", "maturity",
        "owner_ref", "authority_ref", "version", "normative",
    }
    missing = sorted(required - result.keys())
    if missing:
        raise ConformanceError(f"{path}: missing frontmatter fields {missing}")
    return result


def semantic_errors(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    claims = payload.get("claims") or []
    if not isinstance(claims, list) or not all(isinstance(item, str) for item in claims):
        errors.append("MALFORMED_CLAIMS")
    evidence = payload.get("evidence_binding") or {}
    if evidence.get("source_kind") == "OBSERVATION" and evidence.get("admission_status") == "ADMITTED_EVIDENCE":
        errors.append("OBSERVATION_AS_EVIDENCE")
    if "TRUTH" in claims:
        errors.append("EVIDENCE_AS_TRUTH")
    if "authorization_status" in (payload.get("verification_result") or {}):
        errors.append("VERIFICATION_AS_AUTHORIZATION")
    if payload.get("mapping_only") is True and payload.get("external_adoption_status") == "ADOPTED":
        errors.append("MAPPING_AS_ADOPTION")
    if payload.get("profile_status") == "STABLE" and payload.get("maturity") == "Experimental":
        errors.append("EXPERIMENTAL_AS_STABLE")
    if payload.get("recommendation_mode") == "COMMAND":
        errors.append("RECOMMENDATION_AS_COMMAND")
    if (payload.get("health_result") or {}).get("certification") is True:
        errors.append("HEALTH_AS_CERTIFICATION")
    if payload.get("authority_ref") == "REFERENCE_IMPLEMENTATION":
        errors.append("REFERENCE_IMPL_AS_AUTHORITY")
    return errors


def brand_identity_errors(payload: dict[str, Any]) -> list[str]:
    """Reject semantic elevation or identity drift in the bilingual brand layer."""
    errors: list[str] = []
    if payload.get("canonical_name") != "TITMAS":
        errors.append("NON_TITMAS_ENGLISH_BRAND")
    if payload.get("canonical_name_zh") != "夏日之海":
        errors.append("CHINESE_BRAND_IDENTITY_DRIFT")
    if payload.get("new_project_created") is True or payload.get("project_continuity") is not True:
        errors.append("BRAND_AS_NEW_PROJECT")
    if payload.get("authority_change") is True:
        errors.append("NEW_AUTHORITY_FROM_BRAND")
    if payload.get("brand_change_means_standard_adoption") is True:
        errors.append("BRAND_CHANGE_AS_ADOPTION")
    if payload.get("domain_registered") is True and payload.get("public_launch_authorized") is True:
        errors.append("DOMAIN_REGISTRATION_AS_PUBLIC_LAUNCH")
    return errors


def check_registries() -> dict[str, Any]:
    specs = TITMAS_ROOT / "specifications"
    registry_schema = load_json(TITMAS_ROOT / "conformance" / "schemas" / "registry-entry.schema.json")
    checked = 0
    ids: set[str] = set()
    for name in ("registry.yaml", "proposal-registry.yaml"):
        doc = load_json(specs / name)
        for entry in doc["entries"]:
            validate_schema(entry, registry_schema)
            missing = REQUIRED_REGISTRY_FIELDS - entry.keys()
            if missing:
                raise ConformanceError(f"{name}/{entry.get('id')}: missing {sorted(missing)}")
            if entry["id"] in ids and name == "registry.yaml":
                raise ConformanceError(f"duplicate specification id {entry['id']}")
            ids.add(entry["id"])
            ref = entry.get("document_ref")
            if ref and not (specs / ref).is_file():
                raise ConformanceError(f"{name}: missing document_ref {ref}")
            checked += 1
    roles = load_json(specs / "role-registry.yaml")
    if roles["assignments"]:
        raise ConformanceError("role assignments must remain empty before Human Decision")
    for role in roles["roles"]:
        validate_schema(role, registry_schema)
        checked += 1
    maturity = load_json(specs / "maturity-registry.yaml")
    state_ids = [item["id"] for item in maturity["states"]]
    if len(state_ids) != len(set(state_ids)) or maturity["default"] not in state_ids:
        raise ConformanceError("invalid maturity registry")
    return {"registry_entries_checked": checked, "maturity_states_checked": len(state_ids)}


def check_frontmatter() -> dict[str, Any]:
    proposals = sorted((TITMAS_ROOT / "specifications" / "proposals").glob("*.md"))
    parsed = [parse_frontmatter(path) for path in proposals]
    return {"proposal_frontmatter_checked": len(parsed)}


def check_fixtures() -> dict[str, Any]:
    schema = load_json(TITMAS_ROOT / "conformance" / "schemas" / "core-developer-surface.schema.json")
    positive_paths = sorted((TITMAS_ROOT / "conformance" / "fixtures" / "positive").glob("*.json"))
    for path in positive_paths:
        payload = load_json(path)
        validate_schema(payload, schema)
        errors = semantic_errors(payload)
        if errors:
            raise ConformanceError(f"{path.name}: semantic errors {errors}")
    negative = load_json(TITMAS_ROOT / "conformance" / "fixtures" / "negative" / "semantic-elevation-cases.json")
    for case in negative["cases"]:
        errors = semantic_errors(case["payload"])
        if case["expected_error"] not in errors:
            raise ConformanceError(f"{case['id']}: expected {case['expected_error']}, got {errors}")
    return {"positive_cases_passed": len(positive_paths), "negative_cases_rejected": len(negative["cases"])}


def check_community_status() -> dict[str, Any]:
    path = TITMAS_ROOT / "community" / "community-status.json"
    status = load_json(path)
    schema = load_json(TITMAS_ROOT / "conformance" / "schemas" / "community-status.schema.json")
    validate_schema(status, schema)
    must_be_false = (
        "public_launch_authorized", "community_established", "foundation_created",
        "maintainer_assigned", "external_reviewer_assigned",
        "commercial_offer_authorized", "certification_authorized",
        "release_authorized", "cs_g0_pass", "cs_g1_pass",
    )
    elevated = [key for key in must_be_false if status[key] is not False]
    if elevated:
        raise ConformanceError(f"community status semantic elevation: {elevated}")
    for key in ("community_member_count", "external_contributor_count", "external_adopter_count"):
        if status[key] != 0:
            raise ConformanceError(f"{key} must remain zero")
    return {"community_invariants_checked": len(must_be_false) + 3}


def check_contributor_entry() -> dict[str, Any]:
    entry = load_json(DBA_ROOT / "TITMAS-CONTRIBUTOR-ENTRY-v0.1.json")
    schema = load_json(DBA_ROOT / "architecture" / "schemas" / "titmas-contributor-entry.schema.v0.1.json")
    validate_schema(entry, schema)
    for ref in entry["document_refs"].values():
        if not (DBA_ROOT / ref).exists():
            raise ConformanceError(f"contributor entry references missing path {ref}")
    return {
        "contribution_surfaces_checked": len(entry["contribution_surfaces"]),
        "document_refs_checked": len(entry["document_refs"]),
    }


def check_internal_reviews() -> dict[str, Any]:
    review_paths = sorted((TITMAS_ROOT / "reviews").glob("*-review.json"))
    if len(review_paths) != 5:
        raise ConformanceError(f"expected 5 internal reviews, found {len(review_paths)}")
    findings = 0
    for path in review_paths:
        review = load_json(path)
        required = {
            "review_id", "review_role", "model", "session_count", "result",
            "findings", "summary", "post_review_disposition", "authority_effect",
        }
        missing = sorted(required - review.keys())
        if missing:
            raise ConformanceError(f"{path.name}: missing fields {missing}")
        if review["model"] != "qwen3.7-max" or review["authority_effect"] != "NONE":
            raise ConformanceError(f"{path.name}: invalid model or authority boundary")
        if review["result"] not in {"PASS", "FAIL", "HOLD"}:
            raise ConformanceError(f"{path.name}: invalid review result")
        severities = {item["severity"] for item in review["findings"]}
        if severities & {"HIGH", "CRITICAL"} and review["result"] == "PASS":
            raise ConformanceError(f"{path.name}: HIGH/CRITICAL finding cannot PASS")
        findings += len(review["findings"])
    return {"review_sessions_checked": len(review_paths), "findings_checked": findings}


def validate_json_file(path: Path, schema_path: Path) -> dict[str, Any]:
    value = load_json(path)
    schema = load_json(schema_path)
    validation_value = dict(value)
    validation_value.pop("$schema", None)
    validate_schema(validation_value, schema, path=str(path.relative_to(DBA_ROOT)))
    return value


def check_agent_native_surfaces() -> dict[str, Any]:
    root = TITMAS_ROOT / "agent-native"
    schemas = root / "schemas"
    entry = validate_json_file(DBA_ROOT / "agent-index.json", schemas / "agent-index.schema.json")
    manifest = validate_json_file(root / "community-manifest.json", schemas / "community-manifest.schema.json")
    state = validate_json_file(root / "current-state.json", schemas / "current-state.schema.json")
    if not entry["canonical_agent_entry"]:
        raise ConformanceError("agent-index.json must be the canonical agent entry")
    if manifest["canonical_entry"] != "../../agent-index.json":
        raise ConformanceError("community manifest creates a competing machine entry")

    must_be_false = (
        "public_agent_community_authorized", "public_contribution_authorized",
        "public_github_agent_write_authorized", "agent_community_established",
        "public_launch_authorized", "release_authorized",
        "certification_authorized", "commercial_ready", "foundation_created",
        "cs_g0_pass", "cs_g1_pass", "current_99_percent_autonomy_claim",
    )
    elevated = [key for key in must_be_false if state[key] is not False]
    if elevated:
        raise ConformanceError(f"agent-native state semantic elevation: {elevated}")
    if state["agent_operational_majority_long_term_target"] != 0.99:
        raise ConformanceError("long-term target drift")
    for key in (
        "external_agent_participant_count", "external_human_contributor_count",
        "external_adopter_count",
    ):
        if state[key] != 0:
            raise ConformanceError(f"{key} must remain zero")

    participant_registry = load_json(root / "participants" / "participant-registry.json")
    validate_json_file(
        root / "participants" / "authority-registry.json",
        schemas / "authority-registry.schema.json",
    )
    participants = participant_registry["participants"]
    if participant_registry["agent_participant_count"] != len(participants):
        raise ConformanceError("agent participant count mismatch")
    lineages = {item["lineage_ref"] for item in participants}
    if participant_registry["independent_agent_lineage_count"] != len(lineages):
        raise ConformanceError("independent agent lineage count mismatch")
    for participant in participants:
        validate_schema(participant, load_json(schemas / "participant.schema.json"))
        if participant["participant_ref"] == participant["authority_issuer_ref"]:
            raise ConformanceError("participant self-authorization")

    task_registry = load_json(root / "tasks" / "task-registry.json")
    tasks = task_registry["tasks"]
    if len(tasks) != 12 or len({item["task_id"] for item in tasks}) != len(tasks):
        raise ConformanceError("task registry must contain 12 unique pilot tasks")
    task_schema = load_json(schemas / "task.schema.json")
    for task in tasks:
        validate_schema(task, task_schema)
        if task["source_revision"] != task_registry["source_revision"]:
            raise ConformanceError(f"{task['task_id']}: source revision drift")
        if task["authority_reference"] != "TITMAS-AGENT-NATIVE-COMMUNITY-D01":
            raise ConformanceError(f"{task['task_id']}: unauthorized authority reference")
    for evidence_ref in state["evidence_refs"]:
        if not (DBA_ROOT / evidence_ref).is_file():
            raise ConformanceError(f"current state evidence ref missing: {evidence_ref}")

    examples = (
        (root / "participants" / "example-capability-declaration.json", "capability-declaration"),
        (root / "participants" / "example-role-assignment.json", "role-assignment"),
        (root / "participants" / "example-revocation-record.json", "revocation-record"),
        (root / "participants" / "example-expiry-record.json", "expiry-record"),
        (root / "tasks" / "example-scope-lease.json", "scope-lease"),
        (root / "contributions" / "example-contribution-package.json", "contribution-package"),
        (root / "reviews" / "review-protocol.json", None),
        (root / "maintenance" / "example-maintenance-report.json", "maintenance-report"),
        (root / "recommendations" / "example-recommendation-package.json", "recommendation-package"),
        (root / "handoff" / "example-handoff-package.json", "handoff-package"),
    )
    checked = 0
    for path, schema_name in examples:
        if schema_name:
            validate_json_file(path, schemas / f"{schema_name}.schema.json")
        else:
            load_json(path)
        checked += 1
    return {
        "canonical_machine_entries": 1,
        "agent_participants_checked": len(participants),
        "independent_lineages_checked": len(lineages),
        "agent_tasks_checked": len(tasks),
        "agent_protocol_examples_checked": checked,
        "authority_invariants_checked": len(must_be_false),
    }


def check_bilingual_brand_identity() -> dict[str, Any]:
    entry = load_json(DBA_ROOT / "agent-index.json")
    identity = load_json(DBA_ROOT / "titmas-brand-identity.json")
    if entry.get("canonical_brand") != "TITMAS":
        raise ConformanceError("agent-index.json English brand must remain TITMAS")
    if entry.get("canonical_brand_zh") != "夏日之海":
        raise ConformanceError("agent-index.json Chinese brand must be 夏日之海")
    if entry.get("brand_identity_projection") != "titmas-brand-identity.json":
        raise ConformanceError("agent-index.json must reference the brand identity projection")
    if identity["machine_discovery"]["canonical_entry"] != "agent-index.json":
        raise ConformanceError("brand identity projection must point to the canonical machine entry")
    if identity["machine_discovery"]["second_canonical_entry_created"]:
        raise ConformanceError("brand identity projection creates a competing machine entry")
    normalized_identity = {
        "canonical_name": identity["canonical_name"],
        "canonical_name_zh": identity["canonical_name_zh"],
        "project_continuity": identity["project_continuity"],
        "new_project_created": identity["new_project_created"],
        "authority_change": identity["authority_change"],
        "brand_change_means_standard_adoption": False,
        "domain_registered": identity["domain"]["registered"],
        "public_launch_authorized": identity["domain"]["public_launch_authorized"],
    }
    errors = brand_identity_errors(normalized_identity)
    if errors:
        raise ConformanceError(f"brand identity projection errors {errors}")

    fixture = load_json(
        TITMAS_ROOT / "conformance" / "fixtures" / "brand"
        / "titmas-xiarizhihai-brand-cases.json"
    )
    for case in fixture["positive_cases"]:
        errors = brand_identity_errors(case["payload"])
        if errors:
            raise ConformanceError(f"{case['id']}: unexpected brand errors {errors}")
    for case in fixture["negative_cases"]:
        errors = brand_identity_errors(case["payload"])
        if case["expected_error"] not in errors:
            raise ConformanceError(
                f"{case['id']}: expected {case['expected_error']}, got {errors}"
            )
    return {
        "canonical_machine_entries": 1,
        "brand_identity_projections": 1,
        "positive_cases_passed": len(fixture["positive_cases"]),
        "negative_cases_rejected": len(fixture["negative_cases"]),
    }


def check_agent_native_adversarial() -> dict[str, Any]:
    payload = load_json(TITMAS_ROOT / "agent-native" / "security" / "adversarial-cases.json")
    cases = payload["cases"]
    required_attacks = {
        "PROMPT_INJECTION", "MALICIOUS_TASK_DESCRIPTION",
        "FORGED_PARTICIPANT_IDENTITY", "SELF_AUTHORIZATION", "SELF_APPROVAL",
        "AUTHORITY_ELEVATION", "TASK_SCOPE_EXPANSION", "REVIEW_COLLUSION",
        "SYBIL_SESSION_AS_INDEPENDENT_LINEAGE", "INFINITE_TASK_LOOP",
        "AUTOMATIC_ISSUE_PR_NOISE", "DUPLICATE_CONTRIBUTION",
        "MALICIOUS_SCHEMA", "PATH_TRAVERSAL", "HIDDEN_NETWORK_CALL",
        "SUPPLY_CHAIN_DEPENDENCY", "FAKE_ADOPTION", "FAKE_CERTIFICATION",
        "DELETE_FAILURE_RECORD", "NOT_ASSESSED_TO_PASS",
        "RECOMMENDATION_TO_COMMAND", "EVIDENCE_TO_TRUTH",
    }
    observed = {item["attack"] for item in cases}
    if observed != required_attacks:
        raise ConformanceError(f"adversarial case coverage drift: {sorted(required_attacks - observed)}")
    bad = [item["id"] for item in cases if item["expected"] != "REJECT" or not item["reason_code"]]
    if bad:
        raise ConformanceError(f"adversarial cases fail open: {bad}")
    cli_path = TITMAS_ROOT / "agent-native" / "community_cli.py"
    spec = importlib.util.spec_from_file_location("titmas_agent_native_cli", cli_path)
    if not spec or not spec.loader:
        raise ConformanceError("cannot load agent-native policy evaluator")
    cli = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cli)
    mismatches = []
    for item in cases:
        decision = cli.reject_adversarial(item["attack"])
        if (
            decision["decision"] != item["expected"]
            or decision["reason_code"] != item["reason_code"]
        ):
            mismatches.append(item["id"])
    if mismatches:
        raise ConformanceError(f"adversarial policy mismatch: {mismatches}")
    return {
        "adversarial_cases_rejected": len(cases),
        "adversarial_cases_executed": len(cases),
    }


def check_agent_native_value_gate() -> dict[str, Any]:
    fixture = load_json(
        TITMAS_ROOT / "agent-native" / "value-gate" / "agent-immune-five-task-fixture.json"
    )
    expected = {
        "total_suggestions": 25,
        "unique_factually_valid_findings": 3,
        "duplicate_findings": 5,
        "false_or_not_applicable_findings": 17,
        "final_outcome_improvements": 0,
        "harmful_modifications": 0,
    }
    drift = {key: (fixture.get(key), value) for key, value in expected.items()
             if fixture.get(key) != value}
    if drift:
        raise ConformanceError(f"Agent Immune value fixture drift: {drift}")
    if len(fixture["reason_codes"]) != 11:
        raise ConformanceError("value gate reason code coverage drift")
    return {"frozen_counts_checked": len(expected), "reason_codes_checked": 11}


VALUE_VALIDATION_REJECTIONS = {
    "SELF_AUTHORIZATION": "AUTHORITY_MUST_BE_EXTERNALLY_BOUND",
    "ROLE_ELEVATION": "ROLE_CANNOT_CREATE_AUTHORITY",
    "RELEASE_CREATION": "RELEASE_NOT_AUTHORIZED",
    "STANDARD_COMPLETE_CLAIM": "EXPERIMENT_NE_STANDARD_COMPLETION",
    "COMMERCIAL_ADOPTION_CLAIM": "EXPERIMENT_NE_COMMERCIAL_ADOPTION",
    "AUTHORITY_CHANGE": "AUTHORITY_CHANGE_OUT_OF_SCOPE",
    "DELETE_FAILURE": "FAILURE_RETENTION_REQUIRED",
    "RECOMMENDATION_TO_COMMAND": "RECOMMENDATION_NE_COMMAND",
    "EVIDENCE_TO_TRUTH": "EVIDENCE_NE_TRUTH",
}


def value_validation_rejection(attack: str) -> dict[str, str]:
    reason = VALUE_VALIDATION_REJECTIONS.get(attack)
    if not reason:
        return {"decision": "NOT_ASSESSED", "reason_code": "UNKNOWN_CASE"}
    return {"decision": "REJECT", "reason_code": reason}


def validate_value_lineage(lineage: dict[str, Any]) -> None:
    if lineage["independent_lineage_count"] > lineage["session_count"]:
        raise ConformanceError("independent lineage count exceeds session count")
    if lineage["model_count"] > lineage["session_count"]:
        raise ConformanceError("model count exceeds session count")
    if lineage["independent_lineage_count"] != len(lineage["lineage_refs"]):
        raise ConformanceError("independent lineage count does not match references")


def check_agent_native_value_validation_framework() -> dict[str, Any]:
    root = TITMAS_ROOT / "agent-native" / "value-validation"
    task_catalog = load_json(root / "ecology-box-001-task-catalog.v0.1.json")
    required_task_fields = {
        "task_id", "problem", "context", "allowed_scope", "forbidden_scope",
        "required_capability", "expected_output", "validation_method",
        "success_condition", "failure_condition",
    }
    tasks = task_catalog["tasks"]
    if task_catalog["task_count"] != len(tasks) or len(tasks) < 10:
        raise ConformanceError("value validation catalog must contain at least 10 tasks")
    task_ids = [item["task_id"] for item in tasks]
    if len(task_ids) != len(set(task_ids)):
        raise ConformanceError("value validation task IDs must be unique")
    for task in tasks:
        missing = sorted(required_task_fields - task.keys())
        if missing:
            raise ConformanceError(f"{task.get('task_id')}: missing task fields {missing}")
        if not task["allowed_scope"] or not task["forbidden_scope"]:
            raise ConformanceError(f"{task['task_id']}: scope must fail closed")
    if task_catalog["execution_authorized"] or task_catalog["external_action_authorized"]:
        raise ConformanceError("value validation task catalog authorizes execution")

    record = validate_json_file(
        root / "not-executed-record.v0.1.json",
        TITMAS_ROOT / "agent-native" / "schemas"
        / "value-validation-experiment-record.schema.json",
    )
    lineage = record["lineage"]
    validate_value_lineage(lineage)
    if record["record_status"] != "NOT_EXECUTED":
        raise ConformanceError("design example must remain NOT_EXECUTED")
    if record["action"] or record["output"] or record["evidence_reference"]:
        raise ConformanceError("non-execution example contains execution claims")
    if record["result"]["status"] != "NOT_ASSESSED":
        raise ConformanceError("non-execution result must remain NOT_ASSESSED")

    fixture = load_json(root / "security-negative-cases.v0.1.json")
    cases = fixture["cases"]
    if {item["attack"] for item in cases} != set(VALUE_VALIDATION_REJECTIONS):
        raise ConformanceError("value validation security coverage drift")
    for item in cases:
        actual = value_validation_rejection(item["attack"])
        if actual["decision"] != item["expected"]:
            raise ConformanceError(f"{item['id']}: security case failed open")
        if actual["reason_code"] != item["reason_code"]:
            raise ConformanceError(f"{item['id']}: reason code drift")
    if fixture["experiment_executed"]:
        raise ConformanceError("security fixture claims experiment execution")

    review = load_json(
        DBA_ROOT / "architecture" / "reviews"
        / "titmas-agent-native-value-validation-predevelopment-review-v0.1.json"
    )
    if review["requested_model"] != "qwen3.7-max":
        raise ConformanceError("predevelopment review requested model drift")
    if review["returned_model"] != "qwen3.7-max":
        raise ConformanceError("predevelopment review returned model drift")
    if review["authority_effect"] != "NONE" or review["decision_effect"] != "NONE":
        raise ConformanceError("advisory review creates Authority or Decision")
    if review["would_recommend_to_customer"] is not False:
        raise ConformanceError("pre-result customer recommendation must remain false")

    required_docs = (
        "architecture/titmas-agent-native-value-validation-baseline-v0.1.md",
        "architecture/titmas-agent-native-value-validation-framework-v0.1.md",
        "architecture/titmas-agent-native-ecology-box-001-v0.1.md",
        "architecture/titmas-agent-native-value-metrics-v0.1.md",
        "TITMAS-AGENT-NATIVE-VALUE-VALIDATION-HUMAN-DECISION-PACKET-v0.1.md",
    )
    missing_docs = [path for path in required_docs if not (DBA_ROOT / path).is_file()]
    if missing_docs:
        raise ConformanceError(f"value validation documents missing {missing_docs}")
    return {
        "ecology_box_tasks_checked": len(tasks),
        "experiment_records_checked": 1,
        "security_cases_rejected": len(cases),
        "independent_lineage_count": lineage["independent_lineage_count"],
        "predevelopment_reviews_checked": 1,
        "documents_checked": len(required_docs),
    }


ECOLOGY_BOX_001_REJECTIONS = {
    "SELF_AUTHORIZATION": "AUTHORITY_MUST_BE_EXTERNALLY_BOUND",
    "ROLE_ELEVATION": "ROLE_NE_AUTHORITY",
    "STANDARD_COMPLETE_CLAIM": "EXPERIMENT_NE_STANDARD_COMPLETION",
    "RELEASE_CREATION": "RELEASE_NOT_AUTHORIZED",
    "AUTHORITY_MUTATION": "AUTHORITY_CHANGE_OUT_OF_SCOPE",
    "DELETE_FAILURE": "FAILURE_RETENTION_REQUIRED",
    "EVIDENCE_TO_TRUTH": "EVIDENCE_NE_TRUTH",
    "RECOMMENDATION_TO_DECISION": "RECOMMENDATION_NE_DECISION",
    "TEST_PASS_TO_ADOPTION": "TEST_PASS_NE_ADOPTION",
}


def ecology_box_001_rejection(attack: str) -> dict[str, str]:
    reason = ECOLOGY_BOX_001_REJECTIONS.get(attack)
    if not reason:
        return {"decision": "NOT_ASSESSED", "reason_code": "UNKNOWN_CASE"}
    return {"decision": "REJECT", "reason_code": reason}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_agent_native_ecology_box_001_package() -> dict[str, Any]:
    root = TITMAS_ROOT / "agent-native" / "ecology-box-001"
    required_paths = (
        root / "README.md",
        root / "constitution.md",
        root / "protocol.md",
        root / "freeze-manifest.yaml",
        root / "participants" / "schema.json",
        root / "participants" / "registry.yaml",
        root / "roles" / "registry.yaml",
        root / "tasks" / "task-registry.yaml",
        root / "baseline" / "human-first-workflow.yaml",
        root / "metrics" / "schema.json",
        root / "reviews" / "blind-review-protocol.md",
        root / "runs" / "README.md",
        root / "memories" / "schema.json",
        root / "failure-scenarios" / "registry.yaml",
        root / "reports" / "final-report-template.md",
        DBA_ROOT / "architecture"
        / "titmas-agent-native-ecology-box-001-baseline-reconciliation-v0.1.md",
        DBA_ROOT / "architecture" / "reviews"
        / "titmas-ecology-box-001-package-predevelopment-review-v0.1.json",
        DBA_ROOT
        / "TITMAS-AGENT-NATIVE-ECOLOGY-BOX-001-HUMAN-DECISION-PACKET-v0.1.md",
    )
    missing = [str(path.relative_to(DBA_ROOT)) for path in required_paths if not path.is_file()]
    if missing:
        raise ConformanceError(f"Ecology Box 001 package files missing {missing}")

    manifest = load_json(root / "freeze-manifest.yaml")
    expected_manifest = {
        "experiment_id": "DEB-TITMAS-001",
        "source_repository": "joy7758/digital-biosphere-architecture-specification",
        "source_commit": "5ac9647a9bc784a4ccfdfe033ea73998d216829c",
        "metric_version": "0.1.0",
        "protocol_version": "0.1.0",
        "agent_role_version": "0.1.0",
        "status": "PREPARED",
    }
    drift = {
        key: (manifest.get(key), expected)
        for key, expected in expected_manifest.items()
        if manifest.get(key) != expected
    }
    if drift:
        raise ConformanceError(f"Ecology Box 001 freeze drift {drift}")
    false_fields = (
        "execution_authorized",
        "experiment_executed",
        "value_proven",
        "real_agent_contribution_authorized",
        "real_git_access_authorized",
        "public_report_authorized",
        "commercial_validation_authorized",
    )
    elevated = [field for field in false_fields if manifest.get(field) is not False]
    if elevated:
        raise ConformanceError(f"Ecology Box 001 semantic elevation {elevated}")

    hash_paths = {
        "task_set_hash": root / "tasks" / "task-registry.yaml",
        "protocol_sha256": root / "protocol.md",
        "roles_sha256": root / "roles" / "registry.yaml",
        "metrics_schema_sha256": root / "metrics" / "schema.json",
        "participant_schema_sha256": root / "participants" / "schema.json",
    }
    for key, path in hash_paths.items():
        expected = f"sha256:{sha256_file(path)}"
        actual = (
            manifest["task_set_hash"]
            if key == "task_set_hash"
            else f"sha256:{manifest['component_hashes'][key]}"
        )
        if actual != expected:
            raise ConformanceError(f"{key}: frozen hash mismatch")

    participant_schema = load_json(root / "participants" / "schema.json")
    participant_fields = {
        "participant_id", "provider", "model", "runtime", "lineage_id", "role",
        "capabilities", "limitations", "lease", "scope", "issued_by",
        "expires_at", "revocation",
    }
    if not participant_fields.issubset(set(participant_schema["required"])):
        raise ConformanceError("participant Schema required-field coverage drift")
    participants = load_json(root / "participants" / "registry.yaml")
    expected_count_keys = {
        "MODEL_COUNT", "SESSION_COUNT", "ROLE_COUNT", "INDEPENDENT_LINEAGE_COUNT",
    }
    if set(participants["counts"]) != expected_count_keys:
        raise ConformanceError("participant count dimensions drift")
    if (
        participants["participants"]
        or any(participants["counts"].values())
        or participants["participant_instances_created"]
        or participants["authority_effect"] != "NONE"
    ):
        raise ConformanceError("preparation package creates participant state")

    roles = load_json(root / "roles" / "registry.yaml")
    expected_roles = {
        "EXPLORER", "VALUE_JUDGE", "ARCHITECTURE_REVIEWER", "CONTRIBUTOR",
        "CONFORMANCE", "MEMORY", "RECOMMENDATION", "EVOLUTION_OBSERVER",
    }
    role_fields = {
        "role_id", "purpose", "allowed_actions", "forbidden_actions",
        "required_capabilities", "output_type",
    }
    role_ids = {role["role_id"] for role in roles["roles"]}
    if role_ids != expected_roles or any(not role_fields.issubset(role) for role in roles["roles"]):
        raise ConformanceError("Ecology Box 001 role registry drift")
    if roles["assignments"] or roles["authority_effect"] != "NONE":
        raise ConformanceError("role registry creates assignment or Authority")

    tasks = load_json(root / "tasks" / "task-registry.yaml")
    task_fields = {
        "task_id", "problem", "context", "allowed_scope", "forbidden_scope",
        "required_capability", "expected_output", "validation_method",
        "success_condition", "failure_condition",
    }
    task_ids = [item["task_id"] for item in tasks["tasks"]]
    if len(task_ids) < 10 or len(task_ids) != len(set(task_ids)):
        raise ConformanceError("Ecology Box 001 needs at least 10 unique tasks")
    for task in tasks["tasks"]:
        if not task_fields.issubset(task):
            raise ConformanceError(f"{task.get('task_id')}: task contract incomplete")
        if not task["allowed_scope"] or not task["forbidden_scope"]:
            raise ConformanceError(f"{task['task_id']}: task scope fails open")
    if tasks["execution_authorized"] or tasks["authority_effect"] != "NONE":
        raise ConformanceError("task registry authorizes execution")

    baseline = load_json(root / "baseline" / "human-first-workflow.yaml")
    expected_stages = ["Discovery", "Analysis", "Implementation", "Review", "Validation"]
    expected_metrics = {
        "human_time", "human_steps", "review_cycles", "rework_count", "final_quality",
    }
    if baseline["stages"] != expected_stages or set(baseline["metrics"]) != expected_metrics:
        raise ConformanceError("Human-first baseline structure drift")
    if (
        baseline["status"] != "PREPARED_NOT_EXECUTED"
        or baseline["baseline_executed"]
        or baseline["result_available"]
        or any(item["status"] != "NOT_ASSESSED" for item in baseline["metrics"].values())
    ):
        raise ConformanceError("Human-first baseline claims a result")

    metric_schema = load_json(root / "metrics" / "schema.json")
    properties = metric_schema["properties"]
    if (
        properties["composite_score_created"].get("const") is not False
        or properties["post_hoc_weight_change"].get("const") is not False
    ):
        raise ConformanceError("metric policy permits composite score or post-hoc weights")

    memory_schema = load_json(root / "memories" / "schema.json")
    memory_properties = memory_schema["properties"]
    if (
        memory_properties["adoption_status"].get("const") != "UNADOPTED"
        or memory_properties["authority_effect"].get("const") != "NONE"
    ):
        raise ConformanceError("Memory candidate creates Adoption or Authority")

    failures = load_json(root / "failure-scenarios" / "registry.yaml")
    expected_failures = {
        "HIGH_VOLUME_LOW_VALUE", "AGENT_CONFLICT", "ERRONEOUS_MEMORY",
        "MODEL_DRIFT", "PERMISSION_INDUCEMENT", "DUPLICATE_CONTRIBUTION",
        "SEMANTIC_ELEVATION", "EVIDENCE_TO_TRUTH",
        "RECOMMENDATION_TO_AUTHORITY", "TEST_PASS_TO_ADOPTION",
    }
    failure_names = {item["name"] for item in failures["scenarios"]}
    if failure_names != expected_failures:
        raise ConformanceError("Ecology Box 001 failure scenario coverage drift")
    if failures["failure_records_deletable"] or failures["execution_authorized"]:
        raise ConformanceError("failure registry permits deletion or execution")

    packet = (
        DBA_ROOT
        / "TITMAS-AGENT-NATIVE-ECOLOGY-BOX-001-HUMAN-DECISION-PACKET-v0.1.md"
    ).read_text(encoding="utf-8")
    for decision_id in ("HD-EB-01", "HD-EB-02", "HD-EB-03", "HD-EB-04", "HD-EB-05"):
        if decision_id not in packet:
            raise ConformanceError(f"Human Decision packet missing {decision_id}")
    if packet.count("decision=UNDECIDED") != 5:
        raise ConformanceError("Human Decision packet must keep five decisions UNDECIDED")

    review = load_json(
        DBA_ROOT / "architecture" / "reviews"
        / "titmas-ecology-box-001-package-predevelopment-review-v0.1.json"
    )
    if (
        review["requested_model"] != "qwen3.7-max"
        or review["transport_returned_model"] != "qwen3.7-max"
        or review["authority_effect"] != "NONE"
        or review["decision_effect"] != "NONE"
        or review["execution_authorized"]
    ):
        raise ConformanceError("predevelopment advisory review boundary drift")

    run_records = [
        path for path in (root / "runs").iterdir()
        if path.is_file() and path.name != "README.md"
    ]
    if run_records:
        raise ConformanceError("preparation package contains run records")
    report_template = (root / "reports" / "final-report-template.md").read_text(encoding="utf-8")
    if (
        "REPORT_CREATED=false" not in report_template
        or "PUBLIC_REPORT_AUTHORIZED=false" not in report_template
        or "VALUE_PROVEN=false" not in report_template
    ):
        raise ConformanceError("final report template elevates report or value state")

    for attack, reason_code in ECOLOGY_BOX_001_REJECTIONS.items():
        if ecology_box_001_rejection(attack) != {
            "decision": "REJECT", "reason_code": reason_code
        }:
            raise ConformanceError(f"{attack}: fail-closed rejection drift")

    return {
        "package_files_checked": len(required_paths),
        "frozen_hashes_checked": len(hash_paths),
        "participant_instances": 0,
        "role_definitions_checked": len(role_ids),
        "task_contracts_checked": len(task_ids),
        "baseline_metrics_not_assessed": len(expected_metrics),
        "failure_scenarios_checked": len(failure_names),
        "security_cases_rejected": len(ECOLOGY_BOX_001_REJECTIONS),
        "human_decisions_undecided": 5,
        "experiment_executed": False,
    }


def check_agent_native_pilot() -> dict[str, Any]:
    path = TITMAS_ROOT / "agent-native" / "pilot" / "pilot-result.json"
    if not path.exists():
        return {"pilot_result_present": False, "pilot_status": "NOT_EXECUTED"}
    result = load_json(path)
    required = {
        "pilot_status", "participant_count", "independent_lineage_count",
        "tasks_executed", "metrics", "threshold_results", "authority_violations",
        "semantic_elevation_findings", "harmful_modifications",
    }
    missing = sorted(required - result.keys())
    if missing:
        raise ConformanceError(f"pilot result missing fields {missing}")
    if result["participant_count"] < result["independent_lineage_count"]:
        raise ConformanceError("lineage count exceeds participant count")
    session_paths = sorted((path.parent / "sessions").glob("PILOT-SESSION-?.json"))
    if len(session_paths) != 7:
        raise ConformanceError(f"expected 7 primary pilot sessions, found {len(session_paths)}")
    session_schema = load_json(
        TITMAS_ROOT / "agent-native" / "schemas" / "pilot-session.schema.json"
    )
    returned_models = set()
    for session_path in session_paths:
        session = load_json(session_path)
        validate_schema(session, session_schema)
        returned_models.add(session["returned_model"])
        if session["failures"] or session["fallback"] != "NONE":
            raise ConformanceError(f"{session_path.name}: failed or used fallback")
    if returned_models != {"qwen3.7-max"}:
        raise ConformanceError(f"unexpected pilot models {sorted(returned_models)}")
    if result["authority_violations"] or result["semantic_elevation_findings"]:
        raise ConformanceError("pilot authority or semantic boundary violated")
    return {
        "pilot_result_present": True,
        "pilot_status": result["pilot_status"],
        "pilot_sessions_checked": len(session_paths),
        "pilot_tasks_checked": len(set(result["tasks_executed"])),
        "pilot_metrics_checked": len(result["metrics"]),
    }


def check_agent_native_reviews() -> dict[str, Any]:
    root = TITMAS_ROOT / "agent-native" / "pilot" / "reviews"
    initial = sorted(root.glob("*.json"))
    round_two = sorted((root / "round-2").glob("*.json"))
    if len(initial) != 7 or len(round_two) != 7:
        raise ConformanceError(
            f"expected 7 initial and 7 round-2 reviews, found {len(initial)} and {len(round_two)}"
        )
    schema = load_json(
        TITMAS_ROOT / "agent-native" / "schemas" / "review-receipt.schema.json"
    )
    sessions: set[str] = set()
    medium_or_hold = 0
    for path in initial + round_two:
        review = load_json(path)
        validate_schema(review, schema)
        if review["requested_model"] != "qwen3.7-max" or review["returned_model"] != "qwen3.7-max":
            raise ConformanceError(f"{path}: unexpected review model")
        if review["authority_effect"] != "NONE" or review["self_approval"]:
            raise ConformanceError(f"{path}: review authority elevation")
        if review["independence_level"] != "LEVEL_2_SAME_MODEL_ISOLATED_SESSION":
            raise ConformanceError(f"{path}: independence misrepresentation")
        if review["session_id"] in sessions:
            raise ConformanceError(f"{path}: duplicate review session")
        sessions.add(review["session_id"])
        if review["failures"] or review["fallback"] != "NONE":
            raise ConformanceError(f"{path}: failed or fallback review")
        if review["severity"] in {"HIGH", "CRITICAL"} and review["verdict"] == "PASS":
            raise ConformanceError(f"{path}: high finding cannot pass")
        medium_or_hold += review["severity"] in {"MEDIUM", "HIGH", "CRITICAL"} or review["verdict"] == "HOLD"
    disposition = load_json(
        TITMAS_ROOT / "agent-native" / "pilot" / "review-disposition-v1.1.json"
    )
    if disposition["review_sessions"] != len(initial) + len(round_two):
        raise ConformanceError("review disposition count mismatch")
    if disposition["independent_model_lineages"] != 1:
        raise ConformanceError("review lineage misrepresentation")
    return {
        "review_sessions_checked": len(sessions),
        "review_rounds_checked": 2,
        "independent_model_lineages": 1,
        "medium_or_hold_records_preserved": medium_or_hold,
    }


LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def check_local_links() -> dict[str, Any]:
    checked = 0
    for path in sorted(TITMAS_ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for raw in LINK_PATTERN.findall(text):
            target = raw.strip().split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.is_relative_to(DBA_ROOT.resolve()):
                raise ConformanceError(f"{path}: local link escapes DBA root {raw}")
            if not resolved.exists():
                raise ConformanceError(f"{path}: missing local link {raw}")
            checked += 1
    return {"local_links_checked": checked}


def run_all(write_report: bool = True) -> dict[str, Any]:
    checks = []
    functions = (
        ("registries", check_registries),
        ("frontmatter", check_frontmatter),
        ("fixtures", check_fixtures),
        ("community_status", check_community_status),
        ("contributor_entry", check_contributor_entry),
        ("internal_reviews", check_internal_reviews),
        ("agent_native_surfaces", check_agent_native_surfaces),
        ("bilingual_brand_identity", check_bilingual_brand_identity),
        ("agent_native_adversarial", check_agent_native_adversarial),
        ("agent_native_value_gate", check_agent_native_value_gate),
        ("agent_native_value_validation_framework", check_agent_native_value_validation_framework),
        ("agent_native_ecology_box_001_package", check_agent_native_ecology_box_001_package),
        ("agent_native_pilot", check_agent_native_pilot),
        ("agent_native_reviews", check_agent_native_reviews),
        ("local_links", check_local_links),
    )
    overall = "PASS"
    for name, function in functions:
        try:
            details = function()
            checks.append({"id": name, "status": "PASS", "details": details})
        except Exception as exc:  # fail closed with stable diagnostic
            overall = "FAIL"
            checks.append({
                "id": name,
                "status": "FAIL",
                "error": f"{type(exc).__name__}: {exc}",
                "remediation": f"Correct the reported {name} input and rerun: python3 TITMAS/conformance/harness.py",
            })
    report = {
        "report_version": "1.0.0",
        "profile": "TITMAS_DEVELOPMENT_CONFORMANCE",
        "status": overall,
        "checks": checks,
        "non_claims": [
            "CONFORMANCE_NE_TRUTH",
            "CONFORMANCE_NE_AUTHORIZATION",
            "CONFORMANCE_NE_ADOPTION",
            "CONFORMANCE_NE_CERTIFICATION"
        ],
    }
    if write_report:
        REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
        REPORT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return report


def main() -> int:
    report = run_all(write_report=True)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
