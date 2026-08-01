# DEB-001-LITE-DRY-RUN-EVENT-RECORD-v0.1

## Scope

Minimal event record template for the first DEB-001 Lite dry run.

No code.
No API.
No runtime implementation.

References:
- [DEB-001-LITE-DRY-RUN-INSTANCE-v0.1](DEB-001-LITE-DRY-RUN-INSTANCE-v0.1)
- [DEB-001-LITE-EXECUTION-PROTOCOL-v0.1](DEB-001-LITE-EXECUTION-PROTOCOL-v0.1)
- [DEB-001-LITE-MINIMAL-RESULT-v0.1](DEB-001-LITE-MINIMAL-RESULT-v0.1)

## 1) Dry run identity

- `dry_run_id`
- `run_id`
- `seed`
- `timestamp`

## 2) Phase event records

### Stable

- phase start condition
- phase round range
- major phase-level perturbations: none
- transition marker

### Shock

- phase start condition
- phase round range
- perturbation marker
- transition marker

### Recovery

- phase start condition
- phase round range
- recovery marker
- transition marker

Use one row per phase and one optional note per phase.

## 3) Agent event records

Minimum fields per row:

- `agent_id`
- `strategy_type`
- `round`
- `action_id`
- `resource_delta`
- `continuation_state`

Recommended minimal table schema:

| agent_id | strategy_type | round | phase | action_id | resource_delta | continuation_state |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## 4) Evidence generation status

- `agent_state_log`: [PASS | PARTIAL | FAILED]
- `selection_log`: [PASS | PARTIAL | FAILED]
- `phase_log`: [PASS | PARTIAL | FAILED]
- `outcome_log`: [PASS | PARTIAL | FAILED]

Add brief reason when not PASS.

## 5) Completion status

- COMPLETE
- PARTIAL
- FAILED

## 6) Limitations

- Not scientific result
- Not DST validation
- Not production execution

