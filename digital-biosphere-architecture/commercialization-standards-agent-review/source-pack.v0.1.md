# TITMAS Agent-First Review Source Pack v0.1

Status: `PUBLIC_SAFE_FROZEN_INPUT_CANDIDATE`

## Project positioning

TITMAS means **Trusted Infrastructure for Multi-Agent Systems**.

Public positioning:

> An infrastructure developer community building shared trust protocols,
> developer tooling, reference implementations, and validation methods for
> long-running multi-agent systems.

It is not an Agent framework, workflow tool, cloud platform, certification
authority, or finished commercial product.

## Architecture

- DBA is the program governance and architecture layer.
- DBOS governs existence: identity, lifecycle, capability boundaries,
  execution records, evidence records, and verification records.
- SAEE governs evolution: evaluation, reliability, stability, risk,
  adaptability, and evolution recommendations.
- Digital Entities perform domain work.

Required boundaries:

```text
DBOS != SAEE
Evidence != Truth
Recommendation != Decision
Decision != Execution
Capability != Permission
Attestation != Certification
Model session != Digital Entity instance
```

## Current candidate standard direction

VEAP means **Verifiable Execution Attestation Package**.

It is currently a conceptual first-wedge candidate for describing an
evidence-backed execution accountability package. It is not a stable normative
profile, implemented product, certificate, or certification scheme.

Current direct facts:

- architecture and governance materials exist;
- a conceptual ownership crosswalk exists, but ownership is not frozen;
- 20 conceptual conformance cases exist, but none has been executed;
- a problem-validation protocol and risk register exist;
- no VEAP normative profile, normative schema, reference implementation,
  independent implementation, commercial pilot, available offering, customer
  adoption, or certificate exists;
- current implementation, commercial offer, certification, and release
  authorization are false.

## Primary customer strategy

The primary validation customer is the AI agent that must discover, understand,
use, reuse, and appropriately recommend the infrastructure. Human reviewer
feedback is optional reference. Human Program Owner `zhangbin` retains final
governance accountability and all material authorization decisions.

## This review

This is a tool-free review of given public-safe materials. It may assess:

- given-material discoverability;
- positioning comprehension;
- use/reuse path clarity;
- recommendation fitness;
- method, security, claim, and architecture boundaries.

It cannot prove:

- independent open-web discovery;
- installation or execution;
- independent reuse or implementation;
- market adoption, customer adoption, certification, or production readiness.

The correct answer may be `NO` or `CONDITIONAL`. Negative findings and dissent
are valuable.
