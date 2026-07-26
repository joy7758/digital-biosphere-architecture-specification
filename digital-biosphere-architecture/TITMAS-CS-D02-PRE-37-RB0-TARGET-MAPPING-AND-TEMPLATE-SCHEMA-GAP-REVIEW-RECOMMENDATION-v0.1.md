---
document_id: DBA-TITMAS-CS-D02-PRE-37-RB0-TARGET-MAPPING-AND-TEMPLATE-SCHEMA-GAP-REVIEW-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-37 RB0 Target Mapping and Template Schema Gap Review Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-37 RB0 目标映射与模板 Schema 缺口审查建议 v0.1
version: 0.1.0
status: exact-offline-target-mapping-and-schema-gap-review-recommendation-not-decided
maturity: Development
decision_reference: CS-D02-PRE-37
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
target_repository: https://github.com/joy7758/titmas-integrations.git
target_repository_modification_authorized: false
license_adopted: false
implementation_authorized: false
---

# TITMAS CS-D02 PRE-37 RB0 Target Mapping and Template Schema Gap Review Recommendation v0.1

## 1. Why PRE-37 Exists

PRE-36 已在 DBA 中形成并验证九个 public-safe `.candidate` 文件。它们满足当前零实现、
零外部修改和 human/machine consistency 要求。

验证同时保留 `PRE36-GAP-001`：

> adopted implementation declaration template 使用相对 Schema reference，但 PRE-34
> required target file manifest 没有把该 Schema 列为 target file。

直接进入 target application 会产生一个不能在 clean clone 中解析的 template dependency。
因此下一步必须先做纯离线 target mapping 与 Schema gap resolution review，不能直接修改
`titmas-integrations`。

## 2. Agent Recommendation

```text
AGENT_RECOMMENDATION=RECOMMENDED_WITH_FAIL_CLOSED_TARGET_APPLICATION_BLOCK
RECOMMENDED_AS=OFFLINE_EXACT_TARGET_MAPPING_AND_SCHEMA_GAP_RESOLUTION_PACKET
NOT_RECOMMENDED_AS=LICENSE_ADOPTION_TARGET_REPOSITORY_MODIFICATION_OR_RB0_APPLICATION
```

如果潜在开发者询问“是否可以把 PRE-36 文件直接应用到 target”，当前回答是
`NOT_RECOMMENDED`，原因不是 candidate 内容不安全，而是 target manifest 的 Schema
dependency 不完整。

## 3. Exact Recommendation

```text
RECOMMENDED_OPTION=AUTHORIZE_OFFLINE_PRE36_RB0_FILESET_TARGET_MAPPING_AND_TEMPLATE_SCHEMA_GAP_RESOLUTION_PACKET_ONLY
PRIMARY_REPOSITORY=digital-biosphere-architecture
TARGET_REPOSITORY=https://github.com/joy7758/titmas-integrations.git
TARGET_COMMIT=e8eeccbf19e5e1d1f01ab9ad8796a53591a38dc8
IMPLEMENTATION_OWNER_REF=zhangbin
EXTERNAL_REPOSITORY_MODIFICATIONS_MAX=0
TARGET_FILES_CREATED_MAX=0
TARGET_FILES_MODIFIED_MAX=0
IMPLEMENTATION_FILES_MAX=0
NEW_REPOSITORIES_MAX=0
NETWORK_REQUESTS_MAX=0
LIVE_MODEL_REQUESTS_MAX=0
CREDENTIAL_READS_MAX=0
```

## 4. Authorized Review Outputs

只允许在 DBA 中形成：

1. exact candidate-to-target path mapping；
2. PRE-36 九个 candidate digest binding；
3. `PRE36-GAP-001` resolution options matrix；
4. recommended resolution candidate；
5. revised target file manifest candidate；
6. Apache-2.0 license adoption decision input；
7. exact target application plan candidate；
8. rollback plan candidate；
9. PRE-38 decision packet；
10. offline validation result 与 execution receipt。

## 5. Required Gap Resolution Review

至少比较：

### Option A: add exact Schema as a tenth target file

- target path:
  `schemas/implementation-declaration-template.schema.v0.1.json`；
