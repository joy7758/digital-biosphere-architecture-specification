---
document_id: DBA-TITMAS-CS-D02-PRE-23-OFFLINE-LIVE-REVIEW-FAILURE-DIAGNOSTIC-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-23 Offline Live Review Failure Diagnostic Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-23 实时评审失败离线诊断建议 v0.1
version: 0.1.0
status: exact-recommendation-prepared-not-decided
maturity: Development
decision_reference: CS-D02-PRE-23
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
live_model_request_authorized: false
profile_review_completed: false
profile_adopted: false
---

# TITMAS CS-D02 PRE-23 Offline Live Review Failure Diagnostic Recommendation v0.1

## Recommendation

```text
RECOMMENDED_OPTION=AUTHORIZE_OFFLINE_PRE22_EXTRACTION_AND_MODEL_BINDING_DIAGNOSTIC_ONLY
PRIMARY_REPOSITORY=digital-biosphere-architecture
LIVE_MODEL_REQUESTS_MAX=0
PROVIDER_NETWORK_REQUESTS_MAX=0
RETRY_ATTEMPTS_MAX=0
FALLBACK_ATTEMPTS_MAX=0
JSON_REPAIR_ATTEMPTS_MAX=0
IMPLEMENTATION_AUTHORIZED=false
```

建议对 PRE-22 的两个失败类进行一次 deterministic offline diagnostic：

1. Kimi/Qianfan `CLIENT_RESPONSE_EXTRACTION_FAILURE`；
2. DeepSeek `RETURNED_MODEL_MISMATCH`。

PRE-23 只建立 extraction contract candidate、model-binding policy candidate、synthetic
fixtures、离线 validation result、report、receipt 和 cockpit synchronization。它不重新调用
任一 provider，也不重开 PRE-22。

## Evidence

PRE-22 已在远端失败关闭：

```text
AUTHORIZED_SESSIONS=2
EXECUTED_SESSIONS=2
QUERY_BINDINGS_MATCHED=2/2
SCHEMA_CONFORMANT_RESPONSES=1
MODEL_BINDINGS_MATCHED=0
QUALIFYING_SESSIONS=0/2
COMPOSITE_COMPACT_REVIEW_PASS=false
RESULT=INCOMPLETE_FAIL_CLOSED
```

具体事实：

- Kimi installed tool 已调用一次，但 caller 没有保留可提取 answer；
- caller 对 `content[].text` 先执行 JSON parse，再只寻找 wrapper `answer`，因此 plain JSON
  semantic answer 可能被错误丢弃；
- raw tool result 未保存，不能恢复当次 Kimi 内容，也不能证明 provider 是否回答；
- DeepSeek HTTP 200，assistant content direct parse 与 compact response Schema 都通过；
- request 固定 `deepseek-chat`，provider envelope 返回 `deepseek-v4-flash`；
- 未有显式 alias contract，因此 model binding 失败。

## Agent Recommendation Gate

如果潜在 Agent developer 询问当前双 provider compact review 是否值得复用：

```text
CURRENT_PRE22_LIVE_REVIEW_PIPELINE=NOT_RECOMMENDED
OFFLINE_EXTRACTION_AND_MODEL_BINDING_DIAGNOSTIC=CONDITIONALLY_RECOMMENDED
```

当前 pipeline 不推荐的原因：

1. installed tool semantic answer 的 extraction precedence 不完整；
2. wrapper JSON 与 plain response JSON 没有显式区分；
3. conflicting answer locations 没有失败关闭规则；
4. requested model、returned model 与 provider alias 尚无统一判定；
5. 没有在调用前验证 provider 实际返回 model binding；
6. provider content PASS 可能被误写成 qualifying session。

条件式推荐要求：

- 只使用 synthetic wrapper/result fixture，不访问 provider；
- extraction contract 覆盖 structured content、direct answer、JSON wrapper text、plain JSON
  answer text、plain non-JSON text、conflicting answers、missing answer 和 invalid types；
- plain JSON response object 只有在满足 frozen response Schema 时才可作为 semantic answer；
- wrapper JSON 只有存在唯一 string `answer` 时才按 wrapper 处理；
- 多路径 answer 不一致必须失败关闭；
- model binding 明确区分 `EXACT_MATCH`、`EXPLICIT_ALIAS_MATCH`、`MISMATCH` 和 `UNKNOWN`；
- `EXPLICIT_ALIAS_MATCH` 必须有 exact provider source/version 和独立 Decision，不能由 caller
  推定；
- response content Schema PASS 不覆盖 model binding failure；
- fixture 结果不构成 provider success、review completion 或 Profile adoption。

## Exact Candidate Scope

允许创建：

