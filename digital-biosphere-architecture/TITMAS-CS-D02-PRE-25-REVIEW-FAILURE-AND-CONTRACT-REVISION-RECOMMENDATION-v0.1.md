---
document_id: DBA-TITMAS-CS-D02-PRE-25-REVIEW-FAILURE-AND-CONTRACT-REVISION-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-25 Review Failure and Contract Revision Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-25 审查失败与契约修订建议 v0.1
version: 0.1.0
status: exact-recommendation-prepared-not-decided
maturity: Development
decision_reference: CS-D02-PRE-25
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
live_model_request_authorized: false
contract_revision_authorized: false
contract_candidates_adopted: false
implementation_authorized: false
---

# TITMAS CS-D02 PRE-25 Review Failure and Contract Revision Recommendation v0.1

## 1. Recommendation

```text
RECOMMENDED_OPTION=AUTHORIZE_OFFLINE_PRE24_FINDING_TRIAGE_AND_V0_2_CONTRACT_REVISION_CANDIDATES_ONLY
PRIMARY_REPOSITORY=digital-biosphere-architecture
LIVE_MODEL_REQUESTS_MAX=0
PROVIDER_NETWORK_REQUESTS_MAX=0
RETRY_ATTEMPTS_MAX=0
FALLBACK_ATTEMPTS_MAX=0
JSON_REPAIR_ATTEMPTS_MAX=0
CONTRACT_ADOPTION_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
LIVE_RERUN_AUTHORIZED=false
```

建议对 PRE-24 的失败和 3 个 advisory finding 执行 deterministic offline triage（确定性离线
分诊），然后只生成 v0.2 revision candidate（修订候选）。不重新调用 Kimi、DeepSeek 或
其他模型；不直接把 non-qualifying review 写成规范事实。

## 2. Evidence

PRE-24 远端结果：

```text
AUTHORIZED_REVIEW_SESSIONS=2
EXECUTED_REVIEW_SESSIONS=2
KIMI_RESULT=PROVIDER_TIMEOUT_OR_NETWORK_ERROR
DEEPSEEK_DIRECT_JSON_PARSE_PASS=true
DEEPSEEK_RESPONSE_SCHEMA_PASS=true
DEEPSEEK_MODEL_BINDING=MISMATCH
QUALIFYING_REVIEWS=0
ADVISORY_FINDINGS_RETAINED=3
FORMAL_ADOPTION_DECISION_READY=false
CONTRACT_CANDIDATES_ADOPTED=false
```

冻结证据：

| artifact | SHA-256 |
|---|---|
| `contract-adoption-review-validation-result.v0.1.json` | `1bef2ecdce8b7fd6765a0b6e927f7d4f4a6a8871b7a6801744345d71c6062e37` |
| `contract-adoption-review-kimi-session-result.v0.1.json` | `545c98138e38db91d5e453c4c0eb89c19ddf54086fc36712aee678c8483b55be` |
| `contract-adoption-review-deepseek-session-result.v0.1.json` | `f0a13da3c54a2e52f12d23e456ad1c6d0285a5bbec419739f51e6048c50dd750` |
| `contract-adoption-review-execution-receipt.v0.1.json` | `bdfe857d16908724d5f466e03a8cbb5659e7f913cf64d7a924c0192791fb337e` |
| `PRE-24-CONTRACT-ADOPTION-REVIEW-RESULT-v0.1.md` | `49f978784f32a76ecd483d054139482c8c9e9b93e4ef68a617fe4e5c8f0052d7` |

## 3. Pre-development Agent Recommendation Gate

如果潜在 Agent developer 询问当前 v0.1 候选是否可作为稳定契约复用：

```text
V0_1_CONTRACT_CANDIDATES=NOT_RECOMMENDED_FOR_ADOPTION_OR_IMPLEMENTATION
OFFLINE_FINDING_TRIAGE=RECOMMENDED
V0_2_REVISION_CANDIDATES=CONDITIONALLY_RECOMMENDED_AFTER_TRIAGE
```

不推荐当前直接采纳的原因：

1. PRE-24 没有 qualifying review；
2. conflict result 与 qualification failure 的显式映射仍可加强；
3. semantic response extraction 和 provider model extraction 的跨层关系未写清；
4. alias record 的 adoption、有效期、撤销和冲突语义未完整定义；
5. 没有实现反馈或真实 pipeline validation。

修正方式不是相信 non-qualifying reviewer，而是把每项 finding 转换为可证伪的离线问题，
分别检查现有契约、已有 fixtures 和架构不变量。

## 4. Required Finding Triage

### Finding F1: Conflict terminal behavior

Advisory claim：`CONFLICTING_ANSWER_LOCATIONS` 没有明确强制失败。

建议分诊：

```text
INITIAL_CLASSIFICATION=PARTIALLY_SUPPORTED
```

现有契约已禁止 precedence 静默覆盖冲突，并输出
`CONFLICTING_ANSWER_LOCATIONS`；缺口是没有显式 `qualification=false`、terminal class 和
caller obligation。v0.2 应增加：

- `qualifying_states`；
- `terminal_failure_states`；
- `CONFLICTING_ANSWER_LOCATIONS -> qualifying=false`；
- caller 必须停止 review qualification，但保留原始失败状态。

不得把 conflict 自动选择成任一 answer。

### Finding F2: Extraction failure versus model binding

Advisory claim：应新增 `EXTRACTION_FAILED` model-binding state。

建议分诊：

```text
INITIAL_CLASSIFICATION=REQUIRES_CORRECTION
```

