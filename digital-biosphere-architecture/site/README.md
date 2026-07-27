# TITMAS Infrastructure Developer Community Website

中英文双语、agent-readable（智能体可读）的 TITMAS Infrastructure Developer
Community（TITMAS 可信多智能体基础设施开发者社区）公开门户。

## Truth status

```text
SITE_IMPLEMENTED=true
STATIC_SITE_BUILD_PASS=true
ZH_EN_CONTENT_PARITY_PASS=true
AGENT_READABLE_ENTRY_PASS=true
SITE_DEPLOYED=true
SITE_URL=https://redcrag.cn/
ICP_FILING_APPROVED=true
ICP_RECORD_NUMBER=晋ICP备2026006409号-1
ICP_PUBLIC_QUERY_URL=https://beian.miit.gov.cn/
SITE_HEALTH_PASS=true
SITE_ROLLBACK_VALIDATED=true
DEVELOPER_PREVIEW_RELEASED=true
TITMAS_FUTURE_DOMAIN=titmas.cn
TITMAS_FUTURE_DOMAIN_FILING_STATUS=PENDING
TITMAS_FUTURE_DOMAIN_LIVE=false
TITMAS_GITHUB_ORGANIZATION_SLUG=titmas-cn
TITMAS_GITHUB_ORGANIZATION_CREATED=false
TITMAS_REDESIGN_SOURCE_PREPARED=true
TITMAS_REDESIGN_DEPLOYED=true
COMMERCIAL_EVALUATION_V0_2_SOURCE_PREPARED=true
COMMERCIAL_EVALUATION_V0_2_DEPLOYED=true
COMMERCIAL_EVALUATION_V0_2_DEPLOYED_SOURCE_REVISION=7da4bcf16eeec7de1c61031fe08fc04081cf8705
COMMERCIAL_EVALUATION_V0_2_LIVE_VALIDATION_PASS=true
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
| `/community` | 完整中文社区／开发者入口 |
| `/en/community` | Complete English community/developer entry |
| `/industries` | 完整中文制造业应用示例 |
| `/en/industries` | Complete English manufacturing application example |
| `/digital-cell` | TITMAS Digital Cell Demo v0.1 reference page |
| `/en/digital-cell` | English TITMAS Digital Cell Demo v0.1 reference page |
| `/llms.txt` | LLM-readable（大模型可读）项目入口 |
| `/agent-index.json` | Agent discovery（智能体发现）索引 |
| `/status.json` | 机器可读验证状态 |
| `/titmas-community.json` | TITMAS 名称、域名、GitHub、贡献表面、边界和 false effects |
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

首页信息架构进一步参考 OpenTelemetry 与 OpenAI 官网“首页只承载定位和入口、详情由
导航分流”的原则：保留现有色调，将详细治理状态、贡献流程和内部责任域放回 Status /
Developers 页面；首页只保留 Infrastructure、Industry Applications 与 bounded Demo。

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=SIMPLIFIED_INFRASTRUCTURE_PUBLIC_ENTRY
NOT_RECOMMENDED_AS=INDUSTRY_SOLUTION_OR_PRODUCTION_PLATFORM
REASON_FIXED=HOMEPAGE_NO_LONGER_DUPLICATES_DETAILED_STATUS_AND_GOVERNANCE_SECTIONS
REMAINING_CONDITION=DEVELOPER_PREVIEW_AND_REFERENCE_DEMO_BOUNDARIES_MUST_REMAIN_VISIBLE
IMPLEMENTATION_AUTHORIZATION_SOURCE=USER_REQUEST_2026_07_27
DEPLOYMENT_AUTHORIZED=false
```

## Deployment boundary

Developer Preview v0.1 的 TITMAS 明亮版已部署到 `https://redcrag.cn/`；本轮
Commercial Evaluation Pack v0.2（商业评估包 v0.2）已按精确 source revision
`7da4bcf16eeec7de1c61031fe08fc04081cf8705` 部署并通过中英文入口、机器清单、
边界状态、安全头和 HTTP→HTTPS 重定向验证。
`titmas.cn` 正在备案且尚未上线，因此当前 metadata base、sitemap 和机器资源继续使用
`redcrag.cn`。新版本与新域名部署都必须继续通过 manifest hash、Nginx、健康、
安全头和回滚边界验证。Deployment（部署）不等于 Production Readiness（生产就绪）
或 Adoption（采用）。
