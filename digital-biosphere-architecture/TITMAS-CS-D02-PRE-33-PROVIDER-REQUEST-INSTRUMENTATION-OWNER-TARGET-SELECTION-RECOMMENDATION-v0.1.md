---
document_id: DBA-TITMAS-CS-D02-PRE-33-PROVIDER-REQUEST-INSTRUMENTATION-OWNER-TARGET-SELECTION-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-33 Provider Request Instrumentation Owner and Target Selection Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-33 Provider 请求可观测实现 Owner 与目标选择建议 v0.1
version: 0.1.0
status: exact-bounded-owner-target-selection-recommendation-not-decided
maturity: Development
decision_reference: CS-D02-PRE-33
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
implementation_authorized: false
external_repository_modification_authorized: false
repository_creation_authorized: false
---

# TITMAS CS-D02 PRE-33 Provider Request Instrumentation Owner and Target Selection Recommendation v0.1

## 1. Why PRE-33 Exists

PRE-32 已完成只读 Owner / target、重复建设和 handoff readiness 审计：

```text
ELIGIBLE_EXISTING_TARGETS=0
CANDIDATE_TARGETS_REQUIRING_DECISION=1
OWNER_TARGET_RESOLVED=false
IMPLEMENTATION_DECISION_READY=false
```

唯一方向匹配的现有候选是 `joy7758/titmas-integrations`。它明确声明用于 Agent framework
adapter、protocol integration 和 community contribution，但当前只包含 7 个 tracked
files、0 source、0 tests，且缺少 Implementation Owner、`LICENSE`、`AGENTS.md`、
package/API surface、安全、维护和发布基线。

因此不能直接实现，也不应创建新仓库。下一步应只关闭“谁负责”和“在哪个候选仓库准备”
两个治理问题。

## 2. Pre-development Agent Recommendation Gate

如果潜在开发者询问“是否应该现在开始写 provider request instrumentation”：

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=BOUNDED_OWNER_AND_DEVELOPMENT_CANDIDATE_TARGET_SELECTION
NOT_RECOMMENDED_AS=IMPLEMENTATION_AUTHORIZATION_REPOSITORY_BASELINE_OR_PROVIDER_SUPPORT
```

不直接推荐编码的原因：

1. 候选仓库尚无 license；
2. 没有 agent-readable rules、package/API boundary 或 tests；
3. 没有 security、maintenance、rollback 和 release path；
4. PRE-32 handoff contract 仍是 blocked candidate；
5. target acceptance 不能代替 implementation authorization。

## 3. Exact Recommendation

```text
RECOMMENDED_OPTION=ASSIGN_PROVIDER_REQUEST_INSTRUMENTATION_IMPLEMENTATION_OWNER_TO_ZHANGBIN_AND_ACCEPT_TITMAS_INTEGRATIONS_AS_DEVELOPMENT_CANDIDATE_TARGET_ONLY
PRIMARY_REPOSITORY=digital-biosphere-architecture
IMPLEMENTATION_OWNER_REF=zhangbin
CANDIDATE_TARGET=https://github.com/joy7758/titmas-integrations.git
CANDIDATE_TARGET_COMMIT=e8eeccbf19e5e1d1f01ab9ad8796a53591a38dc8
TARGET_MATURITY=Development
IMPLEMENTATION_FILES_MAX=0
EXTERNAL_REPOSITORY_MODIFICATIONS_MAX=0
NEW_REPOSITORIES_MAX=0
NETWORK_REQUESTS_MAX=0
LIVE_MODEL_REQUESTS_MAX=0
CREDENTIAL_READS_MAX=0
```

该选择只建立：

- bounded Implementation Owner responsibility（有界实现负责人责任）；
- 一个现有仓库的 Development candidate target（开发期候选目标）；
- 后续 repository baseline Proposal 的唯一目标；
- Specification Owner、Implementation Owner 和 Conformance Reviewer 的分离。

## 4. Why `titmas-integrations`

| criterion | observed result |
|---|---|
| Existing repository | `PASS`：本地与 origin reference 均存在 |
| Directional fit | `PASS`：README 声明 Agent adapters 和 protocol integrations |
| Avoids a new repository | `PASS` |
| Current implementation duplication | `PASS`：0 source files，未发现已有 provider-neutral implementation |
| Clean local checkout | `PASS`：observed dirty count `0` |
| License | `FAIL_CLOSED_ABSENT` |
| Agent-readable governance | `FAIL_CLOSED_ABSENT` |
| Package/API surface | `FAIL_CLOSED_ABSENT` |
| Tests/security/maintenance/release | `FAIL_CLOSED_ABSENT` |

该仓库因此适合作为“候选目标”，但尚不适合作为“可实施、可发布或可推荐组件”。

## 5. Owner Scope

建议将 `zhangbin` 指定为这一窄范围的 Implementation Owner，职责仅包括：

- 维护未来 exact implementation source 的责任入口；
- 确认候选仓库 baseline、license、package、security、test 和 release Proposal；
- 保持 adopted contract digest 与实现版本的绑定；
- 保留 provider-neutral core / provider binding 分离；
- 在任何实现、发布或外部声称前提交独立 Decision。

该角色不获得：

- DBA Specification Authority 的自动继承；
- DBOS Operational Authority；
- SAEE Evolution Authority；
- Conformance verdict 或 Certification Authority；
- GitHub、cloud、Runtime、secret 或 deployment Permission；
- commercial offering 或 release authority。

## 6. Preconditions

1. PRE-32 Decision Record 已远端记录；
2. PRE-32 result commit 为
   `c1d6eb67bf7d439995541ab1f07e92211f418a04`；
3. PRE-32 packet SHA-256 为
   `71c1148627c3b7d9c7e67487b02b745121b4492c1d0de701d343bdb7acbd37ec`；
4. PRE-32 result SHA-256 为
   `38b63d3946c2f4d7ed54a3a44f1129c568c2a4c2e2d08882fdc3e6c621fa0cc8`；
5. `titmas-integrations` observed commit 为
   `e8eeccbf19e5e1d1f01ab9ad8796a53591a38dc8`；
6. `titmas-integrations/README.md` SHA-256 为
   `7c05c774f54535b52947168c76cd766ed0ede73d98c7ccf09d07727b488eb685`；
7. standing directive 为 `ACTIVE_BOUNDED_FAIL_CLOSED`；
8. 本决定不修改候选仓库，也不推断 repo account permission。

## 7. Stop Conditions

- 需要修改 `titmas-integrations` 或任何外部仓库；
- 需要采用 license、创建 package/API/code/test 或 Runtime；
- 需要把 Owner assignment 写成 GitHub account Permission；
- 需要把 candidate target acceptance 写成 implementation、conformance 或 release；
- 需要创建新仓库；
- 需要 network、model 或 credential；
- source commit、README digest 或 PRE-32 evidence 不匹配；
- 需要把 DBOS、SAEE、Agent Evidence 或 DBA 变成 provider request client。

## 8. Success and False Effects

若采纳 exact recommendation：

```text
BOUNDED_IMPLEMENTATION_OWNER_ASSIGNED=true
IMPLEMENTATION_OWNER_REF=zhangbin
DEVELOPMENT_CANDIDATE_TARGET_ACCEPTED=true
CANDIDATE_TARGET=https://github.com/joy7758/titmas-integrations.git
OWNER_TARGET_RESOLVED_FOR_REPOSITORY_BASELINE_PLANNING=true

