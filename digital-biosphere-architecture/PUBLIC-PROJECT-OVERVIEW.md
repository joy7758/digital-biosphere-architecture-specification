---
document_id: DBA-PUBLIC-OVERVIEW-0.1
title: Digital Biosphere Public Project Overview v0.1
title_zh: 数字生物圈公开项目总览 v0.1
status: developer-preview-v0.1-public-entry
release_status: released-not-production-ready
public_positioning: Trusted Multi-Agent Infrastructure
implementation_authorized: false
runtime_effect: none
last_reviewed: 2026-07-22
---

# Digital Biosphere Public Project Overview v0.1（数字生物圈公开项目总览 v0.1）

> **Infrastructure for long-running, collaborative, and verifiable digital entities.**
>
> **面向长期运行、协作和可验证数字主体的基础设施。**

Digital Biosphere（数字生物圈）是总项目；Trusted Multi-Agent Infrastructure（可信多智能体基础设施）是统一对外定位。它不是新的 Agent Framework（智能体框架），而是把身份、生命周期、执行记录、证据引用、验证、评价和受控演化连接起来的基础设施方向。

公开技术主线是 Protocol → SDK → Reference Implementation → Developer Ecosystem（协议 → SDK → 参考实现 → 开发者生态）。当前 DBA 已定义 Trusted Multi-Agent Protocol v0.1（可信多智能体协议 v0.1）和 OpenTelemetry Observability Profile（开放遥测可观测性配置），并完成 DBOS/SAEE 的 `PR-G1` 只读实现映射；这些仍不是生产实现或部署完成声明。

本页是 `Trusted Multi-Agent Infrastructure Developer Preview v0.1`（可信多智能体基础设施开发者预览版 v0.1）的单一理解入口。AI agent 是首要客户；人类仍保留发布、权限和重大外部动作的最终权力。当前状态是 `RELEASED_NOT_PRODUCTION_READY`：Developer Preview 已正式发布，但不声称三项目已经完成生产端到端集成、客户采用或生产部署。

Developer Preview 也是 DBOS 与 SAEE 的跨项目测试工程：同一个受控协作场景既用于展示，也用于发现记录、验证、接口和评价缺口。测试发现的缺口经过 DBA 归属与重复建设审查后，可以在 DBOS 或 SAEE 中补最小功能；这不允许 Demo 自己成为新的基础设施权威。

## 1. Architecture at a Glance（架构总览）

```text
Digital Biosphere
  public positioning: Trusted Multi-Agent Infrastructure
  |
  +-- DBA   Program Governance and Architecture Cockpit
  |         项目群治理、架构边界、路线图、风险、决策与集成闸门
  |
  +-- DBOS  Existence Infrastructure
  |         身份、生命周期、能力边界、执行记录、证据引用与验证
  |
  +-- SAEE  Evolution Intelligence Layer
  |         可靠性、稳定性、风险评价与演化建议
  |
  +-- Digital Entities
            执行具体任务并产生可被记录的行为材料；不自动获得权限
```

三者共同服务一个项目目标，但保持独立责任域：

```text
DBA_NE_DBOS=true
DBA_NE_SAEE=true
DBOS_NE_SAEE=true
SAEE_NE_DBOS=true
DBOS_NE_AGENT_FRAMEWORK=true
SAEE_NE_AUTOMATIC_CONTROLLER=true
```

## 2. What the Developer Preview Must Demonstrate（开发者预览必须展示什么）

Developer Preview v0.1 只有在以下连续链路可运行并可复核时才成立：

```text
Three governed role simulations（三个受治理角色模拟）
  Research Agent -> Analysis Agent -> Review Agent
        |
        v
DBOS trust records（DBOS 可信记录）
  Identity -> Execution -> Evidence Reference -> Validation
        |
        v
SAEE bounded evaluation（SAEE 受限评价）
  Reliability -> Stability -> Risk -> Evolution Recommendation
        |
        v
Governance Decision（治理决策，保留人工权力）
```

角色名用于演示协作语义，不自动创建生产 Agent、Runtime、Permission 或 Digital Organism（数字有机体）。SAEE 的 Recommendation（建议）不是 Decision（决策），Decision 也不是 Execution（执行）。

## 3. Current Truth（当前事实）

截至 2026-07-22：

