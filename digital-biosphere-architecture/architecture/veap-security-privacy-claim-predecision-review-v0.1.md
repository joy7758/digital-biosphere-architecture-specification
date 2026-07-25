---
document_id: DBA-TITMAS-VEAP-SECURITY-PRIVACY-CLAIM-PREDECISION-REVIEW-0.1
title: VEAP Security, Privacy and Claim Pre-decision Review v0.1
title_zh: VEAP 安全、隐私与声明决定前审查 v0.1
version: 0.1.0
status: review-input-prepared-formal-review-not-complete
maturity: Development
maturity_scope: entire-document
owner_ref: NOT_ASSIGNED
reviewer_ref: NOT_ASSIGNED
decision_reference: CS-D01_NOT_DECIDED
supersedes: NONE
superseded_by: NONE
compatibility_statement: "AI-assisted pre-decision risk review input only; no formal security/privacy review, implementation, certification, compliance, production safety, commercial availability, or customer compatibility claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: non-executable-security-privacy-claim-review-input
architecture_domain: TITMAS
primary_repository: digital-biosphere-architecture
review_input_prepared_at: 2026-07-25
risk_count: 16
open_risk_count: 16
formal_review_complete: false
implementation_authorized: false
authority_effect: none
---

# VEAP Security, Privacy and Claim Pre-decision Review v0.1

## 0. Verdict（结论）

本文件在任何 VEAP normative Profile、Schema 或实现出现前，识别执行证明包可能造成的
Security（安全）、Privacy（隐私）、Claim（公开声明）和 Authority（权力）风险。

```text
VEAP_SECURITY_PRIVACY_CLAIM_REVIEW_INPUT_PREPARED=true
VEAP_RISKS_REGISTERED=16
VEAP_OPEN_RISKS=16
VEAP_FORMAL_SECURITY_REVIEW_COMPLETE=false
VEAP_FORMAL_PRIVACY_REVIEW_COMPLETE=false
VEAP_FORMAL_CLAIM_REVIEW_COMPLETE=false
```

这是 AI-assisted risk discovery（智能体辅助风险发现），不是正式 Human Security Review、
Data Protection review、legal opinion、Certification 或生产安全证明。

机器入口：

- [risk register](veap-security-privacy-claim-risk-register.v0.1.json)；
- [risk register Schema](schemas/veap-security-privacy-claim-risk-register.schema.v0.1.json)。

### Source Basis（来源依据）

- [TITMAS Architecture Charter](titmas-architecture-charter-v0.1.md)；
- [TITMAS Review and Maintenance Model](titmas-review-and-maintenance-model-v0.1.md)；
- [VEAP Canonical Ownership Crosswalk](veap-canonical-ownership-crosswalk-v0.1.md)；
- [VEAP Pre-decision Conformance Design](veap-predecision-conformance-design-v0.1.md)；
- [VEAP Problem Validation Protocol](veap-problem-validation-protocol-v0.1.md)；
- [Commercialization Standards Roadmap](titmas-commercialization-standards-roadmap-v0.1.md)。

这些来源只提供当前边界和审查输入；它们不证明 control 已实现或风险已关闭。

## 1. Review Scope（审查范围）

审查的候选数据流：

```text
Runtime / Framework Observation
  -> DBOS Evidence Admission and canonical references
  -> Verification references
  -> bounded VEAP exchange envelope
  -> optional SAEE read-only evaluation reference
  -> authorized recipient
```

审查不假设此数据流已经实现，也不授权 collector、listener、database、network、key、
signature、Agent、Runtime、Evidence Object 或 external service。

## 2. Protected Assets（受保护资产）

- Agent/Entity/Runtime identity 与 binding status；
- execution、task、model、tool、policy references；
- timestamps、correlation IDs、digests 和 provenance；
- admitted/rejected/partial/failed Evidence references；
- verification rule、verifier、status 和 limitations；
- optional SAEE evaluation/recommendation references；
- tenant、organization、operator 和 human accountability metadata；
- revocation、supersession、incident 和 failure history。

证明包通常是 metadata-rich（元数据密集）的。即使不包含 prompt、response 或 tool payload，
identity、time、task 和 correlation 组合仍可能暴露组织结构、行为模式或敏感关系。

## 3. Data Classification and Minimization（数据分类与最小化）

