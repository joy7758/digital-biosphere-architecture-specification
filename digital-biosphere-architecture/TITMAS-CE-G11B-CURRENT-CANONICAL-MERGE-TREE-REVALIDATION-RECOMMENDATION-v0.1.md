---
document_id: DBA-TITMAS-CE-G11B-CURRENT-CANONICAL-MERGE-TREE-REVALIDATION-RECOMMENDATION-0.1
title: TITMAS CE-G11B Current Canonical Merge-tree Revalidation Recommendation v0.1
title_zh: TITMAS CE-G11B 当前规范分支合并树复验建议 v0.1
version: 0.1.0
status: exact-recommendation-agent-review-pending-decision-pending
maturity: Development
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G11B Current Canonical Merge-tree Revalidation Recommendation v0.1

## 1. Trigger

Draft PR #22 的 frozen review target 为：

```text
old_base=4c95f6b68c21e4bf6e9babb8bd1afa4977cd418a
head=e032115adbe38cc84bde80cc9b10b96f6da1b428
```

当前远端 canonical 已前进为：

```text
current_base=ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
old_base_is_ancestor=true
new_canonical_commits=2
ce_head_already_in_canonical=false
current_base_ahead_of_old_base=2
ce_head_ahead_of_old_base=5
current_merge_base=4c95f6b68c21e4bf6e9babb8bd1afa4977cd418a
```

新增 canonical commits：

```text
cc13ef5 feat(site): add medical evidence demo
ccf473f fix(site): align medical evidence demo boundaries
```

两次提交只改变 `digital-biosphere-architecture/site/`；CE-G11B head 的 21 个 changed
paths 中 `site/` 为 0。`git merge-tree --write-tree current_base head` 成功得到：

```text
candidate_merge_tree=ea296d8b2143aeb7cc220a81689ba4d057e4bb97
textual_conflicts_observed=0
```

## 2. Recommendation

建议采用 **Option A：保持 PR #22 和 frozen head 不变，先对 current canonical +
CE-G11B head 的 candidate merge-tree 做一次离线复验**。

不得直接 merge，也不得 rebase、force-push、修改 head、改网站或重新解释旧的 PR review。

## 3. Bounded revalidation

新的独立 Decision 最多允许：

1. 再次确认 current base/head/merge-base、PR Draft state 和 Actions runs；
2. 用 `git merge-tree --write-tree` 重建 exact candidate tree；
3. 在临时 detached worktree 检出该 tree；
4. 复验 21 个 CE-G11B paths 与 13 个 current-canonical site paths 均存在；
5. 确认两组 changed paths 交集为 0；
6. 运行 CE-G11B Schema、runner/scoped/full-discovery tests；
7. 运行当前 canonical 提供的 site tests/verify-static，只使用仓库已有依赖与命令；
8. 形成 sanitized result/report。

如果 site dependency 不可用、命令不存在或测试失败，必须失败关闭；不得安装新依赖、
修改网站、跳过或把“无冲突”写成验证通过。

## 4. Options

### Option A — Offline merge-tree revalidation（推荐）

不改变任何远端状态，验证当前真实合并候选。

### Option B — Rebase or force-push reviewed head（禁止）

这会改变已经过 hash、测试和 Max review 的 frozen head。

### Option C — Merge based on old-base review（禁止）

canonical 已漂移，旧 review 不能自动覆盖新 merge tree。

### Option D — Close and recreate PR immediately（禁止）

尚无证据证明需要替换 PR；先复验实际 merge tree。

## 5. Agent review gate

本 Recommendation 必须由 exact `qwen3.7-max` 以 direct JSON 审查：

```text
verdict=RECOMMENDED|REVISE|REJECT
selected_option=A|B|C|D
would_recommend_to_agent_customer=true|false
confidence=0..1
topology_drift_correctly_detected=true|false
disjoint_path_evidence_sufficient=true|false
frozen_head_preserved=true|false
merge_tree_revalidation_scope_sufficient=true|false
site_validation_required=true|false
no_remote_mutation=true|false
merge_remains_unauthorized=true|false
blocking_reasons=[]
required_corrections=[]
rationale=string
```

只有 `RECOMMENDED`、Option A、全部 boolean 为 true、0 blocker/correction 才可准备
新的 revalidation Decision。

## 6. Caps and non-claims

```text
RECOMMENDATION_REVIEW_MODEL=qwen3.7-max
RECOMMENDATION_REVIEW_REQUESTS_MAX=1
RETRIES=0
FALLBACKS=0
REBases=0
FORCE_PUSHES=0
PR_MUTATIONS=0
MERGES=0
WORKFLOW_RUNS=0
SITE_CHANGES=0
SERVER_ACTIONS=0
DEPLOYMENTS=0
MERGE_AUTHORIZED=false
PHASE_B_AUTHORIZED=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
```

Recommendation 和 candidate merge-tree 都不是 merge approval、canonical adoption、
workflow authorization、Phase B、deployment 或 release。