1. `compact-review-response-extraction-contract.v0.1.json` 及 Schema；
2. `compact-review-model-binding-policy.v0.1.json` 及 Schema；
3. extraction/model-binding synthetic fixtures 及 Schema；
4. deterministic offline validator result 及 Schema；
5. diagnostic report、execution receipt 和 cockpit synchronization。

禁止：

- Kimi、DeepSeek 或任何第三 provider/model 请求；
- 恢复、猜测或重建 PRE-22 未保存的 Kimi answer；
- 宣称 `deepseek-chat == deepseek-v4-flash`；
- 修改或重写 PRE-22 session result；
- live rerun、retry、fallback 或 JSON repair；
- full-source review、Profile adoption、Adapter implementation、Conformance、Certification
  或 Release。

## Required Extraction Contract

候选提取顺序：

```text
1. structuredContent.answer string
2. direct answer string
3. content text parsed as wrapper with unique string answer
4. content text parsed directly as frozen response object
5. provider-declared plain content text answer
```

约束：

- 同一语义 answer 在多个位置完全一致时可去重；
- 两个非空 answer 不一致时 `CONFLICTING_ANSWER_LOCATIONS`；
- JSON object 有 `answer` 时优先按 wrapper 判断，不能同时被当成 response object；
- direct response object 必须通过指定 response Schema；
- plain non-JSON content 只有 tool contract 明确允许时才可作为 answer；
- extraction 不做 Markdown strip、code-fence strip、JSON repair 或 semantic rewrite。

## Required Model-Binding Policy

```text
requested == returned
  -> EXACT_MATCH

requested != returned
  + exact provider alias record
  + version/source binding
  + independent Decision
  -> EXPLICIT_ALIAS_MATCH

requested != returned
  + no adopted alias record
  -> MISMATCH

returned missing or unextractable
  -> UNKNOWN
```

`EXACT_MATCH` 或 adopted `EXPLICIT_ALIAS_MATCH` 只是 model identity binding；不证明 output
quality、provider support、conformance、certification 或 Truth。

## Preconditions

1. PRE-22 result commit `238583c…` 与 cockpit commit `273fd56…` 在远端可追溯；
2. PRE-22 session results、composite result、receipt 和 report hash 匹配；
3. standing directive active；
4. 独立 PRE-23 Decision、plan 和 input manifest 已形成；
5. Decision/plan/input 在远端验证；
6. live/provider request accounting 在执行前与执行后均为 0。

## Stop Conditions

- PRE-22 input hash mismatch；
- synthetic fixture 读取 real credential、provider 或 network；
- extraction contract 静默选择冲突 answer；
- extraction contract 自动 repair response；
- model policy 自动接受未记录 alias；
- content Schema PASS 覆盖 model mismatch；
- fixture PASS 被升级为 provider success 或 review completion；
- 任何 live request、retry、fallback、implementation 或语义抬升。

## Success Conditions

```text
INPUT_HASHES_MATCH=true
EXTRACTION_FIXTURE_EXPECTATIONS_MATCH=ALL
MODEL_BINDING_FIXTURE_EXPECTATIONS_MATCH=ALL
CONFLICTING_ANSWER_FIXTURES_FAIL_CLOSED=true
UNADOPTED_ALIAS_FIXTURES_FAIL_CLOSED=true
LIVE_MODEL_REQUESTS_EXECUTED=0
PROVIDER_NETWORK_REQUESTS_EXECUTED=0
OFFLINE_FAILURE_DIAGNOSTIC_PASS=true
LIVE_RERUN_READY=false
PROFILE_REVIEW_COMPLETED=false
PROFILE_ADOPTED=false
```

## False Effects

```text
AUTHORITY_CHANGED=false
OWNERSHIP_CHANGED=false
PRE22_RESULT_CHANGED=false
LIVE_REVIEW_EXECUTED=false
COMPACT_PROJECTION_REVIEW_COMPLETED=false
FULL_SOURCE_HUMAN_REVIEW_EXECUTED=false
PROFILE_REVIEW_COMPLETED=false
PROFILE_ADOPTED=false
ADAPTER_IMPLEMENTATION_CREATED=false
CONFORMANCE_EXECUTED=false
PROVIDER_SUPPORTED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
IMPLEMENTATION_AUTHORIZED=false
EXTERNAL_OUTREACH_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

## Standing Directive Eligibility

本建议是单一 exact offline diagnostic action，明确 target artifacts、inputs、fixture
requirements、zero-network limit、stop conditions 和 false effects。它属于 DBA/TITMAS
商业化标准路线中的内部 architecture/specification validation。

```text
STANDING_DIRECTIVE_REFERENCE=TITMAS-CS-STANDING-001
STANDING_DIRECTIVE_ELIGIBLE_CANDIDATE=true
AT_RECOMMENDATION_TIME_PRE23_DECIDED=false
AT_RECOMMENDATION_TIME_LIVE_REQUESTS_EXECUTED=0
```
