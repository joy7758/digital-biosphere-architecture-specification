"""Discover declared relationships; never infer authority from adjacency."""

from __future__ import annotations

from typing import Any

try:
    from cockpit.weekly.cells import WeeklyCell, make_result
except ModuleNotFoundError:
    from cells import WeeklyCell, make_result


class RelationshipDiscoveryCell(WeeklyCell):
    cell_id = "RELATIONSHIP_DISCOVERY_CELL"

    def _run(self, context: dict[str, Any]):
        relationships = [
            {
                "signal_id": "rel:red-yan-to-dba-evidence-handoff",
                "kind": "DECLARED_HANDOFF",
                "signal_type": "DECLARED_HANDOFF",
                "summary_zh": "红岩运行调查证据由产品线产生，DBA 接收摘要",
                "subject": "red-yan-evidence-handoff",
                "observed_state": "DECLARED",
                "authority": "OBSERVATION_ONLY",
                "from_project": "red-yan-official-documents",
                "to_project": "digital-biosphere-architecture-specification",
                "relationship": "evidence_snapshot_and_governance_reporting",
                "source_reference": "current-direction-and-red-yan-evidence-snapshot",
                "observed_at": context.get("as_of", "UNKNOWN"),
                "authority_inherited": False,
            },
            {
                "signal_id": "rel:titmas-supporting-layer",
                "kind": "DECLARED_SUPPORT",
                "signal_type": "DECLARED_SUPPORT",
                "summary_zh": "TITMAS 是信任与证据支撑层，不是当前工程主线",
                "subject": "titmas-supporting-layer",
                "observed_state": "DECLARED",
                "authority": "OBSERVATION_ONLY",
                "from_project": "titmas",
                "to_project": "dba-program-governance",
                "relationship": "supporting_trust_and_evidence_layer",
                "source_reference": "current-direction",
                "observed_at": context.get("as_of", "UNKNOWN"),
                "authority_inherited": False,
            },
        ]
        context.setdefault("discovery_signals", []).extend(relationships)
        return make_result(
            self.cell_id,
            "PASS",
            "仅呈现已声明的交接与支持关系，不从仓库邻接推导权限。",
            discoveries=relationships,
            observations=relationships,
        )
