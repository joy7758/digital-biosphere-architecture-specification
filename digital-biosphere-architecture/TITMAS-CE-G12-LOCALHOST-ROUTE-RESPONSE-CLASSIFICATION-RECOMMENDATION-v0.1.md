---
document_id: DBA-TITMAS-CE-G12-LOCALHOST-ROUTE-RESPONSE-CLASSIFICATION-RECOMMENDATION-0.1
title: TITMAS CE-G12 Localhost Route Response Classification Recommendation v0.1
title_zh: TITMAS CE-G12 本机路由响应分类建议 v0.1
version: 0.1.0
status: read-only-route-response-classification-recommended-agent-review-required
maturity: Development
maturity_scope: failed-deployment-route-contract-diagnostic-only
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G12 Localhost Route Response Classification Recommendation v0.1

## 1. Recommendation

采用 **Option A：执行一次只读 localhost route response classification，分别记录
non-canonical path 与 trailing-slash canonical path 的 HTTP status、Location、final status、
body bytes/hash，并与当前 release 的对应静态文件比较**。

```text
RECOMMENDED_OPTION=A
FAILED_DEPLOYMENT_PRESERVED=true
CURRENT_TARGET_RESTORED=true
READ_ONLY_ROUTE_CLASSIFICATION_RECOMMENDED=true
READ_ONLY_ROUTE_CLASSIFICATION_AUTHORIZED=false
CURRENT_SWITCH_AUTHORIZED=false
ARTIFACT_REUSE_AUTHORIZED=false
DEPLOYMENT_RETRY_AUTHORIZED=false
```

本建议不建立 SSH session、不访问公共外网、不写 server、不复用 artifact/final path、不切换
current、不部署、不发布。

## 2. Preserved failure evidence

| Artifact | SHA-256 |
|---|---|
| `commercial-evaluation-fresh-candidate/ce-g12-portable-candidate-atomic-deployment-result.v0.1.json` | `7997b708cd520574f480221c8b0787920d654cecf888fe12db1ca797d1e32974` |
| `TITMAS-CE-G12-PORTABLE-CANDIDATE-ATOMIC-DEPLOYMENT-REPORT-v0.1.md` | `b51cb0a2b9c686ab4c10f17dde17b998e259c7d630df1bda79049f8957b18034` |

evidence commit：

```text
df1c8f9370cf491936b30d6405692b3efccafe23
```

已确认：

```text
PRE_SWITCH_CURRENT=/srv/tmai/releases/ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
POST_SESSION_CURRENT=/srv/tmai/releases/ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
ROLLBACK_PASS=true
CANDIDATE_ACTIVE=false
RETRIES=0
```

## 3. Exact unresolved observation

```text
ROUTE=/
CURL_EXIT=0
BODY_HASH_MATCH=true

ROUTE=/en
CURL_EXIT=0
BODY_BYTES=178
BODY_HASH_MATCH=false
HTTP_STATUS=NOT_CAPTURED
LOCATION=NOT_CAPTURED
REDIRECT_PROVEN=false
ROOT_CAUSE_PROVEN=false
```

`curl --fail` 对 3xx 不一定失败，178-byte body 也不能单独证明 redirect。因此不能把
failure 自动归类为 trailing-slash behavior。

## 4. Exact future diagnostic scope

未来独立 Decision 最多授权一个 read-only SSH session：

1. 核对治理链远端固定；
2. 核对 current 仍是 restored target `ccf473f3…`；
3. 读取 current `release.json`、manifest 和 relevant HTML hashes；
4. 读取 matching nginx config file 的 hash，并只提取与 `server_name`、`root`、`index`、
   `try_files`、redirect 有关的非敏感 directive；
5. 通过 localhost + configured Host/SNI 对以下 request 执行不跟随与跟随分类：

```text
/
/en
/en/
/status
/status/
/en/status
/en/status/
```

6. 每个 request 记录：
   - initial status；
   - initial `Location`；
   - redirect count；
   - final URL/path；
   - final status；
   - final body bytes/SHA；
   - 与当前 release 对应 file hash 是否相等；
7. 生成 Classification Result/Report；
8. 关闭 session，零 server write；
9. 只提交两个 classification artifact。

不得输出 nginx certificate/private-key path 或内容，不得执行 `nginx -t`、reload、public
external request、current switch、artifact cleanup 或 deployment retry。

## 5. Classification rules

