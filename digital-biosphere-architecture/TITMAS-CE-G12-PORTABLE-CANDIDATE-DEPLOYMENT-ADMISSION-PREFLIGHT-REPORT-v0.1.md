---
document_id: DBA-TITMAS-CE-G12-PORTABLE-CANDIDATE-DEPLOYMENT-ADMISSION-PREFLIGHT-REPORT-0.1
title: TITMAS CE-G12 Portable Candidate Deployment Admission Preflight Report v0.1
title_zh: TITMAS CE-G12 可移植候选部署准入预检报告 v0.1
version: 0.1.0
status: fail-closed-ssh-target-mapping-mismatch-no-server-state-observed
maturity: Development
maturity_scope: read-only-deployment-admission-preflight-only
owner_ref: zhangbin
decision_reference: TITMAS-COMMERCIAL-EVALUATION-CE-G12-PORTABLE-CANDIDATE-DEPLOYMENT-ADMISSION-PREFLIGHT
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G12 Portable Candidate Deployment Admission Preflight Report v0.1

## 1. Outcome

```text
RESULT=FAIL_CLOSED_READ_ONLY_ARTIFACT_ADDRESSED_DEPLOYMENT_ADMISSION_PREFLIGHT_NO_DEPLOYMENT_AUTHORIZED
SSH_SESSIONS=1
SSH_EXIT=255
FAILURE=PERMISSION_DENIED_PUBLICKEY
SERVER_SCRIPT_STARTED=false
SERVER_READS_COMPLETED=0
SERVER_WRITES=0
RETRIES=0
DEPLOYMENT_ADMISSION_PASS=false
```

机器结果：

- [Preflight Result](commercial-evaluation-fresh-candidate/ce-g12-portable-candidate-deployment-admission-preflight-result.v0.1.json)。

## 2. Candidate remained exact

SSH 前本地 candidate：

```text
ARCHIVE=/tmp/titmas-site-c1d8931930fbae15f96ee6a6ac050b081538c919-source-bound-portable.tar.gz
ARCHIVE_BYTES=979463
ARCHIVE_SHA256=f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7
CANDIDATE_HASH_EXACT=true
```

本次没有 transfer、extract、write、deployment 或 candidate change。

## 3. Transport failure

Decision 的 transport target 是：

```text
zhangbin@180.76.115.193
```

唯一 session 在远端脚本启动前返回：

```text
Permission denied (publickey)
```

因此所有 server observation 必须保持 `NOT_OBSERVED`。该失败不能证明服务器不可用、
current target 不存在或 rollback 不可用。

## 4. Local-only mapping diagnosis

失败后只读取本地 SSH config，没有新的 network request 或 SSH session。发现：

```text
Host hongyan-4cj
HostName 180.76.115.193
User root
IdentitiesOnly yes
StrictHostKeyChecking accept-new
```

IdentityFile 的具体路径没有写入结果。诊断：

```text
ROOT_CAUSE=DECISION_TARGET_BYPASSED_CONFIGURED_ALIAS_USER_AND_IDENTITY_MAPPING
```

这证明应先建立新的 exact target-mapping Recommendation/Decision，再使用 alias；不允许把
本地诊断当作对失败 session 的自动 retry。

## 5. Unknowns preserved

```text
CURRENT_TARGET=NOT_OBSERVED
CURRENT_RELEASE_SOURCE_REVISION=NOT_OBSERVED
CURRENT_RELEASE_MANIFEST_HASH=NOT_OBSERVED
STABLE_ROLLBACK_PRESENCE=NOT_OBSERVED
STABLE_ROLLBACK_READABLE=NOT_OBSERVED
FUTURE_RELEASE_PATH_COLLISION=NOT_OBSERVED
FILESYSTEM_CAPACITY=NOT_OBSERVED
NGINX_STATIC_ROOT=NOT_OBSERVED
```

## 6. Boundaries

```text
SSH_AUTH_FAILURE_NE_SERVER_FAILURE=true
LOCAL_CONFIG_MAPPING_NE_SERVER_OBSERVATION=true
DIAGNOSIS_NE_RETRY_AUTHORITY=true
PREFLIGHT_NE_DEPLOYMENT=true
CANDIDATE_PASS_NE_DEPLOYMENT_ADMISSION=true
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

## 7. Next gate

```text
NEXT_ACTION=PREPARE_CE_G12_SSH_TARGET_MAPPING_REMEDIATION_RECOMMENDATION_ONLY
NEXT_ACTION_AUTHORIZED=false
SSH_RETRY_AUTHORIZED=false
SERVER_READ_AUTHORIZED=false
SERVER_WRITE_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

新的 Recommendation 必须把 exact alias `hongyan-4cj` 作为 transport identity，并继续
保持一个 fresh SSH session、read-only script、零写入和完整失败保留。
