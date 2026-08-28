"""Interpret bounded quality evidence for registered projects."""

from __future__ import annotations

from typing import Any

from . import WeeklyCell, make_result, source_value


class QualityCell(WeeklyCell):
    cell_id = "QUALITY_CELL"

    def _run(self, context: dict[str, Any]):
        source_ref = source_value(context, "source_paths", {}).get("convergence", "UNKNOWN")
        updates = [
            {
                "project_id": "DIGITAL_CELL_DEMO",
                "status": "STABLE",
                "status_zh": "参考演示稳定",
                "why_zh": "冻结参考演示及其既有验证记录可读取；本周未授权新增执行。",
                "attention_zh": "该状态不构成生产就绪或认证。",
                "technical_evidence": [source_ref],
            }
        ]
        return make_result(
            self.cell_id,
            "PASS",
            "Bounded quality evidence was interpreted without a composite score.",
            outputs={"project_updates": updates},
        )
