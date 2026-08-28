"""Prepare bounded human handoffs; never emit execution commands."""

from __future__ import annotations

from typing import Any

try:
    from cockpit.weekly.cells import WeeklyCell, make_result
except ModuleNotFoundError:
    from cells import WeeklyCell, make_result


class HandoffCell(WeeklyCell):
    cell_id = "HANDOFF_CELL"

    def _run(self, context: dict[str, Any]):
        packets = [
            {
                "handoff_id": "handoff:dba-dependency-review",
                "project_id": "digital-biosphere-architecture-specification",
                "recipient_role": "human-maintainer",
                "decision_needed": "是否安排独立依赖风险复核",
                "evidence_references": ["reconciliation/current-dependency-audit"],
                "suggested_next_review": "DEPENDENCY_REVIEW",
                "execution_commands": [],
                "authority": "NONE",
            },
            {
                "handoff_id": "handoff:scout-refresh",
                "project_id": "titmac-scout",
                "recipient_role": "human-maintainer",
                "decision_needed": "是否授权刷新只读 Scout 快照",
                "evidence_references": ["cockpit/source-registry.json"],
                "suggested_next_review": "DISCOVERY_SOURCE_REFRESH",
                "execution_commands": [],
                "authority": "NONE",
            },
        ]
        context["handoff_packets"] = packets
        return make_result(
            self.cell_id,
            "PASS",
            "生成 2 个仅供人工判断的交接包；不含执行命令。",
            handoffs=packets,
            observations=packets,
        )
