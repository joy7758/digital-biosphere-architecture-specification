---
document_id: DBA-TITMAS-CE-G11B-PR23-REVIEW-CONTRACT-REMEDIATION-AND-FINDING-ADJUDICATION-RECOMMENDATION-0.1
title: TITMAS CE-G11B PR #23 Review Contract Remediation and Finding Adjudication Recommendation v0.1
title_zh: TITMAS CE-G11B PR #23 审查契约修复与问题裁决建议 v0.1
version: 0.1.0
status: recommendation-pending-independent-review
maturity: Development
owner_ref: zhangbin
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G11B PR #23 Review Contract Remediation and Finding Adjudication Recommendation v0.1

## 1. Problem

PR #23 four-lane review 得到：

```text
LANE_A=REQUEST_CHANGES_CONTRACT_FAILURE
LANE_B=PASS
LANE_C=PASS
LANE_D=REQUEST_CHANGES
SYNTHESIS=NOT_EXECUTED
OVERALL=INCOMPLETE_REVIEW
```

Lane A 把 MEDIUM finding 放入仅允许 CRITICAL/HIGH 的 `blocking_findings`。原 wrapper
漏检 severity/array 组合，因此需要修复 review response contract。

同时，A/D 共 10 个 raw blocking-array entries 尚未裁决。已关闭的无效 PR #24 还保留
3 个自动 review observations；它们指向同一 frozen candidate 内容，也必须作为补充输入
进入裁决。模型 finding 是 review observation，不是代码事实或修改授权。

## 2. Read-only direct evidence

### 2.1 Lane A

源码核验显示：

- `_run_suite()` 使用 argument array
  `[sys.executable, "-m", "unittest", "-v", module]`，没有 `shell=True`；
- 两个实际 caller 将 `module` 固定为
  `test_ce_g11_target_bound_correlator.py` 和 `test_ce_g8_diagnostic.py`；
- `FROZEN_INPUTS` 是模块内 constant map，request 必须与该 map exact match；
- `phase_a_commit` 和 `source_commit` 均在 `git merge-base` 前经过
  `[0-9a-f]{40}` regex；
- `safe_environment_value()` 只用于 receipt 的 runner metadata；test subprocess
  environment 由独立 allowlist 构造；
- `error_class` 由 stable `StageFailure.stage_code` 或 exception class name 形成；
- 现有 tests 覆盖 workflow scope、frozen inputs、authority rejection、fixture privacy、
  request schema、version mismatch、allowlisted environment、suite failure、retry rejection
  和 component hash mismatch。

这些事实至少与部分 Lane A claim 发生直接冲突，但不自动证明所有 finding 都无效。

### 2.2 Lane D

- `PROGRAM-STATUS.md` 是 Markdown status surface，不是
  `titmas-commercialization-standards-entry.schema.v0.1.json` 的 instance；
- `TITMAS-COMMERCIALIZATION-STANDARDS-ENTRY-v0.1.json` 才通过该 Schema 验证，已直接
  observed `PASS`；
- `next_decision_candidate.status` 仍指向历史
  `CE_G11B_DRAFT_PR_DECISION_REVIEW_FAIL_CLOSED_REMEDIATION_PENDING`；
- `current_recommended_option` 仍指向历史
  `PREPARE_CE_G11B_DRAFT_PR_DECISION_REVIEW_RETRY_RECOMMENDATION_ONLY`；
- README 的长历史链可能构成 agent-readability debt，但不是自动的 merge blocker；
- immutable-candidate Recommendation 位于最终 freeze commit 之前，执行 Result 位于
  distinct evidence ref；不能仅因 Recommendation 被纳入 candidate 就认定验证自引用。

因此 Lane D 同时包含明显受直接证据反驳的 claim 和可能真实的 nested status drift。

### 2.3 Closed PR #24 supplemental observations

PR #24 错误地把 distinct evidence ref 指向 `main`，已在不修改或删除 evidence ref 的
前提下关闭。关闭错误 merge surface 不丢弃其三个 review observations。对 frozen
candidate 的直接核验显示：

- `PROGRAM-STATUS.md` frontmatter 仍写
  `titmas_ce_g10_execution_completed: false`、`titmas_ce_g10_workflow_runs: 0` 和
  `ce-g10a-single-workflow-run-observation-pending`，而正文已经记录 CE-G10 完成、
  workflow run `30270198036` 以及后续 CE-G11B 状态；
