---
document_id: DBA-TITMAS-SELF-GOVERNANCE-EXPERIMENT-PROTOCOL-0.1
title: TITMAS Self-Governance Experiment Protocol v0.1
title_zh: TITMAS 自我治理实验协议 v0.1
status: PROTOCOL_ONLY
maturity: Development
maturity_scope: entire-document
primary_repository: digital-biosphere-architecture
document_type: NON_AUTOMATED_MANUAL_EXPERIMENT_PROTOCOL
designed_at: 2026-07-28
source_design: TITMAS_SELF_GOVERNANCE_EXPERIMENT_DESIGN_v0.1.md
source_design_sha256: 394876046ce663390ec7956d6a4aff1daeba868fa79730e20adc3f2303cfed3d
experiment_execution_authorized: false
implementation_authorized: false
code_effect: false
schema_effect: false
api_effect: false
dashboard_effect: false
adapter_effect: false
repository_effect: false
external_action_effect: false
---

# TITMAS Self-Governance Experiment Protocol v0.1

中文：TITMAS 自我治理实验协议 v0.1。

## 0. Protocol boundary（协议边界）

本协议把
[`TITMAS Self-Governance Experiment Design v0.1`](TITMAS_SELF_GOVERNANCE_EXPERIMENT_DESIGN_v0.1.md)
转化为可由人逐步执行、但不自动化的实验流程。

实验只回答：

> TITMAS 是否能降低一个人管理多个仓库、程序、Agent、工具和外部服务的实际成本？

本协议不创建：

- 控制中心；
- 自动调度系统；
- Agent 选择器；
- 外部服务替代品；
- Code、Dashboard、API、Adapter 或 Repository；
- 新的 Architecture Layer、Component、Schema、Runtime 或 Truth source。

```text
PROTOCOL_IS_MANUAL=true
PROTOCOL_IS_EXECUTABLE_AS_HUMAN_PROCEDURE=true
EXPERIMENT_EXECUTION_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
```

“可执行”只表示人可以按步骤操作，不表示当前已经获得执行实验、访问外部账号、调用
Agent、保存 Evidence 或改变任何系统状态的授权。

### 0.1 Inherited experiment boundaries（继承边界）

本协议继承设计文档的：

- single-operator matched comparison；
- 固定 cohort；
- 原生外部工具 Baseline；
- reference-only TITMAS condition；
- Human Attention Amplification；
- full intervention-cost accounting；
- delayed scoped risk adjudication；
- 小样本只支持 local signal；
- 成功不等于 Implementation、Product、Production 或 Customer proof。

若本协议与设计文档冲突，以设计文档为准，并停止受影响 session。

## 1. Roles and separation（角色与分离）

### 1.1 Experiment Owner（实验负责人）

Experiment Owner 必须是明确的人类责任方。

负责：

- 接受或退回 protocol；
- 冻结 cohort、task、timebox、review horizon 和 condition order；
- 确认 source access 与敏感信息边界；
- 指定 Operator 和 Reviewer；
- 决定是否授权一次有界实验；
- 处理 stop、exclusion、protocol deviation 和 unresolved disagreement；
- 确认结果只按 local signal 表述。

不得：

- 为满足成功阈值而改写 session 记录；
- 把 Attention candidate 当作命令；
- 代替外部服务修改其状态；
- 从 protocol 自动授权 Implementation；
- 删除不利、失败或 `INCONCLUSIVE` 结果。

### 1.2 Operator（操作者）

同一个 Human Operator 必须执行全部有效 Baseline 与 TITMAS sessions。

负责：

- 使用已冻结的 task wording；
- 按相同时间粒度记录活动；
- 在 canonical source 中核验风险；
- 记录 source hops、context switches、unknown、stale 和 conflict；
- 形成 Human Decision input；
- 在 TITMAS condition 中保留 override 和 rejected candidates；
- 立即报告 stop condition。

不得：

- 在 Baseline 中使用 TITMAS attention packet；
- 在 TITMAS condition 中把 packet 当作 Truth；
- 根据预期结果改变记录分类；
- 执行未授权的 repository、deployment、database、domain 或 task 变更；
- 在全部 sessions 完成前查看 delayed adjudication 结果。

### 1.3 Reviewer（复核者）

Reviewer 负责 delayed scoped risk adjudication 和 protocol compliance review。

原则上 Reviewer 应与 Operator 分离，并在 adjudication 完成前看不到 condition 标签和
汇总结果。

负责：

- 核对 cohort、source window、task 和 exclusion；
- 按预先冻结的 actionability criteria 复核 source；
- 建立 scoped reference risk set；
- 标记 false positive、false negative、disagreement 和 unknown；
- 核对计算，不替代 Experiment Owner 作采用决定。

不得：

- 把 Evidence 称为绝对 Truth；
- 根据 Condition M/T 改变风险门槛；
- 修改原始 session Evidence；
- 批准外部动作或 Implementation；
- 自动关闭 disagreement。

