---
document_id: DBA-PROGRAM-SOURCE-AND-RESPONSIBILITY-DECISION-PACKET-0.1
title: Program Source and Responsibility Decision Packet v0.1
title_zh: 项目群规范来源与责任决策包 v0.1
status: ACCEPTED_BY_ADR_021
observed_at: 2026-07-21T23:57:45+08:00
accepted_at: 2026-07-22T00:24:02+08:00
decision_ref: ADR-021
decided_by_ref: zhangbin
primary_repository: digital-biosphere-architecture
addresses:
  - DQ-003
  - DQ-006
  - DQ-007
  - DQ-008
  - R-003
  - R-007
  - R-008
  - R-010
governance_record_effect: DBA_GOVERNANCE_ALIGNMENT_ONLY
child_project_truth_changed: false
---

# Program Source and Responsibility Decision Packet v0.1（项目群规范来源与责任决策包 v0.1）

## 1. Outcome（结论）

本决策包把当前最优先的治理修正收敛为两件事：

1. 为每个项目记录可核验的 source candidate（来源候选）、观察时间、branch、commit、
   freshness（新鲜度）和冲突处理规则；
2. 把 Runtime Record、Evidence Package、Audit Projection、Canonical Verification、
   Evaluation、Decision、Execution 和 Release 的责任链明确分开。

Human Program Owner 已通过 [`ADR-021`](architecture/ADR-021-program-source-and-public-entry-authority.md)
接受本决策包中关于 `DQ-003`、`DQ-007`、`DQ-008` 的治理建议；`DQ-006` 仍保持 `OPEN`。
该接受决定只确认 DBA 内的 source routing（来源路由）、人工刷新规则、项目群治理来源与
单一公共信息入口，不修改任何子项目的 canonical source（规范来源），也没有创建
Runtime、Adapter（适配器）、Capability、Evidence、Permission 或 Release
Authorization（发布授权）。机器可读镜像见
[`architecture/program-source-and-responsibility-registry.json`](architecture/program-source-and-responsibility-registry.json)。

```text
SOURCE_CANDIDATES_RECORDED=true
DOMAIN_OWNER_CONFIRMATION_COMPLETE=true
CANONICAL_STATUS_SOURCES_CONFIRMED=true
DBA_CANONICAL_RELATIONSHIP_DECIDED=true
DBA_CROSS_REPOSITORY_REFERENCE_IMPLEMENTED=false
ADJACENT_PROJECT_PORTFOLIO_ADMISSION_COMPLETE=false
RESPONSIBILITY_CHAIN_CLARIFIED=true
CHILD_PROJECT_IMPLEMENTATION_CHANGED=false
GOVERNANCE_IMPLEMENTATION_AUTHORIZED=true
RUNTIME_IMPLEMENTATION_AUTHORIZED=false
```

## 2. Pre-development Agent Recommendation Gate（开发前智能体推荐闸门）

面向潜在用户的当前问题是：

> 如果用户需要把有来源的运行记录转成可移交证据，并在明确 claim（声明）与 scope
> （范围）下获得有界评价，智能体是否会推荐当前项目群？

接受 `ADR-021` 后的当前回答：

```text
INITIAL_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
CURRENT_RECOMMENDATION=RECOMMENDED_FOR_PROGRAM_GOVERNANCE_AND_SOURCE_ROUTING
RECOMMENDED_SCOPE=PROGRAM_GOVERNANCE_SOURCE_ROUTING_AND_BOUNDED_LOCAL_EVALUATION
NOT_RECOMMENDED_SCOPE=END_TO_END_PRODUCTION_TRUST_AND_AUTHORIZED_EXECUTION
RECOMMENDATION_IS_IMPLEMENTATION_AUTHORIZATION=false
```

### 2.1 可以推荐的范围

- DBA：项目群边界、责任路由、Decision / Risk / Gate 和跨项目契约；
- DBOS：Identity、Lifecycle、Execution Record、Canonical Evidence Reference 和
  Verification 的架构责任；
- Agent Evidence：可移植 evidence object / export / offline bundle（证据对象／导出／
  离线包）的独立参考实现边界；
- ARO：tamper-evident audit projection（防篡改审计投影）和有界验证表面；
- SAEE：本地封闭证据包的 adequacy evaluation（充分性评价）与 Recommendation。

### 2.2 暂不推荐的范围和原因

