---
document_id: TMAI-OTLP-1.11-CONFORMANCE-AGENT-REVIEW-20260722
title: OTLP v1.11 Conformance Profile Agent Recommendation
title_zh: OTLP v1.11 符合性配置智能体推荐
status: complete-two-provider-recommended-for-human-review-freeze-production-false
observed_at: 2026-07-22
catalog_case_count: 56
catalog_case_group_count: 7
catalog_freeze_recommended_by_two_agents: true
result_schema_freeze_recommended_by_two_agents: true
open_design_corrections: 0
production_customer_recommendable_now: false
human_decision_recorded: false
tests_executed: false
---

# OTLP v1.11 Conformance Profile Agent Recommendation

中文：OTLP v1.11 符合性配置智能体推荐。

## 1. Review Question（评审问题）

两路独立 provider 评审同一问题：

> 是否建议把 proposed、`NOT_ADOPTED`、`NOT_EXECUTED` 的 OTLP v1.11 conformance profile/catalog 冻结为 Human Review（人工审查）输入和未来另行授权实施的测试合同？

评审明确区分：

```text
Catalog Freeze Recommendation
  != DQ-022 Version Adoption
  != DQ-018 Implementation Authorization
  != DQ-020 Deployment Authorization
  != Test Execution or Evidence
  != Production Customer Recommendation
```

评审输入包含 7 个 case groups、逐 case layer/gate/source/stimulus/expected outcome/observation/forbidden inference，以及所有 effects 为 `false` 的事实。没有向模型提供 provider key、真实客户数据、Runtime、endpoint 或生产结果。

## 2. Review Sessions（评审会话）

| session_id | provider / model | round | result |
|---|---|---:|---|
| `TMAI-OTLP-CONFORMANCE-20260722-QIANFAN-01` | Baidu Qianfan / `ernie-4.5-turbo-128k` | 1 | `CONDITIONALLY_RECOMMENDED`；建议 freeze；指出 response discard 记录、authn/authz 分离和若干边界用例 |
| `TMAI-OTLP-CONFORMANCE-20260722-ARK-01` | Volcengine Ark / `deepseek-v4-flash-260425` | 1 | `CONDITIONALLY_RECOMMENDED`；建议 freeze；指出 gRPC `RetryInfo`、permanent error detail、malformed/unknown response 和 invalid partial count |
| `TMAI-OTLP-CONFORMANCE-20260722-QIANFAN-02` | Baidu Qianfan / `ernie-4.5-turbo-128k` | 2 | `RECOMMENDED`；prior corrections closed；remaining arrays 全空；production customer=false；confidence `high` |
| `TMAI-OTLP-CONFORMANCE-20260722-ARK-02` | Volcengine Ark / `deepseek-v4-flash-260425` | 2 | `RECOMMENDED`；prior corrections closed；remaining arrays 全空；production customer=false；confidence `high` |

调用使用 `/Users/zhangbin/GitHub/SAEE/.env.local` 中现有 provider credentials。key 未输出、未写入 DBA、未进入 prompt 或本记录。

## 3. Normative Triage（规范核验与取舍）

