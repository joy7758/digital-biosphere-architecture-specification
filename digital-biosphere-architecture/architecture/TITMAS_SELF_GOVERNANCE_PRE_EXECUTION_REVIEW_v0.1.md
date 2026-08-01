# TITMAS Self-Governance Pre-Execution Review v0.1

```text
DOCUMENT_TYPE=SELF_GOVERNANCE_PRE_EXECUTION_REVIEW
STATUS=REVIEW_ONLY
VERSION=0.1
DATE=2026-07-28

ORIGINAL_EXPERIMENT_OBJECTIVE_PRESERVED=true
GITHUB_FIRST_CHANGES_EXPERIMENT_DESIGN=false
GITHUB_FIRST_CHANGES_EXPERIMENT_PROTOCOL=false

CURRENT_COHORT_EXISTS=false
COHORT_FROZEN=false
FORMAL_COHORT_FREEZE_READY=false
READY_TO_REQUEST_EXPERIMENT_AUTHORIZATION=false
EXPERIMENT_EXECUTION_AUTHORIZED=false
EXPERIMENT_EXECUTED=false

CONSTITUTION_CHANGED=false
INTERFACE_BOUNDARY_CHANGED=false
EXPERIMENT_PROTOCOL_CHANGED=false
CODE_CREATED=false
DASHBOARD_CREATED=false
API_CREATED=false
ADAPTER_CREATED=false
IMPLEMENTATION_AUTHORIZED=false
```

## 0. Executive decision

The `GitHub-first Discovery Strategy` does not change the original
Self-Governance Experiment objective when it remains:

- a Phase 1 discovery heuristic;
- non-exclusive;
- source-native;
- removable;
- non-authoritative;
- separate from Evidence, Evaluation, Permission, Authorization, and
  Execution.

The experiment continues to ask:

> Does TITMAS reduce the total cognitive and operational cost for one human
> managing multiple repositories, programs, Agents, tools, and external
> services?

However, the current candidate material is not ready to enter experiment
authorization.

The principal blocker is not GitHub-first itself. The blocker is that the
proposed candidate portfolio currently confirms only two actual external
service classes—GitHub and Codex—while the Protocol requires at least four and
at least one deployment, data/backend, planning, or domain/security surface.

Decision:

```text
STRATEGIC_GUARDRAIL_ALIGNMENT=PASS
EXPERIMENT_OBJECTIVE_ALIGNMENT=PASS
CANDIDATE_COHORT_CONCEPTUAL_FIT=PASS_WITH_LIMITATIONS
PRE_EXECUTION_COMPLETENESS=BLOCK
EXPERIMENT_AUTHORIZATION_READINESS=BLOCK

READY_FOR_HUMAN_BLOCKER_RESOLUTION_REVIEW=true
READY_TO_REQUEST_EXPERIMENT_AUTHORIZATION=false
READY_TO_GRANT_EXPERIMENT_AUTHORIZATION=false
```

This review does not execute the experiment, freeze the Cohort, or authorize
Implementation.

## 1. Review basis

| Input | SHA-256 |
|---|---|
| `TITMAS_STRATEGIC_GUARDRAILS_REVIEW_v0.1.md` | `2d7304d751942b15bb400465cd0a39cfe26f1d0a4811eaf0c9dbb6ba8641bafc` |
| `TITMAS_SELF_GOVERNANCE_EXPERIMENT_DESIGN_v0.1.md` | `394876046ce663390ec7956d6a4aff1daeba868fa79730e20adc3f2303cfed3d` |
| `TITMAS_SELF_GOVERNANCE_EXPERIMENT_PROTOCOL_v0.1.md` | `2704cd172f0f23860b93ca0c6dfa0b1b421510bc7e2b143c55137e594aae046f` |
| `TITMAS_SELF_GOVERNANCE_COHORT_PROPOSAL_v0.1.md` | `88edd47590c2550787a6aba822d364ebd6418cb13821f87da7f155b2fab30ed7` |
| `TITMAS_GOVERNANCE_CONSISTENCY_REVIEW_v0.1.md` | `0ff1a815ea8d0b32ae9e66546b97f3dd72be34f557c1cd16bbbec52bc1e35c29` |

The documents have different roles:

