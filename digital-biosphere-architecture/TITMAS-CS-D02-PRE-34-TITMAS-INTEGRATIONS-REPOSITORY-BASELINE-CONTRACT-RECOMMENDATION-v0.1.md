---
document_id: DBA-TITMAS-CS-D02-PRE-34-TITMAS-INTEGRATIONS-REPOSITORY-BASELINE-CONTRACT-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-34 TITMAS Integrations Repository Baseline Contract Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-34 TITMAS Integrations 仓库基线契约建议 v0.1
version: 0.1.0
status: exact-offline-repository-baseline-contract-recommendation-not-decided
maturity: Development
decision_reference: CS-D02-PRE-34
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
target_repository: https://github.com/joy7758/titmas-integrations.git
implementation_authorized: false
external_repository_modification_authorized: false
---

# TITMAS CS-D02 PRE-34 TITMAS Integrations Repository Baseline Contract Recommendation v0.1

## 1. Why PRE-34 Exists

PRE-33 已：

- 指定 `zhangbin` 为 Provider Request Instrumentation 的 bounded Implementation Owner；
- 把 `joy7758/titmas-integrations` 接受为 repository baseline planning 的 Development
  candidate target；
- 保持 implementation、license adoption、repo modification、conformance 与 release
  全部为 false。

候选仓库仍只有 README 和空目录 scaffolding。若直接添加代码，会绕过 license、
agent-readable entry、package boundary、security、tests、maintenance 和 rollback 的统一
基线。

## 2. Pre-development Agent Recommendation Gate

