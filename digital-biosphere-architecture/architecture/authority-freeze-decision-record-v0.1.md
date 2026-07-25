---
document_id: DBA-AUTHORITY-FREEZE-DECISION-RECORD-0.1
title: Authority Freeze Decision Record v0.1
title_zh: 权威冻结决策记录 v0.1
status: AUTHORITY_FREEZE_CANDIDATE_READY_FOR_HUMAN_DECISION
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
document_type: ARCHITECTURE_DECISION_CANDIDATE
primary_repository: digital-biosphere-architecture
reviewed_at: 2026-07-23
decision_effect: NONE_UNTIL_HUMAN_DECISION
authority_assignment_effect: NONE
project_ownership_effect: NONE
implementation_effect: NONE
release_effect: NONE
---

# Authority Freeze Decision Record v0.1

中文：权威冻结决策记录 v0.1。

## 0. Candidate Verdict（候选结论）

本文件把 [Architecture Authority Model v0.1 Review](authority-model-v0.1.md) 的六类
Authority（权威）扩展为七类，新增 Specification Authority（规范权威），并形成等待人工
批准的 Authority Freeze Candidate（权威冻结候选）。它不指派、激活或转移任何 Authority。

```text
FREEZE_RECORD_STATUS=AUTHORITY_FREEZE_CANDIDATE_READY_FOR_HUMAN_DECISION
SEVEN_AUTHORITY_TYPES_DEFINED=true
AUTHORITY_ASSIGNMENTS_PROPOSED=true
AUTHORITY_ASSIGNMENTS_ADOPTED=false
AUTHORITY_ASSIGNMENTS_ACTIVE=false
HUMAN_ARCHITECTURE_DECISION_REQUIRED=true
TITMAS_DELEGATED_AUTHORITY_ASSIGNED=false
PROJECT_OWNERSHIP_CHANGED=false
IMPLEMENTATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
EXTERNAL_ACTION_AUTHORIZED=false
```

这里的 `freeze` 只表示候选边界已经足够明确，可以提交 Human Architecture Decision
（人工架构决定）。在明确 `decision_ref`、`decided_by_ref`、scope（作用范围）和有效期前，
所有候选状态均为 `PROPOSED_NOT_ADOPTED`。

## 1. Current Architecture State Summary（当前架构状态摘要）

### 1.1 Facts（事实）

| 事实 | 当前证据含义 |
|---|---|
| DBA 是 Program Governance and Architecture Specification Hub | 维护总架构、Portfolio、Decision Queue、Gate、Risk、ADR 与跨项目规则；不是 Runtime 或 child-project truth |
| TITMAS 是 DBA 下的 proposed interoperability architecture domain | 当前只有 DBA 内文档；不是第二治理层、项目管理系统、数据库或控制平面 |
| DBOS 是 canonical existence and record boundary | 保留 Identity、Lifecycle、Capability/Execution record、Evidence admission 与 Verification reference 的规范边界 |
| SAEE 是 protected evolution intelligence domain | 保留 Fitness、Reliability、Stability、Risk、Adaptation 与 Evolution Recommendation；无 DBOS 写权 |
| EEOAP 是 accountability profile | profile validation 不等于认证、系统安全、DBOS Truth 或生产符合性 |
| Agent Evidence 存在三个独立表面 | public EEOAP/reference、private/commercial Runtime、AAEL/ASIEP adjacent profile 未合并 |
| ARO 有不一致角色自述 | public bounded receipt/audit-format reference 与 post-execution control-plane 描述尚未对齐 |
| PRA-Server 是 local personal research runtime | 当前不能外推为公共基础设施、DBOS Authority、自动投稿或外部系统控制权 |

### 1.2 Observations（观察）

1. DBOS 推荐的 canonical repository/default branch/source snapshot 已有 decision input，但
   `DQ-003` 尚未决定，实际 project-local status manifest 未创建、未采纳；
2. EEOAP 的 `protocol/manifest.json` 与 repository front door 指向的规范文档角色尚需 Owner/
   version crosswalk（Owner／版本交叉表）；