- DBA 已建立项目群驾驶舱、路线图、项目组合和集成闸门；Developer Preview v0.1 已按 `ADR-022` 发布，但不构成生产就绪或客户采用；
- DBOS 已形成 local editable install（本地可编辑安装）、单一测试入口、Quick Start（快速入门）和三角色 synthetic demo（合成演示）；334/334 tests 与 34/34 validators 在冻结源码通过；
- `DBOS-EXP-0001` 历史 Evidence 没有被改写；版本感知校验能保留旧 binding 并显式警告当前文档漂移；
- SAEE 已形成只读 DBOS Developer Preview adapter（开发者预览适配器），复用现有 Reliability Framework 与 `saee.evaluate_agent_run`；
- DBOS → SAEE 本地合成链路已通过 scoped conformance（限定范围符合性），但结果诚实保持 `Reliability=NOT_ASSESSED`、`Stability=NOT_ASSESSED`、`EvolutionRecommendation=HOLD`；
- 首轮 Agent Customer Validation（智能体客户验证）完成 12/12 个跨千帆／方舟会话并得到 `CONDITIONAL`；修复后复测 `TMAI-ACV-20260722-002` 再完成 12/12，会话与全部预冻结阈值通过，12/12 overall verdict 为边界正确的 `CONDITIONAL`；
- 开放网络观察 `TMAI-OWD-20260722-001` 已得到 GitHub 新 description 的部分索引命中，但规范英文名、中文名和公开搜索仍无精确命中，因此保持 `PARTIAL_METADATA_ONLY`；
- 旧的 3–5 名人类开发者试用路线已由 `ADR-021` 取代为可选次级研究，不再是本次首要发布前置条件；
- DBOS 整仓继续为 private（私有）；exact public-safe wheel 已作为 v0.1 GitHub Release asset 公开，但没有 public Runtime、托管 API、Permission 或生产兼容声明。
- 面向生产的 S0–S9 staged implementation sequence（分阶段实施序列）已经形成并经两路 Agent 推荐为正确的下一条路径；`ADR-024` 仍是 `PROPOSED`，`DQ-018` 仍等待人工决策，`DQ-019`–`DQ-021` 仍为 `BLOCKED_INPUT`，因此当前不构成实施授权或 production readiness（生产就绪）。
- OTLP `v1.11.0` 与 OpenTelemetry Semantic Conventions（开放遥测语义约定）分属 `DQ-022` 和 `DQ-023` 两个版本决策；47-field / 7-group / 9-source semantic mapping 已补充为 8 组、46 个预登记 conformance cases，覆盖 47/47 mappings。目录／结果 Schema、12/12 + 23/23 负例和两路智能体复核通过，但所有 cases 仍为 `NOT_EXECUTED`，reference 未采纳、validator 未实现、没有真实符合性证据。
- `DQ-024` 单独治理 OpenTelemetry Schema/Resource/Entity provenance：7 组 45 个 cases 覆盖 exact schema source、DNS/redirect/cache、transformation lineage、Resource detector/merge、Development Entity quarantine、privacy/retention/tenant isolation 和 result authority。2/2 Schema、3/3 positive fixtures、14/14 + 37/37 negatives 与两路三轮审查通过；模型只推荐 bounded design reference 和 human review，并明确拒绝当前 Runtime recommendation。45 cases 执行为 0、reference 未采纳、validator 未实现。
- `DQ-025` 单独治理 OpenTelemetry Collector distribution：候选锁定 official `v0.156.0` 的 exact releases/core/contrib commits 与 11 个 source-byte digests，提议只编译 8 个组件和 `env/file` 两个本地 providers；8 组 48-case contract 覆盖 supply chain、allowlist、config、security、WAL/delivery、health/operations、capacity/HA 和 authority。两路模型只推荐 bounded design reference 和 human review，并拒绝当前 Runtime recommendation。48 cases 执行为 0，binary/image/config/validator 均不存在。
- `DQ-020` 的 machine deployment profile 已被定义为 proposed input：只覆盖 single-tenant synthetic staging，edge Collector tier 仍 optional、gateway 只在 `G3E` 候选 >=2 replicas；remote config/OpAMP/public ingress/real data 禁止，配置采用 immutable rollout，health 不能单独决定 readiness。它复用现有 56/46/45/48 cases，不创建第五套 catalog；Schema 与两路 human-review recommendation 不产生 config、listener、Runtime 或部署授权，`DQ-020` 继续 `BLOCKED_INPUT`。
- 同一 `DQ-020` 的 operational evidence profile（运维证据画像）进一步定义 internal metrics/logs、OTLP↔Prometheus naming/stability、12 类 observation、6 类 SLI、独立 self-observation/blackbox/storage/drift、composite readiness、no-data alert/runbook 与 delivery reconciliation。45/45 机器负例和两路模型最终复核通过，但 exact query/threshold/alert/route/runbook 仍有意为 `null` 并失败关闭；没有测量、Evidence、Runtime 或生产建议。

