# Candidate Grounding and Incremental Validation Report v0.1

## Scope

This deterministic redesign binds candidate references to the exact frozen
repository tree before Reviewer handoff. It adds:

- exact local resource resolution;
- Contributor abstention when no valid target can be resolved;
- Candidate Preflight before Reviewer;
- incremental conformance before Reviewer;
- Reviewer evidence obligations and abstention;
- grounded Handoff fields;
- corrected Review Catch measurement.

It does not call a model, run Calibration v0.3, execute Ecology Box 001, or
write a real repository candidate.

## Preflight order

```text
Contributor Output
→ Role Contract Validation
→ Scope Validation
→ Resource Resolution
→ Candidate Patch Application in Isolated Copy
→ Reference Re-resolution
→ Incremental Conformance
→ Preflight Result
→ Reviewer
→ Final Conformance
```

`PREFLIGHT` is the only field spelling used by the v1.1 machine contract.

## Historical replay

The immutable Calibration v0.2 Task 1 candidate references:

```text
TITMAS/agent-native/ecology-box-001/calibration/calibration-v0.2.json
```

The exact source tree at
`ecd5d7f041fc3ff2213cb87a85be49f46e8d9399` resolves it as `NOT_FOUND`.
The deterministic replay therefore returns `PREFLIGHT_STATUS=REVISION_REQUIRED`
and `REVIEW_STAGE_REACHED=false`.

```text
CAL2_TASK_001_INVALID_REFERENCE_REJECTED_BEFORE_REVIEW=true
```

The historical candidate, Reviewer `PASS`, final `FAIL`, journal and route
decision are unchanged.

## Validation result

```text
CANDIDATE_GROUNDING_TESTS=20/20_PASS
REVIEW_METRIC_TESTS=6/6_PASS
NONEXISTENT_REFERENCE_REJECTED_BEFORE_REVIEW=true
REVIEW_PASS_WITH_UNRESOLVED_REFERENCE_REJECTED=true
CONTRIBUTOR_ABSTENTION_PATH_PASS=true
MODEL_CALL_COUNT=0
CALIBRATION_V0_3_AUTHORIZED=false
CALIBRATION_V0_3_EXECUTED=false
```

The machine result is
[`candidate-grounding-results-v0.1.json`](candidate-grounding-results-v0.1.json).

## Boundaries

```text
RESOURCE_RESOLUTION_RECEIPT_NE_DBOS_VERIFICATION=true
RESOURCE_RESOLUTION_RECEIPT_NE_EVIDENCE_TRUTH=true
LOCAL_SNAPSHOT_RESOLUTION_NE_CANONICAL_EXISTENCE_AUTHORITY=true
DETERMINISTIC_PASS_NE_MODEL_PIPELINE_PROOF=true
GROUNDING_PASS_NE_AGENT_NATIVE_VALUE_PROOF=true
FINAL_CONFORMANCE_REMAINS_REQUIRED=true
```