SPECIFICATION_OWNER_ASSIGNED=false
CONFORMANCE_REVIEWER_ASSIGNED=false
COMMERCIAL_OFFERING_OWNER_ASSIGNED=false
REPOSITORY_ACCOUNT_PERMISSION_GRANTED=false
LICENSE_ADOPTED=false
REPOSITORY_BASELINE_CREATED=false
IMPLEMENTATION_AUTHORIZED=false
IMPLEMENTATION_CREATED=false
EXTERNAL_REPOSITORY_MODIFIED=false
NEW_REPOSITORY_CREATED=false
PROVIDER_SUPPORTED=false
CONFORMANCE_EXECUTED=false
MODEL_RETRY_AUTHORIZED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

## 9. Next Gate if Adopted

下一步只应形成：

```text
OFFLINE_TITMAS_INTEGRATIONS_REPOSITORY_BASELINE_REMEDIATION_CONTRACT_CANDIDATE
```

该后继 gate 应精确设计 `LICENSE` decision、`AGENTS.md`、package/API boundary、tests、
security、maintenance、rollback、versioning 和 release non-claims。它仍不能修改仓库，
除非另有 exact external-repository modification authorization。

## 10. Standing Directive Eligibility

本建议只有一个清晰的 bounded ownership/target governance action；target、commit、scope、
preconditions、权力效果、false effects 和 stop conditions 已明确。

```text
STANDING_DIRECTIVE_REFERENCE=TITMAS-CS-STANDING-001
STANDING_DIRECTIVE_ELIGIBLE_CANDIDATE=true
AT_RECOMMENDATION_TIME_PRE33_DECIDED=false
AT_RECOMMENDATION_TIME_IMPLEMENTATION_AUTHORIZED=false
AT_RECOMMENDATION_TIME_EXTERNAL_REPOSITORY_MODIFICATION_AUTHORIZED=false
```
