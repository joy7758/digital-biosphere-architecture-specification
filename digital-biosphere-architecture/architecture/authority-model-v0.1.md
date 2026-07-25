---
document_id: DBA-ARCHITECTURE-AUTHORITY-MODEL-REVIEW-0.1
title: Architecture Authority Model v0.1 Review
title_zh: 架构权威模型 v0.1 审查
status: REVIEW_COMPLETE_PASS_WITH_REQUIRED_AUTHORITY_FREEZES
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
document_type: ARCHITECTURE_AUTHORITY_DECISION_MODEL_REVIEW
primary_repository: digital-biosphere-architecture
reviewed_at: 2026-07-23
authority_assignment_effect: NONE
project_ownership_effect: NONE
implementation_effect: NONE
manifest_effect: NONE
release_effect: NONE
---

# Architecture Authority Model v0.1 Review

中文：架构权威模型 v0.1 审查。

## 0. Review Verdict（审查结论）

本审查把 [现有四域 Authority 模型](architecture-authority-model.md) 扩展为六个可独立判断的
Authority axis（权威轴）：Architecture、Source、Status、Release、Operational 与 Evolution。
扩展的目的不是创造更多权力，而是阻止“拥有一个仓库／规范／validator／Runtime”被外推为
拥有其他类型的权力。

```text
REVIEW_RESULT=PASS_WITH_REQUIRED_AUTHORITY_FREEZES
SIX_AUTHORITY_TYPES_DEFINED=true
PROJECT_AUTHORITY_MATRIX_DEFINED=true
ACTIVE_SECOND_FACT_AUTHORITY_CONFIRMED=false
SECOND_FACT_AUTHORITY_CANDIDATE_RISKS=4
IMPLICIT_CROSS_PROJECT_WRITE_AUTHORITY_AUTHORIZED=false
STANDARD_AUTHORITY_CONFLICT_RESOLVED=false
COMMERCIAL_PUBLIC_SPECIFICATION_BOUNDARY_RESOLVED=false
TITMAS_ARCHITECTURE_AUTHORITY_ASSIGNED=false
DBOS_STATUS_AUTHORITY_FROZEN=false
EEOAP_VERSION_AUTHORITY_FROZEN=false
AGENT_EVIDENCE_FAMILY_AUTHORITY_FROZEN=false
IMPLEMENTATION_RECOMMENDED_NOW=false
```

当前没有发现某个支持组件已经合法取得第二事实权威或跨项目写权。但以下问题仍会在未来
接口、商业实现或发布动作中形成第二权威，因此必须保持失败关闭：

1. DBA cockpit 与既有 public meaning layer 的规范关系仍由 `DQ-008` 管理；
2. DBOS 的项目级 Status Authority 仍有 `DQ-003` / project status manifest 缺口；
3. EEOAP 与 Agent Evidence 的 specification、reference implementation、commercial Runtime
   和 release surface 尚未完成同一权属模型；
4. ARO 的公共参考面与 control-plane 自述存在角色冲突。

本文件只建立 decision model（决策模型）和审查结论，不指派 Authority，不修改现有
Authority，不决定项目归属，也不授权实现、发布或运行。

## 1. Scope and Precedence（范围与优先级）

### 1.1 审查对象

本次覆盖：

- DBA；
- TITMAS；
- DBOS；
- EEOAP；
- Agent Evidence；
- ARO / ARO-Audit；
- PRA-Server；
- SAEE。

### 1.2 规范输入

本模型受以下既有边界约束：

- [Program Charter](../PROGRAM-CHARTER.md)：DBA 是 Program Governance 与 Architecture
  Specification Hub，但不是 Runtime；
- [现有 Architecture Authority Model](architecture-authority-model.md)：Program、Architecture、
  Operational 与 Evolution Authority 不可互相替代；
- [TMAP Specification](trusted-multi-agent-protocol-specification.md)：DBOS 拥有 Identity、
  Capability、Execution、Evidence 与 Verification 对象边界，SAEE 拥有 Evolution Interface；
- [Interface Boundary Rules](interface-boundary-rules.md)：一个对象类型只有一个 canonical
  Owner，adapter/supporting component 不得成为第二 Owner；
