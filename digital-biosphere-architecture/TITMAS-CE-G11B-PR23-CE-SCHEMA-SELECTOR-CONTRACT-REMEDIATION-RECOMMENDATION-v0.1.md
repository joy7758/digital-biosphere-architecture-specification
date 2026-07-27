---
document_id: DBA-TITMAS-CE-G11B-PR23-CE-SCHEMA-SELECTOR-CONTRACT-REMEDIATION-RECOMMENDATION-0.1
title: TITMAS CE-G11B PR #23 CE Schema Selector Contract Remediation Recommendation v0.1
title_zh: TITMAS CE-G11B PR #23 CE Schema 选择器契约修正建议 v0.1
version: 0.1.0
status: recommendation-candidate-review-required
maturity: Development
owner_ref: zhangbin
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G11B PR #23 CE Schema Selector Contract Remediation Recommendation v0.1

## Recommendation question

潜在 Agent 开发者是否应推荐对 frozen candidate `e6a193f4...` 进行一次新的
distinct-evidence validation，并把 CE Schema selector 恢复为历史 Decision 已冻结的
三个精确路径，而不是递归匹配所有文件名含 `schema` 的 JSON？

## Preserved failure

```text
FAILED_EVIDENCE_REF=codex/ce-g11b-pr23-remediation-candidate-evidence
FAILED_EVIDENCE_COMMIT=d054b5cf3880904aba84816501b07358fcfb4c06
FAILURE=CE_SCHEMA_SELECTOR_SCOPE_MISMATCH
EXPECTED=3
OBSERVED_AND_META_VALIDATED=11
CE_TESTS_RUN=0
RETRIES=0
```

R1 FAIL 必须保持不可变。它不证明产品 Schema 失败：11 个被选择的 Schema 都完成
meta-validation，失败来自 selector 范围与 Decision 的 3-schema 合同不一致。

## Exact historical contract

R4/R5 Decision 已明确冻结以下三个 CE-G11B Draft 2020-12 Schema：

1. `commercial-evaluation-controller-tls-diagnosis/ce-g11b-run-request.schema.v0.1.json`
   — SHA-256 `6a6e4ee89cc39085950737fcd4a8fc913d4b48a051508e1e1e1e02352e2b1d39`
2. `commercial-evaluation-controller-tls-diagnosis/ce-g11b-cross-version-result.schema.v0.1.json`
   — SHA-256 `6c7f328f28c04c94a955f2b3642c5685590e3b556984d34db693fbef3ff1f15f`
3. `commercial-evaluation-controller-tls-diagnosis/ce-g11b-phase-a-r1-result.schema.v0.1.json`
   — SHA-256 `1e6e4f379a689ae292359efdba2da72b45b55249f39c253e678d28aa8b6c3331`

这不是缩小产品目标，而是恢复原有 CE-G11B validation scope。全仓 tracked JSON
parse/duplicate-key check 仍独立覆盖全部 JSON。

## Options

### Option A — Exact three-path selector on a new R2 evidence ref

推荐。使用新 ref
`codex/ce-g11b-pr23-remediation-candidate-evidence-r2`，从 exact candidate 派生；
重构相同 canonical+candidate merge tree `9171e554...`，运行完整验证一次。CE Schema
阶段只读取上述三个 exact path，并先检查三个 hash。

### Option B — Reinterpret R1 as PASS

拒绝。R1 已按 Decision 合法失败，不能本地改写。

### Option C — Append a PASS commit to the R1 evidence ref

拒绝。移动 R1 ref 会弱化失败证据的稳定引用；R2 必须使用新 ref。

### Option D — Dynamically accept all discovered Schemas

拒绝。这改变了冻结合同，且把未来新增文件悄然纳入 gate。

### Option E — Skip CE Schema or CE tests

拒绝。CE Schema 3/3 与 CE tests 49/49 都是完整 merge-tree validation 的必要部分。

## Bounded R2 contract

冻结：

```text
canonical=ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
candidate=e6a193f4bf0d48d65649077122f0ab262460daac
merge_tree=9171e554cfcbeaa02d5542c3a35cb729bca44185
r1_evidence=d054b5cf3880904aba84816501b07358fcfb4c06
r2_evidence_ref=codex/ce-g11b-pr23-remediation-candidate-evidence-r2
r2_initial_state=absent
```

后续独立 Decision 最多授权：

- 1 个新 R2 evidence ref、1 个 disposable worktree、1 个 synthetic validation commit；
- 全部 tracked JSON parse/duplicate-key 和 commercial entry Schema 各一次；
- offline/ignore-scripts `npm ci`、`npm ls`、`npm test`、`npm run release:formal` 各一次；
- 三个 exact Schema 的存在性、hash 与 `Draft202012Validator.check_schema` 一次；
- CE test discovery 一次，要求 49/49；
- PASS 或 FAIL Result/Report 只进入 R2 ref，1 commit、1 non-force push。

任何 hash、remote、merge tree、PR state、命令结果或 source status 漂移均 FAIL_CLOSED。
不允许 source/test fix、retry、network fallback 或修改 R1。

## Agent-customer recommendation

```text
CURRENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED_FOR_EXACT_SELECTOR_R2_VALIDATION
RECOMMENDED_FOR_PR_OR_MERGE=false
```

## Non-authorizations

本建议不授权 R2 执行、PR 创建/修改、GitHub review/comment、merge、release、deployment、
Standard Ready、Production、certification、SLA、Truth、Permission 或 commercial offering。

若 exact `qwen3.7-max` 返回 `RECOMMENDED / Option A / confidence>=0.9` 且
blocker=0、correction=0，下一步只允许准备 prospective R2 validation Decision。
