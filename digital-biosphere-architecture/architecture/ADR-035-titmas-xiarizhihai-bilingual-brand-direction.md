---
adr_id: ADR-035
title: Adopt TITMAS and Xiarizhihai as Parallel Bilingual Brand Names
title_zh: 采纳 TITMAS 与夏日之海并行双语品牌方向
status: accepted-for-brand-identity-design
maturity: Development
decided_by_ref: zhangbin
decided_at: 2026-07-29
decision_reference: USER_DIRECTION_2026-07-29_RETAIN_TITMAS_ENGLISH_NAME
implementation_authorized: false
external_action_authorized: false
authority_effect: none
---

# ADR-035: 采纳 TITMAS 与夏日之海并行双语品牌方向

## Context

初始品牌设计提案拟使用“夏日之海 / SummerSea”。Human Owner 在设计尚未提交或推送时
明确放弃该英文名，并要求英文继续使用 `TITMAS`。

现有仓库、目录、Schema、API、CLI、package、规范 ID、Git history 和外部技术引用已广泛
使用 TITMAS。保持英文技术身份可以避免无价值的兼容迁移。

## Decision

采纳：

```text
CHINESE_MASTER_BRAND=夏日之海
ENGLISH_MASTER_BRAND=TITMAS
NAMING_MODEL=PARALLEL_BILINGUAL_NAMES_NOT_LITERAL_TRANSLATION
```

“夏日之海”和 `TITMAS` 指向同一持续项目。中文名负责中文品牌表达，英文名同时保持
品牌与稳定技术标识作用。

## Consequences

- 人类入口增加双语映射；
- `agent-index.json` 保持唯一机器入口并增加双语品牌元数据；
- `titmas-brand-identity.json` 只作为该入口引用的品牌投影；
- 现有 TITMAS 技术标识和历史记录全部保留；
- 不需要英文别名迁移、redirect 或 package rename；
- 中文名与英文名不是逐字翻译，入口材料必须明确说明。

## Non-authorizations

```text
NEW_PROJECT_CREATED=false
ARCHITECTURE_CHANGED=false
OWNERSHIP_CHANGED=false
AUTHORITY_CHANGED=false
CAPABILITY_CHANGED=false
SCHEMA_CHANGED=false
API_CHANGED=false
REPOSITORY_RENAMED=false
DNS_CHANGED=false
PUBLIC_LAUNCH_AUTHORIZED=false
COMMUNITY_ESTABLISHED=false
STANDARD_RELEASED=false
RELEASE_AUTHORIZED=false
COMMERCIAL_READY=false
```
