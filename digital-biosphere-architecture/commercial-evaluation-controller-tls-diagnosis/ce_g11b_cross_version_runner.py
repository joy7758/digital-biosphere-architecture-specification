#!/usr/bin/env python3
"""Run one offline CE-G11B Python-version validation job.

The runner verifies ten frozen CE-G11A and historical inputs, validates the
offline binding contract, checks the exact Python patch version, and executes
the 13 target-bound adapter tests plus the 13 historical regression tests.

It consumes a future, separately authorized run request. Merely importing or
testing this module does not create that request, start GitHub Actions, access
the TITMAS site or server, create a live binding, or grant authority.
"""

from __future__ import annotations

import argparse
import hashlib
import ipaddress
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
from typing import Any, Callable


ROOT = Path(__file__).resolve().parent
COMPONENT_DECISION = "TITMAS-COMMERCIAL-EVALUATION-CE-G11B-A"
TRIGGER_DECISION = "TITMAS-COMMERCIAL-EVALUATION-CE-G11B-B"
FROZEN_SOURCE_COMMIT = "457d59f263ef52bb31bba1902cfe4c429e3c2207"
EXPECTED_PYTHON_VERSIONS = (
    "3.10.20",
    "3.11.15",
    "3.12.13",
    "3.13.14",
    "3.14.6",
)
EXPECTED_NEW_TEST_COUNT = 13
EXPECTED_HISTORICAL_TEST_COUNT = 13
EXPECTED_TOTAL_TEST_COUNT = 26
EXPECTED_REQUEST_ID = "TITMAS-CE-G11B-RUN-REQUEST-001"
EXPECTED_BRANCH = "codex/production-observability-baseline"
EXPECTED_TRIGGER_PATH = (
    "digital-biosphere-architecture/"
    "commercial-evaluation-controller-tls-diagnosis/"
    "ce-g11b-run-request.v0.1.json"
)
EXPECTED_ACTIONS = {
    "actions/checkout": "11d5960a326750d5838078e36cf38b85af677262",
    "actions/setup-python": "ece7cb06caefa5fff74198d8649806c4678c61a1",
    "actions/upload-artifact": "ea165f8d65b6e75b540449e92b4886f43607fa02",
}
EXPECTED_CAPS = {
    "trigger_events": 1,
    "workflow_runs": 1,
    "matrix_jobs": 5,
    "target_public_site_requests": 0,
    "ssh_sessions": 0,
    "server_reads": 0,
    "server_writes": 0,
    "deployments": 0,
    "dbos_changes": 0,
    "saee_changes": 0,
    "live_bindings_created": 0,
    "model_requests_during_execution": 0,
}
TEST_ENVIRONMENT_ALLOWLIST = (
    "HOME",
    "LANG",
    "LC_ALL",
    "PATH",
    "SYSTEMROOT",
    "TMPDIR",
    "TZ",
)
FROZEN_INPUTS = {
    "ce_g8_server_log_correlator.py":
        "508245e1a49eb2fba94a3617517da2dfd200f9c8b1677cfdd92e186130ab6bef",
    "test_ce_g8_diagnostic.py":
        "22f500fa5bdb3e72ca424e8bfd800827e6e585c554270bf260d9271a2de74829",
    "fixtures/access.log":
        "3e63d82fd85b151cf3b5479b11b020d113790ac8cd71df561699479dc057bf8d",
    "fixtures/error.log":
        "38e96f94008c3bef6e988f5ef6725f0ccea5439b27a5be35e8f1722ce1709c55",
    "ce-g11-correlation-binding.schema.v0.1.json":
        "2263c3c224097f6d7ed233bd5ff261a6dd225e11f10e290d0d1dc4aa382be684",
    "ce-g11-correlation-binding.offline-fixture.v0.1.json":
        "cee58ceb4088ba99f4c0c5631a309898bf9c7df8a6d6ad64fc85ac920ad80f06",
    "ce_g11_target_bound_correlator.py":
        "b72ad6e707a95f65e20f235963306e04c4f3e81342f4c762514cffcbf7e2d0e3",
    "test_ce_g11_target_bound_correlator.py":
        "39d1b06a16197407fa97e5d884e5703deaa155030fcaeff6bbabba2da152f5cb",
    "ce-g11a-offline-remediation-result.schema.v0.1.json":
        "94e569e8efe70acf767c4680c86204681299ec3ad2179107c43d003d74f874f5",
    "ce-g11a-offline-remediation-result.v0.1.json":
        "47980dcabff53312516a925633db8d5087efeb3058c1422d61ef115788505de7",
}
PHASE_A_COMPONENTS = {
    ".github/workflows/titmas-ce-g11b-target-bound-cross-version.yml":
        ROOT.parents[1]
        / ".github"
        / "workflows"
        / "titmas-ce-g11b-target-bound-cross-version.yml",
    "ce_g11b_cross_version_runner.py":
        ROOT / "ce_g11b_cross_version_runner.py",
    "test_ce_g11b_cross_version_runner.py":
        ROOT / "test_ce_g11b_cross_version_runner.py",
    "ce-g11b-run-request.schema.v0.1.json":
        ROOT / "ce-g11b-run-request.schema.v0.1.json",
    "ce-g11b-cross-version-result.schema.v0.1.json":
        ROOT / "ce-g11b-cross-version-result.schema.v0.1.json",
}
BINDING_SCHEMA = ROOT / "ce-g11-correlation-binding.schema.v0.1.json"
BINDING_FIXTURE = (
    ROOT / "ce-g11-correlation-binding.offline-fixture.v0.1.json"
)


