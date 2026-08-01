---
document_id: DBA-TITMAS-INTERFACE-BOUNDARY-MAP-0.1
title: TITMAS Interface Boundary Map v0.1
title_zh: TITMAS 接口边界图 v0.1
status: ARCHITECTURE_BOUNDARY_MAP_CANDIDATE
maturity: Development
maturity_scope: entire-document
primary_repository: digital-biosphere-architecture
document_type: NON_EXECUTABLE_ARCHITECTURE_BOUNDARY_MAP
created_at: 2026-07-28
source_state_report_ref: /Users/zhangbin/GitHub/agent-evidence/TITMAS_CURRENT_STATE_REPORT.md
source_architecture_decision_ref: architecture/TITMAS_ARCHITECTURE_DECISION_RECORD_v0.1.md
source_constitution_revision_ref: architecture/TITMAS_CONSTITUTION_REVISION_PROPOSAL_v1.1.md
human_decision_status: PENDING
interface_freeze_status: NOT_READY
authority_effect: NONE
implementation_effect: NONE
schema_effect: NONE
protocol_effect: NONE
runtime_effect: NONE
repository_effect: NONE
external_action_effect: NONE
---

# TITMAS Interface Boundary Map v0.1

中文：TITMAS 接口边界图 v0.1。

## 0. Status and scope（状态与范围）

本文件定义 DBA、DBOS、POP、Agent Evidence、Agent Health、SAEE、TITMAS
interoperability domain（互操作域）、DBA Cockpit 内的 TITMAS Situational View
（TITMAS 态势视图）和 Human Authority（人类权威）之间的概念级职责、输入、输出、
Authority 边界、数据方向和禁止依赖。

它只回答：

- 谁负责什么；
- 哪一类信息可以从哪里流向哪里；
- 接收方不能从输入推导出什么；
- 哪些反馈必须通过新记录返回；
- 哪些接口仍然是 Candidate、Gap 或 Human Decision Required。

它不定义字段、JSON、Schema、API、endpoint、transport、SDK、adapter、database、
dashboard、permission policy 或 Runtime 调用。

```text
INTERFACE_BOUNDARY_MAP_DEFINED_AS_CANDIDATE=true
TITMAS_INTERFACE_V0_1_DEFINED=false
TITMAS_INTERFACE_V0_1_FROZEN=false
AUTHORITY_FREEZE_ADOPTED=false
IMPLEMENTATION_READINESS=NOT_READY
IMPLEMENTATION_AUTHORIZED=false
```

### 0.1 Sources（来源）

本边界图基于：

- `/Users/zhangbin/GitHub/agent-evidence/TITMAS_CURRENT_STATE_REPORT.md`；
- [`TITMAS Architecture Decision Record v0.1`](TITMAS_ARCHITECTURE_DECISION_RECORD_v0.1.md)；
- [`TITMAS Constitution Revision Proposal v1.1`](TITMAS_CONSTITUTION_REVISION_PROPOSAL_v1.1.md)；
- [`TITMAS Interface Readiness Review v0.1`](titmas-interface-readiness-review-v0.1.md)；
- [`Digital Biosphere Program Governance Charter`](../PROGRAM-CHARTER.md)；
- [`ADR-016: Program Governance Cockpit`](ADR-016-program-governance-cockpit.md)；
- [`Authority Freeze Decision Record`](authority-freeze-decision-record-v0.1.md)。

仓库和 domain canonical source（领域规范来源）优先于本图。本图中的 `ALLOWED` 只表示
architecture-eligible direction（架构上可进入后续审查的方向），不表示 runtime
Permission、账号权限、接口存在或实现授权。

## 1. Boundary vocabulary（边界词汇）

### 1.1 Artifact classes, not schemas（工件类别，不是 Schema）

| 类别 | 含义 | 不表示 |
|---|---|---|
| `SOURCE_REFERENCE` | 指向 canonical source、版本、观察时间和范围的引用 | 被引用内容已被采纳或仍然最新 |
| `OBSERVATION_MATERIAL` | 保留来源与限制的观察材料 | Evidence、Truth |
| `EVIDENCE_CANDIDATE` | 可提交准入或离线复核的 evidence package candidate | DBOS-admitted Evidence、Truth |
| `VALIDATION_RECEIPT` | 某 validator 在给定版本和范围内的结果 | Certification、DBOS admission |
| `ADMISSION_RESULT` | 适用 DBOS Owner/process 对准入请求的有范围处理结果 | absolute Truth、Permission |
| `HEALTH_FINDING` | 某方法对指定 repository snapshot 的诊断结果 | runtime safety、全局健康、Command |
| `EVALUATION_RECOMMENDATION` | SAEE 对有来源输入的评价、风险或演化建议 | Decision、Authorization、writeback |
| `DECISION_RECORD` | 人类或显式委托 Authority 作出的有范围决定 | 执行已经发生 |
| `AUTHORIZATION_REFERENCE` | 对对象、动作、期限和撤销条件的授权引用 | 通用 Permission 或永久权力 |
| `EXECUTION_RESULT` | 被授权 executor 对实际动作结果的记录 | verified success、Truth |
| `SITUATIONAL_PROJECTION` | DBA Cockpit 对 source-bound 状态、风险和待决事项的只读投影 | canonical project status、Truth source |

