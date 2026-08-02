---
document_id: TITMAS-ASSR-P4-P6-CONFORMANCE-0.1
title: TITMAS Agent Safety Signal Relay P4-P6 Conformance Profile v0.1
status: frozen-local-pilot-profile
decision_ref: ADR-041
normative_for_local_pilot: true
public_standard: false
---

# P4–P6 符合性配置 v0.1

## P4 deterministic applicability

Inputs bind exact `schema_version`, `matcher_version`, signal/profile/context digests and evaluation time.
Predicates are typed `EQ`, `NEQ`, `IN`, or `EXISTS`, grouped as affected `all` + `any` and explicit exclusions.
Missing, conflicted, expired, unconfirmed-time, digest-mismatched or invalid inputs fail closed to `UNKNOWN`.

Only these outcomes are legal:

```text
POSSIBLY_AFFECTED
NOT_AFFECTED
UNKNOWN
```

Every result preserves sorted per-predicate explanations. Applicability never contains local test outcomes,
execution permission or automatic action. Python and independently implemented Ruby evaluators must produce
byte-equivalent normalized result objects for all frozen vectors.

## P5 signed lifecycle

The local pilot directly reuses DSSE framing and OpenSSL Ed25519. It does not define a cryptographic algorithm,
PKI, TUF implementation or global trust root. Only synthetic keys are accepted. The trusted signing time is
inside the signed payload; mutable envelope time cannot change key policy.

Signal objects and lifecycle envelopes are immutable versioned files. A global monotonic change cursor and a
per-signal sequence/predecessor chain support `PUBLISHED`, `UPDATED`, `CORRECTED`, `EXPIRED`, and `REVOKED`.
Terminal signals cannot transition. A client keeps high-water sequence, previous digest and seen digests.

Required rejection/detection classes:

```text
TAMPER_DETECTED
REPLAY_DETECTED
ROLLBACK_DETECTED
FREEZE_DETECTED
OMITTED_CORRECTION_DETECTED
REVOCATION_DETECTED
KEY_POLICY_REJECTED
UNKNOWN
```

Signature validity proves neither content truth nor publisher global trust. TUF/SCITT compatibility remains a
future standards profile, not an implemented claim.

## P6 frozen synthetic case

The first case is Fuzzy Resolution Hijacking. Names, aliases, historical names and fuzzy descriptions only
produce candidates. Stable identity binds and verifiable proof establishes local trust; ambiguity, conflict or
unverifiable proof forbids execution.

The frozen corpus contains 13 matcher vectors and 7 lifecycle vectors. It includes typo recovery, ambiguous
similar names, Unicode homograph, historical alias, conflicting stable identity, missing/invalid/revoked proof,
explicit exclusion, insufficient profile, correction, revocation, expiry, replay/rollback/freeze and key policy.
All data and keys are synthetic; real private traces are forbidden.

## Acceptance

```text
P4_COMPLETE=true
P5_COMPLETE=true
P6_COMPLETE=true
P4_P6_GATE=PASS
DUAL_EVALUATOR_AGREEMENT=true
LLM_IN_DECISION_PATH=false
PRODUCTION_KEY_USED=false
REAL_PRIVATE_DATA_USED=false
```
