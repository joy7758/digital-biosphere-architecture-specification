---
document_id: DBA-TITMAS-CE-G11B-NPM-PREFIX-PATH-NORMALIZATION-R3-RECOMMENDATION-0.1
title: TITMAS CE-G11B npm Prefix Path Normalization R3 Recommendation v0.1
version: 0.1.0
status: exact-recommendation-agent-review-pending-decision-pending
maturity: Development
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G11B npm Prefix Path Normalization R3 Recommendation v0.1

## Recommendation

采用 **Option A：在新的 R3 Decision 下，持久化 raw/realpath prefix observation，以
realpath equality 作为 site-cwd 前置条件，匹配时执行一次原有 zero-install dry-run**。

R3 只修正验证器的 path spelling 比较，不修改 package、lockfile、npm configuration、
网站源码或诊断命令。

## Preserved R2 result

远端 commit `7155474a816d2027ea1c43139d072063d7b7f12e` 固化：

```text
result=FAIL_CLOSED_PRECONDITION_NPM_PREFIX_STRING_MISMATCH
merge_tree_match=true
tracked_or_untracked_status_entries=0
package_json_hash_match=true
package_lock_hash_match=true
node_modules_absent=true
npm_prefix_command_executed=true
npm_prefix_observed_value_persisted=false
npm_prefix_raw_string_match=false
npm_prefix_realpath_match=NOT_ASSESSED
dry_run_attempts=0
actual_install_attempts=0
root_cause=UNKNOWN
```

`/tmp` 与 `/private/tmp` 等 path spelling 只是一项 bounded hypothesis，不是已证明根因。
R2 不得重跑或追溯补写实际 prefix。

## Options

### Option A — New R3 with persisted raw and normalized paths（推荐）

在新的 temporary merge-tree worktree：

1. 记录 `site_path_raw` 和 `npm prefix` 的 raw sanitized value；
2. 分别使用 Python `os.path.realpath` 计算 normalized path；
3. 记录 raw equality 与 realpath equality；
4. 只有 realpath equality 为 true，且 tree/status/package/lock/no-node_modules 均通过时，
   才执行一次：

```text
NPM_CONFIG_OFFLINE=true npm ci --dry-run --offline --ignore-scripts --no-audit --no-fund
```

5. 命令后重新验证 node_modules absence、package/lock hashes、0 Git status 和 unchanged
   merge tree；
6. 任一失败均保留 exact category，不重跑。

### Option B — Continue requiring raw string equality（拒绝）

raw spelling 可能受 macOS `/tmp` symlink canonicalization 影响，不能独立证明 prefix
指向不同 package root。

### Option C — Skip prefix verification（拒绝）

将失去该诊断用于隔离 process cwd 的目的。

### Option D — Run actual install or edit lockfile（禁止）

真实安装、lockfile 修复和 site tests 属于后续独立 gate。

## Frozen inputs

```text
canonical_commit=ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
ce_commit=e032115adbe38cc84bde80cc9b10b96f6da1b428
merge_base=4c95f6b68c21e4bf6e9babb8bd1afa4977cd418a
merge_tree=ea296d8b2143aeb7cc220a81689ba4d057e4bb97
draft_pr=22
draft_pr_state=OPEN_DRAFT
ce_head_actions_runs=0
package_json_sha256=60dc7abf99a878f0e9dd24f0362d1ac7ad9c72a4d21578085fed39c526e3709b
package_lock_sha256=4f179b1107a3a3f18aa906ebd19f952a9a4d190b1ad7123cba0a6884e3a312fd
process_cwd=digital-biosphere-architecture/site
command=NPM_CONFIG_OFFLINE=true npm ci --dry-run --offline --ignore-scripts --no-audit --no-fund
```

任何 topology、PR、Actions、tree 或 hash drift 都停止。

## Caps

```text
RECOMMENDATION_REVIEW_REQUESTS_MAX=1
NEW_DECISION_RECORDED=false
NEW_DECISION_REVIEW_REQUESTS_AUTHORIZED=0
TEMPORARY_WORKTREES_AUTHORIZED=0
NPM_PREFIX_OBSERVATIONS_AUTHORIZED=0
NPM_DRY_RUN_ATTEMPTS_AUTHORIZED=0
ACTUAL_INSTALL_ATTEMPTS=0
DEPENDENCY_MATERIALIZATIONS=0
NETWORK_FALLBACKS=0
SITE_TEST_RUNS=0
SITE_SOURCE_CHANGES=0
PR_MUTATIONS=0
MERGES=0
WORKFLOW_RUNS=0
DEPLOYMENTS=0
```

新的 R3 Decision 通过独立 write-ahead review 后，才可分别把 temporary worktree、
prefix observation 和 dry-run cap 设为 1。

## Review gate

要求 exact `qwen3.7-max` 返回：

```text
verdict=RECOMMENDED
selected_option=A
r2_failure_preserved=true
unknown_root_cause_preserved=true
raw_and_realpath_observations_required=true
realpath_gate_coherent=true
single_new_attempt_only=true
diagnostic_command_unchanged=true
actual_install_unauthorized=true
source_mutation_prohibited=true
merge_unauthorized=true
blocking_reasons=[]
required_corrections=[]
```

## Non-claims

```text
RECOMMENDATION_PREPARED=true
R2_RESULT_PRESERVED=true
R3_DECISION_RECORDED=false
R3_AUTHORIZED=false
DRY_RUN_EXECUTED=false
ACTUAL_INSTALL_AUTHORIZED=false
SITE_TESTS_AUTHORIZED=false
MERGE_AUTHORIZED=false
PHASE_B_AUTHORIZED=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
```