3. Agent Evidence Family 的 public specification、reference implementation、commercial
   implementation、release 与 license Authority 仍未形成统一且分离的身份矩阵；
4. TITMAS 的 mapping/profile/adapter/conformance 范围已能描述，但尚未由 DBA 委托
   Architecture 或 Specification Authority；
5. OpenTelemetry 等生态目前必须分开表达 DBA reference adoption、TITMAS profile adoption
   与 Runtime integration，任一轴不得推高另一轴。

### 1.3 Recommendations（建议）

- 采用本文件第 5 节的七类 Authority 候选边界；
- Authority 必须按对象、版本、环境、channel 和时间明确 scope，不能只按项目名称指派；
- 优先决定 DBOS Status Authority、EEOAP Specification/Version Authority、Agent Evidence
  Family 分离矩阵与 ARO 角色；
- 只有上述决定完成后，才复核 TITMAS Interface v0.1 的冻结条件。

### 1.4 Decisions（决定）

```text
HUMAN_DECISIONS_RECORDED_IN_THIS_DOCUMENT=0
CURRENT_CONTENT_CLASS=DECISION_CANDIDATE_ONLY
```

本文件没有替 Human Program Owner、Human Architecture Decision、DBOS Domain Owner、SAEE
Owner、EEOAP Owner 或任何项目 Release Authority 作出决定。

## 2. Authority Model Principles（权威模型原则）

### `AF-001` Authority 必须有精确 scope

每项 Authority 至少绑定：`authority_type`、`subject_id`、对象类型、canonical source、
版本／commit、Owner/issuer、Decision ref、write effect、delegation、validity、revocation 与
conflict policy。缺失项时只能是 `PROPOSED`、`UNASSIGNED`、`UNKNOWN` 或 `CONFLICTED`。

### `AF-002` 七类 Authority 互不继承

```text
ARCHITECTURE_AUTHORITY_NE_SOURCE_AUTHORITY=true
SOURCE_AUTHORITY_NE_STATUS_AUTHORITY=true
STATUS_AUTHORITY_NE_RELEASE_AUTHORITY=true
RELEASE_AUTHORITY_NE_OPERATIONAL_AUTHORITY=true
OPERATIONAL_AUTHORITY_NE_EVOLUTION_AUTHORITY=true
SPECIFICATION_AUTHORITY_NE_ARCHITECTURE_AUTHORITY=true
SPECIFICATION_AUTHORITY_NE_CERTIFICATION_AUTHORITY=true
```

### `AF-003` 一个对象、范围和版本只有一个 canonical Owner

Mirror、dashboard、mapping、adapter、reference implementation、commercial implementation、
audit result 或 cache 不成为同一对象的第二 canonical Owner。冲突必须保留双方来源并
`FAIL_CLOSED`，不得自动选择更新时间更晚或状态更高的一方。

### `AF-004` Authority 不沿数据流传递

```text
Observation
  -> TITMAS mapping/handoff
  -> EEOAP / Agent Evidence candidate material
  -> DBOS admission and canonical record
  -> SAEE evaluation/recommendation
  -> explicit Human Decision
```

上述箭头不传递 Source、Truth、Permission、Release、Operational 或 Evolution Authority。

### `AF-005` Specification 与实现必须分离

公开规范、参考实现和商业实现可以有不同 Source、Status、Release、License 与 Runtime
Owner。实现一个规范不授予修改该规范的权力；商业关系也不产生标准组织、认证或架构权力。

## 3. Seven Authority Types（七类 Authority）

