---
document_id: DBA-VEAP-AUTHORITY-DEPENDENCY-DISPOSITION-CANDIDATE-0.1
title: VEAP Authority Dependency Disposition Candidate v0.1
title_zh: VEAP 权力依赖处置候选 v0.1
status: DEVELOPMENT_CANDIDATE_OFFLINE_REVIEW_INPUT_ONLY
maturity: Development
maturity_scope: entire-document
created_at: 2026-07-28T22:10:00+08:00
decision_reference: CS-G1-REMEDIATION-D02
primary_repository: digital-biosphere-architecture
authority_effect: none
implementation_effect: none
commercial_effect: none
---

# VEAP Authority Dependency Disposition Candidate v0.1

## 1. Purpose

This candidate defines how the revised VEAP ownership crosswalk must preserve
seven upstream dependencies without silently treating any of them as resolved.
It does not close a Decision Queue item, assign an owner, accept a crosswalk,
create Specification Authority or pass `CS-G1`.

## 2. Dependency dispositions

| Dependency | Current state | Required bounded treatment | Prohibited inference |
|---|---|---|---|
| `DQ-003` | `OPEN` | Preserve DBOS project-local source/status uncertainty and require an exact project source before any current-state claim | DBA becomes DBOS Status Truth |
| `AF-D04` / `AF-D14` | `OPEN` | Bind an EEOAP reference to an exact canonical source, version and issuer; otherwise return `NOT_ASSESSED` | second EEOAP source, certification or legal-responsibility claim |
| `AF-D05` | `OPEN` | Bind an Agent Evidence material reference to an exact named surface and version; otherwise return `NOT_ASSESSED` | family-wide owner inference, merge, migration, rename, relicense or IP transfer |
| `AF-D13` | `OPEN` | Preserve the SAEE `READ_ONLY`, `ADVISORY_ONLY`, `NO_WRITEBACK` boundary and carry uncertainty | Fitness invention, DBOS writeback or recommendation execution |
| `AF-D15` | `OPEN` | Preserve `TITMAS_SPECIFICATION_AUTHORITY_ASSIGNED=false` until an explicit Human Decision | self-assigned TITMAS Specification Authority |
| `AF-D16` | `OPEN` | Keep the v0.2 ownership crosswalk as a Development candidate until explicit Human acceptance | second canonical object or accepted ownership |
| `CS-G6` | `BLOCKED` | Keep `COMMERCIAL_SERVICE` as `NO_OFFERING` and owner unassigned | offering, price, contract, customer adoption or commercial availability |

## 3. Fail-closed rule

An open or blocked dependency may be carried as an explicit unresolved
reference. It may not be converted into `PASS`, `ACCEPTED`, current owner,
Authority, implementation, offering or adoption by timestamp preference,
model output, local Schema validity or candidate completeness.

```text
OPEN_DEPENDENCY_NE_RESOLVED_DEPENDENCY=true
MAPPING_NE_OWNERSHIP_ASSIGNMENT=true
CANDIDATE_NE_ACCEPTED_CROSSWALK=true
SCHEMA_VALID_NE_AUTHORITY=true
MODEL_REVIEW_NE_HUMAN_DECISION=true
```

## 4. Current effects

```text
DEPENDENCY_DISPOSITION_CANDIDATE_DEFINED=true
DEPENDENCIES_RESOLVED=0
AUTHORITY_ASSIGNED=false
OWNERSHIP_ASSIGNED=false
CROSSWALK_ACCEPTED=false
MODEL_REVIEW_AUTHORIZED=false
PROVIDER_REQUESTS_AUTHORIZED=0
CS_G1_PASS=false
STANDARD_READY=false
IMPLEMENTATION_AUTHORIZED=false
COMMERCIAL_READY=false
RELEASE_AUTHORIZED=false
```
