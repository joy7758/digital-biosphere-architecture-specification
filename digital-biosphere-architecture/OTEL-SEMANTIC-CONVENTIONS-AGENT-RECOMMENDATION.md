---
document_id: TMAI-OTEL-SEMANTIC-CONVENTIONS-AGENT-REVIEW-20260722
title: OpenTelemetry Semantic Conventions Mapping Agent Recommendation
title_zh: OpenTelemetry 语义约定映射智能体推荐
status: complete-two-provider-recommended-for-human-review-production-false
observed_at: 2026-07-22
provider_count: 2
mapping_count: 47
mapping_group_count: 7
source_registry_count: 9
contract_freeze_recommended_by_two_agents: true
recommended_to_agent_developer_by_two_agents: true
open_design_corrections: 0
production_customer_recommendable_now: false
human_decision_recorded: false
implementation_authorized: false
---

# OpenTelemetry Semantic Conventions Mapping Agent Recommendation

中文：OpenTelemetry 语义约定映射智能体推荐。

## 1. Review Question（评审问题）

两路独立 provider 以 potential AI-agent developer customer（潜在智能体开发者客户）视角评审：

> 对需要 vendor-neutral、production-oriented、trustworthy multi-agent telemetry semantics（供应商中立、面向生产、可信多智能体遥测语义）的开发者，是否建议把当前合同冻结为 Human Review 输入和未来另行授权实现的架构合同？

评审明确：

```text
Agent Recommendation
  != DQ-023 Human Version Decision
  != DQ-018 Implementation Authorization
  != DQ-020 Collector Deployment Authorization
  != Conformance Evidence
  != Production Customer Recommendation
```

## 2. Review Inputs（评审输入）

- [`architecture/opentelemetry-semantic-conventions-profile.md`](architecture/opentelemetry-semantic-conventions-profile.md)；
- [`architecture/opentelemetry-semantic-mapping.v0.1.json`](architecture/opentelemetry-semantic-mapping.v0.1.json)；
- [mapping schema](architecture/schemas/opentelemetry-semantic-mapping.schema.v0.1.json)；
- [observation schema](architecture/schemas/opentelemetry-semantic-observation.schema.v0.1.json)；
- [`OTEL-SEMANTIC-CONVENTIONS-ADOPTION-DECISION-PACKET.md`](OTEL-SEMANTIC-CONVENTIONS-ADOPTION-DECISION-PACKET.md)。

没有向模型提供 provider key、真实 telemetry、客户数据、Agent instance、Runtime、endpoint 或生产结果。调用只读取 `/Users/zhangbin/GitHub/SAEE/.env.local` 的现有 provider credential；key 未输出、未写入 DBA、未进入 prompt 或本记录。

## 3. Review Sessions（评审会话）

| session_id | provider/model | round | result |
|---|---|---:|---|
| `TMAI-OTEL-SEMCONV-20260722-QIANFAN-01` | Baidu Qianfan / `ernie-4.5-turbo-128k` | 1 | `CONDITIONALLY_RECOMMENDED`；建议 contract freeze；不向开发者推荐；提出字段来源、binding enforcement、敏感 opt-in、基数和 digest 问题 |
| `TMAI-OTEL-SEMCONV-20260722-ARK-01` | Volcengine Ark / `deepseek-v4-flash-260425` | 1 | `CONDITIONALLY_RECOMMENDED`；建议 contract freeze；指出 baggage enforcement、cross-field binding 和 per-field overflow 缺口 |
| `TMAI-OTEL-SEMCONV-20260722-QIANFAN-02` | Baidu Qianfan / `ernie-4.5-turbo-128k` | 2 | `RECOMMENDED`；推荐给潜在 Agent 开发者；prior concerns closed；所有 remaining arrays 为空；confidence `high` |
| `TMAI-OTEL-SEMCONV-20260722-ARK-02` | Volcengine Ark / `deepseek-v4-flash-260425` | 2 | `RECOMMENDED`；推荐给潜在 Agent 开发者；prior concerns closed；所有 remaining arrays 为空；confidence `high` |
| `TMAI-OTEL-SEMCONV-20260722-QIANFAN-03` | Baidu Qianfan / `ernie-4.5-turbo-128k` | 3 delta | `RECOMMENDED`；确认 deployment source 与 Instrumentation Scope stability 校正有效；prior recommendation preserved；所有 remaining arrays 为空；confidence `high` |
| `TMAI-OTEL-SEMCONV-20260722-ARK-03` | Volcengine Ark / `deepseek-v4-flash-260425` | 3 delta | `RECOMMENDED`；确认两个校正改善来源和稳定性精度且未引入新风险；prior recommendation preserved；所有 remaining arrays 为空；confidence `high` |

## 4. Normative Triage and Corrections（规范取舍与修正）

### Closed in Contract（已在合同中关闭）

