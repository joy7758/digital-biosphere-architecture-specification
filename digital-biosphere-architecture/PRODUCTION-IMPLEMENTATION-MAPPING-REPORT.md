---
document_id: TMAI-PRODUCTION-IMPLEMENTATION-MAPPING-20260722
title: TMAI Production Implementation Mapping Report
title_zh: TMAI 生产实现映射报告
status: pr-g1-pass-read-only-mapping-critical-implementation-gaps-open
observed_at: 2026-07-22
primary_repository: digital-biosphere-architecture
dbos_remote_main_commit: cd3f867c4379ec555c45e7d554088ad12ce08a24
saee_remote_main_commit: 2173c258f91aed03fc02c0097d4250a87be703aa
saee_development_observation_commit: 697ae2080f11b7905b20c39079914eb98169783b
implementation_effect: none
deployment_effect: none
production_implementation_authorized: false
production_ready: false
---

# TMAI Production Implementation Mapping Report

中文：TMAI 生产实现映射报告。

## 1. Gate Result（闸门结果）

```text
GATE=PR-G1
RESULT=PASS_READ_ONLY_MAPPING
MAPPING_COMPLETE=true
REMOTE_BASELINE_CREATED=false
DBOS_PRODUCTION_CORE_IMPLEMENTED=false
OTEL_INGESTION_IMPLEMENTED=false
SAEE_PRODUCTION_OTEL_ADAPTER_IMPLEMENTED=false
IMPLEMENTATION_AUTHORIZED=false
PRODUCTION_READY=false
```

`PASS_READ_ONLY_MAPPING` 只表示 TMAP（可信多智能体协议）、OpenTelemetry（开放遥测）观察平面和 Production SLO（生产服务级目标）已经逐项对照当前可取得的 DBOS/SAEE 源码。它不表示任何缺口已经实现，也不授权修改子项目、部署 Collector、创建 endpoint、运行 Pilot 或形成生产声明。

机器可读结果见 [`PRODUCTION-IMPLEMENTATION-MAPPING-v0.1.json`](PRODUCTION-IMPLEMENTATION-MAPPING-v0.1.json)。该 JSON 是本报告的 agent-readable projection（智能体可读投影），不建立第二事实权威。

## 2. Source Truth Separation（来源事实分层）

本次审计使用隔离临时目录对远程 `main` 做 depth-1 clean clone（浅层干净检出），同时只读观察本地开发工作树。三类来源不得互相替代：

| truth surface | exact observation | 用途 | 禁止外推 |
|---|---|---|---|
| DBOS remote `main` | `cd3f867c4379ec555c45e7d554088ad12ce08a24` | 当前远程主线和 Developer Preview wheel 的实现来源 | 本地旧 `origin/main`、测试通过或 wheel 发布不等于生产服务 |
| DBOS local worktree | `main@0caa2c45e511a82d0dcab778b0ffc3163aac0029`，本地 `origin/main` 同步停留于该提交，存在预先已有的 `reports/reference-runs/` 未跟踪目录 | 说明本地工作区不是远程当前主线 | 不作为本报告的生产实现基线；未修改该工作树 |
| SAEE remote public `main` | `2173c258f91aed03fc02c0097d4250a87be703aa` | 对外公开 DBOS preview 只读评价投影 | 不包含当前开发分支的全部 capability inventory（能力清单）或 OTel-style 映射 |
| SAEE development observation | `feat/canonical-capability-inventory-routing-v1@697ae2080f11b7905b20c39079914eb98169783b`；该工作树的本地 `origin/main` 为滞后的 `e503c221...` 且与当前分支无可用 merge base；remote public `main` 另行隔离检出 | 观察现有内部／开发能力和显式缺口 | 不能把本地 remote-tracking ref、单独检出的 public `main` 和 development branch 写成同一历史、公开能力或生产能力 |

本地 remote-tracking reference（远程跟踪引用）滞后本身不是代码失败，但若不区分这些表面，会把开发分支能力误写成公开主线能力，或把旧工作树误写成发布制品来源。

