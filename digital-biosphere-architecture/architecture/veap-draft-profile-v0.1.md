---
document_id: DBA-TITMAS-VEAP-DRAFT-PROFILE-0.1
title: VEAP Draft Profile v0.1
title_zh: VEAP 可验证执行证明包草案规范 v0.1
version: 0.1.0
status: development-candidate-not-adopted
maturity: Development
maturity_scope: entire-document
owner_ref: DBA_ZHANGBIN_DRAFT_STEWARD
decision_reference: CS-D02-PRE-03
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Development candidate only; no implementation compatibility, adopted standard, conformance, certification, commercial availability, or production claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: non-executable-open-profile-candidate
architecture_domain: TITMAS
primary_repository: digital-biosphere-architecture
defined_at: 2026-07-26
normative_profile_adopted: false
specification_authority_assigned: false
implementation_authorized: false
authority_effect: none
---

# VEAP Draft Profile v0.1

中文：Verifiable Execution Attestation Package（可验证执行证明包）草案规范 v0.1。

## 0. Status and Purpose（状态与目的）

VEAP 是一个可携带、版本绑定的 reference envelope（引用信封），用于描述一次 Agent
execution 的身份、执行、上下文、Evidence admission、Verification、限制和撤销引用。

它回答：

> 谁在什么版本和责任上下文中执行了什么；哪些材料经过什么准入；哪个 verifier
> 根据什么规则返回了什么结果；当前有哪些失败、未知、限制和撤销状态？

```text
VEAP_DRAFT_PROFILE_CANDIDATE_CREATED=true
VEAP_NORMATIVE_PROFILE_ADOPTED=false
VEAP_SPECIFICATION_AUTHORITY_ASSIGNED=false
```

本文件使用 MUST、SHOULD、MAY 表达候选要求，便于智能体和 Reviewer 评估未来标准。
这些词在本阶段不构成已采纳标准或实现义务。

机器结构：

- [agent-readable Development entry](veap-development-agent-entry.v0.1.json)；
- [VEAP envelope Schema](schemas/veap-envelope.schema.v0.1.json)；
- [valid synthetic fixture](examples/veap-envelope.valid.v0.1.json)；
- [negative synthetic fixture](examples/veap-envelope.invalid-observation-as-evidence.v0.1.json)；
- [20-case conceptual catalog](veap-predecision-conformance-cases.v0.1.json)；
- [draft authorization](../TITMAS-CS-D02-PRE-03-VEAP-DRAFT-CONTRACT-DECISION-RECORD.md)。

### 0.1 Agent-first bounded reuse（智能体优先的有界复用）

当前唯一可复现的使用路径是 document/schema review（文档／Schema 审查）和 synthetic
Schema rehearsal（合成结构演练）：

1. 读取本 Profile 和机器入口，保持 Development、non-ownership 与 non-claim 状态；
2. 使用 Draft 2020-12 validator 加载候选 Schema，并记录 validator 及版本；
3. 正例 fixture 必须通过结构验证；
4. 缺少 `admission_reference`、却试图把 observation material 提升为 Evidence 的负例
   fixture 必须被拒绝；
5. 保存 Schema/fixture digest、validator/version、环境、实际结果和限制。

该路径不创建 parser、reference implementation、真实执行、Evidence、符合性 PASS 或独立
复用证据。需要当前实现依赖、商业 Offering、Certification 或生产能力时，推荐结果必须
为 `NO`；仅为评审候选契约或复演结构边界时，才可以 `CONDITIONAL`。

## 1. Non-ownership Rule（非所有权规则）

VEAP 只携带引用，不创建或拥有引用对象：

```text
VEAP_OWNS_IDENTITY=false
VEAP_OWNS_EXECUTION=false
VEAP_OWNS_EVIDENCE=false
VEAP_OWNS_VERIFICATION=false
VEAP_OWNS_EVALUATION=false
VEAP_OWNS_PERMISSION=false
VEAP_OWNS_CERTIFICATION=false
```

引用的 canonical Owner、source、namespace、version、digest 和限制必须保留。商业实现、
Validator 或付费服务不得反向成为 VEAP Specification Authority。

## 2. Envelope Requirements（信封要求）

一个结构有效的候选 envelope MUST 包含：

- `profile_version`：精确 Profile 版本；
- `attestation_id`：本包标识，不是 Entity ID、Execution ID 或 Certificate ID；
- `issued_at`：生成时间；
- `package_status`：`CURRENT`、`PARTIAL`、`REVOKED` 或 `NOT_ASSESSED`；
- `subject`：主体引用和 DBOS binding status；
- `execution`：执行来源、版本、任务、时间和状态；
- `context`：模型、工具和策略引用；
- `observation_references`：来源 observation；不得自动称为 Evidence；
- `evidence_bindings`：material、admission 和 canonical Evidence 的三段绑定；
- `verification_bindings`：verifier、rule、subject、status 和 limitations；
- `claims`：VEAP 能证明和明确不能证明的范围；
- `limitations`：已知缺失、不确定性、采样、丢失和适用范围；
- `revocation`：当前、撤销或未知状态。

## 3. Subject and Identity（主体与身份）

`subject.entity_reference` MUST 是带 source、namespace、identifier 和 version 的引用。

`subject.binding_status` 只允许：

- `DBOS_BOUND`：存在可检查的 DBOS binding reference；
- `EXTERNAL_ONLY`：只有外部 framework/runtime identity；
- `NOT_ASSESSED`：尚未判断。

`DBOS_BOUND` MUST 同时携带 `dbos_binding_reference`。Framework-local Agent ID、模型名、
service name 或 trace ID 不得自动成为 DBOS Digital Entity。

## 4. Execution（执行）

执行引用 MUST 包含：

