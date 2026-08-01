# TITMAS Self-Governance Cohort Proposal v0.1

```text
DOCUMENT_TYPE=SELF_GOVERNANCE_EXPERIMENT_COHORT_PROPOSAL
STATUS=PROPOSAL_ONLY
VERSION=0.1
DATE=2026-07-28

PRIMARY_OBJECTIVE=REDUCE_SINGLE_HUMAN_MANAGEMENT_COST
COHORT_CANDIDATE_MATERIAL_PREPARED=true
COHORT_DEFINED=false
COHORT_FROZEN=false
FORMAL_COHORT_FREEZE_READY=false
EXPERIMENT_EXECUTION_AUTHORIZED=false
EXPERIMENT_EXECUTED=false

CODE_CHANGED=false
DASHBOARD_CREATED=false
API_CREATED=false
ADAPTER_CREATED=false
INTEGRATION_CREATED=false
UNIFIED_DATABASE_CREATED=false
EXTERNAL_SERVICE_REPLACED=false
```

## 0. Purpose and boundary

This document prepares candidate material for a future human Cohort Freeze.
It does not freeze a Cohort and does not authorize a Calibration, Management,
Onboarding, Baseline, or TITMAS Condition Session.

The governing question remains:

> Can TITMAS reduce the cognitive and operational cost for one human who
> manages multiple repositories, programs, Agents, tools, and external
> services?

TITMAS is limited to:

- observing permitted native sources;
- retaining minimal source references;
- presenting source-bound Attention Candidates;
- ranking what may deserve human attention;
- preserving uncertainty, staleness, conflict, and unavailable states.

TITMAS does not own or replace GitHub, Codex, Render, Supabase, Context7,
Linear, Cloudflare, Git, repository worktrees, or any provider account.

## 1. Proposal basis

This proposal is based on:

| Input | SHA-256 |
|---|---|
| `TITMAS_SELF_GOVERNANCE_EXPERIMENT_DESIGN_v0.1.md` | `394876046ce663390ec7956d6a4aff1daeba868fa79730e20adc3f2303cfed3d` |
| `TITMAS_SELF_GOVERNANCE_EXPERIMENT_PROTOCOL_v0.1.md` | `2704cd172f0f23860b93ca0c6dfa0b1b421510bc7e2b143c55137e594aae046f` |
| `TITMAS_OPEN_SOURCE_LEARNING_REVIEW_v0.1.md` | `4de6095ecb3ad7f3f99dbdc8b45a25f5f9e4810acd40fda86d9ba4552da59012` |

The Protocol requires a formally frozen Cohort to contain:

- at least five real repositories;
- at least one Agent-assisted development workflow;
- at least four classes of external services in actual use;
- at least one deployment, data/backend, planning, or domain/security surface.

All seven named external services must be checked. A service not actually used
must be marked `NOT_IN_SCOPE_FOR_COHORT`; it must not be simulated to meet the
minimum.

## 2. Proposal status summary

### 2.1 Candidate posture

```text
REPOSITORY_MINIMUM_CANDIDATE_AVAILABLE=true
AGENT_ASSISTED_WORKFLOW_CANDIDATE_AVAILABLE=true
FOUR_ACTUAL_EXTERNAL_SERVICE_CLASSES_CONFIRMED=false
DEPLOYMENT_DATA_PLANNING_OR_SECURITY_SURFACE_CONFIRMED=false
HUMAN_OPERATOR_CONFIRMED=false
HUMAN_OWNER_MAP_CONFIRMED=false
CANONICAL_SOURCE_ACCESS_CONFIRMED=false
SENSITIVE_DATA_BOUNDARY_CONFIRMED=false

PROPOSAL_RESULT=PREPARED_WITH_BLOCKERS
FORMAL_FREEZE_RECOMMENDATION=BLOCK_UNTIL_REQUIRED_CONFIRMATIONS
```

Five primary Management repositories can be proposed from current local and
Git remote evidence. The external-service minimum cannot yet be honestly
confirmed. GitHub and Codex have direct current-use evidence. Cloudflare has
local configuration evidence, but that does not prove a live, accessible
provider account or deployment source. Render, Supabase, Context7, and Linear
do not currently have verified Cohort-specific use evidence.

The formal freeze must therefore remain blocked unless:

1. at least four external-service classes in actual use are confirmed with
   native canonical sources and permitted access; or
2. a separately reviewed Human Decision revises the Protocol minimum before
   any session begins.

This proposal does neither.

### 2.2 Proposed repository roles

| Role | Proposed objects | Counted toward minimum? |
|---|---|---:|
| Primary Management Cohort candidates | DBA Specification workspace, `agent-evidence`, `agent-health`, `digital-biosphere-os`, `titmas-demo` | 5 candidates |
| Conditional Management reserve | `SAEE`, restricted to approved repository-management surfaces | No |
| Onboarding reserve pool | `pop-persona-pack`, `langchain-pop`, `pop-persona-cockpit`, `titmas-integrations`, `titmas-health`, `digital-biosphere-research-agent-pilot` | No, until Human Freeze |
| Excluded candidate | `agent-evidence-layer` | No |

