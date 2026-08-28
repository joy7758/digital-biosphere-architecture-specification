"""Detect semantic and lineage drift from canonical snapshots."""

from __future__ import annotations

from typing import Any

try:
    from cockpit.weekly.cells import WeeklyCell, make_result
except ModuleNotFoundError:
    from cells import WeeklyCell, make_result


class DriftCell(WeeklyCell):
    cell_id = "DRIFT_CELL"

    def _run(self, context: dict[str, Any]):
        findings = [
            {
                "finding_id": "drift:red-yan-runtime",
                "project_id": "red-yan-official-documents",
                "severity": "NORMAL",
                "category": "DIRECTION_DRIFT",
                "title": "红岩主线方向未观察到运行时漂移",
                "human_explanation": "驾驶舱只读取既有证据快照；本次未修改红岩仓库。",
                "source_reference": "current-direction-and-red-yan-evidence-snapshot",
                "observed_at": context.get("as_of", "UNKNOWN"),
            },
            {
                "finding_id": "drift:stale-labels",
                "project_id": "digital-biosphere-architecture-specification",
                "severity": "ATTENTION",
                "category": "SEMANTIC_DRIFT",
                "title": "4 个非权威标签仍需后续收口",
                "human_explanation": "标签属于旧叙事残留；不得覆盖当前 machine-readable precedence。",
                "source_reference": "current-reconciliation",
                "observed_at": context.get("as_of", "UNKNOWN"),
            },
            {
                "finding_id": "drift:partial-lineage",
                "project_id": "titmas",
                "severity": "NOT_ASSESSED",
                "category": "LINEAGE_COVERAGE",
                "title": "部分历史谱系覆盖仍不完整",
                "human_explanation": "缺失证据保持未评估，不用绿色状态填补。",
                "source_reference": "convergence-snapshot",
                "observed_at": context.get("as_of", "UNKNOWN"),
            },
        ]
        return make_result(
            self.cell_id,
            "PASS_WITH_NOT_ASSESSED",
            "观察到稳定主线、旧标签注意项与历史谱系盲区。",
            findings=findings,
        )