semantic answer extraction 和 provider envelope model extraction 是两个不同维度。Answer
缺失不应改写 model identity；returned model 缺失才产生 `UNKNOWN`。v0.2 应增加
cross-layer invariants：

```text
SEMANTIC_EXTRACTION_RESULT_NE_MODEL_BINDING_STATE=true
CONTENT_FAILURE_DOES_NOT_ERASE_MODEL_IDENTITY=true
MODEL_IDENTITY_FAILURE_DOES_NOT_VALIDATE_CONTENT=true
```

不建议新增会混淆两个维度的 `EXTRACTION_FAILED` model state。

### Finding F3: Alias adoption and lifecycle

Advisory claim：alias provenance 需要更严格的 Decision 和 provider version binding。

建议分诊：

```text
INITIAL_CLASSIFICATION=SUPPORTED_WITH_ADDITIONAL_SCOPE
```

v0.1 已要求 provider source/version 和 independent Decision，但没有完整 alias lifecycle。
v0.2 应要求：

- `alias_record_id`；
- exact provider/source/version；
- requested/returned model；
- alias scope；
- explicit `ALIAS_ADOPTION_DECISION_REFERENCE`；
- `effective_at`、可选 `expires_at`；
- `status = ACTIVE | EXPIRED | REVOKED | CONFLICTED`；
- 可选 `revocation_reference`；
- 冲突 alias 必须失败关闭；
- expired/revoked/conflicted alias 不得 qualifying。

Alias adoption 不证明 provider support、output quality、conformance 或 Truth。

## 5. Exact Candidate Scope

后续 Decision 只可授权创建：

1. `compact-review-response-extraction-contract.v0.2.json` 及 Schema；
2. `compact-review-model-binding-policy.v0.2.json` 及 Schema；
3. `compact-review-model-alias-record.schema.v0.1.json` candidate；
4. `compact-review-cross-layer-invariants.v0.1.json` candidate；
5. finding triage matrix；
6. positive/negative fixtures；
7. deterministic offline result、receipt、report 和 cockpit synchronization。

所有 v0.1 文件保持历史不变。

## 6. Required Fixture Classes

至少覆盖：

1. conflict answer produces terminal non-qualifying extraction；
2. identical answer dedup remains qualifying；
3. missing semantic answer with exact model retains separate model state；
4. valid semantic answer with missing returned model produces `UNKNOWN`；
5. active exact-version alias may produce `EXPLICIT_ALIAS_MATCH`；
6. expired alias fails closed；
7. revoked alias fails closed；
8. conflicted aliases fail closed；
9. arbitrary Decision reference cannot activate alias；
10. content Schema PASS cannot override model mismatch。

## 7. Preconditions

1. PRE-24 result commit `83fba0a…` 与 cockpit commit `c851e37…` 在远端可追溯；
2. 本建议列出的 5 个 PRE-24 evidence hash 全部匹配；
3. v0.1 candidate、Schema 和 PRE-23 fixtures hash 保持不变；
4. standing directive active；
5. 独立 PRE-25 Decision、plan 和 input manifest 在执行前形成并远端验证；
6. live/provider request accounting 在执行前后均为 0。

## 8. Stop Conditions

- 把 DeepSeek advisory finding 直接写成 adopted fact；
- 修改或覆盖 v0.1 历史文件；
- 混淆 semantic extraction 与 model identity extraction；
- conflict、expired、revoked 或 conflicted alias 仍可 qualifying；
- alias 由 caller 推定或由普通 review 自动采纳；
- 使用 provider/network/credential；
- 创建实现、live rerun、Profile adoption、Certification、Release 或语义抬升。

## 9. Success Conditions

```text
INPUT_HASHES_MATCH=ALL
FINDINGS_TRIAGED=3/3
TRIAGE_HAS_INDEPENDENT_RULE_JUSTIFICATION=3/3
V0_2_CANDIDATE_SCHEMAS_META_VALID=ALL
FIXTURE_EXPECTATIONS_MATCH=ALL
V0_1_HISTORY_CHANGED=false
LIVE_MODEL_REQUESTS_EXECUTED=0
PROVIDER_NETWORK_REQUESTS_EXECUTED=0
OFFLINE_REVISION_CANDIDATE_PASS=true
CONTRACT_CANDIDATES_ADOPTED=false
IMPLEMENTATION_CREATED=false
LIVE_RERUN_READY=false
```

## 10. False Effects

```text
AUTHORITY_CHANGED=false
OWNERSHIP_CHANGED=false
PRE22_RESULT_CHANGED=false
PRE23_RESULT_CHANGED=false
PRE24_RESULT_CHANGED=false
V0_1_CONTRACTS_CHANGED=false
V0_2_CONTRACT_CANDIDATES_ADOPTED=false
ADAPTER_IMPLEMENTATION_CREATED=false
LIVE_REVIEW_EXECUTED=false
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

## 11. Standing Directive Eligibility

本建议只有一个 exact offline action：分诊 3 个 advisory finding，并建立有界 v0.2
revision candidate 与 fixtures。Inputs、outputs、zero-network limit、stop conditions 和
false effects 均已明确。

```text
STANDING_DIRECTIVE_REFERENCE=TITMAS-CS-STANDING-001
STANDING_DIRECTIVE_ELIGIBLE_CANDIDATE=true
AT_RECOMMENDATION_TIME_PRE25_DECIDED=false
AT_RECOMMENDATION_TIME_CONTRACT_REVISION_EXECUTED=false
AT_RECOMMENDATION_TIME_CONTRACT_CANDIDATES_ADOPTED=false
```
