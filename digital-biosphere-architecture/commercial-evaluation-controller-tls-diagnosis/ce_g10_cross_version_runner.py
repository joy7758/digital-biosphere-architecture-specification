#!/usr/bin/env python3
"""Run one offline CE-G10 Python-version validation job.

The runner verifies the frozen CE-G9 input hashes, checks that the requested
exact Python patch version is active, runs the unchanged 13-test suite, and
writes a sanitized receipt. It has no network, SSH, server, deployment,
credential, DBOS, or SAEE path.

The receipt proves only one offline compatibility observation. It does not
prove TLS root cause, production readiness, certification, SLA, or commercial
availability.
"""

from __future__ import annotations

import argparse
import hashlib
import ipaddress
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
from typing import Any, Callable


ROOT = Path(__file__).resolve().parent
DECISION = "TITMAS-COMMERCIAL-EVALUATION-CE-G10"
FROZEN_SOURCE_COMMIT = "5438215028bc565c24073f51c627f400ce738b0f"
EXPECTED_PYTHON_VERSIONS = (
    "3.10.20",
    "3.11.15",
    "3.12.13",
    "3.13.14",
    "3.14.6",
)
EXPECTED_TEST_COUNT = 13
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
    "ce-g9-offline-remediation-result.schema.v0.1.json":
        "e4e60d8d4715bfbd6495201e3ac00d62c167d3b112605c81606d244f575d5863",
}


class StageFailure(RuntimeError):
    """Stable fail-closed stage code without raw error text."""

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


def safe_environment_value(name: str) -> str:
    value = os.environ.get(name, "")
    if (
        not value
        or len(value) > 64
        or any(
            character
            not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._-"
            for character in value
        )
    ):
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
        "receipt_id": f"TITMAS-CE-G10-PYTHON-{expected_python}",
        "version": "0.1.0",
        "decision_reference": DECISION,
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
            "frozen_input_hashes_match": False,
            "fixture_literal_ip_absent": False,
            "ce_g9_test_count": 0,
            "ce_g9_test_count_expected": EXPECTED_TEST_COUNT,
            "ce_g9_suite_pass": False,
        },
        "execution_caps": {
            "target_public_site_requests": 0,
            "ssh_sessions": 0,
            "server_reads": 0,
            "server_writes": 0,
            "deployments": 0,
            "dbos_changes": 0,
            "saee_changes": 0,
            "credentials_read": 0,
        },
        "effects": {
            "tls_root_cause_proof": False,
            "public_entry_redeployment_admission": False,
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


def execute(
    expected_python: str,
    source_commit: str,
    runner_label: str,
    output: Path,
    *,
    root: Path = ROOT,
    version_reader: Callable[[], str] = platform.python_version,
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
        if expected_python not in EXPECTED_PYTHON_VERSIONS:
            raise StageFailure("EXPECTED_PYTHON_NOT_AUTHORIZED")
        if observed_python != expected_python:
            raise StageFailure("PYTHON_VERSION_MISMATCH")
        receipt["checks"]["exact_python_version_match"] = True

        verify_frozen_inputs(root)
        receipt["checks"]["frozen_input_hashes_match"] = True

        verify_fixture_privacy(root)
        receipt["checks"]["fixture_literal_ip_absent"] = True

        environment = {
            name: os.environ[name]
            for name in TEST_ENVIRONMENT_ALLOWLIST
            if name in os.environ
        }
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        result = test_runner(
            [
                sys.executable,
                "-m",
                "unittest",
                "-v",
                "test_ce_g8_diagnostic.py",
            ],
            cwd=root,
            capture_output=True,
            text=True,
            check=False,
            timeout=30,
            env=environment,
        )
        combined = f"{result.stdout}\n{result.stderr}"
        count = observed_test_count(combined)
        receipt["checks"]["ce_g9_test_count"] = count
        if result.returncode != 0:
            raise StageFailure("CE_G9_SUITE_FAILED")
        if count != EXPECTED_TEST_COUNT:
            raise StageFailure("CE_G9_TEST_COUNT_MISMATCH")
        receipt["checks"]["ce_g9_suite_pass"] = True
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
    parser.add_argument("--expected-python", required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--runner-label", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    return execute(
        args.expected_python,
        args.source_commit,
        args.runner_label,
        args.output,
    )


if __name__ == "__main__":
    raise SystemExit(main())
