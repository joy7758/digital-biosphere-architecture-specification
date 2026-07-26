---
document_id: DBA-TITMAS-CS-D02-PRE-28-HANDOFF-BOUND-CONTRACT-CANDIDATE-REVIEW-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-28 Handoff-bound Contract Candidate Review Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-28 交接绑定契约候选审查建议 v0.1
version: 0.1.0
status: exact-handoff-bound-review-recommendation-not-decided
maturity: Development
decision_reference: CS-D02-PRE-28
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
live_model_request_authorized: false
contract_adoption_authorized: false
implementation_authorized: false
---

# TITMAS CS-D02 PRE-28 Handoff-bound Contract Candidate Review Recommendation v0.1

## 1. Why PRE-28 Exists

PRE-26 没有返回可验证的 sanitized session result，请求预算已经关闭。PRE-27 随后用 11 个
synthetic fixtures 验证了独立于 stdout 的 temporary sink handoff：

```text
PRE27_FIXTURE_EXPECTATIONS_MATCH=11/11
PRE27_STDOUT_SUPPRESSED_VALID_SINK_RECOVERED=true
PRE27_HANDOFF_CONTRACT_CANDIDATE_READY=true
PRE27_PROVIDER_REVIEW_RERUN_READY=false
PRE27_HANDOFF_CONTRACT_ADOPTED=false
PRE27_IMPLEMENTATION_CREATED=false
```

PRE-27 证明的是 offline handoff behavior，不是 provider correctness。若要获得两个独立
Agent reviewer 的实际 advisory input，必须另建新的 provider review Decision，并把每个
session 的 sanitized result 先提交到独立临时 sink，再由外层 consumer 读取。

## 2. Agent Recommendation Gate

如果潜在 Agent 客户现在询问是否应采用 PRE-25 v0.2 contracts：

```text
RECOMMEND_CONTRACT_IMPLEMENTATION_OR_PRODUCTION_USE=NO
REASON=ZERO_QUALIFYING_EXTERNAL_AGENT_REVIEWS
RECOMMEND_EXACT_HANDOFF_BOUND_TWO_SESSION_REVIEW=YES
RECOMMEND_FORMAL_ADOPTION_NOW=NO
```

不推荐立即采用的原因：

1. PRE-25 仍只是 offline candidate；
2. PRE-26 结果不可验证，qualifying review 为 0；
3. PRE-27 只验证 synthetic handoff；
4. provider/model availability、exact binding 和审查内容仍未知；
5. `VALID_PROBLEM_RECORDS=0` 且 `CS_G0_PASS=false`。

## 3. Exact Recommendation

```text
RECOMMENDED_OPTION=AUTHORIZE_EXACT_TWO_SESSION_PRE25_V0_2_CONTRACT_CANDIDATE_REVIEW_WITH_SANITIZED_SINK_HANDOFF_ONLY
PRIMARY_REPOSITORY=digital-biosphere-architecture
ENDPOINT=https://qianfan.baidubce.com/v2/chat/completions
REVIEWER_SESSIONS_MAX=2
KIMI_K2_6_REQUESTS_MAX=1
GLM_5_2_REQUESTS_MAX=1
TOTAL_PROVIDER_NETWORK_REQUESTS_MAX=2
RETRY_ATTEMPTS_MAX=0
FALLBACK_ATTEMPTS_MAX=0
MODEL_SUBSTITUTIONS_MAX=0
ALIAS_INFERENCE_ATTEMPTS_MAX=0
JSON_REPAIR_ATTEMPTS_MAX=0
WEB_SEARCH_REQUESTS_MAX=0
REVIEWER_TOOL_CALLS_MAX=0
CONTRACT_ADOPTION_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
```

两个 session 沿用 PRE-26 冻结 query、request payload、response Schema 和 exact-model
binding，但改变 handoff：

