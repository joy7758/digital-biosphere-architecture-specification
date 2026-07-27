# PRE-70 Explicit Docker Host and Platform Validation Result v0.1

## Result

```text
PRE70_DECISION_RECORDED=true
PRE70_EXECUTION_STARTED=true
PRE70_CONTEXT_AND_CONFIG_CONTROL_GATE=PASS
PRE70_PLATFORM_GATE=PASS_BOUNDED_TWO_LINUX_AMD64_OBSERVATIONS
PRE70_AGENT_REVIEW_GATE=FAIL_CLOSED_NOT_DIRECT_JSON
PRE70_OVERALL=FAIL_CLOSED_AFTER_PLATFORM_PASS
FORMAL_HUMAN_SECURITY_REVIEW_COMPLETE=false
STANDARD_READY=false
```

PRE-70 removed the PRE-69 daemon-selection blocker without using the global
Docker context. The run bound an ephemeral anonymous `DOCKER_CONFIG` to Colima
start/stop, selected the default Colima socket through explicit `DOCKER_HOST`,
pulled both exact public digests and completed both network-none, read-only
Linux/amd64 lanes.

The first agent-assisted review transport returned assistant content, but the
content included a Markdown code fence. The frozen contract required one direct
JSON object and prohibited extraction or repair. The run therefore stopped
fail-closed, did not retry Qianfan and did not call Qwen.

## Platform Results

| Lane | Result | Unit suite | Independent rehearsal |
|---|---|---|---|
| `PFM-LINUX-311-R2` | `PASS_BOUNDED_OBSERVATION` | 92 tests run, 1 expected skip, suite `OK` | 7/7 PASS |
| `PFM-LINUX-314-R2` | `PASS_BOUNDED_OBSERVATION` | 92 tests run, 1 expected skip, suite `OK` | 7/7 PASS |

The skipped case in each lane was the same optional `jsonschema is unavailable`
serialization check. The independent validator still completed all seven
frozen conformance fixtures per lane.

Both containers used:

- `linux/amd64`;
- `--network none`;
- a read-only root filesystem and read-only source mount;
- all Linux capabilities dropped and `no-new-privileges`;
- bounded PID, memory, CPU and tmpfs controls.

These observations do not establish all-Linux support, native-thread fork
safety, real-network conformance or production safety.

## Agent Review Result

| Lane | Result | Retained boundary |
|---|---|---|
| `PRE70-QF-SECURITY-01` | `FAIL_CLOSED_ASSISTANT_CONTENT_CODE_FENCE` | No response extraction, repair or retry; no response content persisted |
| `PRE70-QWEN-SECURITY-02` | `NOT_EXECUTED_DUE_PRIOR_AGENT_CONTRACT_FAILURE` | Sequential stop condition preserved |

The Qianfan request reached the response-processing path and produced an outer
JSON envelope with assistant content. Exact HTTP status and returned model were
not persisted before the direct-JSON contract failure. No favorable or adverse
security verdict is inferred.

## Configuration and Cleanup

```text
GLOBAL_DOCKER_CONFIG_METADATA_ENTRIES_BEFORE=110
GLOBAL_DOCKER_CONFIG_METADATA_ENTRIES_AFTER=110
GLOBAL_DOCKER_CONFIG_METADATA_MATCH=true
GLOBAL_DOCKER_CONFIG_FILE_CONTENT_READS=0
GLOBAL_DOCKER_CONFIG_PATHS_OR_METADATA_PERSISTED=false
DIRECT_CODEX_GLOBAL_CONFIG_WRITE_COMMANDS=0
GLOBAL_CONFIG_REPAIR_ATTEMPTS=0
COLIMA_FINAL_STATE=NOT_RUNNING
TEMP_ROOTS_REMAINING=0
TARGET_WRITES=0
```

The metadata-only guard matched before and after the Colima lifecycle. This is
a bounded guard result, not proof that no system call wrote and restored
metadata or bytes.

## Cap Accounting

```text
TEMP_ROOTS_CREATED=1/1
COLIMA_STARTS=1/1
IMAGE_PULL_ATTEMPTS=2/2
IMAGE_PULL_SUCCESSES=2/2
CONTAINER_RUNS=2/2
AGENT_MODEL_REQUESTS=1/2
RETRY=0
FALLBACK=0
MODEL_SUBSTITUTION=0
JSON_EXTRACTION_OR_REPAIR=0
P1_OR_P2_EXECUTIONS=0
PROVIDER_BINDING_ACTIONS=0
RELEASE_ACTIONS=0
```

Two credential identifiers were configured. One credential value was
necessarily consumed in process memory to form the one authenticated provider
request. No credential value, authorization header or private response was
printed or persisted. This exposes a contract-accounting issue: a live
authenticated request cannot truthfully coexist with
`credential_value_reads=0`. Future contracts must count in-memory credential
consumption separately from secret printing or persistence.

## Target Integrity

```text
TARGET_COMMIT_BEFORE=0030077f29c37145a306b72e7083345eb76b504a
TARGET_COMMIT_AFTER=0030077f29c37145a306b72e7083345eb76b504a
TARGET_REMOTE_COMMIT_AFTER=0030077f29c37145a306b72e7083345eb76b504a
TARGET_DIRTY_BEFORE=0
TARGET_DIRTY_AFTER=0
TARGET_HASHES_BEFORE=10/10
TARGET_HASHES_AFTER=10/10
TARGET_WRITES=0
```

## Gate Result

```text
CONTEXT_AND_CONFIG_CONTROL_GATE=PASS
PLATFORM_GATE=PASS_BOUNDED_TWO_LINUX_AMD64_OBSERVATIONS
AGENT_REVIEW_GATE=FAIL_CLOSED_NOT_DIRECT_JSON
FORMAL_HUMAN_SECURITY_REVIEW_GATE=NOT_SATISFIED
STANDARD_GATE=NOT_SATISFIED
OVERALL=FAIL_CLOSED_AFTER_PLATFORM_PASS
```

## Next Action

```text
NEXT_RECOMMENDATION=
PREPARE_PRE71_AGENT_RESPONSE_CONTRACT_AND_CREDENTIAL_ACCOUNTING_DISPOSITION_RECOMMENDATION

PRE70_RETRY_AUTHORIZED=false
PRE71_EXECUTION_AUTHORIZED=false
```

PRE-71 should decide whether strict direct JSON remains mandatory with a
provider-native structured-output mechanism, or whether a separately specified
and independently validated envelope/extraction contract is required. It must
also replace the ambiguous credential-read counter with separate in-memory use,
printing and persistence fields.

## Truth Boundaries

```text
PLATFORM_PASS_NE_FORMAL_SECURITY_REVIEW
TWO_LINUX_AMD64_OBSERVATIONS_NE_LINUX_SUPPORT
NETWORK_NONE_NE_REAL_NETWORK_CONFORMANCE
AGENT_TRANSPORT_COMPLETION_NE_SCHEMA_VALID_REVIEW
CODE_FENCE_NE_SECURITY_VERDICT
METADATA_MATCH_NE_ZERO_WRITE_PROOF
AUTHENTICATED_REQUEST_NE_SECRET_PERSISTENCE
REFERENCE_IMPLEMENTATION_NE_STANDARD
FORMAL_HUMAN_SECURITY_REVIEW_COMPLETE=false
PROVIDER_SUPPORTED=false
STANDARD_READY=false
RELEASE_AUTHORIZED=false
```
