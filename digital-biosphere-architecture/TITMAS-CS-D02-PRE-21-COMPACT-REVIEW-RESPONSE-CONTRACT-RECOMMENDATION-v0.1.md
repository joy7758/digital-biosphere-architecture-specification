---
document_id: DBA-TITMAS-CS-D02-PRE-21-COMPACT-REVIEW-RESPONSE-CONTRACT-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-21 Compact Review Response Contract Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-21 紧凑评审响应契约建议 v0.1
version: 0.1.0
status: exact-recommendation-prepared-not-decided
maturity: Development
decision_reference: CS-D02-PRE-21
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
live_model_request_authorized: false
profile_review_completed: false
profile_adopted: false
---

# TITMAS CS-D02 PRE-21 Compact Review Response Contract Recommendation v0.1

## Recommendation

```text
RECOMMENDED_OPTION=AUTHORIZE_OFFLINE_COMPACT_REVIEW_RESPONSE_CONTRACT_AND_V0_2_REQUEST_MANIFEST_CANDIDATE_ONLY
PRIMARY_REPOSITORY=digital-biosphere-architecture
LIVE_MODEL_REQUESTS_MAX=0
PROVIDER_NETWORK_REQUESTS_MAX=0
IMPLEMENTATION_AUTHORIZED=false
```

建议建立一个只适用于 `COMPACT_PROJECTION_ONLY` 的 reviewer response Schema candidate、
positive/negative fixtures、离线 validation result 和包含该 Schema 的 compact request
manifest v0.2 candidate。

PRE-21 不执行 live review，也不重新解释 PRE-19。

## Evidence

PRE-20 已证明：

```text
OFFLINE_REMEDIATION_PASS=true
SOURCE_HASHES_MATCHED=10/10
POINTERS_RESOLVED=40/40
REVIEW_CRITERIA_COVERED=7/7
MAX_COMPACT_QUERY_BYTES=13995
INTERNAL_CAP_BYTES=24000
LIVE_REVIEW_READY=false
```

阻塞原因是 PRE-19 full-profile reviewer Schema 没有表达：

```text
REVIEW_SCOPE=COMPACT_PROJECTION_ONLY
FULL_SOURCE_ARTIFACTS_REVIEWED_BY_MODEL=false
```

直接复用会使模型输出看似评审了完整 Profile。

## Agent Recommendation Gate

如果潜在 Agent developer 需要消费 compact review response：

```text
LEGACY_FULL_PROFILE_RESPONSE_SCHEMA_FOR_COMPACT_REVIEW=NOT_RECOMMENDED
EXPLICIT_COMPACT_SCOPE_RESPONSE_SCHEMA=CONDITIONALLY_RECOMMENDED
```

不推荐旧 Schema 的原因：

1. 无法记录模型只读取 projection；
2. 无法记录 omitted material 未被读取；
3. `ACCEPT_FOR_HUMAN_ADOPTION_REVIEW` 会过早跳过 full-source human review；
4. response hash 不能绑定 projection、coverage 和 source manifest；
5. 无法区分 compact projection review 与 Profile review。

条件式推荐要求：

- `review_scope` 固定为 `COMPACT_PROJECTION_ONLY`；
- `full_source_artifacts_reviewed_by_model=false`；
- `profile_review_completed=false`；
- `profile_adopted=false`；
- reviewed projection、coverage matrix 和 source manifest hash 全部固定；
- 七个 criterion 恰好各出现一次；
- `ACCEPT` 只允许进入 `PREPARE_FULL_SOURCE_HUMAN_REVIEW`；
- elevation、missing scope、wrong hash、duplicate criterion 和 verdict inconsistency fixtures
  必须拒绝；
- v0.2 assembled request 继续满足 24,000-byte internal cap。

## Exact Candidate Scope

授权候选仅包括：

1. `architecture/schemas/provider-adapter-compact-review-response.schema.v0.1.json`；
2. `commercialization-standards-provider-adapter-profile-review-remediation/compact-response-schema-fixtures.v0.1.json`；
3. fixture Schema；
4. `compact-review-request-manifest.v0.2.json` 及 Schema；
5. offline response-contract validation result 及 Schema；
6. result report、execution receipt 和 cockpit synchronization。

## Required Response Semantics

允许 verdict：

```text
ACCEPT_COMPACT_REVIEW_FOR_FULL_SOURCE_HUMAN_REVIEW
RETURN_FOR_REVISION
REJECT
```

规则：

- ACCEPT：七项全部 `PASS`，required changes 和 blockers 都为空；
- RETURN：至少一个 `CHANGES_REQUIRED` 且 required changes 非空；
- REJECT：至少一个 `BLOCKER` 且 blockers 非空；
- 无论 verdict 为何，`PROFILE_REVIEW_COMPLETED=false`、`PROFILE_ADOPTED=false`。

## Size Boundary

v0.2 request 必须包含 compact response Schema 的 canonical JSON，以便智能体知道完整输出契约。

```text
TITMAS_INTERNAL_COMPACT_REQUEST_CAP_BYTES=24000
PROVIDER_DECLARED_LIMIT_BYTES=UNKNOWN
CAP_IS_PROVIDER_LIMIT_CLAIM=false
```

若加入 Schema 后任一候选请求超过 24,000 bytes，则 PRE-21 失败关闭，不能自动删除 Schema
字段或 projection coverage。

## Preconditions

1. PRE-20 result、projection、coverage matrix、v0.1 request manifest 和 receipt hash 匹配；
2. PRE-20 remote result baseline 可追溯；
3. standing directive active；
4. 独立 PRE-21 Decision 与 offline plan 已形成；
5. Decision/plan/input manifest 在远端验证；
6. live/provider request 保持 0。

## Stop Conditions

- source hash mismatch；
- response Schema 允许 full-source review claim；
- response Schema 允许 Profile review/adoption elevation；
- 七项 criterion 不唯一或不完整；
- verdict consistency fixtures 未全部匹配；
- v0.2 request 超过 24,000 bytes；
- 请求任何 live model/provider；
- retry、fallback、repair 或隐藏删减；
- 将 Schema rehearsal 升级为 live review、Profile review、Adoption 或 Conformance。

## False Effects

```text
AUTHORITY_CHANGED=false
OWNERSHIP_CHANGED=false
LIVE_REVIEW_EXECUTED=false
COMPACT_PROJECTION_REVIEW_COMPLETED=false
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

本建议包含一个 exact option、明确 scope、inputs、outputs、preconditions、stop conditions
和 false effects，属于 DBA architecture/specification governance 与 offline internal validation。

```text
STANDING_DIRECTIVE_REFERENCE=TITMAS-CS-STANDING-001
STANDING_DIRECTIVE_ELIGIBLE_CANDIDATE=true
AT_RECOMMENDATION_TIME_PRE21_DECIDED=false
```
