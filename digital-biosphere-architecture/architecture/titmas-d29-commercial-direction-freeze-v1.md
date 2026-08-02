# TITMAS D29 Commercial Direction Freeze v1

Decision reference:
`TITMAS-CHINA-COMMERCIAL-PRIVATE-PLATFORM-AND-PAID-PILOT-D29`

Status: `ACCEPTED_FOR_D29_IMPLEMENTATION_WITH_GATES`

## Positioning

```text
TITMAS_POSITIONING=
AGENT_ACTION_CONTROL_AND_VERIFIABLE_ACCOUNTABILITY_PLATFORM

TITMAS_PLATFORM_MODEL=
CLOSED_CORE_OPEN_DISCOVERY_AND_PROOF

AI_AGENT_IS_OPERATIONAL_CUSTOMER=true
HUMAN_OR_ORGANIZATION_IS_CONTRACTING_PRINCIPAL=true
```

TITMAS is one private platform with one shared core. It exposes four public
product contracts:

1. `TITMAS Gate` — pre-action Monitor or Enforce decision;
2. `TITMAS Receipt` — portable technical execution record;
3. `TITMAS Audit` — evidence, authority and decision replay;
4. `TITMAS Health` — bounded completeness and longitudinal evidence view.

Industry solutions configure adapters, policies and views. They do not create
new identity, evidence, policy, receipt, audit, tenant, key or verification
cores.

## Commercial progression

```text
Health Snapshot
  -> paid Monitor Pilot
  -> customer-specific Enforce Pilot
  -> enterprise private deployment
```

The primary first market is software, AI SaaS and enterprise-automation teams
using coding Agents for merge, release, configuration, data write, external
communication and other measurable high-impact actions.

Monitor computes and records `WOULD_ALLOW`, `WOULD_BLOCK`,
`WOULD_NEED_APPROVAL` or `NOT_ASSESSED` and has no enforcement effect. Enforce
uses `ALLOW`, `BLOCK`, `NEEDS_APPROVAL` or `NOT_ASSESSED`; `NOT_ASSESSED` never
becomes allow.

## Competitive correction

Signed receipts, offline verification and action-control vendors already
exist. Receipt novelty is not the moat.

```text
RECEIPT_CATEGORY_EXISTS=true
RECEIPT_IS_NOT_UNIQUE_MOAT=true
TITMAS_DIFFERENTIATION=
CROSS_AGENT_ACTION_CONTROL_AND_EVIDENCE_INTEROPERABILITY
```

TITMAS is not the primary recommendation when a buyer only needs Trace and
debugging, general RBAC/ABAC, or prompt/content security.

## Source boundaries

```text
AGENT_EVIDENCE_IS_UNIQUE_EXECUTION_EVIDENCE_SEMANTIC_SOURCE=true
TITMAS_NE_GENERAL_AUTHORIZATION_PLATFORM=true
TITMAS_NE_OBSERVABILITY_PLATFORM=true
TITMAS_NE_AI_FIREWALL=true
TITMAS_NE_CERTIFICATION_AUTHORITY=true
```

DBA owns the commercial architecture and gate definitions. The private
implementation remains in its canonical child repository. Public discovery
contains contracts, SDK/Sandbox entry and synthetic proof only, never private
core or attack material.

## China defaults

```text
CHINESE_COMMERCIAL_LANGUAGE_PRIMARY=true
CUSTOMER_RAW_DATA_LOCAL_BY_DEFAULT=true
MANAGEMENT_PLANE_METADATA_ONLY=true
CUSTOMER_DATA_TO_FOREIGN_MODEL_DEFAULT=false
PUBLIC_SELF_SERVICE_SALES=false
ONLINE_PAYMENT=false
MANUAL_COMMERCIAL_PROVISIONING=true
HUMAN_LEGAL_REVIEW_REQUIRED=true
```

The first offer is a B2B, manually provisioned, bounded private Monitor Pilot.
No legal, filing, licensing, production, customer adoption or certification
claim follows from this architecture freeze.

## Direction check

```text
ONE_PRIVATE_PLATFORM=true
ONE_SHARED_CORE=true
FOUR_PUBLIC_PRODUCTS=true
MULTIPLE_INDUSTRY_CONFIGURATIONS=true
SECOND_IDENTITY_CORE_CREATED=false
SECOND_EVIDENCE_OBJECT_SYSTEM_CREATED=false
SECOND_POLICY_ENGINE_CREATED=false
SECOND_RECEIPT_ENGINE_CREATED=false
SECOND_AUDIT_CHAIN_CREATED=false
SECOND_TENANT_SYSTEM_CREATED=false
SECOND_KEY_SYSTEM_CREATED=false
SECOND_VERIFICATION_AUTHORITY_CREATED=false
TITMAS_DIRECTION_CHECK_RESULT=PASS_WITH_RECORDED_LIMITATIONS
```