这些名称是概念分类，不创建同名对象或格式。

### 1.2 Interface states（接口状态）

| 状态 | 含义 |
|---|---|
| `CURRENT_LOCAL_SURFACE` | 当前项目已核验的本地职责面 |
| `REFERENCE_ONLY` | 只引用来源，不拥有来源事实 |
| `CANDIDATE_HANDOFF` | 数据方向可以审查，但 Owner、版本、失败语义或实现尚未冻结 |
| `CANONICAL_DOMAIN_BOUNDARY` | 既有架构已确认该 domain 的规范责任 |
| `HUMAN_DECISION_REQUIRED` | 本图不能决定 |
| `PROHIBITED` | 与当前不变量冲突 |
| `NOT_ESTABLISHED` | 不得声称接口或能力存在 |

## 2. System boundary overview（系统边界总览）

```text
                         Human Authority
                   decision / authorization only
                              |
                              v
                    Authorized Executor Role
                   (not a component in this map)
                              |
                              v
                       new execution result
                              |
                              v
Source operation ---> Observation / Evidence Candidate ---> DBOS admission
      |                         ^                              |
      |                         |                              v
      |                  Agent Evidence                canonical scoped refs
      |                                                       |
      +---- repository snapshot ---> Agent Health             v
                                     finding             SAEE evaluation
                                                           recommendation
                                                                  |
                                                                  v
                                                           Human Authority

Canonical source references / findings / recommendations
                              |
                              v
                      DBA Cockpit
                TITMAS Situational View
               reference-only awareness
```

该图包含多条独立路径，不表示所有操作必须先经过 Agent Evidence、所有 Health finding
必须进入 DBOS、所有项目必须调用 SAEE，或所有决定必须由某个单一 Runtime 串行编排。

TITMAS interoperability domain 可以为这些 handoff 提出 mapping/profile/contract
candidate，但它不位于数据路径中央，也不处理运行数据。

## 3. Core component responsibility map（核心组件唯一职责）

| 组件／角色 | 唯一职责 | 明确不拥有 | 当前状态 |
|---|---|---|---|
| **DBA** | Program Governance、Architecture Specification、ADR、gate、风险、依赖、状态引用和单一 Cockpit | child-project truth、Runtime、DBOS state write、SAEE algorithm、execution | `CANONICAL_PROGRAM_GOVERNANCE_BOUNDARY` |
| **DBOS** | Identity、Capability record、Execution record、Evidence admission、Verification、Lifecycle 的 canonical existence boundary | absolute Truth、SAEE evaluation、Human Decision、自动授权 | `CANONICAL_DOMAIN_BOUNDARY_WITH_INTERFACE_GAPS` |
| **POP** | portable persona reference/projection 的 project-local 表面；未来可提交显式 DBOS mapping | authentication、canonical identity、Permission、Agent completeness | `REFERENCE_ROLE_MAPPING_NOT_ADOPTED` |
| **Agent Evidence / `agent-evidence`** | completed-operation observation 的 capture、package、profile validation、export、offline verification reference | DBOS admission、Truth、Certification、governance、Agent Immune host | `CURRENT_LOCAL_SURFACE` |
| **Agent Health / `agent-health`** | 本地静态 repository-health diagnosis、finding、why、applicability、limitation 和 recommendation | runtime monitor、automatic fix、Permission、Evidence infrastructure、SAEE evolution | `CURRENT_LOCAL_SURFACE_SCOPE_BOUNDED` |
| **SAEE** | 有来源、只读、有界的 reliability、stability、risk、fitness、adaptation 和 evolution evaluation/recommendation | DBOS writeback、Command、Permission、Human Approval、public core service | `PROTECTED_DOMAIN_INTERFACE_NOT_APPROVED` |
| **TITMAS interoperability domain** | 在 DBA 委托范围内提出 mapping、profile、handoff、adapter contract 和 conformance architecture | 第二 DBA、canonical object ownership、Runtime、Truth store、control plane | `PROPOSED_DOMAIN_AUTHORITY_NOT_ADOPTED` |
| **TITMAS Situational View** | DBA Cockpit 内面向 TITMAS 的 source-bound 状态、风险、unknown 和 decision-required 投影 | 独立 Cockpit、Truth source、Permission、Command、child write | `REFERENCE_ONLY_LOGICAL_VIEW` |
| **Human Authority** | 对采纳、范围、授权、高影响变化、发布和外部动作作显式决定 | 自动执行、旧 Evidence 改写、由模型分数自动替代 | `REQUIRED_DECISION_BOUNDARY` |

### 3.1 Non-core execution role（非核心执行角色）

Codex 或其他 Agent 可以在具体决定中成为 authorized executor（获授权执行者），但
“Executor”不是本图新增项目，也不是固定由 Codex 担任。执行资格来自一次有范围的
Authorization、目标项目规则和实际账号／Permission，不来自本架构图。

```text
ARCHITECTURE_ROLE_NE_RUNTIME_PERMISSION=true
DECISION_RECORD_NE_EXECUTOR_CREDENTIAL=true
```

## 4. Component input, output and authority boundaries（组件输入输出与权力边界）

