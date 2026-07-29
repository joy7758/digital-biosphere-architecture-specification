#!/usr/bin/env python3
"""Validate the sanitized Stage 5 Agent pilot audit without Provider access."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
AUDIT_ROOT = ROOT / "agent-audit"
SECRET = re.compile(
    r"sk-(?:proj|sp)-[A-Za-z0-9._-]{12,}|"
    r"Authorization\s*:\s*Bearer\s+[A-Za-z0-9._~+/=-]{12,}",
    re.IGNORECASE,
)
PRIVATE_PATH = re.compile(r"/(?:Users|private|home|var|tmp)/|[A-Za-z]:\\")
PROHIBITED_ELEVATION = {
    "STANDARD_ADOPTED",
    "STABLE",
    "CERTIFIED",
    "EXTERNAL_ADOPTION",
}
REGISTRY_FIELDS = {
    "submission_id",
    "type",
    "source",
    "contributor_kind",
    "conformance_status",
    "review_status",
    "human_disposition",
    "pilot_status",
    "hashes",
    "limitations",
}


def load(name: str) -> dict[str, Any]:
    value = json.loads((AUDIT_ROOT / name).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{name} must contain an object")
    return value


def validate() -> dict[str, Any]:
    audit = load("sanitized-agent-pilot-audit.json")
    plan = load("sanitized-contributor-plan.json")
    contribution = load("sanitized-standard-contribution.json")
    registry = json.loads(
        (ROOT / "agent-pilot-contribution-registry.json").read_text(
            encoding="utf-8"
        )
    )
    if audit["model_calls"] != 3 or audit["provider_calls"] != 3:
        raise ValueError("exact three-call audit required")
    if audit["automatic_retry_count"] != 0:
        raise ValueError("automatic retry is prohibited")
    if audit["independent_agent_review_complete"] is not False:
        raise ValueError("unknown Reviewer outcome cannot become complete")
    if audit["review_result"] != "UNKNOWN_POST_DISPATCH_OUTCOME":
        raise ValueError("Reviewer failure classification drift")
    if audit["stage5_private_preview_operational"] is not False:
        raise ValueError("incomplete review cannot become operational")
    if audit["formal_specification_registry_modified"] is not False:
        raise ValueError("formal registry modification is prohibited")
    if plan["checkpoint_state"] != "DURABLE":
        raise ValueError("plan checkpoint is not durable")
    if contribution["checkpoint_state"] != "DURABLE":
        raise ValueError("contribution checkpoint is not durable")
    if contribution["structured_result"]["conformance_status"] != "CONFORMANCE_PASS":
        raise ValueError("captured customer Conformance result drift")
    entries = registry.get("entries")
    if not isinstance(entries, list) or len(entries) != 1:
        raise ValueError("one Agent pilot registry entry required")
    if set(entries[0]) != REGISTRY_FIELDS:
        raise ValueError("pilot registry field boundary drift")
    if entries[0]["pilot_status"] != "PILOT_REJECTED":
        raise ValueError("unknown review must fail closed")
    text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in sorted(AUDIT_ROOT.glob("*.json"))
    )
    if SECRET.search(text) or PRIVATE_PATH.search(text):
        raise ValueError("sanitized audit contains secret or private path")
    if any(value in text for value in PROHIBITED_ELEVATION):
        raise ValueError("sanitized audit contains semantic elevation")
    return {
        "agent_audit_files_checked": 3,
        "agent_pilot_registry_entries_checked": 1,
        "model_calls": 3,
        "automatic_retry_count": 0,
        "durable_checkpoints": 2,
        "review_checkpoint_durable": False,
        "stage5_private_preview_operational": False,
        "secret_findings": 0,
        "private_path_findings": 0,
        "semantic_elevation_findings": 0,
        "status": "PASS_WITH_RECORDED_NEGATIVE_RESULT",
    }


def main() -> int:
    print(json.dumps(validate(), ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
