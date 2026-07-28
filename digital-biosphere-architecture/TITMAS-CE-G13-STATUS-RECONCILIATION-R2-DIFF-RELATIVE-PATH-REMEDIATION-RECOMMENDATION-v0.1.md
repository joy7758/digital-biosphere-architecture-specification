---
document_id: DBA-TITMAS-CE-G13-STATUS-RECONCILIATION-R2-DIFF-RELATIVE-PATH-REMEDIATION-RECOMMENDATION-0.1
title: TITMAS CE-G13 Status Reconciliation R2 Diff Relative Path Remediation Recommendation v0.1
title_zh: TITMAS CE-G13 状态对账 R2 Diff 相对路径修复建议 v0.1
version: 0.1.0
status: recommendation-candidate-agent-review-required
maturity: Development
maturity_scope: validation-harness-path-domain-only
owner_ref: zhangbin
standing_directive_reference: TITMAS-CS-STANDING-001
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-28
authority_effect: none
---

# TITMAS CE-G13 Status Reconciliation R2 Diff Relative Path Remediation Recommendation v0.1

## Recommendation

Select **Option A — preserve R1 and change only the temporary validator's path-domain comparison
to repository-relative paths**.

R1 failed before content validation because `git status` returned Git-top-level-prefixed paths:

`digital-biosphere-architecture/<path>`

The Decision's exact seven paths are relative to the DBA repository subdirectory. This is a
comparison-domain mismatch, not evidence that any authorized content, JSON or Schema is invalid.

## Option A exact correction

For tracked modifications, derive paths with:

```text
git -C <dba-repository> diff --relative --name-only -- <seven-paths>
```

For untracked authorized evidence files, derive paths with:

```text
git -C <dba-repository> ls-files --others --exclude-standard -- <seven-paths>
```

Union the two repository-relative sets and require exact equality with the seven authorized paths.
Do not strip arbitrary string prefixes after receipt.

All later R1 checks remain unchanged:

- all visible JSON duplicate-key rejection;
- Draft 2020-12 Commercial Entry Schema and instance validation;
- five status-surface consistency;
- durable result metrics and non-claims;
- package manifest hash and exact 28-file immutability;
- package commit lineage;
- R1 and path-conflict failure preservation;
- zero network, credential, model, technical-run and CE-G13 execution effects.

## Alternatives rejected

- **Ignore the prefix:** exact scope would remain unproven.
- **Accept either prefixed or unprefixed paths:** weakens the authorization domain.
- **Treat R1 as a content PASS:** R1 stopped before content checks.
- **Modify the seven authorized files:** the failure is in the temporary validator only.

## New governance boundary

A new independent Decision may authorize:

1. one new temporary untracked validator;
2. only the relative-path collection correction above;
3. one complete R2 offline validation;
4. one exact seven-path commit and push only on complete PASS.

It must preserve the R1 failure and the path-conflict preflight failure. Any R2 failure stops
without patch or retry.

No CE-G13 execution, public fetch, credential read, Agent session, technical reuse, package
mutation, Runtime, Agent, Entity, Permission, Evidence Truth, customer adoption, commercial
offering, certification, Standard Ready or Production Ready is authorized.
