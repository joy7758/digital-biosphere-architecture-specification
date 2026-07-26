---
document_id: DBA-TITMAS-CS-D02-PRE-29-PROVIDER-TRANSPORT-PHASE-DIAGNOSTIC-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-29 Provider Transport Phase Diagnostic Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-29 Provider 传输阶段诊断建议 v0.1
version: 0.1.0
status: exact-transport-diagnostic-recommendation-not-decided
maturity: Development
decision_reference: CS-D02-PRE-29
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
provider_network_probe_authorized: false
http_request_authorized: false
live_model_request_authorized: false
implementation_authorized: false
---

# TITMAS CS-D02 PRE-29 Provider Transport Phase Diagnostic Recommendation v0.1

## 1. Why PRE-29 Exists

PRE-28 按已冻结的 handoff contract 执行了两个 provider network request，并把两个失败
结果分别原子提交到独立 sanitized sink。两个 session 都在收到 HTTP response 前出现：

```text
SANITIZED_ERROR_DETAIL=NETWORK_ERROR:TimeoutError
HTTP_STATUS=null
RESPONSE_BYTES=0
QUALIFYING_REVIEWS=0
```

该结果证明失败已被保留并可验证，但当前执行记录没有区分 timeout 发生在 DNS、TCP
connect、TLS handshake、HTTP write 还是 HTTP response read。它不证明 provider 或
model 不可用，也不支持立即重试两个 model request。

## 2. Agent Recommendation Gate

如果潜在 Agent 客户询问是否应在当前证据下再次调用模型或采用 PRE-25 v0.2 contracts：

```text
RECOMMEND_MODEL_REQUEST_RETRY=NO
REASON=TIMEOUT_PHASE_NOT_IDENTIFIED_AND_ZERO_REVIEW_CONTENT_OBSERVED
RECOMMEND_BOUNDED_TRANSPORT_PHASE_DIAGNOSTIC=YES
RECOMMEND_CONTRACT_ADOPTION_NOW=NO
```

不推荐直接重试的原因：

1. PRE-28 两个固定请求预算已经消耗；
2. 两次请求都没有 HTTP status、response bytes 或审查内容；
3. 当前 `TimeoutError` 粒度不足，重试不能解释失败阶段；
4. provider availability、model availability 和契约正确性均未由该失败证明；
5. `VALID_PROBLEM_RECORDS=0` 且 `CS_G0_PASS=false`。

## 3. Exact Recommendation

```text
RECOMMENDED_OPTION=AUTHORIZE_BOUNDED_PRE28_PROVIDER_TRANSPORT_PHASE_DIAGNOSTIC_WITH_ZERO_HTTP_AND_MODEL_REQUESTS_ONLY
PRIMARY_REPOSITORY=digital-biosphere-architecture
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
AUTHORIZATION_HEADERS_MAX=0
RETRY_ATTEMPTS_MAX=0
FALLBACK_ATTEMPTS_MAX=0
ENDPOINT_MUTATIONS_MAX=0
IMPLEMENTATION_AUTHORIZED=false
```

诊断只建立当前环境到冻结 host/port 的分阶段 transport observation（传输观察），不发送
HTTP method、path、headers 或 body，不读取 API key，不调用模型。

## 4. Frozen Diagnostic Phases

### Phase A: DNS

- 对 `qianfan.baidubce.com` 执行一次系统 DNS resolution；
- 只记录成功／失败、sanitized error category、解析地址数量和 elapsed time；
- 不持久化完整 resolver configuration、search domain 或本机网络标识。

### Phase B: TCP

- 仅当 Phase A 成功时，对一个由系统返回的地址执行一次 `443` TCP connect；
- connect timeout 固定为 `10 seconds`；
- 连接成功后立即关闭，不发送应用层字节。

### Phase C: TLS

- 仅当 Phase B 成功时，新建一次 TCP connection 并执行一次带
  `server_hostname=qianfan.baidubce.com` 的 TLS handshake；
- handshake timeout 固定为 `10 seconds`；
- 只记录 TLS version、peer certificate subject/issuer 的 one-way digest、notBefore/
  notAfter 和 hostname verification 结果；
- handshake 完成后立即关闭，不发送 HTTP 字节。

若前一阶段失败，后续阶段必须记为 `NOT_EXECUTED_PREREQUISITE_FAILED`，不能通过额外请求
补偿。

## 5. Required Result Contract

未来独立 Decision 必须在任何 network probe 前冻结：

- diagnostic plan 与 result Schema；
- exact host、port、phase order、timeout 和 request accounting；
- 一个全新、权限为 `0700` 的 temporary root；
- 一个预先不存在、非 symlink 的 sanitized result target；
- source hashes 与 authorization receipt。

结果对象至少记录：

- `observed_at`；
- `target_host` 与 `target_port`；
- 三个 phase 的 `status`、`elapsed_ms` 和 sanitized failure category；
- `external_network_probes_executed`；
- `http_requests_executed=0`；
- `provider_api_requests_executed=0`；
- `live_model_requests_executed=0`；
- `credential_reads_executed=0`；
- exact false effects。

不得持久化 packet capture、socket payload、credential、Authorization header、HTTP body、
provider response、DNS resolver private configuration 或本机敏感网络标识。

