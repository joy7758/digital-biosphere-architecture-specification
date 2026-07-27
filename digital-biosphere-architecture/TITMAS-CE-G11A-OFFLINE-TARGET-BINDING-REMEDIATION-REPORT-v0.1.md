---
document_id: DBA-TITMAS-CE-G11A-OFFLINE-TARGET-BINDING-REMEDIATION-REPORT-0.1
title: TITMAS CE-G11A Offline Target-Binding Remediation Report v0.1
title_zh: TITMAS CE-G11A 离线目标绑定修正报告 v0.1
version: 0.1.0
status: pass-offline-target-binding-remediation-only
maturity: Development
maturity_scope: ce-g11-correlation-target-and-identity-binding-remediation
owner_ref: zhangbin
recommendation_reference: TITMAS-CE-G11A-OFFLINE-TARGET-BINDING-REMEDIATION-RECOMMENDATION-v0.1.md
decision_reference: TITMAS-COMMERCIAL-EVALUATION-CE-G11A
authorization_baseline_commit: 6747714c6dcb793a3e648d8875e9adeeebdf4102
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G11A Offline Target-Binding Remediation Report v0.1

## 1. Outcome

```text
CE_G11A_RESULT=PASS_OFFLINE_TARGET_BINDING_REMEDIATION_ONLY
BINDING_SCHEMA_PASS=true
NEW_TESTS_PASS=13/13
HISTORICAL_CE_G9_TESTS_PASS=13/13
TOTAL_TESTS_PASS=26/26
FULL_CE_G_DISCOVERY_TESTS_PASS=35/35
LOCAL_PYTHON_3_13_12_TESTS_PASS=13/13
LOCAL_PYTHON_3_14_5_TESTS_PASS=13/13
NEGATIVE_CASES_REJECTED=9/9
HISTORICAL_HASHES_MATCH=true
OFFLINE_FIXTURE_AUTHORIZATION_STATUS=NOT_AUTHORIZED
BINDING_AUTHORITY_EFFECT=false
```

Machine result：

[`ce-g11a-offline-remediation-result.v0.1.json`](commercial-evaluation-controller-tls-diagnosis/ce-g11a-offline-remediation-result.v0.1.json)

## 2. Implemented bounded artifacts

| Artifact | Purpose |
|---|---|
| `ce-g11-correlation-binding.schema.v0.1.json` | exact offline binding contract |
| `ce-g11-correlation-binding.offline-fixture.v0.1.json` | `NOT_AUTHORIZED` test fixture |
| `ce_g11_target_bound_correlator.py` | minimal target/identity adapter |
| `test_ce_g11_target_bound_correlator.py` | positive, negative, privacy and reuse tests |
| `ce-g11a-offline-remediation-result.schema.v0.1.json` | fail-closed result contract |
| `ce-g11a-offline-remediation-result.v0.1.json` | bounded execution receipt |

adapter 复用 historical：

```text
parse_iso
access_records
error_classes
journal_classes
```

没有复制或修改 access/error timestamp parsing、source hashing 或 journal
classification semantics。

## 3. Binding boundary

offline fixture 精确绑定：

```text
binding_id=TITMAS-CE-G11-CORRELATION-BINDING-OFFLINE-001
declared_decision_reference=TITMAS-COMMERCIAL-EVALUATION-CE-G11
receipt_id=TITMAS-CE-G11-SERVER-CORRELATION-001
expected_current_release=/srv/tmai/releases/f8107969aa1f43be8ecf43f557297a630309fe41
authorization_status=NOT_AUTHORIZED
authority_effect=false
```

adapter 在使用字段前验证 expected SHA-256 和 exact binding shape。wrong Decision、
wrong receipt、stable/unknown target、tamper、`AUTHORIZED` offline status、
`authority_effect=true` 和 additional property 均失败关闭。

该 binding 不是 Authority。它没有授权读取服务器、切换 release 或产生 Permission。

## 4. Hash evidence

### New artifacts

| File | SHA-256 |
|---|---|
| `ce-g11-correlation-binding.schema.v0.1.json` | `2263c3c224097f6d7ed233bd5ff261a6dd225e11f10e290d0d1dc4aa382be684` |
| `ce-g11-correlation-binding.offline-fixture.v0.1.json` | `cee58ceb4088ba99f4c0c5631a309898bf9c7df8a6d6ad64fc85ac920ad80f06` |
| `ce_g11_target_bound_correlator.py` | `b72ad6e707a95f65e20f235963306e04c4f3e81342f4c762514cffcbf7e2d0e3` |
| `test_ce_g11_target_bound_correlator.py` | `39d1b06a16197407fa97e5d884e5703deaa155030fcaeff6bbabba2da152f5cb` |
| `ce-g11a-offline-remediation-result.schema.v0.1.json` | `94e569e8efe70acf767c4680c86204681299ec3ad2179107c43d003d74f874f5` |

### Frozen historical inputs

| File | SHA-256 |
|---|---|
| `ce_g8_server_log_correlator.py` | `508245e1a49eb2fba94a3617517da2dfd200f9c8b1677cfdd92e186130ab6bef` |
| `test_ce_g8_diagnostic.py` | `22f500fa5bdb3e72ca424e8bfd800827e6e585c554270bf260d9271a2de74829` |
| `fixtures/access.log` | `3e63d82fd85b151cf3b5479b11b020d113790ac8cd71df561699479dc057bf8d` |
| `fixtures/error.log` | `38e96f94008c3bef6e988f5ef6725f0ccea5439b27a5be35e8f1722ce1709c55` |
| `ce-g9-offline-remediation-result.v0.1.json` | `7b5be0c3f6aaf02a9f5093eef4cd1d53163507b1d5ac99bdb5c906871eb8947b` |
| `ce-g10-cross-version-result.v0.1.json` | `3ffabc0fa8b12ff02829b39ce6a6f3a678298ea4fca6fb53e76953c392ee76e3` |

## 5. Execution caps

```text
LIVE_MODEL_REQUESTS_DURING_IMPLEMENTATION=0
PUBLIC_SITE_REQUESTS=0
SSH_SESSIONS=0
SERVER_READS=0
SERVER_WRITES=0
DEPLOYMENTS=0
DBOS_CHANGES=0
SAEE_CHANGES=0
HISTORICAL_FILES_MODIFIED=0
```

测试只使用 repository synthetic fixtures、temporary mutated bindings、injected current
target 和 injected journal runner。

## 6. What this proves

只证明：

> 一个 exact、hash-bound、`NOT_AUTHORIZED` 的 CE-G11 offline binding 可以在不修改
> historical parser 的情况下路由 sanitized correlation identity，并对目标、identity、
> tamper、privacy 和 authority-elevation 失败关闭。

不证明：

```text
LIVE_BINDING_CREATED=false
REMOTE_CROSS_VERSION_VALIDATION_PASS=false
TLS_ROOT_CAUSE_PROVEN=false
PUBLIC_ENTRY_REDEPLOYMENT_ADMISSION_PASS=false
REDEPLOYMENT=false
PRODUCTION_READY=false
CERTIFICATION=false
SLA=false
COMMERCIAL_OFFERING=false
```

## 7. Next gate

下一步只允许准备：

```text
PREPARE_CE_G11B_REMOTE_CROSS_VERSION_VALIDATION_RECOMMENDATION
```

CE-G11B 必须验证新的 adapter/schema/fixture/tests，不能把 CE-G10 对 historical
correlator 的 PASS 自动继承为新 adapter 的跨版本 PASS。Recommendation 仍不是 Decision。
