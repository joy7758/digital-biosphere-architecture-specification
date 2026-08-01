# DEB-001-LITE-EXECUTION-PROTOCOL-v0.1

## Scope

This document defines the minimal execution protocol for DEB-001 Lite. It is a small-scale experimental protocol used to observe selection dynamics with minimal complexity.

No production runtime.
No API.
No governance infrastructure.
No code.

References:
- [DEB-001-LITE-DESIGN-v0.1](DEB-001-LITE-DESIGN-v0.1)
- [Digital-Survival-Theory-Foundation-v0.1](Digital-Survival-Theory-Foundation-v0.1)

## 1) Experiment initialization

1. Set a single experiment identifier and version for the Lite protocol.
2. Fix the random or deterministic seed policy before execution.
3. Freeze phase durations (stable, shock, recovery) and resource scaling rules.
4. Freeze population composition:
   - Efficiency x3
   - Balance x3
   - Exploration x3
5. Fix evidence format and recording schema for all runs.
6. Define run label format for baseline reproducibility (`run_id`, `round_id`, `phase_id`).

## 2) Agent setup

### Population composition

- Efficiency strategy population: **3 agents**
- Balance strategy population: **3 agents**
- Exploration strategy population: **3 agents**

### Population initialization

1. Create each agent instance with minimal strategy metadata only:
   - strategy family
   - initial resource reserve
   - exploration/adaptation toggle states
2. Set all agents to active status at round 0.
3. Ensure no cross-strategy identity leakage in initialization (same starting baseline except strategy tag).
4. Record initial state snapshot for all 9 agents.

## 3) Round lifecycle

Each round executes the following fixed sequence:

1. Observation
   - Capture environment context and available resource level.
   - Record per-agent observable state.
2. Action selection
   - Each agent chooses one action under its strategy rules.
   - No strategy-level exceptions are allowed in Lite protocol.
3. Resource interaction
   - Apply chosen action to shared resource pool.
   - Update resource use and residual availability.
4. Environment update
   - Update phase state if scheduled.
   - Apply any shock/recovery transformations.
5. Continuation evaluation
   - Evaluate each agent’s continuation score for next-round eligibility.
6. Evidence recording
   - Persist observations, actions, resource deltas, state transitions, and continuation outcomes.

All rounds must follow this order without branch logic.

## 4) Stable/Shock/Recovery phase behavior

### Stable phase

- Constant resource scaling.
- No abrupt perturbation.
- Purpose: establish baseline selection pressure and adaptation baseline.
- No forced intervention by protocol except scheduled logging.

### Shock phase

- Apply predefined single perturbation to resource scaling and/or outcome conversion.
- Increase cost of over-specialized/low-adaptive behavior.
- Purpose: test resilience and immediate selection response.

### Recovery phase

- Remove the initial shock and return to reduced-volatility parameters.
- Allow partial re-equilibration.
- Purpose: observe which populations recover continuation better.

Each phase boundary is explicitly logged and included in evidence.

## 5) Minimal state variables

The protocol uses only the following state variables:

- `agent_id`
- `strategy_type`
- `phase` (stable / shock / recovery)
- `round_index`
- `resource_balance`
- `resource_cost`
- `action_id`
- `continuation_score`
- `active_flag`
- `lineage_id`
- `event_tags` (optional, e.g., adaptation_event, stress_signal)

## 6) Minimal evidence outputs

### Required outputs

1. `agent_state_log`
   - agent id, strategy type, phase, round, action, resource cost, remaining resource, active flag
2. `selection_log`
   - continuation score, continuation decision, dropout reason
3. `phase_log`
   - phase start/end, perturbation parameters, replay tags
4. `outcome_log`
   - per-round and per-strategy population outcomes
5. `lineage_log`
   - lineage id, continuation transitions, phase-local transitions

All logs must be immutable-per-run and version-linked.

## 7) Termination conditions

End experiment when any condition is met:

- All agents in one or more strategies become inactive.
- Maximum round limit reached.
- Stable→Shock→Recovery sequence completed.
- Termination rule override not used unless explicitly defined in this protocol revision.

Upon termination, generate one terminal snapshot containing final active composition and complete logs.

## 8) Result summary requirements

A minimal summary must include:

1. Survival/continuation summary by strategy.
2. Distribution of actions by strategy and phase.
3. Resource utilization trend by strategy.
4. Phase transition effects and continuation changes across phase boundaries.
5. Selection transition notes by strategy.
6. Any observed divergence from expected dynamics and open uncertainty.

## 9) Non-goals

- No AI consciousness claims.
- No runtime governance.
- No production deployment.
- No full DEB infrastructure.
- No authority claims over execution permission.

