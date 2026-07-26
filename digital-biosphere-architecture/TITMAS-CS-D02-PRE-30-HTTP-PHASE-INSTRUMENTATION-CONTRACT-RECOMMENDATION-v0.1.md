---
document_id: DBA-TITMAS-CS-D02-PRE-30-HTTP-PHASE-INSTRUMENTATION-CONTRACT-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-30 HTTP Phase Instrumentation Contract Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-30 HTTP 阶段可观测契约建议 v0.1
version: 0.1.0
status: exact-offline-instrumentation-contract-recommendation-not-decided
maturity: Development
decision_reference: CS-D02-PRE-30
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
network_probe_authorized: false
http_request_authorized: false
live_model_request_authorized: false
implementation_authorized: false
---

# TITMAS CS-D02 PRE-30 HTTP Phase Instrumentation Contract Recommendation v0.1

## 1. Why PRE-30 Exists

PRE-28 两个 provider network request 均在观察到 HTTP response 之前出现 `TimeoutError`。
PRE-29 随后在同一执行环境中观察到 DNS、TCP 和 TLS 全部通过：

```text
PRE29_STATUS=PASS_LOWER_LAYER_REACHABLE
PRE29_DNS_STATUS=PASS
PRE29_TCP_STATUS=PASS
PRE29_TLS_STATUS=PASS
PRE29_HTTP_REQUESTS_EXECUTED=0
PRE29_LIVE_MODEL_REQUESTS_EXECUTED=0
```

PRE-29 只证明当次基础传输可达，不能回溯定位 PRE-28 timeout。当前缺口不是再次请求，
而是未来执行需要一个可审计的 request phase instrumentation contract（请求阶段可观测
契约），把 connect、write、response headers、response body、parse 和 handoff 分开。

## 2. Agent Recommendation Gate

如果潜在 Agent 客户现在询问是否应直接重试 PRE-28：

```text
RECOMMEND_MODEL_REQUEST_RETRY=NO
REASON=HTTP_PHASE_ACCOUNTING_NOT_DEFINED
RECOMMEND_OFFLINE_INSTRUMENTATION_CONTRACT_DESIGN=YES
RECOMMEND_PROVIDER_OR_CONTRACT_ADOPTION_NOW=NO
```

不推荐重试的原因：

1. PRE-28 请求预算已关闭；
2. PRE-29 没有发送 HTTP，也没有证明 API/model availability；
3. 当前 caller 只保留单一 `TimeoutError`，无法区分 write、headers 或 body read；
4. 未定义 phase start/end、timeout ownership、partial response 和 sanitized failure semantics；
5. `VALID_PROBLEM_RECORDS=0` 且 `CS_G0_PASS=false`。

## 3. Exact Recommendation

```text
RECOMMENDED_OPTION=AUTHORIZE_OFFLINE_PRE28_HTTP_PHASE_INSTRUMENTATION_CONTRACT_CANDIDATE_DESIGN_ONLY
PRIMARY_REPOSITORY=digital-biosphere-architecture
NETWORK_PROBES_MAX=0
HTTP_REQUESTS_MAX=0
PROVIDER_API_REQUESTS_MAX=0
LIVE_MODEL_REQUESTS_MAX=0
CREDENTIAL_READS_MAX=0
RAW_PROVIDER_ENVELOPES_MAX=0
PACKET_CAPTURES_MAX=0
SYNTHETIC_FIXTURES=12
IMPLEMENTATION_AUTHORIZED=false
```

只建议建立：

- phase instrumentation contract candidate；
- machine-readable Schema；
- 12 个 synthetic event-sequence fixtures；
- offline deterministic validator result；
- boundary report 和 execution receipt。

## 4. Required Phase Model

候选 contract 必须按序定义：

```text
P0 DNS_RESOLUTION
P1 TCP_CONNECT
P2 TLS_HANDSHAKE
P3 HTTP_REQUEST_HEADERS_WRITE
P4 HTTP_REQUEST_BODY_WRITE
P5 HTTP_RESPONSE_STATUS_AND_HEADERS
P6 HTTP_RESPONSE_BODY
P7 RESPONSE_CONTENT_EXTRACTION
P8 RESPONSE_SCHEMA_VALIDATION
P9 SANITIZED_RESULT_HANDOFF_COMMIT
```

每个 phase event 至少包含：

- `phase_id`；
- `status`；
- `started_at_monotonic_ref`；
- `elapsed_ms`；
- `timeout_budget_ms`；
- `bytes_in` 与 `bytes_out` 的数量，不包含 payload；
- `failure_category`；
- `predecessor_phase`；
- `executed`。

## 5. Failure Semantics

候选 contract 至少区分：

```text
DNS_TIMEOUT
TCP_CONNECT_TIMEOUT
TLS_HANDSHAKE_TIMEOUT
HTTP_HEADERS_WRITE_TIMEOUT
HTTP_BODY_WRITE_TIMEOUT
HTTP_RESPONSE_HEADERS_TIMEOUT
HTTP_RESPONSE_BODY_TIMEOUT
HTTP_RESPONSE_TRUNCATED
CONTENT_EXTRACTION_FAILURE
RESPONSE_SCHEMA_FAILURE
SANITIZED_HANDOFF_FAILURE
BOUNDARY_VIOLATION
```

