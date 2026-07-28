---
document_id: DBA-TITMAS-CE-G12-PORTABLE-ARCHIVE-REMEDIATION-RECOMMENDATION-0.1
title: TITMAS CE-G12 Portable Archive Remediation Recommendation v0.1
title_zh: TITMAS CE-G12 可移植归档修复建议 v0.1
version: 0.1.0
status: explicit-bsdtar-metadata-suppression-and-raw-member-validation-recommended-agent-review-required
maturity: Development
maturity_scope: commercial-static-site-portable-archive-only
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G12 Portable Archive Remediation Recommendation v0.1

## 1. Recommendation

采用 **Option A：在相同 exact source 和显式 `SOURCE_REVISION` 重建后，使用本机
`bsdtar` 的 `--no-mac-metadata --no-xattrs` 归档配置，并对原始 archive members 做
fail-closed validation**。

```text
RECOMMENDED_OPTION=A
SOURCE_COMMIT=c1d8931930fbae15f96ee6a6ac050b081538c919
SOURCE_TREE=9171e554cfcbeaa02d5542c3a35cb729bca44185
SOURCE_CODE_CHANGE_REQUIRED=false
SOURCE_REVISION_INPUT=c1d8931930fbae15f96ee6a6ac050b081538c919
ARCHIVE_PRODUCER=bsdtar
ARCHIVE_PRODUCER_VERSION=3.5.3
ARCHIVE_FLAGS=--no-mac-metadata --no-xattrs
RAW_MEMBER_VALIDATION_REQUIRED=true
REBUILD_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

本建议不执行 build、archive、server read、deployment 或 release。

## 2. Direct failure evidence

已远端固定：

| Artifact | SHA-256 |
|---|---|
| `commercial-evaluation-fresh-candidate/ce-g12-source-bound-candidate-baseline.v0.1.json` | `049eaf3b7295e55d1733aae1a00b347add6dc959533273f20eb86056760f2d7e` |
| `commercial-evaluation-fresh-candidate/ce-g12-source-bound-candidate-preparation-result.v0.1.json` | `d075b1cb2bebe880cf57bdfc645830047e477faadd1d80fb93bdafd99ffa4f6f` |
| `TITMAS-CE-G12-SOURCE-BOUND-CANDIDATE-PREPARATION-REPORT-v0.1.md` | `b4a005731ed14f28e81f28096dac6f1acff21cd8e09ad10ac7de228f4ac86f39` |

evidence commit：

```text
2f7bd9ce307ae4aeae19598ec343ff0c07082142
```

已证明：

```text
SOURCE_BINDING_REMEDIATION_PASS=true
release.json.source_revision=c1d8931930fbae15f96ee6a6ac050b081538c919
release-manifest.json.source_revision=c1d8931930fbae15f96ee6a6ac050b081538c919
TRACKED_JSON=1165/1165
SITE_TESTS=16/16
CE_TESTS=49/49
ARCHIVE_ENTRIES_TOTAL=174
NORMAL_PAYLOAD_ENTRIES=87
APPLEDOUBLE_ENTRIES=87
ARCHIVE_MANIFEST_COVERAGE_PASS=false
CANDIDATE_PREPARED=false
```

失败 archive：

```text
/tmp/titmas-site-c1d8931930fbae15f96ee6a6ac050b081538c919-source-bound.tar.gz
SHA256=789064b92d6dd93f615406ae6430d2b5410d5396d01969fc708f89e2e489e665
```

不得覆盖、删除或重新解释。

## 3. Exact producer evidence

当前 host 的 archive producer：

```text
bsdtar 3.5.3 - libarchive 3.7.4
```

本机 `tar` 文档直接暴露：

```text
--mac-metadata
  archive metadata using copyfile(3) in AppleDouble format

--no-mac-metadata
  reverse of --mac-metadata

--no-xattrs
  disable extended file attributes
