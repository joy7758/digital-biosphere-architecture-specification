---
document_id: DBA-TITMAS-VEAP-CANONICAL-OWNERSHIP-CROSSWALK-0.1
title: VEAP Canonical Ownership Crosswalk v0.1
title_zh: VEAP 规范权属交叉表 v0.1
version: 0.1.0
status: predecision-candidate-ownership-not-frozen
maturity: Development
maturity_scope: entire-document
owner_ref: NOT_ASSIGNED
decision_reference: CS-D01_NOT_DECIDED
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Pre-decision ownership review only; no normative, implementation, conformance, certification, commercial, or production compatibility claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: non-executable-canonical-ownership-review-candidate
architecture_domain: TITMAS
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-25
crosswalk_defined: true
ownership_frozen: false
specification_authority_assigned: false
implementation_authorized: false
authority_effect: none
---

# VEAP Canonical Ownership Crosswalk v0.1

## 0. Verdict（结论）

本交叉表回答：

> VEAP 可以引用什么、可以规范什么、绝不能从现有项目夺取什么？

当前结论：

```text
VEAP_CANONICAL_OWNERSHIP_CROSSWALK_DEFINED=true
VEAP_OWNERSHIP_FROZEN=false
VEAP_SPECIFICATION_AUTHORITY_ASSIGNED=false
CS_D01_DECIDED=false
```

VEAP 只能成为一个 future bounded exchange/profile specification candidate（未来有界交换
Profile 规范候选）。它不能成为 Identity、Execution、Evidence、Verification、Evaluation、
Permission、Certification 或商业服务的第二 canonical Owner。

## 1. Source Basis（来源依据）

本次只引用 DBA 当前规范材料：

- [Authority Model Review](authority-model-v0.1.md)；
- [Authority Freeze Decision Record](authority-freeze-decision-record-v0.1.md)；
- [TITMAS and DBA Relationship](titmas-dba-relationship.md)；
- [TITMAS Open Specification Framework](titmas-open-specification-framework-v0.1.md)；
- [DBOS Canonical Source Resolution](dbos-canonical-source-resolution-v0.1.md)；
- [DBOS–SAEE Interface](interface-specification.md)；
- [SAEE–DBOS Contract](saee-dbos-contract.md)；
- [Data Contracts](data-contracts.md)；
- [CS-D01 Decision Packet](../TITMAS-CS-D01-VEAP-PROBLEM-SCOPE-DECISION-PACKET.md)；
- [CS-D01 Agent Review](../TITMAS-CS-D01-AGENT-CUSTOMER-REVIEW.md)。

这些来源中仍存在未决定项，因此本交叉表不能把 `PROPOSED`、`RESPONSIBILITY_DOMAIN`、
`UNASSIGNED` 或 `CANONICAL_SOURCE_UNRESOLVED` 写成 `ACTIVE_AUTHORITY`。

## 2. Ownership Principles（权属原则）

### `VEAP-OWN-001` 引用不产生所有权

VEAP 携带 `entity_reference`、`execution_reference`、`evidence_reference`、
`verification_reference` 或 `evaluation_reference`，不取得这些对象的创建、修改、删除或
解释权。

### `VEAP-OWN-002` Profile 不创建第二对象体系

VEAP 不建立自己的：

- Entity registry；
- lifecycle state machine；
- Evidence store；
- Verification truth；
- Permission store；
- Fitness model；
- Certification registry。

### `VEAP-OWN-003` 外部来源必须保留

Runtime observation、OpenTelemetry data、EEOAP statement、Agent Evidence package、
verifier result 和 SAEE evaluation 必须带 exact source/version/issuer/limitations，不能统一改写
为 “TITMAS fact”。

### `VEAP-OWN-004` 商业实现不能反向拥有规范

未来 private node、managed service、reporting UI 或付费 Adapter 不能因为运行或销售 VEAP
而取得 TITMAS Specification Authority、DBOS record Authority 或 Certification Authority。

## 3. Canonical Ownership Matrix（规范权属矩阵）

