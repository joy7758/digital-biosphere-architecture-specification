---
adr_id: ADR-025
title: Adopt OTLP v1.11.0 as the TMAI Reference Baseline
title_zh: 采纳 OTLP v1.11.0 为 TMAI 参考基线
status: accepted-reference-adoption
date: 2026-07-22
decision_id: DQ-022
decision_effect: exact-reference-adopted-implementation-not-authorized
implementation_authorized: false
deployment_authorized: false
production_ready: false
---

# ADR-025: Adopt OTLP v1.11.0 as the TMAI Reference Baseline

## Context（背景）

`ADR-023` 采纳了 OpenTelemetry-aligned observation plane（OpenTelemetry 对齐观察平面），但 Version Governance（版本治理）要求外部参考变化有 exact source、delta、compatibility、decision 和 freeze，不能跟随 `latest` 自动升级。

OpenTelemetry 在 2026-07-21 发布 `opentelemetry-proto v1.11.0`。相对 `v1.10.0`，当前 TMAI 选定的 Trace/Metric/Log stable wire scope 没有发现破坏，但 OTLP transport specification 新增了请求/响应尺寸、压缩前/解压后限制和相关失败语义，并澄清 `Retry-After` 可以使用 HTTP-date。

## Decision（决定）

1. 把 `v1.11.0` / `790608c4d51e6ffc12210b541e8514cbed9e91a4` 采纳为 TMAI v0.1 production-path 的 exact OTLP reference；
2. 在 selected scope 中继续只要求 Trace、Metric、Log；
3. 把 Profiles 和 Process Context Sharing 保持为 excluded Development scope；
4. 把 request/response size limits、decompression protection、non-retryable failure、unknown acceptance 和 `Retry-After` parsing 纳入后续 conformance；
5. 采纳时同时冻结 [`otlp-v1.11-conformance-profile.md`](otlp-v1.11-conformance-profile.md) 和 56-case machine catalog 的 exact digest，但不改变全部 case 的 `NOT_EXECUTED`；
6. 要求所有未来上游 reference 变化重复同样的 version delta process。

## Compatibility（兼容性）

```text
BACKWARD_COMPATIBILITY=conditional
FORWARD_COMPATIBILITY=conditional
BREAKING_CHANGE_IN_SELECTED_SCOPE=false
RUNTIME_INTEROPERABILITY=NOT_ASSESSED
MIGRATION_REQUIREMENT=reference-and-control-update-only
```

## Alternatives（替代方案）

### Hold v1.10.0

可保持更早的冻结参考，但会缺失 v1.11.0 明确的 production size-limit behavior。本选项不是错误，但必须记录 hold reason 和再审条件。

### Follow latest automatically

拒绝：无法审计 wire/behavior delta，也会绕过 Version Decision 和 implementation conformance。

### Adopt all v1.11.0 packages

拒绝：Profiles 和 Process Context 为 Development，而且 Process Context 不是 OTLP/Collector transport；全量采用会扩大未授权范围。

## Consequences（影响）

- Architecture reference 可精确追溯；
- `OTEL-C016` 将有更强的 size/decompression 负例要求；
- 实现方必须分别记录 proto、SDK、Collector 和 config 版本；
- reference adoption 不产生 SDK/Collector/runtime adoption；
- 在实施测试前，Runtime compatibility 保持 `NOT_ASSESSED`。

## Evidence（证据）

- [`OTLP-1.11-VERSION-DELTA-ASSESSMENT.md`](../OTLP-1.11-VERSION-DELTA-ASSESSMENT.md)
- [`OTLP-1.11-VERSION-ADOPTION-DECISION-PACKET.md`](../OTLP-1.11-VERSION-ADOPTION-DECISION-PACKET.md)
- [`OTLP-1.11-VERSION-ADOPTION-DECISION-PACKET.json`](../OTLP-1.11-VERSION-ADOPTION-DECISION-PACKET.json)
- [`otlp-v1.11-conformance-profile.md`](otlp-v1.11-conformance-profile.md)
- [`otlp-v1.11-conformance-cases.v0.1.json`](otlp-v1.11-conformance-cases.v0.1.json)
- [`schemas/otlp-conformance-result-set.schema.v0.1.json`](schemas/otlp-conformance-result-set.schema.v0.1.json)
- [`examples/otlp-conformance-result-set.not-assessed.example.json`](examples/otlp-conformance-result-set.not-assessed.example.json)
- [`OTLP-1.11-CONFORMANCE-PROFILE-AGENT-RECOMMENDATION.md`](../OTLP-1.11-CONFORMANCE-PROFILE-AGENT-RECOMMENDATION.md)

## Recorded Human Decision（已记录人工决定）

```text
DQ-022=ADOPT_OTLP_1_11_0_REFERENCE_BASELINE
decided_by_ref=zhangbin
decided_at=2026-07-22T12:05:04+08:00
```

```text
ADR_025_STATUS=ACCEPTED_REFERENCE_ADOPTION
DQ_022_DECISION_RECORDED=true
OTLP_1_11_REFERENCE_ADOPTED=true
IMPLEMENTATION_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
PRODUCTION_READY=false
```
