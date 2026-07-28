---
document_id: DBA-TITMAS-CE-G12-MANIFEST-SOURCE-BINDING-REMEDIATION-RECOMMENDATION-0.2
title: TITMAS CE-G12 Manifest Source-binding Remediation Recommendation v0.2
title_zh: TITMAS CE-G12 Manifest 来源绑定修复建议 v0.2
version: 0.2.0
status: explicit-source-revision-injection-and-one-rebuild-recommended-new-review-candidate
maturity: Development
maturity_scope: commercial-static-site-candidate-manifest-source-binding-only
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
supersedes_for_future_review_only: DBA-TITMAS-CE-G12-MANIFEST-SOURCE-BINDING-REMEDIATION-RECOMMENDATION-0.1
---

# TITMAS CE-G12 Manifest Source-binding Remediation Recommendation v0.2

## 1. Prior non-qualifying review transport

v0.1 触发了一个且仅一个 `qwen3.7-max` 请求，但执行会话没有返回任何可观察 stdout 或
stderr，无法证明 returned model、HTTP status 或 direct JSON。该请求没有重试、回退、
模型替换、JSON 提取或修复，并作为 fail-closed evidence 保留：

- [v0.1 Recommendation](TITMAS-CE-G12-MANIFEST-SOURCE-BINDING-REMEDIATION-RECOMMENDATION-v0.1.md)
  SHA-256 `2f511b0c0f1ff152a1e242aefad0160484fdba8bddf4a6196453b90962eca06b`；
- [v0.1 Review Failure](TITMAS-CE-G12-MANIFEST-SOURCE-BINDING-REMEDIATION-RECOMMENDATION-QWEN-REVIEW-FAILURE-v0.1.json)；
- remotely verified evidence commit
  `52b019b0a6c56d7a859729817ff9011a798da643`。

离线诊断只确认：

```text
API_KEY_PRESENT=true
API_KEY_VALUE_RECORDED=false
BASE_URL_PRESENT=true
HTTPS_SCHEME=true
COMPATIBLE_MODE_V1_SUFFIX=true
EXPECTED_CHAT_COMPLETIONS_PATH_CONSTRUCTED=true
```

它没有再次访问 provider，也没有把 transport precondition 升级为模型响应事实。

本 v0.2 是新的 Recommendation candidate。它保留 v0.1 failure，不重解释、不提取、不
修复 v0.1 响应，也不把后续 fresh review 记作 v0.1 retry。

## 2. Recommendation

采用 **Option A：使用 exact source 中已经存在的 `SOURCE_REVISION` 输入契约，在同一个
`c1d8931…` source commit/tree 上执行一次显式来源注入的离线重建，生成新的 immutable
source-bound candidate archive**。

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

## 3. Direct technical evidence

已远端固定的新候选准备证据：

| Artifact | SHA-256 |
|---|---|
| `commercial-evaluation-fresh-candidate/ce-g12-fresh-candidate-baseline.v0.1.json` | `4c7f55b1f277f22eda536a392058031bad04876d2c5b37997a6a505aea5802ed` |
| `commercial-evaluation-fresh-candidate/ce-g12-fresh-candidate-preparation-result.v0.1.json` | `2c0a3c6352f201a690af77f91ecf550c04af5017ea52a383fe525ff536a56110` |
| `TITMAS-CE-G12-FRESH-IMMUTABLE-CANDIDATE-PREPARATION-REPORT-v0.1.md` | `9878aff3d9b4132d99a95d5d47c5f1089d438bcc4c484817f90bc238f23cb22b` |

当前事实：

```text
CANDIDATE_PREPARATION_PASS=true
ARCHIVE_SHA256=7240f58b5f4471ee9166b5fe18fe83937a344116114a4b33468a580e75cdcda2
MANIFEST_SHA256=8b168f1609b99ba04a4ecac81a5a19d789689bc95190d533b00efad9ab58f9d4
ROUTE_HASHES=11/11
MANIFEST_SOURCE_REVISION=working-tree
MANIFEST_SOURCE_BINDING_PASS=false
DEPLOYMENT_ADMISSION_PASS=false
```

exact source `c1d8931…` 已具有输入能力：

```text
EXPORT_SCRIPT=digital-biosphere-architecture/site/scripts/export-static.mjs
EXPORT_SCRIPT_BLOB=f7f3b75370e48577dc5812d389b5ccfd21805044
SOURCE_REVISION_RESOLUTION=process.env.SOURCE_REVISION || "working-tree"
RELEASE_JSON_SOURCE_REVISION=sourceRevision
RELEASE_MANIFEST_SOURCE_REVISION=sourceRevision
PACKAGE_JSON_BLOB=f30dcc3f4b41a53539737becfb58d0b6a1d26525
```

