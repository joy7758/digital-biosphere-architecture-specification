---
document_id: DBA-TITMAS-CS-D02-PRE-26-V0-2-CONTRACT-CANDIDATE-REVIEW-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-26 v0.2 Contract Candidate Review Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-26 v0.2 契约候选审查建议 v0.1
version: 0.1.0
status: exact-recommendation-prepared-not-decided
maturity: Development
decision_reference: CS-D02-PRE-26
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
live_model_request_authorized: false
contract_adoption_authorized: false
implementation_authorized: false
---

# TITMAS CS-D02 PRE-26 v0.2 Contract Candidate Review Recommendation v0.1

## 1. Recommendation

```text
RECOMMENDED_OPTION=AUTHORIZE_EXACT_TWO_SESSION_PRE25_V0_2_CONTRACT_CANDIDATE_REVIEW_ONLY
PRIMARY_REPOSITORY=digital-biosphere-architecture
REVIEWER_SESSIONS_MAX=2
KIMI_K2_6_REQUESTS_MAX=1
GLM_5_2_REQUESTS_MAX=1
RETRY_ATTEMPTS_MAX=0
FALLBACK_ATTEMPTS_MAX=0
JSON_REPAIR_ATTEMPTS_MAX=0
WEB_SEARCH_REQUESTS_MAX=0
REVIEWER_TOOL_CALLS_MAX=0
CONTRACT_ADOPTION_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
LIVE_RERUN_AUTHORIZED=false
```

建议对 PRE-25 产生的 v0.2 contract candidates 执行两个相互独立、只读、结构化的
Agent review session。审查只回答“候选是否足以进入后续 Human Formal Adoption
Decision review”，不采纳契约、不创建实现、不验证 provider runtime。

## 2. Evidence

PRE-25 远端结果：

```text
INPUT_HASHES_MATCHED=13/13
OUTPUT_BINDINGS_MATCHED=11/11
CANDIDATE_SCHEMAS_META_VALID=6/6
CANDIDATE_INSTANCES_SCHEMA_VALID=5/5
FIXTURE_EXPECTATIONS_MATCHED=10/10
V0_1_HISTORY_HASHES_MATCHED=5/5
V0_1_HISTORY_CHANGED=false
OFFLINE_REVISION_CANDIDATE_PASS=true
CONTRACT_CANDIDATES_ADOPTED=false
IMPLEMENTATION_CREATED=false
LIVE_RERUN_READY=false
```

远端 result commit：

```text
3122832f5aa9b93a10f8cd069b7ee3e5855836e7
```

冻结候选证据：

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

## 3. Pre-development Agent Recommendation Gate

如果潜在 Agent developer 询问是否应基于当前 v0.2 candidates 实现生产 Adapter：

```text
V0_2_CONTRACT_CANDIDATES=NOT_RECOMMENDED_FOR_IMPLEMENTATION_OR_PRODUCTION_USE
V0_2_BOUNDED_INDEPENDENT_REVIEW=RECOMMENDED
FORMAL_ADOPTION=CONDITIONALLY_RECOMMENDED_ONLY_AFTER_TWO_QUALIFYING_REVIEWS
```

不推荐立即实现或采纳的原因：

1. PRE-25 只证明离线规则与 synthetic fixtures 一致；
2. 没有 qualifying independent review；
3. alias record lifecycle 尚未经过独立治理审查；
4. 没有独立实现、provider runtime 或 portability evidence；
5. `CS-G0` 仍失败关闭，valid problem record 仍为 0。

本建议修正的是“缺少可复核的独立审查”，不是把 offline PASS 升级为 provider、
market、customer 或 production evidence。

## 4. Exact Review Sessions

### Session A

```text
SESSION_ID=PRE26-KIMI-V0_2-CONTRACT-REVIEW
PROVIDER_PATH=BAIDU_QIANFAN_EXACT_MODEL_TOOL
REQUESTED_MODEL=kimi-k2.6
REVIEWER_ROLE=INTEROPERABILITY_AND_FAILURE_SEMANTICS_REVIEWER
REQUESTS_MAX=1
MODEL_BINDING_REQUIREMENT=EXACT_CONNECTOR_CONTRACT
```

### Session B

```text
SESSION_ID=PRE26-GLM-V0_2-CONTRACT-REVIEW
PROVIDER_PATH=BAIDU_QIANFAN_EXACT_MODEL_TOOL
REQUESTED_MODEL=glm-5.2
REVIEWER_ROLE=GOVERNANCE_ALIAS_AND_VERSIONING_REVIEWER
REQUESTS_MAX=1
MODEL_BINDING_REQUIREMENT=EXACT_CONNECTOR_CONTRACT
```

选择两个不同模型族用于独立审查；同一 provider path 不证明 provider independence。
若任一 exact-model tool 不可用、不能确定模型绑定、超时、返回冲突 answer、JSON
不可解析或 response Schema 不匹配，该 session 必须 non-qualifying，不得替换模型、
切换 provider、重试、fallback 或修复 JSON。

## 5. Review Targets

两个 reviewer 使用同一份 hash-bound bundle，审查：

