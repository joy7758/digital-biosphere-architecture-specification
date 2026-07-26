# PRE-53 China Provider Suitability Benchmark Result v0.1

```text
RESULT=PASS_12_OF_12_BOUND_REQUESTS_PRIMARY_NEW_PROVIDER_QWEN
PROVIDER_REQUESTS=12/12
DIRECT_JSON_PASS=12/12
SCHEMA_PASS=12/12
EXPECTED_BOUNDARY_VALUES_PASS=12/12
EXACT_RETURNED_MODEL_MATCH=12/12
RETRY_FALLBACK_SUBSTITUTION_REPAIR=0
BEST_CURRENT_CONNECTED_MODEL=deepseek-v4-flash
PRIMARY_NEW_PROVIDER_TO_CONNECT=ALIBABA_CLOUD_MODEL_STUDIO
PRIMARY_NEW_MODEL_TO_TEST=qwen3.7-plus-2026-05-26
PRIMARY_NEW_CREDENTIAL_IDENTIFIER=DASHSCOPE_API_KEY
```

## Direct Result

| Provider / model | PASS | Median latency | Advisory |
|---|---:|---:|---|
| DeepSeek `deepseek-v4-flash` | 3/3 | 1,310 ms | `CONDITIONAL`, recommend=true |
| DeepSeek `deepseek-v4-pro` | 3/3 | 2,257 ms | `CONDITIONAL`, recommend=true |
| Qianfan `ernie-4.5-turbo-20260402` | 3/3 | 3,004 ms | `CONDITIONAL`, recommend=true |
| Ark `doubao-seed-2-0-lite-260215` | 3/3 | 7,997 ms | `CONDITIONAL`, recommend=true |

All twelve calls were sequential and used the same two frozen public-safe prompts. No request was
retried, repaired, substituted or filled by another Provider.

The Kimi/Qianfan PRE-51 failure must not be generalized to all Qianfan models: the exact ERNIE route
passed 3/3 in this bounded run. Conversely, 3/3 does not establish a general Qianfan SLA.

## Recommendation

For the existing connected pool, use DeepSeek `deepseek-v4-flash` as the first candidate for
high-volume machine review preflight because it had the lowest observed latency while retaining
3/3 direct JSON, Schema and governance-boundary correctness.

For the current missing independent Security Reviewer Provider, connect:

```text
Provider=Alibaba Cloud Model Studio
Model=qwen3.7-plus-2026-05-26
Credential identifier=DASHSCOPE_API_KEY
OpenAI-compatible base=https://dashscope.aliyuncs.com/compatible-mode/v1
```

Reasons:

1. it adds a fourth Provider distinct from DeepSeek, Qianfan and Ark;
2. official OpenAI-compatible Chat Completions reduces adapter work;
3. official JSON mode directly matches the strict machine-review contract;
4. 1M context fits long architecture and governance packets;
5. the dated snapshot model supports exact version pinning.

Second choice: direct Zhipu BigModel `glm-5.2` with `ZHIPUAI_API_KEY`. It also documents OpenAI
compatibility, JSON structured output and 1M context, but the reviewed model ID is not a dated
snapshot.

Do not paste an API key into a chat or commit it. A future onboarding gate should only check the
presence of `DASHSCOPE_API_KEY`, then run the same three-request benchmark. Connection does not
authorize Provider integration or Security Review.

## Documentation-Only Candidates

- Moonshot direct Kimi `kimi-k2.6`: technically promising, but not directly tested here; the
  Qianfan-hosted Kimi failures do not prove direct Moonshot behavior.
- MiniMax `MiniMax-M2.7`: OpenAI-compatible, but official examples include reasoning in content
  unless separated; strict direct JSON needs a dedicated test.
- Tencent TokenHub Hunyuan `hy3`: OpenAI-compatible and 256K context, but platform migration and
  exact request-contract details add current integration uncertainty.

## Non-Effects

```text
PROVIDER_SUPPORT_CLAIM=false
PROVIDER_CERTIFICATION=false
INDEPENDENT_SECURITY_REVIEW_COMPLETED=false
CUSTOMER_EVIDENCE=false
IMPLEMENTATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
COMMERCIAL_AVAILABILITY=false
```

Three requests per model are a routing signal, not a Provider ranking, SLA or production proof.
