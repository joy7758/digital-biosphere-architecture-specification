---
id: TITMAS-PROP-20260801-MEDIA-EVIDENCE-001
title: TITMAS Media Evidence Profile Architecture Admission Request v0.1
title_zh: TITMAS 媒体证据场景配置架构接纳请求 v0.1
category: REFERENCE_CANDIDATE
status: DEVELOPMENT_DRAFT
maturity: Development
owner_ref: ZHANGBIN
authority_ref: HUMAN_ARCHITECTURE_DECISION_REQUIRED
version: 0.1.0
normative: false
---

# TITMAS 媒体证据场景配置架构接纳请求 v0.1

## 0. Request status（请求状态）

```text
PROPOSAL_ID=TITMAS-PROP-20260801-MEDIA-EVIDENCE-001
REQUESTED_CLASSIFICATION=APPLICATION_PROFILE_AND_REFERENCE_IMPLEMENTATION_CANDIDATE
ARCHITECTURE_ADMISSION_REQUESTED=true
ARCHITECTURE_ADMISSION_DECIDED=false
PORTFOLIO_ADMISSION_GRANTED=false
CANONICAL_REMOTE_SOURCE_CONFIGURED=false
IMPLEMENTATION_REQUESTED=false
RUNTIME_REQUESTED=false
RELEASE_OR_DEPLOYMENT_REQUESTED=false
NEW_EVIDENCE_AUTHORITY_REQUESTED=false
```

本提案向 Digital Biosphere Architecture（数字生物圈架构）驾驶舱报告
`TITMAS Media Evidence v0.1.0` 的有界进展，并请求把它作为
Application Profile（应用场景配置）和 Reference Implementation（参考实现）候选进入
架构审查。

创建本提案、登记候选、加入待决策队列或打开 Draft PR 都不表示接纳、采用、集成、
标准化、发布授权或生产就绪。

## 1. Main-constitution source lock（主宪法来源锁定）

本提案“拉取主宪法”的含义是读取并锁定驾驶舱的权威来源，不复制或重发第二份宪法。
本轮审查基于驾驶舱 `main` 的以下基线：

```text
COCKPIT_REPOSITORY=joy7758/digital-biosphere-architecture-specification
COCKPIT_BASE_REVISION=f4c9ef81caf889d9cc32b912bc3df0e4e8131056
CONSTITUTION_COPY_CREATED=false
CHILD_CONSTITUTION_AUTHORITY_CREATED=false
```

| Authority source | SHA256 at the base revision | Inherited constraint |
|---|---|---|
| `PROGRAM-CHARTER.md` | `23762cf16ba6785564c62e9d978b882a125e30f42788318610e2eb10064e1dd7` | 驾驶舱只读汇总、子项目事实优先、Agent Absolute Priority（智能体绝对优先）不产生智能体权力 |
| `architecture/open-infrastructure-strategy-constitution.md` | `ca34af2be5152e395454a83a0e9d2f085861497b601e980adee39e0a36113954` | 开放基础设施、简单有界主体组合、应用场景配置不得吞并核心 |
| `architecture/titmas-architecture-charter-v1.0.md` | `966ada93612381052272f6bab963baae74c6102d59b83a50fdc5c04efe6e8234` | `EVIDENCE_NE_TRUTH`、`REFERENCE_IMPLEMENTATION_NE_STANDARD`、`MAPPING_NE_ADOPTION` |

后续若上述文件或 revision 变化，必须重新评估本提案；旧 hash 只证明本轮读取的确切字节，
不创建永久宪法分支。

## 2. Progress report（进展报告）

### 2.1 Canonical implementation snapshot candidate

```text
PROJECT=TITMAS Media Evidence
PROJECT_VERSION=v0.1.0
LOCAL_TAG_COMMIT=7eac452f66a2b7de525543f80b9a7cf1465ef9a1
TAG_TYPE=ANNOTATED
REMOTE_CANONICAL_SOURCE=NOT_CONFIGURED
LICENSE=ALL_RIGHTS_RESERVED_WITH_PRIOR_WRITTEN_AUTHORIZATION_REQUIRED
OBSERVED_AT=2026-08-01
```

`titmas-media-guard` 当前没有配置 Git remote，因此上述本地 tag 和 commit 只能作为
source-pinned local observation（来源锁定的本地观察），尚不能满足驾驶舱 `G1` 的稳定
canonical source（规范事实源）要求。

### 2.2 Verified local implementation evidence

在 2026-08-01 使用仓库规定命令重新执行：

```text
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
RAN=112
RESULT=OK
```

