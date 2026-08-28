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
from cockpit.weekly.cells.security import SecurityCell


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
        cls.markdown = (DEMO / "latest.md").read_text(encoding="utf-8")
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

    def test_25_markdown_uses_observed_at_without_false_unknown(self):
        self.assertIn(self.snapshot["observed_at"], self.markdown)
        self.assertNotIn("As of: UNKNOWN", self.markdown)
        self.assertNotIn("观察时间：`UNKNOWN`", self.markdown)

    def test_26_markdown_contains_both_human_decisions(self):
        self.assertIn("是否启动依赖安全专项复核", self.markdown)
        self.assertIn("是否授权刷新 TITMAC Scout 的只读状态", self.markdown)

    def test_27_markdown_contains_all_five_projects(self):
        for name in ("红岩公文", "DBA 驾驶舱", "数字细胞演示", "TITMAS 支撑层", "TITMAC 侦察"):
            self.assertIn(name, self.markdown)

    def test_28_markdown_has_no_false_placeholder_copy(self):
        self.assertNotIn("未命名", self.markdown)
        self.assertNotIn("无说明", self.markdown)

    def test_29_html_and_markdown_share_snapshot_identity(self):
        snapshot_id = self.snapshot["snapshot_id"]
        self.assertIn(snapshot_id, self.html)
        self.assertIn(snapshot_id, self.markdown)

    def test_30_not_assessed_is_not_translated_as_normal(self):
        line = next(line for line in self.markdown.splitlines() if "依赖漏洞的远端运行绑定未观察" in line)
        self.assertIn("NOT_ASSESSED", line)
        self.assertNotIn("正常", line)

    def test_31_markdown_semantics_match_snapshot(self):
        self.assertIn(self.snapshot["weekly_sentence_zh"], self.markdown)
        for item in self.snapshot["discoveries"]:
            self.assertIn(item["title_zh"], self.markdown)
        for item in self.snapshot["blind_spots"]:
            self.assertIn(item["title_zh"], self.markdown)

    def test_32_coordinator_contains_no_project_specific_constants(self):
        source = (WEEKLY / "coordinator.py").read_text(encoding="utf-8")
        for token in ("RED_YAN", "OpenBao", "postcss", "nanoid", "TITMAC_SCOUT"):
            self.assertNotIn(token, source)

    def test_33_coordinator_contains_no_concrete_human_decisions(self):
        source = (WEEKLY / "coordinator.py").read_text(encoding="utf-8")
        self.assertNotIn("是否启动依赖安全专项复核", source)
        self.assertNotIn("是否授权刷新 TITMAC Scout 的只读状态", source)

    def test_34_all_snapshot_decisions_come_from_handoff_cell(self):
        self.assertEqual("HANDOFF_CELL", self.snapshot["decisions_source"])
        self.assertTrue(self.snapshot["decisions"])
        self.assertTrue(all(item["source_cell_id"] == "HANDOFF_CELL" for item in self.snapshot["decisions"]))

    def test_35_security_consumes_only_admitted_observations(self):
        result = SecurityCell().run(
            {
                "admitted_observations": [
                    {"signal_id": "accepted", "kind": "DEPENDENCY_SECURITY_CONFLICT_CANDIDATE"}
                ],
                "rejected_observations": [
                    {"observation": {"signal_id": "rejected", "kind": "DEPENDENCY_SECURITY_CONFLICT_CANDIDATE"}}
                ],
            }
        )
        self.assertEqual(["accepted"], result.outputs["security_consumed_signal_ids"])

    def test_36_rejected_observations_are_not_rendered_as_admitted(self):
        rejected = [item for item in self.snapshot["discoveries"] if item["admission_status"] == "REJECTED"]
        self.assertTrue(rejected)
        self.assertTrue(all(item["admission_label_zh"] == "未通过准入或来源过期" for item in rejected))

    def test_37_openbao_remains_discovered_not_admitted_or_monitored(self):
        item = next(item for item in self.snapshot["discoveries"] if item.get("project_id") == "openbao-adjacent-signal")
        self.assertEqual("DISCOVERED", item["current_state"])
        self.assertEqual("NOT_ADMITTED", item["admission_status"])
        self.assertEqual("NOT_MONITORED", item["monitoring_status"])
        self.assertFalse(item["scan_authorized"])

    def test_38_openbao_is_not_a_human_decision(self):
        decisions = json.dumps(self.snapshot["decisions"], ensure_ascii=False)
        self.assertNotIn("OpenBao", decisions)

    def test_39_dependency_audit_conflict_preserves_both_counts(self):
        finding = next(item for item in self.snapshot["findings"] if item.get("finding_type") == "DEPENDENCY_AUDIT_STATE_CONFLICT")
        self.assertEqual(2, finding["canonical_high_count"])
        self.assertEqual(4, finding["live_candidate_high_count"])
        self.assertEqual("NOT_ASSESSED", finding["exploitability"])

    def test_40_all_live_high_packages_are_visible(self):
        for package in ("image-size", "js-yaml", "nanoid", "vinext"):
            self.assertIn(package, self.html)
            self.assertIn(package, self.markdown)

    def test_41_dashboard_does_not_claim_remote_exploitability(self):
        self.assertNotIn("远端可利用", self.html)
        self.assertNotIn("远端可利用", self.markdown)

    def test_42_first_snapshot_does_not_claim_six_new_signals(self):
        self.assertNotIn("新增6", self.html)
        self.assertNotIn("新增 6", self.markdown)
        self.assertIn("首次快照，尚不能判断这些信号是否相对于上周新增", self.markdown)

    def test_43_machine_status_code_is_hidden_from_hero(self):
        app = (WEEKLY / "ui" / "app.js").read_text(encoding="utf-8")
        hero_line = next(line for line in app.splitlines() if 'el("overall-signal")' in line)
        self.assertNotIn("snapshot.overall_status", hero_line)
        self.assertIn("部分检查尚未完成", hero_line)

    def test_44_human_view_uses_chinese_high_risk_wording(self):
        self.assertIn("高危", self.html)
        self.assertIn("高危", self.markdown)
        self.assertNotRegex(self.html, r"\d+\s*个\s*high")
        self.assertNotRegex(self.markdown, r"\d+\s*个\s*high")

    def test_45_handoff_allows_one_decision_without_forced_symmetry(self):
        result = HandoffCell().run(
            {
                "findings": [
                    {
                        "finding_type": "DEPENDENCY_AUDIT_STATE_CONFLICT",
                        "finding_id": "f1",
                        "project_id": "p1",
                        "canonical_high_count": 2,
                        "live_candidate_high_count": 4,
                    }
                ],
                "blind_spots": [],
            }
        )
        self.assertEqual(1, len(result.outputs["decisions"]))

    def test_46_cell_failure_isolation_remains_fail_closed(self):
        source = (WEEKLY / "coordinator.py").read_text(encoding="utf-8")
        self.assertRegex(source, r"except\s+Exception")
        self.assertIn('status="NOT_ASSESSED"', source)
        self.assertIn("DISCOVERY_UNAVAILABLE", source)

    def test_47_logical_cell_count_remains_twelve(self):
        self.assertEqual(12, len(self.snapshot["logical_cells"]))
        self.assertEqual(12, len(self.snapshot["cell_runs"]))

    def test_48_discovery_admission_counts_are_explicit(self):
        counts = self.snapshot["counts"]
        self.assertEqual(6, counts["discovered_count"])
        self.assertEqual(1, counts["admitted_count"])
        self.assertEqual(5, counts["rejected_or_pending_count"])


if __name__ == "__main__":
    unittest.main()
