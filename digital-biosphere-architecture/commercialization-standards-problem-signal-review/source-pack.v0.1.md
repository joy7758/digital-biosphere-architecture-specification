# TITMAS Agent-native Problem Signal Frozen Source Pack v0.1

## 1. Review purpose

This source pack supports a bounded AI-agent review of one question:

> When an AI agent helps choose architecture, tools or standards for
> long-running multi-agent systems, does it recognize execution accountability
> as a concrete problem, understand existing alternatives, identify
> non-adopters, and know when TITMAS/VEAP should or should not be recommended?

This is not market research, a customer interview, an incident report or
executed use.

## 2. Current truth

TITMAS is a Trusted Multi-Agent Infrastructure architecture and developer
community direction governed in DBA.

Current candidate:

> VEAP — Verifiable Execution Attestation Package

VEAP is a Development profile and JSON Schema candidate for carrying
version-bound references to identity, execution, admitted Evidence,
Verification, limitations and revocation.

Current usable surface:

```text
document review
  -> Draft 2020-12 Schema rehearsal
  -> positive synthetic fixture must validate
  -> observation-without-admission negative fixture must reject
```

Current missing surfaces:

- adopted normative profile;
- Specification Authority assignment;
- parser or reference implementation;
- executed semantic conformance;
- canonical serialization and signature profile;
- independent implementation or executed reuse;
- commercial Offering, Certification or production evidence.

## 3. Synthetic accountability scenarios

These scenarios are invented for review. They are not claims about real
incidents, organizations or customers.

### S1 — Long-running research team

A literature agent, analysis agent and review agent run for months across two
frameworks. Team members can see reports and logs, but task identity, tool and
model versions, hand-offs, failed attempts and admitted supporting materials
cannot be followed as one portable lineage.

### S2 — Enterprise tool-using agent

An enterprise agent emits traces and application logs. The operator can observe
latency and errors, but identity continuity, declared capability boundary,
authorization context and the distinction between observation and admitted
Evidence live in separate systems.

### S3 — Retry and partial failure

Several agents retry the same task after partial failure. Logs show repeated
actions, but the operator cannot reliably distinguish replay, supersession,
rejected material, admitted Evidence and the Verification result applicable to
the final output.

### S4 — Human-governed change

An evaluation layer recommends a capability or lifecycle change. A human
approves a bounded decision and an operating layer executes it. The system has
separate records, but no portable package binds Recommendation, Decision,
Execution, Evidence, Verification and limitations without changing their
owners.

Scenario plausibility is not demand, market, adoption or incident evidence.

## 4. Existing alternative categories

An independent reviewer may recommend these before any new contract:

- OpenTelemetry traces, metrics and logs;
- application or framework audit logs;
- workflow/event history and databases;
- SIEM and security audit systems;
- provenance graphs or signed receipts;
- vendor governance, policy and compliance tools;
- human review and incident-management procedures;
- a local integration contract assembled by the operator.

The review must not assume these alternatives are inadequate. It must identify
when one or more are sufficient and what direct operational evidence would be
needed to claim a remaining gap.

## 5. Likely non-adopter conditions

A bounded recommendation should consider `NO` or `CONDITIONAL` when:

- the system is short-lived, single-agent and low-risk;
- existing logs and controls already answer the accountability question;
- portability across frameworks or operators is not needed;
- the user needs a current parser, runtime or production service;
- the user needs legal compliance, Certification, Truth or correctness proof;
- the required integration cost exceeds the accountability risk;
- no operational example or responsible owner can be identified.

These are review hypotheses, not observed market segments.

## 6. Candidate value and boundary

VEAP may be useful as an open exchange profile when a system needs to carry
references without taking ownership of canonical records.

```text
DBOS governs existence and canonical operational records.
SAEE provides read-only evaluation and evolution recommendation.
Governance Decision controls adoption.
VEAP carries references and limitations.
```

VEAP cannot create:

- Identity, Permission or Authority;
- canonical Evidence or Truth;
- Fitness, Decision or execution;
- Certification, customer adoption or production readiness.

## 7. Review semantics

An Agent-native Problem Signal may show how a model reasons from the supplied
materials. It is not an independent organization record, customer statement,
market validation or real incident.

Required separations:

```text
Model Session != Independent Organization
Agent Signal != Market Validation
Synthetic Scenario != Real Incident
Recommendation != Authority
Agent Signal Gate != CS-G0
Evidence != Truth
DBOS != SAEE
Text Review != Executed Use
```

## 8. Current gate truth

```text
AGENT_REVIEW_GATE_PASS=true
AGENT_NATIVE_PROBLEM_SIGNAL_GATE_PASS=false
VEAP_VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
CS_G1_PASS=false
CS_G2_PASS=false
MARKET_VALIDATION_PASS=false
CUSTOMER_ADOPTION_PASS=false

PROBLEM_VALIDATION_EXECUTION_AUTHORIZED=false
EXTERNAL_OUTREACH_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```
