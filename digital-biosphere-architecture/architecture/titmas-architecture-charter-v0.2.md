---
document_id: DBA-TITMAS-ARCHITECTURE-CHARTER-0.2
title: TITMAS Architecture Charter v0.2
title_zh: TITMAS 架构章程 v0.2
status: accepted-immune-identity-and-required-boundaries
maturity: Development
maturity_scope: entire-document
owner_ref: HUMAN_GOVERNANCE_AUTHORITY
decision_reference: HUMAN_DECISION_ACCEPT_WITH_REQUIRED_BOUNDARIES_2026-07-28
supersedes: titmas-architecture-charter-v0.1.md
predecessor_sha256: 4a0794783f93b543347e30f8056c2912b6b4859ac84b28f782c69f67121e64fc
compatibility_statement: "Project identity and governance guardrails only; no implementation compatibility claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
classification: project-level-adaptive-immune-capability-charter
primary_repository: digital-biosphere-architecture
decision_status: ACCEPT_WITH_REQUIRED_BOUNDARIES
immune_identity: ADOPTED
github_first_immune_sensing: ADOPTED_AS_PHASE_1_BOUNDED_STRATEGY
titmas_drift_check: ADOPTED_AS_MANDATORY_HUMAN_REVIEW_GATE
continuous_monitoring_authorized: false
automatic_response_authorized: false
implementation_authorized: false
execution_authorized: false
repository_created: false
code_created: false
release_authorized: false
production_ready: false
created_at: 2026-07-28
---

# TITMAS Architecture Charter v0.2

中文：TITMAS（Trusted Infrastructure for Trustworthy Multi-Agent Systems，
可信多智能体系统可信基础设施）架构章程 v0.2。

本章程是
[`TITMAS Architecture Charter v0.1`](titmas-architecture-charter-v0.1.md)
的 versioned successor（版本化后继），不是第二份 TITMAS 项目宪法。v0.1 作为历史
前代文档保留；自本章程被接受后，TITMAS 项目身份、边界和漂移审查以 v0.2 为准。

本章程继续受
[`Digital Biosphere Program Charter`](../PROGRAM-CHARTER.md)、
[`Digital Immune Constitution candidate`](titmas-digital-immune-constitution-v1.0.md)、
[`TITMAS Interface Boundary Map v0.1`](TITMAS_INTERFACE_BOUNDARY_MAP_v0.1.md) 和
Human Authority Gate（人类权力闸门）约束。任何更高层规则冲突都按第 12 节处理。

## 0. Decision Scope（决定范围）

人类治理权威已作出以下有界决定：

```text
HUMAN_DECISION=ACCEPT_WITH_REQUIRED_BOUNDARIES
IMMUNE_IDENTITY=ADOPT
GITHUB_FIRST_IMMUNE_SENSING=ADOPT_AS_PHASE_1_BOUNDED_STRATEGY
TITMAS_DRIFT_CHECK=ADOPT_AS_MANDATORY_HUMAN_REVIEW_GATE

CONTINUOUS_MONITORING_AUTHORIZED=false
AUTOMATIC_RESPONSE_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
```

`ADOPT` 只采纳项目身份与治理护栏。它不证明或授权 Runtime、continuous monitoring
（持续监控）、automatic response（自动响应）、新组件、代码、Schema、API、
Dashboard、Adapter、Repository、部署、发布或生产能力。

```text
TITMAS_PROJECT_IDENTITY_ADOPTED=true
TITMAS_PORTFOLIO_ADMISSION_UNCHANGED=true
TITMAS_IMPLEMENTED=false
TITMAS_RUNTIME_CREATED=false
TITMAS_REPOSITORY_CREATED=false
```

## 1. TITMAS Immune Identity Principle（TITMAS 免疫身份原则）

> **TITMAS is an adaptive immune capability for complex digital ecosystems.**

中文：

> **TITMAS 是复杂数字生态的自适应免疫能力。**