- [TITMAS Integrity Review](titmas-integrity-review-v0.1.md)：TITMAS 只拥有 mapping、reference、
  handoff、adapter 与 interoperability profile 候选范围；
- [DBOS Canonical Source Resolution](dbos-canonical-source-resolution-v0.1.md) 与
  [DBOS Project Status Manifest Schema Review](dbos-project-status-manifest-schema-v0.1.md)：
  source coordinate、project status 与 release artifact 必须分离；
- [SAEE–DBOS Contract](saee-dbos-contract.md)：运行记录、验证、评价、建议、授权和执行状态是
  不同 truth surface（事实表面）。

### 1.3 与 Program Authority 的关系

本次用户指定的六类 Authority 不取代既有 Program Authority（项目群权力）和 Human Decision
Authority（人工决策权）。Program Authority 继续负责组合、优先级、Decision Queue、Gate 与
Risk；Human Decision Authority 继续为重大采纳、发布和授权提供明确 `decided_by_ref`。

```text
PROGRAM_AUTHORITY_NE_ARCHITECTURE_AUTHORITY=true
HUMAN_DECISION_NE_STATUS_AUTHORITY=true
HUMAN_DECISION_NE_OPERATIONAL_EXECUTION=true
ARCHITECTURE_REVIEW_NE_AUTHORITY_ASSIGNMENT=true
```

## 2. Authority Model Principles（权威模型原则）

### `AM-001` Authority 必须有作用范围

Authority 不是一个可以在项目之间传递的全局头衔。每项 Authority 至少要绑定：

- `authority_type`；
- `subject`；
- `scope`；
- `owned_object_or_decision_type`；
- `canonical_source_ref`；
- `owner_or_issuer_ref`；
- `decision_ref`；
- `valid_from` / `review_due_at`；
- `write_effect`；
- `delegation_rule`；
- `conflict_policy`；
- `negative_authorities`。

缺少 scope、Owner 或 Decision ref 时，状态只能是 `PROPOSED`、`UNASSIGNED`、`UNKNOWN` 或
`CONFLICTED`，不能写成 `ACTIVE`。

### `AM-002` Authority 不沿依赖图继承

```text
DBA rule
  -> TITMAS mapping
  -> EEOAP / Agent Evidence material
  -> ARO / PRA result
  -> DBOS admission
  -> SAEE evaluation
```

上述箭头只表示 information handoff（信息交接）。任何上游或下游都不能因为接收、转换、
验证或评价了一个对象而继承该对象 Owner 的 Authority。

### `AM-003` Source、Status 与 Release 必须分离

```text
SOURCE_BYTES_NE_PROJECT_STATUS=true
PROJECT_STATUS_NE_RELEASE_DECISION=true
TAG_NE_RELEASE_AUTHORITY=true
PACKAGE_ARTIFACT_NE_SOURCE_AUTHORITY=true
RELEASE_NE_OPERATIONAL_DEPLOYMENT=true
```

Repository、branch、commit 或 package 只能回答有限的 source/release 问题；它们不能自动说明
项目成熟度、当前状态、Owner、生产可用性或运行状态。

### `AM-004` 写权必须显式授予

Read、map、validate、evaluate、recommend、aggregate 或 display 都不产生 write authority。
跨项目 write 必须有对象类型、目标、scope、issuer、有效期、撤销和失败行为。

### `AM-005` 每种对象、范围和版本只能有一个 canonical Owner

副本、缓存、索引、adapter、commercial implementation、dashboard 或 review result 不得升级为
同一对象的第二 canonical Owner。冲突时保留双方来源并进入 `CONFLICTED`，不得选取状态更高或
更新时间更晚的一方作为自动胜者。

## 3. Six Authority Types（六类 Authority 定义）

### 3.1 Architecture Authority（架构权威）

回答：谁可以维护已经采纳的跨项目规则、对象 Owner、边界、不变量、版本与 ADR？

在 Digital Biosphere 范围内，DBA 是 Architecture Governance/Specification 的规范承载面；
重大变化仍需 Human Decision。TITMAS 若未来被采纳，只能获得 DBA 明确委托的
interoperability mapping/profile 维护范围，不能成为平行 Architecture Authority。

