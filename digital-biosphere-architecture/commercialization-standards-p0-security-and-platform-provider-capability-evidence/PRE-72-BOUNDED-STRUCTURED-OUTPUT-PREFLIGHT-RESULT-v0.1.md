# PRE-72 Bounded Structured-Output Preflight Result v0.1

## Result

```text
PRE72_EXECUTED=true
PRE72_RESULT=PASS_BOUNDED_STRUCTURED_OUTPUT_PREFLIGHT_6_OF_6
QIANFAN_PASS=3/3
QWEN_PASS=3/3
EXACT_RETURNED_MODEL_MATCH=6/6
DIRECT_SINGLE_JSON_OBJECT_PASS=6/6
FROZEN_RESPONSE_SCHEMA_PASS=6/6
EXACT_SESSION_BINDING_PASS=6/6
AUTHORITY_BOUNDARY_PASS=6/6
RETRY=0
FALLBACK=0
MODEL_SUBSTITUTION=0
RESPONSE_EXTRACTION=0
JSON_REPAIR=0
RAW_RESPONSE_ENVELOPES_PERSISTED=0
ASSISTANT_CONTENT_PERSISTED=0
CREDENTIAL_VALUES_PRINTED=0
CREDENTIAL_VALUES_PERSISTED=0
CREDENTIAL_VALUES_EXPOSED_OUTSIDE_AUTHORIZED_TRANSPORT=0
RESULT_AND_RECEIPT_SCHEMA_PASS=2/2
RESULT_AND_RECEIPT_NEGATIVE_MUTATIONS_REJECTED=10/10
PROVIDER_SUPPORTED=false
FORMAL_HUMAN_SECURITY_REVIEW_COMPLETE=false
CONFORMANCE_PASS=false
STANDARD_READY=false
RELEASE_AUTHORIZED=false
PRODUCTION_READY=false
```

## Execution

在远端干净检出验证 PRE-72 Decision、4/4 target hashes 与 recommendation hash 后，
执行器才读取本地 Git-excluded 环境文件中的两个 credential value。两个值各读取一次
进入进程内存，共产生 6 次 HTTPS Authorization header emission。

六个请求按冻结顺序执行：

| lane | model | executed | pass |
|---|---|---:|---:|
| Qianfan | `ernie-4.5-turbo-20260402` | 3 | 3 |
| Alibaba Cloud | `qwen3.7-plus` | 3 | 3 |

每次均通过：

1. HTTP 200；
2. exact returned model match；
3. assistant content 为单一 direct JSON object；
4. duplicate key、prefix/suffix、code fence 与 non-object boundary；
5. frozen response Schema；
6. exact session binding；
7. explicit non-claim / authority boundary。

## Credential and persistence boundary

```text
credential_identifiers_configured=2
credential_values_accessed_in_process_memory=2
authorization_header_values_emitted_to_tls_client=6
credential_values_printed=0
credential_values_persisted=0
credential_values_exposed_outside_authorized_transport=0
raw_response_envelopes_persisted=0
assistant_content_persisted=0
```

Git 中只保留 request/response byte count、SHA-256、HTTP status、model binding、验证布尔值、
attempt accounting 和 false effects。Provider envelope、assistant 原文、usage 和 secret value
均未进入 artifact。

结果与回执的两个 machine instance 均通过 JSON Schema 2020-12 校验；10 个
fail-closed mutation（model mismatch、secret print、raw persistence、JSON repair、
formal review elevation 和 next-action auto-authorization 等）全部被拒绝。

## Interpretation

本结果只证明：

> 在 `2026-07-27` 的 exact endpoint、model、request shape 与六次有界请求中，
> 两条 Provider lane 都能够满足 TITMAS strict direct-JSON preflight contract。

它不证明长期可靠性、Provider support、正式 Human Security Review、conformance、
Standard Ready、release 或 production readiness。

## Next step

下一步只允许形成：

```text
PREPARE_PRE73_EXACT_DUAL_PROVIDER_AGENT_ASSISTED_SECURITY_REVIEW_RECOMMENDATION
```

PRE-73 未被本结果自动授权。
