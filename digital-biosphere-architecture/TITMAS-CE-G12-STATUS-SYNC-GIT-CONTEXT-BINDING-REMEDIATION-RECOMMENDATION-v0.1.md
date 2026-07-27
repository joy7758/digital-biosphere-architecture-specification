---
document_id: DBA-TITMAS-CE-G12-STATUS-SYNC-GIT-CONTEXT-BINDING-REMEDIATION-RECOMMENDATION-0.1
title: TITMAS CE-G12 Status Sync Git-context Binding Remediation Recommendation v0.1
title_zh: TITMAS CE-G12 状态同步 Git 上下文绑定修正建议 v0.1
version: 0.1.0
status: exact-offline-recommendation-agent-review-required-decision-pending
maturity: Development
maturity_scope: git-prefix-context-binding-only
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G12 Status Sync Git-context Binding Remediation Recommendation v0.1

## 1. Recommendation

采用 **Option A：以 Git repository identity、HEAD/remote equality 和 exact
`git rev-parse --show-prefix` 代替临时目录绝对路径绑定**。

```text
RECOMMENDED_OPTION=A
R3_FAILURE_RECLASSIFIED_AS_PASS=false
FROZEN_FIVE_PATH_PATCH_CHANGED=false
GIT_CONTEXT_DECISION_RECORDED=false
GIT_CONTEXT_EXECUTION_AUTHORIZED=false
```

## 2. Preserved R3 failure

R2 Decision 远端固定后，唯一执行在 validation bundle 之前失败：

```text
FAILURE=FAIL_CLOSED_LOGICAL_PHYSICAL_CWD_ALIAS_MISMATCH
FAILURE_STAGE=VALIDATION_CWD_EXACT_MATCH_PRECONDITION
DECISION_CWD=/tmp/titmas-ce-g11b-decision.2dqOYW/digital-biosphere-architecture
OBSERVED_CWD=/private/tmp/titmas-ce-g11b-decision.2dqOYW/digital-biosphere-architecture
GIT_PREFIX=digital-biosphere-architecture/
RELATIVE_PATH_ASSERTION_STARTED=false
TRACKED_JSON_VALIDATION_STARTED=false
SCHEMA_VALIDATION_STARTED=false
CROSS_FILE_VALIDATION_STARTED=false
```

直接材料：

- [R3 failure record](TITMAS-COMMERCIAL-EVALUATION-CE-G12-STATUS-SYNC-REVALIDATION-R3-FAILURE-v0.1.json)
  SHA-256 `7ecf21c39b63d484e7dc6dff4f86077926593c798b44f338b36ce26d6caf2392`；
- R2 Decision commit `0caf66abbb10c98c360ab333cc5151713f9de49a`；
- frozen patch SHA-256
  `40319c6101bff7da943c230591a5222e6ac107b5ca0d15c598be652af41b4dec`。

R3 failure 不得改写为 PASS。

## 3. Root cause

macOS 将 `/tmp` 物理解析为 `/private/tmp`。Decision 绑定 logical path，而执行前置检查使用
physical path，因此同一 worktree 被误判为不同 cwd。

临时目录绝对路径不是 repository identity。真正需要验证的是：

```text
LOCAL_HEAD == REMOTE_BRANCH_HEAD
GIT_PREFIX == digital-biosphere-architecture/
FROZEN_PATCH_SHA256 == expected
RELATIVE_PATH_SET == exact five paths
```

## 4. Exact Git-context contract

未来独立 Decision 应取消 `/tmp` 或 `/private/tmp` absolute cwd equality，并固定：

```text
REMOTE=origin
BRANCH=codex/ce-g11b-pr23-remediation-candidate-governance
EXPECTED_GIT_PREFIX=digital-biosphere-architecture/
PATH_ENUMERATION=git diff --relative --name-only --
EXPECTED_PATH_COUNT=5
```

前置检查按顺序：

1. `git rev-parse HEAD` 等于 remote branch HEAD；
2. `git rev-parse --show-prefix` exact 等于
   `digital-biosphere-architecture/`；
3. frozen patch SHA-256 exact 匹配；
4. `git diff --relative --name-only --` exact ordered set 匹配五路径。

不允许：

