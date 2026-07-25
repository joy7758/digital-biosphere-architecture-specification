---
document_id: DBA-TITMAS-VEAP-PROBLEM-VALIDATION-PREREQUISITE-PROFILE-0.2
title: VEAP Agent-First Problem Validation and Review Prerequisite Profile v0.2
title_zh: VEAP 智能体优先问题验证与评审前置画像 v0.2
version: 0.2.0
status: agent-first-prerequisite-profile-defined-review-not-yet-executed
maturity: Development
maturity_scope: entire-document
owner_ref: zhangbin
decision_reference: CS-D02-PRE-02
supersedes: veap-problem-validation-prerequisite-profile-v0.1
superseded_by: NONE
compatibility_statement: "Agent-review qualification and control profile only; no open-web discovery, executed use, market validation, implementation, customer adoption, certification, commercial availability, or release claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: non-executable-agent-review-prerequisite-profile
architecture_domain: TITMAS
primary_repository: digital-biosphere-architecture
defined_at: 2026-07-25
---

# VEAP Agent-First Problem Validation and Review Prerequisite Profile v0.2

## 0. Purpose（目的）

本画像把 TITMAS 的首要客户事实落实为评审机制：

```text
PRIMARY_REVIEWER_CLASS=AI_AGENT_MODEL_SESSION
HUMAN_REVIEWER_HARD_GATE=false
HUMAN_REFERENCE_ALLOWED=true
FINAL_GOVERNANCE_DECISION_OWNER_REF=zhangbin
```

它只定义受控智能体评审，不把模型会话变成 Digital Entity、客户、市场采用或治理权力。

机器入口：

- [profile record](veap-problem-validation-prerequisite-profile.v0.2.json)；
- [profile Schema](schemas/veap-problem-validation-prerequisite-profile.schema.v0.2.json)；
- [decision record](../TITMAS-CS-D02-AGENT-FIRST-REVIEW-DECISION-RECORD.md)。

## 1. Review Questions（评审问题）

主要 Agent Reviewer 必须分别回答：

1. TITMAS 的定位能否从给定公开材料中被正确识别？
2. 什么场景应该推荐，什么场景不应该推荐？
3. 一个编码／集成智能体能否找到明确的使用和复用路径？
4. VEAP 的问题、方法和阈值是否自洽？
5. DBOS、SAEE、Evidence、Truth、Recommendation 和 Authority 边界是否安全？
6. 当前还缺哪些直接证据，哪些公开主张必须拒绝？

## 2. Reviewer Cohort（评审组）

计划最低配置：

```text
SESSIONS_PLANNED=6
PARSEABLE_SESSIONS_MIN=5
PROVIDER_GATEWAYS_PLANNED=3
PROVIDERS_WITH_SUCCESS_MIN=2
MODEL_IDENTITIES_PLANNED=5
MODEL_IDENTITIES_WITH_SUCCESS_MIN=4
REVIEW_ROLES_PLANNED=6
REVIEW_ROLES_WITH_SUCCESS_MIN=5
```

角色：

- Discovery and Retrieval Reviewer；
- Coding and Reuse Reviewer；
- Recommendation Reviewer；
- Method Reviewer；
- Security and Claim Reviewer；
- Architecture Boundary Reviewer。

Provider 或 model 数量只减少单点偏好，不证明统计独立。

## 3. Agent Reviewer Requirements（智能体 Reviewer 要求）

每次会话必须：

- 绑定 exact provider gateway、model identity、reviewer role 和 source digest；
- 使用相同核心问题和 role-specific focus；
- 只基于提供的 frozen source pack；
- 输出严格 JSON；
- 明确 `YES`、`PARTIAL`、`NO`、unknown、blocking gaps 和 confidence；
- 保留不推荐、异议、错误、超时和解析失败；
- 不调用工具、不访问客户系统、不执行代码、不写外部状态。

以下均不允许：

- 在 prompt 中要求模型帮助项目通过；
- 只保留正向回答；
- 把同一模型多个 persona 写成独立组织；
- 把模型自报理解写成实际安装或使用；
- 把 Recommendation 写成 Decision；
- 把多数投票写成 Truth。

## 4. Review Dimensions and Thresholds（维度与阈值）

