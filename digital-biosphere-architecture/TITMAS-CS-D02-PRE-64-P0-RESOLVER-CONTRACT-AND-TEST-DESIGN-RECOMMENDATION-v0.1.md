---
document_id: DBA-TITMAS-CS-D02-PRE-64-P0-RESOLVER-CONTRACT-AND-TEST-DESIGN-RECOMMENDATION-0.1
title: TITMAS P0 Resolver Contract and Test Design Recommendation v0.1
title_zh: TITMAS P0 解析器契约与测试设计建议 v0.1
version: 0.1.0
status: exact-offline-contract-and-test-design-recommended-not-decided
maturity: Development
maturity_scope: entire-document
primary_repository: digital-biosphere-architecture
decision_candidate: CS-D02-PRE-64
standing_directive_reference: TITMAS-CS-STANDING-001
recommended_by: Codex
recommended_at: 2026-07-27T10:37:00+08:00
target_repository_observed: https://github.com/joy7758/titmas-integrations.git
target_branch_observed: codex/rb0-governance-baseline
target_commit_observed: 5ac891c5af88b1e9aeacdb3666217c6f832a57a6
target_write_authorized: false
implementation_authorized: false
network_execution_authorized: false
credential_read_authorized: false
provider_integration_authorized: false
formal_security_review_completed: false
release_authorized: false
standard_ready: false
---

# TITMAS P0 Resolver Contract and Test Design Recommendation v0.1

## Recommendation

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=DEVELOPMENT_P0_RESOLVER_OBSERVATION_CONTRACT_AND_OFFLINE_TEST_DESIGN
NOT_RECOMMENDED_AS=NETWORK_BACKEND_IMPLEMENTATION_OR_PRODUCTION_RESOLVER
EXACT_OPTION=CREATE_VALIDATE_AND_REMOTE_FREEZE_PRE64_P0_RESOLVER_CONTRACT_AND_TEST_DESIGN_PACKET
```

如果潜在开发者需要把 DNS resolution（DNS 解析）与 TCP connect（TCP 连接）分离为
可验证的 P0/P1，我会有条件推荐本契约方向。它定义一个可注入、可替换、一次调用的
resolver boundary（解析器边界），再将同一个内存态解析结果交给 P1，避免默认 HTTP
transport 在 `connect_tcp` 内再次解析。

我不会推荐直接实现。当前仍缺 Agent Maintainer/Security Review、真实平台差异验证、
deadline enforcement（截止时间强制）实现和独立 target write Decision。本阶段只能生成
DBA 协议、Schema、fixture-level test design（夹具级测试设计）和审查输入。

## Why a Separate Contract Is Required

PRE-63 已选择：

```text
one explicit resolver invocation
  -> one deterministic selected address
  -> one TCP connection
  -> TLS verified against the original hostname
