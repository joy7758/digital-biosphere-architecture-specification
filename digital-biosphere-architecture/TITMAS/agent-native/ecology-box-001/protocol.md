# DEB-TITMAS-001 Agent-Native Workflow Protocol

## Purpose

This protocol defines the preparation-time workflow for the Agent-native arm.
It does not execute a task, instantiate a participant or authorize Git access.

## Workflow

```text
Discovery
  ↓
Task Matching
  ↓
Bounded Claim
  ↓
Contribution Candidate
  ↓
Independent Review
  ↓
Conformance
  ↓
Outcome Evaluation
  ↓
Memory Formation Candidate
```

### Discovery

Read only the frozen task and source references. No hidden answer, blind key or
workflow-origin label may be exposed.

### Task Matching

Match declared capability to `required_capability`. Non-fit and insufficient
evidence must produce abstention, not a fabricated contribution.

### Bounded Claim

Bind one participant lease to one task, allowed scope, expiry and issuer.
Participant, session, role and lineage remain separate.

### Contribution Candidate

Produce an unadopted candidate output plus limitations and validation method.
Candidate does not mean accepted, merged or released.

### Independent Review

The reviewer cannot be the candidate producer and must not see whether the
candidate came from a Human or Agent workflow. Same-model isolated sessions are
not automatically independent lineages.

### Conformance

Run only the frozen offline method. Conformance PASS cannot create Truth,
Authority, Adoption or Value.

### Outcome Evaluation

Use the frozen multidimensional metrics. No single composite score and no
post-hoc weight adjustment are allowed.

### Memory Formation Candidate

If a resolution is reusable, create only an unadopted experiment memory
candidate containing context, result, reuse condition and limitations. This is
not a new Memory system or Authority source.

## Comparison controls

- same source commit and task set for both arms;
- counterbalanced order frozen before execution;
- equal wall-clock ceiling and declared tool budget;
- origin-blind outcome review;
- all failures retained;
- no undeclared answer sharing;
- reuse requires an exact `reuse_reference`;
- task pair, not Agent count, is the analysis unit.

## Transition to any future execution

Preparation may advance only after `HD-EB-01=ACCEPT` plus frozen allocation,
budget, reviewer and provider/data controls. Real Agent contribution, Git,
public report and commercial validation each require their own independent
Human Decision. No transition is automatic.

## Stop conditions

- source, task hash, metric version, protocol version or role version drifts;
- participant attempts self-authorization or role elevation;
- blind origin is revealed before review closes;
- Authority, Release, Adoption, Truth or commercial claims appear;
- failure or limitation is deleted;
- prior false/duplicate failure modes cannot be mapped to a control;
- memory candidate creates implicit Authority or unbounded retention;
- A/B comparability cannot be maintained.

```text
PROTOCOL_VERSION=0.1.0
PROTOCOL_STATUS=PREPARED
EXECUTION_AUTHORIZED=false
```
