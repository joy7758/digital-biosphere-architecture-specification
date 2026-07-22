---
document_id: TMAI-OTEL-COLLECTOR-DISTRIBUTION-AGENT-RECOMMENDATION-20260722-001
title: OpenTelemetry Collector Minimal Distribution Agent Recommendation
title_zh: OpenTelemetry Collector 最小发行版智能体建议
status: review-complete-recommend-human-review-not-a-decision
decision_reference: DQ-025
implementation_authorized: false
deployment_authorized: false
production_ready: false
---

# OpenTelemetry Collector Minimal Distribution Agent Recommendation

## Review Scope（审查范围）

本记录保存 `DQ-025` 候选 contract 的 advisory model review（咨询性模型审查）。它不是
Human Decision、distribution adoption、build/deployment authorization、Runtime conformance、
customer adoption 或 production proof。

审查材料：

- [`architecture/opentelemetry-collector-distribution-profile.md`](architecture/opentelemetry-collector-distribution-profile.md)；
- [`architecture/opentelemetry-collector-component-inventory.v0.1.json`](architecture/opentelemetry-collector-component-inventory.v0.1.json)；
- 8 groups / 48 cases conformance catalog；
- [`OTEL-COLLECTOR-DISTRIBUTION-DECISION-PACKET.md`](OTEL-COLLECTOR-DISTRIBUTION-DECISION-PACKET.md)。

| provider | model | authority |
|---|---|---|
| Baidu Qianfan | `ernie-4.5-turbo-128k` | Recommendation only |
| Volcengine Ark | `deepseek-v4-flash-260425` | Recommendation only |

API credential 只从既有本地 ignored environment file 读入进程；key 未输出、未进入 prompt、
未写入本仓库。

## Pass 1 — Challenge（第一轮反对审查）

两模型均：

- 推荐 candidate contract 进入 Human Review；
- 认可 `OPTION_A` custom minimal direction；
- 保持 `production_ready=false`；
- 指出 Alpha/Beta components、未构建、未执行 48 cases、无 security/resilience evidence；
- 不把 Recommendation 当作 adoption 或 authorization。

Ark 直接推荐作为 bounded design reference，同时拒绝 Runtime recommendation。Qianfan 初次
不推荐作为架构客户资产，并要求更清晰集中：

- SBOM/signature/reproducible-build minimum evidence；
- vulnerability/stability response；
- cross-tenant batching validation；
- Alpha health authority boundary；
- deterministic transform error 与 poison retry handling。

SBOM、签名、stability drift 和 reproducible build 在首稿已分散存在；为增强 agent readability，
仍按意见集中重写，而不是把“已提到”当作清晰可验证。

Qianfan 的两项旁支陈述未采纳为事实：

1. “prebuilt distributions lack exact component version pinning”不准确；official manifests 有 exact
   module versions。问题是 component set 与 TMAI profile 不匹配，不是完全没有版本固定；
2. `otelcol-k8s` 的“66 unnecessary components”只是 74 total units 减 8 candidate components 的粗算，
   provider/component 分类和实际 overlap 不等价，规范只保留 74-unit attack-surface comparison。

## Revision（修订）

第二版增加或集中：

- 9 项 Minimum Build Evidence；
- vulnerability scanner/database/time/scope、exception Owner/Reviewer/expiry/Human Decision、
  revocation 和 rebuild rule；
- 两隔离测试租户的 batch/queue/WAL/error/self-telemetry non-disclosure procedure；
- Alpha health 只能作 bounded signal，不能单独驱动 readiness/SLO/gate；
- transform config error、deterministic runtime error、transient failure 与 poison retry stop condition；
- 若 upstream behavior 无法提供有界语义，transform 退出 untrusted ingress，`PR-G3` 保持关闭。

## Pass 2 — Final Delta Review（第二轮最终差异复审）

两模型都给出：

```text
PRIOR_CORRECTIONS_ADDRESSED=true
REMAINING_REQUIRED_CORRECTIONS_BEFORE_HUMAN_REVIEW=0
CANDIDATE_CONTRACT_RECOMMENDATION=RECOMMEND_FOR_HUMAN_REVIEW
ARCHITECTURE_ASSET_CUSTOMER_RECOMMENDATION=RECOMMEND_FOR_BOUNDED_DESIGN_REFERENCE
PRODUCTION_READY=false
```

