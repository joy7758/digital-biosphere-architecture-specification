---
document_id: DBA-TITMAS-CE-G12-PORTABLE-CANDIDATE-DEPLOYMENT-ADMISSION-RECOMMENDATION-0.1
title: TITMAS CE-G12 Portable Candidate Deployment Admission Recommendation v0.1
title_zh: TITMAS CE-G12 可移植候选部署准入建议 v0.1
version: 0.1.0
status: read-only-artifact-addressed-deployment-preflight-recommended-agent-review-required
maturity: Development
maturity_scope: commercial-static-site-deployment-admission-preflight-only
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G12 Portable Candidate Deployment Admission Recommendation v0.1

## 1. Recommendation

采用 **Option A：先执行一次只读 deployment admission preflight，并将未来 release
identity 固定为 source commit + archive SHA，而不是只使用 source commit**。

```text
RECOMMENDED_OPTION=A
CANDIDATE_SOURCE=c1d8931930fbae15f96ee6a6ac050b081538c919
CANDIDATE_ARCHIVE_SHA256=f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7
RELEASE_IDENTITY_SOURCE_BOUND=true
RELEASE_IDENTITY_ARTIFACT_BOUND=true
READ_ONLY_PREFLIGHT_RECOMMENDED=true
READ_ONLY_PREFLIGHT_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

本建议不建立 SSH session，不读取或修改 server，不创建 release directory，不切换 symlink，
不 reload nginx，不部署、不发布。

## 2. Fixed candidate evidence

远端固定：

| Artifact | SHA-256 |
|---|---|
| `commercial-evaluation-fresh-candidate/ce-g12-portable-source-bound-candidate-baseline.v0.1.json` | `a83d8ef4db2ce41166e430cd024df81e4a8df946320996b9f0ba07c4ecdb6b78` |
| `commercial-evaluation-fresh-candidate/ce-g12-portable-source-bound-candidate-preparation-result.v0.1.json` | `d6d5aac53a7e6f5cd7e07d073536e94faf77d2a4bb64aaf4a9ac243afff31d75` |
| `TITMAS-CE-G12-PORTABLE-SOURCE-BOUND-CANDIDATE-PREPARATION-REPORT-v0.1.md` | `01d682b35508cefde8c21c98c28301d6577068ea607f5569d6383ac3992fb3b5` |

evidence commit：

```text
c1ae52b1062f334924b5be6acd5d5a4e132168fb
```

candidate：

```text
ARCHIVE=/tmp/titmas-site-c1d8931930fbae15f96ee6a6ac050b081538c919-source-bound-portable.tar.gz
ARCHIVE_BYTES=979463
ARCHIVE_SHA256=f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7
SOURCE_REVISION=c1d8931930fbae15f96ee6a6ac050b081538c919
RAW_MEMBERS=87
APPLEDOUBLE_MEMBERS=0
MANIFEST_COVERAGE_PASS=true
SOURCE_BINDING_PASS=true
SITE_TESTS=16/16
CE_TESTS=49/49
DEPLOYMENT_ADMISSION_PASS=false
```

## 3. Why source revision alone is not a release identity

本轮已从同一 source commit `c1d8931…` 产生三个不同 archive：

| archive role | SHA-256 | status |
|---|---|---|
| initial | `7240f58b…` | manifest source binding FAIL |
| source-bound | `789064b9…` | portable archive FAIL |
| portable source-bound | `f3f46e5e…` | candidate preparation PASS |

因此：

```text
SOURCE_REVISION_NE_ARTIFACT_IDENTITY=true
SAME_SOURCE_CAN_PRODUCE_MULTIPLE_ARCHIVES=true
RELEASE_PATH_BY_SOURCE_ONLY_COLLISION_RISK=true
```

未来 release directory 不应只使用：

```text
/srv/tmai/releases/c1d8931930fbae15f96ee6a6ac050b081538c919
```

建议使用完整 artifact-addressed identity，例如：

```text
release_id =
  c1d8931930fbae15f96ee6a6ac050b081538c919
  +
  f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7
