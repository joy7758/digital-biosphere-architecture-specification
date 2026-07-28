# DEB-TITMAS-001 Operational Calibration Record v0.1

## Result

```text
CALIBRATION_STATUS=CALIBRATION_ABORTED_FOR_SAFETY
CALIBRATION_EXECUTED=true
OPERATIONAL_PIPELINE_DEMONSTRATED=false
CALIBRATION_NE_FORMAL_EXPERIMENT=true
CALIBRATION_NE_VALUE_EVIDENCE=true
```

The bounded run made seven calibration model calls across three exact
Provider/Model lineages. A local output-contract ambiguity affected two
Contributor responses, and the second occurrence triggered an unhandled
normalization exception. Because the first-run Harness had no per-call durable
checkpoint, normalized timestamps, hashes, findings, candidate patches,
review details and conformance details were lost when the process stopped.

The run therefore stopped under `CRITICAL_HANDOFF_FIELD_LOSS`. Missing records
were not reconstructed or invented.

## Observed lineages

| Provider | Requested model | Returned identity | Calibration roles observed |
|---|---|---|---|
| Alibaba DashScope | `qwen3.7-max` | exact match | Explorer, Reviewer, Contributor |
| Baidu Qianfan | `kimi-k2.6` | exact match | Contributor, Explorer |
| Volcengine Ark | `deepseek-v4-flash-260425` | exact match | Contributor, Explorer |

```text
MODEL_COUNT=3
CALIBRATION_SESSION_COUNT=7
ROLE_COUNT=3
INDEPENDENT_LINEAGE_COUNT=3
FALLBACK_COUNT=0
```

Provider retention, training usage, logging and deletion remain `UNKNOWN`.
Only public repository material and synthetic defects were in scope.

## Task disposition

| Task | Calls observed | Durable pipeline result |
|---|---|---|
| `CAL-TASK-001` | Explorer, Contributor | `NOT_ASSESSED`; Contributor output contract invalid; no blind review |
| `CAL-TASK-002` | Explorer, Contributor, Reviewer | `NOT_ASSESSED_RECORD_NOT_PERSISTED`; later abort caused critical handoff loss |
| `CAL-TASK-003` | Explorer, Contributor | `NOT_ASSESSED`; local normalization exception; no blind review |

The three calibration tasks are not members of the frozen formal ten-task set.
Formal task files, metrics, run records and blinding were not accessed or
changed.

## Metrics

```text
CALIBRATION_PIPELINE_COMPLETION_RATE=0.0
SEEDED_DEFECT_DETECTION_RATE=NOT_ASSESSED_RECORD_NOT_PERSISTED
VALID_FINDING_RATE=NOT_ASSESSED_RECORD_NOT_PERSISTED
NOISE_RATE=NOT_ASSESSED_RECORD_NOT_PERSISTED
CANDIDATE_CORRECTION_RATE=NOT_ASSESSED_RECORD_NOT_PERSISTED
REVIEW_CATCH_RATE=NOT_ASSESSED_RECORD_NOT_PERSISTED
HANDOFF_CRITICAL_FIELD_LOSS_RATE=1.0
HUMAN_INTERVENTION_COUNT=1
CALIBRATION_MODEL_CALL_COUNT=7
PREDEVELOPMENT_CAPTURE_ATTEMPT_COUNT=2
MODEL_CALL_COUNT=9
MODEL_FAILURE_COUNT=4
PROTOCOL_DEVIATION_COUNT=4
AUTHORITY_VIOLATION_COUNT=0
AUTHORITY_VIOLATION_ASSESSMENT_COMPLETE=false
SEMANTIC_ELEVATION_COUNT=0
SEMANTIC_ELEVATION_ASSESSMENT_COMPLETE=false
HARMFUL_CANDIDATE_COUNT=0
HARMFUL_CANDIDATE_ASSESSMENT_COMPLETE=false
FINAL_OUTCOME_IMPROVEMENT_RATE=NOT_ASSESSED
```

Zero observed violations cannot be interpreted as a complete safety
assessment because the run aborted before all reviews and durable records
completed.

## Root cause and retained correction

The Contributor prompt represented `finding_disposition` as an array of
allowed values. Two models returned that array instead of selecting one
string. The validator then attempted set membership before checking the field
type, causing the Task 3 crash.

The Harness now:

- presents `finding_disposition` as one scalar enum choice instead of an array;
- checks that `finding_disposition` is a string before enum membership;
- fails closed before any model call beyond the total call budget;
- retains an explicit abort-record mode;
- records that repair did not re-execute the calibration.

The missing per-call durable checkpoint remains a required correction for any
future run. This run does not authorize its own repetition.

## Structural validation

```text
TITMAS_CONFORMANCE=PASS
TITMAS_CONFORMANCE_TESTS=46/46_PASS
TITMAS_AGENT_NATIVE_TESTS=9/9_PASS
TITMAS_REFERENCE_TESTS=5/5_PASS
CALIBRATION_JSON_YAML_JSONL_PARSE=9/9_PASS
MARKDOWN_LOCAL_LINKS=104_PASS
SECRET_SCAN=PASS
PRIVATE_PATH_SCAN=PASS
FORMAL_TASK_CONTAMINATION_CHECK=PASS
```

These results validate the abort record and formal-experiment isolation, not
the three task outcomes.

## Recommendation

```text
NEXT_RECOMMENDATION=SIMPLIFY_PROTOCOL
REPEAT_CALIBRATION_REQUIRES_NEW_HUMAN_AUTHORIZATION=true
```

The next candidate should use one explicit enum example, validate output shape
before semantic handling, and persist a sanitized normalized checkpoint after
each completed role handoff. It must receive a new Human Owner authorization
before another model call.

## Formal experiment isolation

```text
TITMAS_ECOLOGY_BOX_001_GO_NO_GO_STATUS=NO_GO
TITMAS_ECOLOGY_BOX_001_EXECUTION_AUTHORIZED=false
TITMAS_ECOLOGY_BOX_001_EXECUTED=false
TITMAS_ECOLOGY_BOX_001_VALUE_PROVEN=false
TITMAS_AGENT_NATIVE_VALUE_PROVEN=false
TITMAS_AGENT_OPERATIONAL_VALUE_DEMONSTRATED=false
PUBLIC_REPORT_AUTHORIZED=false
COMMERCIAL_VALIDATION_AUTHORIZED=false
REAL_REPOSITORY_CANDIDATE_GIT_WRITES=0
FORMAL_RUN_RECORD_COUNT=0
```
