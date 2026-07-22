---
spec_id: TMAI-OTEL-OBSERVABILITY-PROFILE-0.1
title: TMAI OpenTelemetry Observability Profile v0.1
title_zh: TMAI OpenTelemetry 可观测性配置 v0.1
status: accepted-non-executable-observability-profile
decision_reference: ADR-023-trusted-multi-agent-protocol-and-production-observability.md
observed_at: 2026-07-22
primary_repository: digital-biosphere-architecture
implementation_authorized: false
collector_deployed: false
otlp_endpoint_created: false
telemetry_collected: false
evidence_created: false
---

# TMAI OpenTelemetry Observability Profile v0.1

## 1. Scope（范围）

本配置定义 Trusted Multi-Agent Infrastructure（可信多智能体基础设施）如何使用 OpenTelemetry（开放遥测，简称 OTel）形成 production-oriented observation plane（面向生产的观察平面）。

它规范 Trace、Metric、Log、Resource、Context、OTLP 和 Collector 与 DBOS Evidence/Verification、SAEE Evaluation 之间的边界。它不是 Collector 配置、SDK 实现、endpoint、Backend 选择或生产部署。

## 2. Reference Baseline（参考基线）

以下是 2026-07-22 的外部规范观察，不因写入本文件而成为 TMAI 实现事实：