```

官方接口事实进一步表明：

1. Python `socket.getaddrinfo()` 返回 `(family, type, proto, canonname, sockaddr)`，
   结果与默认行为可能具有平台差异；
2. Python 官方文档建议在实际连接中限制 `SOCK_STREAM` / `IPPROTO_TCP`；
3. `socket.create_connection()` 会解析并依次尝试多个地址，因此不能满足本
   Development profile 的“一次 P0、一次 P1”；
4. HTTPCore 1.0.9 `SyncBackend.connect_tcp()` 使用 `socket.create_connection()`；
5. HTTPCore trace 只暴露 `connection.connect_tcp`，没有独立 DNS event；
6. HTTPCore 允许 TLS 使用独立 `sni_hostname`，可在连接 IP 时仍验证原始 hostname。

因此，单靠 HTTPCore trace 不能证明 P0/P1 分离；必须建立 replaceable bounded backend
contract（可替换有界后端契约）。上述事实是 exact-version design input，不是 Provider
support 或 dependency adoption。

## Direct Preconditions

```text
DBA_BASELINE_COMMIT=be57e4d1d9f78438da2a72c0f7630ab56ca1b992
TARGET_COMMIT=5ac891c5af88b1e9aeacdb3666217c6f832a57a6
PRE63_RECOMMENDATION_SHA256=1cd01acfd246e12cd3c1b72bdc804666ff2ac4d1b3f550486de2730579d5e950
PRE63_DECISION_SHA256=8303bb217908de4726094478c64c6eb8c60d3ef024fb3180cb7ee97ae1080808
PRE63_CLASSIFICATION_SHA256=d6f370dd03dbcb61422f3dad8bfc9cae38f4aebf2fa76143ceea9a4f11d42444
PRE63_P0_DESIGN_SHA256=faa671e361cbd5fd539fd61997c77f44d1dfed218d09330308eee4d765617eb2
PRE63_RECEIPT_SHA256=519ab21fce7fea208970580b57665a753470786e2650ee7f25ae54866bfd37e6
PRE63_RESULT_SHA256=d4edbfc29374360bde53e41cee512cf7d03671a350d802bb1e04d4c9645f705a
```

## Exact Contract Candidate

### Resolver invocation

```text
RESOLVER_INVOCATIONS_MAX=1
FAMILY_INPUT=AF_UNSPEC
SOCKET_TYPE_INPUT=SOCK_STREAM
PROTOCOL_INPUT=IPPROTO_TCP
FLAGS_INPUT=0
PORT_INPUT=443
IP_LITERAL_HOST_INPUT_ALLOWED=false
EXACT_ALLOWLISTED_HOST_REQUIRED=true
P0_TIMEOUT_BUDGET_MS=5000
RAW_RESULT_COUNT_MAX=64
UNIQUE_USABLE_RESULT_COUNT_MAX=64
```

`getaddrinfo()` 没有独立 timeout parameter。未来实现必须提供可取消、可观测、实际有界
的 deadline mechanism；仅设置 socket global/default timeout 不得被视为 P0 deadline
证据。PRE-64 只把该要求写入测试设计，不选择 thread、process、async resolver 或系统
服务。

### Filtering and selection

只接受：

- `AF_INET` 或 `AF_INET6`；
- `SOCK_STREAM`；
- `IPPROTO_TCP`；
- 对应 family 的合法 `sockaddr`；
- exact port `443`。

先按完整 tuple 去重，再使用：

```text
ADDRESS_SELECTION_RULE=FIRST_UNIQUE_IN_RESOLVER_ORDER_V1
SELECTED_ADDRESSES_MAX=1
```

该规则对给定有序输入确定，但不承诺不同操作系统返回相同顺序。平台可移植性必须进入
known limitation（已知限制），不得写成 cross-platform stability。

### In-memory continuity

P0 成功后形成非序列化 `ResolvedEndpoint`：

```text
original_hostname
port
family
socktype
proto
sockaddr
resolution_handle_ref
```

要求：

- raw `sockaddr` 和 IP 只存在于当前请求内存；
- `resolution_handle_ref` 是随机 opaque reference，不由 hostname/IP 派生；
- P1 必须消费同一个 `ResolvedEndpoint`，且 handle 完全匹配；
- P1 不得调用 resolver、`socket.create_connection()` 或任何会隐式重解析的 API；
- P1 最多一次 socket creation 和一次 connect；
- P1 失败后不得尝试第二地址；
- P2 TLS 必须以原始 allowlisted hostname 作为 SNI 与证书身份；
- 请求完成或首次失败后销毁内存态 endpoint。

### Sanitized P0 observation

只允许序列化：

```text
schema_version
phase_id=P0
status
endpoint_reference
elapsed_ms
timeout_budget_ms
raw_result_count
unique_usable_result_count
selected_address_family
failure_category
resolution_handle_ref
executed
```

禁止序列化：

```text
hostname
IP address
sockaddr
canonname
DNS packet
credential
Authorization header
request/response body
resolver exception string
```

`resolution_handle_ref` 只用于 P0/P1 continuity，不证明 DNS correctness、Provider
identity、Evidence 或 Truth。

### Failure taxonomy

```text
NONE
DNS_TIMEOUT
DNS_NAME_NOT_FOUND
DNS_TEMPORARY_FAILURE
DNS_EMPTY_RESULT
DNS_RESULT_LIMIT_EXCEEDED
DNS_NO_USABLE_TCP_ADDRESS
DNS_RESOLVER_ERROR
DNS_BOUNDARY_VIOLATION
```

P0 只有 `PASS` 或 `FAIL`。`PASS` 必须实际执行一次 resolver，存在 1–64 个可用唯一结果，
选中一个 family 并生成 opaque handle。`FAIL` 必须关闭 P1–P9；不得 synthetic PASS。

## Test Design

所有 PRE-64 tests 都是 offline fixture design，不执行 DNS 或 TCP。

### Positive cases

1. 单一 IPv4 TCP result；
2. 单一 IPv6 TCP result；
3. mixed family，选择 resolver order 中第一个唯一可用结果；
4. duplicate result 去重；
5. sanitized observation 不包含 hostname/IP/sockaddr；
6. P1 只消费同一 `ResolvedEndpoint` 与 handle。

### Negative cases

至少覆盖：

1. hostname 不在 allowlist；
2. hostname 是 IP literal；
3. port 不是 443；
4. resolver 被调用两次；
5. deadline 超时却返回 PASS；
6. name not found 映射错误；
7. temporary failure 映射错误；
8. empty result；
9. raw results 超过 64；
10. usable results 超过 64；
11. unsupported family；
12. non-stream socket；
13. non-TCP protocol；
14. malformed `sockaddr`；
15. selected address 不在 resolver output；
16. P1 handle mismatch；
17. P1 调用 resolver；
18. P1 使用 `socket.create_connection()`；
19. P1 发起第二次 connect；
20. P1 失败后 fallback 到第二地址；
21. TLS identity 改为 IP；
22. raw IP / hostname / exception string 进入 observation；
23. P0 synthetic PASS；
24. additional property 或未知 enum 被接受。

## Agent Recommendation Gate

```text
RECOMMENDATION=CONDITIONALLY_RECOMMENDED
```

### 不推荐原因

- resolver result order 跨平台不稳定；
- `getaddrinfo()` 自身没有 per-call timeout 参数；
- 单地址、无 fallback 会降低网络可用性；
- 内存态 IP 数据仍需实现级 privacy review；
- HTTPCore 默认 `connect_tcp()` 不满足一次 P0 / 一次 P1；
- 当前没有实现、真实平台测试或 formal Human Security Review。

### 本阶段修正

- selection rule 版本化并声明平台限制；
- deadline enforcement 设为必测 gate，不声称标准库自动提供；
- 禁止默认 backend、隐式重解析和 `create_connection()`；
- 通过 `ResolvedEndpoint` 与 opaque handle 定义 P0/P1 continuity；
- 将 raw address 限制在单请求内存；
- 冻结 6 positive + 24 negative case design；
- 准备独立 Agent Maintainer 与 Security Reviewer 输入。

### 剩余停止条件

在以下任一未完成时，不进入实现推荐：

- 至少一个 integration-maintainer agent review；
- 至少一个独立 provider security-review agent review；
- timeout、platform order、privacy 和 TLS identity 均有明确 disposition；
- contract/schema/test design 全部 hash-bound；
- target fileset、dependency、rollback 与 test command 尚未单独决定；
- P0 design 不得宣称 production availability。

## Exact Offline Outputs

PRE-64 只允许创建：

```text
commercialization-standards-p0-resolver-contract-and-test-design/
  p0-resolver-contract.v0.1.json
  p0-resolver-contract.schema.v0.1.json
  p0-resolver-negative-case-catalog.v0.1.json
  p0-resolver-negative-case-catalog.schema.v0.1.json
  p0-resolver-test-design.v0.1.json
  p0-resolver-test-design.schema.v0.1.json
  p0-resolver-agent-review-input.v0.1.json
  p0-resolver-agent-review-input.schema.v0.1.json
  pre64-validation-result.v0.1.json
  pre64-validation-result.schema.v0.1.json
  pre64-execution-receipt.v0.1.json
  pre64-execution-receipt.schema.v0.1.json
  PRE-64-P0-RESOLVER-CONTRACT-AND-TEST-DESIGN-RESULT-v0.1.md
