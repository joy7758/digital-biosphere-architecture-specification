# DEB-TITMAS-001 Blind Evaluation Protocol v0.1

## Status and purpose

This protocol freezes how candidate outcomes would be evaluated after a
separately authorized execution. It does not assign a Reviewer, create an
origin map or evaluate a result.

```text
BLIND_EVALUATION_PROTOCOL_PREPARED=true
BLIND_EVALUATION_EXECUTED=false
INDEPENDENT_REVIEWER_ASSIGNED=false
BLIND_KEY_OWNER_ASSIGNED=false
ORIGIN_MAPPING_CREATED=false
EXECUTION_AUTHORIZED=false
```

The machine-readable contracts are:

- `independent-reviewer-model.yaml`;
- `blind-custodian-protocol.yaml`;
- `provider-privacy-retention-policy.yaml`.

Their design completeness supports a fairness design review. Their unassigned
instances keep execution prerequisites unsatisfied.

## Candidate construction

Each task review packet contains three origin-neutral candidates:

- `Candidate A`;
- `Candidate B`;
- `Candidate C`.

Exactly one candidate is the `HUMAN_FIRST` output and one is the
`AGENT_NATIVE` output. The third is a predeclared calibration anchor derived
from the frozen task contract and contains no experiment result. Candidate C
is not a third workflow arm and is excluded from the primary paired
comparison. Its only purpose is to detect rubric drift and origin guessing.

Candidate labels are randomized independently for each task. The allocation
key is held by a Human custodian who is neither a producer nor the outcome
Reviewer. No key exists before an accepted execution decision.

## Reviewer blinding

The Reviewer receives:

- frozen task contract and source revision;
- origin-neutral candidate content;
- frozen rubric and limitations;
- deterministic validation outputs with secrets and local paths removed.

The Reviewer does not receive:

- workflow, participant, Provider, model, session, role or lineage identity;
- prompts, hidden reasoning, internal transcripts or allocation keys;
- the other arm's work history;
- sponsor preference, expected winner or prior task-level outcome.

Any Reviewer must declare prior access and conflict of interest before
assignment. `HD-EB-07` remains the Human gate for assignment.

The required identity, conflict, prior-access, scope and abstention fields are
defined in `independent-reviewer-model.yaml`. A role profile is not an Agent
instance or reviewer assignment.

## Frozen rubric

Each candidate is assessed independently on:

1. factual and semantic correctness;
2. maintainability and minimality;
3. conformance and boundary preservation;
4. long-term usefulness;
5. Critical defects and known limitations.

Reviewers record dimension-level dispositions and reasons. A composite score,
post-hoc weighting or output-volume proxy is prohibited.

## Sealing and unblinding

Rubrics are sealed before origin reveal. The custodian then reveals the
mapping only to calculate the pre-registered paired comparison. Unblinding
cannot change scores. A later correction is a versioned erratum and preserves
the original record.

Raw blind keys, private paths, credentials, prompts and hidden reasoning are
never copied into public-safe reports.

`blind-custodian-protocol.yaml` defines the Human custodian role,
unblinding conditions and append-only access-log contract. No blind key,
owner assignment, origin mapping or access-log entry currently exists.

## Failure handling

Premature reveal, Reviewer self-review, missing calibration anchor, allocation
tampering, rubric drift or outcome-aware reassignment invalidates the affected
pair. It is retained as `STOPPED` or `NOT_ASSESSED`; it is not silently
excluded or rerun.

This document complements `reviews/blind-review-protocol.md`. If the two
conflict, execution fails closed and requires a versioned Human review.

```text
BLIND_PROTOCOL_DESIGN_REVIEW_STATUS=PASS
BLIND_OPERATIONAL_READINESS=false
```
