# TITMAS CE-G11B Immutable Candidate Merge-Tree Validation Report v0.1

## Result

```text
STATUS=PASS_SHA_BOUND_EXTERNAL_ATTESTATION
CANDIDATE_SHA=c608fd78d7d50d1733ddd9e19aeb6870c5a08288
CANONICAL_SHA=ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
MERGE_TREE_SHA=bd67298eb8d869b024eaf9f03a53636c6dc377d4
TRACKED_JSON=1165/1165 PASS
COMMERCIAL_ENTRY_SCHEMA=PASS
DEPENDENCIES=23/23
SITE_TESTS=16/16
STATIC_EXPORT=PASS
CONTENT_PARITY=PASS
TRUTH_BOUNDARY=PASS
CE_SCHEMAS=3/3
CE_TESTS=49/49
TRACKED_SOURCE_DIFF=0
GIT_STATUS_ENTRIES=0
CANDIDATE_REMOTE_UNCHANGED=true
CANONICAL_REMOTE_UNCHANGED=true
MERGE_TREE_UNCHANGED=true
```

验证按 v0.2 prospective authorization Decision 在一个 disposable merge-tree
worktree 中执行。唯一一次 offline/ignore-scripts `npm ci`、`npm ls`、`npm test`、
`npm run release:formal`、CE Schema meta-validation 和 CE test discovery 全部退出
0。没有重试、网络 fallback、PR 变更、merge、release、deployment 或服务器操作。

## Preserved harness event

所有验证命令完成后，第一版只读汇总解析器退出 2：它假定 Node TAP 计数以 `#`
开头，并寻找不存在的 `STATIC_VERIFY_PASS` 行。实际输出使用 `ℹ tests 16` /
`ℹ pass 16`，而 `release:formal` 通过退出 0、`STATIC_EXPORT_PASS=true`、
`ZH_EN_CONTENT_PARITY_PASS=true`、`TRUTH_BOUNDARY_VALIDATION_PASS=true` 和
`RELEASE_MODE=formal` 表达完成状态。

没有重跑任何验证命令；只对既有输出重新读取和汇总。该解析器事件保留在机器 Result
中，不删除、不覆盖。

## Authority boundary

本结果只证明冻结的 canonical + immutable candidate merge tree 在当前隔离环境完成
完整静态验证。它不创建 replacement PR，不关闭 Draft PR #22，不授权 merge、release
或 deployment，也不使 TITMAS Standard Ready。

下一步只能准备 `CE-G11B replacement Draft PR Decision`，并继续使用 exact
`qwen3.7-max` 做独立质量审查。