class StageFailure(RuntimeError):
    """Stable fail-closed stage code that omits private input values."""

    def __init__(self, stage_code: str):
        super().__init__(stage_code)
        self.stage_code = stage_code


def sha256_file(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            value.update(chunk)
    return value.hexdigest()


def verify_frozen_inputs(root: Path = ROOT) -> dict[str, str]:
    observed: dict[str, str] = {}
    for relative, expected in FROZEN_INPUTS.items():
        path = root / relative
        if not path.is_file():
            raise StageFailure("FROZEN_INPUT_MISSING")
        actual = sha256_file(path)
        if actual != expected:
            raise StageFailure("FROZEN_INPUT_HASH_MISMATCH")
        observed[relative] = actual
    return observed


def contains_literal_ip(value: str) -> bool:
    separators = "[](){}<>,;\"'"
    for token in value.split():
        candidate = token.strip(separators)
        try:
            ipaddress.ip_address(candidate)
        except ValueError:
            continue
        return True
    return False


def verify_fixture_privacy(root: Path = ROOT) -> None:
    for relative in ("fixtures/access.log", "fixtures/error.log"):
        value = (root / relative).read_text(encoding="utf-8")
        if contains_literal_ip(value):
            raise StageFailure("FIXTURE_LITERAL_IP_FOUND")


def _load_json(path: Path, failure: str) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        raise StageFailure(failure)


def verify_binding_contract(
    schema_path: Path = BINDING_SCHEMA,
    fixture_path: Path = BINDING_FIXTURE,
) -> None:
    """Validate the exact const-only Draft 2020-12 binding contract."""
    schema = _load_json(schema_path, "BINDING_SCHEMA_READ_FAILED")
    fixture = _load_json(fixture_path, "BINDING_FIXTURE_READ_FAILED")
    if not isinstance(schema, dict) or not isinstance(fixture, dict):
        raise StageFailure("BINDING_CONTRACT_NOT_OBJECT")
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        raise StageFailure("BINDING_DRAFT_MISMATCH")
    if schema.get("type") != "object" or schema.get("additionalProperties") is not False:
        raise StageFailure("BINDING_SCHEMA_BOUNDARY_MISMATCH")
    required = schema.get("required")
    properties = schema.get("properties")
    if (
        not isinstance(required, list)
        or not isinstance(properties, dict)
        or set(required) != set(fixture)
        or set(properties) != set(fixture)
    ):
        raise StageFailure("BINDING_SCHEMA_FIELD_MISMATCH")
    for field, value in fixture.items():
        contract = properties.get(field)
        if not isinstance(contract, dict) or contract.get("const") != value:
            raise StageFailure("BINDING_SCHEMA_CONST_MISMATCH")
    if fixture.get("authorization_status") != "NOT_AUTHORIZED":
        raise StageFailure("BINDING_AUTHORIZATION_STATUS_INVALID")
    if fixture.get("authority_effect") is not False:
        raise StageFailure("BINDING_AUTHORITY_EFFECT_INVALID")


def load_request(path: Path) -> dict[str, Any]:
    value = _load_json(path, "RUN_REQUEST_READ_FAILED")
    if not isinstance(value, dict):
        raise StageFailure("RUN_REQUEST_NOT_OBJECT")
    return value


def verify_phase_a_components(expected: dict[str, str]) -> None:
    if set(expected) != set(PHASE_A_COMPONENTS):
        raise StageFailure("PHASE_A_COMPONENT_SET_MISMATCH")
    for name, path in PHASE_A_COMPONENTS.items():
        value = expected.get(name)
        if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{64}", value):
            raise StageFailure("PHASE_A_COMPONENT_HASH_INVALID")
        if not path.is_file() or sha256_file(path) != value:
            raise StageFailure("PHASE_A_COMPONENT_HASH_MISMATCH")


def validate_request(
    request: dict[str, Any],
    expected_python: str,
    source_commit: str,
    *,
    git_runner: Callable[..., subprocess.CompletedProcess[str]] = subprocess.run,
) -> str:
    if request.get("$schema") != "./ce-g11b-run-request.schema.v0.1.json":
        raise StageFailure("RUN_REQUEST_SCHEMA_REFERENCE_MISMATCH")
    if request.get("request_id") != EXPECTED_REQUEST_ID:
        raise StageFailure("RUN_REQUEST_ID_MISMATCH")
    if request.get("version") != "0.1.0":
        raise StageFailure("RUN_REQUEST_VERSION_MISMATCH")
    if request.get("status") != "AUTHORIZED_SINGLE_TRIGGER":
        raise StageFailure("RUN_REQUEST_STATUS_MISMATCH")
    if request.get("decision_reference") != COMPONENT_DECISION:
        raise StageFailure("RUN_REQUEST_DECISION_MISMATCH")
    if request.get("trigger_decision_reference") != TRIGGER_DECISION:
        raise StageFailure("RUN_REQUEST_TRIGGER_DECISION_MISMATCH")
    created_at = request.get("created_at")
    if not isinstance(created_at, str) or not re.fullmatch(
        r"[0-9]{4}-[0-9]{2}-[0-9]{2}T"
        r"[0-9]{2}:[0-9]{2}:[0-9]{2}Z",
        created_at,
    ):
        raise StageFailure("RUN_REQUEST_CREATED_AT_INVALID")
    if request.get("source_branch") != EXPECTED_BRANCH:
        raise StageFailure("RUN_REQUEST_BRANCH_MISMATCH")
    phase_a_commit = request.get("phase_a_commit")
    if not isinstance(phase_a_commit, str) or not re.fullmatch(
        r"[0-9a-f]{40}", phase_a_commit
    ):
        raise StageFailure("PHASE_A_COMMIT_INVALID")
    if not re.fullmatch(r"[0-9a-f]{40}", source_commit):
        raise StageFailure("SOURCE_COMMIT_INVALID")
    ancestry = git_runner(
        ["git", "merge-base", "--is-ancestor", phase_a_commit, source_commit],
        cwd=ROOT.parents[1],
        capture_output=True,
        text=True,
        check=False,
        timeout=10,
    )
    if ancestry.returncode != 0:
        raise StageFailure("PHASE_A_COMMIT_NOT_ANCESTOR")
    if request.get("trigger") != {
        "event": "push",
        "branch": EXPECTED_BRANCH,
        "path": EXPECTED_TRIGGER_PATH,
        "events_cap": 1,
    }:
        raise StageFailure("RUN_REQUEST_TRIGGER_MISMATCH")
    if request.get("python_matrix") != list(EXPECTED_PYTHON_VERSIONS):
        raise StageFailure("RUN_REQUEST_MATRIX_MISMATCH")
    if expected_python not in request["python_matrix"]:
        raise StageFailure("RUN_REQUEST_PYTHON_BINDING_MISMATCH")
    if request.get("frozen_inputs") != FROZEN_INPUTS:
        raise StageFailure("RUN_REQUEST_FROZEN_INPUT_MISMATCH")
    components = request.get("phase_a_components")
    if not isinstance(components, dict):
        raise StageFailure("PHASE_A_COMPONENTS_NOT_OBJECT")
    verify_phase_a_components(components)
    if request.get("actions") != EXPECTED_ACTIONS:
        raise StageFailure("RUN_REQUEST_ACTIONS_MISMATCH")
    if request.get("caps") != EXPECTED_CAPS:
        raise StageFailure("RUN_REQUEST_CAPS_MISMATCH")
    if request.get("retry") is not False:
        raise StageFailure("RUN_REQUEST_RETRY_NOT_FALSE")
    if request.get("fallback") is not False:
        raise StageFailure("RUN_REQUEST_FALLBACK_NOT_FALSE")
    if (
        request.get("result_schema_reference")
        != "./ce-g11b-cross-version-result.schema.v0.1.json"
    ):
        raise StageFailure("RUN_REQUEST_RESULT_SCHEMA_MISMATCH")
    return phase_a_commit


def safe_environment_value(name: str) -> str:
    value = os.environ.get(name, "")
    allowed = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz"
        "0123456789._-"
    )
    if not value or len(value) > 64 or any(char not in allowed for char in value):
        return "UNAVAILABLE"
    return value


