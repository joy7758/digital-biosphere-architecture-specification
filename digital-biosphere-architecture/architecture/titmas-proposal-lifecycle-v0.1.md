---
document_id: DBA-TITMAS-PROPOSAL-LIFECYCLE-0.1
title: TITMAS Proposal Lifecycle v0.1
title_zh: TITMAS 提案生命周期 v0.1
version: 0.1.0
status: proposal-lifecycle-defined-candidate
maturity: Development
maturity_scope: entire-document
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Development document; no implementation compatibility claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: non-executable-specification-process-candidate
architecture_domain: TITMAS
document_maturity: Development
owner_ref: NOT_ASSIGNED
decision_reference: NOT_DECIDED
public_process_enabled: false
implementation_authorized: false
authority_effect: none
---

# TITMAS Proposal Lifecycle v0.1

## 1. Lifecycle Overview（生命周期总览）

```text
Stage 0 Idea
  -> Stage 1 Draft
  -> Stage 2 Architecture Review
  -> Stage 3 Community Review Candidate
  -> Stage 4 Experimental Specification
  -> Stage 5 Reference Implementation
  -> Stage 6 Stable Specification
```

该图是目标流程，不表示所有阶段已经启用。当前没有公共 Community Review、Maintainer、
Reference Implementation、Stable Specification 或 Specification Authority。

每次转换都必须有显式 Entry、Exit、Review 和 Authority 记录。Rejected、Deferred、
Withdrawn、Superseded 和 Failed 状态必须保留。

## 2. Stage Definitions（阶段定义）

### Stage 0 — Idea

**Entry**

- 有明确问题、受影响用户或智能体工作流；
- 初步判断属于可信多智能体基础设施，而不是 Agent Framework 功能。

**Exit**

- 问题、范围、非目标、来源和已知重复被记录；
- 开发前 Agent Recommendation 已记录。

**Review**

- intake、duplicate、scope 和 obvious authority conflict review。

**Authority**

- 任何人或受治理智能体可准备 Idea；
- Idea 不产生 Review role、Decision、Authority 或工作分配。

### Stage 1 — Draft

**Entry**

- 使用 Proposal Template；
- contribution type、human accountability、source/version 和 false effects 完整。

**Exit**

- 对象、字段、状态、失败语义、兼容、Security/Privacy 和测试设计足够进入架构审查；
- Owner 缺失或冲突被显式标记。

**Review**

- source、terminology、link、negative cases、known unknowns。

**Authority**

- proposer 只拥有草拟责任；
- Draft 不代表 DBA、TITMAS、DBOS、SAEE 或任何社区认可。

### Stage 2 — Architecture Review

**Entry**

- Draft 完整；
- affected authority domains 和 required Domain Owner inputs 已列出。

**Exit**

- DBA/TITMAS/DBOS/SAEE/evidence-layer ownership 无第二 canonical Owner；
- breaking、security、privacy、compatibility 和 migration 风险有明确结论；
- 形成 `PASS_TO_NEXT_REVIEW`、`REVISE`、`REJECT` 或 `BLOCKED`。

**Review**

- Architecture Review 必需；
- 按触发条件增加 Domain Owner、Security 与 Compatibility Review。

**Authority**

- DBA Architecture Review 路由重大跨域规则；
- review result 不是 Human Architecture Decision。

### Stage 3 — Community Review Candidate

**Entry**

- Architecture Review 允许征求更广反馈；
- public contribution surface 若未授权，只能在 DBA 内作为候选材料存在。

**Exit**

- review window、参与范围、意见、异议、响应和 unresolved issues 可追溯；
- 形成下一阶段 Decision 请求或退回 Draft。

**Review**

- 未来 community feedback、implementation interest、domain expertise；
- 当前 `TITMAS_PUBLIC_CONTRIBUTION_ENABLED=false`，不得创建外部 Issue、PR 或招募。

**Authority**

- Community Review 只提供 input；
- 不产生 Architecture Decision、Specification Authority 或 Maintainer Assignment。

