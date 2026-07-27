---
document_id: DBA-TITMAS-CE-G11B-PR27-POST-MERGE-VERIFIER-REMEDIATION-RECOMMENDATION-0.1
title: TITMAS CE-G11B PR #27 Post-merge Verifier Remediation Recommendation v0.1
title_zh: TITMAS CE-G11B PR #27 合并后验证器修复建议 v0.1
version: 0.1.0
status: recommendation-candidate-review-required
maturity: Development
owner_ref: zhangbin
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G11B PR #27 Post-merge Verifier Remediation Recommendation v0.1

## Question

PR #27 已生成符合冻结 parents/tree 的 merge commit，但第一次 post-merge structural
verification 因错误要求 `PR.baseRefOid == remote base head after merge` 而 fail closed。
是否推荐形成一个新的有界 Decision，只允许修正结构语义并在 disposable clean worktree
对 exact merge commit 运行一次 R2-equivalent isolated validation？

## Frozen merged state

```text
REPOSITORY=joy7758/digital-biosphere-architecture-specification
PR=27
PR_STATE=MERGED
MERGED_AT=2026-07-27T21:16:42Z
MERGE_COMMIT=c1d8931930fbae15f96ee6a6ac050b081538c919
FIRST_PARENT=ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
SECOND_PARENT=e6a193f4bf0d48d65649077122f0ab262460daac
TREE=9171e554cfcbeaa02d5542c3a35cb729bca44185
CANDIDATE_BRANCH_PRESERVED=true
```

## Verifier correction

正确结构合同应分别检查：

```text
REMOTE_BASE_BRANCH_HEAD == MERGE_COMMIT
PR.baseRefOid == FIRST_PARENT
PR.headRefOid == SECOND_PARENT
PR.mergeCommit.oid == MERGE_COMMIT
MERGE_COMMIT.parents == [FIRST_PARENT, SECOND_PARENT]
MERGE_COMMIT.tree == EXPECTED_TREE
```

不得把原失败改写成 PASS；新的验证是独立 remediation validation。

## Recommended option

### Option A — Correct verifier semantics and run one isolated validation

推荐，步骤：

1. 重新读取远端 base、candidate branch 和 PR merge metadata；
2. 按上述六项合同验证结构；
3. 在 exact merge commit 建立一个 disposable detached worktree；
4. 解析全部 tracked JSON 并拒绝 duplicate keys；
5. 验证 commercialization entry Schema；
6. 运行一次 offline `npm ci --offline --ignore-scripts --no-audit --no-fund`；
7. 依次运行 `npm ls --depth=0 --json`、`npm test`、`npm run release:formal`；
8. 对冻结的三个 CE Schema 验证 SHA-256 和 Draft 2020-12 meta-schema；
9. 运行一次 CE tests，要求 `49/49`；
10. 验证 worktree source/status、remote base、candidate branch、merge commit/tree 无漂移；
11. 删除 disposable worktree；
12. 在治理分支保留 PASS 或 FAIL。

任一失败都不授权 reset、force-push、branch deletion 或 automatic revert，必须另建
revert/remediation Decision。

### Option B — Revert immediately

不推荐。直接证据表明 parents、tree 和 PR mergeCommit 已符合冻结合同；当前失败来自
verifier 语义，不是候选内容或合并结构失败。

### Option C — Declare PASS without isolated validation

拒绝。结构诊断不能替代隔离测试。

## Exact CE Schema paths

```text
digital-biosphere-architecture/commercial-evaluation-controller-tls-diagnosis/ce-g11b-run-request.schema.v0.1.json
  sha256=6a6e4ee89cc39085950737fcd4a8fc913d4b48a051508e1e1e1e02352e2b1d39
digital-biosphere-architecture/commercial-evaluation-controller-tls-diagnosis/ce-g11b-cross-version-result.schema.v0.1.json
  sha256=6c7f328f28c04c94a955f2b3642c5685590e3b556984d34db693fbef3ff1f15f
digital-biosphere-architecture/commercial-evaluation-controller-tls-diagnosis/ce-g11b-phase-a-r1-result.schema.v0.1.json
  sha256=1e6e4f379a689ae292359efdba2da72b45b55249f39c253e678d28aa8b6c3331
```

## Agent-customer recommendation

```text
RECOMMENDED=YES_FOR_CORRECTED_POST_MERGE_VALIDATION
RECOMMENDED_TO_REVERT_NOW=false
RECOMMENDED_FOR_RELEASE=false
```

## Non-authorizations

This Recommendation does not authorize history rewrite, reset, force-push, branch deletion,
automatic revert, candidate changes, new merge, release, deployment, Standard Ready,
production readiness or commercial availability. A separate Human Decision and exact
`qwen3.7-max` Decision review are required.
