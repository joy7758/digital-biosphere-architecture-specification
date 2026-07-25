---
adr_id: ADR-031
title: Adopt Agent-First Multi-Model Review for the TITMAS Commercialization Standard Track
title_zh: 采纳智能体优先的多模型评审作为 TITMAS 商业化标准路线的主要评审机制
status: accepted
maturity: Development
maturity_scope: entire-document
owner_ref: zhangbin
decision_reference: CS-D02-PRE-02
supersedes_review_route: veap-problem-validation-prerequisite-profile-v0.1
superseded_by: NONE
compatibility_statement: "Review-governance decision only; no implementation, customer adoption, market validation, certification, commercial availability, or release claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
decided_by_ref: zhangbin
decided_at: 2026-07-25T16:21:10+08:00
primary_repository: digital-biosphere-architecture
agent_api_review_authorized: true
human_or_organization_outreach_authorized: false
final_governance_decision_owner_ref: zhangbin
authority_effect: bounded-agent-review-route-only
---

# ADR-031: Agent-First Multi-Model Review Governance

中文：采纳智能体优先的多模型评审作为 TITMAS 商业化标准路线的主要评审机制。

## Context（背景）

TITMAS 的首要客户是会检索、理解、调用、复用和推荐基础设施的 AI agent。既有
[`ADR-021`](ADR-021-agent-native-customer-validation.md) 已经采用 Agent-Native Customer
Validation（智能体原生客户验证）作为首要预览闸门。

后续的
[`VEAP Problem Validation Prerequisite Profile v0.1`](veap-problem-validation-prerequisite-profile-v0.1.md)
却再次把两名自然人 Reviewer 写成正式审查的硬门槛。这与用户于 2026-07-25 明确确认的
策略冲突：

> 没有真人 reviewer；主要策略是被智能体发现、使用、推荐，真人只是参考；使用本地已有
> 多个智能体 API 权限执行审查。

自然人 Reviewer 缺失不应被伪造成已经存在，也不应继续阻塞以智能体为首要客户的路线。
但模型会话也不能变成自我授权、市场采用或客户事实。

## Decision（决定）

1. TITMAS 商业化标准路线的主要技术、方法、主张、可发现性、可复用性和推荐性 Reviewer
   改为受控 multi-provider / multi-model agent panel（多提供方、多模型智能体评审组）。
2. 自然人 Reviewer 不再是 Agent-facing（面向智能体）问题验证与规范审查的硬门槛；真人
   反馈保留为 optional reference（可选参考）。
3. `zhangbin` 继续承担最终 Program Governance Decision（项目治理决定）责任。模型只能
   提供 Recommendation，不能创建 Decision、Authority、Permission、Certification 或
   Release Authorization。
4. 采用
   [`VEAP Problem Validation Prerequisite Profile v0.2`](veap-problem-validation-prerequisite-profile-v0.2.md)
   作为后继前置画像；v0.1 作为历史路线保留。
5. 授权一次有界 API 评审：
   - 只使用本地已经存在的 Provider credentials；
   - 只发送公开、冻结、无秘密、无客户或个人数据的 source pack；
   - 不启用工具，不写入外部系统，不调用 DBOS 或 SAEE；
   - 保留失败、异议、低分和 response hash；
   - 原始密钥、Provider raw envelope 和敏感 header 不进入仓库。
6. 本轮只能验证 `GIVEN_MATERIAL_DISCOVERY`、comprehension、reuse intent 和
   recommendation。没有开放搜索工具时不得声明 `OPEN_WEB_DISCOVERY_PASS`；没有独立
   沙箱执行时不得声明 `AGENT_USE_PASS` 或 `INDEPENDENT_IMPLEMENTATION_PASS`。
7. Agent Review Gate 可以形成独立机器结果，但不能自动关闭 `CS-G0`–`CS-G7`。

## Review Authority Model（评审权力模型）

```text
Public-safe frozen materials
        ↓
Multi-provider agent reviewers
        ↓
Structured findings + dissent + hashes
        ↓
Deterministic scoring
        ↓
Agent Review Recommendation
        ↓
Human Program Governance Decision
```

```text
AGENT_REVIEWER=PRIMARY_REVIEW_SIGNAL
HUMAN_REVIEWER=OPTIONAL_REFERENCE
HUMAN_PROGRAM_OWNER=FINAL_GOVERNANCE_ACCOUNTABILITY

AGENT_RECOMMENDATION != GOVERNANCE_DECISION
AGENT_REVIEW_PASS != MARKET_ADOPTION
GIVEN_MATERIAL_DISCOVERY != OPEN_WEB_DISCOVERY
REVIEWED_REUSE_PATH != EXECUTED_REUSE
```

## Consequences（影响）

正面影响：

- 评审机制与 TITMAS 的真实首要客户一致；
- 不再等待不存在的自然人 Reviewer；
- 通过 provider、model 和 role 多样性降低单一模型偏好；
- 不推荐、异议和边界失败可以进入可追溯记录；
- 人类责任不再与人工 Reviewer 数量绑定。

限制：

- 多模型不等于统计独立，模型可能共享训练数据或推理模式；
- API 模型拿到给定材料不等于自行从开放网络发现 TITMAS；
- 文字审查不等于安装、运行、集成或复用；
- 智能体正向评价不等于真实客户、市场规模、采购或收入。

## Non-effects（非效果）

```text
AGENT_FIRST_REVIEW_ROUTE_ADOPTED=true
AGENT_API_REVIEW_AUTHORIZED=true
HUMAN_REVIEWER_HARD_GATE=false
HUMAN_REFERENCE_ALLOWED=true
FINAL_GOVERNANCE_DECISION_OWNER_REF=zhangbin

OPEN_WEB_DISCOVERY_PROVEN=false
AGENT_USE_PROVEN=false
MARKET_VALIDATION_PROVEN=false
CUSTOMER_ADOPTION_PROVEN=false

AGENT_INSTANCE_CREATED=false
RUNTIME_CREATED=false
ENTITY_INSTANCE_CREATED=false
PERMISSION_GRANTED=false
CANONICAL_EVIDENCE_CREATED=false
IMPLEMENTATION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```
