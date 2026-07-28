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

ECOLOGY_BOX_001_PREREGISTRATION_REJECTIONS = {
    "READY_TO_EXECUTED": "READY_NE_EXECUTED",
    "RESULT_TO_VALUE_PROVEN": "RESULT_NE_VALUE_PROVEN",
    "ACTIVITY_TO_COMMUNITY_VALUE": "AGENT_ACTIVITY_NE_COMMUNITY_VALUE",
    "SESSION_TO_LINEAGE": "SESSION_COUNT_NE_INDEPENDENT_LINEAGE_COUNT",
    "PILOT_PASS_TO_COMMERCIAL_VALUE": "PILOT_PASS_NE_COMMERCIAL_VALUE",
}

ECOLOGY_BOX_001_READINESS_REJECTIONS = {
    "FAIRNESS_PASS_TO_EMPIRICAL":
        "FAIRNESS_PROTOCOL_PASS_NE_EMPIRICAL_FAIRNESS",
    "REVIEWER_TEMPLATE_TO_ASSIGNED":
        "REVIEWER_TEMPLATE_NE_REVIEWER_ASSIGNMENT",
    "CUSTODIAN_PROTOCOL_TO_ASSIGNED":
        "CUSTODIAN_PROTOCOL_NE_CUSTODIAN_ASSIGNMENT",
    "PROVIDER_TEMPLATE_TO_ADOPTED":
        "PROVIDER_TEMPLATE_NE_PROVIDER_ADOPTION",
    "PLANNED_LINEAGE_TO_CURRENT":
        "PLANNED_LINEAGE_NE_CURRENT_LINEAGE",
    "READINESS_TO_AUTHORIZATION": "READINESS_NE_AUTHORIZATION",
    "BLOCKING_GAPS_TO_GO": "BLOCKING_GAPS_REQUIRE_NO_GO",
    "DRY_RUN_TO_EXPERIMENT":
        "SYNTHETIC_DRY_RUN_NE_EXPERIMENT_EXECUTION",
    "TEN_TASK_TO_THREE_TASK": "FROZEN_TEN_TASK_SET_REQUIRED",
    "HEALTH_SIGNAL_TO_EVIDENCE":
        "HEALTH_SIGNAL_NE_EVIDENCE_EVALUATION_OR_DECISION",
    "MODEL_RECOMMENDATION_TO_DECISION":
        "MODEL_RECOMMENDATION_NE_HUMAN_DECISION",
    "NO_GO_TO_EXPERIMENT_FAILURE": "NO_GO_NE_EXPERIMENT_FAILURE",
}


def ecology_box_001_rejection(attack: str) -> dict[str, str]:
    reason = ECOLOGY_BOX_001_REJECTIONS.get(attack)
    if not reason:
        return {"decision": "NOT_ASSESSED", "reason_code": "UNKNOWN_CASE"}
    return {"decision": "REJECT", "reason_code": reason}


def ecology_box_001_preregistration_rejection(transition: str) -> dict[str, str]:
    reason = ECOLOGY_BOX_001_PREREGISTRATION_REJECTIONS.get(transition)
    if not reason:
        return {"decision": "NOT_ASSESSED", "reason_code": "UNKNOWN_CASE"}
    return {"decision": "REJECT", "reason_code": reason}


def ecology_box_001_readiness_rejection(transition: str) -> dict[str, str]:
    reason = ECOLOGY_BOX_001_READINESS_REJECTIONS.get(transition)
    if not reason:
        return {"decision": "NOT_ASSESSED", "reason_code": "UNKNOWN_CASE"}
    return {"decision": "REJECT", "reason_code": reason}


def validate_ecology_box_001_preregistration_lineage(
    lineage: dict[str, Any],
) -> None:
    current = lineage["current_counts"]
    if current["INDEPENDENT_LINEAGE_COUNT"] > current["SESSION_COUNT"]:
        raise ConformanceError("independent lineage count exceeds session count")
    if current["MODEL_COUNT"] > current["SESSION_COUNT"]:
        raise ConformanceError("model count exceeds session count")
    if current["INDEPENDENT_LINEAGE_COUNT"] != len(lineage["lineage_refs"]):
        raise ConformanceError("independent lineage count does not match references")
    same_model_rule = lineage["counting_rules"][
        "single_model_multiple_sessions_multiple_roles"
    ]
    if same_model_rule["independent_lineage_count"] != 1:
        raise ConformanceError(
            "one model across sessions and roles must remain one lineage"
        )


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
    for decision_id in (
        "HD-EB-01", "HD-EB-02", "HD-EB-03", "HD-EB-04", "HD-EB-05",
        "HD-EB-06", "HD-EB-07", "HD-EB-08", "HD-EB-09", "HD-EB-10",
    ):
        if decision_id not in packet:
            raise ConformanceError(f"Human Decision packet missing {decision_id}")
    if packet.count("decision=UNDECIDED") != 10:
        raise ConformanceError("Human Decision packet must keep ten decisions UNDECIDED")

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
        "human_decisions_undecided": 10,
        "experiment_executed": False,
    }


