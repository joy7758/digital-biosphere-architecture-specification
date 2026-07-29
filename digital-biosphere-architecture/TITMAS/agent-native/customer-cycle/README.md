# Agent Customer Response Capture

中文：智能体客户响应捕获。

This bounded observability component prevents a dispatched model request from
being confused with a completed or valid Agent result. It is Provider-neutral,
uses only the Python standard library and owns no network client.

## Machine entry

- Capture module: [`response_capture.py`](response_capture.py)
- Audit envelope Schema:
  [`response-capture-envelope.schema.json`](response-capture-envelope.schema.json)
- Deterministic tests:
  [`../tests/test_response_capture.py`](../tests/test_response_capture.py)

Run:

```bash
python3 -m unittest TITMAS/agent-native/tests/test_response_capture.py -v
```

## Binding contract

Before an injected transport may run:

```text
CAPTURE_LAYER_READY=true
ATTEMPT_RECORD_DURABLE=true
REQUEST_SHAPE_PREFLIGHT=PASS
CAPTURE_DESTINATION_PREFLIGHT=PASS
```

After a valid response:

```text
RESPONSE_ENVELOPE_FINALIZED=true
RETURNED_MODEL_CAPTURED=true
MODEL_IDENTITY_MATCH=true
DISCOVERY_CONTRACT_PARSED=true
```

Any failure keeps downstream implementation, Issue, PR and Reviewer stages
closed. The component computes retry eligibility but never retries.

## Durable capture

Every envelope update uses a same-directory temporary file, file flush,
`fsync(file)`, `os.replace` and `fsync(parent_directory)`. A raw response body
is first written to a `0600` temporary spool outside Git. Successful or
classified non-crash completion deletes the spool. Crash recovery preserves
the body hash, length and known model identity while returning
`FAILED_RECOVERY_REQUIRED`.

## Boundaries

```text
RESPONSE_CAPTURE_IS_OBSERVABILITY_SUPPORT=true
RESPONSE_CAPTURE_IS_RUNTIME=false
RESPONSE_CAPTURE_IS_PROVIDER_SDK=false
RESPONSE_ENVELOPE_IS_EVIDENCE_TRUTH=false
AUTO_RETRY=false
REAL_MODEL_CALLS_IN_TESTS=0
```

Transport failure is not Agent failure. Parse failure is not Agent abstention.
`requested_model` equals `returned_model` only after explicit verification.
