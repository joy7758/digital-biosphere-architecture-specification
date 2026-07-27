---
document_id: DBA-TITMAS-CE-G11B-ZERO-INSTALL-NPM-CWD-DIAGNOSTIC-RECOMMENDATION-0.1
title: TITMAS CE-G11B Zero-install npm CWD Diagnostic Recommendation v0.1
version: 0.1.0
status: exact-recommendation-agent-review-pending-decision-pending
maturity: Development
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G11B Zero-install npm CWD Diagnostic Recommendation v0.1

## Recommendation

采用 **Option A：在全新临时 merge-tree worktree 中，以 site directory 作为真实进程
cwd，执行一次 offline/ignore-scripts `npm ci --dry-run` 诊断**。

## Evidence

失败的唯一实际命令：

```text
npm --prefix <site> ci --offline --ignore-scripts --no-audit --no-fund
exit=1
error=EUSAGE
reported_missing=site@0.1.0
verbose_cwd=<governance-worktree-root>
prefix=<temporary-merge-tree>/digital-biosphere-architecture/site
```

package/lock root name/version 匹配，无显式 `site` dependency。以上只证明 invocation
form 与进程 cwd 不同；不证明它是根因。

## Exact diagnostic

新的 Decision 最多允许一次：

```text
cd <temporary-merge-tree>/digital-biosphere-architecture/site
NPM_CONFIG_OFFLINE=true npm ci --dry-run --offline --ignore-scripts --no-audit --no-fund
```

同时记录：

- `npm prefix`；
- `npm pkg get name version`；
- package/lock hashes；
- exit code 和 sanitized error category；
- command 前后 `node_modules` absence；
- tracked diff 和 merge-tree hash；
- network fallback、install scripts、dependency materialization 均为 0。

`--dry-run` 不得创建或修改 `node_modules`、package-lock、tracked source 或 cache package
content。任何写入、cache miss、network need 或 second attempt 都失败关闭。

## Interpretation

- dry-run PASS：只证明 cwd-form contract 可进入新的 actual-install Recommendation；
- dry-run FAIL with same error：prefix/cwd hypothesis 不成立；
- different failure：保留新 failure，不修复、不重跑；
- 任一结果都不授权真实安装、site tests 或 merge。

## Options

- **A（推荐）**：one exact cwd-form offline dry-run；
- **B（禁止）**：直接用 cwd-form 重试真实 npm ci；
- **C（禁止）**：修改 lockfile 或 package.json；
- **D（禁止）**：复用现成 node_modules 或联网。

## Max review gate

要求 exact `qwen3.7-max` 返回 `RECOMMENDED`、Option A，并确认：

```text
diagnostic_hypothesis_bounded=true
dry_run_zero_install_boundary=true
single_attempt_only=true
failure_interpretation_coherent=true
source_mutation_prohibited=true
network_prohibited=true
actual_install_unauthorized=true
merge_unauthorized=true
blocking_reasons=[]
required_corrections=[]
```

本 Recommendation 不授权 dry-run、安装、测试、PR mutation、merge、workflow、server
或 deployment。
