#!/usr/bin/env python3
"""Offline tests for the CE-G11 target-bound correlation adapter."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from datetime import timezone
import unittest


ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import ce_g11_target_bound_correlator as adapter


BINDING = ROOT / "ce-g11-correlation-binding.offline-fixture.v0.1.json"
BINDING_SCHEMA = ROOT / "ce-g11-correlation-binding.schema.v0.1.json"
ACCESS_FIXTURE = ROOT / "fixtures" / "access.log"
ERROR_FIXTURE = ROOT / "fixtures" / "error.log"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def journal_ok(command, **kwargs):
    return subprocess.CompletedProcess(command, 0, "", "")


class TargetBoundCorrelatorTests(unittest.TestCase):
    def execute(self, current_target: str = adapter.EXPECTED_RELEASE):
        return adapter.execute(
            BINDING,
            digest(BINDING),
            "2026-07-27T12:31:56Z",
            "2026-07-27T12:31:57Z",
            "fixture-salt",
            access_log=ACCESS_FIXTURE,
            error_log=ERROR_FIXTURE,
            journal_runner=journal_ok,
            local_tz=timezone.utc,
            current_target_reader=lambda: current_target,
        )

    def mutated_binding(self, directory: str, **changes):
        value = json.loads(BINDING.read_text(encoding="utf-8"))
        value.update(changes)
        path = Path(directory) / "binding.json"
        path.write_text(
            json.dumps(value, indent=2, sort_keys=False) + "\n",
            encoding="utf-8",
        )
        return path, digest(path)

    def test_binding_fixture_matches_draft_2020_12_contract(self):
        schema = json.loads(BINDING_SCHEMA.read_text(encoding="utf-8"))
        value = json.loads(BINDING.read_text(encoding="utf-8"))
        self.assertEqual(
            schema["$schema"],
            "https://json-schema.org/draft/2020-12/schema",
        )
        self.assertEqual(schema["type"], "object")
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(set(schema["required"]), set(value))
        self.assertEqual(set(schema["properties"]), set(value))
        for field, contract in schema["properties"].items():
            self.assertEqual(value[field], contract["const"])

    def test_proposed_target_and_exact_identity_pass(self):
        value = self.execute()
        self.assertEqual(
            value["receipt_id"],
            "TITMAS-CE-G11-SERVER-CORRELATION-001",
        )
        self.assertEqual(
            value["decision_reference"],
            "TITMAS-COMMERCIAL-EVALUATION-CE-G11",
        )
        self.assertEqual(
            value["current_release"],
            adapter.EXPECTED_RELEASE,
        )
        self.assertEqual(value["status"], "EXACT_WINDOW_CORRELATION_COMPLETE")
        self.assertEqual(value["access"]["records"], 2)
        self.assertEqual(value["access"]["path_classes"]["TARGET_EN"], 1)
        self.assertFalse(value["binding"]["binding_is_authority"])
        self.assertFalse(value["authority_effect"])

    def test_stable_target_is_rejected_for_proposed_binding(self):
        with self.assertRaises(adapter.StageFailure) as raised:
            self.execute(historical_stable_release())
        self.assertEqual(
            raised.exception.stage_code,
            "CURRENT_TARGET_MISMATCH",
        )

    def test_unknown_target_is_rejected(self):
        with self.assertRaises(adapter.StageFailure) as raised:
            self.execute(
                "/srv/tmai/releases/"
                "0000000000000000000000000000000000000000"
            )
        self.assertEqual(
            raised.exception.stage_code,
            "CURRENT_TARGET_MISMATCH",
        )

    def test_wrong_decision_is_rejected_after_valid_hash(self):
        with tempfile.TemporaryDirectory() as directory:
            path, sha256 = self.mutated_binding(
                directory,
                declared_decision_reference=(
                    "TITMAS-COMMERCIAL-EVALUATION-CE-G8"
                ),
            )
            with self.assertRaises(adapter.StageFailure) as raised:
                adapter.load_binding(path, sha256)
        self.assertEqual(
            raised.exception.stage_code,
            "BINDING_DECISION_MISMATCH",
        )

    def test_wrong_receipt_is_rejected_after_valid_hash(self):
        with tempfile.TemporaryDirectory() as directory:
            path, sha256 = self.mutated_binding(
                directory,
                receipt_id="TITMAS-CE-G8-SERVER-CORRELATION-001",
            )
            with self.assertRaises(adapter.StageFailure) as raised:
                adapter.load_binding(path, sha256)
        self.assertEqual(
            raised.exception.stage_code,
            "BINDING_RECEIPT_MISMATCH",
        )

    def test_binding_tamper_is_rejected_before_parsing(self):
        original_sha256 = digest(BINDING)
        with tempfile.TemporaryDirectory() as directory:
            path, _ = self.mutated_binding(
                directory,
                authority_effect=True,
            )
            with self.assertRaises(adapter.StageFailure) as raised:
                adapter.load_binding(path, original_sha256)
        self.assertEqual(
            raised.exception.stage_code,
            "BINDING_HASH_MISMATCH",
        )

    def test_authority_effect_true_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path, sha256 = self.mutated_binding(
                directory,
                authority_effect=True,
            )
            with self.assertRaises(adapter.StageFailure) as raised:
                adapter.load_binding(path, sha256)
        self.assertEqual(
            raised.exception.stage_code,
            "BINDING_AUTHORITY_EFFECT_INVALID",
        )

    def test_authorized_offline_fixture_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path, sha256 = self.mutated_binding(
                directory,
                authorization_status="AUTHORIZED",
            )
            with self.assertRaises(adapter.StageFailure) as raised:
                adapter.load_binding(path, sha256)
        self.assertEqual(
            raised.exception.stage_code,
            "BINDING_AUTHORIZATION_STATUS_INVALID",
        )

    def test_additional_binding_property_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path, sha256 = self.mutated_binding(
                directory,
                unexpected="value",
            )
            with self.assertRaises(adapter.StageFailure) as raised:
                adapter.load_binding(path, sha256)
        self.assertEqual(
            raised.exception.stage_code,
            "BINDING_SCHEMA_INVALID",
        )

    def test_raw_log_salt_and_literal_fixture_sources_are_not_persisted(self):
        value = self.execute()
        serialized = json.dumps(value)
        self.assertFalse(value["raw_logs_persisted"])
        self.assertNotIn("fixture-source-start", serialized)
        self.assertNotIn("fixture-source-end", serialized)
        self.assertNotIn("fixture-salt", serialized)
        self.assertNotIn("SSL_do_handshake", serialized)

    def test_journal_error_maps_to_stable_sanitized_stage(self):
        def failed_journal(command, **kwargs):
            return subprocess.CompletedProcess(
                command,
                2,
                "",
                "private raw journal failure",
            )

        with self.assertRaises(adapter.StageFailure) as raised:
            adapter.execute(
                BINDING,
                digest(BINDING),
                "2026-07-27T12:31:56Z",
                "2026-07-27T12:31:57Z",
                "fixture-salt",
                access_log=ACCESS_FIXTURE,
                error_log=ERROR_FIXTURE,
                journal_runner=failed_journal,
                local_tz=timezone.utc,
                current_target_reader=lambda: adapter.EXPECTED_RELEASE,
            )
        receipt = adapter._failure_receipt(raised.exception)
        serialized = json.dumps(receipt)
        self.assertEqual(
            receipt["error_class"],
            "JOURNAL_PARSE_FAILED",
        )
        self.assertNotIn("private raw journal failure", serialized)
        self.assertFalse(receipt["authority_effect"])

    def test_adapter_reuses_historical_parsers_without_copying_them(self):
        source = (
            ROOT / "ce_g11_target_bound_correlator.py"
        ).read_text(encoding="utf-8")
        for call in (
            "historical.parse_iso",
            "historical.access_records",
            "historical.error_classes",
            "historical.journal_classes",
        ):
            self.assertIn(call, source)
        for copied_definition in (
            "def parse_access_line(",
            "def parse_access_timestamp(",
            "def parse_error_timestamp(",
            "def salted_ip(",
        ):
            self.assertNotIn(copied_definition, source)


def historical_stable_release() -> str:
    return "/srv/tmai/releases/7da4bcf16eeec7de1c61031fe08fc04081cf8705"


if __name__ == "__main__":
    unittest.main()