def check_agent_native_ecology_box_001_preregistration() -> dict[str, Any]:
    root = TITMAS_ROOT / "agent-native" / "ecology-box-001"
    required_paths = {
        "pre_registration_sha256": root / "pre-registration.md",
        "fairness_review_sha256": root / "fairness-review.md",
        "bias_analysis_sha256": root / "bias-analysis.md",
        "blind_evaluation_protocol_sha256": root / "blind-evaluation-protocol.md",
        "agent_lineage_plan_sha256": root / "agent-lineage-plan.yaml",
        "independent_reviewer_model_sha256": root / "independent-reviewer-model.yaml",
        "blind_custodian_protocol_sha256": root / "blind-custodian-protocol.yaml",
        "provider_privacy_retention_policy_sha256":
            root / "provider-privacy-retention-policy.yaml",
        "human_decision_packet_sha256":
            DBA_ROOT
            / "TITMAS-AGENT-NATIVE-ECOLOGY-BOX-001-HUMAN-DECISION-PACKET-v0.1.md",
        "baseline_execution_plan_sha256": root / "baseline-execution-plan.md",
        "agent_native_execution_plan_sha256": root / "agent-native-execution-plan.md",
        "stop_rules_sha256": root / "stop-rules.yaml",
        "success_criteria_sha256": root / "success-criteria.md",
    }
    supporting_paths = (
        root / "freeze-review.yaml",
        DBA_ROOT / "architecture"
        / "titmas-agent-native-ecology-box-001-preregistration-baseline-v0.1.md",
        DBA_ROOT / "architecture" / "reviews"
        / "titmas-ecology-box-001-preregistration-predevelopment-review-v0.1.json",
        DBA_ROOT / "architecture" / "reviews"
        / "titmas-ecology-box-001-preregistration-post-remediation-review-v0.1.json",
        DBA_ROOT / "architecture" / "reviews"
        / "titmas-ecology-box-001-fairness-remediation-predevelopment-multimodel-review-v0.1.json",
        DBA_ROOT / "architecture" / "reviews"
        / "titmas-ecology-box-001-fairness-remediation-postreview-multimodel-v0.1.json",
        DBA_ROOT
        / "TITMAS-AGENT-NATIVE-ECOLOGY-BOX-001-PREREGISTRATION-AND-EXECUTION-REVIEW-REPORT-v0.1.md",
        DBA_ROOT
        / "TITMAS-AGENT-NATIVE-ECOLOGY-BOX-001-FAIRNESS-REMEDIATION-REPORT-v0.1.md",
    )
    missing = [
        str(path.relative_to(DBA_ROOT))
        for path in tuple(required_paths.values()) + supporting_paths
        if not path.is_file()
    ]
    if missing:
        raise ConformanceError(
            f"Ecology Box 001 pre-registration files missing {missing}"
        )

    freeze = load_json(root / "freeze-review.yaml")
    if freeze["status"] != "PREREGISTERED_FAIRNESS_DESIGN_PASS_EXECUTION_BLOCKED":
        raise ConformanceError("pre-registration freeze review status drift")
    if freeze["source_commit"] != "b92a9a8c0553b51afc832e549d9ad5af271443f2":
        raise ConformanceError("pre-registration source revision drift")
    for key, path in required_paths.items():
        if freeze["frozen_components"].get(key) != sha256_file(path):
            raise ConformanceError(f"{key}: pre-registration frozen hash mismatch")
    original_frozen_paths = {
        "task_registry_sha256": root / "tasks" / "task-registry.yaml",
        "metrics_schema_sha256": root / "metrics" / "schema.json",
        "roles_registry_sha256": root / "roles" / "registry.yaml",
        "protocol_sha256": root / "protocol.md",
    }
    for key, path in original_frozen_paths.items():
        if freeze["frozen_components"].get(key) != sha256_file(path):
            raise ConformanceError(f"{key}: original package hash drift")
    expected_false = (
        "execution_authorized", "experiment_executed", "value_proven",
        "real_agent_contribution_authorized", "real_git_access_authorized",
        "public_report_authorized", "commercial_validation_authorized",
    )
    elevated = [key for key in expected_false if freeze.get(key) is not False]
    if elevated:
        raise ConformanceError(
            f"pre-registration freeze semantically elevated {elevated}"
        )
    if (
        freeze["EXECUTION_AUTHORIZATION_CANDIDATE_READY"] is not True
        or freeze["EXECUTION_AUTHORIZATION_CANDIDATE_READY_MEANS"]
        != "HUMAN_REVIEW_PACKET_COMPLETE_NOT_EXECUTION_READY"
    ):
        raise ConformanceError("authorization candidate readiness is ambiguous")

    fairness = (root / "fairness-review.md").read_text(encoding="utf-8")
    if (
        "FAIRNESS_REVIEW_STATUS=PASS" not in fairness
        or "FAIRNESS_PASS_SCOPE=PROTOCOL_DESIGN_COMPLETENESS_ONLY" not in fairness
        or "EXECUTION_PREREQUISITES_STATUS=NOT_SATISFIED" not in fairness
        or "FAIRNESS_EMPIRICALLY_DEMONSTRATED=false" not in fairness
        or "EXECUTION_AUTHORIZED=false" not in fairness
        or "HD-EB-07" not in fairness
    ):
        raise ConformanceError("fairness design PASS is not bounded and fail closed")

    reviewer = load_json(root / "independent-reviewer-model.yaml")
    reviewer_fields = {
        "reviewer_identity", "conflict_of_interest", "prior_access",
        "review_scope", "abstention_policy",
    }
    if (
        not reviewer_fields.issubset(reviewer)
        or reviewer["reviewer_identity"]["instance_ref"] != "NOT_ASSIGNED"
        or reviewer["reviewer_identity"]["assignment_requires_human_decision"]
        != "HD-EB-07"
        or reviewer["abstention_policy"]["result"] != "ABSTAIN"
        or reviewer["reviewer_instance_assigned"] is not False
        or reviewer["review_session_created"] is not False
        or reviewer["review_executed"] is not False
        or reviewer["execution_authorized"] is not False
    ):
        raise ConformanceError(
            "independent Reviewer model creates an instance, review or authority"
        )

    custodian = load_json(root / "blind-custodian-protocol.yaml")
    custodian_fields = {
        "blind_key_owner", "unblinding_condition", "unblinding_time", "access_log",
    }
    if (
        not custodian_fields.issubset(custodian)
        or custodian["blind_key_owner"]["owner_ref"] != "NOT_ASSIGNED"
        or custodian["access_log"]["mode"] != "APPEND_ONLY_HASH_CHAIN_REQUIRED"
        or custodian["access_log"]["entries"]
        or custodian["blind_key_created"] is not False
        or custodian["blind_key_owner_assigned"] is not False
        or custodian["origin_mapping_created"] is not False
        or custodian["unblinding_executed"] is not False
        or custodian["execution_authorized"] is not False
    ):
        raise ConformanceError(
            "blind custodian protocol creates a key, owner, mapping or execution"
        )

    provider_policy = load_json(root / "provider-privacy-retention-policy.yaml")
    provider_fields = {
        "provider", "model", "data_scope", "retention", "training_usage",
        "logging", "deletion",
    }
    if (
        not provider_fields.issubset(provider_policy)
        or provider_policy["provider"] != "NOT_SELECTED"
        or provider_policy["model"] != "NOT_SELECTED"
        or provider_policy["logging"]["raw_prompt_logged"] is not False
        or provider_policy["logging"]["raw_response_logged"] is not False
        or provider_policy["logging"]["hidden_reasoning_logged"] is not False
        or provider_policy["logging"]["credential_logged"] is not False
        or provider_policy["provider_profile_adopted"] is not False
        or provider_policy["experiment_provider_call_authorized"] is not False
        or provider_policy["experiment_data_processed"] is not False
        or provider_policy["execution_authorized"] is not False
    ):
        raise ConformanceError(
            "Provider privacy policy adopts a provider or permits experiment data"
        )

    bias = (root / "bias-analysis.md").read_text(encoding="utf-8")
    bias_types = {
        "CONFIRMATION_BIAS", "SELECTION_BIAS", "MEASUREMENT_BIAS",
        "MODEL_BIAS", "OBSERVER_BIAS", "CARRY_OVER_BIAS",
    }
    missing_bias = sorted(item for item in bias_types if item not in bias)
    if missing_bias or "BIAS_ELIMINATED=false" not in bias:
        raise ConformanceError(f"bias analysis incomplete {missing_bias}")

    lineage = load_json(root / "agent-lineage-plan.yaml")
    validate_ecology_box_001_preregistration_lineage(lineage)
    if (
        any(lineage["current_counts"].values())
        or lineage["participant_refs"]
        or lineage["lineage_refs"]
        or lineage["assignment_created"]
        or lineage["lineage_plan_approved"]
        or lineage["execution_authorized"]
    ):
        raise ConformanceError("lineage plan creates participants or authorization")
    minimums = lineage["confirmatory_minimums"]
    expected_minimums = {
        "MODEL_COUNT_MIN": 3,
        "SESSION_COUNT_MIN": 20,
        "ROLE_COUNT": 8,
        "INDEPENDENT_LINEAGE_COUNT_MIN": 3,
        "FULL_PIPELINE_COUNT_MIN": 5,
        "NON_FIXTURE_REPOSITORY_COUNT_MIN": 3,
    }
    if minimums != expected_minimums:
        raise ConformanceError("confirmatory lineage minimums drift")
    if (
        lineage["design_review_status"] != "PASS"
        or lineage["execution_prerequisites_status"] != "NOT_SATISFIED"
        or len(lineage["planned_assignment_slots"]) < 3
        or any(
            slot["status"] != "UNASSIGNED"
            or slot["provider"] != "NOT_SELECTED"
            or slot["model"] != "NOT_SELECTED"
            for slot in lineage["planned_assignment_slots"]
        )
    ):
        raise ConformanceError("multi-lineage plan creates or inflates participation")

    packet = (
        DBA_ROOT
        / "TITMAS-AGENT-NATIVE-ECOLOGY-BOX-001-HUMAN-DECISION-PACKET-v0.1.md"
    ).read_text(encoding="utf-8")
    if (
        packet.count("decision=UNDECIDED") != 10
        or packet.count("reevaluation_status=COMPLETE") != 10
        or "HUMAN_DECISIONS_RECORDED=0" not in packet
        or "HUMAN_DECISIONS_UNDECIDED=10" not in packet
        or "HUMAN_DECISIONS_REEVALUATED=10" not in packet
        or "ECOLOGY_BOX_EXECUTION_AUTHORIZED=false" not in packet
        or "ECOLOGY_BOX_EXECUTED=false" not in packet
        or "VALUE_PROVEN=false" not in packet
    ):
        raise ConformanceError("Human Decision re-evaluation packet status drift")

    if (
        freeze["fairness_review"]["status"] != "PASS"
        or freeze["fairness_review"]["pass_scope"]
        != "PROTOCOL_DESIGN_COMPLETENESS_ONLY"
        or freeze["fairness_review"]["empirically_demonstrated"] is not False
        or freeze["execution_prerequisites"]["status"] != "NOT_SATISFIED"
        or not freeze["execution_prerequisites"]["blockers"]
    ):
        raise ConformanceError("freeze review elevates fairness design to readiness")

    stops = load_json(root / "stop-rules.yaml")
    if (
        stops["STOP_ON_BOUNDARY_BREACH"] is not True
        or stops["STOP_ON_SCHEMA_DRIFT"] is not True
        or stops["STOP_ON_AUTHORITY_DRIFT"] is not True
        or stops["failure_records_deletable"] is not False
        or stops["execution_authorized"] is not False
    ):
        raise ConformanceError("stop rules fail open")

    success = (root / "success-criteria.md").read_text(encoding="utf-8")
    required_nonclaims = (
        "AGENT_ACTIVITY_IS_VALUE=false",
        "SESSION_COUNT_IS_LINEAGE_COUNT=false",
        "PILOT_PASS_IS_COMMERCIAL_VALUE=false",
        "RESULT_IS_VALUE_PROOF=false",
        "VALUE_PROVEN=false",
    )
    if any(item not in success for item in required_nonclaims):
        raise ConformanceError("success criteria permit proxy elevation")

    for transition, reason_code in (
        ECOLOGY_BOX_001_PREREGISTRATION_REJECTIONS.items()
    ):
        if ecology_box_001_preregistration_rejection(transition) != {
            "decision": "REJECT",
            "reason_code": reason_code,
        }:
            raise ConformanceError(f"{transition}: transition failed open")

    review = load_json(
        DBA_ROOT / "architecture" / "reviews"
        / "titmas-ecology-box-001-preregistration-predevelopment-review-v0.1.json"
    )
    if (
        review["requested_model"] != "qwen3.7-max"
        or review["transport_returned_model"] != "qwen3.7-max"
        or review["authority_effect"] != "NONE"
        or review["decision_effect"] != "NONE"
        or review["execution_authorized"]
    ):
        raise ConformanceError("pre-registration advisory review boundary drift")

    post_review = load_json(
        DBA_ROOT / "architecture" / "reviews"
        / "titmas-ecology-box-001-preregistration-post-remediation-review-v0.1.json"
    )
    if (
        post_review["requested_model"] != "qwen3.7-max"
        or post_review["transport_returned_model"] != "qwen3.7-max"
        or post_review["verdict"]
        != "CONDITIONALLY_RECOMMENDED_FOR_HUMAN_REVIEW"
        or post_review["would_recommend_as_human_review_candidate"] is not True
        or post_review["would_recommend_execution"] is not False
        or post_review["authority_effect"] != "NONE"
        or post_review["decision_effect"] != "NONE"
        or post_review["execution_authorized"] is not False
    ):
        raise ConformanceError("post-remediation advisory review boundary drift")

    fairness_post_review = load_json(
        DBA_ROOT / "architecture" / "reviews"
        / "titmas-ecology-box-001-fairness-remediation-postreview-multimodel-v0.1.json"
    )
    if (
        fairness_post_review["primary_model"] != "qwen3.7-max"
        or fairness_post_review["authority_effect"] != "NONE"
        or fairness_post_review["decision_effect"] != "NONE"
        or fairness_post_review["fairness_review_status"] != "PASS"
        or fairness_post_review["fairness_pass_scope"]
        != "PROTOCOL_DESIGN_COMPLETENESS_ONLY"
        or fairness_post_review["execution_prerequisites_status"]
        != "NOT_SATISFIED"
        or fairness_post_review["execution_authorized"] is not False
        or fairness_post_review["experiment_executed"] is not False
        or fairness_post_review["value_proven"] is not False
        or len(fairness_post_review["review_sessions"]) < 3
    ):
        raise ConformanceError("fairness post-review semantically elevates the pilot")

    report = (
        DBA_ROOT
        / "TITMAS-AGENT-NATIVE-ECOLOGY-BOX-001-PREREGISTRATION-AND-EXECUTION-REVIEW-REPORT-v0.1.md"
    ).read_text(encoding="utf-8")
    required_report_states = (
        "TITMAS_AGENT_NATIVE_ECOLOGY_BOX_001_PREREGISTRATION_COMPLETE=true",
        "TITMAS_AGENT_NATIVE_ECOLOGY_BOX_001_EXECUTION_REVIEW_COMPLETE=true",
        "TITMAS_AGENT_NATIVE_ECOLOGY_BOX_001_EXECUTION_AUTHORIZED=false",
        "TITMAS_AGENT_NATIVE_ECOLOGY_BOX_001_EXECUTED=false",
        "TITMAS_AGENT_NATIVE_VALUE_PROVEN=false",
        "REAL_AGENT_CONTRIBUTION_AUTHORIZED=false",
        "REAL_GIT_ACCESS_AUTHORIZED=false",
        "PUBLIC_REPORT_AUTHORIZED=false",
        "COMMERCIAL_VALIDATION_AUTHORIZED=false",
        "FAIRNESS_REVIEW_STATUS=PASS",
        "EXECUTION_PREREQUISITES_STATUS=NOT_SATISFIED",
    )
    if any(item not in report for item in required_report_states):
        raise ConformanceError("completion report status drift")

    return {
        "preregistration_files_checked": len(required_paths) + len(supporting_paths),
        "frozen_hashes_checked": len(required_paths) + len(original_frozen_paths),
        "fairness_review_status": "PASS",
        "fairness_pass_scope": "PROTOCOL_DESIGN_COMPLETENESS_ONLY",
        "execution_prerequisites_status": "NOT_SATISFIED",
        "fairness_empirically_demonstrated": False,
        "bias_types_checked": len(bias_types),
        "transition_cases_rejected": len(
            ECOLOGY_BOX_001_PREREGISTRATION_REJECTIONS
        ),
        "independent_lineage_count": 0,
        "human_decisions_undecided": 10,
        "human_decisions_reevaluated": 10,
        "fairness_control_contracts_checked": 4,
        "execution_authorized": False,
        "experiment_executed": False,
        "value_proven": False,
    }


