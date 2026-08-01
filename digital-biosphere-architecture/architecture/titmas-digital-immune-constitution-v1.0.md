---
document_id: DBA-TITMAS-DIGITAL-IMMUNE-CONSTITUTION-1.0
title: TITMAS Digital Immune Constitution v1.0
title_zh: TITMAS 数字免疫宪法 v1.0
status: DEVELOPMENT_CONSTITUTION_CANDIDATE
maturity: Development
maturity_scope: entire-document
architecture_owner_ref: zhangbin
decision_reference: NOT_DECIDED
freeze_reference: NOT_ASSIGNED
normative_effect: NONE
implementation_effect: NONE
execution_effect: NONE
---

# TITMAS Digital Immune Constitution v1.0

中文：TITMAS 数字免疫宪法 v1.0

## 0. Status and Interpretation（状态与解释）

本文是 Digital Immune（数字免疫）方向的 constitutional design candidate（宪法设计候选）。
它将数字免疫类比转换为可审查的架构原则，但当前不构成已冻结规范、实现授权、运行策略、
自动响应规则或项目能力事实。

```text
DOCUMENT_MATURITY=Development
DIGITAL_IMMUNE_CONSTITUTION_ADOPTED=false
DIGITAL_IMMUNE_CONSTITUTION_FROZEN=false
NORMATIVE_EFFECT=NONE
IMPLEMENTATION_AUTHORIZED=false
AUTOMATIC_RESPONSE_AUTHORIZED=false
```

本候选受
[`Digital Biosphere Open Infrastructure Strategy Constitution`](open-infrastructure-strategy-constitution.md)
约束。发生冲突时，既有 DBOS/SAEE、Authority、Permission、Evidence 和 Governance
边界优先；类比语言不得覆盖规范对象所有权或仓库能力事实。

## Preamble（序言）

未来人工智能生态可能由大量自治程度不同的数字主体和服务组成。它们可以具有身份、
能力边界、行为历史、记忆引用与适应机制，但这些属性必须由适用规范和事实分别证明，
不能因被称为 Agent、Digital Entity 或 Digital Cell 而自动成立。

TITMAS 不追求创造一个无限强大的中心智能，而采用以下长期方向：

> 通过大量简单、有限、可验证主体之间的结构化组合，形成具有广泛覆盖能力、
> 适应能力和长期稳定性的数字生态。

英文：

> TITMAS does not pursue an unbounded central intelligence. It seeks broad
> coverage, adaptability, and long-term stability through the governed
> composition of many simple, bounded, and verifiable digital entities.

“简单”表示职责有限、边界明确且可替换；“结构化组合”表示使用显式契约和可观察交互；
“覆盖能力”不表示正确性、Truth、Permission 或全局 Authority。

本阶段的 `Digital Cell` 只是待审查的 qualification/profile metaphor（资格／画像类比）：
它可用于描述一个 Digital Entity 是否具备最低数字免疫结构，但不自动创建新的实体类别，
也不把 Agent、Digital Entity、Digital Organism 或 Runtime 等同起来。

```text
Digital Entity != Digital Cell
Digital Cell != Agent
Digital Cell != Digital Organism
Digital Cell != Runtime
```

## 1. Principle of Distributed Complexity Generation（分布式复杂性生成原则）

系统级能力可以由多个受限主体、协议和关系的组合产生，而不必依赖单一超级 Agent。

```text
bounded entity A
  + bounded entity B
  + bounded entity C
  + explicit protocols
  + observable relationships
  -> candidate system-level capability
```

TITMAS 鼓励小职责、明确边界、可组合、可替换和可局部失效的设计；不鼓励无限增强
单一 Agent、无限扩大权限或把不可审计控制集中到一个中心。

组合产生的能力仍须被独立观察和验证。组合不自动聚合 Authority、Permission、
Decision 或 Truth Ownership。本原则继承
[`ADR-032`](ADR-032-compositional-scale-over-unbounded-center.md)。

## 2. Principle of Digital Identity（主体可识别原则）

任何希望进入受治理数字生态的主体必须能够回答：

> 我是谁，我由谁负责，我处于什么生命周期和边界中？

最低身份描述应能引用：

- stable identity reference（稳定身份引用）；
- entity type and version（主体类型与版本）；
- owner or accountable party reference（所有者或责任方引用）；
- purpose（目的）；
- lifecycle state（生命周期状态）；
- capability and boundary references（能力与边界引用）；
- relevant history references（相关历史引用）。

Permission 可以被身份记录引用，但不属于身份事实本身：

```text
Identity != Permission
Identity reference != Permission grant
```

POP 可作为 identity-related reference（身份相关参考），但本候选不声明 POP 已成为
TITMAS 或 DBOS 的规范身份系统。

## 3. Principle of Verifiable Action（行为可证明原则）

受治理范围内的重要行为应形成可追溯的 Evidence Chain（证据链）：

