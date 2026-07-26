---
document_id: DBA-TITMAS-CS-D02-PRE-29-PROVIDER-TRANSPORT-PHASE-DIAGNOSTIC-DECISION-0.1
title: TITMAS CS-D02 PRE-29 Provider Transport Phase Diagnostic Decision Record v0.1
title_zh: TITMAS CS-D02 PRE-29 Provider 传输阶段诊断决定记录 v0.1
version: 0.1.0
status: authorized-bounded-zero-http-zero-model-transport-diagnostic-only
maturity: Development
decision_id: CS-D02-PRE-29
standing_directive_reference: TITMAS-CS-STANDING-001
decided_by_ref: zhangbin
network_probe_authorized: true
http_request_authorized: false
live_model_request_authorized: false
implementation_authorized: false
---

# TITMAS CS-D02 PRE-29 Provider Transport Phase Diagnostic Decision Record v0.1

## Decision

依据 `TITMAS-CS-STANDING-001` 和远端验证的 PRE-29 exact recommendation，采用：

```text
DECISION_RESULT=AUTHORIZE_BOUNDED_PRE28_PROVIDER_TRANSPORT_PHASE_DIAGNOSTIC_WITH_ZERO_HTTP_AND_MODEL_REQUESTS_ONLY
DECIDED_BY_REF=zhangbin
TARGET_HOST=qianfan.baidubce.com
TARGET_PORT=443
DNS_RESOLUTION_ATTEMPTS_MAX=1
TCP_CONNECT_ATTEMPTS_MAX=1
TLS_HANDSHAKE_ATTEMPTS_MAX=1
TOTAL_EXTERNAL_NETWORK_PROBES_MAX=3
HTTP_REQUESTS_MAX=0
PROVIDER_API_REQUESTS_MAX=0
LIVE_MODEL_REQUESTS_MAX=0
CREDENTIAL_READS_MAX=0
RETRY_ATTEMPTS_MAX=0
FALLBACK_ATTEMPTS_MAX=0
ENDPOINT_MUTATIONS_MAX=0
IMPLEMENTATION_AUTHORIZED=false
```

## Scope

只授权：

- 复核 PRE-29 推荐中的六个冻结来源哈希；
- 对冻结 host/port 依序进行一次 DNS resolution、一次 TCP connect 和一次 TLS handshake；
- 只有前一阶段通过时才执行后一阶段；
- TCP connect 后不发送应用层字节并立即关闭；
- TLS handshake 使用冻结的 SNI 和系统 trust store，完成后不发送 HTTP 字节并立即关闭；
- 将 sanitized phase result 原子提交到预先冻结的唯一临时 sink；
- 仅保留 elapsed time、状态、sanitized failure category、地址数量、TLS version、证书字段
  单向摘要、证书有效期和 hostname verification 结果。

## Authority Boundary

- transport observation 不是 Provider、Model、API 或 Contract conformance；
- DNS/TCP/TLS 全部通过也不能断言 PRE-28 是 HTTP read timeout；
- 不读取 `QIANFAN_API_KEY`，不创建 Authorization header；
- 不发送 HTTP method、path、headers 或 body；
- 不允许 retry、fallback、第二地址探测、代理切换或 endpoint mutation；
- PRE-26 与 PRE-28 request budget 保持关闭；
- 不授权 model retry、contract adoption、implementation、offering、certification 或 release。

## Preconditions

执行 network probe 前必须全部成立：

1. recommendation、Decision、plan 和 Schema 在目标远端；
2. 六个 source hash 全部匹配；
3. 全新 `0700` 临时根与唯一 result target preflight 通过；
4. authorization receipt 已提交并远端验证；
5. PRE-29 network probe accounting 为 0；
6. HTTP、provider API、model request、credential read 和 Authorization header accounting 为 0。

## Stop Conditions

source/hash、host、port、phase order 或 timeout 漂移；需要 credential、HTTP bytes、provider
API request、重试、第二地址、代理、endpoint mutation；临时 target 预先存在或为 symlink；
raw payload、packet capture、resolver private configuration 或敏感本机网络标识将被持久化；
结果无法原子提交或发生任何语义抬升时立即失败关闭。

## Effects

```text
AUTHORITY_CHANGED=false
OWNERSHIP_CHANGED=false
PRE28_RESULT_CHANGED=false
PRE28_REQUEST_BUDGET_REOPENED=false
MODEL_RETRY_AUTHORIZED=false
HANDOFF_CONTRACT_ADOPTED=false
V0_2_CONTRACT_CANDIDATES_ADOPTED=false
ADAPTER_IMPLEMENTATION_CREATED=false
PROVIDER_SUPPORTED=false
CONFORMANCE_EXECUTED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
IMPLEMENTATION_AUTHORIZED=false
EXTERNAL_OUTREACH_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

本 Decision 只形成有界 transport diagnostic 授权。任何 network probe 仍须等待本 Decision
基线和包含精确临时目标的 authorization receipt 均在目标远端验证。
