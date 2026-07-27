#!/usr/bin/env python3
"""Read-only CE-G6 validator for one preserved static release.

The script reads one symlink, one proposed release directory, and one tar.gz
archive. It does not extract, write, deploy, reload, retry, or make network
requests. Output is a sanitized JSON receipt on stdout.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
import tarfile
import time
from typing import Any


DECISION_REFERENCE = "TITMAS-COMMERCIAL-EVALUATION-CE-G6"
CURRENT_LINK = Path("/srv/tmai/current")
EXPECTED_CURRENT = Path(
    "/srv/tmai/releases/7da4bcf16eeec7de1c61031fe08fc04081cf8705"
)
PROPOSED_SOURCE = "f8107969aa1f43be8ecf43f557297a630309fe41"
PROPOSED_RELEASE = Path(f"/srv/tmai/releases/{PROPOSED_SOURCE}")
ARCHIVE = Path(f"/tmp/titmas-site-{PROPOSED_SOURCE}.tar.gz")
EXPECTED_ARCHIVE_BYTES = 962612
EXPECTED_ARCHIVE_SHA256 = (
    "fceb10bba908fee4c36bed5fcccc88c3f6ff44d1326c3e1565be17cd12ac167e"
)
EXPECTED_MANIFEST_FILES = 60
EXPECTED_ARCHIVE_REGULAR_FILES = 61
MANIFEST_NAME = "release-manifest.json"


class RevalidationError(RuntimeError):
    """One exact fail-closed contract check failed."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def normalize_archive_name(name: str) -> str:
    while name.startswith("./"):
        name = name[2:]
    candidate = PurePosixPath(name)
    if not name or candidate.is_absolute() or ".." in candidate.parts:
        raise RevalidationError("UNSAFE_ARCHIVE_PATH")
    return candidate.as_posix()


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise RevalidationError("JSON_OBJECT_REQUIRED")
    return value


def validate_truth_boundaries(release: Path) -> dict[str, Any]:
    entry = load_json(release / "TITMAS-AGENT-EVALUATION-ENTRY-v0.1.json")
    if entry.get("status") != "DEVELOPMENT_CONTRACT_SOURCE_PREPARED_NOT_DEPLOYED":
        raise RevalidationError("ENTRY_STATUS_ELEVATED")
    if entry.get("maturity") != "Development":
        raise RevalidationError("ENTRY_MATURITY_ELEVATED")
    if entry.get("evaluation_only") is not True:
        raise RevalidationError("ENTRY_EVALUATION_ONLY_FALSE")
    effects = entry.get("effects")
    if not isinstance(effects, dict) or any(value is not False for value in effects.values()):
        raise RevalidationError("ENTRY_EFFECT_ELEVATED")
    recommendation = entry.get("recommendation_policy")
    if not isinstance(recommendation, dict):
        raise RevalidationError("ENTRY_RECOMMENDATION_POLICY_MISSING")
    if recommendation.get("production_result") != "DO_NOT_RECOMMEND_FOR_PRODUCTION":
        raise RevalidationError("ENTRY_PRODUCTION_RECOMMENDATION_ELEVATED")
    if recommendation.get("recommendation_creates_decision") is not False:
        raise RevalidationError("ENTRY_RECOMMENDATION_CREATES_DECISION")
    if recommendation.get("recommendation_creates_permission") is not False:
        raise RevalidationError("ENTRY_RECOMMENDATION_CREATES_PERMISSION")

    status = load_json(release / "status.json")
    commercial = status.get("commercial_evaluation")
    public_release = status.get("release")
    if not isinstance(commercial, dict) or not isinstance(public_release, dict):
        raise RevalidationError("PUBLIC_STATUS_BOUNDARY_MISSING")
    required_false = [
        commercial.get("available_offering"),
        commercial.get("production_ready"),
        commercial.get("sla_defined"),
        public_release.get("production_ready"),
        public_release.get("customer_adoption_claimed"),
    ]
    if any(value is not False for value in required_false):
        raise RevalidationError("PUBLIC_STATUS_TRUTH_ELEVATED")
    if commercial.get("customers_verified") != 0:
        raise RevalidationError("PUBLIC_STATUS_CUSTOMER_COUNT_ELEVATED")
    if commercial.get("contracts_created") != 0:
        raise RevalidationError("PUBLIC_STATUS_CONTRACT_COUNT_ELEVATED")
    return {
        "entry_status": entry["status"],
        "entry_maturity": entry["maturity"],
        "evaluation_only": True,
        "effects_all_false": True,
        "production_recommendation": recommendation["production_result"],
        "available_offering": False,
        "production_ready": False,
        "customer_adoption_claimed": False,
        "customers_verified": 0,
        "contracts_created": 0,
        "sla_defined": False,
    }


