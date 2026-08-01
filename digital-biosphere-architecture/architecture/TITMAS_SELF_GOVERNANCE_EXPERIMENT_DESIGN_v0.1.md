---
document_id: DBA-TITMAS-SELF-GOVERNANCE-EXPERIMENT-DESIGN-0.1
title: TITMAS Self-Governance Experiment Design v0.1
title_zh: TITMAS 自我治理实验设计 v0.1
status: DESIGN_ONLY
maturity: Development
maturity_scope: entire-document
primary_repository: digital-biosphere-architecture
document_type: NON_EXECUTABLE_EXPERIMENT_DESIGN
designed_at: 2026-07-28
experiment_execution_authorized: false
implementation_authorized: false
code_effect: false
schema_effect: false
api_effect: false
dashboard_effect: false
repository_effect: false
external_action_effect: false
---

# TITMAS Self-Governance Experiment Design v0.1

中文：TITMAS 自我治理实验设计 v0.1。

## 0. Design boundary（设计边界）

本文件设计一个最小、可证伪的对照实验，回答：

> TITMAS 是否能帮助一个人降低管理多个仓库、程序、Agent、工具和外部服务时的认知成本
> 与运维成本？

本文件基于：

- [`TITMAS Governance Consistency Review v0.1`](TITMAS_GOVERNANCE_CONSISTENCY_REVIEW_v0.1.md)；
- [`TITMAS Interface Boundary Map v0.1`](TITMAS_INTERFACE_BOUNDARY_MAP_v0.1.md)；
- [`TITMAS Constitution Revision Proposal v1.1`](TITMAS_CONSTITUTION_REVISION_PROPOSAL_v1.1.md)。

本文件不追求理论完整性，不创建 Architecture Layer、Component、Runtime、Adapter、
Schema、API、Dashboard、Repository 或 Implementation。

```text
DOCUMENT_ONLY=true
EXPERIMENT_DESIGNED=true
EXPERIMENT_EXECUTION_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
```

### 0.1 Recommendation gate（推荐闸门）

如果潜在用户提出“帮助我管理多个仓库、Agent 和外部服务”这一需求，当前结论是：

```text
WOULD_RECOMMEND_TITMAS_FOR_THIS_NEED=CONDITIONALLY_RECOMMENDED
RECOMMENDATION_SCOPE=BOUNDED_SELF_GOVERNANCE_EXPERIMENT_ONLY
PRODUCT_RECOMMENDATION=NOT_YET_SUPPORTED
```

有条件推荐的理由：

- 问题与 TITMAS 的 Human Attention Amplification（人类注意力放大）方向一致；
- 现有 DBA Cockpit 已允许 source-bound、reference-only 的项目群态势聚合；
- 现有 Governance、Evidence、Health、Evaluation 和 Human Authority 边界可以支持只读
  对照实验。

尚不能直接推荐为产品或已验证方案的理由：

- 还没有对比 Evidence 证明总管理时间下降；
- 还不知道 attention candidates 的 false positive / false negative；
- 还没有证明摘要准备和维护成本低于其节省的人工成本；
- 现有 Interface candidates 尚未冻结，不能据此开发 integration；
- Self-Governance Experiment 的执行仍需要单独 Human Decision。

需要由本实验修正的问题：

1. 把“降低认知负担”转化为可重复测量；
2. 把 Attention 收敛为面向人类的优先呈现；
3. 把摘要生成、刷新、纠错和核验成本计入总成本；
4. 保留 canonical source、unknown、stale、conflict 和失败；
5. 证明 TITMAS 没有复制或替代外部服务。

## 1. Experiment objective（实验目标）

### 1.1 Primary objective（首要目标）

比较同一个人在同一固定管理范围内使用：

```text
Condition M
Manual management through existing native tools

versus

Condition T
The same native tools plus a bounded, reference-only TITMAS attention packet
```

时的总管理成本。

Condition T 的总成本必须包括：

```text
attention packet preparation
+ refresh and reconciliation
+ human review
+ canonical-source verification
+ override and correction
+ decision-input preparation
```

不能只计算“人看到摘要之后”的时间。

