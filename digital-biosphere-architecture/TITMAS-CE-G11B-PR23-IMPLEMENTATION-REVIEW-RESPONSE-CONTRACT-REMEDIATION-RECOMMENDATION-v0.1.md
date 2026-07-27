---
document_id: DBA-TITMAS-CE-G11B-PR23-IMPLEMENTATION-REVIEW-RESPONSE-CONTRACT-REMEDIATION-RECOMMENDATION-0.1
title: TITMAS CE-G11B PR #23 Implementation Review Response Contract Remediation Recommendation v0.1
title_zh: TITMAS CE-G11B PR #23 实现审查响应契约修复建议 v0.1
version: 0.1.0
status: exact-recommendation-agent-review-pending-decision-pending
maturity: Development
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
observed_at: 2026-07-28
primary_repository: digital-biosphere-architecture
authority_effect: none
---

# TITMAS CE-G11B PR #23 Implementation Review Response Contract Remediation Recommendation v0.1

## 1. Problem

七路径 remediation patch 已通过全部 deterministic validation，并由 exact
`qwen3.7-max` 返回：

```text
verdict=PASS
changed_paths_coverage=7/7
required_correction_coverage=5/5
blocking_findings=[]
```

但同一结果把 5 个已实现 finding IDs 写入 `required_corrections[]`。旧 Decision 要求
该数组长度为 0，模型请求却没有明确它只表示 outstanding corrections（尚未完成的修正）。

```text
MODEL_RATIONALE_SAYS_CORRECTIONS_IMPLEMENTED=true
REQUIRED_CORRECTIONS_ARRAY_LENGTH=5
QUALIFYING_REVIEW=false
CANDIDATE_COMMIT_CREATED=false
CANDIDATE_PUSHED=false
```

不能本地重解释、重分类、删除数组或重试。失败已在
`TITMAS-CE-G11B-PR23-REMEDIATION-CANDIDATE-IMPLEMENTATION-RESULT-v0.1.json`
和 commit `4c5480fdb668e8a5377a4d067757990d221385d1` 中远端保留。

## 2. Agent-customer recommendation

如果潜在智能体客户询问是否应放弃该候选：

```text
VERDICT=CONDITIONALLY_RECOMMENDED
ABANDON_CANDIDATE_RECOMMENDED=false
DIRECT_COMMIT_RECOMMENDED=false
RECOMMENDED_OPTION=A
```

原因：直接代码、Schema、状态、站点和回归证据全部通过，模型也没有报告 blocker；
当前缺口是 response contract（响应契约）不能区分“已实现修正”与“仍需修正”。

## 3. Frozen unchanged candidate

```text
base_sha=c608fd78d7d50d1733ddd9e19aeb6870c5a08288
local_branch=codex/ce-g11b-pr23-remediation-candidate
candidate_commit_created=false
candidate_remote_ref_created=false
patch_sha256=61c6bffe91df1f3af4731ae3be721998f5e3c8c687ca05cfc4dac74cd07aa0a8
patch_bytes=10409
patch_lines=181
changed_paths=7/7
required_corrections_implemented=5/5
readme_diff=0
new_paths=0
deleted_paths=0
```

新 review 前必须重新计算 exact patch SHA 和路径集合，但不得修改 candidate、重跑测试、
重新 materialize dependency 或创建新 worktree。

## 4. Frozen validation evidence

```text
source_hashes=7/7
tracked_json_parse=1164/1164
duplicate_json_keys=0
commercial_entry_schema_meta=PASS
commercial_entry_instance=PASS
program_status_consistency=PASS
ce_schema_meta=3/3
npm_ci=PASS_1_ATTEMPT_OFFLINE_IGNORE_SCRIPTS
direct_dependencies=23/23
npm_test=15/15_1_ATTEMPT
static_export_verify=PASS_1_ATTEMPT
ce_tests=49/49_1_ATTEMPT
generated_tracked_paths=0
secret_or_absolute_local_path_hits=0
```

日志 hashes：

| evidence | SHA-256 |
|---|---|
| npm ci | `e7582a1527764bdc6231acca0c9ff91d11fd1f0dce93414fc9d9983faa90650a` |
| npm ls | `bc6c837d04159c3212554784d3e352c46d885541632a329d341c9294a5d10a07` |
| npm test | `d0093c92e98a54191f29f1e3e947b12a4c8702fe7a7681dcc32c57ede92412ce` |
| release:formal | `f86bf8131481cdb669acb59d7a457b5f004dcd33ae576b144aa085f2124def0a` |
| CE tests | `8ab6a92d348b11e1020d76ba719bbf896ef6c003f3b2e026520546a545443153` |

实际 `npm test` 与 `release:formal` 均 exit 0。执行 wrapper 随后错误地期望 16 个 site
tests，而 frozen source 实际为 15；该后置断言没有触发命令重跑，也不是产品失败。

## 5. Options

### Option A — Contract v0.2 with separated coverage and outstanding fields（推荐）

新的 implementation-review response contract 取消
`required_corrections[]`，改为两个不重叠字段：

```text
implemented_correction_ids=[
  D-B03,
  D-B04,
  D-S01,
  D-S02,
  D-S03
]

outstanding_required_corrections=[]
```

本地 deterministic qualification：

