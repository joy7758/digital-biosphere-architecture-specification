---
document_id: ADR-043
title: TITMAS Agent Safety Signal Relay P4-P6 Security Semantics Amendment
status: accepted-local-pilot-security-amendment
amends: TITMAS-ASSR-P4-P6-CONFORMANCE-0.1
reason: P13 adversarial findings
decided_at: 2026-08-02
public_standard: false
---

# ADR-043: P4–P6 安全语义修订

## Defect

P13 reproduced two unsafe outcomes in the frozen P4 matcher: Python equality
could conflate boolean `true` and integer `1`, and a required `FALSE` combined
with another missing/conflicted required condition could return
`NOT_AFFECTED`. Strings were also trimmed before comparison, making whitespace
changes invisible. These are specification defects, not new business features.

## Normative amendment

For the local-pilot security profile:

1. security identifiers, predicate IDs, predicate paths, operators, schema
   versions and digests use explicit ASCII syntax;
2. string values must already be Unicode NFC; implementations reject rather
   than silently normalize;
3. string comparison is exact and does not trim whitespace;
4. `EQ`, `NEQ` and `IN` compare only equal JSON types; type mismatch is
   `UNKNOWN/TYPE_MISMATCH`, including `NEQ`;
5. `EXISTS.expected`, when present, must be a JSON boolean;
6. duplicate predicate IDs are invalid;
7. a complete, explicit exclusion remains sufficient for `NOT_AFFECTED`;
   otherwise any missing, conflicted or type-unknown required condition takes
   precedence over partial affected-condition failure and yields `UNKNOWN`;
8. Python and Ruby evaluators must emit byte-equivalent normalized results.

## Compatibility and evidence

This amendment is intentionally fail-safer but not byte-compatible for hostile
or ambiguous inputs that were previously trimmed or coerced. Existing 13
positive/negative frozen vectors retain their expected outcomes. P13 adds
negative cases for boolean/integer confusion, `NEQ` type mismatch, leading or
trailing whitespace, duplicate predicates, confusable security identifiers and
false-plus-missing/conflict propagation. The full P4–P6 and P7–P13 suite must
pass before the amended profile is cited.

The original P0–P6 documents and commits remain historical facts; this ADR does
not delete or rewrite them.

```text
SPECIFICATION_DEFECT_RECORDED=true
SILENT_BASELINE_REWRITE=false
BACKWARD_COMPATIBLE_FOR_VALID_FROZEN_VECTORS=true
BACKWARD_COMPATIBLE_FOR_HOSTILE_AMBIGUOUS_INPUTS=false
NEW_SIGNAL_DOMAIN_CREATED=false
NEW_INTERFACE_CREATED=false
```
