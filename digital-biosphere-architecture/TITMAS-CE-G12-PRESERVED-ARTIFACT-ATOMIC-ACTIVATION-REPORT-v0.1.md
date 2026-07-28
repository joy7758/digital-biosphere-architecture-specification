---
document_id: DBA-TITMAS-CE-G12-PRESERVED-ARTIFACT-ATOMIC-ACTIVATION-REPORT-0.1
title: TITMAS CE-G12 Preserved Artifact Atomic Activation Report v0.1
title_zh: TITMAS CE-G12 已保留制品原子激活报告 v0.1
version: 0.1.0
status: pass-reverified-preserved-artifact-active-no-new-product-release
maturity: Development
maturity_scope: one-bounded-static-site-preserved-artifact-activation-only
owner_ref: zhangbin
decision_reference: TITMAS-COMMERCIAL-EVALUATION-CE-G12-PRESERVED-ARTIFACT-ATOMIC-ACTIVATION
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G12 Preserved Artifact Atomic Activation Report v0.1

## 1. Outcome

```text
RESULT=PASS_REVERIFIED_PRESERVED_ARTIFACT_ATOMIC_ACTIVATION_NO_NEW_PRODUCT_RELEASE_AUTHORIZED
PRESERVED_ARTIFACT_REVERIFIED=true
FORWARD_SWITCHES=1
ROLLBACK_SWITCHES=0
ROUTE_CONTRACTS_PASS=10/10
CANDIDATE_ACTIVE=true
RETRIES=0
```

机器结果：

- [Activation Result](commercial-evaluation-fresh-candidate/ce-g12-preserved-artifact-atomic-activation-result.v0.1.json)。

## 2. Activated identity

```text
SOURCE_COMMIT=c1d8931930fbae15f96ee6a6ac050b081538c919
ARCHIVE_SHA256=f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7
RELEASE_ID=c1d8931930fbae15f96ee6a6ac050b081538c919--f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7
CURRENT=/srv/tmai/releases/c1d8931930fbae15f96ee6a6ac050b081538c919--f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7
```

current 从 `ccf473f3…` 原子切到 source+artifact 双绑定路径。

## 3. Fresh reverification

```text
ARTIFACT_BYTES=979463
ARTIFACT_SHA256=f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7
MANIFEST_SHA256=f0e42b7f0be3c36f201517d68bef42ec365809261ed46d4fc6af74949a397a60
MANIFEST_FILES=65
ACTUAL_FILES=66
FILE_HASHES_PASS=65/65
DIRECTORIES_INCLUDING_ROOT=21
OWNER_GROUP=root:root
DIRECTORY_MODE=0755
FILE_MODE=0644
UNEXPECTED_SYMLINKS_OR_SPECIALS=0
NGINX_CONFIG_SHA256=ddbd14b27abcce59330d86156fc0d42ea2ebaf933f3bc1447eba0fc9c13b29b5
NGINX_TEST_PASS=true
```

历史 pass 没有直接当作 current truth；所有关键条件均在 activation session 内重新读取。

## 4. Correct canonical route validation

```text
/ = 200 + exact index hash

/en = 301 -> /en/
/en/ = 200 + exact en/index hash
follow(/en) = 200 + exact en/index hash

/status = 301 -> /status/
/status/ = 200 + exact status/index hash
follow(/status) = 200 + exact status/index hash

/en/status = 301 -> /en/status/
/en/status/ = 200 + exact en/status/index hash
follow(/en/status) = 200 + exact en/status/index hash
```

10/10 contract checks PASS。上一次验证器对 301 body 的错误比较没有被重复。

## 5. Mutation boundary

```text
ARCHIVE_TRANSFERS=0
ARCHIVE_EXTRACTIONS=0
ARTIFACT_OR_RELEASE_CREATIONS=0
NGINX_RELOADS=0
PUBLIC_EXTERNAL_REQUESTS=0
CLEANUPS=0
REPAIRS=0
FORWARD_SWITCHES=1
ROLLBACK_SWITCHES=0
```

唯一发布性 mutation 是 atomic current symlink switch。证书、Nginx config、安全设置、DNS、
DBOS 与 SAEE 均未修改。

## 6. Status boundaries

```text
STATIC_SITE_ACTIVATION_PASS=true
CANDIDATE_ACTIVE=true
PUBLIC_SITE_CURRENT_TARGET_CHANGED=true
NEW_PRODUCT_RELEASE_AUTHORIZED=false
NEW_PRODUCT_RELEASE_EXECUTED=false
STANDARD_READY=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
AUTHORITY_CREATED=false
PERMISSION_CREATED=false
EVIDENCE_TRUTH_CHANGED=false
```

“active static site candidate”不等于新产品 release、Production 或商业 offering。

## 7. Remaining external gate

本轮只使用 server-local HTTPS + Host/SNI；没有执行 outside-in public request。因此：

```text
OUTSIDE_IN_PUBLIC_REACHABILITY_FRESHLY_VERIFIED=false
PUBLIC_ROUTE_VALIDATION_AUTHORIZED=false
```

下一步只应准备独立 Public Route Validation Recommendation，限定少量外部 GET/HEAD，核对
TLS、status、redirect、body hash 和 agent-readable endpoints；不得写 server 或产生 release
状态提升。
