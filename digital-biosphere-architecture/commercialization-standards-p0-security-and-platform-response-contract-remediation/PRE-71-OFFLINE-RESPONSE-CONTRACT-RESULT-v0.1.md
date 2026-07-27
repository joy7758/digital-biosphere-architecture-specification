# PRE-71 Offline Response Contract Result v0.1

## Result

```text
PRE71_DECISION_RECORDED=true
PRE71_OFFLINE_EXECUTION_COMPLETED=true
STRICT_RESPONSE_CONTRACT_CANDIDATE_CREATED=true
CREDENTIAL_ACCOUNTING_PROFILE_CREATED=true
CONTRACT_SCHEMA_VALID=true
POSITIVE_CASES_PASS=2/2
NEGATIVE_CASES_REJECTED=8/8
LIVE_MODEL_REQUESTS=0
STANDARD_READY=false
```

PRE-71 completed the authorized offline-only design. It did not retry PRE-70,
read a credential, inspect a raw provider response or modify the target
implementation.

## Contract Disposition

The Development candidate retains one deterministic boundary:

```text
ASSISTANT_CONTENT
  -> one direct JSON object
  -> frozen Schema
  -> exact role/model/target/question binding
  -> explicit non-claims
  -> sanitized review input
```

It rejects:

- Markdown code fences;
- non-whitespace prefix or suffix text;
- multiple JSON values or non-object top levels;
- duplicate object keys and non-finite numbers;
- unbounded size/depth/items/strings;
- substring extraction, repair, coercion or missing-field synthesis;
- automatic retry or model fallback after contract failure.

Leading and trailing JSON whitespace are allowed only for the four JSON
whitespace code points.

## Provider Capability Gate

No Provider structured-output capability is declared proven.

Each future lane must bind evidence to:

```text
provider + endpoint + model + request shape + observed/version time
```

Official documentation is preferred. If it is insufficient, a separately
authorized bounded preflight must produce at least three sequential direct
object responses with zero fence, prefix/suffix, extraction or repair. Prompt
wording alone is not capability evidence.

Current statuses remain:

```text
QIANFAN=PROVIDER_RESPONSE_CONTRACT_UNPROVEN
QWEN=PROVIDER_RESPONSE_CONTRACT_UNPROVEN_FOR_PRE71
```

## Credential Accounting

The ambiguous `credential_value_reads` counter is decomposed into:

1. configured credential identifiers;
2. values accessed in process memory;
3. authorization values emitted to the authorized TLS client;
4. values printed;
5. values persisted;
6. values exposed outside authorized transport.

An authenticated request requires non-zero in-memory access and TLS header
emission. Neither fact automatically means that the secret was printed,
persisted or exposed.

## Validation

```text
CONTRACT_SCHEMA_VALID=true
FIXTURES=10
POSITIVE_PASS=2/2
NEGATIVE_REJECTED=8/8
VALIDATOR_ATTEMPTS=2
```

The first one-off validator attempt contained a local double-inversion error:
it correctly rejected the first negative input, then inverted that result
again. No contract or fixture was changed. The corrected validator logic passed
all ten cases. This harness error is retained rather than hidden.

The eight required negative cases reject:

- code-fenced JSON;
- prefix/suffix prose;
- extraction or repair;
- an unproven Provider capability claim;
- an authenticated request with zero in-memory credential access;
- automatic exposure inference from in-memory access;
- platform PASS as formal Security Review;
- a Development contract candidate as an adopted Standard.

## Target Integrity and Caps

```text
TARGET_COMMIT_BEFORE=0030077f29c37145a306b72e7083345eb76b504a
TARGET_COMMIT_AFTER=0030077f29c37145a306b72e7083345eb76b504a
TARGET_REMOTE_COMMIT_AFTER=0030077f29c37145a306b72e7083345eb76b504a
TARGET_DIRTY_AFTER=0
TARGET_WRITES=0

LIVE_MODEL_REQUESTS=0
CREDENTIAL_VALUE_READS=0
RAW_PROVIDER_RESPONSE_READS=0
EXTERNAL_NETWORK_REQUESTS=0
DBOS_WRITES=0
SAEE_WRITES=0
RUNTIME_CREATIONS=0
AGENT_CREATIONS=0
ENTITY_CREATIONS=0
PERMISSION_CREATIONS=0
RELEASE_ACTIONS=0
```

## Gate Result

```text
OFFLINE_CONTRACT_DESIGN_GATE=PASS
PROVIDER_CAPABILITY_GATE=NOT_EVALUATED
LIVE_AGENT_REVIEW_GATE=NOT_AUTHORIZED_NOT_EXECUTED
FORMAL_HUMAN_SECURITY_REVIEW_GATE=NOT_SATISFIED
STANDARD_GATE=NOT_SATISFIED
OVERALL=PASS_BOUNDED_OFFLINE_DESIGN_ONLY
```

## Next Action

```text
NEXT_RECOMMENDATION=
PREPARE_PRE72_OFFICIAL_PROVIDER_STRUCTURED_OUTPUT_CAPABILITY_EVIDENCE_ACQUISITION_RECOMMENDATION

PRE72_EXTERNAL_REQUEST_AUTHORIZED=false
PRE72_LIVE_MODEL_REQUEST_AUTHORIZED=false
```

PRE-72 should first verify current official Provider documentation for the exact
endpoint/model/request-shape claim. Any bounded preflight or live review remains
a separate material action and requires a new exact Decision.

## Truth Boundaries

```text
PROMPT_REQUESTING_JSON_NE_STRUCTURED_OUTPUT_CAPABILITY
OUTER_JSON_NE_DIRECT_ASSISTANT_JSON
EXTRACTABLE_JSON_NE_DIRECT_JSON
IN_MEMORY_SECRET_ACCESS_NE_SECRET_EXPOSURE
OFFLINE_CONTRACT_DESIGN_NE_PROVIDER_CONFORMANCE
SCHEMA_VALID_NE_STANDARD_ADOPTION
AGENT_REVIEW_NE_FORMAL_HUMAN_SECURITY_REVIEW
PROVIDER_SUPPORTED=false
STANDARD_READY=false
RELEASE_AUTHORIZED=false
```