| Authority | 回答的问题 | 明确不包含 |
|---|---|---|
| Architecture Authority | 谁维护已采纳的跨项目架构、对象 Owner、边界、不变量与 ADR？ | 子项目 source/status/release、Runtime 写权、SAEE 算法权 |
| Source Authority | 哪个精确 repository/spec/ref/commit/version/digest 是命名工件的规范来源？ | 状态成熟度、发布、采用、Truth 或生产可用性 |
| Status Authority | 哪个项目本地入口声明 lifecycle、implementation、release/readiness、unknown/stale/conflicted？ | 自我授权、发布决定、Runtime truth |
| Release Authority | 谁可对 exact version/artifact/channel/audience/license scope 作发布决定？ | 由 tag、CI、仓库权限、历史一次发布自动推导的常设权力 |
| Operational Authority | 谁能在有效 Authorization/Capability/Permission/Lifecycle 下运行系统或写有界运行记录？ | 最终授权、跨项目状态写权、Evolution Authority |
| Evolution Authority | 谁能由有来源的只读输入形成评价与演化建议？ | Command、Permission、Release、DBOS writeback |
| Specification Authority | 谁能维护某个命名规范的 normative text、schema、clause、version 与兼容规则？ | 跨项目总架构、认证、Reference Implementation 或商业 Runtime 所有权 |

Architecture Authority 管“跨域规则与 Owner 边界”；Specification Authority 管“一个命名
规范在其授权范围内的 normative content（规范性内容）”。DBA 可同时承载 DBA/TMAP 的两种
职责，但这不让 DBA 成为 EEOAP、OpenTelemetry、MCP 或子项目内部规范的 Owner。

## 4. Project-to-Authority Candidate Matrix（项目到 Authority 候选映射）

矩阵中的全部内容均为 `PROPOSED_NOT_ADOPTED`，不是 Authority Assignment。

| 项目／规范面 | Architecture | Source | Status | Release | Operational | Evolution | Specification |
|---|---|---|---|---|---|---|---|
| **DBA** | `PRIMARY_PROGRAM_ARCHITECTURE_CANDIDATE` + Human Decision | `PROJECT_LOCAL_DBA_SOURCE`；`DQ-008` 待对齐 | `PROGRAM_PROJECTION_ONLY`，不拥有 child status | `EXACT_SCOPE_HUMAN_DECISION_ONLY` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `DBA_TMAP_NORMATIVE_SCOPE_CANDIDATE` |
| **TITMAS** | `PROPOSED_DELEGATED_INTEROP_SCOPE` | 当前为 DBA 内文档，无独立 source | 由 DBA proposal 状态表达；无 project status authority | `UNASSIGNED_NOT_AUTHORIZED` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `PROPOSED_ADAPTER_PROFILE_CONFORMANCE_SCOPE` |
| **DBOS** | `DOMAIN_CONSTRAINT_CONTRIBUTOR` | `PROJECT_LOCAL_CANDIDATE_REVIEWED`，待 Human acceptance | `UNASSIGNED_DQ_003_MANIFEST_GAP` | 历史 exact release 决定不形成 standing authority | `PRIMARY_BOUNDED_DBOS_DOMAIN_CANDIDATE` | `NOT_APPLICABLE` | `DBOS_CANONICAL_OBJECT_AND_PROJECT_CONTRACT_SCOPE` |
| **SAEE** | `DOMAIN_CONSTRAINT_CONTRIBUTOR` | `PROJECT_LOCAL` | project-wide canonical status source 待 `DQ-003` | exact public-safe decision 不形成 standing authority | 只运行自身评价；无 DBOS/Agent 控制权 | `PRIMARY_PROTECTED_ADVISORY_CANDIDATE` | `SAEE_BOUNDED_INTERFACE_AND_INTERNAL_SPEC_SCOPE` |
| **EEOAP** | 无 Digital Biosphere Architecture Authority | canonical spec source/version 待 crosswalk | 随 canonical source 表达；独立入口未冻结 | `UNVERIFIED_PROJECT_LOCAL` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `EEOAP_PROFILE_NORMATIVE_SCOPE_CANDIDATE` |
| **Agent Evidence Family** | supporting family alias，无跨项目权力 | `SPLIT_SURFACES` | `SPLIT_SURFACES_UNRESOLVED` | 各 surface 独立 | reference 仅 local processing；commercial 仅 product-local Runtime | `NOT_APPLICABLE` | public spec、reference、commercial 必须分离；family alias 无规范权 |
| **ARO / ARO-Audit** | 仅自身格式约束，无跨项目权力 | `PROJECT_LOCAL_CANDIDATE` | `CONFLICTED_ROLE_DESCRIPTION` | `UNVERIFIED_PROJECT_LOCAL` | reference=`BOUNDED_LOCAL_RECEIPT_VERIFIER`；control plane=`NOT_CONFIRMED` | `NOT_APPLICABLE` | receipt/audit format 可为 project-local 候选，非 DBOS Verification 规范 |
| **PRA-Server** | `NOT_APPLICABLE` | `LOCAL_ONLY_CANDIDATE` | `LOCAL_ONLY_UNFROZEN` | `EXTERNAL_RELEASE_NOT_AUTHORIZED` | `PROJECT_LOCAL_PERSONAL_RESEARCH_RUNTIME_ONLY` | `NOT_APPLICABLE` | local runtime policy only；无公共跨项目规范权 |

