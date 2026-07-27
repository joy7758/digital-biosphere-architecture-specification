---
document_id: DBA-TITMAS-CE-G11B-PR27-MERGE-EXECUTION-RECOMMENDATION-0.1
title: TITMAS CE-G11B PR #27 Merge Execution Recommendation v0.1
title_zh: TITMAS CE-G11B PR #27 合并执行建议 v0.1
version: 0.1.0
status: recommendation-candidate-review-required
maturity: Development
owner_ref: zhangbin
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G11B PR #27 Merge Execution Recommendation v0.1

## Question

在 merge admission 已明确通过、但 PR #27 仍为 Open Draft 的情况下，是否推荐对 exact
candidate 执行一次受控 merge commit，并在合并后重新验证结果树？

## Frozen execution target

```text
REPOSITORY=joy7758/digital-biosphere-architecture-specification
PR=27
BASE_BRANCH=codex/production-observability-baseline
BASE_SHA=ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
HEAD_BRANCH=codex/ce-g11b-pr23-remediation-candidate
HEAD_SHA=e6a193f4bf0d48d65649077122f0ab262460daac
EXPECTED_MERGE_TREE=9171e554cfcbeaa02d5542c3a35cb729bca44185
PR_STATE=OPEN
PR_DRAFT=true
PR_MERGEABLE=MERGEABLE
PR_MERGE_STATE=CLEAN
GITHUB_CHECKS=0
GITHUB_REVIEWS=0
BRANCH_PROTECTION=NONE_OBSERVED
ALLOW_MERGE_COMMIT=true
DELETE_BRANCH_ON_MERGE=false
```

Merge-admission evidence:

```text
MERGE_ADMISSION_RESULT_COMMIT=5e47753bbb82ee3a0a249b675f2718686bbe7647
MERGE_ADMISSION_RESULT_SHA256=900169fdf291687d5e7a1b905f1fc0abd8f5cce6ff720eef4e02822eb53597c0
MERGE_ADMISSION_READY=true
MERGE_EXECUTION_DECISION_ALLOWED=true
MERGE_EXECUTION_AUTHORIZED=false
```

## Recommended exact method

### Step 1 — Final preflight

Reverify:

- PR remains Open Draft;
- base/head SHAs exactly match;
- mergeable/clean remains true;
- comments, reviews, requests, checks and commits have not drifted;
- remote base and head branches match the frozen SHAs;
- `git merge-tree --write-tree BASE HEAD` equals
  `9171e554cfcbeaa02d5542c3a35cb729bca44185`;
- merge-admission Decision and result remote commits match.

Any drift stops execution.

### Step 2 — Convert Draft to ready

Use the authenticated GitHub operation equivalent to:

```text
gh pr ready 27 --repo joy7758/digital-biosphere-architecture-specification
```

Immediately reverify PR/base/head before merge. If conversion succeeds but later preconditions
fail, stop and record the partial PR-state mutation. Do not silently convert back or retry.

### Step 3 — Merge commit

Use:

```text
gh pr merge 27
  --repo joy7758/digital-biosphere-architecture-specification
  --merge
  --match-head-commit e6a193f4bf0d48d65649077122f0ab262460daac
  --subject "Merge PR #27: integrate CE-G11B atomic evidence"
```

Prohibited flags and methods:

```text
--admin
--auto
--delete-branch
--squash
--rebase
```

### Step 4 — Structural post-merge verification

The resulting commit must:

- be the remote head of `codex/production-observability-baseline`;
- have first parent `ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14`;
- have second parent `e6a193f4bf0d48d65649077122f0ab262460daac`;
- have tree `9171e554cfcbeaa02d5542c3a35cb729bca44185`;
- close PR #27 as merged;
- leave the candidate branch present.

### Step 5 — Isolated post-merge validation

Create a disposable clean worktree at the exact merge commit and rerun:

- tracked JSON parse and duplicate-key check for the merged tree;
- commercialization entry Schema validation;
- offline `npm ci --ignore-scripts`;
- `npm ls`;
- site tests;
- `release:formal` static/content/truth validation;
- exact three CE Schema metadata/hash checks;
- 49 CE tests;
- source/status/remote/tree drift checks.

Post-merge validation failure does not authorize reset, force-push, deletion or automatic
revert. It requires a separate revert/remediation Recommendation and Decision.

## Zero-check acceptance

For this exact candidate only, GitHub's zero-check state may be accepted as an absence that
is supplemented by commit-bound R2 and semantic-review evidence. It must not become a
general policy or be described as GitHub CI success.

## Options

### Option A — Execute exact merge commit with post-merge validation

推荐, subject to one independent qualifying Decision.

### Option B — Squash or rebase merge

拒绝。It would change the expected commit lineage and invalidate the frozen merge-tree/parent
verification contract.

### Option C — Use admin or auto-merge

拒绝。No branch-protection bypass or asynchronous state change is needed.

### Option D — Delete candidate branch

拒绝。Preserve source lineage until a later cleanup Decision.

### Option E — Keep PR Draft indefinitely

不推荐。R2, semantic review and merge admission are complete; delay adds drift risk without
adding evidence.

## Failure and rollback

- No retries are allowed for Draft conversion or merge execution.
- If Draft conversion succeeds but merge fails, record `PARTIAL_PR_MUTATION` and stop.
- If merge succeeds but structural or isolated validation fails, record the exact merge
  commit and failure evidence, then prepare a separate revert/remediation Decision.
- Never force-push the base branch.

## Agent-customer recommendation

```text
RECOMMENDED=YES_FOR_EXACT_MERGE_COMMIT_EXECUTION
RECOMMENDED_METHOD=MERGE_COMMIT
RECOMMENDED_FOR_RELEASE=false
```

## Non-authorizations

This Recommendation does not authorize PR mutation, merge, rollback, release, deployment,
Standard Ready, production readiness or commercial availability. A separate Human Decision
and exact `qwen3.7-max` Decision review are required.
