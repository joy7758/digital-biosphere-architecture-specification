---
adr_id: ADR-030
title: Adopt titmas.cn and titmas-cn as TITMAS Public Front Door Targets
title_zh: 采纳 titmas.cn 与 titmas-cn 作为 TITMAS 对外入口目标
status: accepted-name-and-prelaunch-preparation
maturity: Development
maturity_scope: entire-document
owner_ref: NOT_ASSIGNED
decision_reference: ADR-030
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Development document; no implementation compatibility claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
decided_by_ref: zhangbin
decided_at: 2026-07-23
primary_repository: digital-biosphere-architecture
public_domain_selected: titmas.cn
public_domain_filing_status: pending
current_public_site: https://redcrag.cn/
github_organization_slug_selected: titmas-cn
github_organization_created: false
dns_cutover_authorized: false
repository_transfer_authorized: false
public_contribution_surface_authorized: false
authority_effect: none
---

# ADR-030: Adopt `titmas.cn` and `titmas-cn` as TITMAS Public Front Door Targets

中文：ADR-030——采纳 `titmas.cn` 与 `titmas-cn` 作为 TITMAS 对外入口目标。

## Context（背景）

TITMAS 已采纳 `TITMAS Infrastructure Developer Community`（TITMAS
可信多智能体基础设施开发者社区）战略方向，但公开入口仍以 `redcrag.cn` 和
`github.com/joy7758` 为主，第一次接触者难以把网站、代码与 TITMAS 名称直接对应。

Human Program Owner 已确认：

- `titmas.cn` 正在备案，预计仍需两至三天；
- GitHub 入口直接使用与 TITMAS 对齐的名称；
- 不等待备案即可推进文档、网站源码、双语内容、机器入口和 GitHub 信息架构准备。

GitHub owner／organization slug 不能包含句点，因此 `titmas.cn` 不能作为 GitHub slug。
2026-07-23 对 GitHub public API 的只读检查返回 `404 Not Found`，说明
`titmas-cn` 当前没有可见的公开用户或组织；这不是 GitHub 名称保留证明。

## Decision（决定）

采纳以下公开入口目标：

```text
Brand: TITMAS
Community: TITMAS Infrastructure Developer Community
Community zh: TITMAS 可信多智能体基础设施开发者社区
Technical positioning: Trusted Multi-Agent Infrastructure
Future primary domain: https://titmas.cn/
Selected GitHub organization slug: titmas-cn
Current public site: https://redcrag.cn/
```

同时决定：

1. 允许在 DBA 内准备网站源码、双语页面、agent-readable（智能体可读）入口、迁移清单、
   GitHub Organization profile copy 和 repository information architecture；
2. `titmas.cn` 在备案、DNS、TLS、健康检查、机器入口和回滚全部通过前不得写成已上线；
3. `redcrag.cn` 在新域名完成公开验证前继续作为 canonical live site（当前规范在线站点）；
4. `titmas-cn` 是选定 GitHub slug，不表示 Organization 已创建或名称已被保留；
5. GitHub Organization 创建、公开贡献渠道、仓库转移和 redirect 分别需要执行确认；
6. 网站和 GitHub 首屏以 TITMAS 基础设施开发者社区为入口，但必须披露
   `COMMUNITY_ESTABLISHED=false` 与 `PUBLIC_CONTRIBUTION_ENABLED=false`；
7. 品牌迁移不改变 DBA、DBOS、SAEE、TMAP、EEOAP 或任何仓库的 Authority、Ownership、
   Capability、Evidence 或 Release truth。

## Name Hierarchy（名称层级）

| 层级 | 规范名称 | 用途 |
|---|---|---|
| 总项目 | Digital Biosphere | 长期愿景与项目群 |
| 对外品牌 | TITMAS | 网站、GitHub 和首次接触入口 |
| 社区 | TITMAS Infrastructure Developer Community | 开发者生态方向 |
| 技术定位 | Trusted Multi-Agent Infrastructure | 解释解决的基础设施问题 |
| 治理层 | DBA | 项目群治理与架构规范 |
| 存在层 | DBOS | 身份、生命周期、执行记录、证据与验证边界 |
| 演化层 | SAEE | 评价、风险、稳定性与演化建议 |

## Alternatives Considered（备选方案）

### A. GitHub 使用 `titmas.cn`

拒绝。GitHub slug 不支持句点。

### B. 备案期间暂停全部工作

拒绝。双语内容、机器入口、迁移验证和 GitHub 信息架构不依赖 DNS 切换。

### C. 备案完成前把所有 canonical URL 改为 `titmas.cn`

拒绝。未上线域名不能替代当前可验证的 `redcrag.cn`。

### D. 立即转移全部仓库

拒绝。仓库转移会改变 remote、链接、CI、release assets 和权限边界，需要独立 inventory、
redirect、rollback 和 Human Execution Decision。

## Consequences（影响）

正面影响：

- 网站、GitHub 与 TITMAS 名称一致；
- 国内无法稳定访问 GitHub 的用户仍可从网站获得完整中英文资料和机器入口；
- 备案等待期可用于完成不依赖外部切换的准备；
- 避免把域名选择误写成上线，把 slug 选择误写成 Organization 创建。

代价与限制：

- 迁移期间会同时存在 `redcrag.cn`、未来 `titmas.cn` 和个人 GitHub 仓库入口；
- 所有公开材料必须明确 current／future URL，避免 canonical drift；
- GitHub 公开 404 检查不能保证 `titmas-cn` 后续仍可注册；
- 网站源码完成不等于已部署，Organization profile 文案完成不等于 Organization 已创建。

## Execution Gates（执行闸门）

```text
GATE_1_SOURCE_AND_CONTENT_PREPARATION=AUTHORIZED
GATE_2_DOMAIN_FILING_CONFIRMATION=PENDING
GATE_3_DNS_TLS_AND_HEALTH_CUTOVER=NOT_AUTHORIZED
GATE_4_REDCRAG_REDIRECT=NOT_AUTHORIZED
GATE_5_GITHUB_ORGANIZATION_CREATION=NOT_AUTHORIZED
GATE_6_REPOSITORY_TRANSFER=NOT_AUTHORIZED
GATE_7_PUBLIC_CONTRIBUTION_ENABLEMENT=NOT_AUTHORIZED
```

## Explicit Non-effects（明确非效果）

```text
TITMAS_PUBLIC_DOMAIN_SELECTED=true
TITMAS_PUBLIC_DOMAIN_LIVE=false
TITMAS_GITHUB_ORGANIZATION_SLUG_SELECTED=true
TITMAS_GITHUB_ORGANIZATION_CREATED=false
TITMAS_REPOSITORY_CREATED=false
TITMAS_REPOSITORY_TRANSFERRED=false
TITMAS_PUBLIC_CONTRIBUTION_SURFACE_AUTHORIZED=false
TITMAS_DEVELOPER_COMMUNITY_ESTABLISHED=false
FOUNDATION_CREATED=false
AGENT_CREATED=false
RUNTIME_CREATED=false
ENTITY_CREATED=false
PERMISSION_GRANTED=false
DBOS_AUTHORITY_CHANGED=false
SAEE_AUTHORITY_CHANGED=false
```
