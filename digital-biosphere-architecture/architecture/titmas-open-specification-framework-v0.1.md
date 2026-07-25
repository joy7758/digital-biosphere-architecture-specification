---
document_id: DBA-TITMAS-OPEN-SPECIFICATION-FRAMEWORK-0.1
title: TITMAS Open Specification Framework v0.1
title_zh: TITMAS 开放规范框架 v0.1
version: 0.1.0
phase: C3
status: open-specification-framework-candidate-no-standard-created
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
document_type: non-executable-specification-system-candidate
architecture_domain: TITMAS
document_maturity: Development
specification_ready: false
stable_specifications_created: 0
number_registry_created: false
implementation_authorized: false
external_action_authorized: false
authority_effect: none
---

# TITMAS Open Specification Framework v0.1

## 1. Purpose（目的）

本框架定义未来 TITMAS Specification System 的文档结构、生命周期和首批候选范围。它不
创建 Standard、Registry、编号、规范 Owner、Reference Implementation 或公共发布。

```text
PHASE=C3_OPEN_SPECIFICATION_FRAMEWORK
TITMAS_OPEN_SPECIFICATION_FRAMEWORK_DEFINED=true
TITMAS_SPECIFICATION_READY=false
TITMAS_STABLE_SPECIFICATIONS_CREATED=0
```

## 2. Specification System（规范系统）

每项未来规范由六类工件构成：

1. **Proposal**：问题、scope、non-goals、来源和替代方案；
2. **Normative Document**：MUST/SHOULD/MAY、对象、状态和失败语义；
3. **Schema/Contract**：可机读结构候选；
4. **Conformance Cases**：positive、negative、unknown、unsupported、failure；
5. **Implementation Declaration**：实现版本、支持矩阵与限制；
6. **Decision and History**：review、Decision、errata、deprecation 与 successor。

这些工件状态相互独立：

```text
SPECIFICATION_NE_IMPLEMENTATION=true
SCHEMA_VALID_NE_STANDARD=true
CONFORMANCE_PASS_NE_CERTIFICATION=true
DOCUMENT_STABLE_NE_ECOSYSTEM_STABLE=true
```

## 3. Numbering Model（编号模型）

未来使用：

```text
TITMAS-XXXX
TITMAS-E-XXXX
TITMAS-A-XXXX
TITMAS-V-XXXX
TITMAS-I-XXXX
TITMAS-R-XXXX
TITMAS-S-XXXX
```

编号规则遵循
[TITMAS RFC Numbering and Document Model](titmas-rfc-numbering-and-document-model-v0.1.md)。
`XXXX` 只由未来获授权的 Number Registry 分配；本文件中的首批候选不占号。

## 4. Specification Lifecycle（规范生命周期）

```text
Idea
  -> Draft
  -> Experimental
  -> Candidate
  -> Stable
  -> Deprecated / Superseded / Archived
```

| Stage | Minimum evidence | Required review | Prohibited claim |
|---|---|---|---|
| `Idea` | problem、scope、user need | intake/duplicate | proposal adopted |
| `Draft` | fields、state、failure、source | architecture/domain | consensus or standard |
| `Experimental` | explicit Decision、version、Owner、test plan | security/compatibility | stable or production |
| `Candidate` | implementation feedback、resolved critical issues | broad + independent review | universal adoption |
| `Stable` | frozen Authority/Owner、compatibility、multiple evidence sources | Human Architecture Decision | certification or commercial availability |

具体 Entry/Exit/Authority 见
[TITMAS Proposal Lifecycle](titmas-proposal-lifecycle-v0.1.md)。

## 5. Initial Specification Candidates（首批规范候选）

以下只使用 candidate label，不是正式编号。

### `TITMAS-E-CANDIDATE` — Agent Evidence Object

候选作用：定义 Agent 行为材料的 exchange envelope、source、lineage、integrity、failure 和
admission status。

边界：

- 不是 DBOS canonical Evidence Object；
- package 或 envelope 不证明 Truth；
- Agent Evidence Family 保持自身 source ownership；
- 只有 DBOS admission 才能产生独立 canonical record。

### `TITMAS-A-CANDIDATE` — Accountability Statement

候选作用：映射 action、actor、context、policy、result reference 与 responsibility statement。

边界：