### 4.1 DBA

**可接受的概念输入**

- 带 canonical source、version/commit、`observed_at` 和 freshness 的状态引用；
- Architecture Proposal、duplicate review、risk、blocker 和 interface gap；
- Human Decision Record；
- DBOS、Agent Evidence、Agent Health、SAEE 等项目提供的有范围结果摘要。

**可产生的概念输出**

- Program Charter、architecture rule、ADR、Decision Queue；
- Ownership/Interface boundary、integration gate 和 risk register；
- reference-only Program Status 与 Cockpit projection；
- 需要下游项目分别处理的有范围 implementation work item candidate。

**Authority 边界**

- 可以维护 DBA 自身规范和项目群决定入口；
- 不写入 DBOS、SAEE、POP、Agent Evidence 或 Agent Health 的 canonical facts；
- 不运行 Agent，不执行授权动作，不修改 child repository；
- dashboard observation 不升级为 project truth。

### 4.2 DBOS

**可接受的概念输入**

- Identity、Capability、Execution、Lifecycle 的 project-local source material；
- 具有 source、scope、version 和 limitation 的 Evidence admission request candidate；
- 显式授权的 lifecycle/execution state-change request；
- 已采纳 mapping 所允许的 external reference。

**可产生的概念输出**

- canonical scoped identity/capability/execution/evidence/verification/lifecycle record；
- admission 的 accepted、rejected、partial、unknown 或 conflicted result；
- 可供有界消费者引用的 versioned record reference；
- 对获授权 state change 的 execution/lifecycle record。

**Authority 边界**

- DBOS 拥有 canonical existence/record boundary，不代表它拥有 absolute Truth；
- DBOS 不能从收到 admission request 推导 Permission；
- DBOS 不能自我授予变化授权；
- DBOS 不执行 SAEE evaluation，也不因 SAEE recommendation 自动改变状态。

### 4.3 POP

**可接受的概念输入**

- POP project-local canonical material；
- persona reference/projection request；
- 未来显式 DBOS mapping 所需的 bounded source reference。

**可产生的概念输出**

- portable persona object/reference/projection；
- source/version-bound persona reference；
- mapping candidate，不是 canonical DBOS identity。

**Authority 边界**

- POP 不证明 authentication；
- persona reference 不授予 Permission；
- POP 不能覆盖 DBOS Identity/Lifecycle；
- POP 到 DBOS 的 mapping 未经 adopted decision 前保持 `CANDIDATE_HANDOFF`。

### 4.4 Agent Evidence

**可接受的概念输入**

- completed-operation observation material；
- actor、subject、operation、time、policy、provenance 和 evidence reference material；
- local profile/bundle validation request；
- DBOS canonical record reference 的 export request，若来源和 scope 允许。

**可产生的概念输出**

- Evidence candidate package；
- EEOAP/profile validation result；
- local bundle/export、manifest、receipt 和 integrity reference；
- limitations、unsupported、partial、unknown 和 failure。

**Authority 边界**

- validator `PASS` 不等于 DBOS admission、Truth、Permission 或 Certification；
- 不直写 DBOS canonical Evidence；
- 不为验证通过而请求修改原始 DBOS record；
- 不复制 DBOS canonical object ownership；
- 不变成 Agent Health、SAEE 或 TITMAS Runtime。

### 4.5 Agent Health

**可接受的概念输入**

- local repository snapshot；
- 静态配置、依赖、文档、测试和项目可发现信号；
- 当前产品范围内可解释的 repository-health signal。

**可产生的概念输出**

- scoped Health finding；
- finding rationale、applicability、why 和 when-not-applicable；
- bounded recommendation 和 limitation；
- timestamped local artifact，若当前项目已支持。

**Authority 边界**

- finding 只描述被扫描 snapshot，不证明 runtime safety；
- Health score 不等于 Permission、Evidence Truth 或 SAEE Fitness；
- 不自动修改 repository、关闭 Agent、限制权限或触发隔离；
- 不把行为漂移、权限漂移或生态异常写成已实现能力；
- `agent-health` v0.2.1 correction-only scope 不因本图扩大。

### 4.6 SAEE

**可接受的概念输入**

- 只有在相关 interface 获 Owner 批准后，接收 DBOS-admitted、versioned、scoped、
  read-only references；
- 评价方法允许且明确标注的 context、time window、limitations 和 uncertainty；
- 不足、冲突、过期和 unsupported 状态。

**可产生的概念输出**

- reliability、stability、risk、fitness 或 adaptation evaluation；
- method/version/time-window-bound recommendation；
- uncertainty、limitation、failure 和 review requirement；
- Evolution Recommendation，不是命令。

**Authority 边界**

- 不直接消费 raw telemetry、未准入 Evidence candidate 或 Cockpit narrative 作为 Truth；
- 不写回 DBOS、Agent 或 repository；
- 不自动改变 Identity、Capability、Permission 或 Lifecycle；
- 不公开或复制 protected core；
- 不把 recommendation 升级为 Human Decision。

### 4.7 TITMAS interoperability domain

**可接受的概念输入**

