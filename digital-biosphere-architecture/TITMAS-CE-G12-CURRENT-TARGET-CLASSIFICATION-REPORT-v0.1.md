---
document_id: DBA-TITMAS-CE-G12-CURRENT-TARGET-CLASSIFICATION-REPORT-0.1
title: TITMAS CE-G12 Current-target Classification Report v0.1
title_zh: TITMAS CE-G12 当前目标分类报告 v0.1
version: 0.1.0
status: pass-read-only-classification-other-canonical-release-no-change-authorized
maturity: Development
maturity_scope: one-read-current-target-classification-only
owner_ref: zhangbin
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G12 Current-target Classification Report v0.1

## 1. Result

已按
[Current-target Classification Decision](TITMAS-COMMERCIAL-EVALUATION-CE-G12-CURRENT-TARGET-CLASSIFICATION-DECISION-RECORD.v0.1.json)
及其
[Qwen Decision Review](TITMAS-COMMERCIAL-EVALUATION-CE-G12-CURRENT-TARGET-CLASSIFICATION-QWEN-DECISION-REVIEW-v0.1.json)
执行一次独立、只读 current-target classification。

```text
RESULT=PASS_READ_ONLY_CURRENT_TARGET_CLASSIFICATION_NO_CHANGE_AUTHORIZED
CLASSIFICATION=OTHER_CANONICAL_RELEASE
CURRENT_SYMLINK=/srv/tmai/current
CANONICAL_RELEASE_ID=ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
CANONICAL_PATH=/srv/tmai/releases/ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
SYMLINK_SHAPE_PASS=true
TARGET_DIRECTORY_SHAPE_PASS=true
```

Machine result：

- [ce-g12-current-target-classification-result.v0.1.json](commercial-evaluation-exact-redeployment/ce-g12-current-target-classification-result.v0.1.json)

## 2. Classification meaning

`/srv/tmai/current` 当前：

1. 是 symlink；
2. `readlink` 成功；
3. 指向 `/srv/tmai/releases/[0-9a-f]{40}` 规范路径；
4. 目标是 non-symlink directory；
5. 不等于 Decision 中的 expected stable `7da4bcf…`；
6. 不等于 proposed `f810796…`。

因此严格分类为：

```text
OTHER_CANONICAL_RELEASE
```

该分类只回答 current target 的结构和标识。它不证明：

- `ccf473f3…` 是错误、过期或不安全 release；
- 谁或什么动作改变了 symlink；
- CE-G12-P mismatch 的完整 root cause；
- proposed release 可以部署；
- repair、rollback 或 redeployment 已获授权。

## 3. Execution accounting

```text
SSH_SESSIONS=1/1
LSTAT_CALLS=1/1
READLINK_CALLS=1/1
TARGET_DIRECTORY_SHAPE_CHECKS=1/1
SERVER_FILE_CONTENT_READS=0
DIRECTORY_LISTINGS=0
RAW_LOG_READS=0
JOURNAL_READS=0
SOURCE_IP_READS=0
SERVER_ENVIRONMENT_READS=0
PUBLIC_REQUESTS=0
SERVER_WRITES=0
NGINX_TESTS=0
NGINX_RELOADS=0
SYMLINK_SWITCHES=0
REPAIRS=0
ROLLBACKS=0
REDEPLOYMENTS=0
RETRIES=0
FALLBACKS=0
```

执行输出只包含 Decision 白名单字段。没有读取或持久化 private key path、credential
value、server environment、file content、directory listing、Nginx config、raw log、
journal 或 source IP。

## 4. Gate effect

本结果把：

```text
ACTUAL_CURRENT_TARGET=UNKNOWN_NOT_PERSISTED
```

收敛为：

```text
ACTUAL_CURRENT_TARGET_CLASSIFICATION=OTHER_CANONICAL_RELEASE
ACTUAL_CURRENT_CANONICAL_RELEASE_ID=ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
```

它不关闭 redeployment admission gate。expected stable、observed canonical target、PR #23
base lineage、历史 release records 与当前 site release pointer 仍需只读对账。

## 5. Next gate

```text
NEXT_ACTION=PREPARE_CE_G12_CURRENT_TARGET_LINEAGE_RECONCILIATION_RECOMMENDATION_ONLY
NEXT_ACTION_AUTHORIZED=false
SECOND_CLASSIFICATION_SSH_AUTHORIZED=false
SERVER_READ_AUTHORIZED=false
SERVER_WRITE_AUTHORIZED=false
REPAIR_AUTHORIZED=false
ROLLBACK_AUTHORIZED=false
REDEPLOYMENT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
STANDARD_READY=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
```

下一步只允许在 DBA 内准备 lineage reconciliation Recommendation。不得在同一动作中再次
连接服务器、修改 symlink、修复、rollback、redeploy 或发布。

## 6. Non-claims

```text
CLASSIFICATION_NE_ROOT_CAUSE=true
CLASSIFICATION_NE_DEPLOYMENT_SUCCESS=true
CLASSIFICATION_NE_REDEPLOYMENT_AUTHORITY=true
OBSERVATION_NE_TRUTH=true
EVIDENCE_NE_TRUTH=true
AUTHORITY_CREATED=false
PERMISSION_CREATED=false
SERVER_STATE_CHANGED=false
```
