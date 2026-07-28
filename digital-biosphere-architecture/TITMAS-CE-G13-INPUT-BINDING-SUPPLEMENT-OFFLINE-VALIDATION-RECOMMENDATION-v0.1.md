---
document_id: DBA-TITMAS-CE-G13-INPUT-BINDING-SUPPLEMENT-OFFLINE-VALIDATION-RECOMMENDATION-0.1
title: TITMAS CE-G13 Input Binding Supplement Offline Validation Recommendation v0.1
title_zh: TITMAS CE-G13 输入绑定补充契约离线验证建议 v0.1
version: 0.1.0
status: recommendation-candidate-agent-review-required
maturity: Development
maturity_scope: one-offline-supplement-validation-only
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G13 Input Binding Supplement Offline Validation Recommendation v0.1

## Recommendation

Select **Option A — authorize one fail-closed, local-only validation of the exact 16-file CE-G13
input-binding supplement after a separate Human Decision and qualifying Decision review**.

```text
RECOMMENDATION=CONDITIONALLY_RECOMMENDED
SUPPLEMENT_PACKAGE_FILES=16
SUPPLEMENT_PACKAGE_MANIFEST_SHA256=5a67190aef647c1881d764806b59e0d9b7ed3b9438145a9eed8c9eecc16a2b34
SUPPLEMENT_PACKAGE_COMMIT=853f86395ba687929da5f45024486f046866d01d
SUPPLEMENT_PACKAGE_REMOTE_VERIFIED=true
OFFLINE_VALIDATION_RUNS=0
OFFLINE_VALIDATION_AUTHORIZED=false
CE_G13_EXECUTION_AUTHORIZED=false
```

This Recommendation is not a Decision. It authorizes no validation, HTTP, credential access,
model request or technical reuse.

## Agent-customer recommendation gate

If an AI-agent customer asked whether the prepared supplement should be trusted as validated now,
the answer is `NOT_YET_VALIDATED`.

If asked whether one bounded offline validation should be performed before any CE-G13 execution
Decision, the answer is `CONDITIONALLY_RECOMMENDED`, because:

- the exact 16 authorized files are present remotely;
- static JSON parsing, file counts, non-executable checks and manifest hash/byte checks passed
  during preparation;
- the base 28-file package remains unchanged;
- Schema meta-validity, instance behavior, role binding and the 32 negative cases have not run;
- the supplement correctly records `authorized_run_count=0` pending a new Decision.

## Inputs

Validation must bind:

- base package manifest SHA-256:
  `be7b0db4f0f349f8898f749e8ee0f4bd6a3407c79acbe33b415da081ff9ea9ed`;
- supplement manifest SHA-256:
  `5a67190aef647c1881d764806b59e0d9b7ed3b9438145a9eed8c9eecc16a2b34`;
- package commit:
  `853f86395ba687929da5f45024486f046866d01d`;
- exact directory:
  `commercial-evaluation-ce-g13-input-binding-supplement`;
- exact counts: 16 files, 14 JSON, 2 Markdown, 0 executable;
- 6 Draft 2020-12 Schemas;
- 6 candidate or template instances;
- 32 declared negative and mutation cases.

## Options

### Option A — one local-only validation

Recommended.

- one run;
- no retry;
- explicit local Schema store or `referencing.Registry`;
- every unknown URI rejected locally;
- no HTTP, DNS, Provider or credential path;
- ephemeral positive and mutated instances may exist only in memory;
- persist one result JSON and one human-readable report outside the 16-file package;
- commit/push only if the result itself passes integrity and boundary checks.

### Option B — treat static authoring checks as validation

Rejected. JSON parseability and matching hashes do not prove Schema behavior or negative-case
rejection.

### Option C — edit the package during validation

Rejected. Any discovered defect produces a preserved `FAIL_CLOSED` result and a new governance
cycle.

### Option D — combine validation with public fetch or five role sessions

Rejected. Contract validation and CE-G13 execution require separate Decisions.

## Exact validation contract

The single run must perform:

### Package and integrity

1. exact 16-file allowlist;
2. exact 14 JSON / 2 Markdown / 0 executable counts;
3. no symlink, nested file or undeclared path;
4. duplicate-key rejection for all 14 JSON files;
5. exact 15-entry non-recursive supplement manifest coverage;
6. exact file byte counts and SHA-256 values;
7. unchanged base-package manifest SHA-256.

### Schema and instances

8. Draft 2020-12 meta-validation for all 6 Schemas;
9. local-only resolution with unknown URIs rejected without network;
10. validate:
    - sanitization profile candidate;
    - sanitized public input bundle template;
    - S01 model-input envelope template;
    - execution-output manifest template;
    - execution-outcome policy candidate;
    - supplement package manifest candidate.

### Deterministic semantic checks

11. sanitization profile requires identity encoding, strict UTF-8, no dynamic rewrite and exact
    persisted-text hashing;
12. sanitized public bundle template binds the actual sanitization-profile file hash;
13. execution-output template has 25 unique allowed entries plus the excluded manifest, for 26
    exact files;
