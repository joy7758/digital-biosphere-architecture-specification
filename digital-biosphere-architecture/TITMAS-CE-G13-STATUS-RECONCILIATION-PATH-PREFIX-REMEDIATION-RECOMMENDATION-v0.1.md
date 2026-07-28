---
document_id: DBA-TITMAS-CE-G13-STATUS-RECONCILIATION-PATH-PREFIX-REMEDIATION-RECOMMENDATION-0.1
title: TITMAS CE-G13 Status Reconciliation Path-prefix Remediation Recommendation v0.1
title_zh: TITMAS CE-G13 状态对账路径前缀修复建议 v0.1
version: 0.1.0
status: recommendation-only
maturity: Development
owner_ref: zhangbin
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G13 Status Reconciliation Path-prefix Remediation Recommendation v0.1

## Problem

The sole validation authorized by
`TITMAS-COMMERCIAL-EVALUATION-CE-G13-INPUT-BINDING-SUPPLEMENT-STATUS-RECONCILIATION-DECISION-RECORD.v0.1.json`
failed closed at the first check.

Git returned exactly seven intended paths, but the repository uses a parent Git top-level:

```text
GIT_TOPLEVEL=/private/tmp/titmas-ce-g11b-decision.2dqOYW
WORKING_DIRECTORY=/private/tmp/titmas-ce-g11b-decision.2dqOYW/digital-biosphere-architecture
RETURNED_PREFIX=digital-biosphere-architecture/
ACTUAL_PATH_COUNT=7
EXPECTED_PATH_COUNT=7
```

The validator compared the prefixed paths with repository-relative expected paths. No later check
ran. This is a harness path-normalization defect, not evidence that the proposed path set expanded.

## Options

### Option A — bounded prefix-aware replacement validation (recommended)

- preserve the v0.1 failed report and result unchanged;
- verify that the Git top-level is the exact parent of the working directory;
- derive the only allowed prefix from the working-directory basename;
- require every changed path to start with that exact prefix;
- remove the prefix once, then compare the normalized set to the exact seven allowed paths;
- run one replacement local-only validation;
- write a new v0.2 result and report; never edit failure into PASS;
- commit and push only if the replacement validation passes.

### Option B — move the worktree to a Git top-level repository

Rejected for this cycle because it changes repository layout and adds unnecessary migration risk.

### Option C — ignore path prefixes

Rejected because broad suffix matching could admit paths from another repository.

## Exact recommended action

```text
RECOMMENDED_OPTION=A
RECOMMENDED_ACTION=AUTHORIZE_ONE_PREFIX_BOUND_REPLACEMENT_RECONCILIATION_VALIDATION
EXPECTED_REPOSITORY_PREFIX=digital-biosphere-architecture/
V0_1_FAILURE_PRESERVED=true
V0_1_RETRY=false
V0_2_REPLACEMENT_RUN_CAP=1
NETWORK_ALLOWED=false
CREDENTIAL_READ_ALLOWED=false
MODEL_REQUEST_AFTER_DECISION_REVIEW_ALLOWED=false
CE_G13_EXECUTION_ALLOWED=false
```

## Replacement scope

The replacement execution may carry forward the same five proposed canonical status changes and
must add immutable failure evidence plus new replacement outputs:

1. `MASTER-ROADMAP.md`
2. `PROGRAM-STATUS.md`
3. `TITMAS-COMMERCIALIZATION-STANDARDS-ENTRY-v0.1.json`
4. `architecture/schemas/titmas-commercialization-standards-entry.schema.v0.1.json`
5. `architecture/titmas-commercialization-standards-roadmap-v0.1.md`
6. `TITMAS-CE-G13-INPUT-BINDING-SUPPLEMENT-STATUS-RECONCILIATION-REPORT-v0.1.md`
7. `commercial-evaluation-fresh-candidate/ce-g13-input-binding-supplement-status-reconciliation-result.v0.1.json`
8. `TITMAS-CE-G13-INPUT-BINDING-SUPPLEMENT-STATUS-RECONCILIATION-REPORT-v0.2.md`
9. `commercial-evaluation-fresh-candidate/ce-g13-input-binding-supplement-status-reconciliation-result.v0.2.json`

The v0.1 files must retain `FAIL_CLOSED_EXACT_PATH_REPOSITORY_PREFIX_MISMATCH`. The v0.2 files may
state PASS only from the one replacement run.

## Required replacement checks

- exact Git top-level and working-directory relationship;
- every path has the one expected prefix;
- normalized path set equals the exact nine-path replacement scope;
- duplicate-key rejection for all tracked JSON plus both result records;
- machine entry validates against its Draft 2020-12 Schema;
- five canonical surfaces agree;
- referenced hashes and commits match;
- replacement remote branch matches the local parent;
- base and supplement package manifests remain unchanged;
- secret scan passes;
- execution and authority effects remain zero.

Failure must stop closed and produce no retry under this recommendation.

## Non-authorizations

This Recommendation does not authorize:

- a validation run or commit;
- public fetch, Agent session, technical reuse or CE-G13 execution;
- Runtime, Agent, Entity, Capability, Permission or Evidence Truth;
- release, offering, certification, Standard Ready or Production Ready;
- force-push, overwrite of the diverged branch, PR creation or merge.

```text
Recommendation != Decision
Decision != Execution
Evidence != Truth
Evaluation != Authority
Capability != Permission
```
