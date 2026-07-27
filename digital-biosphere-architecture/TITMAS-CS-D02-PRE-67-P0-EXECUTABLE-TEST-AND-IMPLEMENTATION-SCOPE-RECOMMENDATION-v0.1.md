---
document_id: DBA-TITMAS-CS-D02-PRE-67-P0-EXECUTABLE-TEST-AND-IMPLEMENTATION-SCOPE-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-67 P0 Executable Test and Implementation Scope Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-67 P0 可执行测试与实现范围建议 v0.1
version: 0.1.0
status: exact-recommendation-ready-not-decided
maturity: Development
recommendation_id: CS-D02-PRE-67
primary_repository: digital-biosphere-architecture
target_repository: https://github.com/joy7758/titmas-integrations.git
target_write_authorized: false
implementation_authorized: false
network_execution_authorized: false
release_authorized: false
---

# TITMAS CS-D02 PRE-67 P0 Executable Test and Implementation Scope Recommendation v0.1

## Recommendation

```text
RECOMMENDATION=AUTHORIZE_EXACT_POSIX_SINGLE_USE_CHILD_P0_RESOLVER_REFERENCE_IMPLEMENTATION_AND_OFFLINE_TESTS
PRIMARY_REPOSITORY=digital-biosphere-architecture
TARGET_REPOSITORY=https://github.com/joy7758/titmas-integrations.git
TARGET_BRANCH=codex/rb0-governance-baseline
TARGET_HEAD=5ac891c5af88b1e9aeacdb3666217c6f832a57a6
NEW_FILES_MAX=11
UPDATED_FILES_MAX=8
NEW_PUBLIC_SYMBOLS_MAX=6
RUNTIME_DEPENDENCIES_MAX=0
PROVIDER_DEPENDENCIES_MAX=0
REAL_DNS_CALLS_DURING_TESTS_MAX=0
REAL_TCP_CALLS_DURING_TESTS_MAX=0
PROVIDER_BINDINGS_MAX=0
RUNTIME_INSTANCES_MAX=0
RELEASES_MAX=0
```

PRE-64 固定了 6 个 positive 和 24 个 negative case；PRE-65 的多模型咨询指出
deadline、DNS rebinding、result-set privacy 和 endpoint continuity 是阻止推荐的主要
原因；PRE-66 选择了 single-use child process（单次子进程）和 same-address pinning
（同地址固定）设计，但没有采纳 contract、实现 resolver 或执行测试。

本建议只授权候选的下一步范围：一个 POSIX-only、Development、provider-neutral、
默认 fail-closed 的 P0 resolver reference implementation，以及完全离线的测试。它不授权
Provider adapter、P1 TCP、P2 TLS、HTTP 请求、DBOS/SAEE 写入、Runtime、release 或正式
security approval。

## Agent Recommendation Gate

### User problem

现有仓库只能表达 P0–P9 observation（观察记录），不能证明 P0 DNS deadline、地址过滤和
P0→P1 连续性能被实现。开发者因此不能把它推荐为可执行的 P0 安全边界参考。

### Current recommendation

独立 Agent 现在只应推荐该仓库用于：

- immutable P0–P9 phase-trace data contract；
- local serialized-contract rehearsal。

不应推荐用于 P0 resolver、DNS rebinding mitigation、SSRF destination policy 或网络执行。

### What prevents recommendation

1. PRE-66 revision candidate 尚未被 Decision 采纳；
2. IANA IPv4/IPv6 registry snapshot 尚未冻结；
3. worker lifecycle、deadline、kill/wait、late-result 和 IPC bound 没有 executable tests；
4. P0→P1 same-address 和 P2 original-hostname 只有设计，没有离线 executable proof；
5. 目标仓库的 public API、truth surface、rollback 和 platform boundary 尚未冻结；
6. 没有 formal human security review、Linux/Windows matrix 或 release evidence。

### Smallest correction

建立一个可替换的小边界：

```text
exact canonical hostname allowlist
  -> one POSIX child resolver
  -> one bounded selected-address result
  -> frozen IANA snapshot policy
  -> transient EndpointBinding
  -> offline continuity validation
```

这不是中心平台，也不创建 Agent、Permission 或 Authority。

## Official Snapshot Inputs

PRE-67 只允许采用下列两个 IANA Protocol Registry CSV 原始字节：

| family | official URL | source last updated | bytes | SHA-256 |
|---|---|---:|---:|---|
| IPv4 | `https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry-1.csv` | `2025-10-09` | `2423` | `e3e39e76d00b1677335db8e9a805c7b9480ea2f4dc9e33f0b93cd3a905128d73` |
| IPv6 | `https://www.iana.org/assignments/iana-ipv6-special-registry/iana-ipv6-special-registry-1.csv` | `2025-10-09` | `2289` | `775feea0621dec8735a44fbf30f762e721e8f0a1b3ab7eb341961a88cfce2139` |

