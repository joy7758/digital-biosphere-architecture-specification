#!/usr/bin/env python3
"""Dependency-free TITMAS Development conformance harness."""

from __future__ import annotations

import json
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
        "boolean": bool, "integer": int,
    }
    if expected in type_map and not isinstance(instance, type_map[expected]):
        raise ConformanceError(f"{path}: expected {expected}")
    if expected == "integer" and isinstance(instance, bool):
        raise ConformanceError(f"{path}: boolean is not an integer")
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
    evidence = payload.get("evidence_binding") or {}
    if evidence.get("source_kind") == "OBSERVATION" and evidence.get("admission_status") == "ADMITTED_EVIDENCE":
        errors.append("OBSERVATION_AS_EVIDENCE")
    if "TRUTH" in (payload.get("claims") or []):
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