## 3. DBOS Mapping（DBOS 映射）

### 3.1 TMAP Object Mapping（协议对象映射）

| TMAP surface | 当前 DBOS 实现 | 分类 | 直接源码 | 生产缺口 |
|---|---|---|---|---|
| Identity Object | 只生成／验证 `PROPOSED` registration mapping；另有受控 `REGISTERED` registration record | `PARTIAL` | `entity_support/entity_registry.py`; `entity_support/registration/registration_executor.py`; `sdk/objects/entity.py`; `schemas/entity-object-schema.yaml` | 没有 canonical entity store、认证 identity binding、租户隔离、迁移与恢复 |
| Lifecycle | 生成 transition record；要求 source/verification，`ACTIVE` 等需 authorization；不修改状态 | `PARTIAL_SAFE_RECORD_ONLY` | `entity_support/lifecycle_support.py` | 没有持久 lifecycle state machine、并发冲突控制、reconciliation 或恢复演练 |
| Capability Object | declaration 默认 `UNVERIFIED`，禁止从记录派生 Permission | `PARTIAL_SAFE_RECORD_ONLY` | `entity_support/capability_registry.py`; `entity_support/capability_boundary.py`; `sdk/objects/capability.py`; `schemas/capability-object-schema.yaml` | 没有生产授权策略引擎、Permission store、revocation enforcement 或 runtime binding |
| Execution Object | construction 状态固定 `CREATED`；不执行任务 | `PARTIAL_SAFE_RECORD_ONLY` | `entity_support/execution_registry.py`; `entity_support/execution_context_integration.py`; `sdk/objects/execution.py`; `schemas/execution-object-schema.yaml` | 没有运行结果、事件顺序、重试／幂等、失败状态、长任务恢复或 runtime integration |
| Evidence Object | 只有 `EvidenceReference`，默认 `UNKNOWN/PENDING`，明确非 canonical Evidence | `REFERENCE_ONLY` | `entity_support/evidence_reference.py`; `entity_support/evidence_integration.py`; `sdk/objects/evidence_reference.py`; `schemas/evidence-reference-object-schema.yaml` | 没有本生产画像所需的 Evidence Object、admission record、provenance、integrity chain、retention 和 restore |
| Verification Object | 只有 pending `V0` reference 和有界 inert SDK object | `REFERENCE_ONLY_SCHEMA_MISMATCH` | `entity_support/verification_reference.py`; `sdk/objects/verification.py`; `schemas/verification-object-schema.yaml` | 未执行 Verification；当前 SDK 字段不足以表达 rule/version/input/limitations/verifier/time 等 TMAP 生产字段 |
| Evolution Interface | 构建 `PREPARED_NOT_SENT` reference envelope；禁止 Fitness/Risk/Recommendation/Permission 字段 | `PARTIAL_SAFE_EXPORT_PREPARATION` | `entity_support/saee_evaluation_adapter.py` | 没有 version negotiation、transport、timeout、backpressure、replay、result correlation 或生产隔离 |

### 3.2 Persistence and Recovery（持久化与恢复）

DBOS 已有有界本地持久化，但不能被称为 production durability（生产耐久性）：

- Authorization、Registration 和 Receipt store 使用 caller-supplied JSON path、`fcntl` sidecar lock、temporary file、`fsync` 和 `os.replace`；
- Authorization history、单授权一次成功登记、失败回执不可覆盖和 identity continuity 已有正负测试；
- 三个 store 彼此独立，没有跨 store transaction、WAL/journal、checksum/signature、backup/restore、schema migration、compaction、retention、multi-node consensus 或高可用；
- `fcntl` 与单机整文件重写是实现约束，不是跨平台或分布式存储承诺；
- 没有生产配置、访问控制、静态加密、容量限制、自观测和 RTO/RPO 证据。

分类：`LOCAL_ATOMIC_FILE_RECORDING_IMPLEMENTED`，`PRODUCTION_DURABILITY_NOT_IMPLEMENTED`。

