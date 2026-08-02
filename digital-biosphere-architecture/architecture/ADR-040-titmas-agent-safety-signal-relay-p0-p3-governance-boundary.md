---
adr_id: ADR-040
title: TITMAS Agent Safety Signal Relay P0-P3 Governance and Ownership Boundary
title_zh: TITMAS 智能体安全信号中继 P0-P3 治理与所有权边界
status: ACCEPTED_WITH_AMENDMENTS_P0_P3_ONLY
decision_ref: TITMAS-AGENT-SAFETY-SIGNAL-RELAY-P0-P3-D01
decided_by_ref: zhangbin
decided_at: 2026-08-02
primary_repository: digital-biosphere-architecture
canonical_source_revision: 9f589e3eacb11eceac004a42e43f695892098a5b
implementation_authorized: false
new_repository_authorized: false
public_signal_authorized: false
release_authorized: false
---

# ADR-040：TITMAS 智能体安全信号中继 P0-P3 治理与所有权边界

## 1. Decision status（决定状态）

Human Program Owner 已对
[`titmas-agent-safety-signal-relay-decision-report-v0.1.md`](titmas-agent-safety-signal-relay-decision-report-v0.1.md)
作出修订后批准。本决定只授权 P0–P3 架构、规范和治理工作，不授权实现或建仓。

```text
DECISION=APPROVE_WITH_AMENDMENTS
P0_P3_AUTHORIZED=true
P4_P10_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
NEW_REPOSITORY_AUTHORIZED=false
PUBLIC_SIGNAL_AUTHORIZED=false
REMOTE_CONTROL_AUTHORIZED=false
AUTO_REMEDIATION_AUTHORIZED=false
```

本 ADR 是 DBA 当前架构契约和职责边界的单一事实源。它不覆盖 DBOS、SAEE、
`agent-evidence`、ARO 或其他子项目的实现事实源。

## 2. Architecture classification（架构分类）

本方向分类为：

```text
PRIMARY_CLASS=ARCHITECTURE_GOVERNANCE
FUTURE_CLASS=BOUNDED_AGENT_SAFETY_SIGNAL_INFRASTRUCTURE
CURRENT_RUNTIME_CLASS=NONE
CURRENT_SERVICE_CLASS=NONE
```

其目标是定义安全信号领域对象、信号自身生命周期、接收方本地验证边界和未来互操作面。
它不是 Runtime、Executor、Identity Authority、Evidence Authority、Truth Authority、
Certification Authority 或通用风险评分服务。

## 3. Ownership freeze（所有权冻结）

```text
architecture_owner=DBA
future_domain_implementation_owner=PROPOSED_RELAY_REPOSITORY_NOT_ACTIVE
evidence_authority=EXISTING_EVIDENCE_AND_DBOS_DEPENDENCIES
recipient_trust_authority=LOCAL_RECIPIENT_POLICY
```

| Responsibility | Owner | Exact boundary |
|---|---|---|
| 架构契约、角色、gate、重复建设审查 | DBA | 只定义规范，不运行服务、不创建下游事实 |
| 安全信号对象自身的 revision/correction/expiry/revocation | 未来候选 Relay 仓库，当前未生效 | 不管理 Agent Identity、Execution 或 DBOS Evidence lifecycle |
| 规范证据引用、摘要、验证回执 | `agent-evidence` 与既有证据依赖 | Relay 只保存引用和保证状态，不复制第二套 Evidence system |
| 稳定身份、identity binding、execution context | DBOS 及其身份依赖 | Relay 不从 name/alias/POP 创建或修复身份 |
| Risk/Fitness/Evolution Recommendation | SAEE | 只读消费匹配结果；不得写回、发布信号或授权执行 |
| 异常候选发现 | 未来可选 `tiamas-scout` safety profile | 只读、emit-only；不发布、不匹配、不执行、不聚合反馈 |
| 派生展示与机器入口 | `redcrag.cn` | 不是事实源、发布门、撤回权威或运行时 |
| 接收方是否信任、测试或行动 | 接收方本地策略 | 发布者保证和信号到达均不替代本地决定 |

发布者角色只证明谁在什么 policy 下对哪些字节作出声明。它不是最终信任权：

```text
PUBLISHER_ROLE_NE_FINAL_TRUST_AUTHORITY=true
PUBLISHER_ASSURANCE_NE_GLOBAL_TRUST=true
RECIPIENT_LOCAL_POLICY_RETAINS_TRUST_DECISION=true
```

## 4. Future repository boundary（未来候选仓库边界）

候选名称保持：

```text
PROPOSED_REPOSITORY=titmas-agent-safety-signal-relay
PROPOSED_REPOSITORY_STATUS=NOT_CREATED_NOT_ACTIVE
```

若未来另有授权，该仓库最多拥有：

1. 六类 Agent Safety Signal 领域对象及兼容配置；
2. 安全信号自身的版本、更新、纠正、过期和撤回记录；
3. 确定性三值 applicability 规范与未来参考实现；
4. 定向查询/分发 metadata 和最小接收确认；
5. 最小验证反馈引用及对下一版本的输入；
6. 离线 conformance fixtures。

明确不拥有：

- Agent Identity/Lifecycle/Execution；
- Canonical Evidence/Verification/Truth；
- SAEE 风险接受或演化权；
- 通用发现、人格、消息队列、威胁情报协议、PKI 或密码算法；
- 远程命令、自动修复、自动扩权、客户执行策略；
- 公共网站或任何唯一全局信任中心。