| Document | Role in this review | Does not establish |
|---|---|---|
| Strategic Guardrails Review | Defines safe meaning of GitHub-first | Strategy adoption or implementation |
| Experiment Design | Defines objective, estimand, outcomes, and safety gates | Execution authorization |
| Experiment Protocol | Defines manual procedures and minimum freeze requirements | A frozen Cohort |
| Cohort Proposal | Supplies candidate objects and blockers | A current or formal Cohort |
| Governance Consistency Review | Preserves Authority and non-elevation constraints | Later acceptance or implementation |

## 2. Does GitHub-first affect the experiment objective?

### 2.1 Formal objective

Status: `NO_CHANGE`

The Design and Protocol retain the same primary question, metrics, and
Authority separation. The Strategic Guardrails Review does not modify either
document.

GitHub-first changes only the likely order in which a human discovers
GitHub-hosted software assets. It does not change:

- the unit of management cost;
- the requirement to include external services;
- the Baseline workflow;
- the TITMAS Condition;
- the risk actionability definition;
- false-positive or false-negative adjudication;
- the Cognitive Overhead Ratio;
- the Human Authority boundary.

```text
ESTIMAND_CHANGED=false
PRIMARY_OUTCOME_CHANGED=false
BASELINE_CHANGED=false
TITMAS_CONDITION_CHANGED=false
SUCCESS_THRESHOLD_CHANGED=false
```

### 2.2 Construct-validity risk

Status: `HIGH_RISK_IF_UNCONTROLLED`

Although the formal objective is unchanged, GitHub-first can narrow the
experiment in practice if:

- all selected assets are represented only as repositories;
- GitHub Issues, PRs, Actions, and Releases are treated as separate external
  service classes;
- non-GitHub provider state is skipped;
- GitHub-native navigation is mistaken for general digital-asset
  understanding;
- a GitHub-heavy result is generalized to heterogeneous services.

If this occurs, the actual tested question becomes:

> Does TITMAS reduce the cost of managing several GitHub repositories?

That is narrower than the approved question.

Required invariant:

```text
FORMAL_OBJECTIVE=HETEROGENEOUS_SOFTWARE_ECOSYSTEM_MANAGEMENT
GITHUB_ONLY_SUBSTITUTE_OBJECTIVE=PROHIBITED
```

### 2.3 Acceptable GitHub-first use

GitHub-first may be retained only when:

1. GitHub is counted as one external-service class;
2. repository objects return to GitHub;
3. local dirty state returns to the selected Git worktree;
4. deployment, backend, planning, documentation, domain, and Agent-task facts
   return to their native sources;
5. source hops to those services remain measured;
6. unavailable external sources remain visible;
7. GitHub ranking or popularity does not define Attention;
8. the conclusion remains bounded to the frozen Cohort.

## 3. Candidate Cohort review

There is no current formal Cohort.

The available object is:

```text
TITMAS_SELF_GOVERNANCE_COHORT_PROPOSAL_v0.1
PROPOSAL_RESULT=PREPARED_WITH_BLOCKERS
COHORT_FROZEN=false
```

This review therefore evaluates the candidate set, not a frozen Cohort.

### 3.1 Candidate repository set

The proposed primary Management candidates are:

1. `digital-biosphere-architecture-specification`;
2. `agent-evidence`;
3. `agent-health`;
4. `digital-biosphere-os`;
5. `titmas-demo`.

The proposal also retains:

- `SAEE` as a protected conditional reserve;
- six possible Onboarding projects;
- `agent-evidence-layer` as excluded pending canonical-source and owner
  resolution.

The repository-count minimum can be met conceptually. Count alone does not
make the Cohort ready.

### 3.2 Digital Asset Understanding

Status: `PARTIAL_PASS`

The candidate set can test understanding of GitHub-hosted software assets
because the proposal identifies:

- remote repository identity;
- local worktree;
- observed branch and `HEAD`;
- source account owner;
- owner uncertainty;
- freshness source;
- Management/Onboarding suitability;
- risks and limitations.

It does not yet support a valid execution because:

- Human Operational Owners are unconfirmed;
- selected native-source access is unconfirmed;
- local/remote mappings remain unresolved for some candidates;
- the two DBA repository identities require an explicit choice;
- `agent-health` has an unresolved upstream mapping;
- non-GitHub asset surfaces are not sufficiently confirmed;
- source windows and review horizons are not frozen.

Decision:

```text
GITHUB_HOSTED_ASSET_UNDERSTANDING_CANDIDATE=PASS
HETEROGENEOUS_DIGITAL_ASSET_UNDERSTANDING_READY=false
```

### 3.3 Evidence First

Status: `DESIGN_PASS / EXECUTION_BLOCK`

The candidate proposal correctly separates:

- GitHub remote facts;
- local worktree facts;
- external-provider facts;
- Source Account Owner;
- Human Operational Owner;
- observed time;
- freshness;
- unknown and unavailable states.

This is consistent with Evidence First.

Execution remains blocked because the following are not frozen:

- exact source references;
- permitted access boundaries;
- expected freshness;
- unavailable/partial behavior;
- sensitive-data exclusions;
- Evidence location;
- retention and access rule;
- reviewer/adjudicator identity.

Required pre-execution invariant:

```text
DISCOVERY_RESULT=OBSERVATION_MATERIAL
CANONICAL_SOURCE_ACCESS=CONFIRMED
FRESHNESS_RULE=FROZEN
SENSITIVE_DATA_BOUNDARY=FROZEN
EVIDENCE_LOCATION=AUTHORIZED_EXISTING_LOCATION
```

Current state:

```text
CANONICAL_SOURCE_ACCESS=UNCONFIRMED
FRESHNESS_RULE=NOT_FROZEN
SENSITIVE_DATA_BOUNDARY=NOT_FROZEN
EVIDENCE_LOCATION=NOT_AUTHORIZED_IN_FREEZE_RECORD
```

### 3.4 Human Attention Amplification

Status: `DESIGN_PASS / SESSION_NOT_READY`

The candidate set is suitable in principle for measuring:

- source hops;
- context switches;
- risk-discovery time;
- project-status understanding;
- new-project onboarding cost;
- false positives and false negatives;
- Attention preparation overhead.

GitHub-first does not change Attention into Agent selection or routing.

However:

- no valid Attention packet exists;
- no Attention Preparer is confirmed;
- no Operator is confirmed;
- no pair/order/window is frozen;
- GitHub search order, topics, stars, or activity have not been approved as
  ranking inputs and must not become such inputs;
- preparation work has already created prior familiarity that must be
  recorded.

```text
ATTENTION_ROLE=HUMAN_ATTENTION_AMPLIFICATION
ATTENTION_AS_GITHUB_RANKING=PROHIBITED
ATTENTION_SESSION_READY=false
```

## 4. Does the experiment still validate the original goal?

### 4.1 Design-level answer

Status: `YES`

The experiment still measures total management cost through:

- active management time;
- source verification time;
- navigation;
- context recovery;
- risk discovery;
- onboarding;
- Attention preparation;
- human review and override;
- error correction;
- false-positive/false-negative adjudication;
- Cognitive Overhead Ratio.

It still requires external services to remain authoritative and independently
usable.

### 4.2 Candidate-execution answer

Status: `NO_NOT_YET`

The current proposal confirms:

| Required dimension | Current preparation evidence |
|---|---|
| At least five real repositories | Candidate set available |
| At least one Agent-assisted workflow | Codex candidate available |
| At least four actual external-service classes | Not met; only GitHub and Codex confirmed |
| Deployment/data/planning/domain-security surface | Not confirmed |
| Formal Cohort | Not frozen |
| Human roles | Not confirmed |
| Source/access/freshness map | Candidate only; not frozen |
| Sensitive-data boundary | Not frozen |
| Pair/order/window | Not frozen |
| Evidence location and retention | Not authorized in a Freeze Record |
| Separate execution authorization | False |

If executed now, the experiment would not validly test the approved
heterogeneous-service objective.

### 4.3 External-service minimum

```text
CONFIRMED_ACTUAL_SERVICE_CLASSES=2
CONFIRMED_SERVICES=GITHUB+CODEX
REQUIRED_SERVICE_CLASSES=4
EXTERNAL_SERVICE_MINIMUM_MET=false
```

Cloudflare remains conditional because local Worker/plugin configuration does
not prove a live, accessible provider object. Context7 remains conditional
because Cohort-specific normal use is unconfirmed. Render, Supabase, and
Linear remain outside the candidate scope until actual use is evidenced.

GitHub-first cannot waive this requirement.

## 5. Platformization risk

Status: `RESIDUAL_HIGH / CONTROL_DEFINED`

### 5.1 Risk

