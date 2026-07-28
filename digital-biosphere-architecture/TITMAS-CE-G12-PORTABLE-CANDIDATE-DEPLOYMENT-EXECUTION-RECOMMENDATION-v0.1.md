---
document_id: DBA-TITMAS-CE-G12-PORTABLE-CANDIDATE-DEPLOYMENT-EXECUTION-RECOMMENDATION-0.1
title: TITMAS CE-G12 Portable Candidate Deployment Execution Recommendation v0.1
title_zh: TITMAS CE-G12 可移植候选部署执行建议 v0.1
version: 0.1.0
status: artifact-addressed-atomic-deployment-recommended-agent-review-required
maturity: Development
maturity_scope: commercial-static-site-bounded-deployment-execution-only
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G12 Portable Candidate Deployment Execution Recommendation v0.1

## 1. Recommendation

采用 **Option A：执行一次 artifact-addressed、manifest-verified、owner-normalized、CAS-guarded
的原子静态站点部署，并在同一 SSH session 内提供失败回滚**。

```text
RECOMMENDED_OPTION=A
ARTIFACT_ADDRESSED_RELEASE=true
SAFE_EXTRACTION_REQUIRED=true
ARCHIVE_OWNER_METADATA_PRESERVED=false
MANIFEST_VERIFICATION_REQUIRED=true
CURRENT_COMPARE_AND_SWAP_REQUIRED=true
ATOMIC_SYMLINK_SWITCH_REQUIRED=true
IN_SESSION_ROLLBACK_REQUIRED=true
DEPLOYMENT_RECOMMENDED=true
DEPLOYMENT_AUTHORIZED=false
NEW_PRODUCT_RELEASE_AUTHORIZED=false
```

本 Recommendation 不建立 SSH session、不传输 archive、不创建目录、不切换 symlink、
不执行 nginx test/reload、不访问公共站点、不部署、不发布。

## 2. Fixed deployment-admission evidence

远端固定：

| Artifact | SHA-256 |
|---|---|
| `commercial-evaluation-fresh-candidate/ce-g12-portable-candidate-deployment-admission-preflight-result.v0.2.json` | `b2ec37cdb80a52bb438d2a2ebab8e745d7033007a284af3b295627da88f2832f` |
| `TITMAS-CE-G12-PORTABLE-CANDIDATE-DEPLOYMENT-ADMISSION-PREFLIGHT-REPORT-v0.2.md` | `b9ed8f77d3fefe44ccfed2dd772c259e10a81bee2ed215431ff8fd05254e04f3` |

evidence commit：

```text
c236ce49af41c070cfd5ec13d880b87c8848b912
```

preflight：

```text
CURRENT_TARGET=/srv/tmai/releases/ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
CURRENT_SOURCE_REVISION=ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
STABLE_ROLLBACK=/srv/tmai/releases/7da4bcf16eeec7de1c61031fe08fc04081cf8705
STABLE_ROLLBACK_READABLE=true
FUTURE_RELEASE_PATH_COLLISION=false
FILESYSTEM_FREE_BYTES=89328644096
NGINX_CURRENT_ROOT_REFERENCE_PRESENT=true
SERVER_WRITES=0
DEPLOYMENT_ADMISSION_PREFLIGHT_PASS=true
DEPLOYMENT_AUTHORIZED=false
```

## 3. Exact candidate and paths

```text
SOURCE_COMMIT=c1d8931930fbae15f96ee6a6ac050b081538c919
ARCHIVE_LOCAL=/tmp/titmas-site-c1d8931930fbae15f96ee6a6ac050b081538c919-source-bound-portable.tar.gz
ARCHIVE_BYTES=979463
ARCHIVE_SHA256=f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7
MANIFEST_SHA256=f0e42b7f0be3c36f201517d68bef42ec365809261ed46d4fc6af74949a397a60
RELEASE_ID=c1d8931930fbae15f96ee6a6ac050b081538c919--f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7
ARTIFACT_PATH=/srv/tmai/artifacts/c1d8931930fbae15f96ee6a6ac050b081538c919--f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7.tar.gz
STAGING_PATH=/srv/tmai/releases/.incoming-c1d8931930fbae15f96ee6a6ac050b081538c919--f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7
FINAL_PATH=/srv/tmai/releases/c1d8931930fbae15f96ee6a6ac050b081538c919--f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7
EXPECTED_PRE_SWITCH_CURRENT=/srv/tmai/releases/ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
ROLLBACK_TARGET=/srv/tmai/releases/ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
STABLE_FALLBACK=/srv/tmai/releases/7da4bcf16eeec7de1c61031fe08fc04081cf8705
```

release identity 继续同时绑定 source SHA 与 archive SHA；不得缩短为 source-only path。

