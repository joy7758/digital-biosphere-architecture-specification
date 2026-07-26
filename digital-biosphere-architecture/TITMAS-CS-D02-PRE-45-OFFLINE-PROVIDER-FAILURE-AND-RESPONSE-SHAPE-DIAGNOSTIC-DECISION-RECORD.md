# TITMAS CS-D02 PRE-45 Offline Provider Failure and Response Shape Diagnostic Decision Record

中文：TITMAS CS-D02 PRE-45 离线 Provider 失败与响应形态诊断决定记录。

```text
DECISION_ID=CS-D02-PRE-45
DECIDED_BY_REF=zhangbin
STANDING_DIRECTIVE_REFERENCE=TITMAS-CS-STANDING-001
DECISION=AUTHORIZE_ZERO_NETWORK_OFFLINE_PRE44_PROVIDER_FAILURE_AND_RESPONSE_SHAPE_DIAGNOSTIC
RECOMMENDATION_COMMIT=334896900070590b4b4c6d8003235233bc9414c2
INPUTS_EXACT=8
OUTPUTS_EXACT=3
NETWORK_REQUESTS_MAX=0
MODEL_REQUESTS_MAX=0
CREDENTIAL_READS_MAX=0
RAW_PROVIDER_ENVELOPE_ACCESSES_MAX=0
PRE44_GATE_PASS_CHANGED=false
RB1_IMPLEMENTATION_AUTHORIZED=false
```

本决定只授权使用 PRE-44 已提交 sanitized metadata 做离线因果边界诊断。

诊断必须保留：

- Kimi timeout 根因 `UNKNOWN`；
- GLM direct-JSON failure 根因 `UNKNOWN`；
- concurrency、query length 与 reviewer profile 为可能混杂因素但未测量；
- PRE-44 gate 继续 `BLOCKED`。

不允许发送新请求、读取 credential、访问 raw Provider envelope、修改
`titmas-integrations`，也不允许形成 RB1 implementation recommendation。

规范机器记录：

- [`Decision JSON`](TITMAS-CS-D02-PRE-45-OFFLINE-PROVIDER-FAILURE-AND-RESPONSE-SHAPE-DIAGNOSTIC-DECISION-RECORD.v0.1.json)
- [`Decision Schema`](architecture/schemas/titmas-cs-d02-pre-45-offline-failure-diagnostic-decision-record.schema.v0.1.json)
