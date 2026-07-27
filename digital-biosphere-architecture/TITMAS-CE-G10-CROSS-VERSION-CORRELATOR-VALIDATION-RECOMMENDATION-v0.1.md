---
document_id: DBA-TITMAS-CE-G10-CROSS-VERSION-CORRELATOR-VALIDATION-RECOMMENDATION-0.1
title: TITMAS CE-G10 Cross-Version Correlator Validation Recommendation v0.1
title_zh: TITMAS CE-G10 日志关联器跨版本验证建议 v0.1
version: 0.1.0
status: exact-recommendation-conditionally-recommended-decision-pending
maturity: Development
maturity_scope: ce-g9-remediated-log-correlator-cross-version-validation
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G10 Cross-Version Correlator Validation Recommendation v0.1

## 1. Recommendation

建议建立一个 manual-only（仅手动触发）、read-only（只读）、fail-closed（失败关闭）的
GitHub Actions matrix，只验证 CE-G9 已冻结的 correlator、tests 和 synthetic fixtures 在
Python 3.10–3.14 的离线兼容性。

本文件是 Recommendation，不是 Decision 或 execution authorization。

## 2. Agent-customer recommendation gate

Alibaba Cloud Model Studio 的 `qwen3.7-plus` 以潜在智能体开发者客户视角审查本建议：

```text
VERDICT=CONDITIONALLY_RECOMMENDED
WOULD_RECOMMEND_TO_AGENT_CUSTOMER=true
CONFIDENCE=0.78
BLOCKING_CORRECTIONS=3
```

首次 request 完成后没有返回可记录正文，按失败关闭不计为有效 verdict；一次压缩后的
最终 request 返回严格 JSON。没有再次重试。

三个 correction 已纳入：

1. 在任何 customer-facing compatibility recommendation（面向客户的兼容性推荐）前，
   必须由独立 Decision 授权并实际完成 3.10–3.14 matrix；
2. 必须固定并记录 test matrix、runner/action 配置、输入 hash 和 fixture/schema；
3. CE-G10 不产生 TLS root-cause、production、certification、SLA 或 commercial
   availability claim；这些结论若未来提出，必须另有直接证据与独立 Decision。

第 3 项不是 CE-G10 离线验证的执行前提，而是任何更高商业声明的停止边界。

## 3. Frozen input set

CE-G10 不修改以下输入：

```text
508245e1a49eb2fba94a3617517da2dfd200f9c8b1677cfdd92e186130ab6bef  commercial-evaluation-controller-tls-diagnosis/ce_g8_server_log_correlator.py
22f500fa5bdb3e72ca424e8bfd800827e6e585c554270bf260d9271a2de74829  commercial-evaluation-controller-tls-diagnosis/test_ce_g8_diagnostic.py
3e63d82fd85b151cf3b5479b11b020d113790ac8cd71df561699479dc057bf8d  commercial-evaluation-controller-tls-diagnosis/fixtures/access.log
38e96f94008c3bef6e988f5ef6725f0ccea5439b27a5be35e8f1722ce1709c55  commercial-evaluation-controller-tls-diagnosis/fixtures/error.log
e4e60d8d4715bfbd6495201e3ac00d62c167d3b112605c81606d244f575d5863  commercial-evaluation-controller-tls-diagnosis/ce-g9-offline-remediation-result.schema.v0.1.json
```

Source commit：

```text
5438215028bc565c24073f51c627f400ce738b0f
```

任何 input hash 变化都必须失败关闭，并重新建立 Recommendation。

## 4. Exact matrix candidate

Python versions 来自 `actions/python-versions` 的 public stable manifest，于
`2026-07-27` 读取：

```text
3.10.20
3.11.15
3.12.13
3.13.14
3.14.6
```

Runner 和 actions：

```text
runner_label=ubuntu-24.04
actions/checkout@11d5960a326750d5838078e36cf38b85af677262
actions/setup-python@ece7cb06caefa5fff74198d8649806c4678c61a1
actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02
permissions.contents=read
timeout_minutes_per_job=5
workflow_trigger=workflow_dispatch_only
```

