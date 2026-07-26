---
document_id: DBA-TITMAS-CS-D02-PRE-28-HANDOFF-BOUND-CONTRACT-CANDIDATE-REVIEW-DECISION-0.1
title: TITMAS CS-D02 PRE-28 Handoff-bound Contract Candidate Review Decision Record v0.1
title_zh: TITMAS CS-D02 PRE-28 交接绑定契约候选审查决定记录 v0.1
version: 0.1.0
status: authorized-exact-two-session-handoff-bound-review-only
maturity: Development
decision_id: CS-D02-PRE-28
standing_directive_reference: TITMAS-CS-STANDING-001
decided_by_ref: zhangbin
review_execution_authorized: true
contract_adoption_authorized: false
implementation_authorized: false
provider_support_claim_authorized: false
release_authorized: false
---

# TITMAS CS-D02 PRE-28 Handoff-bound Contract Candidate Review Decision Record v0.1

## Decision

依据 `TITMAS-CS-STANDING-001` 和远端验证的 PRE-28 exact recommendation，采用：

```text
DECISION_RESULT=AUTHORIZE_EXACT_TWO_SESSION_PRE25_V0_2_CONTRACT_CANDIDATE_REVIEW_WITH_SANITIZED_SINK_HANDOFF_ONLY
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
SANITIZED_TEMPORARY_SINKS_REQUIRED=2
RAW_PROVIDER_ENVELOPE_SINKS_ALLOWED=0
CONTRACT_ADOPTION_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
```

## Scope

只授权：

- 复核 PRE-28 推荐中的 8 个冻结来源哈希；
- 复用 PRE-26 冻结 query、request payload 和 response Schema，不改变审查内容；
- 为 `kimi-k2.6` 与 `glm-5.2` 各建立一个新的 PRE-28 session identifier；
- 在任何 provider request 前创建全新 `0700` 临时根目录，冻结两个 session sink 和一个
  control receipt target 的 path、parent device/inode、mode 与 ownership；
- 将每个 provider envelope 仅在内存中解析为 sanitized session result；
- 通过 session result Schema 后执行
  `exclusive staging write → fsync → atomic rename → parent fsync → read/digest/schema verify`；
- 即使 provider/session non-qualifying，也保留 Schema-valid sanitized failure result；
- 仅保存 sanitized result、单向 digest、字节数、模型绑定、失败分类、composite result、
  receipt 和报告。

## Authority Boundary

- Review 是后续 Formal Adoption Decision 的 advisory input，不是 Adoption；
- sink commit 只证明 caller handoff，不证明 provider correctness、conformance 或 durability；
- returned model 缺失或不等于 requested model 时对应 session non-qualifying；
- 不允许 retry、fallback、model substitution、alias inference、JSON repair 或 semantic rewrite；
- raw envelope、usage、credential、hidden reasoning 和 provider error body 不得持久化；
- PRE-26 历史和 request budget 保持关闭，不将 PRE-28 写成 PRE-26 retry。

## Preconditions

执行 provider request 前必须全部成立：

1. recommendation、Decision、plan、manifests、Schema 在目标远端；
2. 8 个 source hash 全部匹配；
3. 全新临时根和三个 exact target 的 preflight 通过；
4. `QIANFAN_API_KEY` 只完成存在且非空检查，不输出或持久化；
5. authorization receipt 已提交并远端验证；
6. PRE-28 provider request accounting 为 0。

## Stop Conditions

source/query/payload/Schema/endpoint 漂移、target 预先存在或为 symlink、权限／ownership
不符、credential 或 raw body 持久化、超出两次请求、任何 retry/fallback/substitution/
alias inference/repair、sink missing/empty/partial/digest mismatch/schema invalid、finding
删除或语义抬升时立即失败关闭。

普通单 session provider failure 不自动取消另一个已授权 session；共享输入、授权、secret
或 sink boundary failure 停止全部后续请求。

## Effects

```text
AUTHORITY_CHANGED=false
OWNERSHIP_CHANGED=false
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

本 Decision 只形成有界审查授权。任何 provider request 仍须等待本 Decision 基线和包含
精确临时目标的独立 authorization receipt 均在目标远端验证。
