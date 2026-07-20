# AGENTS.md

## Repository role

This repository is the non-executable architecture specification and governance
surface for DBOS, SAEE, Governance Decision, Digital Entity, and related future
ecosystem roles.

It defines meaning, responsibility boundaries, data contracts, lifecycle
models, strategic direction, and ADR context. It does not authorize or create
an implementation, Agent, Runtime, Entity, Capability, Permission, Evidence,
commercial offering, or certification.

## Mandatory strategic entry

Before proposing or changing DBOS, SAEE, Digital Entity, developer-ecosystem,
industry-solution, marketplace, or commercialization direction, read in order:

1. `architecture/open-infrastructure-strategy-constitution.md`
2. `architecture/project-mapping.md`
3. the relevant specification, strategy document, and ADR under `architecture/`

Every proposal must state:

- whether it belongs to Infrastructure, Evolution, Application, or Governance Service;
- whether it strengthens open standards, interoperability, and developer reuse;
- whether it duplicates DBOS, SAEE, a Foundation Model, an Agent framework, or an existing ecosystem component;
- whether it mixes Capability, Permission, Authority, Execution, Evidence, Evaluation, Decision, or Truth;
- whether commercial language is Strategy, Exploration, Available Offering,
  Customer Adoption, or Contractual Commitment.

If these questions are unresolved, keep the proposal at `REVIEW_REQUIRED` and
do not treat it as implementation authorization.

## Strategic invariants

```text
DBOS_NE_AGENT_APPLICATION=true
DBOS_NE_FOUNDATION_MODEL=true
DBOS_NE_SAEE=true
DBOS_GOVERNS_EXISTENCE=true
SAEE_GOVERNS_EVOLUTION=true
DEVELOPER_ECOSYSTEM_FIRST=true
OPEN_INFRASTRUCTURE_NE_FREE_PRODUCT=true
SPECIFICATION_NE_IMPLEMENTATION=true
STRATEGY_NE_COMMERCIAL_COMMITMENT=true
```

## Architecture truth boundaries

- Preserve `SAEE != DBOS` and `DBOS != SAEE`.
- Recommendation is not Decision; Decision is not Execution.
- Capability is not Authority or Permission.
- Evidence is not Truth.
- Candidate is not Entity; Registration is not Activation.
- Repository, specification, component, Agent, Runtime, Digital Entity, and
  Digital Organism are distinct concepts.
- Unknown facts remain unknown; documentation must not promote them.
- Do not create reconstructable runtime or cross-repository execution paths in
  this architecture repository.
- Do not modify DBOS or SAEE from an architecture-only task.
- Do not commit, tag, publish, or claim adoption unless explicitly authorized.

## Change discipline

- Core strategy changes require an ADR and constitution version review.
- Architecture changes must remain non-executable and state their authority effect.
- Open infrastructure does not mean every product or service must be free.
- A specification, test, demo, validator pass, listing, or local artifact does
  not prove implementation, deployment, adoption, certification, or commercial availability.
