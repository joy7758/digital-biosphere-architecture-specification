# TITMAS 企业智能体评测 R0 决策与资产映射

状态：`R0_ARCHITECTURE_FREEZE_CANDIDATE`

基线提交：`40a4b34334607ae5fcf428d9794fd07975ddb629`

核验日期：`2026-08-19`

## 1. 产品定义

TITMAS 企业智能体评测是一个面向明确企业场景的智能体评测、推荐和稳定性分析平台规范。它使用版本绑定的企业要求、冻结案例、执行证据和人工裁决，回答：

> 在指定场景、版本、数据和权限边界内，哪一种智能体部署方案更适合企业，哪些风险不可接受，以及结论在什么条件下仍然有效？

它不是通用智能体运行时、供应商排行榜、认证机构、自动授权系统或新的事实数据库。R0 只冻结配置、场景、裁决、展示和控制接口，不实现执行器。

## 2. 最小主链

```text
Enterprise Evaluation Profile (EEP)
  -> Enterprise Scenario Pack (ESP)
  -> existing thin test/adaptation capability
  -> existing evidence, execution audit and version binding
  -> human adjudication + deterministic rules + optional model judge
  -> recommendation index + red-line result + deployment level + evidence level
  -> arena / replay / short video / recommendation card / evidence report
```

旁支控制只允许通过 `ControlProvider` 接口接入。旁路评测事实源不等于运行时控制决定链；供应商原生成绩不等于供应商加 TITMAS 稳定措施后的成绩。

## 3. 现有资产复用审计

状态词只使用：`REUSABLE`、`WRAP_REQUIRED`、`DO_NOT_REUSE`、`METHOD_ONLY`、`DEPRECATED_OR_FROZEN`、`UNKNOWN`。

| 资产 | 核验来源与状态 | 决定 | R0/R1 用途与边界 |
|---|---|---|---|
| DBA 驾驶舱 | 本仓库 `main@40a4b343...`，非运行仓库 | `REUSABLE` | 作为架构、授权、风险和阶段闸门事实源；不执行评测 |
| Agent Evidence | 本地检出 `911db665...` 有未跟踪材料；公开能力说明存在 0.6.0 证据记录与验证边界 | `WRAP_REQUIRED` | 复用证据事件、完整性与收据语义；R1 必须固定规范版本和来源，不把完整证据解释为业务真相 |
| ExecutionAuditSDK | 本地目录有 `FINAL_LOCK.md` 和测试，但未观察到独立 Git 来源身份 | `WRAP_REQUIRED` | 复用不可覆盖证据包、稳定 `execution_id`、哈希链与 replay；进入 R1 前必须建立来源绑定，不创建新审计 SDK |
| Verifiable Agent Demo | 本地 `e5bd3fa...` 且工作树大量未提交；自述为玩具回执验证 | `METHOD_ONLY` | 只借鉴最小可复现回执流程，不把玩具验证升级为企业能力 |
| SAEE | 本地 `697ae208...` 有未提交论文材料；规范清单仅确认 `saee.evaluate_agent_run` 与 `saee.evaluate_evidence` 为 alpha，`production_ready=false` | `WRAP_REQUIRED` | 复用受限评价、证据充分性和长期稳定性分析；评价不授权部署，不声称客户验证 |
| TITMAS Integrations | 本地 `main@6ed4dadd...` 落后于 `origin/main@68a05db2...`；已有 SDK/MCP 与三态语义 | `REUSABLE` | R1 后仅作为现有运输面；R0 不新增 SDK、MCP 或适配器，不把 OpenAPI 观察副本当第二事实源 |
| TITMAS Action Gate | 本地分支 `27ccf953...`；存在确定性 `ALLOW/BLOCK/REQUIRE_APPROVAL`、人类批准和版本绑定 | `WRAP_REQUIRED` | 作为默认 `ControlProvider` 的候选映射；其试验性实现不等于已采纳生产控制平面 |
| DeepSeek Harness | `agent-evidence/integrations/deepseek-harness/` 仅观察到空 `reports/` 目录 | `UNKNOWN` | 不主张存在可复用适配器；R0 不补建、不调用模型 |
| 芜湖 12345 冻结案例方法 | 规范项目包含显式合成案例、冻结期望、历史失败保留和阶段测试清单；当前工作树有未提交材料 | `METHOD_ONLY` | 只复用“案例冻结、分层、负例保留、期望绑定”的方法，不复用工单内容或客户数据 |
| React/Remotion 展示资产 | DBA 站点有 React 页面；`course-video-factory@122b2b41...` 有 Remotion 组件且工作树不干净 | `METHOD_ONLY` | 后续将同一事实对象投影为 16:9、9:16 和推荐卡；R0 不建仪表盘、不复制不明状态产物 |

