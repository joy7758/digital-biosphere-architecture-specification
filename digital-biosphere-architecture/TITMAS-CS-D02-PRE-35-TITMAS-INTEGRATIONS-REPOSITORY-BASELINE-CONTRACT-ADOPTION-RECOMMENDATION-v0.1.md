---
document_id: DBA-TITMAS-CS-D02-PRE-35-TITMAS-INTEGRATIONS-REPOSITORY-BASELINE-CONTRACT-ADOPTION-RECOMMENDATION-0.1
title: TITMAS CS-D02 PRE-35 TITMAS Integrations Repository Baseline Contract Adoption Recommendation v0.1
title_zh: TITMAS CS-D02 PRE-35 TITMAS Integrations 仓库基线契约采纳建议 v0.1
version: 0.1.0
status: exact-development-adoption-recommendation-not-decided
maturity: Development
decision_reference: CS-D02-PRE-35
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
implementation_authorized: false
external_repository_modification_authorized: false
license_adopted: false
---

# TITMAS CS-D02 PRE-35 TITMAS Integrations Repository Baseline Contract Adoption Recommendation v0.1

## 1. Review Question

PRE-34 已离线形成并验证：

- repository baseline contract candidate；
- required target file manifest；
- implementation declaration template；
- `RB0 → RB1 → RI0` staged gate；
- 4 套 Schema / instance validation；
- 0 target repository modifications。

现在需要决定是否把三项 exact artifacts 采纳为 `Development` repository-baseline planning
input，而不是继续依赖叙述性计划。

## 2. Agent Recommendation

```text
AGENT_RECOMMENDATION=RECOMMENDED_WITH_STRICT_NON_EFFECTS
RECOMMENDED_AS=DEVELOPMENT_REPOSITORY_BASELINE_PLANNING_INPUT
NOT_RECOMMENDED_AS=LICENSE_ADOPTION_TARGET_MODIFICATION_IMPLEMENTATION_OR_RELEASE
```

推荐理由：

1. 明确分离 RB0、RB1 和 RI0；
2. RB0 禁止 package/runtime code；
3. license 只保留 candidate，不自动继承相邻仓库；
4. Agent 入口、machine entry、security、maintenance 和 claims 先于代码；
5. provider-neutral core 与 provider binding 被分离；
6. P0–P9、失败保留、secret non-persistence 和 non-elevation 可进入后续测试；
7. 目标仓库 source、Owner 和 commit 已绑定。

## 3. Exact Recommendation

```text
RECOMMENDED_OPTION=ADOPT_PRE34_EXACT_TITMAS_INTEGRATIONS_REPOSITORY_BASELINE_CONTRACT_AS_DEVELOPMENT_INPUT_ONLY
PRIMARY_REPOSITORY=digital-biosphere-architecture
ADOPTION_MATURITY=Development
TARGET_REPOSITORY=https://github.com/joy7758/titmas-integrations.git
TARGET_COMMIT=e8eeccbf19e5e1d1f01ab9ad8796a53591a38dc8
IMPLEMENTATION_OWNER_REF=zhangbin
EXTERNAL_REPOSITORY_MODIFICATIONS_MAX=0
IMPLEMENTATION_FILES_MAX=0
NETWORK_REQUESTS_MAX=0
LIVE_MODEL_REQUESTS_MAX=0
CREDENTIAL_READS_MAX=0
```

采纳对象：

