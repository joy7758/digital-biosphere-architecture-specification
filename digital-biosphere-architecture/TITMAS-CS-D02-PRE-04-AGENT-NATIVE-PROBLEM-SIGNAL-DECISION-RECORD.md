---
document_id: DBA-TITMAS-CS-D02-PRE-04-AGENT-NATIVE-PROBLEM-SIGNAL-DECISION-RECORD-0.1
title: TITMAS CS-D02-PRE-04 Agent-native Problem Signal Decision Record v0.1
title_zh: TITMAS CS-D02-PRE-04 智能体原生问题信号决定记录 v0.1
version: 0.1.0
status: decided-bounded-agent-signal-review-authorized
maturity: Development
maturity_scope: entire-document
owner_ref: zhangbin
decision_owner_ref: zhangbin
decision_reference: CS-D02-PRE-04
parent_decision_reference: CS-D02
standing_directive_reference: TITMAS-CS-STANDING-001
recommendation_reference: TITMAS-CS-D02-AGENT-NATIVE-PROBLEM-SIGNAL-RECOMMENDATION-v0.1.md
decision_result: AUTHORIZE_BOUNDED_AGENT_NATIVE_PROBLEM_SIGNAL_REVIEW
implementation_authorized: false
authority_effect: bounded-agent-signal-review-only
---

# TITMAS CS-D02-PRE-04 Agent-native Problem Signal Decision Record v0.1

## 1. Decision（决定）

依据
[`TITMAS-CS-STANDING-001`](TITMAS-COMMERCIALIZATION-STANDING-RECOMMENDATION-AUTHORIZATION-v0.1.md)
以及精确的
[双轨推荐](TITMAS-CS-D02-AGENT-NATIVE-PROBLEM-SIGNAL-RECOMMENDATION-v0.1.md)，决定：

```text
CS-D02-PRE-04=AUTHORIZE_BOUNDED_AGENT_NATIVE_PROBLEM_SIGNAL_REVIEW

AGENT_NATIVE_PROBLEM_SIGNAL_PROTOCOL_AUTHORIZED=true
PUBLIC_SAFE_AGENT_SIGNAL_API_REVIEW_AUTHORIZED=true
AGENT_SIGNAL_RECORDING_AUTHORIZED=true

PROBLEM_VALIDATION_EXECUTION_AUTHORIZED=false
ORGANIZATION_OR_CUSTOMER_RECORD_COLLECTION_AUTHORIZED=false
```

机器记录：

- [decision JSON](TITMAS-CS-D02-PRE-04-AGENT-NATIVE-PROBLEM-SIGNAL-DECISION-RECORD.v0.1.json)；
- [decision Schema](architecture/schemas/titmas-cs-d02-pre-04-agent-native-problem-signal-decision-record.schema.v0.1.json)。

## 2. Exact Authorized Scope（精确授权范围）

只允许：

1. 创建
   [Agent-native Problem Signal Protocol](architecture/agent-native-problem-signal-protocol-v0.1.md)；
2. 创建公开安全 source pack、neutral prompt、response Schema、validation plan、观察集、
   确定性评分和报告；
3. 调用本地已有 Qianfan、Ark 和 DeepSeek API credentials；
4. 执行最多六个 model session，禁止工具、浏览和外部写入；
5. 保存 provider/model、request/response digest、usage、结构化结果、失败和限制；
6. 更新 DBA 路线图、README 和机器入口；
7. 执行 path-scoped validation、commit 和 push。

## 3. Data Boundary（数据边界）

```text
PUBLIC_SAFE_ARCHITECTURE_MATERIAL_ONLY=true
SYNTHETIC_SCENARIOS_ONLY=true
RAW_PROVIDER_ENVELOPE_PERSISTED=false
CUSTOMER_OR_PERSONAL_DATA_ALLOWED=false
SECRET_IN_REQUEST_OR_ARTIFACT_ALLOWED=false
MODEL_TOOL_USE_ALLOWED=false
EXTERNAL_SIDE_EFFECTS_ALLOWED=false
```

API credential 只用于请求认证，不进入 prompt、source pack、observation 或 report。

## 4. Decision Separation（决定分离）

本决定新增的是信号类别，不修改既有 Problem Record Contract：

```text
AGENT_SIGNAL_RECORD_NE_VALID_PROBLEM_RECORD=true
MODEL_SESSION_NE_INDEPENDENT_ORGANIZATION=true
AGENT_SIGNAL_GATE_NE_CS_G0=true
AGENT_RECOMMENDATION_NE_MARKET_VALIDATION=true
```

Agent signal 可以证明：给定公开安全场景和材料时，模型是否识别问题、比较替代方案、
指出非采用条件并给出有界推荐。它不能证明真实事件、组织需求、采购、客户、采用或市场。

## 5. Success Effect（成功效果）

阈值全部通过时最多允许：

```text
AGENT_NATIVE_PROBLEM_SIGNAL_GATE_PASS=true
AGENT_PRIMARY_CUSTOMER_SIGNAL_OBSERVED=true
```

仍必须保持：

```text
VEAP_VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
CS_G1_PASS=false
CS_G2_PASS=false
MARKET_VALIDATION_PASS=false
CUSTOMER_ADOPTION_PASS=false
```

## 6. Stop Conditions（停止条件）

沿用推荐文件的 stop conditions，并额外要求：

- 六个 session 共享同一冻结材料与评分阈值；
- network/408/429/5xx 最多重试一次；
- 不允许 fallback model 或 invalid JSON repair；
- 结果低分、`NO`、空内容、timeout 和 provider failure 必须保留；
- 任何 boundary answer 不安全时信号 Gate 失败关闭。

## 7. Non-effects（非效果）

```text
AUTHORITY_CHANGED=false
OWNERSHIP_CHANGED=false
PROBLEM_VALIDATION_EXECUTION_AUTHORIZED=false
EXTERNAL_OUTREACH_AUTHORIZED=false
PARTICIPANT_ENROLLMENT_AUTHORIZED=false
CUSTOMER_DATA_COLLECTION_AUTHORIZED=false
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
