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
            "# DBA 每周驾驶舱",
            "",
            f"- 快照编号：`{snapshot['snapshot_id']}`",
            f"- 观察时间：`{snapshot['observed_at']}`",
            f"- 总体状态：`{snapshot['overall_status']}`",
            "",
            "## 本周一句话",
            "",
            snapshot["weekly_sentence_zh"],
            "",
            "## 本周需要人工决定",
            "",
        ]
        for item in snapshot["decisions"]:
            lines.append(
                f"- **{item['title_zh']}**：{item['why_zh']}"
                f"（负责人：{item['owner_conversation']}）"
            )
        lines.extend(["", "## 项目状态", ""])
        for project in snapshot["projects"]:
            lines.append(
                f"- **{project['display_name_zh']}**｜{project['status_zh']}："
                f"{project['why_zh']} 关注：{project['attention_zh']} "
                f"影响：{project['impact_zh']} 负责人：{project['owner_conversation']}。"
            )
        lines.extend(["", "## 新发现", ""])
        for item in snapshot["discoveries"]:
            lines.append(
                f"- **{item['title_zh']}**｜状态：`{item['status']}`｜"
                f"来源：`{item['source_reference']}`"
            )
        lines.extend(["", "## 检查盲区", ""])
        for item in snapshot["blind_spots"]:
            lines.append(
                f"- **{item['title_zh']}**｜状态：`{item['status']}`：{item['impact_zh']}"
            )
        lines.extend(
            [
                "",
                "## 只读边界",
                "",
                "- 本周报告是来源支持的只读观察视图，不是项目状态事实源。",
                "- 不产生自动修复、自动 PR、自动合并、自动部署或执行授权。",
                "- `NOT_ASSESSED`、`STALE` 和检查盲区保持原义，不翻译为正常或通过。",
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
