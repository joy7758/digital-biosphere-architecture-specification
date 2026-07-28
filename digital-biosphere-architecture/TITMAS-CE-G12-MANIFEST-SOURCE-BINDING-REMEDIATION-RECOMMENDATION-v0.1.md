---
document_id: DBA-TITMAS-CE-G12-MANIFEST-SOURCE-BINDING-REMEDIATION-RECOMMENDATION-0.1
title: TITMAS CE-G12 Manifest Source-binding Remediation Recommendation v0.1
title_zh: TITMAS CE-G12 Manifest 来源绑定修复建议 v0.1
version: 0.1.0
status: explicit-source-revision-injection-and-one-rebuild-recommended-agent-review-required-decision-pending
maturity: Development
maturity_scope: commercial-static-site-candidate-manifest-source-binding-only
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G12 Manifest Source-binding Remediation Recommendation v0.1

## 1. Recommendation

采用 **Option A：使用现有 `SOURCE_REVISION` 输入契约，在同一个 exact source commit
`c1d8931…` 上执行一次显式来源注入的离线重建，生成新的 immutable candidate archive**。

```text
RECOMMENDED_OPTION=A
SOURCE_COMMIT=c1d8931930fbae15f96ee6a6ac050b081538c919
SOURCE_TREE=9171e554cfcbeaa02d5542c3a35cb729bca44185
SOURCE_CODE_CHANGE_REQUIRED=false
SOURCE_REVISION_INPUT=c1d8931930fbae15f96ee6a6ac050b081538c919
CURRENT_ARCHIVE_PRESERVED=true
CURRENT_ARCHIVE_DEPLOYMENT_ADMITTED=false
NEW_ARCHIVE_CREATED=false
REBUILD_AUTHORIZED=false
DEPLOYMENT_RECOMMENDED=false
RELEASE_RECOMMENDED=false
DECISION_RECORDED=false
```

本建议只选择 manifest source binding（manifest 来源绑定）的修复方向。它不在当前动作中：

- 重建 static export；
- 修改 `c1d8931…` 源码或 tree；
- 改写当前 archive、baseline、Result 或 Report；
- 访问服务器或公开网站；
- 建立 release directory；
- 切换 symlink；
- 部署、发布或声明 commercial availability（商业可用）。

## 2. Direct evidence bindings

### 2.1 Prepared candidate

- [Candidate Baseline](commercial-evaluation-fresh-candidate/ce-g12-fresh-candidate-baseline.v0.1.json)
  SHA-256 `4c7f55b1f277f22eda536a392058031bad04876d2c5b37997a6a505aea5802ed`；
- [Preparation Result](commercial-evaluation-fresh-candidate/ce-g12-fresh-candidate-preparation-result.v0.1.json)
  SHA-256 `2c0a3c6352f201a690af77f91ecf550c04af5017ea52a383fe525ff536a56110`；
- [Preparation Report](TITMAS-CE-G12-FRESH-IMMUTABLE-CANDIDATE-PREPARATION-REPORT-v0.1.md)
  SHA-256 `9878aff3d9b4132d99a95d5d47c5f1089d438bcc4c484817f90bc238f23cb22b`；
- remotely verified governance commit
  `3a908c0ef936104409afcd86fe7c373a36d5a847`。

已证明：

```text
CANDIDATE_PREPARATION_PASS=true
ARCHIVE_SHA256=7240f58b5f4471ee9166b5fe18fe83937a344116114a4b33468a580e75cdcda2
ARCHIVE_BYTES=988323
ARCHIVE_ENTRIES=87
MANIFEST_SHA256=8b168f1609b99ba04a4ecac81a5a19d789689bc95190d533b00efad9ab58f9d4
MANIFEST_FILES=65
ROUTE_HASHES=11/11
TRACKED_SOURCE_DIFF=0
REMOTE_SOURCE_DRIFT=0
```

同时明确：

```text
MANIFEST_SOURCE_REVISION=working-tree
MANIFEST_SOURCE_REVISION_MATCHES_CANDIDATE=false
MANIFEST_SOURCE_BINDING_PASS=false
DEPLOYMENT_ADMISSION_PASS=false
```

### 2.2 Existing source-revision input contract

在 exact source commit `c1d8931930fbae15f96ee6a6ac050b081538c919` 中：