- 各 source/spec Owner 发布的 exact source、version 和 semantics；
- DBA-approved architecture question；
- DBOS、POP、Agent Evidence、Agent Health 和 SAEE Owner 的 boundary constraints；
- external standard 的 `REFERENCE_ONLY` material。

**可产生的概念输出**

- mapping/profile/handoff/adapter contract candidate；
- version、failure、non-elevation 和 conformance requirement candidate；
- architecture gap 和 decision request。

**Authority 边界**

- 当前无 adopted independent Architecture/Specification Authority；
- mapping 不创建 canonical DBOS/POP/EEOAP/SAEE object；
- conformance result 不产生 Certification、Adoption 或 Permission；
- 不运行 adapter，不存储运行数据，不管理 Portfolio 或 child status。

### 4.8 TITMAS Situational View within the DBA Cockpit

**可接受的概念输入**

- canonical source 的 bounded read-only reference；
- source-bound Evidence/Health/Evaluation summary；
- `observed_at`、version、freshness、scope 和 limitation；
- `UNKNOWN`、`STALE`、`CONFLICTED`、failure 和 decision-required state。

**可产生的概念输出**

- timestamped situational projection；
- source links、risk summary、gap、dependency 和 pending decision；
- agent-readable navigation to canonical source。

**Authority 边界**

- 只是 DBA Cockpit 中的 logical view，不是第二 Cockpit；
- 不成为 unified data layer、Truth store 或 program status Owner；
- 可以在有 source contract 时直接只读引用 child canonical source，不得写回；
- 不主动调用 Agent Health/SAEE 产生新评价；只展示已存在且允许展示的有范围结果；
- 不授权、不执行、不关闭 gate、不修改 Agent。

### 4.9 Human Authority

**可接受的概念输入**

- source-bound evidence/record references；
- Agent Health finding、SAEE recommendation、risk 和 alternatives；
- Architecture Decision packet；
- known unknowns、failure、security/privacy 和 rollback analysis。

**可产生的概念输出**

- `ACCEPT / REVISE / REJECT / DEFER`；
- 对特定对象、动作、范围、期限和 executor 的 authorization；
- revocation、expiry、review 和 appeal requirement；
- release/external-action decision，若明确在 scope 内。

**Authority 边界**

- Human Decision 不等于执行已经发生；
- decision 不修改历史 Evidence；
- 账号 Permission、Runtime capability 和具体 executor 仍须独立核验；
- 不从模型数量、投票、CI PASS、Health score 或 SAEE recommendation 自动生成决定。

## 5. Architectural responsibility matrix（架构职责矩阵）

本矩阵描述“哪类职责可归属哪个边界”，不是 runtime ACL 或 Permission grant。

| 组件／角色 | 架构规则 | canonical existence record | Evidence candidate | local validation | Evidence admission | static health diagnosis | evolution evaluation | situational projection | decide/authorize | execute |
|---|---|---|---|---|---|---|---|---|---|---|
| DBA | `PRIMARY` | `PROHIBITED` | `NO` | `NO` | `PROHIBITED` | `NO` | `PROHIBITED` | `PRIMARY` | `RECORDS_DECISION_ONLY` | `PROHIBITED` |
| DBOS | `DOMAIN_INPUT` | `PRIMARY` | `MAY_RECEIVE` | `DOMAIN_SPECIFIC_ONLY` | `PRIMARY` | `NO` | `PROHIBITED` | `SOURCE_REFERENCE` | `PROHIBITED` | `AUTHORIZED_DOMAIN_ACTION_ONLY` |
| POP | `DOMAIN_INPUT` | `REFERENCE_ONLY` | `NO` | `PROJECT_LOCAL` | `NO` | `NO` | `NO` | `SOURCE_REFERENCE` | `PROHIBITED` | `PROJECT_LOCAL_ONLY` |
| Agent Evidence | `DOMAIN_INPUT` | `PROHIBITED` | `PRIMARY` | `PRIMARY_LOCAL_SCOPE` | `PROHIBITED` | `NO` | `NO` | `SOURCE_REFERENCE` | `PROHIBITED` | `LOCAL_TOOL_ACTION_ONLY` |
| Agent Health | `DOMAIN_INPUT` | `PROHIBITED` | `NO_AUTOMATIC_EVIDENCE` | `NO` | `PROHIBITED` | `PRIMARY` | `NOT_SAEE_FITNESS` | `SOURCE_REFERENCE` | `PROHIBITED` | `NO_AUTOMATIC_FIX` |
| SAEE | `DOMAIN_INPUT` | `PROHIBITED` | `NO` | `NO` | `PROHIBITED` | `NO` | `PRIMARY_PROTECTED` | `SOURCE_REFERENCE` | `PROHIBITED` | `PROHIBITED_WRITEBACK` |
| TITMAS domain | `CANDIDATE_SCOPE` | `PROHIBITED` | `NO` | `NO_DUPLICATION` | `PROHIBITED` | `NO` | `NO_CORE_OWNERSHIP` | `NO_INDEPENDENT_COCKPIT` | `PROHIBITED` | `PROHIBITED` |
| TITMAS Situational View | `NO` | `READ_ONLY_REFERENCE` | `READ_ONLY_REFERENCE` | `NO` | `NO` | `READ_ONLY_RESULT` | `READ_ONLY_RESULT` | `PRIMARY_LOGICAL_VIEW` | `PROHIBITED` | `PROHIBITED` |
| Human Authority | `DECIDES_ADOPTION` | `NO_DIRECT_WRITE` | `NO` | `NO` | `NO_DIRECT_ADMISSION` | `NO` | `NO` | `CONSUMES` | `PRIMARY` | `SEPARATE_EXECUTOR_REQUIRED` |

