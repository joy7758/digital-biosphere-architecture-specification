# DEB-001-LITE-DRY-RUN-CHECKLIST-v0.1

## Scope

Minimal manual verification checklist for DEB-001 Lite dry run.

No code.
No API.
No runtime implementation.

References:
- [DEB-001-LITE-DESIGN-v0.1](DEB-001-LITE-DESIGN-v0.1)
- [DEB-001-LITE-EXECUTION-PROTOCOL-v0.1](DEB-001-LITE-EXECUTION-PROTOCOL-v0.1)
- [DEB-001-LITE-RUN-CONFIG-v0.1](DEB-001-LITE-RUN-CONFIG-v0.1)
- [DEB-001-LITE-DRY-RUN-PLAN-v0.1](DEB-001-LITE-DRY-RUN-PLAN-v0.1)

## 1) Initialization checks

- [ ] Scope and objective identified as workflow validation only.
- [ ] Run config reference is loaded and recorded (experiment id/version/seed/round plan).
- [ ] Required phase order is confirmed: `Stable -> Shock -> Recovery`.
- [ ] Minimum result schema reference is confirmed (DEB-001-LITE-MINIMAL-RESULT-v0.1).
- [ ] No runtime governance, no deployment, no full DEB infrastructure assumptions applied in dry run.

## 2) Agent population checks

- [ ] Efficiency population size = 3.
- [ ] Balance population size = 3.
- [ ] Exploration population size = 3.
- [ ] Total active initialized agents = 9.
- [ ] All agents have one assigned strategy label.
- [ ] Initial state is baseline and comparable across all agents except strategy tag.

## 3) Phase transition checks

### Stable

- [ ] Stable phase starts at run start.
- [ ] Stable phase label appears in all required evidence outputs.
- [ ] No shock perturbation applied in this phase.

### Shock

- [ ] Shock phase starts at configured round boundary.
- [ ] Shock label appears in all required evidence outputs.
- [ ] Perturbation is applied as specified in run config.
- [ ] Transition from Stable to Shock is uniquely recorded.

### Recovery

- [ ] Recovery phase starts at configured round boundary.
- [ ] Recovery label appears in all required evidence outputs.
- [ ] Post-shock transition is uniquely recorded.
- [ ] No additional unplanned phase appears in output logs.

## 4) State recording checks

- [ ] Per round has `round_index` and `phase`.
- [ ] Per agent has `agent_id`, `strategy_type`, `action_id`, `resource_balance` (or equivalent state field), and `active_flag`.
- [ ] Continuation status is recorded at round end.
- [ ] Lineage identifier is present when agent continuity changes.
- [ ] Event tags are captured for shock-related behavior changes.

## 5) Evidence output checks

### agent_state_log

- [ ] Contains entries for all rounds and all active/changed agents.
- [ ] Contains required fields above.

### selection_log

- [ ] Contains continuation score/decision per agent per round.
- [ ] Contains dropout events with phase and round context.

### phase_log

- [ ] Contains phase boundaries with timestamps/round indexes.
- [ ] Contains phase-specific parameters.

### outcome_log

- [ ] Contains final and per-phase strategy outcomes.
- [ ] Includes survival/continuation summary and resource summaries.

## 6) Minimal result generation checks

- [ ] `DEB-001-LITE-MINIMAL-RESULT-v0.1` object generated.
- [ ] Identity fields complete:
  - run_id
  - experiment_id
  - version
  - seed
  - timestamp
- [ ] All three strategy populations reported:
  - Efficiency
  - Balance
  - Exploration
- [ ] Active agent counts and continuation rates reported.
- [ ] Phase outcome blocks for Stable/Shock/Recovery present.
- [ ] Selection observation blocks present.
- [ ] Evidence references point to produced logs.

## 7) Dry run status

Set exactly one:

- PASS
- PARTIAL
- FAILED

Status rules:

- PASS: all required lifecycle, phase, state, evidence, and result checks pass.
- PARTIAL: workflow mostly complete with limited missing non-critical fields.
- FAILED: missing mandatory field or required evidence output or phase mis-order.

## 8) Non-goals

- no scientific conclusion
- no DST validation
- no production execution

