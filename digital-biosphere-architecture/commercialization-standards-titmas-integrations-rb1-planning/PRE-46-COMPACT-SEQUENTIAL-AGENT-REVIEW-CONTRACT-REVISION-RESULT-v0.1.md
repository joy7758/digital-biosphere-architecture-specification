---
document_id: DBA-TITMAS-INTEGRATIONS-PRE46-COMPACT-SEQUENTIAL-AGENT-REVIEW-CONTRACT-REVISION-RESULT-0.1
title: TITMAS Integrations PRE-46 Compact Sequential Agent Review Contract Revision Result v0.1
title_zh: TITMAS Integrations PRE-46 精简顺序式智能体评审契约修订结果 v0.1
version: 0.1.0
status: pass-offline-contract-revision-pre47-recommendation-allowed
decision_reference: CS-D02-PRE-46
source_commit: 032c8e5b83d75496bfd4eeb60edaaea37e780f56
network_requests: 0
implementation_authorized: false
---

# TITMAS Integrations PRE-46 Compact Sequential Agent Review Contract Revision Result v0.1

## Result

```text
PRE46_OFFLINE_CONTRACT_REVISION_PASS=true
INPUT_HASHES_MATCH=13/13
SCHEMAS_VALID=9/9
INSTANCES_VALID=8/8
OFFLINE_FIXTURES_PASS=6/6
NETWORK_REQUESTS=0
MODEL_REQUESTS=0
CREDENTIAL_READS=0
RAW_PROVIDER_ENVELOPES_ACCESSED=0
PRE44_AGENT_RECOMMENDATION_GATE_PASS=false
RB1_IMPLEMENTATION_RECOMMENDATION_ALLOWED=false
RB1_IMPLEMENTATION_AUTHORIZED=false
```

PRE-46 已离线证明新的 review contract 在自身声明范围内结构一致，并能在不做 JSON 修复
的情况下接受一个合法对象、拒绝五个非法响应形态。它没有重新执行 PRE-44，也没有改变
PRE-44 的 `1/4 qualifying` 和 `BLOCKED` 结果。

## Contract Delta

| control | PRE-44 | PRE-46 | result |
|---|---:|---:|---|
| query template bytes | 4716 | 2516 | reduced |
| top-level required fields | 15 | 13 | reduced |
| future parallel requests | 4 | 1 | sequential isolation |
| qualifying threshold | 3/4 | 3/4 | unchanged |
| retry / fallback / repair | 0 | 0 | unchanged |
| Authority boundary acknowledgements | 6 | 6 | unchanged |

精简没有通过降低门槛实现。长数组与重复说明被压缩为一个 `reason`、一个
`top_blocker` 和一个 `required_correction`；六个 boundary checks 仍全部为常量
`true`。

## Fixture Result

| case | expected | observed |
|---|---|---|
| `PRE46-FX-001` direct valid JSON | accept | `PASS` |
| `PRE46-FX-002` prose wrapper | reject parse | `PASS` |
| `PRE46-FX-003` code fence | reject parse | `PASS` |
| `PRE46-FX-004` additional property | reject Schema | `PASS` |
| `PRE46-FX-005` boundary false | reject boundary | `PASS` |
| `PRE46-FX-006` missing required field | reject Schema | `PASS` |

```text
MARKDOWN_STRIP_ATTEMPTS=0
CODE_FENCE_STRIP_ATTEMPTS=0
JSON_REPAIR_ATTEMPTS=0
SEMANTIC_REWRITE_ATTEMPTS=0
```

## Official Structured-output Finding

百度千帆官方文档确认通用 Chat Completions API 有 `response_format`，但 structured-output
指南明确只有部分模型支持，并没有把 exact `glm-5.2` 或 `kimi-k2.6` 列入公开支持范围。

因此当前 contract 保持：

```text
GLM_5_2_JSON_SCHEMA_SUPPORT=UNKNOWN_NOT_ADOPTED
KIMI_K2_6_JSON_SCHEMA_SUPPORT=UNKNOWN_NOT_ADOPTED
RESPONSE_FORMAT_PARAMETER_INCLUDED=false
```

这不是“不支持”的永久结论，也不是 Provider correctness 评价。

## What This Pass Means

PRE-46 `PASS` 只表示：

- compact query/response candidate 可离线解析和验证；
- future four-session order 明确为 sequential；
- 原阈值、安全边界和失败保留没有降低；
- 可以形成一个独立 PRE-47 exact network-review Recommendation。

## What This Pass Does Not Mean

```text
PRE47_NETWORK_REVIEW_AUTHORIZED=false
CONTRACT_ADOPTED_FOR_NETWORK=false
MODEL_CONTRACT_COMPLIANCE_PROVEN=false
PROVIDER_SUPPORT_PROVEN=false
RB1_IMPLEMENTATION_RECOMMENDATION_ALLOWED=false
RB1_IMPLEMENTATION_AUTHORIZED=false
TARGET_REPOSITORY_MODIFIED=false
PACKAGE_CREATED=false
SOURCE_CREATED=false
TESTS_CREATED=false
CONFORMANCE_EXECUTED=false
RUNTIME_CREATED=false
RELEASE_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
```

## Next Gate

```text
NEXT_ACTION=FORM_PRE47_EXACT_SEQUENTIAL_AGENT_REVIEW_RECOMMENDATION_ONLY
```

PRE-47 必须重新冻结 exact commit、query composition、payload、session order、timeout、
credential read、sanitized sink 和阈值，并获得独立 Decision。PRE-46 本身不允许发送任何
模型请求。

Canonical machine record：

- [`result`](pre46-contract-revision-result.v0.1.json)
- [`execution receipt`](pre46-contract-revision-execution-receipt.v0.1.json)
