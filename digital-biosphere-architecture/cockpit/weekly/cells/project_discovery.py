"""Discover candidate projects without granting monitoring authority."""

from __future__ import annotations

from typing import Any

try:
    from cockpit.weekly.cells import WeeklyCell, make_result, source_value
except ModuleNotFoundError:
    from cells import WeeklyCell, make_result, source_value


class ProjectDiscoveryCell(WeeklyCell):
    cell_id = "PROJECT_DISCOVERY_CELL"

    def _run(self, context: dict[str, Any]):
        registry = (
            source_value(context, "project_registry")
            or source_value(context, "project_check_registry", {})
            or {}
        )
        projects = registry.get("projects", registry.get("entries", []))
        candidates: list[dict[str, Any]] = []
        for project in projects:
            candidate = {
                "candidate_id": f"candidate:{project.get('project_id', 'unknown')}",
                "project_id": project.get("project_id", "UNKNOWN"),
                "display_name_zh": project.get("display_name_zh", project.get("display_name", project.get("project_id", "未知项目"))),
                "canonical_source_ref": project.get("canonical_source_ref", project.get("source_reference", "UNKNOWN")),
                "source_reference": project.get("canonical_source_ref", project.get("source_reference", "UNKNOWN")),
                "discovered_at": context.get("as_of", "UNKNOWN"),
                "lifecycle": ["DISCOVERED", "ADMITTED", "MONITORED"],
                "current_state": "MONITORED",
                "discovery_status": "MONITORED",
                "scan_authorized": project.get("scan_authorized", False),
                "private_content_scanned": False,
                "read_only": True,
            }
            candidates.append(candidate)

        candidates.append(
            {
                "candidate_id": "candidate:openbao-adjacent-signal",
                "project_id": "openbao-adjacent-signal",
                "display_name": "OpenBao 邻接信号",
                "display_name_zh": "OpenBao 邻接信号",
                "source_reference": "https://github.com/openbao/openbao",
                "canonical_source_ref": "https://github.com/openbao/openbao",
                "discovered_at": context.get("as_of", "UNKNOWN"),
                "lifecycle": ["DISCOVERED"],
                "current_state": "DISCOVERED",
                "discovery_status": "DISCOVERED",
                "scan_authorized": False,
                "private_content_scanned": False,
                "read_only": True,
                "note": "仅记录公开邻接信号；未经人工准入，不进入持续监测。",
            }
        )
        context["project_candidates"] = candidates
        return make_result(
            self.cell_id,
            "PASS" if projects else "NOT_ASSESSED",
            f"发现 {len(candidates)} 个候选，其中 {len(projects)} 个来自登记表。",
            discoveries=candidates,
            observations=candidates,
            metadata={"auto_admission": False, "private_scan": False},
        )