TITMAS 的首要目标是帮助一个人以更低的认知和运维成本，在持续增长的 repository
（仓库）、program（程序／项目群）、Agent、工具和外部服务中保持：

- source-bound sensing（带来源的感知）；
- health awareness（健康态势理解）；
- risk recognition（风险识别）；
- human attention focus（人类注意力聚焦）；
- decision support（决策辅助）；
- evidence-bound adaptation（受证据约束的适应演化）。

TITMAS 不追求理论完整性，也不以扩大自身系统边界为成功。任何新增抽象必须证明它能
降低整合复杂度或人工管理成本、改善决策质量，并且不会复制现有服务或产生更大的维护
负担；否则只保留为理论记录，不进入 Implementation。

TITMAS 的 interoperable infrastructure（互操作基础设施）是支持免疫能力的机制，
不是高于免疫身份的第二项目身份。

## 2. What TITMAS Must Not Become（禁止成为）

TITMAS 必须不成为：

1. Digital Asset Management or Custody Platform（数字资产管理或托管平台）；
2. Agent Control Plane（Agent 控制平面）；
3. Unified Gateway（统一入口）；
4. Unified Identity or Permission System（统一身份或权限系统）；
5. Central Truth Source or Database（中央真相来源或数据库）；
6. External Service Replacement Platform（外部服务替代平台）；
7. Automatic Decision Engine（自动决策引擎）；
8. Automatic Scheduling or Agent Selection System（自动调度或 Agent 选择系统）；
9. Unbounded Monitoring or Response Authority（无界监控或响应权力）。

连接更多来源、显示更多状态或生成更强建议，均不得被解释为获得 connected system
（连接系统）的 Ownership、Authority、Permission、Truth 或 Execution 权。

## 3. Immune Operating Cycle（免疫运行循环）

TITMAS 的规范性工作循环是：

```text
Source / Sensing
  -> Observation / Evidence Candidate
    -> Health Diagnosis / Bounded Evaluation
      -> Human Attention Candidate
        -> Human Decision
          -> Separately Authorized Execution
            -> New Observation and Evidence
              -> Adaptation
```

每一步必须保留 source、owner、scope、freshness、limitations 和当前授权状态。后一步
不能自动抬升前一步的语义：

```text
Attention != Authority
Recommendation != Decision
Decision != Execution
Validation != Truth
Observation != Evidence
Evidence Candidate != Canonical Evidence
```

Human Attention Candidate（人类注意力候选）只回答“现在什么值得人看”，不决定谁
必须参与、谁获得 Permission、什么是真相或应执行什么动作。

Execution 必须取得与具体动作、对象、时间和环境相匹配的独立授权。执行结果必须回到
新的 Observation 和 Evidence 流程，而不是反向改写既有记录。

## 4. Current Capability Boundary（当前能力边界）

### 4.1 Verified current surfaces（已核验当前表面）

本章程只承认以下有界、可追溯的当前能力：

| Surface | Current bounded role | Must not be elevated to |
|---|---|---|
| `agent-health` | local static repository health diagnosis and bounded recommendations（本地静态仓库健康诊断与有界建议） | continuous runtime monitor、Authority、automatic fix |
| `agent-evidence` | observation、evidence-candidate packaging、local validation、export and offline review（观察、证据候选打包、本地验证、导出与离线审查） | canonical Truth owner、full governance platform、runtime bridge |
| DBA Cockpit | read-only situational references and pending decisions（只读态势引用与待决定事项） | control console、writeback surface、Truth source |
| Codex | execution assistance after explicit authorization（明确授权后的执行辅助） | automatic Authority、universal executor、decision owner |
| SAEE bounded surface | read-only, evidence-bound evaluation and recommendation（只读、受证据约束的评价与建议） | controller、writeback authority、automatic execution |

这些表面由各自 canonical source（规范来源）证明。DBA 或本章程中的引用不是能力事实
的替代来源。

