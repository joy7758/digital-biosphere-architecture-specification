# TITMAS Private Platform Architecture v0.1

Status: `PORTFOLIO_DIRECTION_FROZEN_BY_D28_CANDIDATE`

Decision: `TITMAS-CLOSED-CORE-OPEN-DISCOVERY-PROOF-PUBLIC-BETA-D28-V3`

Decided by: `zhangbin`

## Direction check

```text
TITMAS_PORTFOLIO_DIRECTION_CHECK_RESULT=PASS
AI_AGENT_IS_OPERATIONAL_CUSTOMER=true
HUMAN_OR_ORGANIZATION_IS_CONTRACTING_PRINCIPAL=true
ONE_PRIVATE_PLATFORM_CORE=true
MULTIPLE_PRODUCTS_ALLOWED=true
MULTIPLE_INDUSTRY_SOLUTIONS_ALLOWED=true
PUBLIC_INTERFACE_NE_PRIVATE_CORE=true
OPEN_DISCOVERY_NE_OPEN_IMPLEMENTATION=true
OPEN_PROOF_NE_OPEN_ALGORITHM=true
DEVELOPER_RECEIVES_STANDARD_INTERFACE_SANDBOX_AND_SCOPED_ACCESS=true
DEVELOPER_RECEIVES_CORE_SOURCE_BY_DEFAULT=false
INDUSTRY_SOLUTION_NE_NEW_PLATFORM=true
ADAPTER_NE_VERIFICATION_ENGINE=true
AGENT_EVIDENCE_IS_UNIQUE_EXECUTION_EVIDENCE_SEMANTIC_SOURCE=true
NEW_IDENTITY_CORE=false
NEW_EVIDENCE_CORE=false
NEW_POLICY_CORE=false
NEW_GATE_CORE=false
NEW_RECEIPT_CORE=false
NEW_AUDIT_CORE=false
NEW_TENANT_CORE=false
```

This check freezes portfolio direction. It does not make the private core
public, create a Runtime, change a database, grant a credential or authorize a
production Gateway.

## One shared private platform

TITMAS uses one private platform with eight internal capability domains. The
domains are responsibility partitions, not eight products or eight new
services.

| Domain | Responsibility | Public mapping |
|---|---|---|
| `IDENTITY_AND_TENANCY` | bounded identity, tenant and scope records | shared platform prerequisite |
| `EVIDENCE_AND_PROVENANCE` | execution evidence semantics and provenance references | Receipt and Audit inputs |
| `POLICY_AND_APPROVAL` | policy and explicit approval references | Gate inputs |
| `ACTION_GATE` | bounded pre-action decision processing | TITMAS Gate |
| `RECEIPT_AND_ISSUANCE` | bounded execution receipts and issuance | TITMAS Receipt |
| `AUDIT_AND_REPLAY` | replay and dispute reconstruction | TITMAS Audit |
| `HEALTH_AND_EVALUATION` | health signals and bounded evaluation | TITMAS Health |
| `ADAPTERS_AND_CONNECTORS` | framework and system mappings | all products, never a truth owner |

```text
ONE_SHARED_CORE=true
INDUSTRY_SPECIFIC_CORE=false
PRODUCT_SPECIFIC_DUPLICATE_CORE=false
```

## PACVP placement

`TITMAS_PRE_ACTION_CONTEXT_VALIDITY_PROFILE` is an architecture candidate
under `ACTION_GATE` and maps publicly to TITMAS Gate. It is not a fifth product.
It remains linked to `ADR-039_EXECUTION_CONTEXT_TRUST_INVALIDATION`.

```text
PACVP_PRODUCT_CLASSIFICATION=ACTION_GATE_INTERNAL_PROFILE
PACVP_IMPLEMENTED=false
PACVP_PUBLIC_CAPABILITY_CLAIM=false
PACVP_SCHEMA_PUBLICATION=false
PACVP_READY_NE_GATE_ALLOW=true
PACVP_REPLAN_NE_GATE_NEEDS_APPROVAL=true
PACVP_STOP_NE_PERMISSION_REVOCATION=true
```

A future Gate decision may consume a PACVP context result together with
Evidence, Policy, Authorization and Approval. The context result alone cannot
authorize execution.

## Current engineering focus

```text
PRIMARY_PRODUCT=TITMAS_GATE
COMPANION_PRODUCT=TITMAS_RECEIPT
PRIMARY_PROOF_SCENARIO=SOFTWARE_DELIVERY
SECONDARY_PROOF_CONFIGURATION=MEDIA_EVIDENCE
```

Audit remains a shared replay surface. Health remains a discovery and
longitudinal-metrics surface. D28 does not authorize full medical,
manufacturing, financial, aerospace, Health-scoring or Audit-console product
development.

## Permanent boundaries

- The public community repository is a discovery, proof and participation
  surface, not the core.
- `agent-evidence` remains the unique execution-evidence semantic source.
- An Adapter does not become a verification engine.
- A Product interface does not expose private algorithms.
- A Solution configuration does not create an industry-specific core.
- Evidence is not Truth; Verification is not Authorization; Receipt is not
  Certification.
