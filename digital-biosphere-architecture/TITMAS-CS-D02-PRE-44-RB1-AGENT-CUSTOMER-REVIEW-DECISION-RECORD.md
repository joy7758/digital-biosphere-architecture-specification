# TITMAS CS-D02 PRE-44 RB1 Agent Customer Review Decision Record

中文：TITMAS CS-D02 PRE-44 RB1 智能体客户审查决定记录。

```text
DECISION_ID=CS-D02-PRE-44
DECIDED_BY_REF=zhangbin
STANDING_DIRECTIVE_REFERENCE=TITMAS-CS-STANDING-001
DECISION=AUTHORIZE_EXACT_FOUR_SESSION_QIANFAN_AGENT_CUSTOMER_REVIEW_WITH_FROZEN_THRESHOLDS_AND_SANITIZED_FAIL_CLOSED_HANDOFF
RECOMMENDATION_COMMIT=258e5e81956c9cd1210054e81b8df95e392cba2c
AGENT_REVIEW_AUTHORIZED=true
NETWORK_REQUESTS_MAX=4
CREDENTIAL_READS_MAX=1
RB1_IMPLEMENTATION_AUTHORIZED=false
TARGET_REPOSITORY_MODIFICATION_AUTHORIZED=false
```

本决定只授权对 PRE-43 冻结 RB1 planning packet 执行四个受控 advisory Agent Review
会话。两个 exact models 为 `kimi-k2.6` 与 `glm-5.2`，各两次；每次最多一个请求。

阈值在执行前冻结为：

- qualifying sessions 至少 3；
- `RECOMMENDED` 或 `CONDITIONALLY_RECOMMENDED` 至少 2；
- `would_recommend_to_agent_developer=true` 至少 2；
- `would_call_or_reuse=true` 至少 2；
- Authority safety failure 必须为 0。

禁止 retry、fallback、model substitution、alias inference、JSON repair、raw provider
envelope persistence、credential persistence、hidden reasoning persistence，以及任何
`titmas-integrations` 写入。

通过只允许形成独立的 RB1 Implementation Recommendation，不授权 package、source、
tests、provider binding、conformance、Runtime、release、commercial offering 或
certification。

规范机器记录：

- [`TITMAS-CS-D02-PRE-44-RB1-AGENT-CUSTOMER-REVIEW-DECISION-RECORD.v0.1.json`](TITMAS-CS-D02-PRE-44-RB1-AGENT-CUSTOMER-REVIEW-DECISION-RECORD.v0.1.json)
- [`Decision Schema`](architecture/schemas/titmas-cs-d02-pre-44-rb1-agent-customer-review-decision-record.schema.v0.1.json)
