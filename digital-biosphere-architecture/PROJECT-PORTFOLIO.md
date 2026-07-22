---
document_id: DBA-PROJECT-PORTFOLIO-0.1
title: Digital Biosphere Project Portfolio v0.1
title_zh: 数字生物圈项目组合 v0.1
status: developer-preview-released-production-implementation-mapping-complete
as_of_date: 2026-07-22
source_policy: reference-only
changes_project_ownership: false
changes_project_status: false
---

# Digital Biosphere Project Portfolio v0.1（数字生物圈项目组合 v0.1）

## 1. Portfolio Tiers（项目组合层级）

| tier | 中文含义 | 准入含义 |
|---|---|---|
| `CORE` | 核心项目 | Digital Biosphere 总目标不可缺少的责任域；不表示仓库被 DBA 所有 |
| `PILOT` | 试验项目 | 用于验证架构契约的受控应用或研究工作流；不表示已实现或已授权执行 |
| `LOGICAL_LAYER` | 逻辑层 | 架构中需要但尚不一定有独立软件仓库的责任边界 |
| `ADJACENT_CANDIDATE` | 相邻候选项目 | 可能复用或接入，但尚未完成项目准入、Owner 和集成边界确认 |
| `OUT_OF_SCOPE` | 当前范围外 | 当前项目群不管理；若未来接入必须重新审查 |

## 2. Core Portfolio（核心项目组合）

| project_id | tier | 项目 | DBA 中的职责 | canonical project source（项目规范来源） | 当前组合状态 | 下一 gate |
|---|---|---|---|---|---|---|
| `DBA` | `CORE` | Digital Biosphere Architecture | Program Governance Hub（项目群治理中心）+ Architecture Specification Hub（架构规范中心）+ Protocol Governance（协议治理）+ Public Entry Governance（公开入口治理） | 本仓库 `README.md`、`PUBLIC-PROJECT-OVERVIEW.md`、`PROGRAM-CHARTER.md`、`architecture/`、ADR | `PRODUCTION_ARCHITECTURE_CONTENT_FROZEN_REMOTE_VERIFICATION_PENDING` | `DQ-022`–`DQ-025` reference、`ADR-024` sequence 与 `DQ-018` bounded implementation decisions 已记录；content commit/tree 已冻结；DQ-020 profiles 仍只是未来输入和 `BLOCKED_INPUT`，不自动授权实现／测量 |
| `DBOS` | `CORE` | Digital Biosphere Operating System | Trusted Multi-Agent Existence Infrastructure（可信多智能体存在基础设施）和 Developer Infrastructure（开发者基础设施） | remote `main@cd3f867...`、README、SDK、`entity_support/`、schemas、tests 与 validators | `DEVELOPER_PREVIEW_RELEASED_PR_G1_MAPPED_PRODUCTION_CORE_MISSING` | 由 `DQ-018` 决定受限 Telemetry admission foundation；不得把现有 JSON records 写成 production durability |
| `SAEE` | `CORE` | Digital Biosphere Evolution Engine | Evolution Intelligence Layer（演化智能层） | `/Users/zhangbin/GitHub/SAEE/STRATEGIC_ALIGNMENT.md`、`PROJECT_STATUS.md`、Capability inventory（能力清单）及其证据文件 | `PUBLIC_READ_ONLY_DEVELOPER_PREVIEW_ADAPTER_RELEASED_ADVISORY_ONLY` | 提供生产适配隔离与版本映射；保持 canonical capability truth 不变 |
| `GOVERNANCE-DECISION` | `LOGICAL_LAYER` | Governance Decision Layer（治理决策层） | Recommendation 到 Decision、Adoption 的记录边界 | DBA 的 `governance-decision-model.md`、状态机与 ADR | `MODEL_DEFINED_IMPLEMENTATION_NOT_ASSESSED` | 指定 deployment-specific decision authority（部署特定决策责任） |
| `TMAP` | `LOGICAL_LAYER` | Trusted Multi-Agent Protocol（可信多智能体协议） | Identity、Capability、Execution、Evidence、Verification 与 Evolution Interface 的开放互操作契约 | DBA 的 `trusted-multi-agent-protocol-specification.md`、`PRODUCTION-IMPLEMENTATION-MAPPING-REPORT.md`、版本治理与 ADR-023 | `PR_G1_MAPPING_COMPLETE_IMPLEMENTATION_NOT_AUTHORIZED` | 审查 `DQ-018`；schema/version 只能在实施仓库按 gate 落地 |
| `RESEARCH-AGENT-PILOT` | `PILOT` | Research Agent Pilot（科研智能体试验） | 第一个 Operational Digital Entity（运行型数字主体）参考试验 | `/Users/zhangbin/GitHub/digital-biosphere-research-agent-pilot/README.md`、`CONSTITUTION.md`、readiness gate（就绪闸门） | `SPECIFICATION_ONLY_NOT_READY` | 完成人工复核、来源批准和原型授权前置条件 |

