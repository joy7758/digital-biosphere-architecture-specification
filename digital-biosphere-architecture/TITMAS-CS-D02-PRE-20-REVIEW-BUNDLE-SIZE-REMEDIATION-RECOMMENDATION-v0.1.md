---
document_id: DBA-TITMAS-CS-D02-PRE-20-REVIEW-BUNDLE-SIZE-REMEDIATION-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-20 Review Bundle Size Remediation Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-20 评审包尺寸修复建议 v0.1
version: 0.1.0
status: exact-recommendation-prepared-not-decided
maturity: Development
decision_reference: CS-D02-PRE-20
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
implementation_authorized: false
live_model_request_authorized: false
profile_adopted: false
valid_problem_records: 0
cs_g0_pass: false
---

# TITMAS CS-D02 PRE-20 Review Bundle Size Remediation Recommendation v0.1

## 1. Recommendation

```text
RECOMMENDED_OPTION=AUTHORIZE_OFFLINE_HASH_BOUND_COMPACT_REVIEW_PROJECTION_CANDIDATE_ONLY
PRIMARY_REPOSITORY=digital-biosphere-architecture
TARGET=PRE18_PROVIDER_ADAPTER_PROFILE_CANDIDATE_REVIEW_MATERIAL
LIVE_MODEL_REQUESTS_MAX=0
PROVIDER_NETWORK_REQUESTS_MAX=0
IMPLEMENTATION_AUTHORIZED=false
```

建议建立一个 provider-neutral、hash-bound、size-bounded 的 Compact Review Projection
candidate（紧凑评审投影候选）及离线 completeness/coverage rehearsal。该动作只修复评审材料
的可传输性和智能体可读性，不重新执行 PRE-19，不评审或采纳 Profile，不创建 Adapter。

## 2. Evidence and Problem

PRE-19 在远端授权基线核验后，以冻结顺序拼接 8 个 hash-matched 组件：

```text
KIMI_QUERY_BYTES=50962
KIMI_QUERY_SHA256=90a84a4348e3b2499ed6dd3fb14a17b42e48066d1205d3ba445537b0e230d2ce
KIMI_PROVIDER_ERROR=query_too_large
QUALIFYING_REVIEWS=0/2
COMPOSITE_RESULT=INCOMPLETE_FAIL_CLOSED
```

来源绑定：

| artifact | SHA-256 |
|---|---|
| `commercialization-standards-provider-adapter-profile-review/PRE-19-PROVIDER-ADAPTER-PROFILE-CANDIDATE-REVIEW-RESULT-v0.1.md` | `18ce8f4ae8b62409ca08db5c6514c53861a07491e8a1f7a2a29c62da2aac41ba` |
| `commercialization-standards-provider-adapter-profile-review/composite-review-result.v0.1.json` | `71a9b1070fddb9d64c505c45967d461c22f48f8a248b3155e93c118d518bf454` |
| `commercialization-standards-provider-adapter-profile-review/execution-receipt.v0.1.json` | `b685d2996fe6bae830510c2eee3b50800948c83a78da2d413d7a25979db6d45e` |

PRE-19 证明当前完整拼接方式无法通过当前 Kimi/Qianfan 通道；它没有证明 Profile 内容错误，
也没有测得 provider 的精确最大请求尺寸。

## 3. Pre-development Agent Recommendation Gate

问题：

> 如果潜在 Agent developer 要评审或实现 Provider Adapter，智能体是否会推荐当前 50,962-byte
> 单体评审包？

结论：

```text
CURRENT_MONOLITHIC_BUNDLE_RECOMMENDATION=NOT_RECOMMENDED
REMEDIATED_COMPACT_PROJECTION_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
```

不推荐当前形式的原因：

1. 当前已观察到 provider 明确拒绝；
2. 单体包把人类说明、机器对象、完整 Schema 和 20-case catalog 重复嵌入同一请求；
3. 智能体无法在传输失败时理解、引用或评审材料；
4. 任意人工删减会破坏 exact input lineage；
5. 一个摘要如果没有 coverage/equivalence 证明，容易被误当成完整候选。

可修正问题：

- 建立有明确字段和 source path 的 normative review projection；
- 对每个投影断言绑定 source artifact、JSON Pointer/section 和 SHA-256；
- 建立 coverage matrix，证明所有声明评审 criteria 均有至少一个来源；
- 单独保留 omitted-material register，不把省略材料隐藏为“已覆盖”；
- 使用固定 local byte cap，但明确该 cap 是 TITMAS 内部约束，不是 provider limit 事实；
- 离线只验证 projection structure、source binding、coverage 和 size，不验证 reviewer verdict。

