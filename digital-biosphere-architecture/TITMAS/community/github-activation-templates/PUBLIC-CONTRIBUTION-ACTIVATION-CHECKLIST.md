# Public Contribution Activation Checklist

Status: `BLOCKED`

The dormant templates may be installed only through a future, independent
Activation PR after every required condition has direct evidence.

| Required condition | Current state |
|---|---|
| `SECURITY_TRANSPORT_ACTIVE=true` | `NOT_MET` |
| `PUBLIC_CONTRIBUTION_SURFACE_AUTHORIZED=true` | `NOT_MET` |
| `COMMUNITY_HD_03=ACCEPT` | `NOT_MET` |
| `ACTIVATION_PR_CREATED=true` | `NOT_MET` |
| `ACTIVATION_PR_HUMAN_REVIEWED=true` | `NOT_MET` |
| `ACTIVE_TEMPLATE_HASHES_MATCH_DORMANT_PACKAGE=true` | `NOT_ASSESSED` |
| `COMMUNITY_STATUS_UPDATED=true` | `NOT_MET` |
| `ROLLBACK_TESTED=true` | `NOT_EXECUTED` |

If any condition is not met, activation fails closed.

```text
ACTIVATION_BLOCKED=true
PUBLIC_CONTRIBUTION_TEMPLATES_INSTALLED=false
PUBLIC_CONTRIBUTION_SURFACE_ACTIVE=false
PUBLIC_ACTIVATION_REQUIRES_SEPARATE_PR=true
```