## 3. Adjacent Candidate Portfolio（相邻候选项目组合）

这些项目已在架构映射或本地发现中出现，但 v0.1 不把它们自动纳入核心治理、依赖或发布计划。

| candidate_id | 本地发现路径 | 候选角色 | 当前准入状态 | 必须回答的问题 |
|---|---|---|---|---|
| `POP` | `/Users/zhangbin/GitHub/persona-object-protocol` | Identity / Persona adjacent component（身份／人格相邻组件） | `MAPPING_ONLY_REVIEW_REQUIRED` | 与 DBOS canonical identity 的 Owner 和映射边界是什么？ |
| `ARO` | `/Users/zhangbin/GitHub/aro-audit` | Audit / Verification adjacent component（审计／验证相邻组件） | `MAPPING_ONLY_REVIEW_REQUIRED` | 与 DBOS Verification、Agent Evidence 的阶段和数据所有权如何分离？ |
| `AGENT-EVIDENCE` | `/Users/zhangbin/GitHub/agent-evidence` | Execution-to-evidence component（执行到证据组件） | `MAPPING_ONLY_REVIEW_REQUIRED` | 哪些记录是 canonical Evidence，哪些只是 receipt（回执）或 transport（传输）？ |
| `TOKEN-GOVERNOR` | `/Users/zhangbin/GitHub/token-governor` | Resource governance adjacent component（资源治理相邻组件） | `MAPPING_ONLY_REVIEW_REQUIRED` | DBOS 运行约束与 SAEE 资源评价之间的责任边界是什么？ |
| `ACP` | `/Users/zhangbin/GitHub/海洋/autonomous-cell-protocol` | Physical Cell protocol（物理单元协议） | `MAPPING_ONLY_REVIEW_REQUIRED` | Physical Cell Identity 与 DBOS Entity Identity 如何保持不等同？ |

本地路径只证明在 2026-07-21 的工作区发现了候选目录，不证明其当前能力、维护状态、发布状态、项目所有权或已接入 Digital Biosphere。

## 4. Portfolio Admission Rules（项目组合准入规则）

项目进入 `CORE` 或 `PILOT` 前必须：

1. 有稳定 `project_id`、项目目的和 canonical source；
2. 指定一个 primary responsibility domain（主责任域）；
3. 通过 duplicate construction review（重复建设审查）；
4. 明确 Capability、Authority、Permission、Execution、Evidence、Evaluation 和 Decision 边界；
5. 记录与 DBOS、SAEE、DBA 或应用层的依赖；
6. 指定状态更新来源和 freshness policy（时效策略）；
7. 通过 [`INTEGRATION-GATES.md`](INTEGRATION-GATES.md) 的 `G0` 与 `G1`；
8. 由显式人工决策记录准入结果。

Repository discovery（仓库发现）不等于 Portfolio Admission（项目组合准入）。

当前 Program Governance Cockpit 与既有 Digital Biosphere public meaning layer 的长期 canonical relationship 尚未决定；本仓库是本次明确目标下的项目群驾驶舱基线，但不会据此静默覆盖、删除或合并另一仓库。该问题登记为 `DQ-008`。

## 5. Portfolio Truth Boundary（项目组合事实边界）

```text
PORTFOLIO_BASELINE_DEFINED=true
STAGED_PRODUCTION_PATH_PROPOSED=true
STAGED_PRODUCTION_PATH_ADOPTED=true
PORTFOLIO_OWNS_CHILD_REPOSITORIES=false
PORTFOLIO_CHANGES_CHILD_STATUS=false
ADJACENT_PROJECTS_ADMITTED=false
DISCOVERY_NE_ADOPTION=true
MAPPING_NE_INTEGRATION=true
TMAP_IS_PROJECT=false
TMAP_IS_RUNTIME=false
PRODUCTION_READY=false
```