### Default allowed as references only

- opaque、versioned IDs；
- source namespace/version；
- status、digest、time window；
- public policy/rule reference；
- explicit limitation、partial、unknown、failure 和 revocation。

### Default prohibited payload

- prompt、response、memory、tool input/output body；
- credential、secret、token、private key；
-未经授权的 PII、客户数据、受监管数据；
-完整代码、文件或数据库内容；
- 模型内部 chain-of-thought（思维链）；
- 未经授权的原始 telemetry payload。

需要内容时必须由独立 data policy 明确 purpose、legal/authorization basis、field allowlist、
redaction、tenant boundary、recipient、retention、deletion 和 incident route。VEAP Profile
不能因为“可验证”而自动扩大采集范围。

## 4. Threat and Misuse Register（威胁与误用台账）

### Security — 5

| ID | Risk | Required control | Current |
|---|---|---|---|
| `VEAP-SEC-001` | digest/reference 被替换或 canonical source 被伪造 | algorithm/version binding、source binding、tamper failure、no silent repair | `OPEN` |
| `VEAP-SEC-002` | replay/duplicate 被当作新的成功证明 | unique package ID、nonce/time policy、dedupe、replay status、immutable failure | `OPEN` |
| `VEAP-SEC-003` | 跨 tenant/entity 绑定造成数据或身份串线 | tenant/subject binding、authorization check、correlation conflict rejection | `OPEN` |
| `VEAP-SEC-004` | issuer/verifier key 或身份受损仍被信任 | issuer registry boundary、key status、revocation、validity interval、incident path | `OPEN` |
| `VEAP-SEC-005` | raw payload、credential、secret 或敏感内容进入包 | deny-by-default fields、allowlist、redaction、secret scanning、stop condition | `OPEN` |

### Privacy — 4

| ID | Risk | Required control | Current |
|---|---|---|---|
| `VEAP-PRIV-001` | 证明用途扩张为监控、画像或二次决策 | purpose binding、recipient scope、secondary-use prohibition | `OPEN` |
| `VEAP-PRIV-002` | 为“完整性”采集不必要内容 | reference-first、data minimization、field-level justification | `OPEN` |
| `VEAP-PRIV-003` | retention、withdrawal、deletion 与历史保留冲突 | class-based retention、tombstone/revocation、deletion proof、legal hold boundary | `OPEN` |
| `VEAP-PRIV-004` | 多个 pseudonymous reference 联结后重新识别主体 | linkability analysis、namespace separation、access control、public-safe extraction | `OPEN` |

### Claim — 5

| ID | Risk | Required control | Current |
|---|---|---|---|
| `VEAP-CLAIM-001` | Evidence/attestation 被称为 Truth 或结果正确 | mandatory limitation、forbidden claim test、public wording review | `OPEN` |
| `VEAP-CLAIM-002` | Verification PASS 被解释为 Permission/Authorization | non-elevation statement、decision reference requirement、negative case | `OPEN` |
| `VEAP-CLAIM-003` | Attestation 被销售为 Certificate/Certified Agent | certificate term ban、Certification Authority gate、marketing rejection | `OPEN` |
| `VEAP-CLAIM-004` | Schema/conformance PASS 被称为 production proven | maturity/evidence label、exact result scope、production claim ban | `OPEN` |
| `VEAP-CLAIM-005` | partial/sampled trace 被宣传为完整执行历史 | completeness status、sampling/drop propagation、unknown preservation | `OPEN` |

### Authority — 2

| ID | Risk | Required control | Current |
|---|---|---|---|
| `VEAP-AUTH-001` | VEAP 成为 DBOS/EEOAP/Verifier 的第二 canonical Owner | ownership crosswalk、opaque references、conflict fail-closed | `OPEN` |
| `VEAP-AUTH-002` | SAEE Evaluation/Recommendation 变成 Decision/Execution | advisory label、decision/authorization binding、no writeback | `OPEN` |

## 5. Required Failure Semantics（强制失败语义）

未来 Profile candidate 至少应支持：

```text
REJECTED_SOURCE
REJECTED_IDENTITY_BINDING
REJECTED_INTEGRITY
REPLAYED
CONFLICTED
PARTIAL
UNKNOWN
UNSUPPORTED_VERSION
REVOKED
EXPIRED
NOT_ASSESSED
BLOCKED_BY_DATA_POLICY
BLOCKED_BY_AUTHORIZATION
```

