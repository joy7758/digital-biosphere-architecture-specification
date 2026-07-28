---
document_id: DBA-TITMAS-CE-G12-PRESERVED-ARTIFACT-ATOMIC-ACTIVATION-RECOMMENDATION-0.1
title: TITMAS CE-G12 Preserved Artifact Atomic Activation Recommendation v0.1
title_zh: TITMAS CE-G12 已保留制品原子激活建议 v0.1
version: 0.1.0
status: preserved-artifact-atomic-activation-recommended-agent-review-required
maturity: Development
maturity_scope: bounded-static-site-preserved-artifact-activation-only
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G12 Preserved Artifact Atomic Activation Recommendation v0.1

## 1. Recommendation

采用 **Option A：只读重验 preserved canonical artifact 与 final tree 后，执行一次
CAS-guarded atomic activation，并使用已证明的 canonical-directory redirect contract 做
in-session validation 和 rollback**。

```text
RECOMMENDED_OPTION=A
PRESERVED_ARTIFACT_REUSE_RECOMMENDED=true
PRESERVED_ARTIFACT_REUSE_AUTHORIZED=false
ARCHIVE_TRANSFER_RECOMMENDED=false
ARCHIVE_EXTRACTION_RECOMMENDED=false
CURRENT_SWITCH_RECOMMENDED=true
CURRENT_SWITCH_AUTHORIZED=false
NEW_PRODUCT_RELEASE_AUTHORIZED=false
```

本 Recommendation 不建立 SSH session、不写 server、不复用 artifact、不切换 current、
不请求 localhost/public site、不部署、不发布。

## 2. Fixed evidence

failed deployment：

| Artifact | SHA-256 |
|---|---|
| `commercial-evaluation-fresh-candidate/ce-g12-portable-candidate-atomic-deployment-result.v0.1.json` | `7997b708cd520574f480221c8b0787920d654cecf888fe12db1ca797d1e32974` |
| `TITMAS-CE-G12-PORTABLE-CANDIDATE-ATOMIC-DEPLOYMENT-REPORT-v0.1.md` | `b51cb0a2b9c686ab4c10f17dde17b998e259c7d630df1bda79049f8957b18034` |

route classification：

| Artifact | SHA-256 |
|---|---|
| `commercial-evaluation-fresh-candidate/ce-g12-localhost-route-response-classification-result.v0.1.json` | `13dd40ebe01124f5d1ee1ae4b79158d4177a033a440add0a69d78b8c869757ba` |
| `TITMAS-CE-G12-LOCALHOST-ROUTE-RESPONSE-CLASSIFICATION-REPORT-v0.1.md` | `6bb14d0ddcd37eca61ca38da6c2ad5f8dd31f95ec05e8c6d4cc6e338fa41d267` |

evidence commit：

```text
cfb20dc8d89465af5ae4ff60612c639c06bab14a
```

## 3. Preserved server paths

失败 execution 已完整通过 transfer、safe extraction、manifest、owner 和 nginx test，并保留：

```text
SOURCE_COMMIT=c1d8931930fbae15f96ee6a6ac050b081538c919
ARCHIVE_SHA256=f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7
MANIFEST_SHA256=f0e42b7f0be3c36f201517d68bef42ec365809261ed46d4fc6af74949a397a60
RELEASE_ID=c1d8931930fbae15f96ee6a6ac050b081538c919--f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7
ARTIFACT_PATH=/srv/tmai/artifacts/c1d8931930fbae15f96ee6a6ac050b081538c919--f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7.tar.gz
FINAL_PATH=/srv/tmai/releases/c1d8931930fbae15f96ee6a6ac050b081538c919--f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7
EXPECTED_CURRENT=/srv/tmai/releases/ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
```

当前 evidence 证明这些路径在 failed session 结束时存在且 exact，但 future activation 必须
fresh reverify；不能把历史 pass 当作当前 truth。

## 4. Required fresh re-verification

未来独立 Decision 必须在任何 switch 前只读证明：

1. current 仍精确等于 expected current；
2. artifact path 是 regular file，bytes=979463、SHA exact；
3. final path 是 root-owned directory；
4. `release.json` 与 manifest source revision exact；
5. manifest SHA exact；
6. manifest files=65、actual files=66、coverage exact；
7. 65/65 bytes/hash pass；
8. dirs `root:root:0755`、files `root:root:0644`；
9. 没有 unexpected symlink/special/extra file；
10. nginx config SHA 仍等于 classification baseline；
11. `nginx -t` pass；
12. rollback target readable。

任一 drift 都停止；不得自动重传、重解包、修复或清理。

## 5. Correct activation validation contract

root：

```text
/ initial=200
/ body_hash=final/index.html
```

