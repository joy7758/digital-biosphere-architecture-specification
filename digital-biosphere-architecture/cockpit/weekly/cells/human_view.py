"""Render the standardized weekly snapshot without adding new facts."""

from __future__ import annotations

import html
import json
from pathlib import Path
from typing import Any

from . import WeeklyCell, make_result


class HumanViewCell(WeeklyCell):
    cell_id = "HUMAN_VIEW_CELL"

    def render(self, snapshot: dict[str, Any], output_dir: str | Path) -> dict[str, str]:
        output = Path(output_dir)
        output.mkdir(parents=True, exist_ok=True)
        weekly = Path(__file__).resolve().parents[1]
        template = (weekly / "ui" / "template.html").read_text(encoding="utf-8")
        styles = (weekly / "ui" / "styles.css").read_text(encoding="utf-8")
        script = (weekly / "ui" / "app.js").read_text(encoding="utf-8")
        serialized = json.dumps(snapshot, ensure_ascii=False, sort_keys=True).replace("</", "<\\/")
        rendered = (
            template.replace("/*__STYLES__*/", styles)
            .replace("/*__SNAPSHOT__*/", serialized)
            .replace("/*__APP__*/", script)
        )
        dashboard = output / "dashboard.html"
        dashboard.write_text(rendered, encoding="utf-8")
        markdown = output / "latest.md"
        markdown.write_text(self.render_markdown(snapshot), encoding="utf-8")
        return {"dashboard": str(dashboard), "markdown": str(markdown)}

    @staticmethod
    def render_markdown(snapshot: dict[str, Any]) -> str:
        counts = snapshot.get("counts", {})
        memory = snapshot.get("memory", {})
        lines = [
            "# DBA 每周驾驶舱",
            "",
            f"- 快照编号：`{snapshot['snapshot_id']}`",
            f"- 观察时间：`{snapshot['observed_at']}`",
            f"- 总体状态：`{snapshot['overall_status']}`",
            "- 视图边界：只读观察；不构成项目真值、执行授权或发布授权。",
            f"- 来源模式：`{snapshot.get('source_observation_summary', {}).get('source_mode', 'RETAINED_SNAPSHOT')}`",
            f"- 发现可用性：`{snapshot.get('discovery_state', 'UNKNOWN')}`",
            "",
            "## 本周一句话",
            "",
            snapshot["weekly_sentence_zh"],
            "",
            "## 本周需要你决定",
            "",
        ]
        decisions = snapshot.get("decisions", [])
        if decisions:
            for item in decisions:
                lines.extend(
                    [
                        f"### {item['title_zh']}",
                        "",
                        item.get("why_zh", "请查看引用证据后作出人工决定。"),
                        "",
                    ]
                )
        else:
            lines.extend(["当前没有登记的人工决定；这不表示没有风险。", ""])

        lines.extend(
            [
                "## 项目状态",
                "",
            ]
        )
        for project in snapshot.get("projects", []):
            lines.extend(
                [
                    f"### {project.get('display_name_zh', project.get('project_id', '项目'))}",
                    "",
                    f"- 状态：`{project.get('status', 'NOT_ASSESSED')}`（{project.get('status_zh', '尚未评估')}）",
                    f"- 来源标签：`{project.get('source_label', 'RETAINED_SNAPSHOT')}`",
                    f"- 说明：{project.get('why_zh', '没有可用的人类解释。')}",
                    f"- 注意：{project.get('attention_zh', '未评估不等于正常。')}",
                    "",
                ]
            )

        lines.extend(
            [
                "## 本周发现信号",
                "",
                (
                    f"共记录 {counts.get('discovered_count', len(snapshot.get('discoveries', [])))} 项信号；"
                    f"已准入 {counts.get('admitted_count', 0)} 项；被拒绝或待确认 "
                    f"{counts.get('rejected_or_pending_count', 0)} 项。"
                ),
                "",
                memory.get("note_zh", "首次快照，尚不能判断这些信号是否相对于上周新增。"),
                "",
            ]
        )
        for item in snapshot.get("discoveries", []):
            lines.extend(
                [
                    f"### {item.get('title_zh', item.get('subject', '发现信号'))}",
                    "",
                    f"- 准入标签：{item.get('admission_label_zh', '待人工确认候选')}",
                    f"- 观察状态：`{item.get('observed_state', item.get('current_state', 'UNKNOWN'))}`",
                    f"- 说明：{item.get('details_zh', item.get('note', '没有附加说明。'))}",
                    f"- 来源：`{item.get('source_reference', 'UNKNOWN')}`",
                    "",
                ]
            )

        lines.extend(["## 检查盲区", ""])
        for item in snapshot.get("blind_spots", []):
            lines.extend(
                [
                    f"### {item.get('title_zh', '未评估盲区')} · `{item.get('status', 'NOT_ASSESSED')}`",
                    "",
                    f"- 状态：`{item.get('status', 'NOT_ASSESSED')}`",
                    f"- 影响：{item.get('impact_zh', '缺少足够证据。')}",
                    "",
                ]
            )
        lines.extend(
            [
                "## 技术证据",
                "",
                f"- 机器总体状态：`{snapshot['overall_status']}`",
                f"- 原始观察时间：`{snapshot['observed_at']}`",
                f"- 逻辑 Cell 数量：{len(snapshot.get('logical_cells', snapshot.get('cell_runs', [])))}",
                f"- 依赖审计状态：`{snapshot.get('dependency_audit_state', {}).get('status', 'NOT_ASSESSED')}`",
                f"- 实时来源成功数：{snapshot.get('counts', {}).get('live_source_success', 0)}",
                f"- 来源未评估数：{snapshot.get('counts', {}).get('source_not_assessed', 0)}",
                f"- 上轮实时制品已读取：`{memory.get('PREVIOUS_LIVE_ARTIFACT_LOADED', False)}`",
                "",
                "固定问题仅查询当前快照，不访问外部服务，也不产生执行命令。",
                "",
            ]
        )
        return "\n".join(lines)

    def _run(self, context: dict[str, Any]):
        snapshot = context.get("snapshot", {})
        output_dir = context.get("output_dir")
        if not snapshot or not output_dir:
            return make_result(self.cell_id, "NOT_ASSESSED", "Snapshot or output directory was unavailable.")
        paths = self.render(snapshot, output_dir)
        return make_result(
            self.cell_id,
            "PASS",
            "Standalone HTML and Markdown were rendered from the standardized snapshot only.",
            observations=[{"artifacts": paths, "snapshot_only": True}],
            outputs={"human_view_artifacts": paths},
        )