### 4.2 Future candidates, not implemented（未来候选，尚未实现）

以下能力只是未来候选，当前均不得声称已经实现：

- continuous runtime monitoring（持续运行时监控）；
- behavioral drift detection（行为漂移检测）；
- permission drift detection（权限漂移检测）；
- real-time cross-service anomaly detection（实时跨服务异常检测）；
- automatic immune-memory learning（自动免疫记忆学习）；
- automatic isolation、shutdown、fix、rollback or response（自动隔离、关闭、修复、
  回滚或响应）。

```text
CONTINUOUS_RUNTIME_MONITORING_IMPLEMENTED=false
BEHAVIORAL_DRIFT_DETECTION_IMPLEMENTED=false
PERMISSION_DRIFT_DETECTION_IMPLEMENTED=false
REAL_TIME_CROSS_SERVICE_ANOMALY_DETECTION_IMPLEMENTED=false
AUTOMATIC_IMMUNE_MEMORY_LEARNING_IMPLEMENTED=false
AUTOMATIC_ISOLATION_FIX_ROLLBACK_RESPONSE_IMPLEMENTED=false
```

## 5. GitHub-first Immune Sensing Strategy（GitHub 优先免疫感知策略）

第一阶段采用 GitHub-first Immune Sensing Strategy，范围只限于：

- 发现 GitHub 托管的软件资产；
- 观察明确允许访问的 repository、Issue、PR、workflow、release 和相关状态；
- 引用 GitHub canonical state（规范状态）；
- 为数字资产理解、风险审查和人类注意力候选提供 source-bound input。

GitHub 是第一阶段的 first sensor source（第一个传感来源），但不是：

- TITMAS 的唯一入口；
- TITMAS 或 Digital Biosphere 的 Authority；
- TITMAS 控制能力的基础；
- 整个数字生态；
- continuous monitoring 的授权；
- GitHub 之外服务状态的替代来源。

```text
GITHUB_FIRST=true
GITHUB_ONLY=false
GITHUB_IS_SENSOR_SOURCE=true
GITHUB_IS_TITMAS_AUTHORITY=false
GITHUB_IS_CONTROL_FOUNDATION=false
CONTINUOUS_GITHUB_MONITORING_AUTHORIZED=false
```

GitHub 继续拥有 GitHub 账户、权限、repository、Issue、PR、workflow、release 和平台
状态的 canonical state。TITMAS 只保留有界引用、时间戳、来源说明、局部解释和限制；
它不复制 GitHub 的完整状态，不写回 GitHub，也不把缓存或摘要升级为 Truth。

## 6. External Ecosystem Boundary（外部生态边界）

外部服务继续保持各自 Authority、canonical state、账户、Permission、数据和运行能力：

| External system | Retained canonical responsibility | TITMAS bounded relationship |
|---|---|---|
| GitHub | source code hosting、repository、Issue、PR、workflow、release、account and Permission state | first bounded sensing source |
| Render | deployment、build、runtime and service status | source-bound runtime-health reference |
| Supabase | database、authentication、storage and service state | source-bound data-service reference |
| Context7 | documentation retrieval service and its cited sources | knowledge-source reference with limitations |
| Linear | planning、Issue and workflow state | planning-source reference |
| Cloudflare | network、DNS、security and edge-service state | source-bound service-health reference |
| Codex | human-authorized coding and execution assistance | separately authorized execution assistant |
| Similar services | their own domain state and operational capability | bounded observation/reference only |

TITMAS 不重建或替代这些服务，也不建立一个统一数据库、统一权限层、统一账户层或跨服务
控制平台。每项引用必须允许人返回 canonical source 核对 freshness 和限制。

“External systems are organs; TITMAS is the immune system.”（外部系统是生态器官，
TITMAS 是免疫系统）只是一种 non-normative metaphor（非规范性比喻），用于说明相互
依赖但职责分离；它不转移 Authority、Truth、Ownership、Permission 或法律责任。