```

具体 filesystem encoding 可在 preflight Result 中固定，但必须无歧义、路径安全、可逆解析，
并同时绑定 source SHA 与 archive SHA。

## 4. Prior server observation is not current truth

已有 lineage evidence：

- `commercial-evaluation-exact-redeployment/ce-g12-current-target-lineage-reconciliation-result.v0.1.json`
  SHA-256 `2afa3d7851d6a8ca6733afa8360e371358d70075f6d94c8e740284fa3ceb073b`；
- `TITMAS-CE-G12-CURRENT-TARGET-LINEAGE-RECONCILIATION-REPORT-v0.1.md`
  SHA-256 `9d19e10761654f03eb9dd08939839c9830b67795ba61066daf0cc2cf89d6ba0b`。

当时只读观察：

```text
OBSERVED_CURRENT_TARGET=ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
HISTORICAL_STABLE_ROLLBACK=7da4bcf16eeec7de1c61031fe08fc04081cf8705
```

该记录是历史 observation，不证明执行时 current target 仍相同，也不证明其 authorized、
unauthorized、safe、stale 或 root cause。

## 5. Exact future read-only preflight scope

未来独立 Decision 最多授权一个 SSH session 内的只读操作：

1. 核对 Recommendation/review/Decision/review 已远端固定；
2. 核对 local portable candidate archive bytes/SHA 和三件 evidence hash；
3. 读取 current symlink target，记录 exact absolute canonical path；
4. 读取 current release 的 `release.json`、`release-manifest.json`、member/file hash baseline；
5. 核对 historical stable rollback target 是否存在、是否仍可读取；
6. 选择并验证一个 source+archive artifact-addressed future release id；
7. 检查 proposed future release path 是否不存在或完全相同；
8. 检查磁盘空间、owner/group/mode、symlink parent 和 nginx/static-root prerequisites；
9. 生成 read-only Preflight Result 和 Report；
10. 关闭 SSH session，零 server write；
11. 只提交 preflight artifacts。

不得在 preflight 中：

- mkdir、copy、extract、chmod、chown、write；
- 创建或切换 symlink；
- 执行 nginx test/reload；
- 发起 public-site request；
- repair、rollback、deploy 或 release。

## 6. Deployment admission conditions after preflight

只有 future preflight 全部证明以下条件，才可再提出 deployment execution Recommendation：

```text
CURRENT_TARGET_EXACTLY_IDENTIFIED=true
ROLLBACK_TARGET_EXACTLY_IDENTIFIED=true
ROLLBACK_TARGET_READABLE=true
CANDIDATE_ARCHIVE_LOCAL_HASH_EXACT=true
FUTURE_RELEASE_ID_SOURCE_AND_ARCHIVE_BOUND=true
FUTURE_RELEASE_PATH_COLLISION=false
FILESYSTEM_PREREQUISITES_PASS=true
NO_SERVER_MUTATION_OBSERVED=true
```

即使全部 PASS，仍需另一个独立 Deployment Decision 和 exact `qwen3.7-max` Decision review。

## 7. Options

### Option A — Artifact-addressed read-only preflight（推荐）

先消除 current target、rollback 与 release identity 未知；不部署。

### Option B — Deploy directly to a source-only path（拒绝）

同一 source 已存在多个不同 archive，source-only path 有碰撞和误绑定风险。

### Option C — Treat candidate PASS as deployment admission（拒绝）

candidate preparation 没有观察 current server、rollback 或 filesystem prerequisites。

### Option D — Roll back before preflight（拒绝）

会改变 server state，且没有新 rollback Decision。

## 8. Caps and stop conditions

未来 preflight caps：

```text
QWEN_DECISION_REVIEW_REQUESTS_MAX=1
SSH_SESSIONS_MAX=1
SERVER_READ_COMMANDS_MAX=12
SERVER_WRITES=0
PUBLIC_SITE_REQUESTS=0
FILE_CREATIONS=0
SYMLINK_SWITCHES=0
NGINX_TESTS=0
NGINX_RELOADS=0
ROLLBACKS=0
DEPLOYMENTS=0
RELEASES=0
RETRIES=0
NETWORK_FALLBACKS=0
```

停止于任何 evidence/archive hash drift、SSH/auth failure、current/rollback target 不可解析、
candidate release path collision、需要 write/retry/fallback、或要求把 preflight 升级为
deployment、release、Standard Ready、Production 或 commercial offering。

## 9. Recommendation review contract

exact `qwen3.7-max` 只允许一次 direct JSON review，必须返回：

```text
verdict
confidence
selected_option
would_recommend_to_agent_customer
candidate_evidence_sufficient
source_revision_not_artifact_identity_sound
artifact_addressed_release_identity_sound
historical_observation_boundary_sound
read_only_preflight_scope_sufficient
deployment_gate_separation_sound
caps_and_stop_rules_sufficient
no_deployment_or_release_inference
authority_boundaries_preserved
blockers
corrections
rationale
```

qualifying：`RECOMMENDED`、Option A、confidence ≥ 0.80、全部 boolean true、空 blockers 和
corrections、returned model exact `qwen3.7-max`。

## 10. Non-authorizations

```text
RECOMMENDATION_NE_DECISION=true
CANDIDATE_PASS_NE_DEPLOYMENT_ADMISSION=true
SOURCE_REVISION_NE_ARTIFACT_IDENTITY=true
READ_ONLY_PREFLIGHT_NE_DEPLOYMENT=true
SERVER_OBSERVATION_NE_AUTHORITY=true
SSH_SESSION_CREATED=false
SERVER_READ_EXECUTED=false
SERVER_WRITE_EXECUTED=false
PUBLIC_SITE_CHANGED=false
DEPLOYMENT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
STANDARD_READY=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
AUTHORITY_CREATED=false
PERMISSION_CREATED=false
EVIDENCE_TRUTH_CHANGED=false
```
