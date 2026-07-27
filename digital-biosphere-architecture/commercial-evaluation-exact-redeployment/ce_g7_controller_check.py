#!/usr/bin/env python3
"""Run the exact CE-G7 immediate controller-side public route gate.

This checker performs one request per declared route. It has no retry,
fallback, proxy, credential, TLS-bypass, deployment, or rollback path.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import tempfile
import time
from typing import Any


DECISION = "TITMAS-COMMERCIAL-EVALUATION-CE-G7"
ORIGIN = "https://redcrag.cn"
PROXY_KEYS = (
    "HTTP_PROXY",
    "HTTPS_PROXY",
    "ALL_PROXY",
    "http_proxy",
    "https_proxy",
    "all_proxy",
)


class GateFailure(RuntimeError):
    """Fail-closed controller gate failure."""


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise GateFailure("baseline must be one JSON object")
    return value


def proxy_present() -> bool:
    return any(os.environ.get(key) for key in PROXY_KEYS)


def observe(route: str, expected_bytes: int, expected_hash: str) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="titmas-ce-g7-controller-") as directory:
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
        payload = body.read_bytes() if body.exists() else b""
        header_lines = (
            headers.read_text(encoding="iso-8859-1").splitlines()
            if headers.exists()
            else []
        )
        status_ok = any(" 200 " in line for line in header_lines if line.startswith("HTTP/"))
        header_names = sorted(
            {
                line.split(":", 1)[0].strip().lower()
                for line in header_lines
                if ":" in line
            }
        )
        digest = hashlib.sha256(payload).hexdigest() if payload else None
        passed = (
            result.returncode == 0
            and status_ok
            and len(payload) == expected_bytes
            and digest == expected_hash
        )
        return {
            "route": route,
            "result": "PASS" if passed else "FAIL_CLOSED",
            "curl_exit_code": result.returncode,
            "http_200": status_ok,
            "latency_seconds": round(time.monotonic() - started, 6),
            "bytes": len(payload),
            "sha256": digest,
            "expected_bytes": expected_bytes,
            "expected_sha256": expected_hash,
            "header_names": header_names,
        }


def execute(baseline_path: Path, output_path: Path) -> int:
    receipt: dict[str, Any] = {
        "receipt_id": "TITMAS-CE-G7-CONTROLLER-IMMEDIATE-001",
        "decision_reference": DECISION,
        "status": "FAIL_CLOSED_INCOMPLETE",
        "observed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "environment": {
            "platform": platform.platform(),
            "curl": None,
            "proxy_environment_present": proxy_present(),
        },
        "requests_executed": 0,
        "records": [],
        "security_headers_passed": [],
        "error_class": None,
    }
    exit_code = 1
    try:
        if proxy_present():
            raise GateFailure("proxy environment must be absent")
        baseline = load_json(baseline_path)
        if baseline.get("decision_reference") != DECISION:
            raise GateFailure("decision reference mismatch")
        if baseline.get("status") != "FIXED_PROPOSED_RELEASE_BASELINE":
            raise GateFailure("baseline status mismatch")
        if baseline.get("public_origin") != ORIGIN:
            raise GateFailure("origin mismatch")
        curl_version = subprocess.run(
            ["/usr/bin/curl", "--version"],
            capture_output=True,
            text=True,
            check=True,
            timeout=5,
        ).stdout.splitlines()[0]
        receipt["environment"]["curl"] = curl_version
        routes = baseline.get("routes")
        if not isinstance(routes, list) or len(routes) != 11:
            raise GateFailure("exact 11-route baseline required")
        for item in routes:
            receipt["records"].append(
                observe(item["path"], item["bytes"], item["sha256"])
            )
            receipt["requests_executed"] += 1
        failed = [
            item["route"]
            for item in receipt["records"]
            if item["result"] != "PASS"
        ]
        required = set(baseline.get("required_security_headers", []))
        present = set(receipt["records"][0]["header_names"])
        passed_headers = sorted(required & present)
        receipt["security_headers_passed"] = passed_headers
        if failed:
            raise GateFailure(f"route gate failed: {failed}")
        if passed_headers != sorted(required):
            raise GateFailure("required security header gate failed")
        receipt["status"] = "CONTROLLER_IMMEDIATE_GATE_PASS"
        exit_code = 0
    except BaseException as error:
        receipt["status"] = "FAIL_CLOSED"
        receipt["error_class"] = type(error).__name__
    output_path.write_text(
        json.dumps(receipt, indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )
    return exit_code


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    arguments = parser.parse_args()
    return execute(arguments.baseline, arguments.output)


if __name__ == "__main__":
    raise SystemExit(main())
