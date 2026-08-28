"""Assess upgrade signals without recommending unverified version changes."""

from __future__ import annotations

from typing import Any

try:
    from cockpit.weekly.cells import WeeklyCell, make_result, source_value
except ModuleNotFoundError:
    from cells import WeeklyCell, make_result, source_value


class UpgradeCell(WeeklyCell):
    cell_id = "UPGRADE_CELL"

    def _run(self, context: dict[str, Any]):
        matrix = source_value(context, "titmas_component_matrix", {}) or {}
        finding = {
            "finding_id": "upgrade:titmas-matrix-refresh-required",
            "project_id": "titmas",
            "severity": "NOT_ASSESSED",
            "category": "UPGRADE_DISCOVERY",
            "title": "TITMAS 组件版本信号需要刷新",
            "human_explanation": "组件矩阵新鲜度不足，不能据此判断当前版本或升级优先级。",
            "source_reference": "titmas-component-matrix",
            "observed_at": matrix.get("observed_at", matrix.get("generated_at", "UNKNOWN")),
            "version_change_recommended": False,
            "authorization": "NONE",
        }
        return make_result(
            self.cell_id,
            "NOT_ASSESSED",
            "没有足够的新鲜版本证据；升级状态保持未评估。",
            findings=[finding],
        )
