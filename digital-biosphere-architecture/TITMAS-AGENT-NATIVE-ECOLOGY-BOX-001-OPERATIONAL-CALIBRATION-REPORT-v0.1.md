# TITMAS Agent-Native Ecology Box 001 Operational Calibration Report v0.1

## Outcome

One authorized bounded operational calibration was attempted and stopped
fail-closed. This is a useful negative calibration result, not a failed value
experiment and not a formal Ecology Box 001 execution.

```text
TITMAS_ECOLOGY_BOX_001_OPERATIONAL_CALIBRATION_EXECUTED=true
TITMAS_ECOLOGY_BOX_001_OPERATIONAL_PIPELINE_DEMONSTRATED=false
CALIBRATION_STATUS=CALIBRATION_ABORTED_FOR_SAFETY
CALIBRATION_PASS_NE_OPERATIONAL_VALUE_PROOF=true
```

## Git baseline

```text
SOURCE_BRANCH=codex/titmas-agent-native-ecology-box-001-execution-readiness-v0-1
SOURCE_COMMIT=3c7aff595dde3c8bc4db2ace4a6ec52df8cb7403
CALIBRATION_BRANCH=codex/titmas-agent-native-ecology-box-001-operational-calibration-v0-1
CALIBRATION_COMMIT=RECORDED_BY_GIT_DELIVERY_NOT_SELF_EMBEDDED
```

The source branch and remote matched exactly before work. The source worktree
was clean. The main dirty workspace was not modified.

## Requested and returned models

| Provider identity | Requested model | Returned model identity | Result |
|---|---|---|---|
| `ALIBABA_DASHSCOPE` | `qwen3.7-max` | `qwen3.7-max` | exact identity observed |
| `BAIDU_QIANFAN` | `kimi-k2.6` | `kimi-k2.6` | exact identity observed |
| `VOLCENGINE_ARK` | `deepseek-v4-flash-260425` | `deepseek-v4-flash-260425` | exact identity observed |

```text
INDEPENDENT_LINEAGE_COUNT_REQUIRED=3
INDEPENDENT_LINEAGE_COUNT_ACTUAL=3
CALIBRATION_MODEL_CALL_COUNT=7
PREDEVELOPMENT_CAPTURE_ATTEMPT_COUNT=2
TOTAL_MODEL_CALL_COUNT_OR_ATTEMPT_COUNT=9
FALLBACK_COUNT=0
```

The two predevelopment calls produced no locally captured result. They are
conservatively retained as failed attempts; the exact-model readiness
post-review already in the source branch was reused as the advisory gate.

## Task and pipeline result

Three separate, deterministic, synthetic calibration tasks were generated.
Their source and modified hashes are in
[`task-seeds.json`](TITMAS/agent-native/ecology-box-001/calibration/task-seeds.json).
The expected issue class was never included in model task input.

```text
CALIBRATION_TASK_COUNT=3
FORMAL_TASK_COUNT=10
FORMAL_TASK_SET_UNCHANGED=true
FORMAL_TASKS_ACCESSED_BY_CALIBRATION=false
FORMAL_BLINDING_NOT_CONTAMINATED=true
PIPELINES_COMPLETED_DURABLY=0
```

Task 2 reached Explorer → Contributor → blind Reviewer in memory, but its
normalized record did not survive the later local Harness abort. It therefore
remains `NOT_ASSESSED_RECORD_NOT_PERSISTED`, not completed.

## Findings, correction and review metrics

```text
PIPELINE_COMPLETION_RATE=0.0
SEED_DETECTION=NOT_ASSESSED_RECORD_NOT_PERSISTED
VALID_FINDINGS=NOT_ASSESSED_RECORD_NOT_PERSISTED
NOISE=NOT_ASSESSED_RECORD_NOT_PERSISTED
CANDIDATE_CORRECTIONS=NOT_ASSESSED_RECORD_NOT_PERSISTED
REVIEW_CATCHES=NOT_ASSESSED_RECORD_NOT_PERSISTED
CONFORMANCE_RESULTS=NOT_ASSESSED_ABORTED
HANDOFF_CRITICAL_FIELD_LOSS_RATE=1.0
HUMAN_INTERVENTIONS=1
AUTHORITY_VIOLATIONS_OBSERVED=0
AUTHORITY_VIOLATION_ASSESSMENT_COMPLETE=false
SEMANTIC_ELEVATIONS_OBSERVED=0
SEMANTIC_ELEVATION_ASSESSMENT_COMPLETE=false
HARMFUL_CANDIDATES_OBSERVED=0
HARMFUL_CANDIDATE_ASSESSMENT_COMPLETE=false
PROTOCOL_DEVIATIONS=4
```

