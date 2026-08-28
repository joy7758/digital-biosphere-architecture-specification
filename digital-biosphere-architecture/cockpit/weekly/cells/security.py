"""Report bounded security observations without remediation authority."""

from __future__ import annotations

from typing import Any

try:
    from cockpit.weekly.cells import WeeklyCell, make_result
except ModuleNotFoundError:
    from cells import WeeklyCell, make_result


class SecurityCell(WeeklyCell):
    cell_id = "SECURITY_CELL"

    def _run(self, context: dict[str, Any]):
        finding = {
            "finding_id": "security:dba-nanoid-via-postcss",
            "project_id": "digital-biosphere-architecture-specification",
            "severity": "ATTENTION",
            "category": "BUILD_DEPENDENCY",
            "title": "文档构建依赖保留 2 个 high 级发现",
            "human_explanation": "现有核验记录显示风险位于构建/开发依赖链；运行时可利用性尚未评估。",
            "source_reference": "reconciliation/current-dependency-audit",
            "observed_at": context.get("as_of", "UNKNOWN"),
            "runtime_binding": "NOT_ESTABLISHED",
            "exploitability": "NOT_ASSESSED",
            "authorization": "NONE",
        }
        return make_result(
            self.cell_id,
            "ATTENTION",
            "安全 Cell 保留已知依赖发现，不自动修复、不创建 PR。",
            findings=[finding],
        )