The experiment can accidentally validate a future platform narrative rather
than management-cost reduction if:

- GitHub metadata is copied into a TITMAS inventory;
- Attention preparation becomes a permanent service;
- the manual packet is described as a Dashboard;
- source navigation becomes a universal portal;
- provider state is normalized into a shadow database;
- a successful result is interpreted as permission to build a platform.

### 5.2 Required control

The Protocol already limits the TITMAS Condition to bounded, deletable,
manually prepared, source-attributed materials.

Before execution, the Human Freeze must reaffirm:

```text
NO_UNIFIED_DATABASE=true
NO_DASHBOARD=true
NO_ADAPTER=true
NO_API=true
NO_WRITEBACK=true
NO_PLATFORM_CLAIM=true
```

Any experiment result remains:

```text
SCOPED_EXPERIMENT_EVIDENCE
NE_PRODUCT_VALIDATION
NE_IMPLEMENTATION_AUTHORIZATION
```

## 6. GitHub-dependency risk

Status: `HIGH`

### 6.1 Sources of dependency

- all five primary repository candidates use GitHub remotes;
- the same source account namespace appears across most candidates;
- GitHub provides multiple repository-native surfaces that may dominate
  navigation;
- the Operator is already familiar with GitHub and the portfolio;
- non-GitHub provider facts are not yet sufficiently confirmed;
- clean and dirty repository states vary widely.

### 6.2 Experimental confounds

| Confound | Potential distortion |
|---|---|
| GitHub familiarity | Makes both conditions faster and reduces generalizability |
| GitHub-heavy sources | Hides the cost of heterogeneous provider switching |
| GitHub object model | Treats Issues/PRs/Actions as universal asset semantics |
| One source-account namespace | Hides organizational owner-discovery cost |
| GitHub search/order | Can introduce hidden Attention ranking |
| Remote/local divergence | Makes GitHub appear more complete than it is |
| Provider absence | Converts external-service management into a repository-only task |

### 6.3 Required pre-execution control

- confirm at least two additional actual external-service classes;
- retain their native source references;
- do not split GitHub into multiple service classes;
- include a deployment, backend, planning, or domain/security surface;
- preserve source hops away from GitHub;
- record prior GitHub and repository familiarity;
- restrict claims to the final frozen Cohort;
- do not introduce a provider solely to satisfy the minimum.

## 7. Centralization risk

Status: `MEDIUM_TO_HIGH / NOT_ACTUALIZED`

No central platform has been created. Centralization remains a design and
experimental-bias risk.

Possible hidden authority:

- GitHub search results determine which assets are reviewed;
- repository activity determines Attention order;
- a manual packet hides candidates outside GitHub;
- the Operator accepts the top three without native-source verification;
- Attention preparation becomes the only allowed route to project state;
- all asset identity is reduced to GitHub owner/repository.

Required invariants:

```text
GITHUB_SEARCH_NE_COMPLETE_COHORT=true
GITHUB_ACTIVITY_NE_PRIORITY=true
ATTENTION_RANKING_NE_AUTHORITY=true
HUMAN_OVERRIDE_REQUIRED=true
NATIVE_SOURCE_DRILL_DOWN_REQUIRED=true
OMITTED_AND_DOWNRANKED_CANDIDATES_VISIBLE=true
```

## 8. New maintenance-cost risk

Status: `MATERIAL_AND_MEASURABLE`

The strategy adds potential overhead even without implementation:

- checking GitHub source identity and freshness;
- reconciling local dirty worktrees with remote branches;
- resolving duplicated or similarly named repositories;
- maintaining source links;
- checking provider access;
- explaining unavailable non-GitHub sources;
- preparing Attention Candidates;
- reviewing and overriding rankings;
- preserving evidence and exclusions;
- updating provider-specific guardrail interpretation.

None of this may be treated as zero-cost preparation.

The experiment must include:

```text
ATTENTION_PREPARATION_TIME
SOURCE_RECONCILIATION_TIME
STALE_LINK_CORRECTION_TIME
HUMAN_REVIEW_TIME
OVERRIDE_TIME
FAILED_SOURCE_ACCESS_TIME
```

The strategy fails its mission if:

```text
TITMAS_PREPARATION_AND_MAINTENANCE_COST
>=
MANUAL_MANAGEMENT_COST_REDUCTION
```

## 9. Governance Consistency status