### 1.4 Role overlap rule（角色重叠）

为验证“一人管理”场景，Experiment Owner 可以兼任 Operator，但必须披露。

Reviewer 应优先独立。确实无法提供独立 Reviewer 时：

1. adjudication 必须延迟到全部 sessions 冻结后；
2. condition、session order 和计算结果必须在复核材料中遮蔽；
3. actionability criteria 必须在首个有效 session 前冻结；
4. 角色重叠必须写入 limitation；
5. 结果不得升级为 independent validation。

### 1.5 Attention preparation activity（Attention 准备活动）

Attention preparation 是 Condition T 中的一项活动，不是新角色或组件。

它可以由 Operator 手工完成，也可以由已有、单独允许使用的 Agent 提供咨询草稿，但：

- 所有人工准备、prompt/context preparation、核验、刷新和纠错时间计入；
- Agent elapsed time 单独记录；
- Agent output 不形成 Authority、Decision、Truth 或执行；
- 不允许后台自动抓取、同步或写回；
- 使用 Agent 需要在 cohort freeze 时声明。

## 2. Cohort freeze procedure（Cohort 冻结流程）

未完成 cohort freeze，不得开始 Calibration 或有效 session。

### 2.1 Freeze inputs（冻结输入）

Experiment Owner 与 Operator 共同完成以下人工清单：

| 冻结项 | 必须记录 |
|---|---|
| Protocol | 本协议版本与 hash |
| Source design | 设计文档版本与 hash |
| Run identity | 唯一人工实验 run 标识 |
| Operator | 姓名或受控标识 |
| Reviewer | 姓名或受控标识；是否独立 |
| Repository cohort | 纳入的真实 repositories |
| Programs / Agents | 纳入对象及其边界 |
| External services | 实际使用与不适用的服务 |
| Canonical source map | 每个对象应返回的 source |
| Observation windows | 每个 matched session 的时间窗口 |
| Review horizon | “actionable”适用的固定时间范围 |
| Session timebox | 每个 session 的统一上限 |
| Pairing rationale | 为什么两侧任务可比 |
| Condition order | M/T 顺序，首个有效 session 前冻结 |
| Sensitive-data boundary | 禁止记录的数据 |
| Evidence location | 已有、获准使用的保存位置 |
| Retention rule | 保留期限与访问者 |
| Stop authority | 谁可以立即停止实验 |

本表是人工检查清单，不是 Schema。

### 2.2 Repository and service minimum（最小范围）

沿用设计文档：

- 不少于五个真实 repository；
- 至少一个 Agent-assisted development workflow；
- 至少四类实际使用的外部服务；
- 至少一个 deployment、data/backend、planning 或 domain/security surface。

必须检查：

- GitHub；
- Codex；
- Render；
- Supabase；
- Context7；
- Linear；
- Cloudflare。

未真实使用的服务标记 `NOT_IN_SCOPE_FOR_COHORT`。不得模拟状态补足服务数量。

### 2.3 Canonical source freeze（事实来源冻结）

每个纳入对象至少记录：

- canonical source 名称；
- source owner；
- source reference；
- access boundary；
- expected freshness；
- unavailable/partial behavior；
- 是否包含敏感信息。

TITMAS 只保存最小引用，不能把这些来源复制为第二事实源。

### 2.4 Pair and order freeze（配对与顺序冻结）

在查看具体风险前，冻结：

- 至少五个 Management matched pairs；
- 至少两个 Onboarding projects per condition；
- Calibration sessions；
- 每个 pair 的 M/T 顺序；
- 每个 pair 的 complexity comparability notes；
- 允许的替换 pair；
- exclusion rule。

建议顺序：

| Pair | First condition | Second condition |
|---|---|---|
| Calibration | M | T |
| 1 | M | T |
| 2 | T | M |
| 3 | M | T |
| 4 | T | M |
| 5 | 在查看 source window 前预先记录 | 另一 condition |

同一具体 snapshot 或已知风险不得先后用于两个 conditions。

### 2.5 Freeze record（冻结确认）

Experiment Owner 逐项确认：

```text
COHORT_DEFINED=true
CANONICAL_SOURCES_RECORDED=true
PAIR_ORDER_RECORDED=true
SENSITIVE_DATA_BOUNDARY_RECORDED=true
EVIDENCE_LOCATION_AUTHORIZED=true
EXPERIMENT_EXECUTION_AUTHORIZED_SEPARATELY=true|false
```

最后一项只有 Human Decision 可以设为 `true`。本协议本身不设置。

### 2.6 Amendment after freeze（冻结后修订）

冻结后发现 cohort、source、task 或 order 需要变化时：

1. 停止尚未开始的受影响 session；
2. 记录原因；
3. 创建新的人工 freeze version；
4. 标记受影响的已完成 sessions；
5. 在不查看汇总结果的前提下决定保留、排除或重跑；
6. 不覆盖旧 freeze record。

