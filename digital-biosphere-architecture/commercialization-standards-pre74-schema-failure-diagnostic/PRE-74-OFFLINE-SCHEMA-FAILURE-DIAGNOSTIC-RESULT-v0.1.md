# PRE-74 Offline Schema-Failure Diagnostic Result v0.1

## Outcome

```text
PRE74_OFFLINE_DIAGNOSTIC=PASS
TRANSMISSION_GAP_PROVEN=true
EXACT_SCHEMA_FAILURE_CAUSE_PROVEN=false
SANITIZED_CAPTURE_DETAILS_PASS=12/12
FORBIDDEN_FIELD_AND_BOUNDARY_NEGATIVES_REJECTED=10/10
LIVE_RETRY_AUTHORIZED=false
STANDARD_READY=false
```

PRE-74 proved that the complete frozen PRE-73 response Schema was not serialized
into either provider review request. Both sessions received only a partial
natural-language description of the contract. The same gaps were present in all
three inspected coverage groups.

This is a bounded transmission diagnosis. It is consistent with the two PRE-73
Schema failures, but it does not prove the exact rejected path from either live
response and does not prove a unique causal explanation.

## Contract transmission findings

| Coverage group | Exact keys transmitted | Shared gap |
|---|---:|---|
| Top-level response object | `6/10` | `verdict`, `summary`, `question_assessments`, `cross_cutting_findings` absent |
| Question assessment object | `1/7` | six required assessment fields absent |
| Explicit non-claims object | `6/8` | `conformance_pass`, `release_authorized` absent |

The frozen response Schema file itself and its structural markers were not
serialized into the system or user messages.

## Sanitized failure-detail design

The Development candidate admits only:

- validation phase;
- error class;
- bounded instance and Schema paths;
- allowlisted validator name;
- offending-value type and length.

It forbids raw error messages, offending values, assistant content, provider
envelopes, request payloads, source packages, credential values and authorization
headers.

Twelve synthetic mutations each failed the frozen response Schema and produced a
sanitized detail that passed the dedicated detail Schema. Ten forbidden-field and
boundary negatives were rejected. Phase accounting preserves a successful direct
JSON parse when a later response-Schema check fails.

## Execution accounting

| Operation | Count |
|---|---:|
| Network requests | `0` |
| Live model requests | `0` |
| Credential value reads | `0` |
| Raw provider response reads | `0` |
| Raw error messages or offending values persisted | `0` |
| Target repository writes | `0` |
| DBOS writes | `0` |
| SAEE writes | `0` |
| Request revisions adopted | `0` |
| Response Schema changes | `0` |
| Live retries | `0` |

## Governance result

The capture contract remains
`DEVELOPMENT_CANDIDATE_NOT_ADOPTED`. PRE-74 does not authorize a revised request,
new provider request, live retry, formal Human Security Review claim, Provider
support claim, conformance claim, Standard Ready state or release.

The next bounded action is to prepare, not execute, a PRE-75 response-contract
transmission remediation and bounded-rerun Recommendation. That Recommendation
must preserve the separate Decision gate.

## Evidence

- [Execution receipt](pre74-execution-receipt.v0.1.json)
- [Offline result](pre74-offline-diagnostic-result.v0.1.json)
- [Transmission map](pre74-response-contract-transmission-map.v0.1.json)
- [Capture contract](pre74-sanitized-failure-detail-capture-contract.v0.1.json)
- [Synthetic fixtures](pre74-synthetic-failure-detail-fixtures.v0.1.json)
