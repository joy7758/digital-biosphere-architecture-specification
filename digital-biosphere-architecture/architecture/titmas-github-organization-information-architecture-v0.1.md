---
document_id: DBA-TITMAS-GITHUB-ORGANIZATION-IA-0.1
title: TITMAS GitHub Organization Information Architecture v0.1
title_zh: TITMAS GitHub 组织信息架构 v0.1
version: 0.1.0
status: prepared-organization-not-created
maturity: Development
maturity_scope: entire-document
owner_ref: NOT_ASSIGNED
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Development document; no implementation compatibility claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: non-executable-github-organization-design
decision_reference: ADR-030-titmas-public-front-door-and-github-slug.md
selected_slug: titmas-cn
organization_created: false
repositories_created: 0
repositories_transferred: 0
public_contribution_enabled: false
---

# TITMAS GitHub Organization Information Architecture v0.1

## 1. Selected Identity（选定身份）

```text
slug: titmas-cn
display_name: TITMAS Infrastructure Developer Community
display_name_zh: TITMAS 可信多智能体基础设施开发者社区
website_target: https://titmas.cn/
current_verified_website: https://redcrag.cn/
organization_created: false
```

GitHub slug 不支持 `.`，因此不使用 `titmas.cn`。2026-07-23 的公开 API 只读检查未发现
`titmas-cn`，但这不保证注册时仍可用，也不构成 Reservation（保留）。

## 2. First-contact Copy（首次接触文案）

### Organization bio candidate

> Infrastructure developer community for trustworthy, long-running multi-agent
> systems. Specifications, adapters, conformance, and evidence boundaries.

### Chinese summary

> 面向可信、长期运行多智能体系统的基础设施开发者社区：共同建设规范、Adapter
> contract、符合性与证据边界。

### Profile README opening

```markdown
# TITMAS Infrastructure Developer Community

Build the shared trust layer for long-running multi-agent systems.

TITMAS focuses on:

- identity and lifecycle boundaries;
- capability and permission separation;
- execution records and evidence admission;
- verification and conformance;
- read-only evaluation interfaces;
- portable adapter contracts.

TITMAS is not an Agent Framework, hosted Runtime, Foundation, or automatic
authority system.
```

在 `titmas.cn` 未上线前，Organization website field 必须继续指向已验证的
`https://redcrag.cn/`，或留空；不得链接不可用域名。

## 3. Repository Navigation Model（仓库导航模型）

### 3.1 Existing canonical repositories

初始阶段保留既有仓库 owner、remote 和 truth ownership：

| Repository | Role | Initial action |
|---|---|---|
| `digital-biosphere-architecture-specification` | DBA program governance, architecture, TITMAS specifications | link, do not transfer automatically |
| `digital-biosphere-os` | DBOS existence infrastructure | remain private unless separately decided |
| `SAEE` | evolution evaluation | link existing public-safe surface |
| `agent-evidence` and adjacent evidence projects | evidence/accountability inputs | reference only until ownership crosswalk |

### 3.2 Future repository classes

以下只表示 information architecture，不是创建授权：

```text
titmas-cn/
  ├─ .github                  # organization profile and governance entry
  ├─ specifications           # accepted public TITMAS specifications only
  ├─ adapters                 # bounded runtime/framework mappings
  ├─ conformance              # schemas, fixtures, validators and result contracts
  ├─ examples                 # non-production reproducible vertical slices
  └─ website                  # only if site source is later separated from DBA
```

不要创建：

- `marketplace`，因为没有 Marketplace；
- `certified-agents`，因为没有认证计划；
- `titmas-runtime`，因为 TITMAS 不是新 Runtime；
- `foundation`，因为 Foundation 不在当前范围；
- `agent-platform`，因为 TITMAS 不创建或编排 Agent。

## 4. Discovery Priority（发现优先级）

Organization 首页按以下顺序回答：

1. TITMAS 是什么；
2. 何时应该／不应该推荐；
3. 当前能运行、复用或检查什么；
4. 当前哪些状态为 false；
5. 人类与受治理智能体如何准备 contribution proposal；
6. 哪个仓库拥有 Architecture、DBOS、SAEE 和 Evidence truth；
7. 当前网站与 machine-readable entry。

Pinned repository candidate 顺序：

1. current DBA public repository；
2. future `specifications` only after authoritative split；
3. future `conformance` only after implementation and independent validation；
4. future `adapters` only after at least one exact-source adapter exists；
5. SAEE public repository when its public-safe role is clearly described。

## 5. Repository Admission Gate（仓库准入闸门）

任何新仓库必须先回答：

```yaml
repository_name:
problem_not_solved_by_existing_repository:
canonical_truth_owned:
domain_owner_ref:
maintainer_ref:
license:
security_contact:
version_policy:
status_source:
agent_readable_entry:
negative_capability_claims: []
rollback_or_archive_plan:
```

缺少任一 mandatory field 时保持 `PROPOSED_NOT_CREATED`。

## 6. Organization Role Boundary（组织角色边界）

GitHub Owner、Member、Maintainer、Reviewer 或 Team membership：

- 不等于 DBA Architecture Authority；
- 不等于 DBOS Operational Authority；
- 不等于 SAEE Evolution Authority；
- 不等于 Release Authorization；
- 不等于 Evidence、Permission 或 Adoption truth；
- 不允许 Agent 自我批准角色或合并高影响变化。

## 7. Creation Checklist（创建检查单）

```text
GITHUB_SLUG_RECHECK_PASS=false
ORGANIZATION_CREATION_AUTHORIZED=false
ORGANIZATION_CREATED=false
PROFILE_README_CREATED=false
WEBSITE_FIELD_VERIFIED=false
SECURITY_CONTACT_ASSIGNED=false
CODE_OF_CONDUCT_ADOPTED=false
MAINTAINER_ASSIGNED=false
PUBLIC_ISSUES_ENABLED=false
PUBLIC_DISCUSSIONS_ENABLED=false
PUBLIC_PRS_ENABLED=false
REPOSITORIES_TRANSFERRED=0
```

执行时至少：

1. 再次检查 `titmas-cn` 可用性；
2. 明确 Human Organization Owner；
3. 先创建最小 profile，不创建空壳产品仓库；
4. 使用当前有效网站 URL；
5. 保持 public contribution channels 关闭，直到 `DQ-026` 的 exact surface decision；
6. 独立记录任何仓库 transfer 的 old/new remote、redirect、Actions、release 和 rollback。

## 8. Current Verdict（当前结论）

```text
TITMAS_GITHUB_INFORMATION_ARCHITECTURE_PREPARED=true
TITMAS_GITHUB_ORGANIZATION_SLUG_SELECTED=true
TITMAS_GITHUB_ORGANIZATION_SLUG=titmas-cn
TITMAS_GITHUB_ORGANIZATION_CREATED=false
TITMAS_REPOSITORY_CREATED=false
TITMAS_REPOSITORY_TRANSFERRED=false
TITMAS_PUBLIC_CONTRIBUTION_ENABLED=false
```