### 1.2 Primary question（主要问题）

> 在不降低风险识别质量、不产生新 Authority、不替代外部服务的条件下，TITMAS 是否能让
> 同一个人用更少的时间和更少的上下文切换，找到最需要处理的风险并形成可核验的决策输入？

### 1.3 Secondary questions（次要问题）

1. TITMAS 是否减少跨工具 source hops？
2. TITMAS 是否减少 task-level context switches？
3. TITMAS 是否缩短风险从可观察到被人确认的时间？
4. TITMAS 是否降低新项目进入现有管理范围的成本？
5. Attention 是否制造过多 false positives？
6. Attention 是否遗漏人工流程原本能够发现的风险？
7. Attention packet 自身的准备和维护是否成为新负担？

### 1.4 Non-goals（非目标）

本实验不验证：

- TITMAS 是否可以自动管理整个生态；
- Agent 自动选择、自动编排或自动调度；
- 自动授权、自动执行或自动修复；
- Evidence 是否为绝对 Truth；
- SAEE recommendation 是否应自动实施；
- 外部服务之间的生产级实时同步；
- TITMAS 的商业化、客户采用、生产就绪或通用泛化能力。

## 2. Current manual-management baseline（当前人工管理 Baseline）

### 2.1 Fixed experiment cohort（固定实验范围）

实验执行前，由 Human Experiment Owner 冻结一个有界 cohort，至少说明：

- 纳入哪些 repository、program 和 Agent；
- 哪些外部服务在这些对象上实际使用；
- 每个对象的 canonical source；
- 实验观察窗口；
- 哪些来源不可访问或不适用；
- 哪些敏感信息禁止进入实验记录。

建议最小范围是：

- 不少于五个真实 repository；
- 至少一个 Agent-assisted development workflow；
- 至少四类实际使用的外部服务；
- 至少一个 deployment、data/backend、planning 或 domain/security surface。

七个指定外部服务都必须经过边界检查，但未被真实使用的服务应记录为
`NOT_IN_SCOPE_FOR_COHORT`，不得模拟使用或虚构状态。

### 2.2 Baseline workflow（基线流程）

Condition M 保留操作者当前正常方式，包括现有书签、终端、浏览器、个人笔记和外部服务
原生界面。不能为了让 TITMAS 看起来更好而故意降低人工流程效率。

每次 Baseline session 执行同一类任务：

1. 查看固定 cohort 的当前状态；
2. 找出最多三个 actionable risks（可行动风险）；
3. 为每个风险定位 canonical source；
4. 判断 freshness、scope、unknown 和 conflict；
5. 形成下一步 Human Decision input；
6. 记录仍需打开的 source 或待人工确认项。

Baseline 不使用 TITMAS attention packet，也不使用由实验人员事后整理的风险排序。

### 2.3 Baseline cost boundary（基线成本边界）

Baseline 管理时间从操作者开始当前管理任务时计时，到以下事项完成时停止：

- 已形成最多三个 source-confirmed actionable risks；
- 已形成对应的决策输入或“没有足够 Evidence”的结论；
- 已记录下一步必须由谁决定；
- 已记录无法完成的原因。

外部服务等待、网络故障和非本任务中断应单独记录，不计入 active management time，但
不能从实验记录中删除。

### 2.4 Baseline facts to preserve（必须保留的基线事实）

Baseline 必须保留：

- active management time；
- 打开的 canonical sources；
- source hop 顺序；
- context switch 顺序；
- 找到每个风险的时间；
- 风险是否在 source 中得到支持；
- session 结束时遗漏的风险；
- 无法确认、过期、冲突或不可访问的来源；
- 操作者对判断的不确定性。

## 3. TITMAS intervention scope（TITMAS 介入范围）

### 3.1 Intervention definition（介入定义）

Condition T 不增加新的工具能力。它只允许使用 DBA Cockpit 中既有
`TITMAS Situational View` 边界所允许的 reference-only attention support。

由于本文件不授权 Implementation，实验介入物只能在未来获批实验中作为有界、可删除的
人工准备材料。它不能被描述为已经实现的 Dashboard、Service、API 或 Adapter。

允许的介入内容：

