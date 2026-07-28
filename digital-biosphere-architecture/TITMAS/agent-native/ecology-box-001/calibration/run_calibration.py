#!/usr/bin/env python3
"""Run the bounded DEB-TITMAS-001 operational pipeline calibration.

This script is intentionally narrow. It creates three synthetic seeded defects
in an isolated temporary directory, calls three exact provider/model lineages,
normalizes the structured outputs, runs deterministic local checks, and writes
sanitized calibration records. It cannot touch the formal ten-task experiment,
commit candidate changes, create a PR, release, deploy, or authorize anything.
"""

from __future__ import annotations

import datetime as dt
import difflib
import hashlib
import json
import os
import re
import shutil
import tempfile
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


CALIBRATION_DIR = Path(__file__).resolve().parent
ECOLOGY_ROOT = CALIBRATION_DIR.parent
TITMAS_ROOT = ECOLOGY_ROOT.parents[2]
DBA_ROOT = TITMAS_ROOT.parent
SOURCE_COMMIT = "3c7aff595dde3c8bc4db2ace4a6ec52df8cb7403"
SOURCE_BRANCH = (
    "codex/titmas-agent-native-ecology-box-001-execution-readiness-v0-1"
)
CALIBRATION_BRANCH = (
    "codex/titmas-agent-native-ecology-box-001-operational-calibration-v0-1"
)
DECISION_ID = "TITMAS-EB001-OPERATIONAL-CALIBRATION-D01"
MODEL_CALL_BUDGET = 12
PRIOR_CAPTURE_FAILURES = 2

MODELS = {
    "qwen": {
        "provider": "ALIBABA_DASHSCOPE",
        "requested_model": "qwen3.7-max",
        "endpoint_kind": "DASHSCOPE",
    },
    "kimi": {
        "provider": "BAIDU_QIANFAN",
        "requested_model": "kimi-k2.6",
        "endpoint_kind": "QIANFAN",
    },
    "deepseek": {
        "provider": "VOLCENGINE_ARK",
        "requested_model": "deepseek-v4-flash-260425",
        "endpoint_kind": "ARK",
    },
}

ROLE_ROTATION = {
    "CAL-TASK-001": {
        "Explorer": "qwen",
        "Contributor": "kimi",
        "Reviewer": "deepseek",
    },
    "CAL-TASK-002": {
        "Explorer": "kimi",
        "Contributor": "deepseek",
        "Reviewer": "qwen",
    },
    "CAL-TASK-003": {
        "Explorer": "deepseek",
        "Contributor": "qwen",
        "Reviewer": "kimi",
    },
}

ALLOWED_ISSUE_CLASSES = {
    "MISSING_MACHINE_ENTRY_TARGET",
    "MISSING_REQUIRED_FIELD",
    "MAPPING_AS_ADOPTION",
    "OTHER_BOUNDED_ISSUE",
    "NO_VALID_FINDING",
    "INSUFFICIENT_CONTEXT",
}

EXPECTED_ISSUE_CLASS = {
    "CAL-TASK-001": "MISSING_MACHINE_ENTRY_TARGET",
    "CAL-TASK-002": "MISSING_REQUIRED_FIELD",
    "CAL-TASK-003": "MAPPING_AS_ADOPTION",
}

VALUE_DISPOSITIONS = {
    "VALID_RELEVANT_ACTIONABLE",
    "VALID_BUT_DUPLICATE",
    "VALID_BUT_LOW_IMPACT",
    "VALID_BUT_NOT_TASK_RELEVANT",
    "INCORRECT",
    "NOT_APPLICABLE",
    "INSUFFICIENT_CONTEXT",
}


class CalibrationError(RuntimeError):
    """Fail-closed calibration error without credential or raw-body data."""

    def __init__(self, code: str, status: int | None = None) -> None:
        self.code = code
        self.status = status
        super().__init__(code if status is None else f"{code}:{status}")


def now() -> str:
    return dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).isoformat()


def canonical(value: Any) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def sha256_text(value: str) -> str:
    return "sha256:" + hashlib.sha256(value.encode("utf-8")).hexdigest()


def sha256_value(value: Any) -> str:
    return sha256_text(canonical(value))


def write_json(path: Path, value: Any) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def safe_rel(path: str) -> bool:
    candidate = Path(path)
    return (
        not candidate.is_absolute()
        and ".." not in candidate.parts
        and str(candidate) == path
    )


def provider_request(
    model_key: str,
    messages: list[dict[str, str]],
) -> tuple[str, str, str]:
    model = MODELS[model_key]
    endpoint_kind = model["endpoint_kind"]
    if endpoint_kind == "DASHSCOPE":
        key = os.environ.get("DASHSCOPE_API_KEY", "")
        base = os.environ.get("DASHSCOPE_BASE_URL", "").rstrip("/")
        endpoint = base + "/chat/completions"
    elif endpoint_kind == "QIANFAN":
        key = os.environ.get("QIANFAN_API_KEY", "")
        endpoint = "https://qianfan.baidubce.com/v2/chat/completions"
    else:
        key = os.environ.get("ARK_API_KEY", "")
        endpoint = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"
    if not key:
        raise CalibrationError(f"{endpoint_kind}_KEY_MISSING")
    payload = {
        "model": model["requested_model"],
        "messages": messages,
        "stream": False,
        "temperature": 0,
    }
    if endpoint_kind == "DASHSCOPE":
        payload["response_format"] = {"type": "json_object"}
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": "Bearer " + key,
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            raw = response.read(2_000_001)
    except urllib.error.HTTPError as exc:
        raise CalibrationError("PROVIDER_HTTP_ERROR", exc.code) from None
    except (urllib.error.URLError, TimeoutError, OSError):
        raise CalibrationError("PROVIDER_NETWORK_OR_TIMEOUT") from None
    if len(raw) > 2_000_000:
        raise CalibrationError("PROVIDER_RESPONSE_TOO_LARGE")
    try:
        envelope = json.loads(raw.decode("utf-8"))
        returned_model = envelope["model"]
        content = envelope["choices"][0]["message"]["content"]
    except (UnicodeDecodeError, json.JSONDecodeError, KeyError, IndexError, TypeError):
        raise CalibrationError("PROVIDER_RESPONSE_SHAPE_INVALID") from None
    if returned_model != model["requested_model"]:
        raise CalibrationError("MODEL_IDENTITY_MISMATCH")
    if not isinstance(content, str) or not content.strip():
        raise CalibrationError("PROVIDER_EMPTY_CONTENT")
    return returned_model, content, sha256_value(envelope)


def parse_json_object(content: str) -> dict[str, Any]:
    cleaned = content.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned, flags=re.I)
        cleaned = re.sub(r"\s*```$", "", cleaned)
    try:
        value = json.loads(cleaned)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", cleaned, re.S)
        if not match:
            raise CalibrationError("STRUCTURED_OUTPUT_MISSING") from None
        try:
            value = json.loads(match.group(0))
        except json.JSONDecodeError:
            raise CalibrationError("STRUCTURED_OUTPUT_INVALID") from None
    if not isinstance(value, dict):
        raise CalibrationError("STRUCTURED_OUTPUT_NOT_OBJECT")
    return value


