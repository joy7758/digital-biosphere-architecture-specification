# TITMAS CS-D02 PRE-50 RB1 DeepSeek Binding Scope and Security Planning Decision Record

```text
DECISION_ID=CS-D02-PRE-50
DECISION_RESULT=AUTHORIZE_DBA_ONLY_RB1_DEEPSEEK_BINDING_SCOPE_SECURITY_AND_AGENT_REVIEW_PLANNING_PACKET
DECIDED_BY_REF=zhangbin
DECIDED_AT=2026-07-27T06:50:29+08:00
STANDING_DIRECTIVE=TITMAS-CS-STANDING-001
RECOMMENDATION_COMMIT=6690a62350f1879ef837fce78764f970760a0a22
PRIMARY_REPOSITORY=digital-biosphere-architecture
TARGET_REPOSITORY_WRITE_PATHS=0
PROVIDER_REQUESTS=0
CREDENTIAL_READS=0
```

本决定依据
[`TITMAS-CS-STANDING-001`](TITMAS-COMMERCIALIZATION-STANDING-RECOMMENDATION-AUTHORIZATION-v0.1.md)
采纳
[`CS-D02-PRE-50 Recommendation`](TITMAS-CS-D02-PRE-50-RB1-DEEPSEEK-BINDING-SCOPE-AND-SECURITY-PLANNING-RECOMMENDATION-v0.1.md)
中的唯一精确选项。

授权仅包括：

1. 在 DBA 创建推荐中列出的 12 个 Provider binding planning artifacts；
2. 固定 DeepSeek OpenAI-compatible Chat Completions 为单一候选，而不是已支持 Provider；
3. 固定 `httpcore==1.0.9` 为待审 transport 候选，而不是已接受依赖；
4. 记录 endpoint、credential identifier、timeout、limit、sanitization、retention、
   failure taxonomy、rollback 和 stop conditions；
5. 保留 `P0_DIRECT_OBSERVABILITY_WITH_CANDIDATE_TRANSPORT=false`；
6. 准备四个顺序 Agent Review session 的机器可读输入，但不调用任何 Agent；
7. 执行 JSON Schema、hash、link、敏感信息和边界验证；
8. 路径限定提交并推送 DBA 当前非默认分支。

本决定不授权：

- 修改 `titmas-integrations`、DBOS、SAEE 或其他仓库；
- 读取 `DEEPSEEK_API_KEY` 的值；
- 发起 Provider 或其他网络请求；
- 安装 `httpcore` 或任何依赖；
- 实现 Provider binding、Runtime、Agent、Entity、Permission 或 Evidence；
- Agent Review、Security Review、Provider Conformance、PR、merge、tag、release、
  deployment、Commercial Offering 或 Certification。

如果远端输入漂移、P0 被伪造为 PASS、敏感内容被读取或保存、Schema/文件集合验证失败，
必须 fail closed 并保留失败记录。