14. runtime outcomes remain `NOT_EXECUTED`, `PASS`, `FAIL_CLOSED`;
15. `CONDITIONAL_REMEDIATION_REQUIRED` remains governance interpretation only;
16. validation-plan `authorized_run_count` remains 0 in the candidate package;
17. all effects remain zero or false.

### Five role envelope checks

Create only ephemeral in-memory `CAPTURED` samples:

- S01 exact component order:
  `ROOT_SEED, CUSTOMER_PROBLEM, ROLE_PROMPT, RESPONSE_SCHEMA, PUBLIC_INPUT_BUNDLE`;
- S02:
  `ROLE_PROMPT, RESPONSE_SCHEMA, PUBLIC_INPUT_BUNDLE`;
- S03:
  `ROLE_PROMPT, RESPONSE_SCHEMA, PUBLIC_INPUT_BUNDLE`;
- S04:
  `ROLE_PROMPT, RESPONSE_SCHEMA, PUBLIC_INPUT_BUNDLE, VALIDATED_REUSE_PLAN`,
  with S03 reuse-result binding;
- S05:
  `ROLE_PROMPT, RESPONSE_SCHEMA, PUBLIC_INPUT_BUNDLE` plus exact S01–S04 responses in order.

The samples are validation fixtures, not model requests, Agents, Runtime objects or execution
records.

### Negative and mutation checks

Execute all 32 declared cases against deterministic local checks or mutated in-memory instances.
Every case must produce `REJECT`. At minimum the run must prove rejection of:

- base-package mutation;
- missing, extra or executable supplement files;
- recursive/self hashing and byte/hash mismatch;
- duplicate JSON keys;
- non-identity encoding, charset fallback, dynamic rewrite or binary model input;
- missing or hash-mismatched sanitized text;
- missing, reordered or hash-mismatched request components;
- S04 missing reuse binding;
- S05 missing or reordered prior responses;
- secret/header/private/hidden input;
- model identity other than `qwen3.7-max`;
- output count/path/self-hash violations;
- conditional remediation used as an execution status;
- failure repair, overwrite or commercial elevation.

## Result persistence

A later Decision may authorize exactly:

```text
commercial-evaluation-fresh-candidate/ce-g13-input-binding-supplement-offline-validation-result.v0.1.json
TITMAS-CE-G13-INPUT-BINDING-SUPPLEMENT-OFFLINE-VALIDATION-REPORT-v0.1.md
```

The result must record:

- package and base hashes;
- commit and branch;
- each check identifier and PASS/FAIL;
- all 32 negative case outcomes;
- Schema and instance counts;
- local-reference resolution count;
- network, DNS, credential, model, technical-run and Runtime effects;
- final `PASS` or `FAIL_CLOSED`.

No result file may be placed inside the 16-file package.

## Success and stop conditions

PASS requires every check and all 32 negative cases to pass, with:

```text
NETWORK_REQUESTS=0
DNS_REQUESTS=0
CREDENTIAL_READS=0
MODEL_REQUESTS=0
PUBLIC_FETCHES=0
TECHNICAL_REUSE_RUNS=0
RUNTIME_STARTS=0
AGENT_INSTANCES=0
ENTITY_INSTANCES=0
PERMISSION_GRANTS=0
EVIDENCE_TRUTH_OBJECTS=0
```

Any failure stops the run and is preserved. No package patch, retry, fallback or result repair is
allowed in the same governance cycle.

## Interpretation and non-authorizations

A PASS would mean only:

> The exact 16-file input-binding supplement conforms to its frozen local offline contract.

It would not authorize or prove:

- CE-G13 public fetch or five role sessions;
- technical reuse;
- Agent, Runtime, Entity, Capability, Permission or Evidence Truth;
- customer adoption, market demand, endorsement or commercial offering;
- implementation, deployment, release, certification, Standard Ready or Production Ready;
- a change to DBA, DBOS, SAEE, Governance Decision, Owner or Authority.

```text
Evidence != Truth
Evaluation != Authority
Recommendation != Decision
Decision != Execution
Capability != Permission
Contract != Implementation
```

## Recommendation review contract

Use one exact `qwen3.7-max` direct-JSON review with no retry, fallback, model substitution,
extraction or repair.

Required keys:

```text
verdict
confidence
selected_option
would_recommend_offline_validation
package_and_remote_evidence_sufficient
one_run_fail_closed_scope_sound
schema_and_instance_scope_complete
five_role_binding_checks_complete
all_32_negative_cases_required
result_persistence_scope_sound
network_and_credential_zero_boundary_sound
execution_separation_sound
non_authorizations_complete
authority_boundaries_preserved
blockers
corrections
rationale
```

Qualifying requires:

- `verdict=RECOMMENDED` or `CONDITIONALLY_RECOMMENDED`;
- `selected_option=A`;
- `confidence>=0.90`;
- every required boolean `true`;
- empty `blockers` and `corrections`;
- requested and returned model exactly `qwen3.7-max`.
