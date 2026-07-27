---
document_id: DBA-TITMAS-CE-G12-STATUS-SYNC-PATH-NORMALIZATION-REMEDIATION-RECOMMENDATION-0.1
title: TITMAS CE-G12 Status Sync Path Normalization Remediation Recommendation v0.1
title_zh: TITMAS CE-G12 状态同步路径归一化修正建议 v0.1
version: 0.1.0
status: exact-offline-recommendation-agent-review-required-decision-pending
maturity: Development
maturity_scope: repository-root-path-normalization-only
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G12 Status Sync Path Normalization Remediation Recommendation v0.1

## 1. Recommendation

采用 **Option A：使用 Git `--relative` 语义固定 DBA 子目录相对路径，并通过新的独立
Decision 执行一次完整离线验证**。

```text
RECOMMENDED_OPTION=A
R2_FAILURE_RECLASSIFIED_AS_PASS=false
FROZEN_FIVE_PATH_PATCH_CHANGED=false
PATH_NORMALIZATION_DECISION_RECORDED=false
PATH_NORMALIZATION_EXECUTION_AUTHORIZED=false
```

## 2. Preserved R2 failure

Remediation Decision 远端固定后，唯一 revalidation 在第一项 exact-path assertion 失败：

```text
FAILURE=FAIL_CLOSED_REPOSITORY_ROOT_PATH_NORMALIZATION_MISMATCH
FAILURE_STAGE=EXACT_FIVE_TARGET_PATH_ASSERTION
EXPECTED_PATH_BASIS=DBA_SUBDIRECTORY_RELATIVE
OBSERVED_PATH_BASIS=REPOSITORY_ROOT_RELATIVE
EXPECTED_FIRST_PATH=MASTER-ROADMAP.md
OBSERVED_FIRST_PATH=digital-biosphere-architecture/MASTER-ROADMAP.md
TRACKED_JSON_VALIDATION_STARTED=false
COMMERCIAL_ENTRY_SCHEMA_VALIDATION_STARTED=false
CROSS_FILE_CONSISTENCY_VALIDATION_STARTED=false
```

直接材料：

- [R2 failure record](TITMAS-COMMERCIAL-EVALUATION-CE-G12-STATUS-SYNC-REVALIDATION-R2-FAILURE-v0.1.json)
  SHA-256 `3703fb13b3ef8b0a7b58a86355e5bf8145d02498c64eb7a838edad61cedf880e`；
- remediation Decision commit `435bc76bd2a7147ca116fa29bd3a1a3029ff1bba`；
- frozen patch SHA-256
  `40319c6101bff7da943c230591a5222e6ac107b5ca0d15c598be652af41b4dec`。

R2 failure 不得重写为 PASS。

## 3. Root cause

worktree 的 Git repository root 位于 DBA 子目录上方。验证器在 DBA 子目录运行：

```text
git diff --name-only
```

但 Git 输出仍以 repository root 为基准：

```text
digital-biosphere-architecture/MASTER-ROADMAP.md
```

Decision 的 `exact_target_paths` 以 DBA 主责任仓库内容根为基准：

```text
MASTER-ROADMAP.md
```

两者表示同一文件，但 validation harness 没有固定 path basis。

## 4. Exact correction

未来独立 Decision 应固定：

```text
VALIDATION_CWD=/tmp/titmas-ce-g11b-decision.2dqOYW/digital-biosphere-architecture
PATH_BASIS=DBA_SUBDIRECTORY_RELATIVE
PATH_ENUMERATION=git diff --relative --name-only --
EXPECTED_PATH_COUNT=5
```

只允许 exact ordered set：

```text
MASTER-ROADMAP.md
PROGRAM-STATUS.md
TITMAS-COMMERCIALIZATION-STANDARDS-ENTRY-v0.1.json
architecture/schemas/titmas-commercialization-standards-entry.schema.v0.1.json
architecture/titmas-commercialization-standards-roadmap-v0.1.md
```

禁止通过 basename-only、suffix match、substring 或去除任意目录前缀来接受路径。

若路径集合 PASS，才执行：

1. 一次 duplicate-rejecting tracked JSON validation；
2. 一次 Commercial Entry exact Schema validation；
3. 一次已固定的 semantic-key-bound five-path consistency validation；
4. 全部 PASS 后仅提交并推送 exact five paths。

## 5. Caps and stop rules

```text
PATH_NORMALIZATION_DECISION_REVIEWS_MAX=1
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

停止条件：

- failure/Recommendation/Review/Decision 尚未远端固定；
- cwd、path basis、ordered set 或 frozen patch SHA 不一致；
- relative path assertion 失败；
- 后续任一 validation 失败；
- 需要第二次执行、patch 修改或 unrelated fix；
- 需要 SSH、server/network action、repair、rollback、redeployment 或 release。

## 6. Options

### Option A — `git diff --relative --name-only --`（推荐）

由 Git 明确产生当前 DBA 子目录相对路径，不做模糊转换。

### Option B — Strip `digital-biosphere-architecture/` manually（拒绝）

手工字符串裁剪可能接受非预期前缀或隐藏路径漂移。

### Option C — Compare basenames only（拒绝）

不同目录的同名文件会错误通过。

### Option D — Skip exact path assertion（拒绝）

无法证明五路径 scope 未扩大。

## 7. Recommendation review contract

exact `qwen3.7-max` 只允许一次 direct JSON review，必须返回：

```text
verdict
confidence
selected_option
would_recommend_to_agent_customer
r2_failure_preservation_sound
repository_root_diagnosis_supported
git_relative_path_binding_sound
exact_ordered_set_sound
no_fuzzy_path_acceptance
frozen_patch_unchanged
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

## 8. Non-authorizations and next gate

```text
RECOMMENDATION_NE_DECISION=true
R2_FAILURE_RECLASSIFICATION_AUTHORIZED=false
FROZEN_PATCH_CHANGE_AUTHORIZED=false
PATH_NORMALIZATION_EXECUTION_AUTHORIZED=false
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
NEXT_ACTION=PREPARE_CE_G12_STATUS_SYNC_PATH_NORMALIZATION_REMEDIATION_DECISION
NEXT_ACTION_AUTHORIZED=false
```
