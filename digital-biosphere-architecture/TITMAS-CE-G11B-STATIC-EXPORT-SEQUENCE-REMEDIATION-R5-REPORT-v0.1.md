# TITMAS CE-G11B Static Export Sequence Remediation R5 Report v0.1

## Result

```text
STATUS=FAIL_CLOSED_FORMAL_RELEASE_CONTEXT_REQUIRED
NPM_CI_EXIT=0
NPM_LS_EXIT=0
NPM_TEST_EXIT=0
NPM_EXPORT_EXIT=1
VERIFY_STATIC_RUNS=0
CE_SCHEMA_RUNS=0
CE_TEST_RUNS=0
RETRY_AUTHORIZED=false
MERGE_AUTHORIZED=false
```

R5 在 disposable merge-tree worktree 中完成唯一 offline/ignore-scripts install、
dependency validation 和 16/16 site tests。随后唯一 `npm run export` 使用默认
`candidate` mode，并在冻结 release boundary 处以
`candidate export requires status.release_claim=false` 失败关闭；当前冻结
`public/status.json` 的 `release_claim` 为 `true`。

Decision 要求失败即停止，因此 `verify:static`、3 个 CE Schema meta-validation 和
49 个 CE tests 均未执行。没有 retry、network fallback、source drift、PR mutation、
workflow、merge 或 deployment。

## Direct boundary evidence

冻结 `release-mode.mjs` 表明：

- 未传 `RELEASE_MODE` 时默认 `candidate`；
- candidate export 要求 public truth surfaces 保持未发布；
- formal export 要求显式 release Decision、released-by、tag 和 DBOS wheel URL，并逐项
  与 public truth surfaces 对齐；
- 冻结 `package.json` 已定义 `release:formal` script，但 R5 Decision 没有授权调用。

这些是脚本和错误的直接观察，不表示 R5 已获得 release authorization，也不允许通过
临时修改 public truth surfaces 绕过 gate。

## Integrity

```text
package_hash_unchanged=true
lock_hash_unchanged=true
export_script_hash_unchanged=true
verify_script_hash_unchanged=true
tracked_source_diff=0
git_status_entries=0
merge_tree_unchanged=true
temporary_worktree_remaining=0
```

下一步只能准备独立 R6 formal-release-context static validation Recommendation，评估
是否可把已冻结的 `release:formal` script 作为本地验证命令。任何新 install、export、
static/CE validation 或 merge 仍需新的 Decision。
