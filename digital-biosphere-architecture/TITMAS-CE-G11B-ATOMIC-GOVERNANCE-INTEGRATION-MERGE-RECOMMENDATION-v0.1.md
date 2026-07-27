---
document_id: DBA-TITMAS-CE-G11B-ATOMIC-GOVERNANCE-INTEGRATION-MERGE-RECOMMENDATION-0.1
title: TITMAS CE-G11B Atomic Governance Integration Merge Recommendation v0.1
version: 0.1.0
status: exact-recommendation-agent-review-pending-decision-pending
maturity: Development
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G11B Atomic Governance Integration Merge Recommendation v0.1

## Agent customer question

如果潜在用户需要把已验证的 CE-G11B implementation（实现）与完整治理证据一起进入
canonical branch，我是否会推荐直接合并当前 Draft PR #22？

```text
VERDICT=CONDITIONALLY_RECOMMENDED
DIRECT_MERGE_PR_22_RECOMMENDED=false
RECOMMENDED_OPTION=A
```

原因：PR #22 的 head 停留在 `e032115...`，只包含 CE Phase A-R1 实现与早期记录；
R3–R6 validation、failure preservation、Decision 和完整 PASS 证据位于其后继 governance
branch `ef0b40e...`。只合并 #22 会把实现和最终治理证据拆开。

## Recommendation

采用 **Option A：先验证 current canonical + governance head 的原子 merge tree，再建立
一个新的 replacement Draft PR；新 PR 通过独立审查后，才分别决定 supersede #22 和
merge**。

本建议不创建或修改 PR，不关闭 #22，不授权 merge，也不把 R6 PASS 自动升级为
canonical admission。

## Direct remote evidence

```text
canonical_ref=codex/production-observability-baseline
canonical_commit=ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
ce_ref=codex/ce-g11b-phase-a-decision
ce_commit=e032115adbe38cc84bde80cc9b10b96f6da1b428
governance_ref=codex/ce-g11b-phase-b-integration-governance
governance_commit=ef0b40e99db90a47a29c9322d771ea9611d3cbaf
governance_remote_match=true
governance_descends_from_ce=true
merge_base=4c95f6b68c21e4bf6e9babb8bd1afa4977cd418a
current_canonical_governance_merge_tree=88e8cdb300e3807b9d18b127cfa826e4e11cfd1f
canonical_only_commits=2
governance_only_commits=37
canonical_changed_paths=13
governance_changed_paths=87
changed_path_intersection=0
governance_only_paths_after_ce=71
```

PR #22 当前：

```text
state=OPEN
draft=true
base_ref=codex/production-observability-baseline
base_sha_observed=4c95f6b68c21e4bf6e9babb8bd1afa4977cd418a
head_ref=codex/ce-g11b-phase-a-decision
head_sha=e032115adbe38cc84bde80cc9b10b96f6da1b428
mergeable=true
merge_state=clean
reviews=0
comments=0
actions_on_head=0
```

R6 已对 `current canonical + CE head` merge tree
`ea296d8b2143aeb7cc220a81689ba4d057e4bb97` 完成：

```text
dependencies=23/23
site_tests=16/16
static_export_verify=PASS
ce_schemas=3/3
ce_tests=49/49
source_tree_drift=0
```

但 R6 没有验证加入 71 个 governance-only paths 后的新 merge tree `88e8cdb...`，因此
不能直接推荐 merge。

## Options

### Option A — Atomic replacement Draft PR after full merge-tree validation（推荐）

1. 新建独立 Decision，只授权在 disposable worktree 验证
   `ccf473f... + ef0b40e... → 88e8cdb...`；
2. 重跑 JSON/Schema/cockpit consistency、site 16 tests、formal static export/verify、
   3 CE Schemas 和 49 CE tests；
3. 要求 source/tree drift 为 0；
4. PASS 后另建 Decision，创建新的 Draft PR：
   - base: `codex/production-observability-baseline`
   - head: `codex/ce-g11b-phase-b-integration-governance`
   - 明示 supersedes PR #22，但创建时不自动关闭 #22；
5. 对新 PR 执行独立 diff/authority/secret/test review；
6. 只有 review PASS 后，分别建立：
   - PR #22 supersession/closure Decision；
   - replacement PR merge Decision。

### Option B — Merge PR #22, then merge governance branch（拒绝）

会产生 canonical 已有实现但缺少最终治理证据的中间状态，并需要两次 merge Decision。

### Option C — Fast-forward the existing PR #22 head ref（拒绝）

会在已审查 head ref 上追加 31+ commits，并使 `phase-a-decision` 分支名称与 Phase B
governance 内容不一致。

### Option D — Directly merge governance branch without replacement PR（拒绝）

绕过可见的 Draft PR、独立 diff review 和 supersession 记录。

### Option E — Merge PR #22 only（拒绝）

不会纳入 R3–R6、失败记录、Decision reviews 和最终 PASS 证据。

## Required next validation

```text
validated_merge_tree=88e8cdb300e3807b9d18b127cfa826e4e11cfd1f
json_duplicate_keys=0
commercial_entry_schema=PASS
site_dependencies=23/23
site_tests=16/16
formal_static_export_verify=PASS
ce_schemas=3/3
ce_tests=49/49
tracked_source_diff=0
git_status_entries=0
merge_tree_unchanged=true
```

## Review gate

精确 `qwen3.7-max` 必须返回：

```text
verdict=RECOMMENDED
selected_option=A
r6_evidence_bound=true
pr22_incomplete_for_full_evidence=true
governance_head_atomicity_preferred=true
new_merge_tree_validation_required=true
replacement_pr_before_supersession=true
pr22_closure_separate_decision=true
merge_separate_decision=true
no_remote_mutation=true
no_merge_authority=true
blocking_reasons=[]
required_corrections=[]
```

## Caps and non-claims

```text
RECOMMENDATION_REVIEW_REQUESTS_MAX=1
NEW_VALIDATION_DECISION_RECORDED=false
NEW_PR_CREATED=false
PR_22_MUTATED=false
PR_22_CLOSED=false
MERGE_DECISION_RECORDED=false
MERGES=0
PUSHES=0
WORKFLOW_RUNS=0
SITE_SOURCE_CHANGES=0
RELEASES=0
DEPLOYMENTS=0
STANDARD_READY=false
COMMERCIAL_OFFERING=false
```
