---
document_id: DBA-TITMAS-CS-D02-PRE-18-PROVIDER-ADAPTER-CONFORMANCE-PROFILE-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-18 Provider Adapter Conformance Profile Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-18 Provider Adapter 符合性画像建议 v0.1
version: 0.1.0
status: recommendation-prepared-not-decided
maturity: Development
document_type: provider-neutral-adapter-conformance-profile-recommendation
decision_candidate_id: CS-D02-PRE-18
owner_ref: zhangbin
observed_on: 2026-07-26
authority_effect: none
---

# TITMAS CS-D02 PRE-18 Provider Adapter Conformance Profile Recommendation v0.1

## 1. Recommendation

建议未来单独决定：

```text
RECOMMENDED_OPTION=AUTHORIZE_PROVIDER_NEUTRAL_AGENT_REVIEW_ADAPTER_CONFORMANCE_PROFILE_CANDIDATE_ONLY
LIVE_MODEL_REQUESTS_MAX=0
PROVIDER_NETWORK_REQUESTS_MAX=0
REFERENCE_PROVIDERS=QIANFAN_AND_DEEPSEEK
REFERENCE_PROVIDER_ADOPTION_EFFECT=false
IMPLEMENTATION_AUTHORIZED=false
AT_RECOMMENDATION_TIME_PRE_18_DECIDED=false
```

PRE-18 只建议形成 provider-neutral（供应商中立）的 Agent Review Adapter Conformance
Profile candidate、Schema 和离线 conformance case catalog。它不实现 Adapter，不调用
provider，也不把 Qianfan 或 DeepSeek 声明为 TITMAS adopted provider。

## 2. Frozen Evidence Basis

```text
PRE17_RESULT_COMMIT=9acb37691f7b8ca58876a274dec6212fb874fbdb
PRE17_TRANSPORT_SEMANTIC_CROSSWALK_SHA256=5a73332191c1a12e293bf64ca42bf2cb5e4d28fb6eff318f6af2ca487fde750a
PRE17_EXTRACTION_CONTRACT_CANDIDATE_SHA256=6cffcecc3158ec462be1c0be69a4ed861ad05445782fef5f78a8107f32f27cef
PRE17_SHAPE_DESCRIPTOR_CONTRACT_SHA256=ace5622502ab29f6f1635f2d2b1968706efa29f8cfdf060224ab76e5dcc138eb
PRE17_OFFLINE_RESULT_SHA256=c0b5af2790430e5bc537c7dd25608f76165a8135672f7b90d73b3b6cabcb5eb5
PRE17_EXECUTION_RECEIPT_SHA256=284cd1881e1167520930465e3673de9060558b70164395b2f4ab4f18140c7ae4
PRE17_SYNTHETIC_CASES_MATCHED=13/13
PRE17_PROVIDER_RUNTIME_VALIDATION_PASS=false
```

PRE-14 至 PRE-17 表明：provider transport success、JSON parse 和 model output 不能直接等于
规范 reviewer response。标准需要一个独立 Adapter conformance boundary。

## 3. Proposed Profile Boundary

Profile candidate 应定义：

### 3.1 Normalized Request Descriptor

- `adapter_request_id`；
- `provider_ref` 与 `model_ref`；
- `reviewer_role`；
- `prompt_sha256`；
- `response_schema_sha256`；
- `request_started_at`；
- retry/fallback/tool policy；
- data classification。

Descriptor 只描述请求契约，不保存 secret。

### 3.2 Normalized Result Descriptor

- `transport_status`；
- `transport_status_code`（如适用）；
- `semantic_answer_status`；
- `extraction_path_id`；
- privacy-preserving shape descriptor；
- `direct_json_parse_status`；
- `full_schema_status`；
- sanitized conformant response reference（仅通过 Schema 时）；
- `failure_class`；
- retry/fallback/request accounting。

### 3.3 Required Failure Classes

至少包括：

