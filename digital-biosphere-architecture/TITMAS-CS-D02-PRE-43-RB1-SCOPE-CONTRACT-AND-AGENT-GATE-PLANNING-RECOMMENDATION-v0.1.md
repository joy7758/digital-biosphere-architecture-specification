---
document_id: DBA-TITMAS-CS-D02-PRE-43-RB1-SCOPE-CONTRACT-AND-AGENT-GATE-PLANNING-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-43 RB1 Scope Contract and Agent Gate Planning Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-43 RB1 范围、契约与智能体闸门规划建议 v0.1
version: 0.1.0
status: exact-recommendation-ready-not-decided
maturity: Development
recommendation_id: CS-D02-PRE-43
primary_repository: digital-biosphere-architecture
target_repository_modification_authorized: false
implementation_authorized: false
model_request_authorized: false
release_authorized: false
---

# TITMAS CS-D02 PRE-43 RB1 Scope Contract and Agent Gate Planning Recommendation v0.1

## Recommendation

```text
RECOMMENDATION=AUTHORIZE_DBA_ONLY_RB1_PACKAGE_AND_CONTRACT_SKELETON_PLANNING_PACKET_WITH_PRE_IMPLEMENTATION_AGENT_RECOMMENDATION_GATE
TARGET_REPOSITORY=https://github.com/joy7758/titmas-integrations.git
TARGET_BRANCH=codex/rb0-governance-baseline
TARGET_HEAD=f80629364752c465316b9d1238fe5447a88565ca
DBA_PLANNING_OUTPUTS_EXACT=7
TARGET_REPOSITORY_MODIFICATION_AUTHORIZED=false
PACKAGE_CREATION_AUTHORIZED=false
SOURCE_CREATION_AUTHORIZED=false
TEST_CREATION_AUTHORIZED=false
MODEL_REQUESTS_MAX=0
```

RB0 已按 exact `9610748…` 采纳，并在 target successor `f806293…` 同步 truth
surfaces。既有已采纳 baseline contract 把 RB1 定义为
`PACKAGE_AND_CONTRACT_SKELETON`：只允许 versioned package metadata、namespace 和
non-network contract types，Runtime effect 必须为 0。

PRE-43 不实现 RB1，只在 DBA 中冻结一个可供开发前智能体推荐审查的 planning packet。

## Exact Problem

RB1 planning 只针对：

```text
PROBLEM=PROVIDER_REQUEST_FAILURE_PHASE_ATTRIBUTION_WITH_DATA_MINIMIZATION
```

直接证据边界：

- PRE-28 的 provider request 在 HTTP response 前 timeout，但当时无法定位具体 phase；
- PRE-29 只证明 DNS/TCP/TLS 当次可达，不能证明 provider/model availability，也没有
  解决 PRE-28 timeout phase；
- PRE-30 已定义 P0-P9 phase contract、first-failure preservation 和 data minimization；
- PRE-31 只把 contract/Schema 采纳为 Development input；
- `VALID_PROBLEM_RECORDS=0`、`CS_G0_PASS=false`，因此不宣称外部市场需求或客户采用。

## Frozen Inputs

- [execution plan](commercialization-standards-titmas-integrations-rb1-planning/pre43-rb1-planning-plan.v0.1.json)；
- [plan Schema](commercialization-standards-titmas-integrations-rb1-planning/pre43-rb1-planning-plan.schema.v0.1.json)；
- [input manifest](commercialization-standards-titmas-integrations-rb1-planning/pre43-rb1-planning-input-manifest.v0.1.json)；
- [manifest Schema](commercialization-standards-titmas-integrations-rb1-planning/pre43-rb1-planning-input-manifest.schema.v0.1.json)；
- target branch `f806293…`；
- adopted contract SHA-256 `f72eb33…`；
- RB0 baseline contract SHA-256 `58920eb…`；
- PRE-42 validation SHA-256 `868aeaaa…`。

## Exact DBA-only Outputs

只允许在
`commercialization-standards-titmas-integrations-rb1-planning/` 新增七个规划 artifact：