`PROJECT_LOCAL_ONLY` 或 `LOCAL_TOOL_ACTION_ONLY` 不说明具体实现存在，只说明某组件不能借
TITMAS 边界获得跨项目权力。

## 6. Allowed interface directions（允许的数据方向）

### 6.1 Source and status awareness

```text
child canonical source
  -> bounded source reference
    -> DBA reference-only aggregation
      -> TITMAS Situational View
        -> Human awareness
```

条件：

- 保留 source、version、`observed_at`、freshness 和 scope；
- source unavailable 时显示 `UNKNOWN` 或 `STALE`；
- Cockpit 不回写 child source；
- projection 不能替代 child canonical status。

### 6.2 External or non-DBOS-native evidence candidate

```text
completed operation
  -> source-preserving observation material
    -> Agent Evidence package / local validation
      -> Evidence candidate + scoped receipt + limitations
        -> DBOS admission request candidate, when applicable
          -> DBOS admission result
```

当前状态：

```text
AGENT_EVIDENCE_LOCAL_SURFACE=CURRENT
AGENT_EVIDENCE_TO_DBOS_HANDOFF=CANDIDATE_NOT_FROZEN
DIRECT_DBOS_WRITE=PROHIBITED
```

### 6.3 DBOS-native execution and export

```text
authorized DBOS-domain execution
  -> DBOS canonical execution/evidence reference
    -> bounded Agent Evidence export/package, when allowed
      -> offline receipt or review artifact
```

export 不重新拥有或重新准入原 canonical record。若 export 后产生新的 assertion 或材料，
它是新的 candidate，不改变原 DBOS record。

### 6.4 Repository-health diagnosis

```text
local repository snapshot
  -> Agent Health static diagnosis
    -> finding + rationale + applicability + limitations
      -> Human review
      -> optional Cockpit reference-only projection
```

该路径可以独立运行，不强制先经过 Agent Evidence 或 DBOS。若未来需要把 finding 作为
Evidence candidate 打包，必须形成单独的 Owner、profile、version 和 non-elevation
contract；本图不授权该 adapter。

### 6.5 SAEE evaluation

```text
DBOS-admitted, versioned, scoped reference
  -> approved bounded read-only SAEE input
    -> evaluation + method + uncertainty + limitations
      -> Human Authority review
      -> optional Cockpit reference-only projection
```

当前状态：

```text
SAEE_PROTECTED_INPUT_INTERFACE=NOT_APPROVED
RAW_TELEMETRY_TO_SAEE=PROHIBITED
SAEE_WRITEBACK=PROHIBITED
SAEE_RECOMMENDATION_TO_AUTOMATIC_EXECUTION=PROHIBITED
```

### 6.6 Governed change and feedback

```text
Evidence / Health / Evaluation / Risk inputs
  -> Human or explicitly delegated Authority
    -> scoped Decision Record + Authorization Reference
      -> separately verified executor
        -> bounded execution
          -> new Execution Result / Observation Material
            -> new evidence and evaluation cycle
```

反馈必须创建新记录或 superseding record。禁止为使决定“看起来正确”而修改旧 Evidence、
旧 Health finding 或旧 Evaluation。

### 6.7 POP reference mapping

```text
POP project-local reference
  -> explicit mapping candidate
    -> DBOS identity/existence mapping review
      -> adopted mapping or rejection, only after Human/Owner decision
```

POP reference 本身不认证身份、不授予 Permission，也不要求 DBOS 接受。

## 7. Prohibited dependency directions（禁止依赖方向）

