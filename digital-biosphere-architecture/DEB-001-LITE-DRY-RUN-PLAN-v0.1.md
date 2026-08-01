# DEB-001-LITE-DRY-RUN-PLAN-v0.1

## Scope

Define the first dry-run validation plan for DEB-001 Lite.

No code.
No API.
No runtime implementation.

References:
- [DEB-001-LITE-DESIGN-v0.1](DEB-001-LITE-DESIGN-v0.1)
- [DEB-001-LITE-EXECUTION-PROTOCOL-v0.1](DEB-001-LITE-EXECUTION-PROTOCOL-v0.1)
- [DEB-001-LITE-RUN-CONFIG-v0.1](DEB-001-LITE-RUN-CONFIG-v0.1)
- [DEB-001-LITE-MINIMAL-RESULT-v0.1](DEB-001-LITE-MINIMAL-RESULT-v0.1)

## 1) Dry-run purpose

Validate the DEB-001 Lite workflow end-to-end.

- Confirm protocol sequence and phase lifecycle behavior are executable by design.
- Confirm required evidence outputs are produced and linked.
- Confirm minimal result object can be generated.

**This is workflow validation only, not scientific hypothesis validation.**

## 2) Minimal setup

- Efficiency population: `3`
- Balance population: `3`
- Exploration population: `3`

Total agents: `9`

## 3) Round configuration

Run with the fixed 3-phase plan:

1. `Stable`
2. `Shock`
3. `Recovery`

Round counts are those defined by `DEB-001-LITE-RUN-CONFIG-v0.1`.

## 4) Validation targets

### 4.1 lifecycle completion

- Confirm initialization -> rounds -> termination path is complete.
- Confirm phase transitions occur in the order `Stable -> Shock -> Recovery`.
- Confirm all required lifecycle steps are logged.

### 4.2 phase transition

- Confirm phase boundaries are explicit and single-source-of-truth in logs.
- Confirm phase labels are consistent across all outputs.

### 4.3 evidence generation

- Confirm required evidence files/streams exist for the run.
- Confirm each required evidence entry has run metadata.

### 4.4 result object generation

- Confirm a minimal result object is produced according to:
  - [DEB-001-LITE-MINIMAL-RESULT-v0.1](DEB-001-LITE-MINIMAL-RESULT-v0.1)
- Confirm run identity and population outputs are present.

## 5) Expected outputs

- `agent_state_log`
- `selection_log`
- `phase_log`
- `outcome_log`

Each output must include:

- phase tag
- round index
- agent identity
- required minimal state/evidence fields

## 6) Success criteria

Dry-run is successful when all conditions are met:

1. complete execution path
2. no missing mandatory fields
3. evidence and result outputs are generated in reproducible structure
4. no deviation from fixed phase order
5. deterministic or fixed-seed reproducibility documented in run header

## 7) Non-goals

- no scientific conclusions
- no theory validation
- no production deployment

