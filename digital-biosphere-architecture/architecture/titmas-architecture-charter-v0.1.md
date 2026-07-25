---
document_id: DBA-TITMAS-ARCHITECTURE-CHARTER-0.1
title: TITMAS Architecture Charter v0.1
title_zh: TITMAS 架构章程 v0.1
status: proposed-concept-boundary-freeze-review-required
maturity: Development
maturity_scope: entire-document
owner_ref: NOT_ASSIGNED
decision_reference: NOT_DECIDED
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Development document; no implementation compatibility claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
classification: strategic-subdomain-technical-infrastructure-architecture
primary_repository: digital-biosphere-architecture
decision_status: REVIEW_REQUIRED
community_direction_status: accepted-strategic-direction-community-not-established
community_strategy_reference: titmas-infrastructure-developer-community-strategy-v0.1.md
community_decision_reference: ADR-029-titmas-infrastructure-developer-community-direction.md
community_established: false
foundation_in_scope: false
agent_recommendation: CONDITIONALLY_RECOMMENDED
implementation_authorized: false
execution_authorized: false
repository_created: false
code_created: false
release_authorized: false
production_ready: false
created_at: 2026-07-23
---

# TITMAS Architecture Charter v0.1

中文：TITMAS（Trusted Infrastructure for Trustworthy Multi-Agent Systems，
可信多智能体系统可信基础设施）架构章程 v0.1。

关系和命名边界的短入口见
[`titmas-dba-relationship.md`](titmas-dba-relationship.md)。本章程继续受
[`open-infrastructure-strategy-constitution.md`](open-infrastructure-strategy-constitution.md)、
[`trusted-multi-agent-protocol-specification.md`](trusted-multi-agent-protocol-specification.md)、
[`saee-dbos-contract.md`](saee-dbos-contract.md) 与
[`interface-boundary-rules.md`](interface-boundary-rules.md) 约束。

## 1. Charter Status（章程状态）

本章程用于冻结 TITMAS 的使命、职责、非目标、权力边界、互操作原则和未来项目组织
候选。`freeze` 在这里仅表示“后续提案必须显式说明是否改变这些边界”，不表示 TITMAS
已进入 DBA Portfolio、已实现、已部署、已获采用或已取得生产授权。

现有生产主线保持 `NEW_PRODUCTION_TECHNICAL_SPECIFICATION_ALLOWED=false`。本章程是由
2026-07-23 明确指令触发的 concept-boundary proposal（概念边界提案），不修改既有
`PR-G2A`、`DQ-019`–`DQ-021` 或其他生产 gate 的优先级和状态。

```text
TITMAS_CHARTER_DEFINED=true
TITMAS_IS_STRATEGIC_SUBDOMAIN=true
TITMAS_CHARTER_ADOPTED=false
TITMAS_PORTFOLIO_ADMITTED=false
TITMAS_IMPLEMENTED=false
TITMAS_RUNTIME_CREATED=false
TITMAS_REPOSITORY_CREATED=false
```

## 2. Mission（使命）

TITMAS 的使命是建立 vendor-neutral、framework-neutral、evidence-aware 和
fail-closed（供应商中立、框架中立、证据感知、失败关闭）的可信多智能体技术基础设施
架构，使不同 Agent Framework、治理执行层、可观测性系统、工具协议、证据组件、审计
组件和演化评价引擎可以在不混淆各自 Authority 与 Truth Owner 的情况下互操作。

一句话定位：

> TITMAS defines the trusted interoperability fabric; it does not become the
> owner of every connected system.

中文：TITMAS 定义可信互操作织层，但不成为所有接入系统的所有者。

## 3. Architecture Classification（架构分类）

