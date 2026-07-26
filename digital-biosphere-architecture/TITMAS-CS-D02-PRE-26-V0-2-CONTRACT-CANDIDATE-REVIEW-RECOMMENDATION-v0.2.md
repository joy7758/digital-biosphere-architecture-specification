---
document_id: DBA-TITMAS-CS-D02-PRE-26-V0-2-CONTRACT-CANDIDATE-REVIEW-RECOMMENDATION-0.2
title: TITMAS CS-D02 PRE-26 v0.2 Contract Candidate Review Recommendation v0.2
title_zh: TITMAS CS-D02 PRE-26 v0.2 契约候选审查建议 v0.2
version: 0.2.0
status: exact-recommendation-revised-provider-path-not-decided
maturity: Development
decision_reference: CS-D02-PRE-26
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
supersedes: TITMAS-CS-D02-PRE-26-V0-2-CONTRACT-CANDIDATE-REVIEW-RECOMMENDATION-v0.1.md
live_model_request_authorized: false
contract_adoption_authorized: false
implementation_authorized: false
---

# TITMAS CS-D02 PRE-26 v0.2 Contract Candidate Review Recommendation v0.2

## 1. Why v0.2 Exists

PRE-26 recommendation v0.1 建议：

```text
KIMI_PROVIDER_PATH=BAIDU_QIANFAN_EXACT_MODEL_TOOL
GLM_PROVIDER_PATH=BAIDU_QIANFAN_EXACT_MODEL_TOOL
```

在形成 Decision 前的只读 tool-surface discovery 中，只发现 exact `kimi-k2.6`
`kimi_chat`，没有发现可调用的 `glm-5.2` exact-model tool。因此 v0.1 的必要前置条件不能
得到直接证据：

```text
PRE26_V0_1_EXACT_KIMI_TOOL_DISCOVERED=true
PRE26_V0_1_EXACT_GLM_TOOL_DISCOVERED=false
PRE26_V0_1_STANDING_DIRECTIVE_APPLICABLE=false
PRE26_V0_1_DECISION_RECORDED=false
PRE26_V0_1_EXECUTION_AUTHORIZED=false
```

本修订不临时替换 GLM，也不把一个不可调用表面写成已存在能力。它把两个 session 统一
绑定到同一公开、OpenAI-compatible Qianfan direct chat endpoint，并要求执行计划在任何
请求前冻结 payload、query hash、response Schema、model binding 和零持久化规则。

v0.1 保留为历史，不删除、不改写。

## 2. Revised Recommendation

```text
RECOMMENDED_OPTION=AUTHORIZE_EXACT_TWO_SESSION_PRE25_V0_2_CONTRACT_CANDIDATE_REVIEW_VIA_QIANFAN_DIRECT_CHAT_ONLY
PRIMARY_REPOSITORY=digital-biosphere-architecture
ENDPOINT=https://qianfan.baidubce.com/v2/chat/completions
CREDENTIAL_SOURCE=QIANFAN_API_KEY_ENVIRONMENT_ONLY
REVIEWER_SESSIONS_MAX=2
KIMI_K2_6_REQUESTS_MAX=1
GLM_5_2_REQUESTS_MAX=1
TOTAL_PROVIDER_NETWORK_REQUESTS_MAX=2
RETRY_ATTEMPTS_MAX=0
FALLBACK_ATTEMPTS_MAX=0
MODEL_SUBSTITUTIONS_MAX=0
JSON_REPAIR_ATTEMPTS_MAX=0
WEB_SEARCH_REQUESTS_MAX=0
REVIEWER_TOOL_CALLS_MAX=0
CONTRACT_ADOPTION_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
LIVE_RERUN_AUTHORIZED=false
```

建议对 PRE-25 的 v0.2 contract candidates 执行两个相互独立、只读、结构化的 Agent
review session。两个请求只用于审查候选是否足以进入后续 Human Formal Adoption
Decision review；不采纳契约、不创建实现、不验证 provider runtime。

## 3. Pre-development Agent Recommendation Gate

