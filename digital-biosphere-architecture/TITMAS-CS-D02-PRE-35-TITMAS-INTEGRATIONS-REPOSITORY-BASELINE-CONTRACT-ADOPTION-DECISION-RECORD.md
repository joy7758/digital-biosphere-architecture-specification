---
document_id: DBA-TITMAS-CS-D02-PRE-35-TITMAS-INTEGRATIONS-REPOSITORY-BASELINE-CONTRACT-ADOPTION-DECISION-0.1
title: TITMAS CS-D02 PRE-35 TITMAS Integrations Repository Baseline Contract Adoption Decision Record v0.1
title_zh: TITMAS CS-D02 PRE-35 TITMAS Integrations 仓库基线契约采纳决定记录 v0.1
version: 0.1.0
status: adopted-as-development-planning-input-only
maturity: Development
decision_id: CS-D02-PRE-35
standing_directive_reference: TITMAS-CS-STANDING-001
decided_by_ref: zhangbin
license_adopted: false
implementation_authorized: false
external_repository_modification_authorized: false
---

# TITMAS CS-D02 PRE-35 TITMAS Integrations Repository Baseline Contract Adoption Decision Record v0.1

## Decision

依据 `TITMAS-CS-STANDING-001`、PRE-34 offline validation 和 PRE-35 exact recommendation，
采用：

```text
DECISION_RESULT=ADOPT_PRE34_EXACT_TITMAS_INTEGRATIONS_REPOSITORY_BASELINE_CONTRACT_AS_DEVELOPMENT_INPUT_ONLY
DECIDED_BY_REF=zhangbin
ADOPTION_MATURITY=Development
TARGET_REPOSITORY=https://github.com/joy7758/titmas-integrations.git
TARGET_COMMIT=e8eeccbf19e5e1d1f01ab9ad8796a53591a38dc8
IMPLEMENTATION_OWNER_REF=zhangbin
```

## Adopted Scope

- `RB0 → RB1 → RI0` staged repository path；
- repository baseline contract exact digest；
- required target file manifest exact digest；
- implementation declaration template exact digest；
- Agent-readable、security、maintenance、rollback 和 non-elevation requirements；
- 每一阶段必须有独立 Decision。

## Non-adopted Scope

- Apache-2.0 license；
- target file content 或 target repository modification；
- package/distribution name、Python version、dependency 或 public API；
- provider SDK、binding、endpoint、model 或 credential；
- implementation、tests、conformance、release、production 或 commercial offering。

## Effects

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
PROVIDER_SUPPORTED=false
CONFORMANCE_EXECUTED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

下一步只能为 `RB0` non-executable repository governance baseline 形成独立 exact
recommendation / Decision。
