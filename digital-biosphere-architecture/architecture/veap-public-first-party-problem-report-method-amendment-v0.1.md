---
document_id: DBA-TITMAS-VEAP-PUBLIC-FIRST-PARTY-PROBLEM-REPORT-METHOD-AMENDMENT-0.1
title: VEAP Public First-party Problem Report Method Amendment Candidate v0.1
title_zh: VEAP 公开一手问题报告方法修订候选 v0.1
version: 0.1.0
status: development-method-amendment-candidate-agent-review-required
maturity: Development
maturity_scope: entire-document
owner_ref: zhangbin
decision_reference: CS-D02-PRE-06
method_adopted: false
desk_research_execution_authorized: false
public_source_collection_authorized: false
public_source_record_counting_authorized: false
valid_problem_records: 0
cs_g0_pass: false
authority_effect: none
---

# VEAP Public First-party Problem Report Method Amendment Candidate v0.1

## 0. Status（状态）

本文件是对
[VEAP Problem Validation Protocol](veap-problem-validation-protocol-v0.1.md)
Option B 的 Development method amendment candidate（方法修订候选）。

```text
METHOD_CANDIDATE_DEFINED=true
METHOD_ADOPTED=false
DESK_RESEARCH_EXECUTION_AUTHORIZED=false
PUBLIC_SOURCE_COLLECTION_AUTHORIZED=false
PUBLIC_SOURCE_RECORD_COUNTING_AUTHORIZED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
```

本候选只定义未来如何审查公开一手问题报告。它没有搜索、下载、登记、评分或计数任何
issue、incident、Maintainer report、组织、个人或客户材料。

机器契约：

- [method contract](veap-public-first-party-problem-report-method-contract.v0.1.json)；
- [contract Schema](schemas/veap-public-first-party-problem-report-method-contract.schema.v0.1.json)。

## 1. Purpose（目的）

当无法或不应立即外联时，公开一手材料可能帮助判断：真实责任方是否明确报告过与
execution accountability（执行可追责）、lineage（来源链）、replay、failure、
verification 或 cross-framework portability 有关的问题。

该方法不验证：

- 来源方是否知道、支持或采用 TITMAS/VEAP；
- 购买意愿、市场规模或商业承诺；
- VEAP 是否优于现有方案；
- 法律责任、安全、Truth、Certification 或生产就绪。

## 2. First-party Source Definition（一手来源定义）

`PUBLIC_FIRST_PARTY_PROBLEM_REPORT` 必须由对被描述系统、项目、运行流程或事件承担直接
维护、运行、治理或调查责任的主体公开发布，并明确描述自己的问题上下文。

| Source class | Candidate treatment | Examples |
|---|---|---|
| `ELIGIBLE_FIRST_PARTY` | 可以进入字段资格审查 | 官方 issue、Maintainer incident report、项目 postmortem、责任组织技术报告 |
| `PARTIAL_FIRST_PARTY` | 只能形成 `PARTIAL` | 来源为官方，但缺近期实例、workaround、影响、责任角色或日期 |
| `INELIGIBLE_SECONDARY` | 不得映射为问题记录 | 新闻、研究者转述、聚合文章、供应商比较、搜索摘要 |
| `INELIGIBLE_PROMOTIONAL` | 不得映射为问题记录 | 营销案例、产品宣传、无失败语义的成功故事 |
| `INELIGIBLE_GENERATED` | 不得映射为问题记录 | 模型回答、自动摘要、synthetic scenario、persona 或推断 |
| `INELIGIBLE_PRIVATE` | 停止处理 | 泄露材料、私有仓库、未授权 transcript、客户数据或凭据 |

公开网页、GitHub issue 或署名本身不证明来源是一手问题报告。必须确认发布者角色与被描述
系统之间的直接责任关系。

## 3. Required Source Qualification（来源资格要求）

只有同时满足以下字段，未来记录才可以成为 `VALID` candidate：

