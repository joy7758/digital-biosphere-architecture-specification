---
snapshot_id: DEB-001-CONFIGURATION-SNAPSHOT-0.1
experiment_id: DEB-001
version: v0.1
scope: immutable-configuration-identity
status: draft
created_at: 2026-07-24
reference_docs:
  - DEB-001-CLOSURE-STATUS-UPDATE-v0.1
  - DEB-001-CLOSURE-PLAN-v0.1
  - DEB-001-PILOT-PACKAGE-v0.1
  - DEB-001-STRATEGY-BASELINE-v0.1
  - SPEC-DIGITAL-ECOLOGY-BOX-RESULT-v0.1
implementation_authorized: false
runtime_authorized: false
api_authorized: false
authority_system: none
---

# DEB-001-CONFIGURATION-SNAPSHOT-v0.1

## 1. Experiment identity（实验身份）

- `experiment_id`: `DEB-001`
- `experiment_name`: `DEB-001 Efficiency vs Survival`
- `version`: `v0.1`
- `snapshot_scope`: pre-alpha immutable configuration identity definition

## 2. Configuration identity block（配置身份块）

### 2.1 Experiment specification identity

- `experiment_specification_reference`: `DEB-001-PILOT-PACKAGE-v0.1`
- `experiment_specification_hash`: `<TBD>`

### 2.2 Strategy baseline identity

- `strategy_baseline_reference`: `DEB-001-STRATEGY-BASELINE-v0.1`
- `strategy_baseline_hash`: `<TBD>`

### 2.3 Environment configuration identity

- `environment_configuration_reference`: `DEB-001-ALPHA-EXECUTION-PLAN-v0.1`
- `environment_configuration_hash`: `<TBD>`

### 2.4 Result schema identity

- `result_schema_reference`: `SPEC-DIGITAL-ECOLOGY-BOX-RESULT-v0.1`
- `result_schema_hash`: `<TBD>`

### 2.5 Metric definition identity

- `metric_definition_reference`: `SPEC-DIGITAL-ECOLOGY-BOX-RESULT-v0.1`
- `metric_definition_hash`: `<TBD>`
- `metric_set`:
  - Survival Fitness
  - Adaptation Velocity
  - Diversity Index
  - Resilience Score
  - Stability Index
  - Dependency Index

## 3. Evidence artifact identity block（证据制品身份块）

### 3.1 lineage_records

- `lineage_records_version`: `<TBD>`
- `lineage_records_hash`: `<TBD>`

### 3.2 action_traces

- `action_traces_version`: `<TBD>`
- `action_traces_hash`: `<TBD>`

### 3.3 selection_records

- `selection_records_version`: `<TBD>`
- `selection_records_hash`: `<TBD>`

### 3.4 outcome_records

- `outcome_records_version`: `<TBD>`
- `outcome_records_hash`: `<TBD>`

## 4. Snapshot lifecycle（快照生命周期）

- `DRAFT`
- `FROZEN`
- `SUPERSEDED`

### Lifecycle meaning

- **DRAFT**: defined and internally reviewed, not yet immutable.
- **FROZEN**: immutable for Alpha execution and review.
- **SUPERSEDED**: archived but replaced by a newer snapshot version.

## 5. Freeze conditions（冻结条件）

A snapshot enters `FROZEN` only when:

1. All references are version-locked.
2. All identity hashes are recorded.
3. Evidence artifact identities are completed.
4. Closure plan indicates no open blockers in core fields.
5. Reviewer confirms closure-readiness alignment.

## 6. Change policy（变更策略）

Any change to any identity field requires a new snapshot version and supersedes prior snapshot:

- experiment specification hash change
- strategy baseline hash change
- environment configuration hash change
- result schema hash change
- metric definition hash change
- evidence artifact version/hash change

No in-place mutation is allowed.

## 7. Non-goals（非目标）

- no execution approval
- no runtime authority
- no scientific conclusion