The Strategic Guardrails Review improves the interpretation of discovery but
does not erase earlier governance blockers.

The Governance Consistency Review retains:

```text
OVERALL=REVISE
AUTHORITY_CONSISTENCY=BLOCK
MANAGEMENT_COST_REDUCTION=BLOCK
IMPLEMENTATION_GATE=BLOCK
```

The Self-Governance Experiment is the proposed way to gather management-cost
Evidence; that does not mean the experiment is already authorized.

Before execution, a Human Decision must explicitly distinguish:

- authorization to conduct one bounded manual experiment;
- adoption of GitHub-first as a project strategy;
- architecture or constitutional adoption;
- Implementation authorization.

Only the first may be considered after the pre-execution blockers are
resolved.

```text
EXPERIMENT_AUTHORIZATION_NE_STRATEGY_ADOPTION=true
EXPERIMENT_AUTHORIZATION_NE_IMPLEMENTATION=true
EXPERIMENT_RESULT_NE_ARCHITECTURE_ADOPTION=true
```

## 10. Pre-execution blocker register

### `PEB-01` — Formal Cohort

```text
STATUS=BLOCK
```

The proposal is not a frozen Cohort.

Required human resolution:

- exact Management repositories;
- exact Onboarding reserves;
- inclusion/exclusion decisions;
- source windows;
- exact remote/worktree/branch/`HEAD`.

### `PEB-02` — Human roles

```text
STATUS=BLOCK
```

Unconfirmed:

- Experiment Owner;
- Operator;
- Reviewer;
- role overlap;
- Human Operational Owner for each object;
- concurrent human or Agent contributors.

### `PEB-03` — External-service minimum

```text
STATUS=BLOCK
```

Only two actual service classes are confirmed. Four are required.

### `PEB-04` — Non-repository surface

```text
STATUS=BLOCK
```

No deployment, data/backend, planning, or domain/security service surface is
yet confirmed with native access and owner/freshness boundaries.

### `PEB-05` — Canonical-source access

```text
STATUS=BLOCK
```

Native source references, access limitations, expected freshness, and
unavailable behavior are not formally frozen.

### `PEB-06` — Sensitive-data boundary

```text
STATUS=BLOCK
```

Repository-specific and provider-specific sensitive-data exclusions require
human confirmation.

### `PEB-07` — Pairing, order, and windows

```text
STATUS=BLOCK
```

Management matched pairs, Onboarding condition assignments, condition order,
observation windows, review horizon, and timebox are not frozen.

### `PEB-08` — Evidence governance

```text
STATUS=BLOCK
```

An existing authorized Evidence location, retention rule, access list, and
stop authority have not been recorded in a Freeze Record.

### `PEB-09` — Prior familiarity

```text
STATUS=REVISE
```

Preparation has exposed repository names, branches, `HEAD` values, dirty path
counts, risks, and external-service gaps. This must be recorded and controlled
in matching and interpretation.

### `PEB-10` — Human disposition of review documents

```text
STATUS=BLOCK
```

The Design, Protocol, Cohort Proposal, Strategic Guardrails Review, and this
Pre-Execution Review remain review/proposal documents. Their existence is not
human acceptance or authorization.

## 11. Conditions for a future authorization request

A request for one bounded manual experiment may be prepared only after all
`BLOCK` items above are resolved and independently checked.

Minimum readiness record:

```text
HUMAN_ROLES_CONFIRMED=true
COHORT_DEFINED=true
COHORT_FROZEN=true
CANONICAL_SOURCES_RECORDED=true
EXTERNAL_SERVICE_CLASS_COUNT>=4
NON_REPOSITORY_SERVICE_SURFACE_CONFIRMED=true
SENSITIVE_DATA_BOUNDARY_RECORDED=true
PAIR_ORDER_RECORDED=true
OBSERVATION_WINDOWS_RECORDED=true
EVIDENCE_LOCATION_AUTHORIZED=true
RETENTION_AND_ACCESS_RECORDED=true
STOP_AUTHORITY_RECORDED=true
PRIOR_FAMILIARITY_RECORDED=true
PROTOCOL_DEVIATIONS=NONE_OR_EXPLICITLY_REVIEWED
```

Even if every condition is met:

```text
EXPERIMENT_EXECUTION_AUTHORIZED=false
```

until an explicit Human Decision authorizes the specific run.

