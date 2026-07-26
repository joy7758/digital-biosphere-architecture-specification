---
document_id: DBA-TITMAS-CS-D02-PRE-09-PUBLIC-FIRST-PARTY-DESK-RESEARCH-DECISION-RECORD-0.1
title: TITMAS CS-D02 PRE-09 Public First-party Desk Research Decision Record v0.1
title_zh: TITMAS CS-D02 PRE-09 公开第一方问题 desk research 决定记录 v0.1
version: 0.1.0
status: decided-authorize-one-bounded-public-desk-research-run
maturity: Development
maturity_scope: entire-document
owner_ref: zhangbin
decision_id: CS-D02-PRE-09
parent_decision_id: CS-D02
standing_directive_reference: TITMAS-CS-STANDING-001
decided_by_ref: zhangbin
decided_at: 2026-07-26T08:29:20Z
authority_effect: bounded-public-read-and-minimal-metadata-only
implementation_authorized: false
commercial_effect: none
---

# TITMAS CS-D02 PRE-09 Public First-party Desk Research Decision Record v0.1

## 1. Decision（决定）

依据
[`TITMAS-CS-STANDING-001`](TITMAS-COMMERCIALIZATION-STANDING-RECOMMENDATION-AUTHORIZATION-v0.1.md)、
[PRE-08 method adoption](architecture/veap-public-first-party-problem-report-method-adoption-v0.2.md)
和 [exact recommendation](TITMAS-CS-D02-PUBLIC-FIRST-PARTY-DESK-RESEARCH-RECOMMENDATION-v0.1.md)，
Human Program Owner `zhangbin` 决定：

```text
DECISION_ID=CS-D02-PRE-09
DECISION_RESULT=AUTHORIZE_ONE_BOUNDED_PUBLIC_DESK_RESEARCH_RUN
DECIDED_BY_REF=zhangbin
```

## 2. Authorized Envelope（授权包络）

| Item | Exact limit |
|---|---|
| Execution | one run |
| Search queries | frozen 8, each at most once |
| Public pages opened | maximum 12 |
| Candidate records | maximum 4 |
| Source time window | `2025-01-01T00:00:00Z` through `2026-07-26T23:59:59Z` |
| Access | anonymous public read only |
| Stored source content | none |
| Quotation | at most 25 words per source |
| Direct personal identifiers | prohibited |
| Candidate counting | prohibited |

授权的 hosts/path prefixes 和 exact query 均以
[frozen execution plan](commercialization-standards-public-source-problem-validation/desk-research-execution-plan-v0.1.md)
为准。

冻结机器材料：

| Artifact | SHA-256 |
|---|---|
| `desk-research-execution-plan.v0.1.json` | `c2b749675f2f4d2330e57bf60518f83b6810db2bdb6b8f996662d6e69703a8be` |
| `desk-research-execution-plan.schema.v0.1.json` | `e3e84de35b0ce25117c60c5fe651fd0ab64d88373e871fa493e26d9d4776aefa` |
| `public-first-party-problem-candidate.schema.v0.1.json` | `546fff6092b867300e1360335d955cb4e2a0e00f85f54e4c8fd697b691c90742` |
| `source-candidate-set.schema.v0.1.json` | `a958f9bdfae8a98a881b3832d82b9c95abff100c82d56cd0b972e8b6ce06ec19` |

## 3. Roles（角色）

- Decision Owner、Data Steward、Incident Owner、Appeal Owner、Counting Owner：
  `zhangbin`；
- Execution Recorder：`codex`；
- candidate creator 不得自我把记录升级为 `VALID`；
- 后续独立 Agent review 和逐记录 Human Decision 不在本决定范围内。

## 4. Data Handling（数据处理）

允许只保存：

- canonical public URL；
- organization/project publisher reference；
- published/updated/observed time；
- non-personal accountable-role reference；
- 不超过 25 个引用词或 public-safe paraphrase；
- qualification fields、known limitation 和 metadata hash。

禁止保存：

- 原始页面、HTML、附件、截图或全文；
- 联系方式、账号、个人姓名或其他直接标识；
- credential、private log、customer/private data；
- 搜索 Cookie、认证材料或 provider raw envelope。

临时 excerpt 必须在同一执行会话的 record extraction 完成后删除；只保留最小 metadata、
hash 和 deletion tombstone。

## 5. Failure and Rollback（失败与回滚）

- 登录、验证码、付费墙、robots/terms 冲突或任何访问控制：立即停止该来源；
- allowlist、时间窗、cap 或 digest 失败：停止整个 run；
- 已产生 candidate 不删除或覆盖，标记 `INVALID_AUTHORIZATION_ENVELOPE` 并保持 count false；
- 删除临时 excerpt 后保留删除时间和 hash tombstone；
- 零候选、全部 `PARTIAL/INVALID` 或来源冲突是有效结果，不扩大搜索范围补齐数量。

## 6. Maximum Positive Effect（最大正向效果）

```text
PUBLIC_DESK_RESEARCH_EXECUTION_AUTHORIZED=true
PUBLIC_SOURCE_SEARCH_AUTHORIZED=true
PUBLIC_SOURCE_COLLECTION_AUTHORIZED=MINIMAL_PUBLIC_METADATA_ONLY
PUBLIC_SOURCE_CANDIDATE_CREATION_AUTHORIZED=true
PUBLIC_SOURCE_CANDIDATE_RECORDS_MAX=4

PUBLIC_SOURCE_RECORD_COUNTING_AUTHORIZED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
```

## 7. Non-effects（非效果）

```text
AUTHORITY_CHANGED=false
OWNERSHIP_CHANGED=false
FULL_CS_D02_EXECUTION_AUTHORIZED=false
PUBLIC_SOURCE_RECORD_COUNTING_AUTHORIZED=false
EXTERNAL_OUTREACH_AUTHORIZED=false
PARTICIPANT_ENROLLMENT_AUTHORIZED=false
PRIVATE_OR_CUSTOMER_DATA_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
CUSTOMER_ADOPTION=false

AGENT_INSTANCE_CREATED=false
RUNTIME_CREATED=false
ENTITY_INSTANCE_CREATED=false
PERMISSION_GRANTED=false
CANONICAL_EVIDENCE_CREATED=false
```

## 8. Execution Prerequisite（执行前置）

本决定、machine Decision、frozen plan 和 output Schema 必须先通过验证、commit 并 push。
远端 commit 未确认前：

```text
PUBLIC_DESK_RESEARCH_EXECUTION_STARTED=false
```
