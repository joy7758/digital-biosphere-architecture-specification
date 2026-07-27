---
document_id: DBA-TITMAS-CE-G11B-PHASE-A-MODEL-REVIEW-CAP-REMEDIATION-RECOMMENDATION-0.1
title: TITMAS CE-G11B Phase A Model Review Cap Remediation Recommendation v0.1
title_zh: TITMAS CE-G11B Phase A 模型审查上限修复建议 v0.1
version: 0.1.0
status: exact-recommendation-agent-reviewed-recommended-decision-pending
maturity: Development
maturity_scope: ce-g11b-phase-a-model-review-cap-remediation
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS CE-G11B Phase A Model Review Cap Remediation Recommendation v0.1

## 1. Recommendation

建议采用 **Option A：重新建立一个前瞻性、非追溯的 Phase A-R1 Decision**。

新的 Decision 只允许对已冻结的 CE-G11B candidate components 进行一次 fresh Phase A
revalidation（重新验证），并把模型调用分为三个互不替代的治理阶段：

| 阶段 | 目的 | 建议上限 | Authority effect |
|---|---|---:|---|
| Pre-decision review | 审查本 Recommendation 与候选 Decision 是否合理 | 每份治理材料最多 1 次 `qwen3.7-max` | 无 |
| Phase A-R1 implementation review | 审查 exact candidate source 与本地验证结果 | 精确 1 次 `qwen3.7-max` | 无 |
| CE-G11B workflow execution | 运行离线跨 Python 版本测试 | 0 次模型请求 | 无 |

既有 Phase A 中发生的模型审查保持历史事实，但不得追溯授权，也不得计入未来
Phase A-R1 的合格审查。新的 Decision 生效后，必须对 exact immutable candidate
重新执行一次 `qwen3.7-max` review。

本文件是 Recommendation，不是 Decision、Implementation Authorization、run request、
workflow execution、Phase B authorization 或 redeployment authorization。

## 2. Exact problem

[Phase A result](commercial-evaluation-controller-tls-diagnosis/ce-g11b-phase-a-result.v0.1.json)
和
[Phase A report](TITMAS-CE-G11B-PHASE-A-COMPONENT-PREPARATION-REPORT-v0.1.md)
记录：

```text
CE_G11B_PHASE_A_RESULT=FAIL_CLOSED_PHASE_A_MODEL_REQUEST_CAP_EXCEEDED
DECISION_MODEL_REQUEST_CAP=0
OBSERVED_MODEL_REQUESTS_DURING_IMPLEMENTATION=1
MODEL=qwen3.7-max
MODEL_REVIEW_VERDICT=PASS
PHASE_A_PASS=false
PHASE_B_AUTHORIZED=false
```

技术审查的 `PASS` 不能覆盖 exact Decision cap。用户同时要求商业化标准工作优先使用
`qwen3.7-max` 保证质量，且不得静默降级。旧 Decision 的 `0` cap 与新的强制质量政策
因此发生了显式冲突。

失败关闭证据已远端固化：

```text
branch=codex/ce-g11b-phase-a-decision
decision_commit=73a1f8d1de6024fe9ad22959998e2bc4a1caa03d
failure_baseline_commit=13fdf8babf0234bf1f03caaa57c6a1fc84073907
ce_g11b_workflow_runs=0
ce_g10_workflow_runs=1
```

## 3. Options

### Option A — Fresh bounded Phase A-R1 Decision（推荐）

建立新的独立 Decision：

- 明确允许 Phase A-R1 恰好 1 次 `qwen3.7-max` implementation review；
- execution-time model requests 继续保持 `0`；
- 旧 review 不追溯授权、不复用为合格结果；
- exact candidate hashes 未变化时允许作为 immutable inputs 重用；
- 任一 hash 漂移都必须停止并重新建立 Recommendation；
- 不创建有效 run request，不触发 workflow，不进入 Phase B。

优点：同时保持质量政策和 Decision/Execution 边界，历史失败不被抹除。

### Option B — 取消 implementation review（不推荐）

把 future implementation model request cap 继续固定为 `0`，只依赖本地测试。

拒绝原因：与用户明确要求的 Max 质量政策冲突，也会失去独立智能体客户审查入口。