| ID | 禁止方向 | 禁止原因 |
|---|---|---|
| `FD-01` | DBA / Cockpit `->` child canonical write | reference-only aggregation 不能变成第二事实源 |
| `FD-02` | TITMAS domain `->` DBOS/POP/EEOAP/SAEE canonical object ownership | mapping/profile 不转移 source 或 specification ownership |
| `FD-03` | Agent Evidence validator `->` DBOS canonical write | local validation 不能自我完成 admission |
| `FD-04` | DBOS record mutation `->` 让 Agent Evidence validation 通过 | 禁止为通过验证而修正历史事实；更正必须形成显式后继记录 |
| `FD-05` | Agent Evidence `PASS` `->` Truth/Permission/Certification | validation scope 与语义不足以支持抬升 |
| `FD-06` | Agent Evidence candidate `->` SAEE direct evaluation truth | SAEE 输入必须遵守 DBOS admission 和受保护接口 |
| `FD-07` | Agent Health finding `->` automatic repository/Agent change | diagnosis 与 execution/authorization 分离 |
| `FD-08` | Agent Health score `->` DBOS admission、Permission 或 SAEE Fitness | 静态健康结果不拥有这些语义 |
| `FD-09` | SAEE recommendation `->` DBOS/Agent writeback | evaluation 是 advisory-only，不是 Command |
| `FD-10` | SAEE `->` Permission、Identity、Capability 或 Lifecycle mutation | 评价不能取得 existence/operational authority |
| `FD-11` | POP reference `->` authentication/Permission grant | persona 不等于 canonical identity 或 authorization |
| `FD-12` | TITMAS Situational View `->` command、approval、gate closure | situational awareness 不是 Authority |
| `FD-13` | Cockpit projection `->` canonical project status | dashboard observation 不覆盖 source truth |
| `FD-14` | Cockpit availability `->` child component availability | child projects 不得依赖展示层才能运行或维护事实 |
| `FD-15` | Human Decision `->` unverified automatic execution | 决定需绑定 target、scope、executor、Permission、expiry 和 rollback |
| `FD-16` | Human Decision `->` retroactive Evidence rewrite | Authority 可以决定下一动作，不能改写已发生历史 |
| `FD-17` | Executor `->` expand its own authorization | execution role 不产生新的 Authority |
| `FD-18` | MCP/HTTP/CLI success `->` semantic success | transport success 不等于 validation/admission/correctness |
| `FD-19` | external reference adoption `->` TITMAS profile/runtime adoption | reference、profile、implementation 三轴独立 |
| `FD-20` | any component `->` second Cockpit / global Truth store | 防止隐藏中心和重复治理 |

### 7.1 Prohibited cycles（禁止循环）

1. **Validation self-approval**

   ```text
   Agent Evidence validation fails
     -> mutate DBOS/source record
       -> validation passes
   ```

2. **Health-validation circular scoring**

   ```text
   Health score defines validation eligibility
     -> validation pass defines Health score
   ```

3. **Evaluation-writeback control loop**

   ```text
   SAEE recommendation
     -> automatic state change
       -> SAEE re-evaluates its own change as approval
   ```

4. **Cockpit-source mutation loop**

   ```text
   Cockpit displays risk
     -> Cockpit modifies child state
       -> display reports risk closed
   ```

5. **Decision-evidence rewrite loop**

   ```text
   Human decision
     -> rewrite prior Evidence
       -> rewritten Evidence justifies decision
   ```

6. **Authority-by-connectivity loop**

   ```text
   component gains more integrations
     -> treated as central Authority
       -> requires all components to depend on it
   ```

允许的 feedback 不是 writeback loop，而是：

```text
old immutable-by-convention record
  + new decision
  + new execution
  + new observation
  -> new linked record
```

这里的 immutable-by-convention 指 digest、append-only history、correction 和 supersession
防止静默改写，不是法律不可抵赖或绝对不可篡改。

## 8. Evidence, Health, Evaluation and Authority relationship（四者关系）

### 8.1 Semantic separation

| 概念 | 回答的问题 | 最低绑定 | 不能回答 |
|---|---|---|---|
| Evidence candidate | 有哪些材料支持某项 operation/history claim？ | source、subject、time、scope、provenance、limitations | 是否绝对真实、是否健康、是否授权 |
| DBOS-admitted Evidence/Verification reference | 哪项材料按哪套规则在什么范围内被准入／验证？ | admission rule/version/result/scope | 科学真理、全局正确性、Permission |
| Health finding | 指定 repository snapshot 出现了哪些可解释健康信号？ | scanner/method/version/time/snapshot/applicability | runtime safety、长期 fitness、Authority |
| Evaluation | 在给定方法、窗口和输入下如何评价可靠性／稳定性／风险／演化？ | input refs、method/version/time window/uncertainty | Human Decision、Command |
| Authority Decision | 谁在什么 scope、期限和责任下决定什么？ | decided-by、object/action/scope/time/expiry/revocation | 执行已完成、Evidence 已验证 |

### 8.2 Allowed relationships

```text
Observation Material
  -> Evidence Candidate
    -> optional DBOS Admission
      -> scoped input candidate for Evaluation

Repository Snapshot
  -> Health Finding
    -> Human review
    -> optional new Evidence Candidate, only through a future approved contract

Evidence + Health + Evaluation + Risk
  -> decision inputs
    -> Human Authority
      -> scoped authorization
        -> separate execution
          -> new evidence cycle
```

### 8.3 Non-equivalences

```text
OBSERVATION_NE_EVIDENCE=true
EVIDENCE_NE_TRUTH=true
VALIDATION_NE_ADMISSION=true
ADMISSION_NE_PERMISSION=true
HEALTH_NE_EVIDENCE_TRUTH=true
HEALTH_NE_FITNESS=true
EVALUATION_NE_AUTHORITY=true
RECOMMENDATION_NE_DECISION=true
DECISION_NE_EXECUTION=true
EXECUTION_NE_VERIFIED_SUCCESS=true
COCKPIT_PROJECTION_NE_CANONICAL_STATUS=true
```

Health finding 或 SAEE evaluation 的“发生”可以在未来成为 evidence candidate，但其内容
不会因此升级为 Truth、Permission 或自我批准的正确性。

## 9. TITMAS Situational Awareness Layer（TITMAS 态势感知层）

### 9.1 Canonical placement

