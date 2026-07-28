---
document_id: DBA-TITMAS-CE-G12-CURRENT-TARGET-DISPOSITION-RECOMMENDATION-0.1
title: TITMAS CE-G12 Current-target Disposition Recommendation v0.1
title_zh: TITMAS CE-G12 当前目标处置建议 v0.1
version: 0.1.0
status: candidate-supersession-and-fresh-immutable-candidate-preparation-recommendation-agent-review-required-decision-pending
maturity: Development
maturity_scope: commercial-static-site-candidate-disposition-only
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G12 Current-target Disposition Recommendation v0.1

## 1. Recommendation

采用 **Option C：保留旧证据、提出 supersede（替代）旧 `f810796…` proposed contract，并以
PR #27 merge commit `c1d8931…` 准备一个新的 immutable candidate**。

```text
RECOMMENDED_OPTION=C
OLD_PROPOSED_RELEASE=f8107969aa1f43be8ecf43f557297a630309fe41
FRESH_CANDIDATE_SOURCE=c1d8931930fbae15f96ee6a6ac050b081538c919
OLD_CANDIDATE_HISTORY_PRESERVED=true
OLD_CANDIDATE_SUPERSEDED=false
FRESH_CANDIDATE_PREPARED=false
FRESH_CANDIDATE_ADOPTED=false
DEPLOYMENT_RECOMMENDED=false
RELEASE_RECOMMENDED=false
DISPOSITION_DECISION_RECORDED=false
```

本建议只选择后续 candidate preparation 的方向。它不在当前动作中：

- 废弃或删除旧 evidence；
- 修改 CE-G7/CE-G12 历史 Result；
- 构建 archive；
- 创建 release directory；
- 读取或修改服务器；
- 切换 symlink；
- 部署、发布或声明 commercial availability。

## 2. Direct evidence bindings

### 2.1 Current target and lineage

- [Lineage Result](commercial-evaluation-exact-redeployment/ce-g12-current-target-lineage-reconciliation-result.v0.1.json)
  SHA-256 `2afa3d7851d6a8ca6733afa8360e371358d70075f6d94c8e740284fa3ceb073b`；
- [Lineage Report](TITMAS-CE-G12-CURRENT-TARGET-LINEAGE-RECONCILIATION-REPORT-v0.1.md)
  SHA-256 `9d19e10761654f03eb9dd08939839c9830b67795ba61066daf0cc2cf89d6ba0b`；
- lineage evidence commit `406270a3d0bae37894cda03ba7f8c1824b41775a`。

已证明：

```text
7da4bcf_IS_ANCESTOR_OF_f810796=true
f810796_IS_ANCESTOR_OF_ccf473f=true
ccf473f_IS_FIRST_PARENT_OF_c1d8931=true
CURRENT_TARGET=ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
REMOTE_PRODUCTION_BASELINE=c1d8931930fbae15f96ee6a6ac050b081538c919
```

仍未知：

```text
CCF473F_DEPLOYMENT_AUTHORIZED=UNKNOWN
CCF473F_DEPLOYMENT_RECEIPT_FOUND=false
CCF473F_SWITCH_SOURCE=UNKNOWN
CCF473F_IS_STALE=UNKNOWN
CCF473F_IS_UNAUTHORIZED=UNKNOWN
```

### 2.2 Old proposed release

- [CE-G7 Result](commercial-evaluation-exact-redeployment/ce-g7-result.v0.1.json)
  SHA-256 `08fbeae76848886950029c1c4fc445ad665bff324a1a1bd18566817b6cbd8276`；
- [CE-G7 Proposed Hash Baseline](commercial-evaluation-exact-redeployment/ce-g7-proposed-release-hash-baseline.v0.1.json)
  SHA-256 `173fa2a0972bbbf3f61d4a649a1331249334c0fa003a668da200318a7858f7fc`。

old proposed：

```text
SOURCE_REVISION=f8107969aa1f43be8ecf43f557297a630309fe41
CE_G7_RESULT=FAIL_CLOSED_ROLLBACK_PASS
NEW_CONTRACT_WEBSITE_DEPLOYED=false
REDEPLOYMENT_ADMISSION_PASS=false
```

`f810796…` 仍是有效历史证据对象，但不是 fresh remote integration baseline。

### 2.3 Fresh candidate basis

