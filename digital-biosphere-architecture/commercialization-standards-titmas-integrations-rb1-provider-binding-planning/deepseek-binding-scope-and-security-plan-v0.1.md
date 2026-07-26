# DeepSeek Binding Scope and Security Plan v0.1

## Status

```text
PLAN_STATUS=PREPARED_NOT_REVIEWED
PROVIDER_CANDIDATE=DEEPSEEK_OPENAI_COMPATIBLE_CHAT_COMPLETIONS
TRANSPORT_CANDIDATE=httpcore==1.0.9
TARGET_REPOSITORY_CHANGED=false
PROVIDER_REQUEST_EXECUTED=false
CREDENTIAL_READ=false
IMPLEMENTATION_AUTHORIZED=false
```

This is an agent-readable planning contract for a possible RB1 Provider binding. It is not a
Provider implementation, support statement, conformance result or security approval.

## Candidate Boundary

| Field | Frozen candidate |
|---|---|
| Base URL | `https://api.deepseek.com` |
| Endpoint | `POST /chat/completions` |
| Model | `deepseek-v4-pro` |
| Stream | `false` |
| Thinking | `disabled` |
| Response format | `json_object` |
| Credential identifier | `DEEPSEEK_API_KEY` |
| Transport | `httpcore==1.0.9` |
| Transport mode | synchronous HTTP/1.1 direct |

Only the identifier `DEEPSEEK_API_KEY` is part of this plan. The credential value is neither read
nor retained.

## P0 Gap

HTTPCore trace exposes TCP connection events but not a separate DNS event. Therefore DNS and TCP
cannot be honestly split into P0 and P1 with this candidate alone.

```text
P0_DIRECT_OBSERVABILITY_WITH_CANDIDATE_TRANSPORT=false
P0_SYNTHETIC_PASS_FORBIDDEN=true
PROVIDER_BINDING_IMPLEMENTATION_RECOMMENDATION_BLOCKED=true
```

The next review must recommend one bounded resolution: resolver observation, auditable custom
network backend, different transport, or an explicit unsupported P0 profile. None is adopted here.

## Sensitive Data Boundary

Never retain:

- credential values or Authorization header values;
- request or response bodies;
- prompts, review content, tool content or hidden reasoning;
- raw Provider error bodies;
- environment dumps.

Only bounded byte counts, approved enum values, SHA-256 digests and sanitized references or
timestamps may be retained.

## Candidate Limits

| Limit | Candidate |
|---|---:|
| Pool timeout | 5 seconds |
| Connect timeout | 10 seconds |
| Write timeout | 30 seconds |
| Read timeout | 60 seconds |
| Total deadline | 90 seconds |
| Serialized request | 131072 bytes |
| Response body | 1048576 bytes |
| Output tokens | 4096 |
| Choices | 1 |

No timeout may be infinite. Response size must be enforced cumulatively before full buffering.

## Fail-Closed Rules

- no retry;
- no fallback;
- no alias inference;
- no model substitution;
- no JSON repair;
- no redirect or proxy;
- no alternate host or IP literal;
- first failure is retained without raw body retention;
- Schema pass does not prove Provider correctness, conformance or production readiness.

## Next Gate

Prepare a separate recommendation for four sequential reviews:

1. Agent developer;
2. Agent recommender / machine customer;
3. integration maintainer;
4. security reviewer.

The review remains unauthorized until that recommendation receives its own Decision.
