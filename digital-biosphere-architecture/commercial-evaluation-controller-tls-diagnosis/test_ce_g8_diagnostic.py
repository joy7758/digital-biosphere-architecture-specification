#!/usr/bin/env python3
"""Offline tests for CE-G8 privacy and classification controls."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parent


def module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(filename)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


diagnostic = module("ce_g8_diagnostic", "ce_g8_controller_diagnostic.py")
composite = module("ce_g8_composite", "ce_g8_composite.py")
correlator = module("ce_g8_correlator", "ce_g8_server_log_correlator.py")


def controller(results: dict[str, str]) -> dict:
    return {
        "records": [
            {"id": key, "result": results[key]}
            for key in ("A", "B", "C", "D")
        ]
    }


class DiagnosticTests(unittest.TestCase):
    def test_ip_classes_do_not_return_literal_ip(self) -> None:
        self.assertEqual(
            diagnostic.ip_class("198.18.0.90"),
            "SYNTHETIC_198_18_0_0_15",
        )
        self.assertEqual(diagnostic.ip_class("180.76.115.193"), "PUBLIC_IPV4")

    def test_interface_identifier_is_reduced_to_class(self) -> None:
        self.assertEqual(diagnostic.interface_class("utun9"), "TUNNEL")
        self.assertEqual(diagnostic.interface_class("en0"), "PHYSICAL")

    def test_curl_only_failure_classification(self) -> None:
        value = composite.classify(
            controller(
                {"A": "FAIL_CLOSED", "B": "PASS", "C": "PASS", "D": "PASS"}
            ),
            {"ssl_or_handshake_signal_count": 0},
        )
        self.assertEqual(value, "CLIENT_STACK_OR_LOCAL_PATH_SIGNAL")

    def test_server_handshake_signal_takes_precedence(self) -> None:
        value = composite.classify(
            controller(
                {
                    "A": "FAIL_CLOSED",
                    "B": "FAIL_CLOSED",
                    "C": "FAIL_CLOSED",
                    "D": "FAIL_CLOSED",
                }
            ),
            {"ssl_or_handshake_signal_count": 1},
        )
        self.assertEqual(value, "SERVER_HANDSHAKE_SIGNAL")

    def test_no_failure_is_observation_not_root_cause(self) -> None:
        value = composite.classify(
            controller({"A": "PASS", "B": "PASS", "C": "PASS", "D": "PASS"}),
            {"ssl_or_handshake_signal_count": 0},
        )
        self.assertEqual(value, "NO_FAILURE_OBSERVED")

    def test_salted_ip_is_not_literal(self) -> None:
        value = correlator.salted_ip("203.0.113.5", "ephemeral-salt")
        self.assertEqual(len(value), 64)
        self.assertNotIn("203.0.113.5", value)


if __name__ == "__main__":
    unittest.main()