## 7. No Duplicate Immune Principle（禁止重复免疫建设原则）

不得为了强化“Immune”叙事而创建：

- `agent-evidence/immune`；
- `titmas-immune-core`；
- 第二个 Health engine；
- 第二个 Cockpit；
- 第二套 Evidence Schema；
- 统一外部服务控制平台；
- 与现有组件职责实质相同但更换名称的新组件。

在 `agent-health`、`titmas-health`、SAEE immune surface 和 `titmas-demo` 的 Owner、
canonical responsibility、保留／合并／废弃处置尚未由 Human Authority 明确前，不得
创建类似 Implementation。

任何新组件提案必须先回答：

1. 是否已有相同或相邻能力；
2. 是否减少整合复杂度和人工管理成本；
3. 是否新增 Authority、Truth、Permission 或 shadow state；
4. 是否复制外部服务、Schema、Health、Evidence、Cockpit 或 Evaluation；
5. 新能力收益是否大于长期维护负担。

未通过时保持理论记录或 `BLOCK`，不得创建。

## 8. Responsibility and Authority Separation（职责与权力分离）

| Role | May do | Must not do |
|---|---|---|
| Source owner | maintain canonical domain state | surrender Authority because TITMAS references it |
| Sensor / observer | collect bounded source observations | decide, execute or declare Truth |
| Agent Evidence | package and locally validate Evidence candidates | admit canonical Truth or decide response |
| Agent Health | diagnose scoped repository health and recommend | control repository or auto-fix |
| SAEE | read-only bounded evaluation and recommendation | write back, authorize or execute |
| DBA Cockpit | aggregate source-bound situational references and attention candidates | become control plane, Permission surface or Truth owner |
| Human Authority | authorize decisions and actions within explicit scope | retroactively rewrite source facts |
| Codex / executing Agent | execute only the separately authorized action | self-authorize, broaden scope or become decision owner |

规范流程保持：

```text
Observe
  -> Evaluate
    -> Authorize
      -> Execute
        -> Verify and create new Evidence
```

Observation、Evaluation、Authority、Execution 和 Verification 不得由一个默认自动
主体合并。工具能执行动作不等于它获得执行授权。

## 9. Evidence, Health, Evaluation and Attention Boundary

- Evidence First 表示决定必须能够返回有来源的 Observation／Evidence Candidate／
  accepted Evidence；不表示所有 Observation 自动成为 Evidence 或 Evidence 等于 Truth。
- Health 是 source-bound diagnosis（带来源诊断），不是 Permission 或处置权。
- SAEE Evaluation 是只读、版本化、受范围约束的建议输入，不得写回 DBOS、Health、
  Evidence 或外部系统。
- Attention 是 Human Attention Amplification（人类注意力放大），只形成可解释、可被
  覆盖的候选顺序；未被选中不形成 negative Evidence（负面证据）。
- Human Authority 决定是否接受、延后、拒绝或授权后续动作。
- 新反馈形成新 Observation、新 Evidence 与新 review；不得改写历史以支持当前结论。

## 10. Carried-forward v0.1 Boundaries（承接 v0.1 的边界）

以下 v0.1 原则继续有效，并在 v0.2 中服从 Immune Identity：

1. vendor-neutral and framework-neutral（供应商中立、框架中立）；
2. adapter/profile over fork（优先有界适配与 profile，不复制完整外部 stack）；
3. exact source and version binding（精确来源与版本绑定）；
4. preserve source semantics（保留来源语义）；
5. no semantic elevation（禁止语义抬升）；
6. fail closed and retain unknowns（失败关闭并保留未知）；
7. privacy and least data（隐私与最少数据）；
8. SAEE read-only and advisory-only（SAEE 只读且仅建议）；
9. agent-readable discovery（智能体可读发现）；
10. Specification、Demo、Validation、Review 与 Implementation、Release、Adoption、
    Production 相互独立。

