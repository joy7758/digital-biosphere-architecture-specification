---
document_id: DBA-TITMAS-CE-G12-PORTABLE-CANDIDATE-DEPLOYMENT-ADMISSION-PREFLIGHT-REPORT-0.2
title: TITMAS CE-G12 Portable Candidate Deployment Admission Preflight Report v0.2
title_zh: TITMAS CE-G12 可移植候选部署准入预检报告 v0.2
version: 0.2.0
status: pass-alias-bound-read-only-preflight-no-deployment-authorized
maturity: Development
maturity_scope: read-only-deployment-admission-preflight-only
owner_ref: zhangbin
decision_reference: TITMAS-COMMERCIAL-EVALUATION-CE-G12-SSH-TARGET-MAPPING-REMEDIATION-PREFLIGHT-R2
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G12 Portable Candidate Deployment Admission Preflight Report v0.2

## 1. Outcome

```text
RESULT=PASS_ALIAS_BOUND_READ_ONLY_ARTIFACT_ADDRESSED_DEPLOYMENT_ADMISSION_PREFLIGHT_NO_DEPLOYMENT_AUTHORIZED
LOCAL_SSH_CONFIG_RESOLUTIONS=1
FRESH_SSH_SESSIONS=1
OLD_SESSION_RETRIES=0
SSH_EXIT=0
SERVER_READ_COMMANDS=9
SERVER_WRITES=0
PUBLIC_SITE_REQUESTS=0
DEPLOYMENT_ADMISSION_PASS=true
DEPLOYMENT_AUTHORIZED=false
```

机器结果：

- [Preflight Result v0.2](commercial-evaluation-fresh-candidate/ce-g12-portable-candidate-deployment-admission-preflight-result.v0.2.json)。

v0.1 的 public-key failure 仍保留，没有覆盖或重试。

## 2. Local and transport gates

SSH 之前全部通过：

```text
GOVERNANCE_LOCAL_REMOTE_EQUAL=true
GOVERNANCE_HEAD=401cd1c86da5e633ed8c7bce5d6dcb9d450bb477
CANDIDATE_HASH_EXACT=true
SSH_TARGET_ALIAS=hongyan-4cj
RESOLVED_HOSTNAME=180.76.115.193
RESOLVED_USER=root
IDENTITIES_ONLY=yes
IDENTITY_FILE_PRESENT=true
IDENTITY_FILE_PATH_RECORDED=false
```

唯一 fresh session 使用 alias、`BatchMode=yes` 和 `StrictHostKeyChecking=yes`。没有直接使用
`user@IP`，没有自动接受新 host key，也没有向工具输出、结果文件或 Git 暴露或记录
private key 内容。

## 3. Fixed candidate

```text
SOURCE_COMMIT=c1d8931930fbae15f96ee6a6ac050b081538c919
ARCHIVE=/tmp/titmas-site-c1d8931930fbae15f96ee6a6ac050b081538c919-source-bound-portable.tar.gz
ARCHIVE_BYTES=979463
ARCHIVE_SHA256=f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7
RELEASE_ID=c1d8931930fbae15f96ee6a6ac050b081538c919--f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7
CANDIDATE_CHANGED=false
```

## 4. Current and rollback observations

current：

```text
CURRENT_TARGET=/srv/tmai/releases/ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
CURRENT_TARGET_ABSOLUTE=true
CURRENT_TARGET_WITHIN_RELEASES_ROOT=true
CURRENT_SOURCE_REVISION=ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
CURRENT_RELEASE_JSON_SHA256=686099343e21602a191366feb186f294ab77178044de1a940b119d60e12699f7
CURRENT_MANIFEST_SHA256=a9bca24223de6d54d683d7c576be967a251633315a2e753288980961d801ada0
```

stable rollback：