| 不推荐范围 | 原因 | 可修正问题 | 停止条件 |
|---|---|---|---|
| 完整生产信任链 | DBA 已确认治理引用路由，但仍没有完整外部身份／委托绑定或独立外部验证 | 完成 identity/delegation contract 和独立验证 | 任何验证仍仅为本地自检或来源已过期／冲突 |
| Dapr / OTLP 到 SAEE 的生产接入 | 当前只有外部 signal（信号）和 synthetic mapping（合成映射），没有经 gate 授权的 Adapter | 先冻结版本化 mapping profile，再由各项目建立独立实施事项 | 上游版本、字段映射、failure semantics 或 Owner 未冻结 |
| 自动 Decision、Execution 或 Release | Recommendation、Decision、Execution 与 Release 必须分层 | 保留 Human Decision / Authorization 和 `released_by_ref` | 任何链路尝试由评价结果自动产生执行或发布 |
| 统一“证据平台”合并 | DBOS、Agent Evidence、ARO 与 SAEE 的能力相邻但权力不同 | 使用责任矩阵与 schema crosswalk，不合并事实权威 | 出现第二个 canonical owner 或重复 receipt/hash/Merkle stack |

## 3. Read-only Observation Snapshot（只读观察快照）

以下只说明 `2026-07-21T23:57:45+08:00` 可观察到的 Git 状态。`worktree_changes`
不表示成熟度、质量、发布状态或子项目真相；值大于零时只表示不可把 HEAD 当作完整当前
工作树内容。

| project_id | repository | branch | commit | worktree_changes | 解释 |
|---|---|---|---|---:|---|
| `PROJECT-DBA-COCKPIT` | `/Users/zhangbin/Documents/New project/digital-biosphere-architecture` | `main` | `91928e3b1096566aad5568124707e3a6cb3a40ca` | 2 | 本次修正前已有 README 与外部情报 intake 未提交 |
| `PROJECT-DBOS` | `/Users/zhangbin/GitHub/digital-biosphere-os` | `main` | `0caa2c45e511a82d0dcab778b0ffc3163aac0029` | 0 | clean observation（干净观察），不是 Release 证明 |
| `PROJECT-SAEE` | `/Users/zhangbin/GitHub/SAEE` | `feat/canonical-capability-inventory-routing-v1` | `0c416f70c56caabe1e24d183a0cfb5af3b0ce8d8` | 667 | 高度混杂，禁止从 HEAD 或单一状态文件概括整个当前工作树 |
| `RESEARCH-AGENT-PILOT` | `/Users/zhangbin/GitHub/digital-biosphere-research-agent-pilot` | `main` | `8445fe5d13cd889032c3786ba527d801f56d5351` | 30 | 当前仍由项目自身声明 `NOT_READY` |
| `PROJECT-AGENT-EVIDENCE` | `/Users/zhangbin/GitHub/agent-evidence` | `revision/softwarex-v2-grounding-fix` | `1b692de391aa04bcfe2666ccc3ddce652ce5c3df` | 87 | 独立参考项目，不能由 DBA 推断当前发布状态 |
| `PROJECT-ARO` | `/Users/zhangbin/GitHub/aro-audit` | `audit-scope-alignment-v1` | `74a7f584b8cb18ca2655a0dac30e77e41e582c43` | 19 | 独立参考项目，当前 freshness/replay policy 仍有缺口 |

## 4. `DQ-003` Accepted Source Decision（已接受来源决定）

### 4.1 推荐规则

每个项目的状态来源必须满足：

```text
one_project_status_entry=true
source_scope_explicit=true
observed_at_required=true
branch_and_commit_or_version_required=true
freshness_rule_required=true
conflict_policy=PRESERVE_CONFLICT_AND_REQUEST_DOMAIN_OWNER
dirty_count_is_maturity=false
README_is_not_automatically_canonical=true
```

### 4.2 已确认的 DBA 引用路由

| project_id | program-level source | scoped source / boundary | 决策状态 |
|---|---|---|---|
| `PROJECT-DBA-COCKPIT` | Mandatory Cockpit 文件组 | 本决策包与机器可读 registry | `ADR-021` 确认为 canonical Program Governance / Architecture Specification source；跨仓库 public meaning layer 交叉引用仍待实施 |
| `PROJECT-DBOS` | `README.md` | 对象事实继续由对应 `registry/*` 约束 | `HUMAN_CONFIRMED`；冲突保留并请求 DBOS Domain Owner |
| `PROJECT-SAEE` | `PROJECT_STATUS.md` | `capability-package/manifest.json#canonical_inventory` 是 sole canonical capability fact source | `HUMAN_CONFIRMED_SPLIT_SCOPE`；旧 registry、活动日志、报告或 README 不覆盖 capability inventory |
| `RESEARCH-AGENT-PILOT` | `README.md#Current Status` | `CONSTITUTION.md` 负责 truth boundary；`AGENTS.md` 负责 Agent 路由 | `HUMAN_CONFIRMED`；`NOT_READY`、`DRAFT`、`UNKNOWN` 和零实例状态不得升级 |
| `PROJECT-AGENT-EVIDENCE` | `docs/project-facts.md` | 只记录该 repository declaration（仓库声明） | 仍待 `DQ-006` Portfolio Admission |
| `PROJECT-ARO` | `README.md`、`docs/evidence-boundary.md`、`docs/threat-model.md` | 能力与限制可核验，尚无单一总体 canonical status source | 保持 `UNCONFIRMED`；仍待 `DQ-006` 与 Domain Owner 确认 |

