#!/usr/bin/env python3
"""Run seven isolated qwen3.7-max advisory reviews with no Authority effect."""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import sys
import urllib.request
from pathlib import Path
from typing import Any

PILOT_DIR = Path(__file__).resolve().parent
DBA_ROOT = PILOT_DIR.parents[2]
REVIEW_ROUND = os.environ.get("TITMAS_REVIEW_ROUND", "round-1")
OUT_DIR = PILOT_DIR / "reviews" / REVIEW_ROUND
MODEL = "qwen3.7-max"

REVIEWS = {
    "constitutional-consistency": [
        "architecture/open-infrastructure-strategy-constitution.md",
        "architecture/ADR-034-titmas-agent-native-standards-community-direction.md",
        "architecture/titmas-agent-native-community-constitutional-baseline-v1.1.md",
    ],
    "agent-native-architecture": [
        "agent-index.json",
        "TITMAS/agent-native/community-manifest.json",
        "TITMAS/agent-native/current-state.json",
        "TITMAS/agent-native/community_cli.py",
    ],
    "security-and-adversarial": [
        "TITMAS/agent-native/security/adversarial-cases.json",
        "TITMAS/agent-native/community_cli.py",
        "TITMAS/conformance/harness.py",
    ],
    "machine-usability": [
        "agent-index.json",
        "TITMAS/README.md",
        "TITMAS/agent-native/README.md",
        "TITMAS/agent-native/guides/agent-in-60-seconds.md",
    ],
    "standards-and-schema": [
        "TITMAS/agent-native/schemas/task.schema.json",
        "TITMAS/agent-native/schemas/participant.schema.json",
        "TITMAS/agent-native/schemas/contribution-package.schema.json",
        "TITMAS/agent-native/schemas/review-receipt.schema.json",
        "TITMAS/agent-native/contributions/example-contribution-package.json",
    ],
    "recommendation-integrity": [
        "TITMAS/agent-native/recommendations/README.md",
        "TITMAS/agent-native/recommendations/calibration-cases.json",
        "TITMAS/agent-native/recommendations/example-recommendation-package.json",
        "TITMAS/agent-native/pilot/pilot-result.json",
    ],
    "community-value-and-noise": [
        "TITMAS/agent-native/value-gate/agent-immune-five-task-fixture.json",
        "TITMAS/agent-native/maintenance/example-maintenance-report.json",
        "TITMAS/agent-native/pilot/pilot-result.json",
        "TITMAS/agent-native/current-state.json",
    ],
}


def instant() -> str:
    return dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).isoformat()


def digest(value: str) -> str:
    return "sha256:" + hashlib.sha256(value.encode()).hexdigest()


def source(paths: list[str]) -> str:
    blocks = []
    for relative in paths:
        path = (DBA_ROOT / relative).resolve()
        if not path.is_relative_to(DBA_ROOT.resolve()) or not path.is_file():
            raise ValueError(relative)
        blocks.append(f"FILE {relative}\n{path.read_text(encoding='utf-8')}")
    return "\n\n".join(blocks)


def call(prompt: str) -> tuple[str, dict[str, Any]]:
    key = os.environ.get("DASHSCOPE_API_KEY")
    base = os.environ.get("DASHSCOPE_BASE_URL", "").rstrip("/")
    if not key or not base:
        raise RuntimeError("DASHSCOPE_API_KEY and DASHSCOPE_BASE_URL are required")
    payload = {
        "model": MODEL,
        "temperature": 0,
        "response_format": {"type": "json_object"},
        "messages": [
            {"role": "system", "content": (
                "You are an advisory reviewer in an internal controlled pilot. "
                "Return one JSON object. You have no Human, Architecture, merge, "
                "release, certification or adoption Authority. Be strict and honest."
            )},
            {"role": "user", "content": prompt},
        ],
    }
    request = urllib.request.Request(
        base + "/chat/completions",
        data=json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        envelope = json.loads(response.read().decode())
    return envelope.get("model", "UNKNOWN"), json.loads(
        envelope["choices"][0]["message"]["content"]
    )


def main() -> int:
    if os.environ.get("TITMAS_CONTROLLED_PILOT") != "1":
        print("TITMAS_CONTROLLED_PILOT=1 is required", file=sys.stderr)
        return 2
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    failures = 0
    for index, (review_id, paths) in enumerate(REVIEWS.items(), 1):
        participant = "PILOT-C" if index % 2 else "PILOT-D"
        session_id = f"V11-{REVIEW_ROUND.upper()}-{index:02d}"
        started = instant()
        prompt = f"""Review type: {review_id}
Reviewed revision: infrastructure commit 76e882d plus controlled-pilot remediation candidate.
Independence: LEVEL_2_SAME_MODEL_ISOLATED_SESSION.
Required boundaries: Evidence != Truth; Verification != Authorization;
Mapping != Adoption; Recommendation != Decision; Agent review != Human Decision;
99% target != current measured fact; no public launch/release/certification.

Return exactly these keys:
severity (NONE|LOW|MEDIUM|HIGH|CRITICAL),
verdict (PASS|FAIL|HOLD|REVISION_REQUIRED),
findings (array of concise strings),
required_corrections (array),
optional_suggestions (array),
uncertainty (array),
limitations (array),
relevance (RELEVANT|PARTIAL|NOT_RELEVANT|NOT_ASSESSED),
uniqueness (UNIQUE|DUPLICATE|NOT_ASSESSED).

Inputs:
{source(paths)}"""
        record: dict[str, Any] = {
            "review_id": f"TITMAS-V11-{review_id.upper()}",
            "reviewer_participant_ref": participant,
            "reviewer_lineage": "QWEN-3.7-MAX",
            "reviewed_revision": f"76e882d+CONTROLLED_PILOT_{REVIEW_ROUND.upper()}",
            "scope": paths,
            "findings": [],
            "evidence": [f"prompt_hash:{digest(prompt)}"],
            "severity": "CRITICAL",
            "relevance": "NOT_ASSESSED",
            "uniqueness": "NOT_ASSESSED",
            "required_corrections": [],
            "optional_suggestions": [],
            "uncertainty": [],
            "verdict": "HOLD",
            "limitations": [],
            "independence_level": "LEVEL_2_SAME_MODEL_ISOLATED_SESSION",
            "same_base_model_different_session": True,
            "contributor_participant_ref": "PILOT-B",
            "self_approval": False,
            "provider": "ALIBABA_CLOUD",
            "requested_model": MODEL,
            "returned_model": "NOT_RETURNED",
            "runtime": "PYTHON_STDLIB_OPENAI_COMPATIBLE_CLIENT",
            "session_id": session_id,
            "started_at": started,
            "completed_at": started,
            "output_hash": digest(""),
            "failures": [],
            "retries": 0,
            "fallback": "NONE",
            "authority_effect": "NONE",
        }
        try:
            returned_model, result = call(prompt)
            record["returned_model"] = returned_model
            if returned_model != MODEL:
                raise RuntimeError(f"returned model mismatch: {returned_model}")
            for key in (
                "severity", "verdict", "findings", "required_corrections",
                "optional_suggestions", "uncertainty", "limitations",
                "relevance", "uniqueness",
            ):
                record[key] = result[key]
            record["output_hash"] = digest(json.dumps(result, sort_keys=True))
        except Exception as exc:
            failures += 1
            record["failures"].append(f"{type(exc).__name__}: {exc}")
        record["completed_at"] = instant()
        (OUT_DIR / f"{review_id}.json").write_text(
            json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        print(f"{review_id}: {record['verdict']} {record['severity']}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
