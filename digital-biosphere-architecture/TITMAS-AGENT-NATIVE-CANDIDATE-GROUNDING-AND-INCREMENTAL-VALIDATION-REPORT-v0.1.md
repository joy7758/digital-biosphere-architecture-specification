# TITMAS Agent-Native Candidate Grounding and Incremental Validation Report v0.1

## Delivery identity

```text
source_repository=joy7758/digital-biosphere-architecture-specification
source_branch=codex/titmas-agent-native-ecology-box-001-operational-calibration-v0-2
source_commit=ecd5d7f041fc3ff2213cb87a85be49f46e8d9399
source_tree=8339d6cb48649288010259c64c224f96b30c0cd8
working_branch=codex/titmas-agent-native-candidate-grounding-v0-1
final_commit=SEE_GIT_COMMIT_CONTAINING_THIS_REPORT
remote_match=true
worktree_state=clean
```

The final commit cannot contain its own Git hash without changing that hash.
The pushed branch head is therefore the canonical `final_commit`; final
delivery verification records the exact value outside this self-referential
field.

## Human decision and scope

```text
DECISION_ID=TITMAS-EB001-CANDIDATE-GROUNDING-D01
DECISION=ACCEPT_DESIGN_AND_DETERMINISTIC_TESTS_ONLY
DECIDED_BY_REF=zhangbin
DESIGN_AND_DETERMINISTIC_VALIDATION_ONLY=true
MODEL_CALL_COUNT=0
CALIBRATION_V0_3_AUTHORIZED=false
CALIBRATION_V0_3_EXECUTED=false
```

Primary repository: DBA. This change is a bounded conformance and contract
redesign. It does not implement DBOS or SAEE and does not create an Agent,
Runtime, Authority, Permission, Evidence Object, Verification Object, Memory
System or formal experiment layer.

