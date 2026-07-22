---
spec_id: TMAI-OTEL-SEMANTIC-CONVENTIONS-PROFILE-0.1
title: TMAI OpenTelemetry Semantic Conventions Profile v0.1
title_zh: TMAI OpenTelemetry 语义约定画像 v0.1
status: proposed-not-adopted-not-implemented
observed_at: 2026-07-22
primary_repository: digital-biosphere-architecture
decision_reference: DQ-023
implementation_authorized: false
telemetry_created: false
evidence_created: false
production_ready: false
---

# TMAI OpenTelemetry Semantic Conventions Profile v0.1

中文：TMAI OpenTelemetry 语义约定画像 v0.1。

## 1. Purpose（目的）

本画像定义 Trusted Multi-Agent Infrastructure（可信多智能体基础设施）如何解释 OpenTelemetry Semantic Conventions（开放遥测语义约定），使不同 Agent framework、SDK、服务和 Collector 产生的 telemetry material（遥测材料）能够进入统一、可版本化且不越权的观察边界。

它补足 [`opentelemetry-observability-profile.md`](opentelemetry-observability-profile.md) 中“使用哪些信号”的说明；Schema acquisition/transformation、Resource detector provenance 与 OTel Entity quarantine 由 [`opentelemetry-schema-resource-entity-provenance-profile.md`](opentelemetry-schema-resource-entity-provenance-profile.md) 独立治理。二者都不创建 instrumentation、SDK、Collector、endpoint、Runtime、Entity、Evidence、Verification、Permission 或生产部署。

```text
OTLP = wire and delivery contract
Semantic Conventions = meaning of observed fields
TMAP = identity, capability, execution, evidence and evolution authority boundaries
```

三者可以协作，但不能互相替代。

## 2. Exact External Baselines（精确外部基线）

以下状态是 2026-07-22 的只读观察，不因写入本文件而成为已采纳版本：

| surface | exact reference | observed stability | TMAI v0.1 handling |
|---|---|---|---|
| OpenTelemetry Specification | `v1.59.0@a824fb4eba795c5c65dd397b3d22e7c28e934de3` | selected Trace、Resource 与 Instrumentation Scope contract 按组件稳定性读取 | OTel structural semantics candidate；observed HEAD `2b04e8b...` 不自动采用 |
| OpenTelemetry Semantic Conventions | `v1.43.0@89aae438b3b3b0a8dd33003c9d70592baf7dbd0d` | 每个领域和字段独立标记；不能只按仓库版本推断稳定性 | `DQ-023` 候选 core mapping baseline（核心映射基线） |
| OpenTelemetry GenAI Semantic Conventions | `2e994c6d59a93bb4fc1752c5378eedb9b8e14d6b` | Agent、tool、evaluation 和 content 字段为 `Development` | exact-commit isolated adapter input（精确提交隔离适配输入） |
| GenAI Schema URL | exact commit README 为 `TODO` | 没有可冻结的 upstream Schema URL | 必须保存 commit；不得宣称 schema compatibility（模式兼容） |
| OTLP | candidate `v1.11.0@790608c4d51e6ffc12210b541e8514cbed9e91a4` | Trace、Metric、Log stable wire scope；`DQ-022` 未采纳 | 本画像不改写 `DQ-022` 状态 |

OpenTelemetry Specification `v1.59.0` 把 Instrumentation Scope 定义为
Stable（稳定）的 `(name, version, schema_url, attributes)` 元组；OTLP `v1.11.0`
分别在 `ScopeSpans.schema_url`、`ScopeMetrics.schema_url` 与
`ScopeLogs.schema_url` 承载同一个作用域 Schema URL。机器目录使用
`instrumentation_scope.schema_url` 作为跨信号的规范化结构路径，而不是新增
OpenTelemetry attribute（属性）。这与 `otel.scope.schema_url` 这个供非 OTLP
exporter 使用的 Development（开发中）属性不同，二者不得混淆。

规范来源：

