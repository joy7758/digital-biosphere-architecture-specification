---
document_id: DBA-TITMAS-CE-G11B-ZERO-INSTALL-NPM-CWD-DIAGNOSTIC-DECISION-REVIEW-RETRY-RECOMMENDATION-0.1
title: TITMAS CE-G11B Zero-install npm CWD Diagnostic Decision Review Retry Recommendation v0.1
version: 0.1.0
status: exact-recommendation-agent-review-pending-decision-pending
maturity: Development
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G11B Zero-install npm CWD Diagnostic Decision Review Retry Recommendation v0.1

## Recommendation

采用 **Option A：保留旧 Decision review failure，建立新的 R2 Decision candidate，并用
write-ahead persistence 执行一次新的 exact `qwen3.7-max` Decision review**。

本 Recommendation 不授权复用或重试旧 Decision，不授权 dry-run、真实安装、site tests、
PR mutation、merge、workflow、server action 或 deployment。

## Preserved failure

远端 commit `22a8d4111bc4d2c7c4837d2d8f789e40a380ce37` 固化：

```text
failure_reference=TITMAS-COMMERCIAL-EVALUATION-CE-G11B-ZERO-INSTALL-NPM-CWD-DIAGNOSTIC-QWEN-DECISION-REVIEW-FAILURE-v0.1.json
old_decision_id=TITMAS-COMMERCIAL-EVALUATION-CE-G11B-ZERO-INSTALL-NPM-CWD-DIAGNOSTIC-R1
old_decision_source_sha256=3be57ae217875b887b88a470ed0166e4c980630c1ce8a898a4722e8d4d5517bd
requested_model=qwen3.7-max
provider_request_count=1
retry_count=0
returned_model=UNKNOWN
http_status=UNKNOWN
verdict=UNKNOWN
qualifying_review=false
dry_run_executed=false
```

一次本地 Node module-format preflight 在 `fetch` 之前失败，不消耗 provider request；
修正后的单次进程已消耗一个 provider request，但没有可持久化的 sanitized result。现有
证据不能区分 provider transport、response capture、process termination 或 tool-output
delivery failure，根因保持 `UNKNOWN`。

## Options

### Option A — New R2 Decision plus write-ahead review（推荐）

- 新 Decision ID 必须是
  `TITMAS-COMMERCIAL-EVALUATION-CE-G11B-ZERO-INSTALL-NPM-CWD-DIAGNOSTIC-R2`；
- R1 Decision 和 review failure 保持不变，不得重试或追溯改写；
- R2 Decision review 最多 1 次 exact `qwen3.7-max` request；
- 请求前必须持久化 sanitized `STARTED` record；
- 传输返回后必须先持久化 HTTP/model/hash observation，再解析 review JSON；
- 不允许 retry、fallback、model substitution、alias inference 或 JSON repair request；
- 只有 HTTP 200、returned model exact、direct JSON、contract pass、`APPROVE`、
  0 blocker 和 0 correction 同时满足，R2 Decision 才可生效。

### Option B — Retry R1（禁止）

R1 已消耗 request cap 且结果不可验证；直接重试会破坏 request accounting。

### Option C — Proceed without review（禁止）

UNKNOWN 不是 APPROVE，不能授权 dry-run。

### Option D — Downgrade or substitute model（禁止）

不得改用其他 Qwen 型号、其他 provider 或 alias。

## Write-ahead review protocol

对本 Recommendation review 和后续 R2 Decision review，分别执行：

1. 计算 exact source SHA-256 与 request payload SHA-256；
2. 在任何网络动作前，用 `apply_patch` 持久化不含 credential 的 `STARTED` record；
3. 发送恰好 1 次 request，`retry=0`、`fallback=0`、`substitution=0`；
4. 直接捕获 command exit、HTTP status、response byte count、envelope hash 和 returned
   model；不持久化 raw envelope、provider error body、credential 或 hidden reasoning；
5. 只有 direct JSON 和 frozen review contract 均通过时写入 sanitized review；
6. 若进程、tool output 或 parsing 失败，保留 `STARTED` record 并解释为
   `NON_QUALIFYING_INCOMPLETE_ATTEMPT`，不得在同一 candidate 下重试。

## Frozen diagnostic scope

R2 不得扩大 R1 的技术范围：

```text
canonical_commit=ccf473f3ea29d5f58326e5b3bf0f57e3536ddd14
ce_commit=e032115adbe38cc84bde80cc9b10b96f6da1b428
merge_base=4c95f6b68c21e4bf6e9babb8bd1afa4977cd418a
merge_tree=ea296d8b2143aeb7cc220a81689ba4d057e4bb97
draft_pr=22
draft_pr_state=OPEN_DRAFT
ce_head_actions_runs=0
package_json_sha256=60dc7abf99a878f0e9dd24f0362d1ac7ad9c72a4d21578085fed39c526e3709b
package_lock_sha256=4f179b1107a3a3f18aa906ebd19f952a9a4d190b1ad7123cba0a6884e3a312fd
process_cwd=digital-biosphere-architecture/site
command=NPM_CONFIG_OFFLINE=true npm ci --dry-run --offline --ignore-scripts --no-audit --no-fund
attempts=1
actual_install=0
dependency_materialization=0
network_fallback=0
site_tests=0
site_source_changes=0
pr_mutations=0
merges=0
workflow_runs=0
deployments=0
```

任何 commit、tree、PR、Actions 或 hash 漂移都要求停止并重新形成 Recommendation。

## Review gate

本 Recommendation 只在 exact `qwen3.7-max` 返回以下结果时通过：

```text
verdict=RECOMMENDED
selected_option=A
old_failure_preserved=true
unknown_root_cause_preserved=true
new_decision_required=true
write_ahead_protocol_coherent=true
single_new_attempt_only=true
no_retry_or_downgrade=true
diagnostic_scope_unchanged=true
dry_run_unauthorized=true
merge_unauthorized=true
blocking_reasons=[]
required_corrections=[]
```

## Non-claims

```text
RECOMMENDATION_PREPARED=true
OLD_DECISION_REVIEW_FAILURE_PRESERVED=true
OLD_DECISION_AUTHORIZED=false
NEW_DECISION_RECORDED=false
NEW_DECISION_AUTHORIZED=false
DRY_RUN_AUTHORIZED=false
DRY_RUN_EXECUTED=false
ACTUAL_INSTALL_AUTHORIZED=false
SITE_TESTS_AUTHORIZED=false
MERGE_AUTHORIZED=false
PHASE_B_AUTHORIZED=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
```