## Pre-development Agent Recommendation Gate

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=DETERMINISTIC_CANDIDATE_GROUNDING_AND_PREFLIGHT_REDESIGN
NOT_RECOMMENDED_AS=MODEL_PIPELINE_OR_AGENT_NATIVE_VALUE_PROOF
```

Why it is recommended: Calibration v0.2 directly showed that a structurally
valid candidate could guess a nonexistent machine surface, receive Reviewer
`PASS`, and fail only at final Conformance. Exact frozen-tree resolution,
Preflight and Reviewer receipt obligations address that observed defect.

Remaining gaps and stop conditions:

- no model or multi-agent pipeline was run;
- deterministic PASS does not show operational value;
- any source drift, unresolved required reference, Preflight failure or final
  Conformance failure remains fail-closed;
- Calibration v0.3 still requires a new explicit Human Decision.

## Immutable v0.2 history

The following original blobs were frozen before modification:

| Artifact | Git blob |
|---|---|
| `calibration-report-v0.2.md` | `1991d8e9050935584d708377af9883c7f4496803` |
| `calibration-results-v0.2.json` | `a71df3d74bbcd0a12a1ccad22bcf3658e3826851` |
| `durable-journal.jsonl` | `7a3163da6169cd41d2385cf536d1753d76fe11a8` |
| `role-output-contracts.json` | `9a4089b2900ebc1530145de1296b48ab397dd28f` |

They continue to state:

```text
CALIBRATION_STATUS=CALIBRATION_NEGATIVE_RESULT
PIPELINES_COMPLETED_DURABLY=3
PIPELINE_COMPLETION_RATE=1.0
CONFORMANCE_PASS_RATE=0.6666666666666666
OPERATIONAL_PIPELINE_DEMONSTRATED=false
CALIBRATION_ROUTE_DECISION=STOP_DIRECT_CALIBRATION_RERUNS
CAL2_TASK_001_REVIEW_VERDICT=PASS
CAL2_TASK_001_CONFORMANCE=FAIL
CAL2_TASK_001_ERROR=MACHINE_ENTRY_TARGET_MISSING
```

The append-only metric correction changes no historical artifact. It records
one real Reviewer opportunity, zero catches and one miss:

```text
REVIEW_CATCH_OPPORTUNITY_COUNT=1
REVIEW_CATCH_COUNT=0
REVIEW_MISS_COUNT=1
REVIEW_CATCH_RATE=0.0
REVIEW_CATCH_CLASSIFICATION=MISS_REQUIRED_RESOURCE_GROUNDING_CHECK
NO_OPPORTUNITY=false
```

## Resource resolver

The local resolver reads only:

- the exact authorized Git tree;
- an isolated candidate copy;
- explicitly allowed repository-relative paths.

It rejects absolute paths, `..` escape, out-of-root symlinks, source revision
drift and unsupported reference kinds. It uses exact paths or exact identifier
matches; it does not use similarity or model inference.

Allowed result states:

```text
RESOLVED
NOT_FOUND
AMBIGUOUS
OUT_OF_SCOPE
INVALID_REFERENCE
NOT_ASSESSED
```

A Resource Resolution Receipt is a local conformance artifact:

```text
RESOURCE_RESOLUTION_RECEIPT_NE_DBOS_VERIFICATION=true
RESOURCE_RESOLUTION_RECEIPT_NE_EVIDENCE_TRUTH=true
LOCAL_SNAPSHOT_RESOLUTION_NE_CANONICAL_EXISTENCE_AUTHORITY=true
```

## Contract changes

ContributorCandidate v1.1 adds `candidate_status`, exact
`reference_claims`, `created_resources`, `modified_resources` and
`abstention_reason`. When no target can be grounded, the Contributor must use
one of the bounded abstention states and produce no candidate files.

ReviewerAssessment v1.1 adds reviewed artifact references, Preflight binding,
checks performed, verified resource references, resolution receipt references,
unverified claims and bounded abstention. Reviewer `PASS` requires Preflight
`PASS`, zero unresolved required references and references to all required
post-apply receipts.

HandoffRecord v1.1 adds grounding status, receipt references, Preflight
reference and unresolved references. A Contributor-to-Reviewer handoff must be
`GROUNDED`; otherwise it is rejected.

## Candidate Preflight

```text
Contributor Output
→ Role Schema Validation
→ Scope Validation
→ Resource Resolution
→ Candidate Patch Application in Isolated Copy
→ Reference Re-resolution
→ Incremental Conformance
→ Preflight Result
→ Reviewer
→ Final Conformance
```

Preflight checks candidate parsing, contract shape, exact reference existence,
machine surfaces, required limitations, semantic elevation, scope, source
revision, candidate-created resources, dangling references and formal-task
contamination. One bounded Contributor revision may rerun the complete
Preflight; a second failure ends the task before Reviewer.

## Historical Task 1 deterministic replay

The unchanged candidate references:

```text
TITMAS/agent-native/ecology-box-001/calibration/calibration-v0.2.json
```

The frozen source tree returns:

```text
RESOURCE_RESOLUTION_STATUS=NOT_FOUND
RESOURCE_RESOLUTION_RECEIPT=RR-dc6972b89e16db19264b
PREFLIGHT_STATUS=REVISION_REQUIRED
REVIEW_STAGE_REACHED=false
CAL2_TASK_001_INVALID_REFERENCE_REJECTED_BEFORE_REVIEW=true
```

The replay does not alter the candidate or retroactively change the historical
Reviewer result.

## Deterministic tests

```text
CANDIDATE_GROUNDING_TESTS=20/20_PASS
REVIEW_METRIC_TESTS=6/6_PASS
NONEXISTENT_REFERENCE_REJECTED_BEFORE_REVIEW=true
REVIEW_PASS_WITH_UNRESOLVED_REFERENCE_REJECTED=true
CONTRIBUTOR_ABSTENTION_PATH_PASS=true
```

The matrix covers exact success, missing/ambiguous/out-of-scope/invalid
references, candidate-created resources, schema and registry misses,
abstention, guessed paths, Reviewer evidence rules, historical replay, bounded
revision, late final-Conformance failure, source drift and Truth/Authority
semantic elevation.

## Formal state and limitations

```text
TITMAS_ECOLOGY_BOX_001_GO_NO_GO_STATUS=NO_GO
TITMAS_ECOLOGY_BOX_001_EXECUTION_AUTHORIZED=false
TITMAS_ECOLOGY_BOX_001_EXECUTED=false
FORMAL_TASK_COUNT=10
FORMAL_RUN_RECORD_COUNT=0
TITMAS_ECOLOGY_BOX_001_VALUE_PROVEN=false
TITMAS_AGENT_NATIVE_VALUE_PROVEN=false
TITMAS_AGENT_OPERATIONAL_VALUE_DEMONSTRATED=false
REAL_REPOSITORY_GIT_WRITE_AUTHORIZED=false
PUBLIC_REPORT_AUTHORIZED=false
COMMERCIAL_VALIDATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

The resolver covers the local frozen repository and isolated candidate copy,
not remote availability, deployment state or canonical existence. YAML
incremental parsing is intentionally bounded to dependency-free structural
checks; final Conformance remains mandatory.

## Next Human Decision

`CG-HD-01` through `CG-HD-04` are prepared and remain `UNDECIDED`. In
particular, deterministic completion does not authorize Calibration v0.3.

```text
PERSIST_BEFORE_PROGRESS=true
VALIDATE_BEFORE_HANDOFF=true
RESOLVE_BEFORE_REVIEW=true
GROUND_BEFORE_RECOMMENDATION=true
ABSTENTION_IS_VALID_WHEN_FACTS_CANNOT_BE_RESOLVED=true
STRUCTURAL_VALIDITY_NE_ENVIRONMENTAL_TRUTH=true
```
