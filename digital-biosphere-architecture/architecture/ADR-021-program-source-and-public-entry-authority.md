---
adr_id: ADR-021
title: Program Source Routing and Public Entry Authority
title_zh: 项目群来源路由与公开入口权威决定
status: accepted-governance-routing
decided_at: 2026-07-22T00:24:02+08:00
decided_by_ref: zhangbin
program_owner_ref: zhangbin
domain_owner_confirmation: confirmed
governance_implementation_authorized: true
git_delivery_authorized: true
child_repository_write_effect: none
runtime_effect: none
release_authorized: false
---

# ADR-021: Program Source Routing and Public Entry Authority（项目群来源路由与公开入口权威决定）

## Context（背景）

[`../PROGRAM-SOURCE-AND-RESPONSIBILITY-DECISION-PACKET.md`](../PROGRAM-SOURCE-AND-RESPONSIBILITY-DECISION-PACKET.md)
已完成 `DQ-003`、`DQ-007`、`DQ-008` 的来源候选、责任链、freshness（新鲜度）、冲突规则
和重复建设停止条件审查。2026-07-22，Human Program Owner（人类项目群负责人）明确回复：

> 确认，给予完全授权。

本 ADR 将该授权解释为对 decision packet（决策包）推荐方案的接受，以及对 DBA 治理文档、
机器可读 registry、受控 Git commit / push 和 draft PR（草稿拉取请求）的授权。它不把“完全
授权”扩写为子项目代码写入、Runtime、Adapter、Agent、Permission、外部试用、独立验证、
Developer Preview Release 或 Production Authorization（生产授权）。

## Decision（决策）

### DQ-003 — Canonical Status Source Routing（规范状态来源路由）

Human Program Owner 以 `zhangbin` 身份确认以下 DBA reference routing（引用路由）：

| project_id | program-level status source | scoped fact source | 冲突规则 |
|---|---|---|---|
| `PROJECT-DBOS` | `README.md` | `registry/*` 中各对象明确声明的 canonical source | 保留冲突并请求 DBOS Domain Owner；README 不覆盖对象 registry |
| `PROJECT-SAEE` | `PROJECT_STATUS.md` | `capability-package/manifest.json#canonical_inventory` 是 sole canonical capability fact source | capability inventory 优先于活动日志、报告、README 和旧 repository snapshot |
| `RESEARCH-AGENT-PILOT` | `README.md#Current Status` | `CONSTITUTION.md` 负责沟通与 truth boundary；`AGENTS.md` 负责 Agent 路由 | `NOT_READY`、`DRAFT`、`UNKNOWN` 和零实例状态不得由 DBA 升级 |

DBA 只读取、引用并带时间记录上述来源，不成为子项目状态事实权威。若 program-level source
与 scoped fact source 冲突，DBA 必须记录 `CONFLICTED`，以 scoped fact source 约束相应事实，
并请求 Domain Owner 处理；不得静默选择对项目更有利的状态。

```text
DQ_003_DECISION=ACCEPTED
CORE_STATUS_SOURCE_ROUTING_CONFIRMED=true
DBA_WRITES_CHILD_STATUS=false
README_OVERRIDES_SCOPED_CANONICAL_FACTS=false
UNKNOWN_MUST_REMAIN_UNKNOWN=true
```

### DQ-007 — Manual Refresh Policy（人工刷新策略）

当前选择 `MANUAL_REFRESH_BEFORE_CONSEQUENTIAL_GATE`，不创建自动 adapter：

- 每次发布、试用、跨项目 gate、Portfolio Admission 或对外状态同步前必须刷新；
- 普通 point-in-time snapshot（时间点快照）超过 24 小时即标记 `STALE`；
- 每次刷新记录 `observed_at`、repository path、branch、commit/version、source ref 和冲突；
- concurrent worktree drift（并发工作树漂移）只记录，不推断作者、原因或成熟度；
- 未来只有在单独 proposal、security review 和 Human Decision 后才能建立只读 adapter；
- adapter 即使建立，也不得写回子项目或自动改变状态。

```text
DQ_007_DECISION=MANUAL_REFRESH_BEFORE_CONSEQUENTIAL_GATE
SNAPSHOT_STALE_AFTER_HOURS=24
READ_ONLY_ADAPTER_AUTHORIZED=false
AUTOMATIC_CHILD_WRITEBACK=false
```

### DQ-008 — Cockpit and Public Meaning Layer Relationship（驾驶舱与公开语义层关系）

确认以下规范关系：

1. 当前 Program Governance Cockpit 是 Digital Biosphere 的 canonical Program Governance
   and Architecture Specification source（规范项目群治理与架构规范来源）；
2. 既有 Digital Biosphere Architecture public meaning layer 保留 public meaning、history
   and public discovery reference（公开语义、历史与发现引用）角色；