```text
Intent reference
  -> Action reference
    -> Execution record
      -> Evidence candidate
        -> Admission and verification
```

并非所有日志都是 Evidence；Observation 必须经过来源、完整性、范围和适用规则检查，
才能进入相应证据边界。

> Evidence can support a claim about execution history; it does not prove
> intelligence, correctness, scientific validity, or absolute truth.

中文：

> 证据可以支持关于执行历史的主张，但不证明智能、结果正确性、科学有效性或绝对真相。

AEO、Agent Evidence 和 VEC 可以作为该方向的 reference candidates（参考候选），
不因本文件而成为已采纳对象、认证或已实现能力。

## 4. Principle of Bounded Autonomy（边界优先原则）

自治必须在显式边界内存在。每个受治理主体至少需要区分：

- declared capability（声明能力）；
- allowed scope（允许范围）；
- constraints（约束）；
- forbidden actions（禁止动作）；
- unknown or unresolved capability（未知或未决能力）；
- applicable authorization and context references（适用授权与上下文引用）。

```text
Capability != Authority
Capability != Permission
Execution requires Capability + Authorization + Context
```

边界不是对智能的否定，而是主体能够被安全组合、替换、隔离和治理的前提。

## 5. Principle of Evidence First（证据优先原则）

结果不能直接产生信任。受治理信任路径应优先表达为：

```text
Execution
  -> Observation
    -> Evidence admission
      -> Verification
        -> bounded trust claim
```

该路径只产生有范围、有方法、有版本和有限制的 trust claim（信任主张），不产生
Truth、Permission、Certification 或无限责任转移。

```text
Observation != Evidence
Evidence != Truth
Verification != Permission
Receipt != Evidence Truth
```

## 6. Principle of Digital Homeostasis（动态平衡原则）

数字生态不以最大化单一指标作为唯一目标。效率、安全、适应性、稳定性、资源分配与开放性
之间可能存在冲突，需要以明确方法和时间窗口进行多维评价。

Digital Homeostasis（数字稳态）在本候选中是一种 evaluation objective（评价目标），
不是自动控制器、健康事实、权限来源或执行授权。SAEE 可以提供只读评价与建议；
Governance Decision 决定是否采纳；DBOS 只执行显式批准且属于其运行边界的变化。

## 7. Principle of Adaptive Response（免疫响应分级原则）

异常响应不应只使用无上下文的“允许／禁止”二元模型。设计时可以使用以下分级语义：

| Level | Candidate meaning | Required boundary |
|---|---|---|
| `0` | Normal（正常） | 保持观察和既有边界 |
| `1` | Observe（观察） | 增强记录，不扩大权限 |
| `2` | Restrict（限制） | 最小必要、范围受限、可复核 |
| `3` | Isolate（隔离） | 显式授权、可恢复、保留历史 |
| `4` | Retirement or removal candidate（退役或移除候选） | 独立决定、执行留证、禁止自动淘汰 |

Health score、Reputation、模型输出或 SAEE Recommendation 均不能自动触发任何等级。
实际响应必须有明确 Authority、适用范围、理由、证据引用、期限和恢复条件。

## 8. Principle of Memory Continuity（历史连续性原则）

数字主体的重要成功、失败、修复、评价、适应和治理变化应保持可追溯连续性。

Memory Continuity 不要求无限保存所有数据，也不允许违反隐私、数据最小化、保留期限、
删除义务或安全边界。规范应区分：

- immutable lineage references（不可静默改写的来源链引用）；
- governed retention（受治理保留）；
- correction and supersession（更正与后继记录）；
- privacy-preserving redaction（保留可追溯性的隐私删减）；
- failed and disputed outcomes（失败与争议结果）。

删除展示内容不应静默删除历史事实；更正不得伪装成原始事实从未发生。

## 9. Principle of Evolutionary Selection（生态选择原则）

生态中的适应与选择不应由一次结果、单一分数或某个中心的无解释判断决定。长期评价可以综合：

- performance（表现）；
- adaptability（适应性）；
- stability（稳定性）；
- evidence quality（证据质量）；
- reputation with provenance（有来源的声誉）；
- risk and resource context（风险与资源上下文）。

Fitness 是带方法、版本、范围和不确定性的评价结果，不是 Truth 或 Authority。
SAEE 负责评价与 Evolution Recommendation；Governance Decision 负责采纳决定；
DBOS 负责获批变化的存在与生命周期执行记录。任何评价都不能自动授予 Permission、
修改能力或淘汰主体。

## 10. Principle of Open Evolution（开放演化原则）

开放数字生态应允许新主体提出进入、旧主体受治理退出、规则按版本演进、能力在显式契约下
迁移，并避免单一实现或供应商锁定。

开放进入不等于自动准入；规则升级不等于 Runtime 自动升级；能力迁移不等于权限继承；
退出不等于删除历史。

```text
Open entry != automatic admission
Version change != implementation change
Capability migration != permission inheritance
Retirement != history deletion
```

