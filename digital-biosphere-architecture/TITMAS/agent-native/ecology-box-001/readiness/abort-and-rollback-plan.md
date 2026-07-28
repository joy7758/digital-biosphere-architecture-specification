# Ecology Box 001 Abort and Rollback Plan v0.1

Stopping a run protects evidence and boundaries. It does not automatically
mean the experimental hypothesis failed.

## Who may stop

- assigned Emergency Stop Authority;
- Accountable Human Owner;
- assigned blind custodian for blinding compromise;
- any participant may request a fail-closed stop, but cannot authorize restart.

## Immediate-stop reason codes

| Code | Condition |
|---|---|
| `ABORT-AUTHORITY` | Authority or Permission boundary violation |
| `ABORT-CREDENTIAL` | credential, secret or private prompt exposure |
| `ABORT-SEMANTIC` | Evidence, Recommendation or test result elevated |
| `ABORT-FREEZE` | source, task, metric, role or protocol drift |
| `ABORT-BLIND` | blind key, label or origin-map compromise |
| `ABORT-REVIEWER` | Reviewer conflict or prohibited prior access |
| `ABORT-LINEAGE` | lineage misrepresentation |
| `ABORT-PROVIDER` | returned model, Provider or retention mismatch |
| `ABORT-PRIVACY` | data-handling policy breach |
| `ABORT-REPRO` | non-reproducible required validation |
| `ABORT-NETWORK` | unapproved external network action |

## Procedure

1. stop the affected task or batch without automatic retry;
2. seal current artifacts and append a sanitized incident receipt;
3. quarantine affected candidates and origin mappings;
4. preserve failures, logs and limitations without deletion;
5. restore only the disposable workspace from the frozen source snapshot;
6. require Human review and a new delta authorization before restart.

Rollback returns the workspace to the frozen input state; it does not delete
evidence or erase the incident.

## Result taxonomy

```text
ABORTED_FOR_SAFETY
INVALIDATED_BY_PROTOCOL_DEVIATION
COMPLETED_NEGATIVE_RESULT
COMPLETED_POSITIVE_RESULT
NOT_ASSESSED
```

Restart eligibility is `NOT_ASSESSED` until the Human Owner records the exact
root cause, corrected control, preserved evidence and new authorization.