| proposal question | v0.1 answer |
|---|---|
| 属于什么类型？ | `STRATEGIC_SUBDOMAIN / TECHNICAL_INFRASTRUCTURE_ARCHITECTURE_DOMAIN` |
| primary repository 是什么？ | 当前仅为 DBA 文档；未来实现仓库未决定 |
| 是否强化开放标准和复用？ | 是；优先 profile、adapter、schema mapping 和 conformance |
| 是否是 Program Governance？ | 否；Portfolio、Roadmap、Decision、Risk 和 Gate 仍属于 DBA |
| 是否是 Agent Framework？ | 否；LangChain、CrewAI 等保持独立 framework truth |
| 是否是 DBOS replacement？ | 否；DBOS 保持存在和运行记录责任域 |
| 是否是 SAEE service？ | 否；SAEE 核心算法和演化智能不进入公共基础设施 |
| 是否已实现？ | 否；v0.1 只有架构章程和关系说明 |

## 4. Responsibilities（TITMAS 负责什么）

TITMAS 架构域负责定义未来可独立实现、可替换和可做符合性测试的以下边界：

1. **Framework Adapter Contract（框架适配契约）**：规定如何从 LangChain、CrewAI、
   Microsoft Agent Governance Toolkit（AGT）和其他 Runtime 获取有来源的 lifecycle、
   model、tool、delegation、policy-decision 与 failure events；
2. **MCP Trust Handoff（MCP 可信交接）**：规定 tool discovery、tool call、result、
   consent、approval、server identity、schema drift 和 audit material 如何交接，但不把
   MCP tool 说明升级为 Capability 或 Permission；
3. **Observation Mapping（观察映射）**：复用 OpenTelemetry 的 Context、Resource、
   Trace、Metric、Log、OTLP 和 Semantic Conventions，并保持 Telemetry 只是 observation
   material；
4. **Evidence-material Handoff（证据材料交接）**：在 Agent Evidence Layer、EEOAP、
   ARO / PRA-Server 与 DBOS admission 之间规定 provenance、version、scope、integrity、
   failure 和 limitation 字段；
5. **Correlation and Lineage（关联与谱系）**：规定跨 framework/runtime/tool/trace/
   evidence/evaluation 引用如何相关联，同时禁止把 correlation ID 当作 Identity；
6. **Profile and Version Negotiation（配置与版本协商）**：为每个外部生态固定
   `source`, `version/commit`, `stability`, `supported`, `unsupported` 和 upgrade review；
7. **Conformance Boundary（符合性边界）**：定义未来 adapter/profile 的正例、负例、
   fail-closed、privacy、authority-elevation 和 unknown-retention 测试义务；
8. **Agent-readable Discovery（智能体可读发现）**：为编码、检索和引用智能体提供稳定
   document ID、Owner、输入输出、非目标、状态常量和 canonical source link。

这些职责是 architecture ownership（架构职责），不是当前 capability truth（能力事实）。

## 5. Explicit Non-responsibilities（明确不负责什么）

TITMAS 不负责：

- Program Portfolio、Roadmap、Sprint、Issue、人员、预算或项目进度管理；
- 创建或管理 DBOS Identity、Capability、Permission、Lifecycle 或 canonical Evidence；
- 复制 TMAP、EEOAP、MCP、OTLP 或任何外部协议成为第二规范权威；
- 实现 LangChain、CrewAI 或 Microsoft AGT 已经拥有的 Agent orchestration、policy engine、
  trust engine、sandbox、fleet management 或 framework Runtime；
- 把 OpenTelemetry Trace/Metric/Log、framework callback、MCP receipt 或 audit log 直接
  宣称为 Evidence、Verification、Truth、Fitness 或 Authorization；
- 公开、复制、重实现、托管或远程调用 SAEE 核心算法和演化智能；
- 自动执行 SAEE Recommendation、AGT verdict、ARO audit result 或 PRA review result；
- 创建新的最高治理层、Architecture Authority、Operational Authority 或 Evolution
  Authority；
- 因命名中含 `Trusted` 就产生认证、合规、客户采用或 production-ready 声明。

## 6. Capability and Truth Ownership Matrix（能力与事实归属矩阵）

下表冻结“谁继续负责什么”。TITMAS 的默认角色是 `MAPPER / ADAPTER CONTRACT OWNER`，
不是连接对象的 canonical Owner。

