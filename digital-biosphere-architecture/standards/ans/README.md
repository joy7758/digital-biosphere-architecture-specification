---
document_id: DBA-STANDARDS-ANS-ALIGNMENT-0.1
title: Agent Name Service Alignment
status: reference-only-architecture-mapping
primary_repository: digital-biosphere-architecture
architecture_layer: agent-identity
implementation_effect: none
---

# Agent Name Service (ANS) Alignment

Agent Name Service (ANS) provides:

- agent identity;
- discovery;
- naming.

Digital Biosphere provides:

- entity relationship;
- execution evidence reference;
- verification linkage.

## Architecture Boundary

Identity answers:

> Who is the agent?

Evidence answers:

> What did the agent actually do?

ANS is an identity layer.

DBA connects identity with evidence without replacing identity infrastructure.
The connection is an architecture relationship and reference boundary; it is
not a second identity registry, an ANS implementation, or proof of ANS
conformance or adoption.

## Related Standards Maps

- [Architecture alignment](../ARCHITECTURE_ALIGNMENT.md)
- [NIST-style evaluation alignment](../nist/README.md)
- [Standards roadmap](../ROADMAP.md)

```text
IDENTITY_NE_EVIDENCE=true
ANS_ROLE=IDENTITY_DISCOVERY_AND_NAMING
DBA_ROLE=ARCHITECTURE_RELATIONSHIP_AND_REFERENCE_LINKAGE
ANS_IMPLEMENTED_BY_DBA=false
ANS_INFRASTRUCTURE_REPLACED_BY_DBA=false
```
