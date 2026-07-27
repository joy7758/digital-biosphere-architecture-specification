"""Offline tests for the CE-G5 fail-closed observation harness."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock


MODULE_PATH = Path(__file__).with_name("ce_g5_observer.py")
SPEC = importlib.util.spec_from_file_location("ce_g5_observer", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load ce_g5_observer")
observer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(observer)


def digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


class ObserverTests(unittest.TestCase):
    def setUp(self) -> None:
        self.bodies = {
            route: f"fixed body for {route}".encode("utf-8")
            for route in observer.EXPECTED_ROUTES
        }
        self.baseline = {
            "status": "FIXED_CURRENT_RELEASE_BASELINE",
            "public_origin": observer.EXPECTED_ORIGIN,
            "active_release": "/srv/tmai/releases/test",
            "routes": [
                {
                    "path": route,
                    "bytes": len(self.bodies[route]),
                    "sha256": digest(self.bodies[route]),
                }
                for route in observer.EXPECTED_ROUTES
            ],
        }
        self.request = {
            "decision_reference": observer.EXPECTED_DECISION,
            "run_id": "CE-G5-TEST",
            "public_origin": observer.EXPECTED_ORIGIN,
            "active_release_expected": "/srv/tmai/releases/test",
            "hash_baseline_reference": "baseline.json",
            "rounds": 3,
            "routes": observer.EXPECTED_ROUTES,
            "requests_per_vantage": 12,
            "total_public_origin_get_cap": 24,
            "round_gap_seconds": 0,
            "retry": False,
            "fallback": False,
            "tls_verification_bypass": False,
            "sequential_within_vantage": True,
        }

    def successful_observation(self, route: str, _user_agent: str):
        return (
            {
                "curl_exit_code": None,
                "http_code": 200,
                "remote_ip": "203.0.113.10",
                "ssl_verify_result": 0,
                "tls_version": "TLSv1.3",
                "cipher": "TEST_CIPHER",
                "latency_seconds": 0.01,
            },
            self.bodies[route],
        )

    def run_execute(self, observation):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "receipt.json"
            with (
                mock.patch.object(
                    observer,
                    "load_json",
                    side_effect=[self.request, self.baseline],
                ),
                mock.patch.object(observer, "proxy_state", return_value={}),
                mock.patch.object(
                    observer,
                    "python_stack",
                    return_value={
                        "client": "python-http-client",
                        "client_version": "test",
                        "tls_backend": "OpenSSL test",
                        "executable": "/usr/bin/python3",
                    },
                ),
                mock.patch.object(
                    observer,
                    "observe_with_python",
                    side_effect=observation,
                ) as request_mock,
                mock.patch.object(observer.time, "sleep"),
            ):
                exit_code = observer.execute(
                    Path("request.json"),
                    "GITHUB_HOSTED_UBUNTU",
                    "python-http-client",
                    output,
                )
            receipt = json.loads(output.read_text(encoding="utf-8"))
        return exit_code, receipt, request_mock.call_count

    def test_exact_twelve_requests_pass(self) -> None:
        exit_code, receipt, call_count = self.run_execute(
            self.successful_observation
        )
        self.assertEqual(exit_code, 0)
        self.assertEqual(call_count, 12)
        self.assertEqual(receipt["execution"]["requests_executed"], 12)
        self.assertEqual(receipt["summary"]["passes"], 12)
        self.assertEqual(receipt["status"], "VANTAGE_OBSERVATION_PASS")

    def test_content_failure_is_preserved_without_retry(self) -> None:
        calls = 0

        def one_mismatch(route: str, user_agent: str):
            nonlocal calls
            calls += 1
            metadata, body = self.successful_observation(route, user_agent)
            if calls == 1:
                body = b"mismatch"
            return metadata, body

        exit_code, receipt, call_count = self.run_execute(one_mismatch)
        self.assertEqual(exit_code, 1)
        self.assertEqual(call_count, 12)
        self.assertEqual(receipt["summary"]["failures"], 1)
        self.assertEqual(
            receipt["records"][0]["error_class"], "HASH_OR_SIZE_MISMATCH"
        )
        self.assertEqual(
            receipt["status"], "VANTAGE_OBSERVATION_FAIL_CLOSED"
        )

    def test_retry_true_is_rejected_before_network(self) -> None:
        self.request["retry"] = True
        exit_code, receipt, call_count = self.run_execute(
            self.successful_observation
        )
        self.assertEqual(exit_code, 1)
        self.assertEqual(call_count, 0)
        self.assertEqual(
            receipt["status"], "FAIL_CLOSED_CONTRACT_OR_ENVIRONMENT"
        )
        self.assertEqual(receipt["error_class"], "CONTRACT_ERROR")


if __name__ == "__main__":
    unittest.main()
