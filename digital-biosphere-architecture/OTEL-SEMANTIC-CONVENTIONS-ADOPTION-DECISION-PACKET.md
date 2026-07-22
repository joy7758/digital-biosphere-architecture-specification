---
document_id: TMAI-OTEL-SEMANTIC-CONVENTIONS-ADOPTION-PACKET-20260722-001
title: OpenTelemetry Semantic Conventions Mapping Adoption Decision Packet
title_zh: OpenTelemetry 语义约定映射采纳决策包
status: ready-for-human-decision-agent-review-complete-not-authorized
decision_id: DQ-023
implementation_authorized: false
deployment_authorized: false
production_ready: false
---

# OpenTelemetry Semantic Conventions Mapping Adoption Decision Packet

中文：OpenTelemetry 语义约定映射采纳决策包。

## Decision Question（决策问题）

是否把：

1. core Semantic Conventions `v1.43.0@89aae438b3b3b0a8dd33003c9d70592baf7dbd0d` 的 selected stable metadata fields（选定稳定元数据字段）；以及
2. GenAI Semantic Conventions `2e994c6d59a93bb4fc1752c5378eedb9b8e14d6b` 的 pinned Development fields（版本钉住开发态字段）

采纳为 TMAI v0.1 的 architecture mapping reference（架构映射参考），同时冻结“GenAI 字段只构成观察提示，不产生 DBOS/SAEE 权力效果”的边界？

## Source Facts（来源事实）

- `v1.43.0` 是当前 core Semantic Conventions 的 exact release/tag，tag commit 为 `89aae438...`；
- service、service instance、service namespace 和部分 instrumentation 字段分别有明确 Stable 状态；
- `deployment.environment.name` 在 exact `v1.43.0` deployment registry 中为 Stable，不以 service 文档代替其字段来源；
- Instrumentation Scope 在 OTel Specification `v1.59.0` 中为 Stable tuple；OTLP `v1.11.0` 的 `ScopeSpans/ScopeMetrics/ScopeLogs.schema_url` 是该作用域 Schema URL 的信号承载位置；
- Resource 文档整体为 Mixed，因此必须逐字段保存 stability；
- GenAI 语义已移动到独立仓库，exact commit 为 `2e994c6d...`；
- exact GenAI README 的 Schema URL 为 `TODO`，仓库没有可供本画像采用的 release tag；
- GenAI agent、workflow、tool、evaluation 和 content 字段为 Development；
- `gen_ai.agent.id` 描述 upstream hosted-agent resource，不是 DBOS Identity；
- input/output messages、system instructions、tool arguments/results 和 retrieval content 可能包含敏感数据。

## Recommended Option（推荐选项）

`OPTION_A`: adopt split-stability reference（采纳分层稳定性参考）。

理由：

- 最大化复用 OpenTelemetry 生态的通用名称，避免自建第二套可观测性词汇；
- core Stable fields 可以提供供应商中立的资源与插桩描述；
- GenAI Development fields 对 Agent framework adapter（智能体框架适配器）有现实互操作价值；
- exact commit、隔离映射、默认禁用内容和无权力效果可以控制上游漂移；
- 不定义 `tmai.*` telemetry namespace，避免把不受信任遥测伪装成 DBOS 事实。

## Options（选项）

| option | result | trade-off |
|---|---|---|
| `OPTION_A` | core `v1.43.0` selected stable mapping + exact GenAI commit isolated Development mapping | 互操作最完整；实现前仍需独立 validator 和 conformance |
| `OPTION_B` | 只采纳 core Stable mapping，暂不采用 GenAI mapping | 漂移风险最低；Agent framework 语义仍碎片化 |
| `OPTION_C` | 退回修订 | 必须指出字段、稳定性、隐私或权力边界的具体缺口 |

## Exact Human Decision Tokens（精确人工决定令牌）

选择分层映射：

```text
DQ-023=ADOPT_OTEL_SEMCONV_1_43_CORE_AND_PINNED_GENAI_MAPPING
decided_by_ref=<human-reference>
```

只选择 core：

```text
DQ-023=ADOPT_OTEL_SEMCONV_1_43_CORE_ONLY
decided_by_ref=<human-reference>
genai_hold_reason=<required>
```

退回修订：

```text
DQ-023=RETURN_OTEL_SEMANTIC_MAPPING_FOR_REVISION
decided_by_ref=<human-reference>
revision_reason=<required>
```

## Accepted Scope If Option A Is Chosen（选择 A 时的接受范围）

- [`architecture/opentelemetry-semantic-conventions-profile.md`](architecture/opentelemetry-semantic-conventions-profile.md) 的 stability lanes（稳定性通道）和 authority boundary（权力边界）；
- [`architecture/opentelemetry-semantic-mapping.v0.1.json`](architecture/opentelemetry-semantic-mapping.v0.1.json) 的 47 项字段处理目录；
- 9 项 exact source registry 对 47 项字段的一次且仅一次来源覆盖；
- [mapping schema](architecture/schemas/opentelemetry-semantic-mapping.schema.v0.1.json) 和 [observation schema](architecture/schemas/opentelemetry-semantic-observation.schema.v0.1.json)；
- [semantic conformance profile](architecture/opentelemetry-semantic-conformance-profile.md)、[46-case catalog](architecture/opentelemetry-semantic-conformance-cases.v0.1.json)、目录 Schema、result-set Schema 和 synthetic `NOT_ASSESSED` 示例；
- 8 个 case groups 对 47/47 mapping IDs 的预登记覆盖，以及 result `PASS` 所需的 exact digest、46/46 case、independent review 和 Decision 绑定；
- raw upstream field preservation（原始上游字段保留）；
- trusted DBOS binding outside telemetry（在遥测之外进行可信 DBOS 绑定）；
- GenAI content capture 默认 disabled；
- deprecated fields reject-and-retain-diagnostic；
- future upstream change 必须走 delta、conformance、Agent recommendation 和 Human Version Decision。