## 4. Ownership risk and extraction policy

preflight 观察到 current 与 stable rollback release directory 都是：

```text
OWNER_GROUP=501:staff
```

该值可能来自 macOS archive metadata。新 deployment 不得复制这个历史行为。

解包器必须：

1. 只接受 directory 和 regular file；
2. 拒绝 absolute path、`..` traversal、symlink、hardlink、device、FIFO 和 socket；
3. 忽略 archive uid/gid；
4. 新目录固定 `root:root:0755`；
5. regular file 固定 `root:root:0644`；
6. 不使用事后静默 recursive `chown` 作为补救；
7. 保留 exact artifact archive，便于复核；
8. 失败 staging 不静默删除，由 receipt 记录并进入单独清理 gate。

优先使用 bounded Python extractor 明确创建 directory/file，而不是以 root 身份让 tar 自动
preserve archive ownership。

## 5. Exact future deployment sequence

未来独立 Decision 最多授权：

1. 核对 Recommendation/review/Decision/review 已远端固定；
2. 重新核对 local candidate bytes/hash 与 preflight evidence hash；
3. 本地解析一次 `ssh -G hongyan-4cj`，继续要求 hostname/user/identitiesonly/identityfile
   mapping 合格且不记录 identity path；
4. 开启一个 fresh、non-interactive、strict-host-key SSH session；
5. session 开始后先重新读取 current target、rollback、future path、artifact path 和 capacity；
6. 要求 current 仍精确等于 `ccf473f3…`，future/staging/artifact path 均不存在；
7. 通过该 session 的 stdin 写入一个 `.partial` artifact；
8. 写满后核对 bytes 和 SHA-256，成功才 atomic rename 为 canonical artifact path；
9. 安全解包到唯一 staging path，忽略 archive owner；
10. 核对 raw members=87、directories=21、files=66、AppleDouble=0、special=0；
11. 核对 `release.json` 和 `release-manifest.json` source revision；
12. 核对 manifest SHA、manifest coverage、每个 file bytes/hash、无 extra file；
13. 核对 staging owner/group/mode 为规范的 root-owned static tree；
14. 执行一次 `nginx -t`，不得 reload；
15. atomic rename staging 为 final path；
16. 再次 CAS 核对 current 未变化；
17. 创建一个临时 symlink 并以 atomic rename 将 `/srv/tmai/current` 切到 final；
18. 在同一 session 内对 `/`、`/en`、`/status`、`/en/status` 做 localhost + configured
    Host header 验证；
19. 任一 post-switch check 失败，立即 atomic rollback 到 captured pre-switch current，
    再验证 rollback target；
20. 输出 bounded machine receipt，关闭 session；
21. 本地生成 Result/Report，只提交这两个治理 artifact。

不得修改 nginx configuration、证书、安全配置或 DNS。由于 nginx static root 已指向
`/srv/tmai/current`，本轮不需要 reload。

## 6. Compare-and-swap and rollback

切换前必须再次满足：

```text
CURRENT_TARGET_EQUALS_PREFLIGHT_TARGET=true
FUTURE_PATH_ABSENT=true
STAGING_PATH_ABSENT=true
ARTIFACT_PATH_ABSENT=true
ROLLBACK_TARGET_READABLE=true
NGINX_TEST_PASS=true
EXTRACTED_MANIFEST_EXACT=true
EXTRACTED_TREE_OWNER_POLICY_PASS=true
```

任何 current drift 都必须在写 symlink 前停止，不得将新的观察自动当成新授权。

atomic switch 后若 route/status check 失败：

```text
ROLLBACK_TARGET=captured pre-switch current
ROLLBACKS_MAX=1
ROLLBACK_VERIFICATION_REQUIRED=true
```

stable fallback `7da4bcf…` 只作为第二层 evidence，不得在本 Decision 下直接切换，除非
captured current 本身不可恢复且另有新 Decision。

## 7. Result contract

future Result/Report 必须至少记录：

- governance/recommendation/decision hashes；
- local candidate and server artifact hash；
- exact pre-switch/post-switch/final current target；
- archive member/security checks；
- manifest and all-file verification counts；
- staging/final owner/group/mode；
- nginx test；
- four local route checks；
- writes、switches、rollback、requests、sessions、retries；
- failure stage 与残留 staging/artifact path；
- `deployment_executed`；
- `new_release_authorized=false`；
- `standard_ready=false`、`production_ready=false`。

成功：

```text
PASS_ARTIFACT_ADDRESSED_ATOMIC_STATIC_SITE_DEPLOYMENT_NO_NEW_RELEASE_AUTHORIZED
```

失败：

