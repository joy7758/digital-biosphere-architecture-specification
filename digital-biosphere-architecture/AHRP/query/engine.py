"""AHRP Query Interface reference engine (Python 3 stdlib only).

Design defaults (SPEC v0.1 Chapter 7):

* Selective Disclosure First: the default query returns an Experience Summary
  (raw counts ``verified_events`` / ``total_events``); detailed events are
  returned only on explicit drill-down. No derived ratios, scores or rankings
  are ever produced (Constitution Section 9 non-goals).
* Three-state null semantics: NO_RECORD / WITHHELD / NOT_APPLICABLE are
  distinct and machine-readable.
* Identity continuity fail-closed: summaries are computed per agent_version;
  cross-version merging is refused by default (Constitution Section 8).
* DATA != INSTRUCTION: free-text fields travel only in the restricted_text
  content channel and are excluded from every summary.
"""

from __future__ import annotations

import copy
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional

from validator.core import (
    FAILURE_CLASS_STATUSES,
    validate_experience_event,
    validate_verification_record,
)

PROTOCOL = "AHRP"
PROTOCOL_VERSION = "0.1.0"
SYNTHETIC_ONLY_NOTE = "Reference implementation; synthetic data only."

# Verification-status precedence for deriving an event-level status from its
# verification records (worst-conflict-first, fail-closed).
_STATUS_PRIORITY = ("CONFLICTED", "INVALID", "PARTIALLY_VERIFIED", "VERIFIED")

# F10: only verifications scoped to the experience event itself and covering
# an event-level aspect count toward event-level aggregation. EVIDENCE_BINDING
# verifies an evidence reference, not the event; NOT_ASSESSED asserts nothing.
_EVENT_SCOPE_SUBJECT_TYPE = "EXPERIENCE_EVENT"
_EVENT_LEVEL_ASPECTS = frozenset({"FULL_EVENT", "OCCURRENCE", "RESULT_STATUS"})

# F4: whitelisted free-text (DATA channel) fields, including nested dot paths.
# They must never enter structured_facts or any decision path.
FREE_TEXT_FIELDS = ("notes", "agent_reference.identity_note")

# Summary projection fields for a single event (no free text).
_SUMMARY_FIELDS = (
    "event_id",
    "agent_version",
    "task_type",
    "action_type",
    "result_status",
    "failure_category",
    "occurred_at",
    "verification_status",
    "evidence_availability",
)


class NullSemantics(str, Enum):
    """Three distinguishable empty-value states (SPEC v0.1 Chapter 11)."""

    NONE = "NONE"                          # content is present
    NO_RECORD = "NO_RECORD"                # nothing was ever recorded
    WITHHELD = "WITHHELD"                  # record exists, disclosure withheld
    NOT_APPLICABLE = "NOT_APPLICABLE"      # the question does not apply


class IngestError(ValueError):
    """Raised when a document fails reference validation (fail-closed)."""

    def __init__(self, validation_result):
        self.validation_result = validation_result
        super().__init__(f"ingest rejected: {validation_result.to_dict()}")


def _envelope(mode: str, null_semantics: NullSemantics, result: Any,
              restricted_fields: Optional[List[str]] = None,
              withheld_count: int = 0) -> Dict[str, Any]:
    return {
        "protocol": PROTOCOL,
        "schema_version": PROTOCOL_VERSION,
        "content_channel": {
            "structured_facts": "payload fields not listed in restricted_text",
            "restricted_text": list(restricted_fields or []),
        },
        "selective_disclosure": {"mode": mode, "withheld_count": withheld_count},
        "null_semantics": null_semantics.value,
        "result": result,
    }


def _parse_instant(value: str):
    """F5: parse an RFC 3339 date-time into an absolute instant (UTC epoch).

    Comparisons and ordering use instants, never string lexicographic order,
    so mixed offsets ('Z' vs '+08:00') compare correctly. Ingest validation
    guarantees parsability; malformed values raise ValueError by design.
    """
    candidate = value[:-1] + "+00:00" if value.endswith("Z") else value
    return datetime.fromisoformat(candidate).timestamp()


