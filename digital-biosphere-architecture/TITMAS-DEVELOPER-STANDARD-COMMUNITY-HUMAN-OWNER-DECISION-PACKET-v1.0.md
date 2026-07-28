# TITMAS Developer Standard Community Human Owner Decision Packet v1.0

中文：TITMAS 开发者标准社区 Human Owner（人类所有者）决定包 v1.0。

状态：`AWAITING_HUMAN_DECISIONS`

本决定包不推荐或自动选择选项。每项只能由 Human Owner 记录
`ACCEPT`、`REJECT` 或 `DEFER`；未记录时一律视为 `DEFER`。

## D1 — 有限私有贡献者试点

- **Options**：`ACCEPT | REJECT | DEFER`
- **Direct impact**：决定是否允许在非公开范围验证 Quickstart、模板和贡献流程。
- **Risk**：隐私、测试材料来源、责任边界和参与者误解。
- **Does not authorize**：公共社区、公开公告、客户数据、商业试点、合并或 Release。
- **Revocation**：可因越权、数据风险、保密失败或审查能力不足立即撤销。
- **Expiry candidate**：决定生效后 60 天。

## D2 — 公共贡献表面

- **Options**：`ACCEPT | REJECT | DEFER`
- **Direct impact**：决定是否允许公众创建规范、集成和缺陷类 Issue/PR。
- **Risk**：没有 Maintainer/Reviewer 时积压；安全问题被公开披露；恶意内容。
- **Does not authorize**：自动接受、自动合并、规范发布、认证、SLA 或 Authority。
- **Revocation**：可关闭模板或改回只读；已存在记录必须保留。
- **Expiry candidate**：决定生效后 90 天复核。

## D3 — 公开社区公告

- **Options**：`ACCEPT | REJECT | DEFER`
- **Direct impact**：决定是否可以对外声明“公共贡献入口已开放”。
- **Risk**：把 Launch-ready candidate 误解为成立、采用、Stable 或产品发布。
- **Does not authorize**：外部邀请名单、商业报价、Foundation、认证或采用声明。
- **Revocation**：发现错误声明或入口不可用时撤回公告并保留更正记录。
- **Expiry candidate**：决定后 30 天内未执行则自动失效。

## D4 — 临时 Maintainer

- **Options**：`ACCEPT | REJECT | DEFER`
- **Direct impact**：指定有期限、范围受限的贡献排队与审查协调责任。
- **Risk**：Owner、Reviewer、Maintainer 与 Architecture Authority 被混淆。
- **Does not authorize**：单人批准自己的规范、安全敏感更改、Release 或 Authority 变化。
- **Revocation**：利益冲突、审查失效、越权或 Human Owner 撤销。
- **Expiry candidate**：任命后 90 天。

## D5 — 首批真实外部 Issue

- **Options**：`ACCEPT | REJECT | DEFER`
- **Direct impact**：决定是否接受真实陌生开发者使用模板创建的首批 Issue。
- **Risk**：PII、secret、漏洞细节、虚假采用声明和无人响应。
- **Does not authorize**：自动创建 Issue、自动回复、自动接受需求、客户记录或产品承诺。
- **Revocation**：模板滥用、安全接收能力不足或响应责任不可持续。
- **Expiry candidate**：决定后 45 天内完成一次复核。

## D6 — 第一位独立 Reviewer

- **Options**：`ACCEPT | REJECT | DEFER`
- **Direct impact**：允许为特定批次指定一位独立 Reviewer，减少作者自审。
- **Risk**：Reviewer 被误写为 Authority、Maintainer、认证者或永久角色。
- **Does not authorize**：批准标准、改变 Gate、签发编号、合并或发布。
- **Revocation**：范围外审查、利益冲突、不可复核结论或 Human Owner 撤销。
- **Expiry candidate**：按批次，到该批次结案或 30 天中较早者。

## D7 — 社区版本标签和 Release

- **Options**：`ACCEPT | REJECT | DEFER`
- **Direct impact**：决定是否允许创建明确标注预览成熟度的 Git tag 和 GitHub Release。
- **Risk**：被误解为 Stable 规范、社区成立、正式采用、认证或商业就绪。
- **Does not authorize**：发布 Stable 标准、包仓库发布、部署、商业报价、认证或公告。
- **Revocation**：Release 可标记撤回或 superseded，但不得删除历史证据。
- **Expiry candidate**：决定后 14 天未执行则自动失效。

## Decision recording form

```text
decided_by_ref=
decided_at=

D1_PRIVATE_CONTRIBUTOR_PILOT=ACCEPT|REJECT|DEFER
D2_PUBLIC_CONTRIBUTION_SURFACE=ACCEPT|REJECT|DEFER
D3_PUBLIC_COMMUNITY_ANNOUNCEMENT=ACCEPT|REJECT|DEFER
D4_INTERIM_MAINTAINER=ACCEPT|REJECT|DEFER
D5_FIRST_REAL_EXTERNAL_ISSUES=ACCEPT|REJECT|DEFER
D6_FIRST_INDEPENDENT_REVIEWER=ACCEPT|REJECT|DEFER
D7_COMMUNITY_TAG_AND_RELEASE=ACCEPT|REJECT|DEFER
```

未填写、条件不完整或相互冲突的决定不产生授权。
