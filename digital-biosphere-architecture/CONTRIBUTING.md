---
document_id: DBA-TITMAS-CONTRIBUTOR-GUIDE-0.1
title: TITMAS Infrastructure Developer Community Contributor Guide v0.1
title_zh: TITMAS 可信多智能体基础设施开发者社区贡献者指南 v0.1
status: contributor-entry-prepared-not-publicly-authorized
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
document_type: non-executable-contributor-entry
architecture_domain: TITMAS
community_state: CONTRIBUTOR_ENTRY_PREPARED
public_contribution_surface_authorized: false
community_established: false
maintainer_assigned: false
external_action_authorized: false
implementation_authorized: false
runtime_effect: none
authority_effect: none
---

# Contributing to TITMAS Infrastructure Developer Community

中文：参与 TITMAS 可信多智能体基础设施开发者社区。

> You build agents. TITMAS helps them collaborate through understandable,
> implementable, and verifiable infrastructure rules.

中文：开发者负责构建 Agent；TITMAS 提供易理解、可实现、可验证的基础设施规则，帮助
不同 Agent 可信协作。

TITMAS 当前是 Digital Biosphere Architecture（DBA）中的 proposed interoperability
architecture domain（拟议互操作架构域）和已采纳的基础设施开发者社区方向。贡献入口已经
准备，但公共贡献表面、社区、SIG、Maintainer、独立仓库和外部招募均未获授权。

```text
TITMAS_IS_AGENT_FRAMEWORK=false
TITMAS_IS_AGENT_PLATFORM=false
TITMAS_IS_FOUNDATION=false
TITMAS_CREATES_AGENTS=false
TITMAS_PUBLIC_CONTRIBUTION_SURFACE_AUTHORIZED=false
```

## 1. Before You Contribute（贡献前）

人类开发者和智能体必须依次读取：

1. [`AGENTS.md`](AGENTS.md)；
2. [`PROGRAM-CHARTER.md`](PROGRAM-CHARTER.md)；
3. [`PROGRAM-STATUS.md`](PROGRAM-STATUS.md)；
4. [`DECISION-QUEUE.md`](DECISION-QUEUE.md)；
5. [`RISK-AND-BLOCKER-REGISTER.md`](RISK-AND-BLOCKER-REGISTER.md)；
6. [`INTEGRATION-GATES.md`](INTEGRATION-GATES.md)；
7. [TITMAS 社区战略](architecture/titmas-infrastructure-developer-community-strategy-v0.1.md)；
8. [TITMAS 贡献者角色模型](architecture/titmas-contributor-role-model-v0.1.md)；
9. [TITMAS 文档成熟度政策](architecture/titmas-document-maturity-policy-v0.1.md)。

首次贡献必须能用自己的话回答：

- TITMAS 解决什么基础设施问题；
- TITMAS 与 DBA、DBOS、SAEE、Agent Framework 和 OpenTelemetry 的区别；
- 当前变更属于 Specification、Mapping、Adapter Contract、Conformance、Documentation、
  Security/Privacy 还是 Reference Candidate；
- 该变更不会产生哪些 Authority、Permission、Truth、Runtime 或 Release 事实。

## 2. What You Can Prepare Now（当前可准备内容）

当前允许在 DBA 工作树内准备：

- 术语澄清、交叉引用、首次接触说明和中英文一致性；
- 规范字段、对象所有权、状态、版本、兼容和失败语义的 Proposal；
- 外部规范到 TITMAS/TMAP 的版本钉住 mapping candidate；
- 正例、负例、unknown、unsupported 和 failure-retention 的测试设计；
- 机器可读发现入口、Schema candidate、文档和本地化；
- 安全、隐私、供应链和 semantic non-elevation（语义不抬升）分析。

当前不得：

- 创建 Agent、Runtime、Entity、Capability 或 Permission 实例；
- 创建或修改 DBOS/SAEE 运行事实；
- 将 Proposal、Review、模型输出或投票写成 Architecture Decision；
- 新建外部 Issue、Pull Request、Discussion、组织、SIG、会议或招募渠道；
- 宣称 TITMAS Interface、实现、符合性、社区、采用或生产状态已经建立。

[Good First Contribution 候选清单](architecture/titmas-good-first-contribution-catalog-v0.1.md)
只提供本地准备题目，不是公开 Issue，也不表示任务已分配。

## 3. Contribution Workflow（贡献流程）

