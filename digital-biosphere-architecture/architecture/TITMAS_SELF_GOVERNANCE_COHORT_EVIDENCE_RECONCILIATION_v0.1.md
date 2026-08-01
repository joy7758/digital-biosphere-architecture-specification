---
document_id: DBA-TITMAS-SELF-GOVERNANCE-COHORT-EVIDENCE-RECONCILIATION-0.1
title: TITMAS Self-Governance Cohort Evidence Reconciliation v0.1
title_zh: TITMAS 自我治理实验对象证据对账 v0.1
status: RECONCILED_FORMAL_FREEZE_BLOCKED
maturity: Development
maturity_scope: entire-document
primary_repository: digital-biosphere-architecture
document_type: READ_ONLY_COHORT_EVIDENCE_RECONCILIATION
observed_at: 2026-07-28T22:32:39+08:00
cohort_frozen: false
experiment_executed: false
implementation_authorized: false
code_effect: false
schema_effect: false
api_effect: false
dashboard_effect: false
adapter_effect: false
repository_effect: false
external_write_effect: false
---

# TITMAS Self-Governance Cohort Evidence Reconciliation v0.1

中文：TITMAS 自我治理实验对象证据对账 v0.1。

## 0. Reconciliation boundary（对账边界）

本文件只核验候选 repository（仓库）与指定外部服务的现有使用证据，回答：

> 当前真实对象是否已经满足正式 Cohort Freeze（实验对象冻结）的全部前置条件？

本文件不执行实验，不冻结 Cohort，不创建代码、Schema、API、Adapter、Dashboard、
Repository、统一数据库、监控或响应系统，也不访问或修改外部服务账号。

本次对账受以下文件约束：

| Required input | SHA-256 |
|---|---|
| [`AGENTS.md`](../AGENTS.md) | `f4e82947f29e2704dff613a82df3b769736eba7e7023cd45e6bc29e79a198c07` |
| [`TITMAS Architecture Charter v0.2`](titmas-architecture-charter-v0.2.md) | `0a175a76b8c4d572025e7baae8ecf05abaf6f864906b7cd79c1d60cba83bc077` |
| [`Cohort Proposal v0.1`](TITMAS_SELF_GOVERNANCE_COHORT_PROPOSAL_v0.1.md) | `88edd47590c2550787a6aba822d364ebd6418cb13821f87da7f155b2fab30ed7` |
| [`Experiment Design v0.1`](TITMAS_SELF_GOVERNANCE_EXPERIMENT_DESIGN_v0.1.md) | `394876046ce663390ec7956d6a4aff1daeba868fa79730e20adc3f2303cfed3d` |
| [`Experiment Protocol v0.1`](TITMAS_SELF_GOVERNANCE_EXPERIMENT_PROTOCOL_v0.1.md) | `2704cd172f0f23860b93ca0c6dfa0b1b421510bc7e2b143c55137e594aae046f` |
| [`Open Source Learning Review v0.1`](TITMAS_OPEN_SOURCE_LEARNING_REVIEW_v0.1.md) | `4de6095ecb3ad7f3f99dbdc8b45a25f5f9e4810acd40fda86d9ba4552da59012` |

Charter v0.2 存在、可读且状态明确。本次任务因此可以继续，但不得扩大 TITMAS
Implementation 范围。

```text
COHORT_EVIDENCE_RECONCILED=true
FORMAL_COHORT_FREEZE_READY=false
EXPERIMENT_EXECUTED=false
IMMUNE_IMPLEMENTATION_CREATED=false
CONTINUOUS_MONITORING_CREATED=false
AUTOMATIC_RESPONSE_CREATED=false
IMPLEMENTATION_AUTHORIZED=false
```

## 1. Evidence method and claim discipline（证据方法与声明纪律）

### 1.1 Observation windows（观察时间）

| Evidence surface | Observation time |
|---|---|
| Local Git worktrees | `2026-07-28T22:26:47+08:00` |
| Same-branch remote HEAD comparison | `2026-07-28T22:28+08:00` approximate command window |
| GitHub repository/API/Actions state | `2026-07-28T22:27+08:00` to `2026-07-28T22:31+08:00` |
| Public domain/DNS/HTTP check | `2026-07-28T22:32:39+08:00` |
| Existing-workspace provider filename/reference scan | `2026-07-28T22:33+08:00` |

这些都是 point-in-time observations（时间点观察），不是持续监控。

### 1.2 Accepted evidence used（实际使用的证据）

本次实际读取或查询：

1. 上述六份强制输入和 DBA mandatory cockpit（强制驾驶舱）治理材料；
2. 各候选 worktree 的 `git rev-parse`、`git status --porcelain`、`git log -1`、
   `git remote get-url`、upstream 和 `git ls-remote`；
3. 各仓库已跟踪的 Agent instructions、README、status、release、risk 或 project-facts
   文件；
4. GitHub native repository metadata、default branch HEAD、open PR/Issue 和 Actions
   run references；
5. 已跟踪 provider-related 文件名与安全过滤后的配置表面；
6. `redcrag.cn` 的 DNS 与公开 HTTP response；
7. 当前 workspace 中 provider configuration filename 和 public-reference filename 的
   只读扫描；