| domain/component | 保留职责 | TITMAS 只做 | TITMAS 不得做 |
|---|---|---|---|
| DBA | 总项目战略、架构规则、TMAP、Portfolio、Decision、Gate、Risk、ADR | 在 DBA 规则内提交互操作架构提案 | 建立第二治理驾驶舱或绕过 ADR |
| DBOS | Identity、Capability record、Execution record、Evidence、Verification、Lifecycle | 定义 observation/evidence material 到 DBOS admission 的接缝 | 建立平行 Identity/Evidence/Permission store |
| SAEE | Evaluation、Reliability、Stability、Risk、Fitness、Adaptation、Evolution Recommendation | 只读、版本化、evidence-bound input/output contract | 公开或复制核心算法、写回 DBOS、执行建议 |
| EEOAP | 执行证据与操作问责的规范要求、profile 和 validator 语义；精确 canonical source 待下一阶段核验 | 做 requirements/profile mapping | 改写 EEOAP 或把 mapping 写成 adoption |
| Agent Evidence Layer | 执行到证据材料的 capture/package/validation surface；精确仓库能力待核验 | 规定 handoff、provenance 和 correlation contract | 自动把 package 升级为 DBOS Evidence Truth |
| ARO / PRA-Server | 候选 audit、review、replay 或 verification provider；精确边界待核验 | 规定 bounded result interface 和 scope preservation | 自动采用结果或宣称其为全局 Verification |
| Microsoft AGT | 外部 policy enforcement、identity/trust、audit、framework/MCP integration surface | 适配 verdict/event/audit handoff，记录 exact version/stability | fork 其完整 stack、把 trust score 当 SAEE Fitness、把 AGT identity 当 DBOS Identity |
| LangChain / CrewAI | Agent framework 与 orchestration truth | 从官方 hook/event/callback surface 获取有来源事件 | 复制 framework，或把角色/状态当 canonical Identity/Execution |
| OpenTelemetry | observation protocol、SDK、Collector、signals、context 和 semantic conventions | 复用并建立版本化 profile | 自建第二 telemetry protocol，或把 telemetry 当 Evidence/Truth |
| MCP | context/tool/resource/prompt 互操作协议 | 规定 consent、tool-call、result、schema/version 和 audit 接缝 | 把 tool annotation 当可信 Capability/Permission |

## 7. Logical Architecture Planes（逻辑架构平面）

```text
Agent Framework and Tool Plane
  LangChain | CrewAI | other runtimes | MCP clients/servers
        ↓ source-preserving adapter events
Governance Enforcement Plane
  Microsoft AGT or other independently owned policy/enforcement providers
        ↓ verdict + policy/version + audit material; no authority promotion
Observation Plane
  OpenTelemetry Context/Resource/Trace/Metric/Log/OTLP
        ↓ provenance, redaction, version, loss/duplicate handling
TITMAS Interoperability Fabric
  adapter contracts | profiles | correlation | handoff | conformance
        ↓ material, never automatic Truth
Evidence and Verification Interfaces
  Agent Evidence Layer | EEOAP | ARO / PRA-Server
        ↓ explicit DBOS admission and canonical object ownership
DBOS Existence Plane
  Identity | Capability | Execution | Evidence | Verification | Lifecycle
        ↓ read-only, versioned, bounded contract
SAEE Evolution Plane
  Evaluation | Fitness | Risk | Stability | Evolution Recommendation
        ↓ explicit Human Review and Decision
DBA / Governance Plane
  architecture rule | adoption | authorization | release gate
```

该图是 information-flow candidate（信息流候选），不是 implementation topology（实现拓扑）。
任何跳过 DBOS admission、直接把 telemetry/framework event 送入 SAEE 形成 canonical
评价的路线，v0.1 默认 `REJECTED`。

## 8. Interoperability Principles（互操作原则）

### `TITMAS-INT-001`: Adapter, not fork

优先构建薄 adapter、profile 和 conformance contract，不 fork 或重实现完整 Agent
Framework、Microsoft AGT、OpenTelemetry Collector 或 MCP stack。

### `TITMAS-INT-002`: Exact source binding

每个 integration profile 必须固定 official source、version/tag/commit、stability、license、
observed_at 和 upgrade trigger。`latest`、文档截图或 package name 不能成为长期合同。

