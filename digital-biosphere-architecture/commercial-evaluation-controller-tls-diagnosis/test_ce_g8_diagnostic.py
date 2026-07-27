#!/usr/bin/env python3
"""Offline tests for CE-G8 privacy and classification controls."""

from __future__ import annotations

import importlib.util
from datetime import timezone
import json
from pathlib import Path
import subprocess
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

    def test_salted_ip_hashes_ipv4_and_ipv6_without_literal(self) -> None:
        values = ("203.0.113.5", "2001:db8::5")
        for source in values:
            with self.subTest(source=source):
                value = correlator.salted_ip(source, "ephemeral-salt")
                self.assertEqual(len(value), 64)
                self.assertNotIn(source, value)

    def test_original_double_escaped_regex_defect_is_removed(self) -> None:
        source = (
            ROOT / "ce_g8_server_log_correlator.py"
        ).read_text(encoding="utf-8")
        self.assertNotIn("re.compile", source)
        self.assertNotIn(r"\\\\[", source)

    def test_access_fixture_includes_exact_boundaries_only(self) -> None:
        start = correlator.parse_iso("2026-07-27T12:31:56Z")
        end = correlator.parse_iso("2026-07-27T12:31:57Z")
        statuses, paths, hashes = correlator.access_records(
            start,
            end,
            "fixture-salt",
            ROOT / "fixtures" / "access.log",
        )
        self.assertEqual(statuses["HTTP_2XX"], 1)
        self.assertEqual(statuses["HTTP_5XX"], 1)
        self.assertEqual(paths["TARGET_EN"], 1)
        self.assertEqual(paths["OTHER"], 1)
        # Persisted fixtures use opaque source labels. Address hashing is
        # covered separately without storing a literal source address here.
        self.assertEqual(len(hashes), 0)

    def test_error_fixture_classifies_exact_window(self) -> None:
        start = correlator.parse_iso("2026-07-27T12:31:56Z")
        end = correlator.parse_iso("2026-07-27T12:31:57Z")
        counts = correlator.error_classes(
            start,
            end,
            ROOT / "fixtures" / "error.log",
            local_tz=timezone.utc,
        )
        self.assertEqual(counts["SSL_HANDSHAKE"], 1)
        self.assertEqual(counts["UPSTREAM"], 1)
        self.assertEqual(sum(counts.values()), 2)

    def test_journal_uses_exact_epoch_and_sanitizes_invalid_json(self) -> None:
        captured = {}

        def runner(command, **kwargs):
            captured["command"] = command
            stdout = "\n".join(
                [
                    json.dumps({"MESSAGE": "SSL handshake failed"}),
                    "not-json",
                ]
            )
            return subprocess.CompletedProcess(command, 0, stdout, "")

        start = correlator.parse_iso("2026-07-27T12:31:56Z")
        end = correlator.parse_iso("2026-07-27T12:31:57Z")
        counts = correlator.journal_classes(start, end, runner=runner)
        self.assertEqual(
            captured["command"][captured["command"].index("--since") + 1],
            f"@{int(start.timestamp())}",
        )
        self.assertEqual(
            captured["command"][captured["command"].index("--until") + 1],
            f"@{int(end.timestamp())}",
        )
        self.assertEqual(counts["SSL_OR_HANDSHAKE"], 1)
        self.assertEqual(counts["MALFORMED_JSON"], 1)

    def test_journal_nonzero_fails_with_stable_stage(self) -> None:
        def runner(command, **kwargs):
            return subprocess.CompletedProcess(command, 2, "", "raw error")

        start = correlator.parse_iso("2026-07-27T12:31:56Z")
        end = correlator.parse_iso("2026-07-27T12:31:57Z")
        with self.assertRaises(correlator.StageFailure) as raised:
            correlator.journal_classes(start, end, runner=runner)
        self.assertEqual(
            raised.exception.stage_code, "JOURNAL_COMMAND_FAILED"
        )

    def test_execute_with_fixtures_persists_no_raw_values(self) -> None:
        def runner(command, **kwargs):
            return subprocess.CompletedProcess(command, 0, "", "")

        value = correlator.execute(
            "2026-07-27T12:31:56Z",
            "2026-07-27T12:31:57Z",
            "fixture-salt",
            access_log=ROOT / "fixtures" / "access.log",
            error_log=ROOT / "fixtures" / "error.log",
            journal_runner=runner,
            local_tz=timezone.utc,
            current_target_reader=lambda: correlator.ROLLBACK,
        )
        serialized = json.dumps(value)
        self.assertFalse(value["raw_logs_persisted"])
        self.assertNotIn("fixture-source-start", serialized)
        self.assertNotIn("fixture-source-end", serialized)
        self.assertNotIn("fixture-salt", serialized)
        self.assertNotIn("SSL_do_handshake", serialized)

    def test_current_target_error_is_stable_and_sanitized(self) -> None:
        with self.assertRaises(correlator.StageFailure) as raised:
            correlator.execute(
                "2026-07-27T12:31:56Z",
                "2026-07-27T12:31:57Z",
                "fixture-salt",
                access_log=ROOT / "fixtures" / "access.log",
                error_log=ROOT / "fixtures" / "error.log",
                current_target_reader=lambda: "/unexpected",
            )
        self.assertEqual(
            raised.exception.stage_code, "CURRENT_TARGET_MISMATCH"
        )


if __name__ == "__main__":
    unittest.main()
