---
document_id: TMAI-OTEL-COLLECTOR-OPERATIONAL-EVIDENCE-CONTRACT-0.1
title: TMAI OpenTelemetry Collector Operational Evidence Contract v0.1
title_zh: TMAI OpenTelemetry Collector 运维证据契约 v0.1
status: proposed-dq-020-input-not-measured-no-runtime-effect
primary_repository: digital-biosphere-architecture
decision_reference: DQ-020
measurement_started: false
operational_evidence_created: false
production_ready: false
---

# TMAI OpenTelemetry Collector Operational Evidence Contract v0.1

中文：TMAI OpenTelemetry Collector（开放遥测采集器）运维证据契约 v0.1。

## 1. Purpose（目的）

本契约定义未来 `TMAI-SELF-HOSTED-SINGLE-TENANT-1` staging deployment（预生产部署）必须如何
把 Collector internal telemetry（内部遥测）、外部 blackbox probe（黑盒探针）、配置／Runtime 摘要、
WAL／磁盘状态和 end-to-end reconciliation（端到端对账）组合成 `PR-G3` 的运维证据输入。

它不创建 Collector configuration、Prometheus rule、dashboard、alert、runbook、endpoint、measurement
或 Evidence Object。机器真值见
[`opentelemetry-collector-operational-evidence-profile.v0.1.json`](opentelemetry-collector-operational-evidence-profile.v0.1.json)，
结构约束见
[`schemas/opentelemetry-collector-operational-evidence-profile.schema.v0.1.json`](schemas/opentelemetry-collector-operational-evidence-profile.schema.v0.1.json)。

```text
Internal telemetry != Composite readiness
Health OK != Export path healthy
No data != Zero failures
Collector sent != End-to-end delivered
Operational evidence != DBOS Evidence != Truth
```

## 2. Official OpenTelemetry Inputs（OpenTelemetry 官方输入）

