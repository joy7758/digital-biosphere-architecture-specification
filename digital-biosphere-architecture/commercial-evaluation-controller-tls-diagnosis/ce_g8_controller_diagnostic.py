#!/usr/bin/env python3
"""Run the exact four-request CE-G8 controller TLS diagnostic matrix.

The script observes the stable rollback site. It never retries, falls back,
disables TLS verification, deploys, mutates the server, or persists raw
response bodies, raw errors, proxy addresses, interface identifiers, or full
network configuration.
"""

from __future__ import annotations

import argparse
import hashlib
import http.client
import ipaddress
import json
import os
from pathlib import Path
import platform
import re
import socket
import ssl
import subprocess
import sys
import tempfile
import time
from typing import Any


DECISION = "TITMAS-COMMERCIAL-EVALUATION-CE-G8"
ORIGIN = "https://redcrag.cn"
HOST = "redcrag.cn"
DIRECT_IP = "180.76.115.193"
ROUTE = "/en/"
MAX_SECONDS = 20
PROXY_ENV_KEYS = (
    "HTTP_PROXY",
    "HTTPS_PROXY",
    "ALL_PROXY",
    "http_proxy",
    "https_proxy",
    "all_proxy",
)
MATRIX = [
    ("A", "MACOS_SYSTEM_CURL", "NORMAL", "DEFAULT"),
    ("B", "MACOS_SYSTEM_CURL", "EXPLICIT_180_76_115_193", "HTTP_1_1"),
    ("C", "PYTHON_HTTP_CLIENT_OPENSSL", "NORMAL_DNS", "HTTP_1_1"),
    (
        "D",
        "PYTHON_SOCKET_OPENSSL",
        "DIRECT_180_76_115_193_WITH_SNI",
        "HTTP_1_1",
    ),
]


class DiagnosticFailure(RuntimeError):
    """Fail-closed diagnostic contract failure."""


def utc_now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def ip_class(value: str | None) -> str:
    if not value:
        return "NONE"
    try:
        address = ipaddress.ip_address(value)
    except ValueError:
        return "INVALID"
    if address in ipaddress.ip_network("198.18.0.0/15"):
        return "SYNTHETIC_198_18_0_0_15"
    if address.is_loopback:
        return "LOOPBACK"
    if address.is_private:
        return "PRIVATE"
    if address.is_link_local:
        return "LINK_LOCAL"
    if address.version == 4:
        return "PUBLIC_IPV4"
    return "PUBLIC_IPV6"


def interface_class(name: str | None) -> str:
    if not name:
        return "UNKNOWN"
    if name.startswith(("utun", "tun", "tap")):
        return "TUNNEL"
    if name.startswith(("en", "eth", "wlan")):
        return "PHYSICAL"
    if name.startswith("lo"):
        return "LOOPBACK"
    return "OTHER"


def sanitize_error(return_code: int, text: str) -> str:
    lowered = text.lower()
    if return_code == 35 or "ssl" in lowered or "tls" in lowered:
        return "TLS_HANDSHAKE_ERROR"
    if return_code == 28 or "timed out" in lowered:
        return "TIMEOUT"
    if "could not resolve" in lowered:
        return "DNS_ERROR"
    if return_code == 0:
        return "NONE"
    return f"CURL_EXIT_{return_code}"


def scutil_proxy_summary() -> dict[str, Any]:
    result = subprocess.run(
        ["/usr/sbin/scutil", "--proxy"],
        capture_output=True,
        text=True,
        check=True,
        timeout=5,
    )
    values: dict[str, str] = {}
    for line in result.stdout.splitlines():
        match = re.match(r"\s*([A-Za-z0-9]+)\s*:\s*(.+?)\s*$", line)
        if match:
            values[match.group(1)] = match.group(2)

    def enabled(name: str) -> bool:
        return values.get(name) == "1"

    def target_class(name: str) -> str:
        target = values.get(name)
        if not target:
            return "NONE"
        return "LOOPBACK" if target in {"127.0.0.1", "::1", "localhost"} else "NON_LOOPBACK"

    return {
        "http_enabled": enabled("HTTPEnable"),
        "http_target_class": target_class("HTTPProxy"),
        "https_enabled": enabled("HTTPSEnable"),
        "https_target_class": target_class("HTTPSProxy"),
        "socks_enabled": enabled("SOCKSEnable"),
        "socks_target_class": target_class("SOCKSProxy"),
        "auto_config_enabled": enabled("ProxyAutoConfigEnable"),
    }


def route_summary() -> dict[str, str]:
    result = subprocess.run(
        ["/sbin/route", "-n", "get", DIRECT_IP],
        capture_output=True,
        text=True,
        check=True,
        timeout=5,
    )
    interface = None
    gateway = None
    for line in result.stdout.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        if key.strip() == "interface":
            interface = value.strip()
        elif key.strip() == "gateway":
            gateway = value.strip()
    return {
        "interface_class": interface_class(interface),
        "gateway_class": ip_class(gateway),
        "destination_class": ip_class(DIRECT_IP),
    }


