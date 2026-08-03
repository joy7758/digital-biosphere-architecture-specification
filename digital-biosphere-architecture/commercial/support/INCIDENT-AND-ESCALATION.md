# Incident and Escalation / 事件与升级

`STATUS=HUMAN_REVIEW_DRAFT`

## Flow

```text
Finding -> Preserve bounded evidence -> Classify -> Human owner review
        -> Contain or stop -> Customer notice if contractually required
        -> Recovery assessment -> Closure or retained limitation
```

Every event record must identify the workspace, time, affected surface, reporter, evidence references, containment, known limitations and Human disposition. Raw customer content, credentials and secrets must not enter the governance repository.

Immediate stop conditions include suspected cross-tenant access, secret disclosure, unauthorized action effect, Receipt integrity failure, uncontrolled retention and inability to revoke access. Verification does not authorize recovery or reopening.

Notification timing, contacts and legal duties remain customer- and contract-specific. Until assigned in a signed SOW:

```text
SECURITY_CONTACT_ASSIGNED=false
INCIDENT_NOTIFICATION_COMMITMENT=false
```
