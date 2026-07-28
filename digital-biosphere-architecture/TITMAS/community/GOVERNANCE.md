# TITMAS Community Governance

Status: `PREPARED_NOT_ACTIVATED`

## Scope

Community governance manages contributions to TITMAS specifications,
conformance assets, reference implementations, adapters and documentation. It
does not operate Agent runtimes, grant DBOS permissions, change SAEE algorithms
or create Architecture Authority.

## Decision path

```text
Contribution
  → completeness and source check
  → technical/domain review
  → security/privacy review when applicable
  → maintainer recommendation
  → Human Architecture Decision when normative or high impact
  → versioned integration
```

Review is input, not a Decision. A Maintainer may merge changes only after the
applicable repository and Human gates exist. None are activated by this file.

## Conflict and appeal

1. Record the disputed text, source, version and affected scope.
2. Reviewer and contributor each provide a written rationale.
3. A reviewer not responsible for the original result performs a second review.
4. Normative, security, role or authority conflicts go to Human Owner.
5. Preserve rejected and unknown outcomes; do not rewrite history.

## Current authority state

```text
COMMUNITY_ESTABLISHED=false
MAINTAINER_ASSIGNED=false
EXTERNAL_REVIEWER_ASSIGNED=false
COMMUNITY_MEMBER_COUNT=0
PUBLIC_CONTRIBUTION_SURFACE_AUTHORIZED=false
```
