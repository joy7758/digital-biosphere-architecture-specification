---
document_id: DBA-TITMAS-CS-D02-PRE-57-QWEN3-7-PLUS-ONBOARDING-BENCHMARK-RECOMMENDATION-0.1
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

# PRE-57 Exact Qwen3.7-Plus Onboarding Benchmark Recommendation

## Recommendation

```text
RECOMMENDATION_ID=CS-D02-PRE-57
RECOMMENDED_ACTION=AUTHORIZE_EXACT_QWEN3_7_PLUS_ONBOARDING_BENCHMARK_THREE_PUBLIC_SAFE_REQUESTS
RECOMMENDATION=RECOMMENDED
PROVIDER=ALIBABA_CLOUD_MODEL_STUDIO
MODEL=qwen3.7-plus
CREDENTIAL_IDENTIFIER=DASHSCOPE_API_KEY
PROVIDER_REQUESTS_MAX=3
MODEL_REQUESTS_MAX=3
CONCURRENCY_MAX=1
RETRY_FALLBACK_SUBSTITUTION_EXTRACTION_REPAIR_MAX=0
IMPLEMENTATION_AUTHORIZED=false
```

建议对 Human Owner 指定的北京区域 OpenAI-compatible endpoint 和 PRE-56 直接发现的
exact model identifier `qwen3.7-plus` 执行一次新的有界 onboarding benchmark。

PRE-55 的 `model_not_found` 是保留失败，不被重写或重试。PRE-56 只证明目录可读和标识存在，
不证明 entitlement（可调用资格）、推理成功、Provider support、Security Review 或长期可用性。

## Exact Evidence Binding

```text
PRE56_RESULT=commercialization-standards-qwen-model-discovery/PRE-56-QWEN-MODEL-DISCOVERY-RESULT-v0.1.md
PRE56_RESULT_SHA256=75cffdf8de4a7a1fcf3316421ad0388822a6021547bedfacbf82adca5768b03b
PRE56_RESULT_COMMIT=660ab543583f6d75ac19d3db779df6b0c999e6f5
BASE_URL_SOURCE=HUMAN_OWNER_PROVIDED
BASE_URL=https://token-plan.cn-beijing.maas.aliyuncs.com/compatible-mode/v1
CHAT_COMPLETIONS_PATH=/chat/completions
MODEL=qwen3.7-plus
CREDENTIAL_IDENTIFIER=DASHSCOPE_API_KEY
```

## Three-Request Sequence

| session | purpose | execution condition |
|---|---|---|
| `QWEN37-ONBOARD-01` | authentication、transport、exact model 和 direct JSON preflight | 始终执行一次 |
| `QWEN37-ONBOARD-02` | 相同边界的 bounded repeatability | 仅 `01` 全部通过 |
| `QWEN37-ONBOARD-03` | machine-customer recommendation advisory | 仅 `01` 与 `02` 全部通过 |

任一 session 失败即停止。后续 session 标记 `NOT_EXECUTED_FAIL_CLOSED`；不得 retry、
fallback、alias inference、model substitution、content extraction、JSON repair 或人工补值。

## Public-Safe Response Contract

只发送合成 TITMAS 边界摘要，不发送私有仓库、个人或客户数据、credential value 或隐藏推理。
Assistant content 必须是一个直接 JSON object：

```json
{
  "request_id": "QWEN37-ONBOARD-01|02|03",
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

全部五个 boundary booleans 必须为 `false`。`would_recommend_to_agent_developer` 只是模型对
bounded non-production evaluation 的 advisory，不是客户证据或市场采用。

## Preconditions

- DBA remote baseline 含 PRE-56 clean-clone pass；
- `DASHSCOPE_API_KEY` 仅在 Git-excluded local secret file 中存在且非空；
- `DASHSCOPE_BASE_URL` 精确匹配 Human Owner 指定值；
- secret file mode 为 `600`；
- frozen plan、Schema 和 Decision 在首次请求前提交并推送；
- credential value 不输出、不写入 packet、不进入 Git；
- 没有更晚、更具体决定冲突。

## Pass Rule

`PASS_3_OF_3` 要求每个 session 同时满足 HTTP 2xx、outer JSON、assistant direct JSON、
冻结 Schema、exact returned model、expected boundary values，以及 secret/private-content scan。

## Permanent Non-Effects

```text
PROVIDER_INTEGRATION_AUTHORIZED=false
PROVIDER_SUPPORTED=false
PROVIDER_CERTIFIED=false
SECURITY_REVIEW_AUTHORIZED=false
SECURITY_REVIEW_COMPLETED=false
IMPLEMENTATION_AUTHORIZED=false
RUNTIME_AUTHORIZED=false
EXTERNAL_REPOSITORY_WRITE_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
STANDARD_READY=false
```

## Next Gate

只有 `PASS_3_OF_3` 才允许形成 multi-Provider Security Review preflight Recommendation。
通过也仅表示该 endpoint、credential 和 model 在当前时间点通过有界 response-contract 测试。