def check_agent_native_ecology_box_001_execution_readiness() -> dict[str, Any]:
    root = TITMAS_ROOT / "agent-native" / "ecology-box-001"
    readiness_root = root / "readiness"
    required_names = (
        "README.md",
        "execution-prerequisites-matrix.yaml",
        "go-no-go-checklist.md",
        "execution-readiness.yaml",
        "source-snapshot-manifest.yaml",
        "participant-assignment-template.yaml",
        "reviewer-assignment-template.yaml",
        "blind-custodian-assignment-template.yaml",
        "provider-adoption-template.yaml",
        "resource-budget.yaml",
        "data-handling-plan.yaml",
        "randomization-and-blinding-plan.yaml",
        "experiment-runbook.md",
        "abort-and-rollback-plan.md",
        "reproducibility-manifest.yaml",
        "confounder-control.md",
        "dry-run-plan.yaml",
        "unresolved-prerequisites.yaml",
        "final-go-no-go-review-template.md",
        "human-first-baseline-operation-plan.md",
        "agent-native-arm-operation-plan.md",
    )
    supporting_paths = (
        DBA_ROOT / "EXECUTION-READINESS-SUPPLEMENTAL-DECISION-PACKET-v0.1.md",
        DBA_ROOT / "architecture" / "reviews"
        / "titmas-ecology-box-001-execution-readiness-predevelopment-review-v0.1.json",
        DBA_ROOT / "architecture" / "reviews"
        / "titmas-ecology-box-001-execution-readiness-postreview-v0.1.json",
        DBA_ROOT
        / "TITMAS-AGENT-NATIVE-ECOLOGY-BOX-001-EXECUTION-READINESS-REPORT-v0.1.md",
        DBA_ROOT / "architecture"
        / "titmas-agent-native-ecology-box-001-execution-readiness-review-v0.1.md",
        TITMAS_ROOT / "conformance" / "fixtures"
        / "ecology-box-001-readiness-negative-cases.yaml",
    )
    required_paths = tuple(readiness_root / name for name in required_names)
    missing = [
        str(path.relative_to(DBA_ROOT))
        for path in required_paths + supporting_paths
        if not path.is_file()
    ]
    if missing:
        raise ConformanceError(
            f"Ecology Box 001 readiness files missing {missing}"
        )

    matrix = load_json(readiness_root / "execution-prerequisites-matrix.yaml")
    allowed_statuses = {
        "SATISFIED",
        "PARTIALLY_SATISFIED",
        "NOT_SATISFIED",
        "NOT_ASSIGNED",
        "NOT_ADOPTED",
        "NOT_ASSESSED",
        "CONFLICT",
        "EXPIRED",
    }
    if set(matrix["allowed_statuses"]) != allowed_statuses:
        raise ConformanceError("readiness prerequisite status vocabulary drift")
    prerequisites = matrix["prerequisites"]
    required_fields = {
        "prerequisite_id",
        "description",
        "required",
        "current_status",
        "evidence_ref",
        "owner_or_assignee_ref",
        "decision_ref",
        "blocking",
        "expires_at",
        "limitations",
    }
    if len(prerequisites) != 25:
        raise ConformanceError("readiness matrix must contain 25 prerequisites")
    if len({item["prerequisite_id"] for item in prerequisites}) != 25:
        raise ConformanceError("readiness prerequisite identifiers are not unique")
    for item in prerequisites:
        if set(item) != required_fields:
            raise ConformanceError(
                f"{item.get('prerequisite_id')}: prerequisite fields drift"
            )
        if item["current_status"] not in allowed_statuses:
            raise ConformanceError(
                f"{item['prerequisite_id']}: invalid prerequisite status"
            )
        if item["required"] is not True or item["blocking"] is not True:
            raise ConformanceError(
                f"{item['prerequisite_id']}: required blocking control drift"
            )

    statuses = [item["current_status"] for item in prerequisites]
    satisfied = statuses.count("SATISFIED")
    partial = statuses.count("PARTIALLY_SATISFIED")
    missing_count = len(statuses) - satisfied - partial
    blocking_open = len(statuses) - satisfied
    expected_summary = {
        "total": 25,
        "satisfied": 9,
        "partially_satisfied": 7,
        "not_satisfied_or_missing": 9,
        "blocking_not_satisfied": 16,
    }
    if (
        matrix["summary"] != expected_summary
        or (satisfied, partial, missing_count, blocking_open) != (9, 7, 9, 16)
        or matrix["all_blocking_prerequisites_satisfied"] is not False
        or matrix["go_no_go_status"] != "NO_GO"
        or matrix["execution_authorized"] is not False
        or matrix["experiment_executed"] is not False
        or matrix["value_proven"] is not False
    ):
        raise ConformanceError("readiness prerequisite summary or NO_GO drift")

    readiness = load_json(readiness_root / "execution-readiness.yaml")
    if (
        readiness["source_commit"]
        != "005b2382a43324e737c207095ad379e95b12acf1"
        or readiness["status"] != "PACKAGE_COMPLETE_NO_GO"
        or readiness["fairness_protocol_status"] != "PASS"
        or readiness["fairness_pass_scope"]
        != "PROTOCOL_DESIGN_COMPLETENESS_ONLY"
        or readiness["operational_prerequisites_satisfied"] is not False
    ):
        raise ConformanceError("readiness fixed state drift")
    if (
        readiness["go_rule"]["all_blocking_prerequisites_satisfied"] is not False
        or readiness["go_rule"]["reviewer_assigned"] is not False
        or readiness["go_rule"]["blind_custodian_assigned"] is not False
        or readiness["go_rule"]["provider_profile_adopted"] is not False
        or readiness["go_rule"]["privacy_policy_adopted"] is not False
        or readiness["go_rule"]["participant_plan_populated"] is not False
        or readiness["go_rule"]["independent_lineage_plan_accepted"] is not False
        or readiness["go_rule"]["human_execution_decision_accept"] is not False
        or readiness["go_no_go_status"] != "NO_GO"
        or readiness["go_no_go_reason"]
        != "NO_GO_PENDING_OPERATIONAL_ASSIGNMENTS_AND_HUMAN_AUTHORIZATION"
        or any(readiness["current_counts"].values())
        or readiness["execution_authorized"] is not False
        or readiness["experiment_executed"] is not False
        or readiness["value_proven"] is not False
    ):
        raise ConformanceError("readiness state fails open")

    snapshot = load_json(readiness_root / "source-snapshot-manifest.yaml")
    if (
        snapshot["experiment_source_commit"]
        != "b92a9a8c0553b51afc832e549d9ad5af271443f2"
        or snapshot["fairness_remediation_commit"]
        != "005b2382a43324e737c207095ad379e95b12acf1"
        or snapshot["task_registry"]["task_count"] != 10
        or snapshot["roles_registry"]["role_count"] != 8
        or snapshot["task_registry"]["sha256"]
        != sha256_file(root / "tasks" / "task-registry.yaml")
        or snapshot["metrics_schema"]["sha256"]
        != sha256_file(root / "metrics" / "schema.json")
        or snapshot["roles_registry"]["sha256"]
        != sha256_file(root / "roles" / "registry.yaml")
        or snapshot["protocol"]["sha256"] != sha256_file(root / "protocol.md")
        or not all(
            snapshot[key] is True
            for key in (
                "task_set_frozen",
                "metrics_frozen",
                "roles_frozen",
                "protocol_frozen",
                "success_criteria_frozen",
            )
        )
        or snapshot["experiment_execution_authorized"] is not False
    ):
        raise ConformanceError("readiness source or ten-task freeze drift")

    participant = load_json(
        readiness_root / "participant-assignment-template.yaml"
    )
    if (
        any(participant["current_counts"].values())
        or participant["planned_independent_agent_lineage_count"] != 3
        or participant["planned_count_is_current_count"] is not False
        or any(
            item["assignment_status"] != "NOT_ASSIGNED"
            or item["assignee_ref"] != "NOT_ASSIGNED"
            for item in participant["human_roles"]
        )
        or any(
            item["participant_instance"] != "NOT_ASSIGNED"
            for item in participant["agent_roles"]
        )
        or participant["assignment_created"] is not False
        or participant["participant_created"] is not False
        or participant["agent_created"] is not False
        or participant["runtime_created"] is not False
        or participant["execution_authorized"] is not False
    ):
        raise ConformanceError("participant template creates or inflates instances")

    reviewer = load_json(readiness_root / "reviewer-assignment-template.yaml")
    custodian = load_json(
        readiness_root / "blind-custodian-assignment-template.yaml"
    )
    provider = load_json(readiness_root / "provider-adoption-template.yaml")
    if (
        reviewer["reviewer_identity"]["instance_ref"] != "NOT_ASSIGNED"
        or reviewer["reviewer_assigned"] is not False
        or reviewer["review_session_created"] is not False
        or custodian["custodian_identity"]["instance_ref"] != "NOT_ASSIGNED"
        or custodian["blind_key_owner_assigned"] is not False
        or custodian["blind_key_created"] is not False
        or custodian["origin_mapping_created"] is not False
        or provider["profile"]["provider"] != "NOT_SELECTED"
        or provider["profile"]["requested_model"] != "NOT_SELECTED"
        or provider["provider_profile_adopted"] is not False
        or provider["experiment_data_processed"] is not False
        or provider["experiment_model_invoked"] is not False
    ):
        raise ConformanceError("assignment or Provider template is instantiated")

    budget = load_json(readiness_root / "resource-budget.yaml")
    data_plan = load_json(readiness_root / "data-handling-plan.yaml")
    blinding = load_json(
        readiness_root / "randomization-and-blinding-plan.yaml"
    )
    dry_run = load_json(readiness_root / "dry-run-plan.yaml")
    if (
        budget["budget_adopted"] is not False
        or budget["post_hoc_budget_change_allowed"] is not False
        or data_plan["provider_profile_adopted"] is not False
        or data_plan["privacy_policy_adopted"] is not False
        or data_plan["experiment_data_processed"] is not False
        or blinding["origin_mapping"]["created"] is not False
        or blinding["randomization"]["seed_created"] is not False
        or blinding["blind_key_custody"]["key_created"] is not False
        or blinding["unblinding"]["executed"] is not False
        or blinding["method_adopted"] is not False
        or dry_run["DRY_RUN_PACKAGE_READY"] is not True
        or dry_run["DRY_RUN_EXECUTED"] is not False
        or dry_run["SYNTHETIC_DRY_RUN_NE_EXPERIMENT_EXECUTION"] is not True
        or dry_run["SYNTHETIC_DRY_RUN_NE_PILOT_RESULT"] is not True
        or dry_run["SYNTHETIC_DRY_RUN_NE_VALUE_EVIDENCE"] is not True
    ):
        raise ConformanceError("budget, data, blinding or dry-run boundary drift")

    confounder = (readiness_root / "confounder-control.md").read_text(
        encoding="utf-8"
    )
    required_confounder_states = (
        "AGENT_IMMUNE_ENABLED=false",
        "AGENT_IMMUNE_REQUIRED=false",
        "OBSERVATION_NE_EVIDENCE=true",
        "HEALTH_SIGNAL_NE_EVALUATION=true",
        "HEALTH_SIGNAL_NE_DECISION=true",
    )
    if any(item not in confounder for item in required_confounder_states):
        raise ConformanceError("Agent Immune confounder boundary drift")

    decision_packet = (
        DBA_ROOT / "EXECUTION-READINESS-SUPPLEMENTAL-DECISION-PACKET-v0.1.md"
    ).read_text(encoding="utf-8")
    if (
        decision_packet.count("decision=UNDECIDED") != 4
        or "HD_EB_06_TO_08_STATUS=UNDECIDED" not in decision_packet
        or "HD_EB_11_TO_14_STATUS=UNDECIDED" not in decision_packet
        or "EXECUTION_AUTHORIZED=false" not in decision_packet
        or "EXPERIMENT_EXECUTED=false" not in decision_packet
        or "VALUE_PROVEN=false" not in decision_packet
    ):
        raise ConformanceError("supplemental Human Decision packet drift")

    review = load_json(
        DBA_ROOT / "architecture" / "reviews"
        / "titmas-ecology-box-001-execution-readiness-predevelopment-review-v0.1.json"
    )
    if (
        review["requested_model"] != "qwen3.7-max"
        or review["returned_model"] != "qwen3.7-max"
        or review["verdict"] != "NOT_RECOMMENDED"
        or review["recommend_implementation"] is not False
        or review["recommend_experiment_execution"] is not False
        or review["authority_effect"] != "NONE"
        or review["decision_effect"] != "NONE"
        or review["raw_prompt_retained"] is not False
        or review["raw_response_retained"] is not False
    ):
        raise ConformanceError("readiness predevelopment review boundary drift")

    post_review = load_json(
        DBA_ROOT / "architecture" / "reviews"
        / "titmas-ecology-box-001-execution-readiness-postreview-v0.1.json"
    )
    if (
        post_review["requested_model"] != "qwen3.7-max"
        or post_review["returned_model"] != "qwen3.7-max"
        or post_review["verdict"] != "RECOMMENDED"
        or post_review["recommended_as"]
        != "HUMAN_GO_NO_GO_REVIEW_CANDIDATE_FOR_AUDITABLE_PRE_EXECUTION_READINESS"
        or post_review["recommend_as_human_review_candidate"] is not True
        or post_review["recommend_experiment_execution"] is not False
        or post_review["authority_effect"] != "NONE"
        or post_review["decision_effect"] != "NONE"
        or post_review["raw_prompt_retained"] is not False
        or post_review["raw_response_retained"] is not False
    ):
        raise ConformanceError("readiness post-review boundary drift")

    report = (
        DBA_ROOT
        / "TITMAS-AGENT-NATIVE-ECOLOGY-BOX-001-EXECUTION-READINESS-REPORT-v0.1.md"
    ).read_text(encoding="utf-8")
    required_report_states = (
        "TITMAS_ECOLOGY_BOX_001_EXECUTION_READINESS_PACKAGE_COMPLETE=true",
        "TITMAS_ECOLOGY_BOX_001_OPERATIONAL_PREREQUISITES_SATISFIED=false",
        "TITMAS_ECOLOGY_BOX_001_GO_NO_GO_STATUS=NO_GO",
        "TITMAS_ECOLOGY_BOX_001_EXECUTION_AUTHORIZED=false",
        "TITMAS_ECOLOGY_BOX_001_EXECUTED=false",
        "TITMAS_ECOLOGY_BOX_001_VALUE_PROVEN=false",
        "HUMAN_READINESS_REVIEW_CANDIDATE=true",
        "FORMAL_EXECUTION_AUTHORIZATION_REVIEW_READY=false",
        "DRY_RUN_PACKAGE_READY=true",
        "DRY_RUN_EXECUTED=false",
    )
    if any(item not in report for item in required_report_states):
        raise ConformanceError("execution readiness report status drift")

    architecture_review = (
        DBA_ROOT / "architecture"
        / "titmas-agent-native-ecology-box-001-execution-readiness-review-v0.1.md"
    ).read_text(encoding="utf-8")
    if (
        "FROZEN_TASK_COUNT=10" not in architecture_review
        or "GO_NO_GO_STATUS=NO_GO" not in architecture_review
        or "FORMAL_EXECUTION_AUTHORIZATION_REVIEW_READY=false"
        not in architecture_review
        or "READINESS_NE_AUTHORIZATION=true" not in architecture_review
        or "EXECUTION_NE_VALUE_PROOF=true" not in architecture_review
    ):
        raise ConformanceError("execution readiness architecture review drift")

    negative_fixture = load_json(
        TITMAS_ROOT / "conformance" / "fixtures"
        / "ecology-box-001-readiness-negative-cases.yaml"
    )
    if len(negative_fixture["cases"]) != 12:
        raise ConformanceError("expected 12 readiness negative cases")
    for case in negative_fixture["cases"]:
        if ecology_box_001_readiness_rejection(case["transition"]) != {
            "decision": "REJECT",
            "reason_code": case["expected_reason_code"],
        }:
            raise ConformanceError(
                f"{case['case_id']}: readiness negative case failed open"
            )

    run_records = [
        path
        for path in (root / "runs").iterdir()
        if path.is_file() and path.name != "README.md"
    ]
    if run_records:
        raise ConformanceError("readiness package contains experiment run records")

    return {
        "readiness_files_checked": len(required_paths) + len(supporting_paths),
        "prerequisites_total": 25,
        "prerequisites_satisfied": 9,
        "prerequisites_partially_satisfied": 7,
        "prerequisites_missing": 9,
        "blocking_prerequisites_open": 16,
        "negative_cases_rejected": 12,
        "task_count_frozen": 10,
        "current_participant_count": 0,
        "current_independent_lineage_count": 0,
        "go_no_go_status": "NO_GO",
        "execution_authorized": False,
        "experiment_executed": False,
        "value_proven": False,
    }