def observed_test_count(output: str) -> int:
    for line in output.splitlines():
        parts = line.strip().split()
        if (
            len(parts) >= 3
            and parts[0] == "Ran"
            and parts[1].isdigit()
            and parts[2] in {"test", "tests"}
        ):
            return int(parts[1])
    return 0


def base_receipt(
    expected_python: str,
    source_commit: str,
    runner_label: str,
    observed_python: str,
) -> dict[str, Any]:
    return {
        "receipt_id": f"TITMAS-CE-G11B-PYTHON-{expected_python}",
        "version": "0.1.0",
        "decision_reference": COMPONENT_DECISION,
        "trigger_decision_reference": TRIGGER_DECISION,
        "run_request_id": EXPECTED_REQUEST_ID,
        "status": "FAIL_CLOSED",
        "source_commit": source_commit,
        "frozen_source_commit": FROZEN_SOURCE_COMMIT,
        "python": {
            "expected": expected_python,
            "observed": observed_python,
            "implementation": platform.python_implementation(),
        },
        "runner": {
            "label_expected": runner_label,
            "os": safe_environment_value("RUNNER_OS"),
            "architecture": safe_environment_value("RUNNER_ARCH"),
            "image_os": safe_environment_value("ImageOS"),
            "image_version": safe_environment_value("ImageVersion"),
        },
        "checks": {
            "exact_python_version_match": False,
            "run_request_contract_match": False,
            "phase_a_commit_is_ancestor": False,
            "phase_a_component_hashes_match": False,
            "frozen_input_hashes_match": False,
            "binding_contract_exact_match": False,
            "fixture_literal_ip_absent": False,
            "new_adapter_test_count": 0,
            "new_adapter_test_count_expected": EXPECTED_NEW_TEST_COUNT,
            "new_adapter_suite_pass": False,
            "historical_test_count": 0,
            "historical_test_count_expected": EXPECTED_HISTORICAL_TEST_COUNT,
            "historical_suite_pass": False,
            "total_test_count": 0,
            "total_test_count_expected": EXPECTED_TOTAL_TEST_COUNT,
        },
        "execution_caps": {
            "target_public_site_requests": 0,
            "trigger_events": 1,
            "workflow_runs": 1,
            "manual_dispatches": 0,
            "ssh_sessions": 0,
            "server_reads": 0,
            "server_writes": 0,
            "deployments": 0,
            "dbos_changes": 0,
            "saee_changes": 0,
            "live_bindings_created": 0,
            "model_requests_during_execution": 0,
            "credentials_read": 0,
        },
        "effects": {
            "authority": False,
            "permission": False,
            "live_binding": False,
            "remote_cross_version_validation": False,
            "tls_root_cause_proof": False,
            "public_entry_redeployment_admission": False,
            "redeployment": False,
            "production_readiness": False,
            "certification": False,
            "sla": False,
            "commercial_offering": False,
        },
        "error_class": None,
    }