### Stage 4 — Experimental Specification

**Entry**

- 有明确 Human Architecture Decision 采纳 experimental scope；
- 版本、Owner、规范性文字、兼容、失败语义和 conformance plan 完整。

**Exit**

- 获得有来源的实现与互操作反馈；
- critical security/authority issues 已关闭或明确阻塞；
- 可以进入 Reference Implementation 阶段，或退回更早阶段。

**Review**

- Architecture、Specification、Security、Compatibility 和 affected Domain Owner。

**Authority**

- 只有显式 Decision 能建立 bounded experimental specification；
- `Experimental ≠ Standard`，不得宣称 Stable、adopted ecosystem standard 或 production。

### Stage 5 — Reference Implementation

**Entry**

- Experimental Specification 已有 exact version；
- implementation authorization、source Owner、license、security 与 test scope 另行批准。

**Exit**

- 实现声明 supported/partial/unsupported/unknown；
- conformance 绑定 specification version、implementation version、environment 和 cases；
- 失败与 limitation 保留。

**Review**

- implementation、security、supply chain、compatibility、independent conformance。

**Authority**

- Reference Implementation Owner 只拥有实现 source；
- `Implementation ≠ Specification`，实现不能反向改写规范或自动成为唯一实现。

如果某类纯文档规范不需要参考实现，必须由 Architecture Decision 记录
`REFERENCE_IMPLEMENTATION_NOT_APPLICABLE`，不能静默跳过实现经验要求。

### Stage 6 — Stable Specification

**Entry**

- 规范范围完整且 Owner/Authority 已冻结；
- 有多个有意义的实现或使用反馈，及独立 conformance/security evidence；
- breaking、migration、deprecation 和 compatibility policy 完整；
- 无未处置关键 Authority 冲突。

**Exit**

- 发布 exact stable version、compatibility commitment、errata 与 deprecation path；
- 后续 substantive change 进入新 Proposal/version。

**Review**

- 完整 Architecture、Specification、Security、Compatibility、Domain Owner 和 Human
  Architecture Decision。

**Authority**

- Stable 由显式 Human Architecture Decision 产生；
- 仍不产生 DBOS Permission、SAEE Command、Evidence Truth、认证或外部标准组织地位。

## 3. Exceptional States（异常状态）

| State | Meaning | Required record |
|---|---|---|
| `REVISE` | 内容不足或边界不清，退回较早阶段 | review findings、target stage |
| `BLOCKED` | 缺 Owner、Authority、Security、source 或 external-action decision | blocker、required human input |
| `REJECTED` | 不符合范围、重复、风险不可接受或无足够价值 | rationale、alternatives |
| `WITHDRAWN` | proposer 主动停止 | withdrawal reason |
| `SUPERSEDED` | 被新 Proposal/version 替代 | successor reference |
| `DEPRECATED` | 不再建议新采用，但保留历史 | replacement、timeline、decision |

## 4. State Separation（状态分离）

Proposal Stage 与 document maturity、implementation、community、release 和 adoption
分别记录。任何阶段名称都不能作为另一个状态的代理。

```text
EXPERIMENTAL_NE_STANDARD=true
MAPPING_NE_ADOPTION=true
IMPLEMENTATION_NE_SPECIFICATION=true
REFERENCE_IMPLEMENTATION_NE_CANONICAL_IMPLEMENTATION=true
REVIEW_NE_DECISION=true
DECISION_NE_IMPLEMENTATION=true
```

## 5. Current Result（当前结果）

```text
TITMAS_PROPOSAL_LIFECYCLE_DEFINED=true
CURRENT_HIGHEST_ENABLED_STAGE=STAGE_2_ARCHITECTURE_REVIEW_CANDIDATE
PUBLIC_COMMUNITY_REVIEW_ENABLED=false
EXPERIMENTAL_SPECIFICATION_CREATED=false
REFERENCE_IMPLEMENTATION_CREATED=false
STABLE_SPECIFICATION_CREATED=false
IMPLEMENTATION_AUTHORIZED=false
```
