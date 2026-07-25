---
document_id: DBA-TITMAS-VEAP-PROBLEM-VALIDATION-PROTOCOL-0.1
title: VEAP Problem Validation Protocol v0.1
title_zh: VEAP 问题验证协议 v0.1
version: 0.1.0
status: protocol-defined-execution-not-authorized
maturity: Development
maturity_scope: entire-document
owner_ref: NOT_ASSIGNED
decision_reference: CS-D01_NOT_DECIDED
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Pre-decision validation protocol only; no outreach, participant enrollment, market validation, product, implementation, commercial availability, or customer compatibility claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: non-executable-market-problem-validation-protocol
architecture_domain: TITMAS
primary_repository: digital-biosphere-architecture
defined_at: 2026-07-25
protocol_defined: true
validation_execution_authorized: false
external_outreach_authorized: false
valid_problem_records: 0
cs_g0_pass: false
authority_effect: none
---

# VEAP Problem Validation Protocol v0.1

## 0. Verdict（结论）

本协议把 “Agent Execution Accountability（智能体执行责任链）是否是值得优先标准化的
真实问题” 转化为可归因、可失败关闭的记录契约。

```text
VEAP_PROBLEM_VALIDATION_PROTOCOL_DEFINED=true
VEAP_PROBLEM_VALIDATION_EXECUTION_AUTHORIZED=false
VEAP_EXTERNAL_OUTREACH_AUTHORIZED=false
VEAP_VALID_PROBLEM_RECORDS=0
CS_G0_PROBLEM_FREEZE_PASS=false
```

协议定义不等于市场验证。现有 API Agent review 是 advisory evidence（建议证据），不能
伪装为独立组织、采购、客户采用或付费意愿。

机器入口：

- [problem-validation contract](veap-problem-validation-contract.v0.1.json)；
- [contract Schema](schemas/veap-problem-validation-contract.schema.v0.1.json)。

### Source Basis（来源依据）

- [TITMAS Adoption Validation Framework](titmas-adoption-validation-framework-v0.1.md)；
- [Commercialization Standards Roadmap](titmas-commercialization-standards-roadmap-v0.1.md)；
- [CS-D01 Agent Customer Review](../TITMAS-CS-D01-AGENT-CUSTOMER-REVIEW.md)；
- [VEAP Canonical Ownership Crosswalk](veap-canonical-ownership-crosswalk-v0.1.md)；
- [VEAP Pre-decision Conformance Design](veap-predecision-conformance-design-v0.1.md)。

本协议细化这些来源，不改变其 Authority、状态或执行授权。

## 1. Validation Question（验证问题）

核心问题：

> 对长期运行、跨框架或多智能体系统的实际责任方，是否经常出现“无法从有来源、版本、
> 完整性和失败语义的材料中证明谁做了什么”的高优先级问题？

验证对象是 problem（问题），不是 VEAP 名称、字段设计或购买意愿。受访者可以认可问题
但拒绝 VEAP，也可以认为现有 OpenTelemetry、audit log、SIEM、workflow history 或人工
流程已经足够。

## 2. Valid Observer Classes（有效观察者类别）

| Class | Acceptable basis | Does not prove |
|---|---|---|
| `ENTERPRISE_AI_INFRA_OWNER` | 对实际 Agent infrastructure、上线或治理负责 | 企业采购 |
| `AGENT_FRAMEWORK_OPERATOR` | 维护真实 framework/runtime workflow | framework 采用 TITMAS |
| `SECURITY_RISK_AUDIT_PRACTITIONER` | 审查实际 AI execution/accountability risk | 合规认可 |
| `REGULATED_DOMAIN_TECH_OWNER` | 管理有监督或受监管技术流程 | 法律结论 |
| `FRAMEWORK_OR_TOOL_PROVIDER` | 维护 Agent、telemetry、evidence 或 verification 工具 | upstream endorsement |
| `GOVERNED_AI_AGENT` | 有 exact model/tool/source trace 与独立人工责任上下文 | 独立组织记录 |