## Explicitly Rejected Scope（明确拒绝范围）

- 自动采用 SDK、instrumentation、Collector 或 GenAI framework；
- 定义新的 `tmai.*` OpenTelemetry attribute namespace；
- 把 `service.instance.id` 或 `gen_ai.agent.id` 写成 DBOS `entity_id`；
- 把 trace/span/conversation ID 写成 `execution_id`；
- 把 `invoke_agent`、`execute_tool` 或 tool metadata 写成 Capability、Permission 或执行授权；
- 把 `gen_ai.evaluation.*` 写成 SAEE Evaluation、Fitness 或 Governance Decision；
- 默认采集 prompt、response、reasoning、tool arguments/results 或 retrieval content；
- 创建 Agent、Entity、Runtime、Telemetry、Evidence、Verification 或 Permission；
- 修改 DBOS/SAEE；
- 宣称 interoperability、implementation、deployment 或 production readiness 已通过。

## Required Follow-ups（后续要求）

如果 `OPTION_A` 被采纳：

1. 更新 `ADR-026`、Decision Queue 和 version registry；
2. 以 immutable DBA commit/tree 和 SHA-256 冻结 profile、catalog 与 schemas；
3. 将 8 组、46 个预登记 conformance cases 及 result-set contract 与同一 immutable baseline 一并冻结；
4. 在 `DQ-018` 另行授权后，DBOS 只实现 mapping validator、semantic validator 和 trusted binding adapter；
5. 真实执行必须保存 46/46 case-level results、47/47 coverage、失败、限制和 artifact/environment digests；
6. 在 `DQ-020` 另行授权后，才允许 Collector staging；
7. Data Governance Gate 未通过前保持 sensitive content disabled；
8. 所有 production gate 保持未通过，直到有真实 implementation/environment/digest-bound evidence。

## Agent Review（智能体评审）

[`OTEL-SEMANTIC-CONVENTIONS-AGENT-RECOMMENDATION.md`](OTEL-SEMANTIC-CONVENTIONS-AGENT-RECOMMENDATION.md) 记录两路独立 provider 的两轮完整评审和一轮 delta review（增量复评）。第一轮问题经 source registry、trusted binding、Data Governance、cardinality 和 strict negative schema 修正后，两路第二轮均为 `RECOMMENDED`；精确校正 deployment source 与 Instrumentation Scope stability 后，两路第三轮均确认 prior recommendation preserved，所有 remaining design arrays 继续为空。

[`OTEL-SEMANTIC-CONFORMANCE-AGENT-RECOMMENDATION.md`](OTEL-SEMANTIC-CONFORMANCE-AGENT-RECOMMENDATION.md)
另行记录 46-case conformance/result contract 的两路审查。两个模型第一轮分别混淆
Human Review 与 Human Decision 顺序、以及把已受控的 upstream GenAI Schema URL 缺失
误作本项目可修事实；证据复核后两路均改为 `RECOMMENDED`，审查前必改项为 0，且都
保持 `production_ready=false` 和 Human Decision required。

评审只把本 packet 提升为 Human Review 输入，不改变 `DQ-023`、实现、部署或生产状态。

## Current Truth（当前事实）

```text
DECISION_RECORDED=false
AGENT_REVIEW_COMPLETE=true
CONTRACT_FREEZE_RECOMMENDED_BY_TWO_AGENTS=true
RECOMMENDED_TO_AGENT_DEVELOPER_BY_TWO_AGENTS=true
CORE_SEMCONV_REFERENCE_ADOPTED=false
GENAI_MAPPING_REFERENCE_ADOPTED=false
MAPPING_CATALOG_COUNT=47
MAPPING_SOURCE_REGISTRY_COUNT=9
MAPPING_SCHEMA_VALID=true
OBSERVATION_SCHEMA_VALID=true
SEMANTIC_CONFORMANCE_PROFILE_DEFINED=true
SEMANTIC_CONFORMANCE_CASE_GROUP_COUNT=8
SEMANTIC_CONFORMANCE_CASE_COUNT=46
SEMANTIC_CONFORMANCE_MAPPING_COVERAGE=47/47
SEMANTIC_CONFORMANCE_CATALOG_SCHEMA_NEGATIVES_REJECTED=12/12
SEMANTIC_CONFORMANCE_RESULT_SCHEMA_NEGATIVES_REJECTED=23/23
SEMANTIC_CONFORMANCE_RESULT_SET_SCHEMA_DEFINED=true
SEMANTIC_CONFORMANCE_RESULT_SET_NOT_ASSESSED_EXAMPLE_VALID=true
SEMANTIC_CONFORMANCE_AGENT_REVIEW_COMPLETE=true
SEMANTIC_CONFORMANCE_FREEZE_RECOMMENDED_BY_TWO_AGENTS=true
SEMANTIC_VALIDATOR_IMPLEMENTED=false
CONFORMANCE_TESTS_EXECUTED=0
IMPLEMENTATION_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
PRODUCTION_READY=false
```
