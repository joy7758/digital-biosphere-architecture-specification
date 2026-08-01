---
spec_id: DBA-DEB-GOVERNANCE-001
title: SPEC-DIGITAL-ECOLOGY-BOX-GOVERNANCE-v0.1
title_zh: 数字生态箱治理规范 v0.1
status: theoretical-governance-spec
scope: scientific-governance-and-reproducibility
document_type: governance-specification
implementation_authorized: false
runtime_authorized: false
api_authorized: false
execution_control_authorized: false
authority_effect: none
created_at: 2026-07-24
primary_repository: digital-biosphere-architecture
---

# SPEC-DIGITAL-ECOLOGY-BOX-GOVERNANCE-v0.1

This specification defines scientific governance and reproducibility principles for Digital Ecology Box (DEB) experiments.

It is a theory-layer specification only:

- not runtime
- not API
- not execution control

## 1. Experiment Lifecycle

DEB experiments must follow five lifecycle stages:

1. Proposal
2. Registration
3. Execution
4. Result publication
5. Archival

### 1.1 Proposal

A proposal must state:

- Research question
- Population strategy set
- Environment model and shocks
- Metrics and expected outputs
- Evidence sources and preservation plan
- Risk and fallback path

Only hypothesis-first proposals are accepted. Implementation details are out of scope.

### 1.2 Registration

Upon approval, the proposal is registered with:

- experiment_id
- experiment_version
- box specification reference
- reproducibility controls
- ownership and review roles

Registration records the exact scope and prevents later scope drift without amendment.

### 1.3 Execution

Execution is evidence-producing only.

- All required evidence channels are enabled.
- No output from execution is treated as runtime governance.
- Failed runs are valid lifecycle events and must be stored.

### 1.4 Result Publication

Results are published only through the DEB result specification model.

Each result must include falsification outcome and the evidence references used.

### 1.5 Archival

After publication, outputs enter immutable archive with versioned references and can be queried for cross-experiment comparison.

## 2. Research Integrity

### 2.1 Prevent selective reporting

- Publish complete planned-vs-observed metric table.
- Publish all major failure modes.
- Report all non-confirming runs in the same package.

### 2.2 Preserve failed experiments

Failures, rejected hypotheses, and operationally abnormal runs are first-class records.

### 2.3 Preserve inconclusive results

Inconclusive outcomes must be retained with explicit uncertainty reasons and follow-up experiment suggestions.

No pruning of negative or incomplete results is allowed.

## 3. Experiment Versioning

DEB governance requires explicit versions for:

- specification version
- environment version
- strategy version
- metric version

All result packages must state these fields and use immutable references.

Version changes require amendment record.

## 4. Reproducibility Requirements

### 4.1 Independent replication

Each experiment claims reproducibility only after at least one independent replication context run.

### 4.2 Evidence preservation

Evidence objects must be preserved and referenceable for all required channels:

- lineage records
- action traces
- selection records
- outcome records

### 4.3 Immutable experiment record

Core experiment metadata and evidence bundles must be immutable once run state enters archival stage.

## 5. Result Publication Rules

Result status is one of:

- supported
- rejected
- inconclusive

### 5.1 Supported

Evidence and metrics are sufficient, and the hypothesis result is supported with transparent reasoning and metric consistency.

### 5.2 Rejected

Evidence and metrics are sufficient, and the hypothesis is falsified under defined conditions.

### 5.3 Inconclusive

Evidence is present but not sufficient for stable conclusion or reproduction is incomplete.

No status may be used to force DST endorsement.

## 6. Relationship with Core Layers

### 6.1 Digital Survival Theory

DEB governance operationalizes theory testing assumptions but does not redefine theory ontology.

### 6.2 Digital Ecology Box

DEB governance defines how ecology-box experiments are proposed, executed, and compared.

### 6.3 Evidence Architecture

Governance depends on evidence architecture for traceability but does not replace it.

### 6.4 Registry

Registry is the discovery and comparison surface for experiments. Governance requires registry entries to be versioned and queryable.

## 7. Non-goals

- no governance authority
- no execution control
- no runtime behavior definition
- no API specification

## 8. Governance Commitments

- all DEB outputs use a common result schema
- failed, rejected, and inconclusive outcomes are non-derogatory scientific outputs
- comparability is based on versioned spec, environment, strategy, and metric definitions
- integrity and reproducibility are mandatory, independent of result success

