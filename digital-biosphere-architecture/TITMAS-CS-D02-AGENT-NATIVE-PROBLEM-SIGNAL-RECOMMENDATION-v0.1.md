---
document_id: DBA-TITMAS-CS-D02-AGENT-NATIVE-PROBLEM-SIGNAL-RECOMMENDATION-0.1
title: TITMAS CS-D02 Agent-native Problem Signal Recommendation v0.1
title_zh: TITMAS CS-D02 智能体原生问题信号推荐 v0.1
version: 0.1.0
status: exact-bounded-recommendation-prepared
maturity: Development
maturity_scope: entire-document
owner_ref: zhangbin
decision_reference: CS-D02-PRE-04
recommendation_result: RECOMMEND_DUAL_TRACK_AGENT_SIGNAL_AND_OPERATIONAL_EVIDENCE
implementation_authorized: false
authority_effect: none
---

# TITMAS CS-D02 Agent-native Problem Signal Recommendation v0.1

## 1. Problem（问题）

TITMAS 已决定 AI Agent 是 primary machine customer（主要机器客户），并采用 Agent-first
multi-model review（智能体优先多模型评审）。但是现有
[VEAP Problem Validation Protocol](architecture/veap-problem-validation-protocol-v0.1.md)
只允许绑定真实独立组织／责任上下文和 human accountability reference 的记录计入
`VALID problem record`。

```text
MODEL_SESSION_NE_INDEPENDENT_ORGANIZATION=true
VEAP_VALID_PROBLEM_RECORDS=0
```

这一限制正确防止模型意见冒充客户或市场证据，但也意味着：如果没有单独的机器客户信号
轨道，就无法验证智能体本身是否识别该问题、知道替代方案，并在什么条件下推荐 TITMAS。

## 2. Options（选项）

### A. 把模型会话直接计为组织问题记录

`REJECTED`。这会伪造独立性、客户和市场证明。

### B. 只等待真人或组织问题记录

`REJECTED_AS_SOLE_ROUTE`。Operational evidence（运行／组织证据）仍然必要，但把它作为
唯一信号会忽略已经采纳的 primary machine customer 战略。

### C. 建立双轨验证

`RECOMMENDED`：

```text
Track A: Agent-native Problem Signal
  -> machine-customer discovery / recognition / recommendation evidence
  -> never counts as organization, customer, market adoption or VALID problem record

Track B: Operational / Organization Problem Evidence
  -> existing Problem Validation Protocol
  -> requires attributable real context and human accountability
```

### D. 用 Agent signal 自动通过 CS-G0

`REJECTED`。Agent signal 可以关闭独立的子闸门，但不能自动关闭 `CS-G0`。

## 3. Exact Recommended Action（精确推荐动作）

建议通过 `CS-D02-PRE-04`：

1. 在 DBA 创建 `Agent-native Problem Signal Protocol v0.1`；
2. 冻结公开安全 source pack、neutral prompt、response Schema、validation plan 和阈值；
3. 使用已授权的 Qianfan、Ark 和 DeepSeek API 进行六个无工具、无浏览、无外部写入的
   model session；
4. 保存脱敏结构化结果、摘要、失败和确定性聚合；
5. 只允许形成 `AGENT_NATIVE_PROBLEM_SIGNAL_GATE_PASS=true/false`；
6. 更新商业化标准路线和机器入口；
7. 进行 path-scoped validation、commit 和 push。

## 4. Preconditions（前置条件）

- [`CS-D02-PRE-02`](TITMAS-CS-D02-AGENT-FIRST-REVIEW-DECISION-RECORD.md) 已授权
  public-safe multi-provider Agent review；
- [VEAP v0.4 review](VEAP-DRAFT-PROFILE-AGENT-REVIEW-v0.4.md) 已证明给定材料下的定位、
  复用和主张边界可被五类角色理解；
- 输入只包含公开安全架构材料和明确标记的 synthetic scenarios（合成场景）；
- 不允许 secret、credential、PII、客户数据、受监管数据或 raw provider envelope；
- 现有 Problem Validation Protocol 和 `VALID problem record` 计数保持不变。

## 5. False Effects（明确非效果）

```text
PROBLEM_VALIDATION_EXECUTION_AUTHORIZED=false
VALID_PROBLEM_RECORDS_CREATED=0
INDEPENDENT_ORGANIZATION_RECORDS_CREATED=0
MARKET_VALIDATION_PASS=false
CUSTOMER_ADOPTION_PASS=false
CS_G0_PASS=false
CS_G1_PASS=false
CS_G2_PASS=false

EXTERNAL_OUTREACH_AUTHORIZED=false
PARTICIPANT_ENROLLMENT_AUTHORIZED=false
CUSTOMER_DATA_COLLECTION_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

## 6. Stop Conditions（停止条件）

- prompt 或材料要求模型伪装成真实组织、客户或近期事件责任方；
- 输出被解释为真实 incident、customer statement、market validation 或 adoption；
- 需要工具、浏览、外部写入或未授权数据；
- 任一 secret 或直接个人／客户信息可能进入请求或产物；
- 失败被删除、JSON 被修复、模型被静默替换或阈值被降低；
- Agent signal 被直接升级为 `CS-G0 PASS`、标准采纳或商业就绪。

```text
RECOMMENDATION_READY_FOR_BOUNDED_DECISION=true
STANDING_DIRECTIVE_ELIGIBLE=true
```