```text
V0_2_CONTRACT_CANDIDATES=NOT_RECOMMENDED_FOR_IMPLEMENTATION_OR_PRODUCTION_USE
V0_2_BOUNDED_INDEPENDENT_REVIEW=RECOMMENDED
FORMAL_ADOPTION=CONDITIONALLY_RECOMMENDED_ONLY_AFTER_TWO_QUALIFYING_REVIEWS
```

不推荐立即实现或采纳：

1. PRE-25 只证明离线规则与 synthetic fixtures 一致；
2. 没有 qualifying independent review；
3. alias lifecycle 尚未经过独立治理审查；
4. 没有独立实现、provider runtime 或 portability evidence；
5. `VALID_PROBLEM_RECORDS=0` 且 `CS_G0_PASS=false`。

## 4. Frozen Source Evidence

PRE-25 result commit：

```text
3122832f5aa9b93a10f8cd069b7ee3e5855836e7
```

| artifact | SHA-256 |
|---|---|
| `offline-contract-revision-validation-result.v0.1.json` | `318a0b46b916898b6d534d56484db01d330b37e755492889f73358a3497fbb00` |
| `PRE-25-OFFLINE-CONTRACT-REVISION-RESULT-v0.1.md` | `2fa3770127829f16fd1acea96e9523753ee39b39b0e6af290e73ab6c5ec410ae` |
| `contract-revision-finding-triage.v0.1.json` | `26a17618ac500fbd2bfb68b87c5eaa73736d1f3089cccfe9249b57cb8bdb2adc` |
| `compact-review-cross-layer-invariants.v0.1.json` | `b7ea94eabee1fd29b7e9370f2caffccb16fe9b89faa7e86c1447d1566e4174ff` |
| `compact-review-response-extraction-contract.v0.2.json` | `a78c7d93cd6591aedc0dc124dacc07882ea0a4f513eea3da129cde2eb2b9ef1c` |
| `compact-review-response-extraction-contract.schema.v0.2.json` | `1d809e2df6237f2c6f5e3bbd498ca724b5af8616fbd58a1ad0a2052948eb843c` |
| `compact-review-model-binding-policy.v0.2.json` | `ee29fe66620b2cdb11d32dd7a0d772522b4100479b2915baf6e61aec18d3f7b9` |
| `compact-review-model-binding-policy.schema.v0.2.json` | `68091fe4f5f78fe1a3a2fcef68eeea1cde97f03396853c069a091333793d3420` |
| `compact-review-model-alias-record.schema.v0.1.json` | `48ca93223b8ee589e1d5fa9119b91c4a911365033353b7d577d409a6a16066f1` |
| `compact-review-contract-revision-fixtures.v0.1.json` | `0d0b8376a3aadee5f0b327e08f14a0c3f0059adfc45f0bc5a0c2e045f6434213` |
| `compact-review-contract-revision-fixtures.schema.v0.1.json` | `8aa6ee95fb13acf8b3b2f13179345ff313bd01161b0ad254773e7c745d30ce96` |

## 5. Exact Provider Contract

两个 session 使用相同 direct endpoint：

```text
POST https://qianfan.baidubce.com/v2/chat/completions
Authorization: Bearer ${QIANFAN_API_KEY}
Content-Type: application/json
Accept: application/json
```

请求 body 只能包含：

```json
{
  "model": "<exact requested model>",
  "messages": [
    {"role": "system", "content": "<frozen non-sensitive contract>"},
    {"role": "user", "content": "<frozen review query>"}
  ],
  "stream": false,
  "temperature": 0
}
```

禁止 tool、tool choice、web、file、image、customer data、personal data、private source code、
credential text 或 unpublished material。`QIANFAN_API_KEY` 只从进程环境读取，不进入
prompt、payload artifact、log、result、receipt、Git 或 error body。

执行时只允许从 provider envelope 内存读取：

- HTTP status；
- `choices[0].message.content`；
- returned model identifier（如 provider 返回）；
- sanitized error category；
- response byte count；
- raw envelope 的 one-way digest。

raw envelope、usage、hidden reasoning 和 provider error body 不持久化。