### `CANONICAL_DIRECTORY_REDIRECT`

仅当同时观察到：

```text
NON_CANONICAL_STATUS in [301,302,307,308]
LOCATION_EQUALS_TRAILING_SLASH_PATH=true
FOLLOWED_FINAL_STATUS=200
FOLLOWED_FINAL_BODY_HASH_EQUALS_EXPECTED_FILE=true
CANONICAL_DIRECT_STATUS=200
CANONICAL_BODY_HASH_EQUALS_EXPECTED_FILE=true
```

### `CONTENT_SERVING_FAILURE`

canonical path final status 不是 200，或 canonical body hash 不等于 current release 对应 file。

### `CONFIG_OR_HOST_ROUTING_MISMATCH`

Host/SNI、root、try_files 或 redirect target 与 expected static tree 不一致。

### `UNKNOWN`

status、Location、final body 或 config evidence 任一不足。

分类是 diagnostic result，不授权 artifact reuse、deployment、release 或 configuration change。

## 6. Options

### Option A — One read-only localhost classification（推荐）

用最小 evidence 消除 178-byte response 的歧义。

### Option B — Assume trailing-slash redirect and redeploy（拒绝）

现有 execution 没有记录 status/Location，假设不能替代 observation。

### Option C — Change nginx configuration（拒绝）

没有证明 config 错误，且本轮禁止配置变更。

### Option D — Delete preserved artifact/final path and rebuild（拒绝）

archive、safe extraction、manifest 和 owner policy 已通过；删除会破坏失败证据且不解决
route contract 歧义。

## 7. Caps and stop conditions

```text
QWEN_DECISION_REVIEW_REQUESTS_MAX=1
LOCAL_SSH_CONFIG_RESOLUTIONS_MAX=1
SSH_SESSIONS_MAX=1
SERVER_READ_COMMANDS_MAX=10
LOCALHOST_ROUTE_REQUESTS_MAX=14
SERVER_WRITES=0
PUBLIC_EXTERNAL_REQUESTS=0
NGINX_TESTS=0
NGINX_RELOADS=0
SYMLINK_SWITCHES=0
ARCHIVE_TRANSFERS=0
ARCHIVE_EXTRACTIONS=0
CLEANUPS=0
DEPLOYMENTS=0
RELEASES=0
RETRIES=0
NETWORK_FALLBACKS=0
```

14 requests 是 7 个 path 的 no-follow 与 follow 两种观察上限；实现可在单次 request 中同时
获得 initial/final chain 时减少，但不得超过。

停止于 governance hash drift、alias/auth/host-key failure、current drift、需要 write、
第二 session、retry、external request、credential disclosure、config change、artifact reuse、
deployment/release 或状态提升。

## 8. Recommendation review contract

exact `qwen3.7-max` 只允许一次 direct JSON review，必须返回：

```text
verdict
confidence
selected_option
would_recommend_to_agent_customer
failure_evidence_sufficient
diagnostic_question_well_formed
route_pair_matrix_sufficient
status_location_body_contract_sufficient
classification_rules_sound
nginx_config_read_boundary_sound
read_only_scope_sufficient
caps_and_stop_rules_sufficient
no_redeployment_or_config_change_inference
authority_boundaries_preserved
blockers
corrections
rationale
```

qualifying：`RECOMMENDED`、Option A、confidence ≥ 0.80、全部 boolean true、空 blockers 和
corrections、returned model exact `qwen3.7-max`。

## 9. Non-authorizations

```text
RECOMMENDATION_NE_DECISION=true
DIAGNOSTIC_NE_REDEPLOYMENT=true
ROUTE_CLASSIFICATION_NE_CONFIG_AUTHORITY=true
PRESERVED_ARTIFACT_NE_ACTIVE_RELEASE=true
SSH_SESSION_CREATED=false
SERVER_READ_EXECUTED=false
SERVER_WRITE_EXECUTED=false
PUBLIC_EXTERNAL_REQUEST_EXECUTED=false
CURRENT_CHANGED=false
ARTIFACT_REUSE_AUTHORIZED=false
DEPLOYMENT_RETRY_AUTHORIZED=false
NEW_PRODUCT_RELEASE_AUTHORIZED=false
STANDARD_READY=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
AUTHORITY_CREATED=false
PERMISSION_CREATED=false
EVIDENCE_TRUTH_CHANGED=false
```
