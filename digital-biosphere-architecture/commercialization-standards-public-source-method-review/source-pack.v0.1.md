# Frozen Source Pack — Public First-party Problem Report Method Review v0.1

## Review status

```text
DECISION_REFERENCE=CS-D02-PRE-06
METHOD_MATURITY=Development
METHOD_ADOPTED=false
DESK_RESEARCH_EXECUTION_AUTHORIZED=false
PUBLIC_SOURCE_COLLECTION_AUTHORIZED=false
PUBLIC_SOURCE_RECORD_COUNTING_AUTHORIZED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
```

This is a method-design review. No public issue, incident, organization, person, customer or private
record has been searched, collected, extracted, scored or counted.

## Predecessor facts

- Agent-native Problem Signal Track A passed under `CS-D02-PRE-05`.
- Model sessions are not independent organizations, customers or market evidence.
- VEAP Problem Validation Protocol requires attributable recent examples, current workarounds,
  measurable cost/risk, priority, independence and accountable context.
- Direct outreach, participant enrollment and data collection remain unauthorized.
- Existing Option B permits design of a public first-party report method only after an independent
  method amendment and Claim/Privacy review.

## Candidate source qualification

An eligible public first-party problem report must be published by a party with direct maintenance,
operational, governance or incident-investigation responsibility for the described project, system,
workflow or event.

Candidate eligible classes:

- official Maintainer issue;
- official incident report;
- official project postmortem;
- accountable organization technical report.

Candidate ineligible classes:

- secondary news or articles;
- promotional case studies;
- search snippets;
- model-generated or synthetic content;
- unattributed, leaked, private or access-controlled material.

Public URL, GitHub issue or byline alone is insufficient. The accountable source role must be
verifiable.

## Required fields

Future `VALID` candidates require explicit source support for:

1. canonical public source reference;
2. publisher reference;
3. accountable source role;
4. publication and observation times;
5. a recent concrete example;
6. problem area;
7. current workaround;
8. workaround limitations;
9. measurable cost or risk;
10. explicit priority basis;
11. existing alternatives;
12. source integrity and version/hash;
13. independence basis;
14. reviewer references;
15. limitations.

Reviewers and models may not infer missing fields. Missing material remains `UNKNOWN` and makes the
record `PARTIAL` or `INVALID`.

## Mapping and claim boundaries

```text
PUBLICATION_NE_CONSENT_TO_TITMAS=true
PUBLIC_REPORT_NE_CUSTOMER=true
PUBLIC_REPORT_NE_ADOPTION=true
SOURCE_PROBLEM_NE_VEAP_FIT=true
PUBLIC_SOURCE_RECORD_CAN_SATISFY_CONTINUE_REVIEW_INTEREST=false
```

- `observer_ref` maps to the first-party publisher or attributable source role.
- `human_accountability_ref` is the source role, not responsibility for TITMAS.
- `consent_reference` is `NOT_APPLICABLE_PUBLIC_SOURCE_USE_BASIS`.
- contract and private-demo review interest remain `NOT_ASKED`.
- commercial commitment and customer adoption remain false.

## Independence and deduplication

- same organization, project or incident: at most one context by default;
- mirrors, forks, reposts and quotation chains do not increase independence;
- multiple models reviewing one source do not increase independence;
- vendor retelling of a customer problem is not a customer first-party report;
- author-related sources disclose conflict and do not count as independent;
- unverifiable relationships remain `PARTIAL`.

## Privacy, copyright and source use

- public access only; no login, paywall or access-control bypass;
- public-safe paraphrase only;
- at most 25 quoted words or an equivalent short phrase per source;
- no full-content storage;
- no direct identifiers, contact details, credentials, private logs or customer Evidence;
- public publication is not research participation, contact consent, customer testimony or
  trademark permission;
- removal, correction, retention and incident paths are required before execution.

## Candidate counting policy

```text
PUBLIC_SOURCE_VALID_RECORDS_MAX_TOWARD_CS_G0=2
PUBLIC_SOURCE_RECORD_CAN_SATISFY_CONTINUE_REVIEW_INTEREST=false
DIRECT_OR_GOVERNED_RESPONSIBILITY_CONTEXT_STILL_REQUIRED=true
AUTOMATIC_COUNTING_ALLOWED=false
```

The cap is intended to prevent desk research from replacing direct or governed responsibility
contexts. It is a review candidate, not an adopted rule.

## Review lifecycle

```text
DISCOVERED
  -> FIRST_PARTY_ROLE_CHECK
  -> SOURCE_AND_VERSION_CHECK
  -> FIELD_EXTRACTION_WITH_UNKNOWN_PRESERVATION
  -> PRIVACY_COPYRIGHT_CLAIM_CHECK
  -> INDEPENDENCE_AND_DEDUPLICATION_CHECK
  -> METHOD_REVIEW
  -> VALID | PARTIAL | INVALID | WITHDRAWN
  -> COUNTING_DECISION | NOT_COUNTED
```

The record creator cannot self-validate. Method and Claim/Privacy inputs are required, followed by an
explicit Human Decision Owner counting decision. Agent review remains advisory.

## Review questions

1. Does the source definition reliably separate first-party responsibility from secondary reporting?
2. Are the required fields strong enough to prevent inferred problem, impact and priority?
3. Are independence and deduplication rules sufficient?
4. Are privacy, copyright, removal and claim boundaries sufficient for a future public-source method?
5. Is a maximum of two public-source records toward the five-record CS-G0 threshold justified,
   too permissive or too restrictive?
6. What exact corrections are required before a human method-adoption decision?

## Maximum result of this review

```text
METHOD_AGENT_REVIEW_COMPLETE=true
METHOD_REVIEW_READY=true

METHOD_ADOPTED=false
DESK_RESEARCH_EXECUTION_AUTHORIZED=false
PUBLIC_SOURCE_COLLECTION_AUTHORIZED=false
PUBLIC_SOURCE_RECORD_COUNTING_AUTHORIZED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
```
