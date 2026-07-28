#!/usr/bin/env python3
"""Observe the Agent Front Door website release from one independent vantage.

This wrapper reuses the bounded CE-G5 transport engine while binding the
Agent Front Door decision, source revision, immutable release directory,
route set, and hash baseline. It is read-only and cannot deploy, retry,
fall back, bypass TLS, or authorize keeping a failed release active.
"""

from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path
import re
from typing import Any


HERE = Path(__file__).resolve().parent
ENGINE_PATH = (
    HERE.parent
    / "commercial-evaluation-independent-vantage"
    / "ce_g5_observer.py"
)
SPEC = importlib.util.spec_from_file_location(
    "titmas_agent_front_door_release_engine",
    ENGINE_PATH,
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("CE-G5 observation engine is unavailable")
engine = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(engine)


DECISION = "AGENT-FRONT-DOOR-PUBLIC-WEBSITE-FORMAL-RELEASE-2026-07-28"
ORIGIN = "https://redcrag.cn"
SOURCE_REVISION = "35f30d81962a02a8353a79763fd4f09db815fd15"
PROPOSED_RELEASE = (
    "/srv/tmai/releases/"
    "35f30d81962a02a8353a79763fd4f09db815fd15"
    "--5b19e75d6ff653f2b44f124a22bf45cea37e8aa771e7e2f8919aeab9ede8eadc"
)
ROUTES = [
    "/",
    "/en/",
    "/agent-index.json",
    "/site-catalog.json",
]
SAFE_REFERENCE = re.compile(r"^[A-Za-z0-9._-]+$")


def validate_request(
    request: dict[str, Any],
    vantage_id: str,
    client: str,
) -> tuple[str, int, dict[str, dict[str, Any]]]:
    if request.get("decision_reference") != DECISION:
        raise engine.ContractError("decision_reference mismatch")
    if request.get("public_origin") != ORIGIN:
        raise engine.ContractError("public_origin mismatch")
    if request.get("source_revision") != SOURCE_REVISION:
        raise engine.ContractError("source_revision mismatch")
    if request.get("active_release_expected") != PROPOSED_RELEASE:
        raise engine.ContractError("active release mismatch")
    if request.get("deployment_state_expected") != "POST_SWITCH_PROPOSED_RELEASE":
        raise engine.ContractError("post-switch deployment state is required")
    if request.get("immediate_gates_passed") is not True:
        raise engine.ContractError("immediate gates must pass before observation")
    if request.get("rollback_on_any_failure") is not True:
        raise engine.ContractError("rollback_on_any_failure must be true")
    if request.get("rounds") != 3 or request.get("routes") != ROUTES:
        raise engine.ContractError("exact three-round four-route contract required")
    if request.get("requests_per_vantage") != 12:
        raise engine.ContractError("requests_per_vantage must equal 12")
    if request.get("total_public_origin_get_cap") != 24:
        raise engine.ContractError("total_public_origin_get_cap must equal 24")
    for key in ("retry", "fallback", "tls_verification_bypass"):
        if request.get(key) is not False:
            raise engine.ContractError(f"{key} must be false")
    if request.get("sequential_within_vantage") is not True:
        raise engine.ContractError("sequential_within_vantage must be true")
    if engine.ALLOWED_CLIENTS.get(vantage_id) != client:
        raise engine.ContractError("vantage/client binding mismatch")

    run_id = request.get("run_id")
    if not isinstance(run_id, str) or not SAFE_REFERENCE.fullmatch(run_id):
        raise engine.ContractError("run_id is missing or unsafe")
    gap_seconds = request.get("round_gap_seconds")
    if not isinstance(gap_seconds, int) or not 0 <= gap_seconds <= 30:
        raise engine.ContractError("round_gap_seconds must be 0..30")

    baseline_ref = request.get("hash_baseline_reference")
    if not isinstance(baseline_ref, str):
        raise engine.ContractError("hash baseline reference is required")
    baseline = engine.load_json(HERE / Path(baseline_ref).name)
    if baseline.get("status") != "FIXED_PROPOSED_RELEASE_BASELINE":
        raise engine.ContractError("proposed-release baseline is not fixed")
    if baseline.get("decision_reference") != DECISION:
        raise engine.ContractError("baseline decision mismatch")
    if baseline.get("public_origin") != ORIGIN:
        raise engine.ContractError("baseline origin mismatch")
    if baseline.get("source_revision") != SOURCE_REVISION:
        raise engine.ContractError("baseline source revision mismatch")
    if baseline.get("active_release_expected") != PROPOSED_RELEASE:
        raise engine.ContractError("baseline active release mismatch")

    values = baseline.get("routes")
    if not isinstance(values, list):
        raise engine.ContractError("baseline routes must be an array")
    route_map = {
        item.get("path"): item
        for item in values
        if isinstance(item, dict) and isinstance(item.get("path"), str)
    }
    if list(route_map) != ROUTES:
        raise engine.ContractError("baseline routes do not match the release route order")
    for route, item in route_map.items():
        if not re.fullmatch(r"[0-9a-f]{64}", str(item.get("sha256", ""))):
            raise engine.ContractError(f"invalid SHA-256 for {route}")
        if not isinstance(item.get("bytes"), int) or item["bytes"] < 1:
            raise engine.ContractError(f"invalid byte count for {route}")
    return run_id, gap_seconds, route_map


def configure_engine() -> None:
    engine.EXPECTED_DECISION = DECISION
    engine.EXPECTED_ORIGIN = ORIGIN
    engine.EXPECTED_ROUTES = ROUTES
    engine.EXPECTED_ROUNDS = 3
    engine.RECEIPT_PREFIX = "AGENT-FRONT-DOOR-FORMAL-RELEASE"
    engine.RECEIPT_SCHEMA = "./ce-g7-vantage-receipt.schema.v0.1.json"
    engine.USER_AGENT_PREFIX = "AGENT-FRONT-DOOR-FORMAL-RELEASE"
    engine.OBSERVER_DESCRIPTION = (
        "Observe one exact Agent Front Door formal website release vantage."
    )
    engine.validate_request = validate_request


def main() -> int:
    configure_engine()
    parser = argparse.ArgumentParser(description=engine.OBSERVER_DESCRIPTION)
    parser.add_argument("--request", required=True, type=Path)
    parser.add_argument("--vantage-id", required=True)
    parser.add_argument(
        "--client",
        required=True,
        choices=("python-http-client", "system-curl"),
    )
    parser.add_argument("--output", required=True, type=Path)
    arguments = parser.parse_args()
    return engine.execute(
        arguments.request,
        arguments.vantage_id,
        arguments.client,
        arguments.output,
    )


if __name__ == "__main__":
    raise SystemExit(main())