Agent-native observation 可以证明可发现性、理解成本和建议倾向；除非绑定一个真实独立
组织问题、人工责任方和近期实例，否则不能计入 `CS-G0` 的独立问题记录。

## 3. Independence Contract（独立性契约）

有效记录必须满足：

1. `observer_ref` 可归因但公共输出可 pseudonymous（假名化）；
2. `organization_or_context_ref` 可验证且与作者上下文区分；
3. `independence_basis` 说明为何不是同一维护者、同一 prompt 或同一组织的重复回答；
4. 同一组织的多个回答默认只计一个独立记录，除非责任域和实例确实独立；
5. 同一模型切换 persona、temperature、prompt 或 provider route 不增加组织独立性；
6. 由 TITMAS 作者提供答案、诱导措辞或事后补写实例的记录无效；
7. 委托 Agent 必须披露 model、tool、source material 与 human accountability reference。

```text
MODEL_SESSION_NE_INDEPENDENT_ORGANIZATION=true
MULTIPLE_PROMPTS_NE_MULTIPLE_CUSTOMERS=true
POLITE_INTEREST_NE_PROBLEM_EVIDENCE=true
```

## 4. Neutral Interview Flow（中立验证流程）

### Phase A — Context before solution

在展示 TITMAS 或 VEAP 前询问：

1. 当前运行或计划运行哪些 Agent/framework，持续时间和责任方是什么？
2. 最近一次无法回答“谁做了什么、为何做、依据和结果是什么”发生在哪里？
3. 当时哪些记录存在，哪些缺失，谁负责拼接？
4. 问题造成了什么可观察的时间、运营、安全、审查或交付成本？

### Phase B — Current workaround

5. 当前使用什么日志、trace、workflow history、SIEM、database 或人工流程？
6. 现有方案在哪些 source/version、identity continuity、failure、replay、retention 或
   verification 环节不足？
7. 如果未来六个月不解决，会发生什么？是否可以接受？

### Phase C — Priority without selling

8. 在当前待办中，该问题是 `HIGH`、`MEDIUM`、`LOW` 还是 `NONE`？为什么？
9. 哪种替代方案最可能优先采用？
10. 哪些条件会使其拒绝新的开放 contract？

### Phase D — Optional concept reaction

只有 A–C 完成后，才可展示 bounded VEAP concept，并询问：

11. 是否愿意评审开放 contract 或最小闭环？
12. 哪个字段、边界、风险或术语会阻止继续？

`VEAP` 反应不得回填或提升此前的问题优先级。

## 5. Problem Record Contract（问题记录契约）

每条记录至少包含：

```yaml
record_id:
observed_at:
observer_class:
observer_ref:
organization_or_context_ref:
independence_basis:
human_accountability_ref:
agent_assistance:
  used:
  model_or_tool_refs: []
recent_example:
problem_area:
current_workaround:
workaround_limitations: []
measurable_cost_or_risk:
priority: HIGH|MEDIUM|LOW|NONE
existing_alternatives: []
contract_review_interest: YES|CONDITIONAL|NO|NOT_ASKED
private_demo_review_interest: YES|CONDITIONAL|NO|NOT_ASKED
negative_or_rejection_reasons: []
consent_reference:
privacy_classification:
source_record_reference:
validation_status: VALID|PARTIAL|INVALID|WITHDRAWN
invalid_reason:
commercial_commitment: false
customer_adoption: false
known_limitations: []
```

`VALID` 至少要求近期实例、现有 workaround、优先级理由、独立性、consent/source reference
和人类责任方完整。缺失项必须是 `PARTIAL` 或 `INVALID`，不得由 Reviewer 猜测补齐。

## 6. Evidence Acceptance and Rejection（证据接受与拒绝）

### Acceptable

- 可归因的近期 workflow/incident/problem example；
- current workaround 与不足；
- 可描述的成本、风险或人工步骤；
- 明确的优先级和拒绝理由；
- 负面、无需求或退出记录。

### Invalid for `CS-G0`