```text
Digital Biosphere Program
  -> DBA Program Governance and Architecture Cockpit
       -> TITMAS Situational View
```

`TITMAS Cockpit` 在本图中只是便于沟通的短称。规范名称是：

```text
TITMAS Situational View within the DBA Cockpit
```

它是 logical awareness layer（逻辑态势感知层），不是独立 Component、Runtime、repository、
service 或 Authority。

### 9.2 Display contract constraints

未来若设计展示面，最低架构约束应包括：

- 每项状态可回到 canonical source；
- 显示 source、version、`observed_at`、freshness 和 scope；
- 保留 `UNKNOWN`、`NOT_ASSESSED`、`STALE`、`CONFLICTED` 和 failure；
- Evidence candidate、validation、DBOS admission、Health、Evaluation、Decision 和
  Execution 使用不同状态标签；
- 不将多项结果压成没有方法和申诉路径的全局分数；
- 敏感 Evidence 默认不复制，只显示最小必要引用和访问边界；
- Cockpit 离线或过期不影响 child canonical source；
- recommendation 必须显示为 recommendation，不显示为 command；
- Human Decision 必须带 decision reference，不从 UI click 推断授权已经完成。

### 9.3 Cockpit non-effects

```text
TITMAS_COCKPIT_IS_SITUATIONAL_AWARENESS_LAYER=true
TITMAS_COCKPIT_IS_INDEPENDENT_COCKPIT=false
TITMAS_COCKPIT_IS_TRUTH_SOURCE=false
TITMAS_COCKPIT_HAS_PERMISSION_AUTHORITY=false
TITMAS_COCKPIT_CAN_MODIFY_AGENT=false
TITMAS_COCKPIT_CAN_EXECUTE_COMMAND=false
TITMAS_COCKPIT_CAN_CLOSE_GATE=false
TITMAS_COCKPIT_IMPLEMENTED=false
```

## 10. Failure, time and freshness boundaries（失败、时间与新鲜度）

任何未来 interface contract 必须保留而不是抹平：

```text
UNKNOWN
UNSUPPORTED
INVALID
PARTIAL
CONFLICTED
STALE
UNAVAILABLE
REJECTED
```

本图不定义它们的字段或 wire representation（传输表示），但规定：

1. producer failure 不能由 consumer 静默转换为 success；
2. missing data 不能用默认高状态补齐；
3. source conflict 不能自动选择更有利的版本；
4. static Health finding 必须绑定 snapshot/time；
5. Evidence 必须绑定 operation/time/source；
6. Evaluation 必须绑定 input version 和 time window；
7. Cockpit projection 必须绑定 `observed_at` 和 freshness；
8. Human Decision 必须绑定 decision time、scope、validity 和 revocation；
9. execution result 必须形成新记录，不回写旧输入；
10. stale historical success 不能证明 current health、fitness 或 readiness。

消费者可以 fail closed、拒绝评价、降低 scope 或请求人工复核，但不得获得新的
Authorization。

## 11. Interface candidate register（接口候选台账）

| ID | 候选 handoff | 当前状态 | 主要缺口 |
|---|---|---|---|
| `IB-01` | source project `->` DBA/Cockpit reference | `REFERENCE_ONLY_POLICY_DEFINED` | canonical source、freshness、conflict policy 未全部决定 |
| `IB-02` | POP `->` DBOS identity mapping | `CANDIDATE_NOT_ADOPTED` | Owner、semantics、version、authentication non-claim |
| `IB-03` | Agent Evidence `->` DBOS admission request | `CANDIDATE_NOT_FROZEN` | object crosswalk、version、failure、non-elevation |
| `IB-04` | DBOS record `->` Agent Evidence bounded export | `CANDIDATE_NOT_FROZEN` | source permission、scope、lineage、repackaging semantics |
| `IB-05` | Agent Health `->` Cockpit projection | `REFERENCE_ONLY_CANDIDATE` | finding version、freshness、sensitive data、display semantics |
| `IB-06` | Agent Health finding `->` Evidence candidate | `NOT_ESTABLISHED` | Owner、profile、necessity、no duplicate schema |
| `IB-07` | DBOS admitted refs `->` SAEE input | `NOT_READY` | SAEE Owner approval、read-only contract、no core disclosure |
| `IB-08` | SAEE recommendation `->` Human Authority | `CONCEPTUAL_DIRECTION_ONLY` | method/version、uncertainty、decision packet boundary |
| `IB-09` | Human Authorization `->` executor | `DECISION_SPECIFIC_ONLY` | target、Permission、expiry、rollback、verification |
| `IB-10` | execution result `->` new evidence cycle | `CONCEPTUAL_DIRECTION_ONLY` | source/profile/admission path depends on target domain |
| `IB-11` | component result `->` TITMAS Situational View | `REFERENCE_ONLY_CANDIDATE` | minimal disclosure、freshness、source contract |
| `IB-12` | TITMAS profile `->` source/consumer adapter | `NOT_READY` | Specification Authority、version、failure semantics、implementation authorization |

本台账不创建 interface；它只登记下一次决定和审查的最小单位。

## 12. Required human decisions before interface freeze（冻结前人工决定）

