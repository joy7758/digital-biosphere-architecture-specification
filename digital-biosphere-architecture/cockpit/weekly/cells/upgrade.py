"""Keep stale or rejected component signals out of upgrade recommendations."""

from __future__ import annotations

from typing import Any

from . import WeeklyCell, make_result


class UpgradeCell(WeeklyCell):
    cell_id = "UPGRADE_CELL"

    def _run(self, context: dict[str, Any]):
        rejected = context.get("rejected_observations", [])
        component_rejected = any(
            item.get("observation", {}).get("kind") == "COMPONENT_STATUS_SIGNAL"
            for item in rejected
        )
        updates = []
        if component_rejected:
            updates.append(
                {
                    "project_id": "TITMAS_SUPPORTING_LAYER",
                    "status": "NOT_ASSESSED",
                    "status_zh": "升级状态未评估",
                    "why_zh": "组件状态来源已过期，不能转化为本周升级建议。",
                    "attention_zh": "需要新的只读证据后再评估。",
                }
            )
        return make_result(
            self.cell_id,
            "NOT_ASSESSED" if component_rejected else "PASS",
            "Rejected or stale signals did not become upgrade recommendations.",
            outputs={
                "project_updates": updates,
                "upgrade_recommendations": [],
            },
        )
