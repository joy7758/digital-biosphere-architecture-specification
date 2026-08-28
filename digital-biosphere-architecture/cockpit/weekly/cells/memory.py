"""Compare weekly snapshots without overwriting historical evidence."""

from __future__ import annotations

from typing import Any

try:
    from cockpit.weekly.cells import WeeklyCell, make_result, source_value
except ModuleNotFoundError:
    from cells import WeeklyCell, make_result, source_value


class MemoryCell(WeeklyCell):
    cell_id = "MEMORY_CELL"

    def _run(self, context: dict[str, Any]):
        previous = source_value(context, "previous_snapshot")
        if not previous:
            context["memory_summary"] = {
                "status": "NOT_ASSESSED_NO_PREVIOUS_SNAPSHOT",
                "new": [], "continuing": [], "closed": [], "reappeared": [],
            }
            return make_result(
                self.cell_id,
                "NOT_ASSESSED",
                "没有上一周快照；首次运行不伪造变化趋势。",
                observations=[{"comparison_status": "NOT_ASSESSED_NO_PREVIOUS_SNAPSHOT"}],
                metadata={"history_overwritten": False},
            )
        observation = {
            "comparison_status": "COMPARED",
            "previous_snapshot_id": previous.get("snapshot_id", "UNKNOWN"),
            "current_snapshot_id": context.get("snapshot_id", "PENDING"),
            "history_overwritten": False,
        }
        context["memory_summary"] = {
            "status": "COMPARED",
            "new": [], "continuing": [], "closed": [], "reappeared": [],
            "previous_snapshot_id": observation["previous_snapshot_id"],
        }
        return make_result(
            self.cell_id,
            "PASS",
            "已建立周间引用关系；旧快照保持不可覆盖。",
            observations=[observation],
        )