- 比较或持久化 `/tmp`、`/private/tmp` absolute path；
- basename、suffix、substring 或 manual prefix stripping；
- 用 path check 替代 HEAD、remote 或 patch hash。

## 5. Validation bundle

只有 Git-context contract PASS，才允许一次：

1. duplicate-rejecting tracked JSON validation；
2. Commercial Entry exact Schema validation；
3. inherited semantic-key-bound five-path consistency validation；
4. 全部 PASS 后仅提交并推送 frozen five paths。

第一次、R2、R3 三个 failure 均保留。

## 6. Caps and stop rules

```text
GIT_CONTEXT_DECISION_REVIEWS_MAX=1
GIT_CONTEXT_ASSERTION_RUNS_MAX=1
RELATIVE_PATH_ASSERTION_RUNS_MAX=1
TRACKED_JSON_VALIDATION_RUNS_MAX=1
COMMERCIAL_ENTRY_SCHEMA_RUNS_MAX=1
CROSS_FILE_CONSISTENCY_RUNS_MAX=1
FROZEN_PATCH_CHANGES=0
UNRELATED_PATH_CHANGES=0
PATH_SCOPED_COMMITS_MAX=1
PATH_SCOPED_PUSHES_MAX=1
RETRIES=0
FALLBACKS=0
SSH_SESSIONS=0
SERVER_READS=0
SERVER_WRITES=0
NETWORK_REQUESTS=0
DEPLOYMENTS=0
```

任何 Git-context、path、JSON、Schema、cross-file 或 patch mismatch 都立即停止。不得在同一
Decision 中修复或第二次执行。

## 7. Options

### Option A — Git-context identity binding（推荐）

避免 platform-specific temporary path alias，同时保持 exact repository scope。

### Option B — Change `/tmp` to `/private/tmp`（拒绝）

仍把短期物理路径误当作 repository identity，跨环境不可复用。

### Option C — Accept either path with string OR（拒绝）

扩大模糊路径接受面，无法证明实际 Git context。

### Option D — Remove all context checks（拒绝）

可能在错误 repository 或 prefix 中验证同名文件。

## 8. Recommendation review contract

exact `qwen3.7-max` 只允许一次 direct JSON review，必须返回：

```text
verdict
confidence
selected_option
would_recommend_to_agent_customer
r3_failure_preservation_sound
tmp_alias_root_cause_supported
git_context_identity_binding_sound
git_prefix_binding_sound
head_remote_and_patch_binding_sound
no_absolute_temp_path_dependency
one_validation_bundle_scope_minimal
non_authorizations_complete
authority_boundaries_preserved
blockers
corrections
rationale
```

合格阈值：

```text
verdict=RECOMMENDED
confidence>=0.90
selected_option=A
would_recommend_to_agent_customer=true
all_boolean_checks=true
blockers=[]
corrections=[]
```

## 9. Non-authorizations and next gate

```text
RECOMMENDATION_NE_DECISION=true
R3_FAILURE_RECLASSIFICATION_AUTHORIZED=false
FROZEN_PATCH_CHANGE_AUTHORIZED=false
GIT_CONTEXT_EXECUTION_AUTHORIZED=false
STATUS_SYNC_COMMIT_AUTHORIZED=false
STATUS_SYNC_PUSH_AUTHORIZED=false
CURRENT_TARGET_CLASSIFICATION_DECISION_AUTHORIZED=false
SECOND_SSH_AUTHORIZED=false
SERVER_READ_AUTHORIZED=false
SERVER_WRITE_AUTHORIZED=false
NETWORK_EXECUTION_AUTHORIZED=false
REPAIR_AUTHORIZED=false
ROLLBACK_AUTHORIZED=false
REDEPLOYMENT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
STANDARD_READY=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
AUTHORITY_ELEVATION=false
OWNERSHIP_CHANGE=false
PERMISSION_CREATED=false
EVIDENCE_TRUTH_CHANGED=false
```

若 review 合格，下一步只允许：

```text
NEXT_ACTION=PREPARE_CE_G12_STATUS_SYNC_GIT_CONTEXT_BINDING_REMEDIATION_DECISION
NEXT_ACTION_AUTHORIZED=false
```
