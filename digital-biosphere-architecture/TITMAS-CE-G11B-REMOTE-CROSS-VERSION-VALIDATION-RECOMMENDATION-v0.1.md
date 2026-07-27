---
document_id: DBA-TITMAS-CE-G11B-REMOTE-CROSS-VERSION-VALIDATION-RECOMMENDATION-0.1
title: TITMAS CE-G11B Remote Cross-Version Validation Recommendation v0.1
title_zh: TITMAS CE-G11B 远程跨版本验证建议 v0.1
version: 0.1.0
status: exact-recommendation-recommended-decision-pending
maturity: Development
maturity_scope: ce-g11-target-bound-correlator-cross-version-validation
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G11B Remote Cross-Version Validation Recommendation v0.1

## 1. Recommendation

建议为 CE-G11A 新增的 target-bound correlator 建立一个 exact、read-only（只读）、
fail-closed（失败关闭）的 GitHub-hosted matrix，精确覆盖 Python `3.10.20`、
`3.11.15`、`3.12.13`、`3.13.14` 和 `3.14.6`。

该 matrix 只验证新 adapter、binding contract、synthetic fixtures 和历史 regression
在五个 Python patch versions 上的离线兼容性。它不访问 TITMAS 公共站点、服务器或
部署环境，不创建 live binding，也不继承 CE-G10 对历史 correlator 的 PASS。

本文件是 Recommendation，不是 Decision、workflow creation authorization 或 run
authorization。

## 2. Why this gate is required

CE-G10 已证明 historical CE-G8/9 correlator 在五个 Python versions 上通过，但该
correlator 固定 CE-G8 target、Decision 和 receipt identity。CE-G11A 随后新增了独立
adapter 和 binding contract：

```text
CE_G11A_RESULT=PASS_OFFLINE_TARGET_BINDING_REMEDIATION_ONLY
CE_G11A_NEW_TESTS_PASS=13/13
CE_G11A_HISTORICAL_TESTS_PASS=13/13
CE_G11A_FULL_DISCOVERY_TESTS_PASS=35/35
CE_G11A_LOCAL_PYTHON_3_13_12_TESTS_PASS=13/13
CE_G11A_LOCAL_PYTHON_3_14_5_TESTS_PASS=13/13
```

该结果没有覆盖 Python 3.10、3.11、3.12，也不能把旧组件的 remote PASS 自动传播给
新组件。因此在任何 revised redeployment Recommendation 前，需要新的直接兼容性证据。

## 3. Agent-customer recommendation gate

初步 `qwen3.7-plus` 审查包含一次无可恢复正文和一次有效 compact response，只作为
历史输入。根据质量升级要求，Alibaba Cloud Model Studio `qwen3.7-max` 随后以
independent senior AI-agent infrastructure customer and release-safety reviewer
（独立高级智能体基础设施客户与发布安全审查者）身份，对本建议全文重新审查并返回
exact model identity 与严格 JSON：

```text
PRIMARY_REVIEW_MODEL=qwen3.7-max
VERDICT=RECOMMENDED
SELECTED_OPTION=A
WOULD_RECOMMEND_TO_AGENT_CUSTOMER=true
CONFIDENCE=0.98
BLOCKING_REASONS=0
REQUIRED_CORRECTIONS=0
FINAL_QUALITY_AUDIT_MODEL=qwen3.7-max
FINAL_QUALITY_AUDIT=PASS
FINAL_AUDIT_BLOCKING_FINDINGS=0
FINAL_AUDIT_REQUIRED_CORRECTIONS=0
```

模型确认：5 jobs × 26 tests = 130 tests 的 arithmetic 一致；十个 exact SHA-256、
two-phase trigger、只读权限、zero-secret/network/server/deployment caps、non-claims
和 runner image receipt 足以进入独立 Decision review。

更高版本候选 `qwen3.8-max-preview` 虽出现在 authenticated model catalog，但相同全文
review 返回 HTTP 400，未形成有效审查，不能用来声称更高模型已认可。当前正式质量
baseline 因此是已直接验证的 `qwen3.7-max`。

该输出是 advisory input，不是 Decision、Authority、Truth 或兼容性执行证据。

## 4. Frozen source baseline

Source commit：

