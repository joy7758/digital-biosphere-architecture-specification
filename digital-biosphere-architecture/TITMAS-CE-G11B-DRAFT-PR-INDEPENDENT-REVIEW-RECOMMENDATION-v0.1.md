---
document_id: DBA-TITMAS-CE-G11B-DRAFT-PR-INDEPENDENT-REVIEW-RECOMMENDATION-0.1
title: TITMAS CE-G11B Draft PR Independent Review Recommendation v0.1
title_zh: TITMAS CE-G11B Draft PR 独立审查建议 v0.1
version: 0.1.0
status: exact-recommendation-agent-review-pending-decision-pending
maturity: Development
maturity_scope: ce-g11b-draft-pr-independent-review
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G11B Draft PR Independent Review Recommendation v0.1

## 1. Recommendation

建议采用 **Option A：对 Draft PR #22 的 frozen head diff 执行一次只读、write-ahead、
exact `qwen3.7-max` independent review**。

本闸门只回答：

> PR #22 的精确差异是否适合进入独立 merge Recommendation 准备？

它不授权 PR comment、Ready for review、approval、merge、run request、workflow、
Phase B、site change、server access、deployment 或 release。

## 2. Frozen review target

```text
repository=joy7758/digital-biosphere-architecture-specification
pull_request=22
pull_request_state=OPEN
pull_request_draft=true
base_branch=codex/production-observability-baseline
base_commit=4c95f6b68c21e4bf6e9babb8bd1afa4977cd418a
head_branch=codex/ce-g11b-phase-a-decision
head_commit=e032115adbe38cc84bde80cc9b10b96f6da1b428
merge_base=4c95f6b68c21e4bf6e9babb8bd1afa4977cd418a
commits_ahead=5
changed_files=21
site_paths=0
head_branch_actions_runs=0
valid_run_request_present=false
final_cross_version_result_present=false
```

如果任一 topology 值漂移，停止并重新形成 Recommendation。

## 3. Review package

一次 review request 必须包含：

1. 本 Recommendation 的 exact source hash；
2. PR #22 的 base/head/merge-base 和 GitHub state observation；
3. `git diff --stat`；
4. 21 个 changed path；
5. exact unified diff；
6. Phase A-R1 result、报告和 Decision 的直接引用；
7. 当前 Actions run count、run-request absence 和 site-path count；
8. 以下审查契约。

不得包含 credential、provider raw envelope、private material、hidden reasoning 或网站内容。

## 4. Review dimensions

`qwen3.7-max` 必须分别判断：

- `scope_integrity`：21 个路径是否均属于 CE-G11B Phase A-R1；
- `historical_failure_preservation`：旧 Phase A fail-closed 是否保留；
- `authority_boundary`：workflow、runner、Schema 或文档是否产生 merge、Phase B、
  deployment、Permission、Evidence Truth 或 production authority；
- `trigger_boundary`：workflow 是否只接受有效、目标绑定的 `workflow_dispatch` 输入；
- `fail_closed_behavior`：无效 input、hash、Schema、job 或 aggregate 是否失败关闭；
- `cross_version_matrix_coherence`：Python 3.10–3.14 matrix 与 aggregate 是否一致；
- `security_and_privacy`：是否写入 credential、raw provider content、private material 或
  不必要的 write permission；
- `compatibility_and_maintainability`：Python 3.10 语法兼容、依赖边界、测试可读性和
  agent-readable contract 是否合格；
- `site_isolation`：diff 中是否为 0 个 `site/` path；
- `merge_readiness_recommendation`：是否值得进入独立 merge Recommendation 准备。

## 5. Review contract

唯一合格输出为 direct JSON：

```text
verdict=PASS|REVISE|REJECT
confidence=0..1
would_recommend_to_agent_customer=true|false
scope_integrity=true|false
historical_failure_preserved=true|false
authority_boundary_preserved=true|false
trigger_boundary_fail_closed=true|false
result_aggregation_fail_closed=true|false
cross_version_matrix_coherent=true|false
security_privacy_boundary_preserved=true|false
python_3_10_compatible=true|false
agent_readable=true|false
site_isolation_preserved=true|false
merge_recommendation_preparation_warranted=true|false
blocking_findings=[]
required_corrections=[]
rationale=string
```

进入下一 gate 必须全部满足：

```text
returned_model=qwen3.7-max
http_status=200
direct_json_parse_pass=true
contract_pass=true
verdict=PASS
would_recommend_to_agent_customer=true
all_boolean_checks=true
blocking_findings=0
required_corrections=0
```

## 6. Write-ahead and request accounting

网络前必须持久化 sanitized `STARTED` record；收到响应后，先持久化 HTTP、response
hash、byte count 和 returned-model observation，再解析正文，最终原子写入终态。

```text
REVIEW_REQUESTS_EXACT=1
RETRY=0
FALLBACK=0
MODEL_SUBSTITUTION=0
ALIAS_INFERENCE=0
EXTRACTION_REQUEST=0
JSON_REPAIR_REQUEST=0
RAW_PROVIDER_ENVELOPE_PERSISTED=false
PROVIDER_ERROR_BODY_PERSISTED=false
```

## 7. Options

### Option A — One bounded read-only Max review（推荐）

保留 PR 为 Draft，执行一次 exact review，形成 sanitized result 和报告。

### Option B — Merge without independent review（禁止）

PR creation、`MERGEABLE` 或 `CLEAN` observation 不等于 merge recommendation 或 approval。

### Option C — Review with a lower or substituted model（禁止）

不允许 `qwen3.7-plus`、alias、fallback 或其他 provider 冒充当前商业化质量基线。

### Option D — Add GitHub comments or reviewers during review（禁止）

本闸门只读，不改变 PR 协作状态。

## 8. Caps and stop conditions

```text
PR_READS_ALLOWED=true
LOCAL_DIFF_READS_ALLOWED=true
MODEL_REQUESTS_MAX=1
PR_COMMENTS=0
PR_REVIEWS_SUBMITTED=0
REVIEWERS_ADDED=0
READY_FOR_REVIEW_TRANSITIONS=0
MERGES=0
VALID_RUN_REQUESTS_CREATED=0
WORKFLOW_RUNS=0
SITE_PATHS_CHANGED=0
SERVER_ACTIONS=0
DEPLOYMENTS=0
DBOS_CHANGES=0
SAEE_CHANGES=0
```

立即停止：

- topology、PR state、draft flag、Actions run count 或 forbidden instance 漂移；
- exact diff 无法形成；
- write-ahead 顺序失败；
- returned model 不是 exact `qwen3.7-max`；
- 需要 retry、fallback、substitution、extraction 或 repair；
- 审查发现 blocker/correction；
- 需要修改 frozen head；
- 结果被描述为 merge approval、Phase B authorization、remote validation PASS、
  production、certification、SLA 或 commercial offering。

## 9. Non-claims and next gate

```text
RECOMMENDATION_PREPARED=true
INDEPENDENT_PR_REVIEW_EXECUTED=false
MERGE_RECOMMENDATION_PREPARED=false
MERGE_AUTHORIZED=false
PR_MERGED=false
VALID_RUN_REQUEST_CREATED=false
WORKFLOW_RUNS=0
PHASE_B_AUTHORIZED=false
PRODUCTION_READY=false
CERTIFICATION=false
SLA=false
COMMERCIAL_OFFERING=false
```

只有本 Recommendation 先通过 exact `qwen3.7-max` advisory review，并由新的独立
Decision 授权后，才可执行 PR #22 的一次只读 review。
