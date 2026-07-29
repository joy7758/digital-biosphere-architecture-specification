# Public Contribution Activation Checklist

Status: `ACTIVATION_PR_PREPARATION_IN_PROGRESS`

The templates are installed only on the independent Activation PR branch.
They remain inactive until that PR is reviewed and merged.

| Required condition | Current state |
|---|---|
| `SECURITY_TRANSPORT_ACTIVE=true` | `MET` |
| `PUBLIC_CONTRIBUTION_SURFACE_AUTHORIZED=true` | `MET` |
| `COMMUNITY_HD_03=ACCEPT_AND_EXECUTE` | `MET` |
| `ACTIVATION_PR_CREATED=true` | `NOT_MET` |
| `ACTIVATION_PR_HUMAN_REVIEWED=true` | `NOT_MET` |
| `ACTIVE_TEMPLATE_HASHES_MATCH_DORMANT_PACKAGE=true` | `MET` |
| `COMMUNITY_STATUS_UPDATED=true` | `MET` |
| `ROLLBACK_TESTED=true` | `MET_DETERMINISTIC_FAIL_CLOSED_SIMULATION` |

If any condition is not met, activation fails closed.

```text
ACTIVATION_BLOCKED=true
PUBLIC_CONTRIBUTION_TEMPLATES_INSTALLED=true
PUBLIC_CONTRIBUTION_SURFACE_ACTIVE=false
PUBLIC_ACTIVATION_REQUIRES_SEPARATE_PR=true
```
