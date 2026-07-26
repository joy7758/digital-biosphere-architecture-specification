---
document_id: DBA-TITMAS-CS-D02-PRE-09-DESK-RESEARCH-EXECUTION-PLAN-0.1
title: TITMAS CS-D02 PRE-09 Public First-party Desk Research Execution Plan v0.1
title_zh: TITMAS CS-D02 PRE-09 公开第一方问题 desk research 执行计划 v0.1
version: 0.1.0
status: frozen-authorization-baseline-not-executed
maturity: Development
maturity_scope: entire-document
owner_ref: zhangbin
decision_reference: CS-D02-PRE-09
frozen_at: 2026-07-26T08:29:30Z
execution_started: false
---

# TITMAS CS-D02 PRE-09 Public First-party Desk Research Execution Plan v0.1

## 1. Purpose（目的）

在不联系任何组织或个人、不访问私有内容、不产生有效问题记录的前提下，验证公开第一方
问题报告方法能否被 Agent 严格执行。

## 2. Exact Queries（固定查询）

每条最多执行一次：

1. `site:github.com/open-telemetry GenAI agent issue trace observability`
2. `site:github.com/microsoft/autogen issue agent reliability execution trace`
3. `site:github.com/microsoft/agent-framework issue telemetry agent execution`
4. `site:github.com/langchain-ai/langchain issue agent trace reliability`
5. `site:github.com/crewAIInc/crewAI issue agent execution trace reliability`
6. `site:github.com/modelcontextprotocol issue audit provenance execution`
7. `site:opentelemetry.io GenAI agent observability limitations`
8. `site:blog.langchain.com agent incident reliability trace`

查询结果页和 snippet 只能用于导航，不能成为 candidate source 或 Evidence。

## 3. Allowlist（允许表面）

- `github.com/open-telemetry/`
- `github.com/microsoft/autogen`
- `github.com/microsoft/agent-framework`
- `github.com/langchain-ai/`
- `github.com/crewAIInc/`
- `github.com/modelcontextprotocol/`
- `opentelemetry.io/`
- `microsoft.github.io/`
- `learn.microsoft.com/`
- `blog.langchain.com/`
- `docs.langchain.com/`
- `crewai.com/`
- `modelcontextprotocol.io/`

只有 official Maintainer issue、official incident/postmortem、official project technical
report 或 accountable organization technical report 可以成为 candidate。论坛、社交媒体、
搜索摘要、二手文章、推广案例和模型生成内容不合格。

## 4. Limits（上限）

```text
RUNS_MAX=1
QUERIES_MAX=8
PUBLIC_PAGES_OPENED_MAX=12
CANDIDATE_RECORDS_MAX=4
SOURCE_TIME_WINDOW=2025-01-01T00:00:00Z..2026-07-26T23:59:59Z
QUOTED_WORDS_PER_SOURCE_MAX=25
RAW_CONTENT_STORED=false
DIRECT_PERSONAL_IDENTIFIERS_STORED=false
```

## 5. Candidate Status（候选状态）

本轮只允许：

- `CANDIDATE_UNREVIEWED`；
- `PARTIAL`；
- `INVALID`；
- `CONFLICTED`；
- `INVALID_AUTHORIZATION_ENVELOPE`。

禁止 `VALID`。后续独立 Agent review 和 Human Counting Decision 另行决定。

## 6. Retention（保留）

- 不持久化页面、HTML、附件、截图或 provider raw envelope；
- 临时 excerpt 只在同一会话 extraction 期间存在；
- extraction 后立即删除，`temporary_excerpt_retention_max_days=0`；
- 只保存最小 metadata、public-safe paraphrase、metadata hash 和 deletion tombstone；
- source correction/removal 触发 candidate suspension，不静默删除历史。

## 7. Fail-closed Rules（失败关闭）

任一条件触发即停止相关 source 或整个 run：

- authentication、captcha、paywall、access-control 或 terms/robots conflict；
- allowlist/time-window/cap violation；
- direct identifier、private/customer data、credential 或 private log；
- Schema/digest/authorization mismatch；
- 需要推断 accountable role、independence 或缺失字段；
- 试图把 publication 当作 consent、customer、market fit 或 VEAP fit；
- 试图自动计数或关闭 `CS-G0`。

## 8. Expected Outputs（预期输出）

- `source-candidate-set.v0.1.json`；
- `DESK-RESEARCH-RESULT-v0.1.md`；
- 所有 query/page/candidate 计数；
- zero-result、failure、unknown、conflict 和 boundary audit；
- `VALID_PROBLEM_RECORDS=0`。

## 9. Execution Gate（执行闸门）

```text
AUTHORIZATION_BASELINE_COMMITTED=false
AUTHORIZATION_BASELINE_PUSHED=false
PUBLIC_DESK_RESEARCH_EXECUTION_STARTED=false
```

三个字段中前两个未得到远端直接证据前，不执行查询。