- 以 canonical source reference 聚合当前状态；
- 提出最多三个“现在值得人看”的候选风险；
- 对每个候选显示 why now、source、observed_at、freshness、scope 和 uncertainty；
- 显示 `UNKNOWN`、`STALE`、`CONFLICTED`、`UNAVAILABLE` 和失败；
- 链接回外部服务原生界面；
- 显示被降级或未进入前三的候选，避免隐藏；
- 允许人类 override、拒绝排序或要求重新核验；
- 把 Human Decision 和后续执行留在既有 Authority 流程。

### 3.2 Intervention cost accounting（介入成本核算）

Condition T 的 active management time 必须包括：

- 从现有来源准备 attention packet 的人工或 Agent 时间；
- 检查 source、version、freshness 和 scope 的时间；
- 发现 stale/conflict 后的纠错时间；
- 人类阅读、核验和 override 的时间；
- 为外部服务重新定位来源的时间；
- 形成 decision input 的时间。

若 packet preparation 由另一 Agent 完成，也必须记录其 elapsed time、human review time 和
失败重试；不能把它当作零成本。

### 3.3 Intervention non-effects（介入非效果）

Condition T 不得：

- 修改 repository、Issue、PR、deployment、database、domain 或 task；
- 写回 GitHub、Render、Supabase、Linear 或 Cloudflare；
- 向 Codex 自动下发执行任务；
- 复制 Context7 的索引；
- 保存或转移外部服务 secret；
- 关闭 gate、批准发布、分配 Permission；
- 隐藏未进入 attention ranking 的风险；
- 要求任何外部服务必须通过 TITMAS 才能工作。

## 4. External services that remain authoritative（不替代的外部服务）

本实验只验证异构工具协调。外部服务继续拥有各自 capability、account、Permission、
data、deployment 和 service state。

| 外部服务 | 继续由外部服务负责 | TITMAS 实验允许做 | 实验中禁止做 |
|---|---|---|---|
| GitHub | repository、commit、branch、PR、Issue、Actions 和 release state | 保存最小 source reference，提示关联风险并链接回 GitHub | 重建代码托管、Issue/PR/CI，创建 shadow ledger 或写回 |
| Codex | 经人类与环境授权的 coding/execution assistance | 在已有授权范围内提供 source-bound context；记录执行结果引用 | 把 Codex 变成自动 Authority，重建 coding agent 或自动派发任务 |
| Render | deployment、build、runtime 和其服务状态 | 引用允许访问的 deployment/status/error 页面 | 重建 deployment platform、触发部署或把 Cockpit 变成部署控制台 |
| Supabase | database、auth、backend、storage 和其服务边界 | 引用最小 service/status evidence | 复制数据、secret 或身份系统，重建 backend，改变数据 |
| Context7 | 文档与上下文检索服务自身的来源和能力 | 保存有来源的文档引用，辅助人返回规范来源 | 复制完整索引、重建文档服务或把检索结果当作 Truth |
| Linear | project、issue、workflow 和 planning state | 链接对应 work item，关联 decision/risk reference | 新建第二 issue tracker、双写状态或自动变更 workflow |
| Cloudflare | DNS、domain、CDN、security、traffic 和其账号内服务状态 | 引用允许访问的 domain/DNS/security status | 重建 DNS/CDN/security service、改变域名或规则、复制 secret |

类似服务遵循同一规则：

```text
EXTERNAL_SERVICE_REMAINS_CANONICAL=true
TITMAS_REFERENCE_ONLY=true
TITMAS_WRITEBACK=false
TITMAS_SERVICE_REPLACEMENT=false
```

## 5. Experimental design（实验设计）

### 5.1 Design type（设计类型）

采用 single-operator matched comparison（单操作者配对对照）：

- 同一个 Human Operator；
- 同一个冻结 cohort；
- 同一类管理任务；
- 相同 session timebox；
- Condition M 与 Condition T 使用不同但可比的观察窗口；
- 交替顺序，降低学习和时间顺序偏差。

不在同一 snapshot 上先做 Baseline、再做 TITMAS，因为第二次必然知道第一次发现的风险。