当前本地参考实现覆盖：

- Evidence Object（证据对象）本地结构候选与确定性检查；
- 生成请求、授权记录、智能体执行记录和媒体记录的生命周期引用；
- C2PA、AIGC 检测、水印和人工审核的模拟 Provider Adapter（提供方适配器）；
- 哈希链接链、异议记录、审核决定和来源关联记录；
- 可携带审计包、发布声明、正向用例和失败关闭攻击样例。

这些测试只验证当前本地规则、结构、引用和字节一致性，不验证内容真实、主体身份、
外部授权、法律效力、生产安全、客户采用或外部标准符合性。

### 2.3 Post-tag workspace boundary

实现代码、Schema、Validator、测试和 Demo 相对 `v0.1.0` 没有已观察到的工作区差异；
README、比赛讲解文档和二进制展示资产存在 tag 之后的未提交变化和未跟踪文件。
这些材料不属于本接纳请求的 v0.1.0 实现证据，也不应被驾驶舱汇总为 release、adoption
或 current canonical status。

### 2.4 Existing public reference surface

驾驶舱网站 RC2 已提供本地合成媒体证据介绍、纯前端演示和机器可读场景配置：

```text
SITE_SOURCE_REVISION=800a3523eab8f3f35295207f4df636dbadf347bf
SITE_DEPLOYMENT_REPORT=site/docs/stage23-deployment-report.md
MACHINE_PROFILE=site/public/media-evidence-profile.json
PUBLIC_SURFACE_STATUS=LOCAL_SYNTHETIC_REFERENCE_IMPLEMENTATION
```

公开页面存在不等于项目已经通过架构接纳；本提案用于关闭“展示面先于架构登记”的治理缺口。

## 3. Proposed architecture classification（拟议架构分类）

```text
PRIMARY_RESPONSIBILITY_DOMAIN=AIGC_MEDIA_REVIEW_GOVERNANCE_PROFILE
PORTFOLIO_TIER_REQUESTED=ADJACENT_CANDIDATE
CORE_COMPONENT_REQUESTED=false
DBOS_MODULE_REQUESTED=false
SAEE_MODULE_REQUESTED=false
STANDARD_REQUESTED=false
```

建议把 Media Evidence 归类为面向广播电视和网络视听人工智能生成内容安全的应用场景
配置与参考实现候选。它展示如何组合有来源、可质疑、可复核的记录，但不成为通用证据
权威、运行平台、审核产品或认证系统。

## 4. Evidence-object ownership gap（证据对象所有权缺口）

驾驶舱现有架构规定：

```text
Evidence Material != Evidence Reference
Evidence Reference != DBOS Canonical Evidence Object
DBOS Canonical Evidence Object != Truth
```

Media Evidence v0.1.0 使用 `MediaEvidenceObject` 名称。架构接纳前必须明确：

1. 当前对象是 media-domain evidence-bearing record（媒体域承载证据的记录）和本地参考格式；
2. 它不是 `DBA-ARCHITECTURE-SCHEMA-0.1/EvidenceObject` 或 DBOS canonical Evidence Object；
3. 若未来进入 DBOS，必须经过单独 Evidence Admission Contract（证据准入契约），保留
   source、version、scope、failure 和 conflict；
4. 本提案不修改 Media Evidence Schema，也不授权创建映射实现。

## 5. Scope and non-goals（范围与非目标）

In scope：

- source-pinned progress report；
- 主宪法继承关系；
- `ADJACENT_CANDIDATE` 候选登记；
- 与 DBA、DBOS、Agent Evidence 及外部媒体工具的边界审查；
- G0、G1 和 G2 所需输入的识别。

Out of scope：

- 修改 Media Evidence 的代码、Schema、Validator 或 Demo；
- 把媒体对象提升为 DBOS canonical Evidence Object；
- 创建 API、SDK、Runtime、数据库、区块链、PKI、认证或生产服务；
- 声称替代或符合 C2PA、检测模型、水印、人工审核或平台审核；
- merge、tag、release、deployment、客户交付或比赛提交。

## 6. Dependency and duplicate review（依赖与重复审查）

| Existing surface | Candidate relationship | Duplicate/authority boundary |
|---|---|---|
| DBA | 继承宪法与架构约束，向驾驶舱提供只读状态引用 | DBA 不复制子仓库实现账本，不把展示状态写成项目事实 |
| DBOS Evidence | 未来可能接收媒体记录或引用作为 Evidence Admission 输入 | DBOS 保留 canonical Evidence Object ownership；本提案不创建准入实现 |
| Agent Evidence | 可能提供 execution-to-evidence receipt/reference handoff | Media Evidence 不取得通用 receipt transport 或跨域 Evidence authority |
| C2PA / detectors / watermark | 外部观察来源的模拟适配对象 | Adapter 不替代来源系统，也不把 observation 自动提升为 truth |
| Human review / platform review | 业务决定与人工升级来源 | Decision 是治理动作，不是事实判断或外部授权证明 |