1. `canonical_public_source_ref`：稳定、可访问的第一方 URL；
2. `source_publisher_ref`：发布项目或组织；
3. `accountable_source_role`：Maintainer、Operator、Incident Owner、Security/Platform
   Owner 等直接责任角色；
4. `published_at` 和 `observed_at`；
5. `recent_example`：具体、可定位且在预先声明窗口内的近期实例；
6. `problem_area`：来源明确表达的问题；
7. `current_workaround`；
8. `workaround_limitations`；
9. `measurable_cost_or_risk`：来源明确说明的时间、失败、运营、安全或审查成本；
10. `priority_basis`：来源明确表达的严重度、阻塞性或优先处理信号；
11. `existing_alternatives`：来源已使用或明确考虑的现有方法；
12. `source_integrity`：内容 hash、抓取时间和来源版本；
13. `independence_basis`；
14. `reviewer_refs` 与 `known_limitations`。

任何字段不得由模型、Reviewer 或 TITMAS 作者猜测补齐。来源未明确表达时使用 `UNKNOWN`，
并使记录保持 `PARTIAL` 或 `INVALID`。

## 4. Problem Record Mapping（问题记录映射）

未来 public-source record 仍映射到既有 Problem Record Contract，但使用以下边界：

| Existing field | Public-source mapping |
|---|---|
| `observer_ref` | 第一方发布者或可归因责任角色引用 |
| `organization_or_context_ref` | 被描述的项目、组织或运行上下文 |
| `human_accountability_ref` | 可核验的来源责任角色，不表示其承担 TITMAS 责任 |
| `consent_reference` | `NOT_APPLICABLE_PUBLIC_SOURCE_USE_BASIS`；公开发布不等于 TITMAS consent |
| `source_record_reference` | canonical URL、版本／时间和 hash |
| `contract_review_interest` | 固定 `NOT_ASKED` |
| `private_demo_review_interest` | 固定 `NOT_ASKED` |
| `commercial_commitment` | 固定 `false` |
| `customer_adoption` | 固定 `false` |

```text
PUBLICATION_NE_CONSENT_TO_TITMAS=true
PUBLIC_REPORT_NE_CUSTOMER=true
PUBLIC_REPORT_NE_ADOPTION=true
SOURCE_PROBLEM_NE_VEAP_FIT=true
```

## 5. Independence and Deduplication（独立性与去重）

- 同一组织、同一项目或同一事件默认最多计一个 context；
- fork、镜像、转载、引用链和相同 postmortem 不增加独立性；
- 同一问题的后续更新必须通过 supersession/lineage 关联；
- 供应商引用客户问题不等于客户第一方报告；
- 多个模型分析同一来源仍然只是一条 source context；
- 作者自己的项目或组织材料必须披露冲突，默认不计独立记录；
- 如果组织关系或来源责任无法验证，记录保持 `PARTIAL`。

## 6. Privacy, Copyright and Source-use Boundary（隐私、版权与来源使用边界）

未来执行若获授权，只允许：

- 公开、无需登录或绕过访问控制即可获得的材料；
- public-safe paraphrase（公开安全释义）；
- 每个来源最多保留一段不超过 25 个英文单词或等量短语的必要短引文；
- 来源 URL、标题、发布者角色、时间、hash 和访问时间；
- 对删除、更新或纠错请求提供可追溯处理路径。

禁止：

- 保存完整文章、完整 issue discussion 或大段受版权保护内容；
- 收集直接标识符、联系方式、credential、私有日志或客户 Evidence；
- 绕过登录、付费墙、robots、访问控制或删除状态；
- 将个人意见扩大为组织立场；
- 将公开发布解释为参与研究、同意联系、客户证言或商标许可。

## 7. Candidate Counting Policy（候选计数策略）

本候选默认：

```text
PUBLIC_SOURCE_VALID_RECORDS_MAX_TOWARD_CS_G0=2
PUBLIC_SOURCE_RECORD_CAN_SATISFY_CONTINUE_REVIEW_INTEREST=false
DIRECT_OR_GOVERNED_RESPONSIBILITY_CONTEXT_STILL_REQUIRED=true
```