时间点事实以 [`PROGRAM-STATUS.md`](PROGRAM-STATUS.md) 为准；本页不把 Developer Preview 发布升级为生产实现、客户采用或运行授权。

## 4. Developer Navigation（开发者导航）

| 需要了解 | 入口 | 当前效力 |
|---|---|---|
| 项目是什么 | 本页 | Developer Preview v0.1 公开定位 |
| 当前做到哪里 | [`PROGRAM-STATUS.md`](PROGRAM-STATUS.md) | 时间点治理快照 |
| 智能体如何发现、评估和推荐 | [`AGENT-CUSTOMER-PACKAGE-v0.1.1.json`](AGENT-CUSTOMER-PACKAGE-v0.1.1.json) | 机器可读入口与复测结果；不等于 Runtime 发布 |
| 智能体客户验证协议 | [`AGENT-CUSTOMER-VALIDATION-PROTOCOL.md`](AGENT-CUSTOMER-VALIDATION-PROTOCOL.md) | 预冻结 Provider、场景、阈值和非效果 |
| 首轮智能体客户验证结果 | [`AGENT-CUSTOMER-VALIDATION-REPORT.md`](AGENT-CUSTOMER-VALIDATION-REPORT.md) | 历史基线 `CONDITIONAL`；失败保留 |
| 修复后智能体客户验证结果 | [`AGENT-CUSTOMER-VALIDATION-RERUN-REPORT.md`](AGENT-CUSTOMER-VALIDATION-RERUN-REPORT.md) | `PASS`；不等于采用或发布授权 |
| 开放网络自然发现观察 | [`OPEN-WEB-DISCOVERY-OBSERVATION.md`](OPEN-WEB-DISCOVERY-OBSERVATION.md) | `PARTIAL_METADATA_ONLY`；描述命中不等于规范名称自然发现 |
| Developer Preview 如何完成 | [`DEVELOPER-PREVIEW-PLAN.md`](DEVELOPER-PREVIEW-PLAN.md) | 交付与 gate 计划 |
| 如何发布 | [`DEVELOPER-PREVIEW-RELEASE-PLAN.md`](DEVELOPER-PREVIEW-RELEASE-PLAN.md) | 发布治理计划 |
| 正式发布证据 | [`DEVELOPER-PREVIEW-v0.1-RELEASE-REPORT.md`](DEVELOPER-PREVIEW-v0.1-RELEASE-REPORT.md) | GitHub、匿名安装与百度云外部复验 |
| 本地符合性结果 | [`DEVELOPER-PREVIEW-CONFORMANCE-REPORT.md`](DEVELOPER-PREVIEW-CONFORMANCE-REPORT.md) | 当前工作树本地通过；不是 release |
| 可选人类可用性研究 | [`EXTERNAL-DEVELOPER-TRIAL-PLAN.md`](EXTERNAL-DEVELOPER-TRIAL-PLAN.md) | 已由 `ADR-021` 取代为非阻塞次级路线 |
| 可选人类试用操作 | [`EXTERNAL-DEVELOPER-TRIAL-GUIDE.md`](EXTERNAL-DEVELOPER-TRIAL-GUIDE.md) | 历史／可选手册，不是首要 gate |
| 反馈格式 | [`DEVELOPER-FEEDBACK-TEMPLATE.md`](DEVELOPER-FEEDBACK-TEMPLATE.md) | 模板已准备；不是采用证明 |
| DBOS public-safe wheel | [`DBOS-PUBLIC-PACKAGE-MANIFEST-v0.1.json`](DBOS-PUBLIC-PACKAGE-MANIFEST-v0.1.json) | 已发布的有界 Developer Preview 包；不是 Runtime 或生产 SDK |
| 架构与责任边界 | [`README.md`](README.md) 与 [`architecture/`](architecture/) | DBA 规范表面 |
| 可信多智能体协议 | [`architecture/trusted-multi-agent-protocol-specification.md`](architecture/trusted-multi-agent-protocol-specification.md) | 六个核心对象、四个可信边界；规范不等于实现 |
| OpenTelemetry 参考配置 | [`architecture/opentelemetry-observability-profile.md`](architecture/opentelemetry-observability-profile.md) | 遥测进入 DBOS 的可观测性边界；Telemetry 不等于 Evidence |
| OpenTelemetry 语义画像 | [`architecture/opentelemetry-semantic-conventions-profile.md`](architecture/opentelemetry-semantic-conventions-profile.md) | core Stable 与 pinned GenAI Development 分层；遥测字段不产生 DBOS/SAEE 权力效果 |
| OpenTelemetry 机器映射 | [`architecture/opentelemetry-semantic-mapping.v0.1.json`](architecture/opentelemetry-semantic-mapping.v0.1.json) | 47-field / 7-group / 9-source；`DQ-023=READY_FOR_REVIEW`，未采纳、未实现 |
| OpenTelemetry 语义一致性合同 | [`architecture/opentelemetry-semantic-conformance-profile.md`](architecture/opentelemetry-semantic-conformance-profile.md) / [`46-case catalog`](architecture/opentelemetry-semantic-conformance-cases.v0.1.json) / [`result schema`](architecture/schemas/opentelemetry-semantic-conformance-result-set.schema.v0.1.json) | 8 组、46 个预登记用例和 47/47 mapping coverage；全部 `NOT_EXECUTED` |
| OpenTelemetry Schema/Resource/Entity provenance | [`architecture/opentelemetry-schema-resource-entity-provenance-profile.md`](architecture/opentelemetry-schema-resource-entity-provenance-profile.md) / [`45-case catalog`](architecture/opentelemetry-schema-resource-conformance-cases.v0.1.json) / [`result schema`](architecture/schemas/opentelemetry-schema-resource-conformance-result-set.schema.v0.1.json) | `DQ-024=READY_FOR_REVIEW`；Development Entity quarantine；45 cases 全部 `NOT_EXECUTED` |
| OpenTelemetry Collector distribution | [`architecture/opentelemetry-collector-distribution-profile.md`](architecture/opentelemetry-collector-distribution-profile.md) / [`inventory`](architecture/opentelemetry-collector-component-inventory.v0.1.json) / [`48-case catalog`](architecture/opentelemetry-collector-distribution-conformance-cases.v0.1.json) / [`result schema`](architecture/schemas/opentelemetry-collector-distribution-conformance-result-set.schema.v0.1.json) | `DQ-025=READY_FOR_REVIEW`；custom-minimal 8 components + 2 local providers；未采纳、未构建、48 cases 全部 `NOT_EXECUTED` |
| OpenTelemetry Collector deployment profile | [`machine profile`](architecture/opentelemetry-collector-deployment-profile.v0.1.json) / [`Schema`](architecture/schemas/opentelemetry-collector-deployment-profile.schema.v0.1.json) / [`readiness matrix`](architecture/opentelemetry-collector-deployment-readiness-matrix.md) | `PROPOSED_DQ_020_INPUT`；synthetic staging only；no new catalog；未配置、未部署、未授权 |
| OpenTelemetry Collector operational evidence | [`machine profile`](architecture/opentelemetry-collector-operational-evidence-profile.v0.1.json) / [`Schema`](architecture/schemas/opentelemetry-collector-operational-evidence-profile.schema.v0.1.json) / [`contract`](architecture/opentelemetry-collector-operational-evidence-contract.md) | 45/45 fail-closed negatives；两模型推荐有限架构审查；exact 运行绑定、测量和真实证据不存在 |
| OpenTelemetry 生产对齐 | [`architecture/opentelemetry-production-alignment-matrix.md`](architecture/opentelemetry-production-alignment-matrix.md) | 60 项官方 OTLP/Collector/SemConv/Schema/Resource/Entity/operations control 到 TMAI gate 和 direct evidence 的映射；不是符合性证明 |
| 生产就绪要求 | [`architecture/production-readiness-specification.md`](architecture/production-readiness-specification.md) | deployment-specific（部署特定）闸门；当前未通过 |
| 生产实现映射 | [`PRODUCTION-IMPLEMENTATION-MAPPING-REPORT.md`](PRODUCTION-IMPLEMENTATION-MAPPING-REPORT.md) | `PR-G1` 已完成；OTLP、生产持久化、恢复、安全、SLO 与 Pilot 仍未实现／未验证 |
| 生产持久化契约 | [`architecture/production-persistence-adapter-specification.md`](architecture/production-persistence-adapter-specification.md) | 事务、幂等、HA、PITR、RPO/RTO 和 OTel 自观测要求；未选后端 |
| OTLP/Collector 生产配置 | [`architecture/otlp-collector-production-profile.md`](architecture/otlp-collector-production-profile.md) | gateway、delivery、queue/WAL、扩缩容与安全边界；未部署 Collector 或 endpoint |
| Telemetry-to-Evidence 准入 | [`architecture/telemetry-to-evidence-admission-contract.md`](architecture/telemetry-to-evidence-admission-contract.md) | 第二次独立准入、provenance、Identity Continuity 和 Data Governance；未创建 Evidence |
| 分阶段生产序列 | [`architecture/production-implementation-sequence.md`](architecture/production-implementation-sequence.md) / [`PRODUCTION-IMPLEMENTATION-SEQUENCE-v0.1.json`](PRODUCTION-IMPLEMENTATION-SEQUENCE-v0.1.json) | S0–S9 人类／机器可读路径；`ADOPTED_STAGE_GATED_NOT_EXECUTED` |
| 生产闸门证据合同 | [`architecture/production-gate-evidence-manifest-specification.md`](architecture/production-gate-evidence-manifest-specification.md) / [`JSON Schema`](architecture/schemas/production-gate-evidence-manifest.schema.v0.1.json) | exact scope、digest、coverage、SLO、OTel accounting、review/Decision；validator 未实现且没有 gate PASS |
| 生产证据合同 Agent 复审 | [`PRODUCTION-EVIDENCE-CONTRACT-AGENT-RECOMMENDATION.md`](PRODUCTION-EVIDENCE-CONTRACT-AGENT-RECOMMENDATION.md) | 两路推荐 S0 架构合同冻结；两路均不推荐当前生产客户使用 |
| 生产路径 Agent 审查 | [`PRODUCTION-PATH-AGENT-RECOMMENDATION.md`](PRODUCTION-PATH-AGENT-RECOMMENDATION.md) | 两路均推荐序列；两路均不推荐当前生产客户使用 |
| 为什么进入此阶段 | [`architecture/ADR-017-trusted-multi-agent-infrastructure-developer-preview.md`](architecture/ADR-017-trusted-multi-agent-infrastructure-developer-preview.md) | 已接受的阶段决策 |
| 为什么允许发布 | [`architecture/ADR-022-developer-preview-release.md`](architecture/ADR-022-developer-preview-release.md) | exact artifact 和公开边界的人工发布决定 |