不能为了改善结果事后改变 review horizon、actionability 或 exclusion。

## 3. Common session preparation（通用 Session 准备）

### 3.1 Preflight（开始前检查）

Operator 在每个 session 前人工确认：

- run、session、pair 和 condition 正确；
- source window 未在另一 condition 中使用；
- task wording 未变化；
- timebox 正确；
- canonical sources 可访问；
- 当前无 credential、privacy 或 service incident 风险；
- Operator 未提前看到该窗口的 adjudication；
- 记录计时工具已准备；
- Condition M 不存在 attention packet；
- Condition T 的 packet 准备方式已记录。

### 3.2 Time categories（时间分类）

所有人工活动按以下四类记录：

| 类别 | 定义 | 示例 |
|---|---|---|
| `DIRECT` | 直接核验风险、评价适用性、形成 decision input | 阅读 source 内容、判断风险、写决策问题 |
| `OVERHEAD` | 为恢复和协调管理上下文产生的额外活动 | 找 source、跨工具导航、恢复上下文、重复对账、准备/刷新/纠正 attention packet |
| `WAIT` | 人没有进行当前任务工作的等待 | 外部服务响应、Agent 生成、网络不可用 |
| `MEASUREMENT` | 仅因实验记录产生的活动 | 填 session log、标注时间类别、整理计数 |

无法判断时先记为 `UNCLASSIFIED`，session 后由 Operator 在不知道汇总结果的前提下说明并
归类。不得默认归入 `DIRECT`。

### 3.3 Manual time resolution（人工计时精度）

- 连续活动按最接近的一分钟记录；
- 不足一分钟的同类短活动可以在 session 内合并；
- 不要求秒级记录；
- `MEASUREMENT` 必须单列，防止记录负担污染管理时间；
- 原始开始/结束时刻仍应保留。

### 3.4 Common task wording（统一任务文本）

Management session：

> 在规定时间内，找出固定 cohort 中最多三个最值得人立即关注的 actionable risks，
> 返回其 canonical source，说明 freshness、scope、uncertainty 和所需 Human Decision，
> 并列出未能确认的事项。

Onboarding session：

> 把一个此前不在 cohort 中的真实项目纳入现有人工管理范围；找到 owner、canonical
> source、current status、risk source、external-service dependencies 和下一次复核入口。

## 4. Baseline Session procedure（Baseline Session 操作流程）

Condition M 使用操作者当前正常工作方式和外部服务原生界面。

### 4.1 Start（开始）

1. 填写 session identity 和 preflight；
2. 记录实际开始时刻；
3. 启动统一 timebox；
4. 打开 Operator 平时使用的第一个 native source；
5. 不查看任何 TITMAS attention packet、排序或事后风险列表。

### 4.2 Native-source review（原生来源检查）

Operator 按正常习惯：

1. 查看 GitHub、Linear、Render、Supabase、Cloudflare 或其他已冻结 source；
2. 使用 Codex 或 Context7 时，只按 Baseline 中预先允许的正常用法；
3. 每次跨 canonical source 记录 source hop；
4. 每次改变管理对象或判断任务记录 context switch；
5. 找 source、恢复上下文和重复对账计入 `OVERHEAD`；
6. 直接核验、判断和形成 decision input 计入 `DIRECT`。

不得为了使 Baseline 更慢而增加无必要步骤，也不得禁用 Operator 原本已经稳定使用的工具。

### 4.3 Risk capture（风险记录）

每发现一个候选风险：

1. 记录首次注意时刻；
2. 返回 canonical source；
3. 记录 source-confirmed 时刻；
4. 记录 observed time、freshness、scope 和 uncertainty；
5. 判断是否需要 Human Decision、review 或有界 action；
6. 未确认时标为 unknown，不得补成风险或成功。

Baseline 最终最多选择三个 actionable risks，同时保留未选择的已发现候选数量。

### 4.4 End（结束）

满足以下任一条件时结束：

- 任务完成；
- timebox 到达；
- stop condition 触发；
- source 不足，无法继续形成 source-bound result。

结束时：

1. 记录结束时刻；
2. 完成 session record；
3. 分开汇总 `DIRECT`、`OVERHEAD`、`WAIT`、`MEASUREMENT`；
4. 记录 source hops 和 context switches；
5. 冻结 top risks、unknowns、conflicts 和 decision inputs；
6. 不进行 delayed adjudication；
7. 保存 Evidence 并只追加更正。

## 5. TITMAS Condition Session procedure（TITMAS 条件操作流程）

Condition T 使用相同 native sources，加一个人工、reference-only attention packet。

### 5.1 Total-cost timer（总成本计时）

Condition T 的计时从准备 attention packet 开始，不从 Operator 阅读完成后的 packet 开始。

必须计入：

- source locating；
- packet preparation；
- Agent prompt/context preparation，若适用；
- human verification；
- refresh；
- stale/conflict reconciliation；
- correction；
- Operator review；
- canonical-source confirmation；
- override；
- decision-input preparation。