`ubuntu-24.04` 是 GitHub-hosted runner label，不是不可变镜像。执行 receipt 必须记录
`ImageOS`、`ImageVersion`、Python exact version 和 action hashes，不得把 label 写成
immutable runner claim。

## 5. Proposed execution paths

只有后续独立 Decision 可以授权新增：

```text
.github/workflows/titmas-ce-g10-correlator-cross-version.yml
digital-biosphere-architecture/commercial-evaluation-controller-tls-diagnosis/ce_g10_cross_version_runner.py
digital-biosphere-architecture/commercial-evaluation-controller-tls-diagnosis/test_ce_g10_cross_version_runner.py
digital-biosphere-architecture/commercial-evaluation-controller-tls-diagnosis/ce-g10-cross-version-result.schema.v0.1.json
digital-biosphere-architecture/commercial-evaluation-controller-tls-diagnosis/ce-g10-cross-version-result.v0.1.json
digital-biosphere-architecture/TITMAS-CE-G10-CROSS-VERSION-CORRELATOR-VALIDATION-REPORT-v0.1.md
```

Correlator、CE-G8/CE-G9 tests 和 fixtures 保持只读。

## 6. Required controls

- matrix 必须是上述 5 个 exact Python patch versions；
- 每个 job 必须运行同一 `13/13` CE-G9 suite；
- runner wrapper 自身必须有 offline tests；
- action 使用 full commit SHA；
- workflow permissions 只有 `contents: read`；
- 不读取 repository/environment secrets；
- test process 不允许 network client、SSH、server path 或 deployment command；
- `PYTHONDONTWRITEBYTECODE=1`；
- 每个 job 只输出 sanitized result；
- artifacts 不含 raw log、literal source IP、salt、proxy/interface detail 或 credential；
- aggregate result 必须通过 Draft 2020-12 Schema 与 date-time format validation；
- 任一 matrix、hash、privacy、Schema 或 artifact 缺失均整体失败关闭。

GitHub checkout、action download 与 Python toolcache provisioning 是 CI control-plane
traffic，不得写成 TITMAS public-site observation；test process 的 public-site requests
必须为 0。

## 7. Pass rule

全部 5 个 exact versions 各自：

```text
CE_G9_TESTS_PASS=13/13
INPUT_HASHES_MATCH=true
PRIVACY_CHECKS_PASS=true
NETWORK_TEST_ACTIONS=0
```

并且 aggregate Schema pass，才可记录：

```text
CE_G10_RESULT=PASS_CROSS_VERSION_OFFLINE_COMPATIBILITY_ONLY
```

## 8. Stop rules and non-claims

出现以下任一情况立即停止：

- input hash 变化；
- Python exact version 不可用或与 matrix 不符；
- action SHA、runner label、permissions 或 timeout 漂移；
- test/runner 需要 credential、public-site request、SSH、server read/write 或 deployment；
- artifact 持久化 raw/private value；
- 任一 job 或 aggregate Schema 不通过；
- 结果被描述为 TLS root-cause、production、certification、SLA 或 commercial claim。

即使 CE-G10 通过，仍保持：

```text
TLS_ROOT_CAUSE_PROVEN=false
PUBLIC_ENTRY_REDEPLOYMENT_ADMISSION_PASS=false
PRODUCTION_READY=false
CERTIFICATION=false
SLA=false
COMMERCIAL_OFFERING=false
```

## 9. Decision boundary

```text
CE_G10_RECOMMENDATION_PREPARED=true
CE_G10_DECISION_RECORDED=false
CE_G10_EXECUTION_AUTHORIZED=false
CE_G10_WORKFLOW_CREATED=false
CE_G10_WORKFLOW_DISPATCHED=false
```

下一动作只允许独立 review 与 Decision，不允许从本建议直接创建或运行 workflow。