## 6. Exact Review Sessions

### Session A

```text
SESSION_ID=PRE26-KIMI-V0_2-CONTRACT-REVIEW
REQUESTED_MODEL=kimi-k2.6
REVIEWER_ROLE=INTEROPERABILITY_AND_FAILURE_SEMANTICS_REVIEWER
REQUESTS_MAX=1
MODEL_BINDING_REQUIREMENT=RETURNED_MODEL_MUST_EQUAL_REQUESTED_MODEL
```

### Session B

```text
SESSION_ID=PRE26-GLM-V0_2-CONTRACT-REVIEW
REQUESTED_MODEL=glm-5.2
REVIEWER_ROLE=GOVERNANCE_ALIAS_AND_VERSIONING_REVIEWER
REQUESTS_MAX=1
MODEL_BINDING_REQUIREMENT=RETURNED_MODEL_MUST_EQUAL_REQUESTED_MODEL
```

若 provider 不返回 model identifier、返回不同 identifier、拒绝精确 model、超时或失败，
session 必须 non-qualifying。不得通过 alias 推断、model substitution、retry 或 fallback
恢复。

## 7. Review Targets and Criteria

两个 reviewer 使用同一 hash-bound bundle：

1. extraction contract v0.2；
2. model-binding policy v0.2；
3. alias record Schema；
4. cross-layer invariants；
5. deterministic fixtures；
6. PRE-24 finding triage 与 PRE-25 result。

必须逐项返回 `PASS | FAIL | UNKNOWN`：

1. `CONFLICT_IS_TERMINAL_NON_QUALIFYING`；
2. `CALLER_STOP_AND_FAILURE_PRESERVATION`；
3. `SEMANTIC_AND_MODEL_DIMENSIONS_SEPARATED`；
4. `CONTENT_PASS_CANNOT_OVERRIDE_MODEL_FAILURE`；
5. `ALIAS_REQUIRES_EXPLICIT_ADOPTION_DECISION`；
6. `ALIAS_SOURCE_VERSION_SCOPE_EXACTNESS`；
7. `ALIAS_EFFECTIVE_EXPIRY_SEMANTICS`；
8. `REVOKED_CONFLICTED_INVALID_ALIAS_FAIL_CLOSED`；
9. `V0_1_HISTORY_AND_V0_2_VERSION_BOUNDARY`；
10. `PROVIDER_NEUTRALITY_AND_PORTABILITY`；
11. `DETERMINISTIC_TESTABILITY`；
12. `AUTHORITY_PERMISSION_TRUTH_NON_ELEVATION`。

每项 `FAIL` 或 `UNKNOWN` 必须给出 target、JSON Pointer/section、severity、reason 和
required change。Reviewer finding 只作为 advisory input，不产生 normative effect。

## 8. Qualification and Composite Gate

单个 session qualifying 必须全部满足：

```text
EXACT_QUERY_HASH_MATCH=true
HTTP_STATUS_200=true
DIRECT_JSON_PARSE_PASS=true
FROZEN_RESPONSE_SCHEMA_PASS=true
RETURNED_MODEL_PRESENT=true
RETURNED_MODEL_EQUALS_REQUESTED_MODEL=true
BOUNDARY_ACKNOWLEDGEMENTS_PASS=true
TERMINAL_EXTRACTION_FAILURE=false
```

只有两个 session 均 qualifying，并且：

```text
BLOCKING_FINDINGS=0
MAJOR_FINDINGS=0
BOTH_RECOMMENDATIONS=ACCEPT_FOR_FORMAL_ADOPTION_DECISION
BOUNDARY_SAFETY_FAILURES=0
```

才可设置：

```text
FORMAL_ADOPTION_DECISION_REVIEW_READY=true
```

该状态不等于 Adoption。任一 session 不 qualifying、结论冲突或有 blocking/major finding
时，composite result 必须失败关闭并保留所有失败。

## 9. Required Future Decision Outputs

若后续独立 Decision 采用本建议，只可授权：

