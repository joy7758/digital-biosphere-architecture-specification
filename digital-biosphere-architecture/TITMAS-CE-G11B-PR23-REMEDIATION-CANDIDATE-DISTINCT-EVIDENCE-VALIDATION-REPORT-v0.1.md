# TITMAS CE-G11B PR #23 Remediation Candidate Distinct Evidence Validation Report v0.1

## Result

```text
STATUS=FAIL_CLOSED
FAILURE=CE_SCHEMA_SELECTOR_SCOPE_MISMATCH
CANONICAL_SHA=ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
CANDIDATE_SHA=e6a193f4bf0d48d65649077122f0ab262460daac
MERGE_TREE_SHA=9171e554cfcbeaa02d5542c3a35cb729bca44185
TRACKED_JSON=1165/1165
COMMERCIAL_ENTRY_SCHEMA=PASS
SITE_TESTS=16/16
STATIC_EXPORT_VERIFY=PASS
CE_SCHEMAS_EXPECTED=3
CE_SCHEMAS_OBSERVED_AND_META_VALIDATED=11
CE_SCHEMA_COMMAND_EXIT=1
CE_TESTS_RUN=0
COMMAND_RETRIES=0
PR_23_MUTATED=false
PR_24_MUTATED=false
MERGE=false
RELEASE=false
DEPLOYMENT=false
```

## Failure

唯一授权的验证执行在 CE Schema meta-validation 门禁失败关闭。执行选择器递归匹配
文件名包含 `schema` 的 JSON，共发现并成功 meta-validate 11 个 Schema；Decision
冻结的精确期望值是 3，因此计数断言退出 1。

不能因为 11 个 Schema 都通过 meta-validation 就把本轮解释成 PASS。该选择器范围与
Decision 合同不一致，CE test discovery 因 fail-closed 顺序没有运行。没有重试、没有
更改 selector、没有修源码或测试。

## Completed checks before failure

- tracked JSON parse and duplicate-key check：1165/1165，duplicate keys 0；
- commercialization entry Schema：PASS；
- offline/ignore-scripts `npm ci`：exit 0，493 packages；
- `npm ls`：exit 0，23 direct dependencies；另透明记录 5 个 extraneous optional WASM
  package observations，不持久化绝对本地路径；
- site tests：16/16；
- local static export、content parity 与 truth boundary：PASS；
- merge-tree worktree 在失败前 tracked diff 0、status entries 0。

这些局部通过项不抵消 CE Schema contract failure，也不构成完整 merge-tree PASS。

## Preserved boundaries

```text
OLD_CANDIDATE_MUTATED=false
OLD_EVIDENCE_MUTATED=false
REMEDIATION_CANDIDATE_MUTATED=false
CANONICAL_MUTATED=false
PR_23_MUTATED=false
PR_24_MUTATED=false
MERGE=false
RELEASE=false
DEPLOYMENT=false
STANDARD_READY=false
AVAILABLE_COMMERCIAL_OFFERING=false
```

## Next gate

只允许准备 CE Schema selector contract remediation Recommendation。新的 Decision
必须明确三个目标 Schema 的精确路径或重新定义可接受的动态集合，不能重用本轮 request
cap，也不能把本次 11-schema observation 本地重解释为完整 PASS。
