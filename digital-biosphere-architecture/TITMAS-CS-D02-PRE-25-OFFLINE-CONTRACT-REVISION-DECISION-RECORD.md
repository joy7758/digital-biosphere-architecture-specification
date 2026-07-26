---
document_id: DBA-TITMAS-CS-D02-PRE-25-OFFLINE-CONTRACT-REVISION-DECISION-0.1
title: TITMAS CS-D02 PRE-25 Offline Contract Revision Decision Record v0.1
title_zh: TITMAS CS-D02 PRE-25 离线契约修订决定记录 v0.1
version: 0.1.0
status: authorized-offline-pre24-finding-triage-and-v0-2-candidates-only
maturity: Development
decision_id: CS-D02-PRE-25
standing_directive_reference: TITMAS-CS-STANDING-001
decided_by_ref: zhangbin
offline_revision_authorized: true
live_model_request_authorized: false
contract_adoption_authorized: false
implementation_authorized: false
---

# TITMAS CS-D02 PRE-25 Offline Contract Revision Decision Record v0.1

## Decision

依据 `TITMAS-CS-STANDING-001` 和远端 PRE-25 recommendation，采用：

```text
DECISION_RESULT=AUTHORIZE_OFFLINE_PRE24_FINDING_TRIAGE_AND_V0_2_CONTRACT_REVISION_CANDIDATES_ONLY
DECIDED_BY_REF=zhangbin
FINDINGS_TO_TRIAGE=3
REQUIRED_FIXTURE_CLASSES=10
LIVE_MODEL_REQUESTS_MAX=0
PROVIDER_NETWORK_REQUESTS_MAX=0
RETRY_ATTEMPTS_MAX=0
FALLBACK_ATTEMPTS_MAX=0
JSON_REPAIR_ATTEMPTS_MAX=0
CONTRACT_ADOPTION_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
LIVE_RERUN_AUTHORIZED=false
```

## Scope

授权创建：

- PRE-24 finding triage matrix；
- extraction contract v0.2 candidate；
- model-binding policy v0.2 candidate；
- model alias record Schema candidate；
- cross-layer invariants candidate；
- 10 类 positive/negative fixtures；
- deterministic offline result、receipt、report 和 cockpit synchronization。

## Required Boundaries

- v0.1 文件及其 hash 不变；
- advisory finding 必须先分诊，不能直接升级为规范事实；
- semantic response extraction 与 provider model extraction 保持独立；
- conflict 必须 terminal non-qualifying；
- expired、revoked、conflicted 或普通 Decision alias 不得 qualifying；
- alias adoption、contract adoption 和 implementation 均不由本决定产生。

## Stop Conditions

v0.1 hash mismatch、provider/network/credential access、维度混淆、alias 推定、历史覆盖、fixture
失败被忽略或任何 Adoption、Implementation、Profile、Certification、Release 抬升时失败关闭。

## Effects

```text
PRE22_RESULT_CHANGED=false
PRE23_RESULT_CHANGED=false
PRE24_RESULT_CHANGED=false
V0_1_CONTRACTS_CHANGED=false
V0_2_CONTRACT_CANDIDATES_ADOPTED=false
ADAPTER_IMPLEMENTATION_CREATED=false
LIVE_REVIEW_EXECUTED=false
PROFILE_REVIEW_COMPLETED=false
PROFILE_ADOPTED=false
PROVIDER_SUPPORTED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
IMPLEMENTATION_AUTHORIZED=false
EXTERNAL_OUTREACH_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

执行前必须把本 Decision、plan 和 input manifest 提交并在目标远端分支验证。
