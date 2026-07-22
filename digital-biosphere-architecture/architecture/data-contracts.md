---
spec_id: DBA-DATA-CONTRACTS-0.1
title: Digital Biosphere Core Data Contracts v0.1
status: non-executable-object-contracts
schema_format_selected: false
object_instances_created: false
schema_mapping_reference: versioned-schema-mapping-specification.md
schema_mapping_governance_defined: true
schema_mapping_applied: false
registration_authorization_contract: registration-authorization-contract.md
registration_authorization_object_defined: true
registration_authorization_object_instantiated: false
verification_object_defined: true
verification_object_instantiated: false
telemetry_admission_contract_reference: telemetry-admission-foundation-specification.md
telemetry_admission_objects_defined: true
telemetry_admission_objects_instantiated: false
evidence_admission_contract_reference: telemetry-to-evidence-admission-contract.md
evidence_admission_objects_defined: true
evidence_admission_objects_instantiated: false
data_migration_effect: none
capability_effect: none
evidence_effect: none
authority_effect: none
permission_effect: none
---

# Digital Biosphere Core Data Contracts v0.1（数字生物圈核心数据契约 v0.1）

## 1. Owner（所有者）的含义

本文件中的 Owner 表示某类 contract object（契约对象）的规范创建、语义解释和版本变更责任域。Owner 不表示：

- 对现实事件或外部系统拥有全局真理权；
- 对其他仓库、代码或数据拥有所有权；
- 已经实现该对象；
- 获得新的执行、修改或治理权限。

Consumer（消费者）可以只读使用对象并创建带引用的派生对象，但不得修改原对象后仍保留原 Owner 和原 provenance（来源）声明。

## 2. 对象归属总表

| object_id | 核心对象 | Owner | 主要消费者 | 事实类别 |
|---|---|---|---|---|
| `DBA-OBJECT-ENTITY` | Entity Object（主体对象） | DBOS | SAEE | 存在与生命周期记录 |
| `DBA-OBJECT-CAPABILITY` | Capability Object（能力对象） | DBOS | Digital Entity、SAEE、Governance Decision Layer | 能力声明、验证和授权状态引用 |
| `DBA-OBJECT-EXECUTION` | Execution Object（执行对象） | DBOS | SAEE | 执行、资源与行为记录 |
| `DBA-OBJECT-EVIDENCE` | Evidence Object（证据对象） | DBOS | SAEE | 证据材料、来源与完整性状态 |
| `DBA-OBJECT-VERIFICATION` | Verification Object（验证对象） | DBOS | SAEE、Governance Decision Layer | 对明确对象、规则、输入和版本的有界检查结果 |
| `DBA-OBJECT-TELEMETRY-OBSERVATION-ENVELOPE` | Telemetry Observation Envelope（遥测观察封装） | DBOS admission boundary | future Evidence admission、SAEE（只读） | 规范化 metadata-only observation material；不是 Evidence |
| `DBA-OBJECT-TELEMETRY-ADMISSION-RECORD` | Telemetry Admission Record（遥测准入记录） | DBOS admission boundary | future Evidence admission、运维审查 | 对观察材料的只追加、失败关闭准入结果；不是 Truth |
| `DBA-OBJECT-EVIDENCE-ADMISSION-REQUEST` | Evidence Admission Request（证据准入请求） | DBOS Evidence admission boundary | Human Review、policy/validator | 对已准入 material 的用途、主体、来源、分类和授权引用；不是 Evidence |
| `DBA-OBJECT-EVIDENCE-ADMISSION-RECORD` | Evidence Admission Record（证据准入记录） | DBOS Evidence admission boundary | Evidence/Verification layer、Human Review、SAEE（只读） | 只追加 ADMITTED/PARTIAL/REJECTED/HOLD/UNKNOWN 结果；不是 Truth/Decision |
| `DBA-OBJECT-EVALUATION` | Evaluation Object（评价对象） | SAEE | DBOS | 基于输入记录形成的派生评价 |
| `DBA-OBJECT-RECOMMENDATION` | Recommendation Object（建议对象） | SAEE | DBOS | 非绑定演化或治理建议 |
| `DBA-OBJECT-DECISION` | Governance Decision Object（治理决策对象） | Governance Decision Layer | DBOS、SAEE（只读引用） | 审查、决策、采纳与执行引用的治理记录 |
| `DBA-OBJECT-REGISTRATION-AUTHORIZATION` | Registration Authorization Object（登记授权对象） | Governance Decision Layer | DBOS | 对指定 Candidate 和 `REGISTERED` target 的有界登记授权记录；不是 Permission |