8. Qwen advisory-only（仅咨询）边界复核。

本次没有读取 `.env` 内容、API Key、token、cookie、password、private key、provider
secret、Supabase data、Cloudflare account detail 或任何私密数据库内容。

### 1.3 Evidence interpretation rules（证据解释规则）

- README 或计划只能证明声明存在，不能证明 Runtime、deployment 或服务实际使用；
- tracked configuration 只能证明配置表面存在，不能证明 provider object 存在或在线；
- Git remote 证明 repository mapping candidate，不证明 Human Operational Owner；
- GitHub account owner 不等于 Human Operational Owner；
- local path owner 不等于已确认 Local Worktree Custodian；
- GitHub Actions success 只证明该 run 的 configured checks，不证明 release、deployment
  或项目健康；
- current Codex task 证明本次辅助工作发生，但不能自证 Protocol 所需的 pre-existing
  Agent-assisted workflow；
- 没有 native provider object 或获准 source reference 时，服务不能计入 minimum；
- 本文件中的引用不成为新的 canonical Truth source。

## 2. Proposal-to-current reconciliation（Proposal 与当前事实对账）

### 2.1 Material changes since the Proposal（重要变化）

| Item | Proposal snapshot | Current observation | Reconciliation |
|---|---|---|---|
| DBA Specification dirty paths | 67 | 73 with `-uall` | changed; count definitions and source window must be frozen |
| `agent-evidence` dirty paths | 88 | 167 with `-uall` | changed materially; publication/research/generated paths require exclusion |
| `agent-health` dirty paths | 50 | 100 with `-uall` | changed materially; branch still has no upstream |
| `digital-biosphere-os` dirty paths | 1 | 2 with `-uall` | changed; local `main` is behind observed remote `main` |
| `titmas-demo` local state | clean | clean | unchanged locally, but local and current remote HEAD differ |
| Research Pilot dirty paths | 34 | 56 with `-uall` | changed materially; protected research boundary remains |
| Candidate GitHub remotes | candidate | all 11 verified | repository existence is supported |
| Same-branch local/remote match | not fully reconciled | 3 match, 8 differ | exact source window is not freeze-ready |
| Countable external services | GitHub and Codex candidates | GitHub only strictly countable | current Codex task is self-referential for this gate |
| Operational external surface | unconfirmed | unconfirmed | Cloudflare code/dependency does not prove live Cloudflare use |

Dirty counts use `git status --porcelain=v1 -uall` and therefore can be higher than a default
directory-collapsed status. They are not workload or quality scores.

### 2.2 Owner and custody rule（Owner 与保管责任）

Across all 11 repositories:

```text
SOURCE_ACCOUNT_OWNER=joy7758
HUMAN_OPERATIONAL_OWNER=UNCONFIRMED_FOR_COHORT
LOCAL_FILESYSTEM_ACCOUNT=zhangbin
LOCAL_WORKTREE_CUSTODIAN=REQUIRES_HUMAN_CONFIRMATION
```

The DBA Program Charter identifies `zhangbin` as Human Program Owner, and the
Research Pilot identifies `bin_zhang` as Human Research Owner. Neither role is
silently promoted to Human Operational Owner or Local Worktree Custodian for
the experiment.

## 3. Primary Management candidate evidence（Management 候选证据）

Suitability values in this review:

```text
CONDITIONAL=real object, but not eligible for formal freeze until named blockers close
NO_CURRENTLY=not suitable under the current evidence and access boundary
```

### 3.1 `digital-biosphere-architecture-specification`

| Required field | Reconciled observation |
|---|---|
| Repository / local path | `digital-biosphere-architecture-specification`; Git root `/Users/zhangbin/Documents/New project`; relevant subtree `/Users/zhangbin/Documents/New project/digital-biosphere-architecture` |
| GitHub remote | `https://github.com/joy7758/digital-biosphere-architecture-specification.git` |
| GitHub remote owner | `joy7758`; public repository |
| Human Operational Owner | `UNCONFIRMED_FOR_COHORT`; Human Program Owner `zhangbin` is a separate observed role |
| Local worktree custodian | filesystem account `zhangbin` observed; human custodian `REQUIRES_HUMAN_CONFIRMATION` |
| Current branch / HEAD | `codex/production-observability-baseline` / `6cc94b5bca6bcee7e3c6651321915ffb4ad6133f` |
| Dirty / clean | `DIRTY`; 73 paths with `-uall`, all under the DBA subtree |
| Latest verifiable activity | local commit `2026-07-26T18:38:38+08:00`; GitHub repository pushed `2026-07-28T14:27:00Z` |
| Canonical source | GitHub for remote state; selected parent Git worktree for local state; DBA accepted documents for architecture/governance |
| Current project status source | `PROGRAM-STATUS.md` is a point-in-time snapshot observed `2026-07-23`; current Git and GitHub must be read separately |
| Current risk source | local dirty state; same-branch local/remote divergence; `RISK-AND-BLOCKER-REGISTER.md`; 13 open GitHub PRs; current Actions run |
| Actually used named services | GitHub `VERIFIED_IN_SCOPE`; current Codex reconciliation task observed but not countable as pre-existing workflow; Cloudflare configuration candidate only |
| Management Session | `CONDITIONAL` |
| Onboarding Session | `NO` because this repository prepared the experiment |
| Sensitive/access limits | parent worktree contains unrelated changes; provider credentials and private governance material excluded |
| Cannot confirm | intended local/remote reconciliation; experiment Owner/Operator/Reviewer; Human Operational Owner; normal-use Codex task reference; live Cloudflare object |

