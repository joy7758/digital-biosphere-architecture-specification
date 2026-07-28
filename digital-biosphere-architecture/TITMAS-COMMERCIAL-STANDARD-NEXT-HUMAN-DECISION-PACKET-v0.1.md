---
document_id: DBA-TITMAS-COMMERCIAL-STANDARD-NEXT-HUMAN-DECISION-PACKET-0.1
title: TITMAS Commercial Standard Next Human Decision Packet v0.1
title_zh: TITMAS 商业标准下一人类决定签署包 v0.1
status: AWAITING_HUMAN_SELECTION
maturity: Development
maturity_scope: entire-document
created_at: 2026-07-28T23:20:00+08:00
primary_repository: digital-biosphere-architecture
decision_owner_ref: zhangbin
source_branch: codex/commercial-standard-next-decision-candidates
source_commit: aa4829c1720512b928a05d9b5f75da42cf59ef56
implementation_effect: none
commercial_effect: none
authority_effect: none-until-explicit-decision
---

# TITMAS Commercial Standard Next Human Decision Packet v0.1

## 1. Purpose

This packet provides one agent-readable and Human-readable signing surface for
the two independent upstream decisions currently blocking further commercial
standard work.

It does not select an option, execute a review, authorize data processing,
create a record or pass a Gate.

## 2. Frozen candidate bindings

| Decision | Candidate | Bytes | SHA-256 |
|---|---|---:|---|
| `CS-G1-REMEDIATION-D03` | exact two-session v0.3 advisory-review authorization | 4,124 | `4e9f2c39670add77732ac34a921ddddd1f5b9ba4fbd0fc0604b5953ebd1b403b` |
| `CS-G0-ACQUISITION-PREP-D01` | source/data/storage/cap contract preparation authorization | 4,534 | `8201236728259d59d18ee42b692aa02fd872727a0709e07382b3bd251afc9d40` |
| candidate validation | offline validation of both candidates | 3,199 | `c5c8c76d1f4c5e44af91b6065e9bb764bf7428136d328145864135c76d42cec3` |

The candidate files and validation report are authoritative for the exact
scope. Any byte change invalidates this packet and requires revalidation.

## 3. Decision A — CS-G1 exact advisory review

Recommended selection:

```text
CS-G1-REMEDIATION-D03=AUTHORIZE_EXACT_TWO_SESSION_QWEN3_7_MAX_REVIEW_OF_FROZEN_V0_3_PROJECTIONS_ONLY
```

If selected, the authorization:

- permits exactly two role-scoped sessions and no more than two provider
  requests;
- requires exact `qwen3.7-max`;
- uses the frozen Security and Crosswalk projections and v0.3 result Schema;
- allows zero retry, fallback, substitution, extraction or repair;
- allows no tools, external retrieval or memory retrieval;
- is one-time and expires 604,800 seconds after the Human Decision is recorded;
- is consumed when both requests have been attempted, whether successful or
  failed;
- stops after deterministic aggregation for a new Human risk/crosswalk
  adjudication.

It does not authorize Security effectiveness claims, risk acceptance,
crosswalk acceptance, Authority assignment, `CS-G1 PASS` or standard
publication.

## 4. Decision B — CS-G0 contract preparation

Recommended selection:

```text
CS-G0-ACQUISITION-PREP-D01=AUTHORIZE_SOURCE_DATA_STORAGE_CAP_CONTRACT_CANDIDATE_PREPARATION_ONLY
```

If selected, the authorization:

- permits one offline integrated contract-candidate preparation cycle;
- covers source/context, data/privacy, storage/access and cap/expiry rules;
- includes a per-batch reviewer assignment/conflict template;
- requires deterministic offline validation;
- permits zero provider requests and no data processing;
- is one-time and expires 604,800 seconds after the Human Decision is recorded;
- is consumed when the candidate validation is recorded or the authorization
  expires.

It does not select a real source, approve storage, assign live sessions,
authorize acquisition, create a problem record or pass `CS-G0`.

## 5. Recommended Human input

The decisions remain independent. The Human Owner may record one or both.

```text
decided_by_ref=zhangbin
CS-G1-REMEDIATION-D03=AUTHORIZE_EXACT_TWO_SESSION_QWEN3_7_MAX_REVIEW_OF_FROZEN_V0_3_PROJECTIONS_ONLY
CS-G0-ACQUISITION-PREP-D01=AUTHORIZE_SOURCE_DATA_STORAGE_CAP_CONTRACT_CANDIDATE_PREPARATION_ONLY
```

Silence, partial quoting, a model recommendation or a Git commit does not count
as selection.

## 6. Execution order after selection

The two tracks remain independent:

```text
CS-G1 D03 Decision
  → record exact Human Decision
  → preflight hashes, bytes, model and unconsumed budget
  → execute at most two advisory requests
  → validate and aggregate
  → stop for Human risk/crosswalk adjudication

CS-G0 PREP D01 Decision
  → record exact Human Decision
  → prepare one integrated contract candidate
  → validate offline
  → stop for a separate acquisition Decision
```

No output from one track closes the other track.

## 7. Current status

```text
PACKET_READY_FOR_HUMAN_SELECTION=true
CS_G1_REMEDIATION_D03_DECISION_STATE=NOT_DECIDED
CS_G0_ACQUISITION_PREP_D01_DECISION_STATE=NOT_DECIDED
CS_G1_REVIEW_EXECUTION_AUTHORIZED=false
CS_G0_CONTRACT_PREPARATION_AUTHORIZED=false
PROVIDER_REQUESTS_AUTHORIZED=0
PROVIDER_REQUESTS_EXECUTED=0
DATA_PROCESSING_AUTHORIZED=false
ACQUISITION_AUTHORIZED=false
CS_G0_PASS=false
CS_G1_PASS=false
STANDARD_READY=false
COMMERCIAL_READY=false
RELEASE_AUTHORIZED=false
```