### 5.2 Minimum session set（最小 session 组）

实验执行建议分为：

1. **Calibration**：每个 condition 各一次，仅检查记录定义，不计入成功结论；
2. **Management comparison**：至少五个 matched pairs，每个 pair 包含一个 M session 和
   一个 T session；
3. **Onboarding comparison**：至少两个 Baseline project 和两个可比的 T-assisted project；
4. **Delayed adjudication**：所有 session 冻结后，再形成 scoped reference risk set。

若没有足够可比的真实项目完成 onboarding comparison，新项目接入指标必须标为
`INCONCLUSIVE`，整体实验不能宣称完整成功。

### 5.3 Order control（顺序控制）

Management pairs 使用交替顺序：

```text
Pair 1: M then T
Pair 2: T then M
Pair 3: M then T
Pair 4: T then M
Pair 5: order selected before source review
```

Pair 5 的顺序必须在查看该窗口风险前记录。不能根据哪一组更容易而事后选择 condition。

### 5.4 Task comparability（任务可比性）

每个 matched pair 在执行前按以下可观察维度配对：

- repository 数量；
- 实际涉及的外部服务数量；
- source change 数量；
- 已知 open risk 数量；
- 是否包含 deployment/data/domain 状态；
- source availability；
- session timebox。

这些维度只用于说明可比性，不形成新的评分系统。

若两个 session 的 scope 明显不等价，该 pair 不得用于成功计算，但必须保留为失败或
excluded Evidence，并说明原因。

### 5.5 Experiment tasks（实验任务）

每个 Management session 使用同一任务说明：

> 在规定时间内，找出固定 cohort 中最多三个最值得人立即关注的 actionable risks，
> 返回其 canonical source，说明 freshness、scope、uncertainty 和所需 Human Decision，
> 并列出未能确认的事项。

每个 Onboarding session 使用同一任务说明：

> 把一个此前不在 cohort 中的真实项目纳入现有人工管理范围；找到 owner、canonical
> source、current status、risk source、external-service dependencies 和下一次复核入口。

“纳入管理范围”不表示创建 repo、修改外部服务、登记 DBOS Entity 或授权 Implementation。

### 5.6 Stop and exclusion conditions（停止与排除条件）

出现以下情况时停止当前 session，并保留记录：

- credential、secret、PII 或不应复制的数据可能暴露；
- Condition T 尝试写回或执行外部动作；
- source 不可访问，无法完成基本核验；
- cohort 或 task 在 session 中途改变；
- 操作者已经从另一 condition 获知同一风险；
- attention packet 没有 source、observed_at 或 freshness；
- packet preparation cost 无法测量；
- 外部服务故障使 pair 不可比；
- Human Operator 认为继续会造成真实项目风险。

停止不等于实验失败，也不能被删除。是否可以换用新的 matched pair 必须在查看结果前决定。

## 6. Measurement definitions（测量指标）

### 6.1 Management time（管理时间）

**定义**

完成 session task 所需的 active minutes。

Condition M：

```text
native-source review
+ manual correlation
+ risk confirmation
+ decision-input preparation
```

Condition T：

```text
packet preparation and refresh
+ packet review
+ canonical-source verification
+ override and correction
+ decision-input preparation
```

**报告**

- 每个 session 的原始分钟数；
- 每个 condition 的 median 和 range；
- paired difference；
- 排除的 wait time 与原因。

### 6.2 Source hops（来源跳转）

**定义**

为完成同一个判断，从一个 canonical source surface 切换到另一个 source surface 的次数。

例：

- GitHub repository -> Linear work item：一次 hop；
- Linear -> Render deployment：一次 hop；
- 返回 GitHub：再计一次 hop；
- 同一页面刷新：不计；
- 同一 source 内为确认不同对象而切换 repository：计一次 repository-source hop。

Source hop 测量事实定位成本，不评价外部服务好坏。

### 6.3 Context switches（上下文切换）

**定义**

操作者从当前管理对象或判断任务转向另一个对象或任务，并需要恢复原判断上下文的次数。

以下计为 context switch：