def write_receipt(path: Path, receipt: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def _run_suite(
    module: str,
    root: Path,
    environment: dict[str, str],
    test_runner: Callable[..., subprocess.CompletedProcess[str]],
) -> tuple[int, subprocess.CompletedProcess[str]]:
    result = test_runner(
        [sys.executable, "-m", "unittest", "-v", module],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
        env=environment,
    )
    return observed_test_count(f"{result.stdout}\n{result.stderr}"), result


def execute(
    request_path: Path,
    expected_python: str,
    source_commit: str,
    runner_label: str,
    output: Path,
    *,
    root: Path = ROOT,
    version_reader: Callable[[], str] = platform.python_version,
    git_runner: Callable[..., subprocess.CompletedProcess[str]] = subprocess.run,
    test_runner: Callable[..., subprocess.CompletedProcess[str]] = subprocess.run,
) -> int:
    observed_python = version_reader()
    receipt = base_receipt(
        expected_python,
        source_commit,
        runner_label,
        observed_python,
    )
    try:
        request = load_request(request_path)
        validate_request(
            request,
            expected_python,
            source_commit,
            git_runner=git_runner,
        )
        receipt["checks"]["run_request_contract_match"] = True
        receipt["checks"]["phase_a_commit_is_ancestor"] = True
        receipt["checks"]["phase_a_component_hashes_match"] = True

        if expected_python not in EXPECTED_PYTHON_VERSIONS:
            raise StageFailure("EXPECTED_PYTHON_NOT_AUTHORIZED")
        if observed_python != expected_python:
            raise StageFailure("PYTHON_VERSION_MISMATCH")
        receipt["checks"]["exact_python_version_match"] = True

        verify_frozen_inputs(root)
        receipt["checks"]["frozen_input_hashes_match"] = True
        verify_binding_contract(
            root / BINDING_SCHEMA.name,
            root / BINDING_FIXTURE.name,
        )
        receipt["checks"]["binding_contract_exact_match"] = True
        verify_fixture_privacy(root)
        receipt["checks"]["fixture_literal_ip_absent"] = True

        environment = {
            name: os.environ[name]
            for name in TEST_ENVIRONMENT_ALLOWLIST
            if name in os.environ
        }
        environment["PYTHONDONTWRITEBYTECODE"] = "1"

        new_count, new_result = _run_suite(
            "test_ce_g11_target_bound_correlator.py",
            root,
            environment,
            test_runner,
        )
        receipt["checks"]["new_adapter_test_count"] = new_count
        if new_result.returncode != 0:
            raise StageFailure("NEW_ADAPTER_SUITE_FAILED")
        if new_count != EXPECTED_NEW_TEST_COUNT:
            raise StageFailure("NEW_ADAPTER_TEST_COUNT_MISMATCH")
        receipt["checks"]["new_adapter_suite_pass"] = True

        historical_count, historical_result = _run_suite(
            "test_ce_g8_diagnostic.py",
            root,
            environment,
            test_runner,
        )
        receipt["checks"]["historical_test_count"] = historical_count
        if historical_result.returncode != 0:
            raise StageFailure("HISTORICAL_SUITE_FAILED")
        if historical_count != EXPECTED_HISTORICAL_TEST_COUNT:
            raise StageFailure("HISTORICAL_TEST_COUNT_MISMATCH")
        receipt["checks"]["historical_suite_pass"] = True

        total = new_count + historical_count
        receipt["checks"]["total_test_count"] = total
        if total != EXPECTED_TOTAL_TEST_COUNT:
            raise StageFailure("TOTAL_TEST_COUNT_MISMATCH")
        receipt["status"] = "PYTHON_VERSION_OFFLINE_PASS"
        exit_code = 0
    except StageFailure as error:
        receipt["error_class"] = error.stage_code
        exit_code = 1
    except BaseException as error:
        receipt["error_class"] = f"UNEXPECTED_{type(error).__name__.upper()}"
        exit_code = 1
    write_receipt(output, receipt)
    return exit_code


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--expected-python", required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--runner-label", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    return execute(
        args.request,
        args.expected_python,
        args.source_commit,
        args.runner_label,
        args.output,
    )


if __name__ == "__main__":
    raise SystemExit(main())
