---
document_id: DBA-TITMAS-PUBLIC-FRONT-DOOR-MIGRATION-PLAN-0.1
title: TITMAS Public Front Door Migration Plan v0.1
title_zh: TITMAS 对外入口迁移计划 v0.1
version: 0.1.0
status: source-preparation-active-external-cutover-pending
maturity: Development
maturity_scope: entire-document
owner_ref: NOT_ASSIGNED
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Development document; no implementation compatibility claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: non-runtime-public-entry-migration-plan
decision_reference: ADR-030-titmas-public-front-door-and-github-slug.md
future_primary_domain: https://titmas.cn/
current_primary_domain: https://redcrag.cn/
github_organization_slug: titmas-cn
domain_filing_status: pending
external_cutover_authorized: false
repository_transfer_authorized: false
---

# TITMAS Public Front Door Migration Plan v0.1

## 1. Outcome（目标结果）

建立一个第一次接触者能立即理解、国内可直接访问、智能体可检索的 TITMAS 统一入口：

```text
https://titmas.cn/
  -> TITMAS Infrastructure Developer Community
  -> Trusted Multi-Agent Infrastructure
  -> Architecture / Specifications / Adapters / Conformance / Status
```

本计划迁移 public front door（公开入口），不重命名 Digital Biosphere 总项目，不合并
DBA、DBOS 或 SAEE，不创建 Agent Platform、Foundation 或第二套治理权力。

## 2. Current Truth（当前事实）

| Surface | Current truth | Target |
|---|---|---|
| Public website | `https://redcrag.cn/` 已上线并通过既有健康／回滚验证 | `https://titmas.cn/` |
| New domain | 已选择，备案中 | 备案、DNS、TLS、健康和回滚通过 |
| GitHub owner | `joy7758` 保存当前公开仓库 | `titmas-cn` selected, not created |
| Community | Strategy adopted; contributor entry prepared | 仍需公共贡献独立授权 |
| Website source | 中英文与 agent-readable 基础已存在 | 以 TITMAS 社区为首屏、资料自包含 |

```text
TITMAS_CN_FILING_STATUS=PENDING
TITMAS_CN_LIVE=false
REDCRAG_CN_REMAINS_LIVE=true
GITHUB_ORGANIZATION_SLUG_SELECTED=titmas-cn
GITHUB_ORGANIZATION_CREATED=false
```

## 3. Information Architecture（信息架构）

网站必须直接提供以下内容，不要求访问者先打开 GitHub：

1. TITMAS 是什么、解决什么问题、不是什么；
2. DBA、DBOS、SAEE 与 Digital Entities 的职责；
3. Identity、Capability、Execution、Evidence 四条可信边界；
4. Specification、Adapter Contract、Conformance、Reference Implementation 的贡献表面；
5. 当前 Developer Preview、生产就绪、社区和公共贡献真实状态；
6. 中英文首页、社区入口、状态页；
7. `llms.txt`、`agent-index.json`、`status.json`、`titmas-community.json`；
8. 当前可验证资源和未来 GitHub 组织状态；
9. Evidence／Truth、Evaluation／Authority、Recommendation／Decision、
   Decision／Execution 的非等价规则。

## 4. Phased Migration（分阶段迁移）

### Phase 0 — Name selection

状态：`PASS`。

- domain：`titmas.cn`；
- GitHub slug：`titmas-cn`；
- current live domain：`redcrag.cn`。

### Phase 1 — Source preparation

状态：`ACTIVE`。

- 把网站首屏改为 TITMAS Infrastructure Developer Community；
- 保持 `redcrag.cn` 为当前 metadata base 和 canonical URL；
- 加入备案中、GitHub slug selected/not created、community not established 的明确状态；
- 新增 `/community/`、`/en/community/` 与 `titmas-community.json`；
- 保留中英文和机器入口内容完整性测试。

完成条件：

```text
SITE_BUILD_PASS=true
ZH_EN_COMMUNITY_PARITY_PASS=true
AGENT_READABLE_COMMUNITY_ENTRY_PASS=true
FUTURE_DOMAIN_NOT_CLAIMED_LIVE=true
```

### Phase 2 — Filing confirmation

状态：`PENDING_EXTERNAL_EVIDENCE`。

需要：

- 可核验备案完成信息；
- 域名主体与网站责任方确认；
- 公安备案或其他适用要求的后续清单，不从 ICP 状态自动推断；
- 决定是否继续使用当前百度云主机。

### Phase 3 — DNS, TLS and candidate health

状态：`NOT_AUTHORIZED`。

执行前要求：

- exact DNS records 与 TTL；
- `titmas.cn` 和 `www.titmas.cn` 路由；
- 对应域名 TLS 证书；
- HTTP→HTTPS；
- HTML、JSON、TXT、XML MIME 与 security headers；
- 中英文、机器入口、匿名访问、404 和回滚验证。

### Phase 4 — Canonical cutover

状态：`NOT_AUTHORIZED`。

只有 Phase 3 全部通过后：

- metadata base、structured data、sitemap、robots 和机器资源从 `redcrag.cn`
  切至 `titmas.cn`；
- `redcrag.cn` 先保留可回滚，再配置 path-preserving 301；
- release manifest 记录切换前后 source revision、hash、时间和 rollback target。

### Phase 5 — GitHub organization

状态：`SLUG_SELECTED_CREATION_NOT_AUTHORIZED`。

按
[GitHub Organization Information Architecture](titmas-github-organization-information-architecture-v0.1.md)
建立 profile candidate。Organization 创建后也不能自动开放 Issue、Discussion、PR 或转移仓库。

### Phase 6 — Repository migration

状态：`NOT_AUTHORIZED`。

每个仓库独立完成：

- canonical truth owner 与 Owner；
- public/private decision；
- secrets、absolute path、license、release assets、Actions 和 Pages audit；
- remote/link/package/import impact；
- redirect 和 rollback；
- clean clone、tests、validators 与 public link verification。

## 5. Release Matrix（发布矩阵）

| Claim | During filing | After source validation | After cutover |
|---|---:|---:|---:|
| `titmas.cn` selected | yes | yes | yes |
| `titmas.cn` live | no | no | only after direct checks |
| website source prepared | no/partial | yes | yes |
| website deployed at `redcrag.cn` | existing fact | unchanged until deployment | redirect or archive by decision |
| GitHub slug selected | yes | yes | yes |
| GitHub Organization created | no | no | only after explicit execution |
| Community established | no | no | separate governance decision |
| Public contribution enabled | no | no | separate governance decision |

## 6. Rollback（回滚）

任何切换失败时：

1. 保留失败记录；
2. 恢复 `redcrag.cn` 的 existing release pointer；
3. 恢复旧 canonical metadata；
4. 不把 DNS 可解析写成网站健康；
5. 不把 Organization 创建写成仓库迁移完成；
6. 在状态页公开 current live URL 和 known limitation。

## 7. Exit Criteria（完成条件）

```text
DOMAIN_FILING_CONFIRMED=true
TITMAS_CN_DNS_PASS=true
TITMAS_CN_TLS_PASS=true
TITMAS_CN_BILINGUAL_CONTENT_PASS=true
TITMAS_CN_MACHINE_ENTRY_PASS=true
TITMAS_CN_SECURITY_HEADERS_PASS=true
TITMAS_CN_ROLLBACK_PASS=true
REDCRAG_REDIRECT_VERIFIED=true
GITHUB_PUBLIC_ENTRY_DECIDED=true
```

上述条件只表示 public front door migration（公开入口迁移）完成，不表示 Community、
Adoption、Production、Agent、Runtime、Permission 或 Foundation 已建立。
