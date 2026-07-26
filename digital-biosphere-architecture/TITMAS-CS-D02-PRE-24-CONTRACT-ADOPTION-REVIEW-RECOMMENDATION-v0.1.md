---
document_id: DBA-TITMAS-CS-D02-PRE-24-CONTRACT-ADOPTION-REVIEW-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-24 Contract Adoption Review Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-24 契约采纳审查建议 v0.1
version: 0.1.0
status: exact-recommendation-prepared-not-decided
maturity: Development
decision_reference: CS-D02-PRE-24
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
review_execution_authorized: false
contract_candidates_adopted: false
implementation_authorized: false
live_rerun_ready: false
---

# TITMAS CS-D02 PRE-24 Contract Adoption Review Recommendation v0.1

## 1. Recommendation

```text
RECOMMENDED_OPTION=AUTHORIZE_EXACT_TWO_SESSION_CONTRACT_ADOPTION_REVIEW_ONLY
PRIMARY_REPOSITORY=digital-biosphere-architecture
REVIEW_TARGETS=2
REVIEWER_SESSIONS_MAX=2
KIMI_K2_6_REQUESTS_MAX=1
DEEPSEEK_CHAT_REQUESTS_MAX=1
RETRY_ATTEMPTS_MAX=0
FALLBACK_ATTEMPTS_MAX=0
JSON_REPAIR_ATTEMPTS_MAX=0
WEB_SEARCH_REQUESTS_MAX=0
PROVIDER_TOOL_CALLS_FROM_REVIEWERS_MAX=0
CONTRACT_ADOPTION_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
LIVE_RERUN_AUTHORIZED=false
```

建议对 PRE-23 形成的两个候选契约执行一次独立、只读、双智能体采纳审查：

1. `compact-review-response-extraction-contract.v0.1.json`；
2. `compact-review-model-binding-policy.v0.1.json`。

本建议只允许收集结构化 review input（审查输入）。Review 不等于 Adoption，两个 review
都通过也只能形成后续 formal adoption Decision（正式采纳决定）的输入。

## 2. Evidence and Current Gap

PRE-23 已证明：

```text
INPUT_HASHES_MATCHED=9/9
FIXTURE_EXPECTATIONS_MATCHED=15/15
EXTRACTION_CASES_MATCHED=10/10
MODEL_BINDING_CASES_MATCHED=5/5
OFFLINE_FAILURE_DIAGNOSTIC_PASS=true
CONTRACT_CANDIDATES_ADOPTED=false
IMPLEMENTATION_CREATED=false
LIVE_RERUN_READY=false
```

该结果证明候选契约对冻结 synthetic fixtures（合成案例）的行为符合预期，但尚未证明：

- 契约的完整性、可移植性和长期版本兼容性；
- 独立智能体能否理解并一致应用规则；
- 未观察 provider shape（提供方返回形态）是否会被安全处理；
- 契约已被实现、在真实 provider pipeline 中运行或具备生产稳定性；
- 任一候选应该正式采纳。

冻结输入及 SHA-256：

| artifact | SHA-256 |
|---|---|
| `compact-review-response-extraction-contract.v0.1.json` | `1ad48badb0767727fde354ca8ed3298261a2117813b8f41ad2f2cdf344286dc4` |
| `compact-review-response-extraction-contract.schema.v0.1.json` | `669dd135951ab16eced4794ca23332505df3a36e7bd2f482e4f981b6dc8ecce2` |
| `compact-review-model-binding-policy.v0.1.json` | `75eb8462b7124fe246889ea600ec52dcc99946d5f16bcc848717d5e39fb4adb2` |
| `compact-review-model-binding-policy.schema.v0.1.json` | `77430ba7d53a6b8162000886dff44ec6c679d34e59cd8ea2dbe15d529f225378` |
| `compact-review-failure-diagnostic-fixtures.v0.1.json` | `2612c33f3dfe3291509e973e12cee37fd3441a8432b83c694573f2feafa78b00` |
| `offline-live-review-failure-diagnostic-result.v0.1.json` | `df96ced84e6186208c668d8673dc9155537cbe61e87691af3eccdb41fb18d616` |
| `PRE-23-OFFLINE-LIVE-REVIEW-FAILURE-DIAGNOSTIC-RESULT-v0.1.md` | `657269b9f67b48d11aa4c34d1683dbf261a4e85c165a124586c7bafd51a109f2` |

## 3. Pre-development Agent Recommendation Gate