GitHub evidence:

- default `main` HEAD:
  `4d69ff79786e28432fdf5e7c830a89d9c480062b`;
- same-branch remote HEAD:
  `c1d8931930fbae15f96ee6a6ac050b081538c919`;
- local and same-branch remote histories were observed as `DIVERGED`;
- latest observed Actions run:
  `https://github.com/joy7758/digital-biosphere-architecture-specification/actions/runs/30339056493`,
  completed `success`.

### 3.2 `agent-evidence`

| Required field | Reconciled observation |
|---|---|
| Repository / local path | `agent-evidence`; `/Users/zhangbin/GitHub/agent-evidence` |
| GitHub remote | `https://github.com/joy7758/agent-evidence.git` |
| GitHub remote owner | `joy7758`; public repository |
| Human Operational Owner | `UNCONFIRMED_FOR_COHORT` |
| Local worktree custodian | filesystem account `zhangbin` observed; human custodian `REQUIRES_HUMAN_CONFIRMATION` |
| Current branch / HEAD | `revision/softwarex-v2-grounding-fix` / `1b692de391aa04bcfe2666ccc3ddce652ce5c3df` |
| Dirty / clean | `DIRTY`; 167 paths with `-uall` |
| Latest verifiable activity | local commit `2026-07-21T23:46:16+08:00`; GitHub repository pushed `2026-07-28T03:27:20Z` |
| Canonical source | GitHub for remote state; local worktree for uncommitted state; `docs/project-facts.md` for declared project facts |
| Current project status source | `docs/project-facts.md` last audited `2026-07-16`; `docs/STATUS.md` contains mixed historical readiness notes and is not sufficient alone |
| Current risk source | local dirty state; branch mapping; 14 open PRs and 4 open non-PR Issues; canonical-facts freshness; claim boundaries |
| Actually used named services | GitHub `VERIFIED_IN_SCOPE`; Codex-related documentation exists but no countable native project-task reference was frozen |
| Management Session | `CONDITIONAL` |
| Onboarding Session | `NO` due extensive prior TITMAS review exposure |
| Sensitive/access limits | paper, release, experiment, generated and possible publication-sensitive paths must be excluded; no private content copied |
| Cannot confirm | which dirty paths belong to the session; current Human Owner; intended remote comparison; independent normal-use Codex record |

GitHub evidence:

- default `main` HEAD:
  `bff5337f3d70488ddca9c64e95eff2d826c0fdbe`;
- same-branch remote HEAD:
  `d26d6dcb79719bbf13dedb7c1b875ee974d1be23`;
- local branch was observed `LOCAL_AHEAD` of the same-branch remote, while still dirty;
- latest observed Actions run:
  `https://github.com/joy7758/agent-evidence/actions/runs/30325968996`,
  completed `success`.

### 3.3 `agent-health`

| Required field | Reconciled observation |
|---|---|
| Repository / local path | `agent-health`; `/Users/zhangbin/GitHub/agent-health` |
| GitHub remote | `https://github.com/joy7758/agent-health.git` |
| GitHub remote owner | `joy7758`; public repository |
| Human Operational Owner | `UNCONFIRMED_FOR_COHORT` |
| Local worktree custodian | filesystem account `zhangbin` observed; human custodian `REQUIRES_HUMAN_CONFIRMATION` |
| Current branch / HEAD | `main` / `6c7937f7b6ad8703922deedaa5ebcde742448320`; configured upstream `NONE` |
| Dirty / clean | `DIRTY`; 100 paths with `-uall` |
| Latest verifiable activity | local commit `2026-07-27T20:00:44+08:00`; GitHub repository pushed `2026-07-28T03:43:42Z` |
| Canonical source | GitHub/npm native state for distribution; local worktree for uncommitted state; `RELEASE_STATUS.md` for declared distribution status |
| Current project status source | `RELEASE_STATUS.md`, verified `2026-07-27`, plus direct GitHub state; it does not describe current dirty work |
| Current risk source | no upstream; local/remote divergence; 100 dirty paths; static-health claim boundary; no open GitHub PR/Issue |
| Actually used named services | GitHub `VERIFIED_IN_SCOPE`; Codex handoff documentation is not a native workflow record |
| Management Session | `CONDITIONAL` |
| Onboarding Session | `NO` due prior release and product-management exposure |
| Sensitive/access limits | release and pilot evidence paths require scope review; no npm/provider credentials inspected |
| Cannot confirm | intended upstream branch; disposition of dirty reports/docs/code; Human Operational Owner; session-safe source window |

GitHub evidence:

- default and same-branch remote `main` HEAD:
  `975da73d93b911a8352afed0f95cfd39ed0305c9`;