## 3. Entity Object（主体对象）

Owner：DBOS

Purpose（目的）：在接口中引用被记录或被评价的 Digital Entity（数字主体），并表达其 DBOS 生命周期状态。

Entity Object 是 [`digital-entity-specification.md`](digital-entity-specification.md) 所定义 Digital Entity aggregate（数字实体聚合）的 Identity/Lifecycle projection（身份/生命周期投影），不是完整 Digital Entity 的单体复制。Capability Boundary 按 [`capability-boundary-specification.md`](capability-boundary-specification.md) 表达，Execution History 与 Evidence History 分别通过相应 DBOS 对象引用表达。

| 字段 | 语义 |
|---|---|
| `entity_id` | DBOS 管理的稳定、不透明主体引用 |
| `entity_type` | DBOS 管理的主体分类；本规范不新增类型 |
| `lifecycle_state` | DBOS 管理的生命周期状态 |

Mutation rule（变更规则）：只有 DBOS 责任域可以产生新的 canonical state（规范状态）记录。SAEE 可以引用 Entity Object，但不能创建身份、改变类型或写入生命周期状态。

Non-claim（非声明）：Entity Object 存在不等于身份已验证、能力存在、权限已授予或主体正在运行。

## 4. Capability Object（能力对象）

Owner：DBOS

Purpose：记录 Digital Entity 的 Capability declaration（能力声明）、有界验证状态、风险和授权引用，不把能力描述升级为 Permission 或 Execution。

| 字段 | 语义 |
|---|---|
| `capability_id` | 稳定、不透明的能力记录引用 |
| `entity_id` | 指向 DBOS 管理的 Entity Identity |
| `description` | 可审查的行为能力描述 |
| `scope` | 任务、对象、环境、时间和资源范围 |
| `constraints` | 禁止项、限制、依赖和失败条件 |
| `risk_level` | Low、Medium、High、Critical 或 unknown |
| `verification_status` | DBOS 有界验证状态 |
| `authorization_status` | 对外部明确授权记录的摘要或引用；不是 Permission |

Mutation rule：Digital Entity 可以提供声明材料；DBOS 管理 canonical Capability Object 与生命周期记录。SAEE 只读评价表现和风险，不能授予或修改 Capability；Governance Decision 记录高风险变化的 Decision，但不能直接写 Capability Object。

Non-claim：Capability Object、Verified 或 Authorized 状态都不证明当前 Permission、Execution、结果或 Digital Organism 资格。完整规则以 [`capability-boundary-specification.md`](capability-boundary-specification.md) 为准。

## 5. Execution Object（执行对象）

Owner：DBOS

Purpose：表达一次执行及其有界历史、时间、资源与行为记录。Digital Entity 可以是行为来源，但不是接口对象的自证权威。

| 字段或组成 | 语义 |
|---|---|
| `execution_id` | 执行记录或记录集合的稳定引用 |
| `entity_ref` | 指向 Entity Object，不复制身份所有权 |
| `event_history` | 有序事件记录或引用；保留缺口和未知项 |
| `timestamps` | 有语义标签和范围的时间记录 |
| `resource_consumption` | 有单位、时间和边界的资源测量 |
| `resource_history` | 有序资源记录或引用 |
| `action` | 被观察或登记的动作 |
| `result` | 与动作关联的有界结果 |
| `context` | 解释动作和结果所需的有界上下文 |

Mutation rule：DBOS 可以追加或更正带版本和来源的新记录，但不得静默重写历史。SAEE 只能读取并通过 `provenance_refs` 创建 Evaluation Object。

