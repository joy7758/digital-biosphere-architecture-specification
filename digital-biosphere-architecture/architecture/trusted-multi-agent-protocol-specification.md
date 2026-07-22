---
spec_id: TMAI-PROTOCOL-0.1
title: Trusted Multi-Agent Protocol Specification v0.1
title_zh: 可信多智能体协议规范 v0.1
status: accepted-non-executable-protocol-baseline
decision_reference: ADR-023-trusted-multi-agent-protocol-and-production-observability.md
decided_by_ref: zhangbin
primary_repository: digital-biosphere-architecture
implementation_authorized: false
runtime_created: false
api_created: false
authority_effect: none
permission_effect: none
evidence_effect: none
---

# Trusted Multi-Agent Protocol Specification v0.1

中文：可信多智能体协议规范 v0.1。

## 1. Purpose（目的）

Trusted Multi-Agent Protocol（可信多智能体协议，简称 TMAP）定义长期运行、相互协作且可验证的 Digital Entity（数字主体）之间所需的共同可信语义。

它是 Digital Biosphere（数字生物圈）的 protocolization（协议化）方向，不是 Agent Platform、Agent Framework、Workflow Tool、AI Cloud Platform、Runtime 或托管服务。

统一对外定位：

> Infrastructure for long-running, collaborative, and verifiable digital entities.

中文：面向长期运行、协作和可验证数字主体的基础设施。

## 2. One Program, Multiple Responsibility Layers（一个项目群，多个责任层）

```text
Digital Biosphere
  ├─ DBA: Program Governance and Architecture Layer
  ├─ DBOS: Trusted Multi-Agent Existence Infrastructure
  ├─ SAEE: Evolution Intelligence Layer
  └─ Digital Entities: task-specific ecosystem members
```

该结构表示一个总项目内的 responsibility separation（职责分离），不表示四个独立产品，也不表示代码依赖、权限继承或 Runtime 控制。

| 层 | 协议职责 | 明确不负责 |
|---|---|---|
| DBA | 战略、协议含义、架构规则、边界、跨项目契约、风险和发布治理 | Agent 执行、DBOS 运行逻辑、SAEE 评价计算 |
| DBOS | Identity、Lifecycle、Capability Boundary、Execution Record、Evidence、Verification 和开发者基础设施 | 创建 Agent、替代 Agent Framework、自动授权、自动演化 |
| SAEE | Evaluation、Reliability、Stability、Risk、Adaptation 与 Evolution Recommendation | 身份创建、DBOS 事实修改、权限授予、建议执行 |
| Digital Entity | 在声明能力、授权和上下文范围内执行领域任务 | 自证身份、自授权限、自改 Evidence、自动获得生态资格 |

## 3. Protocol Objects（协议对象）

TMAP v0.1 定义六类核心对象。对象定义不创建实例；规范 Owner 不等于全局 Truth Authority（事实权威）。

| 对象 | 回答的问题 | 规范 Owner | 核心边界 |
|---|---|---|---|
| Identity Object | 它是谁？ | DBOS | Identity ≠ Permission；外部 Resource 名称不能自动成为 `entity_id` |
| Capability Object | 它声明能做什么？ | DBOS | Capability ≠ Authority ≠ Permission |
| Execution Object | 发生了什么？ | DBOS | Execution Record ≠ Execution correctness（执行正确性） |
| Evidence Object | 有什么可追溯材料？ | DBOS | Evidence ≠ Truth；Telemetry 不能直接成为 canonical Evidence |
| Verification Object | 在什么规则和范围下通过了什么检查？ | DBOS | Verification ≠ Permission ≠ Fitness |
| Evolution Interface | 长期表现和变化风险如何？ | SAEE | Evaluation/Recommendation ≠ Decision ≠ Execution |

对象字段、引用和 Owner 的详细规范见 [`data-contracts.md`](data-contracts.md) 与 [`interface-specification.md`](interface-specification.md)。

## 4. Trusted Agent Four Boundaries（可信智能体四边界）

### 4.1 Identity Boundary（身份边界）

必须能够区分：被观察的服务或进程、运行实例、代码仓库、Agent role、DBOS Entity Identity 和 Human Owner。它们不能因为共享名称、`service.name`、`trace_id` 或部署标签而自动等同。

### 4.2 Capability Boundary（能力边界）

必须记录声明能力、范围、约束、风险、验证状态和授权引用，并始终保持：

```text
Capability != Authority
Capability != Permission
Permission != Identity
```

### 4.3 Execution Boundary（执行边界）

执行需要 Capability、有效 Authorization、当前 Permission 和 Context。执行记录必须保留来源、顺序、失败、重试和未知项；记录存在不表示动作正确、完整或获批。

