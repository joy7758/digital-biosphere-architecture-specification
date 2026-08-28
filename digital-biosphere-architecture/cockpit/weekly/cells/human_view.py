"""Render the weekly snapshot as a standalone human-facing artifact."""

from __future__ import annotations

import html
import json
from pathlib import Path
from typing import Any

try:
    from cockpit.weekly.cells import WeeklyCell, make_result
except ModuleNotFoundError:
    from cells import WeeklyCell, make_result


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
        lines = [
            "# DBA Weekly Cockpit",
            "",
            f"- Snapshot: `{snapshot.get('snapshot_id', 'UNKNOWN')}`",
            f"- As of: `{snapshot.get('as_of', 'UNKNOWN')}`",
            f"- Status: `{snapshot.get('overall_status', 'UNKNOWN')}`",
            "",
            "## 本周需要人工决定",
            "",
        ]
        for item in snapshot.get("decisions", []):
            lines.append(f"- **{item.get('title', '未命名')}**：{item.get('why', '无说明')}")
        lines.extend(["", "## 项目状态", ""])
        for project in snapshot.get("project_views", []):
            lines.append(
                f"- **{project.get('display_name', project.get('project_id'))}** "
                f"`{project.get('status', 'UNKNOWN')}`：{project.get('human_summary', '')}"
            )
        lines.extend(
            [
                "",
                "> 该报告是 source-backed 的只读视图，不是权限、发布、执行或事实真相对象。",
                "",
            ]
        )
        return "\n".join(lines)

    def _run(self, context: dict[str, Any]):
        snapshot = context.get("snapshot", {})
        output_dir = context.get("output_dir")
        if not snapshot or not output_dir:
            return make_result(self.cell_id, "NOT_ASSESSED", "缺少快照或输出目录，未生成视图。")
        paths = self.render(snapshot, output_dir)
        return make_result(
            self.cell_id,
            "PASS",
            "已生成独立 HTML 与 Markdown 人类视图。",
            observations=[{"artifacts": paths, "snapshot_only": True}],
        )
