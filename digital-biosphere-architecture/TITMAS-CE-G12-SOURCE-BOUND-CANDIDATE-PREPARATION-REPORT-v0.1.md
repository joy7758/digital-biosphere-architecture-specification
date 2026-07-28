---
document_id: DBA-TITMAS-CE-G12-SOURCE-BOUND-CANDIDATE-PREPARATION-REPORT-0.1
title: TITMAS CE-G12 Source-bound Candidate Preparation Report v0.1
title_zh: TITMAS CE-G12 精确来源绑定候选准备报告 v0.1
version: 0.1.0
status: fail-closed-source-binding-pass-portable-archive-fail
maturity: Development
maturity_scope: commercial-static-site-source-bound-candidate-preparation-only
owner_ref: zhangbin
decision_reference: TITMAS-COMMERCIAL-EVALUATION-CE-G12-MANIFEST-SOURCE-BINDING-REMEDIATION
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G12 Source-bound Candidate Preparation Report v0.1

## 1. Outcome

```text
RESULT=FAIL_CLOSED_EXACT_SOURCE_BOUND_CANDIDATE_NOT_PREPARED_NO_DEPLOYMENT_AUTHORIZED
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
PORTABLE_ARCHIVE=FAIL
CANDIDATE_PREPARED=false
```

机器材料：

- [Rejected Archive Baseline](commercial-evaluation-fresh-candidate/ce-g12-source-bound-candidate-baseline.v0.1.json)；
- [Preparation Result](commercial-evaluation-fresh-candidate/ce-g12-source-bound-candidate-preparation-result.v0.1.json)。

## 2. Source-binding remediation passed

本次没有修改 source。exact `c1d8931…` 中的既有 `SOURCE_REVISION` contract 被显式调用：

```text
SOURCE_REVISION=c1d8931930fbae15f96ee6a6ac050b081538c919
npm run release:formal
```

直接验证：

```text
release.json.source_revision
==
release-manifest.json.source_revision
==
c1d8931930fbae15f96ee6a6ac050b081538c919
```

因此原 `working-tree` 缺口的根因得到验证：调用方缺少显式输入，export source capability
本身并不缺失。

## 3. Portable archive failure

唯一授权的 archive 已生成：

```text
ARCHIVE=/tmp/titmas-site-c1d8931930fbae15f96ee6a6ac050b081538c919-source-bound.tar.gz
ARCHIVE_BYTES=994348
ARCHIVE_SHA256=789064b92d6dd93f615406ae6430d2b5410d5396d01969fc708f89e2e489e665
MANIFEST_SHA256=f5d26d8e9ae1e26a0288cea24fa3a572a4ba1c1cf39ce6633be7b488db143434
MANIFEST_FILES=65
ROUTE_HASHES=11/11
```

macOS `bsdtar` 将每个正常成员的扩展属性 sidecar 作为 `._*` AppleDouble member 写入归档：

```text
ARCHIVE_ENTRIES_TOTAL=174
PAYLOAD_ENTRIES=87
APPLEDOUBLE_ENTRIES=87
UNIQUE_NAMES=174
DUPLICATE_NAMES=0
```

这些 87 个 sidecar 不在 `release-manifest.json` 的 65-file 内容清单中。虽然 payload route、
manifest 和 exact source binding 都正确，但 archive 实际内容超出 manifest 覆盖范围，
不满足跨平台、agent-readable、可审计的商业候选要求。

BSD `tar -t` 默认视图只显示 87 个正常条目；Python `tarfile` 对原始 archive 的直接读取
揭示了全部 174 个成员。本报告保留这一区别，不用较窄的列表结果覆盖原始 archive 事实。

## 4. Fail-closed disposition

没有执行第二次 archive build，也没有改变第一次 archive：

```text
ARCHIVES_CREATED=1
ARCHIVE_REBUILDS=0
VALIDATION_RETRIES=0
NETWORK_FALLBACKS=0
SOURCE_FIXES=0
```

因此：

```text
SOURCE_BINDING_REMEDIATION_PASS=true
PORTABLE_ARCHIVE_VALIDATION_PASS=false
ARCHIVE_MANIFEST_COVERAGE_PASS=false
ARCHIVE_ADMITTED_AS_CANDIDATE=false
CURRENT_CANDIDATE_SUPERSEDED=false
```

旧 candidate archive
`7240f58b5f4471ee9166b5fe18fe83937a344116114a4b33468a580e75cdcda2`
仍完整存在，未覆盖、未删除、未 supersede。

## 5. Execution boundary

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

## 6. Boundaries

```text
SOURCE_BINDING_PASS_NE_CANDIDATE_PASS=true
TESTS_PASS_NE_PORTABLE_ARCHIVE_PASS=true
ARCHIVE_HASH_NE_MANIFEST_COVERAGE=true
CANDIDATE_PREPARED_NE_DEPLOYMENT=true
EVIDENCE_NE_TRUTH=true
CANDIDATE_PREPARED=false
DEPLOYMENT_ADMISSION_PASS=false
SERVER_STATE_CHANGED=false
DEPLOYMENT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
STANDARD_READY=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
AUTHORITY_CREATED=false
PERMISSION_CREATED=false
```

## 7. Next gate

```text
NEXT_ACTION=PREPARE_CE_G12_PORTABLE_ARCHIVE_REMEDIATION_RECOMMENDATION_ONLY
NEXT_ACTION_AUTHORIZED=false
ARCHIVE_REBUILD_AUTHORIZED=false
SERVER_READ_AUTHORIZED=false
SERVER_WRITE_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

下一 Recommendation 应比较：

1. 在 macOS packaging command 中显式禁止 AppleDouble／extended attribute sidecar；
2. 使用跨平台、可复现的独立 archive producer；
3. 将全部 archive member 纳入 manifest（不推荐，因为 sidecar 不是产品内容）；
4. 忽略 sidecar 并继续（拒绝，因为 manifest coverage 已知失败）。

无论选择哪一项，都必须建立新的 archive identity，保留本次失败 archive，并再次证明
normal member count、sidecar count、manifest coverage、source binding 和 route hashes。
