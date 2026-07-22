---
document_id: TMAI-OTLP-1.11-DELTA-20260722-001
title: OTLP v1.10.0 to v1.11.0 Version Delta Assessment
title_zh: OTLP v1.10.0 至 v1.11.0 版本差异评估
status: reviewed-candidate-reference-not-adopted
observed_at: 2026-07-22
source_repository: open-telemetry/opentelemetry-proto
source_version: v1.10.0
target_version: v1.11.0
implementation_effect: none
deployment_effect: none
---

# OTLP v1.10.0 → v1.11.0 Version Delta Assessment

## 1. Decision Summary（决策摘要）

```text
UPSTREAM_RELEASE_VERIFIED=true
SOURCE_TAG=v1.10.0
SOURCE_COMMIT=ca839c51f706f5d53bfb46f06c3e90c3af3a52c6
TARGET_TAG=v1.11.0
TARGET_COMMIT=790608c4d51e6ffc12210b541e8514cbed9e91a4
TARGET_RELEASE_PUBLISHED_AT=2026-07-21T13:54:02Z
TARGET_RELEASE_IS_DRAFT=false
TARGET_RELEASE_IS_PRERELEASE=false
COMMITS_AHEAD=42
FILES_CHANGED=29
TMAI_SELECTED_STABLE_SIGNAL_WIRE_BREAK=false
TRANSPORT_BEHAVIOR_DELTA=true
RUNTIME_INTEROPERABILITY_TESTED=false
TARGET_REFERENCE_ADOPTED=false
```

建议把 `v1.11.0` 作为 TMAI v0.1 production-path（生产路径）的 OTLP candidate reference（候选参考版本），但必须经过 `DQ-022` 的显式 Architecture Version Decision（架构版本决定）后才能成为冻结参考。

这个建议不选择 SDK、Collector distribution、Collector image、receiver、endpoint 或 backend，也不证明任何 DBOS 实现支持 `v1.11.0`。

## 2. Official Source Evidence（官方来源证据）

