---
document_id: DBA-TITMAS-GOVERNANCE-ACTIVATION-REVIEW-0.1
title: TITMAS Governance Activation Review v0.1
title_zh: TITMAS 治理激活审查 v0.1
version: 0.1.0
phase: C2.5
status: governance-activation-candidate-not-ready
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
document_type: non-executable-governance-decision-candidate
architecture_domain: TITMAS
assessed_at: 2026-07-23
governance_activation_ready: false
governance_activated: false
authority_assigned: false
public_contribution_authorized: false
maintainer_assigned: false
external_action_authorized: false
authority_effect: none
---

# TITMAS Governance Activation Review v0.1

## 1. Verdict（结论）

```text
PHASE=C2_5_GOVERNANCE_ACTIVATION
GOVERNANCE_ACTIVATION_REVIEW_DEFINED=true
GOVERNANCE_ACTIVATION_READY=false
GOVERNANCE_ACTIVATED=false
NEXT_ACTION=HUMAN_ARCHITECTURE_DECISION
```

本文件把治理激活所需决定整理为一个失败关闭的候选包，不激活 Authority、Registry、
Owner、Maintainer、安全渠道、行为规范或公共贡献。

## 2. Permanent Architecture Boundary（永久架构边界）

```text
Digital Biosphere
  -> DBA: Architecture and Program Governance Authority
      -> TITMAS: trusted interoperability architecture domain
          -> DBOS: canonical record boundary
          -> Agent Evidence Family: evidence ecosystem
          -> EEOAP: accountability specification
          -> SAEE: protected evolution intelligence
          -> ARO/PRA: bounded review runtime
```

TITMAS 只能维护未来被 DBA 明确委托的 interoperability specification。它不取得 connected
project 的 Source、Status、Release、Operational、Evolution、Truth 或 Ownership。

## 3. Specification Authority Candidate（规范权威候选）

建议候选：

```yaml
authority_type: BOUNDED_SPECIFICATION_AUTHORITY
authority_holder_ref: NOT_ASSIGNED
governing_authority_ref: DBA_HUMAN_ARCHITECTURE_DECISION
scope:
  - TITMAS_INTEROPERABILITY_PROFILE
  - TITMAS_ADAPTER_CONTRACT
  - TITMAS_CONFORMANCE_VOCABULARY
excluded_scope:
  - DBA_PROGRAM_ARCHITECTURE
  - DBOS_CANONICAL_RECORDS
  - EEOAP_NORMATIVE_OWNERSHIP
  - SAEE_EVALUATION_ALGORITHM
  - EXTERNAL_STANDARD_INTERPRETATION
term: NOT_DECIDED
review_due_at: NOT_DECIDED
revocation_rule: REQUIRED_NOT_DECIDED
decision_reference: NOT_DECIDED
```

激活前必须解决 object ownership crosswalk、DBA 委托范围、有效期、撤销、冲突和替代
Owner。当前：

```text
TITMAS_SPECIFICATION_AUTHORITY_ACTIVE=false
```

## 4. Number Registry Authority Candidate（编号注册权候选）

Number Registry 只分配 `TITMAS-NNNN` lineage identifier，不决定 maturity、adoption、
implementation 或 standard status。

最低候选字段：

```yaml
registry_source_ref: NOT_CREATED
registry_issuer_ref: NOT_ASSIGNED
registry_reviewer_ref: NOT_ASSIGNED
allocation_policy_ref: titmas-rfc-numbering-and-document-model-v0.1.md
conflict_policy: FAIL_CLOSED_NO_REUSE
retirement_policy: RETAIN_HISTORY
decision_reference: NOT_DECIDED
```

当前不创建 Registry 文件、服务或自动编号器：

```text
TITMAS_NUMBER_REGISTRY_CREATED=false
TITMAS_NUMBER_REGISTRY_AUTHORITY_ASSIGNED=false
TITMAS_NUMBERS_ASSIGNED=0
```

## 5. Owner Separation（Owner 分离）

| Role | Future responsibility | Explicit exclusion | Current state |
|---|---|---|---|
| Specification Owner | normative text、version、compatibility、errata | implementation source、commercial service、DBOS/SAEE facts | `NOT_ASSIGNED` |
| Implementation Owner | exact source、build、release、security fixes | normative specification、conformance verdict | `NOT_ASSIGNED` |
| Maintainer | bounded scope intake、review routing、maintenance | DBA Decision、DBOS/SAEE Authority、commercial commitment | `NOT_ASSIGNED` |
| Conformance Reviewer | version-bound cases/result review | certification、permission、truth | `NOT_ASSIGNED` |
| Commercial Offering Owner | future service scope、support、contract delivery | specification ownership、community role | `NOT_ASSIGNED` |