No Onboarding reserve is assigned to Condition M or T in this proposal.
Assignment, order, time window, and comparability must be frozen later without
examining the target risks.

## 3. Canonical source, owner, and freshness rules

### 3.1 Canonical source is fact-specific

A repository does not have one universal source for every fact:

| Fact | Canonical source |
|---|---|
| Remote repository identity, remote branch, commit, PR, Issue, Actions, release | Native GitHub repository surface |
| Local `HEAD`, branch, uncommitted file state, untracked files | The selected local Git worktree |
| Codex task instructions and task-visible output | The native Codex task and its authorized workspace context |
| Deployment/build/runtime status | Native deployment provider surface |
| Database/auth/backend/storage status | Native Supabase project surface, if actually used and permitted |
| Planning/work-item state | Native Linear item/project surface, if actually used |
| DNS/CDN/security/provider status | Native Cloudflare account/project surface, if actually used and permitted |
| Retrieved documentation context | Native Context7 result plus its underlying cited source |

GitHub is not canonical for uncommitted local changes. A local worktree is not
canonical for GitHub PR, Actions, Issue, release, or provider state.

No copied TITMAS record becomes a new canonical source.

### 3.2 Owner types must remain separate

Every formally frozen object must identify:

| Owner type | Meaning |
|---|---|
| Service Authority Owner | The external service that owns its service state and permission model |
| Source Account Owner | The account or organization shown by the native source |
| Human Operational Owner | The human accountable for managing the object during the experiment |
| Local Worktree Custodian | The human or controlled environment responsible for the selected checkout |
| Reviewer | The human who later adjudicates evidence and calculations |

The GitHub remote namespace `joy7758` is observable as a Source Account Owner.
It must not be silently treated as proof of the Human Operational Owner, the
only contributor, or the Experiment Owner.

Until a human confirms the role map:

```text
SOURCE_ACCOUNT_OWNER=joy7758
HUMAN_OPERATIONAL_OWNER=UNCONFIRMED
EXPERIMENT_OWNER=UNCONFIRMED
OPERATOR=UNCONFIRMED
REVIEWER=UNCONFIRMED
```

### 3.3 Freshness is a source observation, not an age assumption

For every source, a future Freeze Record must include:

- `observed_at`;
- source reference;
- branch or provider object identifier;
- commit or run identifier when available;
- expected update mechanism;
- expected freshness window;
- stale/unavailable behavior;
- access limitation.

For local Git worktrees:

- `git status` is fresh only at the observation time;
- the number of changed paths does not reveal when or why the changes arose;
- a dirty path count must not be treated as activity volume;
- commit time does not timestamp uncommitted changes;
- generated files, long-lived drafts, and active work must not be conflated.

For external services:

- local configuration proves only local configuration;
- documentation mentioning a service proves only documentation;
- a native provider URL and permitted live access are required before the
  service is counted as actually used in the Cohort.

## 4. Primary Management Cohort candidates

Suitability codes:

```text
YES=appropriate candidate subject to formal Freeze
CONDITIONAL=requires the stated boundary or confirmation
NO=should not be used for that session type
```

The local observations below are preparation-time snapshots, not frozen
experimental evidence.

### 4.1 `digital-biosphere-architecture-specification`

| Field | Candidate value |
|---|---|
| Candidate role | Program governance and architecture specification |
| Canonical remote source | `https://github.com/joy7758/digital-biosphere-architecture-specification` |
| Selected local worktree | `/Users/zhangbin/Documents/New project` |
| Relevant project subtree | `/Users/zhangbin/Documents/New project/digital-biosphere-architecture` |
| Observed branch | `codex/production-observability-baseline` |
| Observed `HEAD` | `6cc94b5bca6bcee7e3c6651321915ffb4ad6133f` |
| Observed local status | 67 changed paths at preparation time |
| Source Account Owner | `joy7758` |
| Human Operational Owner | `UNCONFIRMED` |
| Freshness source | Native GitHub branch/PR/Actions plus selected local `git status` and `HEAD` |
| Management Session | `YES` |
| Onboarding Session | `NO` — already central to proposal preparation |

**Why it fits Management**

- It contains the governance material that defines the experiment boundary.
- It spans program, architecture, site, and external-provider concerns.
- Its current dirty state creates realistic source-conflict and freshness
  questions.

**Risks and limitations**

- The relevant project is a subtree of a larger Git worktree; the subtree must
  not be mistaken for a separate repository.
