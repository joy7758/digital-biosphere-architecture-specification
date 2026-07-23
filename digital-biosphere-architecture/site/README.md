# Trusted Multi-Agent Infrastructure Website

中英文双语、agent-readable（智能体可读）的 Trusted Multi-Agent
Infrastructure（可信多智能体基础设施）公开门户。

## Truth status

```text
SITE_IMPLEMENTED=true
STATIC_SITE_BUILD_PASS=true
ZH_EN_CONTENT_PARITY_PASS=true
AGENT_READABLE_ENTRY_PASS=true
SITE_DEPLOYED=true
SITE_URL=https://redcrag.cn/
SITE_HEALTH_PASS=true
SITE_ROLLBACK_VALIDATED=true
DEVELOPER_PREVIEW_RELEASED=true
```

这个目录是网站实现，不是 DBOS Runtime（运行时）、SAEE Evaluation
Runtime（评价运行时）或 Agent（智能体）实现。页面将当前项目称为
`Developer Preview v0.1`（开发者预览版 v0.1）。正式发布不构成生产可用性、
客户采用、Runtime 或 Permission 声明。

## Routes

| Route | Purpose |
|---|---|
| `/` | 中文首页 |
| `/en` | English home |
| `/status` | 中文状态页 |
| `/en/status` | English status page |
| `/llms.txt` | LLM-readable（大模型可读）项目入口 |
| `/agent-index.json` | Agent discovery（智能体发现）索引 |
| `/status.json` | 机器可读验证状态 |
| `/agent-customer-package.json` | AI agent 的适用／不适用、精确验证命令、组合流和当前阻塞 |
| `/dbos-public-package-manifest.json` | DBOS exact wheel 的验证、匿名下载、公开边界和已发布状态 |

## Local validation

Requires Node.js `>=22.13.0`.

```bash
npm install
npm run dev
npm test
npm run release:formal
```

`npm test` 会重新构建网站，并验证中英文入口、状态边界、机器可读资源及
candidate/formal release mode（候选／正式发布模式）的失败关闭规则。
`npm run release:formal` 使用 `ADR-022`、`released_by_ref=zhangbin`、固定 tag 和
exact wheel URL 执行失败关闭的正式导出，并生成带 SHA-256 清单的 `out/` 静态部署包；该目录
被 Git 忽略，不作为源码事实提交。

每次构建都会先清空 `dist/` 和 `.vinext/`，避免旧资源混入新的发布清单。

## Design boundary

视觉系统重度参考 OpenTelemetry 官网的明亮信息架构：白色与浅灰页面、紫色主色、
琥珀色与青色强调、清晰导航、模块化能力卡片、有限的高饱和状态区和多语言入口。
不复制其 Logo、插图、文案或项目事实。

## Deployment boundary

Developer Preview v0.1 已部署到 `https://redcrag.cn/`。正式部署必须继续通过
manifest hash、Nginx、健康、安全头和回滚边界验证。Deployment（部署）不等于
Production Readiness（生产就绪）或 Adoption（采用）。
