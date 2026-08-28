#!/usr/bin/env python3
"""Generate a deterministic demo or a bounded live read-only DBA cockpit bundle."""

from __future__ import annotations

import argparse
import os
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    from .coordinator import WeeklyCoordinator
    from .contracts import canonical_json, parse_assignments, read_json
    from .sources.artifact_memory import ArtifactMemory
    from .sources.dependency_readonly import DependencyReadOnlyAdapter
    from .sources.github_readonly import GithubReadOnlyAdapter
    from .sources.public_http_readonly import PublicHttpReadOnlyAdapter
    from .sources.source_result import AVAILABLE, NOT_ASSESSED_CREDENTIAL_UNAVAILABLE, SourceResult
except ImportError:  # Direct execution from cockpit/weekly/run_weekly.py.
    from coordinator import WeeklyCoordinator
    from contracts import canonical_json, parse_assignments, read_json
    from sources.artifact_memory import ArtifactMemory
    from sources.dependency_readonly import DependencyReadOnlyAdapter
    from sources.github_readonly import GithubReadOnlyAdapter
    from sources.public_http_readonly import PublicHttpReadOnlyAdapter
    from sources.source_result import AVAILABLE, NOT_ASSESSED_CREDENTIAL_UNAVAILABLE, SourceResult


WEEKLY = Path(__file__).resolve().parent
DBA_ROOT = WEEKLY.parents[1]
REPOSITORY_ROOT = DBA_ROOT.parent
DEMO_MODE = "demo"
LIVE_MODE = "live-read-only-pilot"
LIVE_SNAPSHOT_MODE = "LIVE_READ_ONLY_OBSERVATION_PILOT"
WORKFLOW_FILE = "dba-weekly-cockpit.yml"


def _base_context(as_of: str) -> dict[str, Any]:
    direction_path = DBA_ROOT / "CURRENT-PROJECT-DIRECTION-2026-08-28.md"
    reconciliation_path = DBA_ROOT / "PROJECT-STATE-RECONCILIATION-2026-08-28.md"
    redyan_path = DBA_ROOT / "RED-YAN-REMOTE-RUNTIME-EVIDENCE-SNAPSHOT-2026-08-28.json"
    matrix_path = DBA_ROOT / "titmas-component-adoption-matrix-v1.0.json"
    convergence_path = DBA_ROOT / "titmas-commercial-product-convergence-status-v1.0.json"
    source_registry_path = DBA_ROOT / "cockpit" / "source-registry.json"
    scout_projection_path = DBA_ROOT / "cockpit" / "projections" / "titmac-scout.json"
    return {
        "weekly_root": WEEKLY,
        "dba_root": DBA_ROOT,
        "repository_root": REPOSITORY_ROOT,
        "as_of": as_of,
        "direction": parse_assignments(direction_path.read_text(encoding="utf-8")),
        "reconciliation": parse_assignments(reconciliation_path.read_text(encoding="utf-8")),
        "redyan": read_json(redyan_path),
        "component_matrix": read_json(matrix_path),
        "convergence_snapshot": read_json(convergence_path),
        "source_registry": read_json(source_registry_path),
        "scout_projection": read_json(scout_projection_path),
        "project_registry": read_json(WEEKLY / "project-check-registry.json"),
        "cell_registry": read_json(WEEKLY / "cell-registry.json"),
        "source_paths": {
            "direction": str(direction_path.relative_to(DBA_ROOT)),
            "reconciliation": str(reconciliation_path.relative_to(DBA_ROOT)),
            "redyan": str(redyan_path.relative_to(DBA_ROOT)),
            "component_matrix": str(matrix_path.relative_to(DBA_ROOT)),
            "convergence": str(convergence_path.relative_to(DBA_ROOT)),
            "source_registry": str(source_registry_path.relative_to(DBA_ROOT)),
            "read_only_adapter": "cockpit/read_only_status_adapter.py",
            "scout_projection": str(scout_projection_path.relative_to(DBA_ROOT)),
        },
    }


