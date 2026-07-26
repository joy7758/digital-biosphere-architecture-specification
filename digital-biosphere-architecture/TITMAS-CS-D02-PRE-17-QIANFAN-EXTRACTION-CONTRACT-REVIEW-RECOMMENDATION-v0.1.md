---
document_id: DBA-TITMAS-CS-D02-PRE-17-QIANFAN-EXTRACTION-CONTRACT-REVIEW-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-17 Qianfan Extraction Contract Static Review Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-17 Qianfan 提取契约静态审查建议 v0.1
version: 0.1.0
status: recommendation-prepared-not-decided
maturity: Development
document_type: zero-request-extraction-contract-static-review-recommendation
decision_candidate_id: CS-D02-PRE-17
owner_ref: zhangbin
observed_on: 2026-07-26
authority_effect: none
---

# TITMAS CS-D02 PRE-17 Qianfan Extraction Contract Static Review Recommendation v0.1

## 1. Recommendation

建议未来单独决定：

```text
RECOMMENDED_OPTION=AUTHORIZE_ZERO_LIVE_REQUEST_QIANFAN_EXTRACTION_CONTRACT_STATIC_REVIEW_ONLY
LIVE_MODEL_REQUESTS_MAX=0
PROVIDER_NETWORK_REQUESTS_MAX=0
RETRY_MAX=0
FALLBACK_MAX=0
JSON_REPAIR_MAX=0
AT_RECOMMENDATION_TIME_PRE_17_DECIDED=false
AT_RECOMMENDATION_TIME_STATIC_REVIEW_AUTHORIZED=false
```

PRE-17 只审查 installed Qianfan/Kimi tool 的声明 `CallToolResult`、PRE-15 ordered
extraction contract 与 PRE-16 sanitized failure classification 之间的契约差异。它不恢复、
重构或猜测 PRE-16 raw provider body，也不发送新的 provider 请求。

## 2. Frozen Evidence Basis

```text
PRE15_RESULT_COMMIT=84718024ce55164f83c3bf6cf966e2d182754deb
PRE15_DECLARED_TOOL_CONTRACT_SHA256=bc7a78ee54a633d46c586994fbfded293d1b05abbfc3d4773917d222ccb80ce9
PRE15_SYNTHETIC_CASES_MATCHED=8/8
PRE16_RESULT_COMMIT=2195720b1100a26bc972293f133dfba1b908ec5e
PRE16_SANITIZED_OBSERVATION_SHA256=39e60eaa6e20233767cbfad2aa3ba4a21025ae471974a0eedd3f81561249e9e1
PRE16_COMPOSITE_GATE_RESULT_SHA256=4e1b0f3d9adc4d64dff1129dcc973e5e29d43cab47a0ec9cdaf727361cf257a3
PRE16_EXECUTION_RECEIPT_SHA256=04c5dcb8f31e8005624ee8bf5545d47c6c294e9e490e1855ed6235d3658f5f19
PRE16_QIANFAN_DIRECT_JSON_PARSE_PASS=true
PRE16_QIANFAN_FULL_FROZEN_SCHEMA_PASS=false
PRE16_RAW_PROVIDER_BODY_PERSISTED=false
PRE16_EXACT_RAW_WRAPPER_SHAPE_PROVEN=false
```

这些材料证明 extraction contract 仍不能稳定得到规范 reviewer response；它们不证明模型
没有回答，也不证明 exact runtime wrapper 的字段结构。

## 3. Exact Static Review Scope

只允许：

1. 区分 `CallToolResult` transport envelope、structured result payload 与 provider
   `answer`；
2. 对声明路径建立 declared-to-caller crosswalk，不读取任何 live response；
3. 检查 PRE-15 第四路径是否过早把任意 plain `content[0].text` 当作 provider answer；
4. 定义 bounded recursive unwrap 候选，只允许显式列出的 wrapper/path，不允许任意递归；
5. 定义 ambiguity、missing、wrong-type、nested-wrapper、non-review-object 和 duplicate-value
   失败语义；