- A separate local repository exists at
  `/Users/zhangbin/GitHub/digital-biosphere-architecture` with remote
  `joy7758/digital-biosphere-architecture`. It is a different Git object and
  must not be double-counted or silently merged with the Specification repo.
- The 67 changed paths may contain unrelated work from the larger worktree.
- Cloudflare-related project files do not prove live Cloudflare service use.
- High prior Operator familiarity may reduce apparent management cost.

**Freeze requirement**

Human review must choose the exact repository object, worktree boundary,
remote branch, permitted source surfaces, and whether unrelated parent
worktree changes are excluded.

### 4.2 `agent-evidence`

| Field | Candidate value |
|---|---|
| Candidate role | Public evidence capture/package/validation/export reference |
| Canonical remote source | `https://github.com/joy7758/agent-evidence` |
| Selected local worktree | `/Users/zhangbin/GitHub/agent-evidence` |
| Observed branch | `revision/softwarex-v2-grounding-fix` |
| Observed `HEAD` | `1b692de391aa04bcfe2666ccc3ddce652ce5c3df` |
| Observed local status | 88 changed paths at preparation time |
| Source Account Owner | `joy7758` |
| Human Operational Owner | `UNCONFIRMED` |
| Freshness source | Native GitHub branch/PR/Actions plus selected local `git status` and `HEAD` |
| Management Session | `YES` |
| Onboarding Session | `NO` — used in prior TITMAS architecture review |

**Why it fits Management**

- It is a real callable project with public claim boundaries and a substantial
  current worktree state.
- It supplies evidence-related management questions without becoming the
  experiment's Truth Owner.
- It provides an Agent-readable repository surface.

**Risks and limitations**

- The dirty path count is high and may mix product, paper, generated,
  documentation, or unrelated work.
- A validator `PASS` cannot be counted as governance approval or truth.
- Existing current-state review creates strong prior familiarity and learning
  effects.
- Private or publication-sensitive materials must not enter session records.

**Freeze requirement**

Select an exact source window and exclude unrelated manuscript, private,
generated, or sensitive paths before any Management pair is defined.

### 4.3 `agent-health`

| Field | Candidate value |
|---|---|
| Candidate role | Local static repository-health diagnosis tool |
| Canonical remote source | `https://github.com/joy7758/agent-health` |
| Selected local worktree | `/Users/zhangbin/GitHub/agent-health` |
| Observed branch | `main` |
| Observed `HEAD` | `6c7937f7b6ad8703922deedaa5ebcde742448320` |
| Observed local status | 50 changed paths at preparation time |
| Observed upstream | `NONE` for the checked-out branch |
| Source Account Owner | `joy7758` |
| Human Operational Owner | `UNCONFIRMED` |
| Freshness source | Native GitHub repository plus selected local `git status`, `HEAD`, and explicit upstream check |
| Management Session | `CONDITIONAL` |
| Onboarding Session | `NO` — extensive prior management exposure |

**Why it may fit Management**

- It directly represents the bounded Agent Health role.
- Missing upstream plus local changes create a real repository-management
  condition.
- Its findings can test whether observation remains separate from execution.

**Risks and limitations**

- No configured upstream for the checked-out branch makes local/remote
  comparison ambiguous.
- The 50 changed paths may represent current work, release preparation,
  generated output, or stale local state.
- The project must remain a repository-health tool, not a TITMAS governance
  system or automatic repair authority.
- Prior release and validation work creates high learning-effect risk.

**Freeze requirement**

Human review must decide whether the intended remote comparison is
`origin/main`, another branch, or local-only. No experiment can infer this
mapping automatically.

### 4.4 `digital-biosphere-os`

| Field | Candidate value |
|---|---|
| Candidate role | DBOS identity/capability/execution/evidence/lifecycle domain |
| Canonical remote source | `https://github.com/joy7758/digital-biosphere-os` |
| Selected local worktree | `/Users/zhangbin/GitHub/digital-biosphere-os` |
| Observed branch | `main` |
| Observed `HEAD` | `0caa2c45e511a82d0dcab778b0ffc3163aac0029` |
| Observed local status | 1 changed path at preparation time |
| Source Account Owner | `joy7758` |
| Human Operational Owner | `UNCONFIRMED` |
| Freshness source | Native GitHub branch/PR/Actions plus selected local `git status` and `HEAD` |
| Management Session | `YES`, as a lower-activity comparator |
| Onboarding Session | `NO` — already part of TITMAS architecture mapping |

**Why it fits Management**

- It represents a distinct constitutional domain from Evidence and Health.
- Its lower local change count can help expose whether a method produces
  unnecessary overhead on quieter repositories.
- It tests whether TITMAS avoids treating DBOS as a universal central runtime.

**Risks and limitations**

- One changed path may produce a floor effect and limited actionable risk.
- Low local change count does not prove low GitHub, Issue, PR, or provider
  activity.
