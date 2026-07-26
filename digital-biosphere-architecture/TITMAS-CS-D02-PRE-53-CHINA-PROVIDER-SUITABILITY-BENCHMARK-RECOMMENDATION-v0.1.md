---
document_id: DBA-TITMAS-CS-D02-PRE-53-CHINA-PROVIDER-SUITABILITY-BENCHMARK-RECOMMENDATION-0.1
version: 0.1.0
status: canonical-recommendation-ready-for-standing-directive-eligibility-review
maturity: Development
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
provider_requests_max: 12
model_requests_max: 12
credential_identifiers_max: 3
implementation_authorized: false
---

# PRE-53 China Provider Suitability Benchmark Recommendation

## Recommendation

```text
RECOMMENDATION_ID=CS-D02-PRE-53
RECOMMENDED_ACTION=AUTHORIZE_PUBLIC_SAFE_SEQUENTIAL_CHINA_PROVIDER_SUITABILITY_BENCHMARK_EXACT_12_REQUESTS
RECOMMENDATION=RECOMMENDED
PROVIDER_REQUESTS_MAX=12
MODEL_REQUESTS_MAX=12
CREDENTIAL_IDENTIFIERS_MAX=3
RETRY_MAX=0
FALLBACK_MAX=0
MODEL_SUBSTITUTION_MAX=0
JSON_REPAIR_MAX=0
TARGET_WRITES=0
IMPLEMENTATION_AUTHORIZED=false
```

建议对当前本机已有 secret-safe credential identifiers（秘密安全凭证标识）的三家中国
Provider、四个 exact model 执行一次统一的 suitability benchmark（适配性基准测试），
用于选择最适合补齐 TITMAS 当前“稳定机器审查通道”和“独立 Security Reviewer”缺口的
接入方向。

测试结果是 bounded observation（有界观测），不是 Provider certification（供应商认证）、
长期 SLA、模型质量排名、客户采用或 Security Review。

## Exact Test Matrix

| Provider | Endpoint | Model | Credential identifier | Requests |
|---|---|---|---|---:|
| DeepSeek | `https://api.deepseek.com/chat/completions` | `deepseek-v4-pro` | `DEEPSEEK_API_KEY` | 3 |
| DeepSeek | `https://api.deepseek.com/chat/completions` | `deepseek-v4-flash` | `DEEPSEEK_API_KEY` | 3 |
| Qianfan | `https://qianfan.baidubce.com/v2/chat/completions` | `ernie-4.5-turbo-20260402` | `QIANFAN_API_KEY` | 3 |
| Ark | `https://ark.cn-beijing.volces.com/api/v3/chat/completions` | `doubao-seed-2-0-lite-260215` | `ARK_API_KEY` | 3 |

Each exact model receives:

1. deterministic governance extraction, run A;
2. identical deterministic governance extraction, run B;
3. machine-customer recommendation advisory.

All requests are sequential. A failed request consumes its budget and remains failed.

## Public-Safe Test Content

The benchmark may send only a synthetic TITMAS boundary summary:

- Evidence proves execution history, not Truth;
- Recommendation is not Decision;
- Evaluation is not Authority;
- Provider/model documentation is not current entitlement;
- role independence is not Provider independence;
- no private repository text, unpublished artifact, personal data, credential or hidden prompt.

Responses must be one direct JSON object with no Markdown. No raw hidden reasoning is requested or
retained.

## Frozen Scoring

| Dimension | Weight | Direct evidence |
|---|---:|---|
| Transport completion | 30 | HTTP completion within 45 seconds |
| Direct JSON compliance | 25 | direct parse without extraction or repair |
| Frozen Schema accuracy | 20 | required fields, enums and expected boundary facts |
| Latency | 10 | bounded observed elapsed time |
| Governance-boundary correctness | 10 | no Authority or Truth elevation |
| Exact model identity | 5 | returned model equals requested exact ID |

The score is descriptive for this run. It cannot prove general reliability. `NOT_TESTED` and
failed requests score zero for their affected direct-evidence dimensions.

## Current Credential-Identifier Evidence

One read-only local inventory found:

```text
QIANFAN_API_KEY_PRESENT_NONEMPTY=true
ARK_API_KEY_PRESENT_NONEMPTY=true
DEEPSEEK_API_KEY_PRESENT_NONEMPTY=true
SECRET_VALUE_OUTPUTS=0
SECRET_VALUE_RETENTION=0
```

Presence does not prove validity, entitlement, balance, safety or future availability.

## Non-Connected Provider Desk Review

The same packet may compare official public API documentation for:

- Alibaba Cloud Model Studio / Qwen;
- Zhipu BigModel / GLM;
- Moonshot AI / Kimi;
- MiniMax;
- Tencent Hunyuan.

These Providers receive zero API requests because no verified non-placeholder credential identifier
was found. Their status must remain `OFFICIAL_DOCUMENTATION_REVIEW_ONLY_NOT_TESTED`.

## Exact Outputs

```text
commercialization-standards-china-provider-suitability-benchmark/
  PRE-53-CHINA-PROVIDER-SUITABILITY-BENCHMARK-RESULT-v0.1.md
  benchmark-plan.v0.1.json
  benchmark-plan.schema.v0.1.json
  sanitized-session-results.v0.1.json
  sanitized-session-results.schema.v0.1.json
  provider-comparison.v0.1.json
  provider-comparison.schema.v0.1.json
  negative-cases.v0.1.json
  negative-cases.schema.v0.1.json
  execution-receipt.v0.1.json
  execution-receipt.schema.v0.1.json
```

Separate Decision Markdown, JSON and Schema may be created before execution.

## Preconditions

- DBA remote remains `ac735a7a897367af7227db831f82f2e3c03f4996`;
- PRE-52 remains unchanged;
- PRE-51 cannot be retried or reinterpreted;
- exact model identifiers are rechecked against official documentation on `2026-07-27`;
- all prompts are frozen and hashed before the first request;
- no later specific Human Decision conflicts.

## Stop Conditions

Stop the affected session, without retry, if:

- exact credential identifier is absent;
- endpoint or model differs from the frozen binding;
- timeout, network, authentication, entitlement, quota or HTTP failure occurs;
- response is empty, non-JSON, fenced JSON or Schema-invalid;
- returned model differs from requested exact ID;
- sanitization would require semantic rewriting;
- a response contains credentials, personal data or private source material.

Stop the whole benchmark if:

- a credential value would be printed, committed or transmitted outside its exact Provider;
- a Provider/model is substituted;
- concurrency exceeds one;
- retry, fallback, alias inference or JSON repair is attempted;
- results are used to authorize implementation, release, commercial offer or Security Review.

## Interpretation Boundaries

- best observed score is not “best Chinese model”;
- three requests are not an SLA;
- model self-recommendation is advisory, not customer evidence;
- an exact model response is not Provider support for TITMAS;
- shared Provider reviewers do not close independent Security Review;
- Schema pass is not scientific correctness, conformance or production readiness.

## Next Gate

Successful PRE-53 may recommend:

1. one primary machine-review Provider/model;
2. one distinct Provider to connect for independent Security Reviewer;
3. an exact future preflight contract.

It does not authorize Provider integration or another live review.
