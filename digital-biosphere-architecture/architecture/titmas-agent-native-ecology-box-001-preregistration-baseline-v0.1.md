---
document_id: DBA-TITMAS-ECOLOGY-BOX-001-PREREGISTRATION-BASELINE-0.1
title: TITMAS Agent-Native Ecology Box 001 Pre-registration Baseline v0.1
title_zh: TITMAS 智能体原生生态实验盒 001 预注册基线 v0.1
version: 0.1.0
status: verified-source-baseline-preregistration-only
maturity: Development
owner_ref: zhangbin
source_revision: b92a9a8c0553b51afc832e549d9ad5af271443f2
implementation_effect: none
experiment_effect: none
authority_effect: none
---

# TITMAS Agent-Native Ecology Box 001 Pre-registration Baseline v0.1

## Scope

This baseline was read from
`joy7758/digital-biosphere-architecture-specification` at
`b92a9a8c0553b51afc832e549d9ad5af271443f2`. It reconciles the existing
`DEB-TITMAS-001` package before pre-registration changes.

The dirty primary workspace contains unrelated untracked Digital Ecology Box
and theory files. They are not part of this source baseline and are not
imported.

## State classification

| Surface | Classification | Verified fact |
|---|---|---|
| TITMAS Conformance harness | `IMPLEMENTED` | Dependency-free local harness and tests exist. |
| Ecology Box constitution, protocol and freeze manifest | `PREPARED` | Package exists and its frozen hashes passed local and remote CI validation. |
| Ten-task registry and eight role definitions | `PREPARED` | Machine-readable registries exist; role assignments remain empty. |
| Participant registry | `PREPARED` | Registry exists with zero participant, model, session, role and independent-lineage counts. |
| Experiment execution | `NOT_AUTHORIZED` | `HD-EB-01` through `HD-EB-05` are `UNDECIDED`. |
| Ecology Box run | `NOT_EXECUTED` | `runs/` contains no run record. |
| Value conclusion | `NOT_PROVEN` | Previous frozen observation recorded zero final outcome improvements. |
| Agent Immune Integration Role Definition | `UNKNOWN_NOT_PRESENT_IN_SOURCE` | No matching tracked role-definition artifact was found at the source revision. |
| TITMAS Digital Immune Constitution | `PREPARED_DEVELOPMENT_DESIGN_BASELINE` | v1.0 exists; it creates no Runtime or Authority. |
| Canonical TITMAS Charter v0.2 named by `AGENTS.md` | `UNKNOWN_NOT_PRESENT_IN_SOURCE` | v0.2 is absent at the source revision; v1.0 exists and defines the drift check. |

## Existing package truth

```text
TITMAS_ECOLOGY_BOX_001_PACKAGE_COMPLETE=true
TITMAS_ECOLOGY_BOX_001_READY=true
TITMAS_ECOLOGY_BOX_001_EXECUTED=false
TITMAS_ECOLOGY_BOX_001_VALUE_PROVEN=false
REAL_AGENT_CONTRIBUTION_AUTHORIZED=false
REAL_GIT_ACCESS_AUTHORIZED=false
PUBLIC_REPORT_AUTHORIZED=false
COMMERCIAL_VALIDATION_AUTHORIZED=false
```

`READY` means package preparation readiness, not execution readiness.

## Prior negative evidence

The prior value-gate fixture remains part of the problem statement:

- 25 total suggestions;
- 3 unique factually valid findings;
- 5 duplicate findings;
- 17 false or not-applicable findings;
- 0 final outcome improvements.

Pre-registration must therefore retain duplicate, false, no-change and harmful
results; use outcome metrics rather than activity volume; and fail closed if
lineage, Authority or result status is elevated.

## Pre-development Agent Recommendation Gate

One exact `qwen3.7-max` advisory review returned `NOT_RECOMMENDED` before
remediation. Its blocking reasons were missing numeric resource budgets,
unassigned independent review, missing Provider/privacy/retention controls,
missing Charter v0.2 reconciliation and insufficient task-to-outcome/effect-size
detail.

This review creates no Decision or Authorization. The current work may correct
the protocol and prepare a Human decision candidate, but it cannot assign an
independent Reviewer, adopt Provider/data controls or reconstruct a canonical
Charter.

After the bounded corrections were added, a second exact `qwen3.7-max`
advisory review returned
`CONDITIONALLY_RECOMMENDED_FOR_HUMAN_REVIEW` and
`would_recommend_execution=false`. The remaining blockers are preserved in
the post-remediation review record. Neither Agent review is Human Decision or
experimental evidence.

## Required semantic separation

```text
IMPLEMENTED_NE_PREPARED=true
PREPARED_NE_AUTHORIZED=true
AUTHORIZED_NE_EXECUTED=true
EXECUTED_NE_PROVEN=true
CONFORMANCE_PASS_NE_VALUE_PROOF=true
```
