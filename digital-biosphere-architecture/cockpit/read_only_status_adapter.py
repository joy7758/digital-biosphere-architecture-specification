#!/usr/bin/env python3
"""Fail-closed, read-only project-status projection for the DBA cockpit."""

from __future__ import annotations

import argparse
import base64
import copy
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any, Callable
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = ROOT / "cockpit" / "source-registry.json"

STATUS_VALUES = {
    "PLANNED",
    "INITIALIZING",
    "IMPLEMENTING",
    "VALIDATING",
    "BLOCKED",
    "NOT_ASSESSED",
    "CANDIDATE",
    "READY_FOR_HUMAN_REVIEW",
    "MERGED",
    "RELEASED",
    "DEPLOYED",
    "MAINTENANCE",
}

REQUIRED_STATUS_FIELDS = {
    "status_contract_version",
    "project_id",
    "project_name",
    "conversation_aliases",
    "repository",
    "repository_visibility",
    "canonical_branch",
    "source_revision",
    "source_tree_digest",
    "architecture_owner",
    "implementation_owner",
    "evidence_semantics_owner",
    "lifecycle_status",
    "development_phase",
    "implementation_status",
    "discovery_layer_status",
    "self_observation_status",
    "problem_evidence_status",
    "canonical_owner_resolution_status",
    "patch_variant_status",
    "sandbox_implementation_status",
    "fitness_evaluation_status",
    "selection_status",
    "rollback_status",
    "lineage_status",
    "self_healing_status",
    "self_evolution_status",
    "autonomous_risk_classes",
    "human_authorization_risk_classes",
    "latest_evolution_run",
    "latest_run_result",
    "latest_run_digest",
    "latest_outcome_evidence",
    "latest_rollback_evidence",
    "test_summary",
    "ci_summary",
    "open_pull_requests",
    "blocking_issues",
    "blocking_decisions",
    "next_human_decision",
    "known_limitations",
    "authority_boundaries",
    "security_boundaries",
    "evolution_progress",
    "p0_10_reopened",
    "production_runtime_changed",
    "database_changed",
    "production_credential_created",
    "generated_at",
    "fresh_until",
}

STATUS_FIELDS = {
    "lifecycle_status",
    "discovery_layer_status",
    "self_observation_status",
    "problem_evidence_status",
    "canonical_owner_resolution_status",
    "patch_variant_status",
    "sandbox_implementation_status",
    "fitness_evaluation_status",
    "selection_status",
    "rollback_status",
    "lineage_status",
    "self_healing_status",
    "self_evolution_status",
}


