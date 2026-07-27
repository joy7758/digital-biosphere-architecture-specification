---
document_id: DBA-TITMAS-CE-G9-OFFLINE-LOG-CORRELATOR-REMEDIATION-REPORT-0.1
title: TITMAS CE-G9 Offline Log Correlator Remediation Report v0.1
title_zh: TITMAS CE-G9 离线日志关联器修正报告 v0.1
version: 0.1.0
status: pass-offline-remediation-only
maturity: Development
maturity_scope: ce-g8-log-correlator-tooling
owner_ref: zhangbin
decision_reference: TITMAS-COMMERCIAL-EVALUATION-CE-G9
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G9 Offline Log Correlator Remediation Report v0.1

## 1. Outcome

```text
CE_G9_RESULT=PASS_OFFLINE_LOG_CORRELATOR_REMEDIATION_ONLY
ORIGINAL_TOOL_DEFECT=DOUBLE_ESCAPED_REGEX_PATTERN
PYTHON_3_14_TESTS_PASS=13/13
PYTHON_3_13_TESTS_PASS=13/13
PUBLIC_REQUESTS=0
SSH_SESSIONS=0
SERVER_READS=0
SERVER_WRITES=0
```

## 2. Defect finding

原 correlator 的 raw regex 包含双重转义：

```text
\\[
\\s
```

该 pattern 在函数首次执行时触发 `re.error`；该异常类名正是 CE-G8 receipt 中的
`error`。CE-G9 可以证明 CE-G8 correlator 的工具失败原因，但不能证明 CE-G7 的 TLS
transport failure 原因。

## 3. Remediation

- 移除 regex；
- 用固定 delimiter 解析 Nginx access line；
- 显式 month table 和 numeric timezone；
- journalctl 使用 exact epoch bounds；
- access/error paths、journal runner、timezone 与 current-target reader 可注入；
- 错误改为 `WINDOW_*`、`CURRENT_TARGET_*`、`ACCESS_PARSE_FAILED`、
  `ERROR_PARSE_FAILED`、`JOURNAL_PARSE_FAILED` 等稳定 code；
- unit test 覆盖 IPv4/IPv6 source hashing；匿名 synthetic fixtures 覆盖边界时间、
  窗口外、malformed line、handshake、upstream、invalid JSON 和 empty output。

## 4. Privacy verification

离线 tests 证明 result 不含：

- raw log line；
- literal source IP；
- ephemeral salt；
- raw SSL error text。

只保存 salted SHA-256、counts 和 classes。

## 5. Boundaries

```text
CE_G8_HISTORICAL_RESULT_CHANGED=false
CE_G8_SERVER_CORRELATION_RECOVERED=false
TLS_ROOT_CAUSE_PROVEN=false
REDEPLOYMENT_AUTHORIZED=false
POLICY_CHANGED=false
PRODUCTION_READY=false
```

本地只有 Python 3.14 与 3.13 直接通过；Python 3.10 尚未直接执行。因此下一步只允许
准备 CE-G10 cross-version offline validation recommendation，不发送 public request 或 SSH。
