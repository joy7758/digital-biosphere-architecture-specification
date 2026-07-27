# TITMAS CS-D02 PRE-72 Official Provider Structured-Output Evidence and Preflight Scope Recommendation v0.1

## 1. Recommendation

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
EXACT_RECOMMENDED_ACTION=AUTHORIZE_BOUNDED_PRE72_DUAL_PROVIDER_STRUCTURED_OUTPUT_PREFLIGHT
PRE72_RECOMMENDATION_PREPARED=true
PRE72_PREFLIGHT_DECIDED=false
PRE72_PREFLIGHT_AUTHORIZED=false
PRE72_LIVE_REQUEST_EXECUTED=false
PROVIDER_SUPPORTED=false
FORMAL_HUMAN_SECURITY_REVIEW_COMPLETE=false
STANDARD_READY=false
```

建议在独立 Architecture Decision（架构决策）之后，对百度千帆
`ernie-4.5-turbo-20260402` 与阿里云百炼 `qwen3.7-plus` 各执行三次顺序、
public-safe（公开安全）且严格有界的结构化输出预检。

本建议只建立官方证据绑定和未来预检范围，不授权、不调用任何模型，不读取凭据。

## 2. Agent recommendation gate

如果潜在客户询问“是否推荐 TITMAS 当前 Provider 审查链路用于正式安全审查”，
智能体当前应回答：

> 有条件推荐继续验证，不推荐将现有结果表述为 Provider support、正式安全审查、
> 标准符合性或生产就绪。官方文档证明两条目标路径存在 JSON 输出控制，但不能证明
> 它们在 TITMAS 严格 direct-JSON contract 下稳定满足要求。

不推荐原因已经被拆解为可验证缺口：

1. Qianfan 官方说明 `response_format` 可能不能满足预期；
2. Qwen JSON mode 需要 prompt 明确包含 `JSON`，thinking mode 还存在严格 JSON 风险；
3. PRE-70 已直接观察到 Qianfan code fence；
4. 官方功能说明不是当前 endpoint、model、request shape 的运行可靠性证据；
5. 提取、剥离 code fence 或 JSON repair 会掩盖契约失败。

## 3. Official evidence conclusion

### 3.1 Baidu Qianfan

官方文档记录：

- OpenAI-compatible endpoint 为
  `https://qianfan.baidubce.com/v2/chat/completions`；
- exact model id 为 `ernie-4.5-turbo-20260402`；
- `response_format.type` 支持 `json_object`、`text` 与 `json_schema`；
- 官方明确提示生成结果可能不满足格式效果；
- 明确列出的不支持模型是 ERNIE X1 Turbo 系列，当前目标 ERNIE 4.5 Turbo
  未列入该排除项。

因此只允许记录：

```text
QIANFAN_STRUCTURED_OUTPUT_PARAMETER_DOCUMENTED=true
QIANFAN_EXACT_ENDPOINT_MODEL_DOCUMENTED=true
QIANFAN_STRICT_DIRECT_JSON_RELIABILITY_PROVEN=false
QIANFAN_STATUS=DOCUMENTED_PARAMETER_AVAILABLE_EXACT_MODEL_NOT_EXCLUDED_LIVE_PREFLIGHT_REQUIRED
```

### 3.2 Alibaba Cloud Model Studio

官方文档记录：

- Beijing workspace OpenAI-compatible Base URL pattern 为
  `https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/compatible-mode/v1`；
- exact model id 为 `qwen3.7-plus`；
- JSON mode request shape 为 `response_format={"type":"json_object"}`；
- prompt 必须明确包含 `JSON`；
- thinking mode 可能不能返回严格有效 JSON，故预检候选明确
  `enable_thinking=false`；
- 本预检不设置 `max_tokens`，避免人为截断结构化结果。

因此只允许记录：

