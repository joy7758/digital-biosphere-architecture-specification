# TITMAS CE-G11B Site-CWD Offline Actual Install R4 Report v0.1

## Result

```text
STATUS=FAIL_CLOSED_STATIC_EXPORT_ARTIFACT_ABSENT
NPM_CI_ATTEMPTS=1
NPM_CI_EXIT=0
NPM_LS_EXIT=0
NPM_TEST_EXIT=0
VERIFY_STATIC_EXIT=1
CE_SCHEMA_RUNS=0
CE_TEST_RUNS=0
RETRY_AUTHORIZED=false
MERGE_AUTHORIZED=false
```

R4 在 frozen merge tree 的 disposable worktree 中完成了唯一一次
offline/ignore-scripts 实际安装。安装成功，`npm ls` 未发现 missing/invalid direct
dependency，`npm test` 完成 build 并通过 16/16 tests。随后唯一一次
`npm run verify:static` 因 `site/out/index.html` 不存在而返回 `ENOENT` / exit `1`。
执行按 Decision 的 stop condition 立即失败关闭，未重试，也未继续 3 个 CE Schema
meta-validation 或精确 49 个 CE tests。

## Direct execution evidence

```text
normalized_prefix_equal=true
install_summary=added 493 packages in 5s
direct_dependencies=23
missing_direct_dependencies=0
invalid_direct_dependencies=0
site_tests=16/16
static_missing_path_suffix=site/out/index.html
package_hash_unchanged=true
lock_hash_unchanged=true
tracked_source_diff=0
git_status_entries=0
merge_tree_unchanged=true
temporary_worktree_remaining=0
```

`package.json` 的当前 `test` script 调用 `npm run build`，而不是 `npm run export`；
`verify:static` 则读取 `site/out/`。这是对冻结脚本和实际错误的直接观察。报告不把这
一观察升级为超出当前证据的内部因果结论。

## Boundary

本结果证明：

- 该 lockfile 可在指定环境中完成一次 offline/ignore-scripts 实际安装；
- direct dependency tree 和当前 `npm test` 可通过；
- 失败没有改变 package、lockfile、tracked source 或 merge tree；
- stop condition、无重试和临时 worktree 清理均生效。

本结果不证明：

- static export 已生成或验证；
- CE Schema 和 49 个 CE tests 已在 R4 链路中执行；
- PR #22 可合并；
- Phase B、Production、Certification、SLA 或 Commercial Offering 已授权。

下一步只能先形成独立 R5 static-export sequence remediation Recommendation，并继续由
精确 `qwen3.7-max` 审查。R4 不允许重跑；任何新的 actual install、export、validation
或 merge 都需要新的 Decision。