| Surface | Current canonical responsibility | VEAP may define/carry | VEAP prohibited effect | Current status |
|---|---|---|---|---|
| Program/Architecture rule | DBA + explicit Human Decision | decision/profile references | self-adopt Architecture rule | `RESPONSIBILITY_DOMAIN_CONFIRMED` |
| VEAP exchange/profile text | future bounded TITMAS Specification Authority | envelope、mapping、version、failure、claim vocabulary | rewrite DBOS/EEOAP/SAEE objects | `UNASSIGNED_CS_D01_AF_D15` |
| Entity identity/lifecycle | DBOS responsibility domain | opaque reference、version、observed state | create/register/activate/modify entity | `RESPONSIBILITY_DOMAIN_CONFIRMED_SOURCE_STATUS_PARTIAL` |
| Capability/Permission | DBOS operational boundary + explicit authorization | declared capability/permission reference if allowed | infer or grant permission | `RESPONSIBILITY_DOMAIN_CONFIRMED` |
| Execution record | DBOS responsibility domain | immutable execution reference and scope | execute task or invent success | `RESPONSIBILITY_DOMAIN_CONFIRMED` |
| Runtime observation | named Runtime/telemetry producer | source/version/event delivery reference | call observation Evidence | `SOURCE_SPECIFIC_EXTERNAL_OWNER` |
| Evidence material/package | named Agent Evidence/source producer | package reference and provenance | make package canonical DBOS Evidence | `SPLIT_SOURCE_SURFACES_UNRESOLVED` |
| Evidence admission/canonical Evidence | DBOS responsibility domain | admission status and canonical evidence reference | bypass admission or assert Truth | `RESPONSIBILITY_DOMAIN_CONFIRMED` |
| Accountability statement | EEOAP canonical Specification Owner candidate | exact-version statement reference | decide legal responsibility or rewrite EEOAP | `CANONICAL_VERSION_OWNER_UNRESOLVED_AF_D04_AF_D14` |
| Verification result | named verifier + DBOS reference boundary | verifier/rule/version/status/limitations | grant Permission or Certification | `SOURCE_SPECIFIC_PLUS_DBOS_BOUNDARY` |
| Evolution evaluation | SAEE protected advisory domain | read-only input/output reference and uncertainty | calculate Fitness or execute recommendation | `RESPONSIBILITY_DOMAIN_CONFIRMED_PUBLIC_CONTRACT_PENDING_AF_D13` |
| Governance Decision | explicit Human/Governance Decision Authority | decision/authorization reference | turn recommendation into decision | `EXPLICIT_DECISION_REQUIRED` |
| Commercial service | future legal/service Owner | separately versioned service reference | sell standard ownership or alter public protocol | `UNASSIGNED_NO_OFFERING` |
| Certification | future independent authorized body, if ever created | certification reference only after authorization | self-certify or issue current certificate | `NOT_CREATED_NOT_AUTHORIZED` |

## 4. VEAP-Owned Candidate Surface（VEAP 可拥有的候选表面）

只有 Human Decision 接受 `CS-D01`、`AF-D15` 和 `AF-D16` 的 exact scope 后，VEAP 才可能
进入以下 bounded Specification candidate：

```text
VEAP_PROFILE_CANDIDATE_SCOPE=
  exchange_envelope
  reference_binding
  profile_version
  compatibility_and_migration
  partial_unknown_failure_revocation_semantics
  implementation_declaration
  conformance_case_and_result_vocabulary
  claim_and_limitation_vocabulary
```

显式排除：

```text
VEAP_OWNS_IDENTITY=false
VEAP_OWNS_EXECUTION=false
VEAP_OWNS_EVIDENCE=false
VEAP_OWNS_VERIFICATION=false
VEAP_OWNS_EVALUATION=false
VEAP_OWNS_PERMISSION=false
VEAP_OWNS_CERTIFICATION=false
```

## 5. Required Reference Classes（必须引用类别）

未来 envelope candidate 若获准起草，至少应区分：