- Footer 仍链接
  `/TITMAS-COMMERCIAL-EVALUATION-PACK-v0.1.json`，而 `agent-index.json`、`llms.txt`
  和 v0.2 manifest 均把 v0.2 标为当前入口，且 v0.2 明确 supersedes v0.1；
- 中英文 commercial evaluation page metadata 仍分别声明
  `第一版商业评估包 v0.1` 和 `Commercial Evaluation Pack v0.1`，页面及当前 manifest
  已使用 v0.2。

这些直接差异支持“可能存在版本／状态一致性债务”，但仍需裁决其 severity、影响范围和
是否要求新的 remediation candidate。

## 3. Options

### Option A — Contract v0.2 + two adjudication lanes + synthesis（推荐）

#### Contract v0.2

取消模型自行选择数组的歧义，只允许单一：

```text
findings[]
```

每个 finding 包含：

- immutable finding id；
- severity；
- path / line or reference；
- claim；
- direct evidence；
- requested correction。

本地 deterministic classifier 根据 severity 派生：

```text
CRITICAL/HIGH -> blocking
MEDIUM/LOW/INFO -> non_blocking
```

模型不能再通过数组位置改变 blocking semantics。

#### Adjudication A

输入：

- Lane A 原始 sanitized review；
- 完整 Lane A patch；
- 上述 direct source excerpts；
- exact caller、data-flow、subprocess 和 test evidence。

逐 finding 输出：

```text
CONFIRMED
PARTIALLY_CONFIRMED
DISPUTED
REJECTED
```

并区分 shell injection、untrusted input、defense-in-depth 和 test-gap。

#### Adjudication D

输入：

- Lane D 原始 sanitized review；
- 完整 Lane D patch；
- PR #24 三个 supplemental review observations 及其 immutable comment identifiers；
- Schema instance boundary；
- direct Schema PASS；
- nested status contexts；
- Footer、agent index、`llms.txt`、v0.2 supersedes marker 与双语 page metadata；
- candidate/evidence branch topology。

逐 finding 裁决 schema claim、status drift、version-link/metadata drift、readability debt
和 self-reference claim。

#### Synthesis

仅在 A/D adjudication 均为 HTTP 200、exact `qwen3.7-max`、direct JSON、finding ID
coverage 完整后执行。结合 B/C PASS，输出：

```text
AGENT_REVIEW_PASS_AFTER_ADJUDICATION
REMEDIATION_CANDIDATE_REQUIRED
INCOMPLETE_ADJUDICATION
```

任何 confirmed CRITICAL/HIGH 或 required correction 都必须得到
`REMEDIATION_CANDIDATE_REQUIRED`。

### Option B — Reclassify Lane A arrays locally and run old synthesis（拒绝）

这等于 JSON repair，会改变模型返回语义并违反 Decision。

### Option C — Accept all A/D findings as truth（拒绝）

多个 claim 与直接源码/Schema evidence 冲突。

### Option D — Reject all findings as hallucinations（拒绝）

Lane D 的 nested status drift 可能真实存在，不能整体丢弃。

## 4. If remediation is required

不得修改 frozen candidate ref 或 PR #23 head。后续必须：

1. 建立新的 remediation candidate branch；
2. 只修改 adjudication confirmed 的文件；
3. 增加对应 tests/Schema/cockpit checks；
4. 重新生成 immutable candidate + external attestation；
5. 另行决定 replacement PR。

PR #23 和所有 finding evidence继续保留。

## 5. Agent-customer recommendation gate

面对“是否应直接采用 PR #23”：

```text
RECOMMENDED=NO_NOT_BEFORE_FINDING_ADJUDICATION
WORTH_CONTINUING=YES
RECOMMENDED_NEXT=OPTION_A
```

原因不是已证明代码有漏洞，而是 review contract 不完整且 findings 未裁决。

## 6. Required Decision

独立 Decision 最多授权：

- exact `qwen3.7-max` adjudication A：1 request；
- exact `qwen3.7-max` adjudication D：1 request；
- gated synthesis：1 request；
- 0 retry/fallback/substitution/JSON repair；
- 0 candidate/PR/GitHub review/comment/merge/release mutation。

## 7. False effects

```text
FINDING_NE_TRUTH=true
ADJUDICATION_NE_CODE_CHANGE_AUTHORIZATION=true
AGENT_REVIEW_NE_GITHUB_APPROVAL=true
PR23_MUTATED=false
PR22_MUTATED=false
MERGE_AUTHORIZED=false
STANDARD_READY=false
```