def load_demo_context(as_of: str) -> dict[str, Any]:
    context = _base_context(as_of)
    fixed_audit = WEEKLY / "inputs" / "live-dependency-audit-candidate-2026-08-29.json"
    previous = sorted((WEEKLY / "history").glob("????-W??.json"))
    context.update(
        {
            "snapshot_mode": "PROTOTYPE_READ_ONLY_CANDIDATE",
            "deterministic": True,
            "live_dependency_audit": read_json(fixed_audit),
            "previous_snapshot": read_json(previous[-1]) if previous else None,
            "source_observations": {},
            "source_observation_records": [],
            "source_observation_summary": {
                "source_mode": "RETAINED_SNAPSHOT",
                "live_source_success_count": 0,
                "not_assessed_count": 0,
            },
        }
    )
    context["source_paths"]["live_dependency_audit"] = str(fixed_audit.relative_to(DBA_ROOT))
    return context


def load_context(as_of: str) -> dict[str, Any]:
    """Backward-compatible deterministic context used by v0.1 callers."""
    return load_demo_context(as_of)


def _credential_unavailable(project: dict[str, Any], observed_at: str) -> SourceResult:
    return SourceResult.unavailable(
        source_id=f"github:{project['project_id']}",
        project_id=project["project_id"],
        source_reference="credential-gated-private-repository",
        observed_at=observed_at,
        status=NOT_ASSESSED_CREDENTIAL_UNAVAILABLE,
        reason="CROSS_REPO_READ_CREDENTIAL_UNAVAILABLE",
    )


def load_live_context(as_of: str, pilot_sequence: str) -> dict[str, Any]:
    context = _base_context(as_of)
    registry_projects = context["project_registry"]["projects"]
    github = GithubReadOnlyAdapter()
    project_results: list[SourceResult] = []
    for project in registry_projects:
        project_id = project["project_id"]
        if project_id == "TITMAC_SCOUT":
            result = github.observe_scout(as_of)
        elif project.get("cross_repo_credential_required") and not os.environ.get("DBA_COCKPIT_READ_TOKEN"):
            result = _credential_unavailable(project, as_of)
        else:
            result = github.observe_project(project, as_of)
        project_results.append(result)

    http_results = PublicHttpReadOnlyAdapter().observe_all(as_of)
    dependency = DependencyReadOnlyAdapter().observe(DBA_ROOT / "site", REPOSITORY_ROOT, as_of)
    repository = os.environ.get(
        "GITHUB_REPOSITORY", "joy7758/digital-biosphere-architecture-specification"
    )
    run_id = os.environ.get("GITHUB_RUN_ID", f"LOCAL-{as_of}")
    memory_result = ArtifactMemory().load_previous(
        repository=repository,
        workflow=WORKFLOW_FILE,
        branch="main",
        current_run_id=run_id,
        observed_at=as_of,
    )
    all_results = project_results + http_results + [dependency, memory_result]
    records = [item.to_dict() for item in all_results]
    available = sum(item.status == AVAILABLE for item in all_results)
    not_assessed = len(all_results) - available
    source_observations = {item.project_id: item.to_dict() for item in project_results}
    source_summary = {
        "source_mode": "LIVE_READ_ONLY",
        "live_source_success_count": available,
        "not_assessed_count": not_assessed,
        "project_source_count": len(project_results),
        "public_endpoint_count": len(http_results),
        "partial_coverage": not_assessed > 0,
        "cross_repo_read_credential": (
            "AVAILABLE" if os.environ.get("DBA_COCKPIT_READ_TOKEN") else "UNAVAILABLE"
        ),
    }
    context.update(
        {
            "snapshot_mode": LIVE_SNAPSHOT_MODE,
            "deterministic": False,
            "pilot_sequence": pilot_sequence,
            "run_identity": {
                "run_id": run_id,
                "repository": repository,
                "workflow": WORKFLOW_FILE,
                "pilot_sequence": pilot_sequence,
            },
            "source_observations": source_observations,
            "public_http_observations": [item.to_dict() for item in http_results],
            "dependency_observation": dependency.to_dict(),
            "source_mutation": dependency.status == "SOURCE_MUTATION_DETECTED",
            "live_dependency_audit": dependency.payload,
            "artifact_memory_observation": memory_result.to_dict(),
            "artifact_memory_metadata": memory_result.payload,
            "previous_snapshot": memory_result.payload.get("snapshot"),
            "source_observation_records": records,
            "source_observation_summary": source_summary,
        }
    )
    context["source_paths"]["live_dependency_audit"] = dependency.source_reference
    context["source_paths"]["artifact_memory"] = memory_result.source_reference
    return context


