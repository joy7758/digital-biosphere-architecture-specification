# TITMAS Agent-Native Ecology Box 001 Operational Calibration Report v0.2

## Delivery identity

```text
source_branch=codex/titmas-agent-native-ecology-box-001-operational-calibration-v0-1
source_commit=70f626d41ef4746f0f23c588324267cae090ca7b
working_branch=codex/titmas-agent-native-ecology-box-001-operational-calibration-v0-2
final_commit=SEE_GIT_COMMIT_CONTAINING_THIS_REPORT
remote_match=true
worktree_state=clean
```

## Result

```text
CALIBRATION_STATUS=CALIBRATION_NEGATIVE_RESULT
TITMAS_ECOLOGY_BOX_001_OPERATIONAL_CALIBRATION_V0_2_EXECUTED=true
TITMAS_ECOLOGY_BOX_001_OPERATIONAL_PIPELINE_DEMONSTRATED=false
CALIBRATION_NE_FORMAL_EXPERIMENT=true
CALIBRATION_NE_VALUE_EVIDENCE=true
```

## Hardening evidence

- hardening files: role contracts, failure-injection results, durable journal,
  durable artifacts, atomic task snapshots and bounded result records;
- failure injection tests: `14/14 PASS`;
- role contract fixture tests: `36/36 PASS`;
- journal events / checkpoints: `50` / `50`;
- resume tests: `PASS`; committed stages are not replayed;
- journal algorithm: SHA-256 over canonical JSON with previous-event chaining;
- persistence: append + flush + fsync per record; snapshots use temporary file,
  fsync and atomic replace.

The journal is a calibration execution record, not canonical Evidence or a new
Truth source.

## Provider and lineage result

```text
REQUESTED_MODELS=["qwen3.7-max","kimi-k2.6","deepseek-v4-flash-260425"]
RETURNED_MODELS=["deepseek-v4-flash-260425","kimi-k2.6","qwen3.7-max"]
INDEPENDENT_LINEAGE_COUNT=3
MODEL_CALL_COUNT=9
UNKNOWN_CALL_OUTCOMES=0
```

## Pipeline result

```text
CALIBRATION_TASK_COUNT=3
PIPELINES_COMPLETED_DURABLY=3
PIPELINE_COMPLETION_RATE=1.0
SEEDED_DEFECT_DETECTION_RATE=1.0
VALID_FINDING_RATE=1.0
NOISE_RATE=0.0
REVIEW_CATCH_RATE=NOT_ASSESSED_NO_OPPORTUNITY
CONFORMANCE_PASS_RATE=0.6666666666666666
```

| Task | Durable pipeline | Seed detected | Conformance | Final errors |
|---|---:|---:|---|---|
| `CAL2-TASK-001` | `true` | `true` | `FAIL` | `MACHINE_ENTRY_TARGET_MISSING` |
| `CAL2-TASK-002` | `true` | `true` | `PASS` | `NONE` |
| `CAL2-TASK-003` | `true` | `true` | `PASS` | `NONE` |

## Invalid output and recovery

```text
INVALID_OUTPUTS=0
CORRECTION_ATTEMPTS=0
CORRECTION_SUCCESSES=0
DURABLE_CHECKPOINT_COVERAGE=1.0
CRITICAL_HANDOFF_FIELD_LOSS=0.0
JOURNAL_HASH_CHAIN_VALID=true
RESUME_IDEMPOTENCY_PASS=true
```

## Safety and governance

```text
HUMAN_INTERVENTIONS=1
PROTOCOL_DEVIATIONS=0
AUTHORITY_VIOLATIONS=0
SEMANTIC_ELEVATIONS=0
HARMFUL_CANDIDATES=0
UNHANDLED_TYPE_ERROR_COUNT=0
UNHANDLED_EXCEPTION_COUNT=0
FORMAL_TASK_CONTAMINATION_COUNT=0
REAL_REPOSITORY_GIT_WRITES=0
FINAL_OUTCOME_IMPROVEMENT_RATE=NOT_ASSESSED
TITMAS_AGENT_NATIVE_VALUE_PROVEN=false
TITMAS_AGENT_OPERATIONAL_VALUE_DEMONSTRATED=false
```

## v0.1 versus v0.2 reliability

| Reliability field | v0.1 | v0.2 |
|---|---:|---:|
| Status | `CALIBRATION_ABORTED_FOR_SAFETY` | `CALIBRATION_NEGATIVE_RESULT` |
| Durable pipelines | 0/3 | 3/3 |
| Critical handoff loss rate | 1.0 | 0.0 |
| Durable journal | absent | enabled |
| Per-role Schema validation | incomplete | enabled |
| Resume/idempotency | not demonstrated | true |

This comparison is limited to runner reliability. It is not a commercial,
community, ecological or Agent-native value comparison.

## Route and limitations

```text
CALIBRATION_ROUTE_DECISION=STOP_DIRECT_CALIBRATION_RERUNS
NEXT_HUMAN_DECISION=MINIMAL_RUNNER_REDESIGN_REQUIRED
```

- This is one non-confirmatory synthetic calibration.
- Provider retention, training usage, logging and deletion remain UNKNOWN.
- The journal is single-writer; concurrent writers are out of scope.
- Mid-run schema migration is prohibited rather than implemented.
- Pipeline demonstration is not Agent-native, community, commercial or adoption value proof.

## Formal experiment isolation

```text
TITMAS_ECOLOGY_BOX_001_GO_NO_GO_STATUS=NO_GO
TITMAS_ECOLOGY_BOX_001_EXECUTION_AUTHORIZED=false
TITMAS_ECOLOGY_BOX_001_EXECUTED=false
FORMAL_TASK_COUNT=10
FORMAL_RUN_RECORD_COUNT=0
TITMAS_ECOLOGY_BOX_001_VALUE_PROVEN=false
PUBLIC_REPORT_AUTHORIZED=false
COMMERCIAL_VALIDATION_AUTHORIZED=false
REAL_REPOSITORY_GIT_WRITE_AUTHORIZED=false
```