失败关闭不得删除原始 failure reference，也不能以 “best effort success” 填充缺失的 identity、
admission、verification 或 evaluation。

## 6. Claim Vocabulary（声明词汇）

### Allowed at current stage

> TITMAS is designing a bounded open profile candidate for evidence-backed execution
> attestations.

中文：

> TITMAS 正在设计一个有界、基于证据的执行证明开放 Profile 候选。

### Prohibited at current stage

- TITMAS-certified Agent；
- Trusted Execution Certificate；
- guaranteed correct/safe/compliant；
- complete execution truth；
- production proven；
- independently validated；
- customer adopted；
- commercially available；
- endorsed/adopted by OpenTelemetry、Microsoft、MCP 或 Agent frameworks。

公开材料必须同时显示 exact maturity、version、executed case count、known limitations 和
non-effects。

## 7. Required Reviewer Roles（所需审查角色）

正式推进至少需要相互区分的：

| Role | Required review | Does not gain |
|---|---|---|
| Security Reviewer | threat、tamper、replay、issuer、tenant、incident | Certification Authority |
| Privacy/Data Steward | purpose、classification、minimization、retention、deletion、recipient | legal conclusion |
| Claim Reviewer | public wording、maturity、evidence scope、misleading implication | release authority |
| DBOS Domain Owner | canonical Identity/Execution/Evidence/Verification references | TITMAS specification ownership |
| SAEE Domain Owner | read-only evaluation/recommendation reference | execution authority |
| TITMAS Specification Owner candidate | bounded profile scope/version/failure/claim vocabulary | DBOS/SAEE ownership |
| Human Architecture Decision Owner | accepts/returns/rejects exact scope | implementation by itself |

当前这些 VEAP-specific roles 均未指派。

## 8. Closure Requirements（关闭要求）

每个风险关闭必须包含：

```yaml
risk_id:
exact_profile_or_control_reference:
reviewer_ref:
reviewer_role_state: ASSIGNED
direct_evidence:
negative_case_reference:
residual_risk:
result: CLOSED|ACCEPTED_WITH_SCOPE|OPEN|BLOCKED
reviewed_at:
human_accountability_ref:
authority_effect: none
```

文档中存在 required control 不等于 control implemented。Schema valid、case designed 或
Agent recommendation 也不能关闭风险。

## 9. Gate Assessment（闸门评估）

```text
RISK_REGISTER_DEFINED=true
SECURITY_REVIEW_INPUT_PREPARED=true
PRIVACY_REVIEW_INPUT_PREPARED=true
CLAIM_REVIEW_INPUT_PREPARED=true

FORMAL_SECURITY_REVIEW_COMPLETE=false
FORMAL_PRIVACY_REVIEW_COMPLETE=false
FORMAL_CLAIM_REVIEW_COMPLETE=false
OPEN_RISKS=16
CLOSED_RISKS=0

CS_D01_HUMAN_DECISION_RECORDED=false
CS_G1_SCOPE_AUTHORITY_FREEZE_PASS=false
NORMATIVE_PROFILE_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
```

该风险输入可供 `CS-D01` Human Owner 决定是否允许 bounded problem/scope freeze；它不能
授权 Draft、Schema、实现、external validation 或商业服务。

## 10. Current State（当前状态）

```text
VEAP_SECURITY_PRIVACY_CLAIM_REVIEW_INPUT_PREPARED=true
VEAP_RISK_RECORDS=16
VEAP_OPEN_RISK_RECORDS=16
VEAP_CLOSED_RISK_RECORDS=0
VEAP_FORMAL_REVIEW_COMPLETE=false

VEAP_DATA_COLLECTION_AUTHORIZED=false
VEAP_NETWORK_PROCESSING_AUTHORIZED=false
VEAP_SECRET_OR_PII_PROCESSING_AUTHORIZED=false
VEAP_PUBLIC_CLAIM_AUTHORIZED=false
VEAP_CERTIFICATE_TERM_AUTHORIZED=false

AUTHORITY_CHANGED=false
OWNERSHIP_CHANGED=false
IMPLEMENTATION_AUTHORIZED=false
EXTERNAL_ACTION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
PRODUCTION_CLAIM_AUTHORIZED=false
```