| official source | retained production implication |
|---|---|
| [Internal telemetry](https://opentelemetry.io/docs/collector/internal-telemetry/) | 默认 metrics 与 logs 可观察进程、receiver、processor、exporter 和 queue；internal telemetry declarative schema 仍在发展，internal traces 仍实验性；Prometheus 与 OTLP 名称可能因 suffix/unit/view 而不同 |
| [Scaling](https://opentelemetry.io/docs/collector/scaling/) | queue utilization、refusal 和 send failure 是扩缩容输入，但 backend/network saturation 时增加 Collector 可能放大故障；阈值必须由 exact workload 校准 |
| [Resiliency](https://opentelemetry.io/docs/collector/resiliency/) | queue、retry、WAL 和 message queue 都存在独立丢失条件；WAL 不能证明 exactly-once 或 DBOS canonical durability |
| [Hosting security](https://opentelemetry.io/docs/security/hosting-best-practices/) | 自监控、最小权限、受限 server-like component、资源告警和存储目录保护是部署责任 |
| [Configuration security](https://opentelemetry.io/docs/security/config-best-practices/) | memory limit、batch、queue、timeout/retry、过滤和资源限制必须组合设计，不能只看单一 CPU 或 queue 指标 |

这些来源是 architecture input（架构输入），不是 OpenTelemetry certification（认证），也不证明
TMAI 已配置、采集、告警或达到 SLO。

## 3. Evidence Source Separation（证据来源分离）

| source class | 能证明 | 不能单独证明 |
|---|---|---|
| Collector internal metrics | 进程、receiver、processor、exporter、queue 的局部观测 | listener 安全范围、WAL 可写、完整 delivery、DBOS Evidence |
| Collector internal logs | start/stop/crash、throttling/invalid-data drop 等事件 | 日志未采样、所有事件完整、Truth |
| Runtime controller | replica、restart、image、failure domain 和 lifecycle | Collector pipeline 内部数据结果 |
| External blackbox probe | 指定来源和凭据下 listener 可达或被拒绝 | 所有来源可达、真实流量授权、后端交付 |
| Storage monitor | WAL volume、quota、write probe 和磁盘状态 | queue item 语义、canonical RPO |
| Immutable reconciler | desired/running config 和 component drift | 数据正确、SLO 达成 |
| Destination receipt | 一跳 destination 的接收结果 | DBOS Evidence admission、端到端 exactly-once |
| DBOS admission ledger | 是否形成规范准入结果 | 科学 Truth 或 SAEE Authority |

任何单一来源缺失、过期或冲突时，不允许用另一个来源静默补零。

## 4. Naming and Stability Boundary（命名与稳定性边界）

未来 implementation 必须以 exact Collector release source 验证每个 instrument（测量工具）的名称、
类型、单位、attributes、verbosity level 和 stability。查询使用 OTLP instrument name 作为规范语义，
同时记录 Prometheus `_total`、unit suffix、dots/underscores 和 metric views 的投影规则。

- `service.instance.id` 是 Collector Resource correlation（资源关联），不是 DBOS `entity_id`；
- third-party `http.*` / `rpc.*` metrics 不继承 Collector first-party stability；
- internal log entry 和格式无稳定保证，关键事件必须与 Runtime controller 或独立记录对账；
- counter reset 必须按 instance lifecycle 分窗，不能产生负 rate 或被当成零失败；
- mixed Collector versions 不允许聚合成一个无版本序列；
- missing/renamed metric 必须是 `UNKNOWN` 并阻止 readiness，不得 zero-fill。

## 5. Required Operational Observation Classes（必需运维观察类）

机器 profile 预注册 12 类 observation：

1. process lifecycle/resource；
2. receiver accepted/refused；
3. processor flow/transform lineage；
4. exporter enqueue outcome；
5. exporter send outcome；
6. queue saturation；
7. WAL/disk/replay；
8. authenticated listener blackbox；
9. config/component drift；
10. self-telemetry freshness/independence；
11. lifecycle/drop/crash events；
12. end-to-end delivery reconciliation。

前六类可以部分利用 OpenTelemetry first-party internal metrics；后六类必须结合外部来源。若 exact
component 不发出候选 helper metric，必须登记 unsupported（不支持）并补充经审查的替代来源，不能
伪造同名指标。

## 6. SLI and Readiness Semantics（SLI 与就绪语义）

profile 定义 refusal、enqueue failure、send failure、queue utilization、self-telemetry freshness 和
delivery-accounting closure 六类 formula semantics（公式语义），但所有阈值、窗口和 query 仍为 `null`。

这些 `null` 是 `INTENTIONALLY_UNRESOLVED_FAIL_CLOSED`（有意未解析且失败关闭），不是缺失文档：
DBA 在没有部署仓库、运行配置、query/rule、route/runbook 和直接测量结果时不能制造摘要。它们不阻止
bounded human architecture review（有限人工架构审查），但必须阻止 implementation authorization
（实现授权）、measurement（测量）、deployment（部署）和 production gate closure（生产闸门关闭）。
精确值只能由未来 Collector platform owner 在 `DQ-020` 人类决定后按受控顺序提供并接受独立审查。

Composite readiness（复合就绪性）继续要求八项同时为 true 且 fresh：

1. process running；
2. approved config digest match；
3. authenticated listener accepting within scope；
4. queue utilization below exact critical threshold；
5. WAL writable within quota；
6. required exporter reachable within outage budget；
7. self-telemetry fresh；
8. no blocking config/security drift。

任一 `UNKNOWN`、stale 或 critical 均为 `NOT_READY`。Human override、health `200 OK` 或 dashboard
green 不能覆盖失败谓词。

## 7. Alert and Runbook Binding（告警与运行手册绑定）

未来告警包必须绑定 exact query/rule digest、warning/critical thresholds、evaluation window、no-data
rule、clock-skew bound、alert route 和 per-critical-alert runbook。SLO 告警要求 multi-window burn-rate
（多窗口错误预算消耗率），但 exact window 和倍数必须由部署工作负载决定。

自动 remediation（修复）只能执行预授权、可回滚且不扩大 Authority 的动作。告警本身不授权扩容、
修改 Capability、改变 DBOS 状态或执行 SAEE Recommendation。

`exact_alert_rule_digest`、`exact_runbook_bundle_digest` 和 `exact_alert_route_reference` 当前为 `null`，
含义是这些实现对象尚不存在；将任意占位字符串写成摘要会制造虚假绑定。它们必须保持阻断状态，直到
对应 bundle（包）、route（路由）和 runbook（运行手册）真实存在并可重复计算摘要。

## 8. Existing Test Reuse（既有测试复用）

本契约不创建新的 conformance catalog。它复用 Collector distribution 的 5 个 operability、4 个
capacity/HA 和 6 个 durability cases，以及既有 OTLP delivery cases。所有 case 当前仍为
`NOT_EXECUTED`；本 profile 的 Schema validation 不能改变它们的结果。

未来真实结果继续进入
[`production-gate-evidence-manifest-specification.md`](production-gate-evidence-manifest-specification.md)，
不得创建旁路“dashboard pass”台账。

## 9. Stop Conditions（停止条件）

出现以下任一情况，`PR-G3` 保持关闭：

- internal telemetry endpoint 或 log destination 未限制来源；
- metric name/stability/config version 未绑定；
- missing series 被当作 0；
- counter reset、mixed version 或 stale series 未处理；
- health OK 覆盖 queue/WAL/exporter/drift 失败；
- self-telemetry 与主 exporter 共享同一不可观察失败路径；
- alert 没有可验证 route/runbook，或 no-data 不告警；
- dashboard screenshot/self-reported summary 被用作唯一 gate evidence；
- Collector receipt 被提升为 DBOS Evidence、Verification、Permission 或 Truth。

## 10. Current State（当前状态）

```text
OPERATIONAL_EVIDENCE_PROFILE_DEFINED=true
OPERATIONAL_EVIDENCE_PROFILE_ADOPTED=false
INTERNAL_TELEMETRY_CONFIGURED=false
METRIC_ENDPOINT_CREATED=false
QUERY_BUNDLE_CREATED=false
ALERT_RULES_CREATED=false
RUNBOOKS_CREATED=false
MEASUREMENT_STARTED=false
OPERATIONAL_EVIDENCE_CREATED=false
DQ_020_STATUS=BLOCKED_INPUT
PRODUCTION_READY=false
```