```text
PROCESS_STDOUT_CANONICAL=false
SANITIZED_TEMPORARY_SINK_CANONICAL=true
SESSION_RESULT_SINKS_REQUIRED=2
RAW_ENVELOPE_SINKS_ALLOWED=0
```

## 4. Frozen Session Contract

### Session A

```text
SESSION_ID=PRE28-KIMI-V0_2-CONTRACT-REVIEW
REQUESTED_MODEL=kimi-k2.6
REVIEWER_ROLE=INTEROPERABILITY_AND_FAILURE_SEMANTICS_REVIEWER
REQUESTS_MAX=1
```

### Session B

```text
SESSION_ID=PRE28-GLM-V0_2-CONTRACT-REVIEW
REQUESTED_MODEL=glm-5.2
REVIEWER_ROLE=GOVERNANCE_ALIAS_AND_VERSIONING_REVIEWER
REQUESTS_MAX=1
```

两个请求使用同一 endpoint 与 PRE-26 request manifest。任一 returned model 缺失或不等于
requested model、HTTP non-200、direct JSON parse failure、response Schema failure 或
boundary acknowledgement failure 均使对应 session non-qualifying。

## 5. Sanitized Sink Handoff

未来 Decision 必须在任何 provider request 前冻结：

- 一个全新 `0700` temporary root；
- 两个互不相同、预先不存在、非 symlink 的 exact committed target；
- 一个 execution control receipt target；
- target path、parent device/inode、mode 和 ownership 的 preflight receipt；
- 每个 payload/query hash；
- session result Schema、response Schema 和 handoff contract hash。

caller 在内存中读取 provider envelope，只提取：

- HTTP status；
- `choices[0].message.content`；
- returned model；
- response byte count；
- raw envelope one-way digest；
- sanitized failure category。

随后构造 session result，Schema-valid 后按
`write exclusive staging -> fsync -> atomic rename -> parent fsync` 提交。raw envelope、
usage、credential、hidden reasoning 和 provider error body 不进入 sink。

即使 session non-qualifying，也必须写入一个 Schema-valid sanitized failure result。若
session result 无法提交，整个 PRE-28 composite 失败关闭，且不重试 provider。

## 6. Composite Gate

只有两个 session 均满足：

```text
SANITIZED_SINK_COMMITTED=true
SESSION_RESULT_SCHEMA_PASS=true
EXACT_QUERY_HASH_MATCH=true
HTTP_STATUS_200=true
DIRECT_JSON_PARSE_PASS=true
FROZEN_RESPONSE_SCHEMA_PASS=true
RETURNED_MODEL_PRESENT=true
RETURNED_MODEL_EQUALS_REQUESTED_MODEL=true
BOUNDARY_ACKNOWLEDGEMENTS_PASS=true
QUALIFYING=true
```

并且：

```text
BLOCKING_FINDINGS=0
MAJOR_FINDINGS=0
BOTH_RECOMMENDATIONS=ACCEPT_FOR_FORMAL_ADOPTION_DECISION
BOUNDARY_SAFETY_FAILURES=0
```

才可设置 `FORMAL_ADOPTION_DECISION_REVIEW_READY=true`。该状态仍不是 Adoption。

## 7. Frozen Sources

