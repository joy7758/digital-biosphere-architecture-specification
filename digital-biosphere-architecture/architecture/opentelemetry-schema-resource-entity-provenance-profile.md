---
document_id: TMAI-OTEL-SCHEMA-RESOURCE-ENTITY-PROVENANCE-PROFILE-0.1
title: OpenTelemetry Schema, Resource, and Entity Provenance Profile v0.1
title_zh: OpenTelemetry 模式、资源与实体来源画像 v0.1
status: proposed-not-adopted-not-implemented-not-executed
decision_reference: DQ-024
primary_repository: digital-biosphere-architecture
implementation_authorized: false
deployment_authorized: false
production_ready: false
---

# OpenTelemetry Schema, Resource, and Entity Provenance Profile v0.1

## 1. Purpose（目的）

本画像定义 TMAI 如何处理 OpenTelemetry Telemetry Schema（遥测模式）、Resource
Detection（资源探测）、Resource Merge（资源合并）和 Development Entity Model
（开发中实体模型）。它解决三个生产级风险：

1. schema translation（模式转换）改变字段后失去原始来源；
2. `OTEL_RESOURCE_ATTRIBUTES`、Resource Detector 或 Collector transformation 被误作
   DBOS 可信身份；
3. OpenTelemetry `Entity` 与 TMAI Digital Entity（数字实体）同名而被错误合并。

```text
OpenTelemetry Resource != DBOS Entity Identity
OpenTelemetry Entity != TMAI Digital Entity
Resource merge precedence != trust authority
Schema translation success != Evidence or Truth
```

本画像不创建 Schema fetcher、translator、Collector、Resource Detector、Entity、DBOS
Identity、Runtime、Evidence、Verification、Permission 或 SAEE Evaluation。

## 2. Exact Source Baseline（精确来源基线）

以下为 2026-07-22 的只读观察；写入本文件不表示采纳：

| source | exact reference | status | observed SHA-256 | bounded use |
|---|---|---|---|---|
| Telemetry Schemas | OTel Specification `v1.59.0@a824fb4.../specification/schemas/README.md` | Stable | `e2004aec29dbe833bd61039b69ec8e08449daf97842a9fcef42d598b49456412` | schema family、URL、immutability、transformation lineage |
| core schema artifact | `https://opentelemetry.io/schemas/1.43.0` | published YAML；candidate only | `6ac5dd367ff707dbcdcb1e5b459d4ac2fd676fb44eb17a21f9494a9fee4233df` | vendored/digest-pinned candidate；不允许隐式网络跟随 |
| Resource SDK | OTel Specification `v1.59.0@a824fb4.../specification/resource/sdk.md` | Stable except named subsections | `2745d9cfa45d2f925ecdb12292793ee908e51dd69692dff927b03338153c66b2` | Resource create/merge/detector provenance |
| Resource Data Model | exact `v1.59.0` file | Development | `1c58df74ec7245a5a5d2054a4106c12a9041c5900794e94953336023e1436f0a` | observation-only reference；不成为 DBOS identity model |
| Entity Data Model | exact `v1.59.0` file | Development | `b0c3f6bbb5ea01628a248edd4c66cb04e5bdd480443cabf2a6b30d1685530408` | quarantine（隔离）；不映射为 Digital Entity |
| Entity Propagation | exact `v1.59.0` file | Development | `5b3ec810c707b7816643a3efcac08d5c17f8fb0a36540f1bbd84715cbb1f5102` | `OTEL_ENTITIES` untrusted input only |

官方来源：

