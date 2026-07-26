---
document_id: DBA-TITMAS-CS-D02-PRE-47-EXACT-SEQUENTIAL-AGENT-REVIEW-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-47 Exact Sequential Agent Review Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-47 精确顺序智能体审查建议 v0.1
version: 0.1.0
status: exact-recommendation-ready-not-decided
maturity: Development
recommendation_id: CS-D02-PRE-47
primary_repository: digital-biosphere-architecture
network_requests_authorized: false
credential_reads_authorized: false
implementation_authorized: false
---

# TITMAS CS-D02 PRE-47 Exact Sequential Agent Review Recommendation v0.1

## Recommendation

```text
RECOMMENDATION=AUTHORIZE_EXACT_FOUR_SESSION_SEQUENTIAL_QIANFAN_AGENT_REVIEW_WITH_FROZEN_PRE46_CONTRACT
PRIMARY_REPOSITORY=digital-biosphere-architecture
SOURCE_DBA_COMMIT=95f771d45b318152a5fda868f7bbd4f6d3218f2d
TARGET_REPOSITORY=https://github.com/joy7758/titmas-integrations.git
TARGET_BRANCH=codex/rb0-governance-baseline
TARGET_HEAD=f80629364752c465316b9d1238fe5447a88565ca
REQUEST_MANIFEST_SHA256=c6af3cf2f6b7e4d57950271cc1ed028bad16b38db5016737035aa43ceef5c984
PLAN_SHA256=0c14371dbc0484b0a96b4ecd585d3568f58ca9d2b42b27144c3188fb3a16e6be
REVIEWER_SESSIONS_MAX=4
PARALLEL_REQUESTS_MAX=1
NETWORK_REQUESTS_MAX=4
CREDENTIAL_READS_MAX=1
TARGET_REPOSITORY_FILES_MODIFIED_MAX=0
IMPLEMENTATION_AUTHORIZED=false
```

PRE-44 的并发四会话审查只有 `1/4` qualifying，冻结门槛为 `3/4`。PRE-45 没有
伪造失败因果；PRE-46 只在离线状态修订并验证了更短、顺序、直接 JSON、无修复的契约。

PRE-47 只建议对该 exact contract 执行一次新的、单路顺序四会话审查。它不重试
PRE-44，不删除 PRE-44 失败，也不降低任何阈值。

## Frozen Sequence

| sequence | session | exact model | reviewer profile | requests max |
|---:|---|---|---|---:|
| 1 | `PRE47-KIMI-AGENT-DEVELOPER` | `kimi-k2.6` | `AGENT_DEVELOPER` | 1 |
| 2 | `PRE47-GLM-RECOMMENDER-AGENT` | `glm-5.2` | `RECOMMENDER_AGENT` | 1 |
| 3 | `PRE47-KIMI-INTEGRATION-MAINTAINER` | `kimi-k2.6` | `INTEGRATION_MAINTAINER` | 1 |
| 4 | `PRE47-GLM-SECURITY-BOUNDARY-REVIEWER` | `glm-5.2` | `SECURITY_BOUNDARY_REVIEWER` | 1 |

每个会话结束后必须先写入、验证并保留该会话的 sanitized result，才能开始下一个会话。
不允许并发，也不允许为失败会话发起替代请求。

## Exact Request Contract

```text
ENDPOINT=https://qianfan.baidubce.com/v2/chat/completions
CREDENTIAL_SOURCE=QIANFAN_API_KEY_ENVIRONMENT_ONLY
REQUEST_TIMEOUT_MS=90000
RESPONSE_FORMAT_PARAMETER_INCLUDED=false
RETRY=0
FALLBACK=0
MODEL_SUBSTITUTION=0
ALIAS_INFERENCE=0
JSON_REPAIR=0
WEB_SEARCH=0
REVIEWER_TOOL_CALLS=0
```

`glm-5.2` 和 `kimi-k2.6` 的 exact-model structured-output support 继续为
`UNKNOWN_NOT_ADOPTED`。通用 endpoint 存在 `response_format` 不构成这两个 exact model
支持的证据，因此请求中不添加该参数。

returned model 必须存在且与 requested model 逐字节一致；否则该会话不 qualifying。
仅接受整个 message content 的直接 JSON parse，不去 Markdown、不去 code fence、不抽取、
不修复、不语义改写。

## Frozen Artifacts

PRE-47 冻结七个 planning artifacts：

1. `pre47-exact-sequential-agent-review-request-manifest.v0.1.json`
   (`c6af3cf2f6b7e4d57950271cc1ed028bad16b38db5016737035aa43ceef5c984`)；
