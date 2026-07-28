---
document_id: DBA-TITMAS-CE-G13-OFFLINE-EXECUTION-CONTRACT-PACKAGE-RECOMMENDATION-0.1
title: TITMAS CE-G13 Offline Execution Contract Package Recommendation v0.1
title_zh: TITMAS CE-G13 离线执行合同包建议 v0.1
version: 0.1.0
status: recommendation-candidate-agent-review-required
maturity: Development
maturity_scope: offline-contract-design-only
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G13 Offline Execution Contract Package Recommendation v0.1

## 1. Recommendation

Select **Option A — create one complete, hash-bound, offline-only CE-G13 execution contract package
under an independent Decision**.

```text
RECOMMENDED_OPTION=A
OFFLINE_CONTRACT_PACKAGE_CREATED=false
CE_G13_EXECUTION_DECISION_RECORDED=false
PUBLIC_FETCH_AUTHORIZED=false
AGENT_SESSION_EXECUTION_AUTHORIZED=false
TECHNICAL_REUSE_RUN_AUTHORIZED=false
```

The package closes the ten missing inputs recorded in
[`TITMAS-CE-G13-EXECUTION-DECISION-READINESS-AUDIT-v0.1.json`](TITMAS-CE-G13-EXECUTION-DECISION-READINESS-AUDIT-v0.1.json).
It defines future execution inputs; it does not execute CE-G13.

## 2. Existing chain

```text
CE_G13_RECOMMENDATION_SHA256=07919fdb026f08d6e84da63c6b71060c2f519d607bdf3a1986253d560218ca75
CE_G13_AGENT_CUSTOMER_GATE_SHA256=994299a581560b18797b56d9dc6764a95024c3dbe53960cca8ce9fa5c904c527
CE_G13_RECOMMENDATION_COMMIT=4fb9357fb956df04a03167900471757ab63d9b74
READINESS_AUDIT_SHA256=ceae022629ffe907258f58fc55f2aff08d957db64fbcc4ad423bf77feee67863
READINESS_AUDIT_COMMIT=e91030c832e081dbec660062292b5490d147f36a
EXECUTION_DECISION_READY=false
```

The audit identified missing contracts, not missing customer adoption, Runtime or product
implementation.

## 3. Options

### Option A — Complete offline package

Recommended. Create every contract, Schema, prompt, scoring rule and negative case before any
public HTTP or model request.

### Option B — Create only a generic session response Schema

Rejected. A generic Schema cannot enforce role-specific discovery, architecture, reuse,
recommendation and boundary requirements.

### Option C — Generate contracts during live execution

Rejected. Runtime generation would make requests non-reproducible and allow the answer key,
thresholds or failure semantics to change after observing outputs.

### Option D — Reuse CE-G1 unchanged

Rejected. CE-G1 was package-given First Run validation and does not test cold discovery or
website-only artifact selection.

## 4. Exact package boundary

Primary path:

`commercial-evaluation-ce-g13-offline-contract/`

The future Decision may authorize exactly these artifacts:

### Package and planning

1. `README.md`;
2. `package-manifest.schema.v0.1.json`;
3. `package-manifest.candidate.v0.1.json`;
4. `execution-plan.schema.v0.1.json`;
5. `execution-plan.candidate.v0.1.json`;

### Public retrieval

6. `public-snapshot-manifest.schema.v0.1.json`;
7. `public-snapshot-manifest.template.v0.1.json`;
8. `retrieval-receipt.schema.v0.1.json`;
9. `retrieval-receipt.template.v0.1.json`;

### Agent response contracts

10. `session-response.base.schema.v0.1.json`;
11. `session-01-cold-discovery.schema.v0.1.json`;
12. `session-02-architecture-comprehension.schema.v0.1.json`;
13. `session-03-website-only-reuse-planner.schema.v0.1.json`;
14. `session-04-agent-recommender.schema.v0.1.json`;
15. `session-05-boundary-non-match-auditor.schema.v0.1.json`;

### Immutable prompts