| 外部表面 | 观察版本或引用 | 规范来源 | 使用规则 |
|---|---|---|---|
| OpenTelemetry Specification | release `v1.59.0@a824fb4eba795c5c65dd397b3d22e7c28e934de3`; separately observed repository HEAD `2b04e8b639d2a1baf2e1eaab68ee254cdc6100f0` is not adopted by this profile | [Specification](https://opentelemetry.io/docs/specs/otel/) / [v1.59.0 tag](https://github.com/open-telemetry/opentelemetry-specification/tree/v1.59.0) / [Versioning and Stability](https://opentelemetry.io/docs/specs/otel/versioning-and-stability/) | Context、Resource、Signal、SDK/Exporter 基础语义；逐组件读取 stability（稳定性）状态；不得把 moving HEAD 当成 `v1.59.0` release |
| OTLP | candidate `v1.11.0`; exact commit `790608c4d51e6ffc12210b541e8514cbed9e91a4` | [tagged release](https://github.com/open-telemetry/opentelemetry-proto/releases/tag/v1.11.0) / [OTLP Specification](https://opentelemetry.io/docs/specs/otlp/) | version delta 与两路评审完成；`DQ-022` 未决定，不能称 adopted/frozen reference；Trace、Metric、Log 为 Stable；Profiles 为 Development，不进入 v0.1 生产必需信号 |
| Semantic Conventions | `1.43.0`; repository HEAD `c63d375f9d4b0ea4a115566138617a29c7416ae5` | [Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/) | 通用、HTTP、RPC、Messaging、Resource 等采用显式版本 |
| GenAI Semantic Conventions | repository HEAD `2e994c6d59a93bb4fc1752c5378eedb9b8e14d6b`; README `Schema URL: TODO` | [exact repository tree](https://github.com/open-telemetry/semantic-conventions-genai/tree/2e994c6d59a93bb4fc1752c5378eedb9b8e14d6b) / [GenAI attribute registry](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/) | 只允许版本钉住的 Development mapping；不得作为稳定 TMAP 合同 |
| Schema / Resource / Entity provenance | exact OTel `v1.59.0` Stable Schema/Resource SDK subset + Development Resource Data Model/Entity quarantine + core schema `1.43.0` candidate | [`opentelemetry-schema-resource-entity-provenance-profile.md`](opentelemetry-schema-resource-entity-provenance-profile.md) | `DQ-024=READY_FOR_REVIEW`；45 cases 全部未执行，reference 未采纳、validator 未实现 |
| Collector Releases | repository HEAD `c895ad0e762bbd5d337a8a9c989c4fc8700db7f3` | [Collector releases repository](https://github.com/open-telemetry/opentelemetry-collector-releases) / [deployment patterns](https://opentelemetry.io/docs/collector/deploy/) | 实现阶段另选受支持版本；本规范不自动采用 latest |

外部规范会变化。每个实现必须记录实际使用的 SDK、Collector、OTLP、Semantic Convention 和 instrumentation version；`latest` 不是合法生产版本标识。上游页面变化不自动修改已冻结 TMAI profile：必须记录 old/new version、normative delta、wire/schema/behavior compatibility、fixture impact 和 Human Version Decision，才能更新本表。`v1.11.0` 的当前证据与待决状态见 [`OTLP-1.11-VERSION-DELTA-ASSESSMENT.md`](../OTLP-1.11-VERSION-DELTA-ASSESSMENT.md) 和 `DQ-022`。

## 3. Adopted OpenTelemetry Architecture Patterns（采用的架构模式）

### 3.1 Vendor-neutral signal model（供应商中立信号模型）

使用 Trace、Metric 和 Log 描述观察材料，不将观测后端的私有字段写入 TMAP canonical objects（规范对象）。Profiles 在 OTLP 中仍为 Development，因此 v0.1 只可作为可选实验输入。

### 3.2 Resource and Instrumentation Scope（资源与插桩范围）

所有信号必须关联 Resource 和 Instrumentation Scope，以识别“被观察对象”和“产生观察的插桩”。二者必须分别记录，避免把 eBPF、sidecar 或 Collector 当作被观察主体。

Resource/Scope `schema_url` precedence、Schema acquisition/cache/transformation、detector merge
provenance 和 OTel Entity/`OTEL_ENTITIES` quarantine 必须遵循
[`opentelemetry-schema-resource-entity-provenance-profile.md`](opentelemetry-schema-resource-entity-provenance-profile.md)。
`OTel Entity != TMAI Digital Entity`，普通 Resource/Entity observation 不产生 Identity、Permission
或 Evidence Truth。

### 3.3 Context Propagation（上下文传播）

分布式调用优先采用 W3C Trace Context。`trace_id`、`span_id` 和 trace flags 只用于相关性；不能承担 DBOS Identity、Authorization、Permission 或 Evidence status。

### 3.4 Collector separation（收集器解耦）

Collector 只承担 receive、process、batch、queue、export 和 self-observation。它不得：

- 创建或激活 DBOS Entity；
- 授予 Capability 或 Permission；
- 把 telemetry 标记为 Truth；
- 生成 SAEE Fitness；
- 作为唯一 Evidence store 或 Verification Authority；
- 静默丢弃后仍报告完整链路。

## 4. Recommended Production Topology（推荐生产拓扑）

```text
Digital Entity / Service instrumentation
  ├─ OTel SDK or auto-instrumentation
  ↓ OTLP over authenticated TLS
Local Collector agent pattern
  ↓ bounded processing, redaction, queue
Gateway Collector pattern
  ├─ Observability backend: traces / metrics / logs
  └─ DBOS Telemetry Transport Adapter: selected metadata-only material
         ↓ Telemetry Observation Envelope
     Telemetry Admission Record
         ↓ separate Evidence Admission Request/Record
     Evidence Object + independent Verification Object
         ↓ read-only contract
     SAEE Evaluation / Recommendation
```

这里的 Collector agent pattern 是 OTel 部署术语，不是 AI Agent、Digital Entity 或 Agent instance。

首个生产配置推荐 self-hosted、single-tenant、human-governed。多租户、跨区域和托管 SaaS 需要独立 Deployment Profile 与威胁模型。

## 5. Signal-to-TMAP Mapping（信号映射）

| OTel 表面 | TMAP 中的允许用途 | 不允许的自动升级 |
|---|---|---|
| Resource | 观察对象、服务、进程、容器或部署上下文引用 | Resource → `entity_id` |
| Trace | 分布式工作流的相关性和因果候选结构 | Trace → Execution completeness / Evidence |
| Span | 有界操作观察、时长、状态和属性 | Span → authorized action / truth |
| Span Event | 操作中的离散观察 | Event → canonical lifecycle transition |
| Metric | SLI、容量、资源与趋势输入 | Metric → SAEE Fitness 或 Risk conclusion |
| Log | 诊断、事件和错误材料 | Log → Evidence Truth |
| Baggage | 非敏感、有限的跨进程相关信息 | Baggage → secrets、Permission、Authorization、PII 或 Evidence status |
| OTLP response | 传输接收、部分接收或失败诊断 | HTTP/gRPC success → DBOS canonical acceptance |
| Collector internal telemetry | Collector 健康、吞吐、拒绝和资源使用 | Collector health → end-to-end evidence completeness |

## 6. Telemetry Observation Envelope（遥测观察封装）

进入 DBOS intake 前，每批或每个可寻址观察应能够表达：

| 字段 | 语义 |
|---|---|
| `telemetry_profile_version` | 本配置版本 |
| `otel_spec_version` | 实际实现所对齐的 OTel specification version |
| `otlp_version` | 实际传输版本；非 OTLP 时明确记录 transport profile |
| `semantic_convention_version` | 通用 Semantic Convention 版本 |
| `genai_semconv_ref` | GenAI/MCP profile 的 exact version/commit；未使用则为空 |
| `resource_ref` | 被观察 Resource 的有界标识和属性引用 |
| `instrumentation_scope` | 插桩名称、版本、schema URL 或明确 `unknown` |
| `signal_type` | `trace`、`metric`、`log` 或受限 `profile` |
| `trace_id` / `span_id` | 可选相关性标识，不作为 DBOS 对象 ID |
| `observed_at` | 观察时间及其时钟来源 |
| `received_at` | 当前接收节点记录时间，不替代发生时间 |
| `collector_path` | 经过的 Collector/processor/exporter 引用 |
| `sampling_state` | 采样决策、规则和已知完整性限制 |
| `redaction_state` | 删除、哈希、截断或过滤规则版本 |
| `delivery_state` | accepted、partial、retrying、dropped、duplicate-suspected 或 unknown |
| `content_capture_state` | disabled、metadata-only、bounded-content 或 prohibited |
| `limitations` | 丢失、乱序、重复、时钟、基数和隐私限制 |

该表是 architecture summary（架构摘要），不是已实现 schema。Exact closed schema、状态、敏感数据、幂等和 reference store 合同以 [`telemetry-admission-foundation-specification.md`](telemetry-admission-foundation-specification.md) 为准。Envelope 仍是 telemetry material（遥测材料），不是 Evidence Object。

## 7. Telemetry → Evidence Admission（遥测到证据的准入）

```text
Raw Telemetry
  → Transport Validation
  → Version and Schema Validation
  → Deduplication / Ordering Assessment
  → Redaction and Data-classification Check
  → Provenance Binding
  → Telemetry Admission Record (material only)
  → separate Evidence Admission Request/Record
  → Evidence Object
  → independent Verification Object
```

必须满足：

1. 传输成功不等于 DBOS 接纳；
2. OTLP 允许重试导致 duplicate data（重复数据），DBOS 必须幂等或显式标记重复；
3. OTLP partial success 必须保存 rejected counts 和诊断；
4. dropped signal、queue overflow、sampling 和 processor error 必须进入完整性限制；
5. 任何字段冲突、版本不兼容或来源不明均保持 `unknown`/`partial`/`rejected`；
6. Evidence Object 与 Verification Object 必须使用新的 DBOS ID，并引用原 telemetry；
7. SAEE 只能消费接纳后的对象或明确标记的受限材料。

Telemetry Admission 的 exact contract 见 [`telemetry-admission-foundation-specification.md`](telemetry-admission-foundation-specification.md)；第二阶段 Evidence Admission 见 [`telemetry-to-evidence-admission-contract.md`](telemetry-to-evidence-admission-contract.md)。两个合同不得合并或用 Collector 配置替代。

Production Collector 部署、HA、queue/WAL、delivery accounting、single-writer 和安全候选以 [`otlp-collector-production-profile.md`](otlp-collector-production-profile.md) 为准。

## 8. Sampling, Cardinality and Long-running Work（采样、基数与长期运行）

- 可观测性采样不得被写成完整执行历史；
- evidence-critical（证据关键）事件必须走不依赖概率采样的 DBOS 记录路径，或在缺失时 fail closed；
- tail sampling 可以用于诊断保留，但不得改变已确认的 DBOS 对象；
- 所有高基数属性必须有预算、限制或降维策略；
- 长期 workflow 必须使用稳定 workflow/execution references，不能只依赖短生命周期 Span；
- 时钟偏差、乱序、断链和跨 Collector 重试必须进入 Verification limitations。

## 9. Security and Sensitive Data（安全与敏感数据）

生产实现必须：

- 对 OTLP 入口和出口使用认证、加密传输与明确 trust boundary；
- 最小化 Collector 组件和监听面；
- 使用最小权限、网络限制、资源上限和内部遥测；
- 对 queue、buffer、temporary storage 和配置中的秘密实施访问控制；
- 默认禁用 prompt、response、tool arguments、tool results 和原始文件内容采集；
- 使用 allowlist、attribute/filter/redaction/transform processors 执行数据最小化；
- 禁止在 Baggage 中传播凭据、令牌、Permission、Authorization、健康或金融数据；
- 保存 redaction policy version 和处理结果，但不保存被删除秘密的副本；
- 为 DoS、超大 payload、高基数和恶意属性制定限流与失败关闭规则。

实现与审查应以 OpenTelemetry 的 [security guidance](https://opentelemetry.io/docs/security/)、[Collector hosting practices](https://opentelemetry.io/docs/security/hosting-best-practices/) 和 [sensitive-data guidance](https://opentelemetry.io/docs/security/handling-sensitive-data/) 为最低外部参考；引用这些指南不等于已通过安全审计。

## 10. GenAI and MCP Profile（生成式 AI 与 MCP 配置）

GenAI 和 MCP Semantic Conventions 当前只作为 version-pinned adapter input（版本钉住的适配输入）：

1. 必须记录 exact repository commit 或 published version；
2. 不稳定字段放在隔离 mapping namespace；
3. Breaking Change 必须产生新 mapping version 和兼容声明；
4. 内容采集默认 `disabled` 或 `metadata-only`；
5. `invoke_agent`、`execute_tool`、evaluation event 等 OTel 术语不能自动创建 TMAP Agent、Execution、Evaluation 或 Decision Object；
6. 如果上游没有稳定 Schema URL，禁止宣称长期兼容；
7. 升级只能经过 mapping conformance 和回放验证，不能跟随 `latest` 自动更新。

## 11. Conformance Requirements（符合性要求）

生产候选至少验证：

- Trace/Metric/Log OTLP round trip；
- Resource 与 instrumentation identity 不混淆；
- W3C Trace Context 跨进程连续性与无上下文负例；
- duplicate、partial success、retryable、non-retryable 和 dropped data；
- sampling 导致的不完整性被正确标记；
- PII、token、prompt、tool arguments 的默认不采集或脱敏；
- Collector 断开、重启、磁盘满、后端不可用和 queue overflow；
- Telemetry 不会直接生成 Permission、Fitness、Decision 或 canonical Evidence；
- GenAI version drift 被 fail closed；
- Collector 自身 telemetry 可支持容量和故障诊断。

## 12. Non-claims（非声明）

```text
OTEL_PROFILE_DEFINED=true
OTEL_PROFILE_IMPLEMENTED=false
OTLP_ENDPOINT_CREATED=false
COLLECTOR_DEPLOYED=false
OBSERVABILITY_BACKEND_SELECTED=false
TELEMETRY_COLLECTED=false
TELEMETRY_ACCEPTED_AS_EVIDENCE=false
EVIDENCE_CREATED=false
VERIFICATION_CREATED=false
PRODUCTION_READY=false
```