因此根因是调用方没有显式传入 `SOURCE_REVISION`，不是已证明的 source capability 缺失。

## 4. Exact future remediation contract

未来独立 Decision 最多授权：

1. 固定本 v0.2、一次 qualifying Recommendation review、Decision 和 Decision review；
2. 核对 governance local/remote HEAD、source commit/tree、两个 source blob 和三件证据
   hash；
3. fetch 一次，创建一个 exact `c1d8931…` disposable detached worktree；
4. 一次 tracked JSON duplicate-rejecting validation 和 Commercial Entry Schema validation；
5. 一次 offline/ignore-scripts `npm ci`、一次 `npm ls`、一次 site tests；
6. 只以
   `SOURCE_REVISION=c1d8931930fbae15f96ee6a6ac050b081538c919`
   执行一次 `npm run release:formal`；
7. 要求 `release.json.source_revision` 与
   `release-manifest.json.source_revision` 都等于 exact full SHA；
8. 一次 CE Schema hash/meta validation 和一次 CE tests；
9. 要求 tracked source diff、source tree drift 和 remote drift 都为 0；
10. 创建一个新路径、一个新 archive，并固定 archive/manifest/route hashes；
11. 新 candidate PASS 后才记录旧 candidate
    `SUPERSEDED_FOR_EXACT_SOURCE_BOUND_CANDIDATE`；旧文件不得覆盖或删除；
12. 清理 worktree，只提交 replacement candidate artifacts；
13. 不读取、不修改服务器，不部署、不发布。

## 5. Why Option A

- **优于修改源码**：existing export script 已提供精确输入点；
- **优于外部 provenance envelope**：archive 内 manifest 可以直接自描述，不形成双重
  来源表面；
- **优于接受 `working-tree`**：消除已知 agent-readable provenance 歧义；
- **优于直接部署**：保持 deployment admission fail-closed。

```text
release.json.source_revision
==
release-manifest.json.source_revision
==
c1d8931930fbae15f96ee6a6ac050b081538c919
```

## 6. Options

- **Option A（推荐）**：现有 `SOURCE_REVISION` contract + same-source one-time rebuild；
- **Option B（拒绝）**：在 Option A 未证明不足前修改 export/build source；
- **Option C（拒绝）**：保留歧义 archive，仅增加 external envelope；
- **Option D（拒绝）**：接受 `working-tree` 或绕过 binding 部署。

## 7. Fresh review transport contract

v0.2 允许一个新的、独立的 Recommendation review request：

```text
MODEL=qwen3.7-max
REQUESTS=1
RETRIES=0
FALLBACKS=0
MODEL_SUBSTITUTIONS=0
JSON_EXTRACTIONS=0
JSON_REPAIRS=0
FOREGROUND_SESSION_OUTPUT_CAPTURE=true
```

必须返回：

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
fresh_review_separation_sound
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

## 8. Caps and stop conditions

未来 remediation caps：

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
NGINX_RELOADS=0
ROLLBACKS=0
DEPLOYMENTS=0
RELEASES=0
PR_MUTATIONS=0
RETRIES=0
NETWORK_FALLBACKS=0
```

停止于任何 SHA/blob/source/path/Schema/duplicate-key/manifest binding 漂移；停止于需要源码
修改、online dependency、retry、fallback、第二 worktree、覆盖历史 evidence 或任何
server/public-site/deployment/release 动作。

## 9. Non-authorizations

```text
RECOMMENDATION_NE_DECISION=true
FRESH_REVIEW_NE_PRIOR_RESPONSE_REPAIR=true
SOURCE_REVISION_INPUT_NE_SOURCE_CHANGE=true
CANDIDATE_REBUILD_NE_DEPLOYMENT=true
MANIFEST_BINDING_PASS_NE_RELEASE_AUTHORITY=true
CURRENT_CANDIDATE_PRESERVED=true
NEW_CANDIDATE_CREATED=false
SOURCE_CHANGED=false
SERVER_STATE_CHANGED=false
PUBLIC_SITE_CHANGED=false
REBUILD_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
STANDARD_READY=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
AUTHORITY_CREATED=false
PERMISSION_CREATED=false
EVIDENCE_TRUTH_CHANGED=false
```
