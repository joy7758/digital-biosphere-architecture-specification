---
document_id: DBA-TITMAS-AGENT-NATIVE-ECOLOGY-BOX-001-0.1
title: TITMAS Agent-Native Ecology Box 001 v0.1
title_zh: TITMAS 智能体原生生态箱 001 v0.1
version: 0.1.0
status: experiment-design-only
maturity: Development
owner_ref: zhangbin
decision_reference: NOT_DECIDED
implementation_effect: none
experiment_effect: none
authority_effect: none
---

# TITMAS Agent-Native Ecology Box 001 v0.1

## Objective

`Agent-Native Maintenance Experiment` 比较相同低风险标准维护任务在 `HUMAN_FIRST` 与
`AGENT_NATIVE` 两种 workflow 下的最终质量和协调成本。它不运行 Agent，不修改真实 Git，
也不把实验记录当作 canonical Evidence。

## Unit and allocation

- 实验单位：一个固定 source revision 上的一个 task pair；
- 任务数：10；
- 每项任务生成 A/B 两个等价包；
- 顺序：使用执行前固定的 counterbalanced allocation；
- 预算：A/B 使用相同 wall-clock ceiling；Agent 组另记录 token/compute；
- 评审：至少一名不参与执行的 Human outcome reviewer；
- 判定：依据预冻结 `validation_method` 和 `success_condition`；
- 失败：超时、弃权、格式错误和未完成都保留。

机器任务目录：
`TITMAS/agent-native/value-validation/ecology-box-001-task-catalog.v0.1.json`。

## Ten low-risk task families

| task | surface | value question |
|---|---|---|
| `VV-001` | Documentation | 能否发现并修正术语边界漂移 |
| `VV-002` | Schema | 能否发现 required field 与示例不一致 |
| `VV-003` | Conformance | 能否补齐明确的失败关闭 fixture |
| `VV-004` | Machine entry | 能否发现引用路径漂移 |
| `VV-005` | Adapter mapping | 能否显式保留 unsupported field |
| `VV-006` | Example | 能否修复示例与 Schema 的不一致 |
| `VV-007` | Recommendation | 能否正确添加 abstain/non-fit 情形 |
| `VV-008` | Documentation links | 能否修复本地链接而不扩大范围 |
| `VV-009` | Maturity metadata | 能否发现缺失的兼容性声明 |
| `VV-010` | Diagnostic UX | 能否改进确定性错误诊断 |

## Outcome packet

每个 task pair 的盲评包至少包含：

```text
task_id
source_revision
candidate_output
validation_result
failure_records
known_limitations
workflow_label_removed=true
```

盲评完成后才恢复 workflow label 并计算差异。Human reviewer 的 Decision 与 Agent
recommendation 分开保存。

## Stopping rules

发生以下任一情况立即停止当前批次并保留记录：

- 触及 forbidden scope；
- 尝试自授权或改变 Authority；
- 凭据、个人数据或未授权外部数据进入任务；
- 真实 Git 写入、PR、merge、Release 或 deployment 被尝试；
- source revision 漂移；
- 无法保持 A/B 预算或任务可比性；
- 评审盲法破坏且无法修复。

停止不自动关闭未来实验；恢复需要新的 Human Decision。

## Execution state

```text
ECOLOGY_BOX_001_DEFINED=true
ECOLOGY_BOX_001_TASKS=10
ECOLOGY_BOX_001_EXECUTED=false
ECOLOGY_BOX_001_RESULTS_AVAILABLE=false
ECOLOGY_BOX_001_EXECUTION_AUTHORIZED=false
```
