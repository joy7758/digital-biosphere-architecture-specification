---
document_id: DBA-TITMAS-CE-G12-FRESH-IMMUTABLE-CANDIDATE-PREPARATION-REPORT-0.1
title: TITMAS CE-G12 Fresh Immutable Candidate Preparation Report v0.1
title_zh: TITMAS CE-G12 新不可变候选准备报告 v0.1
version: 0.1.0
status: pass-fresh-immutable-candidate-prepared-manifest-source-binding-remediation-required
maturity: Development
maturity_scope: commercial-static-site-candidate-preparation-only
owner_ref: zhangbin
decision_reference: TITMAS-COMMERCIAL-EVALUATION-CE-G12-CURRENT-TARGET-DISPOSITION
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G12 Fresh Immutable Candidate Preparation Report v0.1

## 1. Outcome

```text
RESULT=PASS_FRESH_IMMUTABLE_CANDIDATE_PREPARED_NO_DEPLOYMENT_AUTHORIZED
SOURCE_COMMIT=c1d8931930fbae15f96ee6a6ac050b081538c919
SOURCE_TREE=9171e554cfcbeaa02d5542c3a35cb729bca44185
TRACKED_JSON=1165/1165
DUPLICATE_KEYS=0
COMMERCIAL_ENTRY_SCHEMA=PASS
NPM_CI_OFFLINE=PASS
NPM_DIRECT_DEPENDENCIES=23
NPM_REPORTED_PROBLEMS=5
SITE_TESTS=16/16
RELEASE_FORMAL=PASS
CE_SCHEMA_HASHES=3/3
CE_SCHEMA_META=3/3
CE_TESTS=49/49
TRACKED_SOURCE_DIFF=0
REMOTE_SOURCE_DRIFT=0
ARCHIVE_BYTES=988323
ARCHIVE_SHA256=7240f58b5f4471ee9166b5fe18fe83937a344116114a4b33468a580e75cdcda2
MANIFEST_FILES=65
ROUTE_HASHES=11/11
```

机器材料：

- [Candidate Baseline](commercial-evaluation-fresh-candidate/ce-g12-fresh-candidate-baseline.v0.1.json)；
- [Preparation Result](commercial-evaluation-fresh-candidate/ce-g12-fresh-candidate-preparation-result.v0.1.json)。

固定 archive：

```text
/tmp/titmas-site-c1d8931930fbae15f96ee6a6ac050b081538c919.tar.gz
```

## 2. Execution boundary

执行在 exact `c1d8931…` 的一个 disposable detached worktree 中完成：

1. fetch exact source ref 一次；
2. 五个 source evidence hash PASS；
3. source commit/tree/parents/subject PASS；
4. tracked JSON `1165/1165`，duplicate key `0`；
5. commercialization entry Draft 2020-12 Schema PASS；
6. offline/ignore-scripts `npm ci` 一次，安装 `493` packages；
7. `npm ls` 一次，23 direct dependencies，保留 5 个 `extraneous` observations；
8. site tests `16/16`；
9. formal static export、中文/英文 parity、truth boundary PASS；
10. CE Schema hash/meta `3/3`，CE tests `49/49`；
11. source/tree/remote ref drift 为 0；
12. archive、manifest 和 11 条 route hash 已固定。

```text
SSH_SESSIONS=0
SERVER_READS=0
SERVER_WRITES=0
PUBLIC_SITE_REQUESTS=0
SYMLINK_SWITCHES=0
NGINX_TESTS=0
NGINX_RELOADS=0
ROLLBACKS=0
DEPLOYMENTS=0
RELEASES=0
PR_MUTATIONS=0
VALIDATION_RETRIES=0
NETWORK_FALLBACKS=0
```

## 3. Candidate disposition

旧 proposed release：

```text
f8107969aa1f43be8ecf43f557297a630309fe41
```

其 archive、failure、rollback 和 hash history 全部保留。由于新 candidate preparation PASS，
本 Result 只在 candidate-preparation 范围记录：

```text
OLD_CANDIDATE_DISPOSITION=SUPERSEDED_FOR_FRESH_CANDIDATE_PREPARATION
OLD_CANDIDATE_HISTORY_PRESERVED=true
OLD_EVIDENCE_MODIFIED=false
STATUS_SURFACES_SYNCHRONIZED=false
```

这不是删除、撤销或否定旧证据，也不自动改变当前服务器 target。

## 4. Cleanup history

首次 shell exit trap 没有移除 disposable worktree。没有重跑验证、没有重建 archive；
随后只执行一次 cleanup remediation，最终：

```text
DISPOSABLE_WORKTREES_CREATED=1
VALIDATION_COMMANDS_RETRIED=0
CANDIDATE_ARCHIVE_REBUILT=false
FINAL_WORKTREES_REMAINING=0
FINAL_WORKTREE_DIRECTORIES_REMAINING=0
```

该收尾缺口被保留，没有覆盖为“初次 cleanup PASS”。

## 5. Manifest source-binding gap

archive 与外部 Candidate Baseline 已精确绑定：

```text
CANDIDATE_SOURCE_COMMIT=c1d8931930fbae15f96ee6a6ac050b081538c919
CANDIDATE_SOURCE_TREE=9171e554cfcbeaa02d5542c3a35cb729bca44185
ARCHIVE_SHA256=7240f58b5f4471ee9166b5fe18fe83937a344116114a4b33468a580e75cdcda2
```

但 archive 内部 `release-manifest.json` 当前记录：

```text
source_revision=working-tree
```

因此：

```text
CANDIDATE_SOURCE_EXTERNALLY_BOUND=true
MANIFEST_SOURCE_REVISION_MATCHES_CANDIDATE=false
MANIFEST_SOURCE_BINDING_PASS=false
```

这不否定本地 candidate preparation PASS，但阻止把该 archive 直接升级为 deployment-admitted
release。面向智能体的公开 manifest 应能明确回答 exact source revision。

## 6. Boundaries

```text
CANDIDATE_PREPARED_NE_RELEASE=true
CANDIDATE_PREPARED_NE_DEPLOYMENT=true
STATIC_EXPORT_PASS_NE_PRODUCTION_READY=true
ARCHIVE_HASH_NE_COMMERCIAL_AVAILABILITY=true
EXTERNAL_SOURCE_BINDING_NE_INTERNAL_MANIFEST_BINDING=true
EVIDENCE_NE_TRUTH=true
DEPLOYMENT_ADMISSION_PASS=false
SERVER_STATE_CHANGED=false
REPAIR_AUTHORIZED=false
ROLLBACK_AUTHORIZED=false
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
NEXT_ACTION=PREPARE_CE_G12_CANDIDATE_MANIFEST_SOURCE_BINDING_RECOMMENDATION_ONLY
NEXT_ACTION_AUTHORIZED=false
SERVER_READ_AUTHORIZED=false
SERVER_WRITE_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

下一 Recommendation 应比较：

1. 修改 export/build source 以写入 exact revision，并建立新的 source commit/candidate；
2. 保持 archive 不变，增加 signed/external provenance envelope；
3. 接受 `working-tree` 标签并只依赖外部 baseline；
4. 跳过 binding 直接部署。

它必须优先满足 agent-readable exact provenance，同时避免为了修复标签而静默改写当前
candidate 或历史证据。
