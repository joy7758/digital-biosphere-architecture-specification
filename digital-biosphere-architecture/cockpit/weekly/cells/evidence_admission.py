"""Admit evidence only when source identity and time are explicit."""

from __future__ import annotations

from typing import Any

try:
    from cockpit.weekly.cells import WeeklyCell, make_result
except ModuleNotFoundError:
    from cells import WeeklyCell, make_result


class EvidenceAdmissionCell(WeeklyCell):
    cell_id = "EVIDENCE_ADMISSION_CELL"

    @staticmethod
    def admit(observation: dict[str, Any]) -> dict[str, Any]:
        source = observation.get("source_reference")
        observed_at = observation.get("observed_at")
        freshness = observation.get("freshness", "UNKNOWN")
        if not source or source == "UNKNOWN" or not observed_at or observed_at == "UNKNOWN":
            return {"status": "REJECTED", "reason": "MISSING_SOURCE_OR_TIME", "observation": observation}
        if freshness in {"STALE", "STALE_OR_UNKNOWN", "UNKNOWN", "EXPIRED"}:
            return {"status": "REJECTED", "reason": "STALE_OR_UNKNOWN", "observation": observation}
        return {"status": "ADMITTED", "reason": "SOURCE_TIME_AND_FRESHNESS_PRESENT", "observation": observation}

    def _run(self, context: dict[str, Any]):
        incoming = context.get("discovery_signals", context.get("discovery_observations", context.get("observations", [])))
        decisions = [self.admit(item) for item in incoming if isinstance(item, dict)]
        context["admitted_observations"] = [item["observation"] for item in decisions if item["status"] == "ADMITTED"]
        admitted = sum(item["status"] == "ADMITTED" for item in decisions)
        rejected = len(decisions) - admitted
        return make_result(
            self.cell_id,
            "PASS_WITH_NOT_ASSESSED" if rejected else "PASS",
            f"证据准入 {admitted} 项，拒绝或保留 {rejected} 项。",
            observations=decisions,
            metadata={"admitted": admitted, "rejected": rejected, "fail_closed": True},
        )
