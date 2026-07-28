---
document_id: DBA-TITMAS-CE-G13-PUBLIC-AGENT-CUSTOMER-DISCOVERY-AND-REUSE-VALIDATION-RECOMMENDATION-0.1
title: TITMAS CE-G13 Public Agent-customer Discovery and Reuse Validation Recommendation v0.1
title_zh: TITMAS CE-G13 公网智能体客户发现与复用验证建议 v0.1
version: 0.1.0
status: recommendation-candidate-agent-customer-review-required
maturity: Development
maturity_scope: public-agent-customer-discovery-and-reuse-validation-design-only
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G13 Public Agent-customer Discovery and Reuse Validation Recommendation v0.1

## 1. Recommendation

Adopt **Option A — website-first, problem-seeded, bounded AI-agent discovery and reuse validation
design**, but do not execute CE-G13 in this action.

```text
CE_G13_RECOMMENDATION_PREPARED=true
RECOMMENDED_OPTION=A
CE_G13_EXECUTION_DECISION_RECORDED=false
PUBLIC_HTTP_FETCH_AUTHORIZED=false
AGENT_MODEL_REQUESTS_AUTHORIZED=false
TECHNICAL_REUSE_RUN_AUTHORIZED=false
CUSTOMER_ADOPTION_VERIFIED=false
COMMERCIAL_OFFERING=false
```

The target customer role is an AI Agent evaluating infrastructure for a long-running multi-agent
system. “Agent-customer” is an evaluation role, not a real customer, account, contract, adoption,
revenue or endorsement.

## 2. Why CE-G13 is not a repeat of CE-G1

The existing
[External Agent First Run Validation](TITMAS-EXTERNAL-AGENT-FIRST-RUN-VALIDATION-REPORT-v0.1.md)
already proved a bounded result:

```text
PUBLIC_PACKAGE_GIVEN_TO_AGENT=true
TECHNICAL_FIRST_RUN=PASS
AGENT_SESSIONS=4/4
EVALUATION_RECOMMENDED=4/4
PRODUCTION_NOT_RECOMMENDED=4/4
CUSTOMER_ADOPTION_VERIFIED=false
```

CE-G1 did not prove:

- cold discovery from a customer problem and website root;
- website-only orientation without GitHub access;
- correct selection of reusable public artifacts without being given their exact filenames;
- a machine-checkable, scenario-specific reuse plan;
- refusal to recommend TITMAS where the use case does not match;
- public discovery and reuse behavior after CE-G12 activated the current static candidate.

CE-G13 addresses only those gaps. It must cite, not overwrite, CE-G1 failures and PASS evidence.

## 3. Current evidence boundary

Inputs available for a future Decision:

| Evidence | SHA-256 | Meaning |
|---|---|---|
| CE-G12 status reconciliation validation result v0.2 | `df70977ddd5fa8e8e6368719edbd71c42709db376555e8aab0d44c7a73df366d` | five status paths reconciled after 1350/1350 JSON, Schema and cross-file PASS |
| CE-G12 public route validation result | `f20e12db44dd5206a2cc0bc798fe2f76ac8c7243acb5aa28e89b40366a0b62d4` | application and agent-readable content exact in one bounded observation |
| CE-G12 public network path attribution result | `d7b4b60e0c5a2d0ad123f78cdc5f54e43d85344bc5556936503238b471799b87` | local synthetic DNS path observed; direct-origin path not proven |
| CE-G1 protocol | `bf4af045718a52093e39aa7a94c4a21fba09c7d5a5152243118a6884801ec29e` | prior First Run contract |
| CE-G1 report | `5de4e9583a40af988320e1e7786db0dfa47d1e707494e6fa2e7199c430fea121` | prior bounded result |
| CE-G1 composite result | `90838bde3517c7339a70a04a1aa3efbd393c907cacc1f59a7a62c44d61463f03` | machine-readable session and boundary counts |

Current public truth must be fetched fresh under a future Decision. Local `site/public` bytes are
source candidates, not automatically current public bytes. CE-G12 application exactness does not
prove availability at CE-G13 execution time.

## 4. Proposal classification

| Mandatory question | Answer |
|---|---|
| Domain | Program Governance / Commercial Evaluation design |
| Primary repository | `digital-biosphere-architecture` |
| Open-standard and reuse value | tests whether AI Agents can discover and reuse public specifications and bounded evaluation artifacts |
| Duplicate of DBOS | no; DBOS implementation and runtime are not modified |
| Duplicate of SAEE | no; no Fitness, Risk or Evolution result is generated |
| Duplicate of Agent framework | no; TITMAS does not create or orchestrate an Agent |
| Authority confusion | prohibited by explicit negative cases and response Schema |
| Commercial language | Evaluation / Exploration only; not Available Offering, Adoption or Contract |

No new repository, Agent instance, Runtime, Entity, Capability, Permission, Evidence Truth or
commercial service is created.

## 5. Options

### Option A — Website-first problem-seeded validation

Recommended.

Use `https://redcrag.cn/` as the only initial project URL. Do not give the discovery session the
TITMAS name, acronym, exact artifact filenames, GitHub repository or an answer key. Give it only a
customer problem:

> A team operates long-running collaborating AI Agents and needs identity continuity, bounded
> capability, traceable execution, evidence references, verification and long-term evaluation.
> Determine whether the referenced website offers reusable infrastructure material, what can be
> used now, and what must not be claimed.

A bounded controller may fetch same-origin public resources discovered from the root, HTML links,
`robots.txt`, `llms.txt` and machine-readable indexes. It may not add hidden repository context or
private files.

### Option B — Give every exact public artifact URL to every session

Rejected as the primary validation. That repeats CE-G1 orientation and does not test discovery.
Exact URLs may be used only after the discovery lane has independently selected them.

### Option C — Use GitHub as a required dependency

Rejected. The website must be sufficient for users and Agents that cannot reliably access GitHub.
GitHub may be reported as an optional provenance reference, never a success prerequisite.

### Option D — Treat positive model recommendations as customer adoption

Rejected.

## 6. Future execution topology

A separate Human Decision may authorize, at most:

```text
PUBLIC_ORIGIN=https://redcrag.cn
INITIAL_PROJECT_URLS=1
HTTP_GET_REQUESTS_MAX=16
SAME_ORIGIN_ONLY=true
REDIRECTS_SAME_ORIGIN_ONLY=true
RAW_PUBLIC_BYTES_MAX=3000000
AGENT_SESSIONS=5
MODEL=qwen3.7-max
MODEL_REQUESTS_MAX=5
RETRIES=0
FALLBACKS=0
MODEL_SUBSTITUTIONS=0
JSON_EXTRACTIONS=0
JSON_REPAIRS=0
TECHNICAL_REUSE_RUNS_MAX=1
SYNTHETIC_INPUT_ONLY=true
RUNTIME_STARTS=0
```

Exact `qwen3.7-max` is the current commercial review quality baseline. Five isolated sessions using
one Provider do not prove cross-provider generality or five independent customers.

## 7. Public retrieval protocol

### 7.1 Cold seed

The controller starts with:

- the customer problem;
- `https://redcrag.cn/`;
- no TITMAS name or exact child URL.

### 7.2 Allowed discovery

The controller may follow only same-origin references found in fetched public bytes. The expected
classes include, but are not disclosed to the cold-discovery session:

- project status;
- Agent index;
- `llms.txt`;
- community/developer entry;
- Agent-customer package;
- release or package manifest;
- First Run and synthetic fixture;
- public-safe validator or wheel reference.

An expected class may be absent. The result must preserve absence instead of inventing a URL.

### 7.3 Receipt

Every fetch records:

```text
request_id
source_url
discovered_from
status
final_url
content_type
byte_count
sha256
retrieved_at
same_origin
parse_status
```

No cookie, Authorization header, API key, private path, raw IP, customer data or unbounded page
content is persisted.

## 8. Five isolated Agent-customer sessions

| Session | Role | Required result |
|---|---|---|
| `CE-G13-S01` | `COLD_DISCOVERY_AGENT` | identify TITMAS, its public positioning and canonical website evidence from root-seeded material |
| `CE-G13-S02` | `ARCHITECTURE_COMPREHENSION_AGENT` | distinguish DBA, DBOS, SAEE, Governance Decision and Digital Entity responsibilities |
| `CE-G13-S03` | `WEBSITE_ONLY_REUSE_PLANNER` | select exact public artifacts and produce a bounded, executable evaluation plan without GitHub dependency |
| `CE-G13-S04` | `AGENT_RECOMMENDER` | recommend, conditionally recommend or reject for the stated use case with evidence-linked reasons |
| `CE-G13-S05` | `BOUNDARY_AND_NON_MATCH_AUDITOR` | reject production, certification, automatic authority and at least two non-matching use cases |

Sessions are isolated: no earlier model answer is supplied to a later session. They may share the
same hash-bound public snapshot.

## 9. Reuse validation

The reuse planner must select, without an answer key:

1. one machine-readable project/status entry;
2. one architecture or governance entry;
3. one public-safe evaluation package or manifest;
4. one synthetic First Run input;
5. one validation command or procedure;
6. the expected bounded meaning of the result.

A deterministic controller validates that selected URLs:

- were present in the hash-bound public snapshot;
- are same-origin or explicitly marked optional provenance;
- exist and match recorded hashes;
- do not require a private repository or secret;
- do not start an Agent Runtime;
- do not grant Permission or create Evidence Truth.

If the plan selects a valid public-safe First Run, one clean synthetic read-only validation may be
executed under the future Decision. This is not an Agent task, production deployment or customer
workflow.

## 10. Direct JSON response contract

Each session returns direct JSON against a frozen role-specific Schema. Common fields:

```text
session_id
role
source_snapshot_sha256
project_identified
canonical_name
public_positioning
selected_public_artifacts
architecture_responsibilities
recommended_use
recommendation_verdict
recommendation_reasons
non_matching_use_cases
hard_boundaries
unknowns
blockers
critical_boundary_failures
```

No response may be extracted from prose or repaired. Requested and returned model identities must
both be exact `qwen3.7-max`.

