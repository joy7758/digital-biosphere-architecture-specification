# DEB-001-LITE-RUN-CONFIG-v0.1

## Scope

This document defines the minimal fixed run configuration for the first DEB-001 Lite experiment.

No code.
No API.
No runtime implementation.

References:
- [DEB-001-LITE-DESIGN-v0.1](DEB-001-LITE-DESIGN-v0.1)
- [DEB-001-LITE-EXECUTION-PROTOCOL-v0.1](DEB-001-LITE-EXECUTION-PROTOCOL-v0.1)
- [Digital-Survival-Theory-Foundation-v0.1](Digital-Survival-Theory-Foundation-v0.1)

## 1) Experiment identity

- experiment_id: `DEB-001-LITE`
- experiment_version: `v0.1`
- run_type: `minimal_reproducible`
- purpose: observe minimal selection dynamics before larger governance scaling

## 2) Agent configuration

- strategy family: Efficiency
  - count: `3`
- strategy family: Balance
  - count: `3`
- strategy family: Exploration
  - count: `3`

Total agents: `9`

## 3) Initial conditions

### 3.1 starting resource

- initial shared resource budget: fixed value `R0`
- per-agent initial resource grant: `R_agent`
- no private reserve transfer in round 1

### 3.2 initial state

- all agents start active
- all agents start with baseline strategy tag only
- all agents share initial metadata structure
- all phase indicators set to `stable`
- initial continuation score set to the same baseline value

### 3.3 seed policy

- `seed_mode`: fixed and recorded (`seed`)
- `seed_source`: explicit in run header (e.g., `SEED-2026-001`)
- seed must be unchanged for baseline run and reported in evidence header

## 4) Phase configuration

The experiment uses a fixed 3-phase plan:

1. **Stable phase**
   - name: `stable`
   - objective: establish baseline behavior
   - perturbation flag: `false`

2. **Shock phase**
   - name: `shock`
   - objective: test mismatch response under abrupt change
   - perturbation flag: `true`

3. **Recovery phase**
   - name: `recovery`
   - objective: observe rebound and persistence after shock
   - perturbation flag: `false`

## 5) Round configuration

- total rounds: `R_total`
- phase durations:
  - `rounds_stable = N_stable`
  - `rounds_shock = N_shock`
  - `rounds_recovery = N_recovery`
  - constraint: `R_total = N_stable + N_shock + N_recovery`
- phase order: `stable -> shock -> recovery`
- no phase order deviation in this run

## 6) Continuation evaluation reference

Continuation evaluation uses one fixed rule family:

- evaluate continuation at the end of each round
- continuation score computed from resource status, action effectiveness, and shock resilience term
- continuation decision uses threshold-based persistence rule
- score and threshold are fixed for the run

## 7) Evidence output reference

Required outputs are fixed for this run:

- `agent_state_log`
- `selection_log`
- `phase_log`
- `outcome_log`
- `lineage_log`

All evidence outputs must be labeled with:

- experiment_id
- version
- run_id
- seed
- phase tag
- round index

## 8) Reproducibility fields

Must record in every run package:

- experiment_id
- experiment_version
- run_id
- seed
- phase configuration
- agent composition counts
- initial resource values
- round counts per phase
- continuation rule identifier
- evidence output references (immutable per run)
- protocol version reference

## Non-goals

- no production runtime
- no governance authority
- no full DEB infrastructure

