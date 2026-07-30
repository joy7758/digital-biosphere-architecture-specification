---
document_id: DBA-STANDARDS-NIST-EVALUATION-ALIGNMENT-0.1
title: NIST Agent Evaluation Probe Alignment
status: reference-only-architecture-mapping
primary_repository: digital-biosphere-architecture
architecture_layer: evaluation
implementation_effect: none
---

# NIST Agent Evaluation Probe Alignment

NIST-style evaluation focuses on:

- trustworthy AI evaluation;
- observable behavior;
- testing.

DBA contributes an execution evidence perspective:

- runtime trace;
- tool invocation evidence;
- verification result.

## Architecture Boundary

The evaluation layer may reference execution evidence, but evaluation does not
create identity or replace the canonical evidence and verification
responsibilities of their owning systems.

`NIST compatible` in this mapping means conceptually aligned with a
NIST-style evaluation concern. It does not claim NIST endorsement,
certification, formal conformance, or an implemented evaluation probe.

## Related Standards Maps

- [Architecture alignment](../ARCHITECTURE_ALIGNMENT.md)
- [ANS identity alignment](../ans/README.md)
- [Standards roadmap](../ROADMAP.md)

```text
EVIDENCE_NE_EVALUATION=true
EVALUATION_NE_GOVERNANCE_DECISION=true
DBA_ADDS_EXECUTION_EVIDENCE_PERSPECTIVE=true
NIST_EVALUATION_PROBE_IMPLEMENTED_BY_DBA=false
NIST_ENDORSEMENT_OR_CERTIFICATION_CLAIMED=false
```
