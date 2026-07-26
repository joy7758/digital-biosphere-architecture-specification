---
document_id: DBA-TITMAS-CS-D02-PRE-22-BOUNDED-COMPACT-LIVE-REVIEW-DECISION-0.1
title: TITMAS CS-D02 PRE-22 Bounded Compact Projection Live Review Decision Record v0.1
title_zh: TITMAS CS-D02 PRE-22 受限紧凑投影实时评审决定记录 v0.1
version: 0.1.0
status: authorized-exact-two-session-compact-live-review-only
maturity: Development
decision_id: CS-D02-PRE-22
standing_directive_reference: TITMAS-CS-STANDING-001
decided_by_ref: zhangbin
live_model_request_authorized: true
live_model_requests_max: 2
implementation_authorized: false
---

# TITMAS CS-D02 PRE-22 Bounded Compact Projection Live Review Decision Record v0.1

## Decision

依据 `TITMAS-CS-STANDING-001` 和精确 PRE-22 recommendation，采用：

```text
DECISION_RESULT=AUTHORIZE_EXACT_TWO_SESSION_COMPACT_PROJECTION_LIVE_REVIEW_ONLY
DECIDED_BY_REF=zhangbin
LIVE_MODEL_REQUESTS_MAX=2
PROVIDER_NETWORK_REQUESTS_MAX=2
REQUESTS_PER_SESSION_MAX=1
RETRY_ATTEMPTS_MAX=0
FALLBACK_ATTEMPTS_MAX=0
JSON_REPAIR_ATTEMPTS_MAX=0
```

## Authorized Sessions

只授权 PRE-21 v0.2 manifest 中的两条 hash-bound session：

1. Kimi/Qianfan `kimi-k2.6`：
   `PRE21-KIMI-INTEROP-CANDIDATE`，21,010 bytes，
   SHA-256 `a7d762d7bd22c762d2c7d479508c22624e28f51707eeedaf1945c4153fc7fed7`；
2. DeepSeek `deepseek-chat`：
   `PRE21-DEEPSEEK-BOUNDARY-CANDIDATE`，21,006 bytes，
   SHA-256 `d2297316da3e20c750f16119610d1b06c2fae98b84f21ce911ff84c4a4572f6b`。

每条 session 只调用一次。不得修改 reviewer role、query、provider/model 或 response Schema。

## Failure Policy

- ordinary request/response failure 终止并保留该 session，但在 shared preconditions 仍成立时
  继续另一条已授权 session；
- shared integrity、authorization、credential safety、scope 或 request assembly failure
  立即停止所有未执行 session；
- 不 retry、不 fallback、不 silent downgrade、不 JSON repair；
- 任一 session incomplete、invalid、RETURN 或 REJECT 时 composite 必须失败关闭；
- 另一条 PASS 不替代失败 session。

## Persistence Boundary

允许保存符合 compact response Schema 的 JSON object，以及 request/response hash、byte count、
provider/model/session reference、validation status 和失败分类。

不得保存 API key、Authorization header、raw provider transport envelope、usage/计费 envelope、
hidden reasoning 或自动修复后的 invalid response。

## Preconditions

执行前必须：

1. PRE-21 result、v0.2 manifest、response Schema 与 fixtures hash 匹配；
2. recommendation 已在目标远端分支验证；
3. 本 Decision、machine record、plan、input manifest 和 Schema 全部提交；
4. 远端授权 baseline 与本地完全一致；
5. 两条 request 的 byte count 和 SHA-256 可重建；
6. credential 只从现有安全边界读取，不输出、不写入仓库；
7. live request accounting 为 0。

## Stop Conditions

recommendation/Decision/plan/input hash mismatch、remote drift、request hash/bytes mismatch、
secret safety failure、scope/schema drift、第三个 provider/model、第二次 session request、
retry/fallback/repair 或语义抬升时失败关闭。

## Effects

```text
FULL_SOURCE_HUMAN_REVIEW_EXECUTED=false
PROFILE_REVIEW_COMPLETED=false
PROFILE_ADOPTED=false
ADAPTER_IMPLEMENTATION_CREATED=false
CONFORMANCE_EXECUTED=false
PROVIDER_SUPPORTED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
MARKET_VALIDATION_CREATED=false
CUSTOMER_EVIDENCE_CREATED=false
IMPLEMENTATION_AUTHORIZED=false
EXTERNAL_OUTREACH_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

执行前必须把本 Decision 和冻结计划推送到
`codex/production-observability-baseline` 并生成远端授权回执。