## 4. 直接复用、薄适配与停止扩张

直接复用：DBA 阶段治理、现有三态/多态结果语义、现有 SDK/MCP 运输边界、冻结案例方法。

仅允许薄适配：EEP/ESP 到现有证据与执行审计对象的映射；SAEE 只读评价输入映射；Action Gate 到 `ControlProvider` 的决定映射；同一评测事实到不同展示视图的映射。

停止扩张：

- 不再建设新的通用 Agent Runtime、证据系统、审计 SDK、评分事实源或授权链；
- 不把单仓库修复、通用工作流、五家供应商排行榜或“大而全后台”设为首期产品；
- 没有真实失败证据前不建设对应稳定功能；
- 不扩展 DeepSeek Harness 空目录来制造“已有能力”；
- 不把研究路线、Demo、CI 通过或本地页面描述为企业采用、商业就绪或生产能力。

## 5. 与既有层的关系

| 层 | 本规范中的职责 | 不拥有 |
|---|---|---|
| DBA | 冻结 EEP、ESP、阶段和权力边界 | 运行与评分计算 |
| DBOS/TITMAS 事实层 | 身份、版本、执行、证据和验证引用 | 演化评价、企业最终决定 |
| SAEE | 可靠性、稳定性、风险和适应性评价输入/建议 | 授权、执行、事实改写 |
| Governance/Human Authority | 接受、拒绝或限制推荐 | 自动把评价改写为事实 |
| 被测方案 | 在冻结场景内产生行为与输出 | 自证通过、自授权限 |

## 6. 当前不受证据支持的主张

- 已完成企业客户验证、真实客服运行或生产部署；
- 已支持大规模并发评测或长期连续稳定运行；
- 评测结果构成认证、绝对安全、科学真理或永久稳定；
- Agent Control、Galileo、Wayfound 或 Benchboard 已被集成；
- AgentFit 代码或七维实现已被 TITMAS 采用；
- 30 个合成案例能证明所有企业场景的低失败率；
- 模型裁判、证据完整或验证通过自动产生执行授权。

## 7. 反膨胀硬规则

1. 每个架构层最多一个主要方法参照。
2. 第一阶段不新增完整外部运行平台。
3. 所有外部组件只能通过可拔插接口连接。
4. 不允许第二套事实数据库。
5. 不允许第二套评分事实源。
6. 不允许第二套行动授权决定链。
7. 引入外部组件必须明确减少一部分自研工作。
8. 只增加功能、不减少总工作量的组件不引入。
9. 没有真实企业失败案例，不开发对应稳定功能。
10. 一个真实场景跑通前，不增加第三套被测路线。
11. 直播和短视频使用同一事实源。
12. 技术后台不得先于评测闭环扩张。

## 8. R0 决定

本文件不授权实现、模型调用、企业数据处理、外部服务接入、部署或发布。只有本目录的两个模式、推荐规范、控制接口、首期配置和唯一 Skill 全部通过静态验证后，才可形成 `R0_PASS_RECOMMEND_R1` 建议；进入 R1 仍需独立 Human Gate。