```text
FILE=digital-biosphere-architecture/site/scripts/export-static.mjs
GIT_BLOB=f7f3b75370e48577dc5812d389b5ccfd21805044
SOURCE_REVISION_RESOLUTION=process.env.SOURCE_REVISION || "working-tree"
RELEASE_JSON_SOURCE_REVISION=sourceRevision
RELEASE_MANIFEST_SOURCE_REVISION=sourceRevision
```

`verify-static.mjs` 已要求：

```text
release-manifest.source_revision == release.source_revision
```

`site/package.json` blob
`f30dcc3f4b41a53539737becfb58d0b6a1d26525` 的 `release:formal` 当前不固定
`SOURCE_REVISION`，因此调用方必须显式提供。现有实现已经具备正确输入点，不需要为了这一
缺口修改 source commit。

问题的精确根因是：

```text
EXPLICIT_SOURCE_REVISION_NOT_PROVIDED_DURING_CANDIDATE_BUILD=true
EXPORT_SCRIPT_CAPABILITY_MISSING=false
SOURCE_CODE_DEFECT_PROVEN=false
```

## 3. Why Option A best advances commercialization

Agent-readable（智能体可读）公开材料必须让开发者与智能体从归档内部直接回答：

> 该发布内容由哪个精确源码提交生成？

只依赖外部 baseline 会产生两个需要联合解释的事实表面；修改源码会在现有能力已经足够时
制造不必要的新 source commit。跳过绑定则会把已知 `working-tree` 歧义带入公开候选。

Option A 使用现有输入契约：

```text
SOURCE_REVISION=c1d8931930fbae15f96ee6a6ac050b081538c919
npm run release:formal
```

并要求生成后的：

```text
release.json.source_revision
==
release-manifest.json.source_revision
==
c1d8931930fbae15f96ee6a6ac050b081538c919
```

它保持 source commit/tree 不变，只生成新的 derived artifact（派生产物）。旧 archive 与
失败的 binding 证据继续保留，不静默覆盖。

## 4. Exact future remediation scope

未来独立 Decision 最多授权：

1. 要求本 Recommendation、一次 exact `qwen3.7-max` review、Decision 和 Decision review
   全部远端固定；
2. 核对 governance local/remote HEAD 一致；
3. fetch 一次并要求 remote production baseline 仍为 exact `c1d8931…`；
4. 核对 exact source commit/tree、两个 source blob 和三件 candidate evidence hash；
5. 创建一个 disposable detached worktree at exact `c1d8931…`；
6. 执行一次 tracked JSON parse/duplicate-key validation 和一次 Commercial Entry Schema
   validation；
7. 复用已缓存依赖，执行一次 offline `npm ci --ignore-scripts` 和一次 `npm ls`；
8. 执行一次 site tests；
9. 仅以显式环境输入
   `SOURCE_REVISION=c1d8931930fbae15f96ee6a6ac050b081538c919`
   执行一次 `npm run release:formal`；
10. 要求 `release.json` 与 `release-manifest.json` 都精确绑定 `c1d8931…`，且两者相等；
11. 执行一次 CE Schema hash/meta validation 和一次 CE tests；
12. 要求 tracked source diff、source tree drift 和 remote ref drift 为 0；
13. 从新的 exact static export 创建一个且仅一个新 archive，记录 archive、manifest 和
    route hashes；
14. 生成 replacement Candidate Baseline、Result 和 Report；
15. 只有新 candidate 全部 PASS 时，记录当前 archive 为
    `SUPERSEDED_FOR_EXACT_SOURCE_BOUND_CANDIDATE`，但不删除、不覆盖；
16. 清理 disposable worktree；
17. 只提交 replacement candidate artifacts，不读取或修改服务器。

这仍然只是 candidate remediation（候选修复），不是 deployment admission（部署准入）。

## 5. Candidate identity and preservation rules

当前 archive 固定为：

```text
/tmp/titmas-site-c1d8931930fbae15f96ee6a6ac050b081538c919.tar.gz
SHA256=7240f58b5f4471ee9166b5fe18fe83937a344116114a4b33468a580e75cdcda2
```

未来重建不得覆盖该路径。必须使用新的 candidate identity，例如带
`source-bound` 或独立 candidate id 的路径，并记录新的 archive SHA。

```text
OLD_ARCHIVE_HISTORY_PRESERVED=true
OLD_ARCHIVE_OVERWRITE_ALLOWED=false
OLD_BASELINE_OVERWRITE_ALLOWED=false
OLD_RESULT_OVERWRITE_ALLOWED=false
NEW_ARCHIVE_SHA_MUST_DIFFER_IF_CONTENT_DIFFERS=true
```

