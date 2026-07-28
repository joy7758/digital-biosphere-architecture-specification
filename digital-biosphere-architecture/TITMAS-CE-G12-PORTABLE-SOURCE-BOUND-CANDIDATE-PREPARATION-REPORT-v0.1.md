---
document_id: DBA-TITMAS-CE-G12-PORTABLE-SOURCE-BOUND-CANDIDATE-PREPARATION-REPORT-0.1
title: TITMAS CE-G12 Portable Exact-source-bound Candidate Preparation Report v0.1
title_zh: TITMAS CE-G12 可移植精确来源绑定候选准备报告 v0.1
version: 0.1.0
status: pass-portable-exact-source-bound-candidate-prepared-no-deployment-authorized
maturity: Development
maturity_scope: commercial-static-site-candidate-preparation-only
owner_ref: zhangbin
decision_reference: TITMAS-COMMERCIAL-EVALUATION-CE-G12-PORTABLE-ARCHIVE-REMEDIATION
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G12 Portable Exact-source-bound Candidate Preparation Report v0.1

## 1. Outcome

```text
RESULT=PASS_PORTABLE_EXACT_SOURCE_BOUND_CANDIDATE_PREPARED_NO_DEPLOYMENT_AUTHORIZED
SOURCE_COMMIT=c1d8931930fbae15f96ee6a6ac050b081538c919
SOURCE_TREE=9171e554cfcbeaa02d5542c3a35cb729bca44185
TRACKED_JSON=1165/1165
DUPLICATE_KEYS=0
COMMERCIAL_ENTRY_SCHEMA=PASS
NPM_CI_OFFLINE=PASS
SITE_TESTS=16/16
RELEASE_FORMAL=PASS
CE_SCHEMA_HASHES=3/3
CE_SCHEMA_META=3/3
CE_TESTS=49/49
SOURCE_REVISION_BINDING=PASS
PORTABLE_ARCHIVE=PASS
CANDIDATE_PREPARED=true
DEPLOYMENT_ADMISSION_PASS=false
```

机器材料：

- [Portable Candidate Baseline](commercial-evaluation-fresh-candidate/ce-g12-portable-source-bound-candidate-baseline.v0.1.json)；
- [Preparation Result](commercial-evaluation-fresh-candidate/ce-g12-portable-source-bound-candidate-preparation-result.v0.1.json)。

## 2. Fixed candidate

```text
ARCHIVE=/tmp/titmas-site-c1d8931930fbae15f96ee6a6ac050b081538c919-source-bound-portable.tar.gz
ARCHIVE_BYTES=979463
ARCHIVE_SHA256=f3f46e5e51beb33bc3c2bcaec8df98378a6a65aa905b9a93b271d3cbc304a2a7
MANIFEST_SHA256=f0e42b7f0be3c36f201517d68bef42ec365809261ed46d4fc6af74949a397a60
MANIFEST_FILES=65
ROUTE_HASHES=11/11
```

archive producer：

```text
bsdtar 3.5.3 / libarchive 3.7.4
FLAGS=--no-mac-metadata --no-xattrs
```

## 3. Raw-member conformance

Python `tarfile` 对原始 archive 直接读取：

```text
TOTAL_RAW_MEMBERS=87
DIRECTORY_MEMBERS=21
FILE_MEMBERS=66
NORMAL_PAYLOAD_MEMBERS=87
APPLEDOUBLE_MEMBERS=0
DUPLICATE_MEMBER_NAMES=0
UNEXPECTED_SPECIAL_MEMBERS=0
MANIFEST_LISTED_FILES=65
MANIFEST_SELF_ENTRY=1
MANIFEST_FILE_COVERAGE_PASS=true
```

这修复了前一 archive 的 87 个 `._*` AppleDouble sidecar，并证明实际 archive content 与
manifest file contract 一致。

## 4. Exact source binding

```text
release.json.source_revision
==
release-manifest.json.source_revision
==
c1d8931930fbae15f96ee6a6ac050b081538c919
```

source commit/tree 未改变，tracked source diff 为 0。

## 5. Preserved history

两个 prior candidate attempts 均保留：

1. `7240f58b…`：manifest `source_revision=working-tree`；
2. `789064b…`：source binding PASS，但包含 87 个 AppleDouble members。

只有在本 portable candidate 完整 PASS 后，Result 才把它们记录为
`SUPERSEDED_FOR_PORTABLE_EXACT_SOURCE_BOUND_CANDIDATE`。这不是删除、覆盖、撤销或修改
历史 evidence。

## 6. Execution boundary

```text
GIT_FETCHES=1
DISPOSABLE_WORKTREES_CREATED=1
DISPOSABLE_WORKTREES_REMOVED=1
FINAL_WORKTREES_REMAINING=0
NPM_CI_ATTEMPTS=1
NPM_LS_ATTEMPTS=1
SITE_TEST_ATTEMPTS=1
RELEASE_FORMAL_ATTEMPTS=1
CE_TEST_ATTEMPTS=1
PORTABLE_ARCHIVES_CREATED=1
ARCHIVE_REBUILDS=0
VALIDATION_RETRIES=0
NETWORK_FALLBACKS=0
SSH_SESSIONS=0
SERVER_READS=0
SERVER_WRITES=0
PUBLIC_SITE_REQUESTS=0
SYMLINK_SWITCHES=0
NGINX_RELOADS=0
DEPLOYMENTS=0
RELEASES=0
PR_MUTATIONS=0
MODEL_REQUESTS_DURING_EXECUTION=0
```

## 7. Boundaries

```text
PORTABLE_CANDIDATE_PASS_NE_DEPLOYMENT_ADMISSION=true
CANDIDATE_PREPARED_NE_RELEASE=true
TESTS_PASS_NE_PRODUCTION_READY=true
ARCHIVE_HASH_NE_COMMERCIAL_AVAILABILITY=true
EVIDENCE_NE_TRUTH=true
SERVER_STATE_CHANGED=false
DEPLOYMENT_ADMISSION_PASS=false
DEPLOYMENT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
STANDARD_READY=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
AUTHORITY_CREATED=false
PERMISSION_CREATED=false
```

## 8. Next gate

```text
NEXT_ACTION=PREPARE_CE_G12_PORTABLE_CANDIDATE_DEPLOYMENT_ADMISSION_RECOMMENDATION_ONLY
NEXT_ACTION_AUTHORIZED=false
SERVER_READ_AUTHORIZED=false
SERVER_WRITE_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

下一 Recommendation 必须重新核对 current server target、stable rollback reference、
candidate archive/hash、release directory identity、preflight scope 和 rollback conditions。
Candidate PASS 本身不能替代 deployment admission Decision。
