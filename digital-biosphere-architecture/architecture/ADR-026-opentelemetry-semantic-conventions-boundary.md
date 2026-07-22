---
adr_id: ADR-026
title: Establish an OpenTelemetry Semantic Conventions Boundary for TMAI
title_zh: 建立 TMAI OpenTelemetry 语义约定边界
status: accepted-reference-adoption
date: 2026-07-22
decision_id: DQ-023
decision_effect: core-and-pinned-development-references-adopted-implementation-not-authorized
implementation_authorized: false
deployment_authorized: false
production_ready: false
---

# ADR-026: Establish an OpenTelemetry Semantic Conventions Boundary for TMAI

## Context（背景）

`ADR-023` 接受 OpenTelemetry-aligned observation plane（OpenTelemetry 对齐观察平面），`ADR-025` 提议冻结 OTLP v1.11 wire reference（线协议参考）。但 OTLP 只规定传输和 payload schema，不能回答 `service.instance.id`、`gen_ai.agent.id`、`invoke_agent`、`execute_tool` 或 `gen_ai.evaluation.*` 在 TMAI 中代表什么。

如果直接把这些字段映射到 DBOS/SAEE canonical objects，会产生严重越权：

- telemetry resource ID 被当成 Entity Identity；
- Span 被当成完整 Execution；
- tool metadata 被当成 Capability 或 Permission；
- upstream evaluation score 被当成 SAEE Fitness；
- prompt、response 和 tool content 被默认收集；
- GenAI Development 字段随 `main` 漂移。

## Decision（决定）

1. 以 core Semantic Conventions `v1.43.0@89aae438...` 为 selected stable metadata candidate；
2. 以 GenAI Semantic Conventions `2e994c6d...` 为 pinned Development adapter candidate；
3. 不定义新的 `tmai.*` telemetry attribute namespace；
4. 原始 upstream fields 保持原名、原类型和精确版本来源；
5. DBOS Identity/Execution/Capability references 只可由 telemetry 外部的 trusted admission context 绑定；
6. sensitive GenAI content 默认禁用，只有 Data Governance Gate 可在有界范围 opt in；
7. deprecated fields 新实现拒绝产生，输入侧保留诊断；
8. mapping、schema、conformance、Agent recommendation 和 Human Version Decision 分离；
9. mapping adoption 不授权任何实现、Collector、endpoint、Runtime 或生产使用。

## Alternatives（替代方案）

### Define a TMAI-native telemetry namespace

拒绝作为 v0.1 默认路线。它会复制 OpenTelemetry vocabulary，增加 adapter 成本，并可能把 DBOS 权力语义放进不受信任 telemetry。

### Treat all GenAI fields as stable

拒绝。exact upstream 文档明确为 Development，且 Schema URL 仍为 `TODO`。

### Ignore GenAI semantic conventions

保留为 `OPTION_B`。它降低漂移风险，但会失去当前 Agent framework 生态最直接的互操作入口。

### Map telemetry IDs directly to DBOS IDs

拒绝。相关性不等于身份连续性，且任何 instrumentation 或 Collector 都可能伪造 attribute。

## Consequences（影响）

- TMAI 可以复用 OpenTelemetry 标准字段而不变成 Agent framework；
- Agent、tool、workflow 和 evaluation telemetry 获得清晰但非权威的解释；
- 实现需要额外 trusted binding adapter、version/digest verifier 和 negative conformance；
- 默认不采集内容会限制调试深度，但降低隐私、合规和 Evidence 污染风险；
- GenAI upstream 变化需要更频繁的 delta review；
- 采用本 ADR 仍不能关闭 `PR-G2`、`PR-G3` 或任何 production gate。

## Evidence（证据）

- [`opentelemetry-semantic-conventions-profile.md`](opentelemetry-semantic-conventions-profile.md)
- [`opentelemetry-semantic-mapping.v0.1.json`](opentelemetry-semantic-mapping.v0.1.json)
- [`schemas/opentelemetry-semantic-mapping.schema.v0.1.json`](schemas/opentelemetry-semantic-mapping.schema.v0.1.json)
- [`schemas/opentelemetry-semantic-observation.schema.v0.1.json`](schemas/opentelemetry-semantic-observation.schema.v0.1.json)
- [`examples/opentelemetry-semantic-observation.not-assessed.example.json`](examples/opentelemetry-semantic-observation.not-assessed.example.json)
- [`opentelemetry-semantic-conformance-profile.md`](opentelemetry-semantic-conformance-profile.md)
- [`opentelemetry-semantic-conformance-cases.v0.1.json`](opentelemetry-semantic-conformance-cases.v0.1.json)
- [`schemas/opentelemetry-semantic-conformance-case-catalog.schema.v0.1.json`](schemas/opentelemetry-semantic-conformance-case-catalog.schema.v0.1.json)
- [`schemas/opentelemetry-semantic-conformance-result-set.schema.v0.1.json`](schemas/opentelemetry-semantic-conformance-result-set.schema.v0.1.json)
- [`examples/opentelemetry-semantic-conformance-result-set.not-assessed.example.json`](examples/opentelemetry-semantic-conformance-result-set.not-assessed.example.json)
- [`OTEL-SEMANTIC-CONVENTIONS-ADOPTION-DECISION-PACKET.md`](../OTEL-SEMANTIC-CONVENTIONS-ADOPTION-DECISION-PACKET.md)
- [`OTEL-SEMANTIC-CONVENTIONS-AGENT-RECOMMENDATION.md`](../OTEL-SEMANTIC-CONVENTIONS-AGENT-RECOMMENDATION.md)
- [`OTEL-SEMANTIC-CONFORMANCE-AGENT-RECOMMENDATION.md`](../OTEL-SEMANTIC-CONFORMANCE-AGENT-RECOMMENDATION.md)

## Recorded Human Decision（已记录人工决定）

```text
DQ-023=ADOPT_OTEL_SEMCONV_1_43_CORE_AND_PINNED_GENAI_MAPPING
decided_by_ref=zhangbin
decided_at=2026-07-22T12:05:04+08:00
```

```text
ADR_026_STATUS=ACCEPTED_REFERENCE_ADOPTION
DQ_023_DECISION_RECORDED=true
AGENT_REVIEW_COMPLETE=true
CONTRACT_FREEZE_RECOMMENDED_BY_TWO_AGENTS=true
SEMANTIC_CONFORMANCE_CASE_GROUPS=8
SEMANTIC_CONFORMANCE_CASES=46
SEMANTIC_CONFORMANCE_MAPPING_COVERAGE=47/47
SEMANTIC_CONFORMANCE_RESULT_SET_SCHEMA_DEFINED=true
SEMANTIC_CONFORMANCE_FREEZE_RECOMMENDED_BY_TWO_AGENTS=true
CORE_SEMCONV_REFERENCE_ADOPTED=true
GENAI_MAPPING_REFERENCE_ADOPTED=true
SEMANTIC_MAPPING_IMPLEMENTED=false
SEMANTIC_VALIDATOR_IMPLEMENTED=false
CONFORMANCE_TESTS_EXECUTED=0
IMPLEMENTATION_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
PRODUCTION_READY=false
```
