---
document_id: DBA-TITMAS-SPECIFICATION-CONTRIBUTION-FRAMEWORK-0.1
title: TITMAS Specification Contribution Framework v0.1
title_zh: TITMAS 规范贡献框架 v0.1
version: 0.1.0
status: specification-contribution-framework-candidate
maturity: Development
maturity_scope: entire-document
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Development document; no implementation compatibility claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: non-executable-specification-governance-candidate
architecture_domain: TITMAS
document_maturity: Development
owner_ref: NOT_ASSIGNED
decision_reference: NOT_DECIDED
public_contribution_enabled: false
community_established: false
maintainer_assigned: false
implementation_authorized: false
external_action_authorized: false
authority_effect: none
---

# TITMAS Specification Contribution Framework v0.1

中文：TITMAS 规范贡献框架 v0.1。

## 1. Purpose and Current Boundary（目的与当前边界）

本框架定义未来如何向 TITMAS 提出、审查和维护规范类贡献。它是 DBA 内的
Specification Community Ready Candidate（规范社区就绪候选）材料，不是公共贡献入口、
标准组织、正式社区、SIG、Maintainer 指派或实现授权。

```text
TITMAS_CONTRIBUTION_FRAMEWORK_DEFINED=true
TITMAS_PUBLIC_CONTRIBUTION_ENABLED=false
TITMAS_COMMUNITY_ESTABLISHED=false
TITMAS_SPECIFICATION_AUTHORITY_ACTIVE=false
TITMAS_IMPLEMENTATION_AUTHORIZED=false
```

权力边界保持：

```text
Digital Biosphere
  -> DBA: Program Governance and Architecture Authority
      -> TITMAS: proposed trusted interoperability architecture domain
          -> DBOS / evidence-layer ecosystem / SAEE boundaries
```

箭头表示治理和接口约束，不表示 TITMAS 获得 DBA、DBOS、SAEE 或连接项目的
Architecture、Operational、Evolution、Source、Status、Release 或 Truth Authority。

## 2. Contribution Philosophy（贡献理念）

TITMAS 参考以下成熟机制，但不复制其组织结构、品牌、法律地位或现有角色：