- [Telemetry Schemas](https://opentelemetry.io/docs/specs/otel/schemas/)；
- [Resource SDK](https://opentelemetry.io/docs/specs/otel/resource/sdk/)；
- [Resource model](https://opentelemetry.io/docs/specs/otel/resource/)；
- [Entity Data Model](https://opentelemetry.io/docs/specs/otel/entities/data-model/)；
- [Entity Propagation](https://opentelemetry.io/docs/specs/otel/entities/entity-propagation/)；
- [core schema 1.43.0](https://opentelemetry.io/schemas/1.43.0)。

## 3. Stability Lanes（稳定性通道）

| lane | content | TMAI handling |
|---|---|---|
| `SCHEMA_STABLE_PINNED` | exact Stable Telemetry Schema rules + exact vendored schema artifact | 可进入 `DQ-024`；仍需 digest、source 和 transformation tests |
| `RESOURCE_SDK_STABLE_PINNED` | exact Stable Resource SDK merge/error semantics | 可进入 reference implementation contract |
| `RESOURCE_MODEL_DEVELOPMENT_OBSERVED` | Resource Data Model Development portions | 只作原始 observation semantics；不可生成 DBOS identity |
| `OTEL_ENTITY_DEVELOPMENT_QUARANTINED` | Entity model、Entity propagation、`OTEL_ENTITIES` | v0.1 默认隔离；保留 raw ref/diagnostic，不进入 trusted binding |
| `UNKNOWN_OR_DRIFTED` | unknown family/version/digest、unreviewed redirect 或 source drift | fail closed；不得猜测或静默转换 |

稳定性必须按 exact document/subsection 记录，不能因为同属 OTel `v1.59.0` 就把 Entity
Development 自动升级为 Stable。

## 4. Schema Acquisition Boundary（模式获取边界）

OpenTelemetry 允许 Schema URL 通过 HTTP(S) 获取、遵循 redirect（重定向），并指出
已发布 schema file 应保持不可变且可永久缓存。TMAI 的 production default（生产默认）
更严格：

1. Runtime 不按输入 URL 动态联网获取 schema；
2. schema 必须在 build/release gate 中预取、审查、缓存或 vendor（随制品封装）；
3. allowlist 冻结 schema family、exact URL、final redirect URL、content type、最大字节、
   timeout、digest 和 artifact provenance；
4. 禁止 credential-bearing URL、私网／link-local／metadata endpoint、`file:`、非 HTTP(S)、
   未审查 redirect、无限 redirect、DNS rebinding（DNS 重绑定）和 decompression amplification；
5. fetch/parse/digest/redirect 任一失败，结果为 `BLOCKED` 或 `REJECTED`，原始 telemetry
   保留但不转换；
6. cache key 必须绑定 exact URL、final URL、version、digest 和 file format；cache replacement、
   cross-version alias 或 mutable entry 一律拒绝；
7. upstream 文件即使声称 immutable，TMAI 仍必须按 digest 检查；digest drift 进入 Human
   Version Decision，不自动更新。

`https://opentelemetry.io/schemas/1.43.0` 的当前 digest 只是候选观察值；只有 `DQ-024`
采纳和 immutable DBA baseline 冻结后，才成为 TMAI v0.1 contract binding。

## 5. Schema Precedence and Transformation（模式优先级与转换）

OpenTelemetry Schema `v1.59.0` 原文使用 `Resource*` 与 contained
`InstrumentationLibrary*` message：两级 `schema_url` 均非空时，contained message 的值
对其包含的 signal data 取 precedence（优先）。在当前 OTLP 数据模型中，本画像把 contained
message 对应为 Instrumentation Scope 层。该规则只决定 contained signal 的有效 schema，
不是把 Resource 与 Scope 两个 schema domain 合并，也不得覆盖任一原始 URL。TMAI 必须保留
两个原始值、适用范围与 precedence reason。

每次转换必须生成 append-only Transformation Record（追加式转换记录）：

```text
transformation_id
source_signal_ref
resource_schema_url_original
scope_schema_url_original
effective_schema_url_and_precedence_reason
source_schema_artifact_digest
target_schema_url_and_digest
transformer_id_version_artifact_digest
operations_applied
unsupported_or_lossy_operations
input_projection_digest
output_projection_digest
started_at_and_ended_at
result=TRANSFORMED|UNCHANGED|REJECTED|BLOCKED|UNKNOWN
limitations
```

规则：

- 原始对象不可被覆盖；转换结果是新 projection（投影）；
- 不支持或 breaking change（破坏性变更）不得猜测；
- transform 只能执行已冻结 schema 文件中允许的操作；
- unknown transform type、family mismatch、version ordering conflict 或 digest mismatch
  必须 fail closed；
- 转换不得创建、删除或改写 `tmai.*`、`dbos.*`、`saee.*`、Permission、Authorization、
  Evidence/Verification status 等权力字段；
- transformation success 只证明规则应用，不证明输入真实、执行完整或 Evidence 有效。

GenAI exact commit 当前没有 upstream Schema URL，因此不经过 schema translation；继续使用
exact commit + mapping digest 隔离，并保留 `GENAI_SCHEMA_URL_UNAVAILABLE` limitation。

## 6. Resource Detection Provenance（资源探测来源）

Resource attribute 的每个最终值必须保留：

```text
detector_name
detector_version
detector_artifact_digest
detector_config_digest
detector_order
source_class=USER_RESOURCE|ENVIRONMENT|SDK_DEFAULT|PLATFORM_DETECTOR|COLLECTOR_TRANSFORM
source_reference
original_schema_url
merge_precedence
conflict_state
observed_value_digest
```

Resource SDK 的 merge precedence（合并优先级）只决定同名 attribute 的结果，不是
trust precedence（信任优先级）。用户提供值优先于 `OTEL_RESOURCE_ATTRIBUTES`，仍不能
因此成为 DBOS Identity 或 Authority。

### 6.1 Schema URL merge rules

- old URL empty + updating URL non-empty → 使用 updating URL；
- updating URL empty + old URL non-empty → 保留 old URL；
- 两者相同 non-empty → 保留该 URL；
- 两个不同 non-empty URL → merge error；官方说明结果 undefined/implementation-specific，
  TMAI 必须拒绝该合并输出并保存 conflict，不能选择任意一方继续。

### 6.2 Detector rules

- detector 产生 semantic-convention attributes 时必须绑定匹配 Schema URL；
- 不知道所产生 convention 的 environment detector 使用 empty URL，并显式标为 unknown；
- detector name/version/order/config 必须冻结；重复名称和顺序漂移必须报告；
- `OTEL_RESOURCE_ATTRIBUTES` 解码错误时整项丢弃并保留 error，不允许部分拼接；
- Collector enrichment 必须作为新的 transformation source，不得伪装成 SDK 原始 Resource；
- Resource 在同一 producer lifetime 内发生 identity-like drift 时开新 observation lineage，
  不覆写旧值，也不自动改变 DBOS lifecycle。

## 7. OpenTelemetry Entity Quarantine（OpenTelemetry 实体隔离）

OpenTelemetry `Entity` 在 exact `v1.59.0` 是 Development。它描述 telemetry 关联的
object of interest（关注对象）；TMAI Digital Entity 是受 DBOS Identity、Capability、
Lifecycle、Execution 和 Evidence 治理的生态成员。二者没有自动同一性。

```text
OTel Entity.type != DBOS entity_type
OTel Entity ID attributes != DBOS entity_id
OTel repeatable identity != DBOS Identity Continuity proof
OTEL_ENTITIES != Registration Authorization
OTel Entity merge != DBOS Registration or Federation
```

v0.1 handling：

1. `OTEL_ENTITIES` 和 Entity references 进入独立 quarantine raw material；quarantine record
   使用 TMAI-owned `quarantine_record_schema_version=0.1`，并精确绑定
   `otel_specification=v1.59.0@a824fb4...`、Entity source digest、输入 `schema_url` 及 digest；
   若内容引用 core semantic conventions，则另行绑定
   `core_semconv=v1.43.0@89aae438...` 和候选 schema digest。TMAI quarantine schema
   不是 OpenTelemetry Entity schema，也不提升 Development stability；
2. quarantine record 只能包含 source reference、payload digest、parser diagnostics、schema URL、
   tenant/purpose scope 与 policy binding，不得暴露 DBOS canonical identity 字段；
3. parser 结果、跳过的 malformed segment、duplicate/last-wins、schema URL 和 warning 全部保留；
4. 即使 type + ID + schema URL 可按 OTel 规则合并，也只形成 observation correlation；
5. 不同 schema URL 的 Entity 不合并；不能用 schema conversion 绕过 DBOS identity gate；
6. `service.instance.id`、host/container/Kubernetes UID 等只作 infrastructure hints；
7. 只有独立 DBOS Context + canonical record digest + Identity Continuity validator 才能形成
   `entity_reference`，且该 reference 仍不是 Permission；
8. quarantine material 没有 direct promotion（直接晋升）操作；任何未来映射必须进入
   [`digital-entity-admission-specification.md`](digital-entity-admission-specification.md)、
   [`registration-authorization-contract.md`](registration-authorization-contract.md) 与
   [`registration-boundary-rules.md`](registration-boundary-rules.md) 的既有路径：Candidate
   source 可解析 → criteria review 无 unresolved `UNKNOWN`/conflict → explicit Admission Decision
   `APPROVED` → 独立 Registration Authorization `AUTHORIZED` 且 scope 只到 `REGISTERED` →
   DBOS Registration。Registration 仍不产生 `ACTIVE`、Capability Grant 或 Permission；
9. `DQ-024` 未采纳前，trusted admission envelope 不暴露 OTel Entity projection。

## 8. Data Protection and Retention Boundary（数据保护与保留边界）

Telemetry、Resource、environment input、OTel Entity description 和 diagnostics 都可能包含
个人信息、凭据、token、secret、租户标识或受监管数据。`original input retained` 只表示不能被
转换结果静默覆盖，不表示无限期保存。

生产实现必须证明：

- field allowlist、classification（分类）、minimization（最小化）和 redaction（脱敏）在 trusted
  projection 之前执行；未知或未批准敏感字段进入隔离，不进入可信投影；
- diagnostic 只保留 bounded metadata 和 digest reference，不回显 secret/raw payload；digest
  format 固定为 `sha256:<64 lowercase hex>`，但普通 SHA-256 不是访问控制，也不能保护低熵
  payload 免受字典推断；对外只使用 tenant-scoped opaque reference，payload digest 留在授权域，
  或按独立 policy 使用 HMAC-SHA-256。不得公开低熵 payload 的裸 digest；
- 原始与隔离材料绑定 purpose、tenant/subject scope、retention class、expiry/disposition、access
  policy 和 encryption/key reference；缺失任一绑定时不得继续晋升；
- cache、raw input、lineage、result 与 evidence reference 必须 tenant-isolated（租户隔离），引用
  必须不可枚举且在访问前校验 tenant/purpose；引用和错误响应不得泄露其他租户数据是否存在；
- read/export/redact/expire/disposition 都产生 append-only governance event；合规处置可以使
  payload 不再可用，但不能改写历史 conformance result，必须保留 policy-bound tombstone 或
  disposition reference；
- 本规范不自行设定具体保留天数、法域或合规结论；这些必须由独立 data governance policy
  和 Human Decision 冻结。

Result set 的 machine contract 使用 `data_governance_binding` 显式绑定 tenant、purpose、
retention、access、encryption policy，以及 classification/redaction/isolation/retention
validation。任一为 `NOT_ASSESSED`、`FAIL` 或缺失时不得 `PASS`。

Data minimization success 不等于隐私合规，retention event 不等于 Evidence Truth。

## 9. Authority and Evidence Boundary（权力与证据边界）

Schema/Resource/Entity pipeline 不得：

- 注册、激活或退休 Digital Entity；
- 创建 Identity、Capability、Permission、Authorization 或 Execution；
- 把 schema parse/transform success 写成 Verification；
- 把 Resource/Entity consistency 写成 Evidence Truth；
- 把 OTel Entity relationship 写成 DBOS Federation；
- 把 Validator result 写成 Governance Decision；
- 因字段缺失而生成虚构值；
- 静默删除原始、失败、冲突、未知或隔离材料。

## 10. Conformance and Gate Binding（符合性与闸门绑定）

机器合同：

- [`opentelemetry-schema-resource-conformance-cases.v0.1.json`](opentelemetry-schema-resource-conformance-cases.v0.1.json)：7 组、45 个预登记用例；
- [`schemas/opentelemetry-schema-resource-conformance-case-catalog.schema.v0.1.json`](schemas/opentelemetry-schema-resource-conformance-case-catalog.schema.v0.1.json)：目录结构与零权力效果；
- [`schemas/opentelemetry-schema-resource-conformance-result-set.schema.v0.1.json`](schemas/opentelemetry-schema-resource-conformance-result-set.schema.v0.1.json)：case-level result、source/digest/Decision/reviewer 绑定；
- [`examples/opentelemetry-schema-resource-conformance-result-set.not-assessed.example.json`](examples/opentelemetry-schema-resource-conformance-result-set.not-assessed.example.json)：synthetic `NOT_ASSESSED` 示例。

Gate：

- `DQ-024`：是否采纳本 Schema/Resource stable subset 和 Entity quarantine boundary；
- `DQ-023`：core SemConv `1.43.0`/GenAI mapping 版本决定；
- `DQ-022`：OTLP `schema_url` wire field 版本决定；
- `DQ-018`：离线 adapter/validator 实现授权；
- `DQ-020`：认证 Collector/deployment 路径；
- `PR-G2/G3/G5/G6`：分别要求 exact required case groups 和独立结果。

任何 result set 均不能自行关闭 gate。

## 11. Version Change Rule（版本变化规则）

```text
SOURCE_OR_SCHEMA_CHANGE_OBSERVED
  -> exact tag/commit/URL/final URL/digest/status recorded
  -> schema transformation delta inventoried
  -> Resource detector/merge and Entity stability delta reviewed
  -> catalogs/fixtures/results updated
  -> independent agent recommendation
  -> Human Version Decision
  -> implementation and deployment decisions remain separate
```

## 12. Current State（当前状态）

```text
OTEL_SCHEMA_RESOURCE_ENTITY_PROFILE_DEFINED=true
OTEL_SCHEMA_REFERENCE_CANDIDATE=1.43.0
OTEL_SCHEMA_REFERENCE_OBSERVED_DIGEST=sha256:6ac5dd367ff707dbcdcb1e5b459d4ac2fd676fb44eb17a21f9494a9fee4233df
OTEL_RESOURCE_SDK_REFERENCE=1.59.0@a824fb4eba795c5c65dd397b3d22e7c28e934de3
OTEL_ENTITY_MODEL_STATUS=DEVELOPMENT_QUARANTINED
DQ_024_STATUS=DECIDED_REFERENCE_ADOPTED
SCHEMA_FETCHER_IMPLEMENTED=false
SCHEMA_TRANSLATOR_IMPLEMENTED=false
RESOURCE_PROVENANCE_VALIDATOR_IMPLEMENTED=false
OTEL_ENTITY_ADAPTER_IMPLEMENTED=false
CONFORMANCE_TESTS_EXECUTED=0
ENTITY_CREATED=false
IDENTITY_CREATED=false
EVIDENCE_CREATED=false
PERMISSION_CREATED=false
IMPLEMENTATION_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
PRODUCTION_READY=false
```