## 11. Constitutional Architecture Map（宪法架构映射）

```text
Digital Biosphere
  |
  +-- Open Infrastructure Strategy Constitution
        |
        +-- TITMAS Digital Immune Constitution Candidate
              |
              +-- Identity
              +-- Boundary
              +-- Evidence
              +-- Health
              +-- Reputation
              |
              +-- Agent / Digital Entity Ecosystem
                    |
                    +-- Evaluation and governed evolution
```

五个概念面不自动建立五套系统：

| Conceptual surface | Canonical boundary |
|---|---|
| Identity | DBOS existence-governance ownership or an explicitly adopted mapping |
| Boundary | DBOS capability/lifecycle records plus explicit Governance Decision |
| Evidence | DBOS evidence/admission/verification boundary; Evidence remains distinct from Truth |
| Health | evaluation input/output with method and scope; not automatic authority |
| Reputation | derived, provenance-bound and contestable evaluation; not identity or permission |

## 12. Existing Project Crosswalk（现有项目交叉映射）

以下映射是 architecture role hypothesis（架构角色假设），不是所有权迁移、集成事实或
能力声明：

| Project or concept | Candidate constitutional role | Non-claim |
|---|---|---|
| POP | Identity-related reference | 不声明其为 canonical identity authority |
| Agent Evidence / AEO | Evidence-chain reference | 不声明 Observation 已被准入为 Evidence |
| VEC / VEAP | Execution-attestation reference | 不声明已签发证书、通过符合性或获得认证 |
| SAEE | Health, stability and evolution evaluation reference | 不拥有执行、身份或自动响应权 |
| Agent Health | Health interface candidate | 不声明 Health schema 或 Runtime 已采纳 |
| ARO / ARO-Audit | Audit and governed-response reference | 不拥有自动治理权 |
| TEK-Bench | Stress-test reference | 测试结果不等于生产可靠性 |
| DBL / Digital Ecology Box | Evolution experiment reference | 实验或模拟不等于生态事实 |

任何交叉映射进入 `adopted` 状态前，必须有 canonical source、Owner、接口边界、
版本、负面符合性用例和 Architecture Decision。

## 13. Constitutional Review Gate（宪法审查闸门）

本候选进入 `Accepted` 或 `Frozen` 前必须至少回答：

1. Digital Immune 是架构类比、规范域还是公开协议命名？
2. Identity、Boundary、Evidence、Health、Memory 和 Reputation 的 canonical Owner 分别是谁？
3. Health 与 Reputation 如何避免成为 Permission、Authority 或不可申诉的黑箱分数？
4. Level 0–4 响应由谁决定、谁执行、谁复核、如何撤销？
5. 哪些行为属于“重要行为”，证据保留如何兼顾隐私和数据最小化？
6. Digital Cell 与既有 Digital Entity Specification 的差异是否足以建立新术语？
7. AEO、VEC、VEAP、POP、ARO、TEK-Bench 和 DBL 的名称、仓库事实与 Owner 是否已核验？
8. 组合级风险、级联失败和隐藏协调中心如何进行符合性测试？

以上问题未决时，后续 Digital Cell、Immune Response、Health、Reputation 和 Ecology
文档只能引用本文件为 `DEVELOPMENT_CANDIDATE`，不能标记为冻结宪法引用。

## 14. Non-effects（非效果）

本候选：

- 不创建 Agent、Digital Entity、Digital Cell、Digital Organism 或 Runtime；
- 不创建 Capability、Permission、Authority、Evidence Truth、Health score 或 Reputation；
- 不授权 Level 0–4 自动响应、隔离、退役或淘汰；
- 不修改 DBOS、SAEE 或任何外部项目；
- 不采纳 AEO、VEC、VEAP、POP、ARO、TEK-Bench 或 DBL 为规范实现；
- 不授权代码、API、实验、部署、发布、认证、商业服务或外部宣传；
- 不改变 TITMAS Developer Community、Foundation 或 public contribution 的当前状态。

```text
DBOS_GOVERNS_EXISTENCE=true
SAEE_GOVERNS_EVOLUTION=true
DBOS_NE_SAEE=true
IDENTITY_NE_PERMISSION=true
CAPABILITY_NE_PERMISSION=true
EVIDENCE_NE_TRUTH=true
EVALUATION_NE_AUTHORITY=true
RECOMMENDATION_NE_DECISION=true
DECISION_NE_EXECUTION=true
COMPOSITION_NE_AUTHORITY_AGGREGATION=true
DIGITAL_ENTITY_NE_DIGITAL_CELL=true
DIGITAL_CELL_NE_AGENT=true
DIGITAL_CELL_NE_DIGITAL_ORGANISM=true
DIGITAL_CELL_NE_RUNTIME=true
DIGITAL_CELL_CREATED=false
DIGITAL_ORGANISM_CREATED=false
AUTOMATIC_IMMUNE_RESPONSE_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
```
