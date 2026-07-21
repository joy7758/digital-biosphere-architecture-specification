---
document_id: DBA-INTEGRATION-GATES-0.1
title: Digital Biosphere Program Integration Gates v0.1
title_zh: 数字生物圈项目群集成闸门 v0.1
status: fail-closed-gate-baseline
automatic_approval: false
runtime_effect: none
last_reviewed: 2026-07-21
---

# Digital Biosphere Program Integration Gates v0.1（数字生物圈项目群集成闸门 v0.1）

## 1. Gate Principle（闸门原则）

所有跨项目推进默认 fail closed（失败关闭）。`NOT_ASSESSED`、`UNKNOWN`、`STALE`、`PARTIAL`、`PREPARED_ONLY` 和 `BLOCKED` 均不等于 `PASS`。

```text
PLAN_NE_AUTHORIZATION=true
SPECIFICATION_NE_IMPLEMENTATION=true
REFERENCE_NE_INTEGRATION=true
PASS_REQUIRES_SCOPED_EVIDENCE=true
DOWNSTREAM_GATE_CANNOT_BYPASS_UPSTREAM_GATE=true
```

## 2. Standard Gates（标准闸门）

| gate_id | 名称 | 必须证明 | 最小证据 | 失败时 |
|---|---|---|---|---|
| `G0` | Portfolio Admission（项目组合准入） | 项目目的、角色、Owner、范围和非目标明确 | Project Charter、canonical source、准入决定 | 保持 `ADJACENT_CANDIDATE` 或范围外 |
| `G1` | Source Truth（事实来源） | 状态、Capability、Evidence 和 Release 有规范来源 | source path、branch、commit/version、freshness、冲突规则 | 状态保持 `UNKNOWN` / `NOT_ASSESSED` |
| `G2` | Architecture Contract（架构契约） | Owner、对象、方向、权限和失败边界明确 | DBA specification、ADR、data contract、negative rules | 不得创建跨项目实施任务 |
| `G3` | Implementation Mapping（实现映射） | 规范字段能映射到现有实现且没有重复权威 | 实现位置、版本、mapping、unsupported fields | 不得宣称集成可用 |
| `G4` | Conformance（符合性） | 正例、负例、兼容性和 fail-closed 行为通过 | scoped test/validator result、fixture provenance、failure retention | 停止推进并保留失败 |
| `G5` | Authorization（授权） | 具体变化有明确 decision 和 authorization reference | approved decision、scope、issuer、expiry/revocation | 不得执行、注册、激活或授予 Permission |
| `G6` | Execution Evidence（执行证据） | 实际执行形成连续、有来源且不可静默删除的记录 | execution、evidence、verification、failure records | 不得进入评价或采用结论 |
| `G7` | Evaluation and Adoption（评价与采纳） | SAEE 评价与人工决定分离且可追溯 | Fitness/Risk/Recommendation + Human Decision | 不得把 Recommendation 当作状态变化 |
| `G8` | Release and Adoption（发布与采用） | 发布、部署、采用和商业状态分别有证据 | release record、adoption decision、deployment evidence | 只能称为本地或未发布状态 |

## 3. Current Gate Matrix（当前闸门矩阵）

