---
document_id: DBA-TITMAS-CE-G11B-FORMAL-RELEASE-CONTEXT-STATIC-VALIDATION-R6-RECOMMENDATION-0.1
title: TITMAS CE-G11B Formal Release Context Static Validation R6 Recommendation v0.1
version: 0.1.0
status: exact-recommendation-agent-review-pending-decision-pending
maturity: Development
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G11B Formal Release Context Static Validation R6 Recommendation v0.1

## Recommendation

采用 **Option A：在新的 disposable frozen merge-tree worktree 中完成一次离线安装和
site tests 后，执行冻结 public npm script `npm run release:formal` 恰好一次，再完成
3 个 CE Schema 和精确 49 个 CE tests**。

`release:formal` 在本轮仅作为 local static export + verification command（本地静态
导出与验证命令）。它不创建 tag、GitHub Release、deployment、server action 或新的
release authorization。

## Direct evidence

远端 commit `315a384cd80085e49158f4eaba7bdcbb08ce4de6` 固化：

```text
R5_STATUS=FAIL_CLOSED_FORMAL_RELEASE_CONTEXT_REQUIRED
npm_ci_exit=0
npm_ls_exit=0
npm_test_exit=0
site_tests=16/16
npm_export_exit=1
error=candidate export requires status.release_claim=false
public_status_release_claim=true
verify_static_runs=0
ce_schema_runs=0
ce_test_runs=0
retry_count=0
source_tree_unchanged=true
```

冻结 `package.json` 已定义：

```text
release:static=npm run export && npm run verify:static
release:formal=<four exact formal context values> npm run release:static
```

冻结 `release-mode.mjs` 要求 formal context 与 `status.json`、agent index、customer
package 和 DBOS package manifest 逐项一致。R6 不修改这些 truth surfaces。

## Option A — Existing formal script, local validation only（推荐）

新 temporary worktree 中：

1. 复核 frozen topology、Draft PR #22、0 Actions、package/lock/release/export/verify
   hashes、empty status、absent `node_modules`、normalized prefix equality；
2. 执行一次 offline/ignore-scripts `npm ci`；
3. 按顺序各一次执行：
   `npm ls --depth=0 --json` → `npm test` → `npm run release:formal`；
4. `release:formal` 必须完成其内部唯一 `npm run export` 和 `npm run verify:static`；
5. 成功后 meta-validate 3 个 CE Schema，运行精确 49 个 CE tests；
6. 检查 frozen hashes、tracked source、Git status 和 merge tree 不变；
7. 删除 worktree；任一失败即停止，不重试。

### Rejected options

- **B：修改 public truth 为 candidate** — 篡改已发布事实，禁止。
- **C：手工拼接一套新的 formal environment** — 重复冻结 package contract，增加漂移。
- **D：把 script 名称解释为新发布动作** — 错误；本 gate 只观察本地 build artifact。
- **E：跳过 static/CE validation 或直接 merge** — R5 未完成这些证据。

## Frozen inputs

```text
canonical_commit=ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
ce_commit=e032115adbe38cc84bde80cc9b10b96f6da1b428
merge_base=4c95f6b68c21e4bf6e9babb8bd1afa4977cd418a
merge_tree=ea296d8b2143aeb7cc220a81689ba4d057e4bb97
package_json_sha256=60dc7abf99a878f0e9dd24f0362d1ac7ad9c72a4d21578085fed39c526e3709b
package_lock_sha256=4f179b1107a3a3f18aa906ebd19f952a9a4d190b1ad7123cba0a6884e3a312fd
export_static_sha256=cd5cd0eef9b4a61f66cb866b3f96d16d5e95c28768ceda37633f454f3429a8bd
verify_static_sha256=8e26f3af1cba44184f2552969d67fba2983d84459d1e5cd1ab7a75f7436c089d
```

## Required results

```text
npm_ci_attempts=1
npm_ci_exit=0
npm_ls_exit=0
npm_test_exit=0
site_tests_passed=16
release_formal_attempts=1
release_formal_exit=0
static_export_present=true
static_verification_pass=true
ce_schemas_meta_valid=3
ce_tests_passed=49
tracked_source_diff=0
git_status_entries=0
all_frozen_hashes_unchanged=true
merge_tree_unchanged=true
```

## Review gate

Exact `qwen3.7-max` 必须返回：

```text
verdict=RECOMMENDED
selected_option=A
r5_result_bound=true
formal_context_need_proven=true
existing_public_script_preferred=true
truth_surface_mutation_prohibited=true
local_validation_not_release_action=true
single_offline_install_only=true
full_static_and_ce_validation_required=true
source_drift_fails_closed=true
no_remote_mutation=true
merge_unauthorized=true
blocking_reasons=[]
required_corrections=[]
```

## Caps and non-claims

```text
RECOMMENDATION_REVIEW_REQUESTS_MAX=1
NEW_DECISION_RECORDED=false
EXECUTION_AUTHORIZED=false
ACTUAL_INSTALLS=0
RELEASE_FORMAL_RUNS=0
SITE_SOURCE_CHANGES=0
PUBLIC_TRUTH_MUTATIONS=0
TAGS=0
GITHUB_RELEASES=0
PR_MUTATIONS=0
MERGES=0
WORKFLOW_RUNS=0
SERVER_ACTIONS=0
DEPLOYMENTS=0
NEW_RELEASE_AUTHORIZATION=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
```