Agent 或外部服务的纯等待记为 `WAIT`，相应人工准备和复核记入 `OVERHEAD` 或 `DIRECT`。

### 5.2 Manual attention preparation（人工 Attention 准备）

准备者只使用已冻结、可访问的 canonical sources。

步骤：

1. 列出当前可观察的候选事项；
2. 为每项加入 source reference；
3. 记录 observed time、freshness、scope、uncertainty；
4. 说明 why now；
5. 标出需要 Human review 的原因；
6. 选择最多三个优先呈现 candidates；
7. 保留完整候选列表和未进入前三的理由；
8. 记录全部准备与纠错时间；
9. 不执行任何 source writeback。

没有 source 的候选只能标为 `UNVERIFIED_CANDIDATE`，不能进入 source-confirmed top risks。

### 5.3 Operator attention review（操作者复核）

Operator 收到或完成 packet 后：

1. 先记录 packet review 开始时刻；
2. 检查 source、observed time、freshness、scope 和 uncertainty；
3. 对每个 top candidate 返回 canonical source；
4. 独立判断是否 actionable；
5. 记录 accept、reject、defer 或 override；
6. 若排序错误，记录 override reason；
7. 查看完整候选列表，防止前三项隐藏其余风险；
8. 形成最多三个 source-confirmed actionable risks；
9. 形成 Human Decision input；
10. 不授权、不执行、不调度 Agent。

### 5.4 Human Attention Amplification boundary（人类注意力放大边界）

Condition T 只回答：

> 现在什么值得人优先核验？

它不决定：

- 哪个 Agent 参与；
- 哪个 Agent 被调度；
- 谁获得 Permission；
- 哪个动作自动执行；
- 哪个外部服务状态应改变；
- 哪个 Evidence 成为 Truth。

```text
ATTENTION_IS_HUMAN_ATTENTION_AMPLIFICATION=true
ATTENTION_IS_CONTROL_CENTER=false
ATTENTION_IS_AUTOMATIC_SCHEDULER=false
ATTENTION_IS_AGENT_SELECTOR=false
ATTENTION_IS_PERMISSION_SYSTEM=false
ATTENTION_REPLACES_EXTERNAL_SERVICE=false
```

### 5.5 End（结束）

结束条件与 Baseline 相同。

结束时额外记录：

- packet preparation minutes；
- packet refresh/correction minutes；
- Agent/service wait，若适用；
- attention candidates 总数；
- top candidates；
- accept/reject/defer/override；
- source-less candidates；
- stale/conflicted candidates；
- packet maintenance issues。

## 6. Manual Session Record Template（Session 记录模板）

以下模板是人工记录格式，不是 Schema、API payload 或 database model。

### 6.1 Session identity（身份）

| 项目 | 人工填写 |
|---|---|
| Run ID | |
| Protocol version/hash | |
| Source design version/hash | |
| Session ID | |
| Pair ID | |
| Condition | `M` / `T` |
| Session type | Calibration / Management / Onboarding |
| Operator | |
| Owner | |
| Reviewer masked ID | |
| Cohort freeze version | |
| Source window | |
| Review horizon | |
| Planned order | |
| Actual order | |
| Timebox | |
| Prior familiarity | New / Some / High |

### 6.2 Preflight and timing（开始信息）

| 项目 | 人工填写 |
|---|---|
| Preflight complete | Yes / No |
| Start time | |
| End time | |
| Task completed | Yes / Partial / No |
| Stop condition | None / reference |
| Protocol deviation | None / reference |
| External outage | None / description |

### 6.3 Activity totals（活动时间）

| 类别 | Minutes | Notes |
|---|---:|---|
| `DIRECT` | | |
| `OVERHEAD` | | |
| `WAIT` | | |
| `MEASUREMENT` | | |
| `UNCLASSIFIED` before closure | | |
| Wall-clock elapsed | | |
| Active management (`DIRECT + OVERHEAD`) | | |

Condition T 追加：

| 介入活动 | Minutes | Notes |
|---|---:|---|
| Packet preparation | | |
| Prompt/context preparation, if allowed | | |
| Packet verification | | |
| Refresh/reconciliation | | |
| Correction | | |
| Operator override handling | | |
| Agent/service wait | | |

这些时间必须同时归入前述四类，不能从总时间中消失。

### 6.4 Navigation and cognition（导航与认知）

| 项目 | 人工填写 |
|---|---|
| Source hops | |
| Context switches | |
| Canonical sources opened | |
| Repeated source visits | |
| Unknown sources | |
| Stale sources | |
| Conflicted sources | |
| Unavailable sources | |

### 6.5 Session output（结果）

| 项目 | 人工填写 |
|---|---|
| Top risk 1 reference | |
| Top risk 2 reference | |
| Top risk 3 reference | |
| Other candidates count | |
| Source-confirmed discovery times | |
| Required Human Decisions | |
| Unresolved questions | |
| Operator confidence and limitations | |
| Evidence save reference | |
| Correction/superseding reference | |

