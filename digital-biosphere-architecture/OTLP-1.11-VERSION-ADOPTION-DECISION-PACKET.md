---
document_id: TMAI-OTLP-1.11-ADOPTION-PACKET-20260722-001
title: OTLP v1.11.0 Reference Adoption Decision Packet
title_zh: OTLP v1.11.0 参考版本采纳决策包
status: ready-for-human-decision-agent-review-complete-not-authorized
decision_id: DQ-022
implementation_authorized: false
deployment_authorized: false
---

# OTLP v1.11.0 Reference Adoption Decision Packet

## Decision Question（决策问题）

是否把 official `open-telemetry/opentelemetry-proto` `v1.11.0`、commit `790608c4d51e6ffc12210b541e8514cbed9e91a4` 采纳为 TMAI v0.1 production-path 的 OTLP architecture reference（架构参考），并把其 request/response size-limit 与 `Retry-After` 语义纳入后续符合性要求？

## Recommended Option（推荐选项）

`OPTION_A`: adopt reference only（只采纳参考版本）。

理由：

- 上游 release/tag/commit 可验证；
- 当前选定的 Trace/Metric/Log 稳定 wire scope 没有发现破坏；
- 新增 size-limit 规范直接强化 resource exhaustion（资源耗尽）防护；
- Profiles 和 Process Context 可以明确排除；
- 独立版本决定可阻止 `latest` 自动漂移。

## Options（选项）

| option | 结果 | 保留边界 |
|---|---|---|
| `OPTION_A` | 采纳 `v1.11.0` exact tag/commit 作为 reference，并冻结 delta controls | 不授权实现、部署、SDK/Collector 选型或生产使用 |
| `OPTION_B` | 继续使用 `v1.10.0`，把 `v1.11.0` 保持 observed candidate | 必须说明 hold reason 和重新审查条件 |
| `OPTION_C` | 退回修订 | 必须说明 assessment、scope 或兼容声明的具体缺口 |

## Exact Human Decision Tokens（精确人工决定令牌）

采纳：

```text
DQ-022=ADOPT_OTLP_1_11_0_REFERENCE_BASELINE
decided_by_ref=<human-reference>
```

保持旧版本：

```text
DQ-022=HOLD_OTLP_1_10_0_REFERENCE_BASELINE
decided_by_ref=<human-reference>
hold_reason=<required>
```

退回修订：

```text
DQ-022=RETURN_OTLP_1_11_0_ADOPTION_FOR_REVISION
decided_by_ref=<human-reference>
revision_reason=<required>
```

## Accepted Scope If Option A Is Chosen（选 A 时接受范围）

- exact source tag/commit；
- Trace/Metric/Log reference scope；
- request/response pre/post compression size-limit behavior；
- `413`、`RESOURCE_EXHAUSTED`、non-retryable 和 unknown acceptance semantics；
- `Retry-After` HTTP-date 与 delay-seconds；
- Profiles/Process Context exclusion；
- future upstream delta governance。
- [`architecture/otlp-v1.11-conformance-profile.md`](architecture/otlp-v1.11-conformance-profile.md) 的 selected scope、four-layer boundary 和 exact case semantics；
- [`architecture/otlp-v1.11-conformance-cases.v0.1.json`](architecture/otlp-v1.11-conformance-cases.v0.1.json) / [schema](architecture/schemas/otlp-conformance-case-catalog.schema.v0.1.json) 作为后续测试预注册基线；目录中的 `NOT_EXECUTED` 不随版本采纳改变。
- [`architecture/schemas/otlp-conformance-result-set.schema.v0.1.json`](architecture/schemas/otlp-conformance-result-set.schema.v0.1.json) 作为未来逐 case 结果结构；当前 synthetic example 为 `NOT_ASSESSED`，validator 未实现。

## Explicitly Rejected Scope（明确不接受的范围）

- 自动选择或升级任何 SDK/Collector；
- 创建 listener、endpoint、Runtime、Entity、Evidence 或 Permission；
- 修改 DBOS/SAEE；
- 把 upstream stable 声明写成 TMAI Runtime interoperability proof；
- 把 Version Adoption 写成 Implementation、Deployment 或 Production Readiness。

## Required Follow-ups（后续）

若采纳：

1. 更新 `ADR-025`、DQ 和 version record 状态；
2. 在 immutable DBA baseline 中冻结 exact source；
3. 冻结 conformance catalog digest；`DQ-018` 只执行 reference-decoder/authority subset，`DQ-020` 才执行 listener/Collector transport cases；
4. 实施仓库另行选择 SDK/Collector versions，并独立证明 compatibility；
5. 保持所有生产 gate 为未通过，直到 direct evidence 出现。

## Agent Review（智能体评审）

[`OTLP-1.11-VERSION-ADOPTION-AGENT-RECOMMENDATION.md`](OTLP-1.11-VERSION-ADOPTION-AGENT-RECOMMENDATION.md) 记录两路独立 provider 评审。两路均推荐采纳 reference、均未发现 selected stable scope breaking issue、source/delta error 或 design correction，同时均保持 `production_customer_recommendable_now=false`。

[`OTLP-1.11-CONFORMANCE-PROFILE-AGENT-RECOMMENDATION.md`](OTLP-1.11-CONFORMANCE-PROFILE-AGENT-RECOMMENDATION.md) 另记录 catalog、sequence delta 与 Result Set Schema 的多轮评审：两路最终均建议进入 Human Review freeze，open design corrections 0；这仍不是 freeze、Version Decision 或 test execution。

该结果把本决策包提升为 `READY_FOR_HUMAN_DECISION`，不把 `DQ-022` 写成已决定。

```text
DECISION_RECORDED=false
AGENT_REVIEW_COMPLETE=true
REFERENCE_ADOPTION_RECOMMENDED_BY_TWO_AGENTS=true
CONFORMANCE_CATALOG_FREEZE_RECOMMENDED_BY_TWO_AGENTS=true
CONFORMANCE_RESULT_SCHEMA_FREEZE_RECOMMENDED_BY_TWO_AGENTS=true
REFERENCE_ADOPTED=false
IMPLEMENTATION_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
PRODUCTION_READY=false
```