2. `pre47-exact-sequential-agent-review-request-manifest.schema.v0.1.json`
   (`0e0a3486f82133b8040fa7c053b7f44c6422e5dee02c1f348ec0ebb068a104f6`)；
3. `pre47-exact-sequential-agent-review-plan.v0.1.json`
   (`0c14371dbc0484b0a96b4ecd585d3568f58ca9d2b42b27144c3188fb3a16e6be`)；
4. `pre47-exact-sequential-agent-review-plan.schema.v0.1.json`
   (`b0d5b2cec211c6aec685dd1cbaaa13dbad2992c4df6afc620a88324a9a48a6d5`)；
5. `pre47-exact-sequential-agent-review-session-result.schema.v0.1.json`
   (`f74e7f6ad50515920e8b49449d88a5e90036f15739e5228994d0e1c08a09705d`)；
6. `pre47-exact-sequential-agent-review-validation-result.schema.v0.1.json`
   (`00beaef790438a31531ff96eb78b1da1ac06b588c0585e9230c0e8aa254d5ec9`)；
7. `pre47-exact-sequential-agent-review-execution-receipt.schema.v0.1.json`
   (`e964873c84369a016b9fc24e4e9887de09b9d64a1684c43fcf3d0e4fe2ba6a99`)。

它们引用 PRE-46 的 query、response schema 和 contract，但不会改写 PRE-46 或 PRE-44
历史。

## Frozen Thresholds

```text
QUALIFYING_SESSIONS_MIN=3
RECOMMENDED_OR_CONDITIONAL_MIN=2
WOULD_RECOMMEND_MIN=2
WOULD_REUSE_MIN=2
AUTHORITY_SAFETY_FAILURES_MAX=0
```

- `PASS`：只允许形成独立 RB1 implementation recommendation；
- `FAIL`：返回 RB1 planning packet 修订；
- `BLOCKED`：qualifying 会话不足，保留 Provider 失败且不重试。

阈值不得在查看任何 PRE-47 返回后调整。

## Sanitized Persistence Boundary

允许保存：

- session、sequence、requested/returned model 与 reviewer profile；
- query/payload byte count 和 SHA-256；
- HTTP status、response byte count 和 raw-envelope 单向 SHA-256；
- Schema-valid advisory response；
- 不含 Provider body 的短失败类别与错误标识。

禁止保存：

- credential、Authorization header；
- raw Provider envelope、error body、usage；
- prompt、hidden reasoning；
- Schema-invalid 内容的语义；
- 任何抽取、修复或替代结果。

## Result Outputs After Independent Decision

独立 Decision 生效后，最多新增：

1. 四个顺序 session results；
2. `pre47-exact-sequential-agent-review-validation-result.v0.1.json`；
3. `pre47-exact-sequential-agent-review-execution-receipt.v0.1.json`；
4. `PRE-47-EXACT-SEQUENTIAL-AGENT-REVIEW-RESULT-v0.1.md`。

目标 `titmas-integrations` 仓库只读，不能写文件、提交、合并或发布。

## Non-effects

```text
PRE44_HISTORY_CHANGED=false
PRE44_GATE_PASS_CHANGED=false
RB1_IMPLEMENTATION_RECOMMENDATION_ALLOWED=false_BEFORE_RESULT
RB1_IMPLEMENTATION_AUTHORIZED=false
TARGET_REPOSITORY_MODIFIED=false
PACKAGE_CREATED=false
SOURCE_CREATED=false
TESTS_CREATED=false
PROVIDER_SUPPORTED=false
CONFORMANCE_EXECUTED=false
RUNTIME_CREATED=false
RELEASE_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
```

即使 PRE-47 达到阈值，也不产生 implementation、package、provider correctness、
conformance、Human Customer Evidence、Market Adoption、release 或 commercial
availability。

## Stop Conditions

任一 source/target/artifact digest、session order、query/payload binding、Schema、budget、
threshold 或 persistence boundary 漂移；credential 缺失或可能被输出／持久化；需要并发、
retry、fallback、model substitution、alias inference、JSON repair、response-format
推断、raw-envelope persistence；或需要 target write、package、source、tests、Runtime、
DBOS/SAEE change、merge、PR、tag、release、deployment、Certification、Production、
customer 或 commercial claim 时，立即 fail closed。

## Standing Directive Assessment

该建议只有一个 exact option，固定 source/target、四个顺序会话、两个 exact model、请求
bytes/digests、预算、阈值、sanitized sink、effects 和 stop rules，满足
`TITMAS-CS-STANDING-001` 候选条件。执行前仍须生成并远端验证独立 Decision Record。
