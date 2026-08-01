# DEB-001-LITE-MINIMAL-RESULT-v0.1

## Scope

This document defines the smallest experiment result object for the first DEB-001 Lite run.

No code.
No API.
No runtime implementation.

References:
- [DEB-001-LITE-DESIGN-v0.1](DEB-001-LITE-DESIGN-v0.1)
- [DEB-001-LITE-EXECUTION-PROTOCOL-v0.1](DEB-001-LITE-EXECUTION-PROTOCOL-v0.1)
- [DEB-001-LITE-RUN-CONFIG-v0.1](DEB-001-LITE-RUN-CONFIG-v0.1)

## 1) Run identity

- `run_id`
- `experiment_id`
- `version`
- `seed`
- `timestamp`

Example identity block:

- `experiment_id`: `DEB-001-LITE`
- `version`: `v0.1`
- `run_id`: `DEB-001-LITE-RUN-0001`
- `seed`: `SEED-2026-001`
- `timestamp`: ISO-8601

## 2) Population outcome

### 2.1 Efficiency strategy population (x3)

- `active_agents`
- `continuation_rate`
- `resource_summary`

### 2.2 Balance strategy population (x3)

- `active_agents`
- `continuation_rate`
- `resource_summary`

### 2.3 Exploration strategy population (x3)

- `active_agents`
- `continuation_rate`
- `resource_summary`

#### Field definitions

- `active_agents`: number of agents still active at run end
- `continuation_rate`: ratio of active agents to initial population of the strategy
- `resource_summary`: minimal aggregate consumption/effective gain summary per strategy

## 3) Phase outcome

For each phase record:

- `Stable`
- `Shock`
- `Recovery`

Each phase section includes:

- continuation rate by strategy
- population active count by strategy
- resource summary by strategy
- phase-level observation notes (free text)

## 4) Selection observation

Minimal observable selection layer includes:

- `continuation_changes`
  - continuation transitions per strategy and phase
- `dropout_events`
  - identity-linked dropouts with round and phase
- `strategy_behavior_changes`
  - qualitative or encoded behavior drift indicators

## 5) Evidence references

Only include these evidence references:

- `agent_state_log`
- `selection_log`
- `phase_log`
- `outcome_log`

Each reference includes source id, storage location, and immutable checksum.

## 6) Observation confidence and limitations

### Confidence

- Confidence is minimal and evidence-bound.
- Confidence scoring is based only on evidence completeness across required logs and phase coverage.

### Limitations

- Tiny population and fixed strategy count.
- Minimal metrics and coarse behavior encoding.
- No broader DEB policy, governance, or infrastructure effects.
- Results are observational only and should not be over-generalized.

## 7) Non-goals

- no scientific law claims
- no AI consciousness claims
- no governance authority
- no full DEB schema replacement

