# TITMAS CE-G11B Zero-install npm CWD Diagnostic R2 Report v0.1

## Result

```text
STATUS=FAIL_CLOSED_PRECONDITION_NPM_PREFIX_STRING_MISMATCH
DRY_RUN_EXECUTED=false
DRY_RUN_ATTEMPTS=0
ACTUAL_INSTALL_ATTEMPTS=0
MERGE_AUTHORIZED=false
```

R2 没有运行 `npm ci --dry-run`。临时 merge-tree worktree 在命令前的 Git tree、0 status
entry、package/lock SHA-256 和 `node_modules` absence 全部通过；`npm prefix` 命令也已
执行，但其原始字符串与脚本保存的 site 路径不完全相等，因此按 Decision 的前置条件
失败关闭。

## What is proven

- governance Decision remote baseline 等于
  `2430b83430ddbfd219ba068b74f9db130b12aa30`；
- canonical、CE、merge base、merge tree、PR #22 和 0 Actions runs 均与 frozen input
  一致；
- temporary worktree 的 tree 为
  `ea296d8b2143aeb7cc220a81689ba4d057e4bb97`；
- package/lock hashes 精确匹配；
- `node_modules` 不存在；
- dry-run、actual install、dependency materialization、site tests、PR mutation、merge、
  workflow 和 deployment 都没有发生；
- 临时 worktree 已删除，剩余数量为 0。

## What is not proven

- 实际 `npm prefix` 字符串没有被持久化；
- 尚未验证是否只是 `/tmp` 与 `/private/tmp` 等 realpath spelling 差异；
- prefix/cwd hypothesis 没有被接受或拒绝；
- npm lockfile contract、site tests 和 merge readiness 均未验证。

因此根因保持 `UNKNOWN`。不得把本结果写成 npm、lockfile、Vinext、macOS 或 path
canonicalization 的已证明缺陷。

## Next gate

只能准备一个新的 Recommendation，明确：

1. 先持久化 raw sanitized `npm prefix`；
2. 同时比较 raw path 与 `realpath` normalized path；
3. 使用新的 Decision 和新的 temporary-worktree cap；
4. 若 normalized prefix 匹配，才允许一次原有 zero-install dry-run；
5. 仍禁止真实安装、site tests、PR mutation 和 merge。