```text
TRANSPORT_ERROR
PROVIDER_ERROR
NO_EXTRACTABLE_ANSWER
UNKNOWN_RUNTIME_ENVELOPE
UNDECLARED_NESTING
AMBIGUOUS_NON_IDENTICAL_ANSWERS
DIRECT_JSON_PARSE_FAILED
FULL_SCHEMA_VALIDATION_FAILED
POLICY_VIOLATION
```

失败必须保留，不能静默 retry、fallback、repair 或改写。

## 4. Conformance Case Catalog

Profile candidate 至少应包含：

1. direct structured answer；
2. direct semantic answer；
3. approved one-level serialized wrapper；
4. direct reviewer object；
5. unknown JSON transport envelope；
6. missing / wrong-type answer；
7. non-JSON answer；
8. full Schema mismatch；
9. identical candidate deduplication；
10. non-identical ambiguity failure；
11. undeclared second-level nesting；
12. provider transport error；
13. provider-declared error；
14. prohibited retry/fallback/repair；
15. raw/secret/usage persistence rejection；
16. candidate validity/counting semantic non-elevation。

所有 case 初始状态必须为 `NOT_EXECUTED`。Catalog 定义不等于 conformance execution。

## 5. Reference Provider Use

Qianfan/Kimi 与 DeepSeek 只允许作为历史 reference fixture source：

- Qianfan 提供 transport/semantic wrapper gap；
- DeepSeek 提供 direct HTTP + Schema-conformant sanitized result 示例；
- 两者均不自动成为支持列表、合作伙伴、认证对象或 adopted provider；
- 历史调用结果不能替代未来 exact Adapter implementation 的 conformance execution。

## 6. Required Outputs

若未来获准，只允许形成：

- Provider Adapter Conformance Profile candidate；
- machine-readable Profile contract 与 Schema；
- normalized request/result descriptor schemas；
- provider-neutral failure taxonomy；
- 16+ case catalog 与 fixture requirements；
- claim/non-elevation matrix；
- offline schema rehearsal result；
- Decision、authorization receipt、result report 和 execution receipt；
- path-scoped commit/push。

不创建 Adapter code、API endpoint、Runtime、provider account 或 model request。

## 7. Success Criteria

```text
PROFILE_PROVIDER_NEUTRAL=true
TRANSPORT_NE_SEMANTIC_ANSWER=true
TRANSPORT_SUCCESS_NE_SCHEMA_CONFORMANCE=true
SCHEMA_CONFORMANCE_NE_CANDIDATE_VALIDITY=true
FAILURE_TAXONOMY_DEFINED=true
CONFORMANCE_CASES_DEFINED_GE_16=true
CONFORMANCE_CASES_EXECUTED=0
REFERENCE_PROVIDER_ADOPTION_EFFECT=false
LIVE_MODEL_REQUESTS_EXECUTED=0
IMPLEMENTATION_EFFECT=false
```

成功只允许形成一个后续 profile adoption review recommendation；不能自动采纳为 normative
Profile、实现 Adapter 或执行 conformance。

## 8. Stop Conditions

- PRE-18 Decision、plan、Schema 或远端授权基线不存在；
- PRE-17 frozen digest 漂移；
- 需要 live provider request、secret、raw response 或私有数据；
- Profile 引入 provider-specific required field；
- transport success 被升级为 semantic/schema success；
- Schema PASS 被升级为 candidate validity、counting、`CS-G0` 或市场证明；
- 要求实现、部署、外联、Offering、认证或发布。

## 9. False Effects

```text
PRE_18_DECIDED=false
PROFILE_CANDIDATE_AUTHORIZED=false
PROFILE_CANDIDATE_CREATED=false
PROFILE_ADOPTED=false
ADAPTER_IMPLEMENTATION_AUTHORIZED=false
ADAPTER_IMPLEMENTATION_CREATED=false
LIVE_MODEL_REQUESTS_AUTHORIZED=false
PROVIDER_ADOPTION=false
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
