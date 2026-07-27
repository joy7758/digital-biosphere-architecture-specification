---
document_id: DBA-TITMAS-CE-G11B-PHASE-A-R1-REVALIDATION-REPORT-0.1
title: TITMAS CE-G11B Phase A-R1 Revalidation Report v0.1
title_zh: TITMAS CE-G11B Phase A-R1 重新验证报告 v0.1
version: 0.1.0
status: pass-phase-a-r1-revalidation-only
maturity: Development
maturity_scope: ce-g11b-phase-a-r1-local-revalidation
owner_ref: zhangbin
decision_reference: TITMAS-COMMERCIAL-EVALUATION-CE-G11B-A-R1
decision_baseline_commit: fcab763ccdd8077a0f77c7fa879af3979357f0e7
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G11B Phase A-R1 Revalidation Report v0.1

## 1. Outcome

```text
CE_G11B_PHASE_A_R1_RESULT=PASS_PHASE_A_R1_REVALIDATION_ONLY
HISTORICAL_PHASE_A_RESULT=FAIL_CLOSED_PHASE_A_MODEL_REQUEST_CAP_EXCEEDED
HISTORICAL_FAILURE_PRESERVED=true
RETROACTIVE_AUTHORIZATION=false
PHASE_A_R1_PASS=true
PHASE_B_AUTHORIZED=false
```

[Phase A-R1 Decision](TITMAS-COMMERCIAL-EVALUATION-CE-G11B-PHASE-A-R1-DECISION-RECORD.v0.1.json)
在远端 commit `fcab763ccdd8077a0f77c7fa879af3979357f0e7` 固化后，授权了 exact
local revalidation。旧 Phase A 的失败没有被删除、改写或追溯授权。

Machine result：

[ce-g11b-phase-a-r1-result.v0.1.json](commercial-evaluation-controller-tls-diagnosis/ce-g11b-phase-a-r1-result.v0.1.json)

## 2. Immutable candidate verification

五个 candidate components 保持原始 SHA-256：

| Component | SHA-256 |
|---|---|
| `.github/workflows/titmas-ce-g11b-target-bound-cross-version.yml` | `ea97c600c633196cb0afdb767d28fd47610856c9185dfcb0570de53a0a596503` |
| `ce_g11b_cross_version_runner.py` | `8f8d521adfdec1517767313933c5650b684262c97c0756c53372a28f948a5e9d` |
| `test_ce_g11b_cross_version_runner.py` | `e8b3e86a36cc6015937860b61cafb98dcfd7fc092e7fee03cffb318e071e6c24` |
| `ce-g11b-run-request.schema.v0.1.json` | `6a6e4ee89cc39085950737fcd4a8fc913d4b48a051508e1e1e1e02352e2b1d39` |
| `ce-g11b-cross-version-result.schema.v0.1.json` | `6c7f328f28c04c94a955f2b3642c5685590e3b556984d34db693fbef3ff1f15f` |

```text
CANDIDATE_HASHES_MATCH=5/5
CE_G11A_FROZEN_HASHES_MATCH=10/10
CANDIDATE_COMPONENTS_MODIFIED=false
```

## 3. Local technical evidence

```text
DRAFT_2020_12_SCHEMAS_VALID=3/3
RUNNER_TESTS_PYTHON_3_13_12=14/14
RUNNER_TESTS_PYTHON_3_14_5=14/14
ALL_SCOPED_TESTS_PYTHON_3_13_12=40/40
ALL_SCOPED_TESTS_PYTHON_3_14_5=40/40
FULL_CE_G_DISCOVERY_TESTS=49/49
VALID_RUN_REQUEST_INSTANCE_ABSENT=true
FINAL_CROSS_VERSION_RESULT_INSTANCE_ABSENT=true
CE_G11B_WORKFLOW_RUNS=0
CE_G10_WORKFLOW_RUNS=1
PYTHONDONTWRITEBYTECODE=1
PYCACHE_CREATED=false
```

这些检查只证明 Phase A-R1 的本地候选重新验证，不证明五版本 remote matrix。

## 4. Fresh qwen3.7-max implementation review

Phase A-R1 使用了 Decision 允许的唯一一次 implementation model request：

```text
REQUESTED_MODEL=qwen3.7-max
RETURNED_MODEL=qwen3.7-max
RETURNED_MODEL_EQUALS_REQUESTED=true
HTTP_STATUS=200
REQUESTS=1/1
RETRIES=0
FALLBACKS=0
MODEL_SUBSTITUTIONS=0
JSON_REPAIR_REQUESTS=0
VERDICT=PASS
CONFIDENCE=0.95
WOULD_RECOMMEND_TO_AGENT_CUSTOMER=true
PYTHON_3_10_COMPATIBLE=true
WORKFLOW_EXACT_SCOPE=true
WORKFLOW_READ_ONLY=true
REQUEST_CONTRACT_FAIL_CLOSED=true
RUNNER_SANITIZATION_BOUNDARY=true
ENVIRONMENT_ALLOWLIST_BOUNDARY=true
TEST_COVERAGE_SUFFICIENT_FOR_PHASE_A_R1=true
HISTORICAL_FAILURE_PRESERVED=true
CANDIDATE_EDITS_REQUIRED=false
WORKFLOW_EXECUTION_AUTHORIZED=false
PHASE_B_AUTHORIZED=false
BLOCKING_FINDINGS=0
REQUIRED_CORRECTIONS=0
```

Sanitized hashes：

```text
REQUEST_PAYLOAD_SHA256=d8fb78db6ebf2e5226aca03b4bef59d4c212dd315afc55e816cffdd7bedc16ea
REVIEW_BUNDLE_SHA256=9c28084952b49a2b190cb908e5659a19d0d5c355e5ca61d1c94448bd0d0f9c6b
RESPONSE_ENVELOPE_SHA256=b0dcf42cb056ea43a6a736a2b457da7719e25b5e88e69b4c7c4bf399e6857f45
```

未保存 credential、hidden reasoning、raw provider envelope、usage 或 provider error body。
模型输出是 advisory input，不是 Authority、Permission、Decision 或 Truth。

## 5. External-action boundary

```text
TRIGGER_EVENTS=0
WORKFLOW_RUNS=0
MATRIX_JOBS=0
WORKFLOW_EXECUTION_MODEL_REQUESTS=0
TARGET_PUBLIC_SITE_REQUESTS=0
SSH_SESSIONS=0
SERVER_READS=0
SERVER_WRITES=0
DEPLOYMENTS=0
DBOS_CHANGES=0
SAEE_CHANGES=0
SITE_CHANGES_INCLUDED=0
LIVE_BINDINGS_CREATED=0
```

## 6. Non-claims

```text
REMOTE_CROSS_VERSION_VALIDATION_PASS=false
VALID_RUN_REQUEST_CREATED=false
WORKFLOW_RUN=false
PHASE_B_AUTHORIZED=false
LIVE_BINDING_CREATED=false
TLS_ROOT_CAUSE_PROVEN=false
PUBLIC_ENTRY_REDEPLOYMENT_ADMISSION_PASS=false
REDEPLOYMENT=false
PRODUCTION_READY=false
CERTIFICATION=false
SLA=false
COMMERCIAL_OFFERING=false
```

## 7. Next gate

Phase A-R1 的 result commit 必须先远端验证。之后只允许准备新的 Phase B run-request
Decision Recommendation；该 Recommendation 仍不能创建 run request 或触发 workflow。
