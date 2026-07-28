# TITMAS Security Policy

Status: `PREPARED_NOT_ACTIVATED`

## Supported surface

Only the current Development branch candidate is available for review. There is
no supported production release, SLA, certification or security guarantee.

## Reporting

Do not publish suspected vulnerabilities, secrets, personal data or exploit
details in an Issue. A future public surface should enable GitHub private
vulnerability reporting or another Human Owner approved private route.

Current state:

```text
SECURITY_PROCESS_DEFINED=true
SECURITY_DISCLOSURE_PATH_ACTIVATED=false
SECURITY_RESPONSE_TEAM_ASSIGNED=false
```

Until a route is activated, preserve the minimum local finding and request a
Human Owner decision. Do not send external reports automatically.

GitHub Issue and PR templates link to this policy and explicitly prohibit
secrets, PII and public vulnerability details. That link is guidance, not an
activated receiving channel.

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
