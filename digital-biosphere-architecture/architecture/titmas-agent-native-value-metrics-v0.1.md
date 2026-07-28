---
document_id: DBA-TITMAS-AGENT-NATIVE-VALUE-METRICS-0.1
title: TITMAS Agent-Native Value Metrics v0.1
title_zh: TITMAS 智能体原生价值指标 v0.1
version: 0.1.0
status: preregistration-design-only
maturity: Development
owner_ref: zhangbin
decision_reference: NOT_DECIDED
implementation_effect: none
authority_effect: none
---

# TITMAS Agent-Native Value Metrics v0.1

## Interpretation policy

所有 numerator（分子）、denominator（分母）、排除项和 `NOT_ASSESSED` 必须与结果一起
报告。分母为零时不得写 `0` 或 `PASS`，只能写 `NOT_ASSESSED`。模型自评不能作为最终
质量评分。

## 1. Coordination Cost

分别报告，不合成任意权重分数：

```text
HUMAN_INTERVENTION_COUNT
CLARIFICATION_REQUEST_COUNT
REVIEW_CYCLE_COUNT
HUMAN_ACTIVE_MINUTES
REWORK_COUNT
```

主要比较为同一 task pair 的 Agent-native 减 Human-first。负数仅表示该项协调成本较低，
不自动表示总价值更高。

## 2. Useful Intelligence Density

```text
USEFUL_INTELLIGENCE_DENSITY =
  USEFUL_OUTCOME_CHANGING_INSIGHTS / TOTAL_AGENT_OUTPUTS
```

`USEFUL_OUTCOME_CHANGING_INSIGHT` 必须同时满足：唯一、事实有效、与任务相关，并使最终
候选输出或 Human Decision 发生可追踪变化。重复、格式填充、错误和不适用建议进入分母，
不得删除。

冻结的先验观察：

```text
TOTAL_AGENT_OUTPUTS=25
USEFUL_OUTCOME_CHANGING_INSIGHTS=0
UNIQUE_FACTUALLY_VALID_FINDINGS=3
DUPLICATE_FINDINGS=5
FALSE_OR_NOT_APPLICABLE_FINDINGS=17
OUTPUT_VOLUME_NE_VALUE=true
```

这里 3 个有效发现没有改变最终结果，因此不能把它们计为 outcome-changing。

## 3. Contribution Value

```text
CONTRIBUTION_ACCEPTANCE_RATE =
  ACCEPTED_CONTRIBUTION_CANDIDATES / SUBMITTED_CONTRIBUTION_CANDIDATES
```

同时报告被接受贡献带来的最终缺陷变化。`accepted` 需要 Human disposition，不等于
Adoption、merge 或 Release。

## 4. Memory Reuse Rate

```text
MEMORY_REUSE_RATE =
  SIMILAR_ERRORS_PREVENTED_WITH_VALID_REUSE_REF /
  ELIGIBLE_SIMILAR_ERROR_OPPORTUNITIES
```

本指标只复用既有 history/evidence reference，不创建新的 Memory system。必须同时记录
相似性判定、reuse reference 和反事实限制。引用次数增加而重复错误不下降时，该指标不得
被解释为价值。

## 5. Evolution Fitness

以下是分量，不是一个可以事后加权的总分：

- `ADAPTATION`：面对预声明变化仍通过验收的比例；
- `STABILITY`：重复执行的结果差异和关键缺陷波动；
- `RECOVERY`：失败后在允许重试次数内恢复且无新增严重缺陷的比例；
- `DIVERSITY`：真正独立 lineage 的非重复有效发现覆盖度。

SAEE 可以在未来授权实验中读取这些输入形成 evaluation；当前框架不调用 SAEE，不产生
Fitness Assessment，也不把 Evaluation 变成 Authority。

## 6. Outcome quality guardrail

至少记录：

```text
FINAL_ACCEPTANCE_RATE
CRITICAL_DEFECT_COUNT
MAJOR_DEFECT_COUNT
MINOR_DEFECT_COUNT
DEFECT_ESCAPE_COUNT
```

Agent-native 的任何成本优势若伴随更低 acceptance 或更多 Critical/Major defect，H1
不得通过。

## 7. Reporting

结果报告必须包含每组原始计数、task-pair 差异、缺失值、停止事件、失败与限制。样本只有
10 对任务时只报告描述性结果和区间，不宣称普适因果结论。
