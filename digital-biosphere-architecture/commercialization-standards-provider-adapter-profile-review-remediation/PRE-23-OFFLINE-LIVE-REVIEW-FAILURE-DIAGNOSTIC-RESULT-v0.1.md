---
document_id: DBA-TITMAS-CS-D02-PRE-23-OFFLINE-LIVE-REVIEW-FAILURE-DIAGNOSTIC-RESULT-0.1
title: TITMAS CS-D02 PRE-23 Offline Live Review Failure Diagnostic Result v0.1
title_zh: TITMAS CS-D02 PRE-23 实时评审失败离线诊断结果 v0.1
version: 0.1.0
status: offline-diagnostic-pass-contract-candidates-not-adopted
maturity: Development
decision_reference: CS-D02-PRE-23
offline_failure_diagnostic_pass: true
live_rerun_ready: false
profile_review_completed: false
profile_adopted: false
---

# TITMAS CS-D02 PRE-23 Offline Live Review Failure Diagnostic Result v0.1

## Result

PRE-23 在远端授权基线后完成一次零网络失败诊断：

```text
INPUT_HASHES_MATCHED=9/9
CANDIDATE_SCHEMAS_META_VALID=3/3
FIXTURE_EXPECTATIONS_MATCHED=15/15
EXTRACTION_CASES_MATCHED=10/10
MODEL_BINDING_CASES_MATCHED=5/5
POSITIVE_CASES_MATCHED=8/8
NEGATIVE_CASES_MATCHED=7/7

LIVE_MODEL_REQUESTS_EXECUTED=0
PROVIDER_NETWORK_REQUESTS_EXECUTED=0
RETRY_ATTEMPTS=0
FALLBACK_ATTEMPTS=0
JSON_REPAIR_ATTEMPTS=0

OFFLINE_FAILURE_DIAGNOSTIC_PASS=true
CONTRACT_CANDIDATES_ADOPTED=false
IMPLEMENTATION_CREATED=false
LIVE_RERUN_READY=false
```

## Kimi Extraction Diagnosis

PRE-22 caller 对 installed tool `content[].text` 进行了 JSON parse，但若该 text 本身就是
compact response object，caller 随后仍只寻找 wrapper `answer` 字段，导致已经解析出的
semantic object 被丢弃。

诊断分类：

```text
ROOT_CAUSE=PLAIN_JSON_RESPONSE_OBJECT_MISCLASSIFIED_AND_DISCARDED_BY_CALLER
EXACT_PRE22_KIMI_ANSWER_RECOVERED=false
PROVIDER_NO_ANSWER_PROVEN=false
```

由于 isolate 已结束且 raw tool result 未保存，PRE-23 不恢复或猜测当次 answer。

新 extraction contract candidate 要求：

- structured `answer`、direct `answer`、JSON wrapper、direct response object 和 provider
  declared plain content 分开识别；
- direct response object 必须通过 frozen response Schema；
- 多位置内容相同可以去重，不同必须 `CONFLICTING_ANSWER_LOCATIONS`；
- 不 strip Markdown/code fence，不 repair JSON，不 semantic rewrite。

## DeepSeek Model-Binding Diagnosis

PRE-22 的 content JSON 和 response Schema 均通过，但：

```text
REQUESTED_MODEL=deepseek-chat
RETURNED_MODEL=deepseek-v4-flash
CURRENT_ALIAS_RECORDS=0
MODEL_BINDING=MISMATCH
```

新 model-binding policy candidate 只允许：

- byte-for-byte 相同 → `EXACT_MATCH`；
- exact provider source/version + alias scope + 独立 Decision → `EXPLICIT_ALIAS_MATCH`；
- 未采纳 alias → `MISMATCH`；
- returned model 缺失 → `UNKNOWN`。

content PASS 不能覆盖 `MISMATCH`。

## Fixture Coverage

15 个 synthetic case 覆盖：

- structured/direct/wrapper/direct-object/plain-text extraction；
- identical dedup、conflict、missing、non-string 和 Schema mismatch；
- exact model、explicit adopted alias、unadopted alias、missing returned model；
- DeepSeek content PASS + model mismatch。

全部按冻结预期匹配。Fixture PASS 不是 provider evidence、review completion、Profile adoption
或 implementation。

## Next Permitted Action

```text
PREPARE_SEPARATE_PRE22_FAILURE_CONTRACT_ADOPTION_REVIEW_RECOMMENDATION_ONLY
```

在 extraction contract 和 model-binding policy 经独立审查、Decision 与 implementation
validation 之前，不准备新的 live rerun。
