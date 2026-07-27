---
document_id: DBA-TITMAS-CE-G11B-STATIC-EXPORT-SEQUENCE-REMEDIATION-R5-R1-RECOMMENDATION-0.1
title: TITMAS CE-G11B Static Export Sequence Remediation R5-R1 Recommendation v0.1
version: 0.1.0
status: exact-recommendation-agent-review-pending-decision-pending
maturity: Development
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G11B Static Export Sequence Remediation R5-R1 Recommendation v0.1

## Recommendation

采用 **Option A：以新 artifact 保留 R5 的 test→public export→verify 最小修复，并用
修正后的同进程传值采集器完成一次新的 exact `qwen3.7-max` review**。

本建议不重发旧 R5 review，不把旧语义结果升级为合格审查，也不授权安装、export、
tests、PR mutation 或 merge。只有 R5-R1 review 同时证明 HTTP `200`、curl exit `0`、
exact returned model、direct JSON 和完整 contract，才可建立新的 R5 Decision。

## Bound evidence

```text
R4_RESULT_COMMIT=f16f09cc602be40137facce38cac35e5007bdcd7
R4_STATUS=FAIL_CLOSED_STATIC_EXPORT_ARTIFACT_ABSENT
R5_REVIEW_RECORD_COMMIT=9d10c8ba1af0bf6aad52fb0f15bee3bca2901fa0
R5_REVIEW_REQUESTS=1
R5_RETURNED_MODEL=qwen3.7-max
R5_DIRECT_JSON=true
R5_SEMANTIC_VERDICT=RECOMMENDED
R5_SELECTED_OPTION=A
R5_CONFIDENCE=1.0
R5_BLOCKERS=0
R5_CORRECTIONS=0
R5_QUALIFYING_REVIEW=false
R5_FAILURE=HTTP_STATUS_AND_CURL_EXIT_CAPTURE_GAP
```

旧语义结果只用于解释为何不改变实质方案，不是 authorization 或 qualifying evidence。

## R5-R1 substantive sequence

若未来独立 Decision 获批，只能在新的 disposable frozen merge-tree worktree 中：

1. 复核 topology、Draft PR #22、0 Actions、package/lock/export/verify hashes、empty
   status、absent `node_modules` 和 normalized npm prefix equality；
2. 执行一次
   `NPM_CONFIG_OFFLINE=true npm ci --offline --ignore-scripts --no-audit --no-fund`；
3. 成功后按顺序各一次执行：
   `npm ls --depth=0 --json` → `npm test` → `npm run export` →
   `npm run verify:static`；
4. 全部通过后 meta-validate 3 个 CE Schema，并运行精确 49 个 CE tests；
5. 对任何失败或 source/tree drift 失败关闭，不重试；
6. 删除 temporary worktree；network fallback、script mutation、PR mutation、workflow、
   merge、server action 和 deployment 均为 0。

## Review-capture remediation

R5-R1 write-ahead review 必须：

- 在请求前固化 artifact SHA 和 exact payload SHA；
- request count 恰好 1，requested model 恰好 `qwen3.7-max`；
- curl 完成后，在同一 shell process 中把实际 `curl_exit` 与 `http_status` 作为显式
  environment values 传给 sanitizer；
- sanitizer 记录 response byte count、response envelope SHA、envelope/direct JSON
  parse、returned model 和完整 review object；
- HTTP/curl 任一缺失、非 `200`/`0`、model 不等或 JSON/contract 不合格即失败关闭；
- 0 retry、fallback、substitution、alias inference、JSON repair；
- 不持久化 credential、raw request、raw response、hidden reasoning 或 usage。

## Options

- **Option A（推荐）**：新 R5-R1 artifact + 修正采集 + 一次 exact Max review。
- **Option B（拒绝）**：把旧 R5 semantic result 直接视为 qualifying。
- **Option C（拒绝）**：重新发送旧 artifact，覆盖旧失败记录。
- **Option D（拒绝）**：跳过 Recommendation review，直接执行或合并。

## Frozen technical inputs

```text
canonical_commit=ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
ce_commit=e032115adbe38cc84bde80cc9b10b96f6da1b428
merge_base=4c95f6b68c21e4bf6e9babb8bd1afa4977cd418a
merge_tree=ea296d8b2143aeb7cc220a81689ba4d057e4bb97
package_json_sha256=60dc7abf99a878f0e9dd24f0362d1ac7ad9c72a4d21578085fed39c526e3709b
package_lock_sha256=4f179b1107a3a3f18aa906ebd19f952a9a4d190b1ad7123cba0a6884e3a312fd
export_static_sha256=cd5cd0eef9b4a61f66cb866b3f96d16d5e95c28768ceda37633f454f3429a8bd
verify_static_sha256=8e26f3af1cba44184f2552969d67fba2983d84459d1e5cd1ab7a75f7436c089d
```

## Review gate

要求 exact `qwen3.7-max` 返回：

```text
verdict=RECOMMENDED
selected_option=A
r4_result_bound=true
r5_failure_preserved=true
old_semantic_result_not_elevated=true
new_artifact_boundary_clear=true
capture_remediation_sufficient=true
test_export_verify_order_required=true
single_offline_install_only=true
full_ce_validation_required=true
no_remote_mutation=true
merge_unauthorized=true
blocking_reasons=[]
required_corrections=[]
```

## Caps and non-claims

```text
R5_R1_RECOMMENDATION_REVIEW_REQUESTS_MAX=1
R5_OLD_REVIEW_RETRIES=0
NEW_DECISION_RECORDED=false
EXECUTION_AUTHORIZED=false
ACTUAL_INSTALLS=0
EXPORT_RUNS=0
SITE_TEST_RUNS=0
CE_TEST_RUNS=0
SITE_SOURCE_CHANGES=0
PR_MUTATIONS=0
MERGES=0
WORKFLOW_RUNS=0
DEPLOYMENTS=0
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
```