### 3.3 OpenTelemetry Intake（开放遥测接入）

在 DBOS remote `main@cd3f867...` 中，对 `opentelemetry`、`otlp`、`traceparent`、`tracestate`、`baggage`、`span_id`、`instrumentation_scope` 和 GenAI Semantic Conventions 的精确源码检索结果为 0。

DBOS 现有 `environment Collector` 是冻结实验中的环境材料收集组件，不是 OpenTelemetry Collector（开放遥测收集器）。二者不得因同名而合并。

```text
OTEL_SDK_INSTRUMENTATION=false
OTLP_RECEIVER=false
OTLP_EXPORTER=false
W3C_CONTEXT_PROPAGATION=false
TELEMETRY_OBSERVATION_ENVELOPE=false
TELEMETRY_ADMISSION_LEDGER=false
TELEMETRY_TO_EVIDENCE_PROMOTION=false
COLLECTOR_DEPLOYMENT=false
```

## 4. SAEE Mapping（SAEE 映射）

### 4.1 Public Main（公开主线）

SAEE public `main@2173c25...` 提供 `saee_backend/services/dbos_developer_preview_adapter.py`：

- 接收固定 `dba.dbos-saee-developer-preview/v0.1` synthetic envelope（合成封装）；
- 验证 execution/evidence references 和结构 Validation；
- 对 `CREATED` execution fail closed，Reliability/Stability 保持 `NOT_ASSESSED`；
- Evolution Recommendation 固定为 `HOLD`，并声明 advisory-only、无 Decision/Execution authority；
- 不修改输入和 DBOS state，不建立 Evidence Truth、Fitness 或自动演化。

分类：`PUBLIC_READ_ONLY_PREVIEW_ADAPTER_IMPLEMENTED`，不是 production adapter。

### 4.2 Development Observation（开发面观察）

当前开发分支 canonical inventory（规范能力清单）明确记录：

| capability | 当前事实 | 生产解释 |
|---|---|---|
| `saee.otel_style_candidate_mapping` | `implemented / experimental` | 只映射一个 closed synthetic OTel-style event 为非权威 candidate evidence；不是 OTLP、Collector 或 semconv compliance |
| `saee.general_trace_normalization` | `partial / experimental` | 缺 span hierarchy/links、Resource/Scope、sampling/clock 和 current GenAI semconv |
| `saee.otel_sdk_or_otlp_ingestion` | `missing` | 无 SDK、OTLP/gRPC、OTLP/HTTP 或 Collector receiver |
| `saee.trusted_trace_to_evidence_conversion` | `missing` | candidate extraction 不认证 trace，也不提升为 trusted Evidence |
| `saee.external_identity_binding` | `missing` | caller-declared Agent ID 不是外部认证身份 |
| `saee.delegation_binding` | `missing` | synthetic delegation fields 不是签名的端到端 delegation chain |

`saee_backend/services/otel_candidate_mapping.py` 和 `saee_backend/observed_trace_adapter.py` 未发现网络、subprocess 或写回调用；这支持当前局部 zero-writeback（零回写）结论，但没有证明 production transport、timeout isolation、resource exhaustion 或部署安全。

## 5. OpenTelemetry / Production Gap Matrix（开放遥测／生产缺口矩阵）