检索时间为 `2026-07-27T11:42:00+08:00`。IANA/IETF 的 Protocol Registries licensing
statement 将适用权利置于 CC0 1.0；该许可事实只支持 vendoring，不构成 registry 数据
正确、完整、实时或适用于任何目标网络的保证。

目标实现必须在每次加载 policy 时校验这两个 digest。缺失、漂移、无法解析或 source
metadata 不匹配时 fail closed。实现不得联网更新 snapshot，也不得把未来 registry 变化
自动采纳为当前标准。

## Exact Target Fileset

只允许新增 11 个文件：

1. `src/titmas_integrations/p0_resolver.py`
2. `src/titmas_integrations/_p0_resolver_worker.py`
3. `src/titmas_integrations/data/__init__.py`
4. `src/titmas_integrations/data/iana-ipv4-special-registry-2025-10-09.csv`
5. `src/titmas_integrations/data/iana-ipv6-special-registry-2025-10-09.csv`
6. `src/titmas_integrations/data/global-unicast-destination-policy.v1.json`
7. `tests/test_p0_resolver_contract.py`
8. `tests/test_p0_resolver_deadline.py`
9. `tests/test_p0_resolver_security.py`
10. `P0-IMPLEMENTATION-DECLARATION.v0.1.json`
11. `schemas/p0-implementation-declaration.schema.v0.1.json`

只允许更新 8 个文件：

1. `src/titmas_integrations/__init__.py`
2. `pyproject.toml`
3. `README.md`
4. `AGENTS.md`
5. `SECURITY.md`
6. `llms.txt`
7. `TITMAS-INTEGRATIONS-ENTRY.v0.1.json`
8. `schemas/titmas-integrations-entry.schema.v0.1.json`

禁止修改或删除其他路径。特别是：

- `src/titmas_integrations/instrumentation.py` 保持冻结；
- 现有 7 个 conformance fixtures 和 validator 保持冻结；
- `IMPLEMENTATION-DECLARATION.v0.1.json` 保持 PRE-48 历史声明；
- Provider/Framework 占位目录保持空；
- `main` 不变。

## Public API Candidate

Decision 如采纳，只允许新增以下 6 个 public symbols：

- `EndpointBinding`
- `P0ResolverObservation`
- `P0ResolverResult`
- `ResolverFailureCategory`
- `resolve_endpoint`
- `validate_endpoint_continuity`

`EndpointBinding` 是单次 request 范围内的 transient capability carrier（临时能力载体）：

- 不提供 `to_dict()`；
- `repr` 必须隐藏 hostname、address 和 sockaddr；
- pickle/copy/deepcopy 必须 fail closed；
- 不能进入 public observation、log、receipt 或 persistence；
- 不创建 Permission、Authorization、Evidence 或 Truth。

`resolve_endpoint` 只接受 canonical lowercase ASCII hostname、exact immutable allowlist、
port `443` 和固定 `5000 ms` admission deadline。它不接受任意 command、resolver callback、
timeout override、policy override、retry、fallback 或 Provider 参数。

## Worker and Deadline Contract

允许的实现机制：

```text
PLATFORM_GUARD=POSIX_WITH_OS_FORK_AND_WAITPID
PROCESS_MODEL=SINGLE_USE_CHILD_PROCESS_PER_RESOLUTION
SHELL_ALLOWED=false
CHILDREN_OF_WORKER_ALLOWED=false
RESOLVER_INVOCATIONS_MAX=1
SUCCESS_ADMISSION_DEADLINE_MS=5000
DEADLINE_CLOCK=MONOTONIC
TOTAL_WALL_CLOCK_UPPER_BOUND_CLAIM=false
```

父进程必须在 child creation attempt 前记录 monotonic deadline。child：

- 立即清除继承的 environment mapping；
- 捕获并映射错误类别，不输出 exception string；
- 只调用一次 fixed `socket.getaddrinfo`；
- 最多返回一个 selected numeric sockaddr；
- 通过 local one-way pipe 写入不超过 512 bytes 的 canonical JSON；
- 不写 stderr、log、file、socket 或 persistence store；
- 不创建 child。

父进程：

- 只读最多 513 bytes，用第 513 byte 检测越界；
- deadline 后拒绝 late result；
- timeout/boundary violation 后终止 child 并 `waitpid`；
- resolver operation 返回前必须确认 child 不再存活；
- termination 无法确认时返回 `DNS_WORKER_TERMINATION_UNCONFIRMED`；
- 不把 raw IPC、hostname、IP、sockaddr 或 exception string 写入 observation。

