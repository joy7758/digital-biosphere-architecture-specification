# TITMAS Strategic Guardrails Review v0.1

```text
DOCUMENT_TYPE=STRATEGIC_GUARDRAILS_REVIEW
STATUS=REVIEW_ONLY
VERSION=0.1
DATE=2026-07-28

STRATEGY_UNDER_REVIEW=GITHUB_FIRST_DISCOVERY
STRATEGIC_ALIGNMENT=PASS_WITH_REQUIRED_GUARDRAILS
GITHUB_FIRST_NE_GITHUB_ONLY=true
DISCOVERY_NE_TRUST=true
DISCOVERY_NE_AUTHORITY=true
DISCOVERY_NE_PERMISSION=true

DIGITAL_BIOSPHERE_CONSTITUTION_CHANGED=false
TITMAS_CONSTITUTION_CHANGED=false
EXISTING_CONSTITUTION_FILE_CHANGED=false
CODE_CREATED=false
COMPONENT_CREATED=false
API_CREATED=false
DASHBOARD_CREATED=false
IMPLEMENTATION_AUTHORIZED=false
```

## 0. Executive decision

`GitHub-first Discovery Strategy` is compatible with the current TITMAS
constitutional and governance direction only when it means:

> For the first bounded phase, begin discovery of GitHub-hosted software
> assets at their existing GitHub-native surfaces, then help a human
> understand source-bound relationships, limitations, and decision needs
> without replacing GitHub or any other canonical service.

It must not mean:

- GitHub is the universal entry for every digital asset;
- GitHub presence proves quality, trust, ownership, adoption, or permission;
- TITMAS must build a GitHub replacement, registry, search engine, catalog,
  profile platform, or integration hub;
- non-GitHub assets must be copied into GitHub;
- every user must pass through a TITMAS-controlled GitHub experience;
- GitHub ranking, stars, forks, topics, search order, or activity become
  TITMAS governance scores.

Decision:

```text
GITHUB_FIRST_AS_PHASE_1_DISCOVERY_HEURISTIC=PASS
GITHUB_FIRST_AS_CONSTITUTIONAL_PRINCIPLE=BLOCK
GITHUB_AS_UNIVERSAL_ECOSYSTEM_ENTRY=BLOCK
GITHUB_AS_TITMAS_TRUTH_SOURCE=BLOCK
TITMAS_AS_GITHUB_COMPETITOR=BLOCK
TITMAS_AS_MANDATORY_GATEWAY=BLOCK
```

This strategy is a reversible, provider-specific project posture. It is not a
new architecture layer, product, component, or implementation authorization.

## 1. Review basis

This review preserves the boundaries established by:

| Input | SHA-256 |
|---|---|
| `TITMAS_CONSTITUTION_REVISION_PROPOSAL_v1.1.md` | `dcc98d803e9e46f85ad5df69a6780072dedfe07acd7f7f13c546d9ba7629976e` |
| `TITMAS_INTERFACE_BOUNDARY_MAP_v0.1.md` | `241899a8a75b38471c827db8321e64f91dc2def04880f41dc9ddbdfdafe751be` |
| `TITMAS_GOVERNANCE_CONSISTENCY_REVIEW_v0.1.md` | `0ff1a815ea8d0b32ae9e66546b97f3dd72be34f557c1cd16bbbec52bc1e35c29` |
| `TITMAS_SELF_GOVERNANCE_EXPERIMENT_DESIGN_v0.1.md` | `394876046ce663390ec7956d6a4aff1daeba868fa79730e20adc3f2303cfed3d` |
| `TITMAS_OPEN_SOURCE_LEARNING_REVIEW_v0.1.md` | `4de6095ecb3ad7f3f99dbdc8b45a25f5f9e4810acd40fda86d9ba4552da59012` |
| `TITMAS_SELF_GOVERNANCE_COHORT_PROPOSAL_v0.1.md` | `88edd47590c2550787a6aba822d364ebd6418cb13821f87da7f155b2fab30ed7` |

