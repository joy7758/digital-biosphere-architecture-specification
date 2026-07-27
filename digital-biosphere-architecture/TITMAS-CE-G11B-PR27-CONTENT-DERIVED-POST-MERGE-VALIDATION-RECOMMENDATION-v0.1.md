---
document_id: DBA-TITMAS-CE-G11B-PR27-CONTENT-DERIVED-POST-MERGE-VALIDATION-RECOMMENDATION-0.1
title: TITMAS CE-G11B PR #27 Content-derived Post-merge Validation Recommendation v0.1
title_zh: TITMAS CE-G11B PR #27 内容派生式合并后验证建议 v0.1
version: 0.1.0
status: recommendation-candidate-review-required
maturity: Development
owner_ref: zhangbin
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G11B PR #27 Content-derived Post-merge Validation Recommendation v0.1

## Question

第一次 post-merge remediation validation 在任何结构检查、worktree 创建或测试前，因为
inline command 再次手工录入错误的 Decision review SHA-256 而 fail closed。是否推荐
移除所有未知时点产生文件的手工 expected hash，通过本地与远端同一提交内容直接比较，
再执行一次尚未消费的结构与隔离验证合同？

## Failure binding

```text
FAILURE_RECORD=TITMAS-CE-G11B-PR27-POST-MERGE-VALIDATION-HARNESS-BINDING-FAILURE-v0.1.json
FAILURE_PHASE=LOCAL_DECISION_REVIEW_SHA_BINDING
WORKTREES_CREATED=0
TEST_RUNS=0
SOURCE_OR_REMOTE_MUTATIONS=0
```

原 failure 不得改写为 PASS。

## Recommended option

### Option A — Use content-derived remote equality and execute unused validation caps

推荐。新的脚本必须：

1. 从 `git rev-parse HEAD` 和 `git ls-remote` 直接取得治理本地与远端完整 SHA；
2. 要求两者相等；
3. 对 Decision 与 qwen review 分别计算本地文件 SHA-256；
4. 从同一远端治理提交读取相同路径，并计算远端内容 SHA-256；
5. 只比较 `local_hash == remote_hash`，不手工录入 review 的 expected hash；
6. 然后执行已采纳的 corrected structural contract；
7. 只有结构 PASS 才创建一个 disposable worktree 并执行完整 isolated contract；
8. 任一失败停止，不重试、不修源码、不回滚 merge；
9. 删除 disposable worktree，保留 PASS 或 FAIL 结果。

Decision 文件本身的 SHA-256 仍可固定，因为它在 Recommendation 前已经存在；Decision
review 只有在 Decision 后产生，必须使用 content-derived remote equality。

### Option B — 再次手工复制 review hash

拒绝。两次独立 transcription failure 已证明该方法不可靠。

### Option C — 跳过治理 remote binding

拒绝。必须证明执行使用的 Decision 与 review 已远端可追溯。

## Frozen validation target

```text
MERGE_COMMIT=c1d8931930fbae15f96ee6a6ac050b081538c919
FIRST_PARENT=ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
SECOND_PARENT=e6a193f4bf0d48d65649077122f0ab262460daac
TREE=9171e554cfcbeaa02d5542c3a35cb729bca44185
```

## Agent-customer recommendation

```text
RECOMMENDED=YES_FOR_CONTENT_DERIVED_REMOTE_BINDING_AND_UNUSED_VALIDATION_CAPS
RECOMMENDED_FOR_REVERT=false
RECOMMENDED_FOR_RELEASE=false
```

## Non-authorizations

This Recommendation does not authorize silent failure rewriting, source/test fixes, reset,
force-push, branch deletion, automatic revert, new merge, release, deployment, Standard Ready,
production readiness or commercial availability. A separate Human Decision and exact
`qwen3.7-max` Decision review are required.