条件式推荐的剩余条件：

```text
SOURCE_HASHES_MATCH=true
DECLARED_CRITERIA_COVERAGE=100_PERCENT
OMITTED_MATERIAL_REGISTER_PRESENT=true
PROJECTION_BYTE_CAP_MET=true
SUMMARY_EQUIVALENCE_NOT_CLAIMED=true
FULL_PROFILE_REVIEW_NOT_CLAIMED=true
```

## 4. Exact Authorized Candidate Scope

如采用本建议，PRE-20 只可创建：

1. `architecture/provider-adapter-profile-review-projection-v0.1.md`；
2. `architecture/provider-adapter-profile-review-projection.v0.1.json`；
3. 对应 JSON Schema；
4. source-binding and coverage matrix；
5. compact review request manifest candidate；
6. offline validation fixtures/result；
7. result report、execution receipt 和 cockpit synchronization。

投影必须覆盖下列七个 review criteria：

```text
INTEROPERABILITY
DEVELOPER_IMPLEMENTABILITY
NORMALIZED_REQUEST_RESULT_BOUNDARY
FAILURE_TAXONOMY_COMPLETENESS
SEMANTIC_NON_ELEVATION
PRIVACY_AND_PERSISTENCE_BOUNDARY
CONFORMANCE_CASE_ADEQUACY
```

## 5. Size Contract

PRE-20 建议采用：

```text
TITMAS_INTERNAL_COMPACT_REQUEST_CAP_BYTES=24000
PROVIDER_DECLARED_LIMIT_BYTES=UNKNOWN
CAP_IS_PROVIDER_LIMIT_CLAIM=false
```

24,000 bytes 是项目内部 fail-closed cap，用于显著低于已失败的 50,962-byte 请求，不表示
Kimi、Qianfan、DeepSeek 或其他 provider 的官方限制。若投影超过该 cap，离线验证失败，
不得自动删除内容或改变 coverage。

## 6. Projection Truth Boundary

Compact Review Projection：

- 是 source-bound review aid；
- 不是 PRE-18 artifact 的替代品；
- 不是 lossless equivalence 证明；
- 不是完整 Schema conformance execution；
- 不是 Profile review verdict；
- 不是 Profile Adoption 或 Implementation Authorization。

未来模型只能对 projection 的明确内容给出有界意见。任何结论必须标注：

```text
REVIEW_SCOPE=COMPACT_PROJECTION_ONLY
FULL_SOURCE_ARTIFACTS_REVIEWED_BY_MODEL=false
```

## 7. Preconditions

执行前必须同时证明：

1. PRE-19 result、composite result 与 receipt hash 匹配；
2. PRE-18 Profile、machine Profile、两个 descriptor Schema、failure taxonomy、
   conformance case catalog 和 reviewer response Schema hash 匹配；
3. `TITMAS-CS-STANDING-001` 仍 active；
4. 独立 PRE-20 Decision/Authorization Record 已形成；
5. Decision、frozen offline plan 和 source manifest 已提交并在远端验证；
6. live/provider requests 保持 0；
7. 所有生成物只位于 DBA。

任一条件缺失：

```text
STANDING_DIRECTIVE_APPLICABLE=false
PRE20_EXECUTION_STARTED=false
```

## 8. Stop Conditions

必须失败关闭：

- source hash mismatch；
- criterion 无 source coverage；
- projection field 无 source pointer；
- omitted material 未登记；
- compact request 超过 24,000 bytes；
- 投影声称 lossless/full-source equivalence；
- 请求 provider 或 live model；
- 自动删减、retry、fallback 或 repair；
- 将 offline validation 升级为 Review、Adoption、Implementation、Conformance 或 Provider Support。

## 9. False Effects

```text
AUTHORITY_CHANGED=false
OWNERSHIP_CHANGED=false
PROFILE_REVIEW_COMPLETED=false
PROFILE_ADOPTED=false
PROFILE_MATURITY_PROMOTED=false
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

## 10. Standing Directive Eligibility

本建议只有一个 exact option，明确 primary repository、target artifacts、preconditions、
false effects 和 stop conditions；动作属于 architecture/specification governance、
offline internal validation 及 path-scoped commit/push。

因此，在独立 Decision Record 形成并验证后：

```text
STANDING_DIRECTIVE_REFERENCE=TITMAS-CS-STANDING-001
STANDING_DIRECTIVE_ELIGIBLE_CANDIDATE=true
AT_RECOMMENDATION_TIME_PRE20_DECIDED=false
```