理由：

- desk research 可证明公开可见的问题信号，但不能证明当前责任方愿意继续评审；
- 全部五条记录都来自案头研究会把“存在公开问题”误写成“已完成问题验证”；
- 限定最多两条可以补充直接责任记录，而不能替代它们。

该计数策略仍是 review candidate。Agent review、Schema validity 或文件存在均不能使其
自动 adopted，也不能改变 `VALID_PROBLEM_RECORDS=0`。

## 8. Review Lifecycle（审查生命周期）

```text
DISCOVERED
  -> FIRST_PARTY_ROLE_CHECK
  -> SOURCE_AND_VERSION_CHECK
  -> FIELD_EXTRACTION_WITH_UNKNOWN_PRESERVATION
  -> PRIVACY_COPYRIGHT_CLAIM_CHECK
  -> INDEPENDENCE_AND_DEDUPLICATION_CHECK
  -> METHOD_REVIEW
  -> VALID | PARTIAL | INVALID | WITHDRAWN
  -> COUNTING_DECISION | NOT_COUNTED
```

记录创建者不能单独判定自己的记录 `VALID`。至少需要：

- Method review input；
- Claim/Privacy review input；
- Human Decision Owner 对计数的显式决定。

Governed Agent 可以提供前两类 advisory input，但不能成为最终 Human Decision Owner。

## 9. Rejection Rules（拒绝规则）

以下任一条件出现即拒绝计数：

- 非第一方或责任角色不明；
- 没有具体近期实例；
- problem、workaround、limitations、impact 或 priority 由 Reviewer 推断；
- 来源只有对产品、标准或工具的兴趣；
- 同一组织／事件重复；
- 包含私有、泄露、受监管、凭据或不必要个人数据；
- 来源已经删除、无法验证或内容 hash 冲突且无 archive authority；
- 将模型输出、synthetic scenario、搜索摘要或二手报道当作事实来源；
- 试图从公开材料生成 customer、adoption、market、Certification 或 legal claim。

## 10. Adoption and Execution Gates（采纳与执行闸门）

进入方法采纳前至少需要：

1. Method 与 Claim/Privacy Agent review 完成；
2. 必要修正进入文档和机器契约；
3. Human Decision Owner 显式决定采用、退回或拒绝；
4. source collection 的 exact scope、时间、record cap 和 allowed domains；
5. removal/correction path、retention 和 incident route；
6. 独立 record review 与计数 Owner；
7. 失败、`PARTIAL`、`INVALID` 和 negative source 的保留规则。

即使方法未来 adopted，也仍需要单独 execution authorization，才能浏览、收集、登记或计数。

## 11. Current Recommendation（当前推荐）

```text
AGENT_RECOMMENDATION=REVIEW_REQUIRED
RECOMMENDED_AS=FAIL_CLOSED_PUBLIC_FIRST_PARTY_METHOD_CANDIDATE
NOT_RECOMMENDED_AS=DESK_RESEARCH_EXECUTION_OR_MARKET_VALIDATION
```

在 Agent review 完成前，本候选不应进入 adoption decision。

## 12. Non-effects（非效果）

```text
METHOD_ADOPTED=false
DESK_RESEARCH_EXECUTION_AUTHORIZED=false
PUBLIC_SOURCE_COLLECTION_AUTHORIZED=false
PUBLIC_SOURCE_RECORD_COUNTING_AUTHORIZED=false
PROBLEM_VALIDATION_EXECUTION_AUTHORIZED=false
EXTERNAL_OUTREACH_AUTHORIZED=false
DATA_COLLECTION_AUTHORIZED=false
VALID_PROBLEM_RECORDS=0
CS_G0_PASS=false
MARKET_VALIDATION_PASS=false
CUSTOMER_ADOPTION=false

IMPLEMENTATION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```
