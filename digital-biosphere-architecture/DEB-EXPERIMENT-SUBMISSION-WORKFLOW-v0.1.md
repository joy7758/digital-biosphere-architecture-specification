---
spec_id: DBA-DEB-SUBMISSION-WORKFLOW-v0.1
title: DEB Experiment Submission Workflow v0.1
title_zh: DEB 实验提交工作流 v0.1
status: contributor-facing-workflow
scope: scientific-submission-governance
created_at: 2026-07-24
implementation_authorized: false
runtime_authorized: false
api_authorized: false
authority_system: none
---

# DEB-EXPERIMENT-SUBMISSION-WORKFLOW-v0.1

## 1. Purpose（目的）

This workflow defines a contributor-facing process for proposing, reviewing, registering, executing, publishing, archiving, and replicating Digital Ecology Box (DEB) experiments.

It is a scientific operational guide only:

- No code
- No API
- No runtime
- No authority system

Its purpose is to standardize submission quality and reproducibility across DEB experiments.

## 2. Submission Lifecycle（提交生命周期）

```text
Proposal
  -> Review
    -> Registration
      -> Execution
        -> Result Publication
          -> Archive
            -> Replication
```

### 2.1 Proposal（提案）

Researchers submit hypothesis, experiment outline, population selection, and expected contribution to DST.

### 2.2 Review（评审）

A reviewer checks scientific completeness against this workflow and related DEB specs.

### 2.3 Registration（注册）

Upon review pass, the experiment is assigned a versioned lifecycle entry for traceability.

### 2.4 Execution（执行）

Execution is evidence production only. Results must follow `SPEC-DIGITAL-ECOLOGY-BOX-EXPERIMENT-v0.1` and `SPEC-DIGITAL-ECOLOGY-BOX-RESULT-v0.1` output format.

### 2.5 Result Publication（结果发布）

Publish `DigitalEcologyBoxResult` object and classification with reproducibility metadata.

### 2.6 Archive（归档）

Results and evidence links are frozen into immutable records.

### 2.7 Replication（复现）

Replications are submitted as linked follow-up entries and compared against original lifecycle records.

## 3. Required Submission Package（提交包要求）

Every DEB submission package must include:

1. Hypothesis
- core research question
- primary and null hypotheses
- expected falsification conditions

2. Experiment specification
- reference to `SPEC-DIGITAL-ECOLOGY-BOX-EXPERIMENT-v0.1`
- strategy population definitions
- scenario plan and phase model

3. Version references
- specification version
- environment version
- strategy version
- metric definition version
- expected result schema version

4. Evidence plan
- lineage records
- action traces
- selection records
- outcome records
- evidence completeness statement

5. Reproducibility plan
- seed policy
- deterministic controls
- independent replication plan
- replay constraints

## 4. Review Checklist（评审清单）

### 4.1 Hypothesis clarity

- Question is explicit and testable.
- Null hypothesis is included.
- Outcome categories are pre-defined (supported/rejected/inconclusive).

### 4.2 Metric definition

- `Survival Fitness`, `Adaptation Velocity`, `Diversity Index`, `Resilience Score`, `Stability Index`, `Dependency Index` are defined and interpretable.
- Units, aggregation windows, and uncertainty handling are specified.

### 4.3 Reproducibility readiness

- Deterministic controls are explicit.
- Environment and strategy versions are pinned.
- Replay package is planned at proposal time.

### 4.4 Evidence completeness

- All four evidence categories are required:
  - lineage records
  - action traces
  - selection records
  - outcome records
- Missing categories must be justified with status `UNKNOWN/CONFLICTED/PARTIAL`.

### 4.5 Non-goal compliance

- No claim that results imply AI consciousness.
- No replacement for governance or execution authority.
- No API/runtime/control promises.

## 5. Publication Checklist（发布清单）

Before publication, verify:

### 5.1 Result schema compliance

- Uses `DigitalEcologyBoxResult` structure from result specification.
- Includes required metadata and population comparisons.

### 5.2 Falsification status

- One of:
  - supported
  - rejected
  - inconclusive
- Include hypothesis-level reasoning and confidence notes.

### 5.3 Evidence references

- All evidence references are present and immutable.
- Evidence integrity states are declared (AVAILABLE/PARTIAL/CONFLICTED/UNKNOWN/FAIL).

### 5.4 Replication status

- Replication attempts documented.
- Divergence reasons recorded for each non-conforming replay.

## 6. Archive Requirements（归档要求）

### 6.1 Immutable reference

- Publish immutable result artifacts and evidence bundle references.
- No mutation of core lifecycle records after archival state.

### 6.2 Version linkage

- Link all outputs to:
  - experiment specification version
  - environment version
  - strategy version
  - metric version
  - result schema version

### 6.3 Experiment lineage

- Maintain lineage graph:
  - parent experiment
  - derived replications
  - revisions and corrections
  - cross-experiment references (e.g., DEB-001, DEB-002, DEB-003)

## 7. Non-goals（非目标）

This workflow does not provide:

- scientific authority
- approval of conclusions
- execution permission
- runtime rights

It is a submission discipline for scientific consistency only.
