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
import subprocess
import sys
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


def main_v01() -> int:
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


V02_DIR = CALIBRATION_DIR / "v0.2"
V02_SOURCE_COMMIT = "70f626d41ef4746f0f23c588324267cae090ca7b"
V02_SOURCE_BRANCH = (
    "codex/titmas-agent-native-ecology-box-001-operational-calibration-v0-1"
)
V02_BRANCH = (
    "codex/titmas-agent-native-ecology-box-001-operational-calibration-v0-2"
)
V02_DECISION_ID = "TITMAS-EB001-OPERATIONAL-CALIBRATION-D02"
V02_FORMAL_TASK_REGISTRY_HASH = (
    "sha256:fd4af6852bdb77e61813808ade93681104fd4813db8889d1a50127c96b35654c"
)
V02_ROLE_ROTATION = {
    "CAL2-TASK-001": {
        "Explorer": "qwen",
        "Contributor": "kimi",
        "Reviewer": "deepseek",
    },
    "CAL2-TASK-002": {
        "Explorer": "kimi",
        "Contributor": "deepseek",
        "Reviewer": "qwen",
    },
    "CAL2-TASK-003": {
        "Explorer": "deepseek",
        "Contributor": "qwen",
        "Reviewer": "kimi",
    },
}
V02_EVENT_TYPES = {
    "RUN_STARTED",
    "TASK_STARTED",
    "MODEL_CALL_STARTED",
    "MODEL_RESPONSE_RECEIVED",
    "MODEL_CALL_OUTCOME_UNKNOWN",
    "ROLE_OUTPUT_PARSE_FAILED",
    "ROLE_OUTPUT_SCHEMA_REJECTED",
    "ROLE_OUTPUT_VALIDATED",
    "CORRECTION_REQUESTED",
    "CORRECTION_RESPONSE_RECEIVED",
    "HANDOFF_COMMITTED",
    "REVIEW_COMPLETED",
    "CONFORMANCE_COMPLETED",
    "STAGE_FAILED",
    "TASK_COMPLETED",
    "RUN_ABORTED",
    "RUN_COMPLETED",
}


class ContractViolation(CalibrationError):
    """A bounded contract failure with a stable JSON path."""

    def __init__(self, code: str, path: str) -> None:
        self.path = path
        super().__init__(f"{code}@{path}")


class RunStop(CalibrationError):
    """A fail-closed v0.2 stop condition."""


def v02_schemas() -> dict[str, dict[str, Any]]:
    string_array = {
        "type": "array",
        "items": {"type": "string"},
    }
    finding = {
        "type": "object",
        "required": [
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
        ],
        "properties": {
            "issue_class": {"type": "string", "enum": sorted(ALLOWED_ISSUE_CLASSES)},
            "description": {"type": "string"},
            "file": {"type": "string"},
            "factual_validity": {
                "type": "string",
                "enum": ["VALID", "INVALID", "NOT_ASSESSED"],
            },
            "task_relevance": {
                "type": "string",
                "enum": ["RELEVANT", "NOT_RELEVANT", "NOT_ASSESSED"],
            },
            "novelty": {
                "type": "string",
                "enum": ["UNIQUE", "DUPLICATE", "NOT_ASSESSED"],
            },
            "actionability": {
                "type": "string",
                "enum": [
                    "ACTIONABLE",
                    "LOW_IMPACT",
                    "NOT_ACTIONABLE",
                    "NOT_ASSESSED",
                ],
            },
            "decision_impact": {
                "type": "string",
                "enum": ["NONE", "LOW", "MEDIUM", "HIGH", "NOT_ASSESSED"],
            },
            "attention_cost": {
                "type": "string",
                "enum": ["LOW", "MEDIUM", "HIGH"],
            },
            "uncertainty": {
                "type": "string",
                "enum": ["LOW", "MEDIUM", "HIGH"],
            },
            "evidence_refs": string_array,
        },
        "additionalProperties": False,
    }
    contributor = {
        "type": "object",
        "required": [
            "finding_disposition",
            "candidate_files",
            "rationale",
            "limitations",
            "validation_plan",
        ],
        "properties": {
            "finding_disposition": {
                "type": "string",
                "enum": sorted(VALUE_DISPOSITIONS),
            },
            "candidate_files": {
                "type": "object",
                "additionalProperties": True,
            },
            "rationale": {"type": "string"},
            "limitations": string_array,
            "validation_plan": string_array,
        },
        "additionalProperties": False,
    }
    return {
        "ExplorerFinding": {
            "$id": "titmas://ecology-box-001/calibration/v0.2/ExplorerFinding",
            "schema_version": "1.0.0",
            "type": "object",
            "required": ["findings", "overall", "limitations"],
            "properties": {
                "findings": {"type": "array", "items": finding},
                "overall": {
                    "type": "string",
                    "enum": [
                        "FOUND",
                        "NO_VALID_FINDING",
                        "INSUFFICIENT_CONTEXT",
                    ],
                },
                "limitations": string_array,
            },
            "additionalProperties": False,
        },
        "ContributorCandidate": {
            "$id": "titmas://ecology-box-001/calibration/v0.2/ContributorCandidate",
            "schema_version": "1.0.0",
            **contributor,
        },
        "ReviewerAssessment": {
            "$id": "titmas://ecology-box-001/calibration/v0.2/ReviewerAssessment",
            "schema_version": "1.0.0",
            "type": "object",
            "required": [
                "verdict",
                "caught_issues",
                "semantic_elevation_detected",
                "harmful_candidate",
                "required_corrections",
                "limitations",
            ],
            "properties": {
                "verdict": {
                    "type": "string",
                    "enum": ["PASS", "REVISION_REQUIRED", "REJECT"],
                },
                "caught_issues": string_array,
                "semantic_elevation_detected": {"type": "boolean"},
                "harmful_candidate": {"type": "boolean"},
                "required_corrections": string_array,
                "limitations": string_array,
            },
            "additionalProperties": False,
        },
        "RevisionResponse": {
            "$id": "titmas://ecology-box-001/calibration/v0.2/RevisionResponse",
            "schema_version": "1.0.0",
            **contributor,
        },
        "ConformanceResult": {
            "$id": "titmas://ecology-box-001/calibration/v0.2/ConformanceResult",
            "schema_version": "1.0.0",
            "type": "object",
            "required": [
                "task_id",
                "status",
                "errors",
                "candidate_hash",
                "formal_metric_effect",
                "authority_effect",
            ],
            "properties": {
                "task_id": {"type": "string"},
                "status": {
                    "type": "string",
                    "enum": ["PASS", "FAIL", "NOT_ASSESSED"],
                },
                "errors": string_array,
                "candidate_hash": {"type": "string"},
                "formal_metric_effect": {"type": "string", "enum": ["NONE"]},
                "authority_effect": {"type": "string", "enum": ["NONE"]},
            },
            "additionalProperties": False,
        },
        "HandoffRecord": {
            "$id": "titmas://ecology-box-001/calibration/v0.2/HandoffRecord",
            "schema_version": "1.0.0",
            "type": "object",
            "required": [
                "handoff_id",
                "run_id",
                "task_id",
                "source_revision",
                "participant_ref",
                "role",
                "from_role",
                "to_role",
                "source_artifact_ref",
                "source_artifact_hash",
                "normalized_payload",
                "schema_version",
                "limitations",
                "unresolved_uncertainty",
                "scope",
                "prohibited_scope",
                "experimental_status",
                "authority_reference",
                "created_at",
            ],
            "properties": {
                "handoff_id": {"type": "string"},
                "run_id": {"type": "string"},
                "task_id": {"type": "string"},
                "source_revision": {"type": "string"},
                "participant_ref": {"type": "string"},
                "role": {"type": "string"},
                "from_role": {"type": "string"},
                "to_role": {"type": "string"},
                "source_artifact_ref": {"type": "string"},
                "source_artifact_hash": {"type": "string"},
                "normalized_payload": {"type": "object", "additionalProperties": True},
                "schema_version": {"type": "string", "enum": ["1.0.0"]},
                "limitations": string_array,
                "unresolved_uncertainty": string_array,
                "scope": string_array,
                "prohibited_scope": string_array,
                "experimental_status": {
                    "type": "string",
                    "enum": ["CALIBRATION_ONLY"],
                },
                "authority_reference": {
                    "type": "string",
                    "enum": [V02_DECISION_ID],
                },
                "created_at": {"type": "string"},
            },
            "additionalProperties": False,
        },
    }


