---
adr_id: ADR-027
title: Establish an OpenTelemetry Schema, Resource, and Entity Provenance Boundary
title_zh: 建立 OpenTelemetry 模式、资源与实体来源边界
status: accepted-reference-adoption
date: 2026-07-22
decision_id: DQ-024
decision_effect: schema-resource-reference-and-development-entity-quarantine-adopted
implementation_authorized: false
deployment_authorized: false
production_ready: false
---

# ADR-027: Establish an OpenTelemetry Schema, Resource, and Entity Provenance Boundary

## Context（背景）

`ADR-023`–`ADR-026` 已定义 OTel observation、OTLP wire 和 semantic mapping，但没有完整
约束 schema transformation、Resource detector merge provenance 或 Development OTel Entity。
这留下三条旁路：转换后丢失原始来源、环境 Resource 属性伪装成 DBOS Identity、同名 OTel
Entity 绕过 Digital Entity Registration。

## Decision（决定）

1. 采用 exact `v1.59.0` Stable Telemetry Schema / Resource SDK rules 作为候选；
2. 采用 core schema `1.43.0` exact URL + observed digest 作为候选 artifact；
3. Runtime schema fetch 默认关闭；只接受预冻结 allowlist 和 digest；
4. 所有转换保存 original/effective source、operation、artifact/environment 和 input/output lineage；
5. Resource merge precedence 不产生 trust authority；conflicting non-empty URLs fail closed；
6. Resource Data Model、Entity Data Model 和 Entity Propagation Development 内容保持隔离；
7. OpenTelemetry Entity 永不自动成为 TMAI Digital Entity；
8. `DQ-024`、`DQ-023`、`DQ-022`、`DQ-018` 和 `DQ-020` 保持独立。

## Alternatives（替代方案）

### Ignore schema and Resource provenance

拒绝。多版本 SDK/Collector 输入会产生不可审计字段漂移，长期运行无法重放解释。

### Treat OTel Entity as DBOS Entity

拒绝。上游模型为 Development，且 OTel observation identity 不含 DBOS Registration、
Lifecycle、Capability、Authorization 或 Identity Continuity proof。

### Reject all OTel Entity inputs

保留为 `OPTION_B`。风险最低，但失去有界 observation interoperability。

### Fetch schemas dynamically at runtime

拒绝作为 v0.1 默认。它引入 SSRF、redirect、drift、availability 和 supply-chain 风险。

## Consequences（影响）

- schema evolution 可以有来源地进入长期运行基础设施；
- Resource/Entity observation 与 DBOS identity authority 明确分离；
- 实现需要 schema artifact store、transform lineage 和 detector provenance；
- 45-case contract 增加实现成本，但阻止不可复现的 silent transform，并显式覆盖
  schema cache/DNS 供应链、数据最小化、retention、tenant isolation 与 result bypass；
- 采纳本 ADR 仍不授权实现、Collector、Runtime 或生产部署。

## Evidence（证据）

- [`opentelemetry-schema-resource-entity-provenance-profile.md`](opentelemetry-schema-resource-entity-provenance-profile.md)
- [`opentelemetry-schema-resource-conformance-cases.v0.1.json`](opentelemetry-schema-resource-conformance-cases.v0.1.json)
- [`schemas/opentelemetry-schema-resource-conformance-case-catalog.schema.v0.1.json`](schemas/opentelemetry-schema-resource-conformance-case-catalog.schema.v0.1.json)
- [`schemas/opentelemetry-schema-resource-conformance-result-set.schema.v0.1.json`](schemas/opentelemetry-schema-resource-conformance-result-set.schema.v0.1.json)
- [`examples/opentelemetry-schema-resource-conformance-result-set.not-assessed.example.json`](examples/opentelemetry-schema-resource-conformance-result-set.not-assessed.example.json)
- [`OTEL-SCHEMA-RESOURCE-ADOPTION-DECISION-PACKET.md`](../OTEL-SCHEMA-RESOURCE-ADOPTION-DECISION-PACKET.md)
- [`OTEL-SCHEMA-RESOURCE-AGENT-RECOMMENDATION.md`](../OTEL-SCHEMA-RESOURCE-AGENT-RECOMMENDATION.md)

## Recorded Human Decision（已记录人工决定）

```text
DQ-024=ADOPT_OTEL_SCHEMA_RESOURCE_1_59_AND_QUARANTINE_DEVELOPMENT_ENTITY
decided_by_ref=zhangbin
decided_at=2026-07-22T12:05:04+08:00
```

## Current State（当前状态）

```text
ADR_027_STATUS=ACCEPTED_REFERENCE_ADOPTION
DQ_024_DECISION_RECORDED=true
AGENT_REVIEW_COMPLETE=true
HUMAN_REVIEW_RECOMMENDED_BY_TWO_MODELS=true
OTEL_SCHEMA_RESOURCE_REFERENCE_ADOPTED=true
OTEL_ENTITY_POLICY_ADOPTED=true
CONFORMANCE_TESTS_EXECUTED=0
VALIDATOR_IMPLEMENTED=false
IMPLEMENTATION_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
PRODUCTION_READY=false
```