- source 和 namespace；
- `execution_id`；
- `runtime_version`；
- `task_reference`；
- `started_at`；
- `status`。

`SUCCEEDED` 只描述来源记录的状态，不证明输出正确。失败、部分完成或未知必须分别保存为
`FAILED`、`PARTIAL`、`UNKNOWN`，不得被删除或提升为 success。

## 5. Observation and Evidence Admission（观察与证据准入）

```text
Observation
  -> Evidence Admission
  -> Canonical Evidence Reference
```

`observation_references` MUST 保留 producer、schema/version 和 delivery status。Sampling、
drop 或 partial delivery MUST 进入 `limitations`。

每个 `evidence_bindings` MUST 同时绑定：

1. `material_reference`；
2. `admission_reference`；
3. `canonical_evidence_reference`；
4. `admission_status`；
5. `integrity_status`。

没有 admission reference 的 Observation 不得进入 `evidence_bindings`。Schema 结构有效
不证明 admission 真实或 Evidence 内容正确。

## 6. Reference Integrity and Resolution（引用完整性与解析）

`material_reference` 和 `canonical_evidence_reference` MUST 携带 `sha256` 或 `sha512`
digest，且摘要长度必须与算法一致。摘要绑定只用于检测所引用 bytes 是否变化，不证明：

- issuer 可信；
- bytes 内容正确；
- admission 合法；
- material 足以支持某个结论。

其他 reference SHOULD 在后续版本中绑定稳定 URI、retrieval policy、availability status
和 canonical serialization。当前草案尚未定义统一解析协议、签名格式或网络 fetch 行为，
实现不得自行把可解析 URI 写成可信来源。

## 7. Verification（验证）

每个 Verification binding MUST 包含：

- `result_reference`；
- `verifier_reference`；
- `rule_reference`；
- `subject_reference`；
- `verification_status`；
- `limitations`。

Verification PASS 不产生 Permission、Authority、Certification、Truth 或执行成功。

## 8. Evaluation and Decision References（评价与决策引用）

`evaluation_bindings` 和 `decision_bindings` 均为可选只读引用。

- Evaluation 必须保留 SAEE interface/version、advisory status、uncertainty 和 limitations；
- VEAP 不计算 Fitness；
- Recommendation 不等于 Decision；
- Decision 不等于 Execution；
- 缺少 SAEE evaluation 不使现有 DBOS reference 自动失效。

## 9. Claim Profile（主张规则）

VEAP 只可以声明它携带了：

- execution history reference；
- provenance binding；
- verification result reference。

每个 envelope MUST 明确声明它不证明：

- `CORRECTNESS`；
- `TRUTH`；
- `PERMISSION`；
- `CERTIFICATION`。

```text
EVIDENCE_PROVES_EXECUTION_HISTORY_NOT_INTELLIGENCE_CORRECTNESS=true
EVIDENCE_NE_TRUTH=true
VERIFICATION_NE_PERMISSION=true
ATTESTATION_NE_CERTIFICATION=true
```

## 10. Revocation and History（撤销与历史）

`revocation.status=REVOKED` 时 MUST 提供 `revocation.reference` 和 `effective_at`。
被撤销的包不得作为 current 使用，但历史记录不得删除。

`revocation.status=UNKNOWN` 时不得静默当作 `CURRENT`。

## 11. Failure-closed Rules（失败关闭规则）

候选 consumer 应按以下语义处理：

| Condition | Candidate result |
|---|---|
| subject、execution source/version 或 task scope 缺失 | `REJECT` |
| Observation 没有 admission 却作为 Evidence | `REJECT` |
| Evidence digest mismatch | `REJECT` |
| Verification 被用作 Permission | `REJECT` |
| Evaluation 被写成 Decision | `REJECT` |
| Profile version 未知 | `UNSUPPORTED` |
| canonical Owner 冲突 | `CONFLICTED` |
| SAEE 不可用但 DBOS 引用完整 | `ACCEPT_PARTIAL_CANDIDATE` |

这些词是未来 conformance vocabulary 候选。已有
[20-case conceptual catalog](veap-predecision-conformance-cases.v0.1.json)
覆盖 ownership、provenance、semantic non-elevation、lifecycle failure 和 bounded positive，
但本阶段没有 case 被执行或通过。

## 12. Version and Change Control（版本与变更控制）

Profile 变化必须遵循：

- [Version Governance Specification](version-governance-specification.md)；
- [Version Compatibility Policy](version-compatibility-policy.md)；
- [Architecture Change Process](architecture-change-process.md)。

未知版本必须失败关闭；不得 silent downgrade。Development candidate 的字段和语义仍可
变化，任何实现都必须显式声明支持版本，不能以实现行为反向冻结规范。

## 13. Digital Immune Direction Boundary（数字免疫方向边界）

Evidence-first、bounded autonomy、history continuity 和分级响应可以作为未来 Digital
Immune constitutional profile 的设计输入。当前 VEAP v0.1 不定义 Health、Reputation、
Immune Response、Entity elimination 或 Digital Immune Cell，也不改变 DBOS、SAEE 和
Governance Decision 的既有职责。

## 14. Current State and Non-claims（当前状态与非主张）

```text
VEAP_DRAFT_PROFILE_CANDIDATE_CREATED=true
VEAP_SCHEMA_CANDIDATE_CREATED=true
VEAP_NORMATIVE_PROFILE_ADOPTED=false
VEAP_STANDARDIZATION_GATES_PASSED=0

CONFORMANCE_CASES_EXECUTED=0
CONFORMANCE_CASES_PASSED=0
REFERENCE_IMPLEMENTATION_CREATED=false
INDEPENDENT_IMPLEMENTATIONS=0

IMPLEMENTATION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```