- local and remote histories were observed as `DIVERGED`;
- latest observed Actions run:
  `https://github.com/joy7758/agent-health/actions/runs/30326726550`,
  completed `success`.

### 3.4 `digital-biosphere-os`

| Required field | Reconciled observation |
|---|---|
| Repository / local path | `digital-biosphere-os`; `/Users/zhangbin/GitHub/digital-biosphere-os` |
| GitHub remote | `https://github.com/joy7758/digital-biosphere-os.git` |
| GitHub remote owner | `joy7758`; private repository |
| Human Operational Owner | `UNCONFIRMED_FOR_COHORT`; DBOS Domain Owner role is not inferred from access |
| Local worktree custodian | filesystem account `zhangbin` observed; human custodian `REQUIRES_HUMAN_CONFIRMATION` |
| Current branch / HEAD | `main` / `0caa2c45e511a82d0dcab778b0ffc3163aac0029` |
| Dirty / clean | `DIRTY`; 2 paths under `reports/` |
| Latest verifiable activity | local commit `2026-07-21T23:03:57+08:00`; GitHub repository pushed `2026-07-23T06:43:07Z` |
| Canonical source | private GitHub repository for remote code state; selected local worktree for local state; DBOS-native status declarations for capability facts |
| Current project status source | remote `main` and DBOS `README.md` / `STRATEGIC_ALIGNMENT.md`; DBA summaries remain reference-only |
| Current risk source | local `main` behind observed remote `main`; private-source access boundary; dirty reports; no GitHub Actions or open PR/Issue |
| Actually used named services | GitHub `VERIFIED_IN_SCOPE`; no other named service actual-use evidence |
| Management Session | `CONDITIONAL` |
| Onboarding Session | `NO` due prior architecture mapping |
| Sensitive/access limits | private repository; contents require explicit experiment approval; only metadata and already-permitted declarations used |
| Cannot confirm | Human Operational Owner; approved private-source surface; whether local stale checkout is intentional |

GitHub default and same-branch remote `main` HEAD is
`cd3f867c4379ec555c45e7d554088ad12ce08a24`; local `main` was observed
`LOCAL_BEHIND_OR_EQUAL` and not at the same commit.

### 3.5 `titmas-demo`

| Required field | Reconciled observation |
|---|---|
| Repository / local path | `titmas-demo`; `/Users/zhangbin/GitHub/titmas-demo` |
| GitHub remote | `https://github.com/joy7758/titmas-demo.git` |
| GitHub remote owner | `joy7758`; public repository |
| Human Operational Owner | `UNCONFIRMED_FOR_COHORT` |
| Local worktree custodian | filesystem account `zhangbin` observed; human custodian `REQUIRES_HUMAN_CONFIRMATION` |
| Current branch / HEAD | `main` / `7c0470aebe966c72f661394b1a2627b082b90b48` |
| Dirty / clean | `CLEAN` |
| Latest verifiable activity | local commit `2026-07-26T18:24:26+08:00`; GitHub repository pushed `2026-07-26T10:43:01Z` |
| Canonical source | GitHub for current public repository state; local worktree for the selected clean checkout; README/freeze/release records for bounded claims |
| Current project status source | README says reference demo only; local publication record says `PUBLICATION_HOLD`, while GitHub now exposes a public repository |
| Current risk source | local/remote HEAD mismatch; publication-status conflict; deterministic-demo floor effect; no Actions/open PR/open Issue |
| Actually used named services | GitHub `VERIFIED_IN_SCOPE`; no other named service actual-use evidence |
| Management Session | `CONDITIONAL`, calibration or low-activity task only |
| Onboarding Session | `NO` due prior TITMAS familiarity |
| Sensitive/access limits | no provider secret inspected; demo output is not production Evidence |
| Cannot confirm | relation between the local and current remote commit without updating refs; current publication decision; meaningful Management task window |

GitHub default and same-branch remote `main` HEAD is
`2bc410b5ea88dea6a0d7deb8f15d8dde67280f26`. It differs from local `HEAD`;
the exact ancestry was not confirmed without changing local refs.

## 4. Onboarding reserve evidence（Onboarding 储备证据）

### 4.1 `pop-persona-pack`

| Required field | Reconciled observation |
|---|---|
| Repository / local path | `pop-persona-pack`; `/Users/zhangbin/GitHub/pop-persona-pack` |
| GitHub remote / owner | `https://github.com/joy7758/pop-persona-pack.git`; owner `joy7758`; public but `archived=true` |
| Human Operational Owner / custodian | both require Human confirmation; local filesystem account `zhangbin` observed |
| Branch / HEAD / status | `main`; `15677cfab2ff1b018edab7460e4e22b5f35d2f28`; clean |
| Recent activity | local commit `2026-03-23T02:39:42+08:00`; GitHub pushed `2026-05-23T09:53:29Z` |
| Remote state | remote `main` `0706ec704e1cf05be047806007dd6f865d8af742`; local/remote differ |
| Canonical/project-status source | GitHub for archived/repository state; README for the CrewAI persona example scope |
| Current risk source | archived remote; stale local checkout; one older successful Actions run; lifecycle and successor not declared locally |
| Actually used named services | GitHub only; README runtime/provider description is not service-use evidence |
| Management / Onboarding | Management `NO` if reserved; Onboarding `CONDITIONAL` |
| Sensitive/access limits | model/provider credentials must not be used or recorded |
| Cannot confirm | archive decision/successor, Human Owner, intended current revision, prior Operator familiarity |