### 4.4 Evidence Boundary（证据边界）

Evidence 必须由有来源的材料、接纳记录、完整性信息和 Verification 引用构成。Trace、Metric、Log、模型输出、Collector receipt（收集器回执）或签名本身都不能自动证明 Truth。

## 5. Protocol Planes（协议平面）

```text
Observation Plane
  OpenTelemetry signals, external records, runtime observations
        ↓ explicit intake and provenance
Existence Plane / DBOS
  Identity, Capability, Execution, Evidence, Verification, Lifecycle
        ↓ read-only versioned contract
Evolution Plane / SAEE
  Evaluation, Reliability, Risk, Stability, Recommendation
        ↓ explicit review and decision
Governance Plane
  Decision, Adoption, Authorization
        ↓ separately authorized execution
Existence Plane / DBOS
```

- Observation Plane（观察平面）提供材料，不拥有 Evidence Truth；
- Existence Plane（存在平面）形成 DBOS 规范记录，不产生 Fitness；
- Evolution Plane（演化平面）形成派生评价，不产生 Permission；
- Governance Plane（治理平面）记录明确主体作出的决定，不自行执行。

## 6. OpenTelemetry Relationship（与 OpenTelemetry 的关系）

TMAP 重度采用 OpenTelemetry（开放遥测）的开放协议与解耦方法：

- 使用 Resource、Instrumentation Scope、Context Propagation 和 Signals 组织观察材料；
- 优先使用稳定 OTLP 传输 Trace、Metric 与 Log；
- 允许 SDK、Collector、Backend 和 TMAP/DBOS 独立替换；
- 使用版本化 Semantic Conventions（语义约定），对 Development 状态字段 fail closed；
- 以 Collector agent/gateway patterns（收集器代理／网关模式）实现有界采集、处理与路由。

但必须保持：

```text
OTel Resource != DBOS Entity Identity
Trace != Execution Object
Span != Evidence Object
Metric != Fitness Assessment
Log != Truth
Collector != Verification Authority
OTLP acknowledgement != canonical DBOS acceptance
Baggage != Authorization or Permission
```

详细映射与生产约束见 [`opentelemetry-observability-profile.md`](opentelemetry-observability-profile.md)。

## 7. Protocol Versioning and Profiles（协议版本与配置）

TMAP 使用独立版本与 profile（配置）：

- Protocol Version：对象含义、Owner 和不变量；
- Transport Profile：OTLP 或未来其他传输的映射；
- Observability Profile：Signal、Resource、Context、采样和敏感数据规则；
- Deployment Profile：self-hosted、single-tenant 等部署约束；
- Evaluation Profile：SAEE 消费的字段、模型范围和限制。

任一 profile 的发布不自动升级其他 profile。没有共同兼容版本时必须保留 `unsupported_version`，不得猜测、静默降级或把未知字段变成授权。

## 8. Ecosystem Path（生态路径）

```text
Protocol
  → SDK
    → Reference Implementation
      → Adapter Ecosystem
        → Developer and Agent Adoption
```

SDK、Reference Implementation 或 Adapter 只有在其实现仓库形成直接证据后才能被称为已实现。DBA 中的本规范只定义协议和进入条件。

## 9. Proposal Gate（提案闸门）

所有后续开发必须回答：

1. 是否增强长期运行、多主体协作或可验证性？
2. primary repository 是 DBA、DBOS、SAEE 还是 Digital Entity？
3. 是否违反 `DBOS ≠ Agent Framework`、`SAEE ≠ Controller`、`Verification ≠ Permission` 或 `Evidence ≠ Truth`？
4. 是否应形成 Protocol、Schema、SDK 或 Adapter，而不是单一封闭功能？
5. 是否复用 OpenTelemetry、W3C Trace Context 等开放标准，或说明不能复用的理由？
6. 是否记录失败、未知、采样、丢弃、版本和隐私边界？

无法回答时保持 `REVIEW_REQUIRED`。

## 10. Current State and Non-claims（当前状态与非声明）

```text
TMAP_SPECIFICATION_DEFINED=true
TMAP_IMPLEMENTED=false
TMAP_RUNTIME_CREATED=false
TMAP_API_CREATED=false
TMAP_SDK_CREATED=false
TMAP_ADOPTED_BY_DBOS=false
TMAP_ADOPTED_BY_SAEE=false
AGENT_CREATED=false
ENTITY_CREATED=false
CAPABILITY_CREATED=false
PERMISSION_GRANTED=false
EVIDENCE_TRUTH_CHANGED=false
PRODUCTION_READY=false
```