问题：如果潜在 Agent developer（智能体开发者）需要安全解析不同 provider 的结构化审查
响应并验证所请求模型与实际返回模型的绑定，智能体是否会推荐当前两个候选契约？

```text
CURRENT_CANDIDATES=CONDITIONALLY_RECOMMENDED_FOR_ADOPTION_REVIEW
CURRENT_CANDIDATES=NOT_RECOMMENDED_AS_ADOPTED_OR_IMPLEMENTED_STANDARD
PRE24_TWO_AGENT_REVIEW=RECOMMENDED_WITH_FAIL_CLOSED_MODEL_BINDING
```

条件式推荐理由：

1. 候选解决 PRE-22 已观察到的真实 extraction 和 model drift（模型漂移）问题；
2. 冲突 answer、未采纳 alias、Schema mismatch 和 unknown 都失败关闭；
3. content validity（内容有效）与 model identity binding（模型身份绑定）明确分离；
4. fixture 覆盖当前已知正例和负例，且没有 retry、fallback 或 JSON repair；
5. 仍缺独立可理解性审查、兼容性判断和实现反馈，不能直接采纳。

不推荐原因及可修正问题：

| gap | required review evidence |
|---|---|
| source precedence 是否对未来 shape 足够清晰 | reviewer 给出明确反例、JSON Pointer 和 required change |
| wrapper 与 direct response object 的判别是否存在歧义 | reviewer 对 discriminator 和 conflict rule 作独立判断 |
| model alias 的 provenance 要求是否足够可执行 | reviewer 检查 source/version/scope/Decision 全部绑定 |
| current alias records 为空时的行为是否安全 | reviewer 确认只能 `MISMATCH` 或 `UNKNOWN` |
| 版本变化和 backward compatibility 尚未声明 | reviewer 必须评估 breaking-change surface |
| 没有 implementation feedback | 保持 adoption 和 implementation 为 false，转入后续独立 gate |

## 4. Exact Review Sessions

若后续独立 Decision 采纳本建议，只允许：

| session | provider path | requested model | role | request max |
|---|---|---|---|---:|
| `PRE24-KIMI-CONTRACT-REVIEW` | Baidu Qianfan exact-model tool | `kimi-k2.6` | interoperability and extraction reviewer | 1 |
| `PRE24-DEEPSEEK-CONTRACT-REVIEW` | DeepSeek `/v1/chat/completions` | `deepseek-chat` | governance and model-binding reviewer | 1 |

两个 reviewer 接收完全相同、hash-bound（哈希绑定）的 review bundle。Reviewer 不获得
Web、外部工具、credential、仓库写入或决策权。

DeepSeek session 必须记录 provider 返回的 model identifier。若仍返回
`deepseek-v4-flash` 或任何不同 model，结果标记 `MODEL_BINDING_MISMATCH`，不能作为
qualifying review；不得自动建立 alias。Kimi session 的 exact-model claim 只来源于工具
的固定模型契约，不从回答内容推定。

## 5. Required Review Criteria

每个 reviewer 必须逐项返回 `PASS`、`FAIL` 或 `UNKNOWN`：

1. `EXTRACTION_SOURCE_DISCRIMINATION`；
2. `CONFLICT_FAIL_CLOSED`；
3. `NO_REPAIR_OR_SEMANTIC_REWRITE`；
4. `DIRECT_RESPONSE_SCHEMA_BINDING`；
5. `PLAIN_CONTENT_DECLARATION_BOUNDARY`；
6. `MODEL_IDENTITY_SEPARATION_FROM_CONTENT_VALIDITY`；
7. `ALIAS_PROVENANCE_AND_DECISION_BINDING`；
8. `UNKNOWN_AND_MISMATCH_PRESERVATION`；
9. `VERSIONING_AND_BREAKING_CHANGE_SURFACE`；
10. `PROVIDER_NEUTRALITY_AND_PORTABILITY`；
11. `DETERMINISTIC_TESTABILITY`；
12. `AUTHORITY_AND_TRUTH_NON_ELEVATION`。

每个 `FAIL` 或 `UNKNOWN` 必须提供：

```text
contract_target
json_pointer_or_section
reason
required_change
severity
```

不得请求或保存 hidden reasoning（隐藏推理）。只保留最终结构化 review、必要 provider
binding metadata、hash、状态和失败原因。

## 6. Review Verdicts

允许的 reviewer verdict：