| Reference class | Required provenance | Failure when missing |
|---|---|---|
| `subject_reference` | issuer、namespace、version/state、DBOS binding status | `REJECT_OR_NOT_ASSESSED` |
| `execution_reference` | DBOS/source ID、task、time、status、failure | `REJECT` |
| `observation_reference` | producer、schema/version、delivery/sampling status | `MATERIAL_ONLY_NOT_EVIDENCE` |
| `admission_reference` | DBOS rule/version/result、provenance、limitations | `NO_CANONICAL_EVIDENCE_CLAIM` |
| `evidence_reference` | canonical/source type、digest、integrity/unknown | `REJECT` |
| `verification_reference` | verifier、rule/version、subject、status、limitations | `NOT_VERIFIED` |
| `accountability_reference` | EEOAP source/version/issuer status | `UNKNOWN_OR_UNSUPPORTED` |
| `evaluation_reference` | SAEE interface/version、scope、uncertainty、advisory status | `NO_FITNESS_CLAIM` |
| `decision_reference` | issuer、decision type、status、scope、validity | `NO_ADOPTION_OR_EXECUTION_CLAIM` |
| `revocation_reference` | issuer、reason category、effective time、successor | `NOT_CURRENT` |

## 6. Ownership Conflict Policy（权属冲突策略）

当两个来源声称拥有同一对象、版本或状态时：

1. 保留两个 source references；
2. 标记 `CONFLICTED`；
3. 不选择更新时间更新或状态更高的一方自动获胜；
4. 不生成 VEAP success；
5. 路由到对应 Domain Owner 与 Architecture Decision；
6. 在解决前保留 `NOT_ASSESSED` 或 `BLOCKED`。

```text
CONFLICT_AUTO_RESOLUTION=false
LATEST_TIMESTAMP_WINS=false
HIGHER_STATUS_WINS=false
COMMERCIAL_IMPLEMENTATION_WINS=false
```

## 7. Blocking Decisions（阻塞决定）

| Decision | Required resolution | Why it blocks |
|---|---|---|
| `CS-D01` | 接受/退回/拒绝 bounded problem-and-scope freeze | 当前连范围冻结都未获准 |
| `AF-D04` / `AF-D14` | EEOAP canonical document/version/issuer/claim vocabulary | VEAP 不能引用模糊 EEOAP Authority |
| `AF-D13` | SAEE public read-only contract | 防止 VEAP 伪造 Fitness 或越过 DBOS |
| `AF-D15` | TITMAS bounded Specification Authority | 确认谁能维护 VEAP profile |
| `AF-D16` | object ownership crosswalk | 禁止同名第二 canonical object |
| `DQ-003` | DBOS project-local source/status boundary | source/status/release/runtime truth 需分离 |

## 8. Pre-decision Recommendation（决定前建议）

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=PREDECISION_OWNER_BOUNDARY_REVIEW_INPUT
NOT_RECOMMENDED_AS=FROZEN_OWNER_ASSIGNMENT_OR_NORMATIVE_PROFILE
```

当前交叉表已经足以说明 VEAP 可拥有的最小候选表面和不可拥有的对象，但不足以授权规范
起草。下一步应由 Human Owner 决定 `CS-D01`，并由对应 Domain Owner 接受或修订自己的行。

## 9. Final State（最终状态）

```text
VEAP_CANONICAL_OWNERSHIP_CROSSWALK_DEFINED=true
VEAP_CANONICAL_OWNERSHIP_RECORDS=14
VEAP_OWNERSHIP_FROZEN=false
VEAP_SPECIFICATION_AUTHORITY_ASSIGNED=false
VEAP_DOMAIN_OWNER_ACCEPTANCES=0

CS_D01_DECIDED=false
AF_D15_DECIDED=false
AF_D16_DECIDED=false
EEOAP_CANONICAL_VERSION_OWNER_FROZEN=false
SAEE_PUBLIC_CONTRACT_FROZEN=false

NORMATIVE_PROFILE_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
EXTERNAL_ACTION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
```