Non-claim：Execution Object 不证明执行正确、完整、成功或获授权。

## 6. Evidence Object（证据对象）

Owner：DBOS

Purpose：表达由 DBOS 采集、登记或封装的 Evidence material（证据材料）、来源和完整性边界。Verification 作为独立对象表达，防止把材料存在和检查结果混为一体。

| 字段或组成 | 语义 |
|---|---|
| `evidence_id` | Evidence Object 或 Evidence Bundle 的稳定引用 |
| `evidence_type` | 证据材料分类 |
| `integrity_status` | 在声明检查范围内的完整性状态 |
| `source_ref` | 原始记录、执行对象或外部材料的来源引用 |
| `scope` | 证据适用的对象、时间和材料边界 |
| `verification_refs` | 指向独立 Verification Object 的引用集合；缺失不等于未验证或验证通过 |

Mutation rule：DBOS 管理 canonical Evidence Object。SAEE 不得覆盖、删除或重新签发 DBOS Evidence；SAEE 的解释必须进入新的 Evaluation Object，并引用原 Evidence Object。

Compatibility note：既有接口中的 `verification_level` 和 `verification_status` 可以作为 Verification Object 的兼容 projection（投影）继续传输，但必须带 `verification_id` 或稳定来源引用；投影不得成为第二个 canonical Verification truth。

Non-claim：Evidence Object 或 `integrity_status` 不自动证明内容真实、结论正确、全局可信、合规或高适应度。

## 7. Verification Object（验证对象）

Owner：DBOS

Purpose：记录“对哪个对象、依据什么规则和版本、使用哪些输入、在何时得到什么有界检查结果”。Verification Object 独立于 Evidence Object、Permission 和 SAEE Evaluation。

| 字段或组成 | 语义 |
|---|---|
| `verification_id` | 一次有界验证的稳定、不透明引用 |
| `subject_refs` | 被验证的 Entity、Capability、Execution、Evidence 或其他受支持对象引用 |
| `rule_ref` | 验证规则、validator、policy 或 schema 的稳定引用 |
| `rule_version` | 实际执行验证所使用的精确版本 |
| `input_refs` | 输入材料和来源引用；不得只保存结论 |
| `verification_level` | 验证范围或等级，不表示全局可信度 |
| `verification_status` | passed、failed、partial、unknown、unsupported 或受控等价状态 |
| `verified_at` | 验证时间和时间来源 |
| `verifier_ref` | 执行验证的组件或责任来源；不自动成为 Authority |
| `limitations` | 未覆盖范围、采样、丢失、版本、时钟、冲突和其他限制 |

Mutation rule：DBOS 管理 canonical Verification Object。更正或重验必须追加新记录并引用旧结果，不得覆盖失败历史。外部 validator、OpenTelemetry Collector 或 observability backend 可以提供输入或执行材料，但不能因为生成结果而获得 DBOS Object Owner、Permission 或 Truth Authority。

Non-claim：`verification_status=passed` 不等于 Permission、Authorization、Fitness、Scientific Validity、Truth 或 Decision。

## 7A. Telemetry Observation Envelope（遥测观察封装）

Owner：DBOS admission boundary（DBOS 准入边界），仅在 `DQ-018` 获准并实现后才能产生对象实例。

Purpose：用 closed schema（封闭模式）封装 OTel/OTLP-derived metadata reference、Resource、Instrumentation Scope、Context、sampling、redaction、delivery 和 provenance limitation。字段、版本和敏感数据要求由 [`telemetry-admission-foundation-specification.md`](telemetry-admission-foundation-specification.md) 唯一定义；OpenTelemetry core/GenAI 字段进入 envelope 前的 non-authoritative mapping（非权威映射）由 [`opentelemetry-semantic-conventions-profile.md`](opentelemetry-semantic-conventions-profile.md) 与 [`opentelemetry-semantic-mapping.v0.1.json`](opentelemetry-semantic-mapping.v0.1.json) 定义。本文件不复制第二套 schema。

