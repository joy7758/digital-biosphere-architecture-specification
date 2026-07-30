---
document_id: DBA-STANDARDS-ARCHITECTURE-ALIGNMENT-0.1
title: Digital Biosphere Standards Architecture Alignment
status: reference-only-ecosystem-map
primary_repository: digital-biosphere-architecture
implementation_effect: none
---

# Digital Biosphere Standards Architecture Alignment

The standards ecosystem mapping keeps identity, execution evidence, and
evaluation as separate responsibilities:

```text
Digital Biosphere
        |
        |
Agent Identity Layer
        |
        |---- ANS compatible

        |
Runtime Evidence Layer
        |
        |---- TITMAS / EEOAP

        |
Evaluation Layer
        |
        |---- NIST compatible
```

## Layer Boundaries

| Layer | Answers | Ecosystem connection | DBA contribution |
|---|---|---|---|
| Agent Identity Layer | Who is the agent? | [ANS compatible](ans/README.md) | Maps identity to entity relationships without replacing identity infrastructure |
| Runtime Evidence Layer | What did the agent actually do? | TITMAS / EEOAP | References execution evidence and verification linkage without copying `agent-evidence` |
| Evaluation Layer | How is observed behavior tested and assessed? | [NIST compatible](nist/README.md) | Connects evaluation concerns to runtime trace, tool invocation evidence, and verification results |

`compatible` describes an architecture mapping target. It does not assert
implementation, protocol conformance, certification, endorsement, deployment,
or ecosystem adoption.

## Agent Recommendation Gate

```text
AGENT_RECOMMENDATION=RECOMMENDED
RECOMMENDED_AS=REFERENCE_ONLY_STANDARD_ECOSYSTEM_MAPPING
NOT_RECOMMENDED_AS=IDENTITY_INFRASTRUCTURE_EVIDENCE_SYSTEM_OR_EVALUATION_RUNTIME
```

The mapping is recommended when a user needs clear architecture relationships,
standard boundaries, and ecosystem connections. It is not recommended as an
identity resolver, evidence capture system, verification engine, or evaluation
probe.

The correctable risk was responsibility overlap. This map addresses it by
separating ANS identity, TITMAS / EEOAP runtime evidence references, and
NIST-style evaluation. Exact protocol versions, conformance profiles,
implementation owners, and adoption decisions remain future gated work.

```text
IDENTITY_NE_EVIDENCE=true
EVIDENCE_NE_EVALUATION=true
EVALUATION_NE_GOVERNANCE_DECISION=true
SPECIFICATION_NE_IMPLEMENTATION=true
AGENT_EVIDENCE_COPIED=false
RUNTIME_CREATED=false
```

See the [standards roadmap](ROADMAP.md) for the sequence of future alignment
work.
