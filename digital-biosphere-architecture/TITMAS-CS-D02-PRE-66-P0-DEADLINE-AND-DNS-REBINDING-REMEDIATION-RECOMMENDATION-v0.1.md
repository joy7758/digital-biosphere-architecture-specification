---
document_id: DBA-TITMAS-CS-D02-PRE-66-P0-DEADLINE-AND-DNS-REBINDING-REMEDIATION-RECOMMENDATION-0.1
title: TITMAS P0 Deadline and DNS Rebinding Remediation Recommendation v0.1
title_zh: TITMAS P0 截止时间与 DNS 重绑定修复建议 v0.1
version: 0.1.0
status: exact-offline-remediation-design-recommended-not-decided
maturity: Development
maturity_scope: entire-document
primary_repository: digital-biosphere-architecture
decision_candidate: CS-D02-PRE-66
standing_directive_reference: TITMAS-CS-STANDING-001
recommended_by: Codex
recommended_at: 2026-07-27T11:22:00+08:00
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

# TITMAS P0 Deadline and DNS Rebinding Remediation Recommendation v0.1

## Recommendation

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=OFFLINE_P0_CONTRACT_REVISION_AND_EXECUTABLE_TEST_GATE_DESIGN
NOT_RECOMMENDED_AS=RESOLVER_IMPLEMENTATION_OR_FORMAL_SECURITY_APPROVAL
EXACT_OPTION=CREATE_VALIDATE_AND_REMOTE_FREEZE_PRE66_DEADLINE_AND_DNS_REBINDING_REMEDIATION_PACKET
```

如果开发者需要一个可审查的 P0/P1 transport boundary（传输边界），我会有条件推荐：

1. 将单次解析放入 single-use isolated subprocess（一次性隔离子进程）；
2. 以 5000 ms 作为“解析成功可被接受”的 monotonic admission deadline（单调时钟准入截止）；
3. 超时后必须 kill-and-wait（终止并等待）且在 worker 仍存活时禁止进入 P1；
4. 允许 selected sockaddr（已选套接字地址）只通过一次 bounded ephemeral local IPC
   （有界临时本地进程间通信）返回父进程；
5. 父进程对 numeric address（数值地址）执行版本化 destination policy，再固定该地址；
6. P1 直接连接同一地址，不重新解析；P2 继续用原始 allowlisted hostname 做 SNI 与证书校验。

我不会推荐直接实现。Python 官方文档说明 thread 不能被销毁、停止或中断；subprocess timeout
可以在超时后 kill 并 wait，但很多平台上的初始进程创建本身不能被 timeout 中断。因此，
跨平台纯 Python 设计不能诚实承诺“从调用开始到返回绝对不超过 5000 ms”。PRE-66 应修订
现有过强表述，而不是把不可证明的墙钟上限写成标准事实。

## Direct Evidence

```text
DBA_BASELINE_COMMIT=333677b08fe683336f982985c2456452689ec727
TARGET_COMMIT=5ac891c5af88b1e9aeacdb3666217c6f832a57a6
PRE65_RECOMMENDATION_SHA256=e70a061df19e37fc7c602dd6b32aaa349b6d0fef08f44c1b6da126fa9c4b2dea
PRE65_DECISION_SHA256=27619071c696cb3fb705b1c9c381b22f7fdc7638c185c211137b94d424c14e99
PRE64_CONTRACT_SHA256=4dd99f43cbe989e558129929a5f2d8c43d5d22645484137d666d55f52d0eacff
PRE64_TEST_DESIGN_SHA256=1264f92bd1cc15130fac8545ee6fde8c64996c1cc2d2c52120f81226d7bdcd27
PRE65_SANITIZED_RESULTS_SHA256=aa399e3a21e9b1c2d37bd3f1d410c48c81baf86525dbc14210d5e7339c33b2e4
PRE65_RECEIPT_SHA256=d0cb6aa3179d31839abfdf4eb08a86af409cf1b77c3c94dbec89f8d7ab905f58
PRE65_RESULT_SHA256=e11d47988b9f2b904e2c7b4184b9d7c07fa5941b04103b910f9b707c1748719c
```

这些 hash 绑定输入，不证明 finding 是已证实漏洞，也不证明修复、实现或安全审查完成。

## Mechanism Comparison

| candidate | hard cancellation | raw address continuity | portability | disposition |
|---|---|---|---|---|
| bounded thread + `join(timeout)` | 否；超时后线程可继续运行 | 同一进程内存，最好 | 高 | `REJECTED`：违反 no-background-resolution |
| signal/alarm around `getaddrinfo()` | 仅部分 POSIX/main-thread 组合 | 同一进程内存 | 低 | `REJECTED`：不是跨平台 Development profile |
| single-use subprocess | 可 terminate/kill/wait；process creation 仍有平台例外 | 需要一次临时 IPC | POSIX/Windows server/desktop candidate | `SELECTED_WITH_LIMITATIONS` |
| async/c-ares dependency | 可设计为 cancellable | 同一进程对象 | 需新依赖与新 resolver semantics | `DEFERRED`：dependency adoption 未授权 |
| platform-native resolver API | 取决于平台 | 可定制 | 很低 | `DEFERRED`：不适合作为 v0.1 通用参考 |

## Selected Deadline Semantics

推荐将 PRE-64 的单一 `timeout_budget_ms` 拆成：

```text
RESOLUTION_SUCCESS_ADMISSION_DEADLINE_MS=5000
DEADLINE_CLOCK=MONOTONIC
DEADLINE_START=IMMEDIATELY_BEFORE_WORKER_START_ATTEMPT
RESULT_ACCEPTED_AT_OR_AFTER_DEADLINE=false
P1_ALLOWED_AFTER_DEADLINE=false
WORKER_MUST_NOT_BE_ALIVE_BEFORE_RESOLVER_OPERATION_RETURNS=true
TOTAL_WALL_CLOCK_UPPER_BOUND_CLAIM=false
```

这意味着：5000 ms 后即使 worker 返回地址，也不得把 P0 标为 PASS；P1–P9 必须关闭。
父进程必须终止并等待 worker，只有确认 worker 不再存活后才能返回 P0 failure。由于 process
creation、调度和 kill/wait 在所有支持平台上没有共同的绝对墙钟保证，当前不声明总返回上限。

实现若不能证明：

```text
worker_started
worker_terminated_or_completed
worker_not_alive_before_return
late_result_rejected
```

则该平台不得声明 P0 deadline conformance。

## Ephemeral IPC Privacy Revision

一次性 subprocess 与 PRE-64 `ResolvedEndpoint.serialized=false` 存在真实冲突：子进程若只负责
解析而父进程负责连接，selected sockaddr 必须跨进程边界传递。建议将该约束修订为：

```text
PERSISTENT_SERIALIZATION_ALLOWED=false
PUBLIC_OBSERVATION_SERIALIZATION_ALLOWED=false
EPHEMERAL_LOCAL_IPC_SERIALIZATION_ALLOWED=true
IPC_SELECTED_ADDRESS_COUNT_MAX=1
IPC_PAYLOAD_BYTES_MAX=512
IPC_CREDENTIAL_CONTENT_ALLOWED=false
IPC_RAW_DNS_RESULT_SET_ALLOWED=false
IPC_LOGGING_ALLOWED=false
IPC_PERSISTENCE_ALLOWED=false
MEMORY_ZEROIZATION_CLAIM=false
```

worker 只返回一个已过滤、已选择的 numeric sockaddr 及固定元数据；不返回 hostname、完整
resolver result set、canonname、DNS packet、exception string、credential、header 或 body。
父进程形成非持久化 `EndpointBinding`，公开 phase observation 仍不得包含地址。

该修订是明确的 privacy trade-off（隐私取舍），不是“原约束仍完全成立”的文字游戏。

## DNS Rebinding / TOCTOU Disposition

DNS rebinding 不应通过第二次 DNS lookup 解决，因为第二次解析本身会创建新的
time-of-check/time-of-use（检查/使用时序）窗口，并违反 P1 `resolver_calls_max=0`。

推荐不变量：

```text
ALLOWLIST_CHECK=ORIGINAL_HOSTNAME_EXACT_MATCH_BEFORE_RESOLUTION
RESOLUTION_CALLS_MAX=1
DESTINATION_POLICY_CHECK=SELECTED_NUMERIC_ADDRESS_BEFORE_P1
DESTINATION_POLICY=GLOBAL_UNICAST_DESTINATION_PROFILE_V1
ADDRESS_PINNING=SAME_SELECTED_SOCKADDR_P0_TO_P1
P1_RERESOLUTION_ALLOWED=false
P1_ALTERNATE_ADDRESS_ALLOWED=false
TLS_IDENTITY=ORIGINAL_EXACT_ALLOWLISTED_HOSTNAME
```

`GLOBAL_UNICAST_DESTINATION_PROFILE_V1` 必须绑定冻结的 IANA IPv4/IPv6 special-purpose
registry snapshot（特殊用途地址注册表快照）和 digest。没有 snapshot、digest 或 policy
version 时失败关闭。默认拒绝 non-global、loopback、link-local、private-use、shared、
documentation、benchmark、multicast、unspecified 与 reserved destination；例外必须有独立
policy Decision，不能由 DNS 结果自动授权。

这里的安全含义是：

- hostname allowlist 约束“允许向哪个服务名发起请求”；
- numeric destination policy 约束“不得连接哪些地址空间”；
- address pinning 防止 P1 静默使用另一个解析结果；
- TLS original-hostname verification 约束对端证书身份；
- 上述组合降低 rebinding/SSRF 风险，但不证明 DNS 数据本身真实，也不产生 Trust。

## Revised Continuity Object

父进程中的非持久化对象改名为 `EndpointBinding`：

```text
original_hostname
port
family
socket_type
protocol
selected_sockaddr
resolution_handle_ref
resolver_worker_receipt_ref
destination_policy_id
destination_policy_snapshot_sha256
resolved_at_monotonic_ns
success_admission_deadline_monotonic_ns
```

P1 必须消费同一对象和 handle；不得接受只复制字段后重新构造、重新解析或更换地址的对象。
测试必须覆盖 object identity 或 sealed-binding digest continuity，具体实现选择留给后继
implementation Recommendation，不在 PRE-66 虚构代码能力。

## Deterministic Failure Classification

新增或细化：

```text
DNS_WORKER_START_FAILURE
DNS_TIMEOUT
DNS_LATE_RESULT
DNS_WORKER_TERMINATION_UNCONFIRMED
DNS_IPC_BOUNDARY_VIOLATION
DNS_DESTINATION_POLICY_REJECTED
DNS_DESTINATION_POLICY_UNAVAILABLE
DNS_NO_USABLE_TCP_ADDRESS
```

platform order 不稳定不触发 fallback。若所有返回项均 unusable，稳定映射为
`DNS_NO_USABLE_TCP_ADDRESS`；若第一个按规则选中的地址被 destination policy 拒绝，不尝试
第二地址，映射为 `DNS_DESTINATION_POLICY_REJECTED`。这是刻意的 fail-closed availability
trade-off，不是可靠性保证。

## Executable-Test Gate

在任何 target implementation Recommendation 前，必须先冻结：

1. worker process lifecycle harness；
2. late-result rejection；
3. terminate/kill/wait 后 `is_alive=false`；
4. process-start failure；
5. IPC 超长、额外字段、完整 result set 与敏感字段拒绝；
6. IPv4、IPv6、IPv4-mapped IPv6 destination policy；
7. special-purpose registry snapshot/digest mismatch；
8. P0/P1 same-address continuity；
9. P1 zero re-resolution、zero fallback、one connect；
10. P2 original-hostname SNI/certificate identity；
11. prior 6 positive + 24 negative cases 的 migration mapping；
12. supported-platform matrix 与 unsupported-platform fail-closed behavior。

PRE-66 只定义 gate，不创建或执行测试。后继实施建议必须固定 target paths、test command、
Python/platform matrix、dependency decision、rollback 和 independently reviewable results。

## Exact Offline Outputs

PRE-66 只允许在 DBA 创建：

```text
commercialization-standards-p0-deadline-and-dns-rebinding-remediation/
  remediation-input-manifest.v0.1.json
  remediation-input-manifest.schema.v0.1.json
  deadline-mechanism-comparison.v0.1.json
  deadline-mechanism-comparison.schema.v0.1.json
  dns-rebinding-mitigation-contract.v0.1.json
  dns-rebinding-mitigation-contract.schema.v0.1.json
  p0-contract-revision-candidate.v0.2.json
  p0-contract-revision-candidate.schema.v0.2.json
  pre66-validation-result.v0.1.json
  pre66-validation-result.schema.v0.1.json
  pre66-execution-receipt.v0.1.json
  pre66-execution-receipt.schema.v0.1.json
  PRE-66-P0-DEADLINE-AND-DNS-REBINDING-REMEDIATION-RESULT-v0.1.md