```text
Understand the cockpit and current truth
  → Select one bounded contribution surface
  → Fill a Contribution Proposal
  → Source, scope and authority review
  → Draft with explicit maturity
  → Technical and domain review
  → Human Architecture Decision when required
  → Versioned documentation update
  → Separate implementation authorization, if any
  → Independent conformance evidence, if any
```

使用
[Contribution Proposal Template](architecture/titmas-contribution-proposal-template-v0.1.md)。
小型拼写或失效链接修复可以缩减说明，但仍必须保持来源、边界和当前事实。

`Review ≠ Decision`，`Decision ≠ Implementation`，`Conformance ≠ Adoption`。

## 4. Human and Agent Contributions（人类与智能体贡献）

TITMAS 把 AI agent 视为首要使用者和可治理贡献参与者，但智能体不是自动的项目成员、
Maintainer、Architecture Authority 或法律责任主体。

每项贡献必须声明：

```text
contributor_type=HUMAN|GOVERNED_AGENT|HUMAN_WITH_AGENT_ASSISTANCE
human_accountability_ref=
agent_or_tool_ref=
source_refs=
verification_performed_by_ref=
known_unknowns=
```

规则：

- AI 参与必须披露；不得伪装成人工原创或隐藏来源；
- 提交者必须能理解、审查和解释所提交内容；
- 智能体输出必须经过来源、事实、链接、边界和负例验证；
- 智能体不能自我批准、自我授予角色或用自己的评价关闭 Gate；
- 涉及 Authority、Release、External Action、License、Security Disclosure 或
  implementation authorization 时，必须保留明确人工决定。

## 5. Review and Decision Boundaries（审查与决策边界）

当前没有已经指派的 TITMAS Maintainer、Reviewer、Triager 或 SIG。候选角色及其未来进入
条件见[角色模型](architecture/titmas-contributor-role-model-v0.1.md)。

在角色正式获准前：

- `zhangbin` 仍是 Human Program Owner，不因此自动成为 TITMAS Maintainer；
- DBA Architecture Decision 仍是重大架构变化的采纳路径；
- DBOS Domain Owner 对 DBOS canonical fact 负责；
- SAEE Domain Owner 对 SAEE evaluation model 负责；
- 社区意见、智能体推荐和贡献数量只构成 review input。

## 6. Maturity, Version and Evidence（成熟度、版本与证据）

每个新增或修改的规范文档必须声明独立 maturity。无声明时按 `Development` 处理。
成熟度不能从一个文档传播到整个 TITMAS，也不能从规范传播到实现。

每个未来实现必须声明：

- 实现的 TITMAS/TMAP 规范版本；
- supported、partial、unsupported 和 unknown；
- 实现版本、环境与已执行的 conformance cases；
- 已知限制和 breaking change；
- 不能从 PASS 推导出的 Authority、Permission、Truth 或 Adoption。

完整规则见[文档成熟度政策](architecture/titmas-document-maturity-policy-v0.1.md)。

## 7. Conduct and Safety（行为与安全）

公共贡献表面启用前，必须采纳正式 Code of Conduct、Conflict of Interest 和 Security
Disclosure 路径。目前仅有
[Community Conduct Candidate](architecture/titmas-community-conduct-candidate-v0.1.md)，
尚未形成公共报告渠道或执行机构。

不得在贡献中提交：

- credential、secret、token、私钥或账户信息；
- 未经授权的 PII、客户数据、真实 Evidence 或受限研究数据；
- 第三方受限代码、文本、商标或许可证不兼容材料；
- 能被误认为生产凭据、Permission、Registration 或 Release Authorization 的样例。

发现潜在安全问题时，不要创建公开漏洞细节；当前
`SECURITY_DISCLOSURE_PATH_ASSIGNED=false`，应停止外部动作并请求 DBA 明确安全接收路径。

## 8. Current Status（当前状态）

```text
TITMAS_CONTRIBUTOR_ENTRY_PREPARED=true
TITMAS_CONTRIBUTOR_GUIDE_CREATED=true
TITMAS_PUBLIC_CONTRIBUTION_SURFACE_AUTHORIZED=false
TITMAS_GOOD_FIRST_ISSUES_CREATED=false
TITMAS_CODE_OF_CONDUCT_ADOPTED=false
TITMAS_MAINTAINER_ASSIGNED=false
TITMAS_SIG_CREATED=false
TITMAS_COMMUNITY_ESTABLISHED=false
TITMAS_IMPLEMENTATION_AUTHORIZED=false
TITMAS_EXTERNAL_ACTION_AUTHORIZED=false
```