1. review plan 与 input manifest；
2. exact provider contract、request manifest 与 rendered query hashes；
3. review response Schema 与正负 fixtures；
4. session result Schema；
5. 两份 sanitized session result；
6. composite validation result；
7. execution receipt、result report 和 cockpit synchronization。

这些是 review-governance artifacts，不是 reusable Adapter implementation 或产品代码。

## 10. Preconditions

1. v0.2 recommendation 与 PRE-25 result 在目标远端；
2. 上述 11 个 source hash 全部匹配；
3. standing directive active；
4. `QIANFAN_API_KEY` 只验证“存在且非空”，不读取、输出或持久化；
5. endpoint、model、request body、response Schema、query bytes/hash 和 request cap 在独立
   PRE-26 Decision 前冻结；
6. Decision、plan、input manifest 和 Schema 在任何 provider request 前提交并远端验证；
7. live/provider request accounting 在执行前为 0。

provider/model 当前可用性不由静态文件推定；它只由未来授权的单次请求观察，并且失败
关闭。

## 11. Stop Conditions

- 任一 source/hash 漂移；
- credential 缺失，或 credential 被输出／持久化；
- endpoint、model、query、Schema 或 payload 不匹配冻结内容；
- query 超出未来冻结 cap；
- reviewer 获得 tool、web、file、Runtime 或外部操作能力；
- retry、fallback、model substitution、alias inference、JSON repair 或 semantic rewrite；
- raw response、usage、credential、secret、hidden reasoning 或 error body 持久化；
- finding 被删除或自动写成 adopted fact；
- review 被升级为 Adoption、Implementation、Provider Support、Conformance、
  Certification、Release、customer proof 或 `CS-G0 PASS`。

## 12. Success Conditions

```text
INPUT_HASHES_MATCH=ALL
RESPONSE_FIXTURE_EXPECTATIONS_MATCH=ALL
QUERY_BINDINGS_MATCH=2/2
AUTHORIZED_REVIEW_SESSIONS=2
EXECUTED_REVIEW_SESSIONS=2
TOTAL_PROVIDER_NETWORK_REQUESTS_EXECUTED=2
QUALIFYING_REVIEWS=RESULT_DEPENDENT
RETRY_ATTEMPTS=0
FALLBACK_ATTEMPTS=0
MODEL_SUBSTITUTIONS=0
JSON_REPAIR_ATTEMPTS=0
BOUNDARY_SAFETY_FAILURES=0
FORMAL_ADOPTION_DECISION_REVIEW_READY=RESULT_DEPENDENT
CONTRACT_CANDIDATES_ADOPTED=false
IMPLEMENTATION_CREATED=false
LIVE_RERUN_READY=false
```

## 13. False Effects

```text
AUTHORITY_CHANGED=false
OWNERSHIP_CHANGED=false
PRE24_RESULT_CHANGED=false
PRE25_RESULT_CHANGED=false
PRE26_V0_1_HISTORY_CHANGED=false
V0_1_CONTRACTS_CHANGED=false
V0_2_CONTRACT_CANDIDATES_ADOPTED=false
ALIAS_RECORD_ADOPTED=false
ADAPTER_IMPLEMENTATION_CREATED=false
PROFILE_REVIEW_COMPLETED=false
PROFILE_ADOPTED=false
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

## 14. Standing Directive Eligibility

本建议只有一个 exact action：两个固定模型通过同一 allowlisted endpoint 各执行一次只读
结构化审查。Inputs、outputs、request body、network cap、model binding、zero-retry、
stop conditions 和 false effects 已明确。

```text
STANDING_DIRECTIVE_REFERENCE=TITMAS-CS-STANDING-001
STANDING_DIRECTIVE_ELIGIBLE_CANDIDATE=true
AT_RECOMMENDATION_TIME_PRE26_DECIDED=false
AT_RECOMMENDATION_TIME_LIVE_REVIEW_AUTHORIZED=false
AT_RECOMMENDATION_TIME_LIVE_MODEL_REQUESTS_EXECUTED=0
AT_RECOMMENDATION_TIME_CONTRACT_CANDIDATES_ADOPTED=false
```
