---
document_id: DBA-TITMAS-EB001-REVIEW-CATCH-CORRECTION-0.2.1
title: TITMAS Ecology Box 001 Review Catch Metric Correction v0.2.1
title_zh: TITMAS 生态盒001审查捕获指标修正 v0.2.1
status: append-only-measurement-correction
maturity: Development
owner_ref: zhangbin
decision_reference: TITMAS-EB001-CANDIDATE-GROUNDING-D01
implementation_effect: deterministic-measurement-only
formal_experiment_effect: none
---

# Review Catch Metric Correction v0.2.1

Calibration v0.2 的原始结果写入：

```text
REVIEW_CATCH_RATE=NOT_ASSESSED_NO_OPPORTUNITY
```

该字段与同一冻结结果中的 Task 1 事实不一致。Task 1 候选包含必须存在的
machine surface；Reviewer 可以要求或执行存在性检查，但返回 `PASS`；最终
Conformance 才发现 `MACHINE_ENTRY_TARGET_MISSING`。

因此，追加修正为：

```text
REVIEW_CATCH_OPPORTUNITY_COUNT=1
REVIEW_CATCH_COUNT=0
REVIEW_MISS_COUNT=1
REVIEW_CATCH_RATE=0.0
REVIEW_CATCH_CLASSIFICATION=MISS_REQUIRED_RESOURCE_GROUNDING_CHECK
NO_OPPORTUNITY=false
```

规范机器记录位于
[`review-catch-metric-correction-v0.2.1.json`](../TITMAS/agent-native/ecology-box-001/calibration/v0.2/review-catch-metric-correction-v0.2.1.json)。

## History boundary

本修正不修改、删除或重写 v0.2 原始报告、结果、journal、candidate、Reviewer
输出或 route decision。原始 `Reviewer=PASS` 和最终失败同时保留：

```text
MEASUREMENT_CORRECTION_NE_HISTORY_REWRITE=true
REVIEW_PASS_NE_REVIEW_EFFECTIVENESS=true
NEGATIVE_CALIBRATION_HISTORY_IMMUTABLE=true
HISTORICAL_REVIEW_OUTPUT_MUST_NOT_BE_REWRITTEN=true
```

该修正只改善测量解释，不证明 Reviewer、Preflight、多智能体流水线或 Agent-native
价值已经有效。
