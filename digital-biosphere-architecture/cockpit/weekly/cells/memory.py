"""Describe temporal change only when a previous snapshot exists."""

from __future__ import annotations

from typing import Any

from . import WeeklyCell, make_result, source_value


class MemoryCell(WeeklyCell):
    cell_id = "MEMORY_CELL"

    def _run(self, context: dict[str, Any]):
        previous = source_value(context, "previous_snapshot")
        discoveries = context.get("discovery_records", [])
        if not previous:
            memory = {
                "status": "NOT_ASSESSED_NO_PREVIOUS_SNAPSHOT",
                "previous_snapshot_reference": None,
                "trend_claim_allowed": False,
                "note_zh": "首次快照，尚不能判断这些信号是否相对于上周新增。",
            }
            changes = {
                "improved": [],
                "worsened": [],
                "unknown": ["首次快照，尚不能判断这些信号是否相对于上周新增。"],
                "observed_this_week": [
                    item.get("title_zh", item.get("subject", "本周信号"))
                    for item in discoveries
                    if item.get("freshness") == "CURRENT"
                ],
            }
            status = "NOT_ASSESSED"
        else:
            memory = {
                "status": "COMPARISON_AVAILABLE",
                "previous_snapshot_reference": previous.get("snapshot_id", "UNKNOWN"),
                "trend_claim_allowed": True,
                "note_zh": "已登记上一期快照引用；本原型仍不自动生成领域趋势判断。",
            }
            changes = {
                "improved": [],
                "worsened": [],
                "unknown": ["已有上一期引用，但没有获授权的领域变化解释。"],
                "observed_this_week": [],
            }
            status = "PASS_WITH_NOT_ASSESSED"
        return make_result(
            self.cell_id,
            status,
            "Memory preserved temporal boundaries without inventing week-over-week change.",
            outputs={"memory": memory, "changes": changes},
        )