由于 fork/process creation 和 post-kill wait 没有统一的跨平台绝对中断保证，本实现不得声称
总 wall-clock 上界。Windows、Android、iOS、WASI 和无 `fork` 平台必须在调用 resolver
前 fail closed；这不是支持矩阵。

## Destination Policy

`GLOBAL_UNICAST_DESTINATION_PROFILE_V1` 的运行规则：

1. policy manifest、IPv4 CSV 和 IPv6 CSV digest 全部匹配；
2. 只接受 `AF_INET` / `AF_INET6`、`SOCK_STREAM`、`IPPROTO_TCP`、port `443`；
3. 对 special-purpose registry 使用 most-specific prefix match；
4. 命中项只有 `Destination=True` 且 `Globally Reachable=True` 才允许；
5. 空值、`False`、带 footnote 的 `False`、`N/A` 或未知值全部拒绝；
6. 未命中 special-purpose registry 的地址仍须拒绝 unspecified、loopback、link-local、
   multicast 和 reserved fundamental classes；
7. policy rejection 不尝试下一个 address；
8. 自动 exception、allow override 和 caller-supplied policy 禁止。

该 policy 是保守的 Development profile，不证明 destination 可达、DNS Truth、Peer Truth、
TLS identity、Permission 或 Authority。

## Endpoint Continuity Boundary

P0 success 只产生一个 transient `EndpointBinding` 和 sanitized observation。离线
`validate_endpoint_continuity` 必须验证：

- P1 使用同一个 object identity；
- P1 resolver call count 为 `0`；
- P1 connect attempt count 不超过 `1`；
- alternate/fallback count 为 `0`；
- P1 numeric sockaddr 与 P0 固定值相同；
- P2 TLS `server_hostname` 等于原 exact allowlisted hostname。

该函数只验证输入的 offline consumption record，不创建 socket、不 connect、不做 TLS。
真实 P1/P2 实现不在 PRE-67 范围内。

## Exact Executable Test Matrix

测试命令固定：

```text
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -v
```

所有新增测试必须使用 Python standard library 和 injected fork-safe fakes；测试期间：

```text
REAL_DNS_CALLS=0
REAL_TCP_CONNECTS=0
TLS_HANDSHAKES=0
HTTP_REQUESTS=0
CREDENTIAL_READS=0
DEPENDENCY_INSTALLS=0
```

必须执行：

### PRE-64 migration

- `P0-POS-001` 至 `P0-POS-006`：6/6；
- `P0-NEG-001` 至 `P0-NEG-024`：24/24。

### PRE-66 additions

1. child start failure；
2. timeout kills and waits child；
3. late result is rejected；
4. unconfirmed termination fails closed；
5. worker exits without payload；
6. non-zero/abnormal child exit；
7. IPC payload 513 bytes；
8. malformed JSON；
9. unknown/additional IPC field；
10. more than one selected address；
11. hostname in IPC；
12. exception string in IPC；
13. inherited credential-named environment is absent in worker；
14. snapshot missing；
15. snapshot digest drift；
16. IPv4 private/loopback/link-local/shared/documentation/benchmark/multicast/reserved；
17. IPv6 loopback/unspecified/unique-local/link-local/documentation/multicast；
18. most-specific allowed IPv4 entry；
19. most-specific allowed IPv6 entry；
20. P1 re-resolution；
21. P1 second connect；
22. P1 alternate/fallback；
23. P1 changed sockaddr；
24. P2 IP-as-server-hostname；
25. `EndpointBinding` repr/pickle/copy/deepcopy boundary；
26. public observation contains no hostname/IP/sockaddr/raw payload/exception/credential；
27. no Provider/DBOS/SAEE imports；
28. no network call during unit test process；
29. unsupported platform preflight failure；
30. existing 30 tests and 7/7 local rehearsal remain unchanged and pass。

如果任何 test、digest、inventory、environment boundary 或 child liveness check 失败，保留首个
失败并停止，不形成 implementation pass。

## Platform Truth

PRE-67 只允许声明：

```text
IMPLEMENTATION_PLATFORM_REQUIREMENT=POSIX_OS_FORK_WAITPID
OBSERVED_LOCAL_VALIDATION_PLATFORM=Darwin-arm64-macOS-26.5.2-CPython-3.14.5
LINUX_VALIDATED=false
WINDOWS_SUPPORTED=false
MOBILE_SUPPORTED=false
WEBASSEMBLY_SUPPORTED=false
CROSS_PLATFORM_SUPPORT_CLAIM=false
```

源代码可以在其他 POSIX 环境接受后续独立验证，但本次本地 pass 不能升级为 Linux 或通用
生产支持。

## Truth-surface Updates

