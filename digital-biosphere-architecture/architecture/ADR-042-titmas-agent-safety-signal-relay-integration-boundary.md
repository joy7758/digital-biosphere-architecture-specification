---
document_id: ADR-042
title: TITMAS Agent Safety Signal Relay Integration Boundary
status: accepted-architecture-only-not-implemented
decided_by_ref: zhangbin-authorized-P14
decided_at: 2026-08-02
gateway_reference_commit: a367c69b4d30a6e501dcaf4e52c65153e8a21f3a
implementation_authorized: false
gateway_code_change_authorized: false
---

# ADR-042: TITMAS 智能体安全信号中继集成边界

## Context and current facts

P14 only decides architecture. A clean detached worktree of the canonical
TITMAS Sandbox Gateway reference commit was reviewed read-only. Its charter is
stateless, schema-only preflight and explicitly forbids Agent calls,
request-selected fetching, databases, request persistence and authority
elevation. The current checkout is not the current remote head, so this
decision binds the reviewed reference only and does not claim current Gateway
implementation compatibility.

Relay already provides bounded local Direct Call, MCP, CLI and loopback HTTP
adapters. Relay owns signal lifecycle and deterministic applicability; it owns
neither identity, evidence truth, action authorization nor recipient policy.

```text
GATEWAY_ARCHITECTURE_REVIEW=PASS
GATEWAY_REFERENCE_COMMIT=a367c69b4d30a6e501dcaf4e52c65153e8a21f3a
GATEWAY_REFERENCE_IS_CURRENT_REMOTE_HEAD=false
CANONICAL_TITMAS_GATEWAY_INTEGRATION=NOT_IMPLEMENTED
```

## Options and 15-dimension evaluation

| Dimension | IN_GATEWAY | SIDECAR | DIRECT_AGENT_SERVICE |
|---|---|---|---|
| Authority boundary | mixes signal domain into Gateway | Relay remains owner; Gateway is thin adapter | clear, but creates a separate client trust surface |
| Failure coupling | highest | bounded to the optional route | low for Gateway, higher for each client |
| Latency | lowest hop count | one local hop | client/deployment dependent |
| Offline operation | possible but coupled | strong over loopback or Unix socket | strong for local MCP/CLI |
| Privacy | Gateway process sees full profile | minimum projection can cross boundary | client may send profile to a second service |
| Lifecycle independence | coupled to Gateway release | independent Relay updates | independent |
| Blast radius | largest | isolated process and route | new service exposure risk |
| Recursion risk | highest if preflight calls itself | fixed one-way call only | low if clients avoid cycles |
| Availability dependency | existing Gateway depends on Relay | only safety-preflight route depends on sidecar | each client manages another dependency |
| Observability | mixed domain logs | separate bounded receipts | fragmented client logs |
| Evidence ownership | easy to duplicate | agent-evidence stays verify-only authority | stays separate |
| Authorization ambiguity | highest | explicit no-authorization response | requires every client to preserve boundary |
| Rollback/revocation propagation | Gateway caching risk | Relay cursor/high-water remains canonical | direct but client-dependent |
| Deployment complexity | release-coupled | moderate, separately rollbackable | creates another exposed service surface |
| Gateway charter compatibility | incompatible | conditionally compatible after a separate charter amendment | does not implement Gateway integration |

## Decision

```text
GATEWAY_BOUNDARY_DECISION=SIDECAR
RELAY_ROLE=ONLY_SIGNAL_DOMAIN_IMPLEMENTATION
GATEWAY_FUTURE_ROLE=THIN_AUTHENTICATED_MINIMIZING_ADAPTER
DIRECT_LOCAL_AGENT_ACCESS_REMAINS_AVAILABLE=true
DIRECT_PUBLIC_AGENT_ENDPOINT_AUTHORIZED=false
```

If a future implementation is separately authorized, Relay runs as an
independent local sidecar. Gateway may use its existing
`POST /sandbox/v0.1/preflight` surface only after an explicit Gateway charter
amendment defines a typed safety-signal preflight profile. Gateway validates
its own identity/scope, projects minimum fields, makes one fixed-destination
local call to Relay `/v1/preflight`, and returns the Relay result without
reimplementing or interpreting matcher or lifecycle rules.

`IN_GATEWAY` is rejected because it violates the reviewed stateless/schema-only
charter and raises duplication and authority ambiguity. `DIRECT_AGENT_SERVICE`
is retained for local agent-first access, but rejected as the preferred Gateway
topology because it does not itself integrate Gateway and would require a new
exposed authentication and audit surface.

## Future minimum contract

The adapter may forward only stable subject/target references, bounded action
class, context/profile digests, a locally policy-approved minimum exposure
projection, evidence receipt references, disclosure ceiling and recipient
high-water state. Complete private profiles, evidence contents, traces,
credentials and free-form commands are forbidden.

The response must preserve candidate IDs/versions, lifecycle state/cursor,
applicability and predicate reason codes, recommended tests, non-executable
guidance and evidence verification limitations, plus:

```text
authorization_decision=NOT_PROVIDED
automatic_action_allowed=false
SIGNAL_RECEIVED_NE_ACTION_AUTHORIZED=true
```

Gateway may keep a bounded call receipt containing request/response digests,
component versions, result code and timing. It may not persist request bodies,
profiles, advice text or evidence content.

## Failure, privacy and update behavior

- invalid Gateway authentication/scope rejects before Relay and does not reveal signal existence;
- Relay unavailable, timeout, version mismatch, lifecycle gap, freeze or untrusted time returns `UNKNOWN`/unavailable, never an old cached safety conclusion;
- `POSSIBLY_AFFECTED` never becomes Gateway `DENY` and `NOT_AFFECTED` never becomes Gateway `ALLOW`;
- Relay remains the only correction/expiry/revocation owner; Gateway does not cache signal state;
- every response carries signal version, cursor and freshness needed by recipients to reject rollback;
- `PRIVATE_EVIDENCE` and `LOCAL_ONLY` never cross the adapter; restricted validation requires explicit local scope and policy;
- recipients retain the final local trust and action decision.

## Non-goals and authorization

No Gateway code, route, deployment, Token, key registry, website or public
signal is changed by this ADR. It creates no implementation, release or
production authorization.

```text
CANONICAL_GATEWAY_CODE_CHANGED=false
SIDECAR_IMPLEMENTED=false
GATEWAY_INTEGRATION_TESTED=false
PUBLIC_ENDPOINT_CREATED=false
IMPLEMENTATION_AUTHORIZATION_STATUS=NOT_AUTHORIZED
HUMAN_AUTHORIZATION_REQUIRED_FOR_IMPLEMENTATION=true
```
