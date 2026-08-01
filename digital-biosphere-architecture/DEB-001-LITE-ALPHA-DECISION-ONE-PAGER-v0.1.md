# DEB-001-LITE-ALPHA-DECISION-ONE-PAGER-v0.1

## 1) Mission

Run the first minimal Digital Ecology Box experiment workflow in Lite mode to verify whether selection dynamics are observable under a simple Stable/Shock/Recovery sequence, before expanding to full DEB governance and execution infrastructure.

## 2) Current phase and status

- Phase: Pre-Dry-Run preparation
- Status: Ready for dry-run execution documentation package
- Next checkpoint: Dry Run completion review
- Decision objective: determine readiness for Alpha Decision

## 3) Experimental setup

### Population

- Efficiency: `3`
- Balance: `3`
- Exploration: `3`
- Total: `9` agents

### Environment

- Stable phase
- Shock phase
- Recovery phase

### Minimal objective

- Observe whether behavior and continuation differences emerge across the three strategy populations under phase transitions.

## 4) Evidence outputs

Required outputs (minimal set):

- `agent_state_log`
- `selection_log`
- `phase_log`
- `outcome_log`

## 5) Decision pathway

`Dry Run` -> `Alpha Decision` -> `Alpha Run`

### Dry Run outputs to produce

- DEB-001-LITE-DRY-RUN-INSTANCE-v0.1
- DEB-001-LITE-DRY-RUN-CHECKLIST-v0.1
- DEB-001-LITE-DRY-RUN-CHECKLIST-RESULTS-v0.1
- DEB-001-LITE-DRY-RUN-EVENT-RECORD-v0.1
- DEB-001-LITE-DRY-RUN-RESULT-REPORT-v0.1

### Alpha Decision inputs

- Checklist outcome status (PASS / PARTIAL / FAILED)
- Evidence-generation completeness
- Completion status of event and result records

### Alpha Run trigger

- `READY_FOR_ALPHA` recommendation in result report
- all non-negotiable required outputs complete

## 6) Non-goals

- no scientific conclusion
- no DST validation
- no production execution

