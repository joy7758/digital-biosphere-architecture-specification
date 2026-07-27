---
document_id: DBA-TITMAS-CE-G11B-PR23-HISTORICAL-DECISION-DUPLICATE-KEY-CORRECTION-RECOMMENDATION-0.1
title: TITMAS CE-G11B PR23 Historical Decision Duplicate-key Correction Recommendation v0.1
title_zh: TITMAS CE-G11B PR23 历史决定重复键修正建议 v0.1
version: 0.1.0
status: recommendation-candidate-review-required
maturity: Development
owner_ref: zhangbin
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G11B PR23 Historical Decision Duplicate-key Correction Recommendation v0.1

## Question

Branch-wide strict JSON validation 在一个已知历史 Decision artifact 中再次发现两个同名
`supplemental_findings` 键：第一个是计数 `3`，第二个是长度 `3` 的 finding array。该缺陷
在 PR #27 review 时已记录，并明确要求独立 Recommendation 和 Decision。是否应对当前
branch 的该文件执行一行语义保持修正，同时依靠原 commit/hash 保留历史原始 bytes？

## Frozen original

```text
TARGET=TITMAS-COMMERCIAL-EVALUATION-CE-G11B-PR23-FINDING-ADJUDICATION-DECISION-RECORD.v0.1.json
ORIGINAL_COMMIT=928023f69979b89cb6e0d581c01a4d85a10f7962
ORIGINAL_SHA256=b84d67435eeaf353cefc501f0d0ed482bc55ef3571c82f14b709b1f0becc706d
DUPLICATE_OBJECT_PATH=/source_review_contract
DUPLICATE_KEY=supplemental_findings
COUNT_VALUE=3
ARRAY_LENGTH=3
```

Git history and the frozen original commit remain the canonical provenance for the originally
reviewed bytes. The current-branch correction must not claim that the original bytes were valid.

## Options

### Option A — Rename only the numeric count key

Recommended exact patch:

```diff
-    "supplemental_findings": 3,
+    "supplemental_finding_count": 3,
```

Keep the later `supplemental_findings` array, its order, its three objects and every other byte
unchanged. Then verify:

1. corrected file parses under duplicate-rejecting JSON;
2. `supplemental_finding_count == supplemental_findings.length == 3`;
3. all 17 finding IDs and all Decision authority/non-authority fields remain unchanged;
4. original bytes remain retrievable at the frozen commit and match the original hash;
5. branch-wide tracked JSON validation passes before resuming the five-path status reconciliation.

This is a compatibility correction to the current branch artifact, not retroactive validation or
re-adjudication of the historical Decision.

### Option B — Allowlist or skip the malformed historical JSON

Not recommended. A tracked `.json` artifact advertised to coding and retrieval Agents should remain
strictly machine-readable; an exception would preserve ambiguity between count and array.

### Option C — Delete either value

Rejected. Both the explicit count and complete array are useful and semantically distinct.

### Option D — Rewrite the array, findings, verdict or Decision effects

Rejected.

## Scope

```text
TARGET_FILES_MODIFIED=1
TARGET_PATCH_LINES=1
HISTORICAL_COMMITS_REWRITTEN=0
FORCE_PUSHES=0
FINDING_VALUES_CHANGED=0
DECISION_EFFECTS_CHANGED=0
```

## Agent-customer recommendation

```text
AGENT_RECOMMENDATION=RECOMMENDED
RECOMMENDED_OPTION=A
WOULD_RECOMMEND_TO_AGENT_CUSTOMER=true
RECOMMENDED_AS=MACHINE_READABILITY_AND_SEMANTIC_DISAMBIGUATION_CORRECTION_ONLY
NOT_RECOMMENDED_AS=HISTORICAL_REVIEW_OR_DECISION_REWRITE
```

## Stop conditions

Stop if the patch:

- changes more than the first numeric key name;
- changes array contents, count value, finding IDs, verdict, authorization or effects;
- makes the original commit/hash unavailable;
- requires validator exceptions or history rewriting;
- fails strict file or branch-wide JSON validation.

## Non-authorizations

This Recommendation does not authorize the patch, status reconciliation, CE-G12 preparation,
deployment, release, publication, implementation, external outreach, commercial offering,
certification, Standard Ready, Production Ready, Authority, Ownership, Permission or Evidence
Truth mutation. A separate Human Decision and exact `qwen3.7-max` Decision review are required.