## 7. Attention Candidate Record Template（Attention Candidate 记录模板）

每个 Condition T candidate 单独记录。该模板不定义 Agent、Permission 或 execution fields。

| 项目 | 人工填写 |
|---|---|
| Run ID / Session ID | |
| Candidate ID | |
| Display rank | |
| Candidate summary | |
| Why now | |
| Canonical source | |
| Source owner | |
| First observable time, if available | |
| Observed at | |
| Freshness | Current / Stale / Unknown |
| Scope | |
| Uncertainty | |
| Known limitations | |
| Potential impact | |
| Required human review | |
| Preparation minutes | |
| Verification minutes | |
| Presented in top three | Yes / No |
| Operator disposition | Accept / Reject / Defer / Override |
| Disposition reason | |
| Source-confirmed | Yes / No / Partial |
| Actionable within review horizon | Pending adjudication |
| External action executed | Must remain No |
| Permission assigned | Must remain No |

禁止使用以下字段或等价语义：

- selected Agent；
- automatic route；
- execution command；
- granted permission；
- approved by attention；
- truth score。

## 8. Risk adjudication procedure（风险裁定流程）

### 8.1 Entry conditions（进入条件）

只有在以下条件满足后开始：

- 所有计划 sessions 已完成、停止或排除；
- 原始 logs 和 outputs 已冻结；
- Condition T packet cost 已记录；
- actionability criteria 已冻结；
- Reviewer 已收到 condition-masked materials；
- 汇总成功指标尚未计算或未向 Reviewer展示。

### 8.2 Actionability criteria（可行动标准）

风险进入 scoped reference risk set，必须同时满足：

1. 有 canonical source 或明确的 source-access limitation；
2. 在冻结的 observation window 内可观察；
3. 在冻结的 review horizon 内需要 Human Decision、review 或 bounded action；
4. 不是已由 canonical source 关闭的 stale item；
5. scope 与 cohort 相关；
6. uncertainty 和 disagreement 被保留。

该集合是实验裁定集合，不是绝对 Truth。

### 8.3 Masking（条件遮蔽）

Reviewer 优先只看到：

- source window；
- source references；
- risk statements；
- timestamps；
- actionability criteria；
- limitations。

在初次 adjudication 冻结前，不显示：

- Condition M/T；
- attention rank；
- Operator disposition；
- session efficiency；
- success threshold result。

若技术或材料结构无法完全遮蔽，Reviewer 必须记录 unblinding risk。

### 8.4 Exhaustive source review（有界完整复核）

Reviewer 对每个 observation window：

1. 检查全部已冻结 canonical sources；
2. 列出符合 actionability criteria 的 risks；
3. 记录 source 和 first observable time；
4. 标记影响级别，但不由分数自动决定；
5. 保留 unknown、stale、conflict 和 unavailable；
6. 冻结 scoped reference risk set；
7. 再解除 condition masking；
8. 判断每个 session 的 discovered、missed 和 unsupported items。

### 8.5 False positive / false negative assignment

False positive：

- Condition T 呈现的 candidate；
- 在固定 scope/horizon 内缺少来源、不需要 human review/action，或已关闭但因 stale 状态被提升。

False negative：

- scoped reference risk set 中的 actionable risk；
- 在 Condition T timebox 内既未被 Attention 呈现，也未被 Operator 发现。

Baseline 的人工风险列表使用同一 actionability criteria，供 FPR/FNR 对照。

### 8.6 Disagreement（分歧）

Operator、Reviewer 或 Owner 对 actionability、severity 或 source interpretation 有分歧时：

- 不覆盖原判断；
- 分别记录理由和 source；
- 标记 `DISAGREEMENT_UNRESOLVED` 或记录有范围 disposition；
- 必要时将相关 metric 标为 `NOT_CALCULABLE`；
- 不用多数投票产生 Truth。

## 9. Evidence preservation rules（Evidence 保存规则）

### 9.1 Authorized location only（仅使用已授权位置）

实验 Evidence 只能保存到 cohort freeze 中已指定的现有位置。

本协议不授权：

- 新建 Repository；
- 新建 database；
- 新建 Dashboard；
- 新建 API、Adapter、collector 或同步服务；
- 把外部服务数据复制成新的 canonical ledger。

### 9.2 Minimum evidence set（最小证据集）

必须保留：

- protocol、source design 和 cohort freeze references；
- role assignment 与 role overlap；
- condition order；
- 每个 session 原始 record；
- time-segment record；
- attention candidates；
- source references；
- top risks and decision inputs；
- stop、exclusion 和 deviation；
- delayed adjudication；
- calculation sheet or manual calculation record；
- final limitations and result；
- advisory Agent review reference，若使用。

### 9.3 Preservation discipline（保存纪律）

