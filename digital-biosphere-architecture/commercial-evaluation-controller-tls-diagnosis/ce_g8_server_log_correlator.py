#!/usr/bin/env python3
"""Correlate CE-G8 server logs within the exact observation window.

The script prints only sanitized counts, classes, and salted source-IP hashes.
It does not print or persist raw log lines and does not mutate the server.

CE-G9 replaced the original regex and locale-sensitive parsing with
deterministic delimiters, explicit month/timezone handling, injectable paths,
epoch journal bounds, and stable sanitized stage failures.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timedelta, timezone
import hashlib
import ipaddress
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Any, Callable


DECISION = "TITMAS-COMMERCIAL-EVALUATION-CE-G8"
ROLLBACK = (
    "/srv/tmai/releases/7da4bcf16eeec7de1c61031fe08fc04081cf8705"
)
CURRENT = Path("/srv/tmai/current")
ACCESS_LOG = Path("/var/log/nginx/access.log")
ERROR_LOG = Path("/var/log/nginx/error.log")
MONTHS = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
}


class CorrelationFailure(RuntimeError):
    """Fail-closed log-correlation error."""


class StageFailure(CorrelationFailure):
    """Stable sanitized failure that never contains raw log or error text."""

    def __init__(self, stage_code: str):
        super().__init__(stage_code)
        self.stage_code = stage_code


def parse_iso(value: str) -> datetime:
    try:
        if (
            len(value) != 20
            or value[4] != "-"
            or value[7] != "-"
            or value[10] != "T"
            or value[13] != ":"
            or value[16] != ":"
            or value[19] != "Z"
        ):
            raise ValueError
        return datetime(
            int(value[0:4]),
            int(value[5:7]),
            int(value[8:10]),
            int(value[11:13]),
            int(value[14:16]),
            int(value[17:19]),
            tzinfo=timezone.utc,
        )
    except (TypeError, ValueError):
        raise StageFailure("WINDOW_TIMESTAMP_INVALID")


def parse_access_timestamp(value: str) -> datetime:
    """Parse 27/Jul/2026:20:31:56 +0800 without locale or regex."""
    try:
        stamp, offset_text = value.rsplit(" ", 1)
        date_text, hour, minute, second = stamp.split(":")
        day, month_text, year = date_text.split("/")
        if month_text not in MONTHS:
            raise ValueError
        if (
            len(offset_text) != 5
            or offset_text[0] not in "+-"
            or not offset_text[1:].isdigit()
        ):
            raise ValueError
        sign = 1 if offset_text[0] == "+" else -1
        offset = timedelta(
            hours=sign * int(offset_text[1:3]),
            minutes=sign * int(offset_text[3:5]),
        )
        return datetime(
            int(year),
            MONTHS[month_text],
            int(day),
            int(hour),
            int(minute),
            int(second),
            tzinfo=timezone(offset),
        ).astimezone(timezone.utc)
    except (TypeError, ValueError):
        raise StageFailure("ACCESS_TIMESTAMP_INVALID")


def parse_error_timestamp(value: str, local_tz: timezone) -> datetime:
    """Parse 2026/07/27 20:31:56 without locale or regex."""
    try:
        date_text, time_text = value.split(" ", 1)
        year, month, day = (int(item) for item in date_text.split("/"))
        hour, minute, second = (int(item) for item in time_text.split(":"))
        return datetime(
            year,
            month,
            day,
            hour,
            minute,
            second,
            tzinfo=local_tz,
        ).astimezone(timezone.utc)
    except (TypeError, ValueError):
        raise StageFailure("ERROR_TIMESTAMP_INVALID")


def salted_ip(value: str, salt: str) -> str:
    ipaddress.ip_address(value)
    return hashlib.sha256(f"{salt}:{value}".encode()).hexdigest()


def parse_access_line(line: str) -> tuple[str, datetime, str, str] | None:
    """Return source, timestamp, path, status using fixed delimiters."""
    try:
        source = line.split(None, 1)[0]
        bracket_open = line.index("[")
        bracket_close = line.index("]", bracket_open + 1)
        observed = parse_access_timestamp(
            line[bracket_open + 1 : bracket_close]
        )
        quote_open = line.index('"', bracket_close + 1)
        quote_close = line.index('"', quote_open + 1)
        request_parts = line[quote_open + 1 : quote_close].split()
        if len(request_parts) < 2:
            return None
        after = line[quote_close + 1 :].split()
        if not after or len(after[0]) != 3 or not after[0].isdigit():
            return None
        return source, observed, request_parts[1], after[0]
    except (IndexError, ValueError, StageFailure):
        return None


def access_records(
    start: datetime,
    end: datetime,
    salt: str,
    access_log: Path = ACCESS_LOG,
) -> tuple[Counter[str], Counter[str], set[str]]:
    status_counts: Counter[str] = Counter()
    path_counts: Counter[str] = Counter()
    source_hashes: set[str] = set()
    if not access_log.is_file():
        return status_counts, path_counts, source_hashes
    with access_log.open("r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            parsed = parse_access_line(line)
            if parsed is None:
                continue
            source, observed, path, status = parsed
            if not start <= observed <= end:
                continue
            try:
                source_hashes.add(salted_ip(source, salt))
            except ValueError:
                pass
            status_counts[f"HTTP_{status[0]}XX"] += 1
            path_counts["TARGET_EN" if path == "/en/" else "OTHER"] += 1
    return status_counts, path_counts, source_hashes


def error_classes(
    start: datetime,
    end: datetime,
    error_log: Path = ERROR_LOG,
    local_tz: timezone | None = None,
) -> Counter[str]:
    counts: Counter[str] = Counter()
    if not error_log.is_file():
        return counts
    effective_tz = local_tz or datetime.now().astimezone().tzinfo
    if effective_tz is None:
        raise StageFailure("ERROR_TIMEZONE_UNAVAILABLE")
    with error_log.open("r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            if len(line) < 19:
                continue
            try:
                observed = parse_error_timestamp(line[:19], effective_tz)
            except StageFailure:
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


def journal_classes(
    start: datetime,
    end: datetime,
    runner: Callable[..., subprocess.CompletedProcess[str]] = subprocess.run,
) -> Counter[str]:
    counts: Counter[str] = Counter()
    result = runner(
        [
            "journalctl",
            "-u",
            "nginx",
            "--since",
            f"@{int(start.timestamp())}",
            "--until",
            f"@{int(end.timestamp())}",
            "--output=json",
            "--no-pager",
        ],
        capture_output=True,
        text=True,
        check=False,
        timeout=20,
    )
    if result.returncode != 0:
        raise StageFailure("JOURNAL_COMMAND_FAILED")
    for line in result.stdout.splitlines():
        try:
            message = str(json.loads(line).get("MESSAGE", "")).lower()
        except json.JSONDecodeError:
            counts["MALFORMED_JSON"] += 1
            continue
        if "ssl" in message or "handshake" in message:
            counts["SSL_OR_HANDSHAKE"] += 1
        elif "error" in message or "fail" in message:
            counts["OTHER_ERROR"] += 1
        elif message:
            counts["OTHER"] += 1
    return counts


def execute(
    start_text: str,
    end_text: str,
    salt: str,
    access_log: Path = ACCESS_LOG,
    error_log: Path = ERROR_LOG,
    journal_runner: Callable[..., subprocess.CompletedProcess[str]] = subprocess.run,
    local_tz: timezone | None = None,
    current_target_reader: Callable[[], str] | None = None,
) -> dict[str, Any]:
    start = parse_iso(start_text)
    end = parse_iso(end_text)
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
    if current_target != ROLLBACK:
        raise StageFailure("CURRENT_TARGET_MISMATCH")
    try:
        statuses, paths, sources = access_records(
            start, end, salt, access_log
        )
    except BaseException:
        raise StageFailure("ACCESS_PARSE_FAILED")
    try:
        nginx_errors = error_classes(
            start, end, error_log, local_tz=local_tz
        )
    except BaseException:
        raise StageFailure("ERROR_PARSE_FAILED")
    try:
        journal = journal_classes(start, end, runner=journal_runner)
    except BaseException:
        raise StageFailure("JOURNAL_PARSE_FAILED")
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
        error_class = (
            error.stage_code
            if isinstance(error, StageFailure)
            else f"UNEXPECTED_{type(error).__name__.upper()}"
        )
        value = {
            "receipt_id": "TITMAS-CE-G8-SERVER-CORRELATION-001",
            "decision_reference": DECISION,
            "status": "FAIL_CLOSED",
            "error_class": error_class,
            "raw_logs_persisted": False,
            "server_write": False,
        }
        exit_code = 1
    print(json.dumps(value, indent=2, sort_keys=False))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