### Option C — 把旧 review 追溯改写为 pre-decision review（禁止）

通过重新分类既有请求，让旧 Phase A 看起来符合 cap。

拒绝原因：这是 retroactive authorization（追溯授权），会改写已经发生的治理事实，
破坏 Decision 先于 Execution 的原则。

## 4. Proposed Phase A-R1 Decision contract

只有后续独立 Decision 可以采用以下 contract：

```text
DECISION_CANDIDATE=TITMAS-COMMERCIAL-EVALUATION-CE-G11B-A-R1
AUTHORIZED_SCOPE=PHASE_A_R1_REVALIDATION_ONLY
REUSE_EXACT_CANDIDATE_HASHES_IF_UNCHANGED=true
HISTORICAL_REVIEW_COUNTS_AS_R1_REVIEW=false
PRE_DECISION_MODEL=qwen3.7-max
PHASE_A_R1_IMPLEMENTATION_REVIEW_MODEL=qwen3.7-max
PHASE_A_R1_IMPLEMENTATION_MODEL_REQUESTS_EXACT=1
EXECUTION_TIME_MODEL_REQUESTS_MAX=0
MODEL_RETRY_ALLOWED=false
MODEL_FALLBACK_ALLOWED=false
MODEL_SUBSTITUTION_ALLOWED=false
JSON_REPAIR_REQUEST_ALLOWED=false
VALID_RUN_REQUEST_ALLOWED=false
WORKFLOW_TRIGGER_ALLOWED=false
PHASE_B_AUTHORIZED=false
```

一次 HTTP attempt 即计入 Phase A-R1 的唯一模型请求，无论返回成功、HTTP error、
timeout、model identity mismatch、JSON parse failure 或 Schema failure。任何失败都必须
结束 Phase A-R1；不得用 retry、fallback、alias inference 或第二次模型调用修复。

## 5. Frozen candidate inputs

Phase A-R1 只能在以下 SHA-256 全部保持不变时重用 candidate：

```text
ea97c600c633196cb0afdb767d28fd47610856c9185dfcb0570de53a0a596503  .github/workflows/titmas-ce-g11b-target-bound-cross-version.yml
8f8d521adfdec1517767313933c5650b684262c97c0756c53372a28f948a5e9d  commercial-evaluation-controller-tls-diagnosis/ce_g11b_cross_version_runner.py
e8b3e86a36cc6015937860b61cafb98dcfd7fc092e7fee03cffb318e071e6c24  commercial-evaluation-controller-tls-diagnosis/test_ce_g11b_cross_version_runner.py
6a6e4ee89cc39085950737fcd4a8fc913d4b48a051508e1e1e1e02352e2b1d39  commercial-evaluation-controller-tls-diagnosis/ce-g11b-run-request.schema.v0.1.json
6c7f328f28c04c94a955f2b3642c5685590e3b556984d34db693fbef3ff1f15f  commercial-evaluation-controller-tls-diagnosis/ce-g11b-cross-version-result.schema.v0.1.json
```

重用只表示输入 bytes 相同，不继承旧 Phase A review 或 PASS。

## 6. Required Phase A-R1 checks

新的 Decision 应要求：

1. 验证远端 failure baseline commit `13fdf8b…` 和分支精确匹配；
2. 验证五个 candidate hashes；
3. 验证十个 frozen CE-G11A source hashes；
4. 验证三个 Draft 2020-12 Schema；
5. Python 3.13 与 3.14 runner tests 各 `14/14`；
6. 两个本地版本的 scoped tests 各 `40/40`；
7. full CE-G discovery `49/49`；
8. 有效 `ce-g11b-run-request.v0.1.json` 不存在；
9. 最终 `ce-g11b-cross-version-result.v0.1.json` 不存在；
10. CE-G11B workflow run count 保持 `0`；
11. 执行恰好一次 fresh `qwen3.7-max` exact-source review；
12. 记录 sanitized、Schema-valid result，不保存 credential、hidden reasoning、raw provider
    envelope 或未清洗 provider error body。

## 7. Model quality and upgrade policy

当前 verified quality baseline 是 `qwen3.7-max`。`qwen3.8-max-preview` 虽曾出现在
authenticated catalog，但 exact review 返回 HTTP 400，没有形成有效质量证据。

因此：

