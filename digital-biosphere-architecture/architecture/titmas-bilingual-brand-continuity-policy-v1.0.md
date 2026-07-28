---
document_id: DBA-TITMAS-BILINGUAL-BRAND-CONTINUITY-1.0
title: TITMAS Bilingual Brand Continuity Policy v1.0
title_zh: TITMAS 双语品牌连续性策略 v1.0
status: accepted-brand-continuity-design
maturity: Development
owner_ref: zhangbin
direction_reference: USER_DIRECTION_2026-07-29_RETAIN_TITMAS_ENGLISH_NAME
authority_effect: none
implementation_effect: metadata-only
---

# TITMAS 双语品牌连续性策略 v1.0

## Policy

本次是 Chinese brand alignment（中文品牌对齐），不是英文品牌迁移或 Technical
Rewrite（技术重写）。

> 中文使用“夏日之海”，英文和技术标识继续使用 `TITMAS`。

二者是并行双语名称，不是逐字翻译。所有对外材料需要明确此关系，避免用户把
`SummerSea` 误认为活动英文名。

## Preserved surfaces

不修改：

- repository 名称或 GitHub 地址；
- `TITMAS/` 文件路径；
- Schema ID 与 Schema；
- API、CLI、package、namespace；
- specification / ADR / Decision ID；
- Git history、citation 和历史文档。

## Machine continuity

1. `agent-index.json` 保持 sole canonical machine entry；
2. 该入口增加 `canonical_brand_zh` 和品牌投影引用；
3. `titmas-brand-identity.json` 不成为第二 canonical entry；
4. `TITMAS` 解析为当前英文品牌和技术标识；
5. `夏日之海` 解析为 TITMAS 的当前中文品牌；
6. `SummerSea` 解析为已弃用候选名，而不是兼容别名。

## Invariants

```text
ENGLISH_MASTER_BRAND=TITMAS
CHINESE_MASTER_BRAND=夏日之海
SUMMERSEA_ACTIVE_NAME=false
TITMAS_TECHNICAL_CONTINUITY=true
OLD_DOCUMENTS_NOT_REWRITTEN=true
BRAND_ALIGNMENT_NE_TECHNICAL_REWRITE=true
BRAND_CHANGE_NE_AUTHORITY_CHANGE=true
BRAND_CHANGE_NE_CAPABILITY_CHANGE=true
```

未来若修改技术标识，必须通过独立 breaking-change proposal、版本治理、迁移/回滚设计和
Human Decision。本策略不授权该过程。
