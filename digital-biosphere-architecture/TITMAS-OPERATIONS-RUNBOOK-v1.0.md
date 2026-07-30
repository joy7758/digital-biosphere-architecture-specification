# TITMAS Operations Runbook v1.0

## Current state

```text
COMMERCIAL_SERVICE_DEPLOYED=false
SANDBOX_PREVIEW_SERVICE_ACTIVE=true
POSTGRESQL_INSTALLED=false
RUNBOOK_VALIDATED_BY_DRILL=false
```

This runbook is an execution contract for the future commercial candidate. It
does not describe a currently deployed `/api/v1`.

## Baseline environment

Observed on `2026-07-30T19:04:07+08:00`:

```text
host=existing-baidu-server
os=Ubuntu 24.04
cpu=2
memory=7.7 GiB
root_disk_free=83 GiB
sandbox_service=titmas-sandbox-preview.service active
sandbox_release=33a10e37d9582f240c518a0b65fb59f12dd3527c
postgresql=not installed
ubuntu_postgresql_candidate=16
api_v1_public_status=not deployed
```

## Immutable release procedure

1. require an exact merged commit;
2. build in a clean checkout;
3. run tests, scans, SBOM and package verification;
4. produce a manifest with file hashes and dependency lock;
5. copy into `/srv/titmas-commercial/releases/<commit>/`;
6. create an isolated virtual environment;
7. perform migration dry-run and backup;
8. validate configuration without exposing secret values;
9. start a loopback canary on a non-public port;
10. run health, readiness, tenant-isolation and receipt tests;
11. update the Nginx `/api/v1` route only;
12. verify public machine endpoints from independent clients;
13. retain the previous release and rollback instructions.

```text
ZERO_DIRECT_SERVER_SOURCE_EDITING=true
ROLLBACK_TARGET_REQUIRED=true
SANDBOX_ROUTE_MUST_REMAIN_HEALTHY=true
```

## Configuration and secret locations

- service unit: `/etc/systemd/system/titmas-commercial-api.service`;
- environment: root-owned file outside the release;
- receipt private key: separate root-owned file, mode `0600`;
- PostgreSQL credentials: root/service-readable secret, not Git;
- public key and key ID: generated public-safe release artifact.

No command may print credential, database password or private key.

## Database migration

Before migration:

1. verify supported PostgreSQL major/minor;
2. create encrypted backup;
3. validate backup integrity;
4. run migration in a disposable database;
5. record migration hash and expected schema version.

Production-candidate migration runs under a dedicated role. Application
credentials must not own the schema.

## Health model

- liveness: process can serve a minimal response;
- readiness: database, credential registry, signer and migration version are
  usable;
- dependency health: structured internal diagnostic, not public secret detail.

The public status returns only bounded aggregate maturity and health.

## Monitoring

Collect tenant-safe metrics:

- request and outcome counts;
- latency;
- authentication, scope, quota and rate-limit failures;
- database and receipt failures;
- usage-ledger and billing-ledger lag;
- backup age and disk usage.

Never use raw tenant, Agent or credential identifiers as high-cardinality
public labels.

## Alert routing

| severity | example | immediate action |
|---|---|---|
| `SEV-1` | cross-tenant access, key exposure, receipt forgery | stop affected service, revoke, preserve evidence, Human notify |
| `SEV-2` | sustained unavailability, database loss risk | fail closed, rollback or restore |
| `SEV-3` | degraded latency, ledger lag | limit traffic and investigate |
| `SEV-4` | non-urgent warning | schedule correction |

## Rollback

Application rollback:

1. remove or disable only `/api/v1` Nginx route;
2. switch release symlink to the last verified commit;
3. restart commercial service;
4. verify Sandbox and public site unaffected.

Database rollback does not run destructive down migrations automatically.
Restore into a separate database, verify, then switch after a Human safety
check if data loss is possible.

## Backup and restore

Backup scope:

- PostgreSQL metadata and ledgers;
- configuration with secrets separately encrypted;
- public-key metadata;
- audit and release manifests.

Plaintext tokens are never backed up.

Restore evidence must record measured RPO and RTO. Design targets cannot be
reported as measured results.

## Synthetic drills required

1. application process failure;
2. database unavailable;
3. malformed credential registry;
4. receipt signer unavailable;
5. backup restore into an isolated database.

All drills use synthetic tenants only until customer-production-data
authorization exists.

## Stop conditions

Stop and rollback on secret exposure, cross-tenant access, receipt forgery,
billing double count, unexpected raw payload persistence, unrecoverable backup,
unbounded cost or any need for an unauthorized DNS/certificate change.