| evidence_id | 官方来源 | 观察事实 |
|---|---|---|
| `OTLP-111-E01` | [v1.11.0 release](https://github.com/open-telemetry/opentelemetry-proto/releases/tag/v1.11.0) | 正式 release，2026-07-21 发布，非 draft、非 prerelease |
| `OTLP-111-E02` | [v1.10.0...v1.11.0 compare](https://github.com/open-telemetry/opentelemetry-proto/compare/v1.10.0...v1.11.0) | `v1.11.0` 相对 `v1.10.0` 前进 42 个提交；29 个文件发生变化 |
| `OTLP-111-E03` | [v1.11.0 changelog](https://github.com/open-telemetry/opentelemetry-proto/blob/v1.11.0/CHANGELOG.md) | 新增 request/response size limits、ProcessContext；澄清 `Retry-After` |
| `OTLP-111-E04` | [v1.11.0 protocol specification](https://github.com/open-telemetry/opentelemetry-proto/blob/v1.11.0/docs/specification.md) | 定义 gRPC/HTTP 请求与响应的 pre/post compression/decompression 限制和失败语义 |
| `OTLP-111-E05` | [v1.11.0 maturity table](https://github.com/open-telemetry/opentelemetry-proto/blob/v1.11.0/README.md#maturity-level) | Trace、Metric、Log 为 Stable；Profiles 与 Process Context Sharing 为 Development |

所有来源均钉住到正式 tag 或 exact commit；`main`、`latest` 和搜索摘要不是冻结来源。

## 3. Delta Classification（差异分类）

### 3.1 Selected stable TMAI scope

TMAI v0.1 production-required signal scope（生产必需信号范围）仍为 Trace、Metric 和 Log。比较结果中：

- trace proto 无变化；
- logs proto 无变化；
- metrics proto 只修改 unit 注释中的外部链接；
- common proto 只修正文档并把 Profiling 使用的实验字段状态从 `Development` 标为 `Alpha`；
- 没有改变 TMAI 当前选定稳定范围内既有字段的 number、type、name、cardinality 或 service method。

结论：在 TMAI 明确排除 Profiles/Process Context 的当前范围内，没有发现 stable wire breaking change（稳定线协议破坏）。这不是 Runtime interoperability（运行互操作性）测试结果。

### 3.2 Transport behavior delta

`v1.11.0` 对生产接收面增加了必须进入 TMAI control profile（控制配置）的规范行为：

| surface | upstream normative behavior | TMAI candidate control |
|---|---|---|
| gRPC server request | 解压后必须限制；推荐默认 `64 MiB`；超限返回非重试 `RESOURCE_EXHAUSTED` | 同时记录 compressed/uncompressed limits、失败计数和 discard reason |
| gRPC client request | 压缩前应限制；推荐默认 `64 MiB`；超限不得发送并应记录丢弃 | exporter/client 侧必须有独立 outbound limit |
| gRPC client response | 解压后必须限制；典型 `4 MiB` 可接受；超限视为非重试错误 | response decompression limit 与错误分类必须可测 |
| gRPC server response | 压缩前必须限制；推荐默认 `4 MiB`；必要时缩短可选诊断；仍超限则非重试失败，接纳状态可能 unknown | partial-success diagnostics truncation 与 unknown acceptance 必须保留 |
| HTTP server request | 解压后必须限制；推荐默认 `64 MiB`；超限返回 `413` | listener/decompressor 双重限制与 `413` 负例 |
| HTTP client request | 压缩前应限制；推荐默认 `64 MiB`；超限不得发送并应记录 | sender-side limit 与 retained failure record |
| HTTP client response | 解压后必须限制；推荐默认 `4 MiB`；超限为非重试错误 | response bomb 负例与 dropped record |
| HTTP server response | 压缩前必须限制；推荐默认 `4 MiB`；仍超限返回 `500`，接纳状态可能 unknown | 不能把 `500` 自动解释为未接纳或可安全重试 |
| HTTP throttling | `Retry-After` 可以是 HTTP-date 或 delay-seconds | 两种格式、无效/过期时间和 clock skew（时钟偏差）均需负例 |

上述数值是 upstream recommended defaults（上游推荐默认），不是已部署配置。任何未来 deployment profile（部署配置）必须显式冻结自身数值；缺失不得由实现静默猜测。

### 3.3 Excluded development scope

- Profiles 仍为 Development，其 `v1development` schema 有实质变化；
- 新增 Process Context Sharing，同样为 Development，且官方明确它不是 OTLP、不经 gRPC/HTTP/Collector；
- 二者不进入 TMAI v0.1 production-required signals，也不因本次版本采纳自动形成 Capability、Endpoint 或 support commitment（支持承诺）。

## 4. Compatibility Declaration（兼容声明）

```text
SOURCE_VERSION=v1.10.0
TARGET_VERSION=v1.11.0
SCOPE=TMAI_TRACE_METRIC_LOG_OTLP_REFERENCE_AND_TRANSPORT_BEHAVIOR
BACKWARD_COMPATIBILITY=conditional
FORWARD_COMPATIBILITY=conditional
BREAKING_CHANGE=false
MIGRATION_REQUIREMENT=reference-and-control-update-only
RUNTIME_INTEROPERABILITY=NOT_ASSESSED
PROFILES_COMPATIBILITY=OUT_OF_SCOPE_DEVELOPMENT
PROCESS_CONTEXT_COMPATIBILITY=OUT_OF_SCOPE_DEVELOPMENT
```

条件：

1. consumer 对未知 additive fields（增量字段）保持保守兼容；
2. Trace/Metric/Log 的 selected stable scope 不扩展到 Profiles 或 Process Context；
3. 实现记录 exact proto/SDK/Collector versions；
4. 实施前增加 size-limit、decompression、partial-success、unknown acceptance 和 `Retry-After` conformance cases；
5. 实际 Runtime 兼容必须由实施仓库的 direct tests（直接测试）证明，不能由本评估推断。

## 5. TMAI Contract Impact（TMAI 合同影响）

| TMAI surface | candidate change | required evidence before implementation gate pass |
|---|---|---|
| OpenTelemetry profile | reference pin 从 `1.10.0` 更新为 `1.11.0` | human version decision + frozen tag/commit |
| OTel alignment `OTEL-C016` | 从通用资源限制细化为 request/response、pre/post compression limits | config digest + 8 类 size negative tests |
| Telemetry Admission | 超限、响应过大、未知接纳结果必须保留失败记录 | fail-closed records + replay/dedup proof |
| Collector profile | deployment-specific request/response limit 必须显式声明 | exact distribution/image/config + security review |
| Gate evidence manifest | 记录 proto、SDK、Collector 和 limit profile exact versions | immutable digests + reviewer scope |

## 6. Adoption Gate（采用闸门）

只有以下条件全部满足，才能把 candidate reference 写成 adopted/frozen reference：

1. `DQ-022` 记录显式结果和 `decided_by_ref`；
2. [`ADR-025-adopt-otlp-1.11-reference-baseline.md`](architecture/ADR-025-adopt-otlp-1.11-reference-baseline.md) 状态改为 accepted；
3. assessment、profile、alignment matrix、decision packet 和机器投影使用同一 tag/commit；
4. Architecture Contract Freeze 形成 immutable repository reference；
5. 不把 reference adoption 写成 SDK/Collector/runtime adoption。

## 7. Non-claims（非声明）

```text
OTLP_1_11_REFERENCE_CANDIDATE_REVIEWED=true
OTLP_1_11_REFERENCE_ADOPTED=false
OTLP_IMPLEMENTATION_UPGRADED=false
OTLP_ENDPOINT_CREATED=false
COLLECTOR_SELECTED=false
COLLECTOR_DEPLOYED=false
RUNTIME_INTEROPERABILITY_VERIFIED=false
PRODUCTION_GATE_PASS_CREATED=false
PRODUCTION_READY=false
```