- 原记录冻结后不覆盖；
- 更正使用新的 superseding note，并引用旧记录；
- 失败、排除、unknown 和 disagreement 必须保留；
- 适用时记录文件 hash；
- 外部 source 只保存最小引用和观察时间；
- private source 不因实验变为 public；
- Evidence 不因 hash、Reviewer 或数量变成 Truth；
- 不删除“不支持 TITMAS”的结果。

### 9.4 Sensitive information（敏感信息）

不得保存：

- API key、token、password、cookie；
- Supabase private data 或 auth records；
- Cloudflare secret 或受限 DNS/security 配置；
- customer data；
- 不必要的 PII；
- 私有 repository 内容的公开复制；
- Agent prompt 中不应传播的 secret。

若敏感信息进入记录，立即停止，按 Owner 已冻结的安全流程处理。

### 9.5 Access and retention（访问与保留）

实验开始前必须决定：

- 谁可读；
- 谁可更正；
- 保留多久；
- 哪些 reference 可能失效；
- 如何记录删除或访问限制；
- 哪些结果可以公开。

本协议不提供默认公开授权。

## 10. Exclusion and stop rules（排除与停止规则）

### 10.1 Immediate stop（立即停止）

出现以下情况立即停止 session：

- credential、secret、PII 或受限数据可能暴露；
- TITMAS condition 尝试写回或执行外部动作；
- Attention 被用作 Permission、Authority、Agent selection 或 command；
- cohort、task 或 source scope 在 session 中途改变；
- Operator 认为继续会危及真实项目；
- 未授权账号或 source 被访问；
- Evidence 保存位置不再安全。

### 10.2 Analysis exclusion（分析排除）

以下情况可以排除 pair，但必须保留记录：

- 相同风险或 snapshot 已在另一 condition 暴露；
- pair 的 repository/service scope 明显不等价；
- Condition T packet preparation cost 未记录；
- source outage 达到 freeze 时预先定义的 material threshold；
- session timebox 或 task wording 被改变；
- Operator 不是冻结的同一人；
- protocol deviation 足以改变主要指标；
- delayed adjudication 无法绑定 source window。

### 10.3 Non-excludable unfavorable results（不得排除的不利结果）

不能因为以下原因排除：

- TITMAS 更慢；
- false positive 较高；
- false negative 出现；
- COR 恶化；
- Operator reject/override 很多；
- packet 准备成本高；
- 结果未达到成功阈值。

### 10.4 Exclusion timing（排除时点）

排除决定应在 condition 汇总和成功计算前完成。

若只能在 unblinding 后决定：

- 必须记录原因；
- 同时报告 included-only 与 all-completed sensitivity；
- 不得隐藏原 pair；
- Reviewer 必须标记 post-outcome exclusion risk。

## 11. Statistical calculation rules（统计计算规则）

### 11.1 Analysis posture（分析立场）

这是小样本、单操作者的本地管理实验。

只报告：

- raw session values；
- matched-pair differences；
- matched-pair percentage changes；
- median；
- range；
- exclusions and missingness；
- sensitivity by order and learning stage。

不报告：

- population inference；
- customer/general ecosystem effect；
- statistical significance claim；
- p-value 驱动的通过；
- 因五个 pairs 而产生的普遍因果结论。

### 11.2 Pairing rule（配对规则）

只在已冻结且 Reviewer 确认可比的 pair 内计算。

对“越低越好”的指标：

```text
paired difference = T - M
paired percent reduction = (M - T) / M * 100%
```

负的 `paired difference` 表示 T 较低。

若 M 为 0：

```text
paired percent reduction = NOT_CALCULABLE
```

仍报告原始 M、T 和 absolute difference。

设计文档成功门槛使用 condition medians：

```text
condition median reduction =
(median_M - median_T) / median_M * 100%
```

每个 pair 的 difference 和 percent reduction 必须同时报告，作为 task comparability 和
sensitivity Evidence。paired percent reduction median 是辅助结果，不替代 condition
median reduction。

不得只汇总所有 events 而忽略 session 和 pair，也不得只选有利 pairs。

### 11.3 Time calculation（时间）

```text
ACTIVE_MANAGEMENT_TIME = DIRECT + OVERHEAD
```

`WAIT` 和 `MEASUREMENT` 不进入 active management time，但必须分别报告：

- wall-clock completion；
- external/Agent latency；
- measurement burden。

Condition T 的 packet preparation、verification、refresh、correction 和 override handling
必须进入 `DIRECT` 或 `OVERHEAD`，不能只记为附注。

### 11.4 Count metrics（计数指标）

Source hops 和 context switches：

- 按 session 计数；
- 对每个 pair 计算差值和 percent reduction；
- 报告 median、range 和原始值；
- 不用减少 hops 抵消 missed risk。

Onboarding：

- 按预先配对的 projects 计算 active time；
- 同时报告 source hops 和 unresolved mappings；
- 只有时间下降但 unresolved mappings 增加时，不视为完整改善。