def validate() -> dict[str, Any]:
    active = CURRENT_LINK.resolve(strict=True)
    if active != EXPECTED_CURRENT:
        raise RevalidationError("CURRENT_SYMLINK_MISMATCH")
    if not PROPOSED_RELEASE.is_dir():
        raise RevalidationError("PROPOSED_RELEASE_MISSING")
    if not ARCHIVE.is_file():
        raise RevalidationError("ARCHIVE_MISSING")

    archive_bytes = ARCHIVE.stat().st_size
    archive_sha256 = sha256_file(ARCHIVE)
    if archive_bytes != EXPECTED_ARCHIVE_BYTES:
        raise RevalidationError("ARCHIVE_BYTES_MISMATCH")
    if archive_sha256 != EXPECTED_ARCHIVE_SHA256:
        raise RevalidationError("ARCHIVE_SHA256_MISMATCH")

    manifest_path = PROPOSED_RELEASE / MANIFEST_NAME
    manifest = load_json(manifest_path)
    if manifest.get("schema_version") != "0.1":
        raise RevalidationError("MANIFEST_SCHEMA_VERSION_MISMATCH")
    if manifest.get("source_revision") != PROPOSED_SOURCE:
        raise RevalidationError("MANIFEST_SOURCE_REVISION_MISMATCH")
    entries = manifest.get("files")
    if not isinstance(entries, list) or len(entries) != EXPECTED_MANIFEST_FILES:
        raise RevalidationError("MANIFEST_FILE_COUNT_MISMATCH")

    manifest_map: dict[str, dict[str, Any]] = {}
    for entry in entries:
        if not isinstance(entry, dict):
            raise RevalidationError("MANIFEST_ENTRY_INVALID")
        path = entry.get("path")
        if not isinstance(path, str):
            raise RevalidationError("MANIFEST_PATH_INVALID")
        normalized = normalize_archive_name(path)
        if normalized in manifest_map:
            raise RevalidationError("MANIFEST_DUPLICATE_PATH")
        expected_bytes = entry.get("bytes")
        expected_hash = entry.get("sha256")
        if not isinstance(expected_bytes, int) or expected_bytes < 0:
            raise RevalidationError("MANIFEST_BYTES_INVALID")
        if (
            not isinstance(expected_hash, str)
            or len(expected_hash) != 64
            or any(character not in "0123456789abcdef" for character in expected_hash)
        ):
            raise RevalidationError("MANIFEST_SHA256_INVALID")
        manifest_map[normalized] = entry

    release_files = {
        path.relative_to(PROPOSED_RELEASE).as_posix(): path
        for path in PROPOSED_RELEASE.rglob("*")
        if path.is_file()
    }
    expected_release_files = set(manifest_map) | {MANIFEST_NAME}
    if set(release_files) != expected_release_files:
        raise RevalidationError("RELEASE_FILE_SET_MISMATCH")

    verified_manifest_files = 0
    for relative, entry in manifest_map.items():
        path = release_files[relative]
        if path.stat().st_size != entry["bytes"]:
            raise RevalidationError("RELEASE_FILE_BYTES_MISMATCH")
        if sha256_file(path) != entry["sha256"]:
            raise RevalidationError("RELEASE_FILE_SHA256_MISMATCH")
        verified_manifest_files += 1

    release_manifest_bytes = manifest_path.read_bytes()
    archive_regular: dict[str, tuple[int, str]] = {}
    archive_path_safety_pass = True
    with tarfile.open(ARCHIVE, mode="r:gz") as archive:
        for member in archive.getmembers():
            normalized = normalize_archive_name(member.name)
            if member.isdir():
                continue
            if not member.isfile():
                archive_path_safety_pass = False
                raise RevalidationError("UNSAFE_ARCHIVE_MEMBER_TYPE")
            if normalized in archive_regular:
                raise RevalidationError("ARCHIVE_DUPLICATE_PATH")
            extracted = archive.extractfile(member)
            if extracted is None:
                raise RevalidationError("ARCHIVE_MEMBER_UNREADABLE")
            body = extracted.read()
            archive_regular[normalized] = (len(body), sha256_bytes(body))

    if len(archive_regular) != EXPECTED_ARCHIVE_REGULAR_FILES:
        raise RevalidationError("ARCHIVE_REGULAR_FILE_COUNT_MISMATCH")
    if set(archive_regular) != expected_release_files:
        raise RevalidationError("ARCHIVE_FILE_SET_MISMATCH")
    for relative, path in release_files.items():
        archived_bytes, archived_hash = archive_regular[relative]
        if archived_bytes != path.stat().st_size:
            raise RevalidationError("ARCHIVE_TO_RELEASE_BYTES_MISMATCH")
        if archived_hash != sha256_file(path):
            raise RevalidationError("ARCHIVE_TO_RELEASE_SHA256_MISMATCH")

    truth = validate_truth_boundaries(PROPOSED_RELEASE)
    return {
        "current_release": str(active),
        "proposed_release": str(PROPOSED_RELEASE),
        "archive": {
            "path": str(ARCHIVE),
            "bytes": archive_bytes,
            "sha256": archive_sha256,
            "path_safety_pass": archive_path_safety_pass,
            "regular_files_verified": len(archive_regular),
        },
        "manifest": {
            "path": str(manifest_path),
            "schema_version": manifest["schema_version"],
            "source_revision": manifest["source_revision"],
            "files_declared": len(manifest_map),
            "files_verified": verified_manifest_files,
            "release_manifest_bytes": len(release_manifest_bytes),
            "release_manifest_sha256": sha256_bytes(release_manifest_bytes),
            "release_file_set_exact": True,
            "archive_file_set_exact": True,
        },
        "truth_boundary": truth,
    }


