# TITMAS CE-G11B npm Prefix Path Normalization R3 Report v0.1

## Result

```text
STATUS=PASS_NORMALIZED_PREFIX_AND_ZERO_INSTALL_DRY_RUN
RAW_PREFIX_EQUAL=false
NORMALIZED_PREFIX_EQUAL=true
DRY_RUN_ATTEMPTS=1
DRY_RUN_EXIT=0
ACTUAL_INSTALL_ATTEMPTS=0
MERGE_AUTHORIZED=false
```

R3 观察到 temporary site raw path 使用 `/tmp/...`，而 `npm prefix` 返回
`/private/tmp/...`。两者 raw 字符串不同，但 Python `os.path.realpath` 后完全相等。这
提供了与 R2 mismatch 一致的具体路径拼写机制，不表示 npm package root 不同。由于
R2 没有持久化实际 prefix，本结果不追溯证明 R2 的 exact mismatch root cause。

## Dry-run outcome

在 normalized prefix equality、frozen topology、package/lock hashes、empty Git status
和 `node_modules` absence 全部满足后，执行唯一一次：

```text
NPM_CONFIG_OFFLINE=true npm ci --dry-run --offline --ignore-scripts --no-audit --no-fund
```

结果：

```text
exit=0
sanitized_summary=added 493 packages in 414ms
node_modules_after=false
git_status_entries_after=0
package_hash_unchanged=true
lock_hash_unchanged=true
merge_tree_unchanged=true
```

`added 493 packages` 是 npm dry-run 输出，不是实际安装事实。`node_modules` 前后均不
存在，dependency materialization 和 actual install 都是 0。

## Boundary

本结果只证明：

- real site process cwd 可正确解析到 site package root；
- exact lockfile 的 offline/ignore-scripts dry-run 可通过；
- 该 dry-run 未修改 source、lockfile、Git tree 或依赖目录。

本结果不证明：

- 真实 `npm ci` 可以完成；
- site build、tests 或 static verification 通过；
- PR #22 可合并；
- Phase B、Production、Certification、SLA 或 Commercial Offering 已授权。

下一步只能形成新的 actual-install Recommendation，继续使用 disposable worktree、
real site cwd、offline、ignore-scripts、single attempt 和完整 post-install/site/CE
validation；真实安装仍需独立 Decision。
