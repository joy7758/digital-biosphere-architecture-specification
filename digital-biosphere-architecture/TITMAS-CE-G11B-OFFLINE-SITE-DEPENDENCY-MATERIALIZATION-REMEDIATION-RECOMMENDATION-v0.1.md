---
document_id: DBA-TITMAS-CE-G11B-OFFLINE-SITE-DEPENDENCY-MATERIALIZATION-REMEDIATION-RECOMMENDATION-0.1
title: TITMAS CE-G11B Offline Site Dependency Materialization Remediation Recommendation v0.1
title_zh: TITMAS CE-G11B 网站依赖离线物化修复建议 v0.1
version: 0.1.0
status: exact-recommendation-agent-review-pending-decision-pending
maturity: Development
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G11B Offline Site Dependency Materialization Remediation Recommendation v0.1

## Recommendation

建议采用 **Option A：在一次新的临时 merge-tree worktree 中，依据 exact lockfile 使用
本机 npm cache 进行一次严格 offline、ignore-scripts 的 clean dependency
materialization，然后运行 site test 和 static verification**。

该步骤只修复 R1 的 `SITE_DEPENDENCY_NOT_MATERIALIZED`。不修改源文件、不复用现成
`node_modules`、不联网、不修改 PR、不 merge。

## Frozen evidence

```text
merge_tree=ea296d8b2143aeb7cc220a81689ba4d057e4bb97
package_json_sha256=60dc7abf99a878f0e9dd24f0362d1ac7ad9c72a4d21578085fed39c526e3709b
package_lock_sha256=4f179b1107a3a3f18aa906ebd19f952a9a4d190b1ad7123cba0a6884e3a312fd
local_npm_cache_present=true
existing_materialized_dependencies_present=true
existing_direct_missing_or_invalid=0
existing_extraneous_packages=5
existing_node_modules_reuse_allowed=false
R1_CE_TESTS=49/49_PASS
R1_SITE_TESTS=0
```

现成 `node_modules` 含 5 个 extraneous WASM-related packages，所以只作为 cache
availability 的旁证，不作为可复用验证环境。

## Exact offline materialization

新的独立 Decision 最多允许一次：

```text
npm ci --offline --ignore-scripts --no-audit --no-fund
```

约束：

- exact package/lock hashes 必须匹配；
- `NPM_CONFIG_OFFLINE=true`；
- 使用现有用户 npm cache，只读其 package content；允许 npm 写本次本地 cache metadata/log；
- 不允许 registry/network fallback；
- 不允许 lifecycle install scripts；
- 不允许复制、symlink 或 bind 现成 `node_modules`；
- 安装仅存在于临时 worktree，结束后由 `git worktree remove` 清理；
- `npm ci` 非零、cache miss、package hash drift 或需要联网时立即失败关闭。

## Validation after materialization

只有 clean offline materialization 成功后才运行：

```text
npm ls --depth=0 --json
npm test
npm run verify:static
```

并要求：

- missing direct dependency = 0；
- invalid direct dependency = 0；
- test exit = 0；
- verify-static exit = 0；
- tracked source diff = 0；
- merge-tree `git write-tree` 仍等于 `ea296d8b…`；
- CE 49/49 tests 仍通过；
- dependency installation network requests = 0；
- PR mutation、merge、workflow、site source change、server、deployment = 0。

## Options

- **Option A（推荐）**：exact lockfile + offline cache + ignore-scripts clean install；
- **Option B（禁止）**：复用 canonical worktree 的现成 `node_modules`；
- **Option C（禁止）**：联网 `npm ci` 或 registry fallback；
- **Option D（禁止）**：跳过 site tests，直接 merge。

## Max review contract

本 Recommendation 仅在 exact `qwen3.7-max` 返回：

```text
verdict=RECOMMENDED
selected_option=A
would_recommend_to_agent_customer=true
lockfile_binding_sufficient=true
offline_boundary_coherent=true
ignore_scripts_boundary_coherent=true
existing_node_modules_reuse_rejected=true
failure_closed=true
site_validation_scope_sufficient=true
no_remote_mutation=true
merge_remains_unauthorized=true
blocking_reasons=[]
required_corrections=[]
```

后，才可准备独立 Decision。

## Non-claims

```text
RECOMMENDATION_REVIEW_REQUESTS_MAX=1
RETRIES=0
FALLBACKS=0
DEPENDENCY_INSTALLATION_AUTHORIZED=false
NETWORK_ACCESS_AUTHORIZED=false
PR_MUTATION_AUTHORIZED=false
MERGE_AUTHORIZED=false
WORKFLOW_RUNS=0
PHASE_B_AUTHORIZED=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
```