1. `compact-review-response-extraction-contract.v0.2.json`；
2. `compact-review-model-binding-policy.v0.2.json`；
3. `compact-review-model-alias-record.schema.v0.1.json`；
4. `compact-review-cross-layer-invariants.v0.1.json`；
5. `compact-review-contract-revision-fixtures.v0.1.json`；
6. PRE-24 finding triage 和 PRE-25 validation result。

## 6. Required Criteria

每个 reviewer 必须逐项返回 `PASS | FAIL | UNKNOWN`：

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
required change。Reviewer 输出不得产生 normative effect。

## 7. Qualification and Composite Gate

单个 session 只有在以下条件全部满足时才 qualifying：

```text
EXACT_QUERY_HASH_MATCH=true
DIRECT_JSON_PARSE_PASS=true
FROZEN_RESPONSE_SCHEMA_PASS=true
MODEL_BINDING_PASS=true
BOUNDARY_ACKNOWLEDGEMENTS_PASS=true
TERMINAL_EXTRACTION_FAILURE=false
```

只有两个 session 均 qualifying，且：

```text
BLOCKING_FINDINGS=0
MAJOR_FINDINGS=0
BOTH_RECOMMENDATIONS=ACCEPT_FOR_FORMAL_ADOPTION_DECISION
BOUNDARY_SAFETY_FAILURES=0
```

才可得到：

```text
FORMAL_ADOPTION_DECISION_REVIEW_READY=true
```

它仍不等于 Adoption。任一 session 不 qualifying、结论冲突、存在 blocking/major finding
或模型身份不确定时，composite result 必须 `INCOMPLETE_FAIL_CLOSED` 或
`RETURN_FOR_REVISION`，并保留所有失败。

## 8. Required Future Decision Outputs

若后续独立 Decision 采用本建议，只可授权冻结并执行：

1. 两 session review plan 与 input manifest；
2. exact request manifest 和 rendered query hash；
3. v0.2 review response Schema 与正负 fixtures；
4. session result Schema；
5. 两份 sanitized session result；
6. composite validation result；
7. execution receipt 和 result report；
8. cockpit synchronization。

不得持久化 credential、raw provider envelope、usage envelope、hidden reasoning 或未脱敏
provider error body。

## 9. Preconditions

1. PRE-25 result commit `3122832f5aa9b93a10f8cd069b7ee3e5855836e7` 在目标远端；
2. 上述 11 个 artifact hash 全部匹配；
3. standing directive active；
4. exact-model tool availability 在执行前只读验证；
5. 独立 PRE-26 Decision、plan、input manifest、response Schema 和 request hash 在执行前
   形成并远端验证；
6. live request accounting 在执行前为 0。

## 10. Stop Conditions

- 任一 source/hash 漂移；
- exact model tool 不存在或 model binding 不能证明；
- query 超出未来冻结 cap；
- reviewer 获得 tool、web、file、Runtime 或外部操作能力；
- retry、fallback、model substitution、JSON repair 或 semantic rewrite；
- raw response、credential、secret 或 hidden reasoning 持久化；
- finding 被静默删除或自动写成 adopted fact；
- review 被升级为 Adoption、Implementation、Provider Support、Conformance、
  Certification、Release、customer proof 或 `CS-G0 PASS`。

## 11. Success Conditions

```text
INPUT_HASHES_MATCH=ALL
RESPONSE_FIXTURE_EXPECTATIONS_MATCH=ALL
QUERY_BINDINGS_MATCH=2/2
AUTHORIZED_REVIEW_SESSIONS=2
EXECUTED_REVIEW_SESSIONS=2
QUALIFYING_REVIEWS=RESULT_DEPENDENT
RETRY_ATTEMPTS=0
FALLBACK_ATTEMPTS=0
JSON_REPAIR_ATTEMPTS=0
BOUNDARY_SAFETY_FAILURES=0
FORMAL_ADOPTION_DECISION_REVIEW_READY=RESULT_DEPENDENT
CONTRACT_CANDIDATES_ADOPTED=false
IMPLEMENTATION_CREATED=false
LIVE_RERUN_READY=false
```

## 12. False Effects

```text
AUTHORITY_CHANGED=false
OWNERSHIP_CHANGED=false
PRE24_RESULT_CHANGED=false
PRE25_RESULT_CHANGED=false
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

## 13. Standing Directive Eligibility

本建议只有一个 exact action：在远端冻结输入、Schema、query 和模型绑定后，执行 Kimi
与 GLM 各一次只读结构化审查。Inputs、outputs、request cap、zero-retry、stop conditions
和 false effects 均已明确。

```text
STANDING_DIRECTIVE_REFERENCE=TITMAS-CS-STANDING-001
STANDING_DIRECTIVE_ELIGIBLE_CANDIDATE=true
AT_RECOMMENDATION_TIME_PRE26_DECIDED=false
AT_RECOMMENDATION_TIME_LIVE_REVIEW_AUTHORIZED=false
AT_RECOMMENDATION_TIME_LIVE_MODEL_REQUESTS_EXECUTED=0
AT_RECOMMENDATION_TIME_CONTRACT_CANDIDATES_ADOPTED=false
```
