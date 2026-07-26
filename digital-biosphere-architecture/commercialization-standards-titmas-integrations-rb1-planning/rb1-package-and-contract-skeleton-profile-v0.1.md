# TITMAS Integrations RB1 Package and Contract Skeleton Profile v0.1

## Status

```text
MATURITY=Development
STATUS=PLANNING_CANDIDATE_NOT_ADOPTED_NOT_IMPLEMENTED
PACKAGE_CREATED=false
SOURCE_CREATED=false
TESTS_CREATED=false
PUBLIC_API_ADOPTED=false
PROVIDER_SUPPORTED=false
CONFORMANCE_EXECUTED=false
RUNTIME_CREATED=false
RELEASE_AUTHORIZED=false
```

This profile is a DBA planning artifact under `CS-D02-PRE-43`. It is not an
implementation declaration, package, API, Runtime, provider integration or
release.

## Problem

RB1 addresses one bounded problem:

> Attribute the first failure of an AI model/provider request to a P0-P9 phase
> while persisting only sanitized metadata.

PRE-28 observed timeouts before an HTTP response. PRE-29 showed that DNS, TCP and
TLS were reachable during a later diagnostic, but did not resolve the timeout
phase or prove provider/model availability. PRE-30 defined the Development phase
contract. This evidence supports implementation planning only; it does not prove
external demand, customer adoption or market readiness.

## Candidate package surface

The following values are review candidates, not adopted facts:

| Field | Preferred candidate | Status |
|---|---|---|
| distribution | `titmas-integrations` | `NOT_ADOPTED` |
| import namespace | `titmas_integrations` | `NOT_ADOPTED` |
| core module | `titmas_integrations.instrumentation` | `NOT_ADOPTED` |
| provider namespace | `titmas_integrations.providers` | `RESERVED_NOT_CREATED` |
| minimum Python | `>=3.11` | `NOT_ADOPTED` |

Candidate non-network contract types:

- `PhaseId`;
- `PhaseStatus`;
- `FailureCategory`;
- `PhaseEvent`;
- `PhaseTrace`.

They describe values only. RB1 must not send requests, load credentials, import
provider SDKs, call DBOS/SAEE, create Evidence or evaluate fitness.

## Phase contract

`PhaseEvent` must represent the adopted PRE-30 fields:

```text
phase_id
status
started_at_monotonic_ref
elapsed_ms
timeout_budget_ms
bytes_in
bytes_out
failure_category
predecessor_phase
executed
```

P0-P9 order, first-failure retention and dependent-phase closure are inherited
from the exact adopted Development contract. Retry, fallback or repair may not
rewrite the first failure.

## Data minimization

Candidate types may preserve phase timing, byte counts, sanitized failure
category, observed HTTP status, observed returned model identifier and one-way
digests.

They must not persist credentials, authorization headers, raw request/response
bodies, prompts, review content, hidden reasoning, packet captures, resolver
private configuration or local sensitive network identifiers.

## Authority and truth boundary

```text
PHASE_EVENT=OBSERVATION_METADATA
OBSERVATION_NE_EVIDENCE=true
EVIDENCE_NE_TRUTH=true
SCHEMA_PASS_NE_PROVIDER_CORRECTNESS=true
SCHEMA_PASS_NE_CONFORMANCE=true
INSTRUMENTATION_NE_PERMISSION=true
EVALUATION_NE_AUTHORITY=true
```

DBOS and SAEE remain separate. This package candidate neither governs existence
nor evaluates evolution.

## Dependency boundary

- provider-neutral core must not require provider SDKs;
- core must not depend on a DBOS Runtime;
- core must not invoke SAEE execution or evaluation;
- provider bindings are outside RB1 and require a later exact Decision;
- OpenTelemetry/OTLP/SemConv may be mapping references only; compatibility and
  support are not claimed.

## Agent-readable recommendation boundary

An agent may recommend this planning profile when a developer wants to review a
provider-neutral, secret-minimizing phase-attribution contract before
implementation.

An agent must not recommend it as:

- an installable package;
- a runtime adapter;
- a supported provider integration;
- an executed conformance suite;
- production-ready software;
- a source of Evidence, Truth, Permission or Certification.

## Commands

```text
INSTALL=NOT_AVAILABLE
IMPORT=NOT_AVAILABLE
RUN=NOT_AVAILABLE
TEST=NOT_AVAILABLE
CONFORMANCE=NOT_AVAILABLE
ROLLBACK=NOT_AVAILABLE
```

## Next gate

Before any RB1 implementation Decision, PRE-44 must execute a bounded Agent
Customer Review over this exact profile, its machine representation and the
negative-boundary catalog. Recommendation is advisory and cannot authorize
implementation.