这些原则不授权新的 protocol、schema、adapter、conformance implementation 或公共
基础设施。

## 11. TITMAS Drift Check（TITMAS 漂移检查）

每次重大 Codex TITMAS 任务的 final response（最终答复）必须包含：

```text
TITMAS_DRIFT_CHECK

PRIMARY_IMMUNE_OBJECTIVE_PRESERVED=true|false
SINGLE_HUMAN_MANAGEMENT_COST_REDUCED=SUPPORTED|NOT_MEASURED|NOT_SUPPORTED
NEW_CONTROL_AUTHORITY_CREATED=true|false
EXTERNAL_SERVICE_REPLACED=true|false
NEW_TRUTH_SOURCE_CREATED=true|false
DUPLICATE_COMPONENT_CREATED=true|false
CURRENT_CAPABILITY_OVERCLAIMED=true|false
IMPLEMENTATION_AUTHORIZED=true|false
```

若以下任一值为 `true`：

- `NEW_CONTROL_AUTHORITY_CREATED`；
- `EXTERNAL_SERVICE_REPLACED`；
- `NEW_TRUTH_SOURCE_CREATED`；
- `DUPLICATE_COMPONENT_CREATED`；
- `CURRENT_CAPABILITY_OVERCLAIMED`；

则必须记录：

```text
TITMAS_DRIFT_STATUS=STOP_AND_HUMAN_REVIEW_REQUIRED
```

否则记录：

```text
TITMAS_DRIFT_STATUS=PASS_WITH_RECORDED_LIMITATIONS
```

Drift Check 是 mandatory Human Review Gate（强制人工审查闸门），不是 automated
enforcement（自动执行机制）。它只支持显式报告、停止扩大相关提案范围和请求人工审查；
不得自动阻断运行系统、删除、隔离、回滚、修改 Permission、修复或响应。

`IMPLEMENTATION_AUTHORIZED` 必须来自单独且明确的人类授权；Charter、Review、Drift
Check `PASS` 或其他文档状态均不能把它改为 `true`。

## 12. Consistency and Conflict Handling（一致性与冲突处理）

本章程必须与以下边界保持一致：

- Digital Biosphere Program Charter；
- Digital Immune Constitution candidate；
- TITMAS Interface Boundary Map；
- `agent-health` 当前本地静态诊断边界；
- `agent-evidence` 当前 Evidence candidate／local validation／export 边界；
- SAEE read-only、evidence-bound、advisory-only、no-writeback 边界；
- Human Authority Gate；
- connected external services 的 canonical-source ownership。

如果本章程条款与更高层治理文件、canonical child-project fact 或已经生效的 Human
Decision 冲突：

1. 记录 exact source、版本／hash、冲突条款和影响范围；
2. 将冲突条款标为 `STOP_AND_HUMAN_REVIEW_REQUIRED`；
3. 停止扩大与该条款有关的 TITMAS scope；
4. 不由 Codex、Cockpit、Health、Evidence、SAEE 或本章程自行解释并解决；
5. 不影响无冲突条款继续作为项目护栏。

## 13. Change and Implementation Gate（变更与实现闸门）

本章程的后续修改需要 source-bound review、显式 Human Decision 和新版本。任何代码、
Schema、API、Dashboard、Adapter、Repository、continuous monitoring、automatic
response 或 external writeback 都必须取得独立授权，并在相应 canonical repository
完成实施与验证。

```text
CHARTER_V0_1_PRESERVED=true
CHARTER_V0_2_CREATED=true
SECOND_PROJECT_CONSTITUTION_CREATED=false
IMMUNE_IMPLEMENTATION_CREATED=false
CONTINUOUS_MONITORING_CREATED=false
AUTOMATIC_RESPONSE_CREATED=false
IMPLEMENTATION_AUTHORIZED=false
```

本章程的采纳不等于 TITMAS 已实现、实验已执行、Cohort 已冻结、外部服务已集成、产品
已发布或生态已经采用。