| artifact | SHA-256 |
|---|---|
| `sanitized-result-handoff-diagnostic-validation-result.v0.1.json` | `f9d8b98dd6eef26e4069ee31f0114f0fee3a996587cfcd84ed7a24affa9ec871` |
| `sanitized-result-handoff-diagnostic-execution-receipt.v0.1.json` | `3fb5e3e23a733b2c2d88a9528fb0493a7c8f6bdd20ff3875062b49f35c8a33aa` |
| `PRE-27-SANITIZED-RESULT-HANDOFF-DIAGNOSTIC-RESULT-v0.1.md` | `774701b6302ef95b4b5365d5f4a8f89f024e39302a40c3cfd7df12bc518c8861` |
| `sanitized-result-handoff-contract.v0.1.json` | `0d30e8560dc2850e36d41004ebd059863337d2e242837139c58080662d989aa4` |
| `contract-v0-2-candidate-review-input-manifest.v0.1.json` | `f52d751a19f01df5472185c549846a26233670d9c38bc2d5faec4052e5d38c51` |
| `contract-v0-2-candidate-review-request-manifest.v0.1.json` | `fc8a7e1d53224491829b04011a6d298576d25e8c8df2a5e0ab3f54c3f4d2f2ca` |
| `contract-v0-2-candidate-review-response.schema.v0.1.json` | `de01e484b31a315ec6c46065a6937d38debaea1a9eafbf98a463c6eb69e94e72` |
| `contract-v0-2-candidate-review-session-result.schema.v0.1.json` | `dde73eb0c1a5fbacc1abb47375745cd5f881b9022416701f53c0a9de88b86116` |

## 8. Preconditions

1. 上述八个 source hash 全部匹配并在目标远端；
2. standing directive active；
3. `QIANFAN_API_KEY` 只验证存在且非空，不输出或持久化；
4. PRE-28 Decision、exact temporary targets、plan、manifest、Schema 和 authorization
   receipt 在任何 provider request 前提交并远端验证；
5. PRE-28 request accounting 为 0；
6. PRE-26 request budget 保持关闭，不将 PRE-28 写成 PRE-26 retry；
7. provider/model current availability 只由新授权的一次请求观察。

## 9. Stop Conditions

- source/hash、query、payload、Schema 或 endpoint 漂移；
- temporary target 预先存在、为 symlink、权限不符或无法原子提交；
- credential、raw envelope、usage、hidden reasoning 或 error body 持久化；
- retry、fallback、model substitution、alias inference、JSON repair 或 semantic rewrite；
- sink 缺失／空／partial／digest mismatch／Schema invalid；
- finding 删除或审查被抬升为 Adoption、implementation、provider support、conformance、
  certification、release、market/customer proof 或 `CS-G0 PASS`。

## 10. Success and False Effects

```text
SOURCE_HASHES_MATCH=8/8
AUTHORIZED_REVIEW_SESSIONS=2
SANITIZED_SESSION_SINKS_COMMITTED=2
TOTAL_PROVIDER_NETWORK_REQUESTS_EXECUTED=2
QUALIFYING_REVIEWS=RESULT_DEPENDENT
RETRY_ATTEMPTS=0
FALLBACK_ATTEMPTS=0
MODEL_SUBSTITUTIONS=0
JSON_REPAIR_ATTEMPTS=0
FORMAL_ADOPTION_DECISION_REVIEW_READY=RESULT_DEPENDENT

PRE26_RESULT_CHANGED=false
PRE26_REQUEST_BUDGET_REOPENED=false
HANDOFF_CONTRACT_ADOPTED=false
V0_2_CONTRACT_CANDIDATES_ADOPTED=false
ALIAS_RECORD_ADOPTED=false
ADAPTER_IMPLEMENTATION_CREATED=false
PROVIDER_SUPPORTED=false
CONFORMANCE_EXECUTED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
IMPLEMENTATION_AUTHORIZED=false
EXTERNAL_OUTREACH_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

## 11. Standing Directive Eligibility

本建议只有一个 exact action；provider、model、request cap、query/payload、sink handoff、
stop conditions 和 false effects 已明确。

```text
STANDING_DIRECTIVE_REFERENCE=TITMAS-CS-STANDING-001
STANDING_DIRECTIVE_ELIGIBLE_CANDIDATE=true
AT_RECOMMENDATION_TIME_PRE28_DECIDED=false
AT_RECOMMENDATION_TIME_LIVE_REVIEW_AUTHORIZED=false
AT_RECOMMENDATION_TIME_LIVE_MODEL_REQUESTS_EXECUTED=0
AT_RECOMMENDATION_TIME_CONTRACT_CANDIDATES_ADOPTED=false
```