1. `rb1-package-and-contract-skeleton-profile-v0.1.md`；
2. `rb1-package-and-contract-skeleton-profile.v0.1.json`；
3. `rb1-package-and-contract-skeleton-profile.schema.v0.1.json`；
4. `rb1-negative-boundary-case-catalog.v0.1.json`；
5. `rb1-negative-boundary-case-catalog.schema.v0.1.json`；
6. `rb1-agent-customer-review-input.v0.1.json`；
7. `rb1-agent-customer-review-input.schema.v0.1.json`。

这些 artifact 必须表达：

- distribution/import namespace/public API/minimum Python 仍是 candidate，未采纳；
- provider-neutral core 不依赖 provider SDK、DBOS Runtime 或 SAEE execution；
- no-network、no-credential、no-retry、no-fallback、no-JSON-repair；
- Observation 不自动成为 Evidence，Schema pass 不自动成为 provider correctness 或
  conformance；
- source/package/tests/implementation/provider support/Runtime/release 仍为 0/false；
- RB1 implementation Decision 前必须完成独立 Agent Customer Review。

## Pre-implementation Agent Recommendation Gate

规划包必须冻结这个问题：

> 如果智能体开发者需要定位模型／Provider 请求在 P0-P9 哪个阶段首次失败，同时禁止保存
> credential、raw payload、prompt、review content 或 hidden reasoning，智能体是否会推荐
> TITMAS 的 provider-neutral RB1 package/contract skeleton？

审查必须输出：

1. `RECOMMENDED`、`CONDITIONALLY_RECOMMENDED` 或 `NOT_RECOMMENDED`；
2. 推荐／不推荐原因；
3. 接口学习成本和与 OpenTelemetry／现有 HTTP instrumentation 的重复风险；
4. 在实现前必须修正的 agent-readable discovery、API、security 和 boundary 问题；
5. 是否愿意推荐、调用或复用该 package skeleton；
6. 明确“推荐不是 Implementation Authorization”。

PRE-43 不发送模型请求。后继 PRE-44 必须有独立 recommendation、Decision、冻结输入、
request budget、sanitized sink 和失败保留。

## Duplication and Authority Boundary

- RB1 不是 Agent Framework、Runtime、DBOS、SAEE、Evidence Authority 或 Permission
  service；
- RB1 不复制 OpenTelemetry Collector 或通用 telemetry pipeline；
- OTLP/SemConv 只可作为未来 mapping reference，不等于兼容或支持；
- RB1 contract event 是 Observation metadata，不是 Evidence、Truth、Verification、
  Evaluation、Decision、Authorization 或 Execution；
- provider binding、network request、credential read、actual phase observation 和
  conformance execution 全部不在 PRE-43。

## All Effects

| effect class | result |
|---|---|
| Architecture Authority | `UNCHANGED` |
| Ownership | `UNCHANGED` |
| Implementation | `NOT_AUTHORIZED_NOT_CREATED` |
| Target repository modification | `NOT_AUTHORIZED_NOT_EXECUTED` |
| Package / source / tests | `NOT_AUTHORIZED_NOT_CREATED` |
| Agent review | `REQUIRED_LATER_NOT_AUTHORIZED_NOT_EXECUTED` |
| Provider / model / credential action | `ZERO` |
| Provider support / conformance | `NOT_CREATED_NOT_CLAIMED` |
| Runtime / DBOS / SAEE | `UNCHANGED` |
| Commercial Offering | `NOT_AUTHORIZED_NOT_CREATED` |
| Certification | `NOT_AUTHORIZED_NOT_CREATED` |
| Release | `NOT_AUTHORIZED` |
| Permission | `NOT_GRANTED` |
| Evidence Truth | `UNCHANGED` |

## Stop Conditions

任何 canonical input、digest、target branch/commit、RB0 adoption、Schema、output count、
problem scope 或 boundary 漂移，或需要 target write、package、source、tests、provider
SDK、network、model、credential、Runtime、DBOS/SAEE change、merge、PR、tag、release、
deployment、Certification、Production、customer 或 commercial claim 时 fail closed。

## Standing Directive Assessment

该建议固定 exact problem、canonical inputs、target revision、七个 DBA-only output、零
external action、全部 effects、validation 和 stop rules，满足
`TITMAS-CS-STANDING-001` 候选条件，但仍须独立 Decision。