同一人未来可承担多个角色，但每个角色必须有独立 scope、Decision、Conflict of Interest 和
recusal 规则。一个账号或仓库权限不能证明多个 Owner 身份。

## 6. Security Disclosure Path Candidate（安全披露路径候选）

设计流程：

```text
Confidential Intake
  -> Acknowledgement
  -> Severity and Scope Triage
  -> Affected Owner Routing
  -> Containment / Fix Candidate
  -> Coordinated Disclosure Decision
  -> Public Advisory when authorized
  -> Retention and Postmortem
```

激活前必须填写：

```yaml
confidential_contact: NOT_ASSIGNED
primary_response_owner_ref: NOT_ASSIGNED
backup_response_owner_ref: NOT_ASSIGNED
acknowledgement_target: NOT_DECIDED
severity_policy_ref: NOT_DECIDED
retention_privacy_policy_ref: NOT_DECIDED
embargo_and_disclosure_policy_ref: NOT_DECIDED
appeal_path_ref: NOT_DECIDED
```

不得使用普通公开 Issue 接收未修复漏洞。当前：

```text
TITMAS_SECURITY_DISCLOSURE_PATH_ASSIGNED=false
```

## 7. Code of Conduct Readiness（行为规范就绪）

[Community Conduct Candidate](titmas-community-conduct-candidate-v0.1.md) 已描述期望行为，
但 reporting channel、response body、recusal、privacy、appeal 和 enforcement 均未激活。

```text
TITMAS_CODE_OF_CONDUCT_CANDIDATE_AVAILABLE=true
TITMAS_CODE_OF_CONDUCT_ADOPTED=false
TITMAS_CONDUCT_ENFORCEMENT_READY=false
```

## 8. Public Contribution Gate（公共贡献闸门）

只有以下全部为真，才能提交 `DQ-026` 的授权决定：

- [ ] Authority Freeze 已采纳；
- [ ] Specification/Registry/Review Owner 已明确；
- [ ] license、IPR 和 CLA/DCO 路线已决定；
- [ ] 正式 Code of Conduct 与执行路径已采纳；
- [ ] Security Disclosure、privacy、retention 和 appeal 路径可用；
- [ ] public surface、rollback、moderation 和 external-action scope 明确；
- [ ] agent-assisted contribution disclosure 已纳入入口；
- [ ] Human Architecture Decision 明确授权 exact surface。

```text
TITMAS_PUBLIC_CONTRIBUTION_GATE_PASSED=false
TITMAS_PUBLIC_CONTRIBUTION_SURFACE_AUTHORIZED=false
```

## 9. Decision Candidates（人工决定候选）

| ID | Candidate decision | Current result |
|---|---|---|
| `GA-D01` | 是否委托 TITMAS bounded Specification Authority | `NOT_DECIDED` |
| `GA-D02` | 是否建立并指派 Number Registry Authority | `NOT_DECIDED` |
| `GA-D03` | 是否采纳 Specification/Implementation/Maintainer 分离模型 | `NOT_DECIDED` |
| `GA-D04` | 是否建立可运行的 confidential Security Disclosure path | `NOT_DECIDED` |
| `GA-D05` | 是否采纳正式 Code of Conduct 与执行/申诉机制 | `NOT_DECIDED` |
| `GA-D06` | 是否授权 exact public contribution surface | `NOT_DECIDED` |

接受任一决定都不自动接受其余决定，也不自动创建账号、仓库、渠道或权限。

## 10. Final State（最终状态）

```text
GOVERNANCE_ACTIVATION_READY=false
TITMAS_GOVERNANCE_READY=false
TITMAS_SPECIFICATION_AUTHORITY_ACTIVE=false
TITMAS_NUMBER_REGISTRY_AUTHORITY_ASSIGNED=false
TITMAS_SECURITY_DISCLOSURE_PATH_ASSIGNED=false
TITMAS_CODE_OF_CONDUCT_ADOPTED=false
TITMAS_PUBLIC_CONTRIBUTION_SURFACE_AUTHORIZED=false
TITMAS_MAINTAINER_ASSIGNED=false
AUTHORITY_EFFECT=NONE
```