- 不得静默降级到 `qwen3.7-plus` 或其他模型；
- 不得仅凭 catalog 名称升级模型；
- 只有更高模型完成 exact catalog、direct request、returned identity 和 strict response
  contract 验证后，才可由新的 Recommendation/Decision 选择；
- model output 始终是 advisory input，不是 Authority、Decision、Permission 或 Truth。

## 8. Stop rules

出现以下任一情况立即失败关闭：

- 旧失败被改写为 PASS 或旧 review 被追溯授权；
- candidate/frozen input hash 漂移；
- 模型请求不是 exact `qwen3.7-max`；
- model request count 不等于 1；
- 需要 retry、fallback、model substitution 或第二次 JSON repair request；
- 任何测试、Schema、identity、privacy 或 authority boundary 不通过；
- 有效 run request 出现或 workflow run count 大于 0；
- 需要 public-site request、SSH、server read/write、deployment、DBOS/SAEE/site change；
- 结果被描述为 remote compatibility、TLS root cause、redeployment admission、
  Production、Certification、SLA 或 Commercial Offering。

## 9. Agent-customer recommendation gate

`qwen3.7-max` 已对本文件的 pre-review exact bytes（SHA-256
`854f263a4e3bc3b2452cc22ceacb16b60275fc8f5d21a68584daa57368f4c05b`）完成一次
independent review。最终文件只追加该审查回执和结果，没有改变 Option A、caps、stop
rules 或 non-claims。该 review 属于 pre-decision review，不是未来 Phase A-R1
implementation review。

[Sanitized review record](TITMAS-CE-G11B-PHASE-A-MODEL-REVIEW-CAP-REMEDIATION-QWEN-REVIEW-v0.1.json)
记录 exact model identity、请求计数、hash 和 persistence boundary：

```text
PRIMARY_REVIEW_MODEL=qwen3.7-max
RETURNED_MODEL=qwen3.7-max
RETURNED_MODEL_EQUALS_REQUESTED=true
REVIEW_VERDICT=RECOMMENDED
SELECTED_OPTION=A
WOULD_RECOMMEND_TO_AGENT_CUSTOMER=true
CONFIDENCE=0.95
HISTORICAL_FAILURE_PRESERVED=true
RETROACTIVE_AUTHORIZATION_REJECTED=true
REVIEW_STAGES_SEPARATED=true
IMPLEMENTATION_REVIEW_REQUEST_CAP=1
EXECUTION_TIME_MODEL_REQUEST_CAP=0
PHASE_B_AUTHORIZED=false
BLOCKING_REASONS=0
REQUIRED_CORRECTIONS=0
REQUESTS=1
RETRIES=0
FALLBACKS=0
MODEL_SUBSTITUTIONS=0
JSON_REPAIR_REQUESTS=0
```

模型评价是 advisory input，不是 Authority、Decision、Permission 或 Phase A-R1
Authorization。

## 10. Non-claims and next gate

```text
RECOMMENDATION_PREPARED=true
PRE_DECISION_AGENT_REVIEW_COMPLETE=true
PRE_DECISION_AGENT_REVIEW_VERDICT=RECOMMENDED
PRE_DECISION_AGENT_REVIEW_CONFIDENCE=0.95
RETROACTIVE_AUTHORIZATION_ALLOWED=false
NEW_DECISION_RECORDED=false
PHASE_A_R1_AUTHORIZED=false
PHASE_A_R1_EXECUTED=false
PHASE_A_PASS=false
VALID_RUN_REQUEST_CREATED=false
WORKFLOW_RUNS=0
PHASE_B_AUTHORIZED=false
REMOTE_CROSS_VERSION_VALIDATION_PASS=false
LIVE_BINDING_CREATED=false
TLS_ROOT_CAUSE_PROVEN=false
PUBLIC_ENTRY_REDEPLOYMENT_ADMISSION_PASS=false
REDEPLOYMENT=false
PRODUCTION_READY=false
CERTIFICATION=false
SLA=false
COMMERCIAL_OFFERING=false
```

下一步只允许依据 standing directive 建立新的 independent Phase A-R1 Decision，并让
`qwen3.7-max` 对 Decision exact bytes 做独立 pre-implementation review。当前不得执行
Phase A-R1 或 Phase B。