## 5. DQ-006 exact scoped disposition（DQ-006 精确范围处置）

`DQ-006` 的全项目组合问题继续保持 `OPEN`；本 ADR 不拥有把 POP、ARO、Agent Evidence、
Token Governor 或 ACP 全局纳入 Portfolio 的授权。但是，**在 Safety Signal Relay 关系域内**，
以下处置是终局且不得留作模糊映射：

| Candidate | Relay-scope disposition | Portfolio effect |
|---|---|---|
| `agent-evidence` | `EXISTING_ADJACENT_EVIDENCE_REFERENCE_AND_RECEIPT_DEPENDENCY` | 不由本决定重复准入、合并或改权 |
| ARO / ARO-Audit | `OPTIONAL_POST_EXECUTION_AUDIT_REFERENCE_NOT_OWNER` | 不成为 Relay、Publisher、Evidence 或 trust owner |
| POP | `EXCLUDED_FROM_MACHINE_IDENTITY_AND_TRUST_BINDING` | 可选 persona/context 引用；无身份、权限或适用性权威 |
| Token Governor | `OUT_OF_SCOPE_FOR_P0_P3` | 不参与发布、匹配、信任或信号生命周期 |
| ACP | `OUT_OF_SCOPE_FOR_P0_P3` | 不建立 `cell_id` 与 Agent/Signal identity 映射 |

```text
DQ_006_GLOBAL_STATUS=OPEN
DQ_006_RELAY_SCOPE_DISPOSITION=DECIDED_BY_ADR_040
DQ_006_RELAY_SCOPE_CREATES_PORTFOLIO_ADMISSION=false
```

## 6. R-007 exact scoped disposition（R-007 精确范围处置）

R-007 的全局重复建设风险仍存在；在 Relay 关系域内采用以下明确缓解：

1. Relay 只保存 Evidence references/receipts，不创建第二套 Evidence store；
2. ARO 只提供可选 post-execution audit reference，不拥有信号判断或生命周期；
3. DBOS 保留 identity、execution context、canonical Evidence 和 verification authority；
4. SAEE 只读消费，不写回 Relay；
5. POP、Token Governor、ACP 不进入 P0–P3 数据路径；
6. 任一未来接口必须先通过 duplicate capability review 和独立 G3 mapping 决定。

```text
R_007_GLOBAL_STATUS=REVIEW_REQUIRED
R_007_RELAY_SCOPE_STATUS=SCOPED_MITIGATION_DEFINED
R_007_RELAY_SCOPE_DUPLICATE_EVIDENCE_SYSTEM_ALLOWED=false
R_007_RELAY_SCOPE_IMPLEMENTATION_CREATED=false
```

## 7. Gate effects（闸门效力）

| Gate | Relay workstream result | Meaning |
|---|---|---|
| `G0` | `PASS_FOR_DBA_SPECIFICATION_WORKSTREAM_ONLY` | 只接纳 P0–P3 架构工作；未来仓库未准入 |
| `G1` | `PASS_DBA_CANONICAL_SOURCE` | 本轮基于已确认 remote revision；不证明未来实现源 |
| `G2` | `PASS_ARCHITECTURE_BOUNDARY_P0_P3` | Owner、非 Owner、信任和非执行边界已冻结 |
| `G3` | `NOT_AUTHORIZED` | 不建立 interface mapping implementation |
| `G4` | `NOT_AUTHORIZED` | 不运行 conformance implementation |
| `G5` | `NOT_AUTHORIZED_FOR_IMPLEMENTATION` | P4–P10 需新人工授权 |
| `G6` | `NOT_EXECUTED` | 无运行时、服务、信号或接收方执行 |
| `G7` | `NOT_ASSESSED` | 无公共客户采用或生产评价 |
| `G8` | `NOT_RELEASED_NOT_ADOPTED` | 无发布、部署、标准或生产推荐 |

## 8. Required invariants（强制不等同关系）

```text
SIGNAL_RECEIVED_NE_ACTION_AUTHORIZED=true
APPLICABILITY_NE_CONFIRMED_IMPACT=true
PUBLISHER_ASSURANCE_NE_GLOBAL_TRUST=true
EVIDENCE_REFERENCE_NE_TRUTH=true
CORRECTION_NE_HISTORY_DELETION=true
SPECIFICATION_NE_IMPLEMENTATION=true
P0_P3_COMPLETION_NE_P4_P10_AUTHORIZATION=true
```

## 9. Accepted and rejected scope（接受与拒绝范围）

接受：P0 ADR、P1 gap matrix、P2 object model、P3 publication/privacy/revocation policy、
审计报告修订说明、验收矩阵和未决问题清单。

拒绝/未授权：新仓库、runtime code、matcher、API server、CLI、服务启动、公共信号、网站修改、
push、merge、deployment、remote control、auto remediation 和 production recommendation。

## 10. Decision effect（决定效力）

```text
ARCHITECTURE_DECISION_RECORDED=true
FUTURE_DOMAIN_IMPLEMENTATION_OWNER_ACTIVE=false
IMPLEMENTATION_CODE_AUTHORIZED=false
NEW_REPOSITORY_CREATION_AUTHORIZED=false
PUBLIC_SIGNAL_PUBLICATION_AUTHORIZED=false
RECIPIENT_LOCAL_TRUST_PRESERVED=true
CHILD_REPOSITORY_FACTS_CHANGED=false
```
