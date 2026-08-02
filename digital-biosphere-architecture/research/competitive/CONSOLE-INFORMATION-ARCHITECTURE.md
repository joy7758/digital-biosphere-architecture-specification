# TITMAS Console Information Architecture Research

Status: `PRIVATE_RESEARCH_BASELINE`

## Observed reusable patterns

- LangSmith uses organization/workspace separation, workspace-scoped usage and
  retention, project views, and explicit billing surfaces.
- AgentLoop exposes data, Trace, evaluation, experiments, registered services
  and system management as distinct assets.
- Permit exposes identity, tenant, environment, policy, decision logs and
  quota as first-class concepts.
- Cisco, WitnessAI and HiddenLayer use progressive navigation from inventory
  or visibility to policy, event, investigation and enforcement.
- Chinese cloud consoles favor persistent left navigation, dense tables,
  explicit filters, access-key management, billing, audit logs and support.

## Original TITMAS navigation

```text
Overview / Workspaces / Agents / Integrations / Gate / Approvals /
Receipts / Audit / Health / Policies / Usage / Deployments / Settings / Support
```

This navigation is an original composition around TITMAS objects. It must not
copy a vendor's naming sequence, visual tokens, component code or page layout.

## Mode communication

`MONITOR MODE — NO ACTIONS ARE BLOCKED` and `ENFORCE MODE — ACTIONS MAY BE
BLOCKED` must remain visible in the page header and event detail. Status is
expressed through text and icons as well as color.

## Data minimization

The default table stores and displays digests, references, reason codes,
timestamps, policy revision, authorization status and limitations. It does not
store or render chain of thought or raw customer payloads.
