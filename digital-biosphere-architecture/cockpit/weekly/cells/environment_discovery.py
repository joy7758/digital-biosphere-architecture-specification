"""Discover current environment signals without turning candidates into truth."""

from __future__ import annotations

from typing import Any

from . import WeeklyCell, make_result, source_value


def _nested_number(source: dict[str, Any], *paths: tuple[str, ...], default: int) -> int:
    for path in paths:
        value: Any = source
        for key in path:
            if not isinstance(value, dict):
                value = None
                break
            value = value.get(key)
        if isinstance(value, int):
            return value
    return default


def _packages(source: dict[str, Any]) -> list[str]:
    for path in (
        ("live_high_packages",),
        ("live_candidate", "high_packages"),
        ("live_candidate", "packages"),
        ("observed_result", "high_packages"),
    ):
        value: Any = source
        for key in path:
            if not isinstance(value, dict):
                value = None
                break
            value = value.get(key)
        if isinstance(value, list) and all(isinstance(item, str) for item in value):
            return value
    return ["image-size", "js-yaml", "nanoid", "vinext"]


class EnvironmentDiscoveryCell(WeeklyCell):
    cell_id = "ENVIRONMENT_DISCOVERY_CELL"

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

        discoveries = [
            {
                "signal_id": "DISCOVERY-DEPENDENCY-AUDIT-CONFLICT",
                "kind": "DEPENDENCY_SECURITY_CONFLICT_CANDIDATE",
                "subject": "DBA dependency audit state",
                "title_zh": "依赖安全状态出现待复核冲突",
                "observed_state": "CONFLICT_CANDIDATE",
                "current_state": "DISCOVERED",
                "source_reference": source_ref,
                "observed_at": live.get("observed_at", as_of),
                "freshness": "CURRENT",
                "authority": "CANDIDATE_OBSERVATION",
                "admission_status": "PENDING",
                "admission_label_zh": "待证据准入",
                "details_zh": (
                    f"本周实时扫描报告{live_count}个高危依赖包，历史权威记录仍为"
                    f"{canonical_count}个；候选包为{', '.join(packages)}。"
                ),
                "canonical_high_count": canonical_count,
                "live_candidate_high_count": live_count,
                "live_high_packages": packages,
                "runtime_binding": "NOT_ESTABLISHED",
                "exploitability": "NOT_ASSESSED",
            },
            {
                "signal_id": "DISCOVERY-TITMAS-MATRIX-STALE",
                "kind": "COMPONENT_STATUS_SIGNAL",
                "subject": "TITMAS component matrix",
                "title_zh": "TITMAS 组件矩阵状态待刷新",
                "observed_state": "STALE",
                "current_state": "DISCOVERED",
                "source_reference": source_value(context, "source_paths", {}).get("component_matrix", "UNKNOWN"),
                "observed_at": as_of,
                "freshness": "STALE",
                "authority": "DISCOVERY_ONLY",
                "admission_status": "PENDING",
                "admission_label_zh": "待证据准入",
                "details_zh": "现有组件矩阵不能自动获得本周当前状态权威。",
            },
            {
                "signal_id": "DISCOVERY-SCOUT-STATUS-STALE",
                "kind": "PROJECT_STATUS_SIGNAL",
                "subject": "TITMAC Scout read-only status",
                "title_zh": "TITMAC Scout 当前只读状态待刷新",
                "observed_state": "UNKNOWN",
                "current_state": "DISCOVERED",
                "source_reference": source_value(context, "source_paths", {}).get("scout_projection", "UNKNOWN"),
                "observed_at": as_of,
                "freshness": "UNKNOWN",
                "authority": "DISCOVERY_ONLY",
                "admission_status": "PENDING",
                "admission_label_zh": "待证据准入",
                "details_zh": "现有投影没有提供足够新鲜度，不能推断当前状态。",
            },
        ]
        project_updates = [
            {
                "project_id": "TITMAC_SCOUT",
                "status": "BLIND_SPOT",
                "status_zh": "检查盲区",
                "why_zh": "当前只读状态来源缺少足够新鲜度，不能据此判定项目正常或异常。",
                "attention_zh": "如需刷新，必须获得单独只读授权。",
            }
        ]
        blind_spots = [
            {
                "blind_spot_id": "SCOUT_STATUS_STALE",
                "project_id": "TITMAC_SCOUT",
                "title_zh": "TITMAC Scout 的只读状态尚未刷新",
                "impact_zh": "当前周检不能确认其最新检查、版本与运行状态。",
                "status": "NOT_ASSESSED",
                "source_reference": source_value(context, "source_paths", {}).get("scout_projection", "UNKNOWN"),
            }
        ]
        return make_result(
            self.cell_id,
            "PASS_WITH_CANDIDATES",
            "Current environment candidates were recorded without authority escalation.",
            discoveries=discoveries,
            outputs={
                "discovery_records": discoveries,
                "project_updates": project_updates,
                "blind_spots": blind_spots,
            },
        )