Architecture Authority 不包含：

- 子项目代码写权；
- 子项目 Status 或 Release Authority；
- Runtime、Permission 或 Operational Authority；
- SAEE 算法、模型或 Evolution Authority；
- 对 EEOAP、OpenTelemetry、MCP 等外部规范的标准组织权力。

### 3.2 Source Authority（来源权威）

回答：哪个精确 repository/specification、branch/ref、commit/version 和 artifact digest 是某个
命名源码或规范工件的 canonical source？

Source Authority 属于产生该 source 的项目或规范 Owner。DBA 只能引用子项目 source，不能
复制后成为第二 source。Source Authority 只证明来源坐标，不证明内容真实、状态成熟、已经
发布、已获采用或可投入生产。

最低要求：

```text
repository_or_spec=
canonical_ref=
exact_commit_or_version=
owner_ref=
observed_at=
freshness_policy=
conflict_policy=
```

### 3.3 Status Authority（状态权威）

回答：哪个项目本地入口可以声明该项目的 lifecycle、implementation、release、readiness、
unknown、stale 和 conflicted 状态？

Status Authority 必须位于项目自己的 canonical source 内，并具有刷新与冲突规则。DBA 的
`PROGRAM-STATUS.md` 只是 point-in-time program projection（时间点项目群投影），不能覆盖
child project status。README、测试数量、dirty worktree、Roadmap 或 release badge 不能自动
成为 Status Authority。

### 3.4 Release Authority（发布权威）

回答：谁可以对一个 exact version/artifact、channel、audience 和 license scope 作出发布决定？

Release Authority 必须是 explicit human/organizational authority（明确人工／组织权威），并
绑定 exact scope。Git push 权限、tag 创建者、repository Owner、CI PASS、package version、
Architecture Authority 或 Program priority 都不自动构成 Release Authority。

历史上对一个精确版本的 `released_by_ref` 不能外推为 standing release authority（常设发布权）。

### 3.5 Operational Authority（运行权威）

回答：谁可以在有效 Authorization、Capability、Permission、Context 与 Lifecycle gate 下运行
系统、改变有界运行状态或写入 canonical operational records？

DBOS 保持 Digital Biosphere canonical existence/record domain 内的 Operational Authority，
但 DBOS 不是最终授权者，也不能自动扩大 Permission。PRA-Server 可以在自身个人科研节点中
拥有 project-local runtime control；该局部控制不等于 DBOS Operational Authority。

执行一个 validator、生成一个 receipt、运行一个评价函数或维护一个 commercial workspace
不自动取得被审查系统的 Operational Authority。

### 3.6 Evolution Authority（演化权威）

回答：谁可以基于有来源、只读和有界输入形成 Fitness、Reliability、Stability、Risk、
Adaptation 与 Evolution Recommendation？

SAEE 保持唯一受保护 Evolution Authority。该 Authority 是 derived evaluation authority
（派生评价权威），不是 Command、Permission、Operational Authority、Release Authority 或
Human Decision。SAEE 核心算法、模型、权重和演化智能不因接口存在而进入公共基础设施。

## 4. Authority State Vocabulary（Authority 状态词表）

| 状态 | 含义 |
|---|---|
| `PRIMARY` | 在命名对象、范围和版本内已被接受的主要 Authority |
| `PROJECT_LOCAL` | 只覆盖本项目 source/status/runtime，不跨项目扩张 |
| `EXACT_SCOPE_ONLY` | 只对一个明确 Decision、release 或 artifact 有效，不是常设授权 |
| `PROPOSED_NOT_ADOPTED` | 已有提案，尚未形成 Authority Assignment |
| `CANDIDATE_REVIEW_REQUIRED` | 有来源证据，但 Owner、scope、version 或冲突规则未冻结 |
| `SPLIT_SURFACES` | 一个名称下存在多个独立 source/status/release/runtime Owner，禁止合并 |
| `CONFLICTED` | 两个或更多表面给出不兼容 Authority/role 声明 |
| `UNASSIGNED` | 需要 Authority，但尚未记录 Owner/issuer |
| `NOT_APPLICABLE` | 该对象不应拥有此类 Authority |

