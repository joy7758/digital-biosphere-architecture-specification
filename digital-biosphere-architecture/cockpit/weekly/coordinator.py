"""Failure-isolated coordinator for the weekly cockpit."""

from __future__ import annotations

import time
from pathlib import Path
from typing import Any

from contracts import CellResult, canonical_json
from cells.drift import DriftCell
from cells.environment_discovery import EnvironmentDiscoveryCell
from cells.evidence_admission import EvidenceAdmissionCell
from cells.handoff import HandoffCell
from cells.human_view import HumanViewCell
from cells.memory import MemoryCell
from cells.project_discovery import ProjectDiscoveryCell
from cells.quality import QualityCell
from cells.relationship_discovery import RelationshipDiscoveryCell
from cells.security import SecurityCell
from cells.upgrade import UpgradeCell


WORKER_CELLS = [
    ProjectDiscoveryCell,
    EnvironmentDiscoveryCell,
    RelationshipDiscoveryCell,
    EvidenceAdmissionCell,
    SecurityCell,
    UpgradeCell,
    QualityCell,
    DriftCell,
    MemoryCell,
    HandoffCell,
]
DISCOVERY_IDS = {
    "PROJECT_DISCOVERY_CELL",
    "ENVIRONMENT_DISCOVERY_CELL",
    "RELATIONSHIP_DISCOVERY_CELL",
}


