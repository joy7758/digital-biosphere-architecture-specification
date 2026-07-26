---
document_id: DBA-TITMAS-CS-D02-PRE-11-OFFLINE-DIAGNOSTIC-RESULT-0.1
title: TITMAS PRE-11 Offline Provider Diagnostic Result v0.1
title_zh: TITMAS PRE-11 离线 Provider 诊断结果 v0.1
status: PASS_OFFLINE_DIAGNOSTIC_RERUN_REDESIGN_REQUIRED
observed_on: 2026-07-26
decision_reference: CS-D02-PRE-11
live_model_requests_executed: 0
implementation_effect: none
commercial_effect: none
---

# TITMAS PRE-11 Offline Provider Diagnostic Result v0.1

## 1. Outcome（结果）

PRE-11 的离线诊断完成，且没有发送任何模型请求、读取 API key 或保存原始 provider body。

```text
RESULT=PASS_OFFLINE_DIAGNOSTIC_RERUN_REDESIGN_REQUIRED
LIVE_MODEL_REQUESTS_EXECUTED=0
REAL_CREDENTIALS_ACCESSED=false
PLACEHOLDER_FIXTURES=4
PRE_10_RETRY_AUTHORIZED=false
PRE_10_RERUN_AUTHORIZED=false
```

## 2. Layered Findings（分层发现）

### Installed Kimi/Qianfan tool

已安装工具只接受一个非敏感 `query` 字符串，固定使用 `kimi-k2.6`，不允许 fallback。
工具没有向调用者公开内部 provider envelope、timeout、response-format 或 retry 行为。

### Qianfan provider contract

百度千帆当前官方文档列出：

- OpenAI-compatible base URL：`https://qianfan.baidubce.com/v2`；
- chat endpoint：`/chat/completions`；
- Kimi model identifier：`kimi-k2.6`。

因此 PRE-10 的公开模型标识与当前官方列表一致。但由于工具内部封装不可见，两个 timeout /
network error 的确切层次仍为 `UNKNOWN`，不能判断是 wrapper、network、provider capacity
还是其他原因。

### DeepSeek provider contract

DeepSeek 当前官方 Chat Completion 文档定义 `/chat/completions`，并继续支持
`response_format={"type":"json_object"}`，前提是 prompt 也明确要求 JSON。

当前文档列出的模型是 `deepseek-v4-flash` 和 `deepseek-v4-pro`；PRE-10 冻结的是
`deepseek-chat`。因此存在 current contract drift（当前契约漂移）。这是两次 HTTP 400 的
强相关线索，但原始错误 body 未保留，所以不能宣称它是已证明的唯一或确切原因。

## 3. Offline Fixture Results（离线 Fixture 结果）

| Fixture | Expected result | Sent |
|---|---|---|
| Installed Kimi tool `{query}` | `PASS_DECLARED_TOOL_INPUT_SHAPE` | `false` |
| Qianfan `kimi-k2.6` provider shape | `PASS_CURRENT_OFFICIAL_PROVIDER_SHAPE` | `false` |
| DeepSeek `deepseek-v4-pro` JSON shape | `PASS_CURRENT_OFFICIAL_PROVIDER_SHAPE` | `false` |
| PRE-10 `deepseek-chat` shape | `REJECT_CURRENT_OFFICIAL_MODEL_ENUM` | `false` |

Fixtures 只验证当前公开契约的结构，不证明 credential、quota、network、provider availability、
模型输出或生产可用性。

## 4. Rerun Prerequisites（重跑前置条件）

1. DeepSeek 改用当前官方列出的 model identifier；
2. 使用 JSON mode 时，prompt 必须明确要求 JSON；
3. Kimi 继续经过已安装的一字段工具契约，除非另行审查 direct API path；
4. 新计划增加 provider-specific preflight，会话失败时在 candidate review 之前停止；
5. 新计划冻结 model、prompt hash、response Schema、threshold 和请求上限；
6. 任何 live request 前必须先提交、推送并验证新授权基线；
7. PRE-10 失败历史和原阈值永久保留。

## 5. References（引用）

- [Qianfan official model and endpoint documentation](https://cloud.baidu.com/doc/qianfan/s/Smoghsq3g)
- [DeepSeek official Chat Completion documentation](https://api-docs.deepseek.com/api/create-chat-completion/)
- [DeepSeek official JSON Output documentation](https://api-docs.deepseek.com/guides/json_mode/)
- [Placeholder fixtures](provider-request-shape-fixtures.v0.1.json)
- [Machine diagnostic result](provider-path-diagnostic-result.v0.1.json)
- [PRE-10 sanitized observations](../commercialization-standards-public-source-record-review/raw-sanitized-observations.v0.1.json)

## 6. Non-effects（非效果）

```text
OFFLINE_DIAGNOSTIC_COMPLETED=true
LIVE_MODEL_REQUEST_AUTHORIZED=false
RERUN_AUTHORIZED=false
CANDIDATE_STATUS_CHANGED=false
PUBLIC_SOURCE_RECORD_COUNTING_AUTHORIZED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
MARKET_VALIDATION_PASS=false
CUSTOMER_ADOPTION=false
IMPLEMENTATION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```
