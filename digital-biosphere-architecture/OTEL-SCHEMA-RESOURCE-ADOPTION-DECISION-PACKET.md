---
document_id: TMAI-OTEL-SCHEMA-RESOURCE-ADOPTION-PACKET-20260722-001
title: OpenTelemetry Schema, Resource, and Entity Boundary Adoption Decision Packet
title_zh: OpenTelemetry 模式、资源与实体边界采纳决策包
status: ready-for-human-review-not-decided
decision_id: DQ-024
implementation_authorized: false
deployment_authorized: false
production_ready: false
---

# OpenTelemetry Schema, Resource, and Entity Boundary Adoption Decision Packet

## Decision Question（决策问题）

是否把 OpenTelemetry Specification `v1.59.0` 的 Stable Telemetry Schema 与 Stable
Resource SDK 规则、core schema `1.43.0` exact artifact，以及 Development OTel Entity
quarantine（开发中实体隔离）采纳为 TMAI v0.1 的 Schema/Resource provenance boundary
（模式／资源来源边界）？

本决定独立于：

- `DQ-022` OTLP wire reference；
- `DQ-023` Semantic Conventions mapping；
- `DQ-018` DBOS offline implementation slice；
- `DQ-020` Collector/deployment staging。

## Source Facts（来源事实）

- Telemetry Schemas 在 exact OTel Specification `v1.59.0` 为 Stable；
- Resource SDK 为 Stable except where otherwise specified；
- Resource Data Model、Entity Data Model、Entity Propagation 在 exact `v1.59.0` 为 Development；
- Resource merge 遇到两个不同 non-empty Schema URL 时是 merge error，结果 undefined/
  implementation-specific；TMAI 不能使用该结果；
- `OTEL_RESOURCE_ATTRIBUTES` 来自环境，user-provided Resource 有更高 merge precedence，
  但该优先级不是 DBOS trust authority；
- `OTEL_ENTITIES` 是 Development environment propagation input，不是 DBOS Registration；
- core schema URL `https://opentelemetry.io/schemas/1.43.0` 在 2026-07-22 返回
  `application/yaml`，file format `1.1.0`，观察 digest 为
  `sha256:6ac5dd367ff707dbcdcb1e5b459d4ac2fd676fb44eb17a21f9494a9fee4233df`。

## Recommended Option（推荐选项）

`OPTION_A`: adopt Stable Schema/Resource subset and quarantine Development Entity inputs
（采纳稳定模式／资源子集并隔离开发中实体输入）。

理由：

- 保留 OpenTelemetry 的 schema evolution 和 Resource provenance 能力；
- 阻止同名 `Entity` 绕过 DBOS Identity/Lifecycle/Registration；
- 支持未来 Agent framework 和 Collector 的多版本输入；
- exact source/digest/lineage 可以审计转换；
- runtime network fetch 默认关闭，降低 SSRF、漂移和供应链风险。

## Options（选项）

| option | result | trade-off |
|---|---|---|
| `OPTION_A` | Stable Schema/Resource candidate + Development Entity quarantine | 兼容 OTel 演化；实现需要严格 source、transform、detector 和 quarantine validator |
| `OPTION_B` | Stable Schema/Resource candidate + reject all OTel Entity inputs | 最保守；暂时失去 OTel Entity observation 互操作材料 |
| `OPTION_C` | return for revision | 必须指出 exact source、fetch、transform、Resource 或 Entity 边界缺口 |

## Exact Human Decision Tokens（精确人工决定令牌）

```text
DQ-024=ADOPT_OTEL_SCHEMA_RESOURCE_1_59_AND_QUARANTINE_DEVELOPMENT_ENTITY
decided_by_ref=<human-reference>
```

```text
DQ-024=ADOPT_OTEL_SCHEMA_RESOURCE_1_59_AND_REJECT_ALL_ENTITY_INPUTS
decided_by_ref=<human-reference>
entity_rejection_reason=<required>
```

```text
DQ-024=RETURN_OTEL_SCHEMA_RESOURCE_ENTITY_BOUNDARY_FOR_REVISION
decided_by_ref=<human-reference>
revision_reason=<required>
```

## Accepted Scope If Option A Is Chosen（选择 A 时的接受范围）

- exact source registry 和 stability lanes；
- build/release-time allowlisted schema acquisition；
- runtime network schema fetch disabled by default；
- original Resource/Scope schema URLs、effective precedence 和 transformation lineage；
- Resource detector name/version/artifact/config/order/source provenance；
- different non-empty Resource Schema URL conflict fail closed；
- `OTEL_RESOURCE_ATTRIBUTES` environment origin 和整项 parse failure；
- OTel Entity/`OTEL_ENTITIES` quarantine；
- 7 组、45 个 conformance cases 与 strict result-set contract；其中新增 DNS/cache、
  privacy/retention、tenant isolation 和 result-as-decision bypass 失败关闭用例；
- 所有 canonical/authority/production effects 恒 false。

## Explicitly Rejected Scope（明确拒绝范围）

- 动态按任意输入 URL 在 Runtime 获取 schema；
- 把 redirect、remote content 或 cache hit 当成信任；
- 猜测 breaking/unsupported schema conversion；
- 用 implementation-specific Resource merge conflict output；
- 把 merge precedence 当作 trust authority；
- 把 OTel Entity type/ID、`OTEL_ENTITIES` 或 repeatable identity 当成 DBOS Entity；
- 创建 Schema fetcher、translator、Resource Detector、Agent、Runtime、Identity、Evidence 或 Permission；
- 修改 DBOS/SAEE；
- 宣称 implementation、interoperability、deployment 或 production readiness。

## Required Follow-ups（后续要求）

如果被采纳：

1. 冻结 immutable DBA commit/tree、profile/catalog/schemas 和全部 source/artifact digest；
2. `DQ-023`、`DQ-022` 仍需独立决定；
3. `DQ-018` 另行授权后才能实现 offline schema/resource validator；
4. `DQ-020` 另行授权后才能验证 authenticated Collector transformation/deployment；
5. 全部 45 cases 必须产生直接 case-level result，失败和 unknown 不可删除；
6. validator 必须独立核对 source、catalog、case-set、summary、implementation 和 environment；
7. Production Gate Evidence Manifest 必须独立绑定本 catalog/result，不能与 OTLP 或 semantic
   catalog 合并为自报汇总；
8. 任何 upstream change 重新进入 delta + Agent Review + Human Version Decision。

## Current Truth（当前事实）

```text
DQ_024_DECISION_RECORDED=false
AGENT_REVIEW_COMPLETE=true
HUMAN_REVIEW_RECOMMENDED_BY_TWO_MODELS=true
BOUNDED_DESIGN_REFERENCE_RECOMMENDED_BY_TWO_MODELS=true
RUNTIME_RECOMMENDED_BY_MODELS=false
CONTRACT_FREEZE_RECOMMENDED_BY_TWO_AGENTS=false
OTEL_SCHEMA_RESOURCE_REFERENCE_ADOPTED=false
OTEL_ENTITY_QUARANTINE_POLICY_ADOPTED=false
CONFORMANCE_CASE_GROUPS=7
CONFORMANCE_CASES=45
CONFORMANCE_TESTS_EXECUTED=0
VALIDATOR_IMPLEMENTED=false
IMPLEMENTATION_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
PRODUCTION_READY=false
```

审查记录：[`OTEL-SCHEMA-RESOURCE-AGENT-RECOMMENDATION.md`](OTEL-SCHEMA-RESOURCE-AGENT-RECOMMENDATION.md)。
