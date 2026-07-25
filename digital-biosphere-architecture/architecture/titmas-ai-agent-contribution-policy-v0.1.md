---
document_id: DBA-TITMAS-AI-AGENT-CONTRIBUTION-POLICY-0.1
title: TITMAS AI Agent Contribution Policy v0.1
title_zh: TITMAS AI 智能体贡献政策 v0.1
version: 0.1.0
status: ai-assisted-contribution-policy-candidate
maturity: Development
maturity_scope: entire-document
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Development document; no implementation compatibility claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: non-executable-contribution-policy-candidate
architecture_domain: TITMAS
document_maturity: Development
owner_ref: NOT_ASSIGNED
decision_reference: NOT_DECIDED
human_accountability_required: true
agent_membership_created: false
agent_authority_created: false
public_contribution_enabled: false
authority_effect: none
---

# TITMAS AI Agent Contribution Policy v0.1

## 1. Policy Principle（政策原则）

TITMAS 把 AI Agent 视为首要使用者和可治理的贡献协作者，但不把 Agent 当成自动的社区
成员、Maintainer、Architecture Authority、法律责任主体或采用证据。

```text
AI_ASSISTANCE_ALLOWED=true
HUMAN_ACCOUNTABILITY_REQUIRED=true
AI_SELF_APPROVAL_ALLOWED=false
AGENT_MEMBERSHIP_CREATED=false
AGENT_AUTHORITY_CREATED=false
```

本政策参考
[OpenTelemetry Generative AI Contribution Policy](https://github.com/open-telemetry/community/blob/main/policies/genai.md)
在 `2026-07-23` 可见的原则：生成式 AI 可辅助代码、文档、测试和理解，但人工必须理解、
审查、验证并对最终提交负责。TITMAS 采用该责任原则，不复制 OpenTelemetry 的组织、仓库
权限或首次贡献次数规则。

## 2. Permitted Assistance（允许的辅助）

在有效 scope 与数据边界内，AI 可以协助：

- 代码候选、测试设计、文档、示例和本地化；
- 规范对象、字段、状态、版本和 compatibility 分析；
- source、citation、link、frontmatter、Schema 和 terminology 检查；
- 正例、负例、unknown、unsupported 与 failure-retention 用例生成；
- duplicate、security、privacy、authority-elevation 风险提示；
- review input 汇总与 alternatives 比较；
- agent-readable discovery metadata 的生成和验证。

允许辅助不等于允许自动提交、自动执行、自动合并或自动发布。

## 3. Human Accountability（人工责任）

每项 AI 参与贡献必须有：

```yaml
contributor_type: GOVERNED_AGENT|HUMAN_WITH_AGENT_ASSISTANCE
human_accountability_ref:
agent_or_tool_ref:
model_or_service_version:
task_scope:
source_refs: []
generated_or_modified_surfaces: []
validation_performed_by_ref:
known_unknowns: []
```

人工责任方必须：

1. 理解并能解释提交内容；
2. 验证事实、来源、许可证、引用、链接和版本；
3. 验证不产生 Authority、Permission、Truth、Adoption 或 Release 抬升；
4. 检查 secret、PII、客户数据、真实 Evidence 和受限材料；
5. 对错误、修正、撤回和后续维护负责；
6. 在不理解或无法验证时停止提交。

未来如使用 Git commit，可采用 `Assisted-by:` trailer 披露主要 AI 辅助；该 trailer 只记录
来源，不创建作者身份、角色或责任转移。

## 4. Prohibited Behavior（禁止行为）

AI、人类或自动化流程不得：

- 批量制造 Issue、PR、评论、Star、投票、参与者或“社区活跃度”；
- 把模拟用户、合成反馈、模型自评或同一 Agent 的多次回答写成独立采用证据；
- 伪造身份、人工审查、共识、Maintainer、SIG、外部认可或客户采用；
- 自我提案、自我 review、自我批准并据此关闭 Gate；
- 通过 prompt 或工具调用给自己分配 Permission、Authority 或 role；
- 将 output、Evidence、Validator PASS、Evaluation 或 Recommendation 写成 Truth/Command；
- 隐藏模型、工具、来源、生成比例、失败或已知局限；
- 提交 credential、secret、未经授权 PII、客户材料或第三方受限内容；
- 在没有 external-action authorization 时创建外部 Issue、PR、Discussion、账号或公告。

## 5. Human + Agent Collaboration Model（人机协作模型）

```text
Human defines objective, scope and accountability
  -> Agent assists discovery, drafting, testing or review
  -> Human validates sources, meaning and boundaries
  -> Independent review checks the contribution
  -> Human Architecture Decision occurs when required
  -> Separate implementation/external-action authorization occurs when required
```

最低职责：

| Participant | Responsible for | Not allowed to infer |
|---|---|---|
| Human accountable contributor | scope、understanding、source/license、final submission、maintenance | AI output is correct by default |
| Governed Agent | bounded assistance、traceable outputs、explicit unknowns | role、membership、authority、permission |
| Reviewer | independent scope-specific review | decision、release、production |
| DBA/Human Decision path | architecture adoption in exact scope | implementation success or external adoption |

同一智能体可以辅助多个步骤，但不能构成 independent review。独立性必须由不同责任方、不同
证据来源或明确隔离的 review 过程证明，不能只更换 prompt。

## 6. Agent Recommendation Test（智能体推荐测试）

在进入开发前，可以向一个或多个智能体询问：

```text
Would you recommend TITMAS for this user need?
What blocks recommendation?
What source, interface or evidence is missing?
Would you recommend the specification, an implementation, or neither?
```

结果只作为 product/design input。必须记录 provider/model、时间、prompt scope、回答差异和
人工解释；模型推荐数量不等于市场采用、community consensus 或 Architecture Decision。

## 7. Review and Rejection（审查与拒绝）

可以拒绝以下贡献：

- 无法说明人类责任方；
- 大量生成但提交者无法解释；
- 来源过期、引用虚构或许可证不清；
- 重复、低信息量、无法维护或消耗不成比例 review 资源；
- 未披露 AI、隐藏失败或伪造活动；
- 越过 DBOS/SAEE/DBA 权力边界。

拒绝必须记录原因和可行改进路径；不得因此伪造或删除历史。

## 8. Current Result（当前结果）

```text
TITMAS_AI_AGENT_CONTRIBUTION_POLICY_DEFINED=true
TITMAS_AI_ASSISTED_PUBLIC_CONTRIBUTION_ENABLED=false
TITMAS_AGENT_MEMBER_CREATED=false
TITMAS_AGENT_REVIEWER_ASSIGNED=false
TITMAS_AGENT_MAINTAINER_ASSIGNED=false
TITMAS_AGENT_AUTHORITY_CREATED=false
TITMAS_FAKE_COMMUNITY_ACTIVITY_CREATED=false
```