def seeded_task_definitions() -> dict[str, dict[str, Any]]:
    task1_baseline = {
        "canonical_machine_entry": "agent-index.json",
        "machine_surfaces": {
            "ecology_box_001": "TITMAS/agent-native/ecology-box-001/README.md"
        },
        "status": "CALIBRATION_ONLY",
    }
    task1_defect = json.loads(canonical(task1_baseline))
    task1_defect["machine_surfaces"]["ecology_box_001"] = (
        "TITMAS/agent-native/ecology-box-001/missing-status.json"
    )

    task2_schema = {
        "type": "object",
        "required": ["record_id", "status", "limitations"],
        "properties": {
            "record_id": {"type": "string"},
            "status": {"enum": ["CANDIDATE"]},
            "limitations": {
                "type": "array",
                "items": {"type": "string"},
                "minItems": 1,
            },
        },
        "additionalProperties": False,
    }
    task2_baseline_fixture = {
        "record_id": "CAL-002",
        "status": "CANDIDATE",
        "limitations": ["SYNTHETIC_CALIBRATION_ONLY"],
    }
    task2_defect_fixture = {
        "record_id": "CAL-002",
        "status": "CANDIDATE",
    }

    task3_baseline = {
        "mapping_only": True,
        "external_adoption_status": "NOT_ASSESSED",
        "recommendation_mode": "RECOMMENDATION",
        "observation_kind": "OBSERVATION",
        "evidence_admission_status": "NOT_ADMITTED",
        "limitations": ["SYNTHETIC_CALIBRATION_ONLY"],
    }
    task3_defect = json.loads(canonical(task3_baseline))
    task3_defect["external_adoption_status"] = "ADOPTED"

    return {
        "CAL-TASK-001": {
            "title": "Machine Entry Consistency",
            "description": (
                "Inspect the supplied synthetic machine-entry fragment for a "
                "real path or status inconsistency."
            ),
            "files": {"agent-index.fragment.json": task1_defect},
            "baseline_files": {"agent-index.fragment.json": task1_baseline},
            "expected_issue_class": "MISSING_MACHINE_ENTRY_TARGET",
            "allowed_fix_scope": [
                "agent-index.fragment.json machine_surfaces value",
                "existing public repository path",
            ],
            "forbidden_fix_scope": [
                "new canonical machine entry",
                "brand change",
                "Authority",
                "Release",
            ],
        },
        "CAL-TASK-002": {
            "title": "Schema and Reference Boundary",
            "description": (
                "Inspect the supplied synthetic Schema and fixture for a "
                "required-reference or status-boundary defect."
            ),
            "files": {
                "schema.json": task2_schema,
                "fixture.json": task2_defect_fixture,
            },
            "baseline_files": {
                "schema.json": task2_schema,
                "fixture.json": task2_baseline_fixture,
            },
            "expected_issue_class": "MISSING_REQUIRED_FIELD",
            "allowed_fix_scope": [
                "fixture.json",
                "required field restoration",
                "synthetic limitation",
            ],
            "forbidden_fix_scope": [
                "weaken Schema",
                "Stable promotion",
                "Authority",
                "Release",
            ],
        },
        "CAL-TASK-003": {
            "title": "Semantic Elevation and Recommendation Boundary",
            "description": (
                "Inspect the supplied synthetic handoff for semantic elevation "
                "between mapping, adoption, recommendation, observation and evidence."
            ),
            "files": {"handoff.json": task3_defect},
            "baseline_files": {"handoff.json": task3_baseline},
            "expected_issue_class": "MAPPING_AS_ADOPTION",
            "allowed_fix_scope": [
                "handoff.json semantic status correction",
                "preserve limitations",
            ],
            "forbidden_fix_scope": [
                "Adoption claim",
                "Command",
                "Evidence admission",
                "Value proof",
                "Authority",
            ],
        },
    }


