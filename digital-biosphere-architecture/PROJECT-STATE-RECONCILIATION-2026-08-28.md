# Project State Reconciliation — 2026-08-28

```text
PROJECT_STATE_RECONCILIATION=PARTIAL_PASS_COCKPIT_MERGE_BLOCKED
PRIMARY_ACTIVE_PROJECT=红岩公文
PRIMARY_ENGINEERING_DIRECTION=红岩公文
CURRENT_CANONICAL_DOMAIN=https://dcell.net
REDCRAG_CN_ROLE=LEGACY_HISTORICAL_DOMAIN
DIGITAL_CELL_DEMO_STATUS=RELEASED_FROZEN_REFERENCE
DIGITAL_CELL_DEMO_MAINTENANCE_ONLY=true
TITMAS_ROLE=SUPPORTING_INFRASTRUCTURE
DCELL_ROLE=SUPPORTING_ARCHITECTURE
DEB_STATUS=PAUSED
THEORY_EXPANSION_STATUS=PAUSED
```

## Reconciled state

红岩公文是当前真实产品和工程主线。`dcell.net` 是当前公开权威域名。DCell 提供持续
主体架构，TITMAS 与 Evidence 提供边界、执行证据、审查和可验证历史；基础设施支持
产品，产品不是为了证明理论而存在。

Digital Cell Demo `v0.1.0` 已发布、已冻结，只允许不改变冻结语义的维护。DEB、Digital
Survival、Digital Immune、Multi-Cell 和新 TITMAS Runtime 工作默认暂停。

## Repository discovery and actual changes

| Scope | Observed source state | Changes in this reconciliation |
|---|---|---|
| Digital Cell Demo | `joy7758/titmas-demo`, public, `origin/main@2bc410b5ea88dea6a0d7deb8f15d8dde67280f26` | Current README/checklist contradiction correction; one current-state index; existing Release body and repository homepage metadata corrected; PR #5 merged |
| DBA cockpit | `joy7758/digital-biosphere-architecture-specification`, private, `origin/main@40a4b34370578e665767d9ba9a85dca205876b0f` | Current direction, human/machine entry, legacy-site classification, final report, and documentation-only test allowlist; PR #148 remains open because dependency audit failed |
| 红岩公文 | `joy7758/hongyan-official-document`, private; canonical reconciliation branch `875b706edbf687b53df6f39ed73e21e87922aef3` | Read-only; GitHub homepage metadata set to `https://dcell.net`; no source, runtime, deployment, feature, or status-record change |
| Current public site | `https://dcell.net` redirects to `/pilot`; source/runtime ownership remains with 红岩公文 | No visual, branding, architecture, deployment, or redirect change |

Unrelated dirty work was preserved. The primary DBA checkout was dirty, and the primary 红岩公文
workspace contained three unrelated untracked UI artifacts; both were isolated from these changes.

## Validation

```text
DIGITAL_CELL_TEST_COUNT=7
DIGITAL_CELL_TEST_RESULT=PASS
DIGITAL_CELL_DEMO_RUN=PASS
DIGITAL_CELL_DETERMINISTIC_REPLAY=PASS
DIGITAL_CELL_FROZEN_SOURCE_CONSISTENCY=PASS
DIGITAL_CELL_FROZEN_OUTPUT_CONSISTENCY=PASS
DBA_CONFORMANCE=PASS
DBA_UNIT_TESTS=147/147_PASS
DBA_CI_CONFORMANCE=PASS
DBA_CI_DEPENDENCY_AUDIT=FAIL_2_HIGH_NANOID_VIA_POSTCSS
DBA_PR_148_MERGED=false
RED_YAN_STATUS_ARTIFACTS_PARSE=PASS
RED_YAN_GIT_FSCK=PASS_NO_CORRUPTION
DCELL_NET_ROOT_GET=200_AT_HTTPS://DCELL.NET/PILOT
GITHUB_RELEASE_V0_1_0=INTACT_4_ASSETS
NEW_RELEASE_CREATED=false
NEW_TAG_CREATED=false
```