6. 设计 privacy-preserving shape descriptor，未来若另行授权 request，只记录 path
   presence、value type、content type、candidate count 与 value digest，不记录原始值；
7. 使用 synthetic fixtures 验证 extraction contract candidate 和完整 frozen Schema
   validator。

## 4. Required Review Questions

PRE-17 必须回答：

1. tool declaration 中的 `CallToolResult<T>` 与 caller 实际可见对象应如何分层？
2. `content[0].text` 在什么条件下可视为 semantic answer，什么条件下只能视为 transport
   serialization？
3. JSON text 解析得到非 reviewer root object 时，是否应尝试一个且仅一个显式 wrapper
   unwrap，而不是直接把该对象送入 reviewer Schema？
4. 如何在不保存原始 provider body 的情况下证明 extraction path、候选值数量和歧义状态？
5. 哪些情况必须分类为 `UNKNOWN_RUNTIME_ENVELOPE`，而不是模型失败？
6. future one-request confirmation 是否仍有必要；如必要，需要冻结哪些最小诊断元数据？

## 5. Success Criteria

必须同时满足：

```text
LIVE_MODEL_REQUESTS_EXECUTED=0
PROVIDER_NETWORK_REQUESTS_EXECUTED=0
RAW_PRE16_PROVIDER_BODY_ACCESSED=false
TRANSPORT_AND_SEMANTIC_LAYERS_DISTINGUISHED=true
PLAIN_CONTENT_TEXT_ACCEPTANCE_RULE_NARROWED=true
BOUNDED_UNWRAP_PATHS_EXPLICIT=true
PRIVACY_PRESERVING_SHAPE_DESCRIPTOR_DEFINED=true
SYNTHETIC_POSITIVE_AND_NEGATIVE_CASES_VALIDATED=true
PRE16_EXACT_PROVIDER_FAILURE_CAUSE_OVERSPECIFIED=false
```

成功只允许形成一个 future provider confirmation recommendation 或停止继续使用当前
tool path 的 recommendation；不能直接执行请求。

## 6. Required Outputs

若未来获准执行，只允许形成：

- frozen PRE-17 static review plan 与 Schema；
- authorization baseline receipt；
- declared-result / transport-envelope / semantic-answer crosswalk；
- extraction contract candidate；
- privacy-preserving shape descriptor contract；
- synthetic nested-wrapper and ambiguity fixtures；
- deterministic offline validation result 与 Schema；
- human-readable report；
- execution receipt；
- path-scoped commit/push receipt。

## 7. Stop Conditions

- PRE-17 Decision、plan、Schema 或远端授权基线不存在；
- PRE-15/PRE-16 frozen digest 漂移；
- 需要 live model/provider request；
- 需要读取 secret、raw provider body、token usage 或隐藏推理；
- 需要任意递归、substring extraction、fence stripping 或 JSON repair；
- 需要把 transport metadata 猜测成 provider answer；
- synthetic fixture 被抬升为 provider evidence；
- candidate review、validity、counting、Gate、市场、客户或商业效果被请求。

## 8. False Effects

```text
PRE_17_DECIDED=false
STATIC_REVIEW_AUTHORIZED=false
LIVE_MODEL_REQUESTS_AUTHORIZED=false
PRE16_EXACT_QIANFAN_FAILURE_CAUSE_PROVEN=false
QIANFAN_PROVIDER_SCHEMA_CONFIRMATION_PASS=false
COMPOSITE_PROVIDER_GATE_PASS=false
CANDIDATE_REVIEW_COMPLETED=false
RECORD_COUNTING_AUTHORIZED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
MARKET_VALIDATION_PASS=false
CUSTOMER_ADOPTION=false
IMPLEMENTATION_AUTHORIZED=false
EXTERNAL_OUTREACH_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

静态 extraction review 不等于 provider success、候选审查或商业验证。