| requirement | DBOS | SAEE | gate impact | Owner |
|---|---|---|---|---|
| OTel/OTLP exact version pin | `MISSING` | synthetic mapper 无 OTel SDK；GenAI mapping 未生产锁定 | `PR-G3` | DBOS implementation + DBA compatibility review |
| Resource / Instrumentation Scope separation | `MISSING` | `PARTIAL` | `PR-G3` | DBOS |
| W3C Trace Context continuity | `MISSING` | `MISSING` | `PR-G3` | DBOS + Digital Entity instrumentation |
| delivery states: accepted/partial/retry/dropped/duplicate/unknown | `MISSING` | `MISSING_INPUT` | `PR-G2/G3` | DBOS |
| provenance-preserving Telemetry admission | `MISSING` | candidate-only, non-authoritative | `PR-G2/G4` | DBOS; SAEE read-only consumer |
| sensitive data minimization/redaction | `MISSING_CONTROL` | bounded synthetic input only | `PR-G3/G5` | DBOS + deployment owner |
| queue/backpressure/cardinality limits | `MISSING` | `NOT_APPLICABLE_TO_PREVIEW_ADAPTER` | `PR-G3/G5` | DBOS + deployment owner |
| backup/restore/RPO/RTO | `MISSING` | `NOT_ASSESSED` | `PR-G2/G5` | DBOS |
| self-observation/SLI/SLO | `MISSING` | `MISSING` | `PR-G3/G5` | DBOS + SAEE + deployment owner |
| SAEE timeout/version/conflict isolation | reference envelope only | `MISSING_PRODUCTION_CONTRACT` | `PR-G4` | SAEE |
| bounded real pilot evidence | `MISSING` | `MISSING` | `PR-G6` | separately authorized deployment owner |

## 6. Validation Evidence（验证证据）

| validation | exact source | result | 证明范围 |
|---|---|---|---|
| DBOS isolated remote-main tests | `cd3f867...` | `334/334 PASS` in 15 test directories | 有界 object/SDK/registration/validator/demo contracts；不是生产运行 |
| DBOS isolated validators | `cd3f867...` | `34/34 PASS` | 当前 registry/evidence/experiment structural truth；不是 SLO/security/restore |
| SAEE public DBOS adapter tests | `2173c25...` | `8/8 PASS` | deterministic、fail-closed、no authority/evidence truth |
| SAEE development constitution smoke | `697ae208...` | `PASS` | mainline/boundary consistency；`production_ready=false` |
| SAEE governance registry check | `697ae208...` | `PASS` | registries/capabilities consistency；公开 remote 仅 projection/review surface |
| SAEE capability ledger smoke | `697ae208...` | `PASS` | 9/9 capability statuses；duplicate-build prevention |
| SAEE OTel candidate mapping smoke | `697ae208...` | `PASS` | 3 positive、3 negative、7 adversarial、15 deterministic；0 trace auto-accepted as Evidence |
| SAEE development DBOS adapter tests | `697ae208...` | `8/8 PASS` | current branch still preserves preview adapter boundary |

所有验证均设置 `PYTHONDONTWRITEBYTECODE=1` 或在隔离 clone 内执行；DBOS 和 SAEE 原工作树未被本次报告修改。

## 7. Duplicate Authority Review（重复权威审查）

| apparent overlap | 结论 |
|---|---|
| DBOS `EvidenceReference` vs future Evidence Object | reference 不是 canonical Evidence；不得建立第二 Evidence authority |
| DBOS Verification schema vs TMAP Verification Object | 当前对象为有界 preview representation；需要版本化迁移，不得并行保留两个 canonical schema |
| DBOS environment Collector vs OTel Collector | 名称相似、职责不同；禁止复用名称推断兼容 |
| SAEE OTel candidate mapping vs DBOS Telemetry admission | SAEE 只解释受限观察；DBOS 才能决定是否接纳为存在事实材料 |
| DBOS Validation vs SAEE Evaluation | structural Validation 不等于 evolution Evaluation、Fitness 或 Truth |
| OTel Resource/Agent attribute vs DBOS Identity | observation identifier 不等于 governed identity |

未发现需要在 DBA 中新建 Runtime 或第二权威；发现的是需要迁移／适配的结构差距。

## 8. DQ-018 Exact Slice Candidate（首个精确实施切片候选）

建议进入人工审查的第一个切片是：

```text
slice_id=DBOS-PR-2A-TELEMETRY-ADMISSION-FOUNDATION
primary_repository=digital-biosphere-os
owner_role=DBOS_DOMAIN_OWNER
decision_authority=HUMAN_PROGRAM_OWNER
execution_precondition=IMMUTABLE_DBA_PRODUCTION_BASELINE_COMMIT
implementation_authorized=false
```

### Included（纳入）

