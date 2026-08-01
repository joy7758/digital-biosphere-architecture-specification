# DEB-001-LITE-DRY-RUN-INSTANCE-v0.1

## Scope

Define the first concrete dry-run instance configuration for DEB-001 Lite.

No code.
No API.
No runtime implementation.

References:
- [DEB-001-LITE-RUN-CONFIG-v0.1](DEB-001-LITE-RUN-CONFIG-v0.1)
- [DEB-001-LITE-DRY-RUN-PLAN-v0.1](DEB-001-LITE-DRY-RUN-PLAN-v0.1)
- [DEB-001-LITE-DRY-RUN-CHECKLIST-v0.1](DEB-001-LITE-DRY-RUN-CHECKLIST-v0.1)
- [DEB-001-LITE-DRY-RUN-CHECKLIST-RESULTS-v0.1](DEB-001-LITE-DRY-RUN-CHECKLIST-RESULTS-v0.1)

## 1) Dry run identity

- `dry_run_id`: `DEB-001-LITE-DRY-RUN-001`
- `experiment_id`: `DEB-001-LITE`
- `version`: `v0.1`
- `created_at`: `[ISO-8601 timestamp]`

## 2) Configuration reference

### 2.1 run config reference

- `run_config`: [DEB-001-LITE-RUN-CONFIG-v0.1](DEB-001-LITE-RUN-CONFIG-v0.1)

### 2.2 strategy configuration

- Efficiency population size: `3`
- Balance population size: `3`
- Exploration population size: `3`
- Total agents: `9`

### 2.3 environment configuration

- Phase order: `Stable -> Shock -> Recovery`
- Environment follows fixed 3-phase Lite setup.

## 3) Minimal execution parameters

- `agent_count`: `9`
- `total_rounds`: `R_total`
- `stable_phase_rounds`: `N_stable`
- `shock_phase_rounds`: `N_shock`
- `recovery_phase_rounds`: `N_recovery`
- `seed`: `SEED-2026-001`

Constraint:

- `R_total = N_stable + N_shock + N_recovery`

## 4) Expected outputs

- `agent_state_log`
- `selection_log`
- `phase_log`
- `outcome_log`

Each output must include run identity and phase context.

## 5) Completion criteria

Dry run instance is complete when:

1. All 9 agents are initialized according to strategy configuration.
2. Phase sequence is executed in order with recorded boundaries.
3. Required evidence outputs are produced and linked to run identity.
4. Minimal result object can be composed from outputs.
5. No missing mandatory fields in checklist core items.

## 6) Non-goals

- no scientific conclusion
- no DST validation
- no production execution