directory route pairs：

```text
/en -> 301 Location https://redcrag.cn/en/
/en/ -> 200 body_hash=final/en/index.html
follow(/en) -> 200 same body hash

/status -> 301 Location https://redcrag.cn/status/
/status/ -> 200 body_hash=final/status/index.html
follow(/status) -> 200 same body hash

/en/status -> 301 Location https://redcrag.cn/en/status/
/en/status/ -> 200 body_hash=final/en/status/index.html
follow(/en/status) -> 200 same body hash
```

不得再把 no-follow 301 body 与 HTML hash 直接比较。

## 6. Exact future sequence

1. 核对 governance chain、candidate 和 evidence hashes；
2. 解析 exact alias mapping；
3. 开启一个 fresh strict-host-key SSH session；
4. 执行 fresh artifact/final/current/nginx/rollback verification；
5. 重新执行一次 `nginx -t`，不 reload；
6. 再次 CAS 核对 current；
7. atomic switch current 到 preserved final；
8. 在同一 session 执行 root + three route-pair canonical contract；
9. 任一 post-switch failure，atomic rollback 到 captured pre-switch current；
10. 输出 machine receipt 并关闭 session；
11. 只提交 Result/Report。

成功不创建新 artifact、release directory 或 product release。它只激活已保留、重新验证过的
static tree。

## 7. Options

### Option A — Reverify and atomically activate preserved exact tree（推荐）

避免重复 transfer/extraction，缩小 mutation surface。

### Option B — Transfer and extract again（拒绝）

exact artifact/final 已保留；重复写入会制造 collision、重复证据和新失败面。

### Option C — Switch without fresh verification（拒绝）

历史结果不是当前 truth，不能跳过 drift check。

### Option D — Change nginx redirect behavior（拒绝）

canonical directory redirect 已被证明为有效契约，无需配置变更。

### Option E — Delete preserved paths before activation（拒绝）

删除会破坏失败证据，而且没有必要。

## 8. Caps

```text
QWEN_DECISION_REVIEW_REQUESTS_MAX=1
LOCAL_SSH_CONFIG_RESOLUTIONS_MAX=1
SSH_SESSIONS_MAX=1
SERVER_READ_COMMANDS_MAX=12
ARCHIVE_TRANSFERS=0
ARCHIVE_EXTRACTIONS=0
ARTIFACT_OR_RELEASE_CREATIONS=0
NGINX_TESTS_MAX=1
NGINX_RELOADS=0
FORWARD_SWITCHES_MAX=1
ROLLBACK_SWITCHES_MAX=1
LOCALHOST_ROUTE_REQUESTS_MAX=10
PUBLIC_EXTERNAL_REQUESTS=0
CLEANUPS=0
REPAIRS=0
RETRIES=0
NETWORK_FALLBACKS=0
NEW_PRODUCT_RELEASES=0
```

10 requests 覆盖 root 一次，以及三个 route pair 各自的 non-follow、follow、canonical direct。

## 9. Stop conditions

停止于治理/evidence hash drift、alias/auth/host-key failure、current drift、artifact/final/config
hash drift、manifest/file/owner/mode failure、rollback unreadable、nginx test failure、canonical
route contract failure、rollback failure、需要 transfer/extraction/cleanup/repair/second session/
retry/fallback、配置/证书/DNS/DBOS/SAEE 变更或任何 release/status elevation。

## 10. Recommendation review contract

exact `qwen3.7-max` 只允许一次 direct JSON review，必须返回：

```text
verdict
confidence
selected_option
would_recommend_to_agent_customer
fixed_evidence_sufficient
preserved_artifact_reuse_boundary_sound
fresh_reverification_scope_sufficient
no_retransfer_or_reextraction_sound
compare_and_swap_guard_sound
canonical_route_contract_sound
atomic_activation_and_rollback_sound
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

## 11. Non-authorizations

```text
RECOMMENDATION_NE_DECISION=true
PRESERVED_PATH_NE_ACTIVE_RELEASE=true
ACTIVATION_NE_NEW_PRODUCT_RELEASE=true
HISTORICAL_PASS_NE_CURRENT_TRUTH=true
SSH_SESSION_CREATED=false
SERVER_READ_EXECUTED=false
SERVER_WRITE_EXECUTED=false
CURRENT_SWITCH_EXECUTED=false
ARTIFACT_REUSE_AUTHORIZED=false
ACTIVATION_AUTHORIZED=false
NEW_PRODUCT_RELEASE_AUTHORIZED=false
STANDARD_READY=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
AUTHORITY_CREATED=false
PERMISSION_CREATED=false
EVIDENCE_TRUTH_CHANGED=false
```
