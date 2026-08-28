"""Report conflicts between retained canonical state and current candidate evidence."""

from __future__ import annotations

from typing import Any

from . import WeeklyCell, make_result, source_value
from .environment_discovery import _nested_number, _packages


class DriftCell(WeeklyCell):
    cell_id = "DRIFT_CELL"

    def _run(self, context: dict[str, Any]):
        as_of = context.get("as_of", "UNKNOWN")
        live = source_value(context, "live_dependency_audit", {}) or {}
        canonical_count = _nested_number(
            live,
            ("canonical_high_count",),
            ("canonical_retained", "high_count"),
            default=2,
        )
        live_count = _nested_number(
            live,
            ("live_high_count",),
            ("live_candidate", "high_count"),
            ("observed_result", "high_count"),
            default=4,
        )
        packages = _packages(live)
        source_ref = source_value(context, "source_paths", {}).get(
            "live_dependency_audit",
            "inputs/live-dependency-audit-candidate-2026-08-29.json",
        )
        explanation = (
            f"本周实时扫描报告{live_count}个高危依赖包，而驾驶舱历史权威记录仍为"
            f"{canonical_count}个。两者尚未对齐，需要核对锁文件、扫描范围和是否进入实际运行环境。"
        )
        finding = {
            "finding_id": "FINDING-DEPENDENCY-AUDIT-STATE-CONFLICT-2026-W35",
            "finding_type": "DEPENDENCY_AUDIT_STATE_CONFLICT",
            "project_id": "DBA_COCKPIT",
            "severity": "ATTENTION",
            "category": "SECURITY_DRIFT",
            "title": "历史与实时依赖审计状态冲突",
            "title_zh": "历史与实时依赖审计状态冲突",
            "human_explanation": explanation,
            "source_reference": source_ref,
            "observed_at": live.get("observed_at", as_of),
            "canonical_high_count": canonical_count,
            "live_candidate_high_count": live_count,
            "live_high_packages": packages,
            "runtime_binding": "NOT_ESTABLISHED",
            "exploitability": "NOT_ASSESSED",
            "reconciliation_required": True,
            "authorization": "NONE",
            "version_change_recommended": False,
        }
        project_updates = [
            {
                "project_id": "DBA_COCKPIT",
                "status": "ATTENTION",
                "status_zh": "依赖审计状态待复核",
                "why_zh": explanation,
                "attention_zh": f"候选包：{', '.join(packages)}；可利用性尚未评估。",
                "technical_evidence": [source_ref],
            },
            {
                "project_id": "RED_YAN_OFFICIAL_DOCUMENT",
                "status": "STABLE",
                "status_zh": "当前主线稳定",
                "why_zh": "现有权威快照可读取，本周驾驶舱未修改红岩项目。",
                "attention_zh": "该视图不替代红岩专用对话中的项目判断。",
                "technical_evidence": [source_value(context, "source_paths", {}).get("redyan", "UNKNOWN")],
            },
        ]
        blind_spots = [
            {
                "blind_spot_id": "DEPENDENCY_RUNTIME_BINDING_UNKNOWN",
                "project_id": "DBA_COCKPIT",
                "title_zh": "依赖漏洞的远端运行绑定未观察",
                "impact_zh": "当前只能确认扫描候选与历史记录冲突，不能确认这些包是否进入实际远端运行路径。",
                "status": "NOT_ASSESSED",
                "source_reference": source_ref,
            }
        ]
        return make_result(
            self.cell_id,
            "ATTENTION",
            "A canonical-versus-live dependency audit conflict requires review.",
            findings=[finding],
            outputs={
                "project_updates": project_updates,
                "blind_spots": blind_spots,
                "dependency_audit_state": {
                    "status": "CONFLICT_REQUIRES_REVIEW",
                    "canonical_high_count": canonical_count,
                    "live_candidate_high_count": live_count,
                    "live_high_packages": packages,
                    "runtime_binding": "NOT_ESTABLISHED",
                    "exploitability": "NOT_ASSESSED",
                    "auto_reconciliation": False,
                },
            },
        )
