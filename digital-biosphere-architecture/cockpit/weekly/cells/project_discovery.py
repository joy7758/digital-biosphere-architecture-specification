"""Discover registered projects and adjacent candidates without admitting them."""

from __future__ import annotations

from typing import Any

from . import WeeklyCell, make_result, source_value


class ProjectDiscoveryCell(WeeklyCell):
    cell_id = "PROJECT_DISCOVERY_CELL"

    def _run(self, context: dict[str, Any]):
        as_of = context.get("as_of", "UNKNOWN")
        registry = source_value(
            context,
            "project_registry",
            source_value(context, "project_check_registry", {}),
        )
        entries = registry.get("projects", registry.get("entries", [])) if isinstance(registry, dict) else registry
        project_records: list[dict[str, Any]] = []
        for item in entries or []:
            project_records.append(
                {
                    "project_id": item["project_id"],
                    "display_name_zh": item.get("display_name_zh", item["project_id"]),
                    "lifecycle_mode": item.get("lifecycle_mode", "UNKNOWN"),
                    "owner_conversation": item.get("owner_conversation", "UNKNOWN"),
                    "source_reference": item.get("canonical_source_ref", "UNKNOWN"),
                    "source_access_mode": item.get("source_access_mode", "READ_ONLY"),
                    "status": "NOT_ASSESSED",
                    "status_zh": "尚未评估",
                    "why_zh": "已登记项目身份与来源，状态等待有边界的分析 Cell 更新。",
                    "attention_zh": "未评估不等于正常。",
                    "technical_evidence": [item.get("canonical_source_ref", "UNKNOWN")],
                }
            )

        candidate = {
            "candidate_id": "candidate-openbao-2026-W35",
            "signal_id": "DISCOVERY-OPENBAO-CANDIDATE",
            "project_id": "openbao-adjacent-signal",
            "kind": "ADJACENT_PROJECT_CANDIDATE",
            "subject": "OpenBao",
            "display_name": "OpenBao（机密与密钥管理组件）候选",
            "title_zh": "OpenBao（机密与密钥管理组件）候选",
            "source_reference": "project-discovery:public-adjacent-candidate",
            "discovered_at": as_of,
            "observed_at": as_of,
            "lifecycle": "CANDIDATE",
            "current_state": "DISCOVERED",
            "observed_state": "DISCOVERED",
            "freshness": "UNKNOWN",
            "authority": "DISCOVERY_ONLY",
            "scan_authorized": False,
            "private_content_scanned": False,
            "read_only": True,
            "admission_status": "NOT_ADMITTED",
            "monitoring_status": "NOT_MONITORED",
            "admission_label_zh": "待人工确认候选",
            "details_zh": "OpenBao（机密与密钥管理组件）仍是待确认候选；应先刷新当前版本与安全事实。",
            "note": "Discovery does not grant evidence admission, monitoring, or scan authority.",
        }
        return make_result(
            self.cell_id,
            "PASS",
            "Registered project identities and one adjacent candidate were discovered without admission.",
            discoveries=[candidate],
            outputs={
                "project_records": project_records,
                "discovery_records": [candidate],
            },
        )