如果潜在开发者询问“现在是否推荐在 `titmas-integrations` 中开始实现”：

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=OFFLINE_REPOSITORY_BASELINE_CONTRACT_DESIGN
NOT_RECOMMENDED_AS=TARGET_REPOSITORY_MODIFICATION_PACKAGE_IMPLEMENTATION_OR_RELEASE
```

## 3. Exact Recommendation

```text
RECOMMENDED_OPTION=AUTHORIZE_OFFLINE_TITMAS_INTEGRATIONS_REPOSITORY_BASELINE_REMEDIATION_CONTRACT_CANDIDATE_ONLY
PRIMARY_REPOSITORY=digital-biosphere-architecture
TARGET_REPOSITORY=https://github.com/joy7758/titmas-integrations.git
TARGET_COMMIT=e8eeccbf19e5e1d1f01ab9ad8796a53591a38dc8
IMPLEMENTATION_OWNER_REF=zhangbin
IMPLEMENTATION_FILES_MAX=0
EXTERNAL_REPOSITORY_MODIFICATIONS_MAX=0
NEW_REPOSITORIES_MAX=0
NETWORK_REQUESTS_MAX=0
LIVE_MODEL_REQUESTS_MAX=0
CREDENTIAL_READS_MAX=0
```

只建议在 DBA 中形成：

1. repository baseline contract candidate；
2. required target file manifest；
3. license candidate and decision boundary；
4. `AGENTS.md` / `llms.txt` / machine entry requirements；
5. package、namespace、provider-neutral core 与 provider binding boundary；
6. test、negative case、security、secret、maintenance 和 rollback checklist；
7. implementation declaration template；
8. 后续 target-repository modification Decision 的 exact prerequisites。

## 4. Required Baseline Surfaces

候选契约至少覆盖：

| surface | candidate requirement | current target state |
|---|---|---|
| `LICENSE` | exact SPDX license text and Decision reference | `ABSENT` |
| `AGENTS.md` | machine-readable scope, non-goals, commands, claim boundaries | `ABSENT` |
| `llms.txt` / machine entry | discovery, supported/unsupported, canonical links | `ABSENT` |
| package metadata | exact name, version, Python requirement, dependencies | `ABSENT` |
| source layout | provider-neutral core separated from provider bindings | `ABSENT` |
| tests | deterministic contract, negative boundary and no-secret cases | `ABSENT` |
| security | secret, endpoint, timeout, payload, logging and disclosure policy | `ABSENT` |
| maintenance | Owner, versioning, deprecation, archive and rollback | `ABSENT` |
| release | non-claims, clean clone, supply chain and explicit release Decision | `ABSENT` |

## 5. License Candidate Boundary

`Apache-2.0` 可以作为 exact candidate，因为 TITMAS public entry、DBOS、TITMAS Demo 和
Agent Evidence 的相邻公开表面已采用 Apache-2.0，且它适合可替换的开放基础设施实现。

但 PRE-34 只能记录：

```text
LICENSE_CANDIDATE=Apache-2.0
LICENSE_ADOPTED=false
LICENSE_FILE_CREATED=false
```

相邻仓库许可证或 `DQ-012` 不能自动重许可 `titmas-integrations`；必须由后续 exact
repository license Decision 明确采纳。

## 6. Package and Namespace Candidate Boundary

候选契约可以定义语义边界，但不能创建 package：

```text
PYTHON_IMPORT_NAMESPACE_CANDIDATE=titmas_integrations
PROVIDER_NEUTRAL_MODULE_CANDIDATE=titmas_integrations.instrumentation
PROVIDER_BINDING_NAMESPACE_CANDIDATE=titmas_integrations.providers
PACKAGE_NAME=NOT_DECIDED
PUBLIC_API=NOT_DECIDED
VERSION=NOT_DECIDED
```

必须防止：

- 把 provider SDK 包装成 TITMAS core；
- 把 DBOS Evidence Admission 放进 transport package；
- 把 SAEE Evaluation 或 Recommendation 放进 request execution；
- 把 observation 自动升级为 Evidence、Truth、Permission 或 Decision；
- 在 package metadata 中声明未验证 provider support。

## 7. Test and Security Candidate Boundary

最低后继测试类别：

1. P0–P9 order and predecessor continuity；
2. first-failure and dependent-phase closure；
3. timeout、partial write/read、truncation 和 unknown envelope；
4. retry/fallback/repair/alias substitution fail-closed；
5. credential/header/raw body/prompt/review content/hidden reasoning non-persistence；
6. provider-neutral core / provider binding separation；
7. Observation / Evidence / Verification / Permission non-elevation；
8. disable/rollback preserving failure history；
9. clean-clone and declared dependency boundary；
10. implementation declaration supported/partial/unsupported/unknown consistency。

PRE-34 不执行这些测试。

## 8. Preconditions

1. PRE-33 Decision commit：
   `1ca850b5015b16e357aeeda12f315d9ee1a9e5e3`；
2. PRE-33 Decision JSON SHA-256：
   `b561daf8fade1f2febafe3499700e6ce5d07c9e4cf3b5e17c8c9707fbb3e2194`；
3. Owner/Target Assignment JSON SHA-256：
   `43e6225c2e7a71891858b394f8d89b789c2ac3303a269e2ca74a27166df37541`；
4. target commit：
   `e8eeccbf19e5e1d1f01ab9ad8796a53591a38dc8`；
5. target README SHA-256：
   `7c05c774f54535b52947168c76cd766ed0ede73d98c7ccf09d07727b488eb685`；
6. standing directive active；
7. target repository 不被修改。

## 9. Stop Conditions

- 需要修改 `titmas-integrations`；
- 需要创建 `LICENSE`、`AGENTS.md`、`llms.txt`、package、code 或 tests；
- 需要采用 license 或 package name；
- 需要 network、provider API、model 或 credential；
- 需要把 candidate contract 写成 implementation authorization；
- 需要声称 provider support、conformance、release、production 或 commercial availability；
- target source 或 PRE-33 evidence 不匹配；
- 要求新建仓库或把实现改放 DBA、DBOS、SAEE、Agent Evidence 或应用层。

## 10. Success and False Effects

```text
REPOSITORY_BASELINE_CONTRACT_CANDIDATE_DEFINED=true
REQUIRED_TARGET_FILE_MANIFEST_DEFINED=true
LICENSE_CANDIDATE_DEFINED=true
AGENT_READABLE_ENTRY_REQUIREMENTS_DEFINED=true
PACKAGE_NAMESPACE_BOUNDARY_CANDIDATE_DEFINED=true
TEST_SECURITY_MAINTENANCE_ROLLBACK_CHECKLIST_DEFINED=true

LICENSE_ADOPTED=false
REPOSITORY_BASELINE_ADOPTED=false
TARGET_REPOSITORY_MODIFIED=false
IMPLEMENTATION_AUTHORIZED=false
IMPLEMENTATION_CREATED=false
PACKAGE_CREATED=false
API_CREATED=false
TESTS_EXECUTED=0
PROVIDER_SUPPORTED=false
CONFORMANCE_EXECUTED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

## 11. Standing Directive Eligibility

本建议是一个 DBA-only、offline、contract-design action；exact target、source commit、
Owner、输出、限制、false effects 和 stop conditions 已明确。

```text
STANDING_DIRECTIVE_REFERENCE=TITMAS-CS-STANDING-001
STANDING_DIRECTIVE_ELIGIBLE_CANDIDATE=true
AT_RECOMMENDATION_TIME_PRE34_DECIDED=false
AT_RECOMMENDATION_TIME_EXTERNAL_REPOSITORY_MODIFICATION_AUTHORIZED=false
AT_RECOMMENDATION_TIME_IMPLEMENTATION_AUTHORIZED=false
```