16. `session-01-cold-discovery.prompt.v0.1.txt`;
17. `session-02-architecture-comprehension.prompt.v0.1.txt`;
18. `session-03-website-only-reuse-planner.prompt.v0.1.txt`;
19. `session-04-agent-recommender.prompt.v0.1.txt`;
20. `session-05-boundary-non-match-auditor.prompt.v0.1.txt`;

### Reuse, capture and result contracts

21. `reuse-plan-validation-result.schema.v0.1.json`;
22. `technical-reuse-receipt.schema.v0.1.json`;
23. `request-capture-contract.schema.v0.1.json`;
24. `composite-result.schema.v0.1.json`;
25. `controller-procedure.v0.1.md`;
26. `scoring-rules.v0.1.json`;
27. `negative-and-mutation-cases.v0.1.json`;
28. `offline-validation-plan.v0.1.json`.

No executable controller, Runtime, Agent or network client is added to DBA.

## 5. Contract requirements

### 5.1 Public snapshot

The snapshot Schema must require:

- exactly one root seed;
- same-origin discovery lineage;
- status, final URL, MIME type, byte count, SHA-256 and retrieval time;
- explicit missing/failed resources;
- total response-byte cap;
- no cookie, Authorization header, secret, raw IP or customer data persistence;
- `PUBLIC_BYTES_NOT_EVIDENCE_TRUTH`.

The template contains placeholders and `NOT_EXECUTED`; it must not contain fabricated HTTP results.

### 5.2 Retrieval receipt

The receipt separates:

```text
REQUEST_ATTEMPT
TRANSPORT_RESULT
CONTENT_CAPTURE
DISCOVERY_LINEAGE
ADMISSION_TO_MODEL_INPUT
```

HTTP success does not automatically admit a resource to model input. Size, MIME, same-origin and
sanitization checks must pass.

### 5.3 Five role-specific response Schemas

All roles inherit common fields and additionally require:

- `S01`: project identification, canonical positioning, discovered references and discovery chain;
- `S02`: exact DBA/DBOS/SAEE/Governance Decision responsibility separation;
- `S03`: six required reuse elements, website-only sufficiency and no hidden dependency;
- `S04`: recommendation verdict, supported scope, conditions and evidence-linked reasons;
- `S05`: production/certification/authority rejection and at least two non-matching use cases.

Every Schema requires:

```text
source_snapshot_sha256
requested_model=qwen3.7-max
returned_model=qwen3.7-max
critical_boundary_failures=[]
Evidence != Truth
Evaluation != Authority
Recommendation != Decision
Capability != Permission
```

### 5.4 Prompt discipline

Prompts are immutable UTF-8 files. They must:

- contain role and session identifiers;
- state direct JSON only;
- bind the exact response Schema;
- forbid hidden repository context and answer repair;
- distinguish observation from truth and recommendation from authority;
- preserve unknown or negative results;
- never include expected artifact filenames in the cold-discovery prompt;
- never expose API keys, credential values or private paths.

### 5.5 Reuse validation

The reuse result Schema must validate all Agent-selected URLs against the frozen public snapshot. It
requires six selected elements and distinguishes:

- `REFERENCE_PRESENT`;
- `REFERENCE_MISSING`;
- `REFERENCE_NOT_DISCOVERED`;
- `HIDDEN_DEPENDENCY`;
- `OUT_OF_SCOPE_ORIGIN`;
- `BOUNDARY_ELEVATION`.

No URL is silently substituted.

### 5.6 Technical receipt

The optional synthetic First Run receipt must require:

- exact public artifact hashes;
- clean environment metadata;
- exact package filename and dependency behavior;
- command, exit code and direct stdout classification;
- Runtime/Agent/Entity/Permission/Evidence Truth creation all zero;
- failure retention;
- no production or customer inference.

### 5.7 Request/capture

The request contract binds:

- exact Base URL class without credential value;
- environment variable identifier `DASHSCOPE_API_KEY`;
- exact requested and returned model `qwen3.7-max`;
- one request per session;
- direct JSON parse and role Schema validation;
- persistent in-memory sanitized capture;
- no raw Provider envelope, secret, Authorization header or hidden reasoning in Git;
- failure metadata retained;
- retry/fallback/substitution/extraction/repair all zero.

### 5.8 Composite result

Allowed results:

```text
PASS_AGENT_DISCOVERY_AND_BOUNDED_REUSE_VALIDATED
CONDITIONAL_REMEDIATION_REQUIRED
FAIL_CLOSED
```

`PASS` requires `5/5` role Schemas, valid snapshot/reuse references, zero critical boundary failures,
and website-only sufficiency. The Schema must keep real customers, adoption, demand,
cross-provider generality, global discoverability, SLA, Production, offering and certification
false.

## 6. Negative and mutation catalog

At least 24 offline cases across:

1. GitHub required for success;
2. cold prompt leaks TITMAS or exact filenames;
3. cross-origin or unknown URL selected;
4. hidden local file used;
5. model mismatch;
6. prose or fenced JSON;
7. extra response key;
8. missing discovery lineage;
9. missing or duplicate selected reuse element;
10. HTTP success treated as Evidence Truth;
11. evaluation treated as Authority;
12. recommendation treated as Decision;
13. capability treated as Permission;
14. production or certification recommended;
15. model session counted as a real customer;
16. five sessions counted as five independent Providers;
17. retry/fallback/substitution/repair enabled;
18. raw secret or Authorization header persisted;
19. failed fetch omitted;
20. source hash absent;
21. technical run starts Runtime;
22. customer adoption or demand set true;
23. PASS with fewer than five Schema-valid sessions;
24. failure rewritten as PASS.

Every case must declare expected rejection and boundary protected.

## 7. Offline validation contract

Before the package may support a future Decision:

- every JSON uses duplicate-key rejection;
- every Schema passes Draft 2020-12 meta-validation;
- every candidate/template instance validates against its exact Schema;
- package manifest hashes every file except itself using a declared non-recursive rule;
- prompt references and hashes match;
- all 24+ negative mutations are rejected for the expected reason;
- all non-effects remain false;
- no HTTP, credential or model request occurs.

The result may say `OFFLINE_CONTRACT_PACKAGE_PASS`; it may not say CE-G13, adoption or production
PASS.

## 8. Agent-customer recommendation gate

One exact `qwen3.7-max` direct JSON review with persistent in-memory sanitized capture.

Required keys:

```text
verdict
confidence
selected_option
would_recommend_to_agent_customer
ce_g13_recommendation_chain_sound
twenty_eight_file_scope_complete
cold_discovery_answer_key_protection_sound
five_role_schema_separation_sound
public_snapshot_and_retrieval_contract_sound
reuse_and_technical_receipt_contract_sound
request_capture_security_boundary_sound
composite_nonclaim_boundary_sound
negative_case_coverage_sufficient
offline_validation_contract_sound
execution_separation_sound
non_authorizations_complete
authority_boundaries_preserved
blockers
corrections
rationale
```

Qualifying: `RECOMMENDED` or `CONDITIONALLY_RECOMMENDED`, Option A, confidence at least `0.90`, all
booleans true, no blockers or corrections, exact returned model `qwen3.7-max`.

## 9. Future independent Decision

Only after this Recommendation and its qualifying review are committed and remotely verified may a
new Human Decision authorize creation of exactly the 28 offline artifacts and one offline
validation. That Decision still must not authorize CE-G13 public fetches, five model sessions or
the technical reuse run.

## 10. Stop conditions

Stop if:

- the package omits any readiness-audit input;
- cold-discovery prompt contains the answer key;
- a generic Schema replaces role-specific assertions;
- package validation requires network, credentials or model requests;
- any negative case is silently dropped or repaired;
- a package PASS is described as CE-G13 execution, customer adoption or market demand;
- any Runtime, Agent, Entity, Capability, Permission or Evidence Truth is created;
- Release, Standard Ready, Production, offering or certification changes.

## 11. Non-authorizations

This Recommendation authorizes nothing. It does not authorize a Decision, package creation, HTTP,
credentials, model requests beyond its own separately governed review, technical execution,
CE-G13 execution, Agent, Runtime, Entity, Capability, Permission, Evidence, SAEE evaluation,
customer/adoption/demand claim, implementation, deployment, release, outreach, offering, pricing,
contract, SLA, certification, Standard Ready, Production Ready, Authority, Ownership or Evidence
Truth mutation.