`PRIMARY` 只能在 scope 完整且 Decision 可追溯时使用；它不表示其他 Authority 轴也为
`PRIMARY`。

## 5. Project-to-Authority Mapping Matrix（项目到 Authority 映射矩阵）

| 项目／规范面 | Architecture Authority | Source Authority | Status Authority | Release Authority | Operational Authority | Evolution Authority |
|---|---|---|---|---|---|---|
| **DBA** | `PRIMARY_PROGRAM_ARCHITECTURE`；重大变化需 Human Decision | `PROJECT_LOCAL`，但 `DQ-008` 双 DBA 入口仍需对齐 | `PROGRAM_PROJECTION_ONLY`；不拥有 child status | `EXACT_SCOPE_ONLY`；只覆盖有明确 Decision 的 DBA/TMAI release，不覆盖子项目 | `NOT_APPLICABLE` | `NOT_APPLICABLE` |
| **TITMAS** | `PROPOSED_DELEGATED_INTEROP_SCOPE`；尚未采纳 | 当前只有 DBA 内 proposed documents；无独立 implementation source | proposal 状态由 DBA 文档表达；不是独立 project status authority | `UNASSIGNED_NOT_AUTHORIZED` | `NOT_APPLICABLE` | `NOT_APPLICABLE` |
| **DBOS** | `DOMAIN_CONSTRAINT_CONTRIBUTOR`；不能单方面改变 DBA 跨域规则 | `PROJECT_LOCAL_CANDIDATE_REVIEWED`；canonical repository/source policy 待 Human acceptance | `UNASSIGNED_DQ_003_MANIFEST_GAP`；Schema proposal 不是实际 status source | Developer Preview exact artifact 有历史 Decision；standing DBOS release authority 未冻结 | `PRIMARY_BOUNDED_DBOS_DOMAIN`；需独立 Authorization，不是最终授权者 | `NOT_APPLICABLE` |
| **EEOAP** | 不拥有 Digital Biosphere Architecture Authority；只拥有自身 profile semantics 候选 | `CANDIDATE_AGENT_EVIDENCE`；protocol manifest 与 canonical package 入口需 Owner/version crosswalk | 由其 canonical specification/source status 表达；独立 Status Authority 未冻结 | `UNVERIFIED_PROJECT_LOCAL`；validator/profile version 不等于 release decision | `NOT_APPLICABLE`；local validation 不构成运行控制 | `NOT_APPLICABLE` |
| **Agent Evidence** | supporting component，无跨项目 Architecture Authority | `SPLIT_SURFACES`：public reference、private/commercial workspace、AAEL adjacent profile 不能合并 | `SPLIT_SURFACES_UNRESOLVED` | 各 surface 独立；不得从 public release 推断 private release 或反向推断 | public reference 仅有 bounded local processing；commercial surface 只能是 product-local candidate，不能写 DBOS | `NOT_APPLICABLE` |
| **ARO / ARO-Audit** | 无跨项目 Architecture Authority；可维护自身 receipt/audit format | `PROJECT_LOCAL_CANDIDATE`；canonical branch/version/status source 未由 DBA 冻结 | `CONFLICTED_ROLE_DESCRIPTION`：public reference surface 与 control-plane 自述需对齐 | `UNVERIFIED_PROJECT_LOCAL` | 暂按 `BOUNDED_LOCAL_RECEIPT_VERIFIER`；不得宣称 production audit control plane | `NOT_APPLICABLE` |
| **PRA-Server** | `NOT_APPLICABLE`；只接受 DBA/TITMAS interface review | `LOCAL_ONLY_CANDIDATE`；当前无 observed origin、无顶层 license | `LOCAL_ONLY_UNFROZEN`；本地 branch/README 不足以成为跨项目状态源 | `UNASSIGNED_EXTERNAL_RELEASE_NOT_AUTHORIZED` | `PROJECT_LOCAL_PERSONAL_RUNTIME_ONLY`；无 DBOS、投稿或外部系统控制权 | `NOT_APPLICABLE` |
| **SAEE** | `DOMAIN_CONSTRAINT_CONTRIBUTOR`；不拥有 DBA 跨域规则 | `PROJECT_LOCAL`；capability manifest 只拥有 capability facts，不是完整项目状态 | project-wide canonical status source 仍受 `DQ-003` 约束 | public-safe extraction 的 exact Decision 不形成 standing SAEE release authority | 评价代码可运行，但不拥有 DBOS/Agent operational state；外部 writeback 为 false | `PRIMARY_PROTECTED_ADVISORY` |

