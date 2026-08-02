---
document_id: TITMAS-ASSR-P4-P10-LOCAL-PILOT-ACCEPTANCE-0.1
status: pass-with-blocked-integrations-and-limitations
decision_ref: ADR-041
observed_at: 2026-08-02
---

# P4–P10 本地离线试点验收

| Gate | Evidence | Result |
|---|---|---|
| P4 matcher | Python/Ruby, 13 frozen vectors, three outcomes, explanations | `PASS` |
| P5 lifecycle | synthetic DSSE/Ed25519, correction/revocation and attack vectors | `PASS` |
| P6 case | 20 synthetic fixtures, no real private trace | `PASS` |
| P7 interfaces | six schemas, 9 HTTP paths, 8 CLI commands, 7 MCP tools, direct call | `PASS_LOCAL` |
| agent-evidence | existing CLI `verify-bundle`, synthetic receipt, no duplicate store | `PASS_VERIFY_ONLY` |
| Gateway | canonical resolved; stale/dirty checkout and scope boundary | `BLOCKED_CANONICAL_SOURCE` |
| P8 loop | A/B/Unknown, feedback, v2 correction, revocation, old-client detection | `PASS` |
| P9 public entry | source/build/release/live parity | `FAIL_NO_DEPLOY_LOCAL_DERIVED_ONLY` |
| P10 heterogeneous model review | `qwen3.7-max`, `glm-5.2`; not independent adopter evidence | `LOCAL_OFFLINE_PILOT` |

Current verified local test count is 29 unique unittest cases; `make verify-all`, the independent Ruby evaluator,
MCP stdio smoke and full demo all pass. This evidence is owned by the private local implementation repository;
DBA records only the bounded status projection.

```text
IMPLEMENTATION_STATUS=LOCAL_OFFLINE_PILOT
PUBLIC_PRODUCTION_RECOMMENDED=false
PUBLIC_SIGNAL_PUBLISHED=false
PUBLIC_PRODUCTION_DEPLOYED=false
REMOTE_CONTROL_ENABLED=false
AUTO_REMEDIATION_ENABLED=false
INDEPENDENT_EXTERNAL_ADOPTER_RECOMMENDATION=NOT_AVAILABLE
INDEPENDENT_FORMAL_SECURITY_AUDIT=NOT_PERFORMED
```
