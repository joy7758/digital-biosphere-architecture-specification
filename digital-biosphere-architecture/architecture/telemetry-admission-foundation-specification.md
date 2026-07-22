---
spec_id: TMAI-DBOS-TELEMETRY-ADMISSION-FOUNDATION-0.1
title: DBOS Telemetry Admission Foundation Specification v0.1
title_zh: DBOS 遥测准入基础规范 v0.1
status: proposed-pending-dq-018-not-implemented
decision_reference: DQ-018
primary_repository: digital-biosphere-os
architecture_owner: digital-biosphere-architecture
implementation_authorized: false
runtime_created: false
api_created: false
collector_deployed: false
otlp_endpoint_created: false
evidence_created: false
permission_effect: none
production_ready: false
---

# DBOS Telemetry Admission Foundation Specification v0.1

中文：DBOS 遥测准入基础规范 v0.1。

## 1. Purpose（目的）

本规范为候选实施切片 `DBOS-PR-2A-TELEMETRY-ADMISSION-FOUNDATION` 定义 exact implementation contract（精确实现契约）。它把 OpenTelemetry（开放遥测，OTel）观察材料送入 DBOS Existence Plane（存在平面）之前的接收、验证、版本、敏感数据、重复、来源和持久化边界固定下来。

该切片不接收真实网络流量，不创建 canonical Evidence Object，不调用 SAEE，也不启动 Agent、Runtime、Collector 或服务 endpoint。

```text
Contract != Implementation
Telemetry Admission != Evidence Admission
Accepted as Material != Evidence
Transport Acknowledgement != DBOS Acceptance
Duplicate Suspected != Duplicate Proven
```

## 2. Standards Baseline（标准基线）

候选实现必须显式记录实际采用版本，不能使用 `latest`：

