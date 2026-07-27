---
document_id: DBA-TITMAS-CE-G11B-PR27-PREFLIGHT-HARNESS-BINDING-REMEDIATION-RECOMMENDATION-0.1
title: TITMAS CE-G11B PR #27 Preflight Harness Binding Remediation Recommendation v0.1
title_zh: TITMAS CE-G11B PR #27 预检工具绑定修复建议 v0.1
version: 0.1.0
status: recommendation-candidate-review-required
maturity: Development
owner_ref: zhangbin
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G11B PR #27 Preflight Harness Binding Remediation Recommendation v0.1

## Question

第一次 final preflight 因 inline harness 手工录入了错误的治理提交完整 SHA 而在本地绑定
阶段 fail closed，且尚未发生任何 PR 或分支写操作。是否推荐形成一个新的有界 Decision，
只允许使用远端直接解析的治理提交和文件 hash 重跑一次完整无写入 preflight，并在全部
条件通过后继续使用尚未消费的 Draft→Ready 与 merge commit mutation caps？

## Failure binding

```text
FAILURE_RECORD=TITMAS-CE-G11B-PR27-MERGE-EXECUTION-PREFLIGHT-FAILURE-v0.1.json
FAILURE_PHASE=LOCAL_GOVERNANCE_COMMIT_BINDING
EXPECTED_GOVERNANCE_SHA_ENTERED=5aa0d260ba6f4d3ea89d79d1d557cde9219c5470
ACTUAL_GOVERNANCE_SHA=5aa0d266c3c70c4d3f720c3d6606698c573a79d6
PR_MUTATIONS=0
DRAFT_READY_MUTATIONS=0
MERGE_ATTEMPTS=0
```

本次失败不是 PR、base、head、merge tree、Recommendation、Decision 或远端证据漂移。
它是未绑定 inline command 对缩写提交的人工补全错误。失败历史必须保留，不能改写为
首次 preflight PASS。

## Recommended option

### Option A — Authorize one corrected fail-closed preflight

推荐。新的 preflight 必须：

1. 通过 `git ls-remote` 直接解析并比较三个远端 branch ref；
2. 从当前治理 worktree 的 `git rev-parse HEAD` 取得本地完整 SHA，禁止手工补全；
3. 要求本地治理 HEAD 与远端治理 branch 完全相等；
4. 重新计算 `git merge-tree --write-tree BASE HEAD`；
5. 重新查询 PR state、Draft、base/head、mergeable、merge state、comments、reviews、
   review requests、checks 和 commit count；
6. 从远端治理提交读取 Decision 与 qwen review，并校验固定 SHA-256；
7. 任一失败继续 stop，不执行 Ready 或 Merge。

只有新的 preflight 全部 PASS，才可继续原 Decision 尚未消费的：

```text
DRAFT_READY_MUTATIONS=1
MERGE_MUTATIONS=1
MERGE_ATTEMPTS=1
RETRIES=0
```

这不是对 Draft 或 Merge 的 retry，因为此前两项外部 mutation 均未开始。

### Option B — Treat the failed attempt as PASS

拒绝。失败必须保留。

### Option C — Silently rerun the inline command

拒绝。原 Decision 明确要求 fail closed；必须形成新 Decision。

### Option D — Edit or force-update governance history

拒绝。不能为匹配错误输入而改写有效远端提交。

## Corrected preflight target

```text
REPOSITORY=joy7758/digital-biosphere-architecture-specification
PR=27
BASE_SHA=ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
HEAD_SHA=e6a193f4bf0d48d65649077122f0ab262460daac
EXPECTED_MERGE_TREE=9171e554cfcbeaa02d5542c3a35cb729bca44185
GOVERNANCE_BRANCH=codex/ce-g11b-pr23-remediation-candidate-governance
GOVERNANCE_SHA=5aa0d266c3c70c4d3f720c3d6606698c573a79d6
```

## Agent-customer recommendation

```text
RECOMMENDED=YES_FOR_ONE_CORRECTED_NON_MUTATING_PREFLIGHT
RECOMMENDED_TO_CONTINUE_MUTATIONS_ONLY_AFTER_PASS=true
RECOMMENDED_FOR_RELEASE=false
```

## Non-authorizations

This Recommendation does not authorize silent retry, PR mutation, Draft conversion, merge,
rollback, branch deletion, release, deployment, Standard Ready, production readiness or
commercial availability. A separate Human Decision and exact `qwen3.7-max` Decision review
remain required.
