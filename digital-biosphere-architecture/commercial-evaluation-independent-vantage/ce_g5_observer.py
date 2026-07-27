#!/usr/bin/env python3
"""Run one CE-G5 public-entry observation vantage.

This harness is intentionally narrow:

* it performs exactly the requests declared by the decision-bound run request;
* it has no retry, fallback, TLS bypass, mutation, deployment, or credential path;
* it always writes a sanitized receipt before returning failure.

The receipt is transport evidence. It is not availability, SLA, production,
certification, commercial adoption, or content-truth evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import http.client
import json
import os
from pathlib import Path
import platform
import re
import ssl
import subprocess
import sys
import tempfile
import time
from typing import Any
from urllib.parse import urlsplit


EXPECTED_DECISION = "TITMAS-COMMERCIAL-EVALUATION-CE-G5"
EXPECTED_ORIGIN = "https://redcrag.cn"
EXPECTED_ROUTES = [
    "/",
    "/llms.txt",
    "/agent-index.json",
    "/TITMAS-COMMERCIAL-EVALUATION-PACK-v0.2.json",
]
EXPECTED_ROUNDS = 3
MAX_TIME_SECONDS = 20
RECEIPT_PREFIX = "TITMAS-CE-G5"
RECEIPT_SCHEMA = "./ce-g5-vantage-receipt.schema.v0.1.json"
USER_AGENT_PREFIX = "TITMAS-CE-G5"
OBSERVER_DESCRIPTION = "Run one exact TITMAS CE-G5 observation vantage."
ALLOWED_CLIENTS = {
    "GITHUB_HOSTED_UBUNTU": "python-http-client",
    "GITHUB_HOSTED_MACOS": "system-curl",
}
SAFE_REFERENCE = re.compile(r"^[A-Za-z0-9._-]+$")
PROXY_ENV_KEYS = (
    "HTTP_PROXY",
    "HTTPS_PROXY",
    "ALL_PROXY",
    "http_proxy",
    "https_proxy",
    "all_proxy",
)


class ContractError(RuntimeError):
    """Raised when the decision-bound request contract is not exact."""


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ContractError(f"{path.name} must contain one JSON object")
    return value


def validate_request(
    request: dict[str, Any], vantage_id: str, client: str
) -> tuple[str, int, dict[str, dict[str, Any]]]:
    if request.get("decision_reference") != EXPECTED_DECISION:
        raise ContractError("decision_reference mismatch")
    if request.get("public_origin") != EXPECTED_ORIGIN:
        raise ContractError("public_origin mismatch")
    if request.get("rounds") != EXPECTED_ROUNDS:
        raise ContractError("rounds must equal 3")
    if request.get("routes") != EXPECTED_ROUTES:
        raise ContractError("routes must equal the four ordered CE-G5 routes")
    if request.get("requests_per_vantage") != 12:
        raise ContractError("requests_per_vantage must equal 12")
    if request.get("total_public_origin_get_cap") != 24:
        raise ContractError("total_public_origin_get_cap must equal 24")
    if request.get("retry") is not False:
        raise ContractError("retry must be false")
    if request.get("fallback") is not False:
        raise ContractError("fallback must be false")
    if request.get("tls_verification_bypass") is not False:
        raise ContractError("tls_verification_bypass must be false")
    if request.get("sequential_within_vantage") is not True:
        raise ContractError("sequential_within_vantage must be true")
    if ALLOWED_CLIENTS.get(vantage_id) != client:
        raise ContractError("vantage/client binding mismatch")

    run_id = request.get("run_id")
    if not isinstance(run_id, str) or not SAFE_REFERENCE.fullmatch(run_id):
        raise ContractError("run_id is missing or unsafe")
    gap_seconds = request.get("round_gap_seconds")
    if not isinstance(gap_seconds, int) or not 0 <= gap_seconds <= 30:
        raise ContractError("round_gap_seconds must be an integer from 0 to 30")

    baseline_ref = request.get("hash_baseline_reference")
    if not isinstance(baseline_ref, str):
        raise ContractError("hash_baseline_reference is required")
    baseline_path = Path(__file__).resolve().parent / Path(baseline_ref).name
    baseline = load_json(baseline_path)
    if baseline.get("status") != "FIXED_CURRENT_RELEASE_BASELINE":
        raise ContractError("hash baseline is not fixed")
    if baseline.get("public_origin") != EXPECTED_ORIGIN:
        raise ContractError("hash baseline origin mismatch")
    if baseline.get("active_release") != request.get("active_release_expected"):
        raise ContractError("active release baseline mismatch")

    route_values = baseline.get("routes")
    if not isinstance(route_values, list):
        raise ContractError("hash baseline routes must be an array")
    route_map: dict[str, dict[str, Any]] = {}
    for item in route_values:
        if not isinstance(item, dict) or not isinstance(item.get("path"), str):
            raise ContractError("invalid hash baseline route")
        route_map[item["path"]] = item
    if list(route_map) != EXPECTED_ROUTES:
        raise ContractError("hash baseline routes do not match the exact route order")
    for route in EXPECTED_ROUTES:
        item = route_map[route]
        if not re.fullmatch(r"[0-9a-f]{64}", str(item.get("sha256", ""))):
            raise ContractError(f"invalid SHA-256 baseline for {route}")
        if not isinstance(item.get("bytes"), int) or item["bytes"] < 1:
            raise ContractError(f"invalid byte baseline for {route}")

    return run_id, gap_seconds, route_map


def proxy_state() -> dict[str, str]:
    return {key: os.environ[key] for key in PROXY_ENV_KEYS if os.environ.get(key)}


def python_stack() -> dict[str, str]:
    return {
        "client": "python-http-client",
        "client_version": platform.python_version(),
        "tls_backend": ssl.OPENSSL_VERSION,
        "executable": sys.executable,
    }


def curl_stack() -> dict[str, str]:
    executable = "/usr/bin/curl"
    result = subprocess.run(
        [executable, "--version"],
        capture_output=True,
        text=True,
        check=True,
        timeout=5,
    )
    first_line = result.stdout.splitlines()[0].strip()
    return {
        "client": "system-curl",
        "client_version": first_line,
        "tls_backend": first_line,
        "executable": executable,
    }


def classify_exception(error: BaseException) -> str:
    if isinstance(error, ssl.SSLError):
        return "TLS_ERROR"
    if isinstance(error, TimeoutError):
        return "TIMEOUT"
    if isinstance(error, ConnectionError):
        return "CONNECTION_ERROR"
    if isinstance(error, ContractError):
        return "CONTRACT_ERROR"
    return type(error).__name__.upper()


def observe_with_python(
    route: str, user_agent: str
) -> tuple[dict[str, Any], bytes]:
    parsed = urlsplit(EXPECTED_ORIGIN)
    context = ssl.create_default_context()
    connection = http.client.HTTPSConnection(
        parsed.hostname,
        parsed.port or 443,
        timeout=MAX_TIME_SECONDS,
        context=context,
    )
    started = time.monotonic()
    try:
        connection.connect()
        if connection.sock is None:
            raise ConnectionError("TLS socket unavailable")
        remote_ip = connection.sock.getpeername()[0]
        tls_version = connection.sock.version()
        cipher_value = connection.sock.cipher()
        connection.request(
            "GET",
            route,
            headers={
                "User-Agent": user_agent,
                "Accept": "*/*",
                "Connection": "close",
            },
        )
        response = connection.getresponse()
        body = response.read()
        elapsed = time.monotonic() - started
        return (
            {
                "curl_exit_code": None,
                "http_code": response.status,
                "remote_ip": remote_ip,
                "ssl_verify_result": 0,
                "tls_version": tls_version,
                "cipher": cipher_value[0] if cipher_value else None,
                "latency_seconds": round(elapsed, 6),
            },
            body,
        )
    finally:
        connection.close()


def observe_with_curl(
    route: str, user_agent: str
) -> tuple[dict[str, Any], bytes]:
    with tempfile.TemporaryDirectory(prefix="titmas-ce-g5-") as directory:
        body_path = Path(directory) / "body"
        write_out = (
            "%{http_code}\\n%{remote_ip}\\n%{time_total}\\n"
            "%{size_download}\\n%{ssl_verify_result}\\n"
        )
        command = [
            "/usr/bin/curl",
            "--silent",
            "--show-error",
            "--proto",
            "=https",
            "--connect-timeout",
            "10",
            "--max-time",
            str(MAX_TIME_SECONDS),
            "--retry",
            "0",
            "--user-agent",
            user_agent,
            "--header",
            "Accept: */*",
            "--output",
            str(body_path),
            "--write-out",
            write_out,
            f"{EXPECTED_ORIGIN}{route}",
        ]
        started = time.monotonic()
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,
            timeout=MAX_TIME_SECONDS + 5,
        )
        elapsed = time.monotonic() - started
        body = body_path.read_bytes() if body_path.exists() else b""
        values = result.stdout.splitlines()
        metadata: dict[str, Any] = {
            "curl_exit_code": result.returncode,
            "http_code": None,
            "remote_ip": None,
            "ssl_verify_result": None,
            "tls_version": None,
            "cipher": None,
            "latency_seconds": round(elapsed, 6),
        }
        if len(values) >= 5:
            metadata.update(
                {
                    "http_code": int(values[0]) if values[0].isdigit() else None,
                    "remote_ip": values[1] or None,
                    "latency_seconds": float(values[2]),
                    "ssl_verify_result": (
                        int(values[4]) if values[4].isdigit() else None
                    ),
                }
            )
        return metadata, body


def execute(
    request_path: Path,
    vantage_id: str,
    client: str,
    output_path: Path,
) -> int:
    started_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    receipt: dict[str, Any] = {
        "$schema": RECEIPT_SCHEMA,
        "receipt_id": f"{RECEIPT_PREFIX}-{vantage_id}",
        "version": "0.1.0",
        "status": "FAIL_CLOSED_INCOMPLETE",
        "decision_reference": EXPECTED_DECISION,
        "run_id": None,
        "vantage_id": vantage_id,
        "environment": {
            "runner_os": platform.system(),
            "runner_release": platform.release(),
            "runner_machine": platform.machine(),
            "github_actions": os.environ.get("GITHUB_ACTIONS") == "true",
            "github_run_id": os.environ.get("GITHUB_RUN_ID"),
            "github_run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT"),
            "proxy_environment_present": bool(proxy_state()),
            "client_stack": None,
        },
        "execution": {
            "started_at": started_at,
            "ended_at": None,
            "rounds": EXPECTED_ROUNDS,
            "routes_per_round": len(EXPECTED_ROUTES),
            "requests_expected": EXPECTED_ROUNDS * len(EXPECTED_ROUTES),
            "requests_executed": 0,
            "retry": False,
            "fallback": False,
            "tls_verification_bypass": False,
            "sequential": True,
        },
        "records": [],
        "summary": {
            "passes": 0,
            "failures": 0,
            "all_hashes_match": False,
            "result": "FAIL_CLOSED_INCOMPLETE",
        },
        "error_class": None,
        "effects": {
            "deployment": False,
            "configuration_change": False,
            "production": False,
            "sla": False,
            "commercial_offer": False,
            "certification": False,
        },
    }

    exit_code = 1
    try:
        request = load_json(request_path)
        run_id, gap_seconds, route_map = validate_request(
            request, vantage_id, client
        )
        receipt["run_id"] = run_id
        if proxy_state():
            raise ContractError("proxy environment must be absent")

        stack = (
            python_stack()
            if client == "python-http-client"
            else curl_stack()
        )
        receipt["environment"]["client_stack"] = stack
        user_agent = f"{USER_AGENT_PREFIX}/{run_id}/{vantage_id}"

        for round_number in range(1, EXPECTED_ROUNDS + 1):
            for route in EXPECTED_ROUTES:
                observed_at = time.strftime(
                    "%Y-%m-%dT%H:%M:%SZ", time.gmtime()
                )
                record: dict[str, Any] = {
                    "round": round_number,
                    "observed_at": observed_at,
                    "route": route,
                    "result": "FAIL_CLOSED",
                    "http_code": None,
                    "remote_ip": None,
                    "ssl_verify_result": None,
                    "tls_version": None,
                    "cipher": None,
                    "latency_seconds": None,
                    "bytes": 0,
                    "sha256": None,
                    "expected_bytes": route_map[route]["bytes"],
                    "expected_sha256": route_map[route]["sha256"],
                    "error_class": None,
                }
                try:
                    if client == "python-http-client":
                        metadata, body = observe_with_python(route, user_agent)
                    else:
                        metadata, body = observe_with_curl(route, user_agent)
                    record.update(metadata)
                    record["bytes"] = len(body)
                    record["sha256"] = sha256_bytes(body) if body else None
                    curl_ok = metadata.get("curl_exit_code") in (None, 0)
                    status_ok = metadata.get("http_code") == 200
                    verify_ok = metadata.get("ssl_verify_result") == 0
                    hash_ok = record["sha256"] == record["expected_sha256"]
                    bytes_ok = record["bytes"] == record["expected_bytes"]
                    if curl_ok and status_ok and verify_ok and hash_ok and bytes_ok:
                        record["result"] = "PASS"
                        record["error_class"] = "NONE"
                    elif not curl_ok:
                        record["result"] = "TRANSPORT_ERROR"
                        record["error_class"] = (
                            f"CURL_EXIT_{metadata.get('curl_exit_code')}"
                        )
                    elif not status_ok:
                        record["result"] = "HTTP_ERROR"
                        record["error_class"] = "HTTP_NON_200"
                    elif not verify_ok:
                        record["result"] = "TLS_ERROR"
                        record["error_class"] = "TLS_VERIFY_NONZERO"
                    else:
                        record["result"] = "CONTENT_MISMATCH"
                        record["error_class"] = "HASH_OR_SIZE_MISMATCH"
                except BaseException as error:  # Preserve every failed attempt.
                    record["result"] = "TRANSPORT_ERROR"
                    record["error_class"] = classify_exception(error)
                receipt["records"].append(record)
                receipt["execution"]["requests_executed"] += 1
            if round_number < EXPECTED_ROUNDS:
                time.sleep(gap_seconds)

        passes = sum(
            item["result"] == "PASS" for item in receipt["records"]
        )
        failures = len(receipt["records"]) - passes
        all_pass = passes == 12 and failures == 0
        receipt["summary"] = {
            "passes": passes,
            "failures": failures,
            "all_hashes_match": all_pass,
            "result": (
                "VANTAGE_OBSERVATION_PASS"
                if all_pass
                else "VANTAGE_OBSERVATION_FAIL_CLOSED"
            ),
        }
        receipt["status"] = receipt["summary"]["result"]
        exit_code = 0 if all_pass else 1
    except BaseException as error:
        receipt["status"] = "FAIL_CLOSED_CONTRACT_OR_ENVIRONMENT"
        receipt["summary"]["result"] = receipt["status"]
        receipt["error_class"] = classify_exception(error)
        exit_code = 1
    finally:
        receipt["execution"]["ended_at"] = time.strftime(
            "%Y-%m-%dT%H:%M:%SZ", time.gmtime()
        )
        output_path.write_text(
            json.dumps(receipt, indent=2, sort_keys=False) + "\n",
            encoding="utf-8",
        )
    return exit_code


def main() -> int:
    parser = argparse.ArgumentParser(
        description=OBSERVER_DESCRIPTION
    )
    parser.add_argument("--request", required=True, type=Path)
    parser.add_argument("--vantage-id", required=True)
    parser.add_argument(
        "--client",
        required=True,
        choices=("python-http-client", "system-curl"),
    )
    parser.add_argument("--output", required=True, type=Path)
    arguments = parser.parse_args()
    return execute(
        arguments.request,
        arguments.vantage_id,
        arguments.client,
        arguments.output,
    )


if __name__ == "__main__":
    raise SystemExit(main())
