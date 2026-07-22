---
adr_id: ADR-028
title: Establish an Exact Minimal OpenTelemetry Collector Distribution Boundary
title_zh: 建立精确最小 OpenTelemetry Collector 发行版边界
status: accepted-reference-adoption
date: 2026-07-22
decision_id: DQ-025
decision_effect: custom-minimal-inventory-reference-adopted-build-not-authorized
implementation_authorized: false
deployment_authorized: false
production_ready: false
---

# ADR-028: Establish an Exact Minimal OpenTelemetry Collector Distribution Boundary

## Context（背景）

现有 [`otlp-collector-production-profile.md`](otlp-collector-production-profile.md) 定义 transport、
queue/WAL、security、HA 和 operability requirement，但 `B-016` 仍没有 exact distribution、
component inventory 或 source binding。直接采用 `latest`、`otelcol-contrib`、`otelcol-k8s`
或任意预构建镜像会把未审查组件和变动的 tag 引入生产路径；采用 `otelcol-otlp` 又缺少
当前 profile 必需的 resilience/operability primitives。

## Decision（决定）

1. 以 `v0.156.0` 的 exact releases/core/contrib commits 作为版本候选，而不是依赖可移动 tag；
2. 采用 8-component + 2-provider custom minimal inventory 作为首个 architecture reference；
3. 只允许 Trace、Metric、Log；Profiles 和所有 unlisted components/providers 排除；
4. 不增加自定义 Collector component；Telemetry Admission 和 Evidence Admission 仍在 DBOS 边界；
5. 编译 allowlist、运行 config、build artifact 和 deployment 分别绑定，互不自动授权；
6. 用 48-case / 8-group contract 验证 supply chain、allowlist、config、security、durability、
   operability、capacity/HA 和 authority；
7. `DQ-025` 只采纳 architecture reference，build/config/staging/deployment 仍由 `DQ-020` 决定。

## Alternatives（替代方案）

### `otelcol-otlp` prebuilt

拒绝为当前 production profile 默认。攻击面小，但缺 memory limiter、batch、health 和 file
storage，无法满足已定义的资源保护、可运维与重启恢复要求。

### `otelcol-k8s` prebuilt

拒绝为第一画像默认。包含必要组件但同时包含 74 component/provider units，显著增加
receiver、connector、discovery、debug 和 remote-control surface。

### Core `otelcol` prebuilt

拒绝为默认。32 units 超出最小需求，且没有 file storage；不能仅因名称是 core 就推断每个
包含组件适合本 workload。

### Build custom TMAI Collector components

拒绝 v0.1。会复制或侵入 DBOS admission/Evidence authority，并显著增加维护与安全责任。

## Consequences（影响）

- component/source/stability/feature-gate drift 可以被精确审计；
- 第一 production candidate 攻击面从 74-unit Kubernetes distribution 收窄到 8+2；
- TMAI 承担 OCB build、SBOM、signature/provenance、CVE response 和 reproducibility 责任；
- Alpha health 和 Beta transform/file-storage/memory/batch 必须被直接测试，不能因 minimal 而升级；
- 采纳后仍不能构建、配置、运行或部署 Collector；
- 任何新增组件都重新进入 inventory delta、Agent Review 和 Human Decision。

## Evidence（证据）

- [`opentelemetry-collector-distribution-profile.md`](opentelemetry-collector-distribution-profile.md)
- [`opentelemetry-collector-component-inventory.v0.1.json`](opentelemetry-collector-component-inventory.v0.1.json)
- [`schemas/opentelemetry-collector-component-inventory.schema.v0.1.json`](schemas/opentelemetry-collector-component-inventory.schema.v0.1.json)
- [`opentelemetry-collector-distribution-conformance-cases.v0.1.json`](opentelemetry-collector-distribution-conformance-cases.v0.1.json)
- [`schemas/opentelemetry-collector-distribution-conformance-case-catalog.schema.v0.1.json`](schemas/opentelemetry-collector-distribution-conformance-case-catalog.schema.v0.1.json)
- [`schemas/opentelemetry-collector-distribution-conformance-result-set.schema.v0.1.json`](schemas/opentelemetry-collector-distribution-conformance-result-set.schema.v0.1.json)
- [`examples/opentelemetry-collector-distribution-conformance-result-set.not-assessed.example.json`](examples/opentelemetry-collector-distribution-conformance-result-set.not-assessed.example.json)
- [`OTEL-COLLECTOR-DISTRIBUTION-DECISION-PACKET.md`](../OTEL-COLLECTOR-DISTRIBUTION-DECISION-PACKET.md)
- [`OTEL-COLLECTOR-DISTRIBUTION-AGENT-RECOMMENDATION.md`](../OTEL-COLLECTOR-DISTRIBUTION-AGENT-RECOMMENDATION.md)

## Recorded Human Decision（已记录人工决定）

```text
DQ-025=ADOPT_OTEL_COLLECTOR_V0_156_CUSTOM_MINIMAL_INVENTORY
decided_by_ref=zhangbin
decided_at=2026-07-22T12:05:04+08:00
```

## Current State（当前状态）

```text
ADR_028_STATUS=ACCEPTED_REFERENCE_ADOPTION
DQ_025_DECISION_RECORDED=true
AGENT_REVIEW_COMPLETE=true
HUMAN_REVIEW_RECOMMENDED_BY_TWO_MODELS=true
CUSTOM_DISTRIBUTION_ADOPTED=true
COMPONENT_INVENTORY_COUNT=8
CONFIG_PROVIDER_COUNT=2
CONFORMANCE_CASE_COUNT=48
CONFORMANCE_TESTS_EXECUTED=0
VALIDATOR_IMPLEMENTED=false
BUILD_MANIFEST_CREATED=false
COLLECTOR_DEPLOYED=false
IMPLEMENTATION_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
PRODUCTION_READY=false
```
