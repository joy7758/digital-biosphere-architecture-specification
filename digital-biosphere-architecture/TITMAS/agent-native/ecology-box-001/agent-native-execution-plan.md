# DEB-TITMAS-001 Agent-native Execution Plan v0.1

## Status

```text
PLAN_PREPARED=true
WORKFLOW=AGENT_NATIVE
PARTICIPANT_ASSIGNED=false
EXECUTION_AUTHORIZED=false
EXECUTED=false
```

This plan describes a bounded candidate workflow. It does not create an
Agent, session, role assignment, Runtime or result.

## Frozen role sequence

```text
EXPLORER
  -> VALUE_JUDGE
  -> ARCHITECTURE_REVIEWER
  -> CONTRIBUTOR
  -> CONFORMANCE
  -> MEMORY
```

`RECOMMENDATION` and `EVOLUTION_OBSERVER` are optional read-only review roles
and cannot approve, execute or adopt a candidate.

| Role | Input | Output | Required evidence | Human intervention |
|---|---|---|---|---|
| Explorer | frozen task and source | bounded findings | source references, abstentions | only for blocked scope |
| Value Judge | findings and rubric | keep/reject recommendation | reason codes, duplicate check | conflict escalation |
| Architecture Reviewer | retained findings | boundary review | Authority and semantic-elevation checks | required for unresolved conflict |
| Contributor | accepted candidate specification | origin-neutral candidate | exact change set and limitations | no self-expansion |
| Conformance | candidate and frozen tests | deterministic validation result | command class, status, failure retention | approve no exceptions |
| Memory | reviewed outcome | unadopted Memory candidate | provenance and reuse condition | adoption remains Human-governed |

## Per-task budget

- active wall-clock ceiling: `45 minutes`;
- candidate revisions: `2`;
- formal review cycles: `2`;
- local validation invocations: `5`;
- network operations: `0`;
- real Git writes: `0`;
- model input tokens: `65536`;
- model output tokens: `16384`.

Only offline read, candidate-edit and deterministic-test tool classes are
allowed. A limit breach stops the task; it never expands scope.

## Required future record

An authorized session would record model, Provider, session, role and lineage
separately; frozen inputs; tool classes; time and token use; candidate
references; validations; failures; abstentions; Human interventions and known
limitations.

Several sessions or roles of one model remain one independent lineage unless
independence is directly evidenced. Role assignment never creates Authority,
Permission, Adoption or Decision.

## Provider, privacy and retention gate

Before any session:

- Provider and model must be explicitly accepted;
- data classification and prompt/output retention must be declared;
- training use, cross-border handling and deletion expectations must be
  reviewed;
- only public-safe or synthetic material may be used;
- credentials, private paths, raw hidden reasoning and personal data are
  prohibited.

These controls are not yet adopted. Execution therefore remains closed.
