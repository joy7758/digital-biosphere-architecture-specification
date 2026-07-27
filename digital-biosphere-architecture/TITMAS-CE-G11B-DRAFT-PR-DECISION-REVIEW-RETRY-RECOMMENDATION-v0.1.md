---
document_id: DBA-TITMAS-CE-G11B-DRAFT-PR-DECISION-REVIEW-RETRY-RECOMMENDATION-0.1
title: TITMAS CE-G11B Draft PR Decision Review Retry Recommendation v0.1
title_zh: TITMAS CE-G11B Draft PR 决策审查重试建议 v0.1
version: 0.1.0
status: exact-recommendation-agent-review-pending-decision-pending
maturity: Development
maturity_scope: ce-g11b-draft-pr-decision-review-retry
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G11B Draft PR Decision Review Retry Recommendation v0.1

## 1. Recommendation

建议采用 **Option A：建立新的 Decision candidate `CE-G11B-PR-A-R1`，授权一次采用
write-ahead persistence（预写持久化）的 `qwen3.7-max` Decision review**。

旧 Decision candidate 和旧 review attempt 保持失败关闭，不得重试或追溯改写。新
Recommendation 只解决审查结果持久化可靠性，不授权 PR 创建、merge、run request、
workflow、Phase B 或 deployment。

## 2. Exact failure

[Failure record](TITMAS-COMMERCIAL-EVALUATION-CE-G11B-DRAFT-PR-QWEN-DECISION-REVIEW-FAILURE-v0.1.json)
已远端固化：

```text
failure_baseline_commit=a7e0f967fbcc6cc3a492253830fcff55104f4aed
status=NON_QUALIFYING_REVIEW_ATTEMPT
terminal_failure_category=NO_SANITIZED_MODEL_RESULT_AVAILABLE
requested_model=qwen3.7-max
request_count=1
retry_count=0
returned_model=UNKNOWN
http_status=UNKNOWN
direct_json_parse_pass=false
decision_authorized=false
draft_pr_created=false
```

现有证据不能区分 provider transport、response envelope、JSON contract、process
termination 或 local persistence failure，因此不得把根因写成模型故障、供应商故障或
网络故障。

## 3. Options

### Option A — New Decision + write-ahead single attempt（推荐）

建立新的独立 Decision：

- 新 Decision ID 为 `TITMAS-COMMERCIAL-EVALUATION-CE-G11B-PR-A-R1`；
- 旧 Decision 保持 `NOT_AUTHORIZED_DECISION_REVIEW_NON_QUALIFYING`；
- 允许新 Decision review 恰好 1 次 `qwen3.7-max` request；
- request 前先原子写入 sanitized attempt record；
- response 后先记录 HTTP status、body hash 和 returned model observation，再解析正文；
- 任一异常都能形成 terminal sanitized record；
- 不允许 retry、fallback、model substitution、alias inference 或 JSON repair request。

### Option B — Retry the failed Decision candidate（禁止）

旧 candidate 已消耗一次审查请求且结果不可验证；在原 Decision 下直接重试会绕过失败
关闭和 request accounting。

### Option C — Downgrade or substitute model（禁止）

不得切换到 `qwen3.7-plus`、其他 provider 或 alias。用户要求当前商业化标准工作使用
已直接验证的 `qwen3.7-max`，且不得静默降级。

### Option D — Proceed without qualifying review（禁止）

没有 exact returned model identity、verdict、blockers 和 corrections，不能授权 Draft
PR 创建。

## 4. Write-ahead review protocol

新 Decision 应固定以下顺序：

### Step 1 — Prepare exact bytes

计算：

```text
decision_source_sha256
request_payload_sha256
requested_model=qwen3.7-max
request_cap=1
```

不得把 credential 写入 payload record。

### Step 2 — Persist STARTED record before network

在一次 HTTP attempt 前，原子写入 sanitized record：

```json
{
  "status": "STARTED",
  "request_count": 1,
  "requested_model": "qwen3.7-max",
  "decision_source_sha256": "<sha256>",
  "request_payload_sha256": "<sha256>",
  "credential_persisted": false
}
```

如果进程在后续任意阶段停止，该 STARTED record 必须保留并被解释为
`NON_QUALIFYING_INCOMPLETE_ATTEMPT`，不得重试。

### Step 3 — One HTTP attempt

只允许一次 request：

