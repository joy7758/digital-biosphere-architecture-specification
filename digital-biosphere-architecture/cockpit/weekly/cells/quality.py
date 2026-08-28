"""Project existing reconciliation quality facts into a read-only view."""

from __future__ import annotations

from typing import Any

try:
    from cockpit.weekly.cells import WeeklyCell, make_result, source_value
except ModuleNotFoundError:
    from cells import WeeklyCell, make_result, source_value


class QualityCell(WeeklyCell):
    cell_id = "QUALITY_CELL"

    def _run(self, context: dict[str, Any]):
        reconciliation = source_value(context, "reconciliation", {}) or {}
        status = reconciliation.get("overall_status", reconciliation.get("status", "PASS"))
        observation = {
            "observation_id": "quality:dba-reconciliation",
            "project_id": "digital-biosphere-architecture-specification",
            "observed_state": status,
            "source_reference": "machine-readable-reconciliation",
            "observed_at": reconciliation.get("generated_at", context.get("as_of", "UNKNOWN")),
            "interpretation": "既有一致性状态的只读投影，不是新的验收。",
        }
        return make_result(
            self.cell_id,
            "PASS" if str(status).startswith("PASS") else "ATTENTION",
            "复用既有 reconciliation 事实，未创建第二套质量真相。",
            observations=[observation],
        )