```text
ROLLBACK_TARGET=/srv/tmai/releases/7da4bcf16eeec7de1c61031fe08fc04081cf8705
ROLLBACK_EXISTS=true
ROLLBACK_READABLE=true
ROLLBACK_SOURCE_REVISION=7da4bcf16eeec7de1c61031fe08fc04081cf8705
ROLLBACK_RELEASE_JSON_SHA256=117d098bded340fe984d630be8572f1ccc5a7b6b2dfc8fa84ab303d266ba78ad
ROLLBACK_MANIFEST_SHA256=b008349083c448d576fd5bca6da59911b3ef7cbe87527c110f29a470a28a2eae
```

历史 observation 与本次 fresh observation 一致，但本报告只陈述当前读到的事实，不推断
既有 deployment 的 intent 或 authority。

## 5. Future path and infrastructure

```text
FUTURE_RELEASE_PATH_EXISTS=false
FUTURE_RELEASE_PATH_COLLISION=false
RELEASES_ROOT_OWNER_GROUP_MODE=root:root:0755
CURRENT_PARENT_OWNER_GROUP_MODE=root:root:0755
FILESYSTEM_FREE_BYTES=89328644096
CANDIDATE_BYTES=979463
CAPACITY_SUFFICIENT=true
NGINX_CURRENT_ROOT_REFERENCE_PRESENT=true
NGINX_MATCHING_CONFIG=/etc/nginx/conf.d/redcrag.cn.conf
NGINX_TEST_EXECUTED=false
NGINX_RELOAD_EXECUTED=false
```

该结果支持“可以进入 deployment execution Recommendation 设计”，不等于可以部署。

## 6. Newly identified ownership risk

current 与 stable rollback 目录都观察到：

```text
OWNER_GROUP=501:staff
MODE=0755
READABLE=true
```

这表明历史 extraction 可能保留了 macOS archive owner metadata。未来 deployment plan 必须：

1. 解包时显式禁止保留 archive owner；
2. 限定解包目标为新的 artifact-addressed release directory；
3. 解包后重新核验 manifest coverage 和全部 file hashes；
4. 不依赖事后静默 `chown` 修复；
5. 把 owner/group/mode 写入 deployment receipt。

本次没有执行 extraction、`chmod` 或 `chown`。

## 7. Admission result

```text
CURRENT_TARGET_EXACTLY_IDENTIFIED=true
ROLLBACK_TARGET_EXACTLY_IDENTIFIED=true
ROLLBACK_TARGET_READABLE=true
CANDIDATE_ARCHIVE_LOCAL_HASH_EXACT=true
FUTURE_RELEASE_ID_SOURCE_AND_ARCHIVE_BOUND=true
FUTURE_RELEASE_PATH_COLLISION=false
FILESYSTEM_CAPACITY_SUFFICIENT=true
NGINX_CURRENT_ROOT_REFERENCE_PRESENT=true
NO_SERVER_MUTATION_OBSERVED=true
DEPLOYMENT_ADMISSION_PREFLIGHT_PASS=true
```

## 8. Boundaries

```text
PREFLIGHT_PASS_NE_DEPLOYMENT_AUTHORIZATION=true
SERVER_OBSERVATION_NE_AUTHORITY=true
EXISTING_OWNER_METADATA_NE_FUTURE_OWNER_POLICY=true
CANDIDATE_PASS_NE_DEPLOYMENT_EXECUTION=true
SERVER_STATE_CHANGED=false
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

## 9. Next gate

```text
NEXT_ACTION=PREPARE_CE_G12_PORTABLE_CANDIDATE_DEPLOYMENT_EXECUTION_RECOMMENDATION_ONLY
NEXT_ACTION_AUTHORIZED=false
DEPLOYMENT_EXECUTION_AUTHORIZED=false
ARCHIVE_TRANSFER_AUTHORIZED=false
SERVER_WRITE_AUTHORIZED=false
SYMLINK_SWITCH_AUTHORIZED=false
NGINX_TEST_OR_RELOAD_AUTHORIZED=false
PUBLIC_VALIDATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

下一份 Recommendation 必须单独设计：artifact-addressed directory creation、safe extraction、
owner normalization、post-extraction hash verification、atomic symlink switch、nginx validation、
rollback trigger 和完整 receipt。它仍需新的 Decision 与 exact `qwen3.7-max` review。