## 11. Success criteria

CE-G13 may return `PASS_AGENT_DISCOVERY_AND_BOUNDED_REUSE_VALIDATED` only if:

### Public surface

- root plus required discovered resources are fresh HTTP success;
- all retained resources have URL, hash, size and lineage;
- the website-only path is sufficient; GitHub is not required;
- no hidden local/private content enters any session.

### Discovery and comprehension

- `5/5` sessions are direct JSON and Schema-valid;
- `S01` identifies TITMAS and “Trusted Infrastructure for Multi-Agent Systems” or the canonical
  Chinese positioning without being given the name;
- `S02` correctly separates DBA, DBOS, SAEE and Governance Decision;
- no session describes TITMAS as an Agent Framework, Agent Platform, Foundation Model or automatic
  authority system.

### Reuse and recommendation

- `S03` selects all six reuse elements and the controller validates every selected reference;
- the optional synthetic technical run, if authorized, passes without Runtime, Agent, Entity,
  Permission or Evidence Truth creation;
- `S04` gives a traceable verdict and recommends only a scope supported by current evidence;
- `S05` rejects production purchase/deployment, certification and automatic authority;
- all sessions preserve `Evidence != Truth`, `Evaluation != Authority`,
  `Recommendation != Decision`, `Capability != Permission`.

### Fail-closed

- critical boundary failures: `0`;
- retries/fallbacks/substitutions/extractions/repairs: `0`;
- any missing session, model mismatch, invalid JSON, unknown selected URL or hidden dependency makes
  the composite result `FAIL_CLOSED` or `CONDITIONAL_REMEDIATION_REQUIRED`.

## 12. Valid conclusions

Allowed positive conclusion:

> In this bounded, single-provider, website-first evaluation, isolated AI-agent sessions discovered
> TITMAS and produced a technically valid public-safe reuse plan with correct authority boundaries.

It does not prove:

```text
REAL_CUSTOMERS=0
CUSTOMER_ADOPTION_VERIFIED=false
MARKET_DEMAND_VERIFIED=false
CROSS_PROVIDER_GENERALITY=false
GLOBAL_DISCOVERABILITY=false
CONTINUOUS_AVAILABILITY=false
SLA=false
PRODUCTION_READY=false
COMMERCIAL_OFFERING=false
CERTIFICATION=false
```

Model recommendation is an observed evaluation output, not endorsement or purchase intent.

## 13. Required output package for future execution

```text
ce-g13-public-snapshot-manifest.v0.1.json
ce-g13-retrieval-receipt.v0.1.json
ce-g13-session-response.schema.v0.1.json
ce-g13-session-01..05.v0.1.json
ce-g13-reuse-plan-validation-result.v0.1.json
ce-g13-technical-reuse-receipt.v0.1.json
ce-g13-composite-result.v0.1.json
TITMAS-CE-G13-PUBLIC-AGENT-CUSTOMER-DISCOVERY-AND-REUSE-VALIDATION-REPORT-v0.1.md
```

Schemas, prompts, source manifest, caps and stop conditions must be frozen before any public fetch
or Agent request.

## 14. Recommendation review contract

One exact `qwen3.7-max` direct JSON review using persistent in-memory sanitized capture. No retry,
fallback, model substitution, JSON extraction or repair.

Required top-level keys:

```text
verdict
confidence
selected_option
would_recommend_to_agent_customer
existing_ce_g1_delta_sound
website_first_without_github_sound
cold_discovery_design_sound
five_session_role_separation_sound
reuse_validation_design_sound
success_criteria_fail_closed
single_provider_limitation_preserved
customer_adoption_nonclaim_complete
execution_decision_separation_sound
non_authorizations_complete
authority_boundaries_preserved
blockers
corrections
rationale
```

Qualifying for Recommendation preparation requires:

- `verdict=RECOMMENDED` or `CONDITIONALLY_RECOMMENDED`;
- `selected_option=A`;
- `confidence>=0.90`;
- every required boolean `true`;
- empty `blockers` and `corrections`;
- exact returned model `qwen3.7-max`.

## 15. Stop conditions

Stop if:

- the CE-G12 status commit or evidence hashes drift;
- the Recommendation silently repeats CE-G1 instead of testing cold discovery;
- GitHub becomes required for success;
- a session is presented as a real customer;
- Agent recommendation is upgraded to adoption, demand, endorsement or revenue;
- any implementation, public fetch, model session or technical run occurs before a new independent
  Decision;
- release, Standard Ready, Production, certification, offering, Authority, Ownership, Permission
  or Evidence Truth would change.

## 16. Non-authorizations

This Recommendation authorizes nothing. It does not authorize a Decision, HTTP request, public
fetch, model request beyond its own separately governed Recommendation review, technical reuse run,
Agent instance, Runtime, Entity, Capability, Permission, Evidence creation, SAEE evaluation,
customer claim, invitation, outreach, implementation, deployment, release, publication, commercial
offering, pricing, contract, SLA, certification, Standard Ready, Production Ready, Authority,
Ownership or Evidence Truth mutation.