Latest observed Actions:
`https://github.com/joy7758/pop-persona-pack/actions/runs/26329718880`,
completed `success` on `2026-05-23`.

### 4.2 `langchain-pop`

| Required field | Reconciled observation |
|---|---|
| Repository / local path | `langchain-pop`; `/Users/zhangbin/GitHub/langchain-pop` |
| GitHub remote / owner | `https://github.com/joy7758/langchain-pop.git`; owner `joy7758`; public |
| Human Operational Owner / custodian | both require Human confirmation; local filesystem account `zhangbin` observed |
| Branch / HEAD / status | `main`; `0ee1c4b6f547b0ecf7d5d0078d8b721fb043016d`; clean |
| Recent activity | local commit `2026-03-23T02:39:31+08:00`; GitHub pushed `2026-05-23T09:53:21Z` |
| Remote state | remote `main` `cc4ea7963f8051edee20bf3465b07cd4152d17be`; local/remote differ |
| Canonical/project-status source | README explicitly marks this repo a deprecated compatibility wrapper and points to `persona-object-protocol` as canonical implementation |
| Current risk source | deprecated lifecycle; stale local checkout; canonical-home transition; two older Actions workflows |
| Actually used named services | GitHub only; LangChain/OpenAI example code is not proof of external-service use |
| Management / Onboarding | Management `NO` if reserved; Onboarding `CONDITIONAL` |
| Sensitive/access limits | no model/provider credential or live model call permitted |
| Cannot confirm | deprecation schedule, package continuity, Human Owner, current canonical-home mapping |

Latest observed Actions:
`https://github.com/joy7758/langchain-pop/actions/runs/26329716680`,
completed `success` on `2026-05-23`.

### 4.3 `pop-persona-cockpit`

| Required field | Reconciled observation |
|---|---|
| Repository / local path | `pop-persona-cockpit`; `/Users/zhangbin/GitHub/pop-persona-cockpit` |
| GitHub remote / owner | `https://github.com/joy7758/pop-persona-cockpit.git`; owner `joy7758`; private |
| Human Operational Owner / custodian | both require Human confirmation; local filesystem account `zhangbin` observed |
| Branch / HEAD / status | `main`; `b51d2fb4db7c6cebc0d07ba34dac0dbc0e8602b9`; clean; remote same-branch HEAD matches |
| Recent activity | local commit `2026-03-23T02:39:40+08:00`; GitHub pushed `2026-03-22T18:39:42Z` |
| Canonical/project-status source | private GitHub plus README; README says local-first MVP with implemented import and later placeholders |
| Current risk source | private/local-persona-data boundary; placeholder capability status; no Actions/open PR/open Issue |
| Actually used named services | GitHub only; ChatGPT capture support and local web UI are implementation descriptions, not current service-use evidence |
| Management / Onboarding | Management `NO` if reserved; Onboarding `CONDITIONAL` only with code-only safe surface |
| Sensitive/access limits | local ChatGPT exports, persona data, SQLite and session artifacts must be excluded |
| Cannot confirm | whether local data exists, approved safe surface, Human Owner, prior familiarity |

### 4.4 `titmas-integrations`

| Required field | Reconciled observation |
|---|---|
| Repository / local path | `titmas-integrations`; `/Users/zhangbin/GitHub/titmas-integrations` |
| GitHub remote / owner | `https://github.com/joy7758/titmas-integrations.git`; owner `joy7758`; public |
| Human Operational Owner / custodian | both require Human confirmation; local filesystem account `zhangbin` observed |
| Branch / HEAD / status | `main`; `e8eeccbf19e5e1d1f01ab9ad8796a53591a38dc8`; clean; remote match |
| Recent activity | local commit `2026-07-25T05:46:58+08:00`; GitHub pushed `2026-07-27T04:21:04Z` |
| Canonical/project-status source | GitHub and README |
| Current risk source | repository contains README plus empty scaffold directories only; overlaps `agent-evidence/integrations`; no Actions/open PR/open Issue |
| Actually used named services | GitHub only; named frameworks are planned contribution points, not actual integrations |
| Management / Onboarding | Management `NO` if reserved; Onboarding `CONDITIONAL` |
| Sensitive/access limits | no external credentials or provider access allowed |
| Cannot confirm | Owner, justified unique responsibility, whether the repo should remain separate |

### 4.5 `titmas-health`