只有实际实现、全部测试、schema、inventory、old conformance 和 remote clean-clone 全部
通过后，truth surface 才可更新为：

```text
MATURITY=Development
P0_RESOLVER_REFERENCE_IMPLEMENTATION_CREATED=true
BOUNDED_DNS_CAPABILITY_IMPLEMENTED=true
NETWORK_CALLS_EXECUTED_DURING_VALIDATION=0
P1_TCP_IMPLEMENTED=false
P2_TLS_IMPLEMENTED=false
PROVIDER_BINDINGS=0
PROVIDER_SUPPORTED=false
PROVIDER_CONFORMANCE_EXECUTED=false
FORMAL_SECURITY_REVIEW_COMPLETE=false
RUNTIME_CREATED=false
RELEASE_AUTHORIZED=false
COMMERCIAL_AVAILABILITY=NOT_CLAIMED
```

`NETWORK_EXECUTION_IMPLEMENTED=false` 不能继续用于整个 package，因为 P0 resolver 代码将
具备调用 OS resolver 的能力；必须改成更精确的字段，区分“能力已实现”和“验证期间未执行
真实网络”。

## Validation and Result Requirements

实现后必须：

1. target HEAD、branch 和 clean state 与本建议一致；
2. 校验 11 new + 8 updated path inventory，其他 tracked path digest 不变；
3. 校验 vendored IANA bytes 和 policy manifest；
4. 执行全部 unit tests；
5. 执行现有 7/7 independent-path local rehearsal；
6. 验证两个 implementation declaration 和 entry schema；
7. 扫描 credential/raw payload/private path/Provider/DBOS/SAEE boundary；
8. 使用临时目录执行 offline build；缺依赖则 fail closed，不联网安装；
9. 提交并 push 到 `codex/rb0-governance-baseline`，不触碰 `main`；
10. 从远端 fresh clone 执行同一 test、rehearsal、schema 和 inventory checks；
11. 在 DBA 保存 result、validation result、execution receipt 和 exact target commit；
12. cockpit 仍保持 formal security review、release 和 standard-ready 为 false。

## Rollback

```text
TARGET_PARENT=5ac891c5af88b1e9aeacdb3666217c6f832a57a6
ROLLBACK_MEANING=RESTORE_PRE49_DEVELOPMENT_REFERENCE_BASELINE
ROLLBACK_METHOD=FOLLOWUP_COMMIT_ONLY
HISTORY_REWRITE_ALLOWED=false
FORCE_PUSH_ALLOWED=false
MAIN_BRANCH_WRITE_ALLOWED=false
```

回滚必须删除 11 个新增文件并恢复 8 个更新文件。失败记录不得静默删除。

## Non-effects

```text
RECOMMENDATION_IS_DECISION=false
RECOMMENDATION_IS_IMPLEMENTATION=false
TARGET_WRITE_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
REAL_NETWORK_EXECUTION_AUTHORIZED=false
PROVIDER_BINDING_CREATED=false
PROVIDER_SUPPORTED=false
CONFORMANCE_EXECUTED=false
FORMAL_SECURITY_REVIEW_COMPLETED=false
DBOS_CHANGED=false
SAEE_CHANGED=false
AGENT_CREATED=false
RUNTIME_CREATED=false
ENTITY_CREATED=false
PERMISSION_GRANTED=false
EVIDENCE_CREATED=false
EVIDENCE_TRUTH_CHANGED=false
MERGE_AUTHORIZED=false
PULL_REQUEST_AUTHORIZED=false
RELEASE_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
STANDARD_READY=false
```

## Stop Conditions

以下任一情况立即停止：

- target commit、19-path fileset、6 public symbols 或 snapshot bytes 漂移；
- 需要真实 DNS/TCP/TLS/HTTP、credential、Provider API、dependency install；
- 需要 P1/P2 implementation、retry、fallback、address exception 或 policy override；
- child 不能停止并确认回收；
- IPC 超过 512 bytes 或出现 hostname/exception/credential；
- 旧 30 tests、7/7 rehearsal 或新增 test 任一失败；
- 需要 DBOS/SAEE、main、merge、PR、tag、release、deployment、certification 或 commercial
  claim；
- 需要声称 total wall-clock bound、cross-platform support 或 formal security approval。

## Standing Directive Assessment

本建议只有一个 exact option，固定 repository/branch/commit、19 paths、6 public symbols、
2 official snapshot digests、0 dependencies、0 validation network calls、platform guard、test
matrix、rollback、truth surface、non-effects 和 stop conditions，满足
`TITMAS-CS-STANDING-001` 的候选条件。

本文件只是 Recommendation。任何目标仓库写入、contract adoption、implementation 或 test
execution 之前，仍须单独的 PRE-67 Decision Record。