### 4.3 已接受的人工作业

`ADR-021` 已确认以下条件作为 DBA 的治理引用规则，并关闭 `DQ-003` 与 `DQ-007`：

1. Human Program Owner 确认 DBOS、SAEE、Research Agent Pilot 的分域来源路由；
2. 所有快照在 consequential gate（后果性闸门）前人工刷新，超过 24 小时视为 `STALE`；
3. 至少执行一次 source → DBA 的只读人工同步并保留 `UNKNOWN/CONFLICTED/STALE`；
4. DBA 不写回子项目；
5. 更新后的状态不把 dirty count、测试数量或本地 PASS 当作成熟度。

## 5. Evidence and Decision Responsibility Chain（证据与决策责任链）

| stage | canonical architecture owner | supporting / reference role | 不能产生 |
|---|---|---|---|
| Version-pinned Runtime Record（版本固定运行记录） | DBOS 负责规范登记与引用 | 来源 Runtime 只负责发出有 provenance（来源）的记录；Dapr / Microsoft 等只能作为外部来源候选 | Truth、Evidence Sufficiency、Authorization |
| Evidence Material / Reference（证据材料／引用） | DBOS | 外部签名、attestation、telemetry 只作为有来源输入 | Canonical Verification、Evaluation、Permission |
| Portable Evidence Package（可移植证据包） | DBOS 保留规范证据责任 | Agent Evidence 提供独立 reference implementation（参考实现） | 事件真实性、充分性、法律不可否认性 |
| Audit Projection / Integrity Check（审计投影／完整性检查） | DBOS 保留规范 Verification 责任 | ARO 提供 tamper-evident journal、receipt 与 bounded verifier（有界验证器）参考 | 全局 freshness、语义真相、身份授权 |
| Canonical Verification（规范验证） | DBOS | 可以消费外部 verifier result，但必须保留来源与独立性 | Fitness、Recommendation、Decision |
| Evidence Adequacy / Evaluation（证据充分性／评价） | SAEE | 消费有界 Evidence 与 Verification，不重写来源 | Truth、Permission、Execution |
| Governance Decision（治理决定） | 独立 Human Decision / Authorization boundary | DBA 定义流程；SAEE 提供 Recommendation；DBOS 提供事实 | 自动执行或自动发布 |
| Authorized Execution（获授权执行） | DBOS + 具体 Digital Entity，在显式授权下 | DBA/SAEE 不执行 | Release、Adoption、Certification |
| Release（发布） | Human Release Authority | 需要 source commits、验证、限制、试用结果和 `released_by_ref` | Production Readiness、Customer Adoption 的自动推导 |

因此，当前禁止新增第四套 receipt、hash chain 或 Merkle implementation（回执、哈希链或
默克尔实现）。真正需要优先补齐的是 source authority（来源权威）、identity/delegation
binding（身份／委托绑定）、freshness/replay/key lifecycle（新鲜度／重放／密钥生命周期）
和独立验证。

## 6. OpenTelemetry and External Runtime Correction（OpenTelemetry 与外部运行时修正）

SAEE 已存在一个 experimental synthetic OpenTelemetry-style mapping（实验性合成
OpenTelemetry 风格映射）。不得再次把“新增 OpenTelemetry 映射”写成从零开始的缺口。
当前真实缺口是：

- OTLP / SDK / Collector ingestion（接入）；
- span hierarchy、links、resource/scope、sampling 和 clock semantics；
- authenticated trace → trusted evidence conversion（认证轨迹到可信证据转换）；
- external identity binding 与 delegation binding；
- 在明确 trust root、key rotation、revocation 和 freshness policy 下的独立验证。

允许的未来顺序仍是：

```text
version-pinned raw telemetry
  -> explicit mapping profile
  -> provenance-bound Evidence Material / Reference
  -> DBOS Verification
  -> SAEE scoped Evaluation
  -> Human Decision / Authorization
```

