---
document_id: DBA-TITMAS-COMMUNITY-CONDUCT-CANDIDATE-0.1
title: TITMAS Community Conduct Candidate v0.1
title_zh: TITMAS 社区行为规范候选 v0.1
status: candidate-not-adopted-not-publicly-enforced
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
document_type: non-executable-conduct-policy-candidate
architecture_domain: TITMAS
code_of_conduct_adopted: false
reporting_path_assigned: false
enforcement_body_assigned: false
public_community_established: false
authority_effect: none
---

# TITMAS Community Conduct Candidate v0.1

## 1. Current Boundary（当前边界）

本文件定义公共贡献表面启用前必须解决的行为与安全原则，但不是已经采纳或可执行的正式
Code of Conduct。当前没有报告地址、处理机构、社区成员或外部执行权限。

```text
TITMAS_CODE_OF_CONDUCT_CANDIDATE_CREATED=true
TITMAS_CODE_OF_CONDUCT_ADOPTED=false
TITMAS_CONDUCT_REPORTING_PATH_ASSIGNED=false
TITMAS_CONDUCT_ENFORCEMENT_BODY_ASSIGNED=false
```

## 2. Expected Conduct（期望行为）

未来参与者应：

- 专业、尊重、友善地讨论技术和治理分歧；
- 批评设计、证据和边界，不攻击个人、组织或身份；
- 清楚披露 affiliation、Conflict of Interest 和 AI assistance；
- 引用原始来源，承认 unknown、failure、limitation 和 attribution；
- 尊重隐私、许可证、商标、研究伦理和安全披露边界；
- 为不同语言、时区、经验和可访问性需求保留参与路径；
- 避免重复催促 Maintainer、滥发低质量内容或隐藏自动生成材料。

## 3. Unacceptable Conduct（不可接受行为）

包括但不限于：

- 骚扰、威胁、歧视、羞辱、跟踪或发布他人私密信息；
- 伪造身份、贡献来源、测试结果、角色、批准、许可证或外部认可；
- 使用智能体大规模生成未经理解和验证的 Issue、PR、评论或翻译；
- 提交 secret、PII、客户数据、恶意载荷或未经授权的真实 Evidence；
- 以角色、贡献量、投票、模型推荐或社交压力绕过 DBA/DBOS/SAEE Authority；
- 静默删除失败、异议、Rejected Proposal 或历史证据。

## 4. AI-assisted Participation（智能体辅助参与）

AI 可以帮助学习、检索、草拟、检查和测试，但：

- 必须披露 `agent_or_tool_ref` 和人工责任方；
- 人工提交者必须理解并能解释内容；
- 必须验证引用、许可证、事实、边界和生成内容；
- 智能体不能自我认证、批准或成为唯一责任主体；
- 批量、重复、不可验证或无法维护的生成内容可以被拒绝。

该规则吸收 OpenTelemetry 对 AI-assisted contribution 强调披露、理解、审查和维护者负担
的经验，但不复制其特定仓库的贡献次数限制。

## 5. Reporting and Response Requirements（报告与响应前置）

公共贡献表面启用前必须另行确定：

```text
confidential_reporting_channel=
emergency_security_channel=
response_owner_ref=
backup_owner_ref=
acknowledgement_target=
triage_process=
appeal_process=
retention_and_privacy_policy=
conflict_of_interest_recusal=
```

缺一项都不能声称已有完整 Code of Conduct enforcement（行为规范执行能力）。

处理结果必须区分：

- conduct report；
- security report；
- technical disagreement；
- architecture decision；
- legal or license issue。

它们不能由同一个无边界流程自动决定。

## 6. Adoption Gate（采纳闸门）

正式采纳至少要求：

1. Human Program Owner / Architecture Authority 的明确决定；
2. 可用且保密的报告渠道；
3. 指定及备份 response owner；
4. 隐私、保存、recusal 和 appeal 规则；
5. 与贡献指南、Security Disclosure、License 和平台政策对齐；
6. 中英文文本一致性审查；
7. 公共入口启用时间与适用范围。

在此之前：

```text
PUBLIC_CONDUCT_ENFORCEMENT_CLAIM_ALLOWED=false
PUBLIC_CONTRIBUTION_SURFACE_AUTHORIZED=false
```