### 5.1 矩阵解释

1. DBA 的 `PRIMARY_PROGRAM_ARCHITECTURE` 不等于拥有 DBOS/SAEE/EEOAP 源码；
2. TITMAS 当前连 `PROPOSED_NOT_ADOPTED` 都不能外推为独立项目 Source/Status/Release Authority；
3. DBOS 的 Operational Authority 与 Status Authority 分离：能维护规范运行记录不表示项目
   状态 manifest 已冻结；
4. EEOAP 的 profile semantics 属于其 source/version Owner，不因此成为 DBOS Evidence Object
   Owner 或标准组织；
5. Agent Evidence 目前是 family alias，不是可以接受单一 Authority Assignment 的主体；
6. PRA-Server 的 `Personal Runtime Authority` 只对本地科研节点有效；
7. SAEE 的 Evolution Authority 不能变成状态写权或运行控制权。

## 6. Canonical Object and Write Boundary（规范对象与写权边界）

| 对象／记录 | canonical Owner | 允许的外部作用 | 禁止的 Authority 抬升 |
|---|---|---|---|
| Digital Biosphere architecture rule / TMAP rule | DBA + explicit Human Decision | 项目提交 constraint、change proposal、implementation feedback | 子项目或 TITMAS 单方面改规则 |
| TITMAS mapping/profile | 采纳前为 DBA proposal；采纳后仍是 DBA 委托范围 | exact-version crosswalk、handoff、negative/conformance obligations | 成为第二 TMAP、EEOAP、MCP 或 OTel 标准权威 |
| DBOS Identity/Capability/Execution/Evidence/Verification/Lifecycle object | DBOS | EEOAP、Agent Evidence、ARO、PRA 提供 candidate material/reference/result | package、receipt、audit PASS 直接写成 canonical object |
| EEOAP operation accountability statement/profile | EEOAP canonical source/version Owner（待冻结） | TITMAS mapping；Agent Evidence reference implementation | DBA/TITMAS 改写 clause；validator PASS 变成认证或 DBOS Truth |
| Agent Evidence package/receipt | 产生该 package 的 Agent Evidence surface | provenance-preserving handoff、DBOS admission request | commercial/private package 覆盖 public spec，或 package 自证 Truth |
| ARO audit receipt/result | ARO source within exact scope | 作为 review/verification material 候选 | 变成全局 Verification、Governance Decision 或 Permission |
| PRA research/runtime record | PRA-Server local source within approved project scope | 经批准输出最小 result reference | 读取私密研究材料、自动投稿、写 DBOS/SAEE 或取得跨项目 status |
| SAEE Evaluation/Recommendation | SAEE | DBA/Human Review 只读引用；DBOS 可记录原始来源 | Recommendation 变成 Command、Permission、Release 或状态变化 |

默认写权矩阵：

```text
DBA_WRITES_CHILD_PROJECT_STATUS=false
TITMAS_WRITES_CONNECTED_PROJECTS=false
EEOAP_WRITES_DBOS=false
AGENT_EVIDENCE_WRITES_DBOS=false
ARO_WRITES_DBOS=false
PRA_SERVER_WRITES_DBOS=false
PRA_SERVER_WRITES_SAEE=false
SAEE_WRITES_DBOS=false
DBOS_WRITES_SAEE_INTERNAL_STATE=false
```

未来 adapter 若需要持久化，只能写自己的 adapter-local cache/receipt，并必须带 source、scope、
version、freshness 与 `non_canonical=true`；该 cache 不得成为 Status、Evidence 或 Verification
Authority。

## 7. Conflict Review（冲突审查）

### 7.1 第二事实权威

