---
document_id: DBA-TITMAS-CE-G14-CONTEXT-COMPATIBLE-INPUT-PROJECTION-REMEDIATION-RECOMMENDATION-0.1
title: TITMAS CE-G14 Context-compatible Input-projection Remediation Recommendation v0.1
title_zh: TITMAS CE-G14 上下文兼容输入投影修复建议 v0.1
version: 0.1.0
status: recommendation-only
maturity: Development
owner_ref: zhangbin
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G14 Context-compatible Input-projection Remediation Recommendation v0.1

## 1. Problem

The CE-G14 parent Recommendation froze the full CE-G13 sanitized public bundle as the proposed
common two-provider input.

```text
SOURCE_BUNDLE_FILE_BYTES=513351
SOURCE_SANITIZED_TEXT_BYTES=440364
```

Official Baidu Qianfan model metadata for exact
`ernie-4.5-turbo-20260402` reports:

```text
CONTEXT_LENGTH=138240
PROMPT_TOKENS=125952
MAX_COMPLETION_TOKENS=12288
```

No provider-specific tokenizer result proves that the full CE-G13 bundle plus role prompt and
response Schema fits inside `125952` prompt tokens. Therefore:

```text
FULL_BUNDLE_CONTEXT_COMPATIBILITY_PROVEN=false
CE_G14_EXECUTION_DECISION_READY=false
```

This is an input-contract issue, not a failure of Provider B or CE-G13.

## 2. Cost finding

Current official list prices, ignoring free quota, promotions and cache discounts:

| Provider/model | Input price | Output price |
|---|---:|---:|
| Alibaba `qwen3.7-max` | CNY 12 / 1M tokens | CNY 36 / 1M tokens |
| Qianfan `ernie-4.5-turbo-20260402` | CNY 0.0008 / 1K tokens | CNY 0.0032 / 1K tokens |

At a conservative cap of 500,000 input and 8,192 output tokens per provider:

```text
QWEN_MAX_COST_CNY=6.294912
QIANFAN_MAX_COST_CNY=0.4262144
COMBINED_MAX_COST_CNY=6.7211264
ROUNDED_ESTIMATE_CNY=6.73
RECOMMENDED_EXECUTION_COST_CAP_CNY=20
```

The cost precondition can be bounded. Actual charge is not proven and may differ by subscription,
promotion or account plan.

Official references:

- `https://help.aliyun.com/en/model-studio/model-pricing`
- `https://cloud.baidu.com/doc/qianfan-api/s/Dmba8k71y`
- `https://cloud.baidu.com/doc/qianfan-docs/s/Jm8r1826a`

## 3. Options

### Option A — deterministic compact projection from five already-captured machine resources

Recommended.

It preserves public-source provenance, uses no new network request, gives both providers identical
bytes and removes redundant HTML/RSC payloads that are not needed for the CE-G14 questions.

### Option B — send the full bundle and rely on provider rejection

Rejected because a predictable context uncertainty should be resolved before consuming the
four-request budget.

### Option C — provider-specific truncation

Rejected because different input bytes would invalidate cross-provider comparability.

### Option D — summarize the material with another model

Rejected because model-generated summarization would add a new semantic transformation and a
hidden dependency before the validation being measured.

## 4. Exact projection candidate

Select the five already captured machine-readable resources in this exact order:

1. `CE-G13-RESOURCE-08` — `/status.json`
2. `CE-G13-RESOURCE-09` — `/llms.txt`
3. `CE-G13-RESOURCE-10` — `/titmas-community.json`
4. `CE-G13-RESOURCE-11` — `/agent-index.json`
5. `CE-G13-RESOURCE-12` — `/TITMAS-COMMERCIAL-EVALUATION-PACK-v0.2.json`

Their exact sanitized-text total is:

```text
SELECTED_RESOURCES=5
SELECTED_SANITIZED_TEXT_BYTES=79456
```

The deterministic projection envelope may contain only:

- bundle identifier and version;
- source bundle reference and SHA-256;
- projection profile identifier;
- ordered resource identifiers;
- for each resource: source/final URL, raw body SHA-256 and bytes, sanitized text SHA-256 and
  bytes, and exact sanitized text;
- false-effect declarations.

Rules:

```text
RESOURCE_ORDER_FIXED=true
RESOURCE_CONTENT_REWRITTEN=false
RESOURCE_CONTENT_SUMMARIZED=false
WHITESPACE_NORMALIZATION=false
CANONICAL_JSON=utf8_sort_keys_compact_separators_trailing_lf
MAX_PROJECTION_UTF8_BYTES=86000
MAX_ROLE_PROMPT_AND_SCHEMA_UTF8_BYTES=12000
MAX_TOTAL_MODEL_VISIBLE_UTF8_BYTES=100000
```

An in-memory diagnostic using this exact structure produced:

```text
DIAGNOSTIC_CANONICAL_PROJECTION_BYTES=85708
DIAGNOSTIC_CANONICAL_PROJECTION_SHA256=38dc90cb43bfba32a05a71c1ed8aaba3d8115d1a3c26037d1161e653b1b7f6ac
```

This diagnostic did not create or authorize the projection artifact.

## 5. Recommended offline remediation cycle

```text
RECOMMENDED_ACTION=AUTHORIZE_ONE_OFFLINE_CONTEXT_COMPATIBLE_INPUT_PROJECTION_PREPARATION_AND_VALIDATION
NETWORK_REQUESTS=0
MODEL_REQUESTS=0
CREDENTIAL_READS=0
TARGET_REPOSITORY_WRITES=0
CE_G14_EXECUTION=false
```

The future offline cycle should create:

1. projection profile;
2. projection JSON Schema;
3. exact compact projection artifact;
4. role-prompt and response-Schema byte budget manifest;
5. positive and negative validation fixtures;
6. offline validation result;
7. execution receipt;
8. bounded result report.

Required checks:

- source bundle and five resource hashes match immutable CE-G13 inputs;
- no selected content is rewritten or summarized;
- exact order and resource set match;
- canonical projection hash is deterministic across two independent serializations;
- projection bytes are at most `86000`;
- role prompt plus response Schema bytes are at most `12000`;
- total model-visible UTF-8 bytes are at most `100000`;
- duplicate JSON keys and additional properties are rejected;
- missing, reordered, substituted, mutated or sixth resources are rejected;
- any source/hash/byte-count drift fails closed;
- cost math matches the machine assessment;
- all execution, commercial and authority effects remain false.

The UTF-8 byte cap is a conservative cross-provider transport guard. It is not a claim about exact
provider tokenizer behavior. The future CE-G14 Decision must still retain provider-side context
errors as fail-closed results.

## 6. Decision readiness

Only after the offline projection cycle passes may a new Recommendation assess:

```text
CE_G14_EXECUTION_DECISION_READY=true|false
```

The projection PASS would prove a bounded, deterministic, provenance-preserving common input. It
would not authorize the four model requests, two public artifact GETs or technical reuse.

## 7. Non-authorizations

This Recommendation does not authorize:

- projection creation or offline validation;
- CE-G14 execution Decision, model requests, public fetch or technical reuse;
- credential read, Provider onboarding or cost commitment;
- website, DBOS, SAEE or CE-G13 package changes;
- Runtime, Agent, Entity, Capability, Permission or Evidence Truth;
- PR, merge, release, deployment, offering, certification, Standard Ready or Production Ready;
- customer adoption, market demand, Authority or Ownership changes.

```text
Recommendation != Decision
Decision != Execution
Evidence != Truth
Evaluation != Authority
Capability != Permission
```