| ID | 需要决定 | 不自动授权 |
|---|---|---|
| `IB-D01` | DBOS、POP、EEOAP、Health、Evaluation 对象 ownership crosswalk | Schema、implementation |
| `IB-D02` | DBOS admission/verification source、version 和 result authority | Truth、Permission |
| `IB-D03` | POP 到 DBOS Identity 的 mapping 或长期分离 | authentication、migration |
| `IB-D04` | Agent Evidence family 的 canonical source、version 和 public/private separation | merge、relicense |
| `IB-D05` | `agent-health` / `titmas-health` disposition 和 Health finding Owner | archive、delete、runtime monitor |
| `IB-D06` | SAEE protected input approval、read-only/no-writeback/no-core boundary | public service、Command |
| `IB-D07` | DBA/TITMAS Situational View 的 source contracts、freshness、privacy 和 conflict policy | UI、adapter、database |
| `IB-D08` | Decision/Authorization 的 scope、delegation、expiry、revocation 和 executor handoff | execution |
| `IB-D09` | 所有适用 handoff 的 failure/non-elevation responsibility | implementation |
| `IB-D10` | security、privacy、retention、secret 和 supply-chain boundaries | production |
| `IB-D11` | TITMAS bounded Architecture/Specification Authority 是否采纳 | independent governance |
| `IB-D12` | 哪个最小 interface subset 可进入下一次 readiness review | full Interface v0.1 |

任何决定必须有 `decided_by_ref`、`decided_at`、scope、source refs 和 non-effects。接口决定、
Schema 设计、实现授权、release 和 production authorization 是不同 gate。

## 13. Auxiliary agent review（辅助智能体审查）

本轮通过用户指定的安全环境变量路径调用：

- `qwen3.7-max`；
- `deepseek-v4-pro`。

没有读取、复制、记录或回显 API Key。输出仅作为 advisory review。

Qwen 正确提示：

- Agent Evidence 不得为通过验证而反向修改 DBOS/source record；
- candidate validation 不得绕过 DBOS admission；
- Human Decision 与执行必须分离并保留执行前边界检查。

未采纳 Qwen 的以下过严或越界表述：

- Cockpit 不能直接只读引用 child source；
- 所有展示必须来自一个“统一 DBOS 数据层”；
- Agent Evidence validation 具有法律效力对立面；
- Human Decision 到 executor 的任何数据方向都应禁止。

DBA policy 允许带来源的 read-only aggregation；当前没有统一 DBOS Cockpit 数据层或
法律效力声明；Human Decision 可以进入有范围 executor handoff，但不能自动执行。

DeepSeek 正确提示：

- Health、Evidence 和 Evaluation 的时间窗口不一致会产生“过去健康证明现在可信”的
  semantic elevation；
- Health 与 validation 不能相互定义资格；
- 决定与执行之间必须保留可验证 feedback。

未采纳 DeepSeek 关于“只读意味着结果无法反馈”的假设。允许的反馈是新
Execution Result、Observation、Evidence 和 Evaluation 周期；禁止的是修改旧记录或
SAEE/Cockpit writeback。

```text
AUXILIARY_MODEL_OUTPUT_IS_ADVISORY=true
AUXILIARY_MODEL_OUTPUT_IS_DECISION=false
AUXILIARY_MODEL_OUTPUT_IS_AUTHORIZATION=false
LOCAL_CANONICAL_EVIDENCE_HAS_PRECEDENCE=true
```

## 14. Validation and non-effects（验证与非效果）

本边界图的文档验证应检查：

- 所有核心组件都有唯一职责、输入、输出和 Authority 边界；
- 允许方向与禁止方向不冲突；
- DBOS admission 与 Agent Evidence validation 分离；
- Agent Health 与 SAEE Evaluation 分离；
- Human Decision 与 executor 分离；
- Cockpit 是 DBA 内的 Situational Awareness Layer；
- failure、unknown、stale、conflict 和 limitation 得到保留；
- 没有字段级 Schema、API、代码或实现授权。

```text
CORE_RESPONSIBILITIES_MAPPED=true
INPUT_OUTPUT_BOUNDARIES_MAPPED=true
AUTHORITY_BOUNDARIES_MAPPED=true
ALLOWED_DATA_DIRECTIONS_MAPPED=true
FORBIDDEN_DEPENDENCIES_MAPPED=true
EVIDENCE_HEALTH_EVALUATION_AUTHORITY_RELATIONSHIP_MAPPED=true
TITMAS_COCKPIT_ROLE=SITUATIONAL_AWARENESS_LAYER_WITHIN_DBA

INTERFACE_SCHEMA_DEFINED=false
API_DEFINED=false
TRANSPORT_SELECTED=false
ADAPTER_DEFINED=false
RUNTIME_CREATED=false
CODE_MODIFIED=false
SCHEMA_MODIFIED=false
PROTOCOL_MODIFIED=false
DEPENDENCY_ADDED=false
NEW_DIRECTORY_CREATED=false
NEW_PROJECT_CREATED=false
AUTHORITY_ASSIGNMENT_CREATED=false
IMPLEMENTATION_AUTHORIZED=false
AUTOMATIC_RESPONSE_AUTHORIZED=false
COMMIT_CREATED=false
PUSH_PERFORMED=false
```