## 7. Recommendation gate（智能体推荐门禁）

在实施本提案前，最高可用的 `qwen3.8-max-preview` 独立审查结果为：

```text
WOULD_RECOMMEND_OPENING_ARCHITECTURE_REVIEW_REQUEST=CONDITIONAL
WOULD_RECOMMEND_FINAL_ADOPTION=false
```

不直接推荐采用的原因：

- implementation repository 没有配置远程 canonical source；
- `MediaEvidenceObject` 与 DBOS canonical Evidence Object 的 ownership/mapping 尚未决策；
- tag 后未提交的比赛材料不能混入 v0.1.0 实现证据；
- 网站展示已存在，但 portfolio、dependency 和 proposal surface 尚未对齐。

本提案把这些原因分解为可审查 gate，不把智能体建议当作架构决定。

应用上述修正并取得驾驶舱 conformance `PASS`、51 项测试 `OK` 后，同一模型的复审结果
仍为 `CONDITIONAL`：该结果支持把有界请求提交给人类架构审查，但不解除远程规范来源和
DBOS Evidence ownership/mapping 两个阻塞项，也不推荐直接采用。

## 8. Gate assessment（闸门评估）

| Gate | Current result | Required remediation |
|---|---|---|
| `G0` Portfolio Admission | `NOT_PASSED` | 确认 owner、许可边界、稳定 project ID 和规范来源 |
| `G1` Source-of-Truth | `BLOCKED_INPUT` | 配置并确认远程 canonical source、status manifest 和 freshness policy |
| `G2` Architecture Contract | `REVIEW_REQUIRED` | 决定媒体记录到 DBOS Evidence Admission 的命名、owner、失败和版本边界 |
| `G3` Interface/Mapping | `NOT_ASSESSED` | 只有 G2 决策后才能准备 mapping；本提案不创建 mapping |
| `G4` Conformance | `NOT_ASSESSED` | 112 tests 不等于跨仓库 conformance |
| `G5` Authorization | `NOT_AUTHORIZED` | 需要独立 Human architecture decision |
| `G6` Execution | `NOT_EXECUTED` | 不在本提案范围 |
| `G7` Evaluation/Adoption | `NOT_ASSESSED` | 无外部采用证据 |
| `G8` Release/Adoption | `NOT_RELEASED_NOT_ADOPTED` | 网站 reference surface 不升级该状态 |

## 9. Required human decisions（所需人工决定）

1. 是否接受 `APPLICATION_PROFILE_AND_REFERENCE_IMPLEMENTATION_CANDIDATE` 分类；
2. 是否把它保留为 `ADJACENT_CANDIDATE`，而不是 DBOS/TITMAS core；
3. 哪个远程仓库与状态文件成为 canonical implementation source；
4. `MediaEvidenceObject` 是否保持 domain-local 名称，或未来通过什么显式 mapping 进入
   DBOS Evidence Admission；
5. 谁负责项目状态刷新、接口维护和冲突处理。

## 10. Outcome record（结果记录）

```yaml
review_result: PENDING
decision_result: NOT_DECIDED
adopted_version: NOT_ASSIGNED
implementation_status: EXISTING_LOCAL_REFERENCE_IMPLEMENTATION_NOT_ADMITTED
conformance_status: LOCAL_TESTS_PASS_CROSS_PROJECT_NOT_EXECUTED
release_status: NOT_RELEASED_BY_THIS_PROPOSAL
known_limitations:
  - REMOTE_CANONICAL_SOURCE_NOT_CONFIGURED
  - DBOS_CANONICAL_EVIDENCE_OBJECT_MAPPING_NOT_DECIDED
  - POST_TAG_COMPETITION_ASSETS_OUTSIDE_V0_1_0
  - NO_EXTERNAL_ADOPTION_OR_CONFORMANCE_EVIDENCE
```

## 11. AI assistance disclosure（人工智能辅助披露）

```text
PRIMARY_AUTHOR_ACCOUNTABILITY=zhangbin
AI_ASSISTANCE=Codex
INDEPENDENT_RECOMMENDATION_GATE=qwen3.8-max-preview
AI_RECOMMENDATION_NE_HUMAN_DECISION=true
```