```text
457d59f263ef52bb31bba1902cfe4c429e3c2207
```

十个 exact inputs：

```text
508245e1a49eb2fba94a3617517da2dfd200f9c8b1677cfdd92e186130ab6bef  commercial-evaluation-controller-tls-diagnosis/ce_g8_server_log_correlator.py
22f500fa5bdb3e72ca424e8bfd800827e6e585c554270bf260d9271a2de74829  commercial-evaluation-controller-tls-diagnosis/test_ce_g8_diagnostic.py
3e63d82fd85b151cf3b5479b11b020d113790ac8cd71df561699479dc057bf8d  commercial-evaluation-controller-tls-diagnosis/fixtures/access.log
38e96f94008c3bef6e988f5ef6725f0ccea5439b27a5be35e8f1722ce1709c55  commercial-evaluation-controller-tls-diagnosis/fixtures/error.log
2263c3c224097f6d7ed233bd5ff261a6dd225e11f10e290d0d1dc4aa382be684  commercial-evaluation-controller-tls-diagnosis/ce-g11-correlation-binding.schema.v0.1.json
cee58ceb4088ba99f4c0c5631a309898bf9c7df8a6d6ad64fc85ac920ad80f06  commercial-evaluation-controller-tls-diagnosis/ce-g11-correlation-binding.offline-fixture.v0.1.json
b72ad6e707a95f65e20f235963306e04c4f3e81342f4c762514cffcbf7e2d0e3  commercial-evaluation-controller-tls-diagnosis/ce_g11_target_bound_correlator.py
39d1b06a16197407fa97e5d884e5703deaa155030fcaeff6bbabba2da152f5cb  commercial-evaluation-controller-tls-diagnosis/test_ce_g11_target_bound_correlator.py
94e569e8efe70acf767c4680c86204681299ec3ad2179107c43d003d74f874f5  commercial-evaluation-controller-tls-diagnosis/ce-g11a-offline-remediation-result.schema.v0.1.json
47980dcabff53312516a925633db8d5087efeb3058c1422d61ef115788505de7  commercial-evaluation-controller-tls-diagnosis/ce-g11a-offline-remediation-result.v0.1.json
```

任一 hash 变化必须失败关闭，并重新建立 Recommendation 或 Decision scope。

## 5. Exact matrix candidate

```text
python=3.10.20
python=3.11.15
python=3.12.13
python=3.13.14
python=3.14.6
runner_label=ubuntu-24.04
permissions.contents=read
timeout_minutes_per_job=5
matrix_jobs=5
trigger_events_cap=1
workflow_runs_cap=1
retry=false
fallback=false
```

Actions 必须继续使用 full commit SHA：

```text
actions/checkout@11d5960a326750d5838078e36cf38b85af677262
actions/setup-python@ece7cb06caefa5fff74198d8649806c4678c61a1
actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02
```

`ubuntu-24.04` 是 hosted runner label，不是 immutable image。每个 receipt 必须记录
`ImageOS`、`ImageVersion`、exact Python version 和 source commit。

## 6. Candidate implementation paths

只有后续独立 Decision 可以授权创建：

```text
.github/workflows/titmas-ce-g11b-target-bound-cross-version.yml
commercial-evaluation-controller-tls-diagnosis/ce_g11b_cross_version_runner.py
commercial-evaluation-controller-tls-diagnosis/test_ce_g11b_cross_version_runner.py
commercial-evaluation-controller-tls-diagnosis/ce-g11b-run-request.schema.v0.1.json
commercial-evaluation-controller-tls-diagnosis/ce-g11b-run-request.v0.1.json
commercial-evaluation-controller-tls-diagnosis/ce-g11b-cross-version-result.schema.v0.1.json
commercial-evaluation-controller-tls-diagnosis/ce-g11b-cross-version-result.v0.1.json
TITMAS-CE-G11B-REMOTE-CROSS-VERSION-VALIDATION-REPORT-v0.1.md
```

历史文件、CE-G11A adapter/binding/tests 和 CE-G11A result 保持只读。

## 7. Required checks per matrix job

每个 job 必须：

