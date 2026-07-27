---
document_id: DBA-TITMAS-CE-G11B-STATIC-EXPORT-SEQUENCE-REMEDIATION-R5-RECOMMENDATION-0.1
title: TITMAS CE-G11B Static Export Sequence Remediation R5 Recommendation v0.1
version: 0.1.0
status: exact-recommendation-agent-review-pending-decision-pending
maturity: Development
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G11B Static Export Sequence Remediation R5 Recommendation v0.1

## Recommendation

采用 **Option A：在新的 disposable merge-tree worktree 中重新完成一次
offline/ignore-scripts exact-lockfile 安装，并在 `npm test` 后显式执行一次
`npm run export`，再运行 `npm run verify:static` 和完整 CE validation**。

R5 只修正 R4 已直接证明的 validation sequence gap（验证顺序缺口）。它不修改网站
源码、package scripts、package.json 或 lockfile，不复用 R4 已删除的
`node_modules`，不联网，也不授权 PR mutation 或 merge。

## Direct evidence

远端 commit `f16f09cc602be40137facce38cac35e5007bdcd7` 固化：

```text
R4_STATUS=FAIL_CLOSED_STATIC_EXPORT_ARTIFACT_ABSENT
npm_ci_attempts=1
npm_ci_exit=0
npm_ls_exit=0
missing_direct_dependencies=0
invalid_direct_dependencies=0
npm_test_exit=0
site_tests=16/16
verify_static_attempts=1
verify_static_exit=1
missing_path_suffix=site/out/index.html
ce_schema_runs=0
ce_test_runs=0
retry_count=0
tracked_source_diff=0
git_status_entries=0
merge_tree_unchanged=true
```

冻结 `package.json` 直接表明：

```text
test=npm run build + node tests
export=npm run build + node scripts/export-static.mjs
verify:static=node scripts/verify-static.mjs
```

冻结 `verify-static.mjs` 读取 `site/out/`，冻结 `export-static.mjs` 创建并填充
`site/out/`。这些事实支持修正顺序，但不把 R4 观察升级为对 vinext 内部机制的完整
因果声明。

## Options

### Option A — Test, export, then static verification（推荐）

在新的 temporary merge-tree worktree 中：

1. 复核 frozen topology、PR #22、0 Actions、package/lock/script hashes、empty Git
   status 和 absent `node_modules`；
2. 记录 raw/normalized site path 与 npm prefix，要求 normalized equality；
3. 从真实 site cwd 执行恰好一次：

```text
NPM_CONFIG_OFFLINE=true npm ci --offline --ignore-scripts --no-audit --no-fund
```

4. 安装成功后按顺序各执行一次：

```text
npm ls --depth=0 --json
npm test
npm run export
npm run verify:static
```

5. 只有上述四项全部 exit `0`，才运行 3 个 Commercial Evaluation Schema
   meta-validation 和精确 49 个 CE tests；
6. 验证 package/lock/script hashes、tracked source、Git status 和 merge tree 未改变；
7. 保留 exact failure 并删除 temporary worktree；
8. 禁止 retry、network fallback、lifecycle scripts、existing `node_modules` reuse、
   PR mutation、workflow、merge、server action 或 deployment。

`npm run export` 会再次执行 build，这是当前冻结 package script 的显式语义；R5 不以
绕过 package script 的方式调用内部 export 文件。

### Option B — Run verify:static again without export（拒绝）

R4 已直接证明该顺序缺少 `out/index.html`；重复相同动作不会增加新证据。

### Option C — Call export-static.mjs directly（暂不采用）

直接内部脚本可以减少一次 build，但会绕过冻结的 public npm script contract，不适合
本轮最小、可复现验证。

### Option D — Modify package scripts before validation（拒绝）

当前问题可以先通过已存在的 `npm run export` 验证，无需在 merge candidate 中引入
网站源码或 package contract 变更。

### Option E — Merge because install and tests passed（拒绝）

R4 未完成 static 和 CE validation，不能升级为 merge readiness。

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
export_static_sha256=cd5cd0eef9b4a61f66cb866b3f96d16d5e95c28768ceda37633f454f3429a8bd
verify_static_sha256=8e26f3af1cba44184f2552969d67fba2983d84459d1e5cd1ab7a75f7436c089d
node=v26.0.0
npm=11.12.1
python=3.14.5
```

## Required results

```text
npm_ci_attempts=1
npm_ci_exit=0
network_fallbacks=0
install_script_executions=0
npm_ls_exit=0
missing_direct_dependencies=0
invalid_direct_dependencies=0
npm_test_attempts=1
npm_test_exit=0
npm_export_attempts=1
npm_export_exit=0
verify_static_attempts=1
verify_static_exit=0
ce_schemas_meta_valid=3
ce_tests_passed=49
tracked_source_diff=0
git_status_entries=0
package_hash_unchanged=true
lock_hash_unchanged=true
script_hashes_unchanged=true
merge_tree_unchanged=true
```

若 `npm test`、`npm run export` 或同步脚本产生 tracked source drift，即使命令 exit
`0` 也必须失败关闭。

## Caps

```text
RECOMMENDATION_REVIEW_REQUESTS_MAX=1
NEW_DECISION_RECORDED=false
TEMPORARY_WORKTREES_AUTHORIZED=0
NPM_CI_ATTEMPTS_AUTHORIZED=0
NPM_EXPORT_ATTEMPTS_AUTHORIZED=0
SITE_TEST_RUNS_AUTHORIZED=0
CE_TEST_RUNS_AUTHORIZED=0
NETWORK_FALLBACKS=0
EXISTING_NODE_MODULES_REUSES=0
SITE_SOURCE_CHANGES=0
PR_MUTATIONS=0
MERGES=0
WORKFLOW_RUNS=0
SERVER_ACTIONS=0
DEPLOYMENTS=0
```

## Review gate

要求 exact `qwen3.7-max` 返回：

```text
verdict=RECOMMENDED
selected_option=A
r4_result_bound=true
sequence_gap_evidence_sufficient=true
public_export_script_preserved=true
single_actual_install_attempt_only=true
offline_and_ignore_scripts_enforced=true
existing_node_modules_reuse_prohibited=true
test_export_verify_order_required=true
full_ce_validation_required=true
tracked_source_drift_fails_closed=true
no_remote_mutation=true
merge_unauthorized=true
blocking_reasons=[]
required_corrections=[]
```

## Non-claims

```text
RECOMMENDATION_PREPARED=true
R4_FAILURE_PRESERVED=true
R4_RETRY_AUTHORIZED=false
R5_DECISION_RECORDED=false
R5_EXECUTION_AUTHORIZED=false
ACTUAL_INSTALL_EXECUTED=false
STATIC_EXPORT_VALIDATED=false
CE_VALIDATION_COMPLETED=false
MERGE_AUTHORIZED=false
PHASE_B_AUTHORIZED=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
```