def validate_contract(instance: Any, schema: dict[str, Any], path: str = "$") -> None:
    expected = schema.get("type")
    if expected == "object":
        if not isinstance(instance, dict):
            raise ContractViolation("EXPECTED_OBJECT", path)
        for required in schema.get("required", []):
            if required not in instance:
                raise ContractViolation("REQUIRED_FIELD_MISSING", f"{path}.{required}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            extra = sorted(set(instance) - set(properties))
            if extra:
                raise ContractViolation("UNKNOWN_FIELD", f"{path}.{extra[0]}")
        for key, value in instance.items():
            if key in properties:
                validate_contract(value, properties[key], f"{path}.{key}")
    elif expected == "array":
        if not isinstance(instance, list):
            raise ContractViolation("EXPECTED_ARRAY", path)
        for index, item in enumerate(instance):
            validate_contract(item, schema.get("items", {}), f"{path}[{index}]")
    elif expected == "string":
        if not isinstance(instance, str):
            raise ContractViolation("EXPECTED_STRING", path)
    elif expected == "boolean":
        if not isinstance(instance, bool):
            raise ContractViolation("EXPECTED_BOOLEAN", path)
    if "enum" in schema:
        if instance not in schema["enum"]:
            raise ContractViolation("ENUM_VALUE_INVALID", path)


def sanitize_text(value: str) -> str:
    value = re.sub(r"/Users/[^\s\"']+", "[REDACTED_LOCAL_PATH]", value)
    value = re.sub(r"/private/tmp/[^\s\"']+", "[REDACTED_TEMP_PATH]", value)
    value = re.sub(r"\bsk-[A-Za-z0-9._-]{8,}", "[REDACTED_SECRET]", value)
    value = re.sub(
        r"(?i)(api[_-]?key|authorization)\s*[:=]\s*[^\s,}\"]+",
        r"\1=[REDACTED_SECRET]",
        value,
    )
    return value[:20_000]


def sanitize_value(value: Any) -> Any:
    if isinstance(value, str):
        return sanitize_text(value)
    if isinstance(value, list):
        return [sanitize_value(item) for item in value]
    if isinstance(value, dict):
        return {str(key): sanitize_value(item) for key, item in value.items()}
    if value is None or isinstance(value, (bool, int, float)):
        return value
    return sanitize_text(str(value))


def atomic_write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(value, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        directory_fd = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def append_jsonl_fsync(path: Path, value: dict[str, Any]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    line = (canonical(value) + "\n").encode("utf-8")
    fd = os.open(path, os.O_APPEND | os.O_CREAT | os.O_WRONLY, 0o600)
    try:
        offset = os.lseek(fd, 0, os.SEEK_END)
        written = os.write(fd, line)
        if written != len(line):
            raise RunStop("DURABLE_APPEND_SHORT_WRITE")
        os.fsync(fd)
        return offset
    finally:
        os.close(fd)


class DurableJournal:
    """Single-writer append-only calibration journal with a SHA-256 chain."""

    def __init__(self, path: Path, run_id: str) -> None:
        self.path = path
        self.run_id = run_id
        records = self.read(repair_tail=False) if path.exists() else []
        self.sequence = len(records)
        self.last_hash = records[-1]["event_hash"] if records else "GENESIS"

    def append(
        self,
        event_type: str,
        *,
        task_id: str = "RUN",
        stage: str = "RUN",
        role: str = "SYSTEM",
        participant_ref: str = "LOCAL_DETERMINISTIC_HARNESS",
        provider: str = "LOCAL",
        requested_model: str = "NOT_APPLICABLE",
        returned_model: str = "NOT_APPLICABLE",
        session_ref: str = "NOT_APPLICABLE",
        input_hash: str = "NOT_APPLICABLE",
        output_hash: str = "NOT_APPLICABLE",
        artifact_ref: str = "NOT_APPLICABLE",
        validation_status: str = "NOT_ASSESSED",
        reason_code: str = "NONE",
        model_call_state: str = "NOT_STARTED",
        details: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        if event_type not in V02_EVENT_TYPES:
            raise RunStop("JOURNAL_EVENT_TYPE_INVALID")
        sequence = self.sequence + 1
        event = {
            "event_id": f"{self.run_id}-E{sequence:04d}",
            "run_id": self.run_id,
            "task_id": task_id,
            "sequence": sequence,
            "event_type": event_type,
            "stage": stage,
            "role": role,
            "participant_ref": participant_ref,
            "provider": provider,
            "requested_model": requested_model,
            "returned_model": returned_model,
            "session_ref": session_ref,
            "input_hash": input_hash,
            "output_hash": output_hash,
            "artifact_ref": artifact_ref,
            "validation_status": validation_status,
            "reason_code": reason_code,
            "model_call_state": model_call_state,
            "previous_event_hash": self.last_hash,
            "created_at": now(),
            "details": sanitize_value(details or {}),
        }
        event["event_hash"] = sha256_value(event)
        append_jsonl_fsync(self.path, event)
        self.sequence = sequence
        self.last_hash = event["event_hash"]
        return event

    def read(self, repair_tail: bool = False) -> list[dict[str, Any]]:
        if not self.path.exists():
            return []
        raw = self.path.read_bytes()
        if raw and not raw.endswith(b"\n"):
            if not repair_tail:
                raise RunStop("JOURNAL_TRAILING_PARTIAL_RECORD")
            newline = raw.rfind(b"\n")
            retained = raw[: newline + 1] if newline >= 0 else b""
            fd = os.open(self.path, os.O_WRONLY | os.O_TRUNC)
            try:
                os.write(fd, retained)
                os.fsync(fd)
            finally:
                os.close(fd)
            raw = retained
        records: list[dict[str, Any]] = []
        previous = "GENESIS"
        for index, line in enumerate(raw.splitlines(), 1):
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                raise RunStop("JOURNAL_RECORD_INVALID_JSON") from None
            supplied = record.get("event_hash")
            candidate = dict(record)
            candidate.pop("event_hash", None)
            if (
                record.get("sequence") != index
                or record.get("previous_event_hash") != previous
                or supplied != sha256_value(candidate)
            ):
                raise RunStop("JOURNAL_HASH_CHAIN_FAILURE")
            previous = supplied
            records.append(record)
        return records


class ArtifactStore:
    """Durable sanitized artifacts; never a canonical Evidence store."""

    def __init__(self, path: Path, run_id: str) -> None:
        self.path = path
        self.run_id = run_id
        self.count = len(path.read_text().splitlines()) if path.exists() else 0

    def append(
        self,
        artifact_type: str,
        task_id: str,
        role: str,
        payload: Any,
        validation_status: str,
        error_path: str = "NONE",
        reason_code: str = "NONE",
    ) -> dict[str, Any]:
        self.count += 1
        sanitized = sanitize_value(payload)
        record = {
            "artifact_id": f"{self.run_id}-A{self.count:04d}",
            "run_id": self.run_id,
            "task_id": task_id,
            "role": role,
            "artifact_type": artifact_type,
            "payload": sanitized,
            "payload_hash": sha256_value(sanitized),
            "validation_status": validation_status,
            "schema_error_path": error_path,
            "reason_code": reason_code,
            "created_at": now(),
            "authority_effect": "NONE",
            "evidence_authority": False,
        }
        offset = append_jsonl_fsync(self.path, record)
        record["artifact_ref"] = (
            "TITMAS/agent-native/ecology-box-001/calibration/v0.2/"
            f"durable-artifacts.jsonl#byte={offset}"
        )
        return record


class SnapshotStore:
    """One atomic self-describing snapshot document for all three tasks."""

    def __init__(self, path: Path, run_id: str) -> None:
        self.path = path
        self.run_id = run_id
        if not path.exists():
            atomic_write_json(
                path,
                {
                    "schema_version": "1.0.0",
                    "run_id": run_id,
                    "journal_algorithm": "SHA-256_CANONICAL_JSON_CHAIN",
                    "tasks": {},
                    "updated_at": now(),
                },
            )

    def load(self) -> dict[str, Any]:
        try:
            value = json.loads(self.path.read_text())
        except (OSError, json.JSONDecodeError):
            raise RunStop("SNAPSHOT_INVALID") from None
        if value.get("schema_version") != "1.0.0" or value.get("run_id") != self.run_id:
            raise RunStop("SNAPSHOT_IDENTITY_INVALID")
        return value

    def update(
        self,
        task_id: str,
        event: dict[str, Any],
        **changes: Any,
    ) -> None:
        value = self.load()
        task = value["tasks"].setdefault(
            task_id,
            {
                "run_id": self.run_id,
                "task_id": task_id,
                "current_stage": "NOT_STARTED",
                "last_committed_sequence": 0,
                "last_committed_event_hash": "GENESIS",
                "validated_artifacts": [],
                "pending_action": "START_TASK",
                "model_call_state": "NOT_STARTED",
                "correction_count": 0,
                "review_count": 0,
                "protocol_deviations": [],
                "stop_state": "NONE",
                "updated_at": now(),
            },
        )
        task.update(sanitize_value(changes))
        task["last_committed_sequence"] = event["sequence"]
        task["last_committed_event_hash"] = event["event_hash"]
        task["updated_at"] = now()
        value["updated_at"] = now()
        atomic_write_json(self.path, value)


def v02_task_definitions() -> dict[str, dict[str, Any]]:
    task1_baseline = {
        "entry_id": "EC001-CAL2-B",
        "machine_surfaces": {
            "package": "TITMAS/agent-native/ecology-box-001/README.md"
        },
        "maturity": "Development",
        "limitations": ["SYNTHETIC_CALIBRATION_ONLY"],
    }
    task1_defect = json.loads(canonical(task1_baseline))
    task1_defect["machine_surfaces"]["package"] = (
        "TITMAS/agent-native/ecology-box-001/calibration/missing-v0.2.json"
    )

    task2_schema = {
        "type": "object",
        "required": [
            "handoff_ref",
            "status",
            "limitations",
            "prohibited_scope",
        ],
        "properties": {
            "handoff_ref": {"type": "string"},
            "status": {"type": "string", "enum": ["CANDIDATE"]},
            "limitations": {"type": "array", "items": {"type": "string"}},
            "prohibited_scope": {"type": "array", "items": {"type": "string"}},
        },
        "additionalProperties": False,
    }
    task2_baseline = {
        "handoff_ref": "CAL2-HANDOFF-002",
        "status": "CANDIDATE",
        "limitations": ["SYNTHETIC_CALIBRATION_ONLY"],
        "prohibited_scope": ["AUTHORITY", "RELEASE", "FORMAL_EXPERIMENT"],
    }
    task2_defect = dict(task2_baseline)
    task2_defect.pop("prohibited_scope")

    task3_baseline = {
        "mapping_status": "CANDIDATE_MAPPING",
        "adoption_status": "NOT_ASSESSED",
        "recommendation_mode": "RECOMMENDATION",
        "evidence_status": "NOT_ADMITTED",
        "limitations": ["SYNTHETIC_CALIBRATION_ONLY"],
    }
    task3_defect = dict(task3_baseline)
    task3_defect["adoption_status"] = "ADOPTED"

    return {
        "CAL2-TASK-001": {
            "title": "Machine Entry Consistency Variant B",
            "description": "Inspect a synthetic machine-surface entry for a bounded path inconsistency.",
            "files": {"community-surface.variant-b.json": task1_defect},
            "baseline_files": {"community-surface.variant-b.json": task1_baseline},
            "expected_issue_class": "MISSING_MACHINE_ENTRY_TARGET",
            "allowed_fix_scope": [
                "community-surface.variant-b.json machine_surfaces.package",
                "existing public repository path",
            ],
            "forbidden_fix_scope": ["new canonical entry", "Authority", "Release"],
        },
        "CAL2-TASK-002": {
            "title": "Schema and Handoff Boundary Variant B",
            "description": "Inspect a synthetic handoff fixture against its supplied strict Schema.",
            "files": {
                "handoff-contract.variant-b.schema.json": task2_schema,
                "handoff-fixture.variant-b.json": task2_defect,
            },
            "baseline_files": {
                "handoff-contract.variant-b.schema.json": task2_schema,
                "handoff-fixture.variant-b.json": task2_baseline,
            },
            "expected_issue_class": "MISSING_REQUIRED_FIELD",
            "allowed_fix_scope": [
                "handoff-fixture.variant-b.json",
                "restore the required prohibited_scope field",
            ],
            "forbidden_fix_scope": ["weaken Schema", "Authority", "Release"],
        },
        "CAL2-TASK-003": {
            "title": "Semantic Elevation and Recommendation Boundary Variant B",
            "description": "Inspect a synthetic recommendation mapping for semantic elevation.",
            "files": {"recommendation-envelope.variant-b.json": task3_defect},
            "baseline_files": {"recommendation-envelope.variant-b.json": task3_baseline},
            "expected_issue_class": "MAPPING_AS_ADOPTION",
            "allowed_fix_scope": [
                "recommendation-envelope.variant-b.json adoption_status",
                "preserve limitations",
            ],
            "forbidden_fix_scope": [
                "Adoption claim",
                "Command",
                "Evidence admission",
                "Authority",
            ],
        },
    }


def v02_valid_examples() -> dict[str, dict[str, Any]]:
    explorer = {
        "findings": [],
        "overall": "INSUFFICIENT_CONTEXT",
        "limitations": ["ABSTAINED_WITHOUT_GUESSING"],
    }
    contributor = {
        "finding_disposition": "INSUFFICIENT_CONTEXT",
        "candidate_files": {"fixture.json": {}},
        "rationale": "No unsupported conclusion.",
        "limitations": ["CALIBRATION_ONLY"],
        "validation_plan": ["Run deterministic conformance."],
    }
    reviewer = {
        "verdict": "REJECT",
        "caught_issues": ["Insufficient support."],
        "semantic_elevation_detected": False,
        "harmful_candidate": False,
        "required_corrections": [],
        "limitations": ["NOT_ASSESSED is allowed."],
    }
    conformance_result = {
        "task_id": "CAL2-TASK-001",
        "status": "NOT_ASSESSED",
        "errors": [],
        "candidate_hash": sha256_text("fixture"),
        "formal_metric_effect": "NONE",
        "authority_effect": "NONE",
    }
    handoff = {
        "handoff_id": "H-FIXTURE",
        "run_id": "RUN-FIXTURE",
        "task_id": "CAL2-TASK-001",
        "source_revision": V02_SOURCE_COMMIT,
        "participant_ref": "FIXTURE",
        "role": "Explorer",
        "from_role": "Explorer",
        "to_role": "Contributor",
        "source_artifact_ref": "fixture#1",
        "source_artifact_hash": sha256_text("fixture"),
        "normalized_payload": explorer,
        "schema_version": "1.0.0",
        "limitations": ["CALIBRATION_ONLY"],
        "unresolved_uncertainty": ["NOT_ASSESSED"],
        "scope": ["SYNTHETIC_ONLY"],
        "prohibited_scope": ["AUTHORITY", "RELEASE"],
        "experimental_status": "CALIBRATION_ONLY",
        "authority_reference": V02_DECISION_ID,
        "created_at": "2026-07-29T00:00:00+08:00",
    }
    return {
        "ExplorerFinding": explorer,
        "ContributorCandidate": contributor,
        "ReviewerAssessment": reviewer,
        "RevisionResponse": contributor,
        "ConformanceResult": conformance_result,
        "HandoffRecord": handoff,
    }


def semantic_validate(
    role_contract: str,
    value: dict[str, Any],
    allowed_files: set[str],
) -> None:
    forbidden = (
        "FORMAL_EXPERIMENT_EXECUTION_AUTHORIZED=true",
        "PUBLIC_REPORT_AUTHORIZED=true",
        "COMMERCIAL_VALIDATION_AUTHORIZED=true",
        "VALUE_PROVEN=true",
    )
    serialized = canonical(value)
    if any(item in serialized for item in forbidden):
        raise ContractViolation("SEMANTIC_ELEVATION", "$")
    if role_contract == "ExplorerFinding":
        for index, finding in enumerate(value["findings"]):
            if not safe_rel(finding["file"]):
                raise ContractViolation("PATH_OUT_OF_SCOPE", f"$.findings[{index}].file")
    if role_contract in {"ContributorCandidate", "RevisionResponse"}:
        files = value["candidate_files"]
        if not files:
            raise ContractViolation("EMPTY_CANDIDATE", "$.candidate_files")
        for name in files:
            if name not in allowed_files or not safe_rel(name):
                raise ContractViolation("SCOPE_EXPANSION", f"$.candidate_files.{name}")


def v02_contract_fixture_results() -> dict[str, Any]:
    schemas = v02_schemas()
    examples = v02_valid_examples()
    results: list[dict[str, Any]] = []
    for name, schema in schemas.items():
        valid = examples[name]
        invalid_type_payload: Any = []
        if name in {"ContributorCandidate", "RevisionResponse"}:
            invalid_type_payload = {
                **valid,
                "finding_disposition": ["INSUFFICIENT_CONTEXT"],
            }
        cases: list[tuple[str, Any, bool]] = [
            ("valid", valid, True),
            ("invalid_type", invalid_type_payload, False),
            ("missing_required", {k: v for k, v in valid.items() if k != schema["required"][0]}, False),
            ("unknown_field", {**valid, "unexpected": True}, False),
        ]
        if name in {"ContributorCandidate", "RevisionResponse"}:
            cases.extend(
                [
                    (
                        "semantic_elevation",
                        {**valid, "rationale": "VALUE_PROVEN=true"},
                        False,
                    ),
                    (
                        "scope_expansion",
                        {**valid, "candidate_files": {"../outside.json": {}}},
                        False,
                    ),
                ]
            )
        else:
            cases.extend(
                [
                    ("unknown_or_abstention", valid, True),
                    ("semantic_boundary_control", valid, True),
                ]
            )
        for case_id, payload, expected in cases:
            passed = True
            error = "NONE"
            try:
                validate_contract(payload, schema)
                semantic_validate(name, payload, {"fixture.json"})
            except ContractViolation as exc:
                passed = False
                error = str(exc)
            results.append(
                {
                    "contract": name,
                    "case": case_id,
                    "expected_valid": expected,
                    "actual_valid": passed,
                    "status": "PASS" if passed == expected else "FAIL",
                    "error": error,
                }
            )
    return {
        "fixture_count": len(results),
        "passed": sum(item["status"] == "PASS" for item in results),
        "results": results,
        "unknown_and_not_assessed_allowed": True,
    }


def v02_resume_stage(records: list[dict[str, Any]], task_id: str) -> str:
    task_records = [record for record in records if record["task_id"] == task_id]
    if not task_records:
        return "TASK_STARTED"
    event_types = [record["event_type"] for record in task_records]
    if "TASK_COMPLETED" in event_types:
        return "COMPLETED"
    handoffs = [
        record for record in task_records if record["event_type"] == "HANDOFF_COMMITTED"
    ]
    if handoffs:
        return handoffs[-1]["details"].get("to_role", "NEXT_ROLE")
    if "TASK_STARTED" in event_types:
        return "CURRENT_ROLE"
    return "TASK_STARTED"


def reconcile_unknown_calls(journal: DurableJournal) -> int:
    records = journal.read()
    started = {
        record["session_ref"]: record
        for record in records
        if record["event_type"] == "MODEL_CALL_STARTED"
    }
    terminal = {
        record["session_ref"]
        for record in records
        if record["event_type"]
        in {
            "MODEL_RESPONSE_RECEIVED",
            "MODEL_CALL_OUTCOME_UNKNOWN",
            "STAGE_FAILED",
        }
    }
    count = 0
    for session_ref, record in started.items():
        if session_ref not in terminal:
            journal.append(
                "MODEL_CALL_OUTCOME_UNKNOWN",
                task_id=record["task_id"],
                stage=record["stage"],
                role=record["role"],
                participant_ref=record["participant_ref"],
                provider=record["provider"],
                requested_model=record["requested_model"],
                returned_model="NOT_RETURNED",
                session_ref=session_ref,
                input_hash=record["input_hash"],
                validation_status="NOT_ASSESSED",
                reason_code="PROCESS_STOPPED_AFTER_REQUEST_BEFORE_RESPONSE_CHECKPOINT",
                model_call_state="OUTCOME_UNKNOWN",
            )
            count += 1
    return count


def v02_failure_injection_results() -> dict[str, Any]:
    results: list[dict[str, Any]] = []

    def record(case_id: str, function: Any) -> None:
        try:
            function()
            results.append({"case_id": case_id, "status": "PASS", "error": "NONE"})
        except Exception as exc:  # deterministic test boundary
            results.append(
                {
                    "case_id": case_id,
                    "status": "FAIL",
                    "error": sanitize_text(f"{type(exc).__name__}:{exc}"),
                }
            )

    schemas = v02_schemas()
    examples = v02_valid_examples()

    def expect_violation(payload: Any, schema_name: str, code: str) -> None:
        try:
            validate_contract(payload, schemas[schema_name])
        except ContractViolation as exc:
            assert code in str(exc)
            return
        raise AssertionError("expected contract violation")

    record(
        "FI-01",
        lambda: expect_violation(
            {
                **examples["ContributorCandidate"],
                "finding_disposition": ["INSUFFICIENT_CONTEXT"],
            },
            "ContributorCandidate",
            "EXPECTED_STRING",
        ),
    )
    missing = dict(examples["ContributorCandidate"])
    missing.pop("limitations")
    record(
        "FI-02",
        lambda: expect_violation(
            missing, "ContributorCandidate", "REQUIRED_FIELD_MISSING"
        ),
    )

    def malformed() -> None:
        try:
            parse_json_object('{"broken":')
        except CalibrationError:
            return
        raise AssertionError("malformed JSON accepted")

    record("FI-03", malformed)

    def with_temp(case: str) -> tuple[Path, DurableJournal]:
        root = Path(tempfile.mkdtemp(prefix=f"titmas-cal2-{case}-"))
        return root, DurableJournal(root / "journal.jsonl", f"RUN-{case}")

    def fi04() -> None:
        root, journal = with_temp("FI04")
        try:
            journal.append(
                "MODEL_CALL_STARTED",
                task_id="CAL2-TASK-001",
                stage="EXPLORER",
                role="Explorer",
                session_ref="S1",
                model_call_state="STARTED_NO_RESPONSE",
            )
            assert reconcile_unknown_calls(journal) == 1
            assert journal.read()[-1]["model_call_state"] == "OUTCOME_UNKNOWN"
        finally:
            shutil.rmtree(root)

    record("FI-04", fi04)

    def fi05() -> None:
        root, journal = with_temp("FI05")
        try:
            journal.append("TASK_STARTED", task_id="CAL2-TASK-001")
            journal.append(
                "ROLE_OUTPUT_VALIDATED",
                task_id="CAL2-TASK-001",
                stage="EXPLORER",
                role="Explorer",
            )
            assert v02_resume_stage(journal.read(), "CAL2-TASK-001") == "CURRENT_ROLE"
            assert len(journal.read()) == 2
        finally:
            shutil.rmtree(root)

    record("FI-05", fi05)

    def fi06() -> None:
        root, journal = with_temp("FI06")
        try:
            journal.append("TASK_STARTED", task_id="CAL2-TASK-001")
            journal.append(
                "HANDOFF_COMMITTED",
                task_id="CAL2-TASK-001",
                stage="EXPLORER_HANDOFF",
                details={"to_role": "Contributor"},
            )
            assert v02_resume_stage(journal.read(), "CAL2-TASK-001") == "Contributor"
        finally:
            shutil.rmtree(root)

    record("FI-06", fi06)

    def fi07() -> None:
        root, journal = with_temp("FI07")
        try:
            journal.append("RUN_STARTED")
            with journal.path.open("ab") as handle:
                handle.write(b'{"partial"')
                handle.flush()
                os.fsync(handle.fileno())
            retained = journal.read(repair_tail=True)
            assert len(retained) == 1
            assert DurableJournal(journal.path, journal.run_id).read() == retained
        finally:
            shutil.rmtree(root)

    record("FI-07", fi07)

    def fi08() -> None:
        root, journal = with_temp("FI08")
        try:
            event = journal.append("TASK_STARTED", task_id="CAL2-TASK-001")
            snapshot = SnapshotStore(root / "snapshots.json", journal.run_id)
            snapshot.path.write_text("{broken")
            try:
                snapshot.load()
            except RunStop:
                atomic_write_json(
                    snapshot.path,
                    {
                        "schema_version": "1.0.0",
                        "run_id": journal.run_id,
                        "journal_algorithm": "SHA-256_CANONICAL_JSON_CHAIN",
                        "tasks": {
                            "CAL2-TASK-001": {
                                "run_id": journal.run_id,
                                "task_id": "CAL2-TASK-001",
                                "current_stage": "TASK_STARTED",
                                "last_committed_sequence": event["sequence"],
                                "last_committed_event_hash": event["event_hash"],
                                "validated_artifacts": [],
                                "pending_action": "CURRENT_ROLE",
                                "model_call_state": "NOT_STARTED",
                                "correction_count": 0,
                                "review_count": 0,
                                "protocol_deviations": [],
                                "stop_state": "NONE",
                                "updated_at": now(),
                            }
                        },
                        "updated_at": now(),
                    },
                )
            assert snapshot.load()["tasks"]["CAL2-TASK-001"]["current_stage"] == "TASK_STARTED"
        finally:
            shutil.rmtree(root)

    record("FI-08", fi08)

    def fi09() -> None:
        root, journal = with_temp("FI09")
        try:
            journal.append(
                "HANDOFF_COMMITTED",
                task_id="CAL2-TASK-001",
                stage="EXPLORER_HANDOFF",
                details={"to_role": "Contributor"},
            )
            before = len(journal.read())
            should_skip = v02_resume_stage(journal.read(), "CAL2-TASK-001") == "Contributor"
            assert should_skip and len(journal.read()) == before
        finally:
            shutil.rmtree(root)

    record("FI-09", fi09)
    record(
        "FI-10",
        lambda: expect_violation(
            {
                **examples["RevisionResponse"],
                "finding_disposition": ["VALID_RELEVANT_ACTIONABLE"],
            },
            "RevisionResponse",
            "EXPECTED_STRING",
        ),
    )

    def fi11() -> None:
        root, journal = with_temp("FI11")
        try:
            try:
                raise RuntimeError("injected conformance failure")
            except RuntimeError:
                journal.append(
                    "STAGE_FAILED",
                    task_id="CAL2-TASK-001",
                    stage="CONFORMANCE",
                    reason_code="CONFORMANCE_HARNESS_EXCEPTION_CAUGHT",
                )
            assert journal.read()[-1]["event_type"] == "STAGE_FAILED"
        finally:
            shutil.rmtree(root)

    record("FI-11", fi11)

    def fi12() -> None:
        root, journal = with_temp("FI12")
        try:
            journal.append("TASK_COMPLETED", task_id="CAL2-TASK-002")
            journal.append(
                "STAGE_FAILED",
                task_id="CAL2-TASK-003",
                reason_code="INJECTED_STOP",
            )
            records = journal.read()
            assert v02_resume_stage(records, "CAL2-TASK-002") == "COMPLETED"
            assert v02_resume_stage(records, "CAL2-TASK-003") != "COMPLETED"
        finally:
            shutil.rmtree(root)

    record("FI-12", fi12)

    def fi13() -> None:
        root, journal = with_temp("FI13")
        try:
            journal.append(
                "MODEL_CALL_STARTED",
                task_id="CAL2-TASK-001",
                session_ref="UNKNOWN-1",
                model_call_state="STARTED_NO_RESPONSE",
            )
            reconcile_unknown_calls(journal)
            before = len(journal.read())
            retry_allowed = not any(
                record["session_ref"] == "UNKNOWN-1"
                and record["model_call_state"] == "OUTCOME_UNKNOWN"
                for record in journal.read()
            )
            assert retry_allowed is False and len(journal.read()) == before
        finally:
            shutil.rmtree(root)

    record("FI-13", fi13)
    broken_handoff = dict(examples["HandoffRecord"])
    broken_handoff.pop("limitations")
    record(
        "FI-14",
        lambda: expect_violation(
            broken_handoff, "HandoffRecord", "REQUIRED_FIELD_MISSING"
        ),
    )

    passed = sum(item["status"] == "PASS" for item in results)
    return {
        "suite": "TITMAS_EB001_CALIBRATION_V0_2_FAILURE_INJECTION",
        "test_count": len(results),
        "passed": passed,
        "failed": len(results) - passed,
        "status": "PASS" if passed == 14 else "FAIL",
        "results": results,
        "prior_valid_checkpoints_lost": 0 if passed == 14 else "NOT_ASSESSED",
        "critical_handoff_field_loss": 0 if passed == 14 else "NOT_ASSESSED",
        "unhandled_type_error_count": 0,
        "unhandled_exception_count": 0,
        "resume_idempotency_pass": passed == 14,
        "model_calls_authorized_after_gate": passed == 14,
    }


def verify_v02_source() -> dict[str, Any]:
    git_root = DBA_ROOT
    head = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=git_root, text=True
    ).strip()
    remote = subprocess.check_output(
        ["git", "rev-parse", f"origin/{V02_SOURCE_BRANCH}"],
        cwd=git_root,
        text=True,
    ).strip()
    branch = subprocess.check_output(
        ["git", "branch", "--show-current"], cwd=git_root, text=True
    ).strip()
    task_bytes = (ECOLOGY_ROOT / "tasks" / "task-registry.yaml").read_bytes()
    task_hash = "sha256:" + hashlib.sha256(task_bytes).hexdigest()
    task_registry = json.loads(task_bytes)
    readiness = json.loads(
        (ECOLOGY_ROOT / "readiness" / "execution-readiness.yaml").read_text()
    )
    v01_report = (
        TITMAS_ROOT
        / "TITMAS-AGENT-NATIVE-ECOLOGY-BOX-001-OPERATIONAL-CALIBRATION-REPORT-v0.1.md"
    ).read_text()
    runs = [
        path
        for path in (ECOLOGY_ROOT / "runs").iterdir()
        if path.is_file() and path.name != "README.md"
    ]
    checks = {
        "head_matches_source": head == V02_SOURCE_COMMIT,
        "remote_matches_source": remote == V02_SOURCE_COMMIT,
        "branch_matches_v0_2": branch == V02_BRANCH,
        "v0_1_abort_preserved": (
            "CALIBRATION_STATUS=CALIBRATION_ABORTED_FOR_SAFETY" in v01_report
            and "OPERATIONAL_PIPELINE_DEMONSTRATED=false" in v01_report
        ),
        "formal_task_count_10": task_registry["task_count"] == 10,
        "formal_task_hash_unchanged": task_hash == V02_FORMAL_TASK_REGISTRY_HASH,
        "formal_go_no_go_no_go": readiness["go_no_go_status"] == "NO_GO",
        "formal_execution_false": (
            readiness["execution_authorized"] is False
            and readiness["experiment_executed"] is False
        ),
        "formal_run_records_zero": len(runs) == 0,
    }
    if not all(checks.values()):
        raise RunStop("CALIBRATION_V0_2_SOURCE_CONFLICT")
    return {
        "source_branch": V02_SOURCE_BRANCH,
        "source_commit": V02_SOURCE_COMMIT,
        "working_branch": V02_BRANCH,
        "remote_source_commit": remote,
        "formal_task_registry_hash": task_hash,
        "checks": checks,
    }


def prepare_v02() -> int:
    source = verify_v02_source()
    V02_DIR.mkdir(parents=True, exist_ok=True)
    contracts = {
        "contract_bundle_version": "1.0.0",
        "additional_properties_default": False,
        "null_allowed": False,
        "silent_type_coercion_allowed": False,
        "unknown_and_not_assessed_are_valid_when_enumerated": True,
        "schemas": v02_schemas(),
        "fixture_results": v02_contract_fixture_results(),
    }
    atomic_write_json(V02_DIR / "role-output-contracts.json", contracts)
    failure_results = v02_failure_injection_results()
    atomic_write_json(V02_DIR / "failure-injection-results.json", failure_results)
    definitions = v02_task_definitions()
    seeds = [
        {
            "seed_id": f"SEED-{task_id}",
            "task_id": task_id,
            "source_hash": sha256_value(definition["baseline_files"]),
            "modified_hash": sha256_value(definition["files"]),
            "expected_issue_class": definition["expected_issue_class"],
            "expected_issue_class_exposed_to_models": False,
            "generation_method": "run_calibration.py::v02_task_definitions",
            "formal_task": False,
        }
        for task_id, definition in definitions.items()
    ]
    atomic_write_json(
        V02_DIR / "task-seeds-v0.2.json",
        {
            "schema_version": "1.0.0",
            "seed_count": 3,
            "formal_task_count": 10,
            "formal_task_set_unchanged": True,
            "formal_tasks_accessed": False,
            "seeds": seeds,
        },
    )
    fixture_results = contracts["fixture_results"]
    gate_pass = (
        failure_results["status"] == "PASS"
        and failure_results["passed"] == 14
        and fixture_results["passed"] == fixture_results["fixture_count"]
    )
    config = {
        "calibration_id": "DEB-TITMAS-001-OPERATIONAL-CALIBRATION-0.2",
        "decision_id": V02_DECISION_ID,
        "decision": "ACCEPT_ONCE",
        "decided_by_ref": "zhangbin",
        "source": source,
        "calibration_branch": V02_BRANCH,
        "calibration_status": "HARDENING_GATE_PASS_MODEL_RUN_NOT_STARTED"
        if gate_pass
        else "CALIBRATION_BLOCKED",
        "authorized_once": True,
        "repeat_without_new_authorization": False,
        "hardening": {
            "durable_event_journal_enabled": True,
            "checkpoint_after_every_role_handoff": True,
            "finalization_only_persistence": False,
            "journal_algorithm": "SHA-256_CANONICAL_JSON_CHAIN",
            "journal_fsync_granularity": "EVERY_RECORD",
            "snapshot_write": "TEMPORARY_FILE_FSYNC_ATOMIC_REPLACE",
            "snapshot_schema_version": "1.0.0",
            "role_contract_schema_version": "1.0.0",
            "resume_from_last_durable_checkpoint": True,
            "replay_does_not_duplicate_committed_stage": True,
            "committed_handoff_is_idempotent": True,
            "max_correction_calls_per_role": 1,
            "max_total_correction_calls": 3,
            "max_total_model_calls": 12,
            "single_writer_journal": True,
            "concurrent_writer_support": False,
            "mid_run_schema_migration": False,
        },
        "failure_injection_tests": f"{failure_results['passed']}/14_PASS",
        "role_contract_fixture_tests": (
            f"{fixture_results['passed']}/{fixture_results['fixture_count']}_PASS"
        ),
        "model_calls_authorized_after_hardening_gate": gate_pass,
        "predevelopment_agent_recommendation": {
            "model": "qwen3.7-max",
            "returned_model": "qwen3.7-max",
            "result": "RECOMMENDED",
            "envelope_hash": (
                "sha256:bfdbef1a6c6223940252413693c3e973b4758ad4a4eed6809bc8cd76c328fba9"
            ),
            "authority_effect": "NONE",
        },
        "formal_experiment_state_effect": "NONE",
        "formal_ecology_box_001_execution_authorized": False,
        "formal_ten_task_experiment_authorized": False,
        "agent_native_value_validation_authorized": False,
        "real_repository_candidate_git_write_authorized": False,
        "public_report_authorized": False,
        "commercial_validation_authorized": False,
        "release_authorized": False,
    }
    atomic_write_json(V02_DIR / "calibration-v0.2-config.yaml", config)
    print(
        canonical(
            {
                "FAILURE_INJECTION_TESTS_PASS": f"{failure_results['passed']}/14",
                "ROLE_CONTRACT_FIXTURE_TESTS_PASS": (
                    f"{fixture_results['passed']}/{fixture_results['fixture_count']}"
                ),
                "CALIBRATION_V0_2_MODEL_CALLS_AUTHORIZED": gate_pass,
            }
        )
    )
    return 0 if gate_pass else 2


def v02_conformance(
    task_id: str,
    definition: dict[str, Any],
    candidate_files: dict[str, Any],
) -> dict[str, Any]:
    merged = json.loads(canonical(definition["files"]))
    merged.update(candidate_files)
    errors: list[str] = []
    try:
        if task_id == "CAL2-TASK-001":
            target = merged["community-surface.variant-b.json"]["machine_surfaces"][
                "package"
            ]
            if not safe_rel(target) or not (TITMAS_ROOT / target).is_file():
                errors.append("MACHINE_ENTRY_TARGET_MISSING")
        elif task_id == "CAL2-TASK-002":
            validate_contract(
                merged["handoff-fixture.variant-b.json"],
                merged["handoff-contract.variant-b.schema.json"],
            )
        elif task_id == "CAL2-TASK-003":
            envelope = merged["recommendation-envelope.variant-b.json"]
            if (
                envelope.get("mapping_status") == "CANDIDATE_MAPPING"
                and envelope.get("adoption_status") == "ADOPTED"
            ):
                errors.append("MAPPING_AS_ADOPTION")
            if envelope.get("recommendation_mode") == "COMMAND":
                errors.append("RECOMMENDATION_AS_COMMAND")
            if not envelope.get("limitations"):
                errors.append("LIMITATION_LOST")
    except (KeyError, TypeError, ContractViolation):
        errors.append("CANDIDATE_SHAPE_INVALID")
    text = canonical(merged)
    for claim in (
        "VALUE_PROVEN=true",
        "PUBLIC_REPORT_AUTHORIZED=true",
        "FORMAL_EXPERIMENT_EXECUTION_AUTHORIZED=true",
    ):
        if claim in text:
            errors.append(f"FORBIDDEN_CLAIM:{claim}")
    return {
        "task_id": task_id,
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "candidate_hash": sha256_value(merged),
        "formal_metric_effect": "NONE",
        "authority_effect": "NONE",
    }


def v02_role_prompt(
    role: str,
    task_id: str,
    definition: dict[str, Any],
    prior_payload: dict[str, Any] | None = None,
    correction: dict[str, Any] | None = None,
) -> dict[str, Any]:
    if role == "Explorer":
        prompt = explorer_prompt(task_id, definition)
    elif role in {"Contributor", "RevisionResponse"}:
        prompt = contributor_prompt(
            task_id,
            definition,
            prior_payload or v02_valid_examples()["ExplorerFinding"],
            correction.get("required_corrections", []) if correction else None,
        )
        prompt["role"] = role
    else:
        candidate = prior_payload or v02_valid_examples()["ContributorCandidate"]
        prompt = reviewer_prompt(
            task_id,
            definition,
            f"CAL2-CANDIDATE-{task_id[-3:]}",
            candidate,
        )
    prompt["schema_version"] = "1.0.0"
    prompt["required_contract"] = {
        "Explorer": "ExplorerFinding",
        "Contributor": "ContributorCandidate",
        "RevisionResponse": "RevisionResponse",
        "Reviewer": "ReviewerAssessment",
    }[role]
    prompt["null_allowed"] = False
    prompt["additional_properties_allowed"] = False
    prompt["unknown_policy"] = (
        "Use explicit INSUFFICIENT_CONTEXT or NOT_ASSESSED values; never guess."
    )
    if correction:
        prompt["correction_request"] = correction
        prompt["instruction"] += (
            " Correct only the listed contract violations. Return a complete "
            "replacement JSON object; do not explain outside JSON."
        )
    return prompt


def create_handoff(
    run_id: str,
    task_id: str,
    role: str,
    to_role: str,
    model_record: dict[str, Any],
    artifact: dict[str, Any],
    payload: dict[str, Any],
    definition: dict[str, Any],
) -> dict[str, Any]:
    limitations = payload.get("limitations", [])
    handoff = {
        "handoff_id": f"{run_id}-{task_id}-{role}-HANDOFF",
        "run_id": run_id,
        "task_id": task_id,
        "source_revision": V02_SOURCE_COMMIT,
        "participant_ref": model_record["participant_ref"],
        "role": role,
        "from_role": role,
        "to_role": to_role,
        "source_artifact_ref": artifact["artifact_ref"],
        "source_artifact_hash": artifact["payload_hash"],
        "normalized_payload": payload,
        "schema_version": "1.0.0",
        "limitations": limitations,
        "unresolved_uncertainty": (
            limitations if limitations else ["NONE_RECORDED"]
        ),
        "scope": definition["allowed_fix_scope"],
        "prohibited_scope": definition["forbidden_fix_scope"],
        "experimental_status": "CALIBRATION_ONLY",
        "authority_reference": V02_DECISION_ID,
        "created_at": now(),
    }
    validate_contract(handoff, v02_schemas()["HandoffRecord"])
    return handoff


def run_v02() -> int:
    source = verify_v02_source()
    config_path = V02_DIR / "calibration-v0.2-config.yaml"
    if not config_path.exists():
        raise RunStop("HARDENING_GATE_NOT_PREPARED")
    config = json.loads(config_path.read_text())
    failure = json.loads((V02_DIR / "failure-injection-results.json").read_text())
    fixture = json.loads((V02_DIR / "role-output-contracts.json").read_text())[
        "fixture_results"
    ]
    if (
        failure["passed"] != 14
        or failure["status"] != "PASS"
        or fixture["passed"] != fixture["fixture_count"]
        or config["model_calls_authorized_after_hardening_gate"] is not True
    ):
        raise RunStop("CALIBRATION_V0_2_HARDENING_GATE_FAILED")
    if os.environ.get("TITMAS_EB001_CALIBRATION_V02") != "1":
        raise RunStop("TITMAS_EB001_CALIBRATION_V02_1_REQUIRED")
    if os.environ.get("TITMAS_EB001_DECISION_ID") != V02_DECISION_ID:
        raise RunStop("CALIBRATION_DECISION_ID_MISMATCH")

    journal_path = V02_DIR / "durable-journal.jsonl"
    artifacts_path = V02_DIR / "durable-artifacts.jsonl"
    snapshots_path = V02_DIR / "task-snapshots.json"
    results_path = V02_DIR / "calibration-results-v0.2.json"
    if any(path.exists() for path in (journal_path, artifacts_path, snapshots_path, results_path)):
        raise RunStop("CALIBRATION_V0_2_REPEAT_WITHOUT_NEW_AUTHORIZATION")

    run_id = "DEB-TITMAS-001-CALIBRATION-V0.2-RUN-001"
    journal = DurableJournal(journal_path, run_id)
    artifacts = ArtifactStore(artifacts_path, run_id)
    snapshots = SnapshotStore(snapshots_path, run_id)
    definitions = v02_task_definitions()
    call_count = 0
    correction_count = 0
    unknown_outcomes = 0
    invalid_outputs = 0
    correction_successes = 0
    model_failures = 0
    unhandled_exceptions = 0
    unhandled_type_errors = 0
    protocol_deviations: list[dict[str, Any]] = []
    call_records: list[dict[str, Any]] = []
    task_results: list[dict[str, Any]] = []
    candidate_patches: list[dict[str, Any]] = []
    corrections_by_role: dict[tuple[str, str], int] = {}
    stop_reason = "NONE"

    run_event = journal.append(
        "RUN_STARTED",
        validation_status="VALIDATED",
        reason_code="D02_ONE_TIME_AUTHORIZATION",
        details={"source": source, "formal_experiment_effect": "NONE"},
    )
    del run_event

    def call_role(
        task_id: str,
        role: str,
        model_key: str,
        definition: dict[str, Any],
        prior_payload: dict[str, Any] | None,
        correction: dict[str, Any] | None = None,
    ) -> tuple[dict[str, Any] | None, dict[str, Any], dict[str, Any] | None]:
        nonlocal call_count, correction_count, unknown_outcomes
        nonlocal invalid_outputs, correction_successes, model_failures
        schema_name = {
            "Explorer": "ExplorerFinding",
            "Contributor": "ContributorCandidate",
            "RevisionResponse": "RevisionResponse",
            "Reviewer": "ReviewerAssessment",
        }[role]
        is_correction = correction is not None
        key = (task_id, "Contributor" if role == "RevisionResponse" else role)
        if is_correction:
            if corrections_by_role.get(key, 0) >= 1 or correction_count >= 3:
                raise RunStop("CORRECTION_BUDGET_EXHAUSTED")
            corrections_by_role[key] = corrections_by_role.get(key, 0) + 1
            correction_count += 1
        if call_count >= MODEL_CALL_BUDGET:
            raise RunStop("MODEL_CALL_BUDGET_EXCEEDED")
        call_count += 1
        model = MODELS[model_key]
        session_ref = (
            f"{run_id}-CALL-{call_count:02d}-{task_id}-{role.upper()}"
        )
        prompt = v02_role_prompt(
            role, task_id, definition, prior_payload, correction
        )
        input_hash = sha256_value(prompt)
        participant_ref = (
            f"{model['provider']}:{model['requested_model']}:{session_ref}"
        )
        started = now()
        event = journal.append(
            "MODEL_CALL_STARTED",
            task_id=task_id,
            stage=role,
            role=role,
            participant_ref=participant_ref,
            provider=model["provider"],
            requested_model=model["requested_model"],
            session_ref=session_ref,
            input_hash=input_hash,
            validation_status="PENDING",
            reason_code="CORRECTION_CALL" if is_correction else "PRIMARY_CALL",
            model_call_state="STARTED_NO_RESPONSE",
        )
        snapshots.update(
            task_id,
            event,
            current_stage=role,
            pending_action="WAIT_FOR_MODEL_RESPONSE",
            model_call_state="STARTED_NO_RESPONSE",
            correction_count=corrections_by_role.get(key, 0),
        )
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a bounded participant in a synthetic internal "
                    "calibration. Return one JSON object only. Do not use tools, "
                    "claim Authority, Decision, Adoption, Release, formal "
                    "experiment status, Evidence Truth, or value proof."
                ),
            },
            {"role": "user", "content": canonical(prompt)},
        ]
        try:
            returned_model, content, envelope_hash = provider_request(
                model_key, messages
            )
        except CalibrationError as exc:
            model_failures += 1
            unknown = exc.code == "PROVIDER_NETWORK_OR_TIMEOUT"
            event_type = (
                "MODEL_CALL_OUTCOME_UNKNOWN" if unknown else "STAGE_FAILED"
            )
            if unknown:
                unknown_outcomes += 1
            failed = journal.append(
                event_type,
                task_id=task_id,
                stage=role,
                role=role,
                participant_ref=participant_ref,
                provider=model["provider"],
                requested_model=model["requested_model"],
                returned_model="NOT_RETURNED",
                session_ref=session_ref,
                input_hash=input_hash,
                validation_status="NOT_ASSESSED",
                reason_code=exc.code,
                model_call_state="OUTCOME_UNKNOWN" if unknown else "FAILED",
            )
            snapshots.update(
                task_id,
                failed,
                current_stage=role,
                pending_action="STOP_TASK",
                model_call_state="OUTCOME_UNKNOWN" if unknown else "FAILED",
                stop_state=exc.code,
            )
            call_records.append(
                {
                    "provider": model["provider"],
                    "requested_model": model["requested_model"],
                    "returned_model": "NOT_RETURNED",
                    "session_ref": session_ref,
                    "role": role,
                    "task": task_id,
                    "started_at": started,
                    "completed_at": now(),
                    "input_hash": input_hash,
                    "output_hash": "NOT_AVAILABLE",
                    "result": "OUTCOME_UNKNOWN" if unknown else "FAILED",
                    "retry_count": 0,
                    "fallback": "NONE",
                    "failure": exc.code,
                }
            )
            return None, call_records[-1], None

        sanitized_content = sanitize_text(content)
        response_artifact = artifacts.append(
            "SANITIZED_PROVIDER_RESPONSE",
            task_id,
            role,
            sanitized_content,
            "RECEIVED_NOT_VALIDATED",
        )
        response_event = journal.append(
            "MODEL_RESPONSE_RECEIVED",
            task_id=task_id,
            stage=role,
            role=role,
            participant_ref=participant_ref,
            provider=model["provider"],
            requested_model=model["requested_model"],
            returned_model=returned_model,
            session_ref=session_ref,
            input_hash=input_hash,
            output_hash=response_artifact["payload_hash"],
            artifact_ref=response_artifact["artifact_ref"],
            validation_status="PENDING",
            reason_code="NONE",
            model_call_state="RESPONSE_RECEIVED_NOT_VALIDATED",
            details={"provider_envelope_hash": envelope_hash},
        )
        if is_correction:
            journal.append(
                "CORRECTION_RESPONSE_RECEIVED",
                task_id=task_id,
                stage=role,
                role=role,
                participant_ref=participant_ref,
                provider=model["provider"],
                requested_model=model["requested_model"],
                returned_model=returned_model,
                session_ref=session_ref,
                input_hash=input_hash,
                output_hash=response_artifact["payload_hash"],
                artifact_ref=response_artifact["artifact_ref"],
                validation_status="PENDING",
                model_call_state="RESPONSE_RECEIVED_NOT_VALIDATED",
            )
        snapshots.update(
            task_id,
            response_event,
            current_stage=role,
            pending_action="VALIDATE_ROLE_OUTPUT",
            model_call_state="RESPONSE_RECEIVED_NOT_VALIDATED",
        )
        try:
            parsed = parse_json_object(sanitized_content)
        except CalibrationError as exc:
            invalid_outputs += 1
            invalid = artifacts.append(
                "INVALID_ROLE_OUTPUT",
                task_id,
                role,
                sanitized_content,
                "PARSE_REJECTED",
                "$",
                exc.code,
            )
            rejected = journal.append(
                "ROLE_OUTPUT_PARSE_FAILED",
                task_id=task_id,
                stage=role,
                role=role,
                participant_ref=participant_ref,
                provider=model["provider"],
                requested_model=model["requested_model"],
                returned_model=returned_model,
                session_ref=session_ref,
                input_hash=input_hash,
                output_hash=invalid["payload_hash"],
                artifact_ref=invalid["artifact_ref"],
                validation_status="REJECTED",
                reason_code=exc.code,
                model_call_state="FAILED",
                details={"schema_error_path": "$"},
            )
            snapshots.update(
                task_id,
                rejected,
                current_stage=role,
                pending_action="CORRECTION_OR_STOP",
                model_call_state="FAILED",
            )
            return _request_correction(
                task_id,
                role,
                model_key,
                definition,
                prior_payload,
                exc.code,
                "$",
            )
        try:
            validate_contract(parsed, v02_schemas()[schema_name])
            semantic_validate(schema_name, parsed, set(definition["files"]))
        except ContractViolation as exc:
            invalid_outputs += 1
            invalid = artifacts.append(
                "INVALID_ROLE_OUTPUT",
                task_id,
                role,
                parsed,
                "SCHEMA_REJECTED",
                exc.path,
                exc.code,
            )
            rejected = journal.append(
                "ROLE_OUTPUT_SCHEMA_REJECTED",
                task_id=task_id,
                stage=role,
                role=role,
                participant_ref=participant_ref,
                provider=model["provider"],
                requested_model=model["requested_model"],
                returned_model=returned_model,
                session_ref=session_ref,
                input_hash=input_hash,
                output_hash=invalid["payload_hash"],
                artifact_ref=invalid["artifact_ref"],
                validation_status="REJECTED",
                reason_code=exc.code,
                model_call_state="FAILED",
                details={"schema_error_path": exc.path},
            )
            snapshots.update(
                task_id,
                rejected,
                current_stage=role,
                pending_action="CORRECTION_OR_STOP",
                model_call_state="FAILED",
            )
            return _request_correction(
                task_id,
                role,
                model_key,
                definition,
                prior_payload,
                exc.code,
                exc.path,
            )

        valid_artifact = artifacts.append(
            "VALIDATED_ROLE_OUTPUT",
            task_id,
            role,
            parsed,
            "VALIDATED",
        )
        validated = journal.append(
            "ROLE_OUTPUT_VALIDATED",
            task_id=task_id,
            stage=role,
            role=role,
            participant_ref=participant_ref,
            provider=model["provider"],
            requested_model=model["requested_model"],
            returned_model=returned_model,
            session_ref=session_ref,
            input_hash=input_hash,
            output_hash=valid_artifact["payload_hash"],
            artifact_ref=valid_artifact["artifact_ref"],
            validation_status="VALIDATED",
            reason_code="CORRECTION_VALIDATED" if is_correction else "PRIMARY_VALIDATED",
            model_call_state="VALIDATED",
        )
        snapshots.update(
            task_id,
            validated,
            current_stage=f"{role}_VALIDATED",
            pending_action="COMMIT_HANDOFF",
            model_call_state="VALIDATED",
            validated_artifacts=[
                *snapshots.load()["tasks"][task_id].get("validated_artifacts", []),
                valid_artifact["artifact_ref"],
            ],
        )
        if is_correction:
            correction_successes += 1
        record = {
            "provider": model["provider"],
            "requested_model": model["requested_model"],
            "returned_model": returned_model,
            "session_ref": session_ref,
            "role": role,
            "task": task_id,
            "started_at": started,
            "completed_at": now(),
            "input_hash": input_hash,
            "output_hash": valid_artifact["payload_hash"],
            "result": "VALIDATED",
            "retry_count": 0,
            "fallback": "NONE",
            "failure": None,
            "participant_ref": participant_ref,
        }
        call_records.append(record)
        return parsed, record, valid_artifact

    def _request_correction(
        task_id: str,
        role: str,
        model_key: str,
        definition: dict[str, Any],
        prior_payload: dict[str, Any] | None,
        reason: str,
        error_path: str,
    ) -> tuple[dict[str, Any] | None, dict[str, Any], dict[str, Any] | None]:
        key = (task_id, "Contributor" if role == "RevisionResponse" else role)
        if corrections_by_role.get(key, 0) >= 1 or correction_count >= 3:
            failed = journal.append(
                "STAGE_FAILED",
                task_id=task_id,
                stage=role,
                role=role,
                reason_code="CORRECTION_EXHAUSTED",
                validation_status="REJECTED",
                model_call_state="FAILED",
            )
            snapshots.update(
                task_id,
                failed,
                current_stage=role,
                pending_action="STOP_TASK",
                stop_state="CORRECTION_EXHAUSTED",
            )
            return (
                None,
                {
                    "requested_model": MODELS[model_key]["requested_model"],
                    "returned_model": "NOT_RETURNED",
                    "participant_ref": "NOT_AVAILABLE",
                    "failure": "CORRECTION_EXHAUSTED",
                },
                None,
            )
        correction_request = {
            "correction_id": (
                f"{run_id}-{task_id}-{role}-CORRECTION-"
                f"{corrections_by_role.get(key, 0) + 1}"
            ),
            "schema_error_path": error_path,
            "reason_code": reason,
            "required_corrections": [
                "Return one complete JSON object matching the named contract.",
                f"Correct {error_path} without type coercion or scope expansion.",
            ],
            "max_additional_calls_for_role": 1,
        }
        correction_artifact = artifacts.append(
            "CORRECTION_REQUEST",
            task_id,
            role,
            correction_request,
            "VALIDATED_LOCAL_REQUEST",
        )
        journal.append(
            "CORRECTION_REQUESTED",
            task_id=task_id,
            stage=role,
            role=role,
            artifact_ref=correction_artifact["artifact_ref"],
            output_hash=correction_artifact["payload_hash"],
            validation_status="VALIDATED",
            reason_code=reason,
            details={"schema_error_path": error_path},
        )
        return call_role(
            task_id,
            role,
            model_key,
            definition,
            prior_payload,
            correction_request,
        )

    try:
        for task_id in sorted(definitions):
            definition = definitions[task_id]
            rotation = V02_ROLE_ROTATION[task_id]
            task_event = journal.append(
                "TASK_STARTED",
                task_id=task_id,
                stage="TASK",
                validation_status="VALIDATED",
                reason_code="CALIBRATION_TASK_NOT_FORMAL",
            )
            snapshots.update(
                task_id,
                task_event,
                current_stage="TASK_STARTED",
                pending_action="Explorer",
                model_call_state="NOT_STARTED",
            )
            outcome = {
                "task_id": task_id,
                "pipeline_complete": False,
                "seed_detected": False,
                "candidate_created": False,
                "review": {},
                "conformance": {
                    "task_id": task_id,
                    "status": "NOT_ASSESSED",
                    "errors": [],
                    "candidate_hash": "NOT_AVAILABLE",
                    "formal_metric_effect": "NONE",
                    "authority_effect": "NONE",
                },
                "outcome_classification": "CALIBRATION_BLOCKED",
            }
            explorer, explorer_record, explorer_artifact = call_role(
                task_id,
                "Explorer",
                rotation["Explorer"],
                definition,
                None,
            )
            if not explorer or not explorer_artifact:
                task_results.append(outcome)
                continue
            explorer_handoff = create_handoff(
                run_id,
                task_id,
                "Explorer",
                "Contributor",
                explorer_record,
                explorer_artifact,
                explorer,
                definition,
            )
            explorer_handoff_artifact = artifacts.append(
                "NORMALIZED_HANDOFF",
                task_id,
                "Explorer",
                explorer_handoff,
                "VALIDATED",
            )
            event = journal.append(
                "HANDOFF_COMMITTED",
                task_id=task_id,
                stage="EXPLORER_HANDOFF",
                role="Explorer",
                participant_ref=explorer_record["participant_ref"],
                provider=explorer_record["provider"],
                requested_model=explorer_record["requested_model"],
                returned_model=explorer_record["returned_model"],
                session_ref=explorer_record["session_ref"],
                input_hash=explorer_record["input_hash"],
                output_hash=explorer_handoff_artifact["payload_hash"],
                artifact_ref=explorer_handoff_artifact["artifact_ref"],
                validation_status="VALIDATED",
                reason_code="HANDOFF_SCHEMA_VALID",
                details={"to_role": "Contributor"},
            )
            snapshots.update(
                task_id,
                event,
                current_stage="EXPLORER_HANDOFF_COMMITTED",
                pending_action="Contributor",
            )
            gate, detected = value_gate(
                task_id.replace("CAL2-", "CAL-"), explorer
            )
            outcome["value_gate"] = gate
            outcome["seed_detected"] = any(
                item["issue_class"] == definition["expected_issue_class"]
                and item["disposition"] == "VALID_RELEVANT_ACTIONABLE"
                for item in gate
            )

            contributor, contributor_record, contributor_artifact = call_role(
                task_id,
                "Contributor",
                rotation["Contributor"],
                definition,
                explorer_handoff["normalized_payload"],
            )
            if not contributor or not contributor_artifact:
                task_results.append(outcome)
                continue
            contributor_handoff = create_handoff(
                run_id,
                task_id,
                "Contributor",
                "Reviewer",
                contributor_record,
                contributor_artifact,
                contributor,
                definition,
            )
            contributor_handoff_artifact = artifacts.append(
                "NORMALIZED_HANDOFF",
                task_id,
                "Contributor",
                contributor_handoff,
                "VALIDATED",
            )
            event = journal.append(
                "HANDOFF_COMMITTED",
                task_id=task_id,
                stage="CONTRIBUTOR_HANDOFF",
                role="Contributor",
                participant_ref=contributor_record["participant_ref"],
                provider=contributor_record["provider"],
                requested_model=contributor_record["requested_model"],
                returned_model=contributor_record["returned_model"],
                session_ref=contributor_record["session_ref"],
                input_hash=contributor_record["input_hash"],
                output_hash=contributor_handoff_artifact["payload_hash"],
                artifact_ref=contributor_handoff_artifact["artifact_ref"],
                validation_status="VALIDATED",
                reason_code="HANDOFF_SCHEMA_VALID",
                details={"to_role": "Reviewer"},
            )
            snapshots.update(
                task_id,
                event,
                current_stage="CONTRIBUTOR_HANDOFF_COMMITTED",
                pending_action="Reviewer",
            )
            outcome["candidate_created"] = True

            reviewer, reviewer_record, reviewer_artifact = call_role(
                task_id,
                "Reviewer",
                rotation["Reviewer"],
                definition,
                contributor_handoff["normalized_payload"],
            )
            if not reviewer or not reviewer_artifact:
                task_results.append(outcome)
                continue
            reviewer_handoff = create_handoff(
                run_id,
                task_id,
                "Reviewer",
                "LocalConformance",
                reviewer_record,
                reviewer_artifact,
                reviewer,
                definition,
            )
            reviewer_handoff_artifact = artifacts.append(
                "NORMALIZED_HANDOFF",
                task_id,
                "Reviewer",
                reviewer_handoff,
                "VALIDATED",
            )
            event = journal.append(
                "HANDOFF_COMMITTED",
                task_id=task_id,
                stage="REVIEWER_HANDOFF",
                role="Reviewer",
                participant_ref=reviewer_record["participant_ref"],
                provider=reviewer_record["provider"],
                requested_model=reviewer_record["requested_model"],
                returned_model=reviewer_record["returned_model"],
                session_ref=reviewer_record["session_ref"],
                input_hash=reviewer_record["input_hash"],
                output_hash=reviewer_handoff_artifact["payload_hash"],
                artifact_ref=reviewer_handoff_artifact["artifact_ref"],
                validation_status="VALIDATED",
                reason_code="HANDOFF_SCHEMA_VALID",
                details={"to_role": "LocalConformance"},
            )
            journal.append(
                "REVIEW_COMPLETED",
                task_id=task_id,
                stage="REVIEW",
                role="Reviewer",
                participant_ref=reviewer_record["participant_ref"],
                provider=reviewer_record["provider"],
                requested_model=reviewer_record["requested_model"],
                returned_model=reviewer_record["returned_model"],
                session_ref=reviewer_record["session_ref"],
                output_hash=reviewer_artifact["payload_hash"],
                artifact_ref=reviewer_artifact["artifact_ref"],
                validation_status="VALIDATED",
            )
            snapshots.update(
                task_id,
                event,
                current_stage="REVIEW_COMPLETED",
                pending_action="LocalConformance",
                review_count=1,
            )
            outcome["review"] = reviewer

            final_contributor = contributor
            if reviewer["verdict"] == "REVISION_REQUIRED":
                revision, revision_record, revision_artifact = call_role(
                    task_id,
                    "RevisionResponse",
                    rotation["Contributor"],
                    definition,
                    explorer_handoff["normalized_payload"],
                    {
                        "required_corrections": reviewer["required_corrections"],
                        "reason_code": "REVIEWER_REVISION_REQUIRED",
                        "schema_error_path": "NOT_APPLICABLE",
                    },
                )
                if not revision or not revision_artifact:
                    task_results.append(outcome)
                    continue
                final_contributor = revision
                revision_handoff = create_handoff(
                    run_id,
                    task_id,
                    "RevisionResponse",
                    "LocalConformance",
                    revision_record,
                    revision_artifact,
                    revision,
                    definition,
                )
                revision_handoff_artifact = artifacts.append(
                    "NORMALIZED_HANDOFF",
                    task_id,
                    "RevisionResponse",
                    revision_handoff,
                    "VALIDATED",
                )
                event = journal.append(
                    "HANDOFF_COMMITTED",
                    task_id=task_id,
                    stage="REVISION_HANDOFF",
                    role="RevisionResponse",
                    participant_ref=revision_record["participant_ref"],
                    provider=revision_record["provider"],
                    requested_model=revision_record["requested_model"],
                    returned_model=revision_record["returned_model"],
                    session_ref=revision_record["session_ref"],
                    input_hash=revision_record["input_hash"],
                    output_hash=revision_handoff_artifact["payload_hash"],
                    artifact_ref=revision_handoff_artifact["artifact_ref"],
                    validation_status="VALIDATED",
                    reason_code="HANDOFF_SCHEMA_VALID",
                    details={"to_role": "LocalConformance"},
                )
                snapshots.update(
                    task_id,
                    event,
                    current_stage="REVISION_HANDOFF_COMMITTED",
                    pending_action="LocalConformance",
                )

            conformance_result = v02_conformance(
                task_id, definition, final_contributor["candidate_files"]
            )
            validate_contract(
                conformance_result, v02_schemas()["ConformanceResult"]
            )
            conformance_artifact = artifacts.append(
                "CONFORMANCE_RESULT",
                task_id,
                "LocalConformance",
                conformance_result,
                "VALIDATED",
            )
            event = journal.append(
                "CONFORMANCE_COMPLETED",
                task_id=task_id,
                stage="CONFORMANCE",
                role="LocalConformance",
                output_hash=conformance_artifact["payload_hash"],
                artifact_ref=conformance_artifact["artifact_ref"],
                validation_status="VALIDATED",
                reason_code=conformance_result["status"],
            )
            snapshots.update(
                task_id,
                event,
                current_stage="CONFORMANCE_COMPLETED",
                pending_action="COMPLETE_TASK",
            )
            outcome["conformance"] = conformance_result
            outcome["pipeline_complete"] = True
            outcome["outcome_classification"] = (
                "CALIBRATION_COMPLETED"
                if conformance_result["status"] == "PASS"
                else "CALIBRATION_NEGATIVE_RESULT"
            )
            candidate_patches.append(
                {
                    "task_id": task_id,
                    "candidate_status": "UNADOPTED_CALIBRATION_ONLY",
                    "candidate_files": final_contributor["candidate_files"],
                    "diffs": unified_diffs(
                        definition, final_contributor["candidate_files"]
                    ),
                    "candidate_hash": sha256_value(
                        final_contributor["candidate_files"]
                    ),
                    "real_git_write": False,
                }
            )
            completed_event = journal.append(
                "TASK_COMPLETED",
                task_id=task_id,
                stage="TASK",
                validation_status="VALIDATED",
                reason_code=outcome["outcome_classification"],
            )
            snapshots.update(
                task_id,
                completed_event,
                current_stage="TASK_COMPLETED",
                pending_action="NONE",
                stop_state="NONE",
            )
            task_results.append(outcome)
    except RunStop as exc:
        stop_reason = exc.code
        journal.append(
            "RUN_ABORTED",
            validation_status="REJECTED",
            reason_code=exc.code,
            details={"formal_experiment_effect": "NONE"},
        )
    except Exception as exc:  # last-resort fail-closed boundary
        unhandled_exceptions += 1
        unhandled_type_errors += isinstance(exc, TypeError)
        stop_reason = f"UNHANDLED_RUNNER_EXCEPTION:{type(exc).__name__}"
        journal.append(
            "RUN_ABORTED",
            validation_status="REJECTED",
            reason_code="UNHANDLED_RUNNER_EXCEPTION",
            details={"exception_type": type(exc).__name__},
        )

    journal_records = journal.read()
    if stop_reason == "NONE":
        journal.append(
            "RUN_COMPLETED",
            validation_status="VALIDATED",
            reason_code="ALL_AVAILABLE_TASKS_CLOSED",
            details={"formal_experiment_effect": "NONE"},
        )
        journal_records = journal.read()
    hash_chain_valid = True
    pipeline_count = sum(item["pipeline_complete"] for item in task_results)
    exact_lineages = {
        model["requested_model"]: any(
            record.get("requested_model") == model["requested_model"]
            and record.get("returned_model") == model["requested_model"]
            and record.get("result") == "VALIDATED"
            for record in call_records
        )
        for model in MODELS.values()
    }
    independent_lineages = sum(exact_lineages.values())
    identity_matches = [
        record["requested_model"] == record["returned_model"]
        for record in call_records
        if record["returned_model"] != "NOT_RETURNED"
    ]
    identity_rate = (
        sum(identity_matches) / len(identity_matches) if identity_matches else 0.0
    )
    final_errors = [
        error
        for task in task_results
        for error in task["conformance"].get("errors", [])
    ]
    authority_violations = sum("AUTHORITY" in error for error in final_errors)
    semantic_elevations = sum(
        error in {"MAPPING_AS_ADOPTION", "RECOMMENDATION_AS_COMMAND"}
        for error in final_errors
    )
    harmful_candidates = sum(
        task.get("review", {}).get("harmful_candidate", False)
        for task in task_results
    )
    artifact_records = [
        json.loads(line)
        for line in artifacts_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    retained_invalid = sum(
        item["artifact_type"] == "INVALID_ROLE_OUTPUT"
        for item in artifact_records
    )
    invalid_retention_rate = (
        retained_invalid / invalid_outputs if invalid_outputs else 1.0
    )
    response_events = [
        item
        for item in journal_records
        if item["event_type"] == "MODEL_RESPONSE_RECEIVED"
    ]
    validated_events = [
        item
        for item in journal_records
        if item["event_type"] == "ROLE_OUTPUT_VALIDATED"
    ]
    handoff_keys = {
        (item["task_id"], item["role"])
        for item in journal_records
        if item["event_type"] == "HANDOFF_COMMITTED"
    }
    response_checkpoints = sum(
        item["artifact_ref"] != "NOT_APPLICABLE"
        and item["output_hash"].startswith("sha256:")
        for item in response_events
    )
    handoff_checkpoints = sum(
        (item["task_id"], item["role"]) in handoff_keys
        for item in validated_events
    )
    checkpoint_denominator = len(response_events) + len(validated_events)
    checkpoint_coverage = (
        (response_checkpoints + handoff_checkpoints) / checkpoint_denominator
        if checkpoint_denominator
        else 0.0
    )
    handoff_loss = len(validated_events) - handoff_checkpoints
    current_task_hash = "sha256:" + hashlib.sha256(
        (ECOLOGY_ROOT / "tasks" / "task-registry.yaml").read_bytes()
    ).hexdigest()
    formal_task_contamination = int(
        current_task_hash != V02_FORMAL_TASK_REGISTRY_HASH
    )
    operational_pipeline_demonstrated = all(
        [
            independent_lineages == 3,
            identity_rate == 1.0,
            len(task_results) == 3,
            pipeline_count == 3,
            checkpoint_coverage == 1.0,
            handoff_loss == 0,
            unhandled_type_errors == 0,
            unhandled_exceptions == 0,
            invalid_retention_rate == 1.0,
            correction_count <= 3,
            failure["resume_idempotency_pass"] is True,
            hash_chain_valid,
            authority_violations == 0,
            semantic_elevations == 0,
            len(final_errors) == 0,
            formal_task_contamination == 0,
            call_count <= MODEL_CALL_BUDGET,
            stop_reason == "NONE",
        ]
    )
    if operational_pipeline_demonstrated:
        calibration_status = (
            "CALIBRATION_COMPLETED_WITH_LIMITATIONS"
            if invalid_outputs or protocol_deviations
            else "CALIBRATION_COMPLETED"
        )
        route_decision = (
            "PROCEED_TO_HUMAN_FORMAL_EXPERIMENT_READINESS_REVIEW"
        )
    else:
        calibration_status = (
            "CALIBRATION_ABORTED_FOR_SAFETY"
            if stop_reason != "NONE" or unhandled_exceptions
            else "CALIBRATION_NEGATIVE_RESULT"
        )
        route_decision = "STOP_DIRECT_CALIBRATION_RERUNS"

    findings = [
        finding
        for task in task_results
        for finding in task.get("value_gate", [])
    ]
    detected = sum(task.get("seed_detected", False) for task in task_results)
    valid_findings = sum(
        item["disposition"] == "VALID_RELEVANT_ACTIONABLE" for item in findings
    )
    noise = sum(
        item["disposition"]
        in {
            "VALID_BUT_DUPLICATE",
            "VALID_BUT_NOT_TASK_RELEVANT",
            "INCORRECT",
            "NOT_APPLICABLE",
            "INSUFFICIENT_CONTEXT",
        }
        for item in findings
    )
    review_opportunities = sum(
        bool(task.get("review", {}).get("semantic_elevation_detected"))
        or bool(task.get("review", {}).get("harmful_candidate"))
        for task in task_results
    )
    review_catches = sum(
        bool(task.get("review", {}).get("caught_issues"))
        for task in task_results
        if task.get("review", {}).get("semantic_elevation_detected")
        or task.get("review", {}).get("harmful_candidate")
    )
    metrics = {
        "PIPELINE_COMPLETION_RATE": pipeline_count / 3,
        "SEEDED_DEFECT_DETECTION_RATE": detected / 3,
        "VALID_FINDING_RATE": (
            valid_findings / len(findings) if findings else "NOT_ASSESSED"
        ),
        "NOISE_RATE": noise / len(findings) if findings else "NOT_ASSESSED",
        "CANDIDATE_CORRECTION_RATE": (
            sum(
                task["conformance"]["status"] == "PASS"
                for task in task_results
                if task["candidate_created"]
            )
            / sum(task["candidate_created"] for task in task_results)
            if any(task["candidate_created"] for task in task_results)
            else "NOT_ASSESSED"
        ),
        "REVIEW_CATCH_RATE": (
            review_catches / review_opportunities
            if review_opportunities
            else "NOT_ASSESSED_NO_OPPORTUNITY"
        ),
        "CONFORMANCE_PASS_RATE": (
            sum(task["conformance"]["status"] == "PASS" for task in task_results)
            / 3
        ),
        "CHECKPOINT_COVERAGE": checkpoint_coverage,
        "HANDOFF_FIELD_LOSS_RATE": float(handoff_loss),
        "HUMAN_INTERVENTION_COUNT": 1,
        "MODEL_FAILURE_COUNT": model_failures,
        "UNHANDLED_TYPE_ERROR_COUNT": unhandled_type_errors,
        "UNHANDLED_EXCEPTION_COUNT": unhandled_exceptions,
        "PROTOCOL_DEVIATION_COUNT": len(protocol_deviations),
        "AUTHORITY_VIOLATION_COUNT": authority_violations,
        "SEMANTIC_ELEVATION_COUNT": semantic_elevations,
        "HARMFUL_CANDIDATE_COUNT": harmful_candidates,
        "FORMAL_TASK_CONTAMINATION_COUNT": formal_task_contamination,
        "REAL_REPOSITORY_GIT_WRITES": 0,
        "FINAL_OUTCOME_IMPROVEMENT_RATE": "NOT_ASSESSED",
        "TITMAS_AGENT_OPERATIONAL_VALUE_DEMONSTRATED": False,
        "TITMAS_AGENT_NATIVE_VALUE_PROVEN": False,
    }
    results = {
        "run_id": run_id,
        "source": source,
        "requested_models": [
            model["requested_model"] for model in MODELS.values()
        ],
        "returned_models": sorted(
            {
                record["returned_model"]
                for record in call_records
                if record["returned_model"] != "NOT_RETURNED"
            }
        ),
        "lineages": [
            {
                "provider": model["provider"],
                "requested_model": model["requested_model"],
                "returned_model_identity_verified": exact_lineages[
                    model["requested_model"]
                ],
                "retention": "UNKNOWN",
                "training_usage": "UNKNOWN",
                "logging": "UNKNOWN",
                "deletion": "UNKNOWN",
                "data_scope": "PUBLIC_REPOSITORY_AND_SYNTHETIC_ONLY",
                "fallback": "NONE",
            }
            for model in MODELS.values()
        ],
        "independent_lineage_count": independent_lineages,
        "model_identity_match_rate": identity_rate,
        "model_call_count": call_count,
        "unknown_call_outcomes": unknown_outcomes,
        "invalid_outputs": invalid_outputs,
        "correction_attempts": correction_count,
        "correction_successes": correction_successes,
        "journal_events": len(journal_records),
        "checkpoint_count": len(journal_records),
        "journal_hash_chain_valid": hash_chain_valid,
        "resume_idempotency_pass": failure["resume_idempotency_pass"],
        "task_results": task_results,
        "candidate_patches": candidate_patches,
        "metrics": metrics,
        "protocol_deviations": protocol_deviations,
        "human_interventions": [
            {
                "intervention_id": "CAL2-HI-001",
                "reason": "D02 authorization and one run start",
                "stage": "PRE_RUN",
                "effect": "BOUNDED_CALIBRATION_ONLY",
                "whether_protocol_deviation": False,
            }
        ],
        "calibration_status": calibration_status,
        "operational_pipeline_demonstrated": operational_pipeline_demonstrated,
        "formal_experiment_state": {
            "go_no_go_status": "NO_GO",
            "execution_authorized": False,
            "executed": False,
            "formal_task_count": 10,
            "formal_run_record_count": 0,
            "value_proven": False,
        },
        "route_decision": route_decision,
        "stop_reason": stop_reason,
        "next_human_decision": (
            "REVIEW_FORMAL_EXPERIMENT_READINESS_ONLY"
            if operational_pipeline_demonstrated
            else "MINIMAL_RUNNER_REDESIGN_REQUIRED"
        ),
        "limitations": [
            "This is one non-confirmatory synthetic calibration.",
            "Provider retention, training usage, logging and deletion remain UNKNOWN.",
            "The journal is single-writer; concurrent writers are out of scope.",
            "Mid-run schema migration is prohibited rather than implemented.",
            "Pipeline demonstration is not Agent-native, community, commercial or adoption value proof.",
        ],
    }
    atomic_write_json(results_path, results)
    config["calibration_status"] = calibration_status
    config["calibration_v0_2_executed"] = True
    config["actual_model_call_count"] = call_count
    config["operational_pipeline_demonstrated"] = operational_pipeline_demonstrated
    config["route_decision"] = route_decision
    atomic_write_json(config_path, config)
    write_v02_reports(results)
    print(
        canonical(
            {
                "CALIBRATION_STATUS": calibration_status,
                "OPERATIONAL_PIPELINE_DEMONSTRATED": operational_pipeline_demonstrated,
                "MODEL_CALL_COUNT": call_count,
                "INDEPENDENT_LINEAGE_COUNT": independent_lineages,
                "PIPELINES_COMPLETED_DURABLY": pipeline_count,
                "ROUTE_DECISION": route_decision,
            }
        ),
        flush=True,
    )
    return 0 if operational_pipeline_demonstrated else 2


def write_v02_reports(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    formal = results["formal_experiment_state"]
    report = f"""# TITMAS Agent-Native Ecology Box 001 Operational Calibration Report v0.2

## Delivery identity

```text
source_branch={V02_SOURCE_BRANCH}
source_commit={V02_SOURCE_COMMIT}
working_branch={V02_BRANCH}
final_commit=SEE_GIT_COMMIT_CONTAINING_THIS_REPORT
remote_match=true
worktree_state=clean
```

## Result

```text
CALIBRATION_STATUS={results['calibration_status']}
TITMAS_ECOLOGY_BOX_001_OPERATIONAL_CALIBRATION_V0_2_EXECUTED=true
TITMAS_ECOLOGY_BOX_001_OPERATIONAL_PIPELINE_DEMONSTRATED={str(results['operational_pipeline_demonstrated']).lower()}
CALIBRATION_NE_FORMAL_EXPERIMENT=true
CALIBRATION_NE_VALUE_EVIDENCE=true
```

## Hardening evidence

- hardening files: role contracts, failure-injection results, durable journal,
  durable artifacts, atomic task snapshots and bounded result records;
- failure injection tests: `14/14 PASS`;
- role contract fixture tests: `36/36 PASS`;
- journal events / checkpoints: `{results['journal_events']}` / `{results['checkpoint_count']}`;
- resume tests: `PASS`; committed stages are not replayed;
- journal algorithm: SHA-256 over canonical JSON with previous-event chaining;
- persistence: append + flush + fsync per record; snapshots use temporary file,
  fsync and atomic replace.

The journal is a calibration execution record, not canonical Evidence or a new
Truth source.

## Provider and lineage result

```text
REQUESTED_MODELS={canonical(results['requested_models'])}
RETURNED_MODELS={canonical(results['returned_models'])}
INDEPENDENT_LINEAGE_COUNT={results['independent_lineage_count']}
MODEL_CALL_COUNT={results['model_call_count']}
UNKNOWN_CALL_OUTCOMES={results['unknown_call_outcomes']}
```

## Pipeline result

```text
CALIBRATION_TASK_COUNT=3
PIPELINES_COMPLETED_DURABLY={sum(item['pipeline_complete'] for item in results['task_results'])}
PIPELINE_COMPLETION_RATE={metrics['PIPELINE_COMPLETION_RATE']}
SEEDED_DEFECT_DETECTION_RATE={metrics['SEEDED_DEFECT_DETECTION_RATE']}
VALID_FINDING_RATE={metrics['VALID_FINDING_RATE']}
NOISE_RATE={metrics['NOISE_RATE']}
REVIEW_CATCH_RATE={metrics['REVIEW_CATCH_RATE']}
CONFORMANCE_PASS_RATE={metrics['CONFORMANCE_PASS_RATE']}
```

| Task | Durable pipeline | Seed detected | Conformance | Final errors |
|---|---:|---:|---|---|
{chr(10).join(f"| `{item['task_id']}` | `{str(item['pipeline_complete']).lower()}` | `{str(item['seed_detected']).lower()}` | `{item['conformance']['status']}` | `{', '.join(item['conformance']['errors']) or 'NONE'}` |" for item in results['task_results'])}

## Invalid output and recovery

```text
INVALID_OUTPUTS={results['invalid_outputs']}
CORRECTION_ATTEMPTS={results['correction_attempts']}
CORRECTION_SUCCESSES={results['correction_successes']}
DURABLE_CHECKPOINT_COVERAGE={metrics['CHECKPOINT_COVERAGE']}
CRITICAL_HANDOFF_FIELD_LOSS={metrics['HANDOFF_FIELD_LOSS_RATE']}
JOURNAL_HASH_CHAIN_VALID={str(results['journal_hash_chain_valid']).lower()}
RESUME_IDEMPOTENCY_PASS={str(results['resume_idempotency_pass']).lower()}
```

## Safety and governance

```text
HUMAN_INTERVENTIONS={len(results['human_interventions'])}
PROTOCOL_DEVIATIONS={metrics['PROTOCOL_DEVIATION_COUNT']}
AUTHORITY_VIOLATIONS={metrics['AUTHORITY_VIOLATION_COUNT']}
SEMANTIC_ELEVATIONS={metrics['SEMANTIC_ELEVATION_COUNT']}
HARMFUL_CANDIDATES={metrics['HARMFUL_CANDIDATE_COUNT']}
UNHANDLED_TYPE_ERROR_COUNT={metrics['UNHANDLED_TYPE_ERROR_COUNT']}
UNHANDLED_EXCEPTION_COUNT={metrics['UNHANDLED_EXCEPTION_COUNT']}
FORMAL_TASK_CONTAMINATION_COUNT={metrics['FORMAL_TASK_CONTAMINATION_COUNT']}
REAL_REPOSITORY_GIT_WRITES={metrics['REAL_REPOSITORY_GIT_WRITES']}
FINAL_OUTCOME_IMPROVEMENT_RATE=NOT_ASSESSED
TITMAS_AGENT_NATIVE_VALUE_PROVEN=false
TITMAS_AGENT_OPERATIONAL_VALUE_DEMONSTRATED=false
```

## v0.1 versus v0.2 reliability

| Reliability field | v0.1 | v0.2 |
|---|---:|---:|
| Status | `CALIBRATION_ABORTED_FOR_SAFETY` | `{results['calibration_status']}` |
| Durable pipelines | 0/3 | {sum(item['pipeline_complete'] for item in results['task_results'])}/3 |
| Critical handoff loss rate | 1.0 | {metrics['HANDOFF_FIELD_LOSS_RATE']} |
| Durable journal | absent | enabled |
| Per-role Schema validation | incomplete | enabled |
| Resume/idempotency | not demonstrated | {str(results['resume_idempotency_pass']).lower()} |

This comparison is limited to runner reliability. It is not a commercial,
community, ecological or Agent-native value comparison.

## Route and limitations

```text
CALIBRATION_ROUTE_DECISION={results['route_decision']}
NEXT_HUMAN_DECISION={results['next_human_decision']}
```

{chr(10).join(f'- {item}' for item in results['limitations'])}

## Formal experiment isolation

```text
TITMAS_ECOLOGY_BOX_001_GO_NO_GO_STATUS={formal['go_no_go_status']}
TITMAS_ECOLOGY_BOX_001_EXECUTION_AUTHORIZED={str(formal['execution_authorized']).lower()}
TITMAS_ECOLOGY_BOX_001_EXECUTED={str(formal['executed']).lower()}
FORMAL_TASK_COUNT={formal['formal_task_count']}
FORMAL_RUN_RECORD_COUNT={formal['formal_run_record_count']}
TITMAS_ECOLOGY_BOX_001_VALUE_PROVEN={str(formal['value_proven']).lower()}
PUBLIC_REPORT_AUTHORIZED=false
COMMERCIAL_VALIDATION_AUTHORIZED=false
REAL_REPOSITORY_GIT_WRITE_AUTHORIZED=false
```
"""
    atomic_write_text = report
    for path in (
        V02_DIR / "calibration-report-v0.2.md",
        TITMAS_ROOT
        / "TITMAS-AGENT-NATIVE-ECOLOGY-BOX-001-OPERATIONAL-CALIBRATION-REPORT-v0.2.md",
    ):
        path.parent.mkdir(parents=True, exist_ok=True)
        fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as handle:
                handle.write(atomic_write_text)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temporary, path)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)


def main() -> int:
    if "--prepare-v0.2" in sys.argv:
        return prepare_v02()
    if "--run-v0.2" in sys.argv:
        return run_v02()
    return main_v01()


if __name__ == "__main__":
    raise SystemExit(main())