| artifact | SHA-256 |
|---|---|
| `repository-baseline-contract.v0.1.json` | `58920eb5b8c7ce1ecde66472743d408342f7fe7b418b323f48cf28c370c8537b` |
| `repository-baseline-contract.schema.v0.1.json` | `aea7407462c996ea7f6986a2607e5dc35cb84a28a1d4210f0951edeab2d98dd8` |
| `required-target-file-manifest.v0.1.json` | `6135526966bef14ef2d4b33ae55c7fa62266b338a086b30be86aee2f335db664` |
| `required-target-file-manifest.schema.v0.1.json` | `ea93d55c824de2bc1b8de77c929c9df2c3708ea86437f65f735a9c719b672173` |
| `implementation-declaration-template.v0.1.json` | `40de6b9975005b3e8a76a8f5326da815bff7c7d6ae22f488e8fc01d1fa815cc5` |
| `implementation-declaration-template.schema.v0.1.json` | `1649414c13f28d364c5ce1b20b0a66067192b74c9f28b425118a789ccc109377` |

## 4. Adopted Meaning

若采纳：

- 未来 target modification Proposal 必须按 `RB0 → RB1 → RI0` 顺序；
- RB0 只允许 non-executable governance baseline；
- RB1 和 RI0 必须分别获得新的 exact Decision；
- 未来实现声明必须填写 supported/partial/unsupported/unknown；
- contract digest、target commit 和 Owner 必须显式绑定；
- failure、unknown、unsupported 和 rollback history 必须保留。

## 5. Explicitly Not Adopted

- Apache-2.0 license；
- 任何 target file content；
- package/distribution name、Python version、dependency 或 public API；
- provider SDK、endpoint、model 或 credential；
- implementation、tests execution、conformance、security approval；
- provider support、release、production 或 commercial availability。

## 6. Preconditions

1. PRE-34 Decision commit：
   `07738993489846cb06040d99cbc725595954076f`；
2. PRE-34 Decision JSON SHA-256：
   `16156f5b720d5d7b63a3fae02dc500ba891557a39b626159f38a9663d9fca36b`；
3. PRE-34 result commit：
   `f0d4713fecb52a39d017e2f82be48b4ffe90444b`；
4. PRE-34 result SHA-256：
   `af76e8222f14fdf8290a8535e4f3889fa0fdc521cb07eef07383371dba5f47d0`；
5. 三项 artifact 和三项 Schema digest 匹配；
6. target repository 保持 observed commit；
7. standing directive active。

## 7. Stop Conditions

- 任一 digest 不匹配；
- 需要修改 target repository；
- 需要采用 license 或创建 file/package/code/test；
- 需要 network、provider API、model 或 credential；
- Development adoption 被写成 implementation、conformance、release 或 commercial claim；
- Owner / target assignment 被撤销或冲突；
- RB0、RB1、RI0 被合并为一次无界实现。

## 8. Effects

```text
REPOSITORY_BASELINE_CONTRACT_ADOPTED=true
REQUIRED_TARGET_FILE_MANIFEST_ADOPTED=true
IMPLEMENTATION_DECLARATION_TEMPLATE_ADOPTED=true
ADOPTION_MATURITY=Development

LICENSE_ADOPTED=false
TARGET_REPOSITORY_MODIFIED=false
REPOSITORY_BASELINE_APPLIED=false
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

## 9. Next Gate if Adopted

下一步可以形成 `PRE-36` exact recommendation，只处理：

```text
TITMAS_INTEGRATIONS_RB0_NON_EXECUTABLE_REPOSITORY_GOVERNANCE_BASELINE
```

PRE-36 必须逐文件冻结内容、license Decision、validation、rollback 和 target branch；不得
包含 package、runtime、provider request、model call 或 conformance execution。

## 10. Standing Directive Eligibility

本建议只有一个 DBA Development adoption action；exact artifacts、digests、target、Owner、
scope、non-effects 和 stop conditions 已明确。

```text
STANDING_DIRECTIVE_REFERENCE=TITMAS-CS-STANDING-001
STANDING_DIRECTIVE_ELIGIBLE_CANDIDATE=true
AT_RECOMMENDATION_TIME_PRE35_DECIDED=false
AT_RECOMMENDATION_TIME_LICENSE_ADOPTED=false
AT_RECOMMENDATION_TIME_TARGET_MODIFICATION_AUTHORIZED=false
```