## 5. Authority Freeze Candidates（Authority 冻结候选）

### 5.1 Architecture Authority（架构权威）

| 必需输出 | 候选内容 |
|---|---|
| proposed owner | DBA 作为 Digital Biosphere Program Architecture 的规范承载面；重大变更由显式 Human Architecture Decision 批准。TITMAS 仅候选获得 DBA 委托的 interoperability scope。 |
| rationale | DBA 已维护 Portfolio、Decision Gate、TMAP、跨项目边界与 ADR；把 TITMAS 或子项目升级为平行架构层会形成第二治理权威。 |
| allowed responsibility | DBA：总架构规则、Portfolio、Decision Gate、Owner boundary 与 ADR；TITMAS：仅在获委托后维护 adapter/profile/handoff/lineage/version/conformance 的互操作架构。 |
| prohibited responsibility | DBA 不写 child truth；TITMAS 不管理 Portfolio/项目，不修改 DBOS/SAEE/EEOAP 权属，不建立第二 TMAP 或第二驾驶舱。 |
| conflict risk | `DQ-008` 的 DBA/public meaning 入口未对齐；TITMAS 名称与 TMAI/TMAP 接近；委托措辞可能被误读为独立最高 Authority。 |
| required human decision | `AF-D01`：确认 DBA canonical architecture surface 与 `DQ-008` 关系；`AF-D02`：是否委托 TITMAS 精确 interoperability Architecture scope、有效期与撤销规则。 |

### 5.2 Source Authority（来源权威）

| 必需输出 | 候选内容 |
|---|---|
| proposed owner | 每个项目／规范的 project-local canonical Owner；DBA 只拥有 DBA/TITMAS 文档 source。DBOS、SAEE、EEOAP、Agent Evidence 各 surface、ARO、PRA 分别保持自身 source。 |
| rationale | Source Authority 回答精确 bytes/version 的来源，不能由 DBA snapshot、TITMAS mapping、package artifact 或本地 checkout 替代。 |
| allowed responsibility | 维护 canonical repository/spec、ref、exact commit/version/digest、freshness 与 conflict policy；发布方可提供可验证 mirror/reference。 |
| prohibited responsibility | DBA/TITMAS 不复制 child source 后成为第二来源；wheel/tag/README/dirty branch 不自动成为 source authority；商业实现不覆盖公共规范 source。 |
| conflict risk | DBOS source policy待 Human acceptance；EEOAP 两个规范入口未 crosswalk；Agent Evidence 三表面 split；PRA 无 observed origin；ARO 角色/branch 状态未冻结。 |
| required human decision | `AF-D03`：接受或修订 DBOS source coordinate；`AF-D04`：冻结 EEOAP canonical normative source/version；`AF-D05`：冻结 Agent Evidence Family source identity matrix；`AF-D06`：确认 ARO/PRA local source scope。 |

### 5.3 Status Authority（状态权威）