Mutation rule：输入 producer 只提供 untrusted declaration（不可信声明）。DBOS admission boundary 可以形成新 Envelope，但不得由 Resource、Context、digest、Collector 或 producer 声明推导 Identity、Permission 或 Truth。

Non-claim：Envelope 不是 OTLP wire message、Execution Object、Evidence Object 或 Verification Object。

## 7B. Telemetry Admission Record（遥测准入记录）

Owner：DBOS admission boundary，仅在 `DQ-018` 获准并实现后才能产生对象实例。

Purpose：用 append-only lifecycle（只追加生命周期）记录 Envelope 是否被接纳为 material，并保留 partial、rejected、confirmed/suspected duplicate、unknown 和 storage failure 边界。

Mutation rule：状态转换只能追加；producer 不能自证 idempotency trust；任何后续 Evidence admission 必须产生独立 Evidence Object 并引用该记录，不得改写 Admission Record。

Non-claim：`ACCEPTED_AS_MATERIAL`、commit acknowledgement 或 duplicate classification 都不等于 Evidence、Verification、Permission、Fitness 或 Truth。

## 7C. Evidence Admission Request（证据准入请求）

Owner：DBOS Evidence admission boundary，仅在独立 `DQ-021` 类人工授权和实施后才能创建实例。

Purpose：将 Telemetry Admission material、受管 content/material references、已有 DBOS subject/authorization references、purpose、classification、retention 和 provenance assurance 形成可重现的 Evidence admission input。Exact fields 以 [`telemetry-to-evidence-admission-contract.md`](telemetry-to-evidence-admission-contract.md) 为准。

Mutation rule：Request 提交后 immutable；修正需新 request 并引用旧版。OTel Resource/Context 不能生成 `entity_id`、`execution_id` 或 Authorization。

Non-claim：Request 不是 Evidence Object、Governance Decision、Permission 或 admission success。

## 7D. Evidence Admission Record（证据准入记录）

Owner：DBOS Evidence admission boundary，仅在独立授权和实施后才能创建实例。

Purpose：使用 append-only lifecycle 记录 `ADMITTED`、`PARTIAL`、`REJECTED`、`HOLD` 或 `UNKNOWN`，并在成功事务后引用新 Evidence Object。它必须保留 policy/validator version、input digests、provenance/identity/privacy/completeness limitations 和 independent Verification refs。

Mutation rule：所有状态只追加；Verification 失败、访问撤销、保留或 supersession 都用新 record，不改写/删除旧 Evidence。

Non-claim：`ADMITTED`、`P2_SOURCE_SIGNED`、Verification pass 或 Human Review 都不等于 Truth、Scientific Validity、Fitness、Permission 或执行授权。

## 8. Evaluation Object（评价对象）

Owner：SAEE

Purpose：表达 SAEE 基于 DBOS 对象形成的 Fitness Assessment 或 Risk Assessment。

| 字段或组成 | 语义 |
|---|---|
| `evaluation_id` | 一次评价的稳定引用；不替代输入对象标识 |
| `evaluation_type` | `fitness`、`risk` 或后续显式版本化的评价类型 |
| `input_refs` | 对 Entity、Execution、Evidence 或 Verification 输入的引用 |
| `model_ref` | 评价模型及版本引用；DBOS 不拥有该模型 |
| `reliability` | 模型与范围内的可靠性评价 |
| `efficiency` | 模型与范围内的效率评价 |
| `adaptability` | 模型与范围内的适应性评价 |
| `stability` | 模型与范围内的稳定性评价 |
| `risk_level` | 模型与范围内的风险分类 |
| `risk_reason` | 可追溯的风险理由、证据、假设和限制 |

Fitness 与 Risk 字段按 `evaluation_type` 使用；不适用字段必须明确为不适用或缺失，不得制造默认评价。

Mutation rule：SAEE 管理 Evaluation Object。DBOS 可以保存只读副本或引用，并另行记录接收状态；不得修改内容后仍声称为原始 SAEE Evaluation。

Authority class：`Recommendation`。Evaluation Object 是治理输入，不是 Command、授权或 DBOS 状态变化。

