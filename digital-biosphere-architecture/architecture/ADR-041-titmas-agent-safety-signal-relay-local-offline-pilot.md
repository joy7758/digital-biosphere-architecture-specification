---
document_id: ADR-041
title: TITMAS Agent Safety Signal Relay Local Offline Pilot Authorization and Boundary
status: accepted-executed-local-only
decided_by_ref: zhangbin
decided_at: 2026-08-02
supersedes: ADR-040 future_domain_implementation_owner and P4-P10 authorization state only
release_authorized: false
deployment_authorized: false
---

# ADR-041: TITMAS Agent Safety Signal Relay 本地离线试点授权与边界

## Decision

Human Program Owner 授权在 P4–P6 硬门全部通过后创建独立私有本地实现仓库，并连续推进
P7–P10 本地离线试点。该授权已按顺序执行；不追溯修改 ADR-040 的 P0–P3 历史事实。

```text
P4_P6_AUTHORIZED=true
P7_P10_CONDITIONALLY_AUTHORIZED=true
PRIVATE_IMPLEMENTATION_REPOSITORY_AUTHORIZED=true
LOCAL_IMPLEMENTATION_AUTHORIZED=true
LOCAL_INTEGRATION_AUTHORIZED=true
LOCAL_COMMITS_AUTHORIZED=true

PUBLIC_PRODUCTION_DEPLOYMENT_AUTHORIZED=false
PUBLIC_SIGNAL_PUBLICATION_AUTHORIZED=false
REMOTE_CONTROL_AUTHORIZED=false
AUTO_REMEDIATION_AUTHORIZED=false
PRODUCTION_KEY_USE_AUTHORIZED=false
REAL_PRIVATE_TRACE_USE_AUTHORIZED=false
PUBLIC_CORE_SOURCE_EXPORT_AUTHORIZED=false
```

P4–P6 gate 经两个独立语言 evaluator、20 个合成向量和生命周期攻击负例通过后，建立：

```text
implementation_repository=/Users/zhangbin/GitHub/titmas-agent-safety-signal-relay
implementation_repository_visibility=LOCAL_PRIVATE_NO_REMOTE
implementation_status=LOCAL_OFFLINE_PILOT
architecture_owner=DBA
domain_implementation_owner=TITMAS_AGENT_SAFETY_SIGNAL_RELAY_PRIVATE_LOCAL_REPOSITORY
evidence_authority=EXISTING_AGENT_EVIDENCE_AND_DBOS_DEPENDENCIES
recipient_trust_authority=LOCAL_RECIPIENT_POLICY
```

## Gate result

- deterministic three-value matcher: Python/Ruby explanations agree;
- DSSE Ed25519 uses synthetic local keys only; signing time is inside signed payload;
- correction, revocation, tamper, replay, rollback, freeze and omitted-correction detection pass;
- `agent-evidence` is verify-only and remains evidence authority;
- HTTP, CLI, MCP and direct calls share one non-authoritative Relay service;
- two external heterogeneous reviewers both conditionally recommend no more than a local offline pilot.

## Blocked integrations

The Sandbox Gateway canonical source was resolved, but the inspected checkout was stale/dirty and the current
Gateway boundary forbids Agent calls. Direct modification is therefore `BLOCKED_CANONICAL_SOURCE`.
`redcrag.cn` source/build/release/live parity is `FAIL`; no site change or deployment occurred.

## Invariants

```text
SIGNAL_RECEIVED_NE_ACTION_AUTHORIZED=true
APPLICABILITY_NE_CONFIRMED_IMPACT=true
PUBLISHER_ASSURANCE_NE_GLOBAL_TRUST=true
EVIDENCE_REFERENCE_NE_TRUTH=true
CORRECTION_NE_HISTORY_DELETION=true
SPECIFICATION_NE_IMPLEMENTATION=true
LOCAL_PILOT_NE_PUBLIC_PRODUCTION=true
```

Any remote repository creation, push, merge, release, public signal, deployment, production key, real private
trace, Gateway scope change, or public production recommendation needs a new explicit Human decision.