- 新增 9 项 exact stability source registry，47/47 mapping 各有且只有一个字段来源覆盖；
- `deployment.environment.name` 的来源从错误的 service 文档拆分到 exact `v1.43.0` deployment registry；字段仍为 Stable；
- `instrumentation_scope.schema_url` 按 OTel Specification `v1.59.0` 的 Stable Instrumentation Scope tuple 记录为 Stable；它是 `ScopeSpans/ScopeMetrics/ScopeLogs.schema_url` 的跨信号规范化结构路径，不是 Development 的 `otel.scope.schema_url` attribute；
- 把 OpenTelemetry Specification `v1.59.0@a824fb4...` release 与 observed HEAD `2b04e8b...` 分离；
- observation envelope 必须绑定 profile/catalog ID 与 digest；
- sensitive content opt-in 必须有 decision、policy digest、exact field allowlist、retention、residency、access 和 redaction reference；
- `content_capture_state=DISABLED` 时 Schema 直接拒绝 8 类敏感字段；
- strict envelope 不接受 `baggage`，也拒绝 `tmai.*`、`dbos.*`、`saee.*` 和裸 authority-like 字段；
- Metric 直接拒绝 service instance、trace/span、agent、conversation 和 tool call 等高基数标识；
- trusted identity/execution/capability binding 必须引用 `DBOS_CONTEXT`、exact reference 与 binding record digest；
- 机器目录冻结 cardinality prohibited fields、budget scope、overflow action 和 no-silent-drop；
- 47 个 mapping、7 个 group 和 9 个 source registry 均精确覆盖；两个 Schema 正例 0 错误，20/20 负例被拒绝。

### Reclassified as Future Implementation Prerequisites（转为未来实现前置）

- semantic validator 和 upstream stability drift detection；
- Data Governance approval workflow；
- DBOS trusted binding procedure；
- per-tenant/service/window cardinality budget enforcement；
- deprecated GenAI field migration；
- immutable digest computation；
- 47 项映射及所有负例的真实 conformance execution。

这些事项不阻塞 architecture contract freeze，但阻塞任何 implementation、deployment、gate PASS 或 production recommendation。

### Already Covered, Not Duplicated（已有覆盖，不重复增加）

- GenAI 未来获得 tag/Schema URL 的 change process 已在 profile Version Change Rule 明确；
- mapping profile digest 已是 observation envelope required field；
- 每项 mapping 已有 machine-readable `authority_rule`；
- GenAI 没有 tag/Schema URL 是上游当前 limitation，不是 TMAI 虚构的稳定性错误。

## 5. Final Recommendation（最终推荐）

两路第二轮一致返回完整推荐；来源与稳定性精确校正后的第三轮 delta review 继续一致返回：

```text
overall=RECOMMENDED
recommend_contract_freeze=true
recommend_to_potential_agent_developer=true
prior_valid_concerns_closed=true
prior_recommendation_preserved=true
deployment_source_correction_valid=true
instrumentation_scope_stability_correction_valid=true
remaining_factual_or_stability_errors=[]
remaining_missing_required_controls=[]
remaining_authority_boundary_leaks=[]
remaining_sensitive_data_or_cardinality_gaps=[]
required_design_corrections_before_freeze=[]
production_customer_recommendable_now=false
human_decision_still_required=true
confidence=high
```

“推荐给 Agent 开发者”仅表示架构合同可理解、边界清晰且值得进入人工冻结与未来实现评估；不表示 SDK/adapter 已可使用，也不表示真实 Agent 已采用。

## 6. Current Truth（当前事实）

```text
AGENT_REVIEW_COMPLETE=true
PROVIDERS_WITH_SUCCESS=2
FINAL_RECOMMENDATIONS=2
DELTA_REVIEW_SESSIONS=2
DELTA_RECOMMENDATIONS=2
CONTRACT_FREEZE_RECOMMENDED_BY_TWO_AGENTS=true
RECOMMENDED_TO_AGENT_DEVELOPER_BY_TWO_AGENTS=true
PRIOR_RECOMMENDATION_PRESERVED_BY_TWO_AGENTS=true
PRIOR_VALID_CONCERNS_CLOSED=true
OPEN_FACTUAL_OR_STABILITY_ERRORS=0
OPEN_REQUIRED_CONTROLS=0
OPEN_AUTHORITY_LEAKS=0
OPEN_SENSITIVE_OR_CARDINALITY_GAPS=0
OPEN_REQUIRED_DESIGN_CORRECTIONS=0
MAPPING_COUNT=47
MAPPING_GROUP_COUNT=7
SOURCE_REGISTRY_COUNT=9
MAPPING_SCHEMA_VALID=true
OBSERVATION_SCHEMA_VALID=true
NEGATIVE_CASES_REJECTED=20/20
DQ_023_HUMAN_DECISION_RECORDED=false
SEMANTIC_VALIDATOR_IMPLEMENTED=false
CONFORMANCE_TESTS_EXECUTED=0
IMPLEMENTATION_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
PRODUCTION_CUSTOMER_RECOMMENDABLE_NOW=false
PRODUCTION_READY=false
```

## 7. Next Gate（下一闸门）

Human Architecture Version Authority 可以使用 [`OTEL-SEMANTIC-CONVENTIONS-ADOPTION-DECISION-PACKET.md`](OTEL-SEMANTIC-CONVENTIONS-ADOPTION-DECISION-PACKET.md) 对 `DQ-023` 作出显式选择。Agent recommendation 不得填充 `decided_by_ref`，也不得触发 DBOS/SAEE 修改。
