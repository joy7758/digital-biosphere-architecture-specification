---
artifact_type: DEB-READINESS-STATUS-TEMPLATE
artifact_id: DEB-READINESS-STATUS-MATRIX-v0.1
version: v0.1
scope: readiness-status-template
purpose: machine-and-human-readable readiness summary from DEB-001-EXPERIMENTAL-ALIGNMENT-CHECKLIST-v0.1
reference_checklist: DEB-001-EXPERIMENTAL-ALIGNMENT-CHECKLIST-v0.1
status_model: status-values-and-overall-state-only-template
domain: Digital Ecology Box (DBE)
execution_authorized: false
runtime_authorized: false
api_authorized: false
---

# DEB-READINESS-STATUS-MATRIX-v0.1.yaml.md

## 0. Machine-Readable Status Payload（可机读状态载荷）

```yaml
experiment_identity:
  experiment_id: "DEB-001"
  version: "v0.1"
  package_reference: "DEB-001-PILOT-PACKAGE-v0.1.md"

sections:
  - name: identity
    status: UNKNOWN   # PASS | FAIL | NOT_READY | UNKNOWN
    required_items:
      - field: experiment_id
        check: completed_or_pinned
        status: UNKNOWN
        notes: ""
      - field: version
        check: completed_or_pinned
        status: UNKNOWN
        notes: ""
      - field: package_reference
        check: exists_and_trackable
        status: UNKNOWN
        notes: ""

  - name: hypothesis
    status: UNKNOWN
    required_items:
      - field: primary_hypothesis
        check: clear_testable_form
        status: UNKNOWN
        notes: ""
      - field: null_hypothesis
        check: explicitly_defined
        status: UNKNOWN
        notes: ""
      - field: falsification_criteria
        check: measurable_and_predefined
        status: UNKNOWN
        notes: ""

  - name: strategy_baseline
    status: UNKNOWN
    required_items:
      - field: efficiency_strategy
        check: versioned_strategy_baseline_defined
        status: UNKNOWN
        notes: ""
      - field: balance_strategy
        check: versioned_strategy_baseline_defined
        status: UNKNOWN
        notes: ""
      - field: exploration_strategy
        check: versioned_strategy_baseline_defined
        status: UNKNOWN
        notes: ""
      - field: strategy_versioning
        check: immutable_within_run
        status: UNKNOWN
        notes: ""

  - name: environment
    status: UNKNOWN
    required_items:
      - field: environment_phases
        check: defined_and_reproducible
        status: UNKNOWN
        notes: ""
      - field: drift_scarcity_shock_model
        check: phase_boundaries_and_parameters_defined
        status: UNKNOWN
        notes: ""
      - field: environment_version
        check: pinned
        status: UNKNOWN
        notes: ""

  - name: resource_selection_pressure
    status: UNKNOWN
    required_items:
      - field: resource_configuration
        check: total_and_renewal_defined
        status: UNKNOWN
        notes: ""
      - field: selection_pressure_variables
        check: all_variables_defined
        status: UNKNOWN
        notes: ""
      - field: concentration_and_guard_settings
        check: explicitly_stated
        status: UNKNOWN
        notes: ""

  - name: evidence
    status: UNKNOWN
    required_items:
      - field: lineage_records
        check: collection_and_reference_required
        status: UNKNOWN
        notes: ""
      - field: action_traces
        check: collection_and_reference_required
        status: UNKNOWN
        notes: ""
      - field: selection_records
        check: collection_and_reference_required
        status: UNKNOWN
        notes: ""
      - field: outcome_records
        check: collection_and_reference_required
        status: UNKNOWN
        notes: ""

  - name: reproducibility
    status: UNKNOWN
    required_items:
      - field: seed
        check: declared_and_frozen
        status: UNKNOWN
        notes: ""
      - field: environment_configuration_hash
        check: declared
        status: UNKNOWN
        notes: ""
      - field: agent_strategy_version
        check: declared
        status: UNKNOWN
        notes: ""
      - field: experiment_specification_version
        check: declared
        status: UNKNOWN
        notes: ""
      - field: replay_requirements
        check: explicit_and_testable
        status: UNKNOWN
        notes: ""
      - field: independent_replication_plan
        check: planned
        status: UNKNOWN
        notes: ""

  - name: publication
    status: UNKNOWN
    required_items:
      - field: result_schema_compliance
        check: DigitalEcologyBoxResult
        status: UNKNOWN
        notes: ""
      - field: falsification_status
        check: supported_or_rejected_or_inconclusive
        status: UNKNOWN
        notes: ""
      - field: evidence_references
        check: complete_and_immutable
        status: UNKNOWN
        notes: ""
      - field: publication_metadata
        check: includes_versions_and_timestamps
        status: UNKNOWN
        notes: ""

  - name: archive
    status: UNKNOWN
    required_items:
      - field: immutable_reference
        check: write_once_or_never_modify
        status: UNKNOWN
        notes: ""
      - field: version_linkage
        check: all_links_to_versions_recorded
        status: UNKNOWN
        notes: ""
      - field: experiment_lineage
        check: parent_or_follow_ups_recorded
        status: UNKNOWN
        notes: ""

  - name: limitations
    status: UNKNOWN
    required_items:
      - field: non_code_no_runtime_no_api
        check: explicitly_stated
        status: UNKNOWN
        notes: ""
      - field: no_governance_authority
        check: explicitly_stated
        status: UNKNOWN
        notes: ""
      - field: uncertainty_and_scope_notes
        check: included
        status: UNKNOWN
        notes: ""

overall_status: PREPARATION # PREPARATION | READY_FOR_EXECUTION_REVIEW | EXECUTION_READY | PUBLISHED | ARCHIVED

blocking_issues:
  - "List blocking issue statements when section status is FAIL or NOT_READY."

missing_items:
  - "List concrete missing fields and evidence links if applicable."

notes:
  - "Keep this template machine-editable and human-readable in parallel."
  - "Do not infer pass/fail by external interpretation; this file is a reporting template only."

reviewer_comments:
  - reviewer: ""
    comment: ""
    timestamp: ""
```

## 1. Purpose and Use（用途）

This template is for producing a compact readiness report for one DEB experiment (especially DEB-001).

- Populate status values exactly from `{PASS, FAIL, NOT_READY, UNKNOWN}`.
- Keep status values consistent across sections and provide concise supporting notes.
- Do not embed execution logic or automatic evaluators.

## 2. Status Value Meaning（状态说明）

- `PASS`: required conditions met and justified.
- `FAIL`: condition checked and violated.
- `NOT_READY`: not yet prepared or incomplete.
- `UNKNOWN`: not assessed yet.

## 3. Overall Status Meaning（总状态说明）

- `PREPARATION`: initial creation and partial completion.
- `READY_FOR_EXECUTION_REVIEW`: ready for review stage, not yet executed.
- `EXECUTION_READY`: ready for reproducible execution attempt.
- `PUBLISHED`: result published and mapped to result specification.
- `ARCHIVED`: archived immutably with lineage links.

## 4. Reference

- Derived from: `DEB-001-EXPERIMENTAL-ALIGNMENT-CHECKLIST-v0.1.md`

## 5. Non-goals（非目标）

- no code
- no API
- no runtime
- no implementation of validation engine
