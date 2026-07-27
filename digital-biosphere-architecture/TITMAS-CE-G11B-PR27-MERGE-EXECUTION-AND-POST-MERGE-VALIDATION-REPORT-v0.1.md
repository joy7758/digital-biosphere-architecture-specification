# TITMAS CE-G11B PR #27 Merge Execution and Post-merge Validation Report v0.1

## Result

```text
PR27_STATE=MERGED
MERGE_COMMIT=c1d8931930fbae15f96ee6a6ac050b081538c919
MERGE_METHOD=MERGE_COMMIT
EXPECTED_PARENTS=PASS
EXPECTED_TREE=PASS
CANDIDATE_BRANCH_PRESERVED=true
CONTENT_DERIVED_REMOTE_BINDING=PASS
TRACKED_JSON=1165/1165
DUPLICATE_KEYS=0
COMMERCIAL_ENTRY_SCHEMA=PASS
CE_SCHEMA_HASHES=3/3
CE_SCHEMA_META=3/3
SITE_TESTS=16/16
CE_TESTS=49/49
RELEASE_FORMAL_LOCAL=PASS
TRACKED_SOURCE_DIFF=0
REMOTE_DRIFT=0
POST_MERGE_VALIDATION=PASS
```

PR #27 通过一次 plain merge commit 合并到
`codex/production-observability-baseline`。Merge commit 的第一父节点是冻结 base，第二
父节点是冻结 candidate，tree 与 R2 验证的 merge tree 完全一致；candidate branch 未删除。

## Fail-closed history

三个失败均保留，未改写成 PASS：

1. final preflight 的治理提交完整 SHA 手工补全错误；外部 mutation 为 0；
2. 初次 post-merge verifier 错把 `PR.baseRefOid` 当成合并后的远端 base branch head；
3. 初次 remediation validation 手工录入错误的 Decision review SHA，在结构验证和
   worktree 创建前停止。

最终验证移除未知时点文件的手工 expected hash，改为本地文件与同一远端治理提交内容
直接比较。该 binding PASS 后，才运行结构和隔离验证。

## Isolated validation

在 exact merge commit 的 disposable detached worktree 中执行一次：

- 1165 个 tracked JSON 全部解析，duplicate key 为 0；
- commercialization entry Schema PASS；
- offline/ignore-scripts `npm ci` PASS，安装 493 packages；
- `npm ls` exit 0，23 direct dependencies；保留 5 个 optional WASM extraneous
  observations，但不持久化绝对本地路径；
- site tests 16/16；
- local `release:formal` 的 static export、中文/英文 parity 和 truth boundary PASS；
- exact CE Schema hashes 3/3、Draft 2020-12 meta-schema 3/3；
- CE tests 49/49；
- tracked source diff 0，remote drift 0；
- disposable worktree 已删除。

## Boundaries

GitHub checks 和 human reviews 均缺失，不能写成成功或人工审查等价。`release:formal`
只表示隔离环境的静态构建验证，不是新 Release 或 Deployment。

```text
FAILED_ATTEMPTS_OVERWRITTEN=false
GITHUB_CHECKS_SUCCESS=false
HUMAN_REVIEW_EQUIVALENCE=false
RELEASE_AUTHORIZED=false
RELEASE_EXECUTED=false
DEPLOYMENT_AUTHORIZED=false
DEPLOYMENT_EXECUTED=false
STANDARD_READY=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
PERMISSION_CREATED=false
AUTHORITY_ELEVATED=false
EVIDENCE_TRUTH_CHANGED=false
```

## Next gate

下一步只能基于该远端 merge + validation 结果，准备 CE-G11B 商业化状态 reconciliation
和下一个有界标准 gate 的 Recommendation。该动作尚未授权。