- Interface gaps and authority boundaries must not be interpreted as defects
  that TITMAS is authorized to repair.

**Freeze requirement**

Pair this candidate only with a source window and task of comparable
complexity; do not compare its quiet snapshot directly with a highly dirty
repository and attribute the difference to TITMAS.

### 4.5 `titmas-demo`

| Field | Candidate value |
|---|---|
| Candidate role | Bounded deterministic reference demo |
| Canonical remote source | `https://github.com/joy7758/titmas-demo` |
| Selected local worktree | `/Users/zhangbin/GitHub/titmas-demo` |
| Observed branch | `main` |
| Observed `HEAD` | `7c0470aebe966c72f661394b1a2627b082b90b48` |
| Observed local status | Clean at preparation time |
| Source Account Owner | `joy7758` |
| Human Operational Owner | `UNCONFIRMED` |
| Freshness source | Native GitHub branch/PR/Actions plus selected local `git status` and `HEAD` |
| Management Session | `YES`, limited to calibration or lower-activity comparison |
| Onboarding Session | `NO` — already known to the TITMAS program |

**Why it may fit Management**

- It is a small, bounded reference project and can reveal fixed TITMAS
  preparation overhead.
- It provides contrast with large dirty worktrees.
- Its deterministic-demo boundary is explicit.

**Risks and limitations**

- A clean worktree may have no actionable risk in a selected window.
- A deterministic demo is not production runtime, deployment, or ecosystem
  health proof.
- Using it as a primary performance case could make management appear easier
  than the wider portfolio.

**Freeze requirement**

Use only if the human-defined source window contains a meaningful management
task. Otherwise retain it as Calibration or exclude it before outcomes are
examined.

## 5. Conditional Management reserve

### 5.1 `SAEE`

| Field | Candidate value |
|---|---|
| Candidate role | Protected, bounded evaluation/evolution intelligence |
| Canonical remote source | `https://github.com/joy7758/SAEE` |
| Selected local worktree | `/Users/zhangbin/GitHub/SAEE` |
| Observed branch | `feat/canonical-capability-inventory-routing-v1` |
| Observed `HEAD` | `697ae2080f11b7905b20c39079914eb98169783b` |
| Observed local status | 8 changed paths at preparation time |
| Source Account Owner | `joy7758` |
| Human Operational Owner | `UNCONFIRMED` |
| Freshness source | Native permitted GitHub surfaces plus explicitly approved local repository-management metadata |
| Management Session | `CONDITIONAL` |
| Onboarding Session | `NO` |

**Permitted candidate scope**

Only repository-management facts that the Human Owner explicitly permits:

- repository identity;
- approved branch/commit references;
- permitted GitHub PR/Issue/Actions state;
- local `git status` summary if sensitive paths and content are excluded;
- public or explicitly approved governance documentation.

**Forbidden candidate scope**

- protected algorithms or evaluation core;
- private corpora, credentials, provider configuration, unpublished results,
  or customer/materially sensitive data;
- direct evaluation of raw telemetry;
- SAEE recommendation writeback;
- use of SAEE as Human Authority.

**Risks and limitations**

- Access to the local checkout does not imply permission to include its
  contents in experiment Evidence.
- The repository may expose a different confidentiality and claim boundary
  from the other candidates.
- Its inclusion could shift the experiment from management cost into protected
  capability review.

**Reserve rule**

Do not count `SAEE` toward the five-repository minimum unless the Human Owner
approves an exact safe surface before Cohort Freeze. If approved, record only
references and summaries, never protected content.

## 6. Onboarding Session reserve pool

An Onboarding candidate must remain outside the formal Management Cohort and
must be assigned to only one condition. Proposal preparation has already
exposed the Operator to repository names, remotes, branch names, `HEAD`
identifiers, and dirty path counts. That exposure must be recorded as prior
familiarity; these projects cannot be described as wholly unseen.

### 6.1 Candidate matrix

