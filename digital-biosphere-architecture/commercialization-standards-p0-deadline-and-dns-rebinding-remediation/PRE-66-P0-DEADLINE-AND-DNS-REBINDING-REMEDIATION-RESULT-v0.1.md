---
document_id: TITMAS-CS-D02-PRE-66-P0-DEADLINE-AND-DNS-REBINDING-REMEDIATION-RESULT-0.1
title: TITMAS PRE-66 P0 Deadline and DNS Rebinding Remediation Result v0.1
title_zh: TITMAS PRE-66 P0 截止时间与 DNS 重绑定修复结果 v0.1
version: 0.1.0
status: pass-offline-remediation-design-only
maturity: Development
maturity_scope: entire-document
executed_at: 2026-07-27T11:29:00+08:00
formal_security_review_completed: false
implementation_authorized: false
standard_ready: false
---

# TITMAS PRE-66 P0 Deadline and DNS Rebinding Remediation Result v0.1

## Outcome

```text
OFFLINE_REMEDIATION_DESIGN_PASS=true
DEADLINE_MECHANISM_SELECTED_IN_DESIGN=SINGLE_USE_SUBPROCESS_TIMEOUT_V1
RESOLUTION_SUCCESS_ADMISSION_DEADLINE_MS=5000
TOTAL_WALL_CLOCK_UPPER_BOUND_CLAIM=false
DNS_RERESOLUTION_MITIGATION_ALLOWED=false
DESTINATION_POLICY_SNAPSHOT_ADOPTED=false
P0_CONTRACT_REVISION_ADOPTED=false
TESTS_CREATED=false
TESTS_EXECUTED=false
IMPLEMENTATION_AUTHORIZED=false
FORMAL_HUMAN_SECURITY_REVIEW_COMPLETE=false
STANDARD_READY=false
```

PRE-66 完成了一个有界的 contract revision candidate（契约修订候选）。它解决的是设计
诚实性和可实现性边界，不是 resolver 实现或安全批准。

## Deadline Disposition

五种候选机制已比较：

1. thread + timed join：拒绝；Python thread 超时后可能继续解析；
2. signal/alarm：拒绝；平台与线程上下文限制过强；
3. single-use subprocess：有条件选择；
4. async/c-ares：依赖尚未授权，延后；
5. platform-native resolver：不适合作为通用 v0.1 参考，延后。

5000 ms 被修订为“解析成功准入截止”。超时或迟到结果不能进入 P1；worker 必须在 resolver
operation 返回前被确认停止。因为进程创建、调度和终止没有共同的跨平台绝对时限，本候选
明确保持 `TOTAL_WALL_CLOCK_UPPER_BOUND_CLAIM=false`。

## Privacy Trade-off

PRE-64 的 `serialized=false` 与 subprocess 隔离不可同时完整满足。PRE-66 明确允许最多
512 bytes、最多一个 selected address 的 ephemeral local IPC（临时本地 IPC），同时禁止：

- 持久化或日志；
- 公开 phase observation；
- 完整 DNS result set；
- hostname、credential、header、body 与 exception string；
- memory zeroization（内存清零）能力声明。

这是显式的 contract revision，不是对旧约束的静默绕过。

## DNS Rebinding / TOCTOU Disposition

设计不做第二次 DNS lookup。采用：

```text
exact hostname allowlist
  -> one DNS resolution
  -> one selected numeric address
  -> versioned destination-policy check
  -> pin same sockaddr into P1
  -> original hostname TLS verification in P2
```

destination policy 必须绑定冻结的 IANA IPv4/IPv6 special-purpose registry snapshot 和
SHA-256。当前 snapshot 尚未采纳，因此该 policy 不得被写成已可运行。该组合降低
rebinding/SSRF 风险，不证明 DNS Truth、Peer Truth、Permission 或 Authority。

## Validation

```text
SCHEMA_DEFINITIONS_VALID=6/6
SCHEMA_INSTANCES_VALID=6/6
INPUT_HASHES_MATCHED=7/7
DEADLINE_CANDIDATES_EXACT=5/5
CROSS_ARTIFACT_CHECKS=4/4
MUTATION_NEGATIVES_REJECTED=12/12
TARGET_COMMIT_MATCHED=true
TARGET_CLEAN=true
SECRET_OR_PRIVATE_PATH_FINDINGS=0
```

12 个 mutation negative 覆盖 target drift、额外字段、候选缺失、错误选择 thread、墙钟
过度声明、DNS re-check、policy digest 缺失、地址 fallback、错误 worker、公开 raw address
以及虚假 tests-executed。

## Executable-Test Gate

PRE-67 若继续，必须先形成独立 Recommendation 与 Decision，并固定：

- worker lifecycle、timeout、late result、kill/wait；
- IPC privacy 和 512-byte bound；
- IANA snapshot/digest 与 IPv4/IPv6 policy；
- P0/P1 same-address continuity；
- P1 zero re-resolution / zero fallback；
- P2 original-hostname TLS；
- PRE-64 的 6 positive + 24 negative case migration；
- Python/platform matrix、exact fileset、test command、rollback。

该 gate 尚未创建或执行任何测试。

## Boundary Effects

```text
AUTHORITY_CHANGED=false
OWNERSHIP_CHANGED=false
TARGET_REPOSITORY_CHANGED=false
DBOS_CHANGED=false
SAEE_CHANGED=false
NETWORK_EXECUTED=false
CREDENTIAL_READ=false
DEPENDENCY_ADOPTED=false
P0_RESOLVER_IMPLEMENTED=false
TESTS_CREATED=false
TESTS_EXECUTED=false
PROVIDER_SUPPORT_CREATED=false
FORMAL_SECURITY_REVIEW_COMPLETED=false
CUSTOMER_EVIDENCE_CREATED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
STANDARD_READY=false
```

## Final Status

```text
CS_D02_PRE_66_OFFLINE_REMEDIATION_DESIGN_COMPLETE=true
CS_D02_PRE_66_CONTRACT_REVISION_ADOPTED=false
CS_D02_PRE_66_IMPLEMENTATION_AUTHORIZED=false
CS_D02_PRE_66_EXECUTABLE_TEST_GATE_REQUIRED=true
NEXT_ACTION=FORM_PRE67_P0_EXECUTABLE_TEST_AND_IMPLEMENTATION_SCOPE_RECOMMENDATION
TITMAS_STANDARD_READY=false
```
