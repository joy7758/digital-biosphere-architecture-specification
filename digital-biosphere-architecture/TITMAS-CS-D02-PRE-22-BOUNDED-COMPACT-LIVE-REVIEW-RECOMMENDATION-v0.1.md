---
document_id: DBA-TITMAS-CS-D02-PRE-22-BOUNDED-COMPACT-LIVE-REVIEW-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-22 Bounded Compact Projection Live Review Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-22 受限紧凑投影实时评审建议 v0.1
version: 0.1.0
status: exact-recommendation-prepared-not-decided
maturity: Development
decision_reference: CS-D02-PRE-22
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
live_model_request_authorized: false
compact_projection_review_completed: false
profile_review_completed: false
profile_adopted: false
---

# TITMAS CS-D02 PRE-22 Bounded Compact Projection Live Review Recommendation v0.1

## Recommendation

```text
RECOMMENDED_OPTION=AUTHORIZE_EXACT_TWO_SESSION_COMPACT_PROJECTION_LIVE_REVIEW_ONLY
PRIMARY_REPOSITORY=digital-biosphere-architecture
LIVE_MODEL_REQUESTS_MAX=2
PROVIDER_NETWORK_REQUESTS_MAX=2
REQUESTS_PER_SESSION_MAX=1
RETRY_ATTEMPTS_MAX=0
FALLBACK_ATTEMPTS_MAX=0
JSON_REPAIR_ATTEMPTS_MAX=0
IMPLEMENTATION_AUTHORIZED=false
```

建议在独立 Decision、冻结执行计划、输入清单和远端授权基线建立后，对 PRE-21
`compact-review-request-manifest.v0.2.json` 中两条 hash-bound candidate session 各执行一次：

| Session | Provider / model | Reviewer role | Exact query |
|---|---|---|---|
| `PRE21-KIMI-INTEROP-CANDIDATE` | Kimi/Qianfan `kimi-k2.6` | `INTEROPERABILITY_AND_DEVELOPER_IMPLEMENTABILITY_REVIEWER` | 21,010 bytes / `a7d762d7bd22c762d2c7d479508c22624e28f51707eeedaf1945c4153fc7fed7` |
| `PRE21-DEEPSEEK-BOUNDARY-CANDIDATE` | DeepSeek `deepseek-chat` | `SECURITY_FAILURE_AND_SEMANTIC_BOUNDARY_REVIEWER` | 21,006 bytes / `d2297316da3e20c750f16119610d1b06c2fae98b84f21ce911ff84c4a4572f6b` |

候选 session ID 保留 PRE-21 前缀，因为它们是 PRE-21 manifest 已冻结内容；PRE-22 只决定
是否执行，不重写 lineage 或请求内容。

## Evidence

PRE-21 已证明：

```text
INPUT_HASHES_MATCHED=6/6
RESPONSE_SCHEMA_META_VALID=true
FIXTURE_CASES_MATCHED=13/13
POSITIVE_FIXTURES_ACCEPTED=3/3
NEGATIVE_FIXTURES_REJECTED=10/10
V0_2_COMPONENT_BINDINGS_MATCHED=4/4
MAX_V0_2_QUERY_BYTES=21010
INTERNAL_CAP_BYTES=24000
OFFLINE_RESPONSE_CONTRACT_PASS=true
LIVE_MODEL_REQUESTS_EXECUTED=0
LIVE_REVIEW_RECOMMENDATION_READY=true
LIVE_REVIEW_AUTHORIZED=false
```

内部 byte cap 只证明 TITMAS 自身请求预算满足，不声称是 provider 官方限制，也不证明
provider 一定接受请求。

## Agent Recommendation Gate

如果潜在 Agent developer 需要判断 Provider Adapter Profile 是否值得进入完整人工源文件
审查：

```text
MONOLITHIC_FULL_SOURCE_MODEL_REVIEW=NOT_RECOMMENDED
UNSCOPED_COMPACT_MODEL_REVIEW=NOT_RECOMMENDED
HASH_BOUND_COMPACT_TWO_ROLE_REVIEW=CONDITIONALLY_RECOMMENDED
```

不推荐前两种路径的原因：

1. PRE-19 monolithic request 已以 `query_too_large` 失败；
2. compact projection 省略完整 Schema constraints、case text 和历史材料；
3. 无 scope 契约会把 projection review 错写成 Profile review；
4. 单一 reviewer role 不能同时提供最低限度的 implementability 和 boundary 视角；
5. 模型接受不构成人工采纳、实现符合性或 provider support。

条件式推荐要求：

- 两个 reviewer role 使用 PRE-21 冻结的 exact query；
- 每个 session 最多一个 live request；
- 不 retry、不 fallback、不 silent downgrade、不 JSON repair；
- output 只按 compact response Schema 解析和验证；
- `review_scope=COMPACT_PROJECTION_ONLY`；
- `full_source_artifacts_reviewed_by_model=false`；
- 两个 session 独立记账；一个 provider 的 ordinary request/response failure 不取消另一个
  已授权的独立 session；
- shared integrity、authorization、secret-safety 或 request-hash failure 立即停止所有未执行
  session；
- composite PASS 要求两条响应都 parse、Schema 和 session binding 通过，且 verdict 都为
  `ACCEPT_COMPACT_REVIEW_FOR_FULL_SOURCE_HUMAN_REVIEW`；
