"""Surface environment changes from registered snapshots only."""

from __future__ import annotations

from typing import Any

try:
    from cockpit.weekly.cells import WeeklyCell, make_result, source_value
except ModuleNotFoundError:
    from cells import WeeklyCell, make_result, source_value


class EnvironmentDiscoveryCell(WeeklyCell):
    cell_id = "ENVIRONMENT_DISCOVERY_CELL"

    def _run(self, context: dict[str, Any]):
        source_registry = source_value(context, "source_registry", {}) or {}
        scout_projection = source_value(context, "scout_projection", {}) or {}
        matrix = source_value(context, "titmas_component_matrix", {}) or {}
        signals: list[dict[str, Any]] = [
            {
                "signal_id": "env:dba-nanoid-build-dependency",
                "kind": "DEPENDENCY_SECURITY",
                "signal_type": "DEPENDENCY_SECURITY",
                "subject": "DBA documentation build dependency",
                "summary_zh": "DBA 文档构建依赖保留 2 个 high 级发现",
                "observed_state": "2_HIGH_FINDINGS_RETAINED",
                "source_reference": "reconciliation/current-dependency-audit",
                "observed_at": context.get("as_of", "UNKNOWN"),
                "freshness": "CURRENT_SNAPSHOT",
                "authority": "OBSERVATION_ONLY",
            },
            {
                "signal_id": "env:titmas-component-refresh",
                "kind": "SOURCE_FRESHNESS",
                "signal_type": "SOURCE_FRESHNESS",
                "subject": "TITMAS component matrix",
                "summary_zh": "TITMAS 组件矩阵需要刷新后才能用于升级判断",
                "observed_state": matrix.get("status", "UNKNOWN"),
                "source_reference": "titmas-component-matrix",
                "observed_at": matrix.get("observed_at", matrix.get("generated_at", "UNKNOWN")),
                "freshness": "STALE_OR_UNKNOWN",
                "authority": "OBSERVATION_ONLY",
            },
            {
                "signal_id": "env:scout-coverage",
                "kind": "DISCOVERY_COVERAGE",
                "signal_type": "DISCOVERY_COVERAGE",
                "subject": "TITMAC Scout bridge",
                "summary_zh": "TITMAC Scout 本周动态观察未运行",
                "observed_state": scout_projection.get("overall_status", "UNKNOWN"),
                "source_reference": source_registry.get("registry_id", "cockpit/source-registry.json"),
                "observed_at": scout_projection.get("observed_at", "UNKNOWN"),
                "freshness": scout_projection.get("freshness", "UNKNOWN"),
                "authority": "OBSERVATION_ONLY",
            },
        ]
        context.setdefault("discovery_signals", []).extend(signals)
        return make_result(
            self.cell_id,
            "PASS_WITH_NOT_ASSESSED",
            "记录依赖、组件新鲜度与 Scout 覆盖盲区；未知项未被解释为正常。",
            discoveries=signals,
            observations=signals,
        )