| 必需输出 | 候选内容 |
|---|---|
| proposed owner | 每个 project-local Status Owner。DBA 仅为 timestamped program projection；TITMAS 当前无独立项目 Status Authority。 |
| rationale | 项目状态需要 source、freshness、unknown/conflict 和多轴语义；跨项目 cockpit 或 README 不能可靠替代 child-project truth。 |
| allowed responsibility | 项目本地入口维护 lifecycle、implementation、release/readiness、unknown/stale/conflicted；DBA/TITMAS 只读引用 exact source/digest/time。 |
| prohibited responsibility | manifest 不能自我授权；DBA 不回写 child status；测试 PASS、tag、package、Roadmap 或 dashboard observation 不升级状态。 |
| conflict risk | DBOS `PROJECT-STATUS.json` 仍是 schema proposal、未创建；SAEE project-wide status source 待定；Agent Evidence surface status 分裂；ARO role conflicted；PRA local-only。 |
| required human decision | `AF-D07`：决定 DBOS project-local Status Owner/path/freshness/conflict policy；`AF-D08`：分别处理 SAEE、Agent Evidence、ARO、PRA 的 project-local Status Authority，不创建 family-level 假权威。 |

### 5.4 Release Authority（发布权威）

| 必需输出 | 候选内容 |
|---|---|
| proposed owner | 对每个 exact artifact/version/channel/audience/license scope 指定的 Human/Organizational Release Authority；默认不设置跨项目 standing owner。 |
| rationale | Release 是不可逆且外部可见的 scope decision；repository owner、tagger、CI 或历史一次 `released_by_ref` 都不足以形成常设发布权。 |
| allowed responsibility | 对精确 source/artifact/digest、license、audience、channel、rollback 与 non-claims 作一次有界决定，并记录 `decision_ref`。 |
| prohibited responsibility | 从 Architecture/Source/Status/Operational role 推断 release；把 public reference release 推到 private commercial product，或反向推断；自动发布生态 PR。 |
| conflict risk | DBOS/SAEE 只有历史 exact-scope release records；EEOAP/ARO/PRA standing authority 未冻结；Agent Evidence public/private release 与 license 可能混写。 |
| required human decision | `AF-D09`：决定各项目是否需要 standing authority；若不需要，继续 exact-release-only。任何实际 release 必须另建记录，本冻结候选不授权发布。 |

### 5.5 Operational Authority（运行权威）

| 必需输出 | 候选内容 |
|---|---|
| proposed owner | DBOS 在 Digital Biosphere canonical existence/record domain 内拥有有界候选；PRA 只在 personal research node 内拥有 project-local Runtime；其他组件仅在自身本地处理范围内运行。 |
| rationale | 运行、验证、审计和评价必须与最终 Authorization/Permission 分离；TITMAS 是 passive interoperability architecture，不是 Runtime control plane。 |
| allowed responsibility | DBOS 在有效授权、Capability、Permission、Context 与 Lifecycle gate 下维护 canonical operational records；PRA 管理获准的本地科研流程；reference validator 只处理本地输入。 |
| prohibited responsibility | TITMAS/EEOAP/Agent Evidence/ARO/SAEE 不自动写 DBOS；PRA 不自动投稿、外发或控制其他项目；ARO reference 不宣称 production control plane。 |
| conflict risk | “admit/sync/apply/control plane”措辞可能产生隐性写权；ARO 自述冲突；commercial Agent Evidence worker 可能被误读为 DBOS writer。 |
| required human decision | `AF-D10`：确认 DBOS exact Operational scope 与外部 admission 只产生 request；`AF-D11`：对齐 ARO reference/control-plane；`AF-D12`：冻结 PRA local runtime、privacy 与 external-action 禁区。 |

### 5.6 Evolution Authority（演化权威）

