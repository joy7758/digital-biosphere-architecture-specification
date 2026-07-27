---
document_id: DBA-TITMAS-CE-G11B-IMMUTABLE-CANDIDATE-EXTERNAL-ATTESTATION-RECOMMENDATION-0.1
title: TITMAS CE-G11B Immutable Candidate and External Validation Attestation Recommendation v0.1
version: 0.1.0
status: exact-recommendation-agent-review-pending-decision-pending
maturity: Development
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G11B Immutable Candidate and External Validation Attestation Recommendation v0.1

## Problem

Atomic integration Recommendation 被提交后，governance head 从：

```text
before_recommendation=ef0b40e99db90a47a29c9322d771ea9611d3cbaf
after_recommendation=391f45a8496025371d07ea691e5851ab0598d33e
```

因此原先观测的 canonical + governance merge tree `88e8cdb...` 不再是当前候选。

如果把 merge-tree validation result（验证结果）继续提交到同一候选分支：

```text
candidate C0
  → add Decision = C1
  → validate C1
  → add Result = C2
  → C2 is unvalidated
  → validate C2
  → add Result = C3
  → ...
```

这形成 validation self-reference（验证自引用），无法得到同时包含自身最终证明且 SHA
不变的普通 Git commit。

## Recommendation

采用 **Option A：把 validation Decision 作为 candidate 的最后一个 commit，随后冻结
candidate ref；验证结果写入独立 evidence ref，并把它作为 replacement PR 的 external
attestation（外部证明），不再推进 candidate head**。

该模式等同于常规 CI：被测试的 commit 保持不可变，test report 存放在 commit 外部并
通过 SHA 绑定。External 不表示公开服务或外部 Authority，只表示不写入被验证 commit。

## Option A workflow（推荐）

1. 在 governance branch 提交 current merge-tree Validation Decision；
2. 该 Decision commit 成为 immutable candidate commit；
3. 记录：
   - candidate commit；
   - current canonical commit；
   - merge base；
   - exact merge tree；
4. 创建独立 evidence branch，例如
   `codex/ce-g11b-atomic-integration-evidence`，base 为 candidate commit；
5. 在 evidence branch 记录 write-ahead execution、Result、Report 和 cockpit mirror；
6. 验证 disposable worktree 的 exact candidate merge tree；
7. candidate branch 在 Decision commit 后必须保持不变；
8. PASS 后创建 replacement Draft PR：
   - base: canonical ref；
   - head: immutable candidate ref；
   - PR body 绑定 evidence branch、Result SHA 和 tested merge tree；
9. independent PR review 必须确认 candidate SHA 未漂移；
10. PR #22 closure 与 replacement merge 继续分别独立 Decision。

Evidence branch 不自动进入 replacement PR。它保留 merge admission proof（合并准入证明），
之后是否将 evidence records 归档进 canonical documentation 需另行决定。

## Rejected options

### Option B — Result committed back into candidate（拒绝）

产生新的、未验证 candidate SHA，形成无限递归。

### Option C — Validate before Decision commit（拒绝）

Decision 本身会改变候选 tree，最终 PR head 未被实际验证。

### Option D — Treat prior R6 PASS as validation of current governance head（拒绝）

R6 只验证 canonical + CE head tree，不覆盖 71+ governance-only paths。

### Option E — Merge first and record result after（拒绝）

把验证从 admission gate 降级为事后记录。

## Required immutability contract

```text
candidate_ref=codex/ce-g11b-phase-b-integration-governance
candidate_commit=frozen_after_validation_decision
candidate_commits_after_freeze=0
evidence_ref_distinct_from_candidate=true
result_binds_candidate_commit=true
result_binds_canonical_commit=true
result_binds_merge_tree=true
replacement_pr_head_equals_candidate_commit=true
replacement_pr_created_only_after_pass=true
pr22_closure_separate=true
merge_decision_separate=true
```

## Review gate

Exact `qwen3.7-max` 必须返回：

```text
verdict=RECOMMENDED
selected_option=A
self_reference_problem_real=true
immutable_candidate_required=true
decision_as_final_candidate_commit=true
external_attestation_sha_bound=true
evidence_branch_not_candidate=true
replacement_pr_after_pass_only=true
candidate_drift_fails_closed=true
pr22_closure_separate=true
merge_decision_separate=true
no_current_remote_mutation=true
blocking_reasons=[]
required_corrections=[]
```

## Caps and non-claims

```text
RECOMMENDATION_REVIEW_REQUESTS_MAX=1
VALIDATION_DECISION_RECORDED=false
EVIDENCE_BRANCH_CREATED=false
CANDIDATE_FROZEN=false
VALIDATION_EXECUTED=false
REPLACEMENT_PR_CREATED=false
PR_22_MUTATED=false
MERGES=0
RELEASES=0
DEPLOYMENTS=0
STANDARD_READY=false
```
