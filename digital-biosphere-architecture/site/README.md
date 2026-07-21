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
DEVELOPER_PREVIEW_RELEASED=false
```

这个目录是网站实现，不是 DBOS Runtime（运行时）、SAEE Evaluation
Runtime（评价运行时）或 Agent（智能体）实现。页面将当前项目称为
`Developer Preview Candidate in preparation`（正在准备的开发者预览候选），
不构成正式发布或生产可用性声明。

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

## Local validation

Requires Node.js `>=22.13.0`.

```bash
npm install
npm run dev
npm test
npm run release:static
```

`npm test` 会重新构建网站，并验证中英文入口、状态边界和机器可读资源。
`npm run release:static` 会生成带 SHA-256 清单的 `out/` 静态部署包；该目录
被 Git 忽略，不作为源码事实提交。

每次构建都会先清空 `dist/` 和 `.vinext/`，避免旧资源混入新的发布清单。

## Design boundary

视觉系统参考 OpenTelemetry 官网的清晰导航、深色 Hero（首屏）、亮色强调、
模块化能力卡片和多语言入口，但不复制其 Logo、插图、文案或项目事实。

## Deployment boundary

网站候选已部署到 `https://redcrag.cn/`，并完成健康检查和回滚验证。
网站部署不等于 Developer Preview（开发者预览）发布；正式发布仍保留独立
人工决定与跨项目闸门。