| 必需输出 | 候选内容 |
|---|---|
| proposed owner | SAEE 作为唯一 protected, advisory Evolution Authority（受保护、仅建议的演化权威）候选。 |
| rationale | Fitness、Reliability、Stability、Risk、Adaptation 与长期演化判断是 SAEE 核心竞争能力，不能被公共互操作层或 DBOS Runtime 吸收。 |
| allowed responsibility | 消费经 DBOS admission 的版本化、只读、有界输入；形成带 scope、uncertainty、limitations 与 provenance 的 Evaluation/Recommendation。 |
| prohibited responsibility | 公开核心算法/模型/权重；直连原始 telemetry；写回 DBOS/framework/MCP/AGT；把 Recommendation 当 Command、Permission 或 Release Decision。 |
| conflict risk | `Evaluation Input` 名称或 `TITMAS -> SAEE` 简图可能暗示公共算法服务、绕过 DBOS 或自动执行。 |
| required human decision | `AF-D13`：由 SAEE Owner 批准最小 public contract 及 `VIA_DBOS_ADMISSION`、`READ_ONLY`、`NO_CORE_DISCLOSURE`、`NO_WRITEBACK`、`ADVISORY_ONLY`。 |

### 5.7 Specification Authority（规范权威）

| 必需输出 | 候选内容 |
|---|---|
| proposed owner | 按命名规范分域：DBA 拥有 DBA/TMAP normative scope；TITMAS 仅候选拥有其 Adapter Interface、Interoperability Profile 与 conformance rules；DBOS 拥有 DBOS canonical object/project contracts；SAEE 拥有受保护接口和内部规范；EEOAP Owner 候选拥有 EEOAP profile。 |
| rationale | 规范文本、schema、clause、version 与兼容性需要单一 Owner；同时必须避免“实现者就是规范 Owner”或“架构 Owner 拥有所有外部标准”。 |
| allowed responsibility | 每个 Owner 维护其 normative documents、versioning、compatibility、deprecation、claims 与 conformance vocabulary；TITMAS 只维护 mapping/profile/adapter 规范。 |
| prohibited responsibility | TITMAS 不改写 TMAP/EEOAP/OTel/MCP；reference/commercial implementation 不反向改 clause；profile validation 不宣称 certification、安全或 DBOS Truth。 |
| conflict risk | EEOAP normative document/version authority 未冻结；Agent Evidence public spec 与 reference implementation 共仓容易混淆；TITMAS Object 命名可能夺取 DBOS/EEOAP Owner。 |
| required human decision | `AF-D14`：冻结 EEOAP normative document、version issuer 与 public claim vocabulary；`AF-D15`：批准或拒绝 TITMAS 的 bounded Specification scope；`AF-D16`：批准 object ownership crosswalk，禁止同名第二 canonical object。 |

## 6. Required Subject Separations（必须保持的主体分离）

### 6.1 DBA

DBA 候选拥有总架构规则、Portfolio 与 Decision Gate 的 Architecture Authority，以及
DBA/TMAP 范围内的 Specification Authority。它只引用 child source/status，不拥有 DBOS
Runtime、EEOAP profile、SAEE evolution intelligence 或项目 release。

### 6.2 TITMAS

TITMAS 候选范围只有：interop architecture、adapter/profile contract、handoff、lineage、
version 与 conformance rules。即使 `AF-D02`/`AF-D15` 获批，也仍是 DBA 委托、可撤销且无
Source/Status/Release/Operational/Evolution Authority 的范围。

### 6.3 DBOS

DBOS 保持 canonical record boundary，包含 Identity、Lifecycle、Capability/Execution record、
Evidence admission 与 Verification reference。外部 package/receipt/result 只能提交 admission
request，不得直写或自证 canonical Truth。

### 6.4 SAEE

SAEE 保持 Evolution Intelligence 与 Fitness/Reliability/Stability 评价的 protected domain。
TITMAS 只能拥有 `EvaluationInputProfile` 类映射，不拥有 Evaluation、算法、模型、权重或
SAEE release。

### 6.5 EEOAP

EEOAP 是 public accountability profile 的 Specification Authority 候选，不是标准组织、
认证机构、DBOS Evidence Owner 或 Runtime control plane。其 canonical normative document、
version issuer 和 release authority 仍需人工冻结。