结论：`NO_CONFIRMED_ACTIVE_SECOND_FACT_AUTHORITY`，但有四个候选风险。

| finding | 严重度 | 候选第二权威 | 当前判断 | 失败关闭规则 |
|---|---|---|---|---|
| `AM-F001` | `HIGH` | DBA cockpit 与既有 public meaning layer | `DQ-008_OPEN`；不能声称唯一前门已对齐 | 不覆盖、不删除、不自动合并；由 ADR 决定 canonical relationship |
| `AM-F002` | `HIGH` | DBA snapshot / proposed DBOS manifest 与 DBOS project status | `DQ-003_OPEN`；Schema proposal 不是 status source | child-project status 优先；stale/conflict 必须显式保留 |
| `AM-F003` | `HIGH` | Agent Evidence package / ARO result 与 DBOS Evidence/Verification | 当前未获权；未来接口有抬升风险 | 只能作为 candidate material，经 DBOS admission 后产生独立 canonical object |
| `AM-F004` | `MEDIUM` | SAEE evaluation 与 DBOS/Governance state | 现有 no-writeback 边界有效 | Evaluation/Recommendation 永远引用原对象，不覆盖原记录 |

### 7.2 隐性写权限

结论：`IMPLICIT_WRITE_PERMISSION_AUTHORIZED=false`。

高风险措辞包括：`sync status`、`admit evidence`、`apply recommendation`、`publish profile`、
`control plane`、`runtime authority`、`commercial go`。没有 target object、issuer、scope、Decision
和 revocation 时，这些措辞只能解释为 proposal 或 local processing，不能解释为跨项目写权。

必须拒绝：

- TITMAS adapter 自动改变 framework、MCP、AGT、DBOS 或 SAEE state；
- EEOAP validator 把 `PASS` 写入 DBOS canonical Verification；
- Agent Evidence commercial worker 自动登记 DBOS Evidence；
- ARO audit result 自动关闭 DBA Gate；
- PRA-Server 自动投稿、外发、发布或控制其他项目；
- SAEE Recommendation 自动触发 DBOS 生命周期或 Agent 行为变化。

### 7.3 标准权威冲突

结论：`OPEN_REVIEW_REQUIRED`，未发现已生效的第二标准，但有三个未冻结点。

1. EEOAP `protocol/manifest.json` 指向 `docs/protocol/profile.md`，而 repository front door 又把
   `spec/execution-evidence-operation-accountability-profile-v0.1.md` 称为 canonical package
   spec；二者可以是 summary/normative document 分工，但必须由 EEOAP Owner 明确；
2. TITMAS 只能定义 `AccountabilityStatementMapping`、`EvidenceMaterialHandoff` 和
   `VerificationResultReference`，不能发布同名 canonical EEOAP/DBOS 对象；
3. TMAP、EEOAP、OpenTelemetry、MCP 与外部生态各自保留自己的 exact version authority；
   reference adoption、TITMAS profile adoption 与 Runtime integration 必须保持三轴状态。

```text
TMAP_NE_EEOAP=true
TITMAS_MAPPING_NE_STANDARD=true
EEOAP_PROFILE_VALIDATION_NE_CERTIFICATION=true
DBOS_VERIFICATION_NE_EEOAP_VALIDATION_REPORT=true
EXTERNAL_REFERENCE_ADOPTION_NE_RUNTIME_INTEGRATION=true
```

### 7.4 商业实现与公共规范冲突

结论：`HIGH_OPEN_AGENT_EVIDENCE_FAMILY_DECISION_REQUIRED`。

必须保持四条分离：

```text
PUBLIC_SPECIFICATION_OWNERSHIP
!= REFERENCE_IMPLEMENTATION_SOURCE_OWNERSHIP
!= COMMERCIAL_RUNTIME_OWNERSHIP
!= RELEASE_AND_LICENSE_AUTHORITY
```

当前 `agent-evidence` 是公开 EEOAP/reference surface；`agent-evidence-layer` 是本地
commercial/Runtime workspace；`agent-accountability-evidence-layer` 是相邻 AAEL/ASIEP
profile surface。三者不能因共享“Agent Evidence”名称而自动合并、迁移、重许可、统一
release 或归入 TITMAS/SAEE。

