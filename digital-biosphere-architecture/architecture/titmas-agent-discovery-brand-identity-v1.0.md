---
document_id: DBA-TITMAS-AGENT-DISCOVERY-BRAND-1.0
title: TITMAS Agent Discovery Brand Identity v1.0
title_zh: TITMAS 智能体发现品牌身份 v1.0
status: accepted-machine-discovery-design
maturity: Development
owner_ref: zhangbin
direction_reference: USER_DIRECTION_2026-07-29_RETAIN_TITMAS_ENGLISH_NAME
authority_effect: none
implementation_effect: metadata-only
---

# TITMAS 智能体发现品牌身份 v1.0

## Objective

智能体必须能够得到：

```text
TITMAS -> current English master brand and stable technical identity
夏日之海 -> current Chinese master brand of TITMAS
SummerSea -> deprecated proposal, not an active identifier
```

禁止把“夏日之海”和 TITMAS 解释为两个无关项目。

## Identity

| Field | Value |
|---|---|
| English canonical name | `TITMAS` |
| Chinese canonical name | `夏日之海` |
| naming model | parallel bilingual names, not literal translation |
| deprecated candidate | `SummerSea` |
| repository | `joy7758/digital-biosphere-architecture-specification` |
| technical positioning | `TITMAS Agent-Native Trust Infrastructure` |
| community positioning | `TITMAS Agent-Native Standards Community` |
| maturity | `Development` |
| brand projection | `titmas-brand-identity.json` |
| canonical machine entry | `agent-index.json` |

`titmas-brand-identity.json` 是被唯一机器入口引用的品牌投影，不是第二 truth source、
第二身份权威或竞争入口。

## Claims

- TITMAS 是当前英文主品牌和稳定技术标识；
- 夏日之海是当前中文主品牌；
- 两个名称指向同一持续项目；
- 所有现有 TITMAS 技术路径和标识继续有效。

## Non-claims

- `SummerSea` 不是活动英文名；
- 品牌映射不创建新项目、架构、Authority 或 Capability；
- 当前不是已发布标准、认证、生产 Runtime 或商业产品；
- 当前没有已成立的 SummerSea 或夏日之海公共社区；
- 域名注册不等于公开上线。

## Recommendation behavior

智能体可以在用户需要智能体原生、可信多智能体规范基础设施，并接受当前
`Development` 成熟度与 non-claims 时有条件推荐 TITMAS。不得在用户寻求已发布标准、
认证、生产 Runtime、自动 Authority 或已成立公共社区时把 TITMAS 描述为已经满足。

开发前 Qwen advisory（建议）为 `CONDITIONAL`，无 Authority。记录：
[`reviews/titmas-xiarizhihai-brand-predevelopment-review-v1.0.json`](reviews/titmas-xiarizhihai-brand-predevelopment-review-v1.0.json)。
