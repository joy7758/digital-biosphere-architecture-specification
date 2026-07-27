---
document_id: DBA-TITMAS-CE-G11B-PHASE-B-CANONICAL-INTEGRATION-RECOMMENDATION-0.1
title: TITMAS CE-G11B Phase B Canonical Integration Recommendation v0.1
title_zh: TITMAS CE-G11B Phase B 规范分支集成建议 v0.1
version: 0.1.0
status: exact-recommendation-agent-reviewed-recommended-decision-pending
maturity: Development
maturity_scope: ce-g11b-pre-phase-b-canonical-integration
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G11B Phase B Canonical Integration Recommendation v0.1

## 1. Recommendation

建议采用 **Option A：先创建一个 Draft canonical-integration PR（规范分支集成草案
PR）**，把已经远端验证的 CE-G11B 分支提交到
`codex/production-observability-baseline` 审查，但不自动 merge。

这是 Phase B run request 之前的独立 prerequisite gate（前置闸门）。本 Recommendation
不授权创建 PR、merge、有效 run request、workflow run、server access、Phase B execution
或 redeployment。

## 2. Why direct Phase B is not ready

Phase A-R1 已通过并完成远端 clean-clone verification：

```text
PHASE_A_R1_RESULT=PASS_PHASE_A_R1_REVALIDATION_ONLY
REMOTE_HEAD=e032115adbe38cc84bde80cc9b10b96f6da1b428
REMOTE_RESULT_SCHEMA_PASS=true
REMOTE_ENTRY_SCHEMA_PASS=true
REMOTE_CANDIDATE_HASHES_PASS=5/5
REMOTE_FORBIDDEN_INSTANCES_ABSENT=true
REMOTE_CE_G11B_WORKFLOW_RUNS=0
```

但 workflow 的 frozen trigger 只接受：

```text
branch=codex/production-observability-baseline
path=digital-biosphere-architecture/commercial-evaluation-controller-tls-diagnosis/ce-g11b-run-request.v0.1.json
```

当前 remote topology：

```text
canonical_branch=codex/production-observability-baseline
canonical_commit=4c95f6b68c21e4bf6e9babb8bd1afa4977cd418a
ce_g11b_branch=codex/ce-g11b-phase-a-decision
ce_g11b_commit=e032115adbe38cc84bde80cc9b10b96f6da1b428
merge_base=4c95f6b68c21e4bf6e9babb8bd1afa4977cd418a
ce_g11b_commits_ahead=5
ce_g11b_changed_files=21
site_paths_in_branch_diff=0
existing_pull_requests_from_head=0
```

因此，直接在 CE-G11B branch 创建 run request 不会满足 frozen branch trigger；直接修改
trigger 又会改变已经审查的 candidate hash。先进行规范分支集成是必要的。

## 3. Options

### Option A — Draft PR, review, then separate merge Decision（推荐）

创建一个 Draft PR：

```text
repository=joy7758/digital-biosphere-architecture-specification
base=codex/production-observability-baseline
head=codex/ce-g11b-phase-a-decision
base_commit_expected=4c95f6b68c21e4bf6e9babb8bd1afa4977cd418a
head_commit_expected=e032115adbe38cc84bde80cc9b10b96f6da1b428
changed_files_expected=21
site_paths_expected=0
auto_merge=false
merge_authorized=false
```

PR 只暴露 exact branch diff 供审查。创建 Draft PR 本身不改变 base branch，不触发 frozen
run-request path，也不产生 Phase B authorization。

### Option B — Direct fast-forward push to canonical（不推荐）

虽然 remote canonical 是 CE-G11B branch 的 ancestor，直接 fast-forward 技术上可行，
但会绕过独立 review/merge Decision，并使并行网站工作树更难对齐。

### Option C — Retarget workflow to CE-G11B branch（拒绝）

修改 workflow branch filter 会改变 frozen candidate hash，必须重新进入 Recommendation、
Decision、local validation 和 Max review；同时会让验证发生在非 canonical baseline。

### Option D — Mix local website commits into integration（禁止）

网站并行工作与 CE-G11B 标准证据属于不同 scope。不得把任何 `site/` path、网站 commit
或未提交网站状态混入本集成。

## 4. Exact Draft PR candidate

只有后续独立 Decision 可以授权：

1. 再次确认 base/head/merge-base exact hashes；
2. 确认 head 恰好包含以下五个 commits：

```text
73a1f8df08cd96f9ccdc5208e34a6fb4cb7755d8  governance: authorize CE-G11B Phase A components
13fdf8babf0234bf1f03caaa57c6a1fc84073907  standards: fail close CE-G11B Phase A model cap
c8e1977e3406e58215d115434e32d2a6de89d92b  standards: recommend CE-G11B Phase A model cap remediation
fcab763ccdd8077a0f77c7fa879af3979357f0e7  governance: authorize CE-G11B Phase A-R1 revalidation
e032115adbe38cc84bde80cc9b10b96f6da1b428  standards: pass CE-G11B Phase A-R1 revalidation
```