## 6. Interpretation Boundary

| observed result | 允许结论 | 禁止结论 |
|---|---|---|
| DNS failure | 当前环境在该次观察中无法完成目标 host 解析 | provider/model 永久不可用 |
| TCP failure | 当前环境在该次观察中未建立目标端口连接 | API endpoint 错误或 provider 拒绝 |
| TLS failure | 当前环境在该次观察中未完成验证的 TLS handshake | model 不存在或 request contract 错误 |
| DNS/TCP/TLS all pass | 基础传输阶段在该次观察中可达 | PRE-28 必然是 HTTP read timeout、provider/model 可用或重试必然成功 |

即使三阶段全部通过，PRE-28 精确 timeout phase 仍只能标记为：

```text
PRE28_TIMEOUT_PHASE=NOT_RESOLVED_BY_LOWER_LAYER_PROBE
```

该结果只帮助缩小后续 instrumentation（可观测诊断）设计范围。

## 7. Frozen Sources

| artifact | SHA-256 |
|---|---|
| `PRE-28-HANDOFF-BOUND-CONTRACT-CANDIDATE-REVIEW-RESULT-v0.1.md` | `65f722d13503d101f12b7da78db084267c88783c10ce38c6f27ef83cab884da3` |
| `handoff-bound-contract-review-validation-result.v0.1.json` | `d48019d7572d58541bde5b7fcb8d0d668a68dd766364e48f5762b500b38095cc` |
| `handoff-bound-contract-review-execution-receipt.v0.1.json` | `c450930dbc94d0a2e03f5532a5d43e3d7bb840f51bc5a7abb3cc63660ac2f994` |
| `handoff-bound-contract-review-control-receipt.v0.1.json` | `9d97f6c5fd87083cc5ed1e043f92dea53c40c97375bf1dd07ce51b4801fdf58d` |
| `handoff-bound-contract-review-kimi-session-result.v0.1.json` | `d3f8c1af5c3fd27ed623f5bdd74de50a80d387ce85d589bf5f7acf4f2ea7e22e` |
| `handoff-bound-contract-review-glm-session-result.v0.1.json` | `f9ef26916772633597e7c3716418ef51b4f560a6ed05c1f7140f8dcb6672b032` |

这些 artifacts 的结果提交为
`e2f2f1356900334276573641087759885a80b914`。

## 8. Preconditions

1. 上述六个 source hash 全部匹配并在目标远端；
2. standing directive active；
3. PRE-29 独立 Decision、plan、Schema、result target 与 authorization receipt 在任何
   network probe 前提交并远端验证；
4. PRE-29 probe accounting 为 0；
5. PRE-28 和 PRE-26 request budgets 保持关闭；
6. 诊断实现能够证明未生成任何 HTTP application bytes；
7. 结果只写入 sanitized sink，stdout 不是 canonical result。

## 9. Stop Conditions

- source/hash、host、port、phase order 或 timeout 漂移；
- 需要 credential、Authorization header、HTTP method/path/body 或 provider API request；
- retry、fallback、第二地址探测、endpoint mutation 或代理自动切换；
- temporary target 预先存在、为 symlink、权限不符或无法原子提交；
- raw network payload、packet capture、本机敏感网络配置或 secret 将被持久化；
- 结果被抬升为 provider/model availability、contract correctness、conformance、
  certification、market/customer proof、`CS-G0 PASS` 或重试授权。

## 10. Success and False Effects

```text
SOURCE_HASHES_MATCH=6/6
DNS_RESOLUTION_ATTEMPTS_EXECUTED=RESULT_DEPENDENT_MAX_1
TCP_CONNECT_ATTEMPTS_EXECUTED=RESULT_DEPENDENT_MAX_1
TLS_HANDSHAKE_ATTEMPTS_EXECUTED=RESULT_DEPENDENT_MAX_1
TOTAL_EXTERNAL_NETWORK_PROBES_EXECUTED=RESULT_DEPENDENT_MAX_3
HTTP_REQUESTS_EXECUTED=0
PROVIDER_API_REQUESTS_EXECUTED=0
LIVE_MODEL_REQUESTS_EXECUTED=0
CREDENTIAL_READS_EXECUTED=0
RETRY_ATTEMPTS=0

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

## 11. Standing Directive Eligibility

本建议只有一个 exact action；目标、phase、network probe cap、timeout、结果字段、禁止
payload 和 false effects 已明确。它仍涉及三次有界外部网络探测，因此必须先形成独立
Decision、冻结执行包并远端验证。

```text
STANDING_DIRECTIVE_REFERENCE=TITMAS-CS-STANDING-001
STANDING_DIRECTIVE_ELIGIBLE_CANDIDATE=true
AT_RECOMMENDATION_TIME_PRE29_DECIDED=false
AT_RECOMMENDATION_TIME_NETWORK_PROBE_AUTHORIZED=false
AT_RECOMMENDATION_TIME_NETWORK_PROBES_EXECUTED=0
AT_RECOMMENDATION_TIME_HTTP_REQUESTS_EXECUTED=0
AT_RECOMMENDATION_TIME_LIVE_MODEL_REQUESTS_EXECUTED=0
```