```text
FAIL_CLOSED_ARTIFACT_ADDRESSED_ATOMIC_STATIC_SITE_DEPLOYMENT_NO_NEW_RELEASE_AUTHORIZED
```

## 8. Options

### Option A — One-session verified atomic deployment（推荐）

最小化 connection 与 race window，同时保留 exact artifact、verification、CAS 和 rollback。

### Option B — Extract directly into `/srv/tmai/current`（拒绝）

破坏 immutable release 和 rollback；partial extraction 会直接污染 public path。

### Option C — Use source-only release directory（拒绝）

同一 source 已产生多个 archive，存在 artifact identity collision。

### Option D — Preserve archive UID/GID（拒绝）

已观察到 `501:staff` portability risk，继续保留会把本地身份元数据带入服务器。

### Option E — Switch first, verify later（拒绝）

会把未验证内容暴露给 nginx，扩大故障窗口。

## 9. Caps

```text
QWEN_DECISION_REVIEW_REQUESTS_MAX=1
LOCAL_SSH_CONFIG_RESOLUTIONS_MAX=1
SSH_SESSIONS_MAX=1
ARCHIVE_TRANSFERS_MAX=1
SERVER_ARTIFACT_FILES_CREATED_MAX=2
SERVER_RELEASE_DIRECTORIES_CREATED_MAX=2
ARCHIVE_EXTRACTIONS_MAX=1
NGINX_TESTS_MAX=1
NGINX_RELOADS=0
SYMLINK_SWITCHES_MAX=2
LOCALHOST_ROUTE_REQUESTS_MAX=4
PUBLIC_EXTERNAL_REQUESTS=0
ROLLBACKS_MAX=1
RETRIES=0
NETWORK_FALLBACKS=0
NEW_PRODUCT_RELEASES=0
PR_MUTATIONS=0
```

`SYMLINK_SWITCHES_MAX=2` 覆盖一次 forward switch，以及仅在 post-switch failure 时最多一次
rollback switch；成功路径只允许一次。`SERVER_ARTIFACT_FILES_CREATED_MAX=2` 覆盖
`.partial` 与 canonical rename identity，`SERVER_RELEASE_DIRECTORIES_CREATED_MAX=2` 覆盖
staging 与 final rename identity；rename 不表示复制出第二份内容。

## 10. Stop conditions

停止于：

- 治理链或 candidate/evidence hash drift；
- exact `qwen3.7-max` Decision review 不合格；
- alias mapping、auth 或 strict host-key failure；
- current drift；
- artifact/staging/final path collision；
- capacity 不足；
- archive hash/member/security check 失败；
- manifest/source/file coverage/hash 失败；
- extraction owner policy 失败；
- nginx test 失败；
-需要第二个 deployment session、retry 或 fallback；
- rollback 失败；
- 任何要求修改 nginx config、证书、安全配置、DNS、DBOS、SAEE、权限或 evidence truth；
- 任何把 deployment 升级为新 release、Standard Ready、Production 或 commercial offering
  的要求。

## 11. Recommendation review contract

exact `qwen3.7-max` 只允许一次 direct JSON review，必须返回：

```text
verdict
confidence
selected_option
would_recommend_to_agent_customer
preflight_evidence_sufficient
artifact_addressed_paths_sound
safe_extraction_policy_sound
owner_normalization_policy_sound
manifest_verification_scope_sufficient
compare_and_swap_guard_sound
atomic_switch_and_rollback_sound
one_session_transfer_model_sound
result_contract_sufficient
caps_and_stop_rules_sufficient
new_release_gate_separation_sound
authority_boundaries_preserved
blockers
corrections
rationale
```

qualifying：`RECOMMENDED`、Option A、confidence ≥ 0.80、全部 boolean true、空 blockers 和
corrections、returned model exact `qwen3.7-max`。

## 12. Non-authorizations

```text
RECOMMENDATION_NE_DECISION=true
PREFLIGHT_PASS_NE_DEPLOYMENT_AUTHORIZATION=true
DEPLOYMENT_NE_NEW_PRODUCT_RELEASE=true
SERVER_OBSERVATION_NE_AUTHORITY=true
ARTIFACT_PERSISTENCE_NE_EVIDENCE_TRUTH=true
SSH_SESSION_CREATED=false
SERVER_WRITE_EXECUTED=false
ARCHIVE_TRANSFER_EXECUTED=false
ARCHIVE_EXTRACTION_EXECUTED=false
SYMLINK_SWITCH_EXECUTED=false
PUBLIC_SITE_CHANGED=false
DEPLOYMENT_AUTHORIZED=false
NEW_RELEASE_AUTHORIZED=false
STANDARD_READY=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
AUTHORITY_CREATED=false
PERMISSION_CREATED=false
EVIDENCE_TRUTH_CHANGED=false
```