Ark：

```text
FACTUAL_OR_AUTHORITY_ERRORS=0
RUNTIME_CUSTOMER_RECOMMENDATION=DO_NOT_RECOMMEND
```

Qianfan 给出一个 LOW comment，称 profile 未明确 Alpha health independent validation；该评论与修订后
profile 的明确文本冲突，且其 correction 又把 cross-tenant test 错连到 health。复核后将其记录为
model residual misread（模型残余误读），不作为开放文档错误。Qianfan 的
`CONDITIONALLY_RECOMMEND_AFTER_IMPLEMENTATION_EVIDENCE` 只描述未来条件；当前 Runtime 仍按更保守
交集记录为 `DO_NOT_RECOMMEND`。

## Recommendation（建议）

建议 `DQ-025` 进入 Human Architecture Review，推荐 `OPTION_A` 作为有界设计参考，不建议当前
Runtime、生产部署或客户运行使用。对潜在客户必须同时披露：

- `DQ-025` 未决定；
- custom distribution 未采用、未构建、未配置、未运行；
- Alpha/Beta component 风险未由测试证明；
- 48 个 cases 执行为 0，validator 未实现；
- DBOS/SAEE 未修改；
- 没有 production/interoperability/security/customer proof。

## Post-review Contract Hardening and Delta Review（复审后契约加固与差异审查）

在完整 `PASS` shape 审计中又补强：

- 六个 Decision 的 non-null reference/decider/time；
- artifact existence/digest、decision/config/runtime/case/summary/evidence reconciliation；
- independent reviewer separation 与 timestamp/review-record binding；
- observation window time-order validation；
- `115/115` result Schema negatives 与 `4/4` future-validator semantic predicate negatives。

首次 delta review 暴露的是表述分类问题，不是 Runtime 事实：Ark 要求澄清“未实现 validator 为何能
拒绝 semantic mutation”；Qianfan 把 adoption 后的 Decision/build/runtime prerequisites 误列为
Human Review 前的文档修正。随后 profile 与 decision packet 明确：`4/4` 只是 ephemeral in-memory
future-validator design rehearsal；`READY_FOR_REVIEW` 与 future implementation `PASS` prerequisites
相互分离，避免循环授权。

最终 delta review 两模型均确认：

```text
PRIOR_RECOMMENDATION_PRESERVED=true
REQUIRED_DOCUMENT_CORRECTIONS_BEFORE_HUMAN_REVIEW=0
FACTUAL_OR_AUTHORITY_ERRORS=0
RECOMMEND_FOR_HUMAN_REVIEW=true
RECOMMEND_AS_BOUNDED_DESIGN_REFERENCE=true
RECOMMEND_FOR_CURRENT_RUNTIME=false
PRODUCTION_READY=false
```

模型列出的 Decision、artifact、validator、review、48-case runtime evidence 均保留为 adoption 后的
future PASS prerequisites，不被写成当前已满足，也不阻止人类现在审查 architecture candidate。

## Current Truth（当前事实）

```text
AGENT_REVIEW_COMPLETE=true
PROVIDERS_COMPLETED=2/2
POST_HARDENING_DELTA_REVIEW_COMPLETE=true
RESULT_SCHEMA_NEGATIVES_REJECTED=115/115
FUTURE_VALIDATOR_SEMANTIC_NEGATIVE_REHEARSAL=4/4
HUMAN_REVIEW_RECOMMENDED_BY_TWO_MODELS=true
BOUNDED_DESIGN_REFERENCE_RECOMMENDED_BY_TWO_MODELS=true
CURRENT_RUNTIME_RECOMMENDATION=DO_NOT_RECOMMEND
REQUIRED_DOCUMENT_CORRECTIONS_OPEN=0
POST_HARDENING_FACTUAL_OR_AUTHORITY_ERRORS=0
MODEL_RESIDUAL_MISREADS_RECORDED=1
DQ_025_DECIDED=false
CUSTOM_DISTRIBUTION_ADOPTED=false
VALIDATOR_IMPLEMENTED=false
RUNTIME_CASES_EXECUTED=0
IMPLEMENTATION_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
PRODUCTION_READY=false
```
