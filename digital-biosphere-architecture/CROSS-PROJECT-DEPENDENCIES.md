---
document_id: DBA-CROSS-PROJECT-DEPENDENCIES-0.1
title: Digital Biosphere Cross-project Dependency Map v0.1
title_zh: 数字生物圈跨项目依赖图 v0.1
status: architecture-dependency-baseline
dependency_is_implementation: false
dependency_is_runtime_call: false
last_reviewed: 2026-07-21
---

# Digital Biosphere Cross-project Dependency Map v0.1（数字生物圈跨项目依赖图 v0.1）

## 1. Dependency Semantics（依赖语义）

本表的 dependency（依赖）表示推进条件、数据责任、规范约束或治理交接，不表示已经存在代码 import（导入）、API、网络调用、部署关系或所有权。

合法依赖类型：

- `NORMATIVE`：规范约束；
- `DATA_CONTRACT`：数据契约；
- `GOVERNANCE_GATE`：治理闸门；
- `EVIDENCE_INPUT`：证据输入；
- `EVALUATION_INPUT`：评价输入；
- `APPLICATION_SERVICE`：应用使用基础设施的候选关系；
- `STATUS_REFERENCE`：驾驶舱只读状态引用。

## 2. Core Dependency Register（核心依赖登记）

| dependency_id | upstream | downstream | 类型 | 契约或交接 | 当前状态 | 不表示 |
|---|---|---|---|---|---|---|
| `DEP-001` | DBA | DBOS | `NORMATIVE` | DBOS 遵循已采纳的 Identity、Lifecycle、Capability、Evidence 与 Authority 边界 | `SPECIFICATION_DEFINED_ADOPTION_NOT_ASSESSED` | DBA 可以执行或修改 DBOS |
| `DEP-002` | DBA | SAEE | `NORMATIVE` | SAEE 遵循 Evaluation、Recommendation 与非执行边界 | `SPECIFICATION_DEFINED_ADOPTION_NOT_ASSESSED` | DBA 控制 SAEE 算法 |
| `DEP-003` | DBOS | SAEE | `DATA_CONTRACT` | Entity Identity、Execution History、Evidence Bundle、Verification Result、Resource Usage、Behavior Trace | `SPECIFICATION_DEFINED_IMPLEMENTATION_NOT_ASSESSED` | 已有 API 或 Runtime 调用 |
| `DEP-004` | SAEE | Governance Decision | `EVALUATION_INPUT` | Fitness、Risk、Evolution Recommendation、Governance Suggestion | `SPECIFICATION_DEFINED_IMPLEMENTATION_NOT_ASSESSED` | Recommendation 自动获批 |
| `DEP-005` | Governance Decision | DBOS | `GOVERNANCE_GATE` | Approved / Adopted result + separate Authorization reference | `SPECIFICATION_DEFINED_IMPLEMENTATION_NOT_ASSESSED` | Decision 等于 Execution |
| `DEP-006` | DBOS | Digital Entity | `APPLICATION_SERVICE` | Registration、Identity、Capability records、Execution/Evidence/Verification、Lifecycle | `ARCHITECTURE_DEFINED_ENTITY_SPECIFIC_INTEGRATION_NOT_ASSESSED` | Entity 自动 Active 或获得 Permission |
| `DEP-007` | Digital Entity | DBOS | `EVIDENCE_INPUT` | 任务、过程和输出引用进入 DBOS 有界记录 | `ARCHITECTURE_DEFINED_ENTITY_SPECIFIC_INTEGRATION_NOT_ASSESSED` | Agent 自己成为 canonical Evidence authority |
| `DEP-008` | Research Agent Pilot | DBOS | `APPLICATION_SERVICE` | 未来只读/记录接口准备 | `PREPARED_ONLY` | Research Agent 已注册、已连接或已运行 |
| `DEP-009` | Research Agent Pilot | SAEE | `EVALUATION_INPUT` | 未来 Evaluation Profile（评价配置）准备 | `PREPARED_ONLY` | 已形成 Fitness、Risk 或 Recommendation |
| `DEP-010` | Core projects | DBA | `STATUS_REFERENCE` | 项目提供带来源的状态，DBA 只读汇总 | `SOURCE_ALIGNMENT_PENDING` | DBA 状态摘要覆盖子项目事实 |

## 3. Adjacent Dependency Candidates（相邻依赖候选）

| candidate_dependency | 候选关系 | 状态 | 进入核心依赖前的要求 |
|---|---|---|---|
| POP ↔ DBOS | Persona projection 与 canonical identity 映射 | `REVIEW_REQUIRED` | Owner、schema、状态写权与冲突规则 |
| Agent Evidence → DBOS | receipt / evidence reference 交接 | `REVIEW_REQUIRED` | canonical Evidence owner、完整性与版本边界 |
| ARO → DBOS / SAEE | Audit result 作为 Verification 或 Evaluation 输入 | `REVIEW_REQUIRED` | Audit、Verification、Evaluation 三者分离 |
| Token Governor → DBOS / SAEE | 资源约束记录与资源适应度输入 | `REVIEW_REQUIRED` | 执行约束、评价和最终决策责任分离 |
| ACP ↔ DBOS | Physical Cell identity 与 Entity reference 映射 | `REVIEW_REQUIRED` | `cell_id` 不得自动等于 `entity_id` |

## 4. Dependency Change Rule（依赖变更规则）

新增或升级依赖必须：

1. 有稳定 `dependency_id`；
2. 指定 upstream、downstream 和 dependency type；
3. 引用契约、ADR 或状态来源；
4. 明确 data owner（数据所有者）、write authority（写权）和 failure behavior（失败行为）；
5. 通过 duplicate capability review；
6. 通过 [`INTEGRATION-GATES.md`](INTEGRATION-GATES.md) 的相应 gate；
7. 不把 `PLANNED`、`PREPARED_ONLY` 或 `SPECIFICATION_DEFINED` 写成 `IMPLEMENTED`。

```text
DEPENDENCY_MAP_DEFINED=true
RUNTIME_DEPENDENCIES_CREATED=false
API_DEPENDENCIES_CREATED=false
CHILD_REPOSITORIES_CHANGED=false
```
