---
document_id: DBA-TITMAS-CE-G11B-SITE-CWD-OFFLINE-ACTUAL-INSTALL-R4-RECOMMENDATION-0.1
title: TITMAS CE-G11B Site-CWD Offline Actual Install R4 Recommendation v0.1
version: 0.1.0
status: exact-recommendation-agent-review-pending-decision-pending
maturity: Development
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G11B Site-CWD Offline Actual Install R4 Recommendation v0.1

## Recommendation

采用 **Option A：在 disposable merge-tree worktree 的真实 site cwd 中，执行一次
offline/ignore-scripts exact-lockfile 安装，并立即完成完整 site 与 CE validation**。

这是 R3 zero-install dry-run PASS 后的新独立 gate。它不修改网站源码、package.json 或
package-lock，不复用现成 `node_modules`，不联网，不授权 PR mutation 或 merge。

## Direct evidence

远端 commit `a800323a53800c76d8e0d62bc36ce6a85b9ca9ef` 固化：

```text
R3_STATUS=PASS_NORMALIZED_PREFIX_AND_ZERO_INSTALL_DRY_RUN
raw_prefix_equal=false
normalized_prefix_equal=true
npm_package_name=trusted-multi-agent-infrastructure-site
npm_package_version=0.1.0
dry_run_attempts=1
dry_run_exit=0
node_modules_before=false
node_modules_after=false
package_hash_unchanged=true
lock_hash_unchanged=true
git_status_entries_after=0
merge_tree_unchanged=true
actual_install_attempts=0
```

dry-run 输出 `added 493 packages in 414ms` 不构成实际安装事实。

## Options

### Option A — One site-cwd offline install plus full validation（推荐）

在新的 temporary merge-tree worktree 中：

1. 复核 frozen topology、PR #22、0 Actions、package/lock hashes 和 absent
   `node_modules`；
2. 记录 raw/realpath site 与 npm prefix，要求 normalized equality；
3. 从真实 site cwd 执行恰好一次：

```text
NPM_CONFIG_OFFLINE=true npm ci --offline --ignore-scripts --no-audit --no-fund
```

4. 禁止 retry、network fallback、lifecycle scripts、existing `node_modules` copy/symlink；
5. 安装成功后运行：

```text
npm ls --depth=0 --json
npm test
npm run verify:static
```

6. 运行 3 个 Commercial Evaluation Schema meta-validation 和 49 个 CE tests；
7. 验证 package/lock hashes、tracked source、Git tree 未改变；
8. 保留 exact failure，删除 temporary worktree。

### Option B — Reuse existing node_modules（禁止）

现有持久化站点目录曾观察到 extraneous packages；复制或 symlink 会破坏 exact-lockfile
验证。

### Option C — Permit online fallback（禁止）

本 gate 验证本地可复现的 frozen dependency contract，不允许 registry fallback。

### Option D — Merge after install without tests（禁止）

安装成功不证明 build、site tests、static export 或 CE validation 通过。

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
missing_direct_dependencies=0
invalid_direct_dependencies=0
npm_test_exit=0
verify_static_exit=0
ce_schemas_meta_valid=3
ce_tests_passed=49
tracked_source_diff=0
package_hash_unchanged=true
lock_hash_unchanged=true
merge_tree_unchanged=true
```

若 `npm test` 的同步脚本产生 tracked source drift，即使测试通过也必须失败关闭。

## Caps

```text
RECOMMENDATION_REVIEW_REQUESTS_MAX=1
NEW_DECISION_RECORDED=false
TEMPORARY_WORKTREES_AUTHORIZED=0
NPM_CI_ATTEMPTS_AUTHORIZED=0
SITE_TEST_RUNS_AUTHORIZED=0
CE_TEST_RUNS_AUTHORIZED=0
NETWORK_FALLBACKS=0
EXISTING_NODE_MODULES_REUSES=0
SITE_SOURCE_CHANGES=0
PR_MUTATIONS=0
MERGES=0
WORKFLOW_RUNS=0
DEPLOYMENTS=0
```

## Review gate

要求 exact `qwen3.7-max` 返回：

```text
verdict=RECOMMENDED
selected_option=A
r3_result_bound=true
normalized_prefix_gate_preserved=true
single_actual_install_attempt_only=true
offline_and_ignore_scripts_enforced=true
existing_node_modules_reuse_prohibited=true
full_site_and_ce_validation_required=true
tracked_source_drift_fails_closed=true
no_remote_mutation=true
merge_unauthorized=true
blocking_reasons=[]
required_corrections=[]
```

## Non-claims

```text
RECOMMENDATION_PREPARED=true
R3_PASS_PRESERVED=true
ACTUAL_INSTALL_AUTHORIZED=false
ACTUAL_INSTALL_EXECUTED=false
SITE_TESTS_AUTHORIZED=false
CE_TESTS_AUTHORIZED=false
MERGE_AUTHORIZED=false
PHASE_B_AUTHORIZED=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
```