### 11.5 Risk discovery time（风险发现时间）

每个 risk 使用：

```text
source-confirmed discovery time - first observable source time
```

没有可靠 source time 时，使用：

```text
source-confirmed discovery time - session start
```

先计算每个 session 的 median risk discovery time，再做 matched-pair comparison，避免风险
数量较多的 session 支配结果。成功门槛使用两个 conditions 的 session-median 中位数；
paired comparison 作为敏感性结果。

### 11.6 False-positive and false-negative rates

```text
FPR =
false-positive presented items
/ all presented risk items

FNR =
missed actionable risks
/ all actionable risks in the scoped reference set
```

同时报告：

- 每个 session 的 numerator/denominator；
- pooled numerator/denominator；
- 高影响 risk misses 的绝对数量；
- denominator 为 0 时的 `NOT_CALCULABLE`。

缺失值不插补为 0 或 success。

### 11.7 Threshold application（成功阈值）

严格使用设计文档既有阈值：

- management active time 的 condition median reduction 至少 25%；
- risk discovery session medians 的 condition median reduction 至少 25%；
- source hops/context switches 的 condition medians 至少一项降低 25%，另一项恶化不超过 5%；
- onboarding active time 的 condition median reduction 至少 20%；
- 高影响 false negative 为 0；
- 总体 FNR 与 FPR 相对 Baseline 的恶化不超过 5 percentage points；
- source、Authority、external-service 和 sensitive-data gates 全部通过。

本协议不降低或提高这些阈值。需要改变时先修订设计文档。

### 11.8 Missing, outlier and sensitivity rules（缺失、异常与敏感性）

- missing 不插补；
- outlier 默认保留；
- 被排除的 session 仍显示原始值；
- 报告 included pairs；
- 报告 all-completed sensitivity；
- 按 condition order 报告结果；
- 按 early/late stage 报告方向；
- 若结论依赖单个 pair，标为 fragile；
- 不通过删除慢 session 获得成功。

## 12. Cognitive Overhead Ratio（认知开销比）

### 12.1 Purpose（目的）

Cognitive Overhead Ratio，简称 `COR`，衡量一次管理 session 中有多少 active time 用于
“恢复和协调管理上下文”，而不是直接核验风险和准备决策输入。

它是管理负担诊断，不是心理学临床测量，也不声称直接测量人的全部认知状态。

### 12.2 Formula（公式）

```text
COR =
OVERHEAD minutes
/ (DIRECT minutes + OVERHEAD minutes)
```

范围为 0 到 1，也可以报告为百分比。

若 `DIRECT + OVERHEAD = 0`：

```text
COR=NOT_CALCULABLE
```

### 12.3 Required classification（必需分类）

计入 `OVERHEAD`：

- 寻找 canonical source；
- 跨工具导航；
- 恢复 repository/task 上下文；
- 重复复制或对账状态；
- 解决 source conflict；
- 准备、刷新和纠正 attention packet；
- 为理解 packet 重新寻找其来源；
- 处理错误排序和 override。

计入 `DIRECT`：

- 阅读并核验与当前风险直接相关的 source 内容；
- 判断 actionability、scope 和 uncertainty；
- 形成 Human Decision input；
- 明确 unknown 或 insufficient Evidence。

不进入 COR 分母：

- `WAIT`；
- `MEASUREMENT`；
- 与本任务无关的 interruption。

这些时间仍必须报告。

### 12.4 Pair calculation（配对计算）

每个 pair 计算：

```text
COR difference = COR_T - COR_M
COR relative reduction = (COR_M - COR_T) / COR_M * 100%
```

若 `COR_M = 0`，relative reduction 为 `NOT_CALCULABLE`，只报告 difference。

再报告：

- 每个 condition 的 COR median 和 range；
- paired difference median；
- paired relative-reduction median；
- early/late 和 order sensitivity。

### 12.5 Interpretation（解释）

- `COR_T < COR_M`：TITMAS condition 的协调性开销比例较低；
- `COR_T = COR_M`：未观察到比例改善；
- `COR_T > COR_M`：TITMAS 可能增加新的协调负担；
- COR 下降但 active management time 上升：不能称为总降本；
- active management time 下降但 COR 上升超过 5 percentage points：触发
  `COGNITIVE_OVERHEAD_REVIEW_REQUIRED`。

COR 不能替代 management time、risk discovery、FPR 或 FNR，也不能单独决定成功。

## 13. Learning-effect controls（学习效应控制）

### 13.1 Calibration exclusion（校准排除）

- Condition M 和 T 各一次 Calibration；
- Calibration 只检查模板、时间分类和流程理解；
- Calibration 不进入成功计算；
- Calibration 使用的 snapshot/risk 不得再次进入有效 session。

### 13.2 Alternating order（交替顺序）

- Pair 顺序在查看 source window 前冻结；
- 使用 M/T 与 T/M 交替；
- Condition T 不得总在后面；
- 同一具体 snapshot 不重复两种 condition；
- source window 应不同但按 scope 和 complexity notes 配对。

