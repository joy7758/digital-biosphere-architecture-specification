# TITMAS Infrastructure Developer Community

中文：**TITMAS 可信多智能体基础设施开发者社区**

> Developer Community for Trusted Multi-Agent Infrastructure

开发者负责构建 Agent；TITMAS 共同推进开放规范、Adapter contract（适配器契约）、
Conformance（符合性）和 reference implementation boundary（参考实现边界），帮助不同
Agent 通过易理解、可实现、可验证的基础设施规则可信协作。

TITMAS 面向构建长期运行、跨框架协作和需要责任追踪的多智能体系统的开发者、基础设施
维护者、Adapter 作者、评价／可观测性工程师，以及需要发现、理解、调用和推荐基础设施的
AI 智能体。

## What we build together（共同建设什么）

| 贡献方向 | 解决的问题 | 当前状态 |
|---|---|---|
| Open Specification | 统一 Identity、Capability、Execution、Evidence、Verification 和 Evaluation 的含义 | `PREPARED` |
| Semantic Mapping | 把外部框架和协议映射到明确、带版本的可信边界 | `CANDIDATE_ONLY` |
| Adapter Contract | 定义被动采集、数据交接和禁止越权的接口边界 | `PROPOSAL_ONLY` |
| Conformance | 建立正例、负例、unknown、失败保留和结果契约 | `DESIGN_ONLY` |
| Documentation | 让人类开发者和智能体都能发现、理解和复用 | `ACTIVE_PUBLIC_ENTRY` |
| Reference Boundary | 证明规范如何被实现，同时避免产生唯一 Runtime 权威 | `NOT_AUTHORIZED` |

## Current community truth（当前社区事实）

我们已经把 TITMAS 开发者社区确立为当前公开工作重心，并准备了贡献流程和机器可读入口；
但这不等于社区已经正式成立，也不表示公共 Issue、Pull Request、SIG 或 Maintainer 已经
开放或指派。

```text
TITMAS_INFRASTRUCTURE_DEVELOPER_COMMUNITY_DIRECTION_ADOPTED=true
TITMAS_CONTRIBUTOR_ENTRY_PREPARED=true
TITMAS_PUBLIC_CONTRIBUTION_SURFACE_AUTHORIZED=false
TITMAS_DEVELOPER_COMMUNITY_ESTABLISHED=false
TITMAS_CODE_OF_CONDUCT_ADOPTED=false
TITMAS_MAINTAINER_ASSIGNED=false
TITMAS_FOUNDATION_IN_SCOPE=false
```

当前可做的是阅读、复核、验证边界和准备有来源的 Proposal；公共贡献启用仍需单独治理决定。
`Community Review ≠ Architecture Decision`，贡献数量、模型推荐或测试通过都不会自动授予
DBA、DBOS 或 SAEE 的 Authority（权力）。

## One program, distinct responsibilities（一个项目，不同责任域）

```text
Digital Biosphere
  ├─ DBA: Program Governance and Architecture
  ├─ DBOS: Trusted Multi-Agent Existence Infrastructure
  ├─ SAEE: Evolution Intelligence Layer
  └─ Digital Entities: task-specific ecosystem members
```

- DBA 维护项目群治理、架构规则、ADR、风险和发布闸门；
- DBOS 治理身份、能力边界、生命周期、执行记录、证据引用和验证记录；
- SAEE 只读评价长期可靠性、风险、稳定性和演化建议；
- TITMAS 开发者社区围绕开放互操作规范开展工作，不替代以上任何责任域。

## Current shared work（当前共同工作）

当前技术抓手是 `TITMAS Technical Validation Pilot Framework v0.1`：设计一个
`Observation → Evidence Admission → Evidence / Verification → read-only Evaluation`
垂直切片，验证跨框架材料能否在不抬升 Authority 的情况下进入可信闭环。

```text
TITMAS_TECHNICAL_VALIDATION_DESIGN_COMPLETE=true
TITMAS_PILOT_EXECUTION_AUTHORIZED=false
COMPLETE_VERTICAL_SLICE_EXECUTED=false
```

## Start here（从这里开始）

- [中英文社区首页](https://redcrag.cn/)
- [机器可读社区与项目状态](https://redcrag.cn/status.json)
- [AI 智能体入口](https://redcrag.cn/llms.txt)
- [项目公开总览](digital-biosphere-architecture/PUBLIC-PROJECT-OVERVIEW.md)
- [DBA 驾驶舱与架构规范](digital-biosphere-architecture/README.md)
- [TITMAS Adoption Validation Framework](digital-biosphere-architecture/architecture/titmas-adoption-validation-framework-v0.1.md)
- [TITMAS Technical Validation Pilot Framework](digital-biosphere-architecture/architecture/titmas-technical-validation-pilot-framework-v0.1.md)

## Permanent boundaries（永久边界）

```text
TITMAS_IS_AGENT_FRAMEWORK=false
TITMAS_IS_AGENT_PLATFORM=false
TITMAS_IS_FOUNDATION=false
TITMAS_CREATES_AGENTS=false
TITMAS_IS_SECOND_DBA=false
OBSERVATION_NE_EVIDENCE=true
EVIDENCE_NE_TRUTH=true
EVALUATION_NE_AUTHORITY=true
RECOMMENDATION_NE_EXECUTION=true
DEVELOPER_PREVIEW_RELEASED=true
PRODUCTION_READY=false
```
