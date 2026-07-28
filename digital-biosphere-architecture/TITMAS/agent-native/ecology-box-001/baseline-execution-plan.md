# DEB-TITMAS-001 Human-first Baseline Execution Plan v0.1

## Status

```text
PLAN_PREPARED=true
WORKFLOW=HUMAN_FIRST
PARTICIPANT_ASSIGNED=false
EXECUTION_AUTHORIZED=false
EXECUTED=false
```

This is a future execution contract, not an execution record.

## Frozen sequence

For each of the ten task contracts, an assigned Human participant would use:

```text
Discovery
  -> Analysis
  -> Implementation
  -> Review
  -> Validation
```

The participant receives only the frozen source package, task contract,
rubric, allowed tools and known limitations. Work occurs in a sealed,
disposable workspace without network access or real Git writes.

## Per-task budget

| Resource | Ceiling |
|---|---:|
| active work time | 45 minutes |
| candidate revisions | 2 |
| formal review cycles | 2 |
| local validation invocations | 5 |
| network operations | 0 |
| real Git writes | 0 |

Exceeding a ceiling stops the task and records `NOT_ASSESSED` or `STOPPED`.
It does not permit a silent extension.

## Required future record

Every authorized run would record:

- task and frozen source references;
- participant and declared prior-access references;
- stage timestamps and Human active time;
- intervention, revision, review-cycle and validation counts;
- origin-neutral candidate reference;
- failures, abstentions and limitations;
- reviewer disposition and provenance after the blind protocol.

No record may contain credentials, private paths or hidden reasoning.

## Boundary

Human authorship or review does not create Architecture Authority, Adoption,
Release or Evidence Truth. This plan does not assign a participant, approve
data processing or authorize execution.