class WeeklyCoordinator:
    cell_id = "WEEKLY_COORDINATOR_CELL"

    def __init__(self, cell_types: list[type] | None = None) -> None:
        self.cell_types = cell_types or WORKER_CELLS

    def run(
        self, context: dict[str, Any], output_dir: Path, snapshot_name: str = "latest.json"
    ) -> dict[str, Any]:
        output_dir.mkdir(parents=True, exist_ok=True)
        results: list[CellResult] = []
        for cell_type in self.cell_types:
            started = time.perf_counter()
            cell = cell_type()
            try:
                result = cell.run(context)
            except Exception as exc:
                result = CellResult(
                    cell_id=cell.cell_id,
                    status="NOT_ASSESSED",
                    reason_code="CELL_EXECUTION_FAILED",
                    exception_summary=f"{type(exc).__name__}: {str(exc)[:180]}",
                )
            result.duration_ms = round((time.perf_counter() - started) * 1000)
            results.append(result)

        discovery_results = [item for item in results if item.cell_id in DISCOVERY_IDS]
        discovery_unavailable = (
            len(discovery_results) == 3
            and all(item.status == "NOT_ASSESSED" for item in discovery_results)
        )
        snapshot = self._snapshot(context, results, discovery_unavailable)
        human_result = CellResult("HUMAN_VIEW_CELL", "PASS")
        coordinator_result = CellResult(
            self.cell_id,
            "NOT_ASSESSED" if discovery_unavailable else "PASS",
            reason_code="DISCOVERY_UNAVAILABLE" if discovery_unavailable else None,
        )
        snapshot["cell_runs"] = [
            item.to_dict() for item in results + [human_result, coordinator_result]
        ]
        try:
            HumanViewCell().render(snapshot, output_dir)
        except Exception as exc:
            human_result.status = "NOT_ASSESSED"
            human_result.reason_code = "HUMAN_VIEW_GENERATION_FAILED"
            human_result.exception_summary = f"{type(exc).__name__}: {str(exc)[:180]}"
            snapshot["cell_runs"][-2] = human_result.to_dict()
            snapshot["overall_status"] = "PASS_WITH_NOT_ASSESSED"

        (output_dir / snapshot_name).write_text(canonical_json(snapshot), encoding="utf-8")
        (output_dir / "cell-run-summary.json").write_text(
            canonical_json({
                "snapshot_id": snapshot["snapshot_id"],
                "overall_status": snapshot["overall_status"],
                "cell_runs": snapshot["cell_runs"],
            }),
            encoding="utf-8",
        )
        return snapshot

    def _snapshot(
        self,
        context: dict[str, Any],
        results: list[CellResult],
        discovery_unavailable: bool,
    ) -> dict[str, Any]:
        projects = self._projects(context)
        findings = [finding for result in results for finding in result.findings]
        context["findings"] = findings
        signals = context.get("discovery_signals", [])
        candidates = context.get("project_candidates", [])
        open_candidate = next(
            (item for item in candidates if item["discovery_status"] == "DISCOVERED"),
            None,
        )
        discoveries = [
            {
                "title_zh": item["summary_zh"],
                "type": item["signal_type"],
                "status": item.get("freshness", "DISCOVERED"),
                "source_reference": item.get("source_reference"),
            }
            for item in signals
        ]
        if open_candidate:
            discoveries.append({
                "title_zh": f"待人工确认是否监测：{open_candidate['display_name_zh']}",
                "type": "PROJECT_CANDIDATE",
                "status": "DISCOVERED",
                "source_reference": open_candidate["canonical_source_ref"],
            })
        decisions = [
            {
                "decision_id": "DBA-DECISION-001",
                "title_zh": "是否启动依赖安全专项评审",
                "why_zh": "DBA 现有依赖审计记录了 2 个 high，但远端绑定和可利用性均未评估。",
                "owner_conversation": "DBA 专用对话",
                "authorization": "NONE",
            },
            {
                "decision_id": "DBA-DECISION-002",
                "title_zh": "是否把 OpenBao 组件候选纳入正式监测",
                "why_zh": "它只来自历史组件采用矩阵，版本与安全事实必须先刷新。",
                "owner_conversation": "DBA 专用对话",
                "authorization": "NONE",
            },
        ]
        changes = {
            "improved": ["红岩旧 /srv 控制指针已纠正为兼容别名，当前运行时无漂移。"],
            "worsened": [],
            "unknown": ["TITMAC Scout 本周未执行动态刷新，最新外部状态不可据此推断。"],
        }
        blind_spots = [
            {
                "title_zh": "依赖漏洞的远端运行绑定未观察",
                "status": "NOT_ASSESSED",
                "impact_zh": "不能判断该构建与开发工具链问题是否可被远端请求利用。",
            },
            {
                "title_zh": "TITMAC Scout 本周动态观察未运行",
                "status": "STALE",
                "impact_zh": "保留已存投影，但不把它当作本周实时状态。",
            },
        ]
        counts = {
            "total": len(projects),
            "stable": sum(item["status"] == "STABLE" for item in projects),
            "attention": sum(item["status"] == "ATTENTION" for item in projects),
            "blind_spot": sum(item["status"] == "BLIND_SPOT" for item in projects),
        }
        weekly_sentence = (
            f"{counts['total']} 个项目中，{counts['stable']} 个状态稳定，"
            f"{counts['attention']} 个需要关注，{counts['blind_spot']} 个存在检查盲区。"
        )
        memory = context.get("memory_summary", {
            "status": "NOT_ASSESSED_NO_PREVIOUS_SNAPSHOT",
            "new": [], "continuing": [], "closed": [], "reappeared": [],
        })
        overall = (
            "DISCOVERY_UNAVAILABLE"
            if discovery_unavailable
            else "PASS_WITH_NOT_ASSESSED"
            if any(item.status == "NOT_ASSESSED" for item in results) or blind_spots
            else "PASS_WITH_FINDINGS"
        )
        return {
            "schema_version": "0.1",
            "snapshot_id": "DBA-WEEKLY-2026-W35-CANDIDATE",
            "week": "2026-W35",
            "observed_at": context["as_of"],
            "overall_status": overall,
            "mode": "PROTOTYPE_READ_ONLY_CANDIDATE",
            "weekly_sentence_zh": weekly_sentence,
            "counts": counts,
            "projects": projects,
            "discoveries": discoveries,
            "decisions": decisions,
            "changes": changes,
            "blind_spots": blind_spots,
            "findings": findings,
            "handoff_packets": context.get("handoff_packets", []),
            "memory": memory,
            "logical_cells": [
                {
                    "cell_id": item["cell_id"],
                    "display_name_zh": item["display_name_zh"],
                    "niche_zh": item["niche_zh"],
                }
                for item in context["cell_registry"]["cells"]
            ],
            "preset_queries": {
                "本周最需要我处理的是什么？": decisions[0]["title_zh"],
                "哪个项目状态变差了？": "本周没有足够证据确认项目状态变差。",
                "哪些问题连续多周未解决？": "第一周没有历史快照，暂时无法判断连续多周问题。",
                "有哪些升级值得评审？": "组件采用矩阵已过期；应先刷新版本与安全事实，再决定是否评审升级。",
                "哪些检查没有成功运行？": "TITMAC Scout 本周动态观察未运行；依赖漏洞远端绑定未评估。",
                "发现了哪些新项目？": "发现 OpenBao 组件候选，尚未获准纳入正式监测。",
                "发现了哪些跨项目关系？": "红岩运行调查证据由红岩产品线产生，DBA 只接收摘要并登记交接。",
            },
            "source_references": context["source_paths"],
            "boundaries": {
                "read_only": True,
                "view_not_truth": True,
                "discovery_ne_admission": True,
                "discovery_ne_recommendation": True,
                "discovery_ne_authorization": True,
                "discovery_ne_remediation": True,
                "new_truth_source": False,
                "new_control_plane": False,
                "auto_fix": False,
                "auto_pr": False,
                "auto_merge": False,
                "auto_deploy": False,
            },
            "cell_runs": [],
        }

    @staticmethod
    def _projects(context: dict[str, Any]) -> list[dict[str, Any]]:
        redyan = context["redyan"]
        dependency = redyan["dependency_finding"]
        return [
            {
                "project_id": "RED_YAN_OFFICIAL_DOCUMENT",
                "display_name_zh": "红岩公文",
                "status": "STABLE",
                "status_zh": "受控试点运行正常",
                "why_zh": "当前运行提交匹配，运行时无漂移，主控制指针有效。",
                "attention_zh": "品牌部署谱系仍是部分谱系，4 个旧容器标签不具权威性。",
                "impact_zh": "不阻塞当前受控试点；OfficeCLI 当前运行阻断为 0。",
                "owner_conversation": "红岩公文专用对话",
                "technical_evidence": [
                    redyan["runtime_identity"]["observed_commit"],
                    redyan["current_pointers"]["canonical_user_pointer"]["classification"],
                    redyan["brand_deployment_lineage"]["classification"],
                    f"OFFICECLI_PROMOTION_BLOCKERS={redyan['officecli_p1']['candidate_promotion_blocker_count']}",
                ],
            },
            {
                "project_id": "DBA_COCKPIT",
                "display_name_zh": "DBA 驾驶舱",
                "status": "ATTENTION",
                "status_zh": "方向清晰，依赖安全待评估",
                "why_zh": "红岩是唯一工程主线，驾驶舱只负责项目群治理。",
                "attention_zh": "依赖审计记录 2 个 high，可利用性尚未评估。",
                "impact_zh": "属于构建与开发工具链；未观察到远端运行绑定。",
                "owner_conversation": "DBA 专用对话",
                "technical_evidence": [
                    dependency["finding"],
                    dependency["dependency_class"],
                    dependency["exploitability"],
                ],
            },
            {
                "project_id": "DIGITAL_CELL_DEMO",
                "display_name_zh": "数字细胞演示",
                "status": "STABLE",
                "status_zh": "已发布并冻结",
                "why_zh": "它是维护模式下的参考资产。",
                "attention_zh": "本周没有授权功能变化。",
                "impact_zh": "不构成生产认证或数字生命声明。",
                "owner_conversation": "Digital Cell Demo 专用对话",
                "technical_evidence": ["RELEASED_FROZEN_REFERENCE_ASSET"],
            },
            {
                "project_id": "TITMAS_SUPPORTING_LAYER",
                "display_name_zh": "TITMAS 支撑层",
                "status": "STABLE",
                "status_zh": "支撑层边界明确",
                "why_zh": "D29 不是当前工程主线，执行未授权。",
                "attention_zh": "旧商业收敛和组件矩阵只作为保留快照。",
                "impact_zh": "实施前必须刷新组件版本与安全事实。",
                "owner_conversation": "TITMAS 专用对话",
                "technical_evidence": [
                    "D29_ACTIVE_ENGINEERING_MAINLINE=false",
                    "D29_EXECUTION_AUTHORIZED=false",
                    "ARCHITECTURE_DECISION_SUPPORT_SNAPSHOT",
                ],
            },
            {
                "project_id": "TITMAC_SCOUT",
                "display_name_zh": "TITMAC 侦察",
                "status": "BLIND_SPOT",
                "status_zh": "本周动态检查未评估",
                "why_zh": "现有来源注册和只读适配器可复用，但候选 Demo 未调用外部网络。",
                "attention_zh": "已存投影不能替代本周动态观察。",
                "impact_zh": "不推断最新 CI、PR 或远端 revision 状态。",
                "owner_conversation": "TITMAC Scout 专用对话",
                "technical_evidence": [
                    context["source_paths"]["source_registry"],
                    context["source_paths"]["read_only_adapter"],
                ],
            },
        ]