```text
QWEN_STRUCTURED_OUTPUT_PARAMETER_DOCUMENTED=true
QWEN_EXACT_ENDPOINT_MODEL_DOCUMENTED=true
QWEN_STRICT_DIRECT_JSON_RELIABILITY_PROVEN=false
QWEN_STATUS=DOCUMENTED_CAPABILITY_LIVE_PREFLIGHT_REQUIRED
```

## 4. Exact bounded preflight candidate

未来独立 Decision 如采纳，只允许：

| 项目 | 冻结范围 |
|---|---|
| Provider lanes | Qianfan + Alibaba Cloud Model Studio |
| Requests | 每 lane 3 次，合计最多 6 次 |
| Ordering | 顺序执行 |
| Response control | `response_format={"type":"json_object"}` |
| Qwen thinking | `enable_thinking=false` |
| Qianfan thinking | 不启用 thinking，不增加未经证实的 request field |
| Prompt | 明确要求 direct JSON，并包含字面量 `JSON` |
| Validation | assistant content 必须为单一 JSON object，并通过冻结 Schema |
| Retry / fallback / substitution | 0 |
| Fence stripping / extraction / repair | 0 |
| Raw response persistence | 0 |
| Credential identifier count | 2 |
| Credential in-memory access | 最多 6 |
| TLS authorization-header emission | 最多 6 |
| Credential printed / persisted / exposed | 必须为 0 |
| Target repository writes | 0 |

任一请求发生 HTTP、model identity、direct JSON、Schema、boundary、timeout 或
credential accounting 偏差，即 fail closed（失败关闭）并停止该 lane。

## 5. Pass criteria

每条 lane 必须同时满足：

1. 3/3 HTTP success；
2. 3/3 exact returned model match；
3. 3/3 assistant content 为无前后缀、无 code fence 的单一 JSON object；
4. 3/3 frozen Schema PASS；
5. 3/3 authority/non-claim boundary PASS；
6. 0 retry、fallback、substitution、extraction、repair；
7. raw response 和 secret value 均未持久化；
8. sanitized receipt 可追踪至 provider、endpoint、model、request-shape 和时间。

通过后只允许称为：

```text
BOUNDED_STRUCTURED_OUTPUT_PREFLIGHT_PASS
```

不得称为 Provider support、formal Human Security Review、conformance、
certification、Standard Ready、release 或 production readiness。

## 6. Authority and non-effects

```text
Recommendation != Decision
Decision != Execution
Official documentation != live reliability
Preflight pass != Provider support
Agent review != formal Human Security Review
Schema valid != conformance
Evidence != Truth
```

本建议不创建或修改 Runtime、Agent、Entity、Permission、Capability、Evidence Truth、
DBOS、SAEE、target implementation、商业报价、认证或发布状态。

## 7. Machine-readable references

- [Official provider evidence ledger](commercialization-standards-p0-security-and-platform-provider-capability-evidence/official-provider-capability-evidence.v0.1.json)
- [Bounded preflight scope](commercialization-standards-p0-security-and-platform-provider-capability-evidence/pre72-bounded-preflight-scope.v0.1.json)
- [Offline validation result](commercialization-standards-p0-security-and-platform-provider-capability-evidence/PRE-72-OFFICIAL-PROVIDER-CAPABILITY-EVIDENCE-RESULT-v0.1.md)
- [PRE-71 strict response contract](commercialization-standards-p0-security-and-platform-response-contract-remediation/strict-response-contract-candidate.v0.2.json)
- [PRE-71 credential accounting profile](commercialization-standards-p0-security-and-platform-response-contract-remediation/credential-use-accounting-profile.v0.1.json)

## 8. Official public sources

- [Baidu Qianfan text-generation API reference](https://cloud.baidu.com/doc/qianfan-api/s/3m7of64lb)
- [Baidu Qianfan Token Plan endpoint and model reference](https://cloud.baidu.com/doc/qianfan/s/Smoghsq3g)
- [Alibaba Cloud Model Studio structured-output reference](https://help.aliyun.com/en/model-studio/qwen-structured-output)
- [Alibaba Cloud Model Studio model and endpoint reference](https://help.aliyun.com/en/model-studio/models)