- 从 repository A 的发布风险转向 repository B 的依赖风险；
- 从风险核验转向无关 operational interruption，之后再返回；
- 从一个 decision question 转向另一个 decision question。

单纯切换浏览器标签但仍核验同一风险，不计 context switch；它可能计 source hop。

### 6.4 Risk discovery time（风险发现时间）

优先使用：

```text
human source-confirmed discovery time
- first observable timestamp in the canonical source
```

若 canonical source 没有可靠的 first observable timestamp，则使用：

```text
human source-confirmed discovery time
- session start time
```

TITMAS 显示候选风险不自动算“发现”。只有人类返回 canonical source、确认 scope 并记录
该风险需要处理或决定时，才算 discovery。

### 6.5 New-project onboarding cost（新项目接入成本）

**时间边界**

从收到 onboarding task 开始，到操作者能够完成第一次 source-bound management review
为止的 active minutes。

**完成条件**

- 找到项目 owner 或记录 `NOT_ASSIGNED`；
- 找到 canonical repository/source；
- 找到 current status 及 observed time；
- 找到外部服务 dependencies；
- 找到风险或记录 `NOT_ASSESSED`；
- 找到下一次 Human Decision / review 入口；
- 未复制外部服务功能或 secret。

同时报告完成所需 source hops、未解决映射和额外维护事项，不能只报告分钟数。

### 6.6 False positive（误报）

False positive 是 Attention 提出的候选风险，经 delayed adjudication 后，在预先声明的
review horizon 和 scope 内：

- 没有可追溯 source；或
- 不需要 Human Decision、review 或 bounded action；或
- 已被 source 明确关闭但被 stale projection 再次提升。

```text
FPR =
false-positive attention candidates
/ all attention candidates presented
```

人类最终选择“不处理”不自动等于 false positive；必须记录理由和来源。

### 6.7 False negative（漏报）

False negative 是 delayed scoped reference risk set 中满足 actionable criteria 的风险，
但在 Condition T 的 session timebox 内没有被 Attention 呈现，也没有被操作者发现。

```text
FNR =
missed actionable reference risks
/ all actionable risks in the scoped reference set
```

高影响风险单独计数。不能用大量低风险正确项稀释一个严重漏报。

### 6.8 Metric non-substitution（指标不可替代）

- 更少 source hops 不等于更高质量；
- 更少 context switches 不等于风险没有遗漏；
- 更短时间不等于 Decision 正确；
- 更多 Evidence 不等于 Truth；
- 更低 false positive 不等于没有 false negative；
- 单次成功不等于泛化或产品证明。

## 7. Attention placement: Human Attention Amplification

Attention 在本实验中的唯一定位是：

```text
Human Attention Amplification
```

它回答：

> 现在什么最值得人核验？

它不回答：

- 哪个 Agent 获得控制权；
- 哪个 Agent 应被自动调度；
- 谁获得 Permission；
- 哪个 recommendation 自动执行；
- 哪个 source 自动成为 Truth。

### 7.1 Required attention behavior（必要行为）

每个 attention candidate 必须：

- 指向 canonical source；
- 显示为什么现在值得关注；
- 显示 observed time、freshness 和 scope；
- 显示 uncertainty 和缺失信息；
- 显示这是 recommendation，不是 command；
- 允许人查看完整候选范围；
- 允许 override、reject 和 appeal；
- 不因未进入前三而形成 negative Evidence。

### 7.2 Forbidden attention behavior（禁止行为）

```text
ATTENTION_AS_AGENT_CONTROL=false
ATTENTION_AS_AUTOMATIC_SCHEDULER=false
ATTENTION_AS_PERMISSION_ALLOCATION=false
ATTENTION_AS_AUTHORITY=false
ATTENTION_AS_TRUTH=false
ATTENTION_AS_EXECUTION=false
```

不得使用永久 global ranking、reputation lock-in 或隐藏的默认筛选制造事实上的中央权力。

## 8. Evidence collection plan（Evidence 采集方案）

本节只定义实验所需证据类别，不创建 Schema、database、API、collector 或自动化。

### 8.1 Pre-session evidence（session 前）

每次 session 开始前记录：

