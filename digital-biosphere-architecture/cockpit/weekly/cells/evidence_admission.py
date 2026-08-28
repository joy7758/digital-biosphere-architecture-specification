"""Admit only current, sourced observations into downstream analysis."""

from __future__ import annotations

from typing import Any

from . import WeeklyCell, make_result


class EvidenceAdmissionCell(WeeklyCell):
    cell_id = "EVIDENCE_ADMISSION_CELL"

    @staticmethod
    def admit(observation: dict[str, Any]) -> dict[str, Any]:
        if not observation.get("source_reference") or not observation.get("observed_at"):
            return {"status": "REJECTED", "reason": "MISSING_SOURCE_OR_TIME", "observation": observation}
        if observation.get("kind") == "ADJACENT_PROJECT_CANDIDATE":
            return {"status": "PENDING", "reason": "CANDIDATE_NOT_ADMITTED", "observation": observation}
        if observation.get("freshness") in {"STALE", "UNKNOWN", None}:
            return {"status": "REJECTED", "reason": "STALE_OR_UNKNOWN", "observation": observation}
        if observation.get("kind") == "DEPENDENCY_SECURITY_CONFLICT_CANDIDATE":
            return {"status": "ADMITTED", "reason": "CURRENT_SOURCE_BOUND_CANDIDATE", "observation": observation}
        return {"status": "PENDING", "reason": "OUTSIDE_AUTOMATIC_ADMISSION_SCOPE", "observation": observation}

    def _run(self, context: dict[str, Any]):
        records = context.get("discovery_records", [])
        decisions = [self.admit(item) for item in records]
        admitted = [item["observation"] for item in decisions if item["status"] == "ADMITTED"]
        rejected = [item for item in decisions if item["status"] == "REJECTED"]
        pending = [item for item in decisions if item["status"] == "PENDING"]
        updates = []
        labels = {
            "ADMITTED": "已通过证据准入",
            "REJECTED": "未通过准入或来源过期",
            "PENDING": "待人工确认候选",
        }
        for item in decisions:
            observation = item["observation"]
            admission_status = (
                "NOT_ADMITTED"
                if observation.get("kind") == "ADJACENT_PROJECT_CANDIDATE"
                else item["status"]
            )
            updates.append(
                {
                    "signal_id": observation["signal_id"],
                    "admission_status": admission_status,
                    "admission_reason": item["reason"],
                    "admission_label_zh": labels[item["status"]],
                }
            )
        summary = {
            "discovered_count": len(records),
            "admitted_count": len(admitted),
            "rejected_count": len(rejected),
            "pending_count": len(pending),
            "rejected_or_pending_count": len(rejected) + len(pending),
        }
        return make_result(
            self.cell_id,
            "PASS_WITH_REJECTIONS" if rejected or pending else "PASS",
            "Discovery signals were separated from evidence admission.",
            observations=decisions,
            outputs={
                "admitted_observations": admitted,
                "rejected_observations": rejected,
                "pending_observations": pending,
                "discovery_updates": updates,
                "admission_summary": summary,
            },
        )
