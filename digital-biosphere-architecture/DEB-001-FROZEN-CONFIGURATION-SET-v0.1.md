---
artifact_set_id: DEB-001-FROZEN-CONFIGURATION-SET-0.1
experiment_id: DEB-001
version: v0.1
scope: frozen-configuration-set-specification
status: draft
created_at: 2026-07-24
reference_docs:
  - DEB-001-CONFIGURATION-SNAPSHOT-v0.1
  - DEB-001-HASH-MANIFEST-v0.1
  - DEB-001-HASH-CLOSURE-CHECKLIST-v0.1
implementation_authorized: false
runtime_authorized: false
api_authorized: false
authority_system: none
---

# DEB-001-FROZEN-CONFIGURATION-SET-v0.1

## 1. Freeze set identity（冻结集合身份）

- `artifact_set_id`: `DEB-001-FROZEN-CONFIGURATION-SET-0.1`
- `experiment_id`: `DEB-001`
- `experiment_version`: `v0.1`
- `purpose`: define the immutable artifact set required before Alpha execution.
- `scope`: pre-execution configuration closure

## 2. Required artifacts（必需制品）

| artifact_type | name | version | reference | hash_status | freeze_status |
|---|---|---|---|---|---|
| Theory document | Digital Survival Theory Foundation | v0.1 | `Digital-Survival-Theory-Foundation-v0.1.md` | TBD | DRAFT |
| ADR | DST Freeze ADR | v0.1 | `ADR-DIGITAL-SURVIVAL-THEORY-FREEZE-001` | TBD | DRAFT |
| Package | DEB-001 Pilot Package | v0.1 | `DEB-001-PILOT-PACKAGE-v0.1.md` | TBD | DRAFT |
| Baseline | DEB-001 Strategy Baseline | v0.1 | `DEB-001-STRATEGY-BASELINE-v0.1.md` | TBD | DRAFT |
| Plan | DEB-001 Alpha Execution Plan | v0.1 | `DEB-001-ALPHA-EXECUTION-PLAN-v0.1.md` | TBD | DRAFT |
| Specification | Digital Ecology Box Result Specification | v0.1 | `SPEC-DIGITAL-ECOLOGY-BOX-RESULT-v0.1.md` | TBD | DRAFT |
| Snapshot | Configuration Snapshot | v0.1 | `DEB-001-CONFIGURATION-SNAPSHOT-v0.1.md` | TBD | DRAFT |
| Manifest | Hash Manifest | v0.1 | `DEB-001-HASH-MANIFEST-v0.1.md` | TBD | DRAFT |

## 3. Artifact metadata（制品元数据）

For each artifact, record:

- `name`
- `version`
- `reference`
- `hash_status`:
  - `PENDING` (not yet computed)
  - `RECORDING` (in progress)
  - `PRESENT` (computed and verified)
- `freeze_status`:
  - `DRAFT`
  - `FROZEN`
  - `SUPERSEDED`

## 4. Freeze lifecycle（冻结生命周期）

- `DRAFT`: artifact listed, referenced, and under review.
- `FROZEN`: artifact hashes and version references are immutable for this alpha execution set.
- `SUPERSEDED`: replaced by a newer version of the same artifact set.

## 5. Transition criteria（转移条件）

The freeze set can move from `DRAFT` to `FROZEN` when:

1. All required artifacts are present and version-referenced.
2. Hash manifest has all required hashes present for configuration + evidence blocks.
3. Hash closure checklist conditions are all met.
4. Closure status indicates no unresolved blocking issue in configuration identity and hash closure.
5. Reviewer confirmation is attached to the set record.
6. No post-freeze mutation is planned without creating a superseded snapshot version.

## 6. Non-goals（非目标）

- no execution approval
- no runtime authority
- no scientific conclusion