## 9. Recommendation Object（建议对象）

Owner：SAEE

Purpose：表达非绑定的 Evolution Recommendation 或 Governance Suggestion。

| 字段或组成 | 语义 |
|---|---|
| `recommendation_id` | 一次建议的稳定引用 |
| `recommendation_type` | `evolution` 或 `governance`；新增类型必须版本化 |
| `evaluation_refs` | 支持建议的 Evaluation Object 引用 |
| `recommended_change` | 演化建议中的候选变化，不是状态补丁 |
| `confidence` | 模型范围内的有界置信表达 |
| `suggestion` | 治理建议中的候选提议 |
| `rationale` | 支持建议的可追溯理由、假设与限制 |

Evolution 与 Governance 字段按 `recommendation_type` 使用；不适用字段不得被默认填充成伪事实。

Mutation rule：SAEE 管理 Recommendation Object。DBOS 可以记录其接收、审查、拒绝或独立授权结果，但这些状态属于新的 DBOS 记录，不能回写或覆盖原建议。

Authority class：`Recommendation`，明确不是 `Command`。

## 10. Governance Decision Object（治理决策对象）

Owner：Governance Decision Layer

Purpose：记录 Recommendation 的 Review、Decision、Adoption 与 `execution_reference`，保持 Decision 与 DBOS Execution 分离。

本文件只登记对象归属。规范字段、决策类型、状态约束与权限边界以 [`governance-decision-model.md`](governance-decision-model.md) 为准，状态转换以 [`governance-state-machine.md`](governance-state-machine.md) 为准。

Mutation rule：Governance Decision Layer 管理 Decision Object 的规范记录与状态；Architecture Governance 维护其规则定义。SAEE 不能批准或执行自己的 Recommendation；DBOS 不能修改 Decision 后声称为原始授权。DBOS 产生的执行、Evidence 和 Verification 必须作为独立对象通过引用关联。

Non-claim：Decision Object 形成治理记录，但不修改 Entity、Capability、Execution、Evidence、Evaluation 或 Recommendation 事实，也不创建最终授权主体。

## 11. Registration Authorization Object（登记授权对象）

Owner：Governance Decision Layer（治理决策层）管理对象语义、状态与历史。实际 issuer（签发者）必须由 `issuer_reference` 指向外部明确 authority record；Owner 不等于 issuer，也不自动获得签发权。

Purpose：把已批准的 `decision_type=admission` Decision 与 DBOS Registration 分开，表达“DBOS 可以在有界 scope 内尝试登记”，而不表达登记、激活或 Permission 已经发生。

| 字段 | 语义 |
|---|---|
| `authorization_id` | 登记授权记录的稳定、不透明标识；不是 Entity ID 或 Permission ID |
| `decision_reference` | 指向已批准、可解析且未撤销的 Admission Decision |
| `candidate_id` | 授权所针对的 Candidate reference；不是 canonical Entity Identity |
| `target_entity_type` | 已批准映射中的目标 Entity type；不授予其角色能力 |
| `authorized_scope` | operation、`REGISTERED` lifecycle target、conditions、期限和 exclusions |
| `issuer_reference` | 实际 issuer 及 authority record 引用；引用存在不证明有效 |
| `status` | `PENDING`、`AUTHORIZED`、`REJECTED` 或 `REVOKED` |
| `timestamp` | 授权状态事件时间及时间来源 |

Mutation rule：授权签发、拒绝、撤销或替代必须形成有来源、append-only（仅追加）的状态记录。DBOS 可以读取并形成独立 Registration Result，但不得改写 Authorization Object 后冒充原 issuer；SAEE 只能在明确输入范围内只读引用，不能签发或撤销。

Non-claim：`status=AUTHORIZED` 不等于 Registered、Active、Capability Grant、Permission、Execution 或 Runtime。完整签发条件、scope 与 DBOS 使用规则以 [`registration-authorization-contract.md`](registration-authorization-contract.md) 为准；Admission Decision 映射以 [`admission-governance-mapping.md`](admission-governance-mapping.md) 为准。