```text
retry=0
fallback=0
model_substitution=0
alias_inference=0
json_repair_request=0
```

### Step 4 — Persist transport observation before content qualification

收到响应后先记录：

- HTTP status；
- response byte count；
- response envelope SHA-256；
- envelope JSON parse pass/fail；
- returned model observation（可用时）；
- returned model equals requested；
- raw envelope persisted=false；
- provider error body persisted=false。

随后才解析 `choices[0].message.content` 和 strict review JSON。

### Step 5 — Atomically finalize

最终 record 只能进入：

```text
QUALIFYING_REVIEW_COMPLETED
NON_QUALIFYING_HTTP_FAILURE
NON_QUALIFYING_ENVELOPE_FAILURE
NON_QUALIFYING_MODEL_IDENTITY_FAILURE
NON_QUALIFYING_DIRECT_JSON_FAILURE
NON_QUALIFYING_CONTRACT_FAILURE
NON_QUALIFYING_INCOMPLETE_ATTEMPT
```

只在 exact `qwen3.7-max`、HTTP 200、direct JSON、contract pass、`APPROVE`、0 blockers、
0 corrections 全部满足时，新的 Decision 才可生效。

## 5. Frozen PR scope remains unchanged

修复不改变：

```text
repository=joy7758/digital-biosphere-architecture-specification
base=codex/production-observability-baseline
base_commit=4c95f6b68c21e4bf6e9babb8bd1afa4977cd418a
head=codex/ce-g11b-phase-a-decision
head_commit=e032115adbe38cc84bde80cc9b10b96f6da1b428
merge_base=4c95f6b68c21e4bf6e9babb8bd1afa4977cd418a
site_paths=0
draft=true
auto_merge=false
merge_authorized=false
valid_run_request_created=false
workflow_runs=0
phase_b_authorized=false
```

若 topology 漂移，必须停止并重新准备 Recommendation。

## 6. Agent-customer recommendation gate

待 `qwen3.7-max` 使用本 Recommendation 定义的 write-ahead protocol，对本文件 exact
bytes 完成一次 independent review 后填写：

```text
PRIMARY_REVIEW_MODEL=qwen3.7-max
REVIEW_VERDICT=PENDING
SELECTED_OPTION=PENDING
WOULD_RECOMMEND_TO_AGENT_CUSTOMER=PENDING
CONFIDENCE=PENDING
BLOCKING_REASONS=PENDING
REQUIRED_CORRECTIONS=PENDING
```

该 Recommendation review 与未来 Decision review 是两个不同治理阶段，均不产生
Authority。

## 7. Caps and stop conditions

```text
RECOMMENDATION_REVIEW_REQUESTS_MAX=1
NEW_DECISION_RECORDED=false
NEW_DECISION_REVIEW_REQUESTS_AUTHORIZED=0
DRAFT_PR_CREATION_AUTHORIZED=false
DRAFT_PR_CREATED=false
PR_MERGES=0
VALID_RUN_REQUESTS_CREATED=0
WORKFLOW_RUNS=0
SITE_PATHS_INCLUDED=0
DEPLOYMENTS=0
DBOS_CHANGES=0
SAEE_CHANGES=0
```

立即停止：

- write-ahead STARTED record 未在请求前形成；
- request cap、model identity 或 persistence order 漂移；
- 需要 retry、fallback、substitution、alias 或 JSON repair request；
- provider/raw envelope、credential、hidden reasoning 或 error body 被写入仓库；
- base/head/merge-base/site path/workflow count 漂移；
- 结果被描述为 PR authorization、merge approval、Phase B authorization、Production、
  Certification、SLA 或 Commercial Offering。

## 8. Non-claims and next gate

```text
RECOMMENDATION_PREPARED=true
OLD_DECISION_REVIEW_FAILURE_PRESERVED=true
OLD_DECISION_AUTHORIZED=false
NEW_DECISION_RECORDED=false
NEW_DECISION_AUTHORIZED=false
DRAFT_PR_CREATED=false
MERGED=false
VALID_RUN_REQUEST_CREATED=false
WORKFLOW_RUNS=0
PHASE_B_AUTHORIZED=false
PRODUCTION_READY=false
CERTIFICATION=false
SLA=false
COMMERCIAL_OFFERING=false
```

下一步只允许一次 `qwen3.7-max` Recommendation review。审查通过后，才可依据 standing
directive 建立新的 `CE-G11B-PR-A-R1` Decision。
