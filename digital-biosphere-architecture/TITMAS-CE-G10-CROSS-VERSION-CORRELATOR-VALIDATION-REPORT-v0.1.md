---
document_id: DBA-TITMAS-CE-G10-CROSS-VERSION-CORRELATOR-VALIDATION-REPORT-0.1
title: TITMAS CE-G10 Cross-Version Correlator Validation Report v0.1
title_zh: TITMAS CE-G10 日志关联器跨版本验证报告 v0.1
version: 0.1.0
status: pass-cross-version-offline-compatibility-only
maturity: Development
maturity_scope: ce-g9-remediated-log-correlator-cross-version-validation
owner_ref: zhangbin
decision_reference: TITMAS-COMMERCIAL-EVALUATION-CE-G10
trigger_decision_reference: TITMAS-COMMERCIAL-EVALUATION-CE-G10A
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G10 Cross-Version Correlator Validation Report v0.1

## 1. Outcome

```text
CE_G10_RESULT=PASS_CROSS_VERSION_OFFLINE_COMPATIBILITY_ONLY
WORKFLOW_RUN_ID=30270198036
TRIGGER_EVENT=push
TRIGGER_EVENTS=1
WORKFLOW_RUNS=1
MANUAL_DISPATCHES=0
MATRIX_JOBS_PASS=5/5
CE_G9_TESTS_PASS=65/65
ARTIFACTS=5
RETRY=0
```

Run：

<https://github.com/joy7758/digital-biosphere-architecture-specification/actions/runs/30270198036>

Source commit：

```text
8d317bd78b21af76b49c77df25df4a74c95a1c19
```

## 2. Matrix

| Python | CE-G9 tests | Input / request / privacy | Runner image |
|---|---:|---|---|
| `3.10.20` | `13/13` | PASS | `ubuntu24 / 20260720.247.2` |
| `3.11.15` | `13/13` | PASS | `ubuntu24 / 20260720.247.2` |
| `3.12.13` | `13/13` | PASS | `ubuntu24 / 20260720.247.2` |
| `3.13.14` | `13/13` | PASS | `ubuntu24 / 20260720.247.2` |
| `3.14.6` | `13/13` | PASS | `ubuntu24 / 20260720.247.2` |

每个 receipt 都证明：

- exact Python version match；
- run-request contract match；
- Phase A commit 是 trigger commit 的 ancestor；
- Phase A component hashes match；
- CE-G9 frozen input hashes match；
- fixture literal IP absent；
- frozen CE-G9 suite `13/13`；
- raw failure、credential 或 private value 未写入 receipt。

## 3. Artifact integrity

| Artifact | SHA-256 |
|---|---|
| `ce-g10-python-3.10.20` | `76d2638ae73e660dbfa740141f4c1deb06522beee9491d7b7357e848bfafc9a1` |
| `ce-g10-python-3.11.15` | `c03875238a0db656e797c447598ff70ffb38f3184a4c639d168f72ace7446933` |
| `ce-g10-python-3.12.13` | `e2cbcec1bfcbbac151ff6c5f46005187b4bbc3b270e35df38c04163ef89fe9ac` |
| `ce-g10-python-3.13.14` | `4637cde28927acd8f8df778d63f83e0a94c90036f08944f9634a0ec6f763d200` |
| `ce-g10-python-3.14.6` | `59b8628abe5535d2fbe68b767e1d0075d633c642bc119323bd20221481d41fcb` |

## 4. Trigger remediation history

原 `workflow_dispatch` preflight 因 workflow 不在 default branch 而失败关闭，dispatch/run
均为 0。CE-G10A 只替换 trigger mechanism：

1. Phase A 实现 validation branch + exact run-request path，远端 request absent、run=0；
2. Phase B 单独提交 immutable request；
3. 该 push 产生唯一 Run `30270198036`；
4. 没有 merge `main`，没有 retry。

## 5. Caps

```text
TARGET_PUBLIC_SITE_REQUESTS=0
SSH_SESSIONS=0
SERVER_READS=0
SERVER_WRITES=0
DEPLOYMENTS=0
DBOS_CHANGES=0
SAEE_CHANGES=0
MODEL_REQUESTS_DURING_EXECUTION=0
```

GitHub checkout/action/Python provisioning 属于 CI control-plane traffic，不是 TITMAS
public-site observation；测试进程没有 repository/environment secret。

## 6. What this proves

只证明：

> CE-G9 remediated correlator 与 frozen tests 在五个 exact Python patch versions 的
> GitHub-hosted Ubuntu runner 上离线兼容。

不证明：

```text
TLS_ROOT_CAUSE_PROVEN=false
CE_G8_HISTORICAL_RESULT_CHANGED=false
PUBLIC_ENTRY_REDEPLOYMENT_ADMISSION_PASS=false
REDEPLOYMENT=false
PRODUCTION_READY=false
CERTIFICATION=false
SLA=false
COMMERCIAL_OFFERING=false
```

下一步只允许准备 CE-G11 correlated exact redeployment Recommendation；不得从 CE-G10
直接重部署。