| Required field | Reconciled observation |
|---|---|
| Repository / local path | `titmas-health`; `/Users/zhangbin/GitHub/titmas-health` |
| GitHub remote / owner | `https://github.com/joy7758/titmas-health.git`; owner `joy7758`; public |
| Human Operational Owner / custodian | both require Human confirmation; local filesystem account `zhangbin` observed |
| Branch / HEAD / status | `main`; `551810241fbda88fb468bede22bbecbc9c6223cd`; clean; remote match |
| Recent activity | local commit `2026-07-25T06:04:43+08:00`; GitHub pushed `2026-07-24T22:05:09Z` |
| Canonical/project-status source | GitHub and README/docs |
| Current risk source | overlap with `agent-health`; tracked files are documentation, one Schema and one example, with no verified engine implementation; no Actions/open PR/open Issue |
| Actually used named services | GitHub only |
| Management / Onboarding | Management `NO` if reserved; Onboarding `CONDITIONAL` only as a duplication/claim-boundary case |
| Sensitive/access limits | no external service state or private evidence should be introduced |
| Cannot confirm | unique Owner/responsibility, implementation status beyond docs/schema/example, future disposition |

### 4.6 `digital-biosphere-research-agent-pilot`

| Required field | Reconciled observation |
|---|---|
| Repository / local path | `digital-biosphere-research-agent-pilot`; `/Users/zhangbin/GitHub/digital-biosphere-research-agent-pilot` |
| GitHub remote / owner | `https://github.com/joy7758/digital-biosphere-research-agent-pilot.git`; owner `joy7758`; public |
| Human Operational Owner / custodian | Human Research Owner `bin_zhang` is declared; Cohort Operational Owner and custodian still require Human confirmation |
| Branch / HEAD / status | `main`; `3cc08f5cc65025db0db895460813d84bc7ea4bb5`; dirty with 56 paths |
| Recent activity | local commit `2026-07-25T09:35:47+08:00`; GitHub pushed `2026-07-25T01:36:35Z` |
| Remote state | remote `main` `741d6344b014f5992e3e6e5c967da2a48a749318`; histories observed `DIVERGED` |
| Canonical/project-status source | README and AGENTS for `specification-only / NOT_READY`; GitHub for remote repository state |
| Current risk source | protected research/material boundary; 56 dirty paths; local/remote divergence; inconsistent evolving status statements; no Actions/open PR/open Issue |
| Actually used named services | GitHub only; AI-assisted review statements do not identify a countable native Codex/Context7 task |
| Management / Onboarding | Management `NO`; Onboarding `NO_CURRENTLY` |
| Sensitive/access limits | unpublished research, evidence drafts, medical/source-review material and adjacent-project references require explicit exclusion |
| Cannot confirm | exact safe surface, concurrent contributors, Cohort Owner, context status reconciliation, permission to include research metadata |

## 5. External-service evidence reconciliation（外部服务证据对账）

Only the following status vocabulary is used:

```text
VERIFIED_IN_SCOPE
EVIDENCE_INSUFFICIENT
NOT_IN_SCOPE
REQUIRES_HUMAN_CONFIRMATION
```

| Service | Status | Evidence and decision | First-round Immune role |
|---|---|---|---|
| GitHub | `VERIFIED_IN_SCOPE` | all 11 remotes resolved to native GitHub repositories owned by source account `joy7758`; native repository/default-branch/PR/Issue/Actions state was queried read-only | GitHub-hosted software state source |
| Codex | `REQUIRES_HUMAN_CONFIRMATION` | current authorized Codex task exists and produced this read-only reconciliation, but using the current gate-review task to prove a pre-existing cohort workflow would be self-referential; no frozen native task reference, normal-use boundary, timing rule or task owner was provided | authorized execution-assistance source |
| Render | `NOT_IN_SCOPE` | no candidate-repository Render configuration, public service URL, native deployment object or task reference was found | runtime/deployment state source only if later evidenced |
| Supabase | `NOT_IN_SCOPE` | no candidate-repository Supabase project configuration, public project reference or permitted native service object was found | data/backend service state source only if later evidenced |
| Context7 | `EVIDENCE_INSUFFICIENT` | Context7 appears in experiment/governance analysis, but no cohort-specific retrieval result, underlying citation record or normal Operator workflow evidence was found | knowledge/document reference source only if later evidenced |
| Linear | `NOT_IN_SCOPE` | no candidate-specific Linear project, issue URL, work-item reference or existing configuration was found; unrelated word matches were rejected | planning/work-item state source only if later evidenced |
| Cloudflare | `EVIDENCE_INSUFFICIENT` | DBA contains tracked Worker source and Cloudflare build dependencies, but no native account/project/deployment reference; public `redcrag.cn` returned `server: nginx/1.24.0 (Ubuntu)` and DNS did not expose Cloudflare nameservers in this observation | domain/network/security state source only if later evidenced |

For every service:

```text
EXTERNAL_SERVICE_REMAINS_CANONICAL=true
TITMAS_REFERENCE_ONLY=true
TITMAS_WRITEBACK=false
TITMAS_SERVICE_REPLACEMENT=false
```

### 5.1 Strict count（严格计数）

```text
COUNTABLE_EXTERNAL_SERVICE_CLASSES=1
COUNTABLE_EXTERNAL_SERVICE_CLASS_LIST=GitHub
REQUIRED_EXTERNAL_SERVICE_CLASSES=4

CODEX_ACTUAL_CURRENT_TASK_OBSERVED=true
CODEX_COUNTABLE_AS_PREEXISTING_COHORT_WORKFLOW=false

CLOUDFLARE_CODE_OR_DEPENDENCY_PRESENT=true
CLOUDFLARE_NATIVE_SERVICE_OBJECT_VERIFIED=false
```