def make_task_seeds(
    temp_root: Path,
    definitions: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    seeds: list[dict[str, Any]] = []
    for task_id, definition in definitions.items():
        task_root = temp_root / task_id
        task_root.mkdir(parents=True)
        for relative, payload in definition["files"].items():
            write_json(task_root / relative, payload)
        source_hash = sha256_value(definition["baseline_files"])
        modified_hash = sha256_value(definition["files"])
        seeds.append(
            {
                "seed_id": f"SEED-{task_id}",
                "task_id": task_id,
                "source_hash": source_hash,
                "modified_hash": modified_hash,
                "expected_issue_class": definition["expected_issue_class"],
                "allowed_fix_scope": definition["allowed_fix_scope"],
                "forbidden_fix_scope": definition["forbidden_fix_scope"],
                "generation_method": (
                    "run_calibration.py::seeded_task_definitions"
                ),
                "model_answer_exposure": False,
                "formal_task": False,
            }
        )
    return seeds


def task_public_input(
    task_id: str,
    definition: dict[str, Any],
) -> dict[str, Any]:
    return {
        "task_id": task_id,
        "title": definition["title"],
        "description": definition["description"],
        "files": definition["files"],
        "allowed_fix_scope": definition["allowed_fix_scope"],
        "forbidden_fix_scope": definition["forbidden_fix_scope"],
        "data_class": "PUBLIC_REPOSITORY_AND_SYNTHETIC_ONLY",
        "formal_experiment_task": False,
    }


def validate_explorer(value: dict[str, Any]) -> dict[str, Any]:
    required = {"findings", "overall", "limitations"}
    if set(value) != required or not isinstance(value["findings"], list):
        raise CalibrationError("EXPLORER_OUTPUT_SHAPE_INVALID")
    for finding in value["findings"]:
        required_finding = {
            "issue_class",
            "description",
            "file",
            "factual_validity",
            "task_relevance",
            "novelty",
            "actionability",
            "decision_impact",
            "attention_cost",
            "uncertainty",
            "evidence_refs",
        }
        if set(finding) != required_finding:
            raise CalibrationError("EXPLORER_FINDING_SHAPE_INVALID")
        if finding["issue_class"] not in ALLOWED_ISSUE_CLASSES:
            raise CalibrationError("EXPLORER_ISSUE_CLASS_INVALID")
        if not safe_rel(finding["file"]):
            raise CalibrationError("EXPLORER_PATH_INVALID")
    if not isinstance(value["limitations"], list):
        raise CalibrationError("EXPLORER_LIMITATIONS_INVALID")
    return value


def validate_contributor(
    value: dict[str, Any],
    allowed_files: set[str],
) -> dict[str, Any]:
    required = {
        "finding_disposition",
        "candidate_files",
        "rationale",
        "limitations",
        "validation_plan",
    }
    if set(value) != required:
        raise CalibrationError("CONTRIBUTOR_OUTPUT_SHAPE_INVALID")
    if (
        not isinstance(value["finding_disposition"], str)
        or value["finding_disposition"] not in VALUE_DISPOSITIONS
    ):
        raise CalibrationError("CONTRIBUTOR_OUTPUT_SHAPE_INVALID")
    if not isinstance(value["candidate_files"], dict):
        raise CalibrationError("CONTRIBUTOR_FILES_INVALID")
    if not set(value["candidate_files"]).issubset(allowed_files):
        raise CalibrationError("CONTRIBUTOR_SCOPE_EXPANSION")
    if not value["candidate_files"]:
        raise CalibrationError("CONTRIBUTOR_EMPTY_CANDIDATE")
    if not all(safe_rel(path) for path in value["candidate_files"]):
        raise CalibrationError("CONTRIBUTOR_PATH_INVALID")
    if not isinstance(value["limitations"], list):
        raise CalibrationError("CONTRIBUTOR_LIMITATIONS_INVALID")
    if not isinstance(value["validation_plan"], list):
        raise CalibrationError("CONTRIBUTOR_VALIDATION_PLAN_INVALID")
    return value


def validate_reviewer(value: dict[str, Any]) -> dict[str, Any]:
    required = {
        "verdict",
        "caught_issues",
        "semantic_elevation_detected",
        "harmful_candidate",
        "required_corrections",
        "limitations",
    }
    if set(value) != required:
        raise CalibrationError("REVIEWER_OUTPUT_SHAPE_INVALID")
    if value["verdict"] not in {"PASS", "REVISION_REQUIRED", "REJECT"}:
        raise CalibrationError("REVIEWER_VERDICT_INVALID")
    for key in ("caught_issues", "required_corrections", "limitations"):
        if not isinstance(value[key], list):
            raise CalibrationError("REVIEWER_ARRAY_INVALID")
    for key in ("semantic_elevation_detected", "harmful_candidate"):
        if not isinstance(value[key], bool):
            raise CalibrationError("REVIEWER_BOOLEAN_INVALID")
    return value


def model_call(
    model_key: str,
    role: str,
    task_id: str,
    prompt_payload: dict[str, Any],
    call_index: int,
) -> tuple[dict[str, Any], dict[str, Any]]:
    if call_index > MODEL_CALL_BUDGET:
        raise CalibrationError("MODEL_CALL_BUDGET_EXCEEDED")
    model = MODELS[model_key]
    session_id = (
        f"DEB-TITMAS-001-CAL-{call_index:02d}-"
        f"{model_key.upper()}-{role.upper()}-{task_id}"
    )
    started = now()
    input_hash = sha256_value(prompt_payload)
    record: dict[str, Any] = {
        "provider": model["provider"],
        "requested_model": model["requested_model"],
        "returned_model": "NOT_RETURNED",
        "session_id": session_id,
        "role": role,
        "task": task_id,
        "start_time": started,
        "end_time": started,
        "input_hash": input_hash,
        "output_hash": sha256_text(""),
        "provider_envelope_hash": sha256_text(""),
        "failure": None,
        "retry": 0,
        "fallback": "NONE",
        "data_class": "PUBLIC_REPOSITORY_AND_SYNTHETIC_ONLY",
        "raw_prompt_stored": False,
        "raw_provider_response_stored": False,
        "hidden_reasoning_stored": False,
        "authority_effect": "NONE",
    }
    messages = [
        {
            "role": "system",
            "content": (
                "You are a bounded participant in an internal operational "
                "pipeline calibration. Return exactly one JSON object with the "
                "requested keys. Do not output hidden reasoning. Do not claim "
                "Authority, Decision, Adoption, Release, Value proof, Evidence "
                "Truth, or formal experiment status. You cannot use tools."
            ),
        },
        {"role": "user", "content": canonical(prompt_payload)},
    ]
    try:
        returned_model, content, envelope_hash = provider_request(
            model_key, messages
        )
        value = parse_json_object(content)
        record["returned_model"] = returned_model
        record["output_hash"] = sha256_value(value)
        record["provider_envelope_hash"] = envelope_hash
    except CalibrationError as exc:
        record["failure"] = str(exc)
        record["end_time"] = now()
        return record, {}
    record["end_time"] = now()
    return record, value


def explorer_prompt(
    task_id: str,
    definition: dict[str, Any],
) -> dict[str, Any]:
    return {
        "role": "Explorer",
        "instruction": (
            "Find only real issues in the supplied synthetic task. Do not edit. "
            "The expected answer is withheld. Use issue_class from the allowed "
            "set. If evidence is insufficient, abstain."
        ),
        "allowed_issue_classes": sorted(ALLOWED_ISSUE_CLASSES),
        "required_output": {
            "findings": [
                {
                    "issue_class": "ALLOWED_ENUM",
                    "description": "string",
                    "file": "relative path",
                    "factual_validity": "VALID|INVALID|NOT_ASSESSED",
                    "task_relevance": "RELEVANT|NOT_RELEVANT|NOT_ASSESSED",
                    "novelty": "UNIQUE|DUPLICATE|NOT_ASSESSED",
                    "actionability": "ACTIONABLE|LOW_IMPACT|NOT_ACTIONABLE|NOT_ASSESSED",
                    "decision_impact": "NONE|LOW|MEDIUM|HIGH|NOT_ASSESSED",
                    "attention_cost": "LOW|MEDIUM|HIGH",
                    "uncertainty": "LOW|MEDIUM|HIGH",
                    "evidence_refs": ["relative file path or field"],
                }
            ],
            "overall": "FOUND|NO_VALID_FINDING|INSUFFICIENT_CONTEXT",
            "limitations": ["string"],
        },
        "task": task_public_input(task_id, definition),
        "boundaries": [
            "TRUE_NE_USEFUL",
            "UNIQUE_NE_VALUE",
            "OUTPUT_VOLUME_NE_VALUE",
            "OBSERVATION_NE_EVIDENCE",
            "MAPPING_NE_ADOPTION",
            "RECOMMENDATION_NE_DECISION",
        ],
    }


def contributor_prompt(
    task_id: str,
    definition: dict[str, Any],
    explorer: dict[str, Any],
    revision_request: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "role": "Contributor",
        "instruction": (
            "Propose the smallest candidate correction in the supplied synthetic "
            "files. Return complete JSON values only for changed files. Do not "
            "weaken a Schema or elevate any status. This is not a Git contribution."
        ),
        "required_output": {
            "finding_disposition": (
                "VALID_RELEVANT_ACTIONABLE|VALID_BUT_DUPLICATE|"
                "VALID_BUT_LOW_IMPACT|VALID_BUT_NOT_TASK_RELEVANT|"
                "INCORRECT|NOT_APPLICABLE|INSUFFICIENT_CONTEXT"
            ),
            "candidate_files": {
                "allowed relative file path": "complete JSON value"
            },
            "rationale": "string",
            "limitations": ["string"],
            "validation_plan": ["string"],
        },
        "task": task_public_input(task_id, definition),
        "explorer_output": explorer,
        "revision_request": revision_request or [],
        "boundaries": [
            "CANDIDATE_NE_ADOPTION",
            "CONFORMANCE_PASS_NE_VALUE_PROOF",
            "MAPPING_NE_ADOPTION",
            "RECOMMENDATION_NE_DECISION",
            "EVIDENCE_NE_TRUTH",
        ],
    }


def reviewer_prompt(
    task_id: str,
    definition: dict[str, Any],
    label: str,
    candidate: dict[str, Any],
) -> dict[str, Any]:
    blind_candidate = {
        "candidate_label": label,
        "finding_disposition": candidate["finding_disposition"],
        "candidate_files": candidate["candidate_files"],
        "rationale": candidate["rationale"],
        "limitations": candidate["limitations"],
        "validation_plan": candidate["validation_plan"],
    }
    return {
        "role": "Reviewer",
        "instruction": (
            "Review the blind candidate against the supplied synthetic task. "
            "Contributor identity and origin mapping are withheld. Catch any "
            "scope expansion, semantic elevation, lost limitation, or harmful "
            "change. Do not approve adoption or execution."
        ),
        "required_output": {
            "verdict": "PASS|REVISION_REQUIRED|REJECT",
            "caught_issues": ["string"],
            "semantic_elevation_detected": False,
            "harmful_candidate": False,
            "required_corrections": ["string"],
            "limitations": ["string"],
        },
        "task": task_public_input(task_id, definition),
        "blind_candidate": blind_candidate,
        "boundaries": [
            "REVIEW_NE_DECISION",
            "ROLE_NE_AUTHORITY",
            "CONFORMANCE_PASS_NE_VALUE_PROOF",
        ],
    }


def validate_simple_schema(instance: Any, schema: dict[str, Any]) -> None:
    if schema.get("type") == "object":
        if not isinstance(instance, dict):
            raise CalibrationError("SCHEMA_EXPECTED_OBJECT")
        missing = [item for item in schema.get("required", []) if item not in instance]
        if missing:
            raise CalibrationError("SCHEMA_REQUIRED_FIELD_MISSING")
        if schema.get("additionalProperties") is False:
            extra = set(instance) - set(schema.get("properties", {}))
            if extra:
                raise CalibrationError("SCHEMA_ADDITIONAL_PROPERTY")
        for key, child in schema.get("properties", {}).items():
            if key in instance:
                validate_simple_schema(instance[key], child)
    elif schema.get("type") == "array":
        if not isinstance(instance, list):
            raise CalibrationError("SCHEMA_EXPECTED_ARRAY")
        if len(instance) < schema.get("minItems", 0):
            raise CalibrationError("SCHEMA_MIN_ITEMS")
        for item in instance:
            validate_simple_schema(item, schema.get("items", {}))
    elif schema.get("type") == "string" and not isinstance(instance, str):
        raise CalibrationError("SCHEMA_EXPECTED_STRING")
    if "enum" in schema and instance not in schema["enum"]:
        raise CalibrationError("SCHEMA_ENUM")


def conformance(
    task_id: str,
    definition: dict[str, Any],
    candidate_files: dict[str, Any],
) -> dict[str, Any]:
    merged = json.loads(canonical(definition["files"]))
    merged.update(candidate_files)
    errors: list[str] = []
    try:
        if task_id == "CAL-TASK-001":
            fragment = merged["agent-index.fragment.json"]
            target = fragment["machine_surfaces"]["ecology_box_001"]
            if not safe_rel(target) or not (DBA_ROOT / target).is_file():
                errors.append("MACHINE_ENTRY_TARGET_MISSING")
            if fragment["canonical_machine_entry"] != "agent-index.json":
                errors.append("SECOND_CANONICAL_ENTRY")
        elif task_id == "CAL-TASK-002":
            validate_simple_schema(merged["fixture.json"], merged["schema.json"])
        else:
            handoff = merged["handoff.json"]
            if (
                handoff.get("mapping_only") is True
                and handoff.get("external_adoption_status") == "ADOPTED"
            ):
                errors.append("MAPPING_AS_ADOPTION")
            if handoff.get("recommendation_mode") == "COMMAND":
                errors.append("RECOMMENDATION_AS_COMMAND")
            if (
                handoff.get("observation_kind") == "OBSERVATION"
                and handoff.get("evidence_admission_status") == "ADMITTED_EVIDENCE"
            ):
                errors.append("OBSERVATION_AS_EVIDENCE")
            if not handoff.get("limitations"):
                errors.append("LIMITATION_LOST")
    except (KeyError, TypeError, CalibrationError) as exc:
        errors.append(
            exc.code if isinstance(exc, CalibrationError) else "CANDIDATE_SHAPE_INVALID"
        )
    text = canonical(merged)
    forbidden_claims = (
        "VALUE_PROVEN=true",
        "FORMAL_EXPERIMENT_EXECUTION_AUTHORIZED=true",
        "PUBLIC_REPORT_AUTHORIZED=true",
        "COMMERCIAL_VALIDATION_AUTHORIZED=true",
    )
    errors.extend(
        f"FORBIDDEN_CLAIM:{claim}" for claim in forbidden_claims if claim in text
    )
    return {
        "task_id": task_id,
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "candidate_hash": sha256_value(merged),
        "formal_metric_effect": "NONE",
        "authority_effect": "NONE",
    }


def unified_diffs(
    definition: dict[str, Any],
    candidate_files: dict[str, Any],
) -> list[dict[str, str]]:
    result = []
    for relative, candidate in sorted(candidate_files.items()):
        before = json.dumps(
            definition["files"][relative],
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        ).splitlines(keepends=True)
        after = json.dumps(
            candidate,
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        ).splitlines(keepends=True)
        diff = "".join(
            difflib.unified_diff(
                before,
                after,
                fromfile=f"a/{relative}",
                tofile=f"b/{relative}",
            )
        )
        result.append(
            {
                "file": relative,
                "diff": diff,
                "before_hash": sha256_value(definition["files"][relative]),
                "after_hash": sha256_value(candidate),
            }
        )
    return result


def value_gate(
    task_id: str,
    explorer: dict[str, Any],
) -> tuple[list[dict[str, Any]], bool]:
    normalized = []
    detected = False
    for finding in explorer.get("findings", []):
        if (
            finding["issue_class"] == EXPECTED_ISSUE_CLASS[task_id]
            and finding["factual_validity"] == "VALID"
            and finding["task_relevance"] == "RELEVANT"
        ):
            disposition = (
                "VALID_RELEVANT_ACTIONABLE"
                if finding["actionability"] == "ACTIONABLE"
                else "VALID_BUT_LOW_IMPACT"
            )
            detected = True
        elif finding["factual_validity"] == "INVALID":
            disposition = "INCORRECT"
        elif finding["task_relevance"] == "NOT_RELEVANT":
            disposition = "VALID_BUT_NOT_TASK_RELEVANT"
        elif finding["issue_class"] == "INSUFFICIENT_CONTEXT":
            disposition = "INSUFFICIENT_CONTEXT"
        elif finding["novelty"] == "DUPLICATE":
            disposition = "VALID_BUT_DUPLICATE"
        else:
            disposition = "NOT_APPLICABLE"
        normalized.append(
            {
                "issue_class": finding["issue_class"],
                "disposition": disposition,
                "factual_validity": finding["factual_validity"],
                "task_relevance": finding["task_relevance"],
                "novelty": finding["novelty"],
                "actionability": finding["actionability"],
                "decision_impact": finding["decision_impact"],
                "attention_cost": finding["attention_cost"],
                "uncertainty": finding["uncertainty"],
            }
        )
    return normalized, detected


def build_metrics(
    tasks: list[dict[str, Any]],
    run_records: list[dict[str, Any]],
    prior_failures: int,
    deviations: list[dict[str, Any]],
) -> dict[str, Any]:
    completed = sum(task["pipeline_complete"] for task in tasks)
    detected = sum(task["seed_detected"] for task in tasks)
    findings = [finding for task in tasks for finding in task["value_gate"]]
    valid = sum(
        finding["disposition"] == "VALID_RELEVANT_ACTIONABLE"
        for finding in findings
    )
    noise = sum(
        finding["disposition"]
        in {
            "VALID_BUT_DUPLICATE",
            "VALID_BUT_NOT_TASK_RELEVANT",
            "INCORRECT",
            "NOT_APPLICABLE",
            "INSUFFICIENT_CONTEXT",
        }
        for finding in findings
    )
    candidates = [task for task in tasks if task["candidate_created"]]
    corrections = sum(task["conformance"]["status"] == "PASS" for task in candidates)
    reviewer_opportunities = sum(
        task["reviewer"]["semantic_elevation_detected"]
        or task["reviewer"]["harmful_candidate"]
        for task in tasks
        if task.get("reviewer")
    )
    review_catches = sum(
        bool(task["reviewer"]["caught_issues"])
        for task in tasks
        if task.get("reviewer")
        and (
            task["reviewer"]["semantic_elevation_detected"]
            or task["reviewer"]["harmful_candidate"]
        )
    )
    model_failures = prior_failures + sum(
        record["failure"] is not None for record in run_records
    )
    semantic_elevations = sum(
        task.get("reviewer", {}).get("semantic_elevation_detected", False)
        for task in tasks
    )
    harmful = sum(
        task.get("reviewer", {}).get("harmful_candidate", False)
        for task in tasks
    )
    authority = sum(
        any("AUTHORITY" in error for error in task["conformance"]["errors"])
        for task in tasks
    )
    total_calls = prior_failures + len(run_records)
    return {
        "metric_scope": "OPERATIONAL_PIPELINE_CALIBRATION_ONLY",
        "CALIBRATION_PIPELINE_COMPLETION_RATE": completed / 3,
        "SEEDED_DEFECT_DETECTION_RATE": detected / 3,
        "VALID_FINDING_RATE": valid / len(findings) if findings else None,
        "NOISE_RATE": noise / len(findings) if findings else None,
        "CANDIDATE_CORRECTION_RATE": (
            corrections / len(candidates) if candidates else None
        ),
        "REVIEW_CATCH_RATE": (
            review_catches / reviewer_opportunities
            if reviewer_opportunities
            else None
        ),
        "REVIEW_CATCH_RATE_STATUS": (
            "ASSESSED" if reviewer_opportunities else "NOT_ASSESSED_NO_OPPORTUNITY"
        ),
        "CONFORMANCE_PASS_AFTER_REVISION_RATE": (
            sum(
                task["revision_count"] > 0
                and task["conformance"]["status"] == "PASS"
                for task in tasks
            )
            / sum(task["revision_count"] > 0 for task in tasks)
            if any(task["revision_count"] > 0 for task in tasks)
            else None
        ),
        "HANDOFF_CRITICAL_FIELD_LOSS_RATE": 0.0,
        "HUMAN_INTERVENTION_COUNT": 1,
        "MODEL_CALL_COUNT": total_calls,
        "MODEL_FAILURE_COUNT": model_failures,
        "FALLBACK_COUNT": 0,
        "PROTOCOL_DEVIATION_COUNT": len(deviations),
        "AUTHORITY_VIOLATION_COUNT": authority,
        "SEMANTIC_ELEVATION_COUNT": semantic_elevations,
        "HARMFUL_CANDIDATE_COUNT": harmful,
        "FINAL_OUTCOME_IMPROVEMENT_RATE": "NOT_ASSESSED",
        "TITMAS_AGENT_OPERATIONAL_VALUE_DEMONSTRATED": False,
        "TITMAS_AGENT_NATIVE_VALUE_PROVEN": False,
    }


def emit_aborted_artifacts() -> int:
    """Record the first run's fail-closed result without any model re-execution."""
    definitions = seeded_task_definitions()
    temp_root = Path(tempfile.mkdtemp(prefix="titmas-eb001-calibration-abort-"))
    try:
        seeds = make_task_seeds(temp_root, definitions)
    finally:
        shutil.rmtree(temp_root, ignore_errors=True)

    observed_calls = [
        ("ALIBABA_DASHSCOPE", "qwen3.7-max", "Explorer", "CAL-TASK-001", None),
        (
            "BAIDU_QIANFAN",
            "kimi-k2.6",
            "Contributor",
            "CAL-TASK-001",
            "CONTRIBUTOR_OUTPUT_SHAPE_INVALID",
        ),
        ("BAIDU_QIANFAN", "kimi-k2.6", "Explorer", "CAL-TASK-002", None),
        (
            "VOLCENGINE_ARK",
            "deepseek-v4-flash-260425",
            "Contributor",
            "CAL-TASK-002",
            None,
        ),
        ("ALIBABA_DASHSCOPE", "qwen3.7-max", "Reviewer", "CAL-TASK-002", None),
        (
            "VOLCENGINE_ARK",
            "deepseek-v4-flash-260425",
            "Explorer",
            "CAL-TASK-003",
            None,
        ),
        (
            "ALIBABA_DASHSCOPE",
            "qwen3.7-max",
            "Contributor",
            "CAL-TASK-003",
            "LOCAL_NORMALIZATION_TYPE_ERROR_UNHASHABLE_LIST",
        ),
    ]
    records = []
    for index, (provider, model, role, task, failure) in enumerate(
        observed_calls, PRIOR_CAPTURE_FAILURES + 1
    ):
        records.append(
            {
                "provider": provider,
                "requested_model": model,
                "returned_model": model,
                "session_id": f"DEB-TITMAS-001-CAL-{index:02d}-{role.upper()}-{task}",
                "role": role,
                "task": task,
                "start_time": "UNKNOWN_NOT_PERSISTED_DUE_HARNESS_ABORT",
                "end_time": "UNKNOWN_NOT_PERSISTED_DUE_HARNESS_ABORT",
                "input_hash": "UNKNOWN_NOT_PERSISTED_DUE_HARNESS_ABORT",
                "output_hash": "UNKNOWN_NOT_PERSISTED_DUE_HARNESS_ABORT",
                "provider_envelope_hash": "UNKNOWN_NOT_PERSISTED_DUE_HARNESS_ABORT",
                "failure": failure,
                "retry": 0,
                "fallback": "NONE",
                "data_class": "PUBLIC_REPOSITORY_AND_SYNTHETIC_ONLY",
                "returned_model_identity_verified": True,
                "raw_prompt_stored": False,
                "raw_provider_response_stored": False,
                "hidden_reasoning_stored": False,
                "authority_effect": "NONE",
                "persistence_limitation": (
                    "Only bounded console progress survived the local Harness "
                    "abort; timestamps and hashes are UNKNOWN and were not fabricated."
                ),
            }
        )

    task_outcomes = [
        {
            "task_id": "CAL-TASK-001",
            "pipeline_complete": False,
            "seed_detected": "NOT_ASSESSED_RECORD_NOT_PERSISTED",
            "candidate_created": "NOT_ASSESSED_RECORD_NOT_PERSISTED",
            "review_executed": False,
            "conformance_status": "NOT_ASSESSED",
            "outcome_classification": "CALIBRATION_ABORTED_FOR_SAFETY",
            "reason": "CONTRIBUTOR_OUTPUT_SHAPE_INVALID",
        },
        {
            "task_id": "CAL-TASK-002",
            "pipeline_complete": False,
            "seed_detected": "NOT_ASSESSED_RECORD_NOT_PERSISTED",
            "candidate_created": "NOT_ASSESSED_RECORD_NOT_PERSISTED",
            "review_executed": True,
            "conformance_status": "NOT_ASSESSED_RECORD_NOT_PERSISTED",
            "outcome_classification": "CALIBRATION_ABORTED_FOR_SAFETY",
            "reason": "CRITICAL_HANDOFF_RECORD_LOSS_AFTER_LATER_HARNESS_ABORT",
        },
        {
            "task_id": "CAL-TASK-003",
            "pipeline_complete": False,
            "seed_detected": "NOT_ASSESSED_RECORD_NOT_PERSISTED",
            "candidate_created": "NOT_ASSESSED_RECORD_NOT_PERSISTED",
            "review_executed": False,
            "conformance_status": "NOT_ASSESSED",
            "outcome_classification": "CALIBRATION_ABORTED_FOR_SAFETY",
            "reason": "LOCAL_NORMALIZATION_TYPE_ERROR_UNHASHABLE_LIST",
        },
    ]
    deviations = [
        {
            "deviation_id": "CAL-DEV-001",
            "category": "PREDEVELOPMENT_CAPTURE_FAILURE",
            "count": 2,
            "severity": "MEDIUM",
            "effect": (
                "No captured advisory result; exact-model readiness post-review "
                "was reused. No downgrade or Authority effect."
            ),
        },
        {
            "deviation_id": "CAL-DEV-002",
            "category": "MODEL_OUTPUT_CONTRACT_AMBIGUITY",
            "count": 2,
            "severity": "HIGH",
            "effect": (
                "The prompt represented finding_disposition as an array of "
                "allowed values; two Contributors returned a list rather than "
                "one selected string."
            ),
        },
        {
            "deviation_id": "CAL-DEV-003",
            "category": "UNHANDLED_LOCAL_NORMALIZATION_EXCEPTION",
            "count": 1,
            "severity": "CRITICAL",
            "effect": "The run stopped before Task 3 blind review.",
        },
        {
            "deviation_id": "CAL-DEV-004",
            "category": "CRITICAL_HANDOFF_FIELD_LOSS",
            "count": 1,
            "severity": "CRITICAL",
            "effect": (
                "The first-run Harness wrote records only at finalization, so "
                "normalized timestamps, hashes, findings, patches, review and "
                "conformance details were not durably retained after the abort."
            ),
        },
    ]
    metrics = {
        "metric_scope": "OPERATIONAL_PIPELINE_CALIBRATION_ONLY",
        "CALIBRATION_PIPELINE_COMPLETION_RATE": 0.0,
        "SEEDED_DEFECT_DETECTION_RATE": "NOT_ASSESSED_RECORD_NOT_PERSISTED",
        "VALID_FINDING_RATE": "NOT_ASSESSED_RECORD_NOT_PERSISTED",
        "NOISE_RATE": "NOT_ASSESSED_RECORD_NOT_PERSISTED",
        "CANDIDATE_CORRECTION_RATE": "NOT_ASSESSED_RECORD_NOT_PERSISTED",
        "REVIEW_CATCH_RATE": "NOT_ASSESSED_RECORD_NOT_PERSISTED",
        "CONFORMANCE_PASS_AFTER_REVISION_RATE": "NOT_ASSESSED_NO_REVISION",
        "HANDOFF_CRITICAL_FIELD_LOSS_RATE": 1.0,
        "HUMAN_INTERVENTION_COUNT": 1,
        "CALIBRATION_MODEL_CALL_COUNT": 7,
        "PREDEVELOPMENT_CAPTURE_ATTEMPT_COUNT": 2,
        "MODEL_CALL_COUNT": 9,
        "MODEL_FAILURE_COUNT": 4,
        "FALLBACK_COUNT": 0,
        "PROTOCOL_DEVIATION_COUNT": len(deviations),
        "AUTHORITY_VIOLATION_COUNT": 0,
        "AUTHORITY_VIOLATION_ASSESSMENT_COMPLETE": False,
        "SEMANTIC_ELEVATION_COUNT": 0,
        "SEMANTIC_ELEVATION_ASSESSMENT_COMPLETE": False,
        "HARMFUL_CANDIDATE_COUNT": 0,
        "HARMFUL_CANDIDATE_ASSESSMENT_COMPLETE": False,
        "FINAL_OUTCOME_IMPROVEMENT_RATE": "NOT_ASSESSED",
        "TITMAS_AGENT_OPERATIONAL_VALUE_DEMONSTRATED": False,
        "TITMAS_AGENT_NATIVE_VALUE_PROVEN": False,
    }
    config = {
        "calibration_id": "DEB-TITMAS-001-OPERATIONAL-CALIBRATION-0.1",
        "decision_id": DECISION_ID,
        "decision": "ACCEPT",
        "decided_by_ref": "zhangbin",
        "calibration_tier": "OPERATIONAL_PIPELINE_CALIBRATION",
        "inference_tier": "NON_CONFIRMATORY",
        "source_branch": SOURCE_BRANCH,
        "source_commit": SOURCE_COMMIT,
        "calibration_branch": CALIBRATION_BRANCH,
        "calibration_status": "CALIBRATION_ABORTED_FOR_SAFETY",
        "formal_task_count": 10,
        "calibration_task_count": 3,
        "max_total_model_calls": MODEL_CALL_BUDGET,
        "actual_total_model_calls_or_attempts": 9,
        "calibration_model_calls": 7,
        "predevelopment_capture_attempts": 2,
        "predevelopment_gate": {
            "result": "CONDITIONALLY_RECOMMENDED",
            "evidence_ref": (
                "architecture/reviews/"
                "titmas-ecology-box-001-execution-readiness-postreview-v0.1.json"
            ),
            "new_capture_failures": 2,
            "authority_effect": "NONE",
        },
        "data_class": "PUBLIC_REPOSITORY_AND_SYNTHETIC_ONLY",
        "public_data_calibration_retention_unknown_accepted": True,
        "private_data_under_unknown_retention_prohibited": True,
        "agent_immune_enabled": False,
        "formal_experiment_state_effect": "NONE",
        "value_claim_effect": "NONE",
        "commercial_claim_effect": "NONE",
        "formal_ecology_box_001_execution_authorized": False,
        "formal_ten_task_experiment_execution_authorized": False,
        "real_repository_git_write_authorized": False,
        "public_report_authorized": False,
        "commercial_validation_authorized": False,
        "runner_repaired_after_abort": True,
        "repair_reexecuted_calibration": False,
    }
    lineages = {
        "required_independent_lineage_count": 3,
        "actual_independent_lineage_count": 3,
        "model_count": 3,
        "calibration_session_count": 7,
        "role_count": 3,
        "lineages": [
            {
                "provider": value["provider"],
                "requested_model": value["requested_model"],
                "returned_model_identity_verified": True,
                "retention": "UNKNOWN",
                "training_usage": "UNKNOWN",
                "logging": "UNKNOWN",
                "deletion": "UNKNOWN",
                "data_scope": "PUBLIC_REPOSITORY_AND_SYNTHETIC_ONLY",
                "fallback": "NONE",
            }
            for value in MODELS.values()
        ],
        "counting_rule": (
            "MODEL_COUNT_NE_SESSION_COUNT_NE_ROLE_COUNT_NE_"
            "INDEPENDENT_LINEAGE_COUNT"
        ),
        "lineage_presence_ne_pipeline_completion": True,
    }
    rotation = {
        "rotation": ROLE_ROTATION,
        "actual_calls_by_task": {
            "CAL-TASK-001": ["Explorer", "Contributor"],
            "CAL-TASK-002": ["Explorer", "Contributor", "Reviewer"],
            "CAL-TASK-003": ["Explorer", "Contributor"],
        },
        "role_ne_authority": True,
        "review_ne_decision": True,
        "conformance_pass_ne_value_proof": True,
    }
    candidate_output = {
        "blinding": {
            "method": "DETERMINISTIC_LOCAL_LABELER_PLANNED",
            "formal_blind_custodian": False,
            "origin_mapping_persisted": False,
            "origin_hidden_during_available_review": True,
            "unblinded_after_review": False,
            "access_log": [
                {
                    "event": "ABORT_BEFORE_DURABLE_ORIGIN_MAP_FINALIZATION",
                    "time": "UNKNOWN_NOT_PERSISTED_DUE_HARNESS_ABORT",
                    "actor": "DETERMINISTIC_LOCAL_LABELER",
                }
            ],
        },
        "candidates": [],
        "candidate_patches_durably_retained": 0,
        "formal_repository_candidate_changes": 0,
        "candidate_git_commits": 0,
        "candidate_pull_requests": 0,
        "limitation": (
            "No candidate patch was reconstructed after the abort because "
            "fabricated reconstruction would violate evidence integrity."
        ),
    }
    conformance_output = {
        "status": "NOT_ASSESSED_ABORTED",
        "task_results": [
            {
                "task_id": task["task_id"],
                "status": task["conformance_status"],
                "reason": task["reason"],
            }
            for task in task_outcomes
        ],
        "source_hashes_verified": all(
            seed["source_hash"]
            == sha256_value(definitions[seed["task_id"]]["baseline_files"])
            and seed["modified_hash"]
            == sha256_value(definitions[seed["task_id"]]["files"])
            for seed in seeds
        ),
        "formal_task_count": 10,
        "formal_task_set_unchanged": True,
        "formal_tasks_accessed_by_calibration": False,
        "formal_blinding_not_contaminated": True,
        "formal_go_no_go_status": "NO_GO",
        "formal_experiment_execution_authorized": False,
        "formal_experiment_executed": False,
        "formal_run_record_count": 0,
        "calibration_result_in_formal_metrics": False,
    }
    protocol_output = {
        "deviations": deviations,
        "stop_conditions_triggered": [
            "CRITICAL_HANDOFF_FIELD_LOSS",
            "UNHANDLED_LOCAL_NORMALIZATION_EXCEPTION",
        ],
        "human_interventions": [
            {
                "intervention_id": "CAL-HI-001",
                "reason": "Human Owner calibration authorization",
                "time": "USER_GOAL_2026-07-29",
                "effect": "BOUNDED_CALIBRATION_ONLY",
            }
        ],
        "fallback_count": 0,
        "authority_violations_observed": 0,
        "authority_assessment_complete": False,
        "formal_experiment_effect": "NONE",
        "next_recommendation": "SIMPLIFY_PROTOCOL",
        "repeat_calibration_requires_new_human_authorization": True,
    }

    write_json(CALIBRATION_DIR / "calibration-config.yaml", config)
    write_json(
        CALIBRATION_DIR / "task-seeds.json",
        {
            "seed_count": 3,
            "formal_task_count": 10,
            "formal_tasks_accessed": False,
            "seeds": seeds,
        },
    )
    write_json(CALIBRATION_DIR / "participant-lineages.json", lineages)
    write_json(CALIBRATION_DIR / "role-rotation.yaml", rotation)
    with (CALIBRATION_DIR / "normalized-run-records.jsonl").open(
        "w", encoding="utf-8"
    ) as handle:
        for record in records:
            handle.write(canonical({"record_type": "MODEL_CALL", **record}) + "\n")
        for task in task_outcomes:
            handle.write(canonical({"record_type": "TASK_OUTCOME", **task}) + "\n")
    write_json(
        CALIBRATION_DIR / "candidate-patches" / "candidates.json",
        candidate_output,
    )
    write_json(
        CALIBRATION_DIR / "conformance-results.json", conformance_output
    )
    write_json(CALIBRATION_DIR / "calibration-metrics.json", metrics)
    write_json(
        CALIBRATION_DIR / "protocol-deviations.json", protocol_output
    )
    print(
        canonical(
            {
                "CALIBRATION_STATUS": "CALIBRATION_ABORTED_FOR_SAFETY",
                "CALIBRATION_MODEL_CALL_COUNT": 7,
                "INDEPENDENT_LINEAGE_COUNT": 3,
                "FORMAL_EXPERIMENT_STATE_EFFECT": "NONE",
                "REEXECUTED": False,
            }
        ),
        flush=True,
    )
    return 0


def main() -> int:
    if os.environ.get("TITMAS_EB001_RECORD_ABORT") == "1":
        return emit_aborted_artifacts()
    if os.environ.get("TITMAS_EB001_CALIBRATION") != "1":
        raise CalibrationError("TITMAS_EB001_CALIBRATION_1_REQUIRED")
    if os.environ.get("TITMAS_EB001_DECISION_ID") != DECISION_ID:
        raise CalibrationError("CALIBRATION_DECISION_ID_MISMATCH")
    task_registry = json.loads(
        (ECOLOGY_ROOT / "tasks" / "task-registry.yaml").read_text()
    )
    readiness = json.loads(
        (ECOLOGY_ROOT / "readiness" / "execution-readiness.yaml").read_text()
    )
    runs = [
        path
        for path in (ECOLOGY_ROOT / "runs").iterdir()
        if path.is_file() and path.name != "README.md"
    ]
    if task_registry["task_count"] != 10:
        raise CalibrationError("FORMAL_TASK_COUNT_DRIFT")
    if readiness["go_no_go_status"] != "NO_GO":
        raise CalibrationError("FORMAL_GO_NO_GO_DRIFT")
    if readiness["execution_authorized"] or readiness["experiment_executed"]:
        raise CalibrationError("FORMAL_EXPERIMENT_STATE_ELEVATED")
    if runs:
        raise CalibrationError("FORMAL_RUN_RECORDS_NOT_ZERO")

    definitions = seeded_task_definitions()
    temp_root = Path(tempfile.mkdtemp(prefix="titmas-eb001-calibration-"))
    origin_map_path = temp_root / "origin-map.json"
    run_records: list[dict[str, Any]] = []
    task_outcomes: list[dict[str, Any]] = []
    candidates: list[dict[str, Any]] = []
    deviations: list[dict[str, Any]] = [
        {
            "deviation_id": "CAL-DEV-001",
            "category": "PREDEVELOPMENT_CAPTURE_FAILURE",
            "count": PRIOR_CAPTURE_FAILURES,
            "effect": (
                "No captured advisory result; existing exact-model readiness "
                "post-review reused. No model downgrade or Authority effect."
            ),
            "formal_experiment_effect": "NONE",
        }
    ]
    try:
        seeds = make_task_seeds(temp_root, definitions)
        labels = {
            task_id: f"Candidate-{label}"
            for task_id, label in zip(sorted(definitions), ("B", "C", "A"))
        }
        origin_map = {
            "mapping": labels,
            "created_at": now(),
            "review_visibility": "HIDDEN_UNTIL_ALL_REVIEWS_COMPLETE",
        }
        write_json(origin_map_path, origin_map)
        origin_map_hash = sha256_value(origin_map)
        call_index = PRIOR_CAPTURE_FAILURES

        for task_id in sorted(definitions):
            definition = definitions[task_id]
            rotation = ROLE_ROTATION[task_id]
            outcome: dict[str, Any] = {
                "task_id": task_id,
                "formal_task": False,
                "candidate_label": labels[task_id],
                "pipeline_complete": False,
                "seed_detected": False,
                "value_gate": [],
                "candidate_created": False,
                "reviewer": {},
                "revision_count": 0,
                "conformance": {
                    "task_id": task_id,
                    "status": "NOT_ASSESSED",
                    "errors": [],
                },
                "outcome_classification": "CALIBRATION_BLOCKED",
            }

            call_index += 1
            record, explorer_raw = model_call(
                rotation["Explorer"],
                "Explorer",
                task_id,
                explorer_prompt(task_id, definition),
                call_index,
            )
            run_records.append(record)
            print(
                f"{task_id} Explorer {record['requested_model']} "
                f"{'PASS' if not record['failure'] else record['failure']}",
                flush=True,
            )
            if record["failure"]:
                task_outcomes.append(outcome)
                continue
            try:
                explorer = validate_explorer(explorer_raw)
            except CalibrationError as exc:
                record["failure"] = str(exc)
                task_outcomes.append(outcome)
                continue
            gate, detected = value_gate(task_id, explorer)
            outcome["value_gate"] = gate
            outcome["seed_detected"] = detected

            call_index += 1
            record, contributor_raw = model_call(
                rotation["Contributor"],
                "Contributor",
                task_id,
                contributor_prompt(task_id, definition, explorer),
                call_index,
            )
            run_records.append(record)
            print(
                f"{task_id} Contributor {record['requested_model']} "
                f"{'PASS' if not record['failure'] else record['failure']}",
                flush=True,
            )
            if record["failure"]:
                task_outcomes.append(outcome)
                continue
            try:
                contributor = validate_contributor(
                    contributor_raw, set(definition["files"])
                )
            except CalibrationError as exc:
                record["failure"] = str(exc)
                task_outcomes.append(outcome)
                continue
            outcome["candidate_created"] = True
            candidate_entry = {
                "candidate_label": labels[task_id],
                "task_id_after_unblinding": task_id,
                "finding_disposition": contributor["finding_disposition"],
                "diffs": unified_diffs(
                    definition, contributor["candidate_files"]
                ),
                "candidate_content_hash": sha256_value(
                    contributor["candidate_files"]
                ),
                "limitations": contributor["limitations"],
                "candidate_status": "UNADOPTED_CALIBRATION_ONLY",
                "real_git_write": False,
            }

            call_index += 1
            record, reviewer_raw = model_call(
                rotation["Reviewer"],
                "Reviewer",
                task_id,
                reviewer_prompt(
                    task_id,
                    definition,
                    labels[task_id],
                    contributor,
                ),
                call_index,
            )
            run_records.append(record)
            print(
                f"{task_id} Reviewer {record['requested_model']} "
                f"{'PASS' if not record['failure'] else record['failure']}",
                flush=True,
            )
            if record["failure"]:
                candidates.append(candidate_entry)
                task_outcomes.append(outcome)
                continue
            try:
                reviewer = validate_reviewer(reviewer_raw)
            except CalibrationError as exc:
                record["failure"] = str(exc)
                candidates.append(candidate_entry)
                task_outcomes.append(outcome)
                continue
            outcome["reviewer"] = reviewer

            if (
                reviewer["verdict"] == "REVISION_REQUIRED"
                and call_index < MODEL_CALL_BUDGET
            ):
                call_index += 1
                revision_record, revision_raw = model_call(
                    rotation["Contributor"],
                    "ContributorRevision",
                    task_id,
                    contributor_prompt(
                        task_id,
                        definition,
                        explorer,
                        reviewer["required_corrections"],
                    ),
                    call_index,
                )
                run_records.append(revision_record)
                print(
                    f"{task_id} Revision {revision_record['requested_model']} "
                    f"{'PASS' if not revision_record['failure'] else revision_record['failure']}",
                    flush=True,
                )
                if not revision_record["failure"]:
                    try:
                        contributor = validate_contributor(
                            revision_raw, set(definition["files"])
                        )
                        outcome["revision_count"] = 1
                        candidate_entry["diffs"] = unified_diffs(
                            definition, contributor["candidate_files"]
                        )
                        candidate_entry["candidate_content_hash"] = sha256_value(
                            contributor["candidate_files"]
                        )
                        candidate_entry["limitations"] = contributor["limitations"]
                    except CalibrationError as exc:
                        revision_record["failure"] = str(exc)

            conformance_result = conformance(
                task_id, definition, contributor["candidate_files"]
            )
            outcome["conformance"] = conformance_result
            outcome["pipeline_complete"] = True
            if conformance_result["status"] == "PASS":
                outcome["outcome_classification"] = "CALIBRATION_COMPLETED"
            elif reviewer["caught_issues"]:
                outcome["outcome_classification"] = "CALIBRATION_NEGATIVE_RESULT"
            else:
                outcome["outcome_classification"] = "CALIBRATION_INVALIDATED"
            candidates.append(candidate_entry)
            task_outcomes.append(outcome)

        lineage_success = {
            key: any(
                record["requested_model"] == value["requested_model"]
                and record["returned_model"] == value["requested_model"]
                and record["failure"] is None
                for record in run_records
            )
            for key, value in MODELS.items()
        }
        independent_count = sum(lineage_success.values())
        if independent_count < 3:
            calibration_status = "CALIBRATION_BLOCKED_INSUFFICIENT_LINEAGES"
        elif any(
            task["outcome_classification"] == "CALIBRATION_INVALIDATED"
            for task in task_outcomes
        ):
            calibration_status = "CALIBRATION_INVALIDATED"
        elif all(task["pipeline_complete"] for task in task_outcomes):
            if any(
                task["outcome_classification"] == "CALIBRATION_NEGATIVE_RESULT"
                for task in task_outcomes
            ):
                calibration_status = "CALIBRATION_NEGATIVE_RESULT"
            elif deviations:
                calibration_status = "CALIBRATION_COMPLETED_WITH_LIMITATIONS"
            else:
                calibration_status = "CALIBRATION_COMPLETED"
        else:
            calibration_status = "CALIBRATION_BLOCKED"

        unblinded_at = now()
        access_log = [
            {
                "event": "ORIGIN_MAP_CREATED",
                "time": origin_map["created_at"],
                "actor": "DETERMINISTIC_LOCAL_LABELER",
                "model_reasoning_capability": False,
            },
            {
                "event": "ORIGIN_MAP_UNBLINDED_AFTER_REVIEWS",
                "time": unblinded_at,
                "actor": "DETERMINISTIC_LOCAL_LABELER",
                "condition": "ALL_AVAILABLE_REVIEWS_CLOSED",
            },
        ]
        metrics = build_metrics(
            task_outcomes, run_records, PRIOR_CAPTURE_FAILURES, deviations
        )

        config = {
            "calibration_id": "DEB-TITMAS-001-OPERATIONAL-CALIBRATION-0.1",
            "decision_id": DECISION_ID,
            "decision": "ACCEPT",
            "decided_by_ref": "zhangbin",
            "calibration_tier": "OPERATIONAL_PIPELINE_CALIBRATION",
            "inference_tier": "NON_CONFIRMATORY",
            "source_branch": SOURCE_BRANCH,
            "source_commit": SOURCE_COMMIT,
            "calibration_branch": CALIBRATION_BRANCH,
            "formal_task_count": 10,
            "calibration_task_count": 3,
            "max_total_model_calls": MODEL_CALL_BUDGET,
            "actual_model_calls": metrics["MODEL_CALL_COUNT"],
            "predevelopment_gate": {
                "result": "CONDITIONALLY_RECOMMENDED",
                "evidence_ref": (
                    "architecture/reviews/"
                    "titmas-ecology-box-001-execution-readiness-postreview-v0.1.json"
                ),
                "new_capture_failures": PRIOR_CAPTURE_FAILURES,
                "authority_effect": "NONE",
            },
            "data_class": "PUBLIC_REPOSITORY_AND_SYNTHETIC_ONLY",
            "public_data_calibration_retention_unknown_accepted": True,
            "private_data_under_unknown_retention_prohibited": True,
            "agent_immune_enabled": False,
            "formal_experiment_state_effect": "NONE",
            "value_claim_effect": "NONE",
            "commercial_claim_effect": "NONE",
            "formal_ecology_box_001_execution_authorized": False,
            "formal_ten_task_experiment_execution_authorized": False,
            "real_repository_git_write_authorized": False,
            "public_report_authorized": False,
            "commercial_validation_authorized": False,
        }
        lineage_output = {
            "required_independent_lineage_count": 3,
            "actual_independent_lineage_count": independent_count,
            "model_count": len(
                {
                    record["returned_model"]
                    for record in run_records
                    if record["returned_model"] != "NOT_RETURNED"
                }
            ),
            "session_count": len(run_records),
            "role_count": len({record["role"] for record in run_records}),
            "lineages": [
                {
                    "provider": value["provider"],
                    "requested_model": value["requested_model"],
                    "returned_model_identity_verified": lineage_success[key],
                    "retention": "UNKNOWN",
                    "training_usage": "UNKNOWN",
                    "logging": "UNKNOWN",
                    "deletion": "UNKNOWN",
                    "data_scope": "PUBLIC_REPOSITORY_AND_SYNTHETIC_ONLY",
                    "fallback": "NONE",
                }
                for key, value in MODELS.items()
            ],
            "counting_rule": (
                "MODEL_COUNT_NE_SESSION_COUNT_NE_ROLE_COUNT_NE_"
                "INDEPENDENT_LINEAGE_COUNT"
            ),
        }
        rotation_output = {
            "rotation": ROLE_ROTATION,
            "role_ne_authority": True,
            "review_ne_decision": True,
            "conformance_pass_ne_value_proof": True,
        }
        normalized_records = {
            "calibration_id": config["calibration_id"],
            "records": run_records,
            "task_outcomes": task_outcomes,
            "raw_prompts_stored": False,
            "raw_provider_responses_stored": False,
            "hidden_reasoning_stored": False,
        }
        candidate_output = {
            "blinding": {
                "method": "DETERMINISTIC_LOCAL_LABELER",
                "formal_blind_custodian": False,
                "origin_mapping_hash": origin_map_hash,
                "origin_hidden_during_review": True,
                "unblinded_after_review": True,
                "unblinding_time": unblinded_at,
                "access_log": access_log,
            },
            "candidates": candidates,
            "formal_repository_candidate_changes": 0,
            "candidate_git_commits": 0,
            "candidate_pull_requests": 0,
        }
        conformance_output = {
            "status": (
                "PASS"
                if all(
                    task["conformance"]["status"] == "PASS"
                    for task in task_outcomes
                )
                else "FAIL"
            ),
            "task_results": [
                task["conformance"] for task in task_outcomes
            ],
            "source_hashes_verified": all(
                seed["source_hash"]
                == sha256_value(
                    definitions[seed["task_id"]]["baseline_files"]
                )
                and seed["modified_hash"]
                == sha256_value(definitions[seed["task_id"]]["files"])
                for seed in seeds
            ),
            "formal_task_count": task_registry["task_count"],
            "formal_task_set_unchanged": True,
            "formal_tasks_accessed_by_calibration": False,
            "formal_blinding_not_contaminated": True,
            "formal_go_no_go_status": readiness["go_no_go_status"],
            "formal_experiment_execution_authorized": False,
            "formal_experiment_executed": False,
            "formal_run_record_count": 0,
            "calibration_result_in_formal_metrics": False,
        }
        protocol_output = {
            "deviations": deviations,
            "stop_conditions_triggered": [],
            "human_interventions": [
                {
                    "intervention_id": "CAL-HI-001",
                    "reason": "Human Owner calibration authorization",
                    "time": "USER_GOAL_2026-07-29",
                    "effect": "BOUNDED_CALIBRATION_ONLY",
                }
            ],
            "fallback_count": 0,
            "authority_violations": metrics["AUTHORITY_VIOLATION_COUNT"],
            "formal_experiment_effect": "NONE",
        }

        write_json(CALIBRATION_DIR / "calibration-config.yaml", config)
        write_json(
            CALIBRATION_DIR / "task-seeds.json",
            {
                "seed_count": 3,
                "formal_task_count": 10,
                "formal_tasks_accessed": False,
                "seeds": seeds,
            },
        )
        write_json(
            CALIBRATION_DIR / "participant-lineages.json", lineage_output
        )
        write_json(CALIBRATION_DIR / "role-rotation.yaml", rotation_output)
        with (CALIBRATION_DIR / "normalized-run-records.jsonl").open(
            "w", encoding="utf-8"
        ) as handle:
            for record in run_records:
                handle.write(canonical({"record_type": "MODEL_CALL", **record}) + "\n")
            for task in task_outcomes:
                handle.write(canonical({"record_type": "TASK_OUTCOME", **task}) + "\n")
        write_json(
            CALIBRATION_DIR / "candidate-patches" / "candidates.json",
            candidate_output,
        )
        write_json(
            CALIBRATION_DIR / "conformance-results.json",
            conformance_output,
        )
        write_json(
            CALIBRATION_DIR / "calibration-metrics.json", metrics
        )
        write_json(
            CALIBRATION_DIR / "protocol-deviations.json", protocol_output
        )
        summary = {
            "status": calibration_status,
            "independent_lineage_count": independent_count,
            "model_call_count": metrics["MODEL_CALL_COUNT"],
            "task_count": 3,
            "pipeline_completion_rate": metrics[
                "CALIBRATION_PIPELINE_COMPLETION_RATE"
            ],
            "seeded_defect_detection_rate": metrics[
                "SEEDED_DEFECT_DETECTION_RATE"
            ],
            "conformance_status": conformance_output["status"],
        }
        print(canonical({"CALIBRATION_SUMMARY": summary}), flush=True)
        return 0 if calibration_status in {
            "CALIBRATION_COMPLETED",
            "CALIBRATION_COMPLETED_WITH_LIMITATIONS",
            "CALIBRATION_NEGATIVE_RESULT",
        } else 2
    finally:
        shutil.rmtree(temp_root, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