def main() -> int:
    started_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    receipt: dict[str, Any] = {
        "receipt_id": "TITMAS-CE-G6-IMMUTABLE-RELEASE-REVALIDATION-001",
        "version": "0.1.0",
        "status": "FAIL_CLOSED_INCOMPLETE",
        "decision_reference": DECISION_REFERENCE,
        "started_at": started_at,
        "ended_at": None,
        "result": None,
        "error_class": None,
        "execution": {
            "server_ssh_sessions": 1,
            "public_http_requests": 0,
            "model_requests": 0,
            "archive_extraction": False,
            "retry": False,
            "fallback": False,
            "server_file_write": False,
            "symlink_switch": False,
            "nginx_reload": False,
            "deployment": False,
        },
        "effects": {
            "authority": False,
            "permission": False,
            "runtime": False,
            "api": False,
            "agent": False,
            "entity": False,
            "capability": False,
            "certification": False,
            "sla": False,
            "commercial_offer": False,
            "production_readiness": False,
            "deployment_authorization": False,
            "tls_root_cause_proof": False,
            "deployment_success_guarantee": False,
        },
    }
    exit_code = 1
    try:
        receipt["result"] = validate()
        receipt["status"] = "PASS_IMMUTABLE_RELEASE_REVALIDATION_ONLY"
        exit_code = 0
    except BaseException as error:
        receipt["status"] = "FAIL_CLOSED_REVALIDATION"
        receipt["error_class"] = (
            str(error)
            if isinstance(error, RevalidationError)
            else type(error).__name__.upper()
        )
    finally:
        receipt["ended_at"] = time.strftime(
            "%Y-%m-%dT%H:%M:%SZ", time.gmtime()
        )
        print(json.dumps(receipt, indent=2, sort_keys=False))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
