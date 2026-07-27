#!/usr/bin/env python3
"""CE-G11 target-bound correlation adapter candidate.

This adapter reuses the deterministic CE-G9 parsing functions without
modifying the historical CE-G8/CE-G9 correlator.  Its binding is metadata for
evidence routing only.  It does not authorize a server read, deployment,
permission, or runtime action.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import timezone
import hashlib
import hmac
import json
import os
from pathlib import Path
import re
import sys
from typing import Any, Callable


ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import ce_g8_server_log_correlator as historical


BINDING_SCHEMA_REFERENCE = (
    "./ce-g11-correlation-binding.schema.v0.1.json"
)
BINDING_ID = "TITMAS-CE-G11-CORRELATION-BINDING-OFFLINE-001"
VERSION = "0.1.0"
DECLARED_DECISION = "TITMAS-COMMERCIAL-EVALUATION-CE-G11"
RECEIPT_ID = "TITMAS-CE-G11-SERVER-CORRELATION-001"
EXPECTED_RELEASE = (
    "/srv/tmai/releases/f8107969aa1f43be8ecf43f557297a630309fe41"
)
AUTHORIZATION_STATUS = "NOT_AUTHORIZED"
CURRENT = Path("/srv/tmai/current")
EXPECTED_KEYS = {
    "$schema",
    "binding_id",
    "version",
    "declared_decision_reference",
    "receipt_id",
    "expected_current_release",
    "authorization_status",
    "authority_effect",
}
EXPECTED_BINDING = {
    "$schema": BINDING_SCHEMA_REFERENCE,
    "binding_id": BINDING_ID,
    "version": VERSION,
    "declared_decision_reference": DECLARED_DECISION,
    "receipt_id": RECEIPT_ID,
    "expected_current_release": EXPECTED_RELEASE,
    "authorization_status": AUTHORIZATION_STATUS,
    "authority_effect": False,
}
SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")


class StageFailure(RuntimeError):
    """Stable sanitized failure that never contains raw input text."""

    def __init__(self, stage_code: str):
        super().__init__(stage_code)
        self.stage_code = stage_code


def _validate_binding_shape(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != EXPECTED_KEYS:
        raise StageFailure("BINDING_SCHEMA_INVALID")
    for key, expected in EXPECTED_BINDING.items():
        if value.get(key) != expected:
            if key == "declared_decision_reference":
                raise StageFailure("BINDING_DECISION_MISMATCH")
            if key == "receipt_id":
                raise StageFailure("BINDING_RECEIPT_MISMATCH")
            if key == "expected_current_release":
                raise StageFailure("BINDING_RELEASE_MISMATCH")
            if key == "authorization_status":
                raise StageFailure("BINDING_AUTHORIZATION_STATUS_INVALID")
            if key == "authority_effect":
                raise StageFailure("BINDING_AUTHORITY_EFFECT_INVALID")
            raise StageFailure("BINDING_SCHEMA_INVALID")
    return value


def load_binding(
    binding_path: Path,
    expected_sha256: str,
) -> tuple[dict[str, Any], str]:
    """Load only an exact, hash-bound offline binding."""
    if not SHA256_PATTERN.fullmatch(expected_sha256):
        raise StageFailure("BINDING_EXPECTED_HASH_INVALID")
    try:
        raw = binding_path.read_bytes()
    except OSError:
        raise StageFailure("BINDING_READ_FAILED")
    observed_sha256 = hashlib.sha256(raw).hexdigest()
    if not hmac.compare_digest(observed_sha256, expected_sha256):
        raise StageFailure("BINDING_HASH_MISMATCH")
    try:
        value = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise StageFailure("BINDING_JSON_INVALID")
    return _validate_binding_shape(value), observed_sha256


def _historical_stage(error: BaseException, fallback: str) -> StageFailure:
    if isinstance(error, historical.StageFailure):
        return StageFailure(error.stage_code)
    return StageFailure(fallback)


def execute(
    binding_path: Path,
    expected_binding_sha256: str,
    start_text: str,
    end_text: str,
    salt: str,
    access_log: Path = historical.ACCESS_LOG,
    error_log: Path = historical.ERROR_LOG,
    journal_runner: Callable[..., Any] | None = None,
    local_tz: timezone | None = None,
    current_target_reader: Callable[[], str] | None = None,
) -> dict[str, Any]:
    """Create a sanitized correlation receipt under an offline binding."""
    binding, binding_sha256 = load_binding(
        binding_path,
        expected_binding_sha256,
    )
    try:
        start = historical.parse_iso(start_text)
        end = historical.parse_iso(end_text)
    except BaseException as error:
        raise _historical_stage(error, "WINDOW_TIMESTAMP_INVALID")
    if end < start or (end - start).total_seconds() > 60:
        raise StageFailure("WINDOW_RANGE_INVALID")
    try:
        current_target = (
            current_target_reader()
            if current_target_reader is not None
            else os.readlink(CURRENT)
        )
    except OSError:
        raise StageFailure("CURRENT_TARGET_READ_FAILED")
    if current_target != binding["expected_current_release"]:
        raise StageFailure("CURRENT_TARGET_MISMATCH")
    try:
        statuses, paths, sources = historical.access_records(
            start,
            end,
            salt,
            access_log,
        )
    except BaseException:
        raise StageFailure("ACCESS_PARSE_FAILED")
    try:
        nginx_errors = historical.error_classes(
            start,
            end,
            error_log,
            local_tz=local_tz,
        )
    except BaseException:
        raise StageFailure("ERROR_PARSE_FAILED")
    try:
        if journal_runner is None:
            journal = historical.journal_classes(start, end)
        else:
            journal = historical.journal_classes(
                start,
                end,
                runner=journal_runner,
            )
    except BaseException:
        raise StageFailure("JOURNAL_PARSE_FAILED")
    return {
        "receipt_id": binding["receipt_id"],
        "version": VERSION,
        "decision_reference": binding["declared_decision_reference"],
        "status": "EXACT_WINDOW_CORRELATION_COMPLETE",
        "binding": {
            "binding_id": binding["binding_id"],
            "sha256": binding_sha256,
            "authorization_status": binding["authorization_status"],
            "authority_effect": binding["authority_effect"],
            "binding_is_authority": False,
        },
        "window_start": start_text,
        "window_end": end_text,
        "padding_seconds": 0,
        "current_release": binding["expected_current_release"],
        "access": {
            "records": sum(statuses.values()),
            "status_classes": dict(sorted(statuses.items())),
            "path_classes": dict(sorted(paths.items())),
            "salted_source_ip_hashes": sorted(sources),
            "source_hash_salt_sha256": hashlib.sha256(
                salt.encode()
            ).hexdigest(),
        },
        "nginx_error_classes": dict(sorted(nginx_errors.items())),
        "journal_classes": dict(sorted(journal.items())),
        "ssl_or_handshake_signal_count": (
            nginx_errors["SSL_HANDSHAKE"]
            + nginx_errors["SSL_OTHER"]
            + journal["SSL_OR_HANDSHAKE"]
        ),
        "raw_logs_persisted": False,
        "server_write": False,
        "authority_effect": False,
    }


def _failure_receipt(error: BaseException) -> dict[str, Any]:
    error_class = (
        error.stage_code
        if isinstance(error, StageFailure)
        else f"UNEXPECTED_{type(error).__name__.upper()}"
    )
    return {
        "receipt_id": RECEIPT_ID,
        "version": VERSION,
        "decision_reference": DECLARED_DECISION,
        "status": "FAIL_CLOSED",
        "error_class": error_class,
        "authorization_status": AUTHORIZATION_STATUS,
        "binding_is_authority": False,
        "raw_logs_persisted": False,
        "server_write": False,
        "authority_effect": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--binding", type=Path, required=True)
    parser.add_argument("--binding-sha256", required=True)
    parser.add_argument("--window-start", required=True)
    parser.add_argument("--window-end", required=True)
    parser.add_argument("--salt", required=True)
    args = parser.parse_args()
    try:
        value = execute(
            args.binding,
            args.binding_sha256,
            args.window_start,
            args.window_end,
            args.salt,
        )
        exit_code = 0
    except BaseException as error:
        value = _failure_receipt(error)
        exit_code = 1
    print(json.dumps(value, indent=2, sort_keys=False))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