## 12. Decision paths

### 12.1 Resolve the existing Protocol requirements

The Human Owner may confirm actual, already-used external services and
complete the remaining Freeze inputs.

This must not introduce a service solely for the experiment.

### 12.2 Revise the Protocol minimum

If the Human Owner decides that two service classes are sufficient, that is a
Protocol change and requires:

1. a separate Human Decision;
2. a new Protocol version;
3. an updated Cohort Proposal;
4. a new Pre-Execution Review.

This document does not recommend or perform that revision.

### 12.3 Stop or defer

If the external-service and role requirements cannot be satisfied without
artificial setup, the correct result is:

```text
DEFER_OR_REDESIGN
```

not simulated service use or silent scope reduction.

## 13. Qwen advisory review

A Qwen advisory pass challenged the effect of GitHub-first, candidate Cohort
fitness, platform/GitHub dependency, centralization, maintenance confounds,
and authorization readiness. Credentials were read only from the
user-designated local environment file; no key value appears here.

The advisory concluded:

- GitHub-first does not formally change the estimand;
- the current proposal cannot yet validly test heterogeneous digital-asset
  understanding, Evidence First, or Human Attention Amplification;
- GitHub-specific object models can be mistaken for general asset-management
  semantics;
- GitHub can become an assumed central source even when external state is
  missing;
- synchronization or adaptation cost could be hidden from total management
  cost;
- the current state is not ready to request or grant experiment
  authorization.

These findings are consistent with the governing documents and are accepted
as advisory input only.

```text
QWEN_ROLE=ADVISORY_ONLY
QWEN_DECISION_AUTHORITY=false
QWEN_EXPERIMENT_AUTHORITY=false
```

## 14. Final pre-execution decision

### 14.1 Review results

| Question | Result |
|---|---|
| Does GitHub-first change the original experiment objective? | `NO` |
| Does it create construct-validity risk? | `YES_HIGH` |
| Does the candidate set support GitHub-hosted asset understanding? | `PARTIAL_PASS` |
| Does it currently support heterogeneous asset understanding? | `BLOCK` |
| Is Evidence First preserved in the design? | `PASS` |
| Is Evidence First execution-ready? | `BLOCK` |
| Is Human Attention Amplification still the intervention? | `PASS` |
| Is an Attention Session ready? | `BLOCK` |
| Does the experiment still target one-person management cost? | `YES` |
| Can the current proposal validly test the full target? | `NO_NOT_YET` |
| Platformization risk | `HIGH_CONTROL_DEFINED` |
| GitHub dependency risk | `HIGH` |
| Centralization risk | `MEDIUM_TO_HIGH_NOT_ACTUALIZED` |
| New maintenance-cost risk | `MATERIAL_AND_MEASURABLE` |
| Ready for Human blocker-resolution review | `YES` |
| Ready to request experiment authorization | `NO` |
| Ready to grant experiment authorization | `NO` |

### 14.2 Final state

```text
ORIGINAL_MISSION_ALIGNMENT=PASS
GITHUB_FIRST_GUARDRAIL_ALIGNMENT=PASS
EXPERIMENT_DESIGN_ALIGNMENT=PASS
EXPERIMENT_PROTOCOL_ALIGNMENT=PASS
CANDIDATE_COHORT_ALIGNMENT=REVISE

PRE_EXECUTION_REVIEW=BLOCK_PENDING_REQUIRED_CONFIRMATIONS
FORMAL_COHORT_FREEZE_READY=false
EXPERIMENT_AUTHORIZATION_READINESS=false
EXPERIMENT_EXECUTION_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
```

### 14.3 Final conclusion

> The GitHub-first strategy has not displaced the original experiment
> objective. It remains a bounded discovery posture, while the experiment
> continues to test whether TITMAS reduces the cost for one human managing a
> heterogeneous software ecosystem.
>
> The current candidate set is not yet sufficient for authorization. Without
> confirmed human roles, a frozen Cohort, at least four actual external
> service classes, one non-repository service surface, source/access/freshness
> boundaries, pairing, Evidence governance, and a separate Human Decision,
> execution would test a narrower GitHub-repository workflow rather than the
> approved objective.

The only authorized next use of this document is Human review and resolution
of the listed blockers. It does not freeze the Cohort, execute the experiment,
modify governance documents, or authorize Implementation.