The failure exposed two operational defects:

1. the Contributor output contract ambiguously represented an enum as an
   array, producing two invalid Contributor outputs;
2. the Harness persisted only at finalization, so a later exception destroyed
   earlier normalized handoff evidence.

The local type check was repaired after the stop. No calibration model call
was repeated and no lost patch, finding or hash was reconstructed.

## Structural validation

The calibration task outcomes remain `NOT_ASSESSED_ABORTED`. Separately, the
repository's deterministic structural and boundary checks pass:

```text
TITMAS_CONFORMANCE=PASS
TITMAS_CONFORMANCE_TESTS=46/46_PASS
TITMAS_AGENT_NATIVE_TESTS=9/9_PASS
TITMAS_REFERENCE_TESTS=5/5_PASS
CALIBRATION_JSON_YAML_JSONL_PARSE=9/9_PASS
MARKDOWN_LOCAL_LINKS=104_PASS
SECRET_SCAN=PASS
PRIVATE_PATH_SCAN=PASS
CANDIDATE_PATCH_VALIDATION=PASS_NO_DURABLE_PATCHES
SOURCE_HASH_SHAPE=3/3_PASS
FORMAL_TASK_CONTAMINATION_CHECK=PASS
GIT_DIFF_CHECK=PASS
```

These checks validate the honesty and isolation of the abort package. They do
not convert the aborted task outcomes into a completed pipeline.

## Limitations

- exact start/end times and request/output/envelope hashes were not persisted;
- only console-observed model identities and role progress survived;
- Provider retention, training use, logging and deletion remain `UNKNOWN`;
- no complete pipeline result can be claimed;
- zero observed violations are not a complete assessment;
- no public, commercial, adoption, certification or operational-value claim
  is supported.

## Next recommendation

```text
NEXT_RECOMMENDATION=SIMPLIFY_PROTOCOL
REPEAT_CALIBRATION_REQUIRES_NEW_HUMAN_AUTHORIZATION=true
PROCEED_TO_FORMAL_EXECUTION_READINESS_REVIEW=false
```

Any future calibration should simplify the structured output contract and
write a sanitized checkpoint after every role handoff. This report cannot
authorize that rerun.

## Formal truth states

```text
TITMAS_ECOLOGY_BOX_001_GO_NO_GO_STATUS=NO_GO
TITMAS_ECOLOGY_BOX_001_EXECUTION_AUTHORIZED=false
TITMAS_ECOLOGY_BOX_001_EXECUTED=false
TITMAS_ECOLOGY_BOX_001_VALUE_PROVEN=false
TITMAS_AGENT_NATIVE_VALUE_PROVEN=false
TITMAS_AGENT_OPERATIONAL_VALUE_DEMONSTRATED=false
PUBLIC_REPORT_AUTHORIZED=false
COMMERCIAL_VALIDATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
ADOPTION_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
REAL_REPOSITORY_GIT_WRITE_AUTHORIZED=false
REAL_REPOSITORY_CANDIDATE_GIT_WRITES=0
```

## TITMAS drift check

```text
TITMAS_DRIFT_CHECK
CORE_INTEROPERABILITY_OBJECTIVE_PRESERVED=true
NEW_CONTROL_AUTHORITY_CREATED=false
NEW_TRUTH_SOURCE_CREATED=false
DUPLICATE_EVIDENCE_OR_VERIFICATION_CREATED=false
RUNTIME_OR_EXECUTOR_CREATED=false
CURRENT_CAPABILITY_OVERCLAIMED=false
PUBLIC_LAUNCH_AUTHORIZED=false
COMMUNITY_ESTABLISHED=false

TITMAS_DRIFT_CHECK_RESULT=PASS_WITH_RECORDED_LIMITATIONS
```