| Repository | Canonical remote | Owner | Freshness source | Management | Onboarding | Main risk or limitation |
|---|---|---|---|---|---|---|
| `pop-persona-pack` | `joy7758/pop-persona-pack` | Source Account Owner `joy7758`; Human Owner `UNCONFIRMED` | GitHub plus local Git | `NO` if reserved | `YES` | Clean, older `HEAD`; likely floor effect and prior conceptual familiarity |
| `langchain-pop` | `joy7758/langchain-pop` | Source Account Owner `joy7758`; Human Owner `UNCONFIRMED` | GitHub plus local Git | `NO` if reserved | `YES` | Clean, older `HEAD`; integration terminology may be mistaken for active integration |
| `pop-persona-cockpit` | `joy7758/pop-persona-cockpit` | Source Account Owner `joy7758`; Human Owner `UNCONFIRMED` | GitHub plus local Git | `NO` if reserved | `YES` | Name may bias the Operator toward TITMAS Cockpit assumptions; no authority transfer |
| `titmas-integrations` | `joy7758/titmas-integrations` | Source Account Owner `joy7758`; Human Owner `UNCONFIRMED` | GitHub plus local Git | `NO` if reserved | `CONDITIONAL` | Existing overlap with `agent-evidence/integrations`; onboarding could become architecture disposition |
| `titmas-health` | `joy7758/titmas-health` | Source Account Owner `joy7758`; Human Owner `UNCONFIRMED` | GitHub plus local Git | `NO` if reserved | `CONDITIONAL` | Role overlaps `agent-health`; onboarding must not decide ownership or merge projects |
| `digital-biosphere-research-agent-pilot` | `joy7758/digital-biosphere-research-agent-pilot` | Source Account Owner `joy7758`; Human Owner `UNCONFIRMED` | GitHub plus local Git | `NO` if reserved | `CONDITIONAL` | 34 changed paths; higher complexity and possible research/private-material boundary |

### 6.2 Preparation-time observations

| Repository | Observed branch | Observed `HEAD` | Observed local state |
|---|---|---|---|
| `pop-persona-pack` | `main` | `15677cfab2ff1b018edab7460e4e22b5f35d2f28` | clean |
| `langchain-pop` | `main` | `0ee1c4b6f547b0ecf7d5d0078d8b721fb043016d` | clean |
| `pop-persona-cockpit` | `main` | `b51d2fb4db7c6cebc0d07ba34dac0dbc0e8602b9` | clean |
| `titmas-integrations` | `main` | `e8eeccbf19e5e1d1f01ab9ad8796a53591a38dc8` | clean |
| `titmas-health` | `main` | `551810241fbda88fb468bede22bbecbc9c6223cd` | clean |
| `digital-biosphere-research-agent-pilot` | `main` | `3cc08f5cc65025db0db895460813d84bc7ea4bb5` | 34 changed paths |

These observations are not Onboarding Session measurements.

### 6.3 Comparability risks

- Five candidates are clean while one is materially dirty.
- Several POP projects share domain vocabulary and may not be independent.
- `titmas-health` and `titmas-integrations` have known portfolio-overlap
  questions that may dominate onboarding time.
- Older clean `HEAD` timestamps may represent inactivity rather than easy
  onboarding.
- Prior familiarity with TITMAS and POP terminology may shorten onboarding
  without TITMAS intervention.

### 6.4 Pairing recommendation

Before formal Freeze, a human should:

1. select at least four reserve projects;
2. create complexity strata using only pre-outcome facts;
3. assign one project in each comparable pair to Condition M and the other to
   Condition T;
4. freeze assignment and order before examining current risks;
5. ensure no selected project is also in the Management Cohort;
6. record prior familiarity for every selected project;
7. reject a pair when sensitive-data or source-access boundaries differ
   materially.

This proposal does not perform the assignment.

## 7. Excluded repository candidate

### 7.1 `agent-evidence-layer`

| Field | Preparation observation |
|---|---|
| Local path | `/Users/zhangbin/GitHub/agent-evidence-layer` |
| Origin | `NONE` |
| Observed branch | `main` |
| Observed `HEAD` | `e5f3ab67dfc3f0d86c1d83c2fee8d3014a5c6219` |
| Observed local state | 515 changed paths |
| Management Session | `NO` |
| Onboarding Session | `NO` |
| Proposal disposition | `EXCLUDE_PENDING_CANONICAL_SOURCE_AND_OWNER_REVIEW` |

Without a remote canonical source, confirmed Human Owner, and bounded local
state, this checkout would make source verification and freshness
adjudication disproportionate. Exclusion is not a deletion, deprecation, or
project disposition decision.

## 8. Candidate external-service scope

### 8.1 External-service matrix

