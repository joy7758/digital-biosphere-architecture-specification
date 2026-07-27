---
document_id: DBA-TITMAS-CS-D02-PRE-55-QWEN-ONBOARDING-BENCHMARK-RECOMMENDATION-0.1
version: 0.1.0
status: canonical-recommendation-ready-for-standing-directive-eligibility-review
maturity: Development
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
provider_requests_max: 3
model_requests_max: 3
credential_identifiers_max: 1
implementation_authorized: false
---

# PRE-55 Qwen Onboarding Benchmark Recommendation

## Recommendation

```text
RECOMMENDATION_ID=CS-D02-PRE-55
RECOMMENDED_ACTION=AUTHORIZE_QWEN_ONBOARDING_BENCHMARK_EXACT_THREE_PUBLIC_SAFE_REQUESTS
RECOMMENDATION=RECOMMENDED
PROVIDER=ALIBABA_CLOUD_MODEL_STUDIO
MODEL=qwen3.7-plus-2026-05-26
CREDENTIAL_IDENTIFIER=DASHSCOPE_API_KEY
PROVIDER_REQUESTS_MAX=3
MODEL_REQUESTS_MAX=3
CONCURRENCY_MAX=1
RETRY_MAX=0
FALLBACK_MAX=0
MODEL_SUBSTITUTION_MAX=0
JSON_REPAIR_MAX=0
IMPLEMENTATION_AUTHORIZED=false
```

建议对 Human Owner 指定的北京区域 OpenAI-compatible endpoint 和 exact model 执行一次
有界 onboarding benchmark（接入基准测试）。目的只是在当前账户和当前时间点验证：

- credential 能否完成认证；
- endpoint 是否接受 OpenAI-compatible Chat Completions；
- exact model 是否可用且 returned model identity 可核对；
- response 是否能直接解析为冻结 JSON Schema；
- TITMAS Authority／Truth 边界是否保持。

测试结果不是 Provider integration、Provider certification、长期 SLA、Security Review、
客户采用或生产可用性。

## Exact Binding

```text
BASE_URL_SOURCE=HUMAN_OWNER_PROVIDED
BASE_URL=https://token-plan.cn-beijing.maas.aliyuncs.com/compatible-mode/v1
CHAT_COMPLETIONS_PATH=/chat/completions
MODEL=qwen3.7-plus-2026-05-26
CREDENTIAL_IDENTIFIER=DASHSCOPE_API_KEY
```

Base URL 是用户提供的 exact route；本 Recommendation 不把它宣称为阿里云公共默认 endpoint。

## Three-Request Sequence

| session | purpose | execution condition |
|---|---|---|
| `QWEN-ONBOARD-01` | authentication、transport、exact model 和直接 JSON preflight | 始终执行一次 |
| `QWEN-ONBOARD-02` | 重复相同 governance extraction，观察 bounded repeatability | 仅 `01` 全部通过 |
| `QWEN-ONBOARD-03` | machine-customer recommendation advisory | 仅 `01` 与 `02` 全部通过 |

每次请求均消耗预算。失败后不重试；前置 session 失败时，后续 session 标记
`NOT_EXECUTED_FAIL_CLOSED`，不得用其他 Provider 或模型补位。

## Public-Safe Payload Boundary

只允许发送合成的 TITMAS 边界摘要：

- Evidence proves execution history, not Truth；
- Recommendation is not Decision；
- Evaluation is not Authority；
- credential configuration is not Provider connection；
- Provider response is not certification or Security Review。

不得发送私有仓库正文、未公开材料、个人数据、客户数据、credential value 或隐藏推理请求。
Response 必须是一个直接 JSON object，不得使用 Markdown fence；不允许提取、修复或改写。

## Frozen Response Contract

```json
{
  "request_id": "QWEN-ONBOARD-01|02|03",
  "provider_fit": "SUITABLE|CONDITIONAL|NOT_SUITABLE",
  "evidence_is_truth": false,
  "recommendation_is_decision": false,
  "evaluation_is_authority": false,
  "credential_means_connected": false,
  "authority_claimed": false,
  "would_recommend_to_agent_developer": true,
  "reason": "non-empty bounded string"
}
```

`01` 和 `02` 的 expected `provider_fit` 是 `SUITABLE` 或 `CONDITIONAL`；`03` 可返回任一
枚举，但全部五个 boundary booleans 必须保持冻结值。

## Exact Output Packet

```text
commercialization-standards-qwen-onboarding-benchmark/
  PRE-55-QWEN-ONBOARDING-BENCHMARK-RESULT-v0.1.md
  benchmark-plan.v0.1.json
  benchmark-plan.schema.v0.1.json
  sanitized-session-results.v0.1.json
  sanitized-session-results.schema.v0.1.json
  negative-cases.v0.1.json
  negative-cases.schema.v0.1.json
  execution-receipt.v0.1.json
  execution-receipt.schema.v0.1.json
```

Separate Decision Markdown、JSON 和 Schema 可在 execution 前创建。

## Preconditions

- DBA remote HEAD 是 `f56aae624b59381cc22d6d291f7a582db3005569`；
- PRE-54 clean clone、Schema、links 和 secret scan 全部通过；
- `DASHSCOPE_API_KEY` 在 Git-excluded local secret file 中存在且非空；
- `DASHSCOPE_BASE_URL` 与 Human Owner 指定值精确匹配；
- secret file mode 是 `600`；
- credential value 不输出、不写入 packet、不提交 Git；
- 没有更晚、更具体决定冲突。

## Pass and Fail-Closed Rules

`PASS_3_OF_3` 要求每个执行 session 同时满足：

- HTTP 2xx；
- response body 是 JSON；
- assistant content 是 direct JSON object；
- frozen Schema valid；
- returned model 精确匹配 requested model；
- expected boundary values 全部匹配；
- credential、PII 和 private material scan 无命中。

任一项失败即保留失败。不得 retry、fallback、model substitution、alias inference、
content extraction、JSON repair 或人工补值。

## Permanent Non-Effects

```text
PROVIDER_INTEGRATION_AUTHORIZED=false
PROVIDER_SUPPORTED=false
PROVIDER_CERTIFIED=false
SECURITY_REVIEW_AUTHORIZED=false
SECURITY_REVIEW_COMPLETED=false
IMPLEMENTATION_AUTHORIZED=false
RUNTIME_AUTHORIZED=false
EXTERNAL_ACTION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
STANDARD_READY=false
```

## Next Gate

只有 `PASS_3_OF_3` 才允许形成 multi-Provider review preflight Recommendation；即使通过，
Qwen 也只是直接测试过的 Provider candidate，不是已集成 Provider 或独立 Security Review。
