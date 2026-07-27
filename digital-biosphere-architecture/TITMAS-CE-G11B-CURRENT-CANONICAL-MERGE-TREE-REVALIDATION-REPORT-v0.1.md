# TITMAS CE-G11B Current Canonical Merge-tree Revalidation Report v0.1

## Result

```text
RESULT=FAIL_CLOSED_SITE_DEPENDENCY_NOT_MATERIALIZED
MERGE_TREE=ea296d8b2143aeb7cc220a81689ba4d057e4bb97
CE_PATHS=21
CANONICAL_SITE_PATHS=13
PATH_INTERSECTION=0
SCHEMAS_META_VALID=3
CE_TESTS=49/49 PASS
SITE_DEPENDENCIES_MATERIALIZED=false
SITE_TESTS_EXECUTED=0
DEPENDENCY_INSTALLATIONS=0
NETWORK_DEPENDENCY_FETCHES=0
PR_MUTATIONS=0
MERGES=0
WORKFLOW_RUNS=0
```

当前 canonical 与 CE head 的 candidate merge-tree 精确重建成功，路径完全分离，CE
Schema 和测试全部通过。但临时 detached worktree 不包含 `site/node_modules`。Decision
明确禁止安装依赖，也禁止跳过 site validation，因此整体必须失败关闭。

该失败不证明 merge conflict、CE defect 或 site source defect。下一步只能先准备
site dependency materialization / hermetic validation remediation Recommendation；不得
直接 retry 或 merge。
