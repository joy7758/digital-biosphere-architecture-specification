---
document_id: DBA-TITMAS-CS-D02-PRE-16-QIANFAN-RECONFIRMATION-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-16 Qianfan Reconfirmation Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-16 Qianfan 单次重新确认建议 v0.1
version: 0.1.0
status: recommendation-prepared-not-decided
maturity: Development
document_type: bounded-qianfan-reconfirmation-recommendation
decision_candidate_id: CS-D02-PRE-16
owner_ref: zhangbin
observed_on: 2026-07-26
authority_effect: none
---

# TITMAS CS-D02 PRE-16 Qianfan Reconfirmation Recommendation v0.1

## 1. Recommendation

建议未来单独决定：

```text
RECOMMENDED_OPTION=AUTHORIZE_ONE_QIANFAN_RECONFIRMATION_AND_COMPOSITE_GATE_ONLY
QIANFAN_LIVE_MODEL_REQUESTS_MAX=1
DEEPSEEK_NEW_REQUESTS_MAX=0
TOTAL_NEW_LIVE_MODEL_REQUESTS_MAX=1
RETRY_MAX=0
FALLBACK_MAX=0
JSON_REPAIR_MAX=0
AT_RECOMMENDATION_TIME_PRE_16_DECIDED=false
AT_RECOMMENDATION_TIME_LIVE_MODEL_REQUEST_AUTHORIZED=false
```

PRE-16 只允许使用 PRE-15 定义的 ordered extraction contract 对 Qianfan/Kimi 执行一次新
确认，并与 PRE-14 已冻结的 DeepSeek 合格观察形成一个新的 composite provider gate。

PRE-16 不是重开或改写 PRE-14。PRE-14 继续保持 fail closed。

## 2. Frozen Evidence Basis

```text
PRE14_RESULT_COMMIT=ea85ece26b7dfb75ad84b0de3a7ddf0ca7f2738a
PRE14_DEEPSEEK_FULL_SCHEMA_PASS=true
PRE14_DEEPSEEK_SANITIZED_RESPONSE_CANONICAL_SHA256=9fca2ee86499e5ad85b552cc2d17a2dda1fde4239a9ec39336ada1e11a1b97c1
PRE15_RESULT_COMMIT=84718024ce55164f83c3bf6cf966e2d182754deb
PRE15_OFFLINE_DIAGNOSTIC_SHA256=9d442d8b3ec6b6cd2bfbdba0c55ab3bd0336f9fe6799bdda480b007fca97a830
PRE15_EXTRACTION_COVERAGE_GAP_CONFIRMED=true
```

Qianfan 请求继续使用 PRE-13 `SOURCE_QUALIFICATION_REVIEWER` rendered bytes：

```text
QIANFAN_ROLE_SPECIFIC_REQUEST_SHA256=1e0f4d0efbccf31a4fbbc1d4cffab9f1bc4308acee3e8cb8324c0769e5ed4638
RESPONSE_SCHEMA_SHA256=0f3df0688993fe300bae1f8d2c1cb67c0fd31fecbdabcbb89d5a1819c803ccd8
```

## 3. Exact New Session

| Session | Provider/model | Reviewer role | New request max |
|---|---|---|---:|
| `QF-KIMI-SCHEMA-RECONFIRM-PRE16-P1` | Qianfan / `kimi-k2.6` | `SOURCE_QUALIFICATION_REVIEWER` | 1 |

请求只使用 `query`。禁止修改 frozen prompt、source pack、candidate set、response Schema、
role 或 model。

## 4. Ordered Extraction Contract

按顺序检查：

1. `structuredContent.answer`；
2. direct `answer`；
3. `content[0].text` 解析为 JSON wrapper 后的 `answer`；
4. 仅对 `mcp__kimi_qianfan__kimi_chat`，使用 plain `content[0].text` answer。

如果多个路径存在非相同 answer，立即失败关闭。提取后只允许 direct JSON parse 和完整冻结
Schema validation，不允许 fence stripping、substring extraction 或 JSON repair。

## 5. Composite Gate

新 gate 的两个 provider evidence inputs 是：

- PRE-16 Qianfan sanitized Schema-conformant response；
- PRE-14 DeepSeek frozen sanitized Schema-conformant response。

必须同时满足：

```text
NEW_QIANFAN_REQUESTS_EXECUTED_REQUIRED=1
QIANFAN_SCHEMA_CONFORMANT_REQUIRED=true
FROZEN_DEEPSEEK_SCHEMA_CONFORMANT_REQUIRED=true
COMPOSITE_PROVIDERS_WITH_SCHEMA_CONFORMANT_RESPONSE_REQUIRED=2
QIANFAN_CANDIDATE_IDS_COVERED_REQUIRED=4
DEEPSEEK_CANDIDATE_IDS_COVERED_REQUIRED=4
COMPOSITE_BOUNDARY_FAILURES_MAX=0
FROZEN_INPUT_DIGESTS_MATCH_REQUIRED=true
```

任一条件失败，PRE-16 即失败关闭。

即使 composite gate 通过，也只允许：

```text
PREPARE_SEPARATE_FULL_CANDIDATE_REVIEW_RERUN_RECOMMENDATION_ONLY
```

## 6. Required Controls

- 只发送冻结的 public-safe source pack；
- 不浏览、不调用 reviewer tools、不搜索或收集新来源；
- 不读取、展示或持久化 API key；
- 不保存 raw provider body、token usage 或隐藏推理；
- 只保存 sanitized Schema-conformant response 或分类失败状态；
- 不 retry、fallback、JSON repair、fence stripping 或 substring extraction；
- 每个 response 覆盖 `PFPC-001`—`PFPC-004` 且 `counting_effect=false`；
- 所有 `boundary_answers` 必须为 false。

## 7. Stop Conditions

- PRE-16 Decision、plan、Schema 或远端授权基线不存在；
- PRE-13/PRE-14/PRE-15 frozen digest 漂移；
- model、role、endpoint、request bytes、extraction order 或 request cap 漂移；
- 多路径 answer 冲突；
- retry、fallback、tool use、JSON repair 或非 direct parse 被请求；
- secret、个人/客户数据或 raw provider body 将被记录；
- 自动 candidate validity、counting、Gate、市场、客户或商业效果被请求。

## 8. False Effects

```text
PRE_16_DECIDED=false
LIVE_MODEL_REQUEST_AUTHORIZED=false
QIANFAN_RECONFIRMATION_COMPLETED=false
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