- 不改写 EEOAP normative clauses；
- statement 不等于法律责任认定、审计通过或认证；
- mapping 需绑定 exact EEOAP version 和 Owner。

### `TITMAS-V-CANDIDATE` — Verification Result

候选作用：定义 verifier、subject、rule/version、status、limitations 和 evidence references 的
互操作交接。

边界：

- 不是 DBOS canonical Verification Truth；
- Validator PASS 不产生 Permission、Authority、Adoption 或 Certification；
- self-attestation 和 independent verification 必须分开。

### `TITMAS-I-CANDIDATE` — Interoperability Profile

候选作用：定义两个已命名系统之间的 exact-version mapping、supported/partial/unsupported、
error、retry、idempotency 和 no-writeback。

边界：

- Mapping 不表示 Adoption、认可或完整运行兼容；
- Profile 不成为被映射项目的第二 Specification Authority；
- 每个方向分别声明 read/write effect。

### `TITMAS-R-CANDIDATE` — Evaluation Interface

候选作用：定义经 DBOS admission 的只读 Evaluation Input、SAEE Evaluation/Recommendation
reference 和 uncertainty/limitations envelope。

边界：

- SAEE 保持 protected Evolution Authority；
- 不公开 SAEE 核心算法、模型、权重或私有 heuristics；
- Evaluation 不等于 Authority，Recommendation 不等于 Command；
- TITMAS、Adapter 或 DBOS 不生成 Fitness 结论。

## 6. Normative Ownership Crosswalk（规范权属交叉表）

| Candidate | Canonical domain that must be preserved | TITMAS may own only |
|---|---|---|
| `E` | DBOS canonical records + Agent Evidence source | exchange/admission profile |
| `A` | EEOAP specification Owner | exact-version mapping |
| `V` | verifier source + DBOS verification boundary | result handoff/conformance vocabulary |
| `I` | each mapped external/project Owner | interoperability profile |
| `R` | SAEE protected evaluation domain | read-only interface envelope |

Owner/Authority 未冻结时，规范停留 Draft：

```text
NORMATIVE_PROMOTION_ALLOWED=false
```

## 7. Open Specification Requirements（开放规范要求）

未来公开规范必须：

- 可公开读取、版本化和精确引用；
- license/IPR contribution policy 明确；
- machine-readable schema 与 human-readable meaning 一致；
- 公开 errata、breaking、deprecation 和 migration；
- 保留失败、异议和 rejected proposal；
- 不绑定单一模型、Agent framework、Runtime、云或商业服务；
- 允许独立实现，不要求购买商业产品；
- 明确 `Evidence != Truth` 与 `Validator != Authorization`。

## 8. Current Blockers（当前阻塞）

- Authority Freeze 未采纳；
- Specification/Registry Owner 未指派；
- public contribution 未授权；
- license/IPR/CLA 路线未决定；
- Security Disclosure 和正式 Code of Conduct 未激活；
- 没有独立实现或 conformance evidence；
- TITMAS Interface v0.1 仍未达到 freeze ready。

## 9. Human Decision Candidate（人工决定候选）

```yaml
decision_id: OS-D01
question: Adopt the TITMAS open specification system and five initial scopes as Draft candidates?
recommended_result: DEFER_UNTIL_AUTHORITY_AND_OWNERSHIP_FREEZE
scope_if_accepted:
  - specification_process_only
  - five_draft_candidate_scopes
explicit_non_authorizations:
  - number_allocation
  - experimental_or_stable_status
  - schema_or_implementation
  - public_standard_claim
decision_status: NOT_READY_FOR_APPROVAL
```

## 10. Final State（最终状态）

```text
TITMAS_OPEN_SPECIFICATION_FRAMEWORK_DEFINED=true
TITMAS_INITIAL_SPECIFICATION_CANDIDATES_DEFINED=5
TITMAS_SPECIFICATION_READY=false
TITMAS_NUMBER_REGISTRY_CREATED=false
TITMAS_NUMBERS_ASSIGNED=0
TITMAS_EXPERIMENTAL_SPECIFICATIONS_CREATED=0
TITMAS_STABLE_SPECIFICATIONS_CREATED=0
TITMAS_STANDARD_CLAIMED=false
TITMAS_IMPLEMENTATION_AUTHORIZED=false
```