```

以及独立治理记录：

```text
TITMAS-CS-D02-PRE-64-P0-RESOLVER-CONTRACT-AND-TEST-DESIGN-DECISION-RECORD.v0.1.json
architecture/schemas/titmas-cs-d02-pre64-p0-resolver-contract-and-test-design-decision-record.schema.v0.1.json
```

## Scope

```text
PRIMARY_REPOSITORY=digital-biosphere-architecture
OFFLINE_PACKET_FILES=13
NETWORK_REQUESTS_MAX=0
LIVE_MODEL_REQUESTS_MAX=0
CREDENTIAL_READS_MAX=0
TARGET_REPOSITORY_WRITES_MAX=0
DEPENDENCY_INSTALLS_MAX=0
IMPLEMENTATION_WRITES_MAX=0
```

## Validation

必须：

- 7 个 JSON instance 分别通过 frozen Draft 2020-12 Schema；
- 6/6 positive design cases 与 24/24 negative design cases 完整；
- mutation validator 至少拒绝 12 个关键边界变体；
- contract 明确 `getaddrinfo` 参数、结果 cap、selection、sanitization、continuity 和 closure；
- test design 禁止真实 DNS/TCP；
- Agent Review input 不包含 credential、private path、raw endpoint 或 hidden reasoning；
- receipt 绑定除自身外全部 PRE-64 artifacts；
- target commit 与 clean status 不变；
- remote clean clone 重复验证。

## Stop Conditions

以下任一发生立即停止：

- source/target hash 或 branch 漂移；
- P0 使用 synthetic PASS；
- P1 隐式重解析、使用 `create_connection()`、第二地址或 fallback；
- resolver timeout 被写成 Python 标准库已自动保证；
- platform-dependent order 被写成 cross-platform stable；
- raw IP、hostname、credential、Authorization、private path、raw body 或 hidden reasoning
  进入公共 artifact；
- 发生 network/model request、credential read、dependency install、target write 或实现；
- 形成 Provider support、conformance、security approval、release、production 或 commercial
  claim。

## Effects

```text
AUTHORITY_CHANGED=false
OWNERSHIP_CHANGED=false
TARGET_REPOSITORY_CHANGED=false
IMPLEMENTATION_AUTHORIZED=false
P0_RESOLVER_IMPLEMENTED=false
DEPENDENCY_ADOPTED=false
PROVIDER_INTEGRATION_AUTHORIZED=false
PROVIDER_SUPPORTED=false
FORMAL_SECURITY_REVIEW_AUTHORIZED=false
FORMAL_HUMAN_SECURITY_REVIEW_COMPLETE=false
NETWORK_EXECUTION_AUTHORIZED=false
EXTERNAL_EXECUTION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
STANDARD_READY=false
```

## Next Gate

PRE-64 PASS 只能进入：

```text
NEXT_ACTION=FORM_PRE65_P0_RESOLVER_CONTRACT_MULTI_PROVIDER_AGENT_REVIEW_RECOMMENDATION
```

该 review 仍是 AI-assisted input，不是 formal Human Security Review 或实现授权。

## Official Reference Pins

Observed `2026-07-27`:

- Python `socket.getaddrinfo()` and `socket.create_connection()`:
  `https://docs.python.org/3/library/socket.html`；
- HTTPCore extensions and `sni_hostname`:
  `https://www.encode.io/httpcore/extensions/`；
- HTTPCore 1.0.9 network backend base:
  `https://github.com/encode/httpcore/blob/1.0.9/httpcore/_backends/base.py`；
- HTTPCore 1.0.9 sync backend:
  `https://github.com/encode/httpcore/blob/1.0.9/httpcore/_backends/sync.py`。

Official documentation is reference evidence, not adoption, implementation or Provider support.

## Standing Directive Eligibility

本建议只有一个 exact option；primary repository、13-file packet、direct preconditions、
零网络/零 credential/零 target write、false effects 和 stop conditions 均明确。若形成
独立 Decision Record，可按 `TITMAS-CS-STANDING-001` 执行离线设计包；不得据此进入
target implementation。
