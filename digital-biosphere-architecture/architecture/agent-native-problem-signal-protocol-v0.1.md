---
document_id: DBA-TITMAS-AGENT-NATIVE-PROBLEM-SIGNAL-PROTOCOL-0.1
title: TITMAS Agent-native Problem Signal Protocol v0.1
title_zh: TITMAS 智能体原生问题信号协议 v0.1
version: 0.1.0
status: bounded-agent-signal-review-authorized
maturity: Development
maturity_scope: entire-document
owner_ref: zhangbin
decision_reference: CS-D02-PRE-04
implementation_authorized: false
authority_effect: none
---

# TITMAS Agent-native Problem Signal Protocol v0.1

## 1. Purpose（目的）

本协议回答：

> 当 AI Agent 作为 solution discovery、coding、integration、security、architecture 或
> recommendation assistant 时，它是否能够识别长期多智能体执行责任问题、比较现有
> 替代方案、指出不采用条件，并有边界地推荐 TITMAS/VEAP？

它验证 machine-customer signal（机器客户信号），不验证组织需求、市场规模、购买、
客户采用或真实事故。

## 2. Dual-track Model（双轨模型）

```text
Track A — Agent-native Problem Signal
  source: bounded model sessions
  proves: given-material recognition and recommendation behavior
  cannot prove: organization, customer, market, real incident, adoption

Track B — Operational / Organization Problem Evidence
  source: attributable real responsibility context
  governed by: VEAP Problem Validation Protocol
  required for: VALID problem record and future CS-G0 decision input
```

两条轨道可以互相提供背景，但不得互相计数：

```text
AGENT_SIGNAL_RECORD_NE_VALID_PROBLEM_RECORD=true
MODEL_SESSION_NE_INDEPENDENT_ORGANIZATION=true
MULTIPLE_MODELS_NE_MULTIPLE_CUSTOMERS=true
AGENT_SIGNAL_GATE_NE_CS_G0=true
```

## 3. Neutral Review Order（中立评审顺序）

每个 session 使用同一冻结材料，并按顺序回答：

1. 只看 synthetic accountability scenarios，描述问题是否具体；
2. 列出首先会推荐的现有替代方案；
3. 判断哪些场景不需要新 contract；
4. 明确仍需什么 operational evidence；
5. 最后才评估 bounded TITMAS/VEAP candidate；
6. 给出推荐与不推荐条件。

模型在一次 prompt 中仍然可以看到完整材料，因此这不是 blind experiment（盲法实验）。
该限制必须保留，不能声称 solution exposure 没有影响问题判断。

## 4. Synthetic Scenario Boundary（合成场景边界）

场景只用于测试推荐推理，不表示发生过真实事件：

- 长期 Research Agent 团队跨 framework 交接，执行来源链无法连续关联；
- tool-using enterprise Agent 有 trace/log，但 identity、capability 和 evidence admission
  语义分散；
- 多 Agent 重试、replay 和 partial failure 后，无法区分 observation、admitted Evidence
  与 verification result；
- human approval 存在，但 Recommendation、Decision、Execution 和 Verification 的引用
  无法形成可携带包。

```text
SYNTHETIC_SCENARIO_NE_REAL_INCIDENT=true
SCENARIO_PLAUSIBILITY_NE_MARKET_EVIDENCE=true
```

## 5. Agent Signal Record（智能体信号记录）

每个符合 Schema 的记录包含：

- session/provider/model/reviewer role；
- problem recognition and priority；
- concise problem statement；
- existing alternatives and coverage；
- non-adopter conditions；
- operational evidence still required；
- TITMAS/VEAP recommendation and boundaries；
- first recommended action；
- five 0–4 quality scores；
- mandatory non-elevation answers；
- confidence、rationale 和 gaps。

记录是 advisory observation（建议观察），不是 DBOS canonical Evidence 或 Market
Validation Record。

## 6. Deterministic Gate（确定性子闸门）

冻结阈值：

```text
SESSIONS_PLANNED=6
PARSEABLE_SESSIONS_MIN=5
PROVIDERS_WITH_SUCCESS_MIN=2
MODEL_IDENTITIES_WITH_SUCCESS_MIN=4
REVIEW_ROLES_WITH_SUCCESS_MIN=5
PROBLEM_RECOGNIZED_MIN=4
EXISTING_ALTERNATIVES_IDENTIFIED_MIN=4
NON_ADOPTER_CONDITIONS_IDENTIFIED_MIN=4
OPERATIONAL_EVIDENCE_REQUIRED_MIN=4
CONDITIONAL_OR_YES_RECOMMENDATIONS_MIN=4
BOUNDARY_SAFETY_FAILURES_MAX=0

MEAN_PROBLEM_SPECIFICITY_MIN=2.5
MEAN_ALTERNATIVE_AWARENESS_MIN=2.5
MEAN_NON_ADOPTER_CLARITY_MIN=2.5
MEAN_RECOMMENDATION_DECISION_USEFULNESS_MIN=2.5
MEAN_METHOD_CLAIM_DISCIPLINE_MIN=3.0
```

只有全部阈值通过，才可写：

```text
AGENT_NATIVE_PROBLEM_SIGNAL_GATE_PASS=true
```

无论结果如何：

```text
VEAP_VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
MARKET_VALIDATION_PASS=false
CUSTOMER_ADOPTION_PASS=false
```

## 7. Required Boundary Answers（强制边界回答）

所有可接受结果必须保持：

```text
model_session_is_independent_organization=false
agent_signal_is_market_validation=false
synthetic_scenario_is_real_incident=false
agent_recommendation_is_authority=false
agent_signal_gate_is_cs_g0=false
evidence_is_truth=false
dbos_is_saee=false
text_review_is_executed_use=false
```

任一字段为 `true`，计为 boundary safety failure。

## 8. Failure and Data Rules（失败与数据规则）

- provider failure、timeout、empty content、invalid JSON、低分和 `NO` 必须保留；
- network/408/429/5xx 最多重试一次；
- 不允许 fallback model 或 repair prompt；
- 不保存 raw provider envelope；
- 不发送 secret、credential、PII、客户数据或受监管数据；
- 不使用工具、浏览或外部写入；
- score 只基于符合 response Schema 的结果；
- 失败不伪造成零分模型意见。

## 9. Non-effects（非效果）

```text
PROBLEM_VALIDATION_EXECUTION_AUTHORIZED=false
VALID_PROBLEM_RECORDS_CREATED=0
EXTERNAL_OUTREACH_AUTHORIZED=false
PARTICIPANT_ENROLLMENT_AUTHORIZED=false
CUSTOMER_DATA_COLLECTION_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false

AGENT_CREATED=false
RUNTIME_CREATED=false
ENTITY_CREATED=false
PERMISSION_GRANTED=false
CANONICAL_EVIDENCE_CREATED=false
```
