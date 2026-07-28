#!/usr/bin/env python3
"""Dependency-free TITMAS Development conformance harness."""

from __future__ import annotations

import json
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
    assignments = load_json(
        TITMAS_ROOT / "community" / "interim-role-assignments.json"
    )
    if assignments["decision_reference"] != (
        "TITMAS-OPEN-STANDARDS-COMMUNITY-INTEGRATION-D01"
    ):
        raise ConformanceError("interim role assignment lacks decision binding")
    if not assignments["revocable"] or len(assignments["assignments"]) != 3:
        raise ConformanceError("interim role assignment is not bounded")
    prohibited = {
        "DBOS_AUTHORITY",
        "SAEE_AUTHORITY",
        "EVIDENCE_TRUTH_OWNERSHIP",
        "CERTIFICATION_AUTHORITY",
        "COMMERCIAL_AUTHORITY",
        "RELEASE_AUTHORITY",
    }
    if not prohibited.issubset(set(assignments["not_granted"])):
        raise ConformanceError("interim role assignment authority boundary drift")
    return {
        "community_invariants_checked": len(must_be_false) + 3,
        "interim_role_assignments_checked": len(assignments["assignments"]),
    }


def check_internal_reviews() -> dict[str, Any]:
    review_paths = sorted((TITMAS_ROOT / "reviews").glob("integration-*.json"))
    required_scopes = {
        "CANONICAL_ARCHITECTURE",
        "OPEN_STANDARDS_AND_CONFORMANCE",
        "AGENT_NATIVE_USABILITY",
        "SECURITY_AND_CLAIMS",
    }
    if len(review_paths) != len(required_scopes):
        raise ConformanceError(
            f"expected {len(required_scopes)} integration reviews, "
            f"found {len(review_paths)}"
        )
    findings = 0
    scopes: set[str] = set()
    lineages: set[str] = set()
    for path in review_paths:
        review = load_json(path)
        required = {
            "review_id", "review_scope", "provider", "requested_model",
            "returned_model", "reviewer_lineage", "verdict", "findings",
            "blocking", "required_correction", "limitations",
            "authority_effect",
        }
        missing = sorted(required - review.keys())
        if missing:
            raise ConformanceError(f"{path.name}: missing fields {missing}")
        if review["requested_model"] != review["returned_model"]:
            raise ConformanceError(f"{path.name}: silent model substitution")
        if review["authority_effect"] != "NONE":
            raise ConformanceError(f"{path.name}: review creates authority")
        if review["verdict"] not in {"PASS", "REVISION_REQUIRED", "REJECT", "HOLD"}:
            raise ConformanceError(f"{path.name}: invalid review verdict")
        severities = {item["severity"] for item in review["findings"]}
        if severities & {"HIGH", "CRITICAL"} and review["verdict"] == "PASS":
            raise ConformanceError(f"{path.name}: HIGH/CRITICAL finding cannot PASS")
        scopes.add(review["review_scope"])
        lineages.add(review["reviewer_lineage"])
        findings += len(review["findings"])
    if scopes != required_scopes:
        raise ConformanceError(f"integration review scope drift: {sorted(scopes)}")
    if len(lineages) != len(required_scopes):
        raise ConformanceError("integration reviews must use distinct lineages")
    return {
        "review_sessions_checked": len(review_paths),
        "independent_lineages_checked": len(lineages),
        "findings_checked": findings,
    }


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
    if not tasks or len({item["task_id"] for item in tasks}) != len(tasks):
        raise ConformanceError("task registry must contain unique community tasks")
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
            value = validate_json_file(path, schemas / f"{schema_name}.schema.json")
            if schema_name == "contribution-package":
                serialized = json.dumps(value, ensure_ascii=False, sort_keys=True)
                if "PILOT-" in serialized or "CONTROLLED_LOCAL_PILOT" in serialized:
                    raise ConformanceError(
                        "canonical contribution example retains legacy pilot identity"
                    )
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
        ("internal_reviews", check_internal_reviews),
        ("agent_native_surfaces", check_agent_native_surfaces),
        ("agent_native_adversarial", check_agent_native_adversarial),
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