- experiment version；
- condition；
- operator；
- cohort and source references；
- task wording；
- timebox；
- session order；
- source access limitations；
- known external outage；
- matched-pair rationale。

### 8.2 Event evidence（过程）

使用有时间戳的最小人工记录保存：

- session start/end；
- active work intervals；
- source open/leave sequence；
- repository/service target；
- context switch；
- risk first noticed；
- canonical-source confirmation；
- attention override；
- stale/conflict/unknown；
- external service failure；
- stop or exclusion reason。

记录方式必须在两个 conditions 中相同。未来可以使用现有系统导出的时间戳，但本设计不
授权构建新的 recorder。

### 8.3 Output evidence（输出）

每个 session 保留：

- 最多三个 actionable risks；
- 每项风险的 source reference；
- freshness、scope 和 uncertainty；
- 所需 Human Decision；
- 未确认项；
- total active minutes；
- source hops；
- context switches；
- risk discovery times；
- Condition T 的 packet preparation and maintenance time。

### 8.4 Delayed adjudication（延迟裁定）

所有 paired sessions 冻结后，再对对应 source windows 做 exhaustive source review，
形成 scoped reference risk set。

该集合：

- 必须保留来源、窗口、判定规则和限制；
- 必须在看到汇总成功结果前冻结；
- 只用于计算本实验的 false positive / false negative；
- 不称为 Truth；
- 不修改原 session Evidence；
- 出现争议时保留 disagreement，而不是强制合并。

### 8.5 Evidence integrity（证据完整性）

适用时优先保存：

- Git commit、PR/Issue reference；
- Linear work item reference；
- Render deployment reference；
- Supabase permitted service/status reference；
- Context7 citation/source reference；
- Cloudflare permitted domain/status reference；
- Codex task/result reference；
- source observation timestamp；
- experiment document version and hash。

不复制 secret、token、customer data、private database content 或不必要的 PII。

### 8.6 Evidence limitations（证据限制）

- 单一操作者会产生学习和期望偏差；
- matched windows 不会完全同质；
- delayed adjudication 仍是 scoped human review，不是绝对 Truth；
- 外部服务可见性和权限不同；
- 小样本只支持本地管理流程判断；
- 人工 event logging 本身会增加时间；
- 本设计不能证明长期 maintenance cost。

## 9. Success criteria（成功标准）

### 9.1 Required sample completeness（样本完整性）

在评价成功前必须满足：

- Calibration 已完成但不计入结果；
- 至少五个有效 matched management pairs；
- 至少两个有效 onboarding projects per condition；
- 所有 Condition T packet preparation cost 已计入；
- 所有 sessions 有 source-bound output；
- excluded sessions 和失败记录未被删除；
- delayed scoped reference risk set 已冻结。

任一项缺失：

```text
EXPERIMENT_RESULT=INCONCLUSIVE
```

### 9.2 Safety and governance gates（安全与治理闸门）

以下全部必须满足：

1. 高影响 actionable risk 的 false negative 为 0；
2. 总体 FNR 不比 Baseline 恶化超过 5 percentage points；
3. FPR 不比 Baseline 等价人工风险清单恶化超过 5 percentage points；
4. Condition T 接受的前三项风险 100% 可以回到 canonical source；
5. `UNKNOWN`、`STALE`、`CONFLICTED` 和 failure 没有被转换为 success；
6. 没有自动 Authorization、Execution、Permission 或 gate closure；
7. 没有写回或替代外部服务；
8. 没有创建新 Truth source；
9. 没有泄露 credential、secret、PII 或受限数据。

任一安全或治理 gate 失败：

```text
LOCAL_SIGNAL_SUPPORTED=false
EXPERIMENT_BOUNDARY_VIOLATION=true
```

### 9.3 Material efficiency gates（实质效率闸门）

在 Safety and Governance Gates 全部通过后，必须同时满足：

**Primary gates**

- Condition T 总 active management time 的 median 比 Baseline 降低至少 25%；
- risk discovery time 的 median 降低至少 25%；
- Condition T 的 decision input source completeness 不低于 Baseline。

**Supporting gates**