### 6.6 Agent Evidence Family

`Agent Evidence Family` 只是一项 architecture alias，不接受单一 Authority Assignment：

| surface | 候选角色 | 独立 Authority 边界 |
|---|---|---|
| `agent-evidence` | EEOAP public specification surface + bounded reference implementation | 规范与实现必须逻辑分离；repository source/release 不自动代表 EEOAP Owner 决定 |
| `agent-evidence-layer` | private/commercial implementation and Runtime workspace | project-local Source/Status/Release/Operational；不得改写公共 EEOAP 或自动写 DBOS |
| `agent-accountability-evidence-layer` | AAEL/ASIEP adjacent public profile | 独立 Specification/Source/Release；不等于 EEOAP 或 TITMAS standard |

```text
AGENT_EVIDENCE_FAMILY_IS_AUTHORITY_OWNER=false
PUBLIC_SPECIFICATION_NE_REFERENCE_IMPLEMENTATION=true
REFERENCE_IMPLEMENTATION_NE_COMMERCIAL_IMPLEMENTATION=true
COMMERCIAL_IMPLEMENTATION_NE_PUBLIC_SPECIFICATION_AUTHORITY=true
```

### 6.7 ARO

ARO 的 public reference layer 可以维护自身 receipt/audit format 与 bounded local verifier；
production control plane 是独立角色候选，在现有自述冲突解决前为 `NOT_CONFIRMED`。两者不能
共用一个模糊 Operational/Status Authority 声明。

### 6.8 PRA-Server

PRA 只拥有明确个人科研节点内的 local Source/Status/Operational scope 候选。它不拥有 DBA
Architecture、DBOS record、SAEE Evolution、公共 EEOAP specification、外部 release、自动
投稿或消息发送 Authority。

## 7. Conflict and Hidden-Permission Review（冲突与隐性权限审查）

| 检查 | 结论 | 未关闭风险 | 失败关闭行为 |
|---|---|---|---|
| 第二事实权威 | `NO_CONFIRMED_ACTIVE_SECOND_FACT_AUTHORITY` | DBA/public meaning、DBOS status projection、Evidence/Audit result、SAEE evaluation | 保留来源，标记 `CONFLICTED`，不写 canonical object |
| 隐性写权限 | `NO_AUTHORIZED_IMPLICIT_CROSS_PROJECT_WRITE` | sync/admit/apply/control-plane 等措辞 | 默认 `READ_ONLY` / `PASSIVE_CAPTURE` / admission request only |
| 标准权威冲突 | `OPEN_DECISION_REQUIRED` | EEOAP normative source、TITMAS object naming、外部标准 version authority | mapping 不成为 standard；同名对象不发布 |
| 商业实现与公共规范冲突 | `HIGH_OPEN_DECISION_REQUIRED` | Agent Evidence public/private/adjacent surfaces | 不合并、不迁移、不重许可、不统一 release |

必须持续成立：

```text
TELEMETRY_NE_EVIDENCE=true
EVIDENCE_PACKAGE_NE_TRUTH=true
AUDIT_RESULT_NE_AUTHORIZATION=true
PROFILE_MAPPING_NE_CERTIFICATION=true
SAEE_RECOMMENDATION_NE_COMMAND=true
REFERENCE_ONLY_NE_ADOPTED=true
```

## 8. Human Decision Package（人工决策包）

建议按以下顺序处理；`candidate result` 不是已经发生的决定：