该顺序不授权创建 Dapr Adapter、OTLP receiver、Microsoft receipt format 或 SAEE Runtime。

## 7. `DQ-006` and `DQ-008` Recommendations（项目准入与 DBA 前门建议）

### `DQ-006`

ARO 与 Agent Evidence 继续保持 `ADJACENT_CANDIDATE` / `REFERENCE`。本次责任澄清不等于
Portfolio Admission（项目组合准入）。准入前必须分别确认 purpose、Owner、canonical
source、license、重复能力和接口边界。

### `DQ-008`

`ADR-021` 已接受以下关系：

```text
CURRENT_COCKPIT_ROLE=CANONICAL_PROGRAM_GOVERNANCE_AND_ARCHITECTURE_SPECIFICATION
EXISTING_PUBLIC_MEANING_LAYER_ROLE=PUBLIC_MEANING_HISTORY_AND_DISCOVERY_REFERENCE
SILENT_OVERWRITE_ALLOWED=false
SILENT_DELETE_ALLOWED=false
AUTOMATIC_MERGE_ALLOWED=false
SINGLE_PUBLIC_FRONT_DOOR_REQUIRED=true
SINGLE_PUBLIC_INFORMATION_ENTRY=PUBLIC-PROJECT-OVERVIEW.md
WEBSITE_PROJECTION_CANDIDATE=redcrag.cn
WEBSITE_RELEASE_AUTHORIZED=false
```

Human Program Owner 决定：

1. 当前 cockpit 成为项目群治理 canonical source；
2. 既有公开 DBA 保留 public meaning / history（公开语义／历史）角色；
3. 双方通过明确交叉引用连接，不复制会漂移的状态事实；
4. 后续再独立决定 Git root、迁移或归档；本决定未执行这些动作，也未授权网站发布。

跨仓库交叉引用尚未实施，因此 `B-005` 继续保持未清除；这不改变 DBA 项目群治理来源已经
由 `ADR-021` 决定的事实。

## 8. Completed Corrections and Remaining Gates（已完成修正与剩余闸门）

### 已完成

- 将外部信号保持为 reference-only（仅参考），不自动生成 Roadmap 或 Capability；
- 明确已有本地 SAEE evaluator 和 synthetic mapping，不重复立项；
- 明确 Agent Evidence、ARO、DBOS、SAEE 的不同责任；
- 创建带 branch、commit、时间与冲突规则的机器可读候选 registry；
- 由 Human Program Owner 接受 `DQ-003`、`DQ-007` 与 `DQ-008` 的治理决定；
- 固定 consequential gate 前人工刷新和 24 小时 stale threshold；
- 将“独特性”从“别人没有防篡改日志”修正为 stage separation（阶段分离）与 scoped
  sufficiency evaluation（有界充分性评价）。

### 仍未完成

- ARO / Agent Evidence 尚未完成 `DQ-006` Portfolio Admission；
- DBA 与既有 public meaning layer（公开语义层）的跨仓库交叉引用尚未实施；
- SAEE 的外部独立验证尚未完成；
- Dapr / OTLP / identity / delegation contract 尚未获实现授权。

```text
CORRECTION_PACKET_COMPLETE=true
MACHINE_READABLE_REGISTRY_COMPLETE=true
HUMAN_OWNER_CONFIRMATION_RECORDED=true
DQ003_DECIDED=true
DQ007_DECIDED=true
DQ008_DECIDED=true
SCHEMA_VALIDATION_PASSED=true
LOCAL_GOVERNANCE_ARTIFACT_VALIDATION=PASS_EXTERNAL_DRIFT_RECORDED
ADJACENT_REPOSITORY_STATE_STABLE=false
DOMAIN_CONFIRMATION_REQUIRED=false
HUMAN_DECISION_REQUIRED_FOR_DQ006=true
CHILD_REPOSITORY_CHANGE_REQUIRED_NOW=false
RUNTIME_CHANGE_REQUIRED_NOW=false
RELEASE_AUTHORIZED=false
FINAL_RECOMMENDATION=RECOMMENDED_FOR_PROGRAM_GOVERNANCE_AND_SOURCE_ROUTING
```

接受决定前的本地验证证据见
[`PROGRAM-SOURCE-AND-RESPONSIBILITY-VALIDATION-REPORT.md`](PROGRAM-SOURCE-AND-RESPONSIBILITY-VALIDATION-REPORT.md)；
接受决定后的验证见
[`PROGRAM-SOURCE-AUTHORITY-DECISION-VALIDATION-REPORT.md`](PROGRAM-SOURCE-AUTHORITY-DECISION-VALIDATION-REPORT.md)。
