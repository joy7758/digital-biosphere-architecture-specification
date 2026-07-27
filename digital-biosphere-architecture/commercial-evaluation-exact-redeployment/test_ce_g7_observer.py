#!/usr/bin/env python3
"""Offline contract tests for the CE-G7 post-switch observer wrapper."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "ce_g7_observer", ROOT / "ce_g7_observer.py"
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load CE-G7 observer")
observer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(observer)


def exact_request() -> dict:
    return {
        "decision_reference": observer.DECISION,
        "public_origin": observer.ORIGIN,
        "run_id": "CE-G7-20260727-001",
        "hash_baseline_reference": (
            "ce-g7-proposed-release-hash-baseline.v0.1.json"
        ),
        "active_release_expected": observer.PROPOSED,
        "deployment_state_expected": "POST_SWITCH_PROPOSED_RELEASE",
        "immediate_gates_passed": True,
        "rounds": 3,
        "routes": observer.ROUTES,
        "requests_per_vantage": 12,
        "total_public_origin_get_cap": 24,
        "round_gap_seconds": 1,
        "sequential_within_vantage": True,
        "retry": False,
        "fallback": False,
        "tls_verification_bypass": False,
        "rollback_on_any_failure": True,
    }


class ObserverContractTests(unittest.TestCase):
    def test_exact_request_accepts_proposed_release(self) -> None:
        run_id, gap, routes = observer.validate_request(
            exact_request(), "GITHUB_HOSTED_UBUNTU", "python-http-client"
        )
        self.assertEqual(run_id, "CE-G7-20260727-001")
        self.assertEqual(gap, 1)
        self.assertEqual(list(routes), observer.ROUTES)

    def test_pre_switch_request_is_rejected(self) -> None:
        request = exact_request()
        request["deployment_state_expected"] = "PRE_SWITCH"
        with self.assertRaises(observer.engine.ContractError):
            observer.validate_request(
                request, "GITHUB_HOSTED_UBUNTU", "python-http-client"
            )

    def test_missing_immediate_gate_is_rejected(self) -> None:
        request = exact_request()
        request["immediate_gates_passed"] = False
        with self.assertRaises(observer.engine.ContractError):
            observer.validate_request(
                request, "GITHUB_HOSTED_UBUNTU", "python-http-client"
            )

    def test_retry_is_rejected(self) -> None:
        request = exact_request()
        request["retry"] = True
        with self.assertRaises(observer.engine.ContractError):
            observer.validate_request(
                request, "GITHUB_HOSTED_UBUNTU", "python-http-client"
            )

    def test_baseline_is_valid_json(self) -> None:
        value = json.loads(
            (
                ROOT / "ce-g7-proposed-release-hash-baseline.v0.1.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(value["decision_reference"], observer.DECISION)
        self.assertEqual(len(value["routes"]), 11)


if __name__ == "__main__":
    unittest.main()