The prior Strategic Alignment Review was delivered as a read-only chat
artifact because its phase explicitly prohibited file creation. Its governing
conclusion is used here only as an analysis premise:

```text
A_AS_HUMAN_ACCESSIBILITY_AND_UNDERSTANDING_OUTCOME=ACCEPT
B_AS_DISTRIBUTED_ASSURANCE_SUPPORT=ACCEPT
A_OR_B_AS_NEW_ARCHITECTURE_LAYER=REJECT
```

### 1.1 GitHub-native discovery facts

GitHub's official documentation describes:

- repositories as native containers for code, files, revision history, and
  project collaboration;
- repository, topic, people, organization, Explore, and search surfaces for
  project discovery;
- topics as repository classification and discovery metadata;
- releases as repository-native references to tagged software and assets;
- the dependency graph as a summary derived from repository manifests,
  lockfiles, and submitted dependency information.

Official references:

- [GitHub repositories documentation](https://docs.github.com/en/repositories)
- [Discovering projects on GitHub](https://docs.github.com/en/get-started/exploring-projects-on-github/discovering-projects-on-github)
- [Classifying repositories with topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
- [About releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
- [Dependency graph](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependency-graph)

These capabilities support using GitHub as the initial discovery surface for
GitHub-hosted software assets. They do not make GitHub canonical for external
deployment, database, planning, documentation, Agent-task, DNS, or security
state.

## 2. Definition of GitHub-first Discovery Strategy

### 2.1 Positive definition

`GitHub-first` means:

1. Phase 1 is bounded primarily to software assets already hosted or
   represented on GitHub.
2. Discovery begins with the repository's native owner/name identity and
   source-controlled, repository-native materials.
3. Native GitHub references are preserved for repository, commit, branch, PR,
   Issue, Actions, release, topic, and dependency-graph observations.
4. TITMAS may help a human navigate from a discovered GitHub asset to its
   permitted external canonical sources.
5. TITMAS may present source-bound understanding and Attention Candidates.
6. The strategy can be removed or supplemented without changing child
   repository or external-service operation.

### 2.2 Negative definition

`GitHub-first` does not mean:

```text
GITHUB_ONLY=false
GITHUB_REQUIRED_FOR_ALL_ASSETS=false
GITHUB_AUTH_REQUIRED_FOR_ALL_USERS=false
GITHUB_SEARCH_AS_COMPLETE_INVENTORY=false
GITHUB_METADATA_AS_TRUST_SCORE=false
GITHUB_ACTIVITY_AS_PROJECT_HEALTH=false
GITHUB_POPULARITY_AS_AUTHORITY=false
GITHUB_AS_CROSS_SERVICE_CANONICAL_SOURCE=false
```

### 2.3 Phase boundary

The strategy applies only to the first bounded discovery phase for
GitHub-hosted software assets.

It does not establish a general claim about:

- all digital assets;
- private enterprise systems;
- non-software assets;
- local-only repositories;
- GitLab, Bitbucket, cloud-provider, package-registry, model-hub, document,
  database, domain, or planning ecosystems;
- assets for which the user has no access or management authority.

```text
PHASE_1_SCOPE=GITHUB_HOSTED_SOFTWARE_ASSET_DISCOVERY
GENERAL_DIGITAL_ASSET_COVERAGE_CLAIM=false
UNIVERSAL_DISCOVERY_CLAIM=false
```

## 3. Constitutional alignment review

### 3.1 Ecological Self-Limitation

Status: `PASS_WITH_GUARDRAILS`

The strategy is consistent with Ecological Self-Limitation because it reuses
an existing autonomous ecosystem entry instead of building a competing
central entry.

Alignment requires:

- GitHub remains independently usable;
- TITMAS remains independently removable;
- non-GitHub services retain their own entry and canonical state;
- the discovery provider can be substituted or supplemented;
- no single search, catalog, identity, or permission center is created;
- a failure in GitHub discovery does not rewrite other source facts.

Required invariants:

```text
REUSE_EXISTING_ENTRY_NE_CONTROL_EXISTING_ENTRY=true
DISCOVERY_COVERAGE_NE_ECOSYSTEM_OWNERSHIP=true
PROVIDER_FIRST_NE_PROVIDER_LOCK_IN=true
COORDINATION_NE_MANDATORY_CENTER=true
```

Violation occurs if:

- TITMAS requires every asset to be mirrored into GitHub;
- all external tools must register with TITMAS through GitHub;
- GitHub identity becomes the only accepted Agent or human identity;
- GitHub unavailability makes non-GitHub assets undiscoverable by policy;
- the Phase 1 heuristic becomes a permanent constitutional dependency.

### 3.2 Evidence First

Status: `PASS_WITH_NON_ELEVATION`

GitHub discovery produces an observation or source reference. It does not by
itself produce Evidence, Truth, verification, trust, or adoption.

Examples:

| GitHub observation | What it may support | What it cannot establish |
|---|---|---|
| Repository exists | A source reference at an observed time | Owner identity beyond the account, quality, safety |
| Topic is present | Self-described or admin-selected classification | TITMAS compatibility, certification |
| Search result appears | Navigation to a candidate source | Completeness, objective relevance |
| Star/fork count | Platform activity observation | Trust, fitness, authority |
| Commit exists | Versioned source event | Correctness, deployment, human approval |
| Actions check passes | Configured check result | Release approval, production readiness |
| Release exists | Native GitHub release state and assets | External adoption, DOI, deployment |
| Dependency graph shows an edge | GitHub-derived dependency observation | Complete runtime dependency truth |

Required invariants:

```text
DISCOVERY_RESULT=OBSERVATION_MATERIAL
DISCOVERY_NE_EVIDENCE_ADMISSION=true
REPOSITORY_PRESENCE_NE_TRUST=true
TOPIC_NE_CONFORMANCE=true
POPULARITY_NE_QUALITY=true
SEARCH_RANK_NE_ATTENTION_AUTHORITY=true
```

TITMAS must preserve:

- source;
- observed time;
- source object identifier;
- scope;
- freshness;
- access limitation;
- uncertainty;
- conflicting native sources.

### 3.3 Authority Separation

Status: `PASS_WITH_EXPLICIT_ROLE_LIMIT`

GitHub discovery belongs only to the Observation and navigation part of the
governance cycle.

```text
GitHub-native discovery
  -> source-bound observation
    -> optional Evidence/Health/Evaluation process
      -> Human Decision
        -> separately authorized execution
```

GitHub discovery must not:

- authorize Codex;
- grant repository or provider Permission;
- select an Agent for execution;
- approve a merge, release, deployment, or external action;
- automatically submit an object to DBOS;
- trigger SAEE evaluation;
- change Attention priority without explainable, contestable human review;
- close a Human Authority gate.

Required invariants:

```text
DISCOVERY_NE_EVALUATION=true
DISCOVERY_NE_AUTHORIZATION=true
DISCOVERY_NE_EXECUTION=true
GITHUB_PERMISSION_NE_TITMAS_PERMISSION=true
GITHUB_RESULT_NE_HUMAN_DECISION=true
```

### 3.4 No Duplicate Component Principle

Status: `PASS_ONLY_IF_NO_REBUILD`

GitHub already provides repository hosting, search, topics, code navigation,
Issues, PRs, Actions, releases, and related repository surfaces. The strategy
is constitutionally acceptable only if TITMAS does not duplicate them.

Explicitly prohibited:

- TITMAS repository hosting;
- a second GitHub profile or repository homepage system;
- a second repository search engine or code index;
- a universal asset registry;
- duplicate Issue, PR, CI, release, or notification systems;
- a copied GitHub activity database;
- a GitHub metadata normalization service;
- a GitHub permission proxy;
- a GitHub-specific mandatory Adapter layer;
- a ranking system derived from stars, forks, activity, or topics.

```text
GITHUB_FUNCTION_DUPLICATION=BLOCK
GITHUB_SHADOW_DATABASE=BLOCK
GITHUB_SEARCH_REBUILD=BLOCK
GITHUB_PERMISSION_PROXY=BLOCK
```

## 4. Entry-competition review

### 4.1 Competition posture

TITMAS should meet users where their software assets already exist. It should
not compete to become the place where those assets must be created, hosted,
searched, released, deployed, or permitted.

```text
TITMAS_COMPETES_ON_HOSTING=false
TITMAS_COMPETES_ON_CODE_SEARCH=false
TITMAS_COMPETES_ON_IDENTITY=false
TITMAS_COMPETES_ON_DEPLOYMENT=false
TITMAS_COMPETES_ON_PERMISSION=false
TITMAS_VALUE=SOURCE_BOUND_UNDERSTANDING_AND_ASSURANCE_SUPPORT
```

### 4.2 Risk register

| Risk | Severity | Failure mode | Required guardrail |
|---|---|---|---|
| Mandatory gateway | Critical | All users and assets must enter through TITMAS | Native services remain directly usable |
| Shadow GitHub | Critical | TITMAS copies repository, Issue, PR, CI, or release state | Store only minimal source references |
| GitHub as universal Truth | Critical | GitHub state overrides deployment, database, domain, or planning sources | Fact-specific canonical-source map |
| Permission aggregation | Critical | GitHub login or token becomes universal TITMAS permission | Provider permissions remain separate |
| Popularity as trust | High | Stars/forks/activity determine assurance or priority | Treat counts only as scoped observations |
| Search-ranking authority | High | GitHub search order determines what TITMAS shows | Explain source, allow direct query and override |
| GitHub-only lock-in | High | Non-GitHub discovery is indefinitely excluded | Phase scope and exit conditions remain explicit |
| Asset mirroring | High | Non-GitHub objects are copied into GitHub for visibility | Link to native source; do not relocate state |
| Private-source leakage | Critical | Private repo metadata or content enters public discovery | Preserve access boundary; no public copying |
| API coupling | Medium | GitHub API changes become TITMAS operational failure | Strategy remains reference-oriented and replaceable |
| Identity conflation | High | GitHub account is treated as verified human/Agent identity | Keep Source Account Owner separate from Human Owner |
| Maintenance inversion | High | GitHub coordination costs more than manual navigation | Count preparation and reconciliation overhead |
| Portfolio bias | Medium | GitHub-heavy cohort is claimed to represent all ecosystems | Restrict every conclusion to the frozen cohort |

### 4.3 De facto lock-in

Even a non-exclusive written strategy can become GitHub-only through:

- all examples using GitHub;
- every source reference assuming GitHub identifiers;
- non-GitHub assets being permanently deferred;
- ranking logic inheriting GitHub fields;
- governance language treating “repository” as “all digital assets”;
- test evidence covering only GitHub while claims remain universal.

Therefore the strategy must retain:

```text
GITHUB_FIRST_SCOPE_EXPIRY_REVIEW_REQUIRED=true
NON_GITHUB_ASSET_NON_CLAIM_REQUIRED=true
PROVIDER_NEUTRAL_CONSTITUTION_REMAINS=true
```

This review does not define a delivery date or roadmap for other providers.
It only prevents Phase 1 evidence from being generalized beyond its scope.

## 5. Safe definition of the four strategic terms

These terms describe roles or outcomes. They are not new architecture layers.

### 5.1 User entry（用户入口）

Definition:

> The native surface where a user already begins a legitimate task.

Examples may include:

- a GitHub repository, Issue, PR, Actions run, or release;
- a Codex task;
- a Render deployment;
- a Supabase project;
- a Linear work item;
- a Cloudflare project or permitted status surface;
- a Context7 retrieval result and its cited source;
- a local Git worktree.

The user entry is not owned by TITMAS.

```text
USER_ENTRY_NE_TITMAS_PORTAL=true
USER_ENTRY_NE_SINGLE_UI=true
USER_ENTRY_NE_UNIVERSAL_LOGIN=true
```

TITMAS may help the user understand the current task from that entry. It must
not require the user to abandon or duplicate the native workflow.

### 5.2 Ecosystem entry（生态入口）

Definition:

> A provider- or domain-native place where an asset is created, maintained,
> published, discovered, or referenced.

GitHub is an ecosystem entry for GitHub-hosted software assets. It is not the
ecosystem entry for:

- Render deployment truth;
- Supabase data/auth/backend truth;
- Linear planning truth;
- Cloudflare DNS/CDN/security truth;
- Codex task authorization;
- Context7's cited external documentation;
- non-GitHub repositories or local-only assets.

```text
ECOSYSTEM_ENTRY_IS_PLURAL=true
ECOSYSTEM_ENTRY_REMAINS_PROVIDER_NATIVE=true
TITMAS_UNIVERSAL_ENTRY=false
```

No new standardized ingestion point, Adapter, gateway, or provider-neutral
database is created by this definition.

### 5.3 Understanding function（理解能力）

Safer term:

```text
PREFERRED_TERM=SOURCE_BOUND_UNDERSTANDING_FUNCTION
AVOID_TERM=UNIFIED_UNDERSTANDING_LAYER
```

Definition:

> A bounded ability to help a human identify what an observed object is,
> where its canonical source is, how fresh and limited the observation is,
> how it relates to a current task, and what decision—if any—is required.

It may produce:

- direct source navigation;
- owner and scope clarification;
- freshness and uncertainty disclosure;
- relationship explanation;
- a bounded Attention Candidate;
- a record that more evidence is needed.

It may not produce:

- a universal ontology;
- a new asset identity system;
- a copied source database;
- automatic semantic Truth;
- automatic asset classification with authority;
- a decision or command.

```text
UNDERSTANDING_NE_TRUTH=true
RELATIONSHIP_NE_CANONICAL_OWNERSHIP=true
EXPLANATION_NE_DECISION=true
```

### 5.4 Trustworthy support function（可信支撑能力）

Safer term:

```text
PREFERRED_TERM=DISTRIBUTED_EVIDENCE_BACKED_ASSURANCE_SUPPORT
AVOID_TERM=CENTRAL_TRUST_LAYER
```

Definition:

> The bounded, distributed support provided by source preservation, Agent
> Evidence, Agent Health, applicable DBOS admission/verification, protected
> SAEE evaluation, and Human Authority under their existing responsibilities.

It is not a new component or monolithic backend.

```text
ASSURANCE_SUPPORT_IS_DISTRIBUTED=true
ASSURANCE_SUPPORT_NE_CERTIFICATION=true
ASSURANCE_SUPPORT_NE_PERMISSION=true
ASSURANCE_SUPPORT_NE_AUTOMATIC_DECISION=true
```

The component boundaries remain:

| Existing boundary | Contribution | Does not become |
|---|---|---|
| Native source | Own service/domain fact | Universal Truth |
| Agent Evidence | Capture/package/validate candidate | DBOS admission, governance |
| Agent Health | Scoped repository diagnosis | Runtime controller |
| DBOS | Applicable canonical domain boundary | Universal asset registry |
| SAEE | Protected bounded evaluation/recommendation | Command or writeback |
| Human Authority | Explicit scoped decision | Automatic execution |
| DBA Cockpit TITMAS Situational View | Reference-only projection | Truth store or control plane |

## 6. Canonical-source guardrail

GitHub-first discovery must retain fact-specific authority:

| Fact | Canonical source |
|---|---|
| GitHub repository, commit, branch, PR, Issue, Actions, GitHub release | Native GitHub object |
| Uncommitted local state | Selected local Git worktree |
| Codex task and explicit task authorization | Native Codex task and human instruction |
| Render build/deployment/runtime state | Native Render service |
| Supabase project/data/auth/backend state | Native Supabase project |
| Linear planning/work-item state | Native Linear workspace/item |
| Cloudflare DNS/CDN/security/service state | Native Cloudflare account/project |
| Context7 retrieval | Native retrieval result plus underlying cited source |
| Applicable DBOS record | Applicable DBOS Owner/process |
| SAEE evaluation | Approved scoped SAEE evaluation artifact |
| Human authorization | Explicit Human Decision record |

TITMAS may retain a minimal reference to these sources. It must not copy them
into a universal asset record and then claim that the copy is canonical.

## 7. Strategic guardrails

### `SG-01` — Phase-limited scope

GitHub-first applies only to Phase 1 discovery of GitHub-hosted software
assets.

### `SG-02` — GitHub-first, not GitHub-only

Non-GitHub assets remain valid and retain their native ecosystem entries.

### `SG-03` — Native entry remains usable

No GitHub or external-service workflow may require TITMAS to function.

### `SG-04` — No entrance competition

TITMAS does not compete for hosting, search, collaboration, CI, release,
deployment, database, documentation, identity, or account ownership.

### `SG-05` — Discovery is Observation

A discovered object is an observation candidate, not admitted Evidence,
Trust, Permission, or a decision.

### `SG-06` — Popularity is not Trust

Stars, forks, followers, contributors, topics, activity, and search order do
not become Trust, Health, Authority, or Attention scores.

### `SG-07` — No duplicated discovery infrastructure

Do not create a new repository search engine, code index, registry, catalog,
GitHub mirror, or universal asset inventory.

### `SG-08` — No shadow state

Do not copy GitHub or external-provider state into a new TITMAS database,
ledger, or synchronized status store.

### `SG-09` — Fact-specific canonical source

Every displayed fact must return to the service that owns that fact.

### `SG-10` — Source and freshness visible

Every Attention Candidate must preserve source, observed time, scope,
freshness, limitations, and uncertainty.

### `SG-11` — No permission aggregation

TITMAS does not create universal login, token custody, account proxy, or
cross-provider Permission.

### `SG-12` — No automatic writeback

Discovery and understanding do not modify repository, Issue, PR, release,
deployment, database, work item, domain, Agent, or provider state.

### `SG-13` — Human Authority remains explicit

Discovery, ranking, Evidence, Health, and Evaluation do not authorize action.

### `SG-14` — Attention remains contestable

Humans can inspect the source, reject the ranking, expose omitted candidates,
and record unknown or conflicted states.

### `SG-15` — Private boundaries remain private

Private repository or provider information must not be copied into public
discovery or review materials.

### `SG-16` — No mandatory provider identity

GitHub identity is not automatically a DBOS identity, verified human identity,
Agent identity, or universal asset owner.

### `SG-17` — Deletability

The GitHub-first discovery posture must be removable without changing child
repositories or external-service operation.

### `SG-18` — Failure remains local

GitHub search, API, or availability failure becomes an explicit unavailable
source. It must not overwrite or invalidate non-GitHub facts.

### `SG-19` — Maintenance cost is counted

Time spent reconciling GitHub references, stale state, provider differences,
or Attention preparation counts as TITMAS overhead.

### `SG-20` — Claims remain cohort-bound

Evidence from GitHub-heavy repositories does not prove value for all digital
assets, providers, organizations, or users.

## 8. Prohibited strategic anti-patterns

| Anti-pattern | Status | Reason |
|---|---|---|
| “TITMAS is the home of all digital assets” | `BLOCK` | Creates universal entry and ownership implication |
| “Connect GitHub once and TITMAS governs everything” | `BLOCK` | Permission and authority aggregation |
| GitHub stars/forks as Trust score | `BLOCK` | Popularity is not assurance |
| Topic presence as TITMAS conformance | `BLOCK` | Self-description is not validation |
| Search result order as Attention priority | `BLOCK` | Inherits opaque ranking authority |
| Mirror non-GitHub assets into GitHub | `BLOCK` | Replaces native sources |
| Copy GitHub state into a TITMAS database | `BLOCK` | Creates shadow truth and synchronization burden |
| TITMAS-specific mandatory repository metadata | `BLOCK` | Creates entry tax and compatibility gate |
| GitHub account as universal Agent identity | `BLOCK` | Violates DBOS and POP boundaries |
| Automatic execution from GitHub discovery | `BLOCK` | Violates Authority Separation |
| A new GitHub Adapter project | `BLOCK` | New component and duplicated integration burden |
| A TITMAS discovery Dashboard | `BLOCK` | Current phase forbids Dashboard and second Cockpit |
| “GitHub-first proves general accessibility” | `BLOCK` | Evidence exceeds Phase 1 scope |

## 9. Relationship to the Self-Governance Experiment

The current experiment already measures the relevant strategic hypothesis:

- management time;
- source hops;
- context switches;
- risk discovery time;
- project-status understanding;
- onboarding cost;
- false positives and false negatives;
- Cognitive Overhead Ratio;
- Attention preparation and maintenance burden.

GitHub-first must not change the experiment by:

- counting GitHub repository, Issues, PRs, and Actions as separate external
  service classes;
- introducing GitHub tools that were not already part of the normal Baseline;
- treating GitHub-only source windows as representative of all services;
- excluding external canonical checks to make the TITMAS condition faster;
- using GitHub activity as the reference risk set;
- freezing a Cohort merely because five GitHub repositories are available.

The Cohort Proposal currently confirms GitHub and Codex use candidates but
does not yet confirm the required four external-service classes. GitHub-first
does not remove that blocker.

```text
SELF_GOVERNANCE_EXPERIMENT_CHANGE_REQUIRED=false
EXTERNAL_SERVICE_MINIMUM_BYPASSED=false
GITHUB_SURFACES_COUNTED_AS_ONE_SERVICE_CLASS=true
```

## 10. Need for a project-level strategic guardrail document

Decision: `YES_AS_PROJECT_POLICY_CANDIDATE`

A project-level guardrail is justified because GitHub-first is:

- provider-specific;
- reversible;
- Phase-limited;
- below constitutional level;
- likely to drift into a mandatory gateway without explicit constraints;
- relevant to project positioning and future evaluation.

It should not be added to the Digital Biosphere Constitution or TITMAS
Constitution because those documents must remain provider-neutral.

However, a second parallel document is not currently necessary.

This review already contains:

- the strategy definition;
- constitutional checks;
- safe terminology;
- guardrails;
- anti-patterns;
- experiment relationship;
- adoption decision requirements.

Recommended governance disposition:

```text
THIS_REVIEW_ROLE=PROJECT_LEVEL_GUARDRAIL_CANDIDATE
SEPARATE_SECOND_GUARDRAIL_FILE_REQUIRED=false
GUARDRAIL_ADOPTED=false
HUMAN_DECISION_REQUIRED=true
```

A Human Decision may later choose:

```text
ACCEPT
REVISE
REJECT
DEFER
```

Acceptance of the strategic guardrail would not authorize implementation,
integration, API use, metadata changes, repository changes, or public claims.

## 11. Qwen advisory review

A Qwen advisory pass reviewed constitutional alignment, platform lock-in,
hidden authority, terminology, and whether a separate guardrail file is
needed. Credentials were read only from the user-designated local environment
file; no key value appears in this document.

Accepted advisory findings:

- Phase 1 resource concentration can create de facto GitHub-only lock-in even
  when the written strategy is non-exclusive;
- GitHub search, topic, recommendation, and popularity mechanisms can become
  hidden evaluation or Attention authority;
- a provider-specific strategy needs explicit exit and anti-pattern rules;
- a second parallel guardrail file would increase authority and maintenance
  ambiguity.

Rejected or narrowed advisory suggestions:

- no new abstract user-entry layer;
- no standardized ecosystem-ingestion point;
- no new provider Adapter requirement;
- no universal ontology or semantic-alignment component;
- no new multi-source immutable audit claim;
- no elevation of Evidence into absolute Trust.

Qwen remains advisory-only.

```text
QWEN_ROLE=ADVISORY_ONLY
QWEN_DECISION_AUTHORITY=false
QWEN_IMPLEMENTATION_AUTHORITY=false
```

## 12. Final strategic decision

### 12.1 Alignment result

| Review question | Result |
|---|---|
| Does GitHub-first align with Ecological Self-Limitation? | `PASS_WITH_GUARDRAILS` |
| Does it align with Evidence First? | `PASS_WITH_NON_ELEVATION` |
| Does it align with Authority Separation? | `PASS_WITH_ROLE_LIMIT` |
| Does it align with No Duplicate Component? | `PASS_ONLY_IF_NO_REBUILD` |
| Does it create entry competition by definition? | `NO`, if optional and native-source-bound |
| Can it create entry competition in practice? | `YES`, high de facto lock-in risk |
| Is GitHub a universal digital-asset entry? | `NO` |
| Is TITMAS a GitHub competitor? | `NO` |
| Is a project-level guardrail needed? | `YES` |
| Is a second guardrail file needed now? | `NO` |
| Is implementation authorized? | `NO` |

### 12.2 Strict go/no-go

```text
GO=GITHUB_FIRST_AS_PHASE_1_NON_EXCLUSIVE_DISCOVERY_HEURISTIC

NO_GO=GITHUB_ONLY
NO_GO=MANDATORY_TITMAS_ENTRY
NO_GO=GITHUB_SHADOW_PLATFORM
NO_GO=UNIVERSAL_ASSET_REGISTRY
NO_GO=POPULARITY_AS_TRUST
NO_GO=DISCOVERY_AS_PERMISSION
NO_GO=AUTOMATIC_DECISION_OR_EXECUTION
NO_GO=CONSTITUTIONAL_PROVIDER_DEPENDENCY
```

### 12.3 Final wording

Recommended strategic wording:

> **GitHub-first Discovery, source-native governance.**
>
> In its first bounded phase, TITMAS begins with GitHub-native discovery for
> GitHub-hosted software assets. GitHub remains the source for its repository
> objects, while every other service remains authoritative for its own domain.
> TITMAS does not compete for hosting, identity, permission, deployment, or
> asset custody. It helps humans understand source-bound relationships,
> freshness, limitations, and decision needs through distributed
> Evidence-, Health-, Evaluation-, and Human-Authority support.

中文：

> **GitHub 优先发现，事实回归原生来源。**
>
> TITMAS 第一阶段以 GitHub 原生表面发现 GitHub 托管的软件资产。GitHub 继续负责其
> repository 对象，其他服务继续负责各自领域的事实与权限。TITMAS 不竞争代码托管、
> 身份、权限、部署或数字资产托管；它通过分布式 Evidence、Health、Evaluation 和
> Human Authority 支撑，帮助人类理解带来源的关系、新鲜度、限制和待决事项。

Final state:

```text
OVERALL=PASS_WITH_REQUIRED_GUARDRAILS
PROJECT_GUARDRAIL_CANDIDATE=READY_FOR_HUMAN_REVIEW
PROJECT_GUARDRAIL_ADOPTED=false
CONSTITUTION_CHANGE_REQUIRED=false
INTERFACE_CHANGE_REQUIRED=false
EXPERIMENT_CHANGE_REQUIRED=false
IMPLEMENTATION_AUTHORIZED=false
```