```

以及独立治理记录：

```text
TITMAS-CS-D02-PRE-66-P0-DEADLINE-AND-DNS-REBINDING-REMEDIATION-DECISION-RECORD.v0.1.json
architecture/schemas/titmas-cs-d02-pre66-p0-deadline-and-dns-rebinding-remediation-decision-record.schema.v0.1.json
```

## Validation and Stop Conditions

必须：

- 6 个 JSON instance 通过各自 Draft 2020-12 Schema；
- deadline comparison 恰好覆盖 thread、signal、subprocess、async、native 五种候选；
- contract revision 显式写出 `total_wall_clock_upper_bound_claim=false`；
- DNS mitigation 不得进行第二次解析；
- raw address 只能进入 bounded ephemeral local IPC，不得进入公开 observation、Git 或日志；
- receipt 绑定除自身外全部 PRE-66 artifact SHA-256；
- 至少 12 个 mutation negative 全部被 Schema 或 cross-artifact validator 拒绝；
- target repo 保持 exact commit 且 clean；
- 保留 formal Human Security Review、implementation、provider support 和 standard readiness 为 false。

以下任一发生立即停止：

- 把 DNS re-check 写成允许的 rebinding mitigation；
- 把 `subprocess timeout` 写成跨平台绝对墙钟保证；
- 忽略 transient raw-address serialization 与 PRE-64 的冲突；
- 未绑定 destination-policy snapshot/digest 却允许 P0 PASS；
- worker 仍存活却允许 resolver operation 返回或进入 P1；
- 发生 target write、credential read、network/model request、dependency install 或实现修改；
- 产生漏洞证明、Provider support/conformance、formal Security Review、release 或 commercial claim。

## Effects

```text
AUTHORITY_CHANGED=false
OWNERSHIP_CHANGED=false
TARGET_REPOSITORY_CHANGED=false
IMPLEMENTATION_AUTHORIZED=false
PROVIDER_INTEGRATION_AUTHORIZED=false
PROVIDER_SUPPORTED=false
FORMAL_SECURITY_REVIEW_AUTHORIZED=false
FORMAL_HUMAN_SECURITY_REVIEW_COMPLETE=false
DEPENDENCY_ADOPTED=false
P0_REMEDIATION_IMPLEMENTED=false
TESTS_CREATED=false
TESTS_EXECUTED=false
NETWORK_EXECUTED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
STANDARD_READY=false
AGENT_CREATED=false
RUNTIME_CREATED=false
PERMISSION_CREATED=false
```

## Next Gate

PRE-66 通过只允许形成：

```text
NEXT_ACTION=FORM_PRE67_P0_EXECUTABLE_TEST_AND_IMPLEMENTATION_SCOPE_RECOMMENDATION
```

后继仍必须先有独立 Recommendation 与 Decision；不得自动写入 `titmas-integrations`。

## Standing Directive Eligibility

本建议只有一个 exact option，输入 hash、target、13-file output、零网络、零 credential、
零 target write、false effects 与 fail-closed conditions 均已明确。若独立 Decision Record
形成，可按 `TITMAS-CS-STANDING-001` 执行离线包；该指令不授权后继实现、测试执行或正式
Security Review。
