"""Allowlisted GitHub GET observations with no mutation methods."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from http.client import IncompleteRead
from pathlib import Path
from typing import Any, Callable
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

from .source_result import (
    AVAILABLE,
    NOT_ASSESSED_CREDENTIAL_UNAVAILABLE,
    NOT_ASSESSED_SOURCE_UNAVAILABLE,
    SOURCE_DRIFT,
    SourceResult,
)


ALLOWLIST = {
    "DBA_COCKPIT": "joy7758/digital-biosphere-architecture-specification",
    "TITMAS_SUPPORTING_LAYER": "joy7758/titmas",
    "DIGITAL_CELL_DEMO": "joy7758/titmas-demo",
    "TITMAC_SCOUT": "joy7758/titmac-scout",
}


class GithubApi:
    """Minimal GitHub API reader. Only GET is exposed."""

    def __init__(
        self,
        token: str | None = None,
        opener: Callable[..., Any] = urlopen,
        api_root: str = "https://api.github.com",
    ) -> None:
        self._token = token or ""
        self._opener = opener
        self._api_root = api_root.rstrip("/")

    def _request(self, reference: str) -> Request:
        url = reference if reference.startswith("https://") else f"{self._api_root}/{reference.lstrip('/')}"
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "dba-weekly-cockpit-read-only-pilot",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if self._token:
            headers["Authorization"] = f"Bearer {self._token}"
        return Request(url, headers=headers, method="GET")

    def request_json(self, reference: str, *, allow_404: bool = False) -> Any:
        try:
            with self._opener(self._request(reference), timeout=20) as response:
                return json.loads(response.read().decode("utf-8"))
        except HTTPError as exc:
            if allow_404 and exc.code == 404:
                return None
            raise

    def request_bytes(self, reference: str) -> bytes:
        with self._opener(self._request(reference), timeout=30) as response:
            return response.read()


class GithubReadOnlyAdapter:
    """Observe only explicitly configured repositories."""

    def __init__(self, api: GithubApi | None = None) -> None:
        token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
        self.api = api or GithubApi(token=token)

    @staticmethod
    def _assert_allowlisted(project_id: str, repository: str) -> None:
        if ALLOWLIST.get(project_id) != repository:
            raise ValueError("REPOSITORY_NOT_ALLOWLISTED")

    def observe_project(self, project: dict[str, Any], observed_at: str) -> SourceResult:
        project_id = project["project_id"]
        repository = project.get("repository")
        if not repository:
            return SourceResult.unavailable(
                source_id=f"github:{project_id}",
                project_id=project_id,
                source_reference="credential-gated-private-repository",
                observed_at=observed_at,
                status=NOT_ASSESSED_CREDENTIAL_UNAVAILABLE,
                reason="CROSS_REPO_READ_CREDENTIAL_UNAVAILABLE",
            )
        self._assert_allowlisted(project_id, repository)
        if project.get("cross_repo_credential_required") and not os.environ.get("DBA_COCKPIT_READ_TOKEN"):
            return SourceResult.unavailable(
                source_id=f"github:{repository}",
                project_id=project_id,
                source_reference=f"https://github.com/{repository}",
                observed_at=observed_at,
                status=NOT_ASSESSED_CREDENTIAL_UNAVAILABLE,
                reason="CROSS_REPO_READ_CREDENTIAL_UNAVAILABLE",
            )
        try:
            metadata = self.api.request_json(f"repos/{repository}")
            branch = project.get("branch") or metadata.get("default_branch") or "main"
            commit = self.api.request_json(f"repos/{repository}/commits/{quote(branch, safe='')}")
            revision = commit["sha"]
            tree_digest = commit.get("commit", {}).get("tree", {}).get("sha")
            runs = self.api.request_json(
                f"repos/{repository}/actions/runs?branch={quote(branch, safe='')}&status=completed&per_page=5"
            )
            pulls = self.api.request_json(f"repos/{repository}/pulls?state=open&per_page=100")
            issues = self.api.request_json(f"repos/{repository}/issues?state=open&per_page=100")
            release = self.api.request_json(f"repos/{repository}/releases/latest", allow_404=True)
            status_file = self._status_file(project, repository, revision, branch)
            payload = {
                "repository": repository,
                "default_branch": branch,
                "head_revision": revision,
                "head_tree_digest": tree_digest,
                "head_date": commit.get("commit", {}).get("committer", {}).get("date"),
                "recent_completed_ci": [
                    {
                        "run_id": item.get("id"),
                        "name": item.get("name"),
                        "conclusion": item.get("conclusion"),
                        "head_sha": item.get("head_sha"),
                        "completed_at": item.get("updated_at"),
                    }
                    for item in runs.get("workflow_runs", [])
                ],
                "open_pull_request_count": len(pulls) if isinstance(pulls, list) else 0,
                "open_issue_count": len(
                    [item for item in issues if isinstance(item, dict) and "pull_request" not in item]
                ) if isinstance(issues, list) else 0,
                "latest_release": None if release is None else {
                    "tag": release.get("tag_name"),
                    "published_at": release.get("published_at"),
                    "url": release.get("html_url"),
                },
                "declared_status_file": status_file,
            }
            return SourceResult(
                source_id=f"github:{repository}",
                project_id=project_id,
                status=AVAILABLE,
                source_reference=f"https://github.com/{repository}/tree/{revision}",
                observed_at=observed_at,
                retrieved_at=observed_at,
                payload=payload,
                limitations=[
                    "GitHub metadata is a point-in-time observation, not project acceptance.",
                    "Repository visibility does not establish production deployment or safety.",
                ],
            )
        except IncompleteRead:
            return SourceResult(
                source_id=f"github:{repository}",
                project_id=project_id,
                status="NOT_ASSESSED",
                source_reference=f"https://github.com/{repository}",
                observed_at=observed_at,
                retrieved_at=observed_at,
                payload={
                    "repository": repository,
                    "source_kind": "GITHUB_REPOSITORY_METADATA",
                    "reason_code": "NOT_ASSESSED_SOURCE_UNAVAILABLE",
                    "source_available": False,
                    "evidence_admitted": False,
                    "partial_payload_used": False,
                    "exception_class": "IncompleteRead",
                },
                limitations=[
                    "The incomplete response was discarded without parsing partial bytes.",
                    "Source unavailability is not interpreted as a healthy project state.",
                ],
            )
        except (HTTPError, URLError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
            return SourceResult.unavailable(
                source_id=f"github:{repository}",
                project_id=project_id,
                source_reference=f"https://github.com/{repository}",
                observed_at=observed_at,
                reason=f"GITHUB_READ_FAILED:{type(exc).__name__}",
            )

    def _status_file(
        self,
        project: dict[str, Any],
        repository: str,
        revision: str,
        branch: str,
    ) -> dict[str, Any]:
        path = project.get("status_path")
        if not path:
            return {"status": "NOT_DECLARED", "path": None, "revision_relation": "NOT_APPLICABLE"}
        encoded = quote(path, safe="/")
        content = self.api.request_json(
            f"repos/{repository}/contents/{encoded}?ref={quote(revision, safe='')}", allow_404=True
        )
        if content is None:
            return {"status": "NOT_FOUND", "path": path, "revision_relation": "NOT_ASSESSED"}
        history = self.api.request_json(
            f"repos/{repository}/commits?path={encoded}&sha={quote(branch, safe='')}&per_page=1"
        )
        latest = history[0] if isinstance(history, list) and history else {}
        return {
            "status": "PRESENT",
            "path": path,
            "blob_sha": content.get("sha"),
            "size": content.get("size"),
            "last_changed_at": latest.get("commit", {}).get("committer", {}).get("date"),
            "revision_relation": "FETCHED_AT_EXACT_HEAD_REVISION",
        }

    def observe_scout(self, observed_at: str) -> SourceResult:
        """Reuse the existing fail-closed Scout adapter when a dedicated token exists."""
        repository = ALLOWLIST["TITMAC_SCOUT"]
        token = os.environ.get("DBA_COCKPIT_READ_TOKEN")
        if not token:
            return SourceResult.unavailable(
                source_id=f"github:{repository}",
                project_id="TITMAC_SCOUT",
                source_reference=f"https://github.com/{repository}",
                observed_at=observed_at,
                status=NOT_ASSESSED_CREDENTIAL_UNAVAILABLE,
                reason="CROSS_REPO_READ_CREDENTIAL_UNAVAILABLE",
            )

        dba_root = Path(__file__).resolve().parents[3]
        if str(dba_root) not in sys.path:
            sys.path.insert(0, str(dba_root))
        from cockpit.read_only_status_adapter import CockpitSourceError, ReadOnlyStatusAdapter

        def runner(command: list[str]) -> subprocess.CompletedProcess[str]:
            env = dict(os.environ)
            env["GH_TOKEN"] = token
            return subprocess.run(command, capture_output=True, text=True, check=False, env=env)

        try:
            projection = ReadOnlyStatusAdapter(command_runner=runner).fetch_github(
                "titmac-scout",
                retrieved_at=datetime.fromisoformat(observed_at.replace("Z", "+00:00")).astimezone(timezone.utc),
            )
            return SourceResult(
                source_id=f"github:{repository}:existing-adapter",
                project_id="TITMAC_SCOUT",
                status=AVAILABLE,
                source_reference=f"cockpit/source-registry.json#titmac-scout@{projection['source_revision']}",
                observed_at=observed_at,
                retrieved_at=observed_at,
                payload=projection,
                limitations=["The projection remains observation-only and fail-closed on source drift."],
            )
        except CockpitSourceError as exc:
            status = SOURCE_DRIFT if exc.code == "SOURCE_DRIFT" else NOT_ASSESSED_SOURCE_UNAVAILABLE
            return SourceResult.unavailable(
                source_id=f"github:{repository}:existing-adapter",
                project_id="TITMAC_SCOUT",
                source_reference="cockpit/source-registry.json#titmac-scout",
                observed_at=observed_at,
                status=status,
                reason=exc.code,
            )