def _get_path(doc: Dict[str, Any], dotted: str) -> Any:
    """Resolve a dotted path (e.g. 'agent_reference.identity_note')."""
    node: Any = doc
    for part in dotted.split("."):
        if not isinstance(node, dict) or part not in node:
            return None
        node = node[part]
    return node


class HistoryStore:
    """In-memory federated-holding simulation (one holder's ledger).

    AHRP is NOT a central database; this store simulates a single federated
    holder. All ingestion is validated first and fails closed.
    """

    def __init__(self) -> None:
        self._events: Dict[str, Dict[str, Any]] = {}
        self._verifications: Dict[str, Dict[str, Any]] = {}

    # ------------------------------------------------------------- ingest
    def ingest_event(self, event: Dict[str, Any]) -> str:
        result = validate_experience_event(event)
        if not result.valid:
            raise IngestError(result)
        event_id = event["event_id"]
        if event_id in self._events:
            raise ValueError(f"duplicate event_id: {event_id}")
        # F11: deep-copy on ingest so later mutation of the caller's dict
        # (aliasing) can never alter the stored record.
        self._events[event_id] = copy.deepcopy(event)
        return event_id

    def ingest_verification(self, record: Dict[str, Any]) -> str:
        result = validate_verification_record(record)
        if not result.valid:
            raise IngestError(result)
        verification_id = record["verification_id"]
        if verification_id in self._verifications:
            raise ValueError(f"duplicate verification_id: {verification_id}")
        self._verifications[verification_id] = copy.deepcopy(record)
        return verification_id

    # ------------------------------------------------------ derived state
    def verifications_for_event(self, event_id: str) -> List[Dict[str, Any]]:
        # Output copies: callers can never mutate stored records.
        return [
            copy.deepcopy(v) for v in self._verifications.values()
            if v.get("scope", {}).get("subject_event_id") == event_id
        ]

    def _event_scoped_verifications(self, event_id: str) -> List[Dict[str, Any]]:
        """F10: verifications eligible for event-level aggregation.

        Requires scope.subject_type == EXPERIENCE_EVENT and covered_aspect in
        {FULL_EVENT, OCCURRENCE, RESULT_STATUS}. Records scoped to evidence
        references or covering only EVIDENCE_BINDING assert nothing about the
        event itself and are excluded (fail-closed).
        """
        eligible = []
        for v in self._verifications.values():
            scope = v.get("scope", {})
            if scope.get("subject_event_id") != event_id:
                continue
            if scope.get("subject_type") != _EVENT_SCOPE_SUBJECT_TYPE:
                continue
            if scope.get("covered_aspect") not in _EVENT_LEVEL_ASPECTS:
                continue
            eligible.append(v)
        return eligible

    def event_verification_status(self, event_id: str) -> str:
        records = self._event_scoped_verifications(event_id)
        if not records:
            return "NOT_ASSESSED"  # fail-closed default, never assumed verified
        present = {r["verification_status"] for r in records}
        for status in _STATUS_PRIORITY:
            if status in present:
                return status
        return "NOT_ASSESSED"

    def _event_is_withheld(self, event: Dict[str, Any]) -> bool:
        return event.get("disclosure", {}).get("disclosure_scope") == "WITHHELD"

    def _event_summary(self, event: Dict[str, Any]) -> Dict[str, Any]:
        entry: Dict[str, Any] = {}
        for field in _SUMMARY_FIELDS:
            if field == "verification_status":
                entry[field] = self.event_verification_status(event["event_id"])
            elif field == "evidence_availability":
                entry[field] = [
                    ref["availability_status"]
                    for ref in event.get("evidence_references", [])
                ]
            elif field == "failure_category":
                # Three-state field projection: NOT_APPLICABLE for non-failure
                # results; a failure-class event without the category would
                # have been rejected at ingest.
                if event["result_status"] in FAILURE_CLASS_STATUSES:
                    entry[field] = event.get("failure_category")
                else:
                    entry[field] = NullSemantics.NOT_APPLICABLE.value
            else:
                entry[field] = event.get(field)
        scoped = self._event_scoped_verifications(event["event_id"])
        entry["self_verified_only"] = all(
            v.get("self_verification") is True for v in scoped
        ) if scoped else None
        return entry

    # ------------------------------------------------------------- queries
    def _select(self, identity_ref: Optional[str], agent_version: Optional[str],
                task_type: Optional[str], time_start: Optional[str],
                time_end: Optional[str], verification_status: Optional[str]):
        # F6: addressing filters (identity_ref, agent_version) are applied
        # FIRST; withheld records are only counted within that addressed
        # scope, so a query for an unrelated identity can never observe the
        # existence of another party's withheld records (existence leak).
        addressed = []
        for event in self._events.values():
            if identity_ref is not None and \
                    event["agent_reference"]["identity_ref"] != identity_ref:
                continue
            if agent_version is not None and event["agent_version"] != agent_version:
                continue
            addressed.append(event)
        withheld = sum(1 for e in addressed if self._event_is_withheld(e))
        selected = []
        start = _parse_instant(time_start) if time_start is not None else None
        end = _parse_instant(time_end) if time_end is not None else None
        for event in addressed:
            if self._event_is_withheld(event):
                # withheld events are counted but never filtered on content
                continue
            if task_type is not None and event["task_type"] != task_type:
                continue
            # F5: absolute-instant comparison, not string lexicographic order.
            instant = _parse_instant(event["occurred_at"])
            if start is not None and instant < start:
                continue
            if end is not None and instant > end:
                continue
            if verification_status is not None and \
                    self.event_verification_status(event["event_id"]) != verification_status:
                continue
            selected.append(event)
        return selected, withheld

    def summary(self, identity_ref: str,
                agent_version: Optional[str] = None) -> Dict[str, Any]:
        """Default query: Experience Summary (Selective Disclosure First).

        Raw counts only (``verified_events``, ``total_events``); NO derived
        ratios, scores or rankings. Identity continuity fail-closed: without
        an explicit ``agent_version``, counts are reported per version and
        never merged across versions.
        """
        all_events = [
            e for e in self._events.values()
            if e["agent_reference"]["identity_ref"] == identity_ref
        ]
        if not all_events:
            return _envelope(
                "summary", NullSemantics.NO_RECORD,
                {"agent_identity_ref": identity_ref, "total_events": 0,
                 "verified_events": 0, "withheld_events": 0},
            )
        withheld = sum(1 for e in all_events if self._event_is_withheld(e))
        visible = [e for e in all_events if not self._event_is_withheld(e)]
        # F9: this identity holds records but every one is withheld -> the
        # honest answer is WITHHELD, not an empty NONE summary.
        if not visible:
            return _envelope(
                "summary", NullSemantics.WITHHELD,
                {"agent_identity_ref": identity_ref, "total_events": 0,
                 "verified_events": 0, "withheld_events": withheld,
                 "by_version": {}},
                withheld_count=withheld,
            )
        versions = sorted({e["agent_version"] for e in visible})
        if agent_version is not None:
            versions = [v for v in versions if v == agent_version]
        # F9: the identity has visible records but none in the requested
        # version scope -> NO_RECORD for that scope (nothing was withheld
        # here, so NOT_APPLICABLE/WITHHELD would both be dishonest).
        if not versions:
            return _envelope(
                "summary", NullSemantics.NO_RECORD,
                {"agent_identity_ref": identity_ref,
                 "agent_version": agent_version, "total_events": 0,
                 "verified_events": 0, "withheld_events": 0,
                 "by_version": {}},
            )
        by_version: Dict[str, Dict[str, Any]] = {}
        for version in versions:
            v_events = [e for e in visible if e["agent_version"] == version]
            verified = [
                e for e in v_events
                if self.event_verification_status(e["event_id"]) == "VERIFIED"
            ]
            by_task: Dict[str, int] = {}
            by_status: Dict[str, int] = {}
            for e in v_events:
                by_task[e["task_type"]] = by_task.get(e["task_type"], 0) + 1
                by_status[e["result_status"]] = by_status.get(e["result_status"], 0) + 1
            by_version[version] = {
                "total_events": len(v_events),
                "verified_events": len(verified),
                "events_by_task_type": by_task,
                "events_by_result_status": by_status,
            }
        result = {
            "agent_identity_ref": identity_ref,
            "identity_continuity": "FAIL_CLOSED_PER_VERSION_COUNTS_ONLY",
            "by_version": by_version,
            "withheld_events": withheld,
            "note": "Raw counts only. No derived ratios, scores or rankings "
                    "(AHRP Constitution Section 9 non-goals).",
        }
        return _envelope("summary", NullSemantics.NONE, result,
                         withheld_count=withheld)

    def query_events(self, identity_ref: Optional[str] = None,
                     agent_version: Optional[str] = None,
                     task_type: Optional[str] = None,
                     time_start: Optional[str] = None,
                     time_end: Optional[str] = None,
                     verification_status: Optional[str] = None) -> Dict[str, Any]:
        """Filtered list query returning summary projections only."""
        selected, withheld = self._select(
            identity_ref, agent_version, task_type,
            time_start, time_end, verification_status)
        if not selected and withheld > 0:
            semantics = NullSemantics.WITHHELD
        elif not selected:
            semantics = NullSemantics.NO_RECORD
        else:
            semantics = NullSemantics.NONE
        ordered = sorted(selected,
                         key=lambda e: _parse_instant(e["occurred_at"]))
        return _envelope(
            "summary", semantics,
            {"events": [self._event_summary(e) for e in ordered],
             "count": len(ordered)},
            withheld_count=withheld,
        )

    def get_event(self, event_id: str,
                  capability: str = "summary") -> Dict[str, Any]:
        """Drill-down. Detail requires explicit capability='detail' AND a
        disclosure scope that permits it; otherwise fail-closed."""
        event = self._events.get(event_id)
        if event is None:
            return _envelope("detail", NullSemantics.NO_RECORD,
                             {"event_id": event_id})
        if self._event_is_withheld(event):
            return _envelope("detail", NullSemantics.WITHHELD,
                             {"event_id": event_id}, withheld_count=1)
        if capability != "detail":
            return _envelope("summary", NullSemantics.NONE,
                             self._event_summary(event))
        # F4: every whitelisted free-text field (including nested dot paths)
        # is stripped from structured_facts and declared in restricted_text.
        restricted = [f for f in FREE_TEXT_FIELDS
                      if _get_path(event, f) is not None]
        structured = copy.deepcopy(event)
        restricted_payload: Dict[str, Any] = {}
        for dotted in restricted:
            node = structured
            container = restricted_payload
            parts = dotted.split(".")
            for part in parts[:-1]:
                node = node[part]
                container = container.setdefault(part, {})
            container[parts[-1]] = node.pop(parts[-1])
        structured["verification_status"] = self.event_verification_status(event_id)
        structured["verification_records"] = self.verifications_for_event(event_id)
        return _envelope(
            "detail", NullSemantics.NONE,
            {"structured_facts": structured,
             "restricted_text": restricted_payload},
            restricted_fields=restricted,
        )

    def get_failure_category(self, event_id: str) -> Dict[str, Any]:
        """Dedicated projection demonstrating the three-state null semantics.

        NO_RECORD: event unknown; NOT_APPLICABLE: result is not failure-class;
        otherwise the enumerated failure_category value.
        """
        event = self._events.get(event_id)
        if event is None:
            return _envelope("detail", NullSemantics.NO_RECORD,
                             {"event_id": event_id})
        if self._event_is_withheld(event):
            return _envelope("detail", NullSemantics.WITHHELD,
                             {"event_id": event_id}, withheld_count=1)
        if event["result_status"] not in FAILURE_CLASS_STATUSES:
            return _envelope("detail", NullSemantics.NOT_APPLICABLE,
                             {"event_id": event_id, "failure_category": None})
        return _envelope("detail", NullSemantics.NONE,
                         {"event_id": event_id,
                          "failure_category": event["failure_category"]})