def _write_pilot_files(snapshot: dict[str, Any], context: dict[str, Any], output_dir: Path) -> None:
    summary = {
        **context.get("source_observation_summary", {}),
        "observed_at": snapshot["observed_at"],
        "discovery_state": snapshot.get("discovery_state", "UNKNOWN"),
        "sources": context.get("source_observation_records", []),
    }
    memory = snapshot.get("memory", {})
    sequence = context.get("pilot_sequence", "first")
    source_mutation = (
        context.get("dependency_observation", {}).get("status") == "SOURCE_MUTATION_DETECTED"
    )
    memory_required_failed = (
        sequence == "second" and memory.get("PREVIOUS_LIVE_ARTIFACT_LOADED") is not True
    )
    credential_missing = (
        context.get("source_observation_summary", {}).get("cross_repo_read_credential")
        == "UNAVAILABLE"
    )
    if source_mutation or memory_required_failed:
        pilot_status = "LIVE_READ_ONLY_PILOT_FAILED"
    elif credential_missing:
        pilot_status = "LIVE_READ_ONLY_PILOT_PASS_WITH_PARTIAL_COVERAGE"
    else:
        pilot_status = "LIVE_READ_ONLY_PILOT_PASS"
    boundary = {
        "mode": LIVE_SNAPSHOT_MODE,
        "pilot_sequence": sequence,
        "pilot_status": pilot_status,
        "prototype_only": False,
        "pilot_only": True,
        "schedule_enabled": False,
        "source_mutation": source_mutation,
        "red_yan_runtime_access": False,
        "auto_fix": False,
        "auto_pr": False,
        "auto_merge": False,
        "auto_deploy": False,
        "cross_repo_private_coverage": (
            "NOT_ASSESSED_CREDENTIAL_UNAVAILABLE" if credential_missing else "AVAILABLE"
        ),
        "memory": {
            key: memory.get(key)
            for key in (
                "PREVIOUS_LIVE_ARTIFACT_LOADED",
                "MEMORY_COMPARISON_EXECUTED",
                "ARTIFACT_FROM_CURRENT_RUN_REJECTED",
                "FAILED_OR_EXPIRED_ARTIFACT_REJECTED",
            )
        },
    }
    (output_dir / "source-observation-summary.json").write_text(
        canonical_json(summary), encoding="utf-8"
    )
    (output_dir / "pilot-boundary-report.json").write_text(
        canonical_json(boundary), encoding="utf-8"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--mode", choices=(DEMO_MODE, LIVE_MODE), default=DEMO_MODE)
    parser.add_argument("--pilot-sequence", choices=("first", "second"), default="first")
    parser.add_argument("--demo", action="store_true", help="Backward-compatible alias for --mode demo")
    parser.add_argument("--as-of")
    args = parser.parse_args()
    mode = DEMO_MODE if args.demo else args.mode
    as_of = args.as_of or (
        "2026-08-29T00:30:00+08:00"
        if mode == DEMO_MODE
        else datetime.now().astimezone().isoformat(timespec="seconds")
    )
    output_dir = args.output_dir.resolve()
    if mode == DEMO_MODE:
        context = load_demo_context(as_of)
        snapshot_name = "weekly-snapshot-2026-W35.json"
    else:
        context = load_live_context(as_of, args.pilot_sequence)
        snapshot_name = "latest.json"
    snapshot = WeeklyCoordinator().run(context, output_dir, snapshot_name)
    if mode == LIVE_MODE:
        _write_pilot_files(snapshot, context, output_dir)
    print(f"DBA_WEEKLY_COCKPIT_STATUS={snapshot['overall_status']}")
    print(f"SNAPSHOT={output_dir / snapshot_name}")
    print(f"DASHBOARD={output_dir / 'dashboard.html'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
