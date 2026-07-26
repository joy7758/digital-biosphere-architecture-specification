# Frozen Delta Source Pack — Public First-party Problem Report Method v0.2

## Review status

```text
DECISION_REFERENCE=CS-D02-PRE-07
PREDECESSOR_DECISION_REFERENCE=CS-D02-PRE-06
METHOD_MATURITY=Development
METHOD_V0_2_CANDIDATE_DEFINED=true
METHOD_ADOPTED=false
DESK_RESEARCH_EXECUTION_AUTHORIZED=false
PUBLIC_SOURCE_SEARCH_AUTHORIZED=false
PUBLIC_SOURCE_COLLECTION_AUTHORIZED=false
PUBLIC_SOURCE_RECORD_COUNTING_AUTHORIZED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
```

This is a delta review. No public issue, incident, organization, person, customer, private record or
source page has been searched, collected, copied, extracted, scored or counted.

## PRE-06 retained result

The v0.1 review completed two sessions:

- Qianfan Method Reviewer: `RETURN_FOR_REVISION`;
- DeepSeek Claim/Privacy Reviewer: `ACCEPT_WITH_CHANGES`;
- both retained `KEEP_MAX_2`;
- boundary safety failures: 0;
- applied corrections in v0.1: 0.

Required revisions:

1. complex organization independence and deduplication;
2. documented accountable source role verification;
3. multiple and conflicting report handling;
4. temporary excerpt and metadata retention/deletion;
5. correction/removal/withdrawal lifecycle;
6. candidate counting cap requires method adoption and per-record Human Decision.

The v0.1 files and dissent remain unchanged.

## v0.2 qualification delta

The required qualification fields now explicitly include:

- `accountable_role_verification`;
- `relationship_classification`;
- `source_context_key`;
- `report_lineage`;
- `retention_disposition`.

Missing fields remain `UNKNOWN` and make the record `PARTIAL` or `INVALID`. Reviewers and models may
not infer missing problem, workaround, impact, priority, role or organization relationship.

## Accountable source role verification

Required evidence:

1. publisher-controlled role reference;
2. source-to-system responsibility binding;
3. observation time and reviewer reference.

Reviewer judgment alone is insufficient. Unverifiable role is `PARTIAL`; contradictory role signal
is `CONFLICTED`; role verification never proves TITMAS responsibility.

## Organization relationship classification

Every candidate uses one:

- `SAME_CONTROL_OR_ORGANIZATION`;
- `PARENT_CHILD_CONTROL`;
- `CONSORTIUM_OR_SHARED_GOVERNANCE`;
- `RELATED_BUT_OPERATIONALLY_DISTINCT`;
- `INDEPENDENT_ORGANIZATION`;
- `UNKNOWN_RELATIONSHIP`.

Parent/child and consortium members are not automatically independent. Related organizations may
only be proposed as distinct when separate operational responsibility, separate problem instance
and separate control path are documented. Unknown relationship is `PARTIAL`.

## Context key and deduplication

The context key contains:

```text
controlling organization or governance
+ governed project/system/workflow
+ incident/event/problem root
+ declared time window
```

- same context key: one canonical record;
- updates use lineage and do not duplicate counting;
- mirrors, forks, reposts, quotation chains and multiple model reviews do not increase independence;
- same organization reports about one event/root merge into one context;
- possibly distinct incidents may be retained separately but do not increase organization
  independence before Human Decision;
- author-related sources disclose conflict and do not count independently by default.

## Multiple and conflicting reports

- no silent overwrite;
- canonical record retains lineage references;
- conflict status is `CONFLICTED`;
- conflict immediately suspends counting;
- source versions, conflict summary, reviewer inputs and resolution decision are retained;
- only Human Decision Owner may merge, supersede, separate or invalidate;
- no selection of the TITMAS-favorable version before resolution.

## Retention and deletion

- no full page/article/issue discussion or raw provider envelope storage;
- quote/excerpt maximum: 25 English words or equivalent;
- temporary excerpt retention maximum: 7 days after extraction review;
- then temporary excerpt is deleted;
- long-term minimum metadata: canonical reference, title, publisher, verified role, times, hash,
  context key, field paraphrases, status, review/decision references and limitations;
- direct identifiers, contacts, credentials, private logs and customer Evidence are prohibited;
- deletion keeps a minimal tombstone, hash and disposition;
- this policy creates no Store, crawler, database or collection authority.

## Correction, removal and withdrawal

```text
ACTIVE
  -> CORRECTION_PENDING
  -> CORRECTED | WITHDRAWN | SOURCE_REMOVED_UNVERIFIABLE
```

Correction, removal, hash drift or role change immediately suspends counting. Corrected versions
link predecessors. Silent history deletion is forbidden. Removed/unverifiable sources cannot stay
`VALID`. Recounting requires new Method/Claim-Privacy input and Human Decision.

## Candidate counting policy

```text
COUNTING_POLICY_STATUS=CANDIDATE_NOT_ADOPTED
PUBLIC_SOURCE_VALID_RECORDS_MAX_TOWARD_CS_G0=2
PUBLIC_SOURCE_RECORD_CAN_SATISFY_CONTINUE_REVIEW_INTEREST=false
DIRECT_OR_GOVERNED_RESPONSIBILITY_CONTEXT_STILL_REQUIRED=true
METHOD_ADOPTION_REQUIRED_BEFORE_COUNTING=true
PER_RECORD_HUMAN_COUNTING_DECISION_REQUIRED=true
AUTOMATIC_COUNTING_ALLOWED=false
```

The cap is a candidate only. Delta review cannot adopt it. Method adoption and each record counting
decision remain separate Human Decisions.

## Permanent claim boundaries

```text
PUBLICATION_NE_CONSENT_TO_TITMAS=true
PUBLIC_REPORT_NE_CUSTOMER=true
PUBLIC_REPORT_NE_ADOPTION=true
SOURCE_PROBLEM_NE_VEAP_FIT=true
PUBLIC_SOURCE_REVIEW_NE_MARKET_VALIDATION=true
MODEL_REVIEW_NE_INDEPENDENT_ORGANIZATION=true
METHOD_CANDIDATE_NE_EXECUTION_AUTHORIZATION=true
DELTA_REVIEW_NE_METHOD_ADOPTION=true
METHOD_REVIEW_NE_CS_G0=true
```

## Maximum result

```text
METHOD_V0_2_DELTA_REVIEW_COMPLETE=true
METHOD_ADOPTION_REVIEW_READY=true

METHOD_ADOPTED=false
DESK_RESEARCH_EXECUTION_AUTHORIZED=false
PUBLIC_SOURCE_SEARCH_AUTHORIZED=false
PUBLIC_SOURCE_COLLECTION_AUTHORIZED=false
PUBLIC_SOURCE_RECORD_COUNTING_AUTHORIZED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
```
