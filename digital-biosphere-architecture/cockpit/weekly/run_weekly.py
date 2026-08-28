#!/usr/bin/env python3
"""Generate a read-only DBA weekly cockpit candidate bundle."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

from coordinator import WeeklyCoordinator
from contracts import parse_assignments, read_json


WEEKLY = Path(__file__).resolve().parent
DBA_ROOT = WEEKLY.parents[1]


def load_context(as_of: str) -> dict[str, object]:
    direction_path = DBA_ROOT / "CURRENT-PROJECT-DIRECTION-2026-08-28.md"
    reconciliation_path = DBA_ROOT / "PROJECT-STATE-RECONCILIATION-2026-08-28.md"
    direction = parse_assignments(direction_path.read_text(encoding="utf-8"))
    reconciliation = parse_assignments(reconciliation_path.read_text(encoding="utf-8"))
    redyan_path = DBA_ROOT / "RED-YAN-REMOTE-RUNTIME-EVIDENCE-SNAPSHOT-2026-08-28.json"
    matrix_path = DBA_ROOT / "titmas-component-adoption-matrix-v1.0.json"
    convergence_path = DBA_ROOT / "titmas-commercial-product-convergence-status-v1.0.json"
    source_registry_path = DBA_ROOT / "cockpit" / "source-registry.json"
    scout_projection_path = DBA_ROOT / "cockpit" / "projections" / "titmac-scout.json"
    live_audit_path = WEEKLY / "inputs" / "live-dependency-audit-candidate-2026-08-29.json"
    previous = sorted((WEEKLY / "history").glob("????-W??.json"))
    return {
        "weekly_root": WEEKLY,
        "dba_root": DBA_ROOT,
        "as_of": as_of,
        "direction": direction,
        "reconciliation": reconciliation,
        "redyan": read_json(redyan_path),
        "component_matrix": read_json(matrix_path),
        "convergence_snapshot": read_json(convergence_path),
        "source_registry": read_json(source_registry_path),
        "scout_projection": read_json(scout_projection_path),
        "live_dependency_audit": read_json(live_audit_path),
        "project_registry": read_json(WEEKLY / "project-check-registry.json"),
        "cell_registry": read_json(WEEKLY / "cell-registry.json"),
        "previous_snapshot": read_json(previous[-1]) if previous else None,
        "source_paths": {
            "direction": str(direction_path.relative_to(DBA_ROOT)),
            "reconciliation": str(reconciliation_path.relative_to(DBA_ROOT)),
            "redyan": str(redyan_path.relative_to(DBA_ROOT)),
            "component_matrix": str(matrix_path.relative_to(DBA_ROOT)),
            "convergence": str(convergence_path.relative_to(DBA_ROOT)),
            "source_registry": str(source_registry_path.relative_to(DBA_ROOT)),
            "read_only_adapter": "cockpit/read_only_status_adapter.py",
            "scout_projection": str(scout_projection_path.relative_to(DBA_ROOT)),
            "live_dependency_audit": str(live_audit_path.relative_to(DBA_ROOT)),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--demo", action="store_true")
    parser.add_argument("--as-of")
    args = parser.parse_args()
    as_of = args.as_of or (
        "2026-08-29T00:30:00+08:00"
        if args.demo
        else datetime.now().astimezone().isoformat(timespec="seconds")
    )
    output_dir = args.output_dir.resolve()
    snapshot_name = "weekly-snapshot-2026-W35.json" if args.demo else "latest.json"
    snapshot = WeeklyCoordinator().run(load_context(as_of), output_dir, snapshot_name)
    print(f"DBA_WEEKLY_COCKPIT_STATUS={snapshot['overall_status']}")
    print(f"SNAPSHOT={output_dir / snapshot_name}")
    print(f"DASHBOARD={output_dir / 'dashboard.html'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
