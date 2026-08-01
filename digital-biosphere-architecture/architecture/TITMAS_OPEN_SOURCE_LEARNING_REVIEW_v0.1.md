# TITMAS Open Source Learning Review v0.1

```text
DOCUMENT_TYPE=OPEN_SOURCE_ECOSYSTEM_LEARNING_REVIEW
STATUS=ANALYSIS_ONLY
VERSION=0.1
DATE=2026-07-28

PRIMARY_OBJECTIVE=REDUCE_SINGLE_HUMAN_MANAGEMENT_COST
OPEN_SOURCE_LEARNING_NE_FEATURE_ROADMAP=true
LEARNING_NE_COPYING=true
INTEGRATION_NE_REPLACEMENT=true
OBSERVATION_NE_CONTROL=true
RECOMMENDATION_NE_AUTHORITY=true

CONSTITUTION_CHANGED=false
INTERFACE_BOUNDARY_CHANGED=false
SCHEMA_CREATED=false
CODE_CREATED=false
API_CREATED=false
DASHBOARD_CREATED=false
REPOSITORY_CREATED=false
IMPLEMENTATION_AUTHORIZED=false
INTEGRATION_AUTHORIZED=false
ADOPTION_DECISION=false
LICENSE_COMPATIBILITY_ASSESSED=false
SECURITY_DUE_DILIGENCE_COMPLETE=false
```

## 0. Review purpose

This document evaluates what TITMAS can learn from existing open-source and
open-ecosystem projects without turning the review into a feature roadmap.

The only governing question is:

> Can a learning reduce the cognitive or operational cost for one human who
> manages multiple repositories, programs, agents, tools, and external
> services?

The review does not propose a new product, architecture layer, component,
schema, API, adapter, dashboard, repository, or implementation.

TITMAS must continue to coordinate heterogeneous tools rather than replace
GitHub, Codex, Render, Supabase, Context7, Linear, Cloudflare, or comparable
services.

## 1. Review basis

The review is bounded by:

- `TITMAS_SELF_GOVERNANCE_EXPERIMENT_DESIGN_v0.1.md`
- `TITMAS_SELF_GOVERNANCE_EXPERIMENT_PROTOCOL_v0.1.md`
- `TITMAS_INTERFACE_BOUNDARY_MAP_v0.1.md`
- `TITMAS_GOVERNANCE_CONSISTENCY_REVIEW_v0.1.md`

Source snapshots used for this review:

```text
TITMAS_SELF_GOVERNANCE_EXPERIMENT_DESIGN_v0.1.md
SHA256=394876046ce663390ec7956d6a4aff1daeba868fa79730e20adc3f2303cfed3d

TITMAS_SELF_GOVERNANCE_EXPERIMENT_PROTOCOL_v0.1.md
SHA256=2704cd172f0f23860b93ca0c6dfa0b1b421510bc7e2b143c55137e594aae046f

TITMAS_INTERFACE_BOUNDARY_MAP_v0.1.md
SHA256=241899a8a75b38471c827db8321e64f91dc2def04880f41dc9ddbdfdafe751be

TITMAS_GOVERNANCE_CONSISTENCY_REVIEW_v0.1.md
SHA256=0ff1a815ea8d0b32ae9e66546b97f3dd72be34f557c1cd16bbbec52bc1e35c29
```

## 2. Method and decision vocabulary

### 2.1 Evaluation lens

Each reference is assessed against five experimental outcomes:

| Code | Outcome | Question |
|---|---|---|
| `SH` | Source hops | Could it reduce the number of sources a human must open? |
| `CS` | Context switches | Could it reduce transitions between unrelated interfaces or mental models? |
| `RD` | Risk discovery | Could it shorten the time from an observable risk to human awareness? |
| `PS` | Project status understanding | Could it make current state and provenance faster to understand? |
| `ON` | New-project onboarding | Could it reduce the work required to include a project in the management cohort? |

All benefits stated in this review are hypotheses for the self-governance
experiment. They are not proven TITMAS capabilities.

### 2.2 Disposition vocabulary

| Disposition | Meaning in this review |
|---|---|
| **借鉴 / Learn** | Reuse a design lesson, boundary, or operating practice. No code or dependency is implied. |
| **集成 / Integrate candidate** | At most, consider a read-only reference to an already-used external tool's native output in a later, separately authorized experiment. |
| **保持距离 / Keep distance** | Study the project but do not import its platform or operating model into TITMAS. |
| **明确不做 / Explicitly do not** | Record a durable negative boundary against duplicating the referenced capability. |

In this document, “integration” never means installing a tool, creating an
adapter, parsing its output, synchronizing its state, copying its schema, or
making it a TITMAS truth source.

## 3. Category 1 — Agent development environments

### 3.1 OpenHands

