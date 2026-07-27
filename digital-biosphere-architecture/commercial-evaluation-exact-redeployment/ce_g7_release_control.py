#!/usr/bin/env python3
"""Execute the exact CE-G7 static-release switch or rollback on the web host.

The program is intentionally decision-bound. It can only move the canonical
symlink between the two immutable releases named below. It does not build,
upload, delete a release, change Nginx configuration, or create a Runtime.

Run from the controller by streaming this reviewed source to the host:

    ssh hongyan-4cj 'python3 - switch' < ce_g7_release_control.py

The JSON emitted on stdout is a sanitized execution receipt. Any post-switch
failure causes an immediate exact rollback before the program returns failure.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
from typing import Any


DECISION = "TITMAS-COMMERCIAL-EVALUATION-CE-G7"
CURRENT = Path("/srv/tmai/current")
PROPOSED = Path(
    "/srv/tmai/releases/f8107969aa1f43be8ecf43f557297a630309fe41"
)
ROLLBACK = Path(
    "/srv/tmai/releases/7da4bcf16eeec7de1c61031fe08fc04081cf8705"
)
ARCHIVE = Path(
    "/tmp/titmas-site-f8107969aa1f43be8ecf43f557297a630309fe41.tar.gz"
)
ARCHIVE_BYTES = 962612
ARCHIVE_SHA256 = (
    "fceb10bba908fee4c36bed5fcccc88c3f6ff44d1326c3e1565be17cd12ac167e"
)
ROLLBACK_ROOT_SHA256 = (
    "992ca20edcc603a087db7875c7d21ff3ce390700cd8879fedebdbd5585b303a5"
)
ORIGIN = "https://redcrag.cn"
TEMP_LINK = Path(
    "/srv/tmai/.current.ce-g7-f8107969aa1f43be8ecf43f557297a630309fe41"
)
ROUTES = [
    ("/", "index.html", 46401, "67ca2e49dbb558a6b6ff155d9e0889817a83f67a073f7a4646383862a8190929"),
    ("/en/", "en/index.html", 48045, "b7c8f1d1faef23ab104fe87fde00003e52eb4869aba8b01d0b81b34d626ff50a"),
    ("/llms.txt", "llms.txt", 28852, "1b687ce3cda5e81cee6ac2dde41131c5f5b8059be956d25a648cfc06b90c2837"),
    ("/agent-index.json", "agent-index.json", 19998, "3849b2ecff7e2fd44f361b284b3314a77fa1923bf71f9d59785a37d1cc29465d"),
    ("/status.json", "status.json", 19358, "8d7cef3c6b07916ddd3e5e40d988764a95ad9a97878584986c2c33f1cdef2b33"),
    (
        "/TITMAS-COMMERCIAL-EVALUATION-PACK-v0.2.json",
        "TITMAS-COMMERCIAL-EVALUATION-PACK-v0.2.json",
        4276,
        "54a738beef94c2e5e6b3fa28f8a8c299681e05ec5c3e82ec6901710dcfea8269",
    ),
    (
        "/TITMAS-AGENT-EVALUATION-ENTRY-v0.1.json",
        "TITMAS-AGENT-EVALUATION-ENTRY-v0.1.json",
        6036,
        "af106a96eceb9e555ef73948eff3d15c7e48b5c9657d5d1d7d7c205bf905b114",
    ),
    (
        "/TITMAS-AGENT-EVALUATION-ENTRY-VALIDATION-REPORT-v0.1.md",
        "TITMAS-AGENT-EVALUATION-ENTRY-VALIDATION-REPORT-v0.1.md",
        3087,
        "5b472f3db7b9a27e61ab31ad6cc2e490af5749d37abfd668b549e6e57c5f2cf4",
    ),
    (
        "/architecture/titmas-agent-evaluation-entry-contract-v0.1.md",
        "architecture/titmas-agent-evaluation-entry-contract-v0.1.md",
        8053,
        "6b2cae58f15ba69a459e4273c6cc69f1aed302904b134dcd5fc7c4aa2cd31fa5",
    ),
    (
        "/architecture/schemas/titmas-agent-evaluation-entry.schema.v0.1.json",
        "architecture/schemas/titmas-agent-evaluation-entry.schema.v0.1.json",
        12819,
        "a49b8d25b2d1c0a79a37fb6449408df3ddbd97b952bff2f7917f913627e55f1c",
    ),
    (
        "/release-manifest.json",
        "release-manifest.json",
        10678,
        "578d3aa556efe3a647cb44fe40dad74d675dac11e92c87b38c298be97969fc2b",
    ),
]
REQUIRED_HEADERS = {
    "strict-transport-security",
    "content-security-policy",
    "x-content-type-options",
    "x-frame-options",
    "referrer-policy",
    "permissions-policy",
}


class GateFailure(RuntimeError):
    """Fail-closed CE-G7 gate failure."""


def now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def exact_target(link: Path) -> str:
    if not link.is_symlink():
        raise GateFailure(f"{link} is not a symlink")
    return os.readlink(link)


def validate_file(
    release: Path, relative: str, expected_bytes: int, expected_sha256: str
) -> None:
    path = release / relative
    if not path.is_file() or path.is_symlink():
        raise GateFailure(f"release file missing or unsafe: {relative}")
    if path.stat().st_size != expected_bytes:
        raise GateFailure(f"release byte mismatch: {relative}")
    if sha256_file(path) != expected_sha256:
        raise GateFailure(f"release hash mismatch: {relative}")


def validate_preconditions() -> dict[str, Any]:
    if exact_target(CURRENT) != str(ROLLBACK):
        raise GateFailure("current symlink is not the exact rollback target")
    if not PROPOSED.is_dir() or PROPOSED.is_symlink():
        raise GateFailure("proposed immutable release is missing or unsafe")
    if not ROLLBACK.is_dir() or ROLLBACK.is_symlink():
        raise GateFailure("rollback immutable release is missing or unsafe")
    if not ARCHIVE.is_file() or ARCHIVE.is_symlink():
        raise GateFailure("archive is missing or unsafe")
    if ARCHIVE.stat().st_size != ARCHIVE_BYTES:
        raise GateFailure("archive byte count mismatch")
    if sha256_file(ARCHIVE) != ARCHIVE_SHA256:
        raise GateFailure("archive SHA-256 mismatch")
    for _, relative, size, digest in ROUTES:
        validate_file(PROPOSED, relative, size, digest)
    run_checked(["nginx", "-t"], "nginx pre-switch test")
    return {
        "current_target": str(ROLLBACK),
        "proposed_release_exists": True,
        "rollback_release_exists": True,
        "archive_bytes": ARCHIVE_BYTES,
        "archive_sha256": ARCHIVE_SHA256,
        "routes_verified": len(ROUTES),
        "nginx_test_pass": True,
    }


def run_checked(command: list[str], label: str) -> None:
    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        timeout=30,
    )
    if result.returncode != 0:
        raise GateFailure(f"{label} failed with exit {result.returncode}")


def atomic_switch(link: Path, expected: Path, target: Path, temp_link: Path) -> None:
    if exact_target(link) != str(expected):
        raise GateFailure("atomic switch expected-current mismatch")
    if temp_link.exists() or temp_link.is_symlink():
        raise GateFailure("decision-bound temporary symlink already exists")
    os.symlink(str(target), temp_link)
    try:
        os.replace(temp_link, link)
    except BaseException:
        if temp_link.is_symlink():
            temp_link.unlink()
        raise
    if exact_target(link) != str(target):
        raise GateFailure("atomic switch target verification failed")


def parse_headers(path: Path) -> dict[str, str]:
    headers: dict[str, str] = {}
    for line in path.read_text(encoding="iso-8859-1").splitlines():
        if ":" not in line:
            continue
        name, value = line.split(":", 1)
        headers[name.strip().lower()] = value.strip()
    return headers


def local_tls_observation(
    route: str, expected_bytes: int, expected_sha256: str
) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="titmas-ce-g7-") as directory:
        body = Path(directory) / "body"
        headers = Path(directory) / "headers"
        command = [
            "/usr/bin/curl",
            "--silent",
            "--show-error",
            "--proto",
            "=https",
            "--connect-timeout",
            "10",
            "--max-time",
            "20",
            "--retry",
            "0",
            "--resolve",
            "redcrag.cn:443:127.0.0.1",
            "--dump-header",
            str(headers),
            "--output",
            str(body),
            f"{ORIGIN}{route}",
        ]
        started = time.monotonic()
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=25,
        )
        elapsed = round(time.monotonic() - started, 6)
        payload = body.read_bytes() if body.exists() else b""
        header_map = parse_headers(headers) if headers.exists() else {}
        status_line = (
            headers.read_text(encoding="iso-8859-1").splitlines()[0]
            if headers.exists() and headers.stat().st_size
            else ""
        )
        status_ok = " 200 " in status_line
        digest = sha256_bytes(payload) if payload else None
        passed = (
            result.returncode == 0
            and status_ok
            and len(payload) == expected_bytes
            and digest == expected_sha256
        )
        return {
            "route": route,
            "result": "PASS" if passed else "FAIL_CLOSED",
            "curl_exit_code": result.returncode,
            "http_200": status_ok,
            "latency_seconds": elapsed,
            "bytes": len(payload),
            "sha256": digest,
            "expected_bytes": expected_bytes,
            "expected_sha256": expected_sha256,
            "headers": header_map,
        }


def validate_local_release() -> tuple[list[dict[str, Any]], list[str]]:
    records = [
        local_tls_observation(route, size, digest)
        for route, _, size, digest in ROUTES
    ]
    failures = [item["route"] for item in records if item["result"] != "PASS"]
    root_headers = records[0]["headers"]
    missing_headers = sorted(REQUIRED_HEADERS - set(root_headers))
    if failures:
        raise GateFailure(f"server-local route gate failed: {failures}")
    if missing_headers:
        raise GateFailure(f"server-local security headers missing: {missing_headers}")
    sanitized = [
        {key: value for key, value in item.items() if key != "headers"}
        for item in records
    ]
    return sanitized, sorted(REQUIRED_HEADERS)


def rollback_release() -> dict[str, Any]:
    current_before = exact_target(CURRENT)
    if current_before == str(ROLLBACK):
        switched = False
    elif current_before == str(PROPOSED):
        atomic_switch(CURRENT, PROPOSED, ROLLBACK, TEMP_LINK)
        switched = True
    else:
        raise GateFailure("rollback refused an unknown current target")
    run_checked(["nginx", "-t"], "nginx rollback test")
    run_checked(["systemctl", "reload", "nginx"], "nginx rollback reload")
    if exact_target(CURRENT) != str(ROLLBACK):
        raise GateFailure("rollback target verification failed")
    root = local_tls_observation("/", 46401, ROLLBACK_ROOT_SHA256)
    if root["result"] != "PASS":
        raise GateFailure("rollback root verification failed")
    return {
        "status": "PASS",
        "switched": switched,
        "target": str(ROLLBACK),
        "current_after": exact_target(CURRENT),
        "nginx_test_pass": True,
        "nginx_reload_pass": True,
        "root_verification": {
            key: value for key, value in root.items() if key != "headers"
        },
    }


def execute_switch() -> tuple[dict[str, Any], int]:
    receipt: dict[str, Any] = {
        "receipt_id": "TITMAS-CE-G7-SERVER-SWITCH-001",
        "decision_reference": DECISION,
        "status": "FAIL_CLOSED_INCOMPLETE",
        "started_at": now(),
        "ended_at": None,
        "preconditions": None,
        "switch": {
            "from": str(ROLLBACK),
            "to": str(PROPOSED),
            "atomic": False,
            "nginx_test_pass": False,
            "nginx_reload_pass": False,
        },
        "server_local_observation": {
            "requests_executed": 0,
            "records": [],
            "security_headers_passed": [],
        },
        "rollback": None,
        "error_class": None,
        "effects": {
            "runtime": False,
            "api": False,
            "agent": False,
            "entity": False,
            "permission": False,
            "capability": False,
            "certification": False,
            "sla": False,
            "commercial_offering": False,
            "production_readiness": False,
        },
    }
    exit_code = 1
    switched = False
    try:
        receipt["preconditions"] = validate_preconditions()
        atomic_switch(CURRENT, ROLLBACK, PROPOSED, TEMP_LINK)
        switched = True
        receipt["switch"]["atomic"] = True
        run_checked(["nginx", "-t"], "nginx post-switch test")
        receipt["switch"]["nginx_test_pass"] = True
        run_checked(["systemctl", "reload", "nginx"], "nginx post-switch reload")
        receipt["switch"]["nginx_reload_pass"] = True
        records, headers = validate_local_release()
        receipt["server_local_observation"] = {
            "requests_executed": len(records),
            "records": records,
            "security_headers_passed": headers,
        }
        receipt["status"] = "SWITCH_AND_SERVER_LOCAL_GATE_PASS"
        exit_code = 0
    except BaseException as error:
        receipt["status"] = "FAIL_CLOSED_ROLLBACK_REQUIRED"
        receipt["error_class"] = type(error).__name__
        if switched:
            try:
                receipt["rollback"] = rollback_release()
                receipt["status"] = "FAIL_CLOSED_ROLLBACK_PASS"
            except BaseException as rollback_error:
                receipt["rollback"] = {
                    "status": "FAIL",
                    "error_class": type(rollback_error).__name__,
                }
                receipt["status"] = "FAIL_CLOSED_ROLLBACK_FAIL"
    finally:
        receipt["ended_at"] = now()
    return receipt, exit_code


def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] not in {"switch", "rollback"}:
        print("usage: ce_g7_release_control.py switch|rollback", file=sys.stderr)
        return 2
    if sys.argv[1] == "switch":
        receipt, exit_code = execute_switch()
    else:
        receipt = {
            "receipt_id": "TITMAS-CE-G7-ROLLBACK-001",
            "decision_reference": DECISION,
            "observed_at": now(),
        }
        try:
            receipt["rollback"] = rollback_release()
            receipt["status"] = "ROLLBACK_PASS"
            exit_code = 0
        except BaseException as error:
            receipt["status"] = "ROLLBACK_FAIL"
            receipt["error_class"] = type(error).__name__
            exit_code = 1
    print(json.dumps(receipt, indent=2, sort_keys=False))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