- 只有模型对概念的赞扬；
- “听起来有意思”或愿意看 Demo；
- 无近期实例的假设性意见；
- 从公开文章推断某组织有需求；
- 多个 prompt 冒充多个组织；
- 内部作者自评；
- 销售名单、邮件打开、网页访问；
- 未经同意的会议记录、PII、credential 或客户材料。

## 7. Deterministic Scoring（确定性计数）

只有 `validation_status=VALID` 的记录可计数。进入 `CS-G0` 至少需要：

```text
VALID_INDEPENDENT_PROBLEM_RECORDS>=5
INDEPENDENT_ORGANIZATION_OR_CONTEXTS>=3
HIGH_PRIORITY_RECORDS>=3
RECENT_EXAMPLE_PRESENT=5/5
CURRENT_WORKAROUND_PRESENT=5/5
CONTINUE_REVIEW_INTEREST>=2
NEGATIVE_AND_WITHDRAWN_RECORDS_PRESERVED=true
```

其中 `CONTINUE_REVIEW_INTEREST` 只表示愿意继续评审 contract 或 private Demo，不是客户、
Design Partner、Commercial Commitment 或 Adoption。

任何阈值未满足：

```text
CS_G0_PROBLEM_FREEZE_PASS=false
COMMERCIALIZATION_STANDARD_READY=false
```

## 8. Privacy and Data Handling（隐私与数据处理）

执行前必须另行建立：

- validation Owner、Reviewer 和 Data Steward；
- consent、purpose、retention、withdrawal 和 deletion path；
- pseudonymization 与 public-safe extraction；
- credential、secret、PII、客户数据和受监管数据排除；
- raw record access control；
- security finding confidential route；
- negative result preservation。

公开报告默认只发布 aggregated counts、pseudonymous context 和 public-safe paraphrase。未经
单独授权，不发布组织名、人员名、原始 transcript 或 endorsement。

## 9. Stop Conditions（停止条件）

出现以下任一项必须停止当前记录：

- 无 consent 或责任方；
- 被要求披露 credential、secret、客户 Evidence 或受监管数据；
- 观察者撤回；
- 作者诱导或篡改回答；
- 独立性无法证明；
- raw data retention/recipient 不清楚；
- 试图将问题反馈包装成客户证言、采用或销售承诺。

停止和撤回记录必须保留最小 provenance，不保留已要求删除的内容。

## 10. Authorization Boundary（授权边界）

当前允许：

- 内部协议审查；
- synthetic empty ledger / record example 设计；
- consent、retention、redaction 模板准备；
- Human Decision 所需的风险汇总。

当前不允许：

- 联系观察者；
- 发送问卷或邀请；
- 收集组织/客户数据；
- enrollment；
- 对外发布 market claim；
- 创建 prospect、pipeline、Design Partner 或客户记录；
- 承诺 Demo、Pilot、产品或服务。

## 11. Current State（当前状态）

```text
VEAP_PROBLEM_VALIDATION_PROTOCOL_DEFINED=true
VEAP_PROBLEM_VALIDATION_CONTRACT_CREATED=true
VEAP_PROBLEM_VALIDATION_EXECUTION_AUTHORIZED=false
VEAP_EXTERNAL_OUTREACH_AUTHORIZED=false

VEAP_VALID_PROBLEM_RECORDS=0
VEAP_INDEPENDENT_ORGANIZATION_CONTEXTS=0
VEAP_HIGH_PRIORITY_RECORDS=0
VEAP_CONTINUE_REVIEW_INTEREST=0

CS_G0_PROBLEM_FREEZE_PASS=false
MARKET_VALIDATION_PASS=false
CUSTOMER_ADOPTION=false
COMMERCIAL_COMMITMENT=false
COMMERCIAL_OFFER_CREATED=false

AUTHORITY_CHANGED=false
OWNERSHIP_CHANGED=false
IMPLEMENTATION_AUTHORIZED=false
EXTERNAL_ACTION_AUTHORIZED=false
```
