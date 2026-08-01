---
manifest_id: DEB-001-HASH-MANIFEST-0.1
experiment_id: DEB-001
version: v0.1
scope: immutable-hash-manifest
status: draft
created_at: 2026-07-24
reference_docs:
  - DEB-001-CONFIGURATION-SNAPSHOT-v0.1
  - DEB-001-CLOSURE-PLAN-v0.1
  - DEB-001-CLOSURE-STATUS-UPDATE-v0.1
implementation_authorized: false
runtime_authorized: false
api_authorized: false
authority_system: none
---

# DEB-001-HASH-MANIFEST-v0.1

## 1. Experiment identity（实验身份）

- `experiment_id`: `DEB-001`
- `experiment_version`: `v0.1`
- `experiment_name`: `DEB-001 Efficiency vs Survival`
- `manifest_scope`: configuration identity closure before Alpha execution

## 2. Configuration hash entries（配置哈希条目）

### 2.1 experiment specification

- `experiment_specification_reference`: `DEB-001-PILOT-PACKAGE-v0.1`
- `experiment_specification_hash`: `<TBD>`

### 2.2 strategy baseline

- `strategy_baseline_reference`: `DEB-001-STRATEGY-BASELINE-v0.1`
- `strategy_baseline_hash`: `<TBD>`

### 2.3 environment configuration

- `environment_configuration_reference`: `DEB-001-ALPHA-EXECUTION-PLAN-v0.1`
- `environment_configuration_hash`: `<TBD>`

### 2.4 result schema

- `result_schema_reference`: `SPEC-DIGITAL-ECOLOGY-BOX-RESULT-v0.1`
- `result_schema_hash`: `<TBD>`

### 2.5 metric definition

- `metric_definition_reference`: `SPEC-DIGITAL-ECOLOGY-BOX-RESULT-v0.1`
- `metric_definition_hash`: `<TBD>`
- `metric_set`:
  - Survival Fitness
  - Adaptation Velocity
  - Diversity Index
  - Resilience Score
  - Stability Index
  - Dependency Index

## 3. Evidence artifact hash entries（证据制品哈希条目）

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

## 4. Hash metadata（哈希元数据）

- `algorithm`: `sha256`
- `generated_at`: `<ISO-8601 timestamp>`
- `source_reference`: `DEB-001-CONFIGURATION-SNAPSHOT-v0.1`
- `version`: `v0.1`
- `status`: `DRAFT`

## 5. Manifest lifecycle（清单生命周期）

- `DRAFT`
- `FROZEN`
- `SUPERSEDED`

### Lifecycle semantics

- `DRAFT`: defined but not yet immutable.
- `FROZEN`: finalized and treated as immutable for Alpha execution.
- `SUPERSEDED`: replaced by a newer manifest version.

## 6. Freeze requirements（冻结要求）

A manifest can enter `FROZEN` only when:

1. All configuration hash entries are present and populated.
2. All evidence artifact hash entries are present and populated.
3. Source references point to immutable snapshots.
4. Reviewer confirmation is recorded and linked.

## 7. Non-goals（非目标）

- no execution approval
- no runtime authority
- no scientific conclusion