| decision | candidate result | 关闭内容 | 明确不授权 |
|---|---|---|---|
| `AF-D01` | `ACCEPT_DBA_AS_CANONICAL_PROGRAM_ARCHITECTURE_SURFACE_WITH_DQ_008_FOLLOWUP` | DBA Architecture scope | 删除/覆盖 public meaning layer |
| `AF-D02` | `DELEGATE_BOUNDED_TITMAS_INTEROP_ARCHITECTURE_SCOPE` | TITMAS Architecture candidate | Portfolio/Status/Runtime 权力 |
| `AF-D03`/`AF-D07` | `ACCEPT_DBOS_SOURCE_POLICY_AND_PROJECT_LOCAL_STATUS_MODEL_WITH_FOLLOWUP` | DBOS Source/Status owner model | 创建 manifest、改 revision、pull/merge |
| `AF-D04`/`AF-D14` | `FREEZE_EEOAP_NORMATIVE_SOURCE_VERSION_AND_CLAIMS` | EEOAP Specification | certification/production claim |
| `AF-D05` | `FREEZE_AGENT_EVIDENCE_FAMILY_SEPARATION_MATRIX` | spec/reference/commercial/AAEL 分离 | 合并、迁移、重许可、IP 转移 |
| `AF-D11` | `RECONCILE_ARO_REFERENCE_AND_CONTROL_PLANE_ROLES` | ARO Source/Status/Operational | production deployment/DBOS write |
| `AF-D12` | `FREEZE_PRA_LOCAL_PERSONAL_RUNTIME_BOUNDARY` | PRA local Authority | 外发、投稿、公共发布 |
| `AF-D13` | `ACCEPT_SAEE_PROTECTED_ADVISORY_BOUNDARY` | SAEE Evolution scope | core disclosure/writeback |
| `AF-D15`/`AF-D16` | `DELEGATE_TITMAS_SPEC_SCOPE_AFTER_OBJECT_CROSSWALK` | TITMAS Specification/object naming | schema、代码、第二 canonical object |

任何一项被接受后，仍须形成可追溯的 `decision_ref` 与 scope；本表不能作为执行凭证。

## 9. Freeze Gate（冻结闸门）

Authority Freeze 只有在以下全部满足后才可从 Candidate 进入 Adopted：

1. Human Architecture Decision 记录 `decided_by_ref`、时间、accepted/rejected scope；
2. Architecture 与 Specification Authority 的差异被明确接受；
3. DBOS Status Owner/path/freshness/conflict policy 被决定；
4. EEOAP canonical normative document/version/claims 被决定；
5. Agent Evidence Family 分离矩阵被决定；
6. ARO reference/control-plane 角色被对齐；
7. SAEE protected interface 得到 SAEE Owner 审核；
8. 每项 negative authority（不拥有的 Authority）和撤销规则保留；
9. 没有 manifest、代码、仓库或 release 被候选文档自动创建。

```text
AUTHORITY_FREEZE_CANDIDATE_COMPLETE=true
AUTHORITY_FREEZE_ADOPTED=false
AUTHORITY_FREEZE_GATE_PASSED=false
NEXT_ACTION=HUMAN_ARCHITECTURE_DECISION
```

## 10. Final Non-claims（最终非声明）

```text
AUTHORITY_FREEZE_DECISION_RECORD_V0_1_DEFINED=true
AUTHORITY_ASSIGNMENTS_CREATED=false
AUTHORITY_ASSIGNMENTS_CHANGED=false
TITMAS_ARCHITECTURE_AUTHORITY_ACTIVE=false
TITMAS_SPECIFICATION_AUTHORITY_ACTIVE=false
DBOS_STATUS_AUTHORITY_ASSIGNED=false
EEOAP_SPECIFICATION_AUTHORITY_ASSIGNED=false
AGENT_EVIDENCE_FAMILY_MERGED=false
ARO_CONTROL_PLANE_AUTHORITY_CONFIRMED=false
PRA_EXTERNAL_AUTHORITY_CREATED=false
SAEE_EVOLUTION_AUTHORITY_EXPANDED=false
PROJECT_OWNERSHIP_CHANGED=false
PROJECT_STATUS_CHANGED=false
MANIFEST_INSTANCE_CREATED=false
SCHEMA_CREATED=false
CODE_CHANGED=false
REPOSITORIES_MOVED=false
RELEASE_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
PRODUCTION_READY=false
```

本文件是 Authority Freeze Decision Candidate，不是 Authority registry、Permission grant、
Project Status、标准认证、项目重组、实现计划、Release Record 或 Production fact。