- retain the adopted template bytes and relative `$schema` reference；
- update exact manifest and target path count；
- verify Schema meta-valid and template instance valid in simulated target layout。

### Option B: change the template Schema reference

- would alter the PRE-35 adopted template bytes；
- requires a new template revision, Schema revision and adoption decision；
- cannot silently replace the adopted digest。

PRE-37 可以推荐一个 option，但不能采纳、应用或修改 target。

## 6. Validation Requirements

1. all PRE-36 candidate digests match commit
   `3dbb37d95a2494d02af750b0fa4599d84581ede3`；
2. target mapping has no collisions, traversal or undeclared paths；
3. simulated target layout resolves all local `$schema` references；
4. revised manifest candidate is Schema-valid；
5. license text digest remains exact and `license_adopted=false`；
6. README / AGENTS / llms / machine entry remain consistent；
7. rollback removes only exact newly applied RB0 paths and restores the prior README bytes；
8. target HEAD and dirty count remain unchanged；
9. no network/model/credential action；
10. unknowns and failure states are retained.

## 7. Preconditions

1. PRE-36 Decision commit:
   `95a9cef87ed8a4a82b476c0836e1d58d2c8cba61`；
2. PRE-36 candidate commit:
   `3dbb37d95a2494d02af750b0fa4599d84581ede3`；
3. PRE-36 result commit:
   `2925c3a53326195f7598ec1021b3b54ed0e5b2f6`；
4. PRE-36 result SHA-256:
   `e270b64c7f368fc48f7b8a676327c0413b2caaf548f21708c4eb78e0f15fc0ea`；
5. validation result SHA-256:
   `c98fd094ec125325465b8f26b92283bd26dea964ca8c870eb72d2a411f3bb5a1`；
6. execution receipt SHA-256:
   `9f7ca51b7cadefcbc8bce1d0d79c3723a0aea2a733569fa0b5496167b3f5b0a2`；
7. target remains at exact observed commit and dirty count `0`；
8. standing directive active.

## 8. Stop Conditions

- 需要修改、commit、push 或 rename target repository 文件；
- 需要直接采纳 license；
- 需要绕过 `PRE36-GAP-001`；
- 需要改变 PRE-35 adopted artifact bytes 而不建立新 revision；
- 需要创建 source、package、tests、API 或 Runtime；
- 需要 network、provider API、model 或 credential；
- simulated target layout 仍有 unresolved local reference；
- 产生 provider support、conformance、release、production 或 commercial claim。

## 9. Effects

```text
PRE37_RECOMMENDATION_DEFINED=true
PRE37_DECISION_RECORDED=false
PRE37_REVIEW_EXECUTED=false

LICENSE_ADOPTED=false
TARGET_REPOSITORY_MODIFIED=false
REPOSITORY_BASELINE_APPLIED=false
PACKAGE_CREATED=false
IMPLEMENTATION_AUTHORIZED=false
IMPLEMENTATION_CREATED=false
TESTS_EXECUTED=0
PROVIDER_SUPPORTED=false
CONFORMANCE_EXECUTED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

## 10. Next Gate if Successful

下一步是 `PRE-38`：

```text
DECIDE_EXACT_LICENSE_ADOPTION_AND_TARGET_RB0_APPLICATION_OR_REJECT
```

PRE-38 必须绑定最终 target paths、exact bytes、license effect、rollback、target branch、
pre/post validation 与 external repository modification authorization。它不能夹带 RB1、
RI0、provider support、conformance 或 release。

## 11. Standing Directive Eligibility

本建议是 DBA-only offline review-and-packet action；exact sources、target、零外部修改、
validation、false effects 和 stop conditions 已明确。

```text
STANDING_DIRECTIVE_REFERENCE=TITMAS-CS-STANDING-001
STANDING_DIRECTIVE_ELIGIBLE_CANDIDATE=true
AT_RECOMMENDATION_TIME_PRE37_DECIDED=false
AT_RECOMMENDATION_TIME_TARGET_MODIFICATION_AUTHORIZED=false
AT_RECOMMENDATION_TIME_LICENSE_ADOPTED=false
```