3. 确认 diff 中 `site/` path 数量为 0；
4. 确认有效 run request 和 final cross-version result 仍不存在；
5. 确认 CE-G11B workflow runs 仍为 0；
6. 创建一个 Draft PR，不设置 auto-merge，不 merge；
7. 保存 PR number/URL、base/head hashes、changed files、mergeability observation 和
   checks observation；
8. 创建后再次确认 base branch 没有变化且 workflow runs 仍为 0。

## 5. Review and merge separation

Draft PR 创建后仍需要：

```text
PR_CREATED_NE_PR_APPROVED=true
PR_REVIEW_NE_MERGE_DECISION=true
MERGE_DECISION_NE_MERGE_EXECUTION=true
MERGE_NE_PHASE_B_RUN_REQUEST_AUTHORIZATION=true
```

只有新的 independent merge Recommendation/Decision 才能允许 merge。merge 完成并验证
canonical branch 后，还需要另一个 Phase B run-request Recommendation/Decision 才能创建
唯一 run request。

## 6. Agent-customer recommendation gate

`qwen3.7-max` 已对本文件的 pre-review exact bytes（SHA-256
`cd5603bb7096475b54f266bffd5d36b7fc01cce88563e5d7b8585ced94e9347a`）完成一次
independent review。最终文件只追加审查回执和结果，没有改变 topology、Option A、
caps、stop conditions 或 non-claims。

[Sanitized review record](TITMAS-CE-G11B-PHASE-B-CANONICAL-INTEGRATION-QWEN-REVIEW-v0.1.json)
记录：

```text
PRIMARY_REVIEW_MODEL=qwen3.7-max
RETURNED_MODEL=qwen3.7-max
RETURNED_MODEL_EQUALS_REQUESTED=true
REVIEW_VERDICT=RECOMMENDED
SELECTED_OPTION=A
WOULD_RECOMMEND_TO_AGENT_CUSTOMER=true
CONFIDENCE=0.95
TOPOLOGY_REASONING_COHERENT=true
DRAFT_PR_BOUNDARY_PRESERVED=true
SITE_SCOPE_ISOLATED=true
WORKFLOW_RUN_BOUNDARY_PRESERVED=true
MERGE_REQUIRES_SEPARATE_DECISION=true
PHASE_B_AUTHORIZED=false
BLOCKING_REASONS=0
REQUIRED_CORRECTIONS=0
```

模型 review 是 advisory input，不是 PR、merge 或 Phase B Authority。

## 7. Caps and stop conditions

Draft PR Decision candidate 应固定：

```text
PR_CREATION_ATTEMPTS_MAX=1
PR_CREATED_MAX=1
PR_MERGES=0
AUTO_MERGE=false
COMMITS_CREATED=0
PUSHES=0
VALID_RUN_REQUESTS_CREATED=0
WORKFLOW_RUNS=0
MODEL_REQUESTS_DURING_PR_CREATION=0
SITE_PATHS_INCLUDED=0
TARGET_PUBLIC_SITE_REQUESTS=0
SSH_SESSIONS=0
SERVER_READS=0
SERVER_WRITES=0
DEPLOYMENTS=0
DBOS_CHANGES=0
SAEE_CHANGES=0
```

出现以下任一情况必须停止：

- base/head/merge-base/hash/commit set 漂移；
- diff 出现 `site/`、credential、private material 或未授权 path；
- 有效 run request 或 final cross-version result 出现；
- PR 已存在但身份、base/head 或状态不匹配；
- PR 创建需要 push、force push、merge、auto-merge 或 base branch mutation；
- CE-G11B workflow run count 大于 0；
- 需要 server、deployment、DBOS、SAEE、site 或 live-binding change；
- PR 被描述为 merge approval、Phase B authorization、remote matrix PASS、Production、
  Certification、SLA 或 Commercial Offering。

## 8. Non-claims and next gate

```text
RECOMMENDATION_PREPARED=true
PHASE_A_R1_REMOTE_BASELINE_VERIFIED=true
PRE_DECISION_AGENT_REVIEW_COMPLETE=true
PRE_DECISION_AGENT_REVIEW_VERDICT=RECOMMENDED
PRE_DECISION_AGENT_REVIEW_CONFIDENCE=0.95
DRAFT_PR_DECISION_RECORDED=false
DRAFT_PR_CREATION_AUTHORIZED=false
DRAFT_PR_CREATED=false
PR_APPROVED=false
MERGE_AUTHORIZED=false
MERGED=false
VALID_RUN_REQUEST_CREATED=false
WORKFLOW_RUNS=0
PHASE_B_AUTHORIZED=false
REMOTE_CROSS_VERSION_VALIDATION_PASS=false
LIVE_BINDING_CREATED=false
REDEPLOYMENT=false
PRODUCTION_READY=false
CERTIFICATION=false
SLA=false
COMMERCIAL_OFFERING=false
```

下一步只允许依据 standing directive 建立 exact Draft PR Creation Decision，并由
`qwen3.7-max` 对 Decision exact bytes 做独立 pre-execution review。当前仍不得创建 PR、
merge、run request 或 workflow run。
