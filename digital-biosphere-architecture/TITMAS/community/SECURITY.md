# TITMAS Security Policy

Status: `PROCESS_DEFINED_TRANSPORT_ACTIVE_LIMITED_PREVIEW`

## Supported surface

Only the current Development branch candidate is available for review. There is
no supported production release, SLA, certification or security guarantee.

## Reporting

Do not publish suspected vulnerabilities, secrets, personal data or exploit
details in an Issue. GitHub Private Vulnerability Reporting was enabled and
verified through the repository API on 2026-07-29. Use **Report a
vulnerability** under the repository Security / Advisories area. No private
mailbox is invented, and no response SLA is claimed. `zhangbin` is the
temporary, revocable process owner through 2026-09-30T23:59:59+08:00.

Current state:

```text
SECURITY_PROCESS_DEFINED=true
SECURITY_PROCESS_OWNER_ASSIGNED=true
SECURITY_DISCLOSURE_PATH_ACTIVATED=true
SECURITY_TRANSPORT_VERIFIED=true
SECURITY_RESPONSE_TEAM_ASSIGNED=false
PUBLIC_LAUNCH_BLOCKER_SECURITY_TRANSPORT=false
```

Do not send external reports automatically. The private reporting path is a
transport, not a security audit, certification or guarantee.

GitHub Issue and PR templates are installed only on the Activation PR branch.
They remain inactive until merge and never replace the private reporting path.

## Review requirements

Schema, validator, adapter and reference changes must assess:

- untrusted input and fail-closed behavior;
- path traversal, unsafe deserialization and command execution;
- secret, PII and customer-data exclusion;
- dependency and supply-chain changes;
- denial-of-service and size limits;
- semantic elevation from Observation, Evidence or Verification;
- rollback and historical record preservation.

Security review does not grant Authorization or Certification.