商业实现可以实现或适配一个公开 profile，但必须：

- 固定被实现的 exact spec/version/digest；
- 明确 extensions 与 normative fields；
- 不使用私有实现反向改写公共 clause；
- 不把商业 validator、SLA、customer result 或付费关系写成官方认证；
- 独立记录 source、status、release、Runtime 与 license Owner；
- 对 SAEE 关系使用 `STRATEGIC_SUBSYSTEM_RELATIONSHIP` 等精确类型，不使用模糊“owned by”
  推导源码、Runtime、Release 或 IP 转移。

### 7.5 ARO 角色冲突

当前 ARO 根 README 把仓库限定为 public receipt/audit-format reference surface，并否认 production
audit control plane；`docs/boundaries.md` 又把它描述为 post-execution audit control plane。
在 Owner 完成 role/status reconciliation 前：

```text
ARO_AUTHORITY_STATE=CONFLICTED_ROLE_DESCRIPTION
ARO_PUBLIC_SAFE_INTERPRETATION=BOUNDED_LOCAL_RECEIPT_VERIFIER
ARO_PRODUCTION_OPERATIONAL_AUTHORITY=false
ARO_DBOS_WRITE_AUTHORITY=false
```

这不是修改 ARO 状态，而是本次 DBA review 的失败关闭解释。

## 8. Authority Assignment Decision Model（Authority 指派决策模型）

未来任何 Authority Assignment ADR 必须回答：

| 字段 | 必须说明 |
|---|---|
| `assignment_id` | 稳定、唯一的 Authority Assignment ID |
| `authority_type` | 六类 Authority 之一；Program/Human Decision 另行引用 |
| `subject_id` | 被指派的项目、规范、组织或明确 Human role |
| `scope` | 对象类型、项目、环境、版本、channel、tenant 和时间范围 |
| `canonical_source_ref` | exact repository/spec/ref/commit/version/digest |
| `status_source_ref` | 该 Authority 自身状态的项目本地入口 |
| `owner_or_issuer_ref` | 能被验证的 Owner/issuer，不从 Git author 推断 |
| `decision_ref` | Human Decision / ADR；缺失时不能 ACTIVE |
| `write_effect` | `NONE` 或列出 exact target object/operation |
| `delegation_rule` | 是否可委托、委托范围、是否允许再委托 |
| `separation_of_duties` | proposer、reviewer、approver、operator、releaser 是否需要分离 |
| `validity` | `valid_from`、`review_due_at`、expiry |
| `revocation` | 撤销主体、撤销路径与已产生记录的保留规则 |
| `conflict_policy` | source/status/Owner 冲突时的失败关闭行为 |
| `negative_authorities` | 明确列出不拥有的 Authority 和 Permission |

Authority 状态机：

```text
PROPOSED
  -> READY_FOR_HUMAN_REVIEW
  -> ASSIGNED
  -> ACTIVE
  -> STALE | CONFLICTED | SUSPENDED
  -> SUPERSEDED | REVOKED | EXPIRED
```

文档、Schema 或 registry 可以记录状态，但不能自行执行上述转换。

## 9. Decision Points（待决事项）

| decision_id | 优先级 | 必须决定 | 不授权 |
|---|---|---|---|
| `AM-D01` | `P0` | DBA cockpit 与 public meaning layer 的 Architecture/Source Authority 关系 | 删除、覆盖、迁移或强制推送 |
| `AM-D02` | `P0` | DBOS project-local Status Authority、Owner、freshness 与 conflict policy | 自动选择 source、创建 manifest 或修改 revision |
| `AM-D03` | `P0` | Agent Evidence Family 的 spec/source/status/release/runtime/license Owner 矩阵 | 合并、改名、迁移、重许可或 IP 转移 |
| `AM-D04` | `P0` | EEOAP canonical normative document、version authority 与 release authority | 宣称标准组织采纳、认证或生产符合性 |
| `AM-D05` | `P1` | ARO public reference 与 control-plane role 的 canonical reconciliation | 生产审计部署、DBOS 写权或全局 Verification |
| `AM-D06` | `P1` | PRA-Server local Source/Status/Operational scope 和未来最小结果接口 | 读取私密材料、自动投稿、外发或公开发布 |
| `AM-D07` | `P1` | TITMAS 是否获得 DBA 委托的 bounded interoperability Architecture scope | Portfolio、Status、Release、Operational 或 Evolution Authority |
| `AM-D08` | `P1` | SAEE project-wide Status Source 与 standing Release Authority 是否需要单独冻结 | 核心算法公开、直连 telemetry、DBOS writeback |

