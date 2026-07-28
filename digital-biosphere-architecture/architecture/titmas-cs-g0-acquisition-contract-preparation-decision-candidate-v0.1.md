---
document_id: DBA-TITMAS-CS-G0-ACQUISITION-CONTRACT-PREPARATION-DECISION-CANDIDATE-0.1
title: TITMAS CS-G0 Acquisition Contract Preparation Decision Candidate v0.1
title_zh: TITMAS CS-G0 采集契约准备决定候选 v0.1
status: HUMAN_DECISION_REQUIRED_OPTION_NOT_SELECTED
maturity: Development
maturity_scope: entire-document
created_at: 2026-07-28T22:45:00+08:00
primary_repository: digital-biosphere-architecture
decision_id: CS-G0-ACQUISITION-PREP-D01
decision_owner_ref: zhangbin
implementation_effect: none
commercial_effect: none
authority_effect: none-until-explicit-decision
---

# TITMAS CS-G0 Acquisition Contract Preparation Decision Candidate v0.1

## 1. Decision required

`CS-G0-REVIEWER-D01` accepted the bounded role-scoped reviewer-process
contract, but the current readiness matrix remains:

```text
PASS=5
PARTIAL=2
BLOCKED=3
ACQUISITION_READY=false
ACQUISITION_AUTHORIZED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
```

The next decision is whether to prepare one integrated source/data/storage/cap
contract candidate. Preparation must occur before any source selection, data
processing, provider request or record creation.

## 2. Option A — recommended

Authorize preparation only of:

1. a source and operational-context eligibility profile;
2. a data classification, minimization and prohibited-content profile;
3. a storage, access, retention, deletion and incident-handling profile;
4. a batch cap, provider budget, timebox, expiry and revocation profile;
5. a per-batch reviewer assignment and conflict declaration template;
6. a machine-readable candidate plus deterministic offline validation.

The candidate must define requirements without selecting a real source,
creating a store, processing data, assigning live sessions or sending provider
requests.

Recommended exact selection:

```text
CS-G0-ACQUISITION-PREP-D01=AUTHORIZE_SOURCE_DATA_STORAGE_CAP_CONTRACT_CANDIDATE_PREPARATION_ONLY
```

## 3. Required candidate boundaries

### Source and context

- require exact source identity, owner/controller reference, applicable terms,
  context-independence status and observed time;
- preserve `UNKNOWN`, `CONFLICTED`, `NOT_ASSESSED` and rejected sources;
- prohibit synthetic, model-authored or project-controlled material from being
  called independent external evidence.

### Data and privacy

- reference-first and minimum-necessary fields;
- explicit purpose, recipient, legal/ethical basis and data-class declaration;
- credentials, secrets, direct personal identifiers and regulated raw content
  prohibited by default;
- no inference that Evidence completeness proves Truth or scientific validity.

### Storage and access

- exact store owner, access roles, encryption expectation, retention period,
  deletion/hold rule and incident path;
- failed or rejected records remain immutable;
- no unspecified external or model memory storage.

### Cap and expiry

- maximum candidate records, provider sessions, requests, request bytes, cost
  budget and wall-clock window;
- explicit authorization expiry and revocation behavior;
- no retry, fallback, substitution or cross-role fill unless separately
  decided.

## 4. Other options

### Option B — source-only preparation

Not recommended. Source eligibility without privacy, storage and cap controls
cannot make a future acquisition decision safe or countable.

### Option C — immediately authorize acquisition

Not recommended and outside the current evidence. The integrated contract does
not yet exist, no real source is approved and no storage path is authorized.

### Option D — defer or reject

Preserve the current `5 PASS / 2 PARTIAL / 3 BLOCKED` state.

## 5. Agent-customer recommendation gate

```text
AGENT_RECOMMENDATION=RECOMMENDED
RECOMMENDED_AS=OFFLINE_INTEGRATED_CONTRACT_PREPARATION_ONLY
NOT_RECOMMENDED_AS=DATA_ACQUISITION_STORAGE_ACTIVATION_OR_RECORD_CREATION
WHY_RECOMMENDED=THREE_REMAINING_BLOCKED_DIMENSIONS_REQUIRE_ONE_CONSISTENT_FAIL_CLOSED_CONTRACT
NEW_PROVIDER_REQUESTS_EXECUTED=0
HUMAN_DECISION_REQUIRED=true
```

The integrated candidate improves agent readability because one future
acquisition agent can determine source eligibility, permitted fields, storage
rules, budget and stop conditions from a single versioned contract.

## 6. Effects that remain false under every option

```text
REAL_SOURCE_SELECTED=false
SOURCE_CHANNEL_APPROVED=false
STORAGE_CREATED=false
STORAGE_APPROVED=false
DATA_PROCESSING_AUTHORIZED=false
EXTERNAL_OUTREACH_AUTHORIZED=false
LIVE_REVIEWER_SESSION_ASSIGNED=false
PROVIDER_REQUESTS_AUTHORIZED=0
ACQUISITION_AUTHORIZED=false
RECORD_CREATED=false
RECORD_VALIDATED=false
RECORD_COUNTED=false
CS_G0_PASS=false
IMPLEMENTATION_AUTHORIZED=false
STANDARD_READY=false
COMMERCIAL_READY=false
RELEASE_AUTHORIZED=false
```

No option is selected by this candidate.
