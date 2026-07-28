---
document_id: DBA-TITMAS-CE-G12-PORTABLE-CANDIDATE-ATOMIC-DEPLOYMENT-REPORT-0.1
title: TITMAS CE-G12 Portable Candidate Atomic Deployment Report v0.1
title_zh: TITMAS CE-G12 可移植候选原子部署报告 v0.1
version: 0.1.0
status: fail-closed-route-body-mismatch-rollback-pass
maturity: Development
maturity_scope: one-bounded-static-site-deployment-attempt-only
owner_ref: zhangbin
decision_reference: TITMAS-COMMERCIAL-EVALUATION-CE-G12-PORTABLE-CANDIDATE-ATOMIC-DEPLOYMENT
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G12 Portable Candidate Atomic Deployment Report v0.1

## 1. Outcome

```text
RESULT=FAIL_CLOSED_ARTIFACT_ADDRESSED_ATOMIC_STATIC_SITE_DEPLOYMENT_NO_NEW_RELEASE_AUTHORIZED
FAILURE_STAGE=LOCALHOST_ROUTE_VALIDATION
FAILURE_ROUTE=/en
ROLLBACK_EXECUTED=true
ROLLBACK_PASS=true
POST_SESSION_CURRENT=/srv/tmai/releases/ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
CANDIDATE_ACTIVE=false
RETRIES=0
```

机器结果：

- [Atomic Deployment Result](commercial-evaluation-fresh-candidate/ce-g12-portable-candidate-atomic-deployment-result.v0.1.json)。

本轮没有重试。candidate 曾被原子切到 current，route gate 失败后在同一个 SSH session 内
恢复到 pre-switch current。

## 2. Gates that passed

本地：

```text
GOVERNANCE_LOCAL_REMOTE_EQUAL=true
CANDIDATE_EXACT=true
EXTRACTOR_DRY_RUNS_EXECUTED=1
EXTRACTOR_DRY_RUN_PASS=true
SSH_MAPPING_EXACT=true
IDENTITY_PATH_RECORDED=false
```

服务器：

```text
ARCHIVE_TRANSFER_BYTES=979463
ARCHIVE_TRANSFER_SHA256=f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7
RAW_MEMBERS=87
DIRECTORIES=21
FILES=66
APPLEDOUBLE=0
DUPLICATES=0
SPECIAL_MEMBERS=0
MANIFEST_FILES=65
MANIFEST_COVERAGE_PASS=true
FILE_HASHES_PASS=65/65
SOURCE_BINDING_PASS=true
OWNER_POLICY=root:root
DIRECTORY_MODE=0755
FILE_MODE=0644
NGINX_TEST_PASS=true
NGINX_RELOADS=0
```

这证明 portable archive、safe extractor 和 owner normalization 工作正常，但不把 route
validation failure 改写为 deployment success。

## 3. Preserved server artifacts

失败关闭后保留：

```text
ARTIFACT=/srv/tmai/artifacts/c1d8931930fbae15f96ee6a6ac050b081538c919--f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7.tar.gz
FINAL_PATH=/srv/tmai/releases/c1d8931930fbae15f96ee6a6ac050b081538c919--f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7
ARTIFACT_HASH_EXACT=true
EXTRACTED_TREE_VERIFIED=true
FUTURE_REUSE_AUTHORIZED=false
```

没有静默删除失败路径。它们是 deployment-attempt artifact，不是 active release、Evidence
Truth 或新的发布授权。

## 4. Route failure

`/`：

```text
CURL_EXIT=0
BODY_BYTES=46401
BODY_SHA256=cca332da1364a614bbef83939d0ff7c948739e673d14c7c1b2a60cd9d500abf8
EXPECTED_SHA256=cca332da1364a614bbef83939d0ff7c948739e673d14c7c1b2a60cd9d500abf8
PASS=true
```

`/en`：

```text
CURL_EXIT=0
BODY_BYTES=178
BODY_SHA256=7cb59ce037656d9a4e8ee9194bc31dfc540cbc8fd5b19c64439a89631cde3715
EXPECTED_FILE=en/index.html
EXPECTED_SHA256=562c061979c8cd72b1a94a74715727a898251a7716d61f64f4760468c0fb65f1
PASS=false
```

执行器没有记录 HTTP status 或 `Location`，也没有跟随 redirect。因此：

```text
REDIRECT_PROVEN=false
TRAILING_SLASH_ROOT_CAUSE_PROVEN=false
NGINX_CONTENT_FAILURE_PROVEN=false
FAILURE_CLASSIFICATION=RESPONSE_BODY_HASH_MISMATCH_HTTP_STATUS_AND_REDIRECT_NOT_CAPTURED
```

178-byte response 很像 nginx redirect body，但这只能作为下一步待验证假设，不能升级为
root cause。

## 5. Rollback

```text
PRE_SWITCH_CURRENT=/srv/tmai/releases/ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
FORWARD_SWITCHES=1
ROLLBACK_SWITCHES=1
ROLLBACK_TARGET_VERIFIED=true
POST_SESSION_CURRENT=/srv/tmai/releases/ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
```

stable fallback `7da4bcf…` 没有被使用。当前网站最终 target 与 session 前一致。

## 6. State and boundaries

```text
DEPLOYMENT_ATTEMPTED=true
DEPLOYMENT_PASS=false
SERVER_ARTIFACTS_PERSIST=true
SERVER_STATE_CHANGED=true
PUBLIC_SITE_TRANSIENTLY_CHANGED=true
PUBLIC_SITE_FINAL_TARGET_CHANGED=false
CANDIDATE_ACTIVE=false
NEW_PRODUCT_RELEASE_AUTHORIZED=false
NEW_PRODUCT_RELEASE_EXECUTED=false
STANDARD_READY=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
AUTHORITY_CREATED=false
PERMISSION_CREATED=false
EVIDENCE_TRUTH_CHANGED=false
```

## 7. Next gate

```text
NEXT_ACTION=PREPARE_CE_G12_LOCALHOST_ROUTE_RESPONSE_CLASSIFICATION_RECOMMENDATION_ONLY
NEXT_ACTION_AUTHORIZED=false
DEPLOYMENT_RETRY_AUTHORIZED=false
SECOND_SSH_SESSION_AUTHORIZED=false
SERVER_READ_AUTHORIZED=false
SERVER_WRITE_AUTHORIZED=false
ARTIFACT_REUSE_AUTHORIZED=false
SYMLINK_SWITCH_AUTHORIZED=false
PUBLIC_REQUEST_AUTHORIZED=false
NEW_PRODUCT_RELEASE_AUTHORIZED=false
```

下一步只应分类 `/en`、`/status`、`/en/status` 的 exact HTTP status、redirect chain、canonical
path 和 final body contract。分类完成前不得再次切换 current。