- [Semantic Conventions v1.43.0 release](https://github.com/open-telemetry/semantic-conventions/releases/tag/v1.43.0)；
- [OpenTelemetry Specification v1.59.0](https://github.com/open-telemetry/opentelemetry-specification/tree/v1.59.0)；
- [Service resource conventions](https://opentelemetry.io/docs/specs/semconv/resource/service/)；
- [Resource conventions](https://opentelemetry.io/docs/specs/semconv/resource/)；
- [Instrumentation Scope specification v1.59.0](https://github.com/open-telemetry/opentelemetry-specification/blob/v1.59.0/specification/common/instrumentation-scope.md)；
- [OTLP trace scope schema field v1.11.0](https://github.com/open-telemetry/opentelemetry-proto/blob/v1.11.0/opentelemetry/proto/trace/v1/trace.proto)；
- [GenAI exact agent span conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/2e994c6d59a93bb4fc1752c5378eedb9b8e14d6b/docs/gen-ai/gen-ai-agent-spans.md)；
- [GenAI exact repository README](https://github.com/open-telemetry/semantic-conventions-genai/blob/2e994c6d59a93bb4fc1752c5378eedb9b8e14d6b/README.md)。

`latest`、仓库 `main`、SDK 默认输出或 Collector 能启动都不是合法的生产版本证据。

## 3. Stability Lanes（稳定性通道）

| lane | upstream state | handling |
|---|---|---|
| `CORE_STABLE` | 精确版本中标记为 `Stable` 的 service、deployment、scope、error 或结构字段 | 可作为默认 metadata mapping（元数据映射），仍不得创建 DBOS 事实 |
| `CORE_DEVELOPMENT_OR_MIXED` | core semconv 中的 `Development`、`Alpha`、`Release Candidate` 或 Mixed 文档子项 | 必须按字段记录稳定性、显式 opt-in、版本漂移时 fail closed |
| `GENAI_DEVELOPMENT_PINNED` | exact GenAI commit 中的 agent、workflow、tool、evaluation、content 字段 | 只允许进入隔离观察提示；不得成为 TMAP canonical field（规范字段） |
| `DEPRECATED_REJECTED` | upstream 标记 `Deprecated` 的字段 | 新实现不得产生；接收时保留原始输入和拒绝／迁移诊断 |

同一个文档中字段稳定性可能不同。`Resource Status=Mixed` 不允许把其中所有字段统一标成 Stable；反之也不能因为文档 Mixed 而忽略 `service.name` 等精确 Stable 字段。

## 4. Two-layer Mapping Model（双层映射模型）

### 4.1 Raw OpenTelemetry layer（原始 OpenTelemetry 层）

原始 OTLP payload、Resource、Instrumentation Scope、Span、Metric、Log 和 Event 保留 upstream name、type、value、scope/schema reference 与 stability observation。TMAI 不重命名 upstream 字段，也不向 `gen_ai.*`、`service.*` 或 `otel.*` namespace 注入 DBOS 权力语义。

### 4.2 Trusted admission layer（可信准入层）

DBOS Telemetry Admission Adapter 未来可以把已验证来源的有限字段投影到 Telemetry Observation Envelope，但必须：

1. 区分原始 field value、Collector transformation 和 trusted adapter binding；
2. 由独立 DBOS context 绑定 `entity_reference`、`execution_reference` 或 `capability_reference`；
3. 不从任意 upstream attribute 自行生成上述引用；
4. 保存 mapping profile、upstream version/commit、instrumentation scope 和 transformation digest；
5. 对 unknown、conflict、missing、deprecated 和 drift 保持 fail closed。

本画像不定义新的 `tmai.*` OpenTelemetry attribute namespace。规范引用属于 admission envelope，而不是不受信任的 telemetry attribute。

## 5. Identity Boundary（身份边界）

| observed field | meaning | prohibited inference |
|---|---|---|
| `service.namespace` + `service.name` | 产生 telemetry 的逻辑服务 | DBOS Entity、Owner 或授权主体 |
| `service.instance.id` | 同一 service 的运行实例标识 | Digital Entity identity、Agent identity 或 Runtime authorization |
| `gen_ai.agent.id` | upstream hosted-agent resource hint；exact GenAI 规范不推荐写入临时内存实例 ID | DBOS `entity_id`、Registered Entity 或 Active Entity |
| `gen_ai.agent.name` / `.version` | 人类可读名称和 upstream 版本提示 | capability truth、身份连续性或已批准升级 |
| `trace_id` / `span_id` | 分布式相关性标识 | DBOS `execution_id`、完整历史或 Evidence ID |
| `gen_ai.conversation.id` | 上游会话相关性；没有真实 ID 时不得用随机 UUID、trace ID 或内容哈希伪造 | Entity identity、Execution completeness 或长期主体记忆 |

Identity Continuity 必须由 DBOS 独立校验；字段值相同只构成候选关联，不构成 identity proof（身份证明）。

## 6. Capability, Execution and Authority Boundary（能力、执行与权力边界）

- `gen_ai.operation.name=create_agent` 只表示观察到上游“创建 Agent”类型操作，不创建 TMAI Agent 或 Entity；
- `invoke_agent`、`invoke_workflow`、`plan` 和 `execute_tool` Span 只表示观察到的操作，不证明授权、成功、完整性或实际外部副作用；
- `gen_ai.tool.name`、`.type`、`.call.id` 和 tool definitions 只描述工具使用，不创建 Capability、Capability Grant 或 Permission；
- Span status、`error.type` 和 provider response 只描述观察结果，不是 DBOS Verification；
- Sampling、missing parent、disconnect、retry 或 duplicate 必须进入 limitations，不允许用完整 Span 树推断完整执行历史；
- Governance Decision、Authorization 和 Permission 不得放入 Baggage 或由任意 telemetry field 推导。

## 7. Evaluation Boundary（评价边界）

OpenTelemetry GenAI 的 `gen_ai.evaluation.*` 字段表示 upstream evaluator output（上游评价器输出）。它们可以作为明确来源和版本的 evaluation material（评价材料），但：

```text
gen_ai.evaluation.score.value != SAEE Fitness Assessment
gen_ai.evaluation.score.label != Governance Decision
gen_ai.evaluation.explanation != Evidence Truth
```

SAEE 若未来使用这些材料，必须经 DBOS read-only contract、保留 evaluator identity/version/metric definition，并独立形成 SAEE Evaluation Object。Telemetry adapter 不得产生 Fitness、Risk Assessment 或 Evolution Recommendation。

## 8. Sensitive Content Policy（敏感内容策略）

下列字段默认不得采集：

- `gen_ai.system_instructions`；
- `gen_ai.input.messages`；
- `gen_ai.output.messages`；
- `gen_ai.tool.call.arguments`；
- `gen_ai.tool.call.result`；
- `gen_ai.retrieval.query.text`；
- `gen_ai.retrieval.documents`；
- `gen_ai.evaluation.explanation`。

只有 Data Governance Gate（数据治理闸门）明确批准 purpose、data class、tenant、retention、residency、access、redaction、deletion 和 incident response 后，才可以在 exact scope 中 opt in。即使批准，也应优先记录 hash/reference、length、media type、schema digest 和 redaction outcome，而不是原始内容。

禁止把 prompt、response、reasoning、tool arguments/results、credentials、health/financial data 或 Permission 放入 Baggage。内容未采集时必须记录 `content_capture_state=DISABLED`，不能用空值伪装“内容不存在”。

机器 envelope 故意不提供 `baggage` 字段；`additionalProperties=false` 会拒绝把 Baggage 复制到准入对象。`tmai.*`、`dbos.*`、`saee.*` 以及裸 `entity_id`、`execution_id`、`permission`、`authorization`、`evidence_status`、`verification_status`、`verified` 属性同样不得进入 raw attribute projection（原始属性投影），以阻止 telemetry-side authority injection（遥测侧权力注入）。原始 payload 若包含这些字段，必须在隔离原始材料中保留并以 rejected/unknown diagnostic 处理，不能映射为规范对象。

## 9. Cardinality and Cost Policy（基数与成本策略）

- `service.name`、`service.namespace`、`gen_ai.operation.name`、`gen_ai.provider.name`、`gen_ai.workflow.name` 和 `error.type` 必须有有界字典或预算；
- `gen_ai.workflow.name` 只有在低基数、应用提供的静态名称存在时才记录；
- `gen_ai.agent.id`、`conversation.id`、tool call ID、trace/span ID 和 provider response ID 不得成为 Metric label（指标标签）；
- model、tool 和 error dimensions 必须定义最大唯一值、overflow behavior 和 cardinality telemetry；
- 超预算时保留 dropped/aggregated/unknown limitation，不得静默丢弃后报告完整。

机器目录明确列出 metric label 禁止字段、需要 deployment budget 的低基数字段、`PER_TENANT_PER_SERVICE_PER_WINDOW` 预算范围和统一 overflow behavior。具体数值必须由 `DQ-020` 的 exact deployment profile 按 workload 冻结；在数值缺失前，相关生产 Metric profile 不可通过。

## 10. Instrumentation and Schema Binding（插桩与模式绑定）

每个 observation batch（观察批次）必须记录：

- Instrumentation Scope name/version；
- Scope schema URL，缺失时明确 `unknown`；
- SDK name/language/version；
- distribution name/version（如存在）；
- core semconv exact tag/commit；
- GenAI exact commit（使用时）；
- OTLP exact tag/commit；
- Collector distribution/component/config digest（经过 Collector 时）；
- mapping profile ID/digest。

GenAI upstream exact commit 的 Schema URL 为 `TODO`，因此 v0.1 必须用 exact commit + mapping digest 绑定，不能制造或猜测 upstream Schema URL。

core schema artifact、Resource/Scope precedence 和任何未来 schema translation 只有在独立
`DQ-024` 决定与 provenance contract 下才可进入实现考虑；`DQ-023` 的 semantic mapping
adoption 不能替代 `DQ-024`，反之亦然。

Instrumentation Scope 的 `schema_url` 缺失时必须记录 `unknown` limitation（未知限制），不得猜测；这不要求拒绝同批次中其余可独立解释的 Stable metadata。GenAI 因 exact commit 明确没有可用 Schema URL，必须以 commit + mapping digest 代替，并保留该限制。

## 11. Machine Contract（机器合同）

- [`opentelemetry-semantic-mapping.v0.1.json`](opentelemetry-semantic-mapping.v0.1.json)：47 项字段处理目录；
- [`schemas/opentelemetry-semantic-mapping.schema.v0.1.json`](schemas/opentelemetry-semantic-mapping.schema.v0.1.json)：目录形状和非权威效果约束；
- [`schemas/opentelemetry-semantic-observation.schema.v0.1.json`](schemas/opentelemetry-semantic-observation.schema.v0.1.json)：单个映射结果 envelope 的 fail-closed 结构；
- [`examples/opentelemetry-semantic-observation.not-assessed.example.json`](examples/opentelemetry-semantic-observation.not-assessed.example.json)：synthetic `NOT_ASSESSED` 示例；
- [`opentelemetry-semantic-conformance-profile.md`](opentelemetry-semantic-conformance-profile.md)：46 个用例的执行层、证据和 gate 规则；
- [`opentelemetry-semantic-conformance-cases.v0.1.json`](opentelemetry-semantic-conformance-cases.v0.1.json)：8 组、46 个预登记用例和 47/47 mapping coverage；
- [`schemas/opentelemetry-semantic-conformance-case-catalog.schema.v0.1.json`](schemas/opentelemetry-semantic-conformance-case-catalog.schema.v0.1.json)：目录形状和零权力效果约束；
- [`schemas/opentelemetry-semantic-conformance-result-set.schema.v0.1.json`](schemas/opentelemetry-semantic-conformance-result-set.schema.v0.1.json)：case-level result、digest、decision、implementation、environment、review 和 fail-closed `PASS` 约束；
- [`examples/opentelemetry-semantic-conformance-result-set.not-assessed.example.json`](examples/opentelemetry-semantic-conformance-result-set.not-assessed.example.json)：46 个 required case 均未执行的 synthetic `NOT_ASSESSED` 示例。

Schema validation 只证明 shape（形状），不证明 upstream authenticity、DBOS binding、Evidence admissibility、conformance execution 或 production readiness。唯一性、47/47 coverage、group closure、stability drift 和 cross-field binding 仍需要独立 semantic validator（语义验证器）。

## 12. Required Conformance（必需符合性）

未来实现至少验证：

1. Stable core metadata 保留 exact upstream semantics；
2. Resource、Instrumentation Scope 和 observed subject 不混淆；
3. forged `service.instance.id` / `gen_ai.agent.id` 不能创建或绑定 DBOS Identity；
4. trace/span/conversation ID 不能创建 `execution_id`；
5. `invoke_agent` / `execute_tool` 不能创建 Capability、Permission 或成功执行事实；
6. `gen_ai.evaluation.*` 不能创建 SAEE Evaluation 或 Governance Decision；
7. sensitive content 默认 disabled，opt-in 缺少治理字段时拒绝；
8. deprecated `gen_ai.system`、`gen_ai.prompt` 和 `gen_ai.completion` 被拒绝并记录迁移诊断；
9. GenAI commit 或 mapping digest 漂移时 fail closed；
10. high-cardinality、sampling、drop、duplicate、retry 和 out-of-order limitations 被保留；
11. observation acceptance 不创建 Evidence 或 Verification；
12. 所有负例保留失败结果，不静默覆盖。

上述要求已经被投影为 8 组、46 个预登记用例并完成 47/47 mapping ID
覆盖检查，但 semantic validator（语义验证器）尚未实现，46 个用例全部为
`NOT_EXECUTED`。先前的 20/20 local negative rehearsal（本地负例演练）只验证
mapping/observation Schema 对畸形对象的拒绝，不是 DBOS 实现或 conformance execution
（符合性执行）证据。

## 13. Version Change Rule（版本变化规则）

```text
UPSTREAM_CHANGE_OBSERVED
  -> EXACT_COMMIT_AND_TAG_RECORDED
  -> FIELD_STABILITY_DELTA_INVENTORIED
  -> CONTENT_AND_CARDINALITY_REVIEWED
  -> MAPPING_AND_FIXTURES_UPDATED
  -> POSITIVE_AND_NEGATIVE_CONFORMANCE
  -> AGENT_RECOMMENDATION
  -> HUMAN_VERSION_DECISION
  -> PROFILE_ADOPTION
```

GenAI 获得 release tag 或 Schema URL 时也必须走完整流程；不能自动把当前 Development mapping 升级为 Stable。

## 14. Non-claims（非声明）

```text
OTEL_SEMANTIC_PROFILE_DEFINED=true
OTEL_SEMANTIC_PROFILE_STATUS=REFERENCE_ADOPTED_NOT_IMPLEMENTED
CORE_SEMCONV_CANDIDATE=1.43.0@89aae438b3b3b0a8dd33003c9d70592baf7dbd0d
GENAI_SEMCONV_CANDIDATE=2e994c6d59a93bb4fc1752c5378eedb9b8e14d6b
GENAI_SCHEMA_URL_AVAILABLE=false
SEMANTIC_MAPPING_IMPLEMENTED=false
SEMANTIC_CONFORMANCE_PROFILE_DEFINED=true
SEMANTIC_CONFORMANCE_CASE_GROUPS=8
SEMANTIC_CONFORMANCE_CASES=46
SEMANTIC_CONFORMANCE_MAPPING_COVERAGE=47/47
SEMANTIC_CONFORMANCE_RESULT_SET_SCHEMA_DEFINED=true
SEMANTIC_CONFORMANCE_RESULT_SET_EXAMPLE=NOT_ASSESSED
SEMANTIC_CONFORMANCE_VALIDATOR_IMPLEMENTED=false
SEMANTIC_CONFORMANCE_TESTS_EXECUTED=0
TELEMETRY_CREATED=false
ENTITY_CREATED=false
EXECUTION_CREATED=false
EVIDENCE_CREATED=false
VERIFICATION_CREATED=false
PERMISSION_CREATED=false
SAEE_EVALUATION_CREATED=false
IMPLEMENTATION_AUTHORIZED=false
PRODUCTION_READY=false
```