3. 单一公开信息前门是本 cockpit 中的 `PUBLIC-PROJECT-OVERVIEW.md`；`redcrag.cn` 是其当前
   website candidate projection（网站候选投影），在 `DQ-009` 前不得称为正式 Developer
   Preview Release；
4. public meaning layer 应通过显式交叉引用指向 canonical cockpit，不复制易漂移的 Program
   Status、Decision Queue、Risk Register 或 Release 状态；
5. 本决定不删除、合并或重写既有仓库与历史；跨仓库交叉引用实现继续作为独立 work item。

```text
DQ_008_DECISION=ACCEPTED
CANONICAL_PROGRAM_GOVERNANCE_SOURCE=DBA_PROGRAM_GOVERNANCE_COCKPIT
CANONICAL_PUBLIC_INFORMATION_ENTRY=PUBLIC-PROJECT-OVERVIEW.md
PUBLIC_WEBSITE_ROLE=WEBSITE_CANDIDATE_PROJECTION_NOT_RELEASE
PUBLIC_MEANING_LAYER_ROLE=PUBLIC_MEANING_HISTORY_AND_DISCOVERY_REFERENCE
SILENT_OVERWRITE_ALLOWED=false
SILENT_DELETE_ALLOWED=false
CROSS_REPOSITORY_REFERENCE_IMPLEMENTED=false
```

## Authorization Scope（授权范围）

本轮“完全授权”的可执行范围为：

```text
DBA_GOVERNANCE_DOCUMENT_ALIGNMENT_AUTHORIZED=true
DBA_MACHINE_READABLE_REGISTRY_ALIGNMENT_AUTHORIZED=true
DBA_VALIDATION_AUTHORIZED=true
SCOPED_GIT_BRANCH_COMMIT_PUSH_AUTHORIZED=true
DRAFT_PR_AUTHORIZED=true
CHILD_REPOSITORY_WRITE_EXECUTED=false
RUNTIME_IMPLEMENTATION_AUTHORIZED=false
ADAPTER_IMPLEMENTATION_AUTHORIZED=false
EXTERNAL_TRIAL_EXECUTION_AUTHORIZED=false
DEVELOPER_PREVIEW_RELEASE_AUTHORIZED=false
PRODUCTION_AUTHORIZED=false
INDEPENDENT_VALIDATION_CLAIM_AUTHORIZED=false
```

Git delivery（Git 交付）只发布本 ADR 及其 DBA 治理闭包。它不触发 `DQ-009`、不补造
`participant_source`、不添加 DBOS collaborator，也不执行跨仓库 public meaning layer 修改。

## Agent Recommendation Review（智能体推荐复核）

来源权威、责任链、freshness 与冲突规则已经明确，因此：

```text
INITIAL_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
OWNER_CONFIRMATION_RECEIVED=true
SOURCE_ROUTING_CONFIRMED=true
RESPONSIBILITY_CHAIN_CONFIRMED=true
FINAL_RECOMMENDATION=RECOMMENDED_FOR_PROGRAM_GOVERNANCE_AND_SOURCE_ROUTING
RECOMMENDED_FOR_RUNTIME_IMPLEMENTATION=false
RECOMMENDED_FOR_EXTERNAL_TRIAL_EXECUTION=false
RECOMMENDED_FOR_FORMAL_RELEASE=false
```

智能体现在可以推荐本 cockpit 用于 Program Governance、Architecture Specification、
source routing 和 bounded local evidence evaluation（有界本地证据评价）。在真实外部验证、
身份／委托绑定、试用结果和 Release Authority 缺失时，仍不会推荐端到端生产信任或正式发布。

## Consequences（影响）

- `DQ-003`、`DQ-007`、`DQ-008` 从开放队列移入已关闭决定；
- `M2` 达到 `GATE_PASSED`，但不会自动启动 `M3`；
- `B-003` 解除，`R-003` 与 `R-008` 转入 resolved-by-governance（由治理解决）；
- `R-010` 降级但保持 active，直到既有 public meaning layer 完成显式交叉引用；
- `B-005` 保持为 cross-repository reference implementation pending（跨仓库引用实现待完成）；
- `DQ-006`、`DQ-009` 和 `B-008` 不受本决定影响。

## Non-effects（非效果）

```text
HUMAN_CONFIRMATION_NE_RUNTIME=true
HUMAN_CONFIRMATION_NE_EXTERNAL_VALIDATION=true
GOVERNANCE_DECISION_NE_CHILD_PROJECT_FACT=true
SOURCE_ROUTING_NE_SOURCE_CONTENT_TRUTH=true
M2_GATE_PASS_NE_M3_EXECUTION=true
PUBLIC_ENTRY_DECISION_NE_RELEASE=true
COMMIT_PUSH_NE_ADOPTION=true
AGENT_CREATED=false
RUNTIME_CREATED=false
PERMISSION_GRANTED=false
RELEASE_CREATED=false
```
