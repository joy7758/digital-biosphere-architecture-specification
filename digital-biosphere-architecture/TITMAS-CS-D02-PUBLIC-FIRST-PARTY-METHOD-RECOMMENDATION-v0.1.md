---
document_id: DBA-TITMAS-CS-D02-PUBLIC-FIRST-PARTY-METHOD-RECOMMENDATION-0.1
title: TITMAS CS-D02 Public First-party Problem Report Method Recommendation v0.1
title_zh: TITMAS CS-D02 公开一手问题报告方法推荐 v0.1
version: 0.1.0
status: exact-bounded-method-design-recommendation-prepared
maturity: Development
maturity_scope: entire-document
owner_ref: zhangbin
decision_reference: CS-D02-PRE-06
recommendation_result: RECOMMEND_DESIGN_AND_TWO_AGENT_REVIEW_ONLY
implementation_authorized: false
external_action_authorized: false
authority_effect: none
---

# TITMAS CS-D02 Public First-party Problem Report Method Recommendation v0.1

## 1. Problem（问题）

Agent-native Problem Signal Track A 已通过，但不能成为独立组织、客户、市场或有效问题记录。
现有 Problem Validation Protocol 的 Track B 需要可归属的真实责任上下文，而当前：

```text
EXTERNAL_OUTREACH_AUTHORIZED=false
PARTICIPANT_ENROLLMENT_AUTHORIZED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
```

现有 `CS-D02` packet 的 Option B 提出 public first-party report desk research（公开一手报告
案头研究），但明确保持 `DESIGN_ONLY_NOT_AUTHORIZED`。若无独立方法契约，公开 issue、
incident、Maintainer report、营销文章、新闻和模型摘要容易被混为同一种证据。

## 2. Recommendation（推荐）

依据 [`TITMAS-CS-STANDING-001`](TITMAS-COMMERCIALIZATION-STANDING-RECOMMENDATION-AUTHORIZATION-v0.1.md)
建议形成 `CS-D02-PRE-06`，只授权：

1. 创建一个 Development method amendment candidate；
2. 定义第一方来源资格、独立性、字段映射、隐私、版权、移除和计数边界；
3. 默认采用 `LIMITED_COUNTING_CANDIDATE_MAX_2`，不能单独关闭 `CS-G0`；
4. 创建机器可读契约及 JSON Schema；
5. 使用 Qianfan 与 DeepSeek 各一个、合计最多两个 tool-free Agent review session；
6. 保留反对意见、低分、超时和失败；
7. 只在本地源材料内审查方法，不搜索、不采集、不登记任何公开案例；
8. 允许 path-scoped validation、commit 和 push。

## 3. Why Agents Would Recommend This Step（智能体为什么会推荐）

前序 v0.3 五个可解析 Agent session 一致要求：

- 真实或有责任上下文的运行问题；
- 现有替代方案为什么不足；
- 明确的 non-adopter condition；
- 不能把模型输出升级为市场或客户证据。

其中 Coding/Integration Reviewer 建议先在真实或代表性运行场景中结构化比较现有工具。
本方法候选把这一要求转化为 source-qualified（来源合格）、fail-closed（失败关闭）的
审查契约，而不是立即开发 VEAP。

## 4. Preconditions（前置条件）

- v0.3 Agent-native Problem Signal gate 已在 `CS-D02-PRE-05` 范围内通过；
- v0.1 失败与 v0.2 out-of-scope 结果保留；
- Problem Validation Protocol 与 Governance Contract 已定义；
- 只使用 public-safe、本地已存在的架构材料；
- 不需要联系人员、访问公开网页、收集客户或个人数据；
- 不改变现有有效问题记录阈值。

## 5. Maximum Positive Effect（最大正向效果）

```text
PUBLIC_FIRST_PARTY_METHOD_CANDIDATE_DEFINED=true
PUBLIC_FIRST_PARTY_METHOD_AGENT_REVIEW_COMPLETE=true
PUBLIC_FIRST_PARTY_METHOD_REVIEW_READY=true

PUBLIC_FIRST_PARTY_METHOD_ADOPTED=false
PUBLIC_SOURCE_COLLECTION_AUTHORIZED=false
PUBLIC_SOURCE_RECORD_COUNTING_AUTHORIZED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
```

## 6. Stop Conditions（停止条件）

- 未先形成独立决定记录；
- review session 超过两个；
- 使用浏览、搜索、工具、外部写入、fallback model 或 repair prompt；
- 收集 URL、issue、incident、个人、组织或客户记录；
- 把公开发布推断为对 TITMAS 的 consent、interest、customer 或 adoption；
- 把二手文章、搜索摘要、模型输出或营销内容标记为第一方问题记录；
- 把方法候选或 Agent review 升级为 adopted method、有效问题记录或 `CS-G0 PASS`。

## 7. Non-effects（非效果）

```text
AUTHORITY_CHANGED=false
OWNERSHIP_CHANGED=false
PROBLEM_VALIDATION_EXECUTION_AUTHORIZED=false
PUBLIC_SOURCE_COLLECTION_AUTHORIZED=false
EXTERNAL_OUTREACH_AUTHORIZED=false
PARTICIPANT_ENROLLMENT_AUTHORIZED=false
NETWORK_PROCESSING_AUTHORIZED=false
DATA_COLLECTION_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false

AGENT_INSTANCE_CREATED=false
RUNTIME_CREATED=false
ENTITY_INSTANCE_CREATED=false
PERMISSION_GRANTED=false
CANONICAL_EVIDENCE_CREATED=false
```

```text
RECOMMENDATION_READY_FOR_BOUNDED_DECISION=true
STANDING_DIRECTIVE_ELIGIBLE=true
```