1. 精确匹配指定 Python patch version；
2. 验证十个 frozen input hashes；
3. 验证 binding fixture 通过 Draft 2020-12 Schema；
4. 运行 CE-G11A new adapter tests `13/13`；
5. 运行 historical CE-G9 regression tests `13/13`；
6. 验证 offline fixture 仍是 `NOT_AUTHORIZED` 和 `authority_effect=false`；
7. 验证 test process 没有 network client、SSH、server path、deployment 或 credential
   dependency；
8. 验证 artifact 不含 raw logs、literal source value、salt、credential、
   proxy/interface detail 或 private error；
9. 使用 `PYTHONDONTWRITEBYTECODE=1`；
10. 只输出 sanitized, Schema-valid receipt。

总计预期：

```text
NEW_ADAPTER_TESTS_PASS=65/65
HISTORICAL_TESTS_PASS=65/65
TOTAL_MATRIX_TESTS_PASS=130/130
MATRIX_JOBS_PASS=5/5
```

## 8. Trigger and execution separation

为保持 trigger 可审计，建议沿用 CE-G10 已验证的 two-phase pattern：

1. Phase A 只提交 workflow、runner、runner tests 和 Schema；不得包含有效 run request；
2. Phase A 的 exact commit/hash 必须先远端可见；
3. Phase B 必须由独立 Decision 固定唯一 run-request bytes/hash、branch、path、source
   commit 和一次 trigger cap；
4. 只允许一个 path-scoped push event；不允许手动补跑、retry、fallback 或替代 matrix；
5. workflow run 完成后必须确认 run count 恰好为 `1`。

GitHub checkout、action download 和 Python toolcache 属于 CI control-plane traffic，不得写成
TITMAS public-site observation。test process 的 public-site requests 必须为 `0`。

## 9. Pass rule

只有五个 exact jobs 全部通过 hashes、Schema、26 tests、privacy 和 authority checks，
且 aggregate result 通过 Draft 2020-12 Schema，才可记录：

```text
CE_G11B_RESULT=PASS_REMOTE_CROSS_VERSION_OFFLINE_COMPATIBILITY_ONLY
```

任何单项失败都必须整体失败关闭并保留结果。

## 10. Caps, stop rules and non-claims

```text
MODEL_REQUESTS_DURING_EXECUTION=0
TARGET_PUBLIC_SITE_REQUESTS=0
SSH_SESSIONS=0
SERVER_READS=0
SERVER_WRITES=0
DEPLOYMENTS=0
DBOS_CHANGES=0
SAEE_CHANGES=0
LIVE_BINDINGS_CREATED=0
```

出现以下任一情况立即停止：

- source commit、input hash、matrix、action SHA、permissions 或 timeout 漂移；
- binding fixture 被改为 `AUTHORIZED` 或产生 Authority；
- test count、negative boundary、privacy check、artifact 或 aggregate Schema 不通过；
- 需要 secret、public-site request、SSH、server read/write、deployment 或 DBOS/SAEE change；
- 结果被描述为 live compatibility、TLS root cause、redeployment admission、
  Production、Certification、SLA 或 Commercial Offering。

即使 CE-G11B 未来通过，仍保持：

```text
LIVE_BINDING_CREATED=false
TLS_ROOT_CAUSE_PROVEN=false
PUBLIC_ENTRY_REDEPLOYMENT_ADMISSION_PASS=false
REDEPLOYMENT=false
PRODUCTION_READY=false
CERTIFICATION=false
SLA=false
COMMERCIAL_OFFERING=false
```

## 11. Decision boundary

```text
CE_G11B_RECOMMENDATION_PREPARED=true
CE_G11B_PRIMARY_REVIEW_MODEL=qwen3.7-max
CE_G11B_AGENT_VERDICT=RECOMMENDED
CE_G11B_WOULD_RECOMMEND_TO_AGENT_CUSTOMER=true
CE_G11B_AGENT_CONFIDENCE=0.98
CE_G11B_DECISION_RECORDED=false
CE_G11B_IMPLEMENTATION_AUTHORIZED=false
CE_G11B_WORKFLOW_CREATED=false
CE_G11B_WORKFLOW_RUNS=0
CE_G11B_REDEPLOYMENT_AUTHORIZED=false
```

下一步只允许 independent Decision review。不得从本建议直接创建 workflow、run request、
live binding 或 redeployment。