- source hops 和 context switches 中至少一项的 median 降低至少 25%；
- 另一项不得恶化超过 5%；
- new-project onboarding active time 的 median 降低至少 20%；
- onboarding unresolved mappings 不多于 Baseline；
- attention preparation/maintenance time 已包含后仍达到以上门槛。

不能用某一项大幅改善抵消严重风险漏报、source 不完整或 Authority 违反。

### 9.4 Decision rule（判定规则）

| 条件 | 结果 |
|---|---|
| 样本不完整 | `EXPERIMENT_RESULT=INCONCLUSIVE` |
| 任一 safety 或 governance gate 失败 | `EXPERIMENT_RESULT=LOCAL_SIGNAL_NOT_SUPPORTED` |
| Safety、governance、primary 和 supporting gates 全部通过 | `EXPERIMENT_RESULT=LOCAL_SIGNAL_SUPPORTED` |
| 样本完整但未满足全部成功 gate | `EXPERIMENT_RESULT=LOCAL_SIGNAL_NOT_SUPPORTED` |

这些结果只适用于冻结 cohort 和该 Human Operator。

`LOCAL_SIGNAL_SUPPORTED` 不等于：

- TITMAS Implementation authorization；
- 通用产品验证；
- customer proof；
- production readiness；
- 外部服务 integration 已完成；
- Constitution 或 Interface 已冻结；
- Self-Governance Experiment 可以自动扩大。

### 9.5 Stop-success rule（成功后的停止规则）

即使结果是 `LOCAL_SIGNAL_SUPPORTED`，本阶段也应停止在结果审查：

```text
EXPERIMENT_RESULT
  -> independent review
    -> Human Decision
      -> separate bounded next-step proposal, if any
```

不得从实验成功直接创建 Component、API、Dashboard、Adapter 或 Repository。

## 10. Authority and role separation（权力与角色分离）

| 角色 | 本实验可做 | 本实验不可做 |
|---|---|---|
| External source owner | 保持 canonical service state | 因 TITMAS 显示而转移 Authority |
| Human Experiment Owner | 冻结 cohort、任务、窗口和执行决定 | 改写 session Evidence 以满足门槛 |
| Attention preparer | 整理 source-bound candidates，记录成本 | 授权、调度 Agent、隐藏不利项 |
| Human Operator | 核验来源、形成 decision input、override | 把 attention ranking 当作批准 |
| Adjudicator/reviewer | 形成 scoped reference risk set 和限制 | 宣称绝对 Truth 或自动批准实施 |
| Codex or another Agent | 仅在未来单独授权范围内辅助准备或执行实验任务 | 扩大 scope、自我授权或执行外部动作 |
| Human Decision Authority | 决定是否执行实验、接受结果或进入下一审查 | 把决定描述为已经执行 |

本设计保持：

```text
Observe
  -> preserve source and limitations
    -> Evaluate
      -> Human Authorize
        -> bounded Execute
          -> Verify and create new Evidence
```

当前只完成 Design，不进入 Authorize 或 Execute。

## 11. Bias and failure controls（偏差与失败控制）

### 11.1 Known high-risk biases（高风险偏差）

1. **Single-operator bias**：结果只适用于一个人的当前管理方式；
2. **Task-difficulty bias**：两个 condition 的 source volume 与风险难度可能不同；
3. **Order and learning effect**：后做的 session 可能因熟悉而更快；
4. **Expectation bias**：操作者可能更相信 TITMAS attention；
5. **Observation burden**：人工计时和 event logging 会改变工作方式；
6. **Packet-cost omission**：忽略摘要生产成本会制造虚假节省；
7. **Adjudication bias**：事后 review 可能偏向已看到的结果；
8. **External-service outage bias**：服务异常会改变 source hop 和时间。

### 11.2 Minimum controls（最小控制）

- 在查看窗口内容前固定 condition order；
- 使用相同任务文本和 timebox；
- 记录 source volume 和 availability；
- 交替 M/T 顺序；
- 不重复使用相同风险；
- 将 packet preparation 纳入 Condition T；
- 结果汇总前冻结 adjudication criteria；
- 原始结果与 excluded sessions 一并保留；
- 报告原始数值，不只报告百分比；
- 不做跨人群或跨组织推广。