| Service | Candidate scope | Canonical source | Owner | Freshness source | Management Session | Onboarding Session | Current proposal status |
|---|---|---|---|---|---|---|---|
| GitHub | Repository, branch, commit, PR, Issue, Actions, release references | Native GitHub repository/object page | GitHub owns service state; `joy7758` is observed source account; Human Owner pending | Live native object observed at session time | `YES` | `YES` | `CANDIDATE_IN_SCOPE_ACTUAL_USE_OBSERVED` |
| Codex | Human-authorized coding/task assistance and source-bound result references | Native Codex task plus authorized local workspace result | OpenAI owns service state; Human task owner pending | Current task/thread state and exact local result reference | `YES` | `YES` | `CANDIDATE_IN_SCOPE_ACTUAL_USE_OBSERVED` |
| Cloudflare | Permitted deployment, DNS, CDN, security, or status reference for a selected project | Native Cloudflare account/project/deployment surface | Cloudflare owns service state; account/project owner pending | Live native provider object at session time | `CONDITIONAL` | `CONDITIONAL` | `ACTUAL_SERVICE_USE_AND_ACCESS_UNCONFIRMED` |
| Context7 | Source-attributed documentation retrieval used in the Operator's normal workflow | Native Context7 result plus underlying cited official source | Context7 owns service state; cited publisher owns source content | Retrieval time and cited source version/date | `CONDITIONAL` | `CONDITIONAL` | `COHORT_SPECIFIC_USE_UNCONFIRMED` |
| Render | Permitted deployment/build/runtime status reference | Native Render service/deployment page | Render owns service state; account/service owner pending | Live native deployment/build object | `NO` until verified | `NO` until verified | `NOT_IN_SCOPE_FOR_COHORT_CANDIDATE` |
| Supabase | Permitted project/service status only; never private data/auth records | Native Supabase project/status surface | Supabase owns service state; project owner pending | Live native project/status object | `NO` until verified | `NO` until verified | `NOT_IN_SCOPE_FOR_COHORT_CANDIDATE` |
| Linear | Permitted project/work-item state | Native Linear project/issue page | Linear owns service state; workspace/item owner pending | Live native work item at session time | `NO` until verified | `NO` until verified | `NOT_IN_SCOPE_FOR_COHORT_CANDIDATE` |

### 8.2 GitHub

**Appropriate scope**

- native repository identity;
- exact branch and commit;
- PR, Issue, Actions, and release state;
- native timestamps and direct URLs.

**Risks and limits**

- GitHub does not show uncommitted local worktree state.
- GitHub owner namespace does not prove the Human Operational Owner.
- GitHub Actions `PASS` is scoped to the configured checks and is not release
  or deployment authorization.
- Multiple repositories with similar names must not be conflated.

**Authority**

```text
GITHUB_REMAINS_CANONICAL=true
TITMAS_GITHUB_WRITEBACK=false
TITMAS_SHADOW_LEDGER=false
```

### 8.3 Codex

**Appropriate scope**

- the human-issued task;
- task boundary and explicit authorization;
- source-bound references to inspected or produced local results;
- time spent by Codex and by the human reviewing its output.

**Risks and limits**

- Codex task context is not canonical for GitHub or provider state.
- Agent output is not Human Authority or verified Evidence merely because it
  is well formed.
- Current Cohort preparation creates familiarity that must be disclosed.
- Credentials and private context must not enter session records.

**Authority**

```text
CODEX_REMAINS_EXTERNAL_EXECUTION_ASSISTANCE=true
CODEX_AUTO_AUTHORITY=false
TITMAS_AUTO_DISPATCH_TO_CODEX=false
```

### 8.4 Cloudflare

Local project files currently show a Cloudflare Worker entry point and
Cloudflare build dependencies in the DBA Specification workspace. This proves
only that Cloudflare-related code or tooling is present.

It does not prove:

- a live deployment;
- current account ownership;
- an accessible native status surface;
- that Cloudflare is used by the selected experiment snapshot;
- permission to record DNS, traffic, security, or account details.

Cloudflare may be counted only after Human confirmation of an actual service
object and a permitted native source reference.

### 8.5 Context7

Context7 may enter the Cohort only if the Operator already uses it in the
normal Baseline workflow. It must not be introduced solely to satisfy the
four-service minimum.

A Context7 result remains a retrieval surface. The underlying cited
documentation remains the source for the technical claim.

```text
CONTEXT7_INDEX_COPY=false
CONTEXT7_RESULT_AS_TRUTH=false
CONTEXT7_USE_MUST_BE_PREEXISTING=true
```

### 8.6 Render, Supabase, and Linear

No Cohort-specific actual-use evidence was established during this proposal
preparation. They must remain:

```text
RENDER=NOT_IN_SCOPE_FOR_COHORT_CANDIDATE
SUPABASE=NOT_IN_SCOPE_FOR_COHORT_CANDIDATE
LINEAR=NOT_IN_SCOPE_FOR_COHORT_CANDIDATE
```

This status may change only through later human verification of:

- a real native object;
- actual use by a selected repository/program;
- Human Owner and access boundary;
- permitted source reference;
- expected freshness;
- sensitive-data exclusions.

The proposal does not access, create, or modify provider accounts.

## 9. External-service minimum blocker

The Protocol requires at least four classes of external services in actual
use. Current preparation evidence supports:

| Service | Actual use sufficiently evidenced for proposal? | Can count now? |
|---|---:|---:|
| GitHub | Yes | Candidate `YES` |
| Codex | Yes | Candidate `YES` |
| Cloudflare | Local configuration only | `NO` |
| Context7 | General design reference only | `NO` |
| Render | No Cohort-specific evidence | `NO` |
| Supabase | No Cohort-specific evidence | `NO` |
| Linear | No Cohort-specific evidence | `NO` |

Therefore:

```text
CONFIRMED_EXTERNAL_SERVICE_CLASS_COUNT=2
REQUIRED_EXTERNAL_SERVICE_CLASS_COUNT=4
EXTERNAL_SERVICE_MINIMUM_MET=false
FORMAL_COHORT_FREEZE_READY=false
```

GitHub Actions must not be split from GitHub to inflate the count. Local Git
and the terminal are important observation surfaces but are not external
services. Cloudflare package dependencies must not be counted as an active
Cloudflare account.

If the Human Owner wants a smaller-service experiment, the correct sequence
is:

```text
record current blocker
  -> review the Protocol minimum
    -> issue a new Human-approved Protocol version if justified
      -> prepare a new Cohort Freeze candidate
```

The minimum must not be bypassed inside this proposal.

## 10. Management Session suitability

### 10.1 Proposed use

The five primary candidates cover different management conditions:

| Candidate | Condition represented | Main metric value |
|---|---|---|
| DBA Specification workspace | Program governance, dirty multi-surface workspace | source hops, context switches, status understanding |
| `agent-evidence` | Callable evidence project with high local activity | risk discovery, source verification |
| `agent-health` | Health tool with ambiguous upstream mapping | freshness and canonical-source adjudication |
| `digital-biosphere-os` | Lower-activity constitutional domain | TITMAS preparation overhead and false positives |
| `titmas-demo` | Clean bounded reference project | floor effect, calibration, unnecessary attention |

This diversity is useful for exploratory validity but creates comparability
risk. The formal Freeze must define matched source windows and complexity
notes; repository names alone do not create matched pairs.

### 10.2 Management exclusions

A repository/window should not be used when:

- Human Owner or access permission is unresolved;
- the canonical remote/local mapping is unresolved;
- the session would expose protected or private content;
- there is no meaningful management task inside the review horizon;
- current work belongs to another experiment, publication, release, or
  sensitive program;
- the same risk or snapshot was already used in the other condition;
- the source window changes after outcome inspection.

## 11. Onboarding Session suitability

### 11.1 What onboarding must test

An Onboarding Session must measure the cost of finding:

- project identity and purpose;
- Human Owner or `NOT_ASSIGNED`;
- canonical repository/source;
- current branch/version/snapshot;
- callable or management-relevant surfaces;
- external services actually used;
- freshness and access limitations;
- claim and sensitive-data boundaries.

It must not install, integrate, refactor, or normalize the project.

### 11.2 Candidate quality

The reserve pool is usable only after comparability review:

- clean POP-family repositories may form low-complexity candidates;
- `titmas-integrations` and `titmas-health` may expose duplication and owner
  ambiguity but must not trigger a disposition decision;
- `digital-biosphere-research-agent-pilot` may provide a higher-complexity
  candidate but requires a research-data boundary;
- no candidate is fully “unseen” after this preparation pass.

The formal Freeze must record this familiarity rather than pretending it did
not occur.

## 12. Selection bias and confounding risks

| Risk | Why material | Required control before Freeze |
|---|---|---|
| Single-account bias | Most remotes use `joy7758`; results may not generalize to organizational ownership | Limit claim to this portfolio and confirm actual Human Owner |
| Prior-familiarity bias | The Operator has repeatedly worked with TITMAS core repositories | Record familiarity and balance matched pairs |
| Dirty-state heterogeneity | Candidate dirty counts range from 0 to 88 | Match source-window complexity; do not treat count as workload |
| Related-project dependence | Repositories share governance, terminology, and owner | Do not claim repository observations are independent samples |
| Floor effect | Clean or quiet repositories may show little management work | Use for calibration/lower-activity comparison, not only headline result |
| Protected-source asymmetry | SAEE and research projects may have stricter access boundaries | Exclude or create an exact safe surface before Freeze |
| Duplicate-checkout ambiguity | Similar DBA names and multiple local checkouts can be confused | Freeze exact remote, worktree, branch, and `HEAD` |
| Tool-introduction bias | Adding a service solely for the experiment changes Baseline | Only include tools already in normal use |
| Attention-preparation leakage | Preparation may reveal risks before a session | Use non-overlapping future source windows and record exposure |
| Hidden collaborator/Agent activity | One-person assumption may be false if other actors manage state | Confirm contributors and concurrent activity for each source window |

## 13. Candidate sensitive-data boundary

The following must not enter the Cohort record:

- API keys, tokens, passwords, session cookies, private keys, or `.env`
  contents;
- Supabase private data, auth records, or storage content;
- Cloudflare secrets or restricted DNS/security configuration;
- private repository contents not expressly approved;
- SAEE protected core, private corpora, or unpublished evaluation data;
- private customer, payment, identity, health, or research-participant data;
- full external-service exports when a minimal source reference is sufficient.

This proposal records no secret values.

## 14. Minimal human confirmation checklist

