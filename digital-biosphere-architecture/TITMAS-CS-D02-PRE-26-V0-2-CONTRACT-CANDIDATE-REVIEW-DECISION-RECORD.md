---
document_id: DBA-TITMAS-CS-D02-PRE-26-V0-2-CONTRACT-CANDIDATE-REVIEW-DECISION-0.1
title: TITMAS CS-D02 PRE-26 v0.2 Contract Candidate Review Decision Record v0.1
title_zh: TITMAS CS-D02 PRE-26 v0.2 契约候选审查决定记录 v0.1
version: 0.1.0
status: authorized-exact-two-session-qianfan-direct-review-only
maturity: Development
decision_id: CS-D02-PRE-26
standing_directive_reference: TITMAS-CS-STANDING-001
decided_by_ref: zhangbin
review_execution_authorized: true
contract_adoption_authorized: false
implementation_authorized: false
provider_support_claim_authorized: false
release_authorized: false
---

# TITMAS CS-D02 PRE-26 v0.2 Contract Candidate Review Decision Record v0.1

## Decision

依据 `TITMAS-CS-STANDING-001` 和远端验证的 PRE-26 v0.2 exact recommendation，采用：

```text
DECISION_RESULT=AUTHORIZE_EXACT_TWO_SESSION_PRE25_V0_2_CONTRACT_CANDIDATE_REVIEW_VIA_QIANFAN_DIRECT_CHAT_ONLY
DECIDED_BY_REF=zhangbin
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
PROVIDER_SUPPORT_CLAIM_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

## Scope

只授权：

- 冻结 PRE-25 v0.2 契约候选、依赖 Schema、fixtures、triage 和离线结果的输入哈希；
- 冻结 public-safe、无密钥、无私有源码的审查 query 与 exact request body；
- 建立 strict response Schema、正负 fixtures、session result Schema 和 composite result
  Schema；
- 通过同一 Qianfan direct chat endpoint 对 `kimi-k2.6` 与 `glm-5.2` 各执行一次只读
  reviewer session；
- 仅保留 sanitized review response、model binding、HTTP status、byte count、one-way
  digest、失败分类、composite result、receipt、report 和 cockpit synchronization。

## Authority Boundary

- Review 是后续 Human Formal Adoption Decision 的 advisory input，不是 Adoption；
- reviewer 不获得 Decision、Permission、仓库写入、Runtime、工具、Web 或外部操作能力；
- `PASS` 不覆盖 input hash、query hash、direct JSON parse、Schema、model binding、
  provenance 或 boundary failure；
- returned model 缺失或与 requested model 不完全相等即 non-qualifying；
- 不允许 alias 推断、模型替换、重试、fallback、JSON repair 或语义改写；
- provider/model 的一次响应不形成 provider support、portability、conformance、
  certification、market validation、customer proof 或 release claim。

## Preconditions

执行 provider request 前必须全部成立：

1. PRE-26 v0.2 recommendation 与本 Decision 在目标远端；
2. 11 个 PRE-25 source hash 全部匹配；
3. plan、input manifest、request manifest、query、response Schema、fixtures 和 result
   Schema 已提交并在目标远端验证；
4. `QIANFAN_API_KEY` 只完成存在且非空检查，不进入任何 artifact、prompt、log 或 Git；
5. authorization receipt 另行建立、提交并远端验证；
6. provider request accounting 为 0。

## Stop Conditions

input/query/payload/Schema hash 漂移、credential 泄漏、endpoint/model 不匹配、超出两个网络
请求、retry、fallback、model substitution、alias inference、JSON repair、raw envelope／usage／
hidden reasoning／error body 持久化、finding 删除或任何语义抬升时立即失败关闭。

普通单 session provider failure 不自动取消另一个已授权 session；共享输入、授权或密钥
边界失败停止全部后续请求。

## Effects

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

本 Decision 只形成有界审查授权。任何 provider request 仍须等待本 Decision 基线和独立
authorization receipt 均在目标远端验证。