- 即使 composite PASS，下一步也只能准备完整源文件人工审查。

## Exact Authorized Candidate Scope

PRE-22 的后续 Decision 只能授权：

1. 一个 frozen live-review plan 及其 Schema；
2. 一个 hash-bound input/authorization manifest 及其 Schema；
3. Kimi/Qianfan `kimi-k2.6` 一次 exact compact request；
4. DeepSeek `deepseek-chat` 一次 exact compact request；
5. 每个 session 的 normalized result record 及其 Schema；
6. composite validation result、execution receipt、报告和 cockpit synchronization；
7. 对成功 JSON 响应保存 compact response object；对失败响应只保存 failure class、状态、
   byte count、hash 和非敏感 provider error，不保存 raw provider envelope、usage、credential
   或 hidden reasoning。

不授权：

- full-source model review；
- full-source human review 的完成或替代；
- Profile adoption、implementation、conformance、certification 或 release；
- provider fallback、替代模型、第二次请求或输出修复；
- 任何 DBOS、SAEE、Adapter 或 Runtime 代码。

## Independent Session Failure Policy

两条 session 是独立、有界的审查输入：

- ordinary provider failure、timeout、rate limit、empty response、invalid JSON 或 Schema failure
  只终止并保留该 session，不触发 retry；
- 若另一 session 尚未执行且 shared preconditions 仍成立，则继续执行另一条 exact session；
- source/request hash mismatch、remote authorization drift、credential safety failure、scope
  contract drift 或 request assembly drift 属于 shared stop condition，所有未执行 session
  停止；
- composite result 对任一 incomplete/invalid/rejected session 必须失败关闭，不得用另一条
  PASS 替代。

该策略获得两个独立事实，不把“继续第二个 session”解释成 retry 或 fallback。

## Response and Persistence Boundary

允许保存：

- 符合 compact response Schema 的模型 JSON object；
- request hash、response hash、byte count、provider/model/session reference；
- parse、Schema、binding、criterion 和 verdict validation result；
- 失败分类及非敏感错误摘要。

禁止保存或输出：

- API key、credential、Authorization header；
- raw provider transport envelope；
- token usage 或计费 envelope；
- hidden chain-of-thought；
- invalid response 的全文自动修复版本；
- 把模型自报身份升级为 human reviewer、maintainer 或 authority。

## Preconditions

1. PRE-21 result、response Schema、fixtures 和 v0.2 manifest hash 匹配；
2. PRE-21 remote result baseline `a8f0f72a60d44a9ba6a151af2d1f6a92af13675b` 可追溯；
3. standing directive active；
4. 独立 PRE-22 Decision、machine record、plan 和 input manifest 已形成；
5. Decision/plan/input manifest 在目标远端分支验证；
6. Kimi/Qianfan callable tool 可用；
7. DeepSeek local credential variables 存在但不读取、输出或持久化 secret 值；
8. live request accounting 在执行前为 0。

## Success Conditions

```text
AUTHORIZED_SESSIONS=2
EXECUTED_SESSIONS=2
REQUESTS_PER_SESSION=1
RETRY_ATTEMPTS=0
FALLBACK_ATTEMPTS=0
JSON_REPAIR_ATTEMPTS=0
VALID_COMPACT_RESPONSES=2
ACCEPT_VERDICTS=2
COMPOSITE_COMPACT_REVIEW_PASS=true
FULL_SOURCE_HUMAN_REVIEW_STILL_REQUIRED=true
PROFILE_REVIEW_COMPLETED=false
PROFILE_ADOPTED=false
```

任一 provider/session 失败时仍必须产生可追溯结果，但：

```text
COMPOSITE_COMPACT_REVIEW_PASS=false
NEXT_ACTION=REMEDIATE_OR_STOP_BY_RECORDED_FAILURE
```

## Stop Conditions

- recommendation、Decision、plan、manifest 或 response Schema hash mismatch；
- remote authorization baseline 不等于本地 frozen baseline；
- reconstructed query byte count 或 SHA-256 不匹配；
- 请求第三个 provider/model、第二次调用、retry、fallback 或 repair；
- credential 被输出、写入仓库或发送到非目标 provider；
- response scope、source-review 声明或 session binding 不匹配；
- 把一条 session 的结果复制、推定或替代另一条；
- 把 compact review 升级为完整 Profile review、Adoption、Conformance、provider support、
  market/customer evidence、Authority、Permission、Certification 或 Release；
- 任何 DBOS/SAEE/Adapter implementation。

## False Effects

```text
AUTHORITY_CHANGED=false
OWNERSHIP_CHANGED=false
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

## Standing Directive Eligibility

本建议包含一个 exact option、两个清晰分离且各一次的 session、固定 query、provider/model、
preconditions、persistence boundary、stop conditions 和 false effects。动作属于 DBA/TITMAS
商业化标准路线内部受限 review，不是 outreach、implementation、commercial offer、
certification 或 release。

```text
STANDING_DIRECTIVE_REFERENCE=TITMAS-CS-STANDING-001
STANDING_DIRECTIVE_ELIGIBLE_CANDIDATE=true
AT_RECOMMENDATION_TIME_PRE22_DECIDED=false
AT_RECOMMENDATION_TIME_LIVE_REQUESTS_EXECUTED=0
```
