---
document_id: DBA-TITMAS-CS-D02-PRE-15-QIANFAN-WRAPPER-EXTRACTION-DIAGNOSTIC-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-15 Qianfan Wrapper Extraction Diagnostic Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-15 Qianfan Wrapper 提取离线诊断建议 v0.1
version: 0.1.0
status: recommendation-prepared-not-decided
maturity: Development
document_type: offline-wrapper-extraction-diagnostic-recommendation
decision_candidate_id: CS-D02-PRE-15
owner_ref: zhangbin
observed_on: 2026-07-26
authority_effect: none
---

# TITMAS CS-D02 PRE-15 Qianfan Wrapper Extraction Diagnostic Recommendation v0.1

## 1. Recommendation

建议未来单独决定：

```text
RECOMMENDED_OPTION=AUTHORIZE_OFFLINE_QIANFAN_WRAPPER_EXTRACTION_DIAGNOSTIC_ONLY
LIVE_MODEL_REQUESTS_MAX=0
PROVIDER_NETWORK_REQUESTS_MAX=0
RETRY_MAX=0
FALLBACK_MAX=0
JSON_REPAIR_MAX=0
AT_RECOMMENDATION_TIME_PRE_15_DECIDED=false
AT_RECOMMENDATION_TIME_DIAGNOSTIC_AUTHORIZED=false
```

PRE-15 只诊断 PRE-14 Qianfan/Kimi 会话的 extraction boundary（提取边界）。它必须区分：

1. provider/model 没有返回回答；
2. installed tool 返回了回答，但 caller 没有从正确的 wrapper field 提取；
3. wrapper contract 不足以在不查看 raw body 的条件下分类。

PRE-15 不允许恢复、读取或重构 PRE-14 raw response；该数据没有被持久化。

## 2. Frozen Evidence Basis

```text
PRE14_REMOTE_RESULT_COMMIT=ea85ece26b7dfb75ad84b0de3a7ddf0ca7f2738a
PRE14_REQUESTS_EXECUTED=2
PRE14_QIANFAN_FAILURE_CLASS=PROVIDER_RESPONSE_NOT_EXTRACTABLE
PRE14_DEEPSEEK_FULL_SCHEMA_PASS=true
PRE14_PROVIDER_SCHEMA_CONFIRMATION_PASS=false
PRE14_REQUEST_CAP_CONSUMED=true
```

冻结输入包括：

- PRE-14 Decision、execution plan、authorization receipt；
- PRE-14 sanitized observations、gate result、execution receipt；
- installed Qianfan/Kimi tool 的公开 machine tool contract；
- PRE-13 provider-binding fixtures；
- response Schema。

## 3. Exact Offline Scope

只允许：

- 记录 installed tool 的公开输出契约和 caller extraction assumptions；
- 定义 wrapper shape classification fixtures，不包含 provider raw response；
- 为 `structuredContent.answer`、direct `answer`、JSON-wrapped text、plain text 和
  missing-answer 等候选 envelope 建立 synthetic cases；
- 明确哪些字段可以被视为 model answer，哪些只能视为 transport metadata；
- 使用 synthetic answer fixture 执行 deterministic extraction + direct JSON parse +
  frozen Schema validation；
- 形成 offline diagnostic result、limitations 和下一步 recommendation boundary。

Synthetic fixture 不能证明 PRE-14 provider 实际返回了哪一种 envelope。

## 4. Required Diagnostic Questions

PRE-15 必须回答：

1. installed tool 的声明输出类型是否包含 `answer`？
2. caller 是否只检查了部分合法 envelope path？
3. 未检查的合法路径是否可能解释 PRE-14 的 extraction failure？
4. 在没有 raw response 的情况下，PRE-14 的精确 provider failure cause 是否仍为
   `UNKNOWN`？
5. future Qianfan confirmation 若获单独授权，应冻结哪个 extraction contract？

## 5. Success Criteria

必须同时满足：

```text
LIVE_MODEL_REQUESTS_EXECUTED=0
RAW_PRE14_PROVIDER_BODY_ACCESSED=false
DECLARED_TOOL_OUTPUT_CONTRACT_CAPTURED=true
EXTRACTION_PATH_CLASSIFICATION_DEFINED=true
SYNTHETIC_POSITIVE_AND_NEGATIVE_CASES_VALIDATED=true
PRE14_EXACT_PROVIDER_FAILURE_CAUSE_OVERSPECIFIED=false
```

成功只允许形成一个独立的 future one-request Qianfan confirmation recommendation。

## 6. Required Outputs

若未来获准执行，只允许形成：

- frozen PRE-15 offline diagnostic plan 与 Schema；
- authorization baseline receipt；
- declared wrapper contract record；
- synthetic wrapper extraction fixtures 与 Schema；
- deterministic offline diagnostic result 与 Schema；
- human-readable diagnostic report；
- execution receipt；
- path-scoped commit/push receipt。

## 7. Stop Conditions

- PRE-15 Decision、plan、Schema 或远端授权基线不存在；
- PRE-14 result digest 漂移；
- 需要 live model/provider request；
- 需要读取 secret、PRE-14 raw body、token usage 或隐藏推理；
- synthetic fixture 被抬升为 PRE-14 provider evidence；
- JSON repair、候选 review、validity、counting、Gate 或商业效果被请求。

## 8. False Effects

```text
PRE_15_DECIDED=false
OFFLINE_DIAGNOSTIC_AUTHORIZED=false
LIVE_MODEL_REQUESTS_AUTHORIZED=false
PRE14_QIANFAN_EXACT_FAILURE_CAUSE_PROVEN=false
QIANFAN_PROVIDER_SCHEMA_CONFIRMATION_PASS=false
PROVIDER_SCHEMA_CONFIRMATION_PASS=false
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

Offline wrapper diagnosis 不等于 provider success；synthetic extraction PASS 不等于 PRE-14
response 可恢复或 candidate review 完成。
