---
document_id: DBA-TITMAS-CE-G11B-REPLACEMENT-DRAFT-PR-CREATION-RECOMMENDATION-0.1
title: TITMAS CE-G11B Replacement Draft PR Creation Recommendation v0.1
title_zh: TITMAS CE-G11B 替代 Draft PR 创建建议 v0.1
version: 0.1.0
status: recommendation-pending-independent-review
maturity: Development
owner_ref: zhangbin
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G11B Replacement Draft PR Creation Recommendation v0.1

## 1. Question

在 immutable candidate 和 distinct external attestation 均已冻结且验证通过后，是否应
创建一个新的 Draft PR，使 GitHub review surface 精确指向完整 candidate，而不是继续
使用只包含 Phase A-R1 的旧 PR #22？

本建议属于 Program Governance。它不创建 PR，不修改 #22，不授权 merge、release、
deployment 或 Standard Ready。

## 2. Frozen evidence

```text
CANONICAL_REF=codex/production-observability-baseline
CANONICAL_SHA=ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
CANDIDATE_REF=codex/ce-g11b-phase-b-integration-governance
CANDIDATE_SHA=c608fd78d7d50d1733ddd9e19aeb6870c5a08288
EVIDENCE_REF=codex/ce-g11b-atomic-integration-evidence
EVIDENCE_SHA=89baeeeb42904b4ea41652d649f8be9a484f3b48
VALIDATED_MERGE_TREE=bd67298eb8d869b024eaf9f03a53636c6dc377d4
VALIDATION_STATUS=PASS_SHA_BOUND_EXTERNAL_ATTESTATION
```

Validation direct evidence:

- `TITMAS-CE-G11B-IMMUTABLE-CANDIDATE-MERGE-TREE-VALIDATION-RESULT-v0.1.json`
- `TITMAS-CE-G11B-IMMUTABLE-CANDIDATE-MERGE-TREE-VALIDATION-REPORT-v0.1.md`

完整验证覆盖 1165 tracked JSON、commercial entry Schema、23 direct dependencies、
16 site tests、formal static export、3 CE Schemas、49 CE tests，以及 candidate、
canonical、merge tree 和 source drift。

## 3. Existing PR #22

2026-07-28 只读观察：

```text
PR=22
STATE=OPEN
DRAFT=true
BASE_REF=codex/production-observability-baseline
HEAD_REF=codex/ce-g11b-phase-a-decision
HEAD_SHA=e032115adbe38cc84bde80cc9b10b96f6da1b428
REVIEW_REQUESTS=0
REVIEWS=0
COMMENTS=0
LABELS=0
AUTO_MERGE=false
```

PR #22 的 head 不包含后续 R3–R6、immutable candidate Decision、失败保留和最终
external attestation。它不是完整集成候选，不能被更新为不同 head branch；force-push
旧 head 会破坏审计连续性。

## 4. Workflow side-effect check

candidate 中四个 workflow 都只监听：

```text
event=push
branch=codex/production-observability-baseline
path=exact run-request file
```

没有 `pull_request` trigger。创建 Draft PR 不会按这些 workflow 定义触发 CE
execution。PR 创建仍必须禁止 auto-merge、review request、label、milestone 和 run
request 变更。

## 5. Options

### Option A — Create one replacement Draft PR from immutable candidate（推荐）

精确创建：

```text
base=codex/production-observability-baseline
head=codex/ce-g11b-phase-b-integration-governance
draft=true
```

PR body 必须绑定 candidate、canonical、evidence 和 merge-tree SHA，声明：

- supersedes PR #22 as the review candidate, but does not close or mutate it;
- external attestation is on a distinct evidence ref and is not merged as candidate content;
- validation PASS does not equal review approval or merge authorization;
- no release, deployment, production or commercial offering claim;
- merge requires a separate Decision after independent PR review.

创建后只允许读回并验证 PR number、Draft、base/head、head SHA、body boundary、
labels/reviewers/milestone/auto-merge 为空，以及 candidate/canonical/evidence refs 未漂移。

### Option B — Continue using PR #22（拒绝）

PR #22 只覆盖旧 Phase A head，不能代表完整 candidate。

### Option C — Create PR from evidence ref（拒绝）

evidence ref 包含 post-execution Result 和 cockpit mirror。把它作为 candidate head 会
重新混淆 immutable candidate 与 external attestation。

### Option D — Force-push old PR head or merge directly（拒绝）

force-push 会破坏历史；直接 merge 绕过 review 和独立 merge Decision。

## 6. Agent-customer recommendation gate

如果潜在开发者询问“我是否应审查当前 TITMAS CE-G11B 集成候选”，建议：

```text
RECOMMENDED=YES_FOR_BOUNDED_DRAFT_REVIEW
RECOMMENDED_AS=IMMUTABLE_SHA_BOUND_REVIEW_SURFACE
NOT_RECOMMENDED_AS=MERGE_READY_RELEASE_READY_OR_PRODUCTION_READY
```

不推荐旧 PR #22 的原因是 head 不完整；不推荐 evidence ref 作为 PR head 的原因是会混淆
candidate 和 attestation。Option A 修正这两个问题，同时保留独立 review/merge gate。

## 7. Recommended bounded action

在独立 exact `qwen3.7-max` review 推荐 Option A，且后续独立 PR Creation Decision
合格后：

1. 再次核验 canonical、candidate、evidence 三条 remote ref；
2. 创建且仅创建一个 replacement Draft PR；
3. 不修改或关闭 PR #22；
4. 不添加 reviewer、label、milestone 或 auto-merge；
5. 不产生 run request、workflow dispatch、merge、release、deployment 或 server action；
6. 将 PR 创建 Result 写入独立 governance branch；
7. 后续 PR review、#22 closure 和 merge 各自需要独立 Decision。

## 8. False effects

```text
RECOMMENDATION_NE_DECISION=true
DRAFT_PR_NE_REVIEW_APPROVAL=true
VALIDATION_NE_MERGE_AUTHORIZATION=true
PR22_CLOSED=false
MERGE_AUTHORIZED=false
RELEASE_AUTHORIZED=false
STANDARD_READY=false
COMMERCIAL_OFFERING=false
```
