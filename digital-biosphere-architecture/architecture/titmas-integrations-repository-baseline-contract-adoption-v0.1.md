---
document_id: DBA-TITMAS-INTEGRATIONS-REPOSITORY-BASELINE-CONTRACT-ADOPTION-0.1
title: TITMAS Integrations Repository Baseline Contract Adoption v0.1
title_zh: TITMAS Integrations 仓库基线契约采纳 v0.1
version: 0.1.0
status: adopted-development-planning-input
maturity: Development
decision_reference: CS-D02-PRE-35
license_adopted: false
implementation_authorized: false
target_repository_modified: false
---

# TITMAS Integrations Repository Baseline Contract Adoption v0.1

## Adopted Development Inputs

| artifact | SHA-256 |
|---|---|
| repository baseline contract | `58920eb5b8c7ce1ecde66472743d408342f7fe7b418b323f48cf28c370c8537b` |
| required target file manifest | `6135526966bef14ef2d4b33ae55c7fa62266b338a086b30be86aee2f335db664` |
| implementation declaration template | `40de6b9975005b3e8a76a8f5326da815bff7c7d6ae22f488e8fc01d1fa815cc5` |

相应三项 Schema 也以 PRE-35 Decision 中的 exact digest 绑定。

## Adoption Effect

未来 `titmas-integrations` Proposal 必须：

1. 先完成 `RB0` non-executable governance baseline；
2. 再单独决定 `RB1` package / contract skeleton；
3. 最后单独决定 `RI0` instrumentation implementation；
4. 保持 Owner、spec digest、target commit、license、security、tests、rollback 和 claims
   可追溯。

```text
REPOSITORY_BASELINE_CONTRACT_ADOPTED=true
ADOPTION_MATURITY=Development
LICENSE_ADOPTED=false
TARGET_REPOSITORY_MODIFIED=false
REPOSITORY_BASELINE_APPLIED=false
IMPLEMENTATION_AUTHORIZED=false
PROVIDER_SUPPORTED=false
```
