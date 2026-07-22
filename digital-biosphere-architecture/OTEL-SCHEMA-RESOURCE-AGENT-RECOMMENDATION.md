---
document_id: TMAI-OTEL-SCHEMA-RESOURCE-AGENT-RECOMMENDATION-20260722-001
title: OpenTelemetry Schema, Resource, and Entity Boundary Agent Recommendation
title_zh: OpenTelemetry 模式、资源与实体边界智能体建议
status: review-complete-recommend-human-review-not-a-decision
decision_reference: DQ-024
implementation_authorized: false
deployment_authorized: false
production_ready: false
---

# OpenTelemetry Schema, Resource, and Entity Boundary Agent Recommendation

## Review Scope（审查范围）

本记录保存 `DQ-024` 候选架构的 advisory model review（咨询性模型审查）。它不是
Human Decision（人工决定）、reference adoption（参考采纳）、implementation
authorization（实现授权）、runtime conformance（运行时符合性）或 customer proof（客户证明）。

审查对象：

- [`architecture/opentelemetry-schema-resource-entity-provenance-profile.md`](architecture/opentelemetry-schema-resource-entity-provenance-profile.md)；
- 7 组、45 个预登记 conformance cases；
- case catalog 与 result-set JSON Schema；
- synthetic `DRAFT/NOT_ASSESSED` example；
- [`OTEL-SCHEMA-RESOURCE-ADOPTION-DECISION-PACKET.md`](OTEL-SCHEMA-RESOURCE-ADOPTION-DECISION-PACKET.md)。

Review providers（审查提供方）：

| provider | model | role | authority |
|---|---|---|---|
| Baidu Qianfan | `ernie-4.5-turbo-128k` | independent advisory model reviewer | Recommendation only |
| Volcengine Ark | `deepseek-v4-flash-260425` | independent advisory model reviewer | Recommendation only |

API credentials 未写入本记录或仓库。

## Three-pass Review（三级审查）

### Pass 1 — challenge

两个模型都拒绝 production/runtime recommendation。首轮提出：

- Development Entity/Resource stability 必须继续隔离；
- privacy、retention、tenant isolation、cache、DNS/redirect、result bypass 需要更明确；
- Ark 认为 Scope-level `schema_url` 不存在 precedence。

最后一项经 OpenTelemetry Specification `v1.59.0` exact source 核验为模型误判：当
Resource 与 contained `InstrumentationLibrary*` 两级 `schema_url` 均非空时，contained
value 对其 signal data 取 precedence。规范随后收紧为：只影响 contained signal，不覆盖
两个原始 URL，不合并两个 schema domain，也不产生 trust authority。

### Pass 2 — revised contract

合同从 6 组 36 cases 扩展为 7 组 45 cases，新增：

- DNS rebinding、redirect loop/hop、cache mutation/poisoning；
- sensitive-field minimization、retention policy、tenant isolation；
- quarantine authority-field rejection；
- data-operation audit、safe reference、result-as-decision bypass。

两模型随后均给出：

```text
CANDIDATE_CONTRACT_RECOMMENDATION=RECOMMEND_FOR_HUMAN_REVIEW
ARCHITECTURE_ASSET_CUSTOMER_RECOMMENDATION=RECOMMEND_FOR_BOUNDED_DESIGN_REFERENCE
RUNTIME_CUSTOMER_RECOMMENDATION=DO_NOT_RECOMMEND
PRODUCTION_READY=false
```

Qianfan 仍要求澄清 quarantine exact version binding、低熵 digest protection，以及 OTel
Entity 到 DBOS Registration 的既有治理路径。

### Pass 3 — final delta

最终修订：

- quarantine record 使用 TMAI schema `0.1` 并绑定 exact OTel/SemConv source 与 digest；
- 明确 SHA-256 不是 access control，低熵 payload 不公开裸 digest，使用 tenant-scoped opaque
  reference 或独立 policy 下的 HMAC-SHA-256；
- result Schema 增加强制 `data_governance_binding`；
- 显式引用 Candidate → Admission Decision → Registration Authorization → DBOS Registration
  既有路径，并保持 `REGISTERED != ACTIVE`、Registration 不产生 Capability/Permission。

最终两模型均确认：

```text
REQUIRED_CORRECTIONS_BEFORE_HUMAN_REVIEW=0
FACTUAL_OR_AUTHORITY_ERRORS=0
CANDIDATE_CONTRACT_RECOMMENDATION=RECOMMEND_FOR_HUMAN_REVIEW
ARCHITECTURE_ASSET_CUSTOMER_RECOMMENDATION=RECOMMEND_FOR_BOUNDED_DESIGN_REFERENCE
RUNTIME_CUSTOMER_RECOMMENDATION=DO_NOT_RECOMMEND
PRODUCTION_READY=false
```

## Recommendation（建议）

建议 `DQ-024` 进入 human architecture review（人工架构审查），不建议当前 Runtime、生产
部署或客户运行使用。对潜在客户只能推荐这些资料作为 governed telemetry provenance
（受治理遥测来源）设计参考，必须同时披露：

- `DQ-024` 未决定；
- validator 未实现；
- 45 个 runtime conformance cases 执行为 0；
- DBOS/SAEE 未因本审查发生实现变更；
- 没有 production、interoperability 或 customer proof。

## Future Implementation Obligations（未来实现义务）

只有后续独立决定明确授权后，才可：

1. 实现 schema acquisition/cache/transform、Resource provenance 与 Entity quarantine validator；
2. 执行 45/45 case-level runtime conformance；
3. 绑定 exact source、implementation、environment、policy 和 reviewer digests；
4. 由独立 evaluator 复核 result；
5. 由人类治理决定 gate，result 不能自闭环。

## Current Truth（当前事实）

```text
AGENT_REVIEW_COMPLETE=true
HUMAN_REVIEW_RECOMMENDED_BY_TWO_MODELS=true
BOUNDED_DESIGN_REFERENCE_RECOMMENDED_BY_TWO_MODELS=true
RUNTIME_RECOMMENDED_BY_MODELS=false
REQUIRED_DOCUMENT_CORRECTIONS_OPEN=0
DQ_024_DECIDED=false
REFERENCE_ADOPTED=false
VALIDATOR_IMPLEMENTED=false
RUNTIME_CASES_EXECUTED=0
IMPLEMENTATION_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
PRODUCTION_READY=false
```