第一轮意见没有自动进入规范。每项先与 official [`v1.11.0` OTLP specification](https://github.com/open-telemetry/opentelemetry-proto/blob/v1.11.0/docs/specification.md) 核验：

### Accepted and Closed（已接受并闭合）

- 新增 response additive unknown protobuf field case；
- 新增 malformed gRPC/HTTP success response cases；
- 新增 gRPC `RetryInfo` throttling case，并区分 `RESOURCE_EXHAUSTED` 有／无 `RetryInfo`；
- 新增 gRPC `INVALID_ARGUMENT + BadRequest` permanent failure case；
- 新增 partial rejected count 超出 sent count 的 TMAI fail-closed case；
- 新增 rejected count `0` + non-empty `error_message` warning case；
- 把 transport authentication 与 policy authorization 拆成独立 cases；
- gRPC/HTTP oversized client response 明示记录 discarded response fact 和 `UNKNOWN` acceptance；
- 明确 unknown protobuf wire compatibility 与 TMAI mapped-envelope allowlist 是两层规则。

### Not Added as Duplicate or Non-normative（未作为新用例加入）

- exact `4 MiB` gRPC/HTTP response boundary 已由 `OTLP-CF-GRPC-005` / `OTLP-CF-HTTP-005` 覆盖，不重复创建；
- OTLP partial success 定义 rejected count 和 optional diagnostic，没有 item-level unknown acceptance 字段；因此没有虚构“部分 item unknown”协议状态。request-level/hop-level `UNKNOWN` 已由 response oversize、malformed response、disconnect 和 reconciliation cases 覆盖。

## 4. Final Recommendation（最终推荐）

两路第二轮均返回：

```text
overall=RECOMMENDED
recommend_catalog_freeze=true
prior_corrections_closed=true
remaining_missing_normative_cases=[]
remaining_incorrect_expected_outcomes=[]
remaining_layer_boundary_violations=[]
required_design_corrections=[]
production_customer_recommendable_now=false
confidence=high
```

这是“可进入人工冻结审查”的推荐，不是已经冻结。`DQ-022` 仍是 `READY_FOR_REVIEW`，56 个 case 仍全部 `NOT_EXECUTED`，validator 仍未实现。

## 5. Result Set Schema Review（结果集 Schema 评审）

目录完成后，审计发现 `case_results_ref` 尚无 shape contract。新增 [`architecture/schemas/otlp-conformance-result-set.schema.v0.1.json`](architecture/schemas/otlp-conformance-result-set.schema.v0.1.json) 和 synthetic [`NOT_ASSESSED` example](architecture/examples/otlp-conformance-result-set.not-assessed.example.json)，再进行独立评审。

| session_id | provider/model | result |
|---|---|---|
| `TMAI-OTLP-RESULT-SCHEMA-20260722-QIANFAN-01` | Qianfan / `ernie-4.5-turbo-128k` | 初评不建议 freeze；部分意见错误地要求 Result Set 自行改变 production state，但有效地指出需显式 validator/digest binding |
| `TMAI-OTLP-RESULT-SCHEMA-20260722-ARK-01` | Ark / `deepseek-v4-flash-260425` | 建议 freeze；无 gap/leak/correction；production=false |
| `TMAI-OTLP-RESULT-SCHEMA-20260722-QIANFAN-02` | Qianfan | 确认 prior valid concerns closed、missing/leak arrays 为空，但仍把 validator implementation 错误前置于 architecture schema freeze |
| `TMAI-OTLP-RESULT-SCHEMA-20260722-ARK-02` | Ark | `RECOMMENDED`；明确 `NOT_IMPLEMENTED → DRAFT/NOT_ASSESSED` 是正确失败关闭 |
| `TMAI-OTLP-RESULT-SCHEMA-20260722-QIANFAN-03` | Qianfan | `recommend_schema_contract_freeze=true`；architecture-before-implementation=true；negative demonstrated=true；authority preserved=true；design corrections=[]；future gate-use prerequisites 单列 |
| `TMAI-OTLP-RESULT-SCHEMA-20260722-ARK-03` | Ark | `RECOMMENDED`；四个布尔均 true；design corrections=[]；production=false |

有效修正：

- `validation_binding` 要求 validator ID/version/artifact digest、schema/semantic/case-set/summary checks、catalog/Decision/implementation/environment verification 和 digested report；
- PASS-like fixture 在 validator 为 `NOT_IMPLEMENTED` 时被 14 条约束拒绝；
- `authority_boundary` 直接编码 Result Set 不是 Gate Decision/Human Authorization、不能改变 Runtime，并要求独立 evaluator/reviewer/human decision；
- Decision record/scope digest、authority registry、decider/time 被纳入 PASS shape。

拒绝让 `effects.production_ready` 或 `closes_production_gate` 可变：那会把结果文件变成自我授权主体。Qianfan 最终同意 schema contract 可以先冻结，同时把 validator 实施、digest verification 和 evaluator/Reviewer 建立保留为 future gate-use prerequisites（未来闸门使用前置）。

## 6. Current Truth（当前事实）

```text
AGENT_REVIEW_COMPLETE=true
PROVIDERS_WITH_SUCCESS=2
FINAL_RECOMMENDATIONS=2
CATALOG_FREEZE_RECOMMENDED_BY_TWO_AGENTS=true
OPEN_NORMATIVE_CASE_GAPS=0
OPEN_INCORRECT_EXPECTED_OUTCOMES=0
OPEN_LAYER_BOUNDARY_VIOLATIONS=0
OPEN_REQUIRED_DESIGN_CORRECTIONS=0
CATALOG_CASE_COUNT=56
CATALOG_CASE_GROUP_COUNT=7
CATALOG_SCHEMA_VALID=true
CATALOG_SEMANTIC_CHECK_PASS=true
CATALOG_FROZEN_BY_HUMAN_DECISION=false
RESULT_SET_SCHEMA_DEFINED=true
RESULT_SET_NOT_ASSESSED_EXAMPLE_VALID=true
RESULT_SET_SCHEMA_NEGATIVES_REJECTED=5/5
PASS_WITH_VALIDATOR_NOT_IMPLEMENTED_REJECTED=true
RESULT_SCHEMA_FREEZE_RECOMMENDED_BY_TWO_AGENTS=true
RESULT_SCHEMA_OPEN_DESIGN_CORRECTIONS=0
OTLP_REFERENCE_ADOPTED=false
TESTS_EXECUTED=0
CONFORMANCE_VALIDATOR_IMPLEMENTED=false
IMPLEMENTATION_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
PRODUCTION_CUSTOMER_RECOMMENDABLE_NOW=false
PRODUCTION_READY=false
```

## 7. Next Gate（下一闸门）

Human Architecture Version Authority 可以把本记录与 [`OTLP-1.11-VERSION-ADOPTION-DECISION-PACKET.md`](OTLP-1.11-VERSION-ADOPTION-DECISION-PACKET.md) 一并用于 `DQ-022`。Agent recommendation 不得填充 `decided_by_ref`，也不得触发 DBOS/SAEE 修改。
