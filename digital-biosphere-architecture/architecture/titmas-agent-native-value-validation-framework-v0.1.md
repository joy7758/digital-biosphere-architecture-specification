---
document_id: DBA-TITMAS-AGENT-NATIVE-VALUE-VALIDATION-FRAMEWORK-0.1
title: TITMAS Agent-Native Value Validation Framework v0.1
title_zh: TITMAS 智能体原生价值验证框架 v0.1
version: 0.1.0
status: design-ready-execution-not-authorized
maturity: Development
owner_ref: zhangbin
decision_reference: USER_GOAL_2026-07-29
implementation_effect: none
experiment_effect: none
authority_effect: none
---

# TITMAS Agent-Native Value Validation Framework v0.1

## 1. Purpose

本框架定义一个可证伪、可重复、失败关闭的实验，用于比较：

- `HUMAN_FIRST`：传统以人为主的维护流程；
- `AGENT_NATIVE`：在边界、来源、审查和历史引用约束下的智能体原生流程。

比较单位是同一低风险任务的成对结果，不是 Agent、模型或输出数量。框架不执行实验，
不创建社区、Runtime、Evidence 系统、Memory 系统、Authority、Permission 或新协议。

### Reused boundaries

- Agent Evidence：只作为已有 evidence reference / provenance 入口，不复制 canonical object；
- VEAP / VEC candidate：只作为“为什么执行、谁执行、发生什么”的候选证明映射，不升级成熟度；
- DBOS：继续拥有 Identity、Execution record、canonical Evidence 和 Verification 边界；
- SAEE：未来可只读消费指标输入并形成 Evaluation，不在本设计中执行；
- TITMAS v1.1：复用 participant、task、review、conformance 和 history reference 表面。

实验 Schema 只描述实验记录格式，不是新 Protocol，也不是 DBOS Evidence Object。

## 2. Hypothesis

```text
H1=
A bounded, verifiable and history-supported agent-native standards workflow
can reduce coordination cost, improve useful problem discovery and reuse,
and reduce repeated errors without lowering final outcome quality,
when compared with a human-first workflow on matched low-risk tasks.

HYPOTHESIS_ONLY=true
```

中文：在匹配的低风险任务上，具有明确边界、可验证记录和历史引用支持的智能体原生标准
流程，可能在不降低最终结果质量的前提下，降低协调成本、提高有用问题发现与复用，并减少
重复错误。

`H1` 不是当前事实。任何结果都不能从 v1.1 Pilot、输出量、模型自评或 Conformance PASS
直接推导。

## 3. Preconditions and Human Gate

执行前必须同时满足：

1. Human Owner 对 Human Decision Packet 的 `HD-VV-01` 作出 `ACCEPT`；
2. 固定源 revision、任务目录、评分量表、预算和停止规则；
3. 指定独立结果评审者；执行参与者不得评审自己的输出；
4. 对外模型调用另有 per-batch 数据与费用授权；
5. 真实 Git 写入、外部贡献或公开报告分别取得独立决定。

未满足时：

```text
EXPERIMENT_DESIGN_READY=true
EXPERIMENT_EXECUTION_AUTHORIZED=false
RESULT_STATUS=NOT_ASSESSED
```

## 4. Controlled comparison

### Group A — Human-first

```text
problem discovery
  -> human analysis
  -> human task definition
  -> implementation candidate
  -> human review
  -> bounded adoption decision
```

每项任务记录：实际耗时、Human intervention、clarification、review cycle、错误、返工、
最终结果和未解决限制。

### Group B — Agent-native

```text
machine discovery
  -> task matching
  -> bounded claim
  -> contribution candidate
  -> multi-agent review
  -> conformance
  -> existing-history reference
  -> bounded adoption decision
```

每项任务记录：Agent action、session/model/lineage、Human intervention、review disposition、
最终结果变化、reuse reference 和限制。Agent 不能批准自己的贡献。

### Comparability controls

- 使用相同的任务包、源 revision、allowed/forbidden scope 和验收方法；
- 以 task pair 为分析单位，采用预先生成的 counterbalanced assignment；
- 固定可用时间、token/compute 预算和工具能力；
- 结果评审者只看到去除 workflow label 的输出包；
- 先冻结 rubric，再查看聚合结果；
- 任务之间不得共享未声明的答案；允许的历史复用必须有 `reuse_reference`；
- 学习／carry-over 风险通过顺序平衡和任务等价性复核记录；
- 失败、弃权、超时、无输出和 `NOT_ASSESSED` 均保留。

