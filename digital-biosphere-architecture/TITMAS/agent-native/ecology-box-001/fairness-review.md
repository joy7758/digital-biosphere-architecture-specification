# DEB-TITMAS-001 Fairness Review v0.1

## Review result

```text
FAIRNESS_REVIEW_STATUS=REQUIRES_CORRECTION
FAIRNESS_REVIEW_COMPLETE=true
EXECUTION_AUTHORIZED=false
```

The comparison controls are defined, but execution cannot be considered fair
until a Human decision binds an independent Reviewer, accepted lineage plan
and Provider/data controls.

## 1. Task fairness

Both workflows use the same ten task contracts, source revision, allowed and
forbidden scope, success/failure conditions and validation methods. Each arm
uses a sealed workspace. Candidate outputs are not shared between arms.

Status: `CONTROL_DEFINED`.

Residual risk: documentation, Schema and machine-entry tasks may favor an
Agent-native workflow. Results cannot be generalized beyond this task class.

## 2. Information fairness

Both arms receive the same source package, task contract, public-safe
references, rubric and known limitations. Neither arm receives hidden answers,
candidate-origin labels, blind keys or the other arm's output.

Status: `CONTROL_DEFINED`.

Residual risk: Human and model prior knowledge cannot be made identical and
must be disclosed as a limitation.

## 3. Resource fairness

The following per-task ceilings are predeclared for both arms:

| Resource | Human-first | Agent-native |
|---|---:|---:|
| active wall-clock work | 45 minutes | 45 minutes |
| candidate revisions | 2 | 2 |
| formal review cycles | 2 | 2 |
| local validation invocations | 5 | 5 |
| network access | 0 | 0 |
| real Git writes | 0 | 0 |

The Agent-native arm additionally has a `65536` input-token ceiling and
`16384` output-token ceiling per task because tokens are an Agent-specific
resource. Human access is limited to the same frozen source files rather than
an artificial token equivalent. Both arms use the same offline read/edit/test
tool classes.

Status: `CONTROL_DEFINED_WITH_NON_EQUIVALENT_MODALITY_DISCLOSED`.

## 4. Evaluation fairness

Candidate labels are randomized and reviewers see neither workflow source nor
participant/model identity. The frozen rubric evaluates correctness,
maintainability, conformance and long-term usefulness. Source is revealed only
after rubric records are sealed.

Status: `REQUIRES_CORRECTION`.

Blocking corrections:

- `HD-EB-07` must approve and bind an independent Reviewer;
- conflict-of-interest and prior-access declarations must be recorded;
- randomized candidate mapping and blind-key custody must be assigned;
- Reviewer budget and failure/abstention behavior must be accepted.

## Disposition

The design is reviewable, but not executable. `HD-EB-06` should remain
`DEFER` until every blocking correction is directly evidenced.

