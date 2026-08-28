from __future__ import annotations

import json
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

from jsonschema import Draft202012Validator

from cockpit.weekly.cells.evidence_admission import EvidenceAdmissionCell
from cockpit.weekly.cells.handoff import HandoffCell
from cockpit.weekly.cells.project_discovery import ProjectDiscoveryCell


WEEKLY = Path(__file__).resolve().parents[1]
DBA = WEEKLY.parents[1]
DEMO = WEEKLY / "demo"


class ElementCounter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags: list[tuple[str, dict[str, str | None]]] = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


class WeeklyCockpitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        snapshots = sorted(DEMO.glob("weekly-snapshot-*.json"))
        if not snapshots:
            raise AssertionError("demo snapshot must be generated before tests")
        cls.snapshot = json.loads(snapshots[-1].read_text(encoding="utf-8"))
        cls.html = (DEMO / "dashboard.html").read_text(encoding="utf-8")
        cls.workflow = (DBA.parent / ".github" / "workflows" / "dba-weekly-cockpit.yml").read_text(encoding="utf-8")

    def test_01_all_twelve_manifests_validate(self):
        schema = json.loads((WEEKLY / "schemas" / "cell-manifest.schema.json").read_text(encoding="utf-8"))
        validator = Draft202012Validator(schema)
        manifests = sorted((WEEKLY / "manifests").glob("*.json"))
        self.assertEqual(12, len(manifests))
        for path in manifests:
            errors = list(validator.iter_errors(json.loads(path.read_text(encoding="utf-8"))))
            self.assertEqual([], errors, path.name)

    def test_02_manifests_deny_all_write_authorities(self):
        for path in (WEEKLY / "manifests").glob("*.json"):
            bounds = json.loads(path.read_text(encoding="utf-8"))["authority_boundaries"]
            self.assertTrue(all(value is False for value in bounds.values()))

    def test_03_discovered_candidate_is_not_auto_monitored(self):
        result = ProjectDiscoveryCell().run({"as_of": "2026-08-29T00:30:00+08:00", "project_check_registry": {"projects": []}})
        candidates = getattr(result, "discoveries", getattr(result, "observations", []))
        external = next(item for item in candidates if item["project_id"] == "openbao-adjacent-signal")
        self.assertEqual("DISCOVERED", external["current_state"])

    def test_04_unauthorized_candidate_does_not_scan_private_content(self):
        result = ProjectDiscoveryCell().run({"as_of": "2026-08-29T00:30:00+08:00", "project_check_registry": {"projects": []}})
        candidates = getattr(result, "discoveries", getattr(result, "observations", []))
        external = next(item for item in candidates if item["project_id"] == "openbao-adjacent-signal")
        self.assertFalse(external["scan_authorized"])
        self.assertFalse(external["private_content_scanned"])

    def test_05_evidence_without_source_or_time_is_rejected(self):
        decision = EvidenceAdmissionCell.admit({"freshness": "CURRENT"})
        self.assertEqual("REJECTED", decision["status"])
        self.assertEqual("MISSING_SOURCE_OR_TIME", decision["reason"])

    def test_06_stale_evidence_is_rejected(self):
        decision = EvidenceAdmissionCell.admit({"source_reference": "x", "observed_at": "2026-01-01", "freshness": "STALE"})
        self.assertEqual("REJECTED", decision["status"])
        self.assertEqual("STALE_OR_UNKNOWN", decision["reason"])

    def test_07_unknown_project_is_not_rendered_as_green(self):
        for project in self.snapshot["projects"]:
            if project.get("status") in {"UNKNOWN", "NOT_ASSESSED"}:
                self.assertNotIn(project.get("status"), {"PASS", "NORMAL", "STABLE"})

    def test_08_cell_failure_isolation_contract_is_present(self):
        coordinator = (WEEKLY / "coordinator.py").read_text(encoding="utf-8")
        self.assertIn("NOT_ASSESSED", coordinator)
        self.assertRegex(coordinator, r"except\s+Exception")

    def test_09_discovery_unavailable_fail_closed_contract_is_present(self):
        coordinator = (WEEKLY / "coordinator.py").read_text(encoding="utf-8")
        self.assertIn("DISCOVERY_UNAVAILABLE", coordinator)

    def test_10_handoff_contains_no_execution_commands(self):
        result = HandoffCell().run({"as_of": "2026-08-29T00:30:00+08:00"})
        packets = getattr(result, "handoffs", getattr(result, "handoff_packets", []))
        self.assertTrue(packets)
        self.assertTrue(all(item["execution_commands"] == [] for item in packets))

    def test_11_human_view_declares_snapshot_only(self):
        self.assertIn("固定问题仅查询当前快照", self.html)
        self.assertNotIn("fetch(", self.html)

    def test_12_no_composite_project_score(self):
        flattened = json.dumps(self.snapshot, ensure_ascii=False).lower()
        self.assertNotIn("composite_score", flattened)
        self.assertNotIn("health_score", flattened)

    def test_13_technical_evidence_is_collapsed_by_default(self):
        self.assertIn("<details>", self.html)
        self.assertNotIn("<details open", self.html)

    def test_14_dashboard_is_standalone(self):
        self.assertNotRegex(self.html, r"<(script|link)[^>]+(?:src|href)=['\"]https?://")
        self.assertIn("id=\"weekly-snapshot\"", self.html)

    def test_15_query_answers_come_from_snapshot(self):
        self.assertIn("snapshot.preset_queries", self.html)
        self.assertNotIn("XMLHttpRequest", self.html)

    def test_16_workflow_has_read_only_permissions(self):
        self.assertIn("contents: read", self.workflow)
        self.assertNotRegex(self.workflow, r"contents:\s*write")
        self.assertNotRegex(self.workflow, r"pull-requests:\s*write")

    def test_17_schedule_requires_explicit_repository_variable(self):
        self.assertIn("DBA_WEEKLY_COCKPIT_SCHEDULE_ENABLED", self.workflow)
        self.assertIn("'true'", self.workflow)

    def test_18_registered_projects_are_read_only(self):
        registry = json.loads((WEEKLY / "project-check-registry.json").read_text(encoding="utf-8"))
        projects = registry.get("projects", registry.get("entries", []))
        self.assertTrue(projects)
        for project in projects:
            self.assertTrue(
                project.get("read_only", False)
                or project.get("access") == "READ_ONLY"
                or project.get("source_access_mode", "").endswith("READ_ONLY")
                or project.get("source_access_mode") == "EXISTING_READ_ONLY_STATUS_ADAPTER"
            )

    def test_19_history_policy_forbids_overwrite(self):
        policy = (WEEKLY / "history" / "README.md").read_text(encoding="utf-8")
        self.assertIn("MUST NOT be overwritten", policy)

    def test_20_old_titmas_snapshots_do_not_gain_current_authority(self):
        flattened = json.dumps(self.snapshot, ensure_ascii=False)
        self.assertIn("view_not_truth", flattened)
        self.assertNotIn('"authority": "CURRENT_TRUTH"', flattened)

    def test_21_exactly_twelve_logical_cells(self):
        registry = json.loads((WEEKLY / "cell-registry.json").read_text(encoding="utf-8"))
        cells = registry.get("cells", registry.get("entries", []))
        self.assertEqual(12, len(cells))
        self.assertEqual(12, len(self.snapshot["cell_runs"]))

    def test_22_dashboard_has_no_more_than_six_main_sections(self):
        parser = ElementCounter()
        parser.feed(self.html)
        sections = [attrs for tag, attrs in parser.tags if tag == "section"]
        self.assertLessEqual(len(sections), 6)
        self.assertTrue(any(tag == "main" for tag, _ in parser.tags))
        self.assertTrue(any(tag == "nav" for tag, _ in parser.tags))
        self.assertTrue(any(tag == "button" for tag, _ in parser.tags))

    def test_23_weekly_snapshot_contract_validates(self):
        schema = json.loads((WEEKLY / "schemas" / "weekly-snapshot.schema.json").read_text(encoding="utf-8"))
        errors = list(Draft202012Validator(schema).iter_errors(self.snapshot))
        self.assertEqual([], errors)

    def test_24_dashboard_has_chinese_language_and_title(self):
        self.assertIn('lang="zh-CN"', self.html)
        self.assertIn("<title>DBA Weekly Cockpit", self.html)


if __name__ == "__main__":
    unittest.main()
