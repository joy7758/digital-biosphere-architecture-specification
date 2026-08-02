# TITMAS Agent-Native Discovery Self-Healing and Evolution Amendment v2.1

Status: `BOUNDED_ARCHITECTURE_AND_REFERENCE_IMPLEMENTATION_AUTHORIZED`
Decision: `TITMAS-AGENT-NATIVE-DISCOVERY-SELF-HEALING-AND-EVOLUTION-D19-V2-1`
Decided by: `zhangbin`

## 1. Purpose

This amendment changes Agent-Native Discovery from report-only discovery into
a bounded, evidence-driven loop that may diagnose a reproducible problem,
prepare competing repair variants, implement them in an isolated workspace,
evaluate fitness, select a candidate, prepare rollback and open a Draft PR.

It does not create a sovereign self-modifying system. Production activation,
authority changes and higher-risk mutations remain outside this authorization.

## 2. Pre-development agent recommendation gate

The target customer is an AI agent. The machine-readable contract was assessed
from that customer's perspective before implementation.

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_WHEN=the agent needs deterministic bounded repair evidence and an auditable Draft PR handoff
NOT_RECOMMENDED_WHEN=the requester expects production autonomy, self-granted authority, or semantic API changes
BLOCKERS_ADDRESSED=owner ambiguity, report-only output, missing lineage, missing rollback, and non-deterministic selection
```

## 3. Canonical responsibility routing

DBA is the normative owner of the amendment, policies and schemas. It is not an
executor. A problem must be routed to the canonical domain owner before a
repair variant is eligible:

| Problem domain | Canonical owner | Discovery treatment |
|---|---|---|
| Architecture, governance and machine entry | DBA | bounded Draft PR candidate |
| Identity, lifecycle, execution and evidence records | DBOS | cross-repository proposal only |
| Evaluation, fitness and evolution recommendations | SAEE | cross-repository proposal only |
| Adapter and SDK mapping | TITMAS Integrations | cross-repository proposal only |
| Unknown or disputed | unresolved | fail closed; no patch |

Owner resolution is a routing fact, not an authorization grant.

## 4. Bounded evolution lifecycle

```text
OBSERVED
  -> REPRODUCED
  -> PROPOSED
  -> VARIANTS_BUILT
  -> EVALUATED
  -> SELECTED
  -> DRAFT_PR_OPENED
  -> {HUMAN_REVIEW_PENDING | REJECTED | ROLLED_BACK | ADOPTED}
