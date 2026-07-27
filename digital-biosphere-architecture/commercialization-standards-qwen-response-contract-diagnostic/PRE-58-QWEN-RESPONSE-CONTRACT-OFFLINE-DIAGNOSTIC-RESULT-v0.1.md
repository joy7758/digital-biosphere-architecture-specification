# PRE-58 Qwen Response Contract Offline Diagnostic Result v0.1

```text
RESULT=PASS_CONTRACT_TRANSMISSION_GAP_PROVEN
INPUT_HASHES_MATCHED=4/4
CHECKS_MATCHED=8/8
PROVIDER_NETWORK_REQUESTS=0
LIVE_MODEL_REQUESTS=0
CREDENTIAL_READS=0
SOURCE_MUTATIONS=0
```

## Finding

The PRE-57 plan defined the frozen `provider_fit` enum:

```text
SUITABLE
CONDITIONAL
NOT_SUITABLE
```

The exact enum instruction was present in the actual `prompt_text` for sessions `01` and `02`.
It was absent from session `03`. The runner transmitted only each session's `prompt_text` plus a
generic system instruction; the separate plan contract was not serialized into the request.

Therefore:

```text
CONTRACT_TRANSMISSION_GAP_PROVEN=true
PRIMARY_DIAGNOSTIC=SESSION_03_REQUEST_DID_NOT_TRANSMIT_PROVIDER_FIT_ENUM
MODEL_CAUSALITY_PROVEN=false
```

## Corroborating Observation

Session `03` asked the model to act as a:

```text
bounded, non-production TITMAS machine-review candidate
```

The observed `provider_fit` was:

```text
bounded non-production TITMAS machine-review candidate
```

Both normalize to:

```text
bounded non production titmas machine review candidate
```

This is consistent with prompt copying, but it is not proof of the model's internal causal
process.

## Contract Decision

The response Schema remains correct and unchanged. The defect is in the session-specific request
binding: session `03` omitted a requirement that existed only in the offline plan contract.

A minimal prompt revision candidate inserts:

```text
provider_fit must be SUITABLE, CONDITIONAL, or NOT_SUITABLE.
```

The candidate is prepared but not adopted.

## Non-Effects

```text
PROVIDER_SUPPORTED=false
PROVIDER_INTEGRATION_AUTHORIZED=false
SECURITY_REVIEW_AUTHORIZED=false
SECURITY_REVIEW_COMPLETED=false
IMPLEMENTATION_AUTHORIZED=false
PROMPT_REVISION_ADOPTED=false
LIVE_RERUN_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
STANDARD_READY=false
```

## Next Action

```text
NEXT_ACTION=FORM_EXACT_PROMPT_CONTRACT_REVISION_RECOMMENDATION
```

Any prompt adoption and any live rerun remain separate decisions.
