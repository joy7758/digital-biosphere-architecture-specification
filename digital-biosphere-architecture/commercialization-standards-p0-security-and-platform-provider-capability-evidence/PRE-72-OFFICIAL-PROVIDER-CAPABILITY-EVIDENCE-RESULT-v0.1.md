# PRE-72 Official Provider Capability Evidence Result v0.1

## Result

```text
PRE72_RECOMMENDATION_PREPARED=true
OFFICIAL_PROVIDER_DOCUMENTATION_BOUND=true
NEW_MACHINE_INSTANCES_SCHEMA_PASS=3/3
PREFLIGHT_RESPONSE_SCHEMA_METASCHEMA_PASS=true
COMMERCIALIZATION_ENTRY_SCHEMA_PASS=1/1
NEGATIVE_MUTATIONS_REJECTED=16/16
NETWORK_REQUESTS=0
MODEL_REQUESTS=0
CREDENTIAL_VALUE_READS=0
RAW_RESPONSES_PERSISTED=0
TARGET_REPOSITORY_WRITES=0
PREFLIGHT_DECIDED=false
PREFLIGHT_AUTHORIZED=false
PROVIDER_SUPPORTED=false
FORMAL_HUMAN_SECURITY_REVIEW_COMPLETE=false
STANDARD_READY=false
```

## Evidence acquisition

只读取百度智能云与阿里云官方公开文档，未访问任何模型 API。官方证据支持：

- Qianfan exact endpoint/model 和 `response_format` 参数存在；
- Alibaba Cloud exact endpoint family/model 和 JSON mode request shape 存在；
- 两条路径均有必须保留的严格 JSON 限制或风险说明；
- 官方文档不足以证明 live reliability。

## Offline validation

三个新增 machine instance 均通过各自 JSON Schema 2020-12 校验，预检响应
Schema 通过 JSON Schema 2020-12 metaschema 校验；
商业化机器入口继续通过其既有 Schema。

16 个 mutation（变异负例）全部被拒绝：

| case | mutation | result |
|---|---|---|
| `PRE72-N001` | 将 live strict reliability 改为 true | REJECTED_PASS |
| `PRE72-N002` | 将 Provider supported 改为 true | REJECTED_PASS |
| `PRE72-N003` | 将 bounded preflight authorized 改为 true | REJECTED_PASS |
| `PRE72-N004` | 将 official source 降级为 HTTP | REJECTED_PASS |
| `PRE72-N005` | 将 formal Human Security Review 改为 complete | REJECTED_PASS |
| `PRE72-N006` | 将 recommendation-only status 改为 authorized | REJECTED_PASS |
| `PRE72-N007` | 将 request cap 从 6 扩大为 7 | REJECTED_PASS |
| `PRE72-N008` | 将 retry cap 从 0 改为 1 | REJECTED_PASS |
| `PRE72-N009` | 允许 response extraction | REJECTED_PASS |
| `PRE72-N010` | 允许 raw response persistence | REJECTED_PASS |
| `PRE72-N011` | 允许打印 credential value | REJECTED_PASS |
| `PRE72-N012` | 将 Decision recorded 改为 true | REJECTED_PASS |
| `PRE72-N013` | 从 request contract 删除 JSON mode | REJECTED_PASS |
| `PRE72-N014` | 允许 request contract JSON repair | REJECTED_PASS |
| `PRE72-N015` | 让 response Schema 接受 Provider supported=true | REJECTED_PASS |
| `PRE72-N016` | 让 Qianfan response 使用 Qwen model | REJECTED_PASS |

第一次一次性 Python 校验命令在执行 mutation validation 前出现生成器表达式语法错误。
该错误没有修改 Schema、instance 或 fixture；修正一次性命令后，原 12 个负例
全部通过。此过程事实被保留，不升级为契约缺陷。

在补齐 exact preflight request/response contract 后，增加的 4 个负例也全部通过。

## Boundary conclusion

PRE-72 只完成：

1. official documentation binding；
2. agent-readable machine evidence；
3. bounded preflight scope recommendation；
4. fail-closed negative validation。

它没有记录 Architecture Decision，没有调用 Provider，没有读取 secret，也没有形成
Provider support、formal Human Security Review、conformance、Standard Ready 或 release。