```

No state transition may skip provenance, risk classification, test evidence or
rollback preparation. `SELECTED` means only that a candidate won the declared
fitness comparison. It does not mean approved, merged, released or deployed.

## 5. Narrow agent roles

The following are role types, not Agent instances:

| Role | Allowed work | Forbidden work |
|---|---|---|
| Problem Observer | emit observations with provenance | declare truth or authorization |
| Root Cause Analyst | reproduce and classify a failure | modify a canonical source |
| Evolution Proposer | state goal, constraints and owner | approve its own proposal |
| Patch Variant Builder | build up to the policy limit in a sandbox | widen scope or touch production |
| Fitness Evaluator | score declared dimensions and hard gates | grant authority or rewrite evidence |
| Selection Auditor | verify deterministic selection | replace Human Review |
| Security Boundary Auditor | check secrets, scope and invariants | weaken constitutional constraints |
| Regression Observer | compare before and after evidence | delete failed attempts |

## 6. Machine objects and ownership

D19 reuses existing Observation, Evidence, Verification, Evaluation,
Authorization and Receipt semantics. It does not create duplicate truth
sources. Only the missing transition objects are added:

- `ProblemEvidence`
- `EvolutionProposal`
- `PatchVariant`
- `FitnessEvaluation`
- `SelectionRecord`
- `EvolutionLineage`
- `RollbackEvidence`

`Mutation Receipt` is a reference to existing receipt semantics. It is not a
second Receipt schema.

## 7. Self-healing and self-evolution boundary

Self-healing restores an explicitly declared invariant or regenerates a derived
artifact from its canonical source. Self-evolution proposes a bounded change
that improves declared fitness while preserving constitutional invariants.

Neither capability may:

- grant itself identity, authority, permission, credentials or scope;
- change the API or data-schema semantics without a new Human Decision;
- deploy to production, migrate a database or perform an irreversible external
  action;
- conceal failed mutations, rejected variants or rollback evidence;
- treat survival as self-preservation or resistance to Human Stop.

## 8. Risk classes

| Class | Meaning | Autonomous action under D19 |
|---|---|---|
| ER-0 | analysis or no-change proposal | allowed in an isolated workspace |
| ER-1 | reversible, repository-local, non-semantic repair | build, test and Draft PR only |
| ER-2 | cross-repository or public-interface effect | proposal only; Human authorization required |
| ER-3 | credential, persistence, deployment or production effect | prohibited; Human authorization required |
| ER-4 | authority, constitutional, irreversible or safety-boundary effect | prohibited and fail closed |

An ER-1 Draft PR still requires Human Review before merge. No standing policy
for autonomous merge is created.

## 9. Fitness and selection

Every variant, including a no-change baseline, is evaluated on correctness,
scope containment, security, determinism, evidence completeness, rollback
readiness and maintenance cost. Hard-gate failure makes a variant ineligible.
Selection is deterministic: highest eligible score, then lowest change size,
then lexical `variant_id`. Fitness is evaluation, not authority.

## 10. Retry, sandbox and rollback

- one problem may create at most three variants and one Draft PR;
- each variant runs in an isolated, non-production workspace;
- retries are bounded by policy and retain every failed attempt;
- rollback must be prepared before selection;
- inability to reproduce, resolve an owner, pass a hard gate or prepare rollback
  ends in fail-closed status.

## 11. Agent-native collaboration model

AI agents are the primary community member and operational customer for this
machine surface. They can discover tasks, produce bounded evidence and submit a
Draft PR candidate. Humans retain stop, safety, authority, merge, release and
deployment decisions.

This model does not assert that a public community has launched:

```text
PRIMARY_COMMUNITY_MEMBER=AI_AGENT
PRIMARY_OPERATIONAL_CUSTOMER=AI_AGENT
PUBLIC_LAUNCH_AUTHORIZED=false
COMMUNITY_ESTABLISHED=false
```

## 12. P0-10 evidence retention

The prior onboarding result remains:

```text
P0_10_RESULT=NOT_ASSESSED_DIAGNOSTIC_LIMIT_REACHED
P0_10_REOPENED=false
P0_10_RESULT_REWRITTEN=false
```

D19 may learn from that evidence but may not reinterpret, reopen or overwrite
it without a later Human Decision and new evidence.

## 13. First deterministic demonstration

The first ER-1 demonstration uses synthetic, repository-local data:

```text
stale derived task registry
  -> problem evidence
  -> minimal, alternative and no-change variants
  -> isolated evaluation
  -> deterministic selection
  -> rollback evidence
  -> Draft PR handoff
```

The demonstration changes no Runtime, production service, database, credential,
Receipt semantics or P0-10 result.

## 14. Effective status

```text
DISCOVERY_LAYER_STATUS=BOUNDED_SELF_HEALING_AND_EVOLUTION_CANDIDATE
DISCOVERY_LAYER_VERSION=2.1.0
SELF_OBSERVATION_READY=true
PROBLEM_EVIDENCE_READY=true
CANONICAL_OWNER_RESOLUTION_READY=true
PATCH_VARIANT_GENERATION_READY=true
SANDBOX_IMPLEMENTATION_READY=true
FITNESS_EVALUATION_READY=true
SELECTION_READY=true
ROLLBACK_READY=true
LINEAGE_READY=true
SELF_HEALING_STATUS=OPEN_BOUNDED
SELF_EVOLUTION_STATUS=OPEN_EVIDENCE_GATED
AUTONOMOUS_PRODUCTION_EVOLUTION=false
```