1. `TelemetryObservationEnvelope v0.1` schema：锁定 TMAP/OTel/OTLP/semconv version、Resource、Instrumentation Scope、signal reference、Context、sampling、redaction、delivery state、limitations；
2. `TelemetryAdmissionRecord v0.1`：`RECEIVED | VALIDATING | ACCEPTED_AS_MATERIAL | PARTIAL | REJECTED | DUPLICATE_CONFIRMED | DUPLICATE_SUSPECTED | UNKNOWN`，明确 `ACCEPTED_AS_MATERIAL != Evidence`；
3. append-only admission ledger（只追加准入台账）：DBOS-issued committed intake receipt、source digest、版本化 suspected fingerprint、provenance、重复／冲突检测和失败保留；external idempotency key 最多只能形成 suspected classification；
4. crash-safe local reference backend（崩溃安全本地参考后端）：事务边界、schema version、checksum、migration fixture、cross-version/corruption/backup/restore test；SQLite 只是 single-host conformance backend，production persistence backend 尚未选定；
5. fail-closed validation：unsupported version、missing Resource/Scope、invalid Context、partial/retry/drop、sensitive content、oversize/high-cardinality、identity/permission/evidence elevation；
6. self-observation counters：received/accepted/partial/rejected/duplicate/unknown 和 processing latency；只定义本模块内部可观测性；
7. conformance/negative/fault tests 和 agent-readable README（智能体可读说明）。

### Excluded（排除）

- OTLP network listener、Collector deployment、public API 或 hosted service；
- canonical Evidence/Verification creation；
- Entity/Agent/Runtime/Permission creation；
- SAEE invocation、Fitness、Recommendation 或 DBOS writeback；
- multi-tenant、distributed consensus、production deployment 或 SLO achieved claim；
- 修改冻结 DBOS-EXP-0001 Evidence。

### Exit Evidence（退出证据）

- exact schema and compatibility matrix；
- positive、negative、duplicate、crash/restore 和 migration tests；
- no-authority/evidence-elevation audit；
- threat model for local intake material；
- before/after complete DBOS tests and validators；
- source commit and rollback plan。

该切片不是因为“最容易”而选择；它先建立 Observation Plane→Existence Plane 的唯一、可恢复、失败关闭边界。没有这一边界，直接部署 Collector 或实现 Evidence promotion 会把传输成功误写成事实成功。

## 9. Gate and Blocker Disposition（闸门与阻塞处置）

```text
PR_G1_READ_ONLY_MAPPING=PASS
B_012_MAPPING_NOT_ASSESSED=CLEARED
B_013_DBOS_PRODUCTION_ADMISSION_DURABILITY=OPEN
B_014_SAEE_PRODUCTION_ADAPTER_ISOLATION=OPEN
DQ_018_EXACT_SLICE=READY_FOR_REVIEW
DQ_018_DECISION_PACKET_READY=true
DQ_018_AGENT_RECOMMENDATION_COMPLETE=true
DQ_018_NEXT_SLICE_RECOMMENDED_BY_TWO_AGENTS=true
DQ_018_IMPLEMENTATION_AUTHORIZED=false
PRODUCTION_CUSTOMER_RECOMMENDABLE_NOW=false
PRODUCTION_ARCHITECTURE_REMOTE_BASELINE_CREATED=false
PR_G2_DBOS_CORE_CONFORMANCE=NOT_ASSESSED
PR_G3_OTEL_OBSERVABILITY_CONFORMANCE=NOT_ASSESSED
PR_G4_SAEE_ISOLATION_CONFORMANCE=NOT_ASSESSED
PR_G5_SECURITY_RECOVERY=NOT_ASSESSED
PR_G6_BOUNDED_PILOT=NOT_ASSESSED
PR_G7_PRODUCTION_DECISION=NOT_ASSESSED
PRODUCTION_READY=false
```

下一动作必须是 Human Program Owner 对 `DQ-018` 的 scope、Owner 和实施授权作显式决定。未决定前，本报告不允许自动触发 DBOS/SAEE 修改。