## 6. Execution caps for a future Decision

```text
QWEN_DECISION_REVIEW_REQUESTS_MAX=1
GIT_FETCHES_MAX=1
DISPOSABLE_WORKTREES_MAX=1
NPM_CI_ATTEMPTS_MAX=1
NPM_LS_ATTEMPTS_MAX=1
SITE_TEST_ATTEMPTS_MAX=1
RELEASE_FORMAL_ATTEMPTS_MAX=1
CE_TEST_ATTEMPTS_MAX=1
CANDIDATE_ARCHIVES_MAX=1
SERVER_READS=0
SERVER_WRITES=0
PUBLIC_SITE_REQUESTS=0
SSH_SESSIONS=0
SYMLINK_SWITCHES=0
NGINX_TESTS=0
NGINX_RELOADS=0
ROLLBACKS=0
DEPLOYMENTS=0
RELEASES=0
PR_MUTATIONS=0
RETRIES=0
NETWORK_FALLBACKS=0
MODEL_REQUESTS_DURING_REMEDIATION=0
```

## 7. Options

### Option A — Use the existing `SOURCE_REVISION` contract and rebuild once（推荐）

同一 exact source commit/tree，显式注入来源，生成新的 source-bound archive；不改源码、
不部署。

### Option B — Modify export/build source and create a new source commit（当前拒绝）

现有 `export-static.mjs` 已提供正确输入点。除非 Option A 的独立执行证明现有 contract
无法满足要求，否则修改源码属于扩大变更面。

### Option C — Preserve the archive and add an external provenance envelope（当前拒绝）

它可以补充 provenance，但 archive 内 manifest 仍为 `working-tree`，形成双重来源表面；
不满足 agent-readable archive self-description（归档自描述）优先目标。

### Option D — Accept `working-tree` or deploy without binding（拒绝）

这会绕过已明确失败的 deployment admission gate，并把可避免的来源歧义公开化。

## 8. Stop conditions

- Recommendation 或 review 未远端固定；
- 返回模型不是 exact `qwen3.7-max`；
- direct JSON 或 review contract 无效；
- Decision/Decision review 未远端固定；
- remote production baseline 不再是 exact `c1d8931…`；
- exact source script/package blob 或三件 evidence hash 漂移；
- 需要修改源码才能继续，但没有新的 Recommendation/Decision；
- 需要覆盖当前 archive、baseline、Result、Report 或历史 evidence；
- `release.json` 或 manifest 仍为 `working-tree`、空值、短 SHA 或与 exact source 不一致；
- build 需要 online dependency resolution、retry、第二 worktree 或 network fallback；
- 需要任何 server/public-site/SSH/symlink/nginx/rollback/deployment/release/PR mutation；
- source-bound candidate 被升级为 Standard Ready、Production、commercial offering、SLA
  或 certification。

## 9. Recommendation review contract

exact `qwen3.7-max` 只允许一次 direct JSON review，必须返回：

```text
verdict
confidence
selected_option
would_recommend_to_agent_customer
existing_source_revision_contract_sufficient
root_cause_scope_sound
same_source_rebuild_sound
archive_self_description_priority_sound
history_preservation_sound
caps_and_stop_rules_sufficient
no_deployment_or_release_inference
authority_boundaries_preserved
blockers
corrections
rationale
```

qualifying 条件：

```text
returned_model == qwen3.7-max
verdict == RECOMMENDED
selected_option == A
confidence >= 0.80
would_recommend_to_agent_customer == true
all boolean controls == true
blockers == []
corrections == []
```

## 10. Non-authorizations

```text
RECOMMENDATION_NE_DECISION=true
SOURCE_REVISION_INPUT_NE_SOURCE_CHANGE=true
CANDIDATE_REBUILD_NE_DEPLOYMENT=true
MANIFEST_BINDING_PASS_NE_RELEASE_AUTHORITY=true
CURRENT_CANDIDATE_PRESERVED=true
NEW_CANDIDATE_CREATED=false
SOURCE_CHANGED=false
SERVER_STATE_CHANGED=false
PUBLIC_SITE_CHANGED=false
REBUILD_AUTHORIZED=false
REPAIR_AUTHORIZED=false
ROLLBACK_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
STANDARD_READY=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
AUTHORITY_CREATED=false
PERMISSION_CREATED=false
EVIDENCE_TRUTH_CHANGED=false
```