## 12. 对象引用与历史规则

1. 派生对象必须通过稳定引用指向输入对象，不得复制后切断 provenance。
2. Consumer 不得修改 Owner 对象并冒充原始对象。
3. 更正应产生带版本、时间和理由的新记录，不得静默删除历史。
4. Adapter（适配器）只转换表达形式，不因此成为对象 Owner。
5. `unknown`、`partial`、`conflicted` 和 `not_applicable` 必须保持可区分。
6. 对象所有权变化属于不兼容架构变更，需要 ADR 和显式人工批准。

## 13. Versioned Schema Mapping Governance（版本化模式映射治理）

本文件的字段表属于 Architecture Schema（架构模式），用于定义 canonical meaning（规范语义）。Contract Schema（契约模式）与 Implementation Schema（实现模式）中的同名或相似字段不得据此自动视为等价，也不得反向覆盖本文件的语义。

版本化映射规则以 [`versioned-schema-mapping-specification.md`](versioned-schema-mapping-specification.md) 为准；当前实体、能力与证据映射分别记录在：

- [`entity-schema-mapping.md`](entity-schema-mapping.md)；
- [`capability-schema-mapping.md`](capability-schema-mapping.md)；
- [`evidence-schema-mapping.md`](evidence-schema-mapping.md)。

兼容性与变更分类以 [`schema-version-policy.md`](schema-version-policy.md) 为准。当前已知边界包括：

1. `owner_reference` 是 Research Agent Registration Contract（科研智能体登记契约）中的 contract extension（契约扩展），当前不是本文件 Entity Object 的字段；
2. Architecture Capability Object 的 `description` 与实现观察到的 `capability_name` 只能通过显式映射关联；
3. `Medium` 与实现观察到的 `MODERATE` 未经治理决定不得视为等价；
4. `authorization_status` 不得被解释为 Permission（许可），且当前架构未定义独立的 canonical Permission Object；
5. Evidence Material（证据材料）、Evidence Reference（证据引用）与 canonical Evidence Object（规范证据对象）必须保持区分。

Schema Mapping（模式映射）不执行 Data Migration（数据迁移）、版本升级、对象实例化或状态变更。无法证明语义等价的字段必须保持 `Unknown`，不得用猜测补齐。

## 14. 非实现状态

```text
DATA_OBJECT_CONTRACTS_DEFINED=true
DATA_OBJECTS_INSTANTIATED=false
SERIALIZATION_DEFINED=false
DATABASE_DEFINED=false
OBJECT_OWNER_GRANTS_RUNTIME_AUTHORITY=false
GOVERNANCE_DECISION_OBJECT_INSTANTIATED=false
REGISTRATION_AUTHORIZATION_OBJECT_DEFINED=true
REGISTRATION_AUTHORIZATION_OBJECT_INSTANTIATED=false
REGISTRATION_AUTHORIZATION_ISSUED=false
REGISTRATION_PERMISSION_EFFECT=NONE
DBOS_REGISTRATION_EXECUTED=false
CAPABILITY_OBJECT_INSTANTIATED=false
VERIFICATION_OBJECT_DEFINED=true
VERIFICATION_OBJECT_INSTANTIATED=false
TELEMETRY_ADMISSION_OBJECTS_DEFINED=true
TELEMETRY_ADMISSION_OBJECTS_INSTANTIATED=false
TELEMETRY_ADMISSION_IMPLEMENTATION_AUTHORIZED=false
EVIDENCE_ADMISSION_OBJECTS_DEFINED=true
EVIDENCE_ADMISSION_OBJECTS_INSTANTIATED=false
EVIDENCE_ADMISSION_IMPLEMENTATION_AUTHORIZED=false
VERSIONED_SCHEMA_MAPPING_REFERENCE_DEFINED=true
SCHEMA_MAPPING_APPLIED=false
DATA_MIGRATION_AUTHORIZED=false
DATA_MIGRATION_EXECUTED=false
IMPLEMENTATION_SCHEMA_CANONICALIZED=false
```
