---
document_id: DBA-TITMAS-CE-G11B-PR23-REMEDIATION-REPLACEMENT-DRAFT-PR-RECOMMENDATION-0.1
title: TITMAS CE-G11B PR #23 Remediation Replacement Draft PR Recommendation v0.1
title_zh: TITMAS CE-G11B PR #23 修正候选替代 Draft PR 建议 v0.1
version: 0.1.0
status: recommendation-candidate-review-required
maturity: Development
owner_ref: zhangbin
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G11B PR #23 Remediation Replacement Draft PR Recommendation v0.1

## Question

潜在 Agent 开发者是否应获得一个新的、精确指向修正候选与 R2 evidence 的 Draft PR
review surface，而不是继续把 PR #23 的旧 candidate 或 PR #24 的 evidence branch 当作
当前审查对象？

## Frozen bindings

```text
BASE_REF=codex/production-observability-baseline
BASE_SHA=ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
HEAD_REF=codex/ce-g11b-pr23-remediation-candidate
HEAD_SHA=e6a193f4bf0d48d65649077122f0ab262460daac
VALIDATED_MERGE_TREE=9171e554cfcbeaa02d5542c3a35cb729bca44185
R1_EVIDENCE_REF=codex/ce-g11b-pr23-remediation-candidate-evidence
R1_EVIDENCE_SHA=d054b5cf3880904aba84816501b07358fcfb4c06
R2_EVIDENCE_REF=codex/ce-g11b-pr23-remediation-candidate-evidence-r2
R2_EVIDENCE_SHA=27bc3b6e586a2259d17152a2022a85d2dd69107b
R2_STATUS=PASS_SHA_BOUND_EXACT_THREE_SCHEMA_R2_VALIDATION
```

R2 direct evidence：tracked JSON 1165/1165、site 16/16、exact CE Schema
hash/meta 3/3、CE tests 49/49、static verification PASS、source/remote/tree drift 0。
R1 的 selector-scope FAIL 仍是不可变历史。

## Current PR state

```text
PR22=OPEN_DRAFT_PHASE_A_HEAD
PR23=OPEN_DRAFT_OLD_CANDIDATE_c608fd78
PR24=CLOSED_NOT_MERGED_EVIDENCE_TO_MAIN_DIRTY
```

三者都不能表示当前修正候选：

- #22 只指向 Phase A；
- #23 指向 remediation 前的 `c608fd78...`；
- #24 错误地使用 evidence ref 作为 head，且 base 为 `main`。

## Options

### Option A — Create one new bounded Draft PR

推荐：

```text
base=codex/production-observability-baseline
head=codex/ce-g11b-pr23-remediation-candidate
draft=true
```

PR body 精确绑定 base/head/merge-tree/R1/R2 SHA，并声明 R2 PASS 不是 review approval、
merge authorization、release 或 production evidence。创建后只读核验 number、Draft、
base/head/head SHA、body、empty reviewers/labels/milestone、auto-merge disabled。

### Option B — Retarget or force-push PR #23

拒绝。会破坏旧 candidate 的审查连续性。

### Option C — Reopen or修复 PR #24

拒绝。evidence ref 不能成为产品 candidate head，且 `main` 不是冻结 base。

### Option D — Merge candidate directly

拒绝。绕过独立 PR review 和后续 Merge Decision。

## Agent-customer recommendation

```text
RECOMMENDED=YES_FOR_NEW_BOUNDED_DRAFT_REVIEW
NOT_RECOMMENDED_AS=MERGE_READY_RELEASE_READY_PRODUCTION_READY
```

## Bounded action

只有后续独立 Decision 经 exact `qwen3.7-max` 合格审查后，才允许创建一个 Draft PR。
不得修改/关闭 #22/#23/#24，不得添加 reviewer、label、milestone、auto-merge，不得
dispatch workflow、写 run request、merge、release、deploy 或操作服务器。

## Next gate

若 exact `qwen3.7-max` 返回 `RECOMMENDED / Option A / confidence>=0.9` 且
blocker=0、correction=0，只允许准备 replacement Draft PR Creation Decision。

Draft PR 不是批准；Validation 不是 Merge Authorization；Evidence 不是 Truth。