def address_summary() -> dict[str, Any]:
    values = socket.getaddrinfo(HOST, 443, type=socket.SOCK_STREAM)
    classes: dict[str, int] = {}
    for value in values:
        category = ip_class(value[4][0])
        classes[category] = classes.get(category, 0) + 1
    return {
        "records": len(values),
        "address_classes": classes,
        "ipv4_available": any(item[0] == socket.AF_INET for item in values),
        "ipv6_available": any(item[0] == socket.AF_INET6 for item in values),
    }


def curl_stack() -> str:
    return subprocess.run(
        ["/usr/bin/curl", "--version"],
        capture_output=True,
        text=True,
        check=True,
        timeout=5,
    ).stdout.splitlines()[0]


def base_record(identifier: str, client: str, resolution: str, http: str) -> dict[str, Any]:
    return {
        "id": identifier,
        "client": client,
        "resolution": resolution,
        "http": http,
        "route": ROUTE,
        "attempts": 1,
        "started_at": utc_now(),
        "ended_at": None,
        "result": "FAIL_CLOSED",
        "error_class": "INCOMPLETE",
        "http_code": None,
        "remote_ip_class": "NONE",
        "tls_version": None,
        "cipher": None,
        "latency_seconds": None,
        "bytes": 0,
        "sha256": None,
    }


def curl_observation(
    identifier: str, resolution: str, http: str, direct: bool
) -> dict[str, Any]:
    record = base_record(identifier, "MACOS_SYSTEM_CURL", resolution, http)
    with tempfile.TemporaryDirectory(prefix="titmas-ce-g8-curl-") as directory:
        body = Path(directory) / "body"
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
            str(MAX_SECONDS),
            "--retry",
            "0",
            "--output",
            str(body),
            "--write-out",
            write_out,
        ]
        if direct:
            command.extend(
                [
                    "--http1.1",
                    "--resolve",
                    f"{HOST}:443:{DIRECT_IP}",
                ]
            )
        command.append(f"{ORIGIN}{ROUTE}")
        started = time.monotonic()
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,
            timeout=MAX_SECONDS + 5,
        )
        values = result.stdout.splitlines()
        payload = body.read_bytes() if body.exists() else b""
        record["ended_at"] = utc_now()
        record["latency_seconds"] = round(time.monotonic() - started, 6)
        record["bytes"] = len(payload)
        record["sha256"] = sha256_bytes(payload) if payload else None
        record["error_class"] = sanitize_error(result.returncode, result.stderr)
        if len(values) >= 5:
            record["http_code"] = int(values[0]) if values[0].isdigit() else None
            record["remote_ip_class"] = ip_class(values[1])
            if values[2]:
                record["latency_seconds"] = float(values[2])
        if result.returncode == 0 and record["http_code"] == 200 and payload:
            record["result"] = "PASS"
            record["error_class"] = "NONE"
        return record


def http_client_observation() -> dict[str, Any]:
    record = base_record(
        "C", "PYTHON_HTTP_CLIENT_OPENSSL", "NORMAL_DNS", "HTTP_1_1"
    )
    context = ssl.create_default_context()
    connection = http.client.HTTPSConnection(
        HOST, 443, timeout=MAX_SECONDS, context=context
    )
    started = time.monotonic()
    try:
        connection.connect()
        if connection.sock is None:
            raise ConnectionError("TLS socket unavailable")
        record["remote_ip_class"] = ip_class(connection.sock.getpeername()[0])
        record["tls_version"] = connection.sock.version()
        cipher = connection.sock.cipher()
        record["cipher"] = cipher[0] if cipher else None
        connection.request(
            "GET",
            ROUTE,
            headers={"Host": HOST, "Connection": "close", "Accept": "*/*"},
        )
        response = connection.getresponse()
        payload = response.read()
        record["http_code"] = response.status
        record["bytes"] = len(payload)
        record["sha256"] = sha256_bytes(payload) if payload else None
        if response.status == 200 and payload:
            record["result"] = "PASS"
            record["error_class"] = "NONE"
        else:
            record["error_class"] = "HTTP_OR_EMPTY_BODY"
    except ssl.SSLError:
        record["error_class"] = "TLS_HANDSHAKE_ERROR"
    except TimeoutError:
        record["error_class"] = "TIMEOUT"
    except socket.gaierror:
        record["error_class"] = "DNS_ERROR"
    except BaseException:
        record["error_class"] = "PYTHON_TRANSPORT_ERROR"
    finally:
        record["latency_seconds"] = round(time.monotonic() - started, 6)
        record["ended_at"] = utc_now()
        connection.close()
    return record