| integration_track | G0 | G1 | G2 | G3 | G4 | G5-G8 | 结论 |
|---|---|---|---|---|---|---|---|
| DBA Program Governance Cockpit | `PASS` | `PASS_REMOTE_BASELINE` | `PASS` | `NOT_APPLICABLE` | `PASS_CLEAN_CLONE_DOCUMENTATION` | `NOT_APPLICABLE` | 远端文档基线与干净检出已验证；不表示正式发布或子项目采用 |
| DBOS ↔ SAEE Contract | `PASS_CORE_ROLE` | `PASS_FROZEN_REMOTE_SOURCES` | `SPECIFICATION_DEFINED` | `PASS_SCOPED_CLEAN_CLONE` | `PASS_SCOPED_CLEAN_CLONE` | `G6_SYNTHETIC_RECORD_CHAIN_G7_RECOMMENDATION_ONLY` | 只可称为冻结源码上的合成契约符合性；不得称为生产集成或受治理演化闭环 |
| Research Agent Pilot ↔ DBOS / SAEE | `PASS_PILOT_ROLE` | `PARTIAL` | `SPECIFICATION_DEFINED` | `PREPARED_ONLY` | `NOT_ASSESSED` | `BLOCKED_NOT_READY` | 不得创建 Prototype、Agent、Runtime 或实验 |
| Adjacent components | `NOT_PASSED` | `NOT_ASSESSED` | `REVIEW_REQUIRED` | `NOT_ASSESSED` | `NOT_ASSESSED` | `NOT_ASSESSED` | 仅保留候选映射 |
| Trusted Multi-Agent Infrastructure Developer Preview | `PASS_CORE_SCOPE` | `PASS_FROZEN_REMOTE_BASELINE` | `PASS` | `PASS_SCOPED_CLEAN_CLONE` | `PASS_CLEAN_CLONE_ADVISORY_ONLY` | `G6_SYNTHETIC_G7_PASS_G8_TRIAL_BLOCKED_PARTICIPANT_SOURCE` | 技术试用包已冻结并通过 Clean Clone；真实参与者来源、试用和发布仍未完成 |

### Developer Preview Gate Detail（开发者预览闸门明细）

| preview milestone | required gate | 当前结果 | 直接证据 | 下一状态条件 |
|---|---|---|---|---|
| `DP-1` | `G1/G2` | `PASS_CLEAN_CLONE` | DBA `91928e3` 已推送；99 个 Markdown 文件、317 个本地链接、0 缺失 | 保持同一公开入口 |
| `DP-2` | `G3/G4` | `PASS_CLEAN_CLONE` | DBOS `0caa2c4` fresh install；331/331 tests；34/34 validators | 保持同一冻结 commit |
| `DP-3` | `G4/G6` | `PASS_SYNTHETIC_SCOPE` | 11/11 tests；3 角色、3 execution records、3 Evidence References、9 Validation results | 不外推为真实 Agent/Execution |
| `DP-4` | `G3/G4/G7` | `PASS_CLEAN_CLONE_ADVISORY_ONLY` | SAEE `2173c25` public main；8/8 adapter tests；pipeline 输出 `HOLD` 且无 Authority | 不外推为 SAEE 决策权或生产集成 |
| `DP-5A` | `G8_PREPARATION` | `PASS_TECHNICAL_PACKAGE_FROZEN` | `TMAI-DP-v0.1-TRIAL-20260721-001`、Plan、Guide、Feedback Template、ADR-018 | 不表示分发、联系或试用执行授权 |
| `DP-5B` | `G1/G4/G8_TRIAL` | `BLOCKED_PARTICIPANT_SOURCE` | 参与者 0；`participant_source` 未确认；`DQ-010` 条件尚未满足 | 提供 3–5 名真实开发者或明确招募渠道 |
| `DP-R` | `G8` | `BLOCKED_DP-5B_DQ-009` | 本地候选与 Trial Plan 齐备；没有外部 Trial Result 或 `released_by_ref` | 人工发布决定和完整 release record |

## 4. Gate Evidence Record（闸门证据记录）

每次 gate 判断至少记录：

```text
gate_record_id=
gate_id=
integration_track=
scope=
evidence_refs=
observed_version_or_commit=
positive_checks=
negative_checks=
unknowns=
result=PASS|FAIL|BLOCKED|NOT_ASSESSED|NOT_APPLICABLE
reviewed_by_ref=
reviewed_at=
next_gate=
```

本格式是文档契约，不创建 Gate Service（闸门服务）、API、Permission 或自动审批系统。

## 5. Gate Authority Boundary（闸门权力边界）

- DBA 定义 gate 和记录评审结果；
- 子项目提供自己领域内的实现和证据；
- Human Decision Authority 决定是否采纳或授权；
- DBOS 只在有效授权下执行；
- SAEE 评价 gate 产生的运行材料，但不能批准自己进入下一 gate；
- validator pass（验证器通过）只对声明范围有效，不能代替人工决策、发布或采用。

```text
INTEGRATION_GATES_DEFINED=true
AUTOMATIC_GATE_APPROVAL=false
IMPLEMENTATION_AUTHORIZED=FROZEN_PUBLIC_SAFE_SOURCES_ONLY
EXECUTION_AUTHORIZED=false
```