```

因此本次 87 个 `._*` members 与 producer 默认 macOS metadata 行为一致。推荐命令必须
显式关闭该行为，而不是依赖 `tar -t` 的过滤视图。

## 4. Raw-member conformance contract

新的 archive 只有在全部条件满足时才可成为 candidate：

```text
TOTAL_RAW_MEMBERS=87
NORMAL_PAYLOAD_MEMBERS=87
APPLEDOUBLE_MEMBERS=0
DUPLICATE_MEMBER_NAMES=0
UNEXPECTED_SPECIAL_MEMBERS=0
MANIFEST_FILES=65
MANIFEST_LISTED_FILES_MATCH_PAYLOAD_FILES=true
RELEASE_SOURCE_REVISION_EXACT=true
MANIFEST_SOURCE_REVISION_EXACT=true
ROUTE_HASHES=11/11
```

验证必须使用能够看到全部 raw members 的 reader，例如 Python `tarfile`；不得只依赖
macOS `tar -t`，因为后者在本次失败 archive 上只显示 87 个正常条目。

archive 中 21 个 directory entries 与 66 个 file entries 合计 87。manifest 的 65 files
不包含 manifest 自身；因此合法 file contract 是：

```text
ARCHIVE_FILE_ENTRIES=66
MANIFEST_LISTED_FILES=65
MANIFEST_SELF_ENTRY=1
```

## 5. Exact future remediation scope

未来独立 Decision 最多授权：

1. 固定本 Recommendation、一次 exact `qwen3.7-max` review、Decision 和 Decision review；
2. 核对 governance local/remote、exact source、source blobs 和两个历史 archive/evidence
   hash；
3. 一个 fetch、一个 disposable exact-source worktree；
4. 一次 tracked JSON、Commercial Entry Schema、offline npm ci、npm ls、site tests；
5. 一次 exact `SOURCE_REVISION` formal release export；
6. 一次 CE Schema hash/meta 和 CE tests；
7. 要求 source/tree/remote snapshot drift 为 0；
8. 以
   `tar --no-mac-metadata --no-xattrs -czf <new-path> -C site/out .`
   创建一个新 archive；
9. 使用 raw-member reader 验证本节全部 conformance 条件；
10. 生成新的 portable Candidate Baseline、Result 和 Report；
11. 只有完整 PASS 才记录前两个 candidate attempts 为 superseded；历史 archive 不删除；
12. 清理 worktree，只提交三个结果 artifacts；
13. 不访问服务器、不部署、不发布。

## 6. Options

### Option A — Explicit `bsdtar` metadata suppression + raw-member validation（推荐）

最小改变 packaging invocation；不改 source，不接受不可见成员。

### Option B — New independent archive producer（暂缓）

可能提高跨平台可复现性，但会引入新的 producer、metadata normalization 和验证面。只有
Option A 证明不足时再独立评估。

### Option C — Add AppleDouble members to manifest（拒绝）

sidecar 不是产品内容；纳入 manifest 会固化 host-specific metadata。

### Option D — Ignore hidden members and continue（拒绝）

已知 archive 内容超出 manifest coverage，不能依赖较窄列表假装不存在。

## 7. Caps and stop conditions

```text
QWEN_DECISION_REVIEW_REQUESTS_MAX=1
GIT_FETCHES_MAX=1
DISPOSABLE_WORKTREES_MAX=1
NPM_CI_ATTEMPTS_MAX=1
NPM_LS_ATTEMPTS_MAX=1
SITE_TEST_ATTEMPTS_MAX=1
RELEASE_FORMAL_ATTEMPTS_MAX=1
CE_TEST_ATTEMPTS_MAX=1
PORTABLE_ARCHIVES_MAX=1
SERVER_READS=0
SERVER_WRITES=0
PUBLIC_SITE_REQUESTS=0
SSH_SESSIONS=0
DEPLOYMENTS=0
RELEASES=0
RETRIES=0
NETWORK_FALLBACKS=0
```

停止于任何 SHA/blob/source/Schema/test/binding drift；停止于 producer version/flag 不可用、
任意 `._*` member、unexpected special member、manifest coverage mismatch、第二 archive、
retry、fallback、source change、server 或 release 动作。

## 8. Recommendation review contract

exact `qwen3.7-max` 只允许一次 direct JSON review，必须返回：

```text
verdict
confidence
selected_option
would_recommend_to_agent_customer
root_cause_evidence_sufficient
explicit_metadata_suppression_sound
raw_member_contract_sound
manifest_file_count_contract_sound
same_source_rebuild_sound
history_preservation_sound
caps_and_stop_rules_sufficient
no_deployment_or_release_inference
authority_boundaries_preserved
blockers
corrections
rationale
```

qualifying：`RECOMMENDED`、Option A、confidence ≥ 0.80、全部 boolean true、空 blockers 和
corrections、returned model exact `qwen3.7-max`。

## 9. Non-authorizations

```text
RECOMMENDATION_NE_DECISION=true
PACKAGING_REMEDIATION_NE_SOURCE_CHANGE=true
ARCHIVE_PASS_NE_DEPLOYMENT=true
CURRENT_FAILURE_ARCHIVE_PRESERVED=true
PORTABLE_CANDIDATE_CREATED=false
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