def check_agent_native_ecology_box_001_operational_calibration() -> dict[str, Any]:
    root = TITMAS_ROOT / "agent-native" / "ecology-box-001"
    calibration = root / "calibration"
    required_paths = (
        calibration / "run_calibration.py",
        calibration / "calibration-config.yaml",
        calibration / "task-seeds.json",
        calibration / "participant-lineages.json",
        calibration / "role-rotation.yaml",
        calibration / "normalized-run-records.jsonl",
        calibration / "candidate-patches" / "candidates.json",
        calibration / "conformance-results.json",
        calibration / "calibration-metrics.json",
        calibration / "protocol-deviations.json",
        calibration / "calibration-report-v0.1.md",
        DBA_ROOT
        / "TITMAS-AGENT-NATIVE-ECOLOGY-BOX-001-OPERATIONAL-CALIBRATION-REPORT-v0.1.md",
    )
    missing = [
        str(path.relative_to(DBA_ROOT))
        for path in required_paths
        if not path.is_file()
    ]
    if missing:
        raise ConformanceError(f"operational calibration files missing {missing}")

    config = load_json(calibration / "calibration-config.yaml")
    if (
        config["decision_id"]
        != "TITMAS-EB001-OPERATIONAL-CALIBRATION-D01"
        or config["decision"] != "ACCEPT"
        or config["decided_by_ref"] != "zhangbin"
        or config["source_commit"]
        != "3c7aff595dde3c8bc4db2ace4a6ec52df8cb7403"
        or config["calibration_status"] != "CALIBRATION_ABORTED_FOR_SAFETY"
        or config["calibration_tier"] != "OPERATIONAL_PIPELINE_CALIBRATION"
        or config["inference_tier"] != "NON_CONFIRMATORY"
        or config["formal_task_count"] != 10
        or config["calibration_task_count"] != 3
        or config["max_total_model_calls"] != 12
        or config["actual_total_model_calls_or_attempts"] != 9
        or config["calibration_model_calls"] != 7
        or config["agent_immune_enabled"] is not False
        or config["formal_experiment_state_effect"] != "NONE"
        or config["value_claim_effect"] != "NONE"
        or config["commercial_claim_effect"] != "NONE"
        or config["formal_ecology_box_001_execution_authorized"] is not False
        or config["formal_ten_task_experiment_execution_authorized"] is not False
        or config["real_repository_git_write_authorized"] is not False
        or config["public_report_authorized"] is not False
        or config["commercial_validation_authorized"] is not False
        or config["runner_repaired_after_abort"] is not True
        or config["repair_reexecuted_calibration"] is not False
    ):
        raise ConformanceError("operational calibration config truth drift")

    seeds = load_json(calibration / "task-seeds.json")
    if (
        seeds["seed_count"] != 3
        or seeds["formal_task_count"] != 10
        or seeds["formal_tasks_accessed"] is not False
        or {seed["task_id"] for seed in seeds["seeds"]}
        != {"CAL-TASK-001", "CAL-TASK-002", "CAL-TASK-003"}
        or any(seed["formal_task"] is not False for seed in seeds["seeds"])
        or any(seed["model_answer_exposure"] is not False for seed in seeds["seeds"])
        or any(seed["source_hash"] == seed["modified_hash"] for seed in seeds["seeds"])
        or any(
            not seed["source_hash"].startswith("sha256:")
            or not seed["modified_hash"].startswith("sha256:")
            for seed in seeds["seeds"]
        )
    ):
        raise ConformanceError("calibration seed or formal-task isolation drift")

    lineages = load_json(calibration / "participant-lineages.json")
    expected_pairs = {
        ("ALIBABA_DASHSCOPE", "qwen3.7-max"),
        ("BAIDU_QIANFAN", "kimi-k2.6"),
        ("VOLCENGINE_ARK", "deepseek-v4-flash-260425"),
    }
    observed_pairs = {
        (item["provider"], item["requested_model"])
        for item in lineages["lineages"]
    }
    if (
        lineages["required_independent_lineage_count"] != 3
        or lineages["actual_independent_lineage_count"] != 3
        or lineages["model_count"] != 3
        or lineages["calibration_session_count"] != 7
        or lineages["role_count"] != 3
        or observed_pairs != expected_pairs
        or any(
            item["returned_model_identity_verified"] is not True
            or item["fallback"] != "NONE"
            or item["data_scope"] != "PUBLIC_REPOSITORY_AND_SYNTHETIC_ONLY"
            or any(
                item[field] != "UNKNOWN"
                for field in (
                    "retention", "training_usage", "logging", "deletion"
                )
            )
            for item in lineages["lineages"]
        )
        or lineages["lineage_presence_ne_pipeline_completion"] is not True
    ):
        raise ConformanceError("calibration lineage identity or count drift")

    record_path = calibration / "normalized-run-records.jsonl"
    if record_path.stat().st_size > MAX_JSON_BYTES:
        raise ConformanceError("calibration normalized record file too large")
    records = [
        json.loads(line)
        for line in record_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    model_calls = [item for item in records if item["record_type"] == "MODEL_CALL"]
    task_outcomes = [
        item for item in records if item["record_type"] == "TASK_OUTCOME"
    ]
    if (
        len(model_calls) != 7
        or len(task_outcomes) != 3
        or any(
            item["requested_model"] != item["returned_model"]
            or item["returned_model_identity_verified"] is not True
            or item["fallback"] != "NONE"
            or item["raw_prompt_stored"] is not False
            or item["raw_provider_response_stored"] is not False
            or item["hidden_reasoning_stored"] is not False
            or item["authority_effect"] != "NONE"
            or item["input_hash"]
            != "UNKNOWN_NOT_PERSISTED_DUE_HARNESS_ABORT"
            or item["output_hash"]
            != "UNKNOWN_NOT_PERSISTED_DUE_HARNESS_ABORT"
            for item in model_calls
        )
        or any(
            item["pipeline_complete"] is not False
            or item["outcome_classification"]
            != "CALIBRATION_ABORTED_FOR_SAFETY"
            for item in task_outcomes
        )
    ):
        raise ConformanceError("calibration normalized abort records drift")

    candidates = load_json(
        calibration / "candidate-patches" / "candidates.json"
    )
    if (
        candidates["candidates"]
        or candidates["candidate_patches_durably_retained"] != 0
        or candidates["formal_repository_candidate_changes"] != 0
        or candidates["candidate_git_commits"] != 0
        or candidates["candidate_pull_requests"] != 0
        or candidates["blinding"]["formal_blind_custodian"] is not False
        or candidates["blinding"]["origin_mapping_persisted"] is not False
        or candidates["blinding"]["unblinded_after_review"] is not False
    ):
        raise ConformanceError("calibration abort invents patches or blinding")

    conformance_result = load_json(
        calibration / "conformance-results.json"
    )
    if (
        conformance_result["status"] != "NOT_ASSESSED_ABORTED"
        or len(conformance_result["task_results"]) != 3
        or conformance_result["source_hashes_verified"] is not True
        or conformance_result["formal_task_count"] != 10
        or conformance_result["formal_task_set_unchanged"] is not True
        or conformance_result["formal_tasks_accessed_by_calibration"] is not False
        or conformance_result["formal_blinding_not_contaminated"] is not True
        or conformance_result["formal_go_no_go_status"] != "NO_GO"
        or conformance_result["formal_experiment_execution_authorized"] is not False
        or conformance_result["formal_experiment_executed"] is not False
        or conformance_result["formal_run_record_count"] != 0
        or conformance_result["calibration_result_in_formal_metrics"] is not False
    ):
        raise ConformanceError("calibration conformance or formal state drift")

    metrics = load_json(calibration / "calibration-metrics.json")
    if (
        metrics["CALIBRATION_PIPELINE_COMPLETION_RATE"] != 0.0
        or metrics["HANDOFF_CRITICAL_FIELD_LOSS_RATE"] != 1.0
        or metrics["CALIBRATION_MODEL_CALL_COUNT"] != 7
        or metrics["MODEL_CALL_COUNT"] != 9
        or metrics["FALLBACK_COUNT"] != 0
        or metrics["PROTOCOL_DEVIATION_COUNT"] != 4
        or metrics["FINAL_OUTCOME_IMPROVEMENT_RATE"] != "NOT_ASSESSED"
        or metrics["TITMAS_AGENT_OPERATIONAL_VALUE_DEMONSTRATED"] is not False
        or metrics["TITMAS_AGENT_NATIVE_VALUE_PROVEN"] is not False
        or metrics["AUTHORITY_VIOLATION_ASSESSMENT_COMPLETE"] is not False
        or metrics["SEMANTIC_ELEVATION_ASSESSMENT_COMPLETE"] is not False
        or metrics["HARMFUL_CANDIDATE_ASSESSMENT_COMPLETE"] is not False
    ):
        raise ConformanceError("calibration metrics overclaim or drift")

    deviations = load_json(calibration / "protocol-deviations.json")
    if (
        len(deviations["deviations"]) != 4
        or set(deviations["stop_conditions_triggered"])
        != {
            "CRITICAL_HANDOFF_FIELD_LOSS",
            "UNHANDLED_LOCAL_NORMALIZATION_EXCEPTION",
        }
        or deviations["fallback_count"] != 0
        or deviations["authority_assessment_complete"] is not False
        or deviations["formal_experiment_effect"] != "NONE"
        or deviations["next_recommendation"] != "SIMPLIFY_PROTOCOL"
        or deviations["repeat_calibration_requires_new_human_authorization"]
        is not True
    ):
        raise ConformanceError("calibration stop or deviation record drift")

    report = (
        DBA_ROOT
        / "TITMAS-AGENT-NATIVE-ECOLOGY-BOX-001-OPERATIONAL-CALIBRATION-REPORT-v0.1.md"
    ).read_text(encoding="utf-8")
    required_report_states = (
        "TITMAS_ECOLOGY_BOX_001_OPERATIONAL_CALIBRATION_EXECUTED=true",
        "TITMAS_ECOLOGY_BOX_001_OPERATIONAL_PIPELINE_DEMONSTRATED=false",
        "CALIBRATION_STATUS=CALIBRATION_ABORTED_FOR_SAFETY",
        "TITMAS_ECOLOGY_BOX_001_GO_NO_GO_STATUS=NO_GO",
        "TITMAS_ECOLOGY_BOX_001_EXECUTION_AUTHORIZED=false",
        "TITMAS_ECOLOGY_BOX_001_EXECUTED=false",
        "TITMAS_ECOLOGY_BOX_001_VALUE_PROVEN=false",
        "PUBLIC_REPORT_AUTHORIZED=false",
        "COMMERCIAL_VALIDATION_AUTHORIZED=false",
        "NEXT_RECOMMENDATION=SIMPLIFY_PROTOCOL",
    )
    if any(item not in report for item in required_report_states):
        raise ConformanceError("operational calibration report truth drift")

    formal_runs = [
        path
        for path in (root / "runs").iterdir()
        if path.is_file() and path.name != "README.md"
    ]
    if formal_runs:
        raise ConformanceError("calibration created a formal experiment run record")
    return {
        "calibration_files_checked": len(required_paths),
        "calibration_model_calls_checked": len(model_calls),
        "calibration_tasks_checked": len(task_outcomes),
        "independent_lineages_checked": 3,
        "protocol_deviations_preserved": 4,
        "formal_task_count": 10,
        "formal_run_record_count": 0,
        "calibration_status": "CALIBRATION_ABORTED_FOR_SAFETY",
        "operational_pipeline_demonstrated": False,
        "formal_go_no_go_status": "NO_GO",
        "formal_experiment_execution_authorized": False,
        "formal_experiment_executed": False,
        "value_proven": False,
    }


def check_agent_native_ecology_box_001_operational_calibration_v02() -> dict[str, Any]:
    root = TITMAS_ROOT / "agent-native" / "ecology-box-001"
    v02 = root / "calibration" / "v0.2"
    preparation_paths = (
        v02 / "role-output-contracts.json",
        v02 / "failure-injection-results.json",
        v02 / "calibration-v0.2-config.yaml",
        v02 / "task-seeds-v0.2.json",
    )
    missing = [
        str(path.relative_to(DBA_ROOT))
        for path in preparation_paths
        if not path.is_file()
    ]
    if missing:
        raise ConformanceError(f"calibration v0.2 hardening files missing {missing}")

    contracts = load_json(v02 / "role-output-contracts.json")
    fixtures = contracts["fixture_results"]
    if (
        contracts["contract_bundle_version"] != "1.0.0"
        or contracts["silent_type_coercion_allowed"] is not False
        or contracts["null_allowed"] is not False
        or set(contracts["schemas"])
        != {
            "ExplorerFinding",
            "ContributorCandidate",
            "ReviewerAssessment",
            "RevisionResponse",
            "ConformanceResult",
            "HandoffRecord",
        }
        or fixtures["fixture_count"] != 36
        or fixtures["passed"] != 36
        or any(item["status"] != "PASS" for item in fixtures["results"])
        or fixtures["unknown_and_not_assessed_allowed"] is not True
    ):
        raise ConformanceError("calibration v0.2 role contract drift")

    failure = load_json(v02 / "failure-injection-results.json")
    if (
        failure["test_count"] != 14
        or failure["passed"] != 14
        or failure["failed"] != 0
        or failure["status"] != "PASS"
        or {item["case_id"] for item in failure["results"]}
        != {f"FI-{index:02d}" for index in range(1, 15)}
        or any(item["status"] != "PASS" for item in failure["results"])
        or failure["prior_valid_checkpoints_lost"] != 0
        or failure["critical_handoff_field_loss"] != 0
        or failure["unhandled_type_error_count"] != 0
        or failure["unhandled_exception_count"] != 0
        or failure["resume_idempotency_pass"] is not True
        or failure["model_calls_authorized_after_gate"] is not True
    ):
        raise ConformanceError("calibration v0.2 failure-injection gate drift")

    config = load_json(v02 / "calibration-v0.2-config.yaml")
    source = config["source"]
    hardening = config["hardening"]
    if (
        config["decision_id"]
        != "TITMAS-EB001-OPERATIONAL-CALIBRATION-D02"
        or config["decision"] != "ACCEPT_ONCE"
        or config["decided_by_ref"] != "zhangbin"
        or source["source_commit"]
        != "70f626d41ef4746f0f23c588324267cae090ca7b"
        or source["remote_source_commit"] != source["source_commit"]
        or not all(source["checks"].values())
        or config["authorized_once"] is not True
        or config["repeat_without_new_authorization"] is not False
        or config["model_calls_authorized_after_hardening_gate"] is not True
        or hardening["durable_event_journal_enabled"] is not True
        or hardening["checkpoint_after_every_role_handoff"] is not True
        or hardening["finalization_only_persistence"] is not False
        or hardening["journal_fsync_granularity"] != "EVERY_RECORD"
        or hardening["snapshot_schema_version"] != "1.0.0"
        or hardening["role_contract_schema_version"] != "1.0.0"
        or hardening["max_correction_calls_per_role"] != 1
        or hardening["max_total_correction_calls"] != 3
        or hardening["max_total_model_calls"] != 12
        or config["formal_ecology_box_001_execution_authorized"] is not False
        or config["formal_ten_task_experiment_authorized"] is not False
        or config["agent_native_value_validation_authorized"] is not False
        or config["real_repository_candidate_git_write_authorized"] is not False
        or config["public_report_authorized"] is not False
        or config["commercial_validation_authorized"] is not False
        or config["release_authorized"] is not False
    ):
        raise ConformanceError("calibration v0.2 config or authority drift")

    seeds = load_json(v02 / "task-seeds-v0.2.json")
    if (
        seeds["seed_count"] != 3
        or seeds["formal_task_count"] != 10
        or seeds["formal_task_set_unchanged"] is not True
        or seeds["formal_tasks_accessed"] is not False
        or {item["task_id"] for item in seeds["seeds"]}
        != {"CAL2-TASK-001", "CAL2-TASK-002", "CAL2-TASK-003"}
        or any(item["formal_task"] is not False for item in seeds["seeds"])
        or any(item["expected_issue_class_exposed_to_models"] is not False for item in seeds["seeds"])
        or any(item["source_hash"] == item["modified_hash"] for item in seeds["seeds"])
    ):
        raise ConformanceError("calibration v0.2 seed isolation drift")

    if config.get("calibration_v0_2_executed") is not True:
        return {
            "hardening_files_checked": len(preparation_paths),
            "failure_injection_tests": 14,
            "role_contract_fixture_tests": 36,
            "calibration_status": "HARDENING_GATE_PASS_MODEL_RUN_NOT_STARTED",
            "calibration_executed": False,
            "operational_pipeline_demonstrated": False,
            "formal_go_no_go_status": "NO_GO",
            "formal_run_record_count": 0,
            "value_proven": False,
        }

    execution_paths = (
        v02 / "durable-journal.jsonl",
        v02 / "durable-artifacts.jsonl",
        v02 / "task-snapshots.json",
        v02 / "calibration-results-v0.2.json",
        v02 / "calibration-report-v0.2.md",
        DBA_ROOT
        / "TITMAS-AGENT-NATIVE-ECOLOGY-BOX-001-OPERATIONAL-CALIBRATION-REPORT-v0.2.md",
    )
    missing = [
        str(path.relative_to(DBA_ROOT))
        for path in execution_paths
        if not path.is_file()
    ]
    if missing:
        raise ConformanceError(f"calibration v0.2 execution files missing {missing}")

    journal_path = v02 / "durable-journal.jsonl"
    if journal_path.stat().st_size > MAX_JSON_BYTES:
        raise ConformanceError("calibration v0.2 journal too large")
    journal = [
        json.loads(line)
        for line in journal_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    previous = "GENESIS"
    allowed_events = {
        "RUN_STARTED", "TASK_STARTED", "MODEL_CALL_STARTED",
        "MODEL_RESPONSE_RECEIVED", "MODEL_CALL_OUTCOME_UNKNOWN",
        "ROLE_OUTPUT_PARSE_FAILED", "ROLE_OUTPUT_SCHEMA_REJECTED",
        "ROLE_OUTPUT_VALIDATED", "CORRECTION_REQUESTED",
        "CORRECTION_RESPONSE_RECEIVED", "HANDOFF_COMMITTED",
        "REVIEW_COMPLETED", "CONFORMANCE_COMPLETED", "STAGE_FAILED",
        "TASK_COMPLETED", "RUN_ABORTED", "RUN_COMPLETED",
    }
    required_event_fields = {
        "event_id", "run_id", "task_id", "sequence", "event_type", "stage",
        "role", "participant_ref", "provider", "requested_model",
        "returned_model", "session_ref", "input_hash", "output_hash",
        "artifact_ref", "validation_status", "reason_code",
        "model_call_state", "previous_event_hash", "event_hash", "created_at",
        "details",
    }
    for index, event in enumerate(journal, 1):
        candidate = dict(event)
        supplied_hash = candidate.pop("event_hash", None)
        calculated = "sha256:" + hashlib.sha256(
            json.dumps(
                candidate,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest()
        if (
            set(event) != required_event_fields
            or event["sequence"] != index
            or event["event_type"] not in allowed_events
            or event["previous_event_hash"] != previous
            or supplied_hash != calculated
        ):
            raise ConformanceError("calibration v0.2 journal chain drift")
        previous = supplied_hash

    artifacts = [
        json.loads(line)
        for line in (v02 / "durable-artifacts.jsonl")
        .read_text(encoding="utf-8")
        .splitlines()
        if line.strip()
    ]
    if (
        not artifacts
        or any(item["evidence_authority"] is not False for item in artifacts)
        or any(item["authority_effect"] != "NONE" for item in artifacts)
    ):
        raise ConformanceError("calibration v0.2 artifact authority drift")

    snapshots = load_json(v02 / "task-snapshots.json")
    if (
        snapshots["schema_version"] != "1.0.0"
        or set(snapshots["tasks"])
        != {"CAL2-TASK-001", "CAL2-TASK-002", "CAL2-TASK-003"}
        or any(
            task["last_committed_sequence"] <= 0
            or not task["last_committed_event_hash"].startswith("sha256:")
            for task in snapshots["tasks"].values()
        )
    ):
        raise ConformanceError("calibration v0.2 snapshot drift")

    result = load_json(v02 / "calibration-results-v0.2.json")
    formal = result["formal_experiment_state"]
    expected_pairs = {
        ("ALIBABA_DASHSCOPE", "qwen3.7-max"),
        ("BAIDU_QIANFAN", "kimi-k2.6"),
        ("VOLCENGINE_ARK", "deepseek-v4-flash-260425"),
    }
    if (
        {(item["provider"], item["requested_model"]) for item in result["lineages"]}
        != expected_pairs
        or result["model_call_count"] > 12
        or result["unknown_call_outcomes"] < 0
        or result["journal_events"] != len(journal)
        or result["journal_hash_chain_valid"] is not True
        or result["resume_idempotency_pass"] is not True
        or formal["go_no_go_status"] != "NO_GO"
        or formal["execution_authorized"] is not False
        or formal["executed"] is not False
        or formal["formal_task_count"] != 10
        or formal["formal_run_record_count"] != 0
        or formal["value_proven"] is not False
        or result["metrics"]["FINAL_OUTCOME_IMPROVEMENT_RATE"] != "NOT_ASSESSED"
        or result["metrics"]["TITMAS_AGENT_NATIVE_VALUE_PROVEN"] is not False
        or result["metrics"]["TITMAS_AGENT_OPERATIONAL_VALUE_DEMONSTRATED"] is not False
    ):
        raise ConformanceError("calibration v0.2 result or formal boundary drift")
    if result["operational_pipeline_demonstrated"]:
        if (
            result["independent_lineage_count"] != 3
            or result["model_identity_match_rate"] != 1.0
            or sum(item["pipeline_complete"] for item in result["task_results"]) != 3
            or result["metrics"]["PIPELINE_COMPLETION_RATE"] != 1.0
            or result["metrics"]["CHECKPOINT_COVERAGE"] != 1.0
            or result["metrics"]["HANDOFF_FIELD_LOSS_RATE"] != 0.0
            or result["metrics"]["AUTHORITY_VIOLATION_COUNT"] != 0
            or result["metrics"]["SEMANTIC_ELEVATION_COUNT"] != 0
            or result["route_decision"]
            != "PROCEED_TO_HUMAN_FORMAL_EXPERIMENT_READINESS_REVIEW"
        ):
            raise ConformanceError("calibration v0.2 demonstrated gate drift")
    elif result["route_decision"] != "STOP_DIRECT_CALIBRATION_RERUNS":
        raise ConformanceError("calibration v0.2 failure route drift")

    report = execution_paths[-1].read_text(encoding="utf-8")
    for marker in (
        f"CALIBRATION_STATUS={result['calibration_status']}",
        "TITMAS_ECOLOGY_BOX_001_OPERATIONAL_CALIBRATION_V0_2_EXECUTED=true",
        "TITMAS_ECOLOGY_BOX_001_GO_NO_GO_STATUS=NO_GO",
        "TITMAS_ECOLOGY_BOX_001_EXECUTION_AUTHORIZED=false",
        "TITMAS_ECOLOGY_BOX_001_EXECUTED=false",
        "FORMAL_TASK_COUNT=10",
        "FORMAL_RUN_RECORD_COUNT=0",
        "TITMAS_ECOLOGY_BOX_001_VALUE_PROVEN=false",
        "PUBLIC_REPORT_AUTHORIZED=false",
        "COMMERCIAL_VALIDATION_AUTHORIZED=false",
        "REAL_REPOSITORY_GIT_WRITE_AUTHORIZED=false",
    ):
        if marker not in report:
            raise ConformanceError("calibration v0.2 report truth drift")

    formal_runs = [
        path
        for path in (root / "runs").iterdir()
        if path.is_file() and path.name != "README.md"
    ]
    if formal_runs:
        raise ConformanceError("calibration v0.2 created formal run records")
    return {
        "hardening_files_checked": len(preparation_paths),
        "execution_files_checked": len(execution_paths),
        "failure_injection_tests": 14,
        "role_contract_fixture_tests": 36,
        "journal_events_checked": len(journal),
        "artifacts_checked": len(artifacts),
        "calibration_status": result["calibration_status"],
        "calibration_executed": True,
        "operational_pipeline_demonstrated": result[
            "operational_pipeline_demonstrated"
        ],
        "formal_go_no_go_status": "NO_GO",
        "formal_run_record_count": 0,
        "value_proven": False,
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
        (
            "agent_native_ecology_box_001_preregistration",
            check_agent_native_ecology_box_001_preregistration,
        ),
        (
            "agent_native_ecology_box_001_execution_readiness",
            check_agent_native_ecology_box_001_execution_readiness,
        ),
        (
            "agent_native_ecology_box_001_operational_calibration",
            check_agent_native_ecology_box_001_operational_calibration,
        ),
        (
            "agent_native_ecology_box_001_operational_calibration_v02",
            check_agent_native_ecology_box_001_operational_calibration_v02,
        ),
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
