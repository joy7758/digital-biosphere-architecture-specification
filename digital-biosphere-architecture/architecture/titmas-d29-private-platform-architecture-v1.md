# TITMAS D29 Private Platform Architecture v1

Status: `ARCHITECTURE_FROZEN_IMPLEMENTATION_INCOMPLETE`

Commercial entry is governed by `TITMAS-COMMERCIAL-C01`. The entry sequence is
`TITMAS Observer -> Health Snapshot -> Monitor -> separately authorized
Enforce -> Receipt/Audit -> optional private deployment`. Observer is an entry
layer over this platform, not a new service, product, Trace backend or Evidence
owner.

## Repository decision

The existing private repository `joy7758/titmas-sandbox-gateway` is the
canonical composition candidate. Its current commercial surface already owns
the bounded API entry, tenant-bound credentials, quota, Receipt metadata,
verification and audit metadata. Creating `joy7758/titmas-private-platform`
would duplicate composition and tenant/key surfaces.

```text
PRIVATE_PLATFORM_REPOSITORY=joy7758/titmas-sandbox-gateway
OBSERVED_MAIN_HEAD=efdfc84462628abdfbfe111f61253f76569edec0
REUSE_EXISTING_REPOSITORY=true
CREATE_NEW_PRIVATE_PLATFORM_REPOSITORY=false
DUPLICATION_AUDIT=PASS_REUSE_REQUIRED
```

This observation is point-in-time and must be refreshed before merge or
deployment.

## Plane model

```text
Customer Agent / Application
        |
        v
TITMAS Observer Entry Layer (no authority / no enforcement)
        |
        v
Customer Data Plane Adapter
        |
        v
TITMAS Gate API
        |
        +--> Policy + Authorization References
        +--> Monitor Shadow Decision
        +--> Enforce Decision after customer-specific authorization
        |
        v
Customer Action Boundary
        |
        v
Receipt -> Independent Verification -> Audit / Health
```

### Customer Data Plane

- customer action and raw data;
- customer raw Trace;
- local adapter, optional local policy cache and customer KMS/HSM;
- optional local Receipt storage;
- customer-side enforcement and rollback.

### TITMAS Private Platform Plane

- tenant and workspace metadata;
- Agent registration reference;
- scoped-key verifier and lifecycle;
- policy and authorization references;
- Gate decision, Receipt, verification and audit metadata;
- usage, retention, support and console views.

### Management Plane

- manual customer/workspace provisioning;
- plan and quota configuration;
- deployment record and version;
- support, security notice and commercial status.

The first version keeps management offline or Human-operated. A normal Agent
cannot create credentials, change plan/quota, alter owner maps or deploy.

## Canonical implementation status

| Capability | Current evidence at observed head | D29 status |
|---|---|---|
| separate `/sandbox/v0.1` and `/api/v1` realms | repository layout and AGENTS contract | `PRESENT` |
| tenant-bound credential and scope | commercial service/store/tests | `PRESENT_REVERIFY_REQUIRED` |
| PostgreSQL RLS | migrations and integration tests | `PRESENT_REVERIFY_REQUIRED` |
| quota and idempotency | store and regression tests | `PRESENT_REVERIFY_REQUIRED` |
| signed Receipt and verify endpoint | receipt/service/API tests | `PRESENT_REVERIFY_REQUIRED` |
| audit metadata | database audit insertions | `PARTIAL` |
| formal Workspace object | no canonical network/control-plane surface observed | `MISSING` |
| Monitor shadow vocabulary and no-effect proof | C-01 contract defines the target; runtime proof not observed | `C01_CONTRACT_DEFINED_IMPLEMENTATION_MISSING` |
| bounded Enforce pre-side-effect contract | preflight exists but D29 policy/authorization binding not complete | `PARTIAL` |
| offline Audit Bundle export | not observed | `MISSING` |
| Health Snapshot | not observed as D29 product view | `MISSING` |
| data deletion workflow | not observed | `MISSING` |
| commercial console | not observed | `MISSING` |

The missing items above are implementation gaps. C-01 defines their target
contracts but does not upgrade them to `PRESENT`.

## First-value data and permission boundary

```text
SYNTHETIC_FIRST_VALUE_CUSTOMER_DATA_REQUIRED=false
SYNTHETIC_FIRST_VALUE_PRODUCTION_PERMISSION_REQUIRED=false
MONITOR_FIRST_VALUE_PRODUCTION_WRITE_PERMISSION_REQUIRED=false
MONITOR_FIRST_VALUE_AUTOMATIC_ENFORCEMENT=false
RAW_TRACE_UPLOAD_DEFAULT=false
METADATA_ONLY_ENTRY_AVAILABLE=true
CUSTOMER_EXIT_PATH_REQUIRED=true
KEY_REVOCATION_PATH_REQUIRED=true
DELETION_REQUEST_PATH_REQUIRED=true
```

The Human console and Agent entry are derived views over these contracts. They
must not bypass identity binding, workspace isolation, scope, reason codes,
high-risk confirmation, Receipt/Audit limitations or separate Human Enforce
authorization.

`PRESENT` does not mean production ready. Current security/runbook records
retain a failed historical D04/CR-01 ledger-integrity condition and prohibit
reopening or rewriting it.

## Deployment profiles

| Profile | D29 target |
|---|---|
| `LOCAL_DEVELOPER_SANDBOX` | retain current public-safe/stateless route |
| `CHINA_MANAGED_PRIVATE_PILOT` | Pilot architecture and packaging; no automatic deployment |
| `CUSTOMER_VPC` | reference deployment and customer-data-local adapter |
| `CUSTOMER_ON_PREMISES` | reproducible guide and demo-level packaging |
| `AIR_GAPPED_FUTURE_PROFILE` | architecture reservation only |

The existing Baidu Cloud host is the primary China infrastructure candidate
because it is an already-owned resource. Vendor selection does not prove legal
or production readiness and does not authorize deployment.

## Non-negotiable invariants

```text
CUSTOMER_RAW_DATA_STAYS_IN_CUSTOMER_ENVIRONMENT=true
MANAGEMENT_PLANE_RECEIVES_METADATA_ONLY=true
CHAIN_OF_THOUGHT_CAPTURED=false
NORMAL_AGENT_CAN_CREATE_CREDENTIAL=false
NORMAL_AGENT_CAN_CHANGE_PLAN=false
NORMAL_AGENT_CAN_CHANGE_QUOTA=false
UNKNOWN_TO_ALLOW=false
OBSERVER_IS_PRODUCT=false
PUBLIC_PRODUCT_COUNT=4
MONITOR_AUTHORITY_EFFECT=NONE
MONITOR_ENFORCEMENT_EFFECT=NONE
ENFORCE_REQUIRES_SEPARATE_HUMAN_AUTHORIZATION=true
P0_10_REOPENED=false
D04_REOPENED=false
PUBLIC_CORE_SOURCE=false
```
