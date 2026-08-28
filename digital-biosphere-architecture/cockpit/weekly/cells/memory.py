"""Describe temporal change only when a previous snapshot exists."""

from __future__ import annotations

from typing import Any

from . import WeeklyCell, make_result, source_value


class MemoryCell(WeeklyCell):
    cell_id = "MEMORY_CELL"

    def _run(self, context: dict[str, Any]):
        previous = source_value(context, "previous_snapshot")
        discoveries = context.get("discovery_records", [])
        live_mode = context.get("snapshot_mode") == "LIVE_READ_ONLY_OBSERVATION_PILOT"
        artifact = context.get("artifact_memory_metadata", {})
        if not previous:
            artifact_status = artifact.get("memory_status")
            memory = {
                "status": artifact_status or "NOT_ASSESSED_NO_PREVIOUS_SNAPSHOT",
                "previous_snapshot_reference": None,
                "trend_claim_allowed": False,
                "note_zh": (
                    "没有符合条件的上一轮实时制品，尚不能形成跨运行变化判断。"
                    if live_mode else "首次快照，尚不能判断这些信号是否相对于上周新增。"
                ),
                "PREVIOUS_LIVE_ARTIFACT_LOADED": False,
                "MEMORY_COMPARISON_EXECUTED": False,
                "ARTIFACT_FROM_CURRENT_RUN_REJECTED": artifact.get(
                    "ARTIFACT_FROM_CURRENT_RUN_REJECTED", True if live_mode else None
                ),
                "FAILED_OR_EXPIRED_ARTIFACT_REJECTED": artifact.get(
                    "FAILED_OR_EXPIRED_ARTIFACT_REJECTED", True if live_mode else None
                ),
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
            current_findings = context.get("findings", [])
            comparison = self.compare_findings(previous.get("findings", []), current_findings)
            memory = {
                "status": "COMPARISON_AVAILABLE",
                "previous_snapshot_reference": previous.get("snapshot_id", "UNKNOWN"),
                "trend_claim_allowed": True,
                "note_zh": "已按 finding_id、project_id 与 finding_type 比较上一轮实时制品。",
                "PREVIOUS_LIVE_ARTIFACT_LOADED": True,
                "MEMORY_COMPARISON_EXECUTED": True,
                "ARTIFACT_FROM_CURRENT_RUN_REJECTED": artifact.get(
                    "ARTIFACT_FROM_CURRENT_RUN_REJECTED", True
                ),
                "FAILED_OR_EXPIRED_ARTIFACT_REJECTED": artifact.get(
                    "FAILED_OR_EXPIRED_ARTIFACT_REJECTED", True
                ),
                "comparison": comparison,
            }
            changes = {
                "improved": comparison["CLOSED"],
                "worsened": comparison["NEW"] + comparison["REAPPEARED"],
                "unknown": comparison["CONTINUING"],
                "observed_this_week": comparison["NEW"] + comparison["CONTINUING"] + comparison["REAPPEARED"],
            }
            status = "PASS"
        return make_result(
            self.cell_id,
            status,
            "Memory preserved temporal boundaries without inventing week-over-week change.",
            outputs={"memory": memory, "changes": changes},
        )

    @staticmethod
    def compare_findings(
        previous_findings: list[dict[str, Any]], current_findings: list[dict[str, Any]]
    ) -> dict[str, list[str]]:
        def identity(item: dict[str, Any]) -> tuple[str, str, str] | None:
            values = (
                item.get("finding_id"), item.get("project_id"), item.get("finding_type")
            )
            return values if all(isinstance(value, str) and value for value in values) else None

        previous = {key: item for item in previous_findings if (key := identity(item))}
        current = {key: item for item in current_findings if (key := identity(item))}
        continuing = sorted(" | ".join(key) for key in previous.keys() & current.keys())
        new = sorted(" | ".join(key) for key in current.keys() - previous.keys())
        closed = sorted(" | ".join(key) for key in previous.keys() - current.keys())
        reappeared = sorted(
            " | ".join(key)
            for key in previous.keys() & current.keys()
            if previous[key].get("lifecycle_status") == "CLOSED"
        )
        continuing = [item for item in continuing if item not in reappeared]
        return {
            "NEW": new,
            "CONTINUING": continuing,
            "CLOSED": closed,
            "REAPPEARED": reappeared,
        }