一个 phase 失败后，所有依赖 phase 必须为
`NOT_EXECUTED_PREREQUISITE_FAILED`。不允许通过 retry、fallback、model substitution、
alias inference、JSON repair 或 semantic rewrite 抹去第一次失败。

## 6. Data Minimization Boundary

契约只允许持久化：

- phase timing；
- byte count；
- sanitized failure category；
- HTTP status（若已观察）；
- returned model identifier（若已观察）；
- raw envelope one-way digest（若实际 response 已存在）；
- sanitized result digest。

禁止持久化：

- credential 或 Authorization header；
- raw request/response body；
- prompt、review content 或 hidden reasoning；
- packet capture；
- resolver private configuration；
- 本机敏感网络标识。

## 7. Synthetic Fixture Matrix

12 个 fixtures 必须包括：

1. all phases pass；
2. DNS timeout；
3. TCP connect timeout；
4. TLS handshake timeout；
5. request headers write timeout；
6. request body write timeout；
7. response headers timeout；
8. response body timeout；
9. truncated response body；
10. content extraction failure；
11. response Schema failure；
12. sanitized handoff failure。

fixture 只验证状态机、计数、前置关闭和数据最小化规则，不模拟 provider correctness，
不形成 runtime、implementation 或 conformance evidence。

## 8. Frozen Sources

| artifact | SHA-256 |
|---|---|
| `PRE-29-PROVIDER-TRANSPORT-PHASE-DIAGNOSTIC-RESULT-v0.1.md` | `80bb5388ed9d7e881ba9b09d3e71e651e280550115bf6c0e8bfb19b29e7bdb2b` |
| `transport-phase-diagnostic-result.v0.1.json` | `94de383d754fcbfb9bc78d2a0006e0a3016843c388349f36ed1804c1beeee391` |
| `transport-phase-diagnostic-execution-receipt.v0.1.json` | `686b2c7b3965a9a070a4a354d51ba98451b75040824d9a009dee581a7e985d6e` |
| `transport-phase-diagnostic-authorization-receipt.v0.1.json` | `f0070a97ed6d45041e646291ce8486930648d4a4de46d5afb9b5e76116a418fc` |
| `PRE-29 Decision Record JSON` | `721c7ee24c9d85fdbcd0c74d11bc46bf0bbdcfa8de704a9fa7ed36072021a0ce` |
| `transport-phase-diagnostic-plan.v0.1.json` | `5fbbccafb137185e9093f53a0aea0e071eebb6415520c7b691cd026443883ab4` |

PRE-29 result commit：

```text
8e50b734e8e7e86f267da7a3a8557ae38a73d206
```

## 9. Preconditions

1. 六个 frozen source hash 全部匹配并在目标远端；
2. standing directive active；
3. PRE-30 独立 Decision、plan、contract Schema 和 fixture Schema 在 offline validation 前
   提交并远端验证；
4. PRE-30 network、HTTP、provider API、model request 和 credential read accounting 为 0；
5. validator 只能读取 frozen local artifacts 和 synthetic fixtures；
6. 所有失败、未知、negative fixture 必须保留。

## 10. Stop Conditions

- source/hash 或 phase order 漂移；
- 需要 network、HTTP、provider API、credential、external tool 或 model request；
- contract 包含 raw payload、credential、prompt、review content 或 hidden reasoning；
- fixture 被写成 provider response、customer evidence 或 runtime observation；
- validator 自动修复、重排或删除失败；
- offline PASS 被抬升为 implementation、provider support、conformance、certification、
  market/customer proof、model retry 或 `CS-G0 PASS`。

## 11. Success and False Effects

```text
SOURCE_HASHES_MATCH=6/6
CONTRACT_SCHEMA_META_VALID=1
FIXTURE_SCHEMA_META_VALID=1
SYNTHETIC_FIXTURES_VALIDATED=12/12
EXPECTED_OUTCOMES_MATCH=12/12
NETWORK_PROBES_EXECUTED=0
HTTP_REQUESTS_EXECUTED=0
PROVIDER_API_REQUESTS_EXECUTED=0
LIVE_MODEL_REQUESTS_EXECUTED=0
CREDENTIAL_READS_EXECUTED=0

PRE28_RESULT_CHANGED=false
PRE29_RESULT_CHANGED=false
MODEL_RETRY_AUTHORIZED=false
INSTRUMENTATION_IMPLEMENTATION_CREATED=false
HANDOFF_CONTRACT_ADOPTED=false
V0_2_CONTRACT_CANDIDATES_ADOPTED=false
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

## 12. Standing Directive Eligibility

本建议只有一个 offline exact action；artifact、phase model、fixture 数量、零外部动作、
stop conditions 和 false effects 已明确。

```text
STANDING_DIRECTIVE_REFERENCE=TITMAS-CS-STANDING-001
STANDING_DIRECTIVE_ELIGIBLE_CANDIDATE=true
AT_RECOMMENDATION_TIME_PRE30_DECIDED=false
AT_RECOMMENDATION_TIME_OFFLINE_VALIDATION_AUTHORIZED=false
AT_RECOMMENDATION_TIME_NETWORK_PROBES_EXECUTED=0
AT_RECOMMENDATION_TIME_HTTP_REQUESTS_EXECUTED=0
AT_RECOMMENDATION_TIME_LIVE_MODEL_REQUESTS_EXECUTED=0
```