def direct_socket_observation() -> dict[str, Any]:
    record = base_record(
        "D",
        "PYTHON_SOCKET_OPENSSL",
        "DIRECT_180_76_115_193_WITH_SNI",
        "HTTP_1_1",
    )
    started = time.monotonic()
    raw = None
    tls = None
    try:
        raw = socket.create_connection((DIRECT_IP, 443), timeout=MAX_SECONDS)
        context = ssl.create_default_context()
        tls = context.wrap_socket(raw, server_hostname=HOST)
        record["remote_ip_class"] = ip_class(tls.getpeername()[0])
        record["tls_version"] = tls.version()
        cipher = tls.cipher()
        record["cipher"] = cipher[0] if cipher else None
        request = (
            f"GET {ROUTE} HTTP/1.1\r\n"
            f"Host: {HOST}\r\n"
            "Accept: */*\r\n"
            "Connection: close\r\n\r\n"
        ).encode("ascii")
        tls.sendall(request)
        chunks: list[bytes] = []
        while True:
            value = tls.recv(65536)
            if not value:
                break
            chunks.append(value)
        response = b"".join(chunks)
        headers, separator, payload = response.partition(b"\r\n\r\n")
        status_line = headers.splitlines()[0] if headers else b""
        match = re.match(rb"HTTP/\d(?:\.\d)?\s+(\d{3})", status_line)
        record["http_code"] = int(match.group(1)) if match else None
        record["bytes"] = len(payload) if separator else 0
        record["sha256"] = sha256_bytes(payload) if payload else None
        if record["http_code"] == 200 and payload:
            record["result"] = "PASS"
            record["error_class"] = "NONE"
        else:
            record["error_class"] = "HTTP_OR_EMPTY_BODY"
    except ssl.SSLError:
        record["error_class"] = "TLS_HANDSHAKE_ERROR"
    except TimeoutError:
        record["error_class"] = "TIMEOUT"
    except BaseException:
        record["error_class"] = "PYTHON_TRANSPORT_ERROR"
    finally:
        if tls is not None:
            tls.close()
        elif raw is not None:
            raw.close()
        record["latency_seconds"] = round(time.monotonic() - started, 6)
        record["ended_at"] = utc_now()
    return record


def execute(output: Path) -> int:
    receipt: dict[str, Any] = {
        "receipt_id": "TITMAS-CE-G8-CONTROLLER-001",
        "version": "0.1.0",
        "decision_reference": DECISION,
        "status": "FAIL_CLOSED_INCOMPLETE",
        "window_start": None,
        "window_end": None,
        "environment": {
            "platform": platform.platform(),
            "proxy_environment_present": any(
                os.environ.get(key) for key in PROXY_ENV_KEYS
            ),
            "system_proxy": None,
            "route": None,
            "curl_stack": None,
            "python_version": platform.python_version(),
            "python_tls_stack": ssl.OPENSSL_VERSION,
            "address_summary": None,
        },
        "matrix": [
            {"id": a, "client": b, "resolution": c, "http": d, "attempts": 1}
            for a, b, c, d in MATRIX
        ],
        "requests_expected": 4,
        "requests_executed": 0,
        "retry": False,
        "fallback": False,
        "tls_verification_bypass": False,
        "records": [],
        "summary": None,
        "error_class": None,
    }
    exit_code = 1
    try:
        if receipt["environment"]["proxy_environment_present"]:
            raise DiagnosticFailure("proxy environment variables are forbidden")
        receipt["environment"]["system_proxy"] = scutil_proxy_summary()
        receipt["environment"]["route"] = route_summary()
        receipt["environment"]["curl_stack"] = curl_stack()
        receipt["environment"]["address_summary"] = address_summary()
        receipt["window_start"] = utc_now()
        observations = [
            curl_observation("A", "NORMAL", "DEFAULT", False),
            curl_observation(
                "B", "EXPLICIT_180_76_115_193", "HTTP_1_1", True
            ),
            http_client_observation(),
            direct_socket_observation(),
        ]
        receipt["records"] = observations
        receipt["requests_executed"] = 4
        receipt["window_end"] = utc_now()
        passes = sum(item["result"] == "PASS" for item in observations)
        receipt["summary"] = {
            "passes": passes,
            "failures": 4 - passes,
            "passing_ids": [
                item["id"] for item in observations if item["result"] == "PASS"
            ],
            "failing_ids": [
                item["id"] for item in observations if item["result"] != "PASS"
            ],
            "content_hashes_for_passes": sorted(
                {
                    item["sha256"]
                    for item in observations
                    if item["result"] == "PASS" and item["sha256"]
                }
            ),
        }
        receipt["status"] = "DIAGNOSTIC_MATRIX_COMPLETE"
        exit_code = 0
    except BaseException as error:
        receipt["status"] = "FAIL_CLOSED_CONTRACT_OR_ENVIRONMENT"
        receipt["error_class"] = type(error).__name__
    output.write_text(
        json.dumps(receipt, indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )
    return exit_code


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    return execute(args.output)


if __name__ == "__main__":
    raise SystemExit(main())
