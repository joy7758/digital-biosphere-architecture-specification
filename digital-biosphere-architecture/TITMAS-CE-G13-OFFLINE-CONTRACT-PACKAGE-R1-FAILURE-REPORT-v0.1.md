---
document_id: DBA-TITMAS-CE-G13-OFFLINE-CONTRACT-PACKAGE-R1-FAILURE-REPORT-0.1
title: TITMAS CE-G13 Offline Contract Package R1 Failure Report v0.1
title_zh: TITMAS CE-G13 离线契约包 R1 失败报告 v0.1
version: 0.1.0
status: fail-closed-validation-evidence
maturity: Development
owner_ref: zhangbin
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G13 Offline Contract Package R1 Failure Report v0.1

## Result

```text
R1_RESULT=FAIL_CLOSED_SCHEMA_REFERENCE_RESOLUTION_ATTEMPTED_REMOTE_FETCH
OFFLINE_VALIDATION_PASS=false
REMOTE_FETCH_ATTEMPT_OBSERVED=true
REMOTE_FETCH_SUCCESS=false
REMOTE_RESPONSE_OBSERVED=PROXY_503_SERVICE_UNAVAILABLE
MODEL_REQUESTS=0
CREDENTIAL_READS=0
TECHNICAL_REUSE_RUNS=0
RUNTIME_STARTS=0
AGENT_INSTANCES=0
ENTITY_INSTANCES=0
PERMISSION_GRANTS=0
EVIDENCE_TRUTH_OBJECTS=0
PACKAGE_COMMITTED=false
PACKAGE_PUSHED=false
RETRY_AUTHORIZED=false
```

R1 is immutable failure evidence. It is not a package pass and cannot be reinterpreted as an
offline result.

## Observed failure

The five role schemas use:

```text
$ref=./session-response.base.schema.v0.1.json#/$defs/common
```

Their canonical `$id` base resolves that reference to:

```text
https://titmas.cn/schemas/session-response.base.schema.v0.1.json
```

The base schema instead declared:

```text
https://titmas.cn/schemas/ce-g13-session-response.base.schema.v0.1.json
```

The R1 validator registered the declared `$id`, so the resolved URI missed the local store.
The deprecated resolver then attempted a remote GET. The proxy returned 503 and validation stopped.

## Boundary interpretation

- The remote attempt violates the R1 zero-network contract even though no public content was
  successfully retrieved.
- The 28-file package remains an uncommitted candidate.
- No CE-G13 session, public snapshot capture, technical reuse run or customer workflow occurred.
- The failure does not authorize a source edit, retry, commit or push.
- A new Recommendation and independent Decision are required.