```text
ACCEPT_BOTH_FOR_FORMAL_ADOPTION_DECISION
ACCEPT_EXTRACTION_ONLY_RETURN_MODEL_POLICY_FOR_REVISION
ACCEPT_MODEL_POLICY_ONLY_RETURN_EXTRACTION_FOR_REVISION
RETURN_BOTH_FOR_REVISION
INSUFFICIENT_EVIDENCE
```

Composite result（组合结果）规则：

- 两个 qualifying reviewer 都选择第一个 verdict，且 12 项均为 `PASS`，才可标记
  `FORMAL_ADOPTION_DECISION_READY=true`；
- 任一 reviewer 有 `FAIL`、`UNKNOWN`、model mismatch、response Schema failure 或未完成，
  必须保留并使 `FORMAL_ADOPTION_DECISION_READY=false`；
- 两个 reviewer verdict 不一致时标记 `REVIEW_CONFLICT`；
- Review pass 不自动改变候选文件的 `status`，也不自动产生 Adoption。

## 7. Required Artifacts Before Any Review Call

后续 Decision 执行前必须形成并在远端验证：

1. 独立 PRE-24 Decision Record；
2. hash-bound review plan；
3. exact input manifest；
4. compact review response Schema 与 positive/negative fixtures；
5. 两个 exact query 的 byte count 和 SHA-256；
6. authorization baseline receipt；
7. zero-retry、zero-fallback、zero-repair accounting。

执行后必须保存：

- 两个 sanitized session result；
- composite validation result；
- execution receipt；
- bounded result report；
- cockpit synchronization。

## 8. Preconditions

1. PRE-23 result commit `5916d8b…` 与 cockpit commit `99af818…` 在远端可追溯；
2. 本建议所列 7 个输入 hash 全部匹配；
3. `TITMAS-CS-STANDING-001` 仍为 active；
4. PRE-24 Decision、plan、manifest 和 response contract 在调用前单独 commit/push；
5. 授权基线 commit 必须是远端分支祖先；
6. 两个 query 必须只包含 public-safe architecture material；
7. 调用前、调用后 credential 均不输出、不持久化。

## 9. Stop Conditions

- 任一输入 hash 或 query hash 不匹配；
- reviewer session 无法绑定到 exact authorized path/model；
- query 包含 secret、PII、客户数据、未公开源码或 raw provider envelope；
- caller 尝试 retry、fallback、JSON repair、Markdown strip 或 semantic rewrite；
- caller 静默接受 model mismatch 或推定 alias；
- reviewer 试图修改契约、批准自身建议或产生执行命令；
- review result 被升级为 provider support、Profile adoption、Implementation、Certification
  或 Release；
- 任一 materially different action 没有新的 recommendation 和 Decision。

## 10. Success Conditions

```text
INPUT_HASHES_MATCH=ALL
QUERY_BINDINGS_MATCH=2/2
AUTHORIZED_REVIEW_SESSIONS=2
EXECUTED_REVIEW_SESSIONS=2
RETRY_ATTEMPTS=0
FALLBACK_ATTEMPTS=0
JSON_REPAIR_ATTEMPTS=0
BOUNDARY_SAFETY_FAILURES=0
FAILURES_AND_UNKNOWN_PRESERVED=true
FORMAL_ADOPTION_DECISION_READY=RESULT_DEPENDENT
CONTRACT_CANDIDATES_ADOPTED=false
IMPLEMENTATION_CREATED=false
LIVE_RERUN_READY=false
```

## 11. False Effects

```text
AUTHORITY_CHANGED=false
OWNERSHIP_CHANGED=false
PRE22_RESULT_CHANGED=false
PRE23_RESULT_CHANGED=false
CONTRACT_CANDIDATES_ADOPTED=false
ADAPTER_IMPLEMENTATION_CREATED=false
LIVE_REVIEW_RERUN_EXECUTED=false
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

## 12. Standing Directive Eligibility

本建议只有一个 exact action：执行两个指定 provider/model path 的只读契约采纳审查。
Inputs、review criteria、output verdict、request cap、preconditions、stop conditions 和 false
effects 已明确；任何后续 Adoption、Implementation 或 live rerun 都必须形成独立建议和决定。

```text
STANDING_DIRECTIVE_REFERENCE=TITMAS-CS-STANDING-001
STANDING_DIRECTIVE_ELIGIBLE_CANDIDATE=true
AT_RECOMMENDATION_TIME_PRE24_DECIDED=false
AT_RECOMMENDATION_TIME_REVIEW_EXECUTED=false
AT_RECOMMENDATION_TIME_CONTRACT_CANDIDATES_ADOPTED=false
```