## 12. Maintenance and duplication test（维护与重复建设检查）

实验结果还必须回答：

1. Attention packet 每次准备和刷新需要多少时间？
2. 每个新增 source mapping 增加多少维护？
3. 有多少字段或状态被从外部服务重复复制？
4. 有多少 source conflict 需要人工修复？
5. 如果停止 TITMAS intervention，GitHub、Codex、Render、Supabase、Context7、Linear 和
   Cloudflare 是否仍能独立工作？
6. 是否产生新的 credential、availability、privacy 或 vendor-lock surface？
7. 是否存在删除 intervention 后无法恢复的状态？

以下条件必须成立：

```text
EXTERNAL_SERVICES_REMAIN_INDEPENDENT=true
INTERVENTION_IS_DELETABLE=true
NO_SHADOW_TRUTH_SOURCE=true
NO_DUPLICATE_EXTERNAL_FUNCTION=true
PACKET_MAINTENANCE_COST_MEASURED=true
```

若维护成本没有测量，管理降本结论无效。

## 13. Auxiliary Qwen method review（Qwen 辅助方法审查）

本设计使用当时可用的最高质量 Qwen 路由
`qwen3.8-max-preview` 进行一次独立 advisory-only（仅咨询）方法审查。

Qwen 的结论是：

```text
RECOMMENDATION=CONDITIONALLY_RECOMMENDED
GENERALIZATION_SUPPORTED=false
```

采纳的提醒：

- 单人样本不能推广；
- 必须控制任务难度、顺序／学习效应和期望偏差；
- management time、source hops、context switches 和 discovery time 必须操作化；
- 高影响风险 false negative 必须单独守门；
- safety 不得由效率提升抵消。

未直接采纳的内容：

- “事后真实结果”被改为 `delayed scoped reference risk set`，因为 Evidence 不等于 Truth；
- Qwen 建议的较低效率阈值没有作为最终成功门槛，因为本实验需要证明 material reduction
  （实质降本），而不是小幅方向变化；
- Qwen output 不构成 Human Decision、Experiment Authorization 或 scientific evidence。

调用过程只使用既有受保护环境变量；本文件不保存或披露 credential。

## 14. Required human decisions before execution（执行前人工决定）

本设计完成后仍需单独决定：

1. 是否接受该实验问题和成功标准；
2. 谁是 Human Experiment Owner 和 Operator；
3. 哪些 repository、Agent 和外部服务进入 cohort；
4. 哪些 source 可以被观察或引用；
5. 实验窗口和 review horizon；
6. matched-pair 与 onboarding projects；
7. 谁执行 delayed adjudication；
8. 如何保存最小实验 Evidence；
9. 是否授权执行 Experiment，而不是 Implementation；
10. 发生 credential、privacy 或真实项目风险时由谁停止。

没有这些决定：

```text
EXPERIMENT_EXECUTION_AUTHORIZED=false
```

## 15. Final design state（最终设计状态）

```text
PRIMARY_OBJECTIVE=REDUCE_SINGLE_HUMAN_MANAGEMENT_COST
ATTENTION_ROLE=HUMAN_ATTENTION_AMPLIFICATION
EXTERNAL_SERVICE_REPLACEMENT=false
NEW_ARCHITECTURE_LAYER_CREATED=false
NEW_COMPONENT_CREATED=false
CODE_CREATED=false
SCHEMA_CREATED=false
API_CREATED=false
DASHBOARD_CREATED=false
REPOSITORY_CREATED=false
IMPLEMENTATION_AUTHORIZED=false
EXPERIMENT_EXECUTION_AUTHORIZED=false
```

本设计的最小验证逻辑是：

```text
same human
+ fixed cohort
+ comparable tasks
+ native-tool baseline
+ reference-only TITMAS attention support
+ full intervention-cost accounting
+ source-bound evidence
+ no safety or authority regression
-> local management-cost signal
```

在真实对比 Evidence 产生前：

```text
MANAGEMENT_COST_REDUCTION=NOT_YET_DEMONSTRATED
KEEP_AS_EXPERIMENT_DESIGN=true
```
