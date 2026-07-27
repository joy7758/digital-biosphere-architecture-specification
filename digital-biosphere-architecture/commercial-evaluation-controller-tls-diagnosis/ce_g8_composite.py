#!/usr/bin/env python3
"""Classify CE-G8 sanitized controller and server receipts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


DECISION = "TITMAS-COMMERCIAL-EVALUATION-CE-G8"
ALLOWED = {
    "CLIENT_STACK_OR_LOCAL_PATH_SIGNAL",
    "ADDRESS_PATH_SIGNAL",
    "SERVER_HANDSHAKE_SIGNAL",
    "INCONCLUSIVE",
    "NO_FAILURE_OBSERVED",
}


class CompositeFailure(RuntimeError):
    """Fail-closed composite validation failure."""


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise CompositeFailure("receipt must be an object")
    return value


def classify(controller: dict[str, Any], server: dict[str, Any]) -> str:
    records = controller.get("records")
    if not isinstance(records, list) or len(records) != 4:
        raise CompositeFailure("exact four controller records required")
    result_by_id = {
        item.get("id"): item.get("result")
        for item in records
        if isinstance(item, dict)
    }
    if set(result_by_id) != {"A", "B", "C", "D"}:
        raise CompositeFailure("request matrix IDs mismatch")
    failed = {key for key, value in result_by_id.items() if value != "PASS"}
    if int(server.get("ssl_or_handshake_signal_count", 0)) > 0:
        result = "SERVER_HANDSHAKE_SIGNAL"
    elif not failed:
        result = "NO_FAILURE_OBSERVED"
    elif failed <= {"A", "B"} and {"C", "D"}.isdisjoint(failed):
        result = "CLIENT_STACK_OR_LOCAL_PATH_SIGNAL"
    elif failed & {"A", "C"} and not failed & {"B", "D"}:
        result = "ADDRESS_PATH_SIGNAL"
    else:
        result = "INCONCLUSIVE"
    if result not in ALLOWED:
        raise CompositeFailure("classification is outside the decision")
    return result


def execute(controller_path: Path, server_path: Path, output: Path) -> int:
    result: dict[str, Any] = {
        "result_id": "TITMAS-CE-G8-COMPOSITE-001",
        "version": "0.1.0",
        "decision_reference": DECISION,
        "status": "FAIL_CLOSED",
        "classification": "INCONCLUSIVE",
        "classification_strength": "SUPPORTED_NOT_PROVEN",
        "root_cause_proven": False,
        "policy_changed": False,
        "redeployment_authorized": False,
        "error_class": None,
    }
    exit_code = 1
    try:
        controller = load(controller_path)
        server = load(server_path)
        if controller.get("decision_reference") != DECISION:
            raise CompositeFailure("controller decision mismatch")
        if server.get("decision_reference") != DECISION:
            raise CompositeFailure("server decision mismatch")
        if controller.get("window_start") != server.get("window_start"):
            raise CompositeFailure("window start mismatch")
        if controller.get("window_end") != server.get("window_end"):
            raise CompositeFailure("window end mismatch")
        if server.get("padding_seconds") != 0:
            raise CompositeFailure("server window padding is forbidden")
        if server.get("raw_logs_persisted") is not False:
            raise CompositeFailure("raw log persistence is forbidden")
        result["classification"] = classify(controller, server)
        result["status"] = "DIAGNOSTIC_CLASSIFICATION_COMPLETE"
        result["controller_receipt"] = controller_path.name
        result["server_receipt"] = server_path.name
        result["request_summary"] = controller.get("summary")
        result["server_signal_summary"] = {
            "access_records": server.get("access", {}).get("records"),
            "ssl_or_handshake_signal_count": server.get(
                "ssl_or_handshake_signal_count"
            ),
        }
        exit_code = 0
    except BaseException as error:
        result["error_class"] = type(error).__name__
    output.write_text(
        json.dumps(result, indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )
    return exit_code


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--controller", required=True, type=Path)
    parser.add_argument("--server", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    return execute(args.controller, args.server, args.output)


if __name__ == "__main__":
    raise SystemExit(main())
