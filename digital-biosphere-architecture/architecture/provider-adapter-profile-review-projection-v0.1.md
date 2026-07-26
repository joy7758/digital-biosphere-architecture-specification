---
document_id: DBA-TITMAS-PROVIDER-ADAPTER-PROFILE-REVIEW-PROJECTION-0.1
title: TITMAS Provider Adapter Profile Compact Review Projection Candidate v0.1
title_zh: TITMAS Provider Adapter Profile 紧凑评审投影候选 v0.1
version: 0.1.0
status: compact-projection-candidate-not-reviewed
maturity: Development
decision_reference: CS-D02-PRE-20
review_scope: compact-projection-only
full_source_artifacts_reviewed_by_model: false
profile_review_completed: false
profile_adopted: false
---

# TITMAS Provider Adapter Profile Compact Review Projection Candidate v0.1

## Purpose

本文件是 PRE-18 Provider Adapter Conformance Profile candidate 的 source-bound compact
review aid（来源绑定紧凑评审辅助材料）。它把跨 6 个机器对象的评审重点投影为一个较小、
结构化、可由智能体读取的对象。

它不是原始 Profile 或 Schema 的替代品，不声称 lossless equivalence，不表示任何模型已读取
完整 source artifacts。

## Review Scope

未来如有独立授权，智能体只能对下列七项投影内容给出意见：

1. Interoperability；
2. Developer Implementability；
3. Normalized Request/Result Boundary；
4. Failure Taxonomy Completeness；
5. Semantic Non-elevation；
6. Privacy and Persistence Boundary；
7. Conformance Case Adequacy。

任何 review result 必须声明：

```text
REVIEW_SCOPE=COMPACT_PROJECTION_ONLY
FULL_SOURCE_ARTIFACTS_REVIEWED_BY_MODEL=false
PROFILE_REVIEW_COMPLETED=false
```

## Projected Contract

机器投影见
[`provider-adapter-profile-review-projection.v0.1.json`](provider-adapter-profile-review-projection.v0.1.json)。
它保留：

- provider-neutral purpose；
- normalized request/result 字段集合；
- 传输、语义答案、direct JSON 与 full Schema 状态分离；
- maximum unwrap depth 1；
- no automatic retry/fallback/repair/rewrite；
- 9 个 failure class；
- 20 个未执行 conformance case 的 ID、stage 和 expected failure class；
- claim non-elevation 与 conformance entry requirements；
- reviewer output 的最小结构。

## Omitted Material

为控制请求尺寸，投影明确省略：

- 人类文档的重复解释、历史叙事和例子；
- JSON Schema 的逐关键词、条件分支和错误消息全文；
- 每个 conformance case 的完整 stimulus/assertions 文本；
- PRE-14 至 PRE-19 的历史报告正文；
- provider raw envelope、usage 或 hidden reasoning。

这些省略项均在机器对象的 `omitted_material_register` 中登记。省略意味着未来模型没有评审
对应全文，不能把 compact review 升级为 full-source review。

## Size and Provider Boundary

```text
TITMAS_INTERNAL_COMPACT_REQUEST_CAP_BYTES=24000
PROVIDER_DECLARED_LIMIT_BYTES=UNKNOWN
CAP_IS_PROVIDER_LIMIT_CLAIM=false
```

24,000 bytes 是 TITMAS 内部 fail-closed cap，不是任何 provider 的官方限制或支持声明。

## Non-effects

```text
PROJECTION_CREATED=true
LIVE_MODEL_REQUESTS_EXECUTED=0
PROFILE_REVIEW_COMPLETED=false
PROFILE_ADOPTED=false
ADAPTER_IMPLEMENTATION_CREATED=false
CONFORMANCE_EXECUTED=false
PROVIDER_SUPPORTED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
```