### `TITMAS-INT-003`: Preserve source semantics

每个事件必须保留 source framework、source object type、source event name、source version、
original timestamp、ingest timestamp、scope、limitations 和 raw reference。归一化不得删除
失败、重试、未知、冲突、采样、丢失或重复语义。

### `TITMAS-INT-004`: No semantic elevation

```text
Framework role != DBOS Identity
Tool registration != Capability Authorization
Tool call != correct Execution
Policy verdict != Program Decision
Trace/span != Evidence Object
Audit receipt != Verification
Trust score != SAEE Fitness
Evaluation != Permission
Recommendation != Execution
```

### `TITMAS-INT-005`: Fail closed and retain unknowns

版本不支持、来源不明、签名无效、schema drift、correlation 冲突、敏感字段策略未知、
input 不完整或 adapter exception 时，必须保留 `unsupported`、`unknown`、`conflicted`、
`partial` 或 `failed`，不得静默构造成功记录。

### `TITMAS-INT-006`: SAEE is read-only and advisory-only

TITMAS 到 SAEE 的接口只能提供有来源、版本化、有 Evidence/Verification limitation 的
只读输入；SAEE 输出只能作为 Evaluation/Recommendation，不得通过 TITMAS 写回 DBOS、
framework、MCP server、AGT policy 或执行环境。

### `TITMAS-INT-007`: Vendor and framework neutrality

一个 framework/provider 的事件模型不能成为 TITMAS canonical model。共同语义应通过
TMAP、EEOAP、OTel/MCP 官方契约和显式 mapping 表达；不兼容部分必须保留为 profile-
specific extension（配置特定扩展）。

### `TITMAS-INT-008`: Privacy and least data

默认不采集 prompt、response、tool payload、credential、PII 或 secret。需要内容时必须有
purpose、consent/authorization、redaction、retention、tenant boundary 和 deletion policy；
可观测性需求不能自动扩大 Evidence 收集范围。

## 9. SAEE Core Protection Boundary（SAEE 核心保护边界）

TITMAS 可以公开或共享的 SAEE 表面仅限：

- versioned input contract（版本化输入契约）；
- minimal Evaluation/Recommendation output contract（最小评价／建议输出契约）；
- supported/unsupported profile 和 fail-closed semantics；
- evidence、model/version、scope、uncertainty 和 limitation 引用要求；
- adapter conformance cases，不包含核心算法实现。

以下能力继续属于 SAEE 核心，不进入 TITMAS 公共基础设施：

- Fitness、Reliability、Stability 和 Risk 的内部模型、权重与组合逻辑；
- world model、counterfactual simulation、evolution modeling；
- genome/trait extraction、branching、mutation、recombination；
- selection、dormancy、rollback、next-generation orchestration；
- ecological simulation、proprietary heuristics、训练数据、内部 prompt、模型工件；
- 对算法访问、开源、授权、商业许可或远程服务化的决定。

```text
SAEE_PUBLIC_INTERFACE_BOUNDED=true
SAEE_CORE_ALGORITHMS_PUBLIC_INFRASTRUCTURE=false
SAEE_CORE_SOURCE_DISCLOSURE_AUTHORIZED=false
SAEE_REMOTE_ALGORITHM_SERVICE_AUTHORIZED=false
SAEE_WRITEBACK_ALLOWED=false
SAEE_RECOMMENDATION_IS_COMMAND=false
```

具体公开范围、许可证和实现形式只能由 SAEE canonical source、Domain Owner 与独立
Human Decision 决定，TITMAS 章程无权代替。

## 10. Ecosystem Interoperability Baseline（生态互操作基线）

下列外部资料只作为 `REFERENCE_ONLY` 输入，observed at `2026-07-23`。引用不表示 DBA
或 TITMAS 已采用、实现或验证对应项目。