这些 decision point 是审查输出，不自动修改 `DECISION-QUEUE.md`，也不构成 ADR。

## 10. Pre-development Agent Recommendation（开发前智能体建议）

若潜在用户询问“现在是否应把这八个项目接成一个统一 Authority Runtime”，本审查的答案是：

```text
AGENT_RECOMMENDATION=NOT_RECOMMENDED_AS_UNIFIED_AUTHORITY_RUNTIME
RECOMMENDED_AS=ARCHITECTURE_AUTHORITY_DECISION_MODEL
IMPLEMENTATION_RECOMMENDED_NOW=false
```

不推荐统一 Runtime 的原因：

- DBOS 与 SAEE 必须分别保留 Operational/Evolution Authority；
- TITMAS 尚未获得 Architecture scope，也不得取得项目状态或写权；
- DBOS 与 SAEE project-wide Status Authority 尚未完成 `DQ-003`；
- EEOAP/Agent Evidence/ARO 的 specification、status、release 与 Runtime Owner 尚有歧义；
- PRA-Server 目前是 local personal runtime，不能作为公共基础设施或跨项目控制面；
- commercial implementation 与 public specification 尚未冻结可验证的继承/扩展关系。

重新评估 bounded implementation（有界实现）的最低条件：

1. `AM-D02`–`AM-D05` 的 Authority owner/scope 决策完成；
2. 每个接口对象只有一个 canonical Owner；
3. 所有 adapter 默认 `PASSIVE_CAPTURE` / read-only；
4. cross-project write matrix 全部以负例验证失败关闭；
5. Release Authority 绑定 exact artifact，而不是 repository role；
6. SAEE 保持 `NO_CORE_DISCLOSURE`、`NO_DIRECT_TELEMETRY_INPUT`、`NO_WRITEBACK`；
7. Human Decision 明确授权一个最小、可撤销的实现范围。

## 11. Final Freeze and Non-claims（最终冻结与非声明）

```text
ARCHITECTURE_AUTHORITY_MODEL_REVIEW_V0_1_DEFINED=true
ARCHITECTURE_AUTHORITY_MODEL_REVIEW_ADOPTED=false
AUTHORITY_ASSIGNMENTS_CREATED=false
AUTHORITY_ASSIGNMENTS_CHANGED=false
PROJECT_OWNERSHIP_CHANGED=false
PROJECT_STATUS_CHANGED=false
PROJECT_RELEASE_STATUS_CHANGED=false
SOURCE_REVISIONS_CHANGED=false
MANIFEST_INSTANCE_CREATED=false
SCHEMA_CREATED=false
CODE_CHANGED=false
REPOSITORIES_MOVED=false
DBA_IS_CHILD_STATUS_AUTHORITY=false
TITMAS_IS_SECOND_ARCHITECTURE_AUTHORITY=false
TITMAS_HAS_CROSS_PROJECT_WRITE_AUTHORITY=false
DBOS_OPERATIONAL_AUTHORITY_EXPANDED=false
EEOAP_STANDARD_BODY_AUTHORITY_CLAIMED=false
AGENT_EVIDENCE_FAMILY_MERGED=false
ARO_PRODUCTION_AUTHORITY_CLAIMED=false
PRA_EXTERNAL_OPERATIONAL_AUTHORITY_CLAIMED=false
SAEE_EVOLUTION_AUTHORITY_EXPANDED=false
SAEE_CORE_EXPOSED=false
RELEASE_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
PRODUCTION_READY=false
```

本文件是 Architecture Governance 下的 Authority decision model review，不是 Authority
registry、status manifest、permission service、project reorganization、runtime topology、标准
认证、commercial agreement、release record 或 production fact。
