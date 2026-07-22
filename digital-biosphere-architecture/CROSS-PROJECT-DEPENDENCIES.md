---
document_id: DBA-CROSS-PROJECT-DEPENDENCIES-0.1
title: Digital Biosphere Cross-project Dependency Map v0.1
title_zh: 数字生物圈跨项目依赖图 v0.1
status: architecture-dependency-baseline
dependency_is_implementation: false
dependency_is_runtime_call: false
last_reviewed: 2026-07-23
---

# Digital Biosphere Cross-project Dependency Map v0.1（数字生物圈跨项目依赖图 v0.1）

## 1. Dependency Semantics（依赖语义）

本表的 dependency（依赖）表示推进条件、数据责任、规范约束或治理交接，不表示已经存在代码 import（导入）、API、网络调用、部署关系或所有权。

合法依赖类型：

- `NORMATIVE`：规范约束；
- `DATA_CONTRACT`：数据契约；
- `GOVERNANCE_GATE`：治理闸门；
- `EVIDENCE_INPUT`：证据输入；
- `OBSERVATION_INPUT`：可观测性材料输入；在 DBOS 接纳前不等于 Evidence；
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
| `DEP-011` | OpenTelemetry SDK / Collector / OTLP | DBOS | `OBSERVATION_INPUT` | DQ-018 无 listener、metadata-only reference boundary 的 current source P003 模拟 32-worker run 为 18,953/18,953、0 errors；当前 manifest 的 P001/P002/P004/P005 与原生 x86_64 尚未验证 | `DQ_018_CURRENT_SOURCE_P003_PASS_FULL_WORKLOAD_REBASE_INCOMPLETE_PR_G2A_NOT_READY_NETWORK_AND_PRODUCTION_BLOCKED` | Version reference、emulation、load characterization 或 offline PASS 自动等于 SDK/Collector/runtime adoption；Telemetry 自动成为 Evidence、Verification、Truth、Permission 或 SAEE 评价结论 |
| `DEP-012` | Collector transport storage | DBOS production persistence | `NORMATIVE` | DSN、identity、network、volume、key、backup 强制隔离；delivery outcome 通过记录引用交接 | `SPECIFICATION_DEFINED_BOTH_IMPLEMENTATIONS_MISSING` | Collector WAL/message queue 是 DBOS canonical store、backup 或 RPO proof |
| `DEP-013` | Telemetry Admission | Evidence Admission | `DATA_CONTRACT` | accepted material 只能通过 EvidenceAdmissionRequest/Record、Identity Continuity、Data Governance、P0–P3 provenance 和独立 Verification 交接 | `SPECIFICATION_DEFINED_DQ_021_BLOCKED_INPUT` | `ACCEPTED_AS_MATERIAL`、Collector ack、signature 或 Human Review 自动等于 Evidence/Truth/Permission |
| `DEP-014` | Canonical Evidence / Verification | SAEE production adapter | `EVALUATION_INPUT` | SAEE 只读消费 exact objects、policy/model versions 和 delivery/privacy/completeness limitations | `SPECIFICATION_DEFINED_PR_G4_NOT_STARTED` | SAEE 自行提升 raw telemetry、回写 DBOS 或执行 Recommendation |
| `DEP-015` | DBA Collector distribution contract | future deployment infrastructure | `NORMATIVE` | `DQ-025` 已采纳 exact source/component/provider/stability inventory 和 48-case conformance boundary；仍需 `DQ-020` 绑定 build/config/runtime/Owner | `DQ_025_REFERENCE_ADOPTED_NOT_BUILT_NOT_CONFIGURED_NOT_DEPLOYED` | DBA 是 Collector operator，inventory 是 binary/image/config，或 distribution adoption 自动授权 listener、deployment、Evidence、Permission 与 production gate |
| `DEP-016` | DBA Collector deployment profile | future deployment infrastructure | `NORMATIVE` | `DQ-020` input profile 只定义 single-tenant synthetic staging 的 topology/config/security/durability/readiness 空位和现有 56/46/45/48 case reuse；真实配置必须在独立 deployment repository 产生 | `PROFILE_SCHEMA_DEFINED_DQ_020_BLOCKED_INPUT_NO_CONFIGURATION` | profile 是 Collector YAML、deployment manifest、Runtime、Owner 指派或 deployment authorization；Collector edge tier 是 AI Agent |
| `DEP-017` | DBA Collector operational evidence contract | future deployment and operations infrastructure | `NORMATIVE` | `DQ-020` input profile 定义 internal metrics/logs、命名稳定性、12 类 observation、6 类 SLI、复合 readiness、no-data/alert/runbook 与 delivery reconciliation 的失败关闭绑定；复用现有 Collector cases | `PROFILE_SCHEMA_45_NEGATIVES_TWO_MODEL_REVIEW_COMPLETE_EXACT_BINDINGS_NULL_NO_MEASUREMENT` | profile 创建 query/alert/runbook/endpoint/measurement/Evidence，或 health/dashboard/self-report 自动关闭 `PR-G3` |
| `DEP-018` | DBA human-decision readiness registry | ADR-024 / DQ-018 / DQ-022–DQ-025 / DQ-019–DQ-021 | `GOVERNANCE_GATE` | DQ-022–025、ADR-024 与 DQ-018 已记录；current source P003 receipt 和 DBA supplement 均已远端验证，但 P001/P002/P004/P005 重基线未完成 | `CURRENT_SOURCE_PACKET_REFRESH_REQUIRED_REMOTE_ATTESTED_PR_G2A_NOT_READY_NOT_APPROVED` | 注册表、supplement/attestation、P003 PASS 或 Agent recommendation 自动关闭 review gate、把模拟升级为原生、选择 backend 或授权生产 |

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
5. 对观测数据额外声明采样、基数、敏感字段、版本、部分成功、重试和重复处理；
6. 通过 duplicate capability review；
7. 通过 [`INTEGRATION-GATES.md`](INTEGRATION-GATES.md) 的相应 gate；
8. 不把 `PLANNED`、`PREPARED_ONLY` 或 `SPECIFICATION_DEFINED` 写成 `IMPLEMENTED`。

```text
DEPENDENCY_MAP_DEFINED=true
RUNTIME_DEPENDENCIES_CREATED=false
API_DEPENDENCIES_CREATED=false
CHILD_REPOSITORIES_CHANGED=false
OPENTELEMETRY_RUNTIME_DEPLOYED=false
COLLECTOR_DISTRIBUTION_ADOPTED=false
COLLECTOR_DISTRIBUTION_BUILT=false
COLLECTOR_DEPLOYMENT_PROFILE_DEFINED=true
COLLECTOR_CONFIGURATION_CREATED=false
HUMAN_DECISION_READINESS_REGISTRY_DEFINED=true
HUMAN_DECISIONS_RECORDED_BY_REGISTRY=true
REFERENCE_DECISIONS_ADOPTED=true
STAGED_SEQUENCE_ADOPTED=true
DQ_018_IMPLEMENTATION_AUTHORIZED=true
DQ_018_IMPLEMENTATION_COMPLETE=true
PR_G2A_READY_FOR_HUMAN_REVIEW=false
PR_G2A_CURRENT_SOURCE_PACKET_REFRESH_REQUIRED=true
PR_G2A_HUMAN_REVIEW_APPROVED=false
FULL_PR_G2_READY=false
IMMUTABLE_DBA_BASELINE_CREATED=true
IMMUTABLE_DBA_CONTENT_COMMIT=264f3171c3dfa8a9f614c7d0c835e4be26870d01
TELEMETRY_NE_EVIDENCE=true
EVIDENCE_NE_TRUTH=true
```