The first DBA unit-test run retained one `UNAPPROVED_CHANGE_PATH` failure because the old
path-scoped test did not recognize the two new state records or the legacy-site README. The
allowlist was narrowed to those documentation-only paths; no site implementation path was opened,
and the complete rerun passed 147/147.

## RedCrag classification

The count scope is the two changed repositories at their `origin/main` baselines plus current
GitHub repository homepage metadata. Baseline source contained 568 case-insensitive
`redcrag.cn` occurrences: 556 were already historical, while 12 appeared on current surfaces.
Two repository homepage references were also current, for 14 stale current references in total.

The merged Demo correction and two live GitHub metadata corrections close 3. The DBA candidate
branch closes the remaining 11, but those corrections are not current `main` truth until PR #148
passes CI and merges.

```text
CURRENT_REDCRAG_REFERENCES=11
HISTORICAL_REFERENCES_PRESERVED=556
STALE_CURRENT_REFERENCES_FIXED=3
STALE_CURRENT_REFERENCES_FIXED_IN_OPEN_PR=11
UNRESOLVED_REFERENCES=11
```

The candidate branch itself has zero current RedCrag references in the audited surfaces. The
nonzero current count above reflects the unmerged DBA `main` state, not a claim that the candidate
still treats RedCrag as canonical.

## Unresolved factual issues

1. `https://dcell.net/digital-cell/`, `/digital-cell.json`, `/.well-known/titmas.json`,
   `/agent-index.json`, and `/llms.txt` all returned 404 on 2026-08-28. No dedicated Digital Cell
   page, TITMAS discovery surface, or public GitHub link was found on the current product page.
2. 红岩公文 remains in `REFINE_CORRECT_SIMPLIFY_STABILIZE_ONLY` freeze mode. Its current running
   commit is `4c98ba8a09eb1ae2d1a5dbdc5c66f8b4131848dd` with high confidence, while the old
   `/srv/hongyan-v1/current` pointer remains at `1e990d5380de83d0048c4ee881ed126b4835d029`.
   The drift class is `MULTIPLE_SIMULTANEOUS_DRIFTS`; no correction, restart, recreate, image
   change, release switch, migration, feature-flag change, or customer-task restart was executed.
3. Three OfficeCLI P1 items remain open: remote runtime drift, macOS screenshot backend, and
   document toolchain lock. The brand deployment receipt commit `9287c8ae9d507bdf4c4769c5e255dda4210198e8`
   still has no corresponding remote branch, so that evidence lineage remains incomplete.
4. Production readiness, real customer validation, `main` merge, and `v1.0.0` tag remain false.
5. DBA PR #148 has a passing conformance check, but its site build fails `npm audit --omit=dev`
   on two high-severity findings in the existing `postcss` to `nanoid <3.3.18` dependency chain.
   This reconciliation changed no package or lock file. Dependency repair is a separate security
   change and was not authorized by this state-only goal, so the PR was not bypassed or merged.

## Exact next action for 红岩公文

```text
RED_YAN_CURRENT_STATE=REMOTE_RUNTIME_CANONICAL_TRUTH_RECONCILED_WITH_MULTIPLE_DRIFTS_AND_3_OPEN_P1
RED_YAN_NEXT_SINGLE_EXECUTABLE_MILESTONE=KEEP_REMOTE_RUNTIME_UNCHANGED_AND_INVESTIGATE_STALE_CONTROL_AND_CONFIGURATION_METADATA
RED_YAN_CURRENT_BLOCKERS=STALE_SRV_CURRENT_POINTER;STALE_BASE_CONTAINER_CONFIGURATION_LABELS;3_OPEN_OFFICECLI_P1;BRAND_DEPLOYMENT_RECEIPT_LINEAGE_NOT_REMOTE
```

This recommendation is investigation-only. It does not authorize a runtime pointer correction,
restart, container recreation, deployment, feature change, merge, tag, release, or production
claim.