class CockpitSourceError(RuntimeError):
    """A fail-closed source error with a stable machine reason code."""

    def __init__(self, code: str, detail: str | None = None) -> None:
        self.code = code
        self.detail = detail
        super().__init__(code if detail is None else f"{code}:{detail}")


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def parse_timestamp(value: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (AttributeError, ValueError) as exc:
        raise CockpitSourceError("SOURCE_INVALID", "INVALID_TIMESTAMP") from exc
    if parsed.tzinfo is None:
        raise CockpitSourceError("SOURCE_INVALID", "TIMESTAMP_MISSING_TIMEZONE")
    return parsed.astimezone(timezone.utc)


def safe_source_path(value: str) -> str:
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts:
        raise CockpitSourceError("SOURCE_INVALID", "UNSAFE_SOURCE_PATH")
    return str(path)


class ReadOnlyStatusAdapter:
    """Read-only adapter; intentionally exposes no write or mutation methods."""

    def __init__(
        self,
        registry_path: Path = DEFAULT_REGISTRY,
        command_runner: Callable[[list[str]], subprocess.CompletedProcess[str]] | None = None,
    ) -> None:
        self.registry_path = Path(registry_path)
        self.command_runner = command_runner or self._run

    def source(self, project_id: str) -> dict[str, Any]:
        try:
            registry = json.loads(self.registry_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise CockpitSourceError("SOURCE_REGISTRY_INVALID") from exc
        matches = [entry for entry in registry.get("sources", []) if entry.get("project_id") == project_id]
        if len(matches) != 1:
            raise CockpitSourceError("SOURCE_REGISTRATION_NOT_UNIQUE")
        entry = matches[0]
        if entry.get("access_mode") != "READ_ONLY" or entry.get("refresh_mode") != "ON_DEMAND":
            raise CockpitSourceError("SOURCE_REGISTRY_AUTHORITY_INVALID")
        return entry

    def fetch_local_git(
        self,
        project_id: str,
        repository_path: Path,
        *,
        candidate: bool = False,
        retrieved_at: datetime | None = None,
    ) -> dict[str, Any]:
        entry = self.source(project_id)
        ref = entry["candidate_source_branch"] if candidate else entry["source_branch"]
        expected_revision = entry.get("candidate_source_revision") if candidate else None
        expected_tree = entry.get("candidate_source_tree_digest") if candidate else None
        expected_digest = entry.get("candidate_status_digest") if candidate else None
        repository_path = Path(repository_path).resolve()

        revision = self._git(repository_path, "rev-parse", ref)
        tree_digest = self._git(repository_path, "rev-parse", f"{ref}^{{tree}}")
        status_bytes = self._git_bytes(repository_path, "show", f"{ref}:{safe_source_path(entry['source_status_path'])}")
        schema_bytes = self._git_bytes(repository_path, "show", f"{ref}:{safe_source_path(entry['source_schema_path'])}")
        return self._project(
            entry,
            status_bytes,
            schema_bytes,
            revision=revision,
            tree_digest=tree_digest,
            source_ref=ref,
            source_mode="CANDIDATE_EXACT_REVISION" if candidate else "CANONICAL_BRANCH",
            expected_revision=expected_revision,
            expected_tree=expected_tree,
            expected_digest=expected_digest,
            retrieved_at=retrieved_at,
        )

    def fetch_github(
        self,
        project_id: str,
        *,
        candidate: bool = False,
        retrieved_at: datetime | None = None,
    ) -> dict[str, Any]:
        entry = self.source(project_id)
        ref = entry["candidate_source_branch"] if candidate else entry["source_branch"]
        expected_revision = entry.get("candidate_source_revision") if candidate else None
        expected_tree = entry.get("candidate_source_tree_digest") if candidate else None
        expected_digest = entry.get("candidate_status_digest") if candidate else None
        repository = entry["source_repository"]

        commit = self._gh_json(f"repos/{repository}/commits/{quote(ref, safe='')}")
        revision = commit.get("sha")
        tree_digest = commit.get("commit", {}).get("tree", {}).get("sha")
        if not revision or not tree_digest:
            raise CockpitSourceError("SOURCE_UNAVAILABLE", "GITHUB_COMMIT_METADATA")
        status_bytes = self._gh_content(repository, entry["source_status_path"], ref)
        schema_bytes = self._gh_content(repository, entry["source_schema_path"], ref)
        return self._project(
            entry,
            status_bytes,
            schema_bytes,
            revision=revision,
            tree_digest=tree_digest,
            source_ref=ref,
            source_mode="CANDIDATE_EXACT_REVISION" if candidate else "CANONICAL_BRANCH",
            expected_revision=expected_revision,
            expected_tree=expected_tree,
            expected_digest=expected_digest,
            retrieved_at=retrieved_at,
        )

    def _project(
        self,
        entry: dict[str, Any],
        status_bytes: bytes,
        schema_bytes: bytes,
        *,
        revision: str,
        tree_digest: str,
        source_ref: str,
        source_mode: str,
        expected_revision: str | None,
        expected_tree: str | None,
        expected_digest: str | None,
        retrieved_at: datetime | None,
    ) -> dict[str, Any]:
        if expected_revision and revision != expected_revision:
            raise CockpitSourceError("SOURCE_DRIFT", "REVISION_MISMATCH")
        if expected_tree and tree_digest != expected_tree:
            raise CockpitSourceError("SOURCE_DRIFT", "TREE_MISMATCH")

        status_digest = hashlib.sha256(status_bytes).hexdigest()
        if expected_digest and status_digest != expected_digest:
            raise CockpitSourceError("SOURCE_INVALID", "DIGEST_MISMATCH")

        try:
            status = json.loads(status_bytes)
            schema = json.loads(schema_bytes)
        except json.JSONDecodeError as exc:
            raise CockpitSourceError("SOURCE_INVALID", "JSON_PARSE") from exc
        self._validate_status(status, schema, entry)

        resolved = copy.deepcopy(status)
        if resolved["source_revision"] == "SELF":
            resolved["source_revision"] = revision
        if resolved["source_tree_digest"] == "SELF_TREE":
            resolved["source_tree_digest"] = tree_digest
        for stage in resolved["evolution_progress"].values():
            if stage.get("source_revision") == "SELF":
                stage["source_revision"] = revision
        if resolved.get("test_summary", {}).get("source_revision") == "SELF":
            resolved["test_summary"]["source_revision"] = revision
        for pull_request in resolved["open_pull_requests"]:
            if pull_request.get("head_revision") == "SELF":
                pull_request["head_revision"] = revision
        if resolved["source_revision"] != revision:
            raise CockpitSourceError("SOURCE_DRIFT", "REVISION_MISMATCH")
        if resolved["source_tree_digest"] != tree_digest:
            raise CockpitSourceError("SOURCE_DRIFT", "TREE_MISMATCH")

        now = (retrieved_at or datetime.now(timezone.utc)).astimezone(timezone.utc)
        fresh_until = parse_timestamp(resolved["fresh_until"])
        if now > fresh_until:
            raise CockpitSourceError("SOURCE_STALE")

        return {
            "projection_contract_version": "0.1",
            "project_id": entry["project_id"],
            "display_name": entry["display_name"],
            "conversation_alias": entry["conversation_alias"],
            "source_reference": {
                "repository": entry["source_repository"],
                "branch": source_ref,
                "status_path": entry["source_status_path"],
                "schema_path": entry["source_schema_path"],
                "mode": source_mode,
            },
            "source_revision": revision,
            "source_tree_digest": tree_digest,
            "status_source_digest": status_digest,
            "source_freshness": "FRESH",
            "fresh_until": resolved["fresh_until"],
            "retrieved_at": now.isoformat().replace("+00:00", "Z"),
            "source_integrity": "PASS",
            "source_revision_match": True,
            "summary": self._summary(resolved),
            "community_boundaries": {
                "architecture_status": "READY",
                "protocol_status": "CANDIDATE",
                "public_operation_status": "NOT_YET_VERIFIED",
            },
            "projection_boundaries": {
                "cockpit_pull_only": True,
                "cockpit_push": False,
                "cockpit_stores_projection": True,
                "cockpit_stores_canonical_run": False,
                "raw_run_copied": False,
                "status_projection_is_adoption": False,
            },
        }

    def _validate_status(
        self,
        status: dict[str, Any],
        schema: dict[str, Any],
        entry: dict[str, Any],
    ) -> None:
        missing = sorted(REQUIRED_STATUS_FIELDS - status.keys())
        if missing:
            raise CockpitSourceError("SOURCE_INVALID", f"MISSING_FIELDS:{','.join(missing)}")
        schema_required = set(schema.get("required", []))
        if not REQUIRED_STATUS_FIELDS.issubset(schema_required):
            raise CockpitSourceError("SOURCE_INVALID", "SCHEMA_REQUIRED_FIELDS")
        expected = {
            "project_id": "titmac-scout",
            "project_name": "titmac-scout",
            "conversation_aliases": ["tiamas-scout"],
            "repository": entry["source_repository"],
            "repository_visibility": "PRIVATE",
            "canonical_branch": "main",
            "p0_10_reopened": False,
            "production_runtime_changed": False,
            "database_changed": False,
            "production_credential_created": False,
        }
        for key, value in expected.items():
            if status.get(key) != value:
                raise CockpitSourceError("SOURCE_INVALID", f"BOUNDARY:{key}")
        invalid = sorted(key for key in STATUS_FIELDS if status.get(key) not in STATUS_VALUES)
        if invalid:
            raise CockpitSourceError("SOURCE_INVALID", f"STATUS_ENUM:{','.join(invalid)}")
        if not status.get("known_limitations"):
            raise CockpitSourceError("SOURCE_INVALID", "KNOWN_LIMITATIONS_REQUIRED")

    @staticmethod
    def _summary(status: dict[str, Any]) -> dict[str, Any]:
        return {
            "implementation_owner": status["implementation_owner"],
            "canonical_repository": status["repository"],
            "lifecycle_status": status["lifecycle_status"],
            "development_phase": status["development_phase"],
            "implementation_status": status["implementation_status"],
            "discovery_status": status["discovery_layer_status"],
            "self_healing_status": status["self_healing_status"],
            "self_evolution_status": status["self_evolution_status"],
            "latest_evolution_run": status["latest_evolution_run"],
            "latest_evolution_result": status["latest_run_result"],
            "latest_selected_variant": None,
            "latest_outcome_evidence": status["latest_outcome_evidence"],
            "latest_rollback_evidence": status["latest_rollback_evidence"],
            "tests": status["test_summary"],
            "ci": status["ci_summary"],
            "open_pull_requests": status["open_pull_requests"],
            "blocking_issues": status["blocking_issues"],
            "blocking_decisions": status["blocking_decisions"],
            "next_human_decision": status["next_human_decision"],
            "known_limitations": status["known_limitations"],
            "authority_boundaries": status["authority_boundaries"],
            "evolution_progress": status["evolution_progress"],
            "p0_10_reopened": status["p0_10_reopened"],
        }

    def _git(self, repository_path: Path, *arguments: str) -> str:
        result = self.command_runner(["git", "-C", str(repository_path), *arguments])
        if result.returncode != 0:
            raise CockpitSourceError("SOURCE_UNAVAILABLE", result.stderr.strip())
        return result.stdout.strip()

    def _git_bytes(self, repository_path: Path, *arguments: str) -> bytes:
        result = subprocess.run(
            ["git", "-C", str(repository_path), *arguments],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if result.returncode != 0:
            raise CockpitSourceError("SOURCE_UNAVAILABLE", result.stderr.decode("utf-8", errors="replace").strip())
        return result.stdout

    def _gh_json(self, endpoint: str) -> dict[str, Any]:
        result = self.command_runner(["gh", "api", endpoint])
        if result.returncode != 0:
            raise CockpitSourceError("SOURCE_UNAVAILABLE", result.stderr.strip())
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError as exc:
            raise CockpitSourceError("SOURCE_UNAVAILABLE", "GITHUB_JSON_INVALID") from exc

    def _gh_content(self, repository: str, path: str, ref: str) -> bytes:
        payload = self._gh_json(
            f"repos/{repository}/contents/{safe_source_path(path)}?ref={quote(ref, safe='')}"
        )
        if payload.get("encoding") != "base64" or not payload.get("content"):
            raise CockpitSourceError("SOURCE_UNAVAILABLE", "GITHUB_CONTENT_INVALID")
        try:
            return base64.b64decode(payload["content"], validate=False)
        except (ValueError, TypeError) as exc:
            raise CockpitSourceError("SOURCE_UNAVAILABLE", "GITHUB_CONTENT_DECODE") from exc

    @staticmethod
    def _run(arguments: list[str]) -> subprocess.CompletedProcess[str]:
        return subprocess.run(arguments, check=False, capture_output=True, text=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-id", default="titmac-scout")
    parser.add_argument("--local-repository", type=Path)
    parser.add_argument("--candidate", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    adapter = ReadOnlyStatusAdapter()
    try:
        if args.local_repository:
            projection = adapter.fetch_local_git(
                args.project_id,
                args.local_repository,
                candidate=args.candidate,
            )
        else:
            projection = adapter.fetch_github(args.project_id, candidate=args.candidate)
    except CockpitSourceError as exc:
        print(canonical_json({"ok": False, "cockpit_status": exc.code, "detail": exc.detail}), end="")
        return 1

    output = canonical_json(projection)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