1. `implemented_correction_ids` 必须与 frozen expected set exact equal；
2. `outstanding_required_corrections` 必须为空；
3. `blocking_findings` 必须为空；
4. `verdict` 必须为 `PASS`；
5. base、patch、paths、validation hashes、model identity 和 Authority boundary 必须匹配；
6. 任一 unknown、missing、duplicate 或 contradictory field 都失败关闭。

通过新的独立 Decision，只授权对 exact unchanged patch 执行一次 fresh
`qwen3.7-max` review。若合格，才允许对已经验证的 7 个路径形成一个 candidate commit
并 push 一次。

### Option B — Locally reinterpret the old array（拒绝）

这会修改模型语义并绕过 zero-max contract，属于未授权 JSON reinterpretation。

### Option C — Remove the five IDs from the stored output（拒绝）

会直接改写模型结果，违反 failure preservation。

### Option D — Retry under the consumed Decision（拒绝）

旧 Decision 的一请求 cap 已用尽，retry count 必须保持 0。

### Option E — Modify candidate source to satisfy a non-specific list（拒绝）

旧模型没有提出任何具体未完成 correction，且 rationale 明确说 5 项已经实现。凭数组歧义
继续改代码会制造 scope drift。

## 6. Contract v0.2 output

模型只能返回以下语义：

```text
verdict=PASS|REQUEST_CHANGES|FAIL
confidence=0..1
base_sha=<exact 40-hex>
patch_sha256=<exact 64-hex>
source_hashes_matched=true|false
changed_paths_exact=true|false
changed_paths_coverage="7/7"
implemented_correction_ids=[string]
implemented_correction_coverage="5/5"
outstanding_required_corrections=[string]
blocking_findings=[string]
d_b05_not_scope_expansion=true|false
entry_schema_consistent=true|false
program_status_consistent=true|false
site_version_consistent=true|false
regression_assertions_sufficient=true|false
json_and_schema_validation_pass=true|false
site_validation_pass=true|false
ce_validation_pass=true|false
wrapper_observation_transparently_classified=true|false
no_hidden_product_failure=true|false
no_out_of_scope_change=true|false
no_old_ref_or_pr_mutation=true|false
no_merge_authority=true|false
no_release_or_deployment_authority=true|false
rationale=string
```

禁止提供 `required_corrections` 字段，避免旧语义再次出现。

## 7. New review qualification

```text
HTTP_STATUS=200
CURL_EXIT=0
REQUESTED_MODEL=qwen3.7-max
RETURNED_MODEL=qwen3.7-max
DIRECT_JSON=true
RETRY=0
FALLBACK=0
MODEL_SUBSTITUTION=0
JSON_EXTRACTION=0
JSON_REPAIR=0
VERDICT=PASS
IMPLEMENTED_CORRECTION_IDS_EXACT=5/5
OUTSTANDING_REQUIRED_CORRECTIONS=0
BLOCKING_FINDINGS=0
```

所有 boolean safety/consistency fields 必须为 true。模型 rationale 不得覆盖结构化失败。

## 8. Bounded next Decision

新的 prospective Decision 最多授权：

- 0 candidate source edits；
- 0 dependency materialization；
- 0 test reruns；
- 0 new worktrees；
- 1 次 exact `qwen3.7-max` review；
- 0 retry/fallback/substitution/extraction/repair；
- 所有 frozen/deterministic/model gate PASS 后 1 candidate commit；
- 1 candidate branch push；
- 1 governance result commit/push。

仍不授权：

- distinct evidence ref 或 evidence validation；
- PR create/update/close/retarget；
- GitHub review/comment；
- merge、release、deployment；
- production、certification、SLA、Standard Ready 或 commercial offering。

## 9. Stop conditions

1. governance result commit `4c5480f...` 未远端匹配；
2. base、patch、7 paths、5 corrections 或 validation hashes 漂移；
3. candidate source/status 在新 review 前变化；
4. 需要重跑 install、tests 或创建新 worktree；
5. request 仍包含旧 `required_corrections` 字段；
6. response 出现 unknown/missing/duplicate key；
7. `implemented_correction_ids` 不是 exact five-ID set；
8. `outstanding_required_corrections` 或 `blocking_findings` 非空；
9. verdict 不是 PASS，或任一 safety/consistency boolean 不是 true；
10. model/transport/direct-JSON contract 不合格或需要 retry/repair；
11. 需要 evidence、PR、merge、release、deployment 或公开状态动作。

## 10. Recommendation review gate

本 Recommendation 的一次 write-ahead exact `qwen3.7-max` review 必须返回：

```text
verdict=RECOMMENDED
selected_option=A
confidence>=0.90
old_failure_preserved=true
contract_ambiguity_proven=true
covered_vs_outstanding_separation_sufficient=true
frozen_patch_preserved=true
no_source_or_test_rerun=true
new_review_request_requires_new_decision=true
candidate_commit_remains_gated=true
evidence_pr_merge_separate=true
blocking_reasons=[]
required_corrections=[]
```

## 11. Non-claims

```text
RECOMMENDATION_REVIEW_REQUESTS_MAX=1
NEW_DECISION_RECORDED=false
NEW_IMPLEMENTATION_REVIEW_AUTHORIZED=false
NEW_IMPLEMENTATION_REVIEW_EXECUTED=false
CANDIDATE_COMMIT_CREATED=false
CANDIDATE_PUSHED=false
EVIDENCE_CREATED=false
PR_MUTATED=false
MERGE=false
RELEASE=false
DEPLOYMENT=false
STANDARD_READY=false
AVAILABLE_COMMERCIAL_OFFERING=false
```