### 13.3 Prior familiarity（既有熟悉度）

每个 session 开始前记录 Operator 对该 repository/window 的熟悉度：

- `New`；
- `Some`；
- `High`。

matched pair 应尽量使用相同 familiarity category。明显不匹配时标记 limitation 或排除。

### 13.4 Information isolation（信息隔离）

- Operator 在全部有效 sessions 完成前不查看 adjudication；
- 不把前一 condition 的风险清单带入后一 condition；
- 已知重复风险立即标记 contamination；
- Attention preparer 不向 Operator 提供 packet 之外的额外口头提示；
- Reviewer 在初次 adjudication 时不看 condition 和效率结果。

### 13.5 Early/late sensitivity（前后阶段敏感性）

分别报告：

- 前半 sessions 的 paired direction；
- 后半 sessions 的 paired direction；
- M-first pairs；
- T-first pairs；
- Calibration 后第一个有效 pair；
- 去除第一个有效 pair 后的方向。

第一个有效 pair 不自动排除。只有预先冻结的规则或明确 deviation 才能排除。

### 13.6 Learning-effect failure（学习效应失败）

以下任一情况使结果至少标为 `LEARNING_EFFECT_UNCONTROLLED`：

- T 总在 M 之后；
- 同一风险被两种 condition 重复使用；
- condition order 在看过风险后改变；
- Operator 看到 adjudication 或汇总成功结果；
- early/late 方向完全相反且无法解释；
- familiarity 严重不匹配。

此时不得声称 TITMAS 导致改善；Experiment Owner 决定 `INCONCLUSIVE` 或重新设计。

## 14. Manual result review（人工结果复核）

Reviewer 依次确认：

1. cohort freeze 完整；
2. roles 和 overlap 已披露；
3. Calibration 未进入结果；
4. 至少五个有效 matched pairs；
5. onboarding 样本满足设计；
6. exclusions 在汇总前决定；
7. packet cost 全部计入；
8. source hops/context switches 定义一致；
9. delayed adjudication 完成；
10. FPR/FNR denominator 可追溯；
11. COR 分类可复核；
12. learning-effect sensitivity 已报告；
13. external services 未被替代或写回；
14. Authority 和 sensitive-data gates 通过；
15. 结论只在冻结 cohort 和 Operator 范围内成立。

Reviewer 输出只能是有范围的 protocol review，不是 Architecture Decision 或
Implementation Authorization。

## 15. Auxiliary Qwen protocol review（Qwen 辅助协议审查）

首先尝试使用当时端点中最高代际的 `qwen3.8-max-preview`。该请求在 120 秒内未返回：

```text
QWEN_3_8_REVIEW=NO_CURRENT_VERDICT_TIMEOUT
```

超时不等于通过。

随后按实际可用性降级到 `qwen3.7-max`，完成 advisory-only protocol review。

采纳：

- `DIRECT / OVERHEAD / WAIT / MEASUREMENT` 必须严格分离；
- packet 准备、刷新和纠错必须进入 `OVERHEAD`；
- Reviewer 应尽量对 condition 设盲；
- Calibration 不进入最终计算；
- 不允许自动抓取、自动计时、自动 adjudication 或外部写回。

未采纳：

- 对至少五个 pairs 使用 Wilcoxon significance test；
- 把 M/T order 作为协变量做推断。

原因：

- 本设计是小样本 local signal，不支持 population inference；
- 预先设计明确要求原始值、paired difference、median、range 和 sensitivity；
- 增加显著性检验会制造超出当前 Evidence 的统计外观；
- Qwen output 不构成 Human Decision、scientific evidence 或实验授权。

调用只使用受保护环境变量；本协议不保存或披露 credential。

## 16. Protocol completion and non-effects（协议完成与非效果）

协议文档完成后：

```text
PROTOCOL_DOCUMENT_CREATED=true
COHORT_FROZEN=false
ROLES_ASSIGNED=false
SESSIONS_EXECUTED=0
EVIDENCE_COLLECTED=false
ADJUDICATION_COMPLETED=false
STATISTICS_CALCULATED=false
EXPERIMENT_RESULT=NOT_RUN
```

并保持：

```text
NEW_CONTROL_CENTER_CREATED=false
NEW_AUTOMATIC_SCHEDULER_CREATED=false
NEW_AGENT_SELECTOR_CREATED=false
EXTERNAL_SERVICE_REPLACED=false
CODE_CREATED=false
DASHBOARD_CREATED=false
API_CREATED=false
ADAPTER_CREATED=false
REPOSITORY_CREATED=false
SCHEMA_CREATED=false
IMPLEMENTATION_AUTHORIZED=false
EXPERIMENT_EXECUTION_AUTHORIZED=false
```

下一步只能是 Human Review 本协议，并单独决定是否冻结 cohort 和授权一次人工实验。