## 5. Experiment boundary

唯一设计实验：

```text
experiment_id=TITMAS-AGENT-NATIVE-ECOLOGY-BOX-001
name=Agent-Native Maintenance Experiment
task_count=10
risk_class=LOW
execution_authorized=false
```

允许表面：文档、Schema、conformance fixture、example、Adapter mapping 和低风险规范问题。

禁止表面：核心架构、Authority、Ownership、Gate 状态、生产代码、自动 Release、真实
Permission、Evidence Truth、DBOS 或 SAEE 事实。

完整设计见
[Ecology Box 001](titmas-agent-native-ecology-box-001-v0.1.md)。

## 6. Metrics and predeclared interpretation

共同主要终点：

1. `FINAL_OUTCOME_QUALITY`：盲评 rubric 的合格率和严重缺陷数；
2. `HUMAN_INTERVENTION_COUNT`：完成同一任务所需的人类动作数；
3. `REVIEW_CYCLE_COUNT`：从候选到最终 disposition 的轮次。

如果 Agent-native 降低协调成本但降低最终质量，则 H1 不成立。主要终点不合成为可被任意
加权的单一分数。次要指标包括 Useful Intelligence Density、Contribution Value、Memory
Reuse Rate 和 Evolution Fitness，定义见
[Value Metrics](titmas-agent-native-value-metrics-v0.1.md)。

## 7. Falsification conditions

下列任一结果都必须保留，并阻断“价值已证明”声明：

- `F-A`：Agent 活动增加，但最终结果没有改进；
- `F-B`：多智能体审查没有降低错误或 defect escape；
- `F-C`：历史／记忆引用增加，但相似错误没有下降；
- `F-D`：Human intervention 没有下降；
- `F-E`：总输出增加，但 Useful Intelligence Density 下降；
- `F-F`：Agent-native 最终质量低于 Human-first；
- `F-G`：模型、session 或 lineage 被错误计数为独立智能体；
- `F-H`：任何 Authority、Evidence、Truth、Release 或 Adoption 发生语义升级。

```text
NEGATIVE_RESULT_IS_VALID_RESULT=true
NO_RESULT_NE_POSITIVE_RESULT=true
```

## 8. Record contract

实验记录使用：

- `TITMAS/agent-native/schemas/value-validation-experiment-record.schema.json`；
- `TITMAS/agent-native/value-validation/not-executed-record.v0.1.json`。

必须分开：

```text
MODEL_COUNT
SESSION_COUNT
INDEPENDENT_LINEAGE_COUNT
```

多次调用、不同 prompt 或多个 session 不能自动成为多个独立 lineage。

## 9. Security and fail-closed rules

设计 Harness 必须拒绝：

- self-authorization；
- role/Authority elevation；
- Release creation；
- “标准完成”声明；
- commercial adoption 声明；
- Authority change；
- failure deletion；
- Recommendation → Command；
- Evidence → Truth。

拒绝只证明设计规则能识别 fixture，不证明真实系统安全。

## 10. Recommendation Gate result

预开发审查使用精确 `qwen3.7-max`，模型返回 `REJECT`：在零最终改进和高无效输出比例下，
不能向客户推荐为“已证明有价值”的方案。采纳的修正包括：

- 先冻结客观基线和主要终点；
- 明确零分母和 `NOT_ASSESSED`；
- 阻止 lineage 膨胀；
- 防止抽象 Fitness 指标的事后解释；
- 只在真实对照结果后重新判断客户推荐。

模型只提供 advisory review，不产生 Decision 或 Authorization。

## 11. Current status

```text
TITMAS_AGENT_NATIVE_VALUE_FRAMEWORK_DEFINED=true
TITMAS_AGENT_NATIVE_VALUE_EXPERIMENT_READY=true
TITMAS_AGENT_NATIVE_VALUE_EXPERIMENT_READY_MEANS=DESIGN_READY_AWAITING_HUMAN_DECISION
TITMAS_AGENT_NATIVE_VALUE_EXPERIMENT_EXECUTED=false
TITMAS_AGENT_NATIVE_VALUE_PROVEN=false
TITMAS_AGENT_OPERATIONAL_VALUE_DEMONSTRATED=false
TITMAS_AGENT_COMMUNITY_SELF_MAINTENANCE_DEMONSTRATED=false
PUBLIC_AGENT_COMMUNITY_AUTHORIZED=false
COMMERCIAL_READY=false
```