## 5. Public Claim Boundary（对外声明边界）

Release Gate（发布闸门）已经通过。当前允许使用：

> Trusted Multi-Agent Infrastructure Developer Preview v0.1 is released（可信多智能体基础设施开发者预览版 v0.1 已发布）。

仍不得使用：

- production-ready（生产就绪）；
- end-to-end integration verified（端到端集成已验证）；
- autonomous evolution（自主演化）；
- Agent platform（智能体平台）；
- production SDK（生产 SDK）；
- evidence proves truth（证据证明真相）。

```text
PUBLIC_ENTRY_DEFINED=true
DEVELOPER_PREVIEW_RELEASED=true
SCOPED_LOCAL_DEMO_CONFORMANCE_PASS=true
FULL_END_TO_END_INTEGRATION_VERIFIED=false
PRIMARY_CUSTOMER=AI_AGENT
AGENT_CUSTOMER_VALIDATION_BASELINE=CONDITIONAL
AGENT_CUSTOMER_VALIDATION_RERUN=PASS
AGENT_CUSTOMER_API_SESSIONS=24
HUMAN_DEVELOPER_TRIAL_REQUIRED_FOR_PRIMARY_ROUTE=false
OPEN_WEB_DISCOVERY=PARTIAL_METADATA_ONLY
OPEN_WEB_DISCOVERY_OBSERVATION_ID=TMAI-OWD-20260722-001
GITHUB_DISCOVERY_METADATA_REMEDIATED=true
GITHUB_METADATA_DESCRIPTION_MATCH=true
OPEN_WEB_CANONICAL_NAME_MATCH=false
PRODUCTION_RUNTIME_CREATED=false
AGENT_INSTANCE_CREATED=false
PERMISSION_GRANTED=false
EVIDENCE_NE_TRUTH=true
TRUSTED_MULTI_AGENT_PROTOCOL_DEFINED=true
PRODUCTION_ARCHITECTURE_BASELINE_DEFINED=true
STAGED_PRODUCTION_IMPLEMENTATION_SEQUENCE_DEFINED=true
STAGED_PRODUCTION_IMPLEMENTATION_SEQUENCE_RECOMMENDED_BY_TWO_AGENTS=true
STAGED_PRODUCTION_IMPLEMENTATION_SEQUENCE_ADOPTED=true
OTEL_PRODUCTION_ALIGNMENT_MATRIX_DEFINED=true
PRODUCTION_GATE_EVIDENCE_MANIFEST_CONTRACT_DEFINED=true
PRODUCTION_GATE_EVIDENCE_VALIDATOR_IMPLEMENTED=false
ANY_PRODUCTION_GATE_PASS_CREATED=false
S0_ARCHITECTURE_CONTRACT_FREEZE_RECOMMENDED_BY_TWO_AGENTS=true
PRODUCTION_IMPLEMENTATION_AUTHORIZED=false
PRODUCTION_READY=false
```
