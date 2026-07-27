#!/usr/bin/env python3
"""Correlate CE-G8 server logs within the exact observation window.

The script prints only sanitized counts, classes, and salted source-IP hashes.
It does not print or persist raw log lines and does not mutate the server.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import ipaddress
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from typing import Any


DECISION = "TITMAS-COMMERCIAL-EVALUATION-CE-G8"
ROLLBACK = (
    "/srv/tmai/releases/7da4bcf16eeec7de1c61031fe08fc04081cf8705"
)
CURRENT = Path("/srv/tmai/current")
ACCESS_LOG = Path("/var/log/nginx/access.log")
ERROR_LOG = Path("/var/log/nginx/error.log")


class CorrelationFailure(RuntimeError):
    """Fail-closed log-correlation error."""


def parse_iso(value: str) -> datetime:
    parsed = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(
        tzinfo=timezone.utc
    )
    return parsed


def salted_ip(value: str, salt: str) -> str:
    ipaddress.ip_address(value)
    return hashlib.sha256(f"{salt}:{value}".encode()).hexdigest()


def access_records(
    start: datetime, end: datetime, salt: str
) -> tuple[Counter[str], Counter[str], set[str]]:
    status_counts: Counter[str] = Counter()
    path_counts: Counter[str] = Counter()
    source_hashes: set[str] = set()
    pattern = re.compile(
        r'^(\S+).*\\[([^\\]]+)\\]\\s+"\\S+\\s+([^\\s]+)\\s+[^"]+"\\s+(\\d{3})\\s'
    )
    if not ACCESS_LOG.is_file():
        return status_counts, path_counts, source_hashes
    with ACCESS_LOG.open("r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            match = pattern.search(line)
            if not match:
                continue
            try:
                observed = datetime.strptime(
                    match.group(2), "%d/%b/%Y:%H:%M:%S %z"
                ).astimezone(timezone.utc)
            except ValueError:
                continue
            if not start <= observed <= end:
                continue
            source, path, status = (
                match.group(1),
                match.group(3),
                match.group(4),
            )
            try:
                source_hashes.add(salted_ip(source, salt))
            except ValueError:
                pass
            status_counts[f"HTTP_{status[0]}XX"] += 1
            path_counts["TARGET_EN" if path == "/en/" else "OTHER"] += 1
    return status_counts, path_counts, source_hashes


def error_classes(start: datetime, end: datetime) -> Counter[str]:
    counts: Counter[str] = Counter()
    if not ERROR_LOG.is_file():
        return counts
    local_tz = datetime.now().astimezone().tzinfo
    pattern = re.compile(r"^(\\d{4}/\\d{2}/\\d{2} \\d{2}:\\d{2}:\\d{2})")
    with ERROR_LOG.open("r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            match = pattern.match(line)
            if not match:
                continue
            try:
                observed = datetime.strptime(
                    match.group(1), "%Y/%m/%d %H:%M:%S"
                ).replace(tzinfo=local_tz).astimezone(timezone.utc)
            except ValueError:
                continue
            if not start <= observed <= end:
                continue
            lowered = line.lower()
            if "ssl_do_handshake" in lowered or "handshake" in lowered:
                counts["SSL_HANDSHAKE"] += 1
            elif "ssl" in lowered:
                counts["SSL_OTHER"] += 1
            elif "upstream" in lowered:
                counts["UPSTREAM"] += 1
            else:
                counts["OTHER_NGINX_ERROR"] += 1
    return counts


def journal_classes(start_text: str, end_text: str) -> Counter[str]:
    counts: Counter[str] = Counter()
    result = subprocess.run(
        [
            "journalctl",
            "-u",
            "nginx",
            "--since",
            start_text,
            "--until",
            end_text,
            "--output=json",
            "--no-pager",
        ],
        capture_output=True,
        text=True,
        check=False,
        timeout=20,
    )
    if result.returncode not in (0, 1):
        raise CorrelationFailure("journalctl failed")
    for line in result.stdout.splitlines():
        try:
            message = str(json.loads(line).get("MESSAGE", "")).lower()
        except json.JSONDecodeError:
            continue
        if "ssl" in message or "handshake" in message:
            counts["SSL_OR_HANDSHAKE"] += 1
        elif "error" in message or "fail" in message:
            counts["OTHER_ERROR"] += 1
        elif message:
            counts["OTHER"] += 1
    return counts


def execute(start_text: str, end_text: str, salt: str) -> dict[str, Any]:
    start = parse_iso(start_text)
    end = parse_iso(end_text)
    if end < start or (end - start).total_seconds() > 60:
        raise CorrelationFailure("window is invalid or exceeds 60 seconds")
    if not CURRENT.is_symlink() or os.readlink(CURRENT) != ROLLBACK:
        raise CorrelationFailure("current release is not the exact rollback target")
    statuses, paths, sources = access_records(start, end, salt)
    nginx_errors = error_classes(start, end)
    journal = journal_classes(start_text, end_text)
    return {
        "receipt_id": "TITMAS-CE-G8-SERVER-CORRELATION-001",
        "version": "0.1.0",
        "decision_reference": DECISION,
        "status": "EXACT_WINDOW_CORRELATION_COMPLETE",
        "window_start": start_text,
        "window_end": end_text,
        "padding_seconds": 0,
        "current_release": ROLLBACK,
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
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--window-start", required=True)
    parser.add_argument("--window-end", required=True)
    parser.add_argument("--salt", required=True)
    args = parser.parse_args()
    try:
        value = execute(args.window_start, args.window_end, args.salt)
        exit_code = 0
    except BaseException as error:
        value = {
            "receipt_id": "TITMAS-CE-G8-SERVER-CORRELATION-001",
            "decision_reference": DECISION,
            "status": "FAIL_CLOSED",
            "error_class": type(error).__name__,
            "raw_logs_persisted": False,
            "server_write": False,
        }
        exit_code = 1
    print(json.dumps(value, indent=2, sort_keys=False))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