- [OpenTelemetry contribution entry](https://opentelemetry.io/docs/contributing/)：
  为首次贡献者提供清晰入口，并把文档、测试和实现反馈都视为有效贡献；
- [IETF Introduction](https://www.ietf.org/about/introduction/) 与
  [RFC 2026](https://www.rfc-editor.org/info/rfc2026/)：先形成可讨论的草案，再经过
  迭代审查、实现与互操作经验进入更高成熟状态；
- [W3C Process Document 2025](https://www.w3.org/policies/process/20250818/)：
  Draft 不等于认可，成熟度转换需要记录、审查和实现经验；
- [CNCF governance guidance](https://contribute.cncf.io/projects/best-practices/governance/)：
  治理文件必须准确描述现实角色与过程，不能把愿景写成已经存在的组织事实。

TITMAS 采用以下原则：

1. specification before implementation（规范先于实现）；
2. proposal before decision（提案先于决策）；
3. exact source and version（精确来源与版本）；
4. one canonical owner per object/scope/version（每个对象、范围和版本一个规范 Owner）；
5. positive、negative、unknown、unsupported 和 failure 全部可追溯；
6. 社区 Review 只构成输入，DBA Architecture Decision 才能采纳重大跨域规则；
7. 实现、符合性、采用、发布与生产状态分别记录；
8. Agent 可读入口必须显式暴露 current truth、non-goals 和 false effects。

## 3. Contribution Types（贡献类型）

以下 `Owner` 表示未来 artifact accountability（工件责任），不是当前 Authority 指派。
本文件创建时全部为 `NOT_ASSIGNED`。

| Type | Scope | Owner | Review Requirement | Initial Maturity |
|---|---|---|---|---|
| **Specification Contribution** | 术语、对象、字段、状态、版本、兼容、失败语义和规范性要求 | `NOT_ASSIGNED`；重大跨域采纳走 DBA Decision | Proposal、Architecture、affected Domain Owner、Compatibility；高风险时加 Security | `Development` |
| **Reference Implementation Contribution** | 可替换、非唯一、声明规范版本的最小实现候选 | `NOT_ASSIGNED`；不得由规范文本自动指定 | Specification binding、Security、Compatibility、independent conformance plan | `Development` |
| **Integration Contribution** | Framework、MCP、OpenTelemetry 或其他生态的 mapping、adapter contract、handoff | `NOT_ASSIGNED`；受影响 canonical Owner 保持不变 | Architecture、affected Domain Owner、Compatibility、Security/Privacy | `Development` |
| **Research Contribution** | 可复核的问题、方法、数据引用、分析、局限和研究反馈 | `NOT_ASSIGNED`；研究者不获得 Truth Authority | Method、source/provenance、ethics/privacy、reproducibility | `Development` |
| **Documentation Contribution** | 首次接触、教程、示例、术语、本地化和迁移说明 | `NOT_ASSIGNED` | factual/source、link、terminology、accessibility/localization | `Development` |

任何 Contribution Type 都不能单独产生：

```text
AUTHORITY=false
PERMISSION=false
TRUTH=false
ADOPTION=false
RELEASE=false
IMPLEMENTATION_AUTHORIZATION=false
```

## 4. Required Contribution Record（必需贡献记录）

每项贡献至少声明：

```yaml
proposal_id:
contribution_type:
title:
problem_statement:
scope:
non_goals:
proposer_ref:
contributor_type: HUMAN|GOVERNED_AGENT|HUMAN_WITH_AGENT_ASSISTANCE
human_accountability_ref:
agent_or_tool_ref:
canonical_source_refs: []
affected_authority_domains: []
owner_ref: NOT_ASSIGNED
required_reviews: []
document_status: Draft
document_maturity: Development
compatibility_statement:
security_privacy_statement:
known_unknowns: []
decision_reference: NOT_DECIDED
implementation_authorization_reference: NOT_AUTHORIZED
```

详细填写方式使用
[TITMAS Contribution Proposal Template](titmas-contribution-proposal-template-v0.1.md)。

## 5. Ownership and Review Routing（所有权与审查路由）

- DBA 维护项目群架构规则、边界、ADR 与人工决策路径；
- TITMAS 只能在未来明确委托后维护有界 interoperability specification；
- DBOS 保持 Identity、Capability、Execution、Evidence、Verification 与 Lifecycle 的
  canonical operational boundary；
- SAEE 保持 Evaluation、Fitness、Risk、Stability、Adaptation 与 Evolution Recommendation
  的受保护演化域；
- evidence-layer ecosystem 只能提供有来源的 package、mapping、receipt 或 candidate
  material，不成为 DBOS Evidence Truth；
- 外部规范的 mapping 不取得外部标准的维护或解释权。

Owner 缺失、冲突或未冻结时：

```text
CONTRIBUTION_STATE=REVIEW_BLOCKED
ADOPTION_ALLOWED=false
IMPLEMENTATION_ALLOWED=false
```

## 6. Maturity and State Separation（成熟度与状态分离）

每项贡献必须分别记录：

```text
proposal_lifecycle_stage=
document_status=
document_maturity=
review_status=
decision_status=
implementation_status=
conformance_status=
adoption_status=
release_status=
community_status=
```

这些字段不能互相推导。完整文档成熟度继续遵循
[TITMAS Document Maturity Policy](titmas-document-maturity-policy-v0.1.md)。

## 7. Prohibited Elevations（禁止抬升）

```text
EXPERIMENTAL_NE_STANDARD=true
MAPPING_NE_ADOPTION=true
IMPLEMENTATION_NE_SPECIFICATION=true
CONFORMANCE_NE_CERTIFICATION=true
VALIDATOR_NE_AUTHORIZATION=true
EVIDENCE_NE_TRUTH=true
COMMUNITY_REVIEW_NE_ARCHITECTURE_DECISION=true
MAINTAINER_REVIEW_NE_RELEASE_AUTHORIZATION=true
```

## 8. Pre-development Agent Recommendation（开发前智能体推荐）

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=SPECIFICATION_AND_INTEROPERABILITY_CONTRIBUTION_CANDIDATE
NOT_RECOMMENDED_AS=ESTABLISHED_COMMUNITY_STANDARD_OR_IMPLEMENTATION
```

条件限制：Authority Freeze 尚未采纳、Specification Owner 未指派、公共贡献未授权、
Security Disclosure 路径和正式 Code of Conduct 未建立、无 Maintainer、无真实外部采用
证据。C2 只减少流程歧义，不关闭这些缺口。

## 9. Current Result（当前结果）

```text
TITMAS_CONTRIBUTION_FRAMEWORK_DEFINED=true
TITMAS_SPECIFICATION_PROCESS_DEFINED=true
TITMAS_PUBLIC_CONTRIBUTION_ENABLED=false
TITMAS_COMMUNITY_ESTABLISHED=false
TITMAS_SPECIFICATION_AUTHORITY_ACTIVE=false
TITMAS_MAINTAINER_ASSIGNED=false
TITMAS_SIG_CREATED=false
TITMAS_IMPLEMENTATION_AUTHORIZED=false
TITMAS_EXTERNAL_ACTION_AUTHORIZED=false
```