GitHub API and Actions were actually queried during reconciliation. This is
current read-only source verification, not experiment execution.

## 6. Protocol minimum reconciliation（Protocol 最低范围对账）

### 6.1 Required outputs（必须输出）

```text
REPOSITORY_MINIMUM_MET=false
AGENT_WORKFLOW_MINIMUM_MET=false
EXTERNAL_SERVICE_CATEGORY_MINIMUM_MET=false
OPERATIONAL_SURFACE_MINIMUM_MET=false
```

### 6.2 Why repository minimum remains false

Five named Management repositories are real and accessible:

```text
REAL_MANAGEMENT_REPOSITORY_EXISTENCE_COUNT=5
```

However, the Protocol minimum applies to the formally frozen Cohort, not to a
name list. None of the five currently has a complete experiment-level Human
Operational Owner, Local Worktree Custodian, exact local/remote mapping,
approved sensitive-data boundary and frozen source window. Therefore:

```text
FORMALLY_FREEZABLE_MANAGEMENT_REPOSITORY_COUNT=0
```

This does not deny repository existence; it prevents existence from being
silently upgraded to a frozen experiment object.

### 6.3 Why Agent workflow minimum remains false

The current Codex task demonstrates that Agent assistance is available, but it
is the task performing this reconciliation. Counting it would allow the gate
to prove itself and would contaminate later familiarity measurements.

An eligible workflow still needs:

- a pre-existing, cohort-specific native task reference;
- Human task owner and authorization boundary;
- repository/source binding;
- timing and review-cost method;
- confirmation that it is normal practice rather than introduced for the
  experiment.

### 6.4 Why external and operational minimums remain false

Only GitHub is strictly countable. Four service classes require three more
actually used services.

No verified Render deployment, Supabase backend, Linear planning item or
Cloudflare domain/security provider object is in the current Cohort.
Consequently no required deployment/data/planning/domain-security surface is
verified.

## 7. First-round Immune sensing boundary（第一轮免疫感知边界）

If a later Human Decision authorizes a manual experiment, the first round may
observe only existing, bounded signals:

- repository existence and exact remote;
- local and remote branch/HEAD references;
- dirty/clean state at an observation time;
- open PR/Issue references;
- existing GitHub Actions or native check references;
- public deployment/domain reference only when its provider source is verified;
- documented status drift;
- missing Owner/custodian;
- `STALE`, `UNKNOWN`, `CONFLICTED`, `UNAVAILABLE`;
- source/claim boundary mismatches.

This review does not establish current capability for:

- continuous monitoring;
- real-time anomaly detection;
- automatic behavior-drift detection;
- automatic permission-drift detection;
- automatic immune-memory learning;
- automatic isolation;
- automatic repair;
- automatic rollback;
- automatic external response.

## 8. Freeze blockers and minimum real correction paths

### 8.1 Missing conditions（缺失条件）

1. Human Experiment Owner、Operator 和 Reviewer 未指派；
2. 五个 Management objects 的 Human Operational Owner 未确认；
3. 五个 selected worktrees 的 Local Worktree Custodian 未确认；
4. 8/11 local HEAD 与同名 remote branch 不一致，拟使用的 source window 未冻结；
5. DBA dual-repository identity 仍需选择 exact object；
6. `agent-health` upstream 仍为 `NONE`；
7. dirty worktree 的 excluded paths、sensitive boundary 和 concurrent contributors
   未冻结；
8. pre-existing Agent-assisted workflow 未以独立 native task reference 确认；
9. 只有一类外部服务严格可计数，低于四类；
10. 没有已核验的 deployment、data/backend、planning 或 domain/security surface；
11. Onboarding pair、complexity strata、condition/order 和 prior familiarity 未冻结；
12. Evidence location、retention 和 access rule 未获授权。

### 8.2 Allowed bounded path A（从现有真实项目选择）

Human Owner may nominate existing real projects that already use the missing
service classes. Reconciliation must then verify native, permitted objects
such as:

- an existing Render service/deployment;
- an existing Supabase project status surface, without private data;
- an existing Linear work item/project;
- an existing Cloudflare domain/project/status object;
- a pre-existing Context7 retrieval record plus its underlying cited source;
- a pre-existing Codex task bound to a candidate repository.

No project qualifies merely because it contains a dependency, example,
README, empty configuration, upstream clone or planned integration.

A broad filename-only workspace check found:

- one `wrangler.toml` under `pydantic-ai-ei`, but no Human Owner, Cohort role or
  live provider object was established;
- a Supabase migration example under an unrelated MCP example repository,
  which is not actual Cohort service use;
- no eligible Render, Supabase, Linear, Context7 or Cloudflare object for the
  current Cohort.

These findings are not recommended replacement objects until a Human Owner
identifies a real operational need and permits canonical-source verification.

### 8.3 Allowed bounded path B（单独修订 Protocol）

If the Human Owner concludes that four external-service classes do not reflect
the intended first experiment, the only alternative is:

```text
record current blocker
  -> separate Human review
    -> issue a new versioned Protocol decision
      -> prepare a new Cohort Proposal
        -> repeat Evidence Reconciliation
```

This document does not revise the Protocol.

### 8.4 Prohibited pseudo-satisfaction（禁止伪满足）

Do not:

- adopt software solely for the experiment;
- create a fake deployment;
- create an empty database;
- create a purposeless Linear project;
- introduce Context7 only to increase the count;
- create a new Integration or Adapter;
- count GitHub Actions separately from GitHub;
- count local Git, terminal or Codex as multiple services;
- count README/config/package dependencies as live provider use;
- count the current reconciliation task as independent historical proof;
- copy provider state into a TITMAS database.

## 9. Recommended candidate disposition before any Freeze

No repository is frozen by this document.

| Candidate | Current disposition | Required before reconsideration |
|---|---|---|
| DBA Specification workspace | `CONDITIONAL_MANAGEMENT` | resolve exact Git object, owner/custodian, divergence and path exclusions |
| `agent-evidence` | `CONDITIONAL_MANAGEMENT` | freeze source window and exclude paper/private/generated/unrelated work |
| `agent-health` | `CONDITIONAL_MANAGEMENT` | resolve upstream and divergent/dirty state |
| `digital-biosphere-os` | `CONDITIONAL_MANAGEMENT` | approve private safe surface and current revision |
| `titmas-demo` | `CONDITIONAL_CALIBRATION_OR_LOW_ACTIVITY` | reconcile publication/current remote state and define meaningful task |
| `pop-persona-pack` | `CONDITIONAL_ONBOARDING` | record archive state, successor and current revision |
| `langchain-pop` | `CONDITIONAL_ONBOARDING` | freeze deprecated-wrapper/canonical-home task |
| `pop-persona-cockpit` | `CONDITIONAL_ONBOARDING` | code-only safe surface; exclude personal data |
| `titmas-integrations` | `CONDITIONAL_ONBOARDING` | preserve scaffolding/duplication finding without disposition action |
| `titmas-health` | `CONDITIONAL_ONBOARDING` | preserve overlap and implementation-status uncertainty |
| Research Agent Pilot | `EXCLUDE_CURRENTLY` | explicit safe surface, owner/custodian and research-data approval |

## 10. Content that could not be verified（无法核验内容）

The following remain explicitly unverified:

- Human Experiment Owner、Operator、Reviewer and role overlap;
- Human Operational Owner for every candidate repository;
- Local Worktree Custodian for every selected checkout;
- concurrent human or Agent contributors in a future source window;
- intended resolution of divergent or stale local/remote branches;
- reason, age or relevance of uncommitted changes;
- complete current risk set for any repository;
- private DBOS or Cockpit content beyond the permitted metadata/declarations;
- safe experiment surface for `agent-evidence`, DBOS and Research Pilot;
- pre-existing countable Codex workflow and its timing/review-cost method;
- Cohort-specific Context7 retrieval history;
- actual Render service;
- actual Supabase project;
- actual Linear project/work item;
- actual Cloudflare provider object or permitted domain/security status;
- provider account ownership and access boundaries;
- onboarding pair comparability and prior-familiarity balance;
- Evidence save location, retention and readers;
- whether four service classes should remain the intended Protocol minimum.

Unknowns remain unknown; none are converted to a pass.

## 11. Final readiness decision（最终就绪判断）

```text
FORMAL_COHORT_FREEZE_READY=false

REPOSITORY_MINIMUM_MET=false
AGENT_WORKFLOW_MINIMUM_MET=false
EXTERNAL_SERVICE_CATEGORY_MINIMUM_MET=false
OPERATIONAL_SURFACE_MINIMUM_MET=false

COHORT_FROZEN=false
EXPERIMENT_EXECUTION_AUTHORIZED=false
EXPERIMENT_EXECUTED=false
IMPLEMENTATION_AUTHORIZED=false
```

The current evidence is sufficient to reconcile the candidate set and to
identify real blockers. It is not sufficient to freeze a formal Cohort.

The next permitted action is Human review of:

1. exact repository/owner/custodian/source-window choices;
2. whether existing real projects can provide at least three additional
   countable service classes, including one operational surface;
3. whether a pre-existing Codex workflow can be independently referenced;
4. or whether the Protocol minimum should be revised through a separate,
   versioned Human Decision.

No experiment, integration or implementation follows automatically.

## 12. TITMAS Drift Check

```text
TITMAS_DRIFT_CHECK

PRIMARY_IMMUNE_OBJECTIVE_PRESERVED=true
SINGLE_HUMAN_MANAGEMENT_COST_REDUCED=NOT_MEASURED
NEW_CONTROL_AUTHORITY_CREATED=false
EXTERNAL_SERVICE_REPLACED=false
NEW_TRUTH_SOURCE_CREATED=false
DUPLICATE_COMPONENT_CREATED=false
CURRENT_CAPABILITY_OVERCLAIMED=false
IMPLEMENTATION_AUTHORIZED=false
TITMAS_DRIFT_STATUS=PASS_WITH_RECORDED_LIMITATIONS
```