Before a formal Cohort Freeze, the Human Experiment Owner and Operator must
confirm:

### 14.1 Roles

- [ ] Experiment Owner identity.
- [ ] Operator identity.
- [ ] Reviewer identity and independence status.
- [ ] Whether the Experiment Owner and Operator are the same person.
- [ ] Human Operational Owner for every selected repository.
- [ ] Concurrent human or Agent contributors during each source window.

### 14.2 Repository scope

- [ ] Exactly five or more Management repositories.
- [ ] Exact remote URL, local worktree, branch, and starting `HEAD`.
- [ ] Local/remote mapping for dirty worktrees.
- [ ] Resolution of `agent-health` upstream ambiguity.
- [ ] Resolution of the two DBA repository identities.
- [ ] Approved SAEE safe surface, or explicit exclusion.
- [ ] Excluded paths, generated output, manuscripts, and sensitive material.

### 14.3 External services

- [ ] GitHub native source access.
- [ ] Codex normal-use boundary and timing method.
- [ ] Whether a real Cloudflare service object is in current use.
- [ ] Whether Context7 is already part of normal Operator practice.
- [ ] Whether Render, Supabase, or Linear has an actual Cohort-specific object.
- [ ] At least four actually used service classes, or a separately approved
      Protocol revision.
- [ ] Native URL/reference, Source Owner, freshness, and access boundary for
      every counted service.

### 14.4 Onboarding

- [ ] At least four reserve projects selected.
- [ ] Projects remain outside the Management Cohort.
- [ ] Complexity strata and pairing rationale.
- [ ] Condition M/T assignment frozen before risk inspection.
- [ ] Prior familiarity recorded.
- [ ] Sensitive-data and source-access comparability.

### 14.5 Experiment governance

- [ ] Observation windows.
- [ ] Review horizon.
- [ ] Session timebox.
- [ ] Condition order.
- [ ] Stop authority.
- [ ] Existing authorized Evidence location and retention rule.
- [ ] Separate Human authorization to execute, if ever granted.

## 15. Qwen advisory review

A Qwen advisory pass reviewed selection bias, Management/Onboarding fit,
canonical-source errors, owner ambiguity, and the external-service minimum.
Credentials were read only from the user-designated local environment file;
no key value is included here.

The advisory correctly highlighted:

- repository complexity and dirty-state heterogeneity can confound results;
- a GitHub account owner is not automatically the Human Operational Owner;
- local Cloudflare configuration is not the provider's canonical service
  state;
- dirty path counts do not reveal work age or management cost;
- `agent-health` upstream ambiguity requires human resolution;
- clean Onboarding candidates can create floor effects.

The advisory suggested treating fewer than four confirmed external services as
a limitation rather than a blocker. This proposal does not adopt that
suggestion because the current Protocol explicitly defines at least four
actually used external-service classes as a minimum. Only a separate Human
Decision and Protocol revision can change that rule.

```text
QWEN_ROLE=ADVISORY_ONLY
QWEN_AUTHORITY=false
QWEN_FREEZE_AUTHORITY=false
QWEN_PROTOCOL_OVERRIDE=false
```

## 16. Final proposal decision

### 16.1 Candidate repository conclusion

Five primary Management repositories are available as candidates:

1. `digital-biosphere-architecture-specification`;
2. `agent-evidence`;
3. `agent-health`;
4. `digital-biosphere-os`;
5. `titmas-demo`.

`SAEE` remains a conditional reserve. Six repositories remain in the
Onboarding reserve pool. `agent-evidence-layer` is excluded pending canonical
source and owner resolution.

### 16.2 External-service conclusion

GitHub and Codex are supported as actual-use candidates. Cloudflare and
Context7 require human confirmation. Render, Supabase, and Linear remain
`NOT_IN_SCOPE_FOR_COHORT_CANDIDATE` on current evidence.

### 16.3 Freeze readiness

```text
COHORT_PROPOSAL_COMPLETE=true
REPOSITORY_CANDIDATE_SET_AVAILABLE=true
ONBOARDING_RESERVE_AVAILABLE=true

OWNER_CONFIRMATION_REQUIRED=true
CANONICAL_SOURCE_ACCESS_CONFIRMATION_REQUIRED=true
EXTERNAL_SERVICE_MINIMUM_CONFIRMATION_REQUIRED=true
PAIRING_AND_ORDER_FREEZE_REQUIRED=true
SENSITIVE_DATA_BOUNDARY_CONFIRMATION_REQUIRED=true

COHORT_FROZEN=false
FORMAL_COHORT_FREEZE_READY=false
EXPERIMENT_EXECUTION_AUTHORIZED=false
```

The only authorized next action from this document is Human Review of the
candidate material. It does not authorize Cohort Freeze, experiment execution,
integration, implementation, writeback, or replacement of any external
service.
