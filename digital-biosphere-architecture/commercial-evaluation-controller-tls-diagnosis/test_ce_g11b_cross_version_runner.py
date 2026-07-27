#!/usr/bin/env python3
"""Offline tests for the CE-G11B cross-version runner candidate."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import re
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parent
WORKFLOW = (
    ROOT.parents[1]
    / ".github"
    / "workflows"
    / "titmas-ce-g11b-target-bound-cross-version.yml"
)
REQUEST_SCHEMA = ROOT / "ce-g11b-run-request.schema.v0.1.json"
SPEC = importlib.util.spec_from_file_location(
    "ce_g11b_cross_version_runner",
    ROOT / "ce_g11b_cross_version_runner.py",
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load CE-G11B runner")
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


def completed(
    returncode: int,
    count: int = 13,
    private_failure: str = "raw private failure",
) -> subprocess.CompletedProcess[str]:
    return subprocess.CompletedProcess(
        ["python"],
        returncode,
        "",
        f"Ran {count} tests in 0.001s\n"
        + ("OK\n" if returncode == 0 else private_failure + "\n"),
    )


def git_success(*args, **kwargs) -> subprocess.CompletedProcess[str]:
    return subprocess.CompletedProcess(["git"], 0, "", "")


class CrossVersionRunnerTests(unittest.TestCase):
    def test_workflow_is_exactly_scoped_and_read_only(self) -> None:
        value = WORKFLOW.read_text(encoding="utf-8")
        self.assertNotIn("workflow_dispatch:", value)
        self.assertIn("\n  push:", value)
        self.assertIn("- codex/production-observability-baseline", value)
        self.assertIn(
            "- digital-biosphere-architecture/"
            "commercial-evaluation-controller-tls-diagnosis/"
            "ce-g11b-run-request.v0.1.json",
            value,
        )
        self.assertNotIn("\n  pull_request:", value)
        self.assertNotIn("\n  schedule:", value)
        self.assertIn("permissions:\n  contents: read", value)
        self.assertIn("timeout-minutes: 5", value)
        self.assertIn("fetch-depth: 2", value)
        self.assertNotIn("secrets.", value)

    def test_workflow_matrix_and_actions_are_exact(self) -> None:
        value = WORKFLOW.read_text(encoding="utf-8")
        for version in runner.EXPECTED_PYTHON_VERSIONS:
            self.assertEqual(value.count(f'- "{version}"'), 1)
        actions = re.findall(
            r"uses: ([A-Za-z0-9_./-]+)@([0-9a-f]+)",
            value,
        )
        self.assertEqual(
            actions,
            [
                (
                    "actions/checkout",
                    "11d5960a326750d5838078e36cf38b85af677262",
                ),
                (
                    "actions/setup-python",
                    "ece7cb06caefa5fff74198d8649806c4678c61a1",
                ),
                (
                    "actions/upload-artifact",
                    "ea165f8d65b6e75b540449e92b4886f43607fa02",
                ),
            ],
        )

    def test_frozen_inputs_match(self) -> None:
        self.assertEqual(
            runner.verify_frozen_inputs(),
            runner.FROZEN_INPUTS,
        )

    def test_binding_contract_and_authority_boundary_match(self) -> None:
        runner.verify_binding_contract()
        value = json.loads(runner.BINDING_FIXTURE.read_text())
        self.assertEqual(value["authorization_status"], "NOT_AUTHORIZED")
        self.assertFalse(value["authority_effect"])

    def test_binding_authority_elevation_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            schema = Path(directory) / "schema.json"
            fixture = Path(directory) / "fixture.json"
            schema.write_text(runner.BINDING_SCHEMA.read_text())
            value = json.loads(runner.BINDING_FIXTURE.read_text())
            value["authority_effect"] = True
            fixture.write_text(json.dumps(value))
            with self.assertRaises(runner.StageFailure) as raised:
                runner.verify_binding_contract(schema, fixture)
        self.assertEqual(
            raised.exception.stage_code,
            "BINDING_SCHEMA_CONST_MISMATCH",
        )

    def test_fixture_privacy_rejects_literal_ipv4_and_ipv6(self) -> None:
        self.assertTrue(runner.contains_literal_ip("source 203.0.113.5"))
        self.assertTrue(runner.contains_literal_ip("source [2001:db8::5]"))
        self.assertFalse(runner.contains_literal_ip("fixture-source-start"))

    def request_value(self) -> dict:
        return {
            "$schema": "./ce-g11b-run-request.schema.v0.1.json",
            "request_id": runner.EXPECTED_REQUEST_ID,
            "version": "0.1.0",
            "status": "AUTHORIZED_SINGLE_TRIGGER",
            "decision_reference": runner.COMPONENT_DECISION,
            "trigger_decision_reference": runner.TRIGGER_DECISION,
            "created_at": "2026-07-27T00:00:00Z",
            "source_branch": runner.EXPECTED_BRANCH,
            "phase_a_commit": "a" * 40,
            "trigger": {
                "event": "push",
                "branch": runner.EXPECTED_BRANCH,
                "path": runner.EXPECTED_TRIGGER_PATH,
                "events_cap": 1,
            },
            "python_matrix": list(runner.EXPECTED_PYTHON_VERSIONS),
            "frozen_inputs": runner.FROZEN_INPUTS,
            "phase_a_components": {
                name: runner.sha256_file(path)
                for name, path in runner.PHASE_A_COMPONENTS.items()
            },
            "actions": runner.EXPECTED_ACTIONS,
            "caps": runner.EXPECTED_CAPS,
            "retry": False,
            "fallback": False,
            "result_schema_reference":
                "./ce-g11b-cross-version-result.schema.v0.1.json",
        }

    def request(self, directory: str) -> Path:
        path = Path(directory) / "request.json"
        path.write_text(json.dumps(self.request_value()), encoding="utf-8")
        return path

    def test_request_schema_matches_synthetic_contract(self) -> None:
        schema = json.loads(REQUEST_SCHEMA.read_text())
        value = self.request_value()
        self.assertEqual(
            schema["$schema"],
            "https://json-schema.org/draft/2020-12/schema",
        )
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(set(schema["required"]), set(value))
        self.assertEqual(set(schema["properties"]), set(value))
        for field in (
            "$schema",
            "request_id",
            "version",
            "status",
            "decision_reference",
            "trigger_decision_reference",
            "source_branch",
            "python_matrix",
            "frozen_inputs",
            "actions",
            "caps",
            "retry",
            "fallback",
            "result_schema_reference",
        ):
            self.assertEqual(schema["properties"][field]["const"], value[field])

    def test_version_mismatch_fails_before_suites(self) -> None:
        calls = 0

        def no_call(*args, **kwargs):
            nonlocal calls
            calls += 1
            return completed(0)

        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "receipt.json"
            exit_code = runner.execute(
                self.request(directory),
                "3.10.20",
                "b" * 40,
                "TEST",
                output,
                version_reader=lambda: "3.10.19",
                git_runner=git_success,
                test_runner=no_call,
            )
            receipt = json.loads(output.read_text())
        self.assertEqual(exit_code, 1)
        self.assertEqual(calls, 0)
        self.assertEqual(receipt["error_class"], "PYTHON_VERSION_MISMATCH")

    def test_pass_receipt_records_both_suites_and_is_sanitized(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "receipt.json"
            exit_code = runner.execute(
                self.request(directory),
                "3.10.20",
                "b" * 40,
                "TEST",
                output,
                version_reader=lambda: "3.10.20",
                git_runner=git_success,
                test_runner=lambda *args, **kwargs: completed(0),
            )
            text = output.read_text()
            receipt = json.loads(text)
        self.assertEqual(exit_code, 0)
        self.assertEqual(receipt["status"], "PYTHON_VERSION_OFFLINE_PASS")
        self.assertEqual(receipt["checks"]["new_adapter_test_count"], 13)
        self.assertEqual(receipt["checks"]["historical_test_count"], 13)
        self.assertEqual(receipt["checks"]["total_test_count"], 26)
        self.assertTrue(receipt["checks"]["binding_contract_exact_match"])
        self.assertFalse(receipt["effects"]["authority"])
        self.assertFalse(receipt["effects"]["live_binding"])
        self.assertNotIn("raw private failure", text)

    def test_test_process_receives_allowlisted_environment_only(self) -> None:
        captured = []

        def inspect_environment(*args, **kwargs):
            captured.append(dict(kwargs["env"]))
            return completed(0)

        with tempfile.TemporaryDirectory() as directory:
            exit_code = runner.execute(
                self.request(directory),
                "3.10.20",
                "d" * 40,
                "TEST",
                Path(directory) / "receipt.json",
                version_reader=lambda: "3.10.20",
                git_runner=git_success,
                test_runner=inspect_environment,
            )
        self.assertEqual(exit_code, 0)
        self.assertEqual(len(captured), 2)
        for environment in captured:
            self.assertEqual(environment["PYTHONDONTWRITEBYTECODE"], "1")
            self.assertTrue(
                set(environment)
                <= set(runner.TEST_ENVIRONMENT_ALLOWLIST)
                | {"PYTHONDONTWRITEBYTECODE"}
            )
            self.assertFalse(
                any(
                    token in name
                    for name in environment
                    for token in ("TOKEN", "SECRET", "KEY")
                )
            )

    def test_new_suite_failure_stops_before_historical_suite(self) -> None:
        calls = 0

        def fail_first(*args, **kwargs):
            nonlocal calls
            calls += 1
            return completed(1)

        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "receipt.json"
            exit_code = runner.execute(
                self.request(directory),
                "3.10.20",
                "e" * 40,
                "TEST",
                output,
                version_reader=lambda: "3.10.20",
                git_runner=git_success,
                test_runner=fail_first,
            )
            text = output.read_text()
            receipt = json.loads(text)
        self.assertEqual(exit_code, 1)
        self.assertEqual(calls, 1)
        self.assertEqual(receipt["error_class"], "NEW_ADAPTER_SUITE_FAILED")
        self.assertNotIn("raw private failure", text)

    def test_historical_failure_returns_stable_error(self) -> None:
        calls = 0

        def fail_second(*args, **kwargs):
            nonlocal calls
            calls += 1
            return completed(0 if calls == 1 else 1)

        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "receipt.json"
            exit_code = runner.execute(
                self.request(directory),
                "3.10.20",
                "f" * 40,
                "TEST",
                output,
                version_reader=lambda: "3.10.20",
                git_runner=git_success,
                test_runner=fail_second,
            )
            receipt = json.loads(output.read_text())
        self.assertEqual(exit_code, 1)
        self.assertEqual(calls, 2)
        self.assertEqual(receipt["error_class"], "HISTORICAL_SUITE_FAILED")

    def test_request_contract_rejects_retry(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request = self.request(directory)
            value = json.loads(request.read_text())
            value["retry"] = True
            request.write_text(json.dumps(value))
            output = Path(directory) / "receipt.json"
            exit_code = runner.execute(
                request,
                "3.10.20",
                "e" * 40,
                "TEST",
                output,
                version_reader=lambda: "3.10.20",
                git_runner=git_success,
                test_runner=lambda *args, **kwargs: completed(0),
            )
            receipt = json.loads(output.read_text())
        self.assertEqual(exit_code, 1)
        self.assertEqual(
            receipt["error_class"],
            "RUN_REQUEST_RETRY_NOT_FALSE",
        )

    def test_phase_a_component_hash_mismatch_is_rejected(self) -> None:
        value = self.request_value()
        value["phase_a_components"][
            "ce_g11b_cross_version_runner.py"
        ] = "0" * 64
        with self.assertRaises(runner.StageFailure) as raised:
            runner.validate_request(
                value,
                "3.10.20",
                "b" * 40,
                git_runner=git_success,
            )
        self.assertEqual(
            raised.exception.stage_code,
            "PHASE_A_COMPONENT_HASH_MISMATCH",
        )


if __name__ == "__main__":
    unittest.main()
