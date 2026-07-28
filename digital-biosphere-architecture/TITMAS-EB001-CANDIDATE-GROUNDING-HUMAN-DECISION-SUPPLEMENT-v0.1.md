# TITMAS EB001 Candidate Grounding Human Decision Supplement v0.1

本文件只准备后继 Human Decision（人工决策）问题，不作决定，不授权 Calibration
v0.3、正式实验、外部动作、发布或商业验证。

| Decision | Question | Status |
|---|---|---|
| `CG-HD-01` | 是否接受 Candidate Grounding 设计？ | `UNDECIDED` |
| `CG-HD-02` | 是否接受 Review Catch 历史指标修正？ | `UNDECIDED` |
| `CG-HD-03` | 是否授权一次最终 Calibration v0.3？ | `UNDECIDED` |
| `CG-HD-04` | 是否停止多智能体校准路线？ | `UNDECIDED` |

## Decision inputs

- Candidate Grounding deterministic result:
  [`candidate-grounding-results-v0.1.json`](TITMAS/agent-native/ecology-box-001/calibration/grounding/candidate-grounding-results-v0.1.json)
- Review Catch append-only correction:
  [`review-catch-metric-correction-v0.2.1.json`](TITMAS/agent-native/ecology-box-001/calibration/v0.2/review-catch-metric-correction-v0.2.1.json)
- Original Calibration v0.2 result:
  [`calibration-results-v0.2.json`](TITMAS/agent-native/ecology-box-001/calibration/v0.2/calibration-results-v0.2.json)

## Frozen state

```text
CG_HD_01=UNDECIDED
CG_HD_02=UNDECIDED
CG_HD_03=UNDECIDED
CG_HD_04=UNDECIDED
CALIBRATION_V0_3_AUTHORIZED=false
CALIBRATION_V0_3_EXECUTED=false
FORMAL_ECOLOGY_BOX_EXECUTION_AUTHORIZED=false
PUBLIC_REPORT_AUTHORIZED=false
COMMERCIAL_VALIDATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

`UNDECIDED` 不得被测试 PASS、报告、Recommendation 或后继智能体解释为默示接受。
