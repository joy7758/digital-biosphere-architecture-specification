---
document_id: DBA-TITMAS-CS-D02-PRE-29-PROVIDER-TRANSPORT-PHASE-DIAGNOSTIC-RESULT-REPORT-0.1
title: TITMAS CS-D02 PRE-29 Provider Transport Phase Diagnostic Result v0.1
title_zh: TITMAS CS-D02 PRE-29 Provider 传输阶段诊断结果 v0.1
version: 0.1.0
status: executed-lower-layer-reachable-timeout-phase-unresolved
maturity: Development
decision_reference: CS-D02-PRE-29
network_probes_executed: 3
http_requests_executed: 0
live_model_requests_executed: 0
model_retry_authorized: false
---

# TITMAS CS-D02 PRE-29 Provider Transport Phase Diagnostic Result v0.1

## 1. Result

PRE-29 已按
[Decision](../TITMAS-CS-D02-PRE-29-PROVIDER-TRANSPORT-PHASE-DIAGNOSTIC-DECISION-RECORD.md)、
[authorization receipt](transport-phase-diagnostic-authorization-receipt.v0.1.json) 和冻结计划
执行。机器结果与执行回执：

- [sanitized result](transport-phase-diagnostic-result.v0.1.json)；
- [execution receipt](transport-phase-diagnostic-execution-receipt.v0.1.json)。

```text
PRE29_STATUS=PASS_LOWER_LAYER_REACHABLE
PRE29_DNS_STATUS=PASS
PRE29_TCP_STATUS=PASS
PRE29_TLS_STATUS=PASS
PRE29_TOTAL_EXTERNAL_NETWORK_PROBES_EXECUTED=3
PRE29_APPLICATION_BYTES_SENT=0
PRE29_HTTP_REQUESTS_EXECUTED=0
PRE29_PROVIDER_API_REQUESTS_EXECUTED=0
PRE29_LIVE_MODEL_REQUESTS_EXECUTED=0
PRE29_CREDENTIAL_READS_EXECUTED=0
PRE29_RETRY_ATTEMPTS=0
```

## 2. Phase Observations

| phase | result | sanitized observation |
|---|---|---|
| DNS | `PASS` | 2 个唯一 address candidate；elapsed `4.766 ms` |
| TCP | `PASS` | 对冻结的第一个 address candidate 完成一次 `443` connect；elapsed `0.293 ms`；随后关闭 |
| TLS | `PASS` | SNI 与 hostname verification 通过；TLS `TLSv1.2`；elapsed `201.41 ms`；随后关闭且未发送 HTTP bytes |

证书 subject 与 issuer 只保留 one-way digest；没有持久化 raw certificate、IP address、
resolver private configuration、packet capture、HTTP payload、credential 或 Authorization
header。

## 3. Allowed Interpretation

本次结果只允许：

> 当前执行环境在 `2026-07-27T01:10:52+08:00` 对
> `qianfan.baidubce.com:443` 的 DNS、TCP 和经过系统 trust store 验证的 TLS 基础传输
> 观察均通过。

它缩小了后续诊断范围，但不能回溯证明 PRE-28 timeout 的确切阶段：

```text
PRE28_TIMEOUT_PHASE=NOT_RESOLVED_BY_LOWER_LAYER_PROBE
```

## 4. Prohibited Interpretation

不得由本结果推导：

- Qianfan provider、API 或目标模型可用；
- PRE-28 必然是 HTTP response read timeout；
- PRE-28 request contract 正确；
- `kimi-k2.6` 或 `glm-5.2` 存在、可访问或符合 exact binding；
- 允许重试 PRE-28 或重新打开 PRE-26/PRE-28 request budget；
- handoff contract 或 v0.2 contract candidates 已被审查或采纳；
- conformance、implementation、certification、market/customer proof 或 `CS-G0 PASS`。

## 5. Boundary Verification

```text
SOURCE_HASHES_MATCH=6/6
DECISION_BASELINE_REMOTE_VERIFIED=true
AUTHORIZATION_RECEIPT_REMOTE_VERIFIED=true
SANITIZED_RESULT_SCHEMA_PASS=true
SANITIZED_RESULT_ATOMICALLY_COMMITTED=true
TEMPORARY_RESULT_CONSUMED=true
TEMPORARY_ROOT_REMOVED=true

MODEL_RETRY_AUTHORIZED=false
HANDOFF_CONTRACT_ADOPTED=false
V0_2_CONTRACT_CANDIDATES_ADOPTED=false
ADAPTER_IMPLEMENTATION_CREATED=false
PROVIDER_SUPPORTED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
```

## 6. Next Gate

基础传输层当次可达，而 PRE-28 在收到 HTTP response 前超时。下一步不应重试模型；只能
先形成一个新的、独立的 offline instrumentation recommendation，用于设计未来 request
phase accounting：

```text
DNS
-> TCP
-> TLS
-> HTTP_REQUEST_WRITE
-> HTTP_RESPONSE_HEADERS
-> HTTP_RESPONSE_BODY
```

该后续工作应保持 provider/model requests、credential reads 和 network probes 为 0，只
定义可审计的 phase timing/failure contract。任何未来 live confirmation 仍需新的 exact
recommendation、Decision、请求预算与远端 authorization baseline。