- [PR #27 Merge and Validation Result](TITMAS-CE-G11B-PR27-MERGE-EXECUTION-AND-POST-MERGE-VALIDATION-RESULT-v0.1.json)
  SHA-256 `bda16758916a8df843c84bd5ca803b7a50d3343e5248f56ba94b944509d64c86`。

`c1d8931…` 已具备 repository-level candidate basis：

```text
PR27_STATE=MERGED
REMOTE_BASE_HEAD=c1d8931930fbae15f96ee6a6ac050b081538c919
MERGE_TREE=9171e554cfcbeaa02d5542c3a35cb729bca44185
TRACKED_JSON_PASS=1165
DUPLICATE_KEYS=0
COMMERCIAL_ENTRY_SCHEMA_PASS=true
CE_SCHEMA_HASHES_PASS=3/3
CE_META_SCHEMAS_PASS=3/3
NPM_CI_OFFLINE_PASS=true
SITE_TESTS_PASS=16/16
RELEASE_FORMAL_STATIC_EXPORT_PASS=true
RELEASE_FORMAL_CONTENT_PARITY_PASS=true
RELEASE_FORMAL_TRUTH_BOUNDARY_PASS=true
RELEASE_FORMAL_MANIFEST_FILES=65
CE_TESTS_PASS=49/49
TRACKED_SOURCE_DIFF=0
REMOTE_DRIFT=0
```

这些是 candidate-preparation evidence，不是 release/deployment authority。原 Result 明确：

```text
GITHUB_CHECKS_SUCCESS=false
HUMAN_REVIEW_EQUIVALENCE=false
RELEASE_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
STANDARD_READY=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
```

## 3. Candidate freshness assessment

exact repository facts：

```text
f810796_IS_ANCESTOR_OF_c1d8931=true
ccf473f_IS_ANCESTOR_OF_c1d8931=true
REMOTE_PRODUCTION_BASELINE_HEAD=c1d8931930fbae15f96ee6a6ac050b081538c919
```

相对 `ccf473f…`，`c1d8931…` 的 merge tree 包含新的 commercial-standard integration
surface，包括：

- commercialization entry 与 Schema 更新；
- bilingual commercial-evaluation routes 更新；
- agent-readable README 与状态材料；
- CE-G11B cross-version runner、Schema 和测试；
- 已通过的 formal static export 和 truth-boundary validation。

因此：

```text
F810796_HISTORICAL_EVIDENCE_VALID=true
F810796_FRESH_CANDIDATE_BASIS=false
C1D8931_FRESH_CANDIDATE_BASIS=true
C1D8931_RELEASE_READY=false
C1D8931_DEPLOYMENT_READY=false
```

## 4. Why Option C best advances commercialization

继续围绕 `f810796…` redeploy 会把发布内容固定在 PR #27 integration 之前，并重复已经发生的
candidate drift。直接采用 current `ccf473f…` 会绕过 deployment receipt 和 PR #27
integration。直接 rollback 会改变服务器而没有新的处置 Decision。

Option C 把下一步收敛为：

1. 保留 CE-G7 failure/rollback 和 `f810796…` archive/hash history；
2. 通过独立 Decision 将旧 proposed contract 标记为
   `SUPERSEDED_FOR_FRESH_CANDIDATE_PREPARATION`，而不是 deleted/revoked；
3. 从 exact `c1d8931…` 在 disposable clean worktree 中重新生成 static export；
4. 建立新的 candidate archive、manifest、route hash baseline 和 validation Result；
5. 停在 candidate prepared，不接触服务器；
6. 后续再决定 current-target preflight、rollback baseline 和 deployment admission。

这比继续调查 current symlink 的历史来源更直接推进第一版商业候选，同时不牺牲证据链。

## 5. Exact future candidate-preparation scope

未来独立 Decision 最多授权：

1. 要求 Recommendation、review、Decision 和 Decision review 已远端固定；
2. 核对 remote production baseline 仍为 exact `c1d8931…`；
3. 创建一个 disposable clean worktree at exact `c1d8931…`；
4. 对 tracked JSON 执行 parse 与 duplicate-key validation；
5. 验证 commercialization entry against exact Schema；
6. 使用已缓存依赖执行一次 offline `npm ci --ignore-scripts`；
7. 执行一次 `npm ls`、一次 site tests、一次 `npm run release:formal` 和一次 CE tests；
8. 要求 source/tree drift 为 0；
9. 从 exact static export 生成一个新的 candidate archive、SHA-256、manifest 和 route baseline；
10. 生成 Candidate Result 和 Report；
11. 清理 disposable worktree；
12. 只提交 candidate-preparation artifacts，不修改 server 或 public site。

候选 artifact 应使用新的 identity，不复用：

```text
/tmp/titmas-site-f8107969aa1f43be8ecf43f557297a630309fe41.tar.gz
/srv/tmai/releases/f8107969aa1f43be8ecf43f557297a630309fe41
```

未来 candidate source identity 固定为：

```text
c1d8931930fbae15f96ee6a6ac050b081538c919
```

## 6. Candidate-preparation caps

未来 Decision 应保持：

```text
QWEN_DECISION_REVIEW_REQUESTS_MAX=1
DISPOSABLE_WORKTREES_MAX=1
NPM_CI_ATTEMPTS_MAX=1
NPM_LS_ATTEMPTS_MAX=1
SITE_TEST_ATTEMPTS_MAX=1
RELEASE_FORMAL_ATTEMPTS_MAX=1
CE_TEST_ATTEMPTS_MAX=1
CANDIDATE_ARCHIVES_MAX=1
SERVER_READS=0
SERVER_WRITES=0
PUBLIC_SITE_REQUESTS=0
SSH_SESSIONS=0
SYMLINK_SWITCHES=0
NGINX_RELOADS=0
ROLLBACKS=0
DEPLOYMENTS=0
RELEASES=0
PR_MUTATIONS=0
RETRIES=0
NETWORK_FALLBACKS=0
MODEL_REQUESTS_DURING_PREPARATION=0
```

## 7. Options

### Option A — Continue redeployment planning for `f810796…`（拒绝）

它保留历史价值，但已不是 current remote integration baseline，并缺少 PR #27 新增 surface。

### Option B — Adopt current `ccf473f…` as approved target（拒绝）

current observation、canonical directory 和 Git ancestry 不等于 deployment authorization 或
fresh candidate adoption。

### Option C — Supersede old proposed contract and prepare `c1d8931…` candidate（推荐）

保留历史证据，用 fresh merged and validated source 建立新的 immutable candidate；当前不部署。

### Option D — Immediate rollback, repair or deployment（拒绝）

缺少新的 candidate package、fresh target preflight、rollback disposition 和独立 execution
Decision。

## 8. Stop conditions

- Recommendation 或 review 未远端固定；
- 返回模型不是 exact `qwen3.7-max`；
- lineage Result/Report 或 PR #27 Result hash 漂移；
- remote production baseline 不再是 exact `c1d8931…`；
- 需要覆盖、删除或改写 `f810796…` 历史 evidence；
- 需要把 `ccf473f…` 解释为 authorized、unauthorized、safe、stale 或 root cause；
- 需要在 Recommendation 动作中构建 archive 或运行 candidate preparation；
- future preparation 需要 network fallback、第二 worktree、retry 或 source fix；
- 需要任何 server/public-site/SSH/symlink/nginx/rollback/deployment/release/PR mutation；
- candidate prepared 被升级为 Standard Ready、Production、commercial offering、SLA 或
  certification。

## 9. Recommendation review contract

exact `qwen3.7-max` 只允许一次 direct JSON review，必须返回：

```text
verdict
confidence
selected_option
would_recommend_to_agent_customer
lineage_evidence_sufficient
old_candidate_supersession_justified
c1d893_candidate_basis_justified
candidate_preparation_only_scope_sound
history_preservation_sound
current_target_boundary_sound
no_deployment_or_release_inference
candidate_validation_requirements_sufficient
caps_and_stop_rules_sufficient
no_server_repair_or_redeployment_authority
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
selected_option=C
would_recommend_to_agent_customer=true
all_boolean_checks=true
blockers=[]
corrections=[]
```

## 10. Non-authorizations and next gate

```text
RECOMMENDATION_NE_DECISION=true
OLD_CANDIDATE_SUPERSEDED=false
FRESH_CANDIDATE_PREPARATION_AUTHORIZED=false
FRESH_CANDIDATE_PREPARED=false
SERVER_READ_AUTHORIZED=false
SERVER_WRITE_AUTHORIZED=false
SYMLINK_CHANGE_AUTHORIZED=false
ROLLBACK_AUTHORIZED=false
REDEPLOYMENT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
PR_MUTATION_AUTHORIZED=false
STANDARD_READY=false
PRODUCTION_READY=false
SLA=false
CERTIFICATION=false
COMMERCIAL_OFFERING=false
AUTHORITY_ELEVATION=false
PERMISSION_CREATED=false
EVIDENCE_TRUTH_CHANGED=false
```

若 review 合格，下一步只允许：

```text
PREPARE_CE_G12_CURRENT_TARGET_DISPOSITION_DECISION_ONLY
```

Decision preparation 不得在同一动作中执行 supersession、candidate build、archive generation、
server read、repair、rollback、deployment、release 或 PR mutation。