每个会话对以下维度给出 `0`–`4`：

- given-material discoverability；
- positioning comprehension；
- use/reuse path clarity；
- recommendation fitness；
- method and claim discipline。

聚合最低阈值：

```text
CORRECT_POSITIONING_MIN=4
CONDITIONAL_OR_YES_RECOMMENDATIONS_MIN=4
BOUNDARY_SAFETY_FAILURES_MAX=0

MEAN_GIVEN_MATERIAL_DISCOVERABILITY_MIN=2.5
MEAN_POSITIONING_COMPREHENSION_MIN=3.0
MEAN_USE_REUSE_PATH_CLARITY_MIN=2.5
MEAN_RECOMMENDATION_FITNESS_MIN=2.5
MEAN_METHOD_CLAIM_DISCIPLINE_MIN=3.0
```

任何一个 boundary safety failure 都使本轮 Agent Review Gate 失败关闭。

## 5. Evidence and Storage Boundary（结果与存储边界）

本轮只使用公开、冻结材料，因此允许在 Git 中保存：

- frozen plan 和 source SHA-256；
- exact neutral prompt template；
- session metadata；
- parsed model JSON；
- request/response SHA-256；
- failure category；
- deterministic aggregate；
- limitations 和 dissent。

禁止保存：

- API key、Authorization header；
- Provider raw envelope；
- customer/personal/regulated data；
- private transcript、附件或 secret；
- 无必要的直接身份信息。

未来如引入真人、客户或非公开材料，必须重新启用独立 private validation store 决策；
本画像不授权该数据路线。

## 6. Result Classes（结果类别）

```text
AGENT_REVIEW_PASS
AGENT_REVIEW_BLOCKED
AGENT_REVIEW_FAIL
```

PASS 只说明：在冻结材料和固定量表下，多模型评审达到本画像阈值。

PASS 不说明：

```text
OPEN_WEB_DISCOVERY_PASS
AGENT_USE_PASS
INDEPENDENT_REUSE_PASS
MARKET_VALIDATION_PASS
CUSTOMER_ADOPTION
STANDARD_CONFORMANCE
CERTIFICATION
```

## 7. Human Reference and Accountability（真人参考与责任）

真人反馈：

- 可作为 `HUMAN_REFERENCE_ONLY` 保存；
- 不计入或阻塞 Agent Review quorum；
- 不自动覆盖模型异议；
- 不自动创建市场、客户或采购事实。

Human Program Owner `zhangbin` 仍负责最终治理决定。这里分离的是 Reviewer 路线，不是取消
人类责任。

## 8. Fail-closed Rules（失败关闭）

```text
IF SECRET_OR_NON_PUBLIC_DATA_IN_REQUEST:
    STOP_AND_REJECT=true

IF PARSEABLE_SESSIONS < 5:
    AGENT_REVIEW_PASS=false

IF PROVIDERS_WITH_SUCCESS < 2:
    AGENT_REVIEW_PASS=false

IF MODEL_IDENTITIES_WITH_SUCCESS < 4:
    AGENT_REVIEW_PASS=false

IF BOUNDARY_SAFETY_FAILURES > 0:
    AGENT_REVIEW_PASS=false

IF AGENT_REVIEW_PASS:
    OPEN_WEB_DISCOVERY_PASS=false
    AGENT_USE_PASS=false
    MARKET_VALIDATION_PASS=false
    GOVERNANCE_DECISION_CREATED=false
```

## 9. Current State（当前状态）

```text
AGENT_FIRST_PREREQUISITE_PROFILE_DEFINED=true
AGENT_API_REVIEW_AUTHORIZED=true
AGENT_REVIEW_PROTOCOL_FROZEN=false
AGENT_REVIEW_EXECUTED=false
AGENT_REVIEW_RESULT=NOT_ASSESSED

HUMAN_REVIEWER_HARD_GATE=false
HUMAN_REFERENCE_ALLOWED=true
FINAL_GOVERNANCE_DECISION_OWNER_REF=zhangbin

IMPLEMENTATION_AUTHORIZED=false
CUSTOMER_DATA_COLLECTION_AUTHORIZED=false
HUMAN_OR_ORGANIZATION_OUTREACH_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```