| standard | v0.1 architecture baseline | rule |
|---|---|---|
| [OpenTelemetry Specification](https://opentelemetry.io/docs/specs/otel/) | `1.59.0` | API、SDK、Resource、Context 和 Signal 的参考语义；实现库版本必须单独记录 |
| [OTLP Specification](https://opentelemetry.io/docs/specs/otlp/) | `1.11.0` | 2026-07-22 未冻结参考基线；Trace/Metric/Log Stable；Profiles Development，首切片拒绝 Profiles |
| [Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/) | `1.43.0` | schema URL、Resource、通用属性和 signal semantics 使用显式版本 |
| [Telemetry Schemas](https://opentelemetry.io/docs/specs/otel/schemas/) | exact immutable schema URL | 不支持的 schema 不能被猜测或静默转换；本切片禁止运行时网络获取 schema |
| [GenAI attribute registry](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/) | Development / moved repository | 只允许 exact ref、metadata-only、显式 opt-in；不得写成稳定 TMAP contract |

OTel client package version、OTel specification version、OTLP version 和 Semantic Convention version 是独立版本面，不能共用一个模糊的 `otel_version` 字段。

## 3. Scope（范围）

### 3.1 Included（纳入）

- `TelemetryObservationEnvelope v0.1` closed schema（封闭 schema）；
- `TelemetryAdmissionRecord v0.1` append-only state record（只追加状态记录）；
- deterministic validation（确定性验证）和 stable reason codes（稳定原因码）；
- version and schema compatibility decision（版本与 schema 兼容判断）；
- provenance、source digest、bounded idempotency 和 duplicate classification；
- metadata-only sensitive-data policy；
- local transactional reference store、migration、backup、restore 和 integrity verification；
- bounded self-observation counters/histograms；
- positive、negative、fault、recovery、migration 和 concurrency tests。

### 3.2 Excluded（排除）

- OTLP/gRPC、OTLP/HTTP listener 或 exporter；
- OTel SDK instrumentation 或 auto-instrumentation；
- OpenTelemetry Collector deployment/configuration；
- raw prompt、response、tool arguments、tool results 或原始文件内容存储；
- canonical Evidence/Verification、Identity、Entity、Capability、Authorization 或 Permission 创建；
- SAEE transport、Evaluation、Fitness 或 Recommendation；
- multi-tenant、distributed consensus、HA、hosted service 或 production deployment；
- DBOS-EXP-0001 冻结材料修改。

## 4. Responsibility Boundary（责任边界）

| responsibility | Owner | non-owner |
|---|---|---|
| Envelope 与 Admission Record 的协议含义 | DBA | DBOS 不能单方面改变边界 |
| schema、validator、reference store 和 tests | DBOS | DBA 不实现运行逻辑 |
| OTel wire decoding | future transport adapter | 本切片不实现 |
| canonical Evidence admission | future DBOS Evidence layer | Admission Foundation 不执行 |
| Evolution evaluation | SAEE | DBOS 不生成 Fitness |
| implementation authorization | Human Program Owner | validator、模型或路线图不能批准 |

## 5. TelemetryObservationEnvelope v0.1（遥测观察封装）

### 5.1 Object Identity（对象身份）

```text
object_kind=TelemetryObservationEnvelope
schema_version=0.1.0
profile_id=TMAI-OTEL-OBSERVABILITY-PROFILE-0.1
```

Envelope 是 normalized observation material（规范化观察材料），不是 OTLP wire envelope、Execution Object 或 Evidence Object。

### 5.2 Required Fields（必需字段）

| field | type / constraint | semantics |
|---|---|---|
| `observation_id` | stable TMAI reference | 由 DBOS intake boundary 分配；不是 `trace_id` |
| `object_kind` | const | `TelemetryObservationEnvelope` |
| `schema_version` | SemVer | 本对象 schema 版本 |
| `profile_id` | const/versioned ref | TMAI OTel profile 引用 |
| `otel_spec_version` | non-empty version | 实际对齐的 OTel specification |
| `otlp_version` | version or `NOT_OTLP` | 输入 transport profile；本切片不声称已解码 OTLP |
| `semantic_convention_version` | version or `UNKNOWN` | 通用 semconv 版本；`UNKNOWN` 不能被当作兼容 |
| `semantic_convention_schema_url` | HTTPS URL or `UNKNOWN` | schema family/version；禁止运行时 fetch |
| `genai_semconv_ref` | exact version/commit or `NOT_USED` | GenAI development mapping 引用 |
| `producer_reference` | bounded reference | 产生／转交观察材料的声明来源；不是认证 Identity |
| `transport_source_reference` | bounded reference | 传输节点或离线 fixture 来源；不是 Authority |
| `resource` | closed object | Resource attributes reference + schema URL；不得含 DBOS `entity_id` 推导 |
| `instrumentation_scope` | closed object | name、version、schema URL；缺失必须拒绝或保持 `UNKNOWN` |
| `signal_type` | enum | `TRACE`、`METRIC`、`LOG`；`PROFILE` 在 v0.1 拒绝 |
| `signal_reference` | bounded reference | 外部 signal/batch 引用，不保存 payload |
| `context` | closed object | normalized `trace_id`、`span_id`、flags 和 parent state；允许 `NOT_APPLICABLE` |
| `observed_at` | timezone-aware timestamp | 声明的发生／观察时间 |
| `received_at` | timezone-aware timestamp | Admission boundary 的接收时间 |
| `clock_source` | enum/reference | `SOURCE_DECLARED`、`INTAKE_CLOCK` 或 `UNKNOWN` |
| `sampling_state` | closed object | decision、rule ref、known loss；不允许隐含完整性 |
| `redaction_state` | closed object | policy ref、result、removed/hashed counts；不保存被删除内容 |
| `content_capture_state` | enum | `DISABLED`、`METADATA_ONLY`；其他值拒绝 |
| `delivery_state` | enum | `RECEIVED`、`PARTIAL`、`RETRYING`、`DROPPED`、`UNKNOWN` |
| `source_digest` | `sha256:<64 hex>` | 上游 adapter 对 exact source bytes 的摘要；摘要不是签名或真实性 |
| `source_size_bytes` | bounded non-negative integer | 用于大小限制和审计 |
| `idempotency_reference` | bounded ref or `UNKNOWN` | upstream attempt hint（上游尝试提示）；始终不可信，最多支持 suspected classification |
| `limitations` | bounded unique reason-code array | 丢失、乱序、采样、版本、时钟、来源和隐私限制 |

### 5.3 Resource Object（资源对象）

Resource 只描述被观察的 service/process/container/deployment material：

```text
resource.reference
resource.schema_url
resource.attribute_set_digest
resource.attribute_count
```

首切片不保存任意 Resource attribute values。`service.name`、`gen_ai.agent.id`、MCP server name 或 Resource entity 不得自动成为 DBOS Identity。

### 5.4 Instrumentation Scope（插桩范围）

```text
instrumentation_scope.name
instrumentation_scope.version
instrumentation_scope.schema_url
instrumentation_scope.attribute_set_digest
```

插桩名称不是 producer authentication。缺少 name/version/schema information 时必须形成限制，不能用 Collector 名称替代。

### 5.5 Context（上下文）

- `trace_id` / `span_id` 只用于 correlation（相关性）；
- W3C Trace Context 无效时不得猜测 parent；
- Baggage 不进入本对象；
- credentials、tokens、Permission、Authorization 和 Evidence status 在 Context 中一律拒绝；
- `trace_id` 不能作为唯一 idempotency key。

## 6. TelemetryAdmissionRecord v0.1（遥测准入记录）

### 6.1 Required Fields（必需字段）

| field | semantics |
|---|---|
| `admission_record_id` | append-only transition record ID |
| `admission_id` | 一个 admission lifecycle 的稳定 ID |
| `observation_reference` | 指向 Envelope，不内嵌或改写 Envelope |
| `sequence` | 从 1 开始严格递增；同一 lifecycle 不可重复 |
| `previous_record_reference` | 除首记录外必须连续 |
| `state` | 本节定义的状态 |
| `policy_version` | admission policy exact version |
| `validator_version` | validator exact version |
| `source_digest` | 必须与 Envelope 一致 |
| `idempotency_reference` | 与 Envelope 一致的 untrusted hint 或 `UNKNOWN` |
| `intake_receipt_reference` | DBOS 在首次事务成功 commit 后签发的有界回执引用；只用于同一 admission lifecycle 重放检查 |
| `duplicate_reference` | confirmed/suspected target 或 `null` |
| `comparison_fingerprint` | 基于白名单字段的版本化摘要；只支持 suspected classification |
| `fingerprint_version` | exact canonicalization/hash policy version |
| `accepted_item_count` | 非负整数 |
| `rejected_item_count` | 非负整数 |
| `reason_codes` | bounded stable enum；不能写入 raw payload |
| `limitations` | bounded unique enum/reference list |
| `recorded_at` | DBOS intake clock timestamp |
| `actor_reference` | admission component version；不是 Human/Agent Authority |

### 6.2 States（状态）

```text
RECEIVED
  → VALIDATING
    → ACCEPTED_AS_MATERIAL
    → PARTIAL
    → REJECTED
    → DUPLICATE_CONFIRMED
    → DUPLICATE_SUSPECTED
    → UNKNOWN
```

- 所有转换必须追加新 record，不能覆盖旧状态；
- terminal result（终态结果）不得改写；重新处理必须创建新的 `admission_id` 并引用旧 lifecycle；
- `ACCEPTED_AS_MATERIAL` 只表示材料通过本策略，不创建 Evidence；
- `PARTIAL` 必须保存 accepted/rejected counts 和原因；
- `UNKNOWN` 必须保留，不得自动重试或升级。

## 7. Validation and Reason Codes（验证与原因码）

### 7.1 Validation Order（验证顺序）

```text
1. size and closed-shape limits
2. object/schema/profile version
3. field types and enum values
4. timestamp and reference syntax
5. OTel/OTLP/semconv compatibility
6. Resource and Instrumentation Scope presence
7. sensitive-content and prohibited-key scan
8. digest and provenance continuity
9. idempotency/duplicate classification
10. append-only persistence transaction
```

顺序是可观察合同：永久坏数据不能在持久化后被伪装为成功，storage failure 也不能返回 admission success。

### 7.2 Stable Reason Codes（稳定原因码）

最小集合：

```text
TA_SCHEMA_UNSUPPORTED
TA_PROFILE_UNSUPPORTED
TA_SIGNAL_UNSUPPORTED
TA_SHAPE_INVALID
TA_SIZE_LIMIT_EXCEEDED
TA_RESOURCE_MISSING
TA_INSTRUMENTATION_SCOPE_MISSING
TA_CONTEXT_INVALID
TA_SCHEMA_URL_UNKNOWN
TA_SEMCONV_UNSUPPORTED
TA_GENAI_SEMCONV_UNPINNED
TA_CONTENT_CAPTURE_PROHIBITED
TA_SENSITIVE_KEY_DETECTED
TA_DIGEST_INVALID
TA_PROVENANCE_INCOMPLETE
TA_IDEMPOTENCY_UNKNOWN
TA_INTAKE_RECEIPT_INVALID
TA_DUPLICATE_CONFIRMED
TA_DUPLICATE_SUSPECTED
TA_FINGERPRINT_POLICY_UNSUPPORTED
TA_FINGERPRINT_COLLISION_OR_LEGITIMATE_DUPLICATE
TA_IDEMPOTENCY_CONFLICT
TA_PARTIAL_INPUT
TA_SAMPLING_LIMITATION
TA_CLOCK_UNCERTAIN
TA_STORAGE_UNAVAILABLE
TA_STORAGE_INTEGRITY_FAILURE
TA_INTERNAL_UNKNOWN
```

Reason code 可以稳定，human-readable detail 必须有长度限制、转义且不得包含 raw content。

## 8. Idempotency and Duplicate Semantics（幂等与重复语义）

OTLP 在确认丢失、断线和重试时允许产生 duplicate data，因此本切片不得声称能够识别所有重复。

| condition | result |
|---|---|
| 同一 DBOS-issued `intake_receipt_reference` 可通过本地已提交记录查询，且 admission ID + `source_digest` 相同 | `DUPLICATE_CONFIRMED`；仅确认同一 intake lifecycle 重放，不确认 producer identity 或现实事件重复 |
| 同一 DBOS-issued receipt + 不同 admission ID 或 digest | `REJECTED / TA_IDEMPOTENCY_CONFLICT` |
| receipt 不存在、未 commit、格式无效或由 producer 自行声称 | `REJECTED / TA_INTAKE_RECEIPT_INVALID` |
| 只有 upstream `idempotency_reference` 或 content fingerprint 相同 | `DUPLICATE_SUSPECTED`，两条都保留 |
| `trace_id` 相同 | 只作相关性，不足以判重 |
| metrics/logs 内容相同 | 不足以证明重复 |

判重结果必须保留 lineage。`DUPLICATE_SUSPECTED` 不得静默删除，避免把合法重复观测当成重放攻击。

`intake_receipt_reference` 不是 producer credential（生产者凭据）、签名、Permission 或真实性证明。其唯一验证机制是：在同一 DBOS reference store 内查找已 commit 的原始 admission lifecycle，校验 receipt、admission ID 和 digest 一致，然后追加新的 duplicate record。本切片不定义 producer authentication；所有外部键最多形成 `DUPLICATE_SUSPECTED`。

`comparison_fingerprint` 必须使用带版本的 deterministic canonicalization（确定性规范化），且只覆盖 allowlisted metadata、`source_digest`、signal type 和有界 source binding。它不得包含原始内容，不得作为真实性、身份或 confirmed duplicate 证明。

Fingerprint collision 不做“解决”或自动合并：相同 fingerprint 的每个 Envelope 和 Admission lifecycle 均必须保留，第二及后续记录只可追加 `DUPLICATE_SUSPECTED` + `TA_FINGERPRINT_COLLISION_OR_LEGITIMATE_DUPLICATE`。如果 canonicalization version 不同或未支持，不得比较，必须返回 `TA_FINGERPRINT_POLICY_UNSUPPORTED`。

## 9. Sensitive Data and Resource Limits（敏感数据与资源限制）

参考 OTel [Security](https://opentelemetry.io/docs/security/)、[Handling sensitive data](https://opentelemetry.io/docs/security/handling-sensitive-data/) 和 [Collector hosting best practices](https://opentelemetry.io/docs/security/hosting-best-practices/)：

- 默认 `content_capture_state=DISABLED`；
- v0.1 最多允许 `METADATA_ONLY`；
- persistence serializer（持久化序列化器）必须使用 exact field allowlist，不能将输入对象、`extras`、dynamic attributes 或 `__dict__` 直接写入；
- 所有 local opaque reference 必须满足 `^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$`，external URL 只能进入专用 schema URL 字段并经 exact allowlist；应用端用户文本、文件路径、URL query、email 或 prompt 不能直接成为 reference；
- prompt、response、tool arguments/results、Baggage、credentials、tokens、PII/PHI/financial content keys 一律拒绝；
- schema URL 不在运行时获取，避免 SSRF 和 version drift；
- object bytes、nested depth、list count、reason count、reference length、attribute count 必须有硬上限；
- unknown keys 拒绝；
- high-cardinality values 不进入 metrics attributes；
- error detail 不能回显 raw input；
- store directory、backup 和 lock 文件必须是 explicit path、最小权限和非世界可读。

Prohibited-key scan 只是 defense in depth（纵深防御），不是主隔离层。主隔离层是 closed input schema + exact output allowlist + bounded opaque references。实现必须对 store、backup、exception、log、metric 和 test artifact 运行同一组 secret/PII canary 负例。

## 10. Local Transactional Reference Store（本地事务参考存储）

如果 `DQ-018` 获准，首切片采用 SQLite reference backend（SQLite 参考后端），用于证明单机事务、幂等、迁移和恢复合同，不作为 HA 或最终生产数据库声明。

### 10.0 Deployment Grade Boundary（部署等级边界）

```text
REFERENCE_CONFORMANCE_BACKEND=SQLite single-host
PRODUCTION_PERSISTENCE_BACKEND=NOT_SELECTED
PRODUCTION_DEPLOYMENT_AUTHORIZED=false
HA_RTO_RPO_VALIDATED=false
```

SQLite 选择只回答“能否用一个可重现的单机实现证明 admission contract”。它不回答 multi-node availability、tenant isolation、regional disaster recovery 或 hosted production capacity。任何未来 production persistence adapter（生产持久化适配器）必须独立实现同一 append-only/ack-after-commit/idempotency/recovery contract，重跑全部符合性测试，并经 `PR-G5`、bounded pilot 和 Human Production Authorization；不得因 SQLite 参考后端通过而自动进入生产。

### 10.1 Required Store Properties（存储要求）

- explicit caller-owned path；无默认 live DBOS path；
- SQLite foreign keys enabled；
- WAL mode 或平台支持的等价 crash-recovery mode；
- `synchronous=FULL` 或经证据批准的更强／等价设置；
- bounded busy timeout；
- schema migration table + immutable migration checksums；
- admission lifecycle、records、idempotency binding 和 backup metadata 同一数据库事务一致；
- acknowledgement only after commit（提交后才确认）；
- append-only SQL surface；无 update/delete public operation；
- SQLite online backup API 或一致 snapshot；禁止复制活跃数据库文件冒充 backup；
- restore 后执行 integrity、foreign-key、sequence、digest 和 count checks；
- corruption、disk full、lock timeout、commit interruption 均 fail closed。

### 10.2 Tables（逻辑表）

```text
schema_migrations
observation_envelopes
admission_lifecycles
admission_records
intake_receipts
untrusted_idempotency_hints
backup_manifests
```

数据库不能存 raw telemetry payload。`source_digest`、bounded metadata 和 external reference 是允许的材料。

## 11. Self-observation Contract（自观测契约）

候选 custom metrics（自定义指标）位于 `tmai.dbos.telemetry_admission.*` namespace，stability=`development`，不是 OTel 官方 Semantic Convention：

| metric | type | bounded attributes |
|---|---|---|
| `tmai.dbos.telemetry_admission.requests` | Counter | outcome、signal_type、schema_version |
| `tmai.dbos.telemetry_admission.items` | Counter | outcome、signal_type |
| `tmai.dbos.telemetry_admission.duration` | Histogram | outcome |
| `tmai.dbos.telemetry_admission.storage_commit_duration` | Histogram | outcome |
| `tmai.dbos.telemetry_admission.duplicates` | Counter | classification |
| `tmai.dbos.telemetry_admission.recovery_events` | Counter | result |

禁止加入 `trace_id`、`span_id`、observation ID、prompt、tool name、error detail 或任意用户值作为 metric attribute。

Metrics 失败不得改变 admission 结果；同时必须产生 bounded local diagnostic，不能静默隐藏自观测故障。

## 12. Compatibility and Migration（兼容与迁移）

- `0.1.x` 只允许兼容修正；
- 新 required field、状态语义变化、dedupe 语义变化或 Evidence promotion 均为 breaking change；
- unknown schema/profile/semconv 必须拒绝或 `UNKNOWN`，不得自动降级；
- migration 必须先 dry-run、backup、checksum、apply、validate；
- migration 失败必须回滚到 backup，并保留失败记录；
- downgrade 不自动执行；只能 restore 到已验证 backup；
- future OTLP adapter 必须把 transport outcome 与 admission outcome 分开记录。

## 13. Acceptance Criteria（验收条件）

实施切片只有在以下全部满足时才能进入 `PR-G2` review（审查）：

1. schema、reason codes、state machine 和 migration files 版本锁定；
2. conformance、negative、fault、concurrency、migration、backup/restore tests 全部通过；
3. current DBOS 334 tests 和 34 validators 无回归；
4. no Agent、Runtime、Permission、Evidence 或 network endpoint；
5. no raw telemetry or sensitive content persisted/reflected；
6. acknowledged committed records 在声明测试范围内 `RPO=0`；
7. restore 后 chain/count/digest/integrity 全部一致；
8. Critical/High threat finding 为 0，或有单独 Human time-bounded risk acceptance；
9. agent recommendation gate 已记录；
10. exact source commit、artifact hash 和 rollback plan 可追溯。

这些条件通过仍只表示本切片候选实现可以进入 `PR-G2`；不表示 OTLP、Collector、Evidence、SAEE、Pilot 或 Production Ready。

## 14. Non-claims（非声明）

```text
TELEMETRY_ADMISSION_SPECIFICATION_DEFINED=true
TELEMETRY_ADMISSION_IMPLEMENTED=false
TELEMETRY_ADMISSION_AUTHORIZED=false
SQLITE_STORE_CREATED=false
OTLP_LISTENER_CREATED=false
COLLECTOR_DEPLOYED=false
TELEMETRY_COLLECTED=false
EVIDENCE_CREATED=false
VERIFICATION_CREATED=false
AGENT_CREATED=false
RUNTIME_CREATED=false
PERMISSION_GRANTED=false
PRODUCTION_READY=false
```