**Official source:** [OpenHands repository](https://github.com/OpenHands/OpenHands)

**A. What management problem does it solve?**

OpenHands provides an environment in which software agents can work on
development tasks with bounded workspaces, tool access, and reviewable task
results. Its ecosystem also exposes a useful distinction between an agent
workspace and the operator's broader machine.

**B. What human cost can it reduce?**

It can reduce manual setup for a coding task and reduce repeated transitions
between task instructions, execution context, and produced changes.

**C. Does it overlap with TITMAS?**

There is limited overlap in task provenance and human review. There is strong
non-overlap in purpose: OpenHands is an agent development/execution
environment, while TITMAS is being tested as a human attention amplifier
across heterogeneous systems.

**D. TITMAS disposition**

- **借鉴:** isolate task scope, expose source/result links, and make environment
  boundaries visible.
- **保持距离:** its agent workspace and automation platform are not a TITMAS
  architecture template.
- **明确不做:** do not build an OpenHands-like coding canvas, runtime, sandbox,
  automation server, or agent control plane.

**Potential metric effect:** `SH`, `CS`, and `PS`, if an experiment can reference
the existing task source and result without copying runtime state.

**Boundary:** a task result remains an observation. It is not permission,
authority, approval, or evidence of correctness.

### 3.2 SWE-agent

**Official source:** [SWE-agent repository](https://github.com/SWE-agent/SWE-agent)

**A. What management problem does it solve?**

SWE-agent narrows an agent's work to a software-engineering task, commonly an
issue and repository snapshot, and attempts to produce a patch.

**B. What human cost can it reduce?**

It can reduce the manual effort required to translate a well-bounded issue
into a candidate code change.

**C. Does it overlap with TITMAS?**

The useful overlap is the explicit binding between a task, repository state,
and candidate result. Autonomous repair is outside the TITMAS experiment's
observation and attention scope.

**D. TITMAS disposition**

- **借鉴:** keep task scope narrow and bind findings to the repository and
  issue that produced them.
- **保持距离:** treat automatic patch generation as an external execution
  capability.
- **明确不做:** do not reproduce a coding executor, autonomous fixer, or
  benchmark harness.

**Potential metric effect:** `PS` and `RD` through clearer task-to-result
provenance, not through autonomous repair.

**Boundary:** a generated patch is a proposal. It is not a decision, approval,
or verified repair.

### 3.3 Claude Code-related public ecosystem

**Official sources:**

- [Claude Code public repository](https://github.com/anthropics/claude-code)
- [Claude Code Action security documentation](https://github.com/anthropics/claude-code-action/blob/main/docs/security.md)

**A. What management problem does it solve?**

The public Claude Code ecosystem demonstrates repository-scoped coding work,
tool permission boundaries, and action-based execution connected to existing
developer workflows.

**B. What human cost can it reduce?**

It can reduce handoffs between a repository, a coding task, and candidate
changes while retaining explicit review and permission surfaces.

**C. Does it overlap with TITMAS?**

It overlaps only where TITMAS may reference agent task state as one external
source. It does not define TITMAS governance. The existence of a public
repository must not be treated as proof that the complete product core is
open source.

**D. TITMAS disposition**

- **借鉴:** repository scoping, least privilege, explicit permission, and
  source/result links.
- **集成候选:** only a static reference to an already-existing task or result
  may be considered in a separately authorized experiment.
- **明确不做:** do not clone the coding agent, action runtime, permission
  system, or provider integration.

**Potential metric effect:** `SH`, `CS`, and `PS`.

**Boundary:** TITMAS may observe a task reference; it must not silently widen
the task's permissions or convert a tool result into approval.

### 3.4 LangGraph

**Official source:** [LangGraph human-in-the-loop documentation](https://docs.langchain.com/oss/python/langchain/human-in-the-loop)

**A. What management problem does it solve?**

LangGraph provides stateful agent workflows, including interruption before
sensitive actions and later resumption after human input.

**B. What human cost can it reduce?**

It can reduce the effort required to reconstruct workflow state when a human
must approve, edit, reject, or respond to an interrupted action.

**C. Does it overlap with TITMAS?**

It overlaps with the conceptual `Observe -> Evaluate -> Authorize -> Execute
-> Verify` separation. It does not imply that TITMAS needs a graph runtime or
workflow state machine.

**D. TITMAS disposition**

- **借鉴:** durable pause/resume semantics and explicit human interruption
  before consequential actions.
- **保持距离:** keep the orchestration runtime outside TITMAS's current scope.
- **明确不做:** do not create a graph engine, checkpoint store, or workflow
  executor as a result of this review.

**Potential metric effect:** `CS` and `PS`, because explicit interruption state
can make pending human action easier to understand.

**Boundary:** human-in-the-loop is an authority boundary, not an excuse to add
an orchestration layer.

### 3.5 CrewAI

**Official sources:**

- [CrewAI documentation](https://docs.crewai.com/)
- [CrewAI repository](https://github.com/crewAIInc/crewAI)

**A. What management problem does it solve?**

CrewAI organizes multi-agent work through agents, crews, and flows, with
supporting memory, knowledge, and observability surfaces.

**B. What human cost can it reduce?**

It can reduce the manual sequencing of multi-agent work within a chosen
orchestration environment.

**C. Does it overlap with TITMAS?**

There is high terminology overlap around agents, flows, memory, and
observability, but the operating objective differs. Adopting this model would
risk turning TITMAS into a centralized orchestrator.

**D. TITMAS disposition**

- **借鉴:** make agent roles and handoff boundaries legible to a human.
- **保持距离:** do not use its orchestration/control-plane model as TITMAS
  architecture.
- **明确不做:** do not build crews, flows, an agent registry, execution runtime,
  or control plane.

**Potential metric effect:** only `PS` as a documentation lesson.

**Boundary:** an agent role description does not grant authority, routing
priority, or execution permission.

### 3.6 AutoGen

**Official source:** [AutoGen repository](https://github.com/microsoft/autogen)

**A. What management problem does it solve?**

AutoGen provides a framework for multi-agent applications and conversations.
Its current official repository also records a material lifecycle signal:
the project is in maintenance mode and directs new users toward another
framework.

**B. What human cost can it reduce?**

Multi-agent conversation frameworks can reduce custom coordination code, but
framework lifecycle changes can create migration and maintenance cost.

**C. Does it overlap with TITMAS?**

It overlaps in multi-agent vocabulary but not in the present human-attention
experiment. Its lifecycle is more useful as a governance lesson than as an
integration candidate.

**D. TITMAS disposition**

- **借鉴:** treat project lifecycle, succession, and migration signals as
  inputs to maintenance-risk review.
- **保持距离:** do not adopt a maintenance-mode framework for this experiment.
- **明确不做:** do not reproduce its agent conversation runtime.

**Potential metric effect:** `RD` and `ON`, by exposing lifecycle risk before
onboarding or expansion.

**Boundary:** popularity, prior adoption, or a successor recommendation is not
an authority decision for TITMAS.

## 4. Category 2 — Agent observability

### 4.1 OpenTelemetry

**Official source:** [What is OpenTelemetry?](https://opentelemetry.io/docs/what-is-opentelemetry/)

**A. What management problem does it solve?**

OpenTelemetry provides vendor- and tool-neutral conventions and tooling to
generate, collect, and export traces, metrics, and logs. It explicitly does
not provide the observability backend that stores and visualizes the data.

**B. What human cost can it reduce?**

Shared telemetry semantics can reduce repeated interpretation work when a
human moves between services and observability vendors.

**C. Does it overlap with TITMAS?**

It overlaps with source correlation and observation, but telemetry is not
TITMAS Evidence, Truth, Evaluation, or Authority.

**D. TITMAS disposition**

- **借鉴:** vendor-neutral correlation, stable identifiers, timestamps, and
  clear separation between instrumentation and backend.
- **集成候选:** an existing native trace URL may later be referenced read-only.
- **明确不做:** do not build an OpenTelemetry collector, backend, storage
  system, instrumentation SDK, or dashboard.

**Potential metric effect:** `SH`, `CS`, `RD`, and `PS`.

**Boundary:** telemetry describes observed runtime signals; it does not prove
causality, correctness, compliance, or authorization.

### 4.2 Langfuse

**Official source:** [Langfuse repository](https://github.com/langfuse/langfuse)

**A. What management problem does it solve?**

Langfuse combines LLM tracing with evaluation, metrics, prompt management,
and datasets in an LLM engineering platform.

**B. What human cost can it reduce?**

It can reduce source hops when a team already uses the platform to investigate
an LLM interaction and its related evaluation context.

**C. Does it overlap with TITMAS?**

It has high overlap with any proposed unified trace, evaluation, or dashboard
surface. That overlap is a reason not to duplicate the platform.

**D. TITMAS disposition**

- **借鉴:** provide trace-to-source navigation and preserve native provenance.
- **集成候选:** only reference an existing native trace URL in a later
  authorized experiment.
- **保持距离:** retain its platform, data model, evaluation, prompts, and
  datasets as external.
- **明确不做:** do not build another LLM observability platform or ingest its
  data into a TITMAS truth store.

**Potential metric effect:** `SH`, `CS`, `RD`, and `PS`.

**Boundary:** an evaluation score is an observation or recommendation, not
permission, truth, or an automatic routing decision.

### 4.3 Arize Phoenix

**Official source:** [Arize Phoenix repository](https://github.com/Arize-ai/phoenix)

**A. What management problem does it solve?**

Phoenix combines OpenTelemetry-based tracing with evaluation, datasets,
experiments, and prompt-management capabilities for AI applications.

**B. What human cost can it reduce?**

It can reduce investigation time by linking an AI behavior to traces and
evaluation context in one external platform.

**C. Does it overlap with TITMAS?**

Its tracing and evaluation surfaces overlap strongly with any proposed
TITMAS observability dashboard. The repository's current license is also a
reminder that “public source” and OSI-approved open source must not be treated
as synonyms without license due diligence.

**D. TITMAS disposition**

- **借鉴:** make trace breakdown and source linkage understandable.
- **集成候选:** only a native trace link from an already-used deployment.
- **保持距离:** keep its trace store, evaluation engine, datasets, experiments,
  and UI external.
- **明确不做:** do not reproduce or embed the Phoenix platform.

**Potential metric effect:** `SH`, `RD`, and `PS`.

**Boundary:** this review does not assess license compatibility, security,
deployment suitability, or adoption.

### 4.4 OpenLLMetry

**Official source:** [OpenLLMetry repository](https://github.com/traceloop/openllmetry)

**A. What management problem does it solve?**

OpenLLMetry supplies OpenTelemetry extensions and instrumentation for LLM and
generative-AI workloads so they can feed existing observability systems.

**B. What human cost can it reduce?**

It can reduce bespoke instrumentation and make AI traces easier to compare
with existing service telemetry.

**C. Does it overlap with TITMAS?**

It overlaps only at the observation boundary. Instrumentation and collection
are not TITMAS's current role.

**D. TITMAS disposition**

- **借鉴:** reuse semantic-convention thinking and correlate AI activity with
  its native operational context.
- **保持距离:** leave instrumentation, exporters, and collectors to the
  existing observability ecosystem.
- **明确不做:** do not implement an instrumentation library or telemetry
  pipeline.

**Potential metric effect:** `SH`, `RD`, and `PS`.

**Boundary:** a common telemetry format does not create a common truth source.

## 5. Category 3 — Multi-repository management

### 5.1 repo (Google/Gerrit)

**Official source:** [repo tool repository](https://gerrit.googlesource.com/git-repo/)

**A. What management problem does it solve?**

`repo` coordinates work across many Git repositories using manifests while
remaining layered on top of Git rather than replacing it.

**B. What human cost can it reduce?**

It can reduce repeated repository checkout and synchronization commands when
a stable multi-repository manifest already exists.

**C. Does it overlap with TITMAS?**

It overlaps with cohort definition and source referencing. TITMAS must not
create a competing manifest authority or duplicate Git state.

**D. TITMAS disposition**

- **借鉴:** coordinate rather than replace; preserve native repository
  identity; make cohort membership explicit.
- **集成候选:** reference an existing native manifest if the frozen experiment
  cohort already uses it.
- **明确不做:** do not create a TITMAS manifest format, manifest parser, sync
  engine, or Git replacement.

**Potential metric effect:** `SH`, `CS`, `PS`, and `ON`.

**Boundary:** a manifest describes scope; it does not prove health, ownership,
or authorization.

### 5.2 Backstage Software Catalog

**Official source:** [Backstage Software Catalog documentation](https://backstage.io/docs/features/software-catalog/)

**A. What management problem does it solve?**

The Backstage Software Catalog centralizes ownership and software metadata
while storing catalog metadata with source code.

**B. What human cost can it reduce?**

It can reduce the time needed to discover what a component is, who owns it,
and where its supporting resources live.

**C. Does it overlap with TITMAS?**

It has high overlap with any proposed ownership catalog, developer portal, or
centralized Cockpit inventory. This is a strong reason to avoid duplicating
those functions.

**D. TITMAS disposition**

- **借鉴:** keep ownership metadata close to source, make provenance visible,
  and link to native systems.
- **集成候选:** only reference an existing catalog entry when the experiment
  cohort already uses Backstage.
- **保持距离:** do not adopt a centralized catalog as TITMAS authority.
- **明确不做:** do not build a second catalog, developer portal, inventory
  database, or dashboard.

**Potential metric effect:** `SH`, `CS`, `PS`, and `ON`.

**Boundary:** a catalog entry is metadata supplied by a source; it is not
verified truth or governance authority.

### 5.3 Sourcegraph Code Search

**Official source:** [Sourcegraph Code Search documentation](https://sourcegraph.com/docs/code-search)

**A. What management problem does it solve?**

Sourcegraph Code Search supports search across repositories, code hosts,
branches, and commits.

**B. What human cost can it reduce?**

It can reduce repository-by-repository search and the context switches needed
to locate a symbol, dependency, or policy reference.

**C. Does it overlap with TITMAS?**

Search is useful to TITMAS's human-attention objective, but indexing and code
intelligence are mature external capabilities. Product documentation is an
ecosystem reference and must not automatically be labeled wholly open source.

**D. TITMAS disposition**

- **借鉴:** use deep links that preserve query and repository context.
- **集成候选:** a static external search URL may be referenced if Sourcegraph
  is already used by the frozen cohort.
- **明确不做:** do not build, proxy, embed, or host a search/indexing service.

**Potential metric effect:** `SH`, `CS`, `PS`, and `ON`.

**Boundary:** search ranking is a navigation aid, not evidence, truth,
attention authority, or an automatic agent-selection mechanism.

### 5.4 Zoekt

**Official source:** [Zoekt repository](https://github.com/sourcegraph/zoekt)

**A. What management problem does it solve?**

Zoekt provides fast, indexed search across source-code repositories.

**B. What human cost can it reduce?**

It can reduce repeated local searches across many repositories and shorten
the time to locate relevant code.

**C. Does it overlap with TITMAS?**

An index would overlap with a hypothetical TITMAS code-intelligence layer,
which is outside the approved architecture and experiment.

**D. TITMAS disposition**

- **借鉴:** show search scope and index freshness so humans can judge result
  coverage.
- **保持距离:** treat indexing as an external specialist capability.
- **明确不做:** do not build or host an index, web interface, or search API.

**Potential metric effect:** `SH`, `CS`, and `ON`.

**Boundary:** an indexed result can be stale or incomplete and cannot be
elevated to a completeness claim.

### 5.5 OpenGrok

**Official source:** [OpenGrok repository](https://github.com/oracle/opengrok)

**A. What management problem does it solve?**

OpenGrok provides source-code search and cross-reference navigation across
code trees.

**B. What human cost can it reduce?**

It can reduce the time needed to trace definitions and references across
repositories.

**C. Does it overlap with TITMAS?**

Its search and cross-reference functions would be duplicated by a TITMAS code
index or search UI.

**D. TITMAS disposition**

- **借鉴:** preserve direct navigation from a finding to its exact source.
- **保持距离:** use an existing deployment only as an external source.
- **明确不做:** do not create another code search, cross-reference engine,
  index, or web UI.

**Potential metric effect:** `SH`, `CS`, `PS`, and `ON`.

**Boundary:** cross-reference results support human investigation; they do not
make decisions or grant execution rights.

## 6. Category 4 — Engineering health detection

### 6.1 Renovate

**Official source:** [Renovate repository](https://github.com/renovatebot/renovate)

**A. What management problem does it solve?**

Renovate automates dependency-update discovery and proposes updates across
many package managers and code-hosting platforms.

**B. What human cost can it reduce?**

It can reduce repeated dependency checks and manual creation of routine update
proposals.

**C. Does it overlap with TITMAS?**

It overlaps with dependency-risk observation, not with authority. TITMAS
should not become an updater or merge controller.

**D. TITMAS disposition**

- **借鉴:** present dependency findings with repository, package, version, and
  native proposal provenance.
- **集成候选:** only a static link to an existing Renovate PR or report.
- **明确不做:** do not build a dependency scanner, update bot, runner,
  automerge function, or output parser.

**Potential metric effect:** `SH`, `RD`, and `PS`.

**Boundary:** an update proposal does not authorize merge, release, deployment,
or acceptance of the dependency risk.

### 6.2 OpenSSF Scorecard

**Official source:** [OpenSSF Scorecard repository](https://github.com/ossf/scorecard)

**A. What management problem does it solve?**

OpenSSF Scorecard applies heuristic security checks to open-source projects
and reports explainable per-check scores.

**B. What human cost can it reduce?**

It can reduce the initial manual effort required to identify common
repository-security hygiene gaps.

**C. Does it overlap with TITMAS?**

It overlaps with risk observation and prioritization. Its scores must not
become TITMAS truth, permission, or an automatic block.

**D. TITMAS disposition**

- **借鉴:** keep findings explainable and trace each score to a specific check.
- **集成候选:** only reference an existing native report.
- **保持距离:** leave checks, scoring, datasets, and action execution external.
- **明确不做:** do not create a duplicate security score or aggregate it into
  an opaque TITMAS health score.

**Potential metric effect:** `RD` and `PS`.

**Boundary:** a heuristic score is a recommendation input. It is not proof of
security, compliance, permission, or project quality.

### 6.3 Trivy

**Official source:** [Trivy repository scanning documentation](https://trivy.dev/docs/latest/target/repository/)

**A. What management problem does it solve?**

Trivy can scan repositories for vulnerabilities, misconfigurations, secrets,
and license findings. Its documentation also exposes useful snapshot and
cache limitations, including special handling for dirty repositories.

**B. What human cost can it reduce?**

It can reduce the initial manual search for common dependency and
configuration risks.

**C. Does it overlap with TITMAS?**

It overlaps at risk observation only. Scanning, caching, databases, and result
interpretation remain external responsibilities.

**D. TITMAS disposition**

- **借鉴:** bind a finding to a commit or clearly disclose dirty-worktree and
  freshness limitations.
- **集成候选:** only link to an existing native scan report.
- **明确不做:** do not build a scanner, vulnerability database, report parser,
  or enforcement gate.

**Potential metric effect:** `RD` and `PS`.

**Boundary:** absence of a finding is not evidence of absence. A scan result
does not authorize remediation, shutdown, merge blocking, or deployment.

### 6.4 SonarQube Community Build

**Official source:** [SonarQube Community Build documentation](https://docs.sonarsource.com/sonarqube-community-build)

**A. What management problem does it solve?**

SonarQube Community Build provides static analysis and automated code-review
findings through an existing quality-analysis system.

**B. What human cost can it reduce?**

It can reduce repeated manual review for known classes of code-quality and
maintainability findings.

**C. Does it overlap with TITMAS?**

It overlaps with engineering-health observation. Reproducing its scanner,
server, dashboard, or quality gate would directly violate the no-duplication
constraint.

**D. TITMAS disposition**

- **借鉴:** keep a finding linked to the rule, file, revision, and native
  report.
- **集成候选:** only reference an already-existing report or quality-gate page.
- **明确不做:** do not build a static analyzer, rule engine, server, dashboard,
  or TITMAS-owned quality gate.

**Potential metric effect:** `RD` and `PS`.

**Boundary:** an external quality gate remains that service's output. It does
not become Human Authority or a TITMAS authorization gate.

### 6.5 CI health as a native external surface

**Reference surface:** existing code-host checks, actions, and deployment
provider status pages in the frozen cohort.

**A. What management problem does it solve?**

Native CI and deployment systems record whether configured jobs ran and what
they reported for a specific repository revision.

**B. What human cost can it reduce?**

Direct links to failing checks can reduce the time spent locating the relevant
repository, run, and log.

**C. Does it overlap with TITMAS?**

CI execution, log storage, reruns, and deployment controls belong to GitHub,
Render, Cloudflare, and other existing providers, not TITMAS.

**D. TITMAS disposition**

- **借鉴:** retain provider, repository, revision, check, timestamp, and native
  URL.
- **集成候选:** only static links to existing native checks during the manual
  experiment.
- **明确不做:** do not create a CI aggregator, runner, log store, parser,
  retry controller, or deployment control surface.

**Potential metric effect:** `SH`, `CS`, `RD`, and `PS`.

**Boundary:** `PASS`, `FAIL`, or a provider status is scoped to the configured
check. It is not release approval, production proof, or human authorization.

## 7. Category 5 — MCP ecosystem tools

### 7.1 Model Context Protocol architecture

**Official sources:**

- [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture)
- [MCP server features](https://modelcontextprotocol.io/specification/2025-06-18/server/index)
- [MCP tools specification](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)

**A. What management problem does it solve?**

MCP standardizes how hosts, clients, and servers exchange tools, resources,
and prompts without prescribing how an application or model must make
governance decisions.

**B. What human cost can it reduce?**

Shared protocol surfaces can reduce bespoke tool connection and discovery
work across heterogeneous services.

**C. Does it overlap with TITMAS?**

MCP can transport access to external capabilities, but it is not TITMAS
Authority, Evidence, Truth, Attention, Evaluation, or Cockpit.

**D. TITMAS disposition**

- **借鉴:** preserve host/client/server boundaries, capability declarations,
  and least-capability exposure.
- **集成候选:** use an already-authorized MCP capability only through its
  existing host and permission model.
- **明确不做:** do not create a TITMAS MCP gateway, registry, permission
  system, broker, or replacement client.

**Potential metric effect:** `SH`, `CS`, and `ON`.

**Boundary:** tool discovery or model invocation does not equal human
permission, authority, truth, decision, or execution authorization.

### 7.2 MCP Inspector

**Official source:** [MCP Inspector repository](https://github.com/modelcontextprotocol/inspector)

**A. What management problem does it solve?**

MCP Inspector helps developers manually inspect and test MCP server
capabilities and interactions.

**B. What human cost can it reduce?**

It can reduce the effort needed to understand what a server exposes and to
diagnose protocol-boundary problems.

**C. Does it overlap with TITMAS?**

It overlaps with interface inspection, but not with ongoing ecosystem
governance or attention allocation.

**D. TITMAS disposition**

- **借鉴:** make capability boundaries inspectable before use.
- **保持距离:** keep inspection as a specialist development activity.
- **明确不做:** do not build a new inspector, protocol-debug UI, or dashboard.

**Potential metric effect:** `PS` and `ON`.

**Boundary:** successful inspection proves only the tested interaction under
the tested conditions.

### 7.3 MCP Registry

**Official source:** [MCP Registry preview announcement](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/)

**A. What management problem does it solve?**

The MCP Registry aims to provide a discoverable catalog and API for MCP server
metadata.

**B. What human cost can it reduce?**

It can reduce the initial search effort required to find a server and its
published metadata.

**C. Does it overlap with TITMAS?**

A TITMAS registry would duplicate discovery infrastructure and risk becoming
a central authority. Registry metadata is self-described discovery data, not
trust evidence.

**D. TITMAS disposition**

- **借鉴:** separate discovery from verification, adoption, and permission.
- **保持距离:** treat the Registry as an external evolving service.
- **明确不做:** do not build a competing registry, mirror, crawler, trust
  score, or approval list.

**Potential metric effect:** `SH` and `ON`.

**Boundary:** listing does not equal trust, safety, adoption, compatibility,
permission, or authority.

### 7.4 GitHub MCP Server

**Official source:** [GitHub MCP Server repository](https://github.com/github/github-mcp-server)

**A. What management problem does it solve?**

GitHub MCP Server exposes GitHub capabilities through configurable toolsets
and individual tools, including a read-only mode that takes precedence over
write tools.

**B. What human cost can it reduce?**

When already authorized and used, limiting exposed toolsets can reduce
irrelevant capability discovery and context load while allowing direct access
to native GitHub state.

**C. Does it overlap with TITMAS?**

It overlaps with access to repository facts, but GitHub remains the canonical
external service. TITMAS must not proxy, copy, or re-authorize GitHub state.

**D. TITMAS disposition**

- **借鉴:** least capability, read-only-first access, explicit tool allowlists,
  and native-source provenance.
- **集成候选:** only continued use of an already-authorized GitHub MCP Server
  in its existing permission model.
- **明确不做:** do not create a GitHub proxy, MCP gateway, permission
  allocator, cache, or replacement repository service.

**Potential metric effect:** `SH`, `CS`, `PS`, and `ON`.

**Boundary:** availability of a write tool does not authorize its use. TITMAS
Attention must not select tools or allocate permissions.

## 8. Cross-project learning matrix

| Reference | Highest-value learning | Potential metric benefit | Disposition | Durable negative boundary |
|---|---|---|---|---|
| OpenHands | Task/environment isolation | `SH`, `CS`, `PS` | Learn / distance | No coding canvas or control plane |
| SWE-agent | Issue-to-snapshot binding | `PS`, `RD` | Learn / distance | No autonomous fixer |
| Claude Code ecosystem | Repository scope and explicit permission | `SH`, `CS`, `PS` | Learn / static reference candidate | No cloned agent runtime |
| LangGraph | Human interrupt and durable resume | `CS`, `PS` | Learn / distance | No workflow state machine |
| CrewAI | Legible roles and handoffs | `PS` | Distance | No crews, flows, or control plane |
| AutoGen | Lifecycle and migration risk | `RD`, `ON` | Distance | No conversation runtime |
| OpenTelemetry | Neutral correlation semantics | `SH`, `CS`, `RD`, `PS` | Learn / native-link candidate | No collector or backend |
| Langfuse | Trace-to-source navigation | `SH`, `CS`, `RD`, `PS` | Native-link candidate / distance | No LLM observability platform |
| Phoenix | Trace breakdown and source linkage | `SH`, `RD`, `PS` | Native-link candidate / distance | No trace/evaluation store |
| OpenLLMetry | AI telemetry conventions | `SH`, `RD`, `PS` | Learn / distance | No instrumentation pipeline |
| repo | Coordination without Git replacement | `SH`, `CS`, `PS`, `ON` | Learn / native-manifest candidate | No TITMAS manifest or sync |
| Backstage | Source-controlled ownership metadata | `SH`, `CS`, `PS`, `ON` | Learn / distance | No second catalog or portal |
| Sourcegraph | Context-preserving cross-repo links | `SH`, `CS`, `PS`, `ON` | Static-link candidate | No search proxy or index |
| Zoekt | Scope and freshness disclosure | `SH`, `CS`, `ON` | Learn / distance | No index or search API |
| OpenGrok | Direct source cross-reference | `SH`, `CS`, `PS`, `ON` | Learn / distance | No cross-reference engine |
| Renovate | Native dependency proposal provenance | `SH`, `RD`, `PS` | Static-report candidate | No updater or parser |
| OpenSSF Scorecard | Explainable heuristic checks | `RD`, `PS` | Static-report candidate | No opaque TITMAS score |
| Trivy | Snapshot/freshness limitations | `RD`, `PS` | Static-report candidate | No scanner or parser |
| SonarQube Community Build | Rule/file/revision linkage | `RD`, `PS` | Static-report candidate | No analyzer or quality gate |
| Native CI health | Run-to-revision provenance | `SH`, `CS`, `RD`, `PS` | Static-link candidate | No CI aggregator or controller |
| MCP architecture | Protocol and capability boundaries | `SH`, `CS`, `ON` | Learn | No gateway or permission system |
| MCP Inspector | Manual interface inspection | `PS`, `ON` | Learn / distance | No inspector UI |
| MCP Registry | Discovery is not trust | `SH`, `ON` | Distance | No registry or approval list |
| GitHub MCP Server | Read-only-first and tool allowlists | `SH`, `CS`, `PS`, `ON` | Learn / existing-use candidate | No GitHub proxy or re-authorization |

## 9. Most relevant learning for the self-governance experiment

### 9.1 Static source and deep links

The highest-confidence, lowest-maintenance learning is to preserve direct links
to the native source:

- repository and revision;
- issue, pull request, or task;
- CI run or scanner report;
- trace or provider status;
- external search query when already available.

This could reduce `SH`, `CS`, and risk-discovery time without moving native
state into TITMAS.

The experiment must measure whether the link actually saves time. It must not
assume benefit.

### 9.2 Source-controlled ownership and cohort metadata

Backstage and multi-repository manifests show the value of keeping scope and
ownership metadata close to source. TITMAS should learn the provenance rule,
not create a new catalog or manifest.

For the manual experiment, the frozen cohort record may point to existing
source metadata. It must not invent a synchronization service or canonical
ownership database.

### 9.3 Native health and observability outputs

Existing CI, dependency, security, code-quality, and trace systems already
produce specialized findings. TITMAS should test whether presenting a
human-readable attention candidate with a native link reduces discovery time.

It must not parse, normalize, score, aggregate, or store those external
outputs in this phase.

### 9.4 Snapshot and freshness disclosure

Search indexes, scan caches, repository revisions, and telemetry windows can
all be incomplete or stale. Every manual experiment record should therefore
retain:

- native source;
- observed timestamp;
- repository revision or provider run identifier when available;
- known freshness or dirty-worktree limitation;
- operator interpretation;
- later adjudication result.

This is Evidence First without claiming that all observations are equally
complete or reliable.

### 9.5 Read-only and least-capability access

MCP and coding-agent ecosystems reinforce a simple boundary: expose only the
capability needed for observation, prefer read-only access, and keep
authorization separate from discovery.

This is an operating constraint, not a proposal for a TITMAS permission
service.

## 10. Explicit non-roadmap

This review does not create a roadmap for any of the following:

1. agent coding canvas, runtime, sandbox, or control plane;
2. multi-agent orchestrator, graph engine, workflow state machine, or router;
3. unified developer portal, service catalog, inventory database, or Cockpit
   dashboard;
4. code search engine, code index, cross-reference engine, or search proxy;
5. telemetry SDK, collector, backend, trace store, or observability UI;
6. dependency updater, security scanner, static analyzer, CI runner, or
   deployment controller;
7. MCP gateway, registry, inspector, trust list, broker, or permission system;
8. external-output parser, normalization layer, synchronization service,
   cache, or copied truth source;
9. automatic agent selection, attention routing, remediation, shutdown,
   rollback, merge, release, or deployment;
10. replacement for GitHub, Codex, Render, Supabase, Context7, Linear,
    Cloudflare, or any comparable external service.

Any future proposal touching this list requires a new human decision and must
prove that it reduces management complexity and maintenance burden without
duplicating an existing service.

## 11. Rules for experimental use

The following rules apply if these learnings are later used in the already
planned manual experiment:

1. Only tools already present in the frozen cohort may be observed.
2. Do not install or adopt a tool solely because it appears in this review.
3. The external service remains the canonical source for its own state.
4. TITMAS Condition may record only a static link or manually transcribed,
   source-attributed observation.
5. Do not add an API, adapter, parser, scraper, webhook, synchronization job,
   database, or dashboard.
6. The operator must be able to reach the native source and adjudicate the
   finding.
7. The experiment must measure `SH`, `CS`, risk-discovery time, status
   comprehension, onboarding effort, false positives, false negatives, and
   the Cognitive Overhead Ratio.
8. Time spent maintaining links or reconciling external state counts as
   TITMAS overhead.
9. A finding can become an Attention Candidate, not a command.
10. Human Authority retains every authorization decision.

## 12. Risks identified by the learning review

### 12.1 Integration creep

“Reference an external result” can gradually become parsing, normalization,
storage, aggregation, and a new dashboard. The phase boundary therefore
permits only source-attributed static links or manual records.

### 12.2 Hidden authority

Scores, rankings, search order, CI status, trace evaluations, and scanner
severity can silently become automatic blocking or routing rules.

Required invariant:

```text
EXTERNAL_FINDING=OBSERVATION
ATTENTION_CANDIDATE=RECOMMENDATION
HUMAN_AUTHORITY_GATE=UNCHANGED
```

### 12.3 Maintenance burden

External APIs, output formats, licenses, product lifecycles, and provider
interfaces change. A parser or synchronization layer would convert external
change into TITMAS maintenance cost.

Required invariant:

```text
NO_EXTERNAL_OUTPUT_PARSER=true
NO_EXTERNAL_STATE_COPY=true
NATIVE_SOURCE_REMAINS_CANONICAL=true
```

### 12.4 False completeness

A single catalog, search index, scanner, trace system, or registry never
represents the whole ecosystem. The Cockpit must not present a partial source
as a complete truth surface.

### 12.5 License and security ambiguity

Public source availability does not prove license compatibility, security,
operational suitability, or adoption fitness. This learning review does not
perform those assessments.

## 13. External advisory review

A Qwen advisory pass was used to challenge the draft's scope boundaries.
Credentials were read only from the user-designated local environment file;
no key value is included in this document.

The advisory emphasized:

- cross-repository deep links and trace-to-source URLs are the strongest
  candidates for reducing source hops and context switches;
- existing CI and scanner reports are the strongest candidates for reducing
  risk-discovery time;
- source-controlled native metadata can lower onboarding cost;
- external-output parsing is the largest likely maintenance trap;
- converting observation or scores into automatic control is the largest
  authority risk;
- static references must not evolve into a unified dashboard, proxy, catalog,
  parser, or synchronization layer.

The advisory is non-authoritative. Its findings were accepted only where they
were independently consistent with the governing documents and official
project sources.

```text
QWEN_REVIEW_ROLE=ADVISORY_ONLY
QWEN_DECISION_AUTHORITY=false
QWEN_IMPLEMENTATION_AUTHORITY=false
```

## 14. Final assessment

### 14.1 What TITMAS should learn

TITMAS should learn five practices:

1. bind every observation to its native source and snapshot;
2. make repository, task, ownership, and freshness context legible;
3. use read-only and least-capability access for observation;
4. preserve human interruption before consequential execution;
5. treat discovery, telemetry, scores, and recommendations as non-authoritative.

### 14.2 What TITMAS may test manually

Within the frozen self-governance experiment, TITMAS may test whether static
native-source links and source-attributed Attention Candidates reduce:

- source hops;
- context switches;
- risk-discovery time;
- project-status comprehension time;
- new-project onboarding effort.

This is an experimental hypothesis, not an integration or implementation
decision.

### 14.3 What TITMAS should explicitly not become

TITMAS should not become:

- an agent development environment;
- a multi-agent orchestrator;
- an observability platform;
- a service catalog or developer portal;
- a code-intelligence or indexing product;
- an engineering scanner or CI controller;
- an MCP gateway or registry;
- an external-service replacement;
- a centralized truth, permission, decision, or execution authority.

### 14.4 Review status

```text
CORE_OBJECTIVE_ALIGNMENT=PASS
OPEN_SOURCE_LEARNING_SCOPE=PASS
NO_NEW_ARCHITECTURE_LAYER=PASS
NO_NEW_COMPONENT=PASS
NO_EXTERNAL_SERVICE_REPLACEMENT=PASS

LEARNING_RECOMMENDATION=PROCEED_AS_ANALYSIS_INPUT
FEATURE_ROADMAP_CREATED=false
INTEGRATION_DECISION=NOT_MADE
ADOPTION_DECISION=NOT_MADE
IMPLEMENTATION_AUTHORIZED=false
HUMAN_AUTHORITY_GATE=UNCHANGED
```

The appropriate next use of this review is limited to informing the manual
Self-Governance Experiment. Any implementation, integration, adoption, or
architecture change remains outside this document and requires a separate
human-authorized decision.