| ecosystem | official reference | TITMAS v0.1 interpretation |
|---|---|---|
| Microsoft Agent Governance Toolkit | [official repository](https://github.com/microsoft/agent-governance-toolkit), [architecture](https://microsoft.github.io/agent-governance-toolkit/ARCHITECTURE/), [framework adapters](https://microsoft.github.io/agent-governance-toolkit/tutorials/28-build-custom-integration/) | 作为外部治理执行与 adapter provider；其 Public Preview / component status 必须逐版本核验 |
| LangChain | [custom middleware hooks](https://docs.langchain.com/oss/python/langchain/middleware/custom) | 候选事件截取点；hook 执行不自动成为 DBOS Execution |
| CrewAI | [official documentation](https://docs.crewai.com/) | Crew/Task/Flow/callback/event 为 framework-owned source；角色与流程状态不自动提升 |
| OpenTelemetry | [specification](https://opentelemetry.io/docs/specs/otel/), [GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/) | observation layer；Development 字段必须 version-pinned、fail-closed |
| MCP | [architecture overview](https://modelcontextprotocol.io/docs/learn/architecture), [tools specification](https://modelcontextprotocol.io/specification/latest/server/tools) | tools/resources/prompts 与 JSON-RPC 接缝；tool annotations 和 results 必须按 untrusted input 处理 |

所有未来 adapter 必须在实现前重新核验官方文档、包身份、license、release status 和
stability。现有 DBA 已采纳的 exact OpenTelemetry references 继续由对应 ADR/profile 治理，本表不
创建第二套 version authority。

## 11. Infrastructure Developer Community Direction（基础设施开发者社区方向）

TITMAS 的开发者社区方向已由
[`ADR-029`](ADR-029-titmas-infrastructure-developer-community-direction.md) 采纳。规范名称为：

```text
English: TITMAS Infrastructure Developer Community
Chinese: TITMAS 可信多智能体基础设施开发者社区
Subtitle: Developer Community for Trusted Multi-Agent Infrastructure
```

该方向服务于开放规范、Adapter contract、Conformance、参考实现边界、文档、本地化和
agent-readable discovery。它不建立普通 Agent 社区，不开发 Agent Framework，也不创建
基金会或第二个 DBA。

社区组织方式重度参考 OpenTelemetry，但只参考：

- specification、implementation 与 contrib surface 分离；
- 每份规范独立声明 maturity 和 version；
- 实现声明其支持的规范版本；
- Proposal、Review、Decision、Implementation 和 Conformance 分离；
- 首次贡献入口、公开记录和文档贡献；
- 只有在真实工作、参与者和 Owner 形成后才建立 SIG。

社区方向已经采纳，不改变本章程其余 `REVIEW_REQUIRED` 状态。Authority Freeze、
Interface v0.1、公共贡献表面、仓库、SIG、Maintainer、Adapter 和外部动作仍须分别获得
明确决定。

完整社区路线和防跑偏检查见
[`TITMAS Infrastructure Developer Community Strategy v0.1`](titmas-infrastructure-developer-community-strategy-v0.1.md)。

```text
TITMAS_INFRASTRUCTURE_DEVELOPER_COMMUNITY_DIRECTION_ADOPTED=true
TITMAS_DEVELOPER_COMMUNITY_ESTABLISHED=false
TITMAS_PUBLIC_CONTRIBUTION_SURFACE_AUTHORIZED=false
TITMAS_FOUNDATION_IN_SCOPE=false
```

## 12. Future GitHub Project Organization（未来 GitHub 项目组织）

`ADR-030` 已选择 `titmas-cn` 作为 GitHub Organization slug；本节只设计 logical
organization（逻辑组织），不创建 Organization，不创建仓库，不移动文件，也不改变现有
项目归属。GitHub slug 不能包含 `.`，因此不使用 `titmas.cn`。

```text
TITMAS logical GitHub organization (selected slug: titmas-cn; NOT_CREATED)
  ├─ Governance and architecture
  │    └─ digital-biosphere-architecture
  │         ├─ architecture/titmas-dba-relationship.md
  │         └─ architecture/titmas-architecture-charter-v0.1.md
  │
  ├─ Existing independent truth owners (unchanged; verify next phase)
  │    ├─ DBOS source
  │    ├─ SAEE source
  │    ├─ Agent Evidence / Agent Evidence Layer source(s)
  │    ├─ EEOAP canonical source
  │    └─ ARO / PRA-Server source(s)
  │
  └─ Future TITMAS implementation candidates (NOT_CREATED)
       ├─ titmas-conformance
       ├─ titmas-adapters
       │    ├─ microsoft-agt profile
       │    ├─ langchain profile
       │    ├─ crewai profile
       │    ├─ opentelemetry profile
       │    └─ mcp profile
       └─ titmas-reference-topology
```

组织规则：

1. v0.1 只在 DBA 保存 Charter 和 relationship；不创建 `titmas-core`；
2. 不把 SAEE、EEOAP、agent-evidence、ARO、PRA-Server 或 DBOS 移入 TITMAS 目录；
3. `titmas-adapters` 默认是未来单一候选仓库，只有 release cadence、language、security
   boundary 或 Owner 明显分离时才考虑拆分；
4. `titmas-conformance` 只保存跨实现的 contract/fixtures/validator 候选，不成为任何子项目
   capability/evidence truth；
5. `titmas-reference-topology` 若未来存在，只能是可替换的 reference deployment，不是
   production service 或 canonical Runtime；
6. 每个仓库必须有一个 canonical status source、Owner、license、version policy 和
   `AGENTS.md`；
7. GitHub Project board、Issue label 或目录层级不改变项目 Authority、Truth Owner 或
   Portfolio 状态。

```text
GITHUB_ORGANIZATION_SLUG_SELECTED=true
GITHUB_ORGANIZATION_SLUG=titmas-cn
GITHUB_ORGANIZATION_CREATED=false
NEW_REPOSITORIES_CREATED=false
EXISTING_REPOSITORIES_MOVED=false
TITMAS_CORE_REPOSITORY_PROPOSED=false
FUTURE_REPOSITORY_PLAN_IS_AUTHORIZATION=false
```

完整 profile、repository navigation 和创建前检查单见
[`TITMAS GitHub Organization Information Architecture v0.1`](titmas-github-organization-information-architecture-v0.1.md)。

## 13. Pre-development Agent Recommendation Gate（开发前智能体推荐闸门）

问题：如果潜在用户需要把多个 Agent Framework、治理工具、MCP tool server、
OpenTelemetry observation、执行证据规范和演化评价引擎连接成边界清晰、可替换、可审计
的基础设施，我是否会推荐 TITMAS？

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=ARCHITECTURE_BOUNDARY_AND_INTEROPERABILITY_DOMAIN
NOT_RECOMMENDED_AS=RUNTIME_OR_PROJECT_MANAGEMENT_SYSTEM
NOT_RECOMMENDED_AS=DBA_DBOS_TMAP_OR_SAEE_REPLACEMENT
IMPLEMENTATION_RECOMMENDED_NOW=false
```

### 13.1 Why not unconditionally recommended（为何不是无条件推荐）

| 不推荐原因 | v0.1 修正 | 剩余缺口 / 停止条件 |
|---|---|---|
| 与已有 TMAI、TMAP、DBOS 名称和职责高度重叠 | 本章程固定 public positioning、protocol、existence runtime 与 interop domain 的差异 | 完成 canonical naming review；未完成前不对外重命名 |
| 容易退化成“大目录 + 总项目管理系统” | 明确无 Portfolio/Project/Sprint 管理权，禁止移动现有仓库 | 下一阶段只做 read-only ownership map，不搬迁 |
| EEOAP、Agent Evidence Layer、ARO、PRA-Server 的精确当前归属尚未在本阶段核验 | 所有角色均标为 interface candidate / source to verify | canonical source、Owner、version 不明时不得写实现任务 |
| 外部生态变化快，adapter 容易绑定 moving target | 强制 exact source/version/stability/license profile | 未钉住版本和 upgrade policy 时不得实现 |
| SAEE 接入可能泄露或公共化核心演化智能 | 固定 contract-only、read-only、no-writeback、no-core-disclosure | SAEE Owner 未明确批准公开表面时不得扩展接口 |
| evidence、audit、telemetry、policy verdict 容易互相升级 | 固定 no-semantic-elevation 和 DBOS admission boundary | 负例/conformance contract 未定义时不得实现 |

### 13.2 Remaining human decisions（剩余人工决定）

- 是否接受 TITMAS 作为 DBA 下的正式 `ARCHITECTURE_DOMAIN`；
- 是否保留 `TITMAS` 名称，及其与 `TMAI` 的对外关系；
- 哪些现有项目进入正式 Portfolio，哪些只作为 external/adjacent dependency；
- 是否以及何时创建未来 adapter/conformance repository；
- 哪个责任方拥有实现、security review、release 和 operation；
- SAEE 可公开的最小 contract、license 和 access model。

Agent recommendation 不是 Architecture Decision 或 Implementation Authorization。

## 14. Staged Route and Stop Conditions（分阶段路线与停止条件）

| stage | 目标 | 允许产物 | 明确禁止 |
|---|---|---|---|
| `T0` Concept Boundary Freeze | 当前阶段 | 本章程、关系说明、最小 README 入口 | 代码、仓库、搬迁、Portfolio 状态升级 |
| `T1` Ownership and Project Map | 下一阶段 | read-only source/Owner/capability/overlap map | 修改子仓库、假定归属、统一重命名 |
| `T2` Architecture Decision | 人工审查 | ADR、accepted/rejected scope、primary repository decision | 用 Charter 自动采纳 |
| `T3` Contract and Conformance Design | 经授权后 | adapter/profile/schema/test obligations | Runtime、endpoint、真实数据 |
| `T4` Bounded Implementation | 独立授权后 | 一个精确 adapter/conformance slice | 大爆炸集成、SAEE core 暴露、生产声明 |
| `T5` External Ecosystem Route | 独立审查后 | upstream issue/PR plan、compatibility report | 未授权外部联系、PR、发布或 adoption claim |

任一阶段出现以下情况必须停止：

- 找不到 canonical source 或 Owner；
- 与 DBOS、SAEE、EEOAP、TMAP 或外部生态存在重复 canonical Owner；
- 需要公开 SAEE 核心算法才能继续；
- 需要把 telemetry/audit/framework result 自动升级为 Evidence/Truth/Permission；
- 需要在没有 exact version 和 conformance negatives 的情况下实现；
- 需要创建新仓库、push、PR、external issue、release 或部署而没有明确授权。

## 15. Non-claims（非声明）

```text
TITMAS_ARCHITECTURE_CHARTER_V0_1_DEFINED=true
TITMAS_RELATIONSHIP_TO_DBA_DEFINED=true
TITMAS_INFRASTRUCTURE_DEVELOPER_COMMUNITY_DIRECTION_ADOPTED=true
TITMAS_DEVELOPER_COMMUNITY_ESTABLISHED=false
TITMAS_FOUNDATION_IN_SCOPE=false
TITMAS_CONCEPT_BOUNDARY_PROPOSED=true
TITMAS_CONCEPT_BOUNDARY_ADOPTED=false
TITMAS_PROJECT_MAP_CREATED=false
TITMAS_PORTFOLIO_ADMISSION_DECIDED=false
TITMAS_IMPLEMENTATION_MAPPING_CREATED=false
TITMAS_CODE_CREATED=false
TITMAS_REPOSITORY_CREATED=false
TITMAS_ADAPTER_IMPLEMENTED=false
TITMAS_CONFORMANCE_VALIDATOR_IMPLEMENTED=false
MICROSOFT_AGT_ADOPTED=false
LANGCHAIN_INTEGRATION_IMPLEMENTED=false
CREWAI_INTEGRATION_IMPLEMENTED=false
OPENTELEMETRY_RUNTIME_INTEGRATION_CREATED=false
MCP_INTEGRATION_IMPLEMENTED=false
AGENT_EVIDENCE_LAYER_OWNERSHIP_CHANGED=false
EEOAP_OWNERSHIP_CHANGED=false
SAEE_CORE_EXPOSED=false
DBOS_AUTHORITY_CHANGED=false
EXTERNAL_ACTION_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
EXECUTION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
PRODUCTION_READY=false
```
