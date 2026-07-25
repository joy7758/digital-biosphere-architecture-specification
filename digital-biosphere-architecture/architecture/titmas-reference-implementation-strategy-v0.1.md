---
document_id: DBA-TITMAS-REFERENCE-IMPLEMENTATION-STRATEGY-0.1
title: TITMAS Reference Implementation Strategy v0.1
title_zh: TITMAS 参考实现战略 v0.1
version: 0.1.0
phase: C3.5
status: reference-implementation-strategy-defined-no-implementation-authorized
maturity: Development
maturity_scope: entire-document
owner_ref: NOT_ASSIGNED
decision_reference: NOT_DECIDED
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Development document; no implementation compatibility claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: non-executable-implementation-boundary-strategy
architecture_domain: TITMAS
document_maturity: Development
reference_implementation_created: false
commercial_implementation_created: false
implementation_authorized: false
release_authorized: false
authority_effect: none
---

# TITMAS Reference Implementation Strategy v0.1

## 1. Purpose and Verdict（目的与结论）

本战略定义未来哪些实现表面可以开放、哪些核心必须保护，以及 Reference Implementation
与 Commercial Implementation 的永久边界。它不创建代码、仓库、SDK、Adapter、Validator
或商业产品。

```text
PHASE=C3_5_REFERENCE_IMPLEMENTATION_STRATEGY
TITMAS_REFERENCE_IMPLEMENTATION_STRATEGY_DEFINED=true
TITMAS_REFERENCE_IMPLEMENTATION_CREATED=false
TITMAS_IMPLEMENTATION_AUTHORIZED=false
```

## 2. Open Candidate Surface（开放候选表面）

| Surface | Purpose | Minimum obligations | Current state |
|---|---|---|---|
| Example | 展示一个对象/失败语义 | synthetic data、exact spec version、non-production label | `NOT_CREATED` |
| SDK | 降低正确构造/解析 contract 的成本 | semantics-preserving、replaceable、fail-closed | `NOT_CREATED` |
| Adapter | 连接外部框架/协议 | passive/read-only default、no-writeback、version binding | `NOT_CREATED` |
| Validator | 拒绝结构或边界错误 | deterministic scope、negative cases、no certification claim | `NOT_CREATED` |
| Test Suite | 提供 conformance fixtures/results | spec/implementation/environment binding、failure retention | `NOT_CREATED` |

开放候选优先遵循 OpenTelemetry 将 Specification、API/SDK 和 optional Contrib 分开的思路；
参考 [OpenTelemetry specification overview](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/overview.md)。
该参考不表示 TITMAS 属于 OpenTelemetry 或已实现运行兼容。

## 3. Protected Surface（保护表面）

以下不因 Open Specification 或 Reference Implementation 自动公开：

- SAEE Core Algorithm；
- Evolution Model、weights、private heuristics 和 training data；
- private/commercial evaluation models；
- customer-specific policies、connectors 和 deployment topology；
- credentials、secrets、PII、客户数据和真实 Evidence；
- enterprise security operations、incident data 和 contractual material；
- DBOS private deployment/source，除非其 Owner 另行发布。

公开 interface envelope 不要求公开内部算法。

## 4. Implementation Class Model（实现类别）

| Class | Definition | May claim | Must not claim |
|---|---|---|---|
| `Toy Example` | 教学性片段或 fixture | demonstrates syntax | conformance、security、support |
| `Local Reference` | 可重复的最小本地实现 | implements declared subset | official/unique implementation |
| `Conformance Fixture` | 用于验证边界的测试对象 | case-bound behavior | customer or production proof |
| `Reference Implementation Candidate` | 经单独授权、维护并声明版本的替换性实现 | declared spec coverage | Stable/production without Decision |
| `Commercial Implementation` | 有服务、合同或企业功能的独立产品表面 | exact available offering facts | ownership of open specification |
| `Production Deployment` | 特定环境的运行实例 | evidence-bound deployment state | universal product readiness |

## 5. Reference vs Commercial Boundary（参考实现与商业实现边界）

| Dimension | Reference Implementation | Commercial Implementation |
|---|---|---|
| Primary purpose | 证明开放 contract 可实现 | 提供部署、运营、支持或企业价值 |
| Required access | 可由开发者读取、替换和复现 | 可包含私有组件和服务 |
| Specification effect | 无；只声明实现版本 | 无；商业需求通过 Proposal 影响规范 |
| Canonical truth | 只拥有自身 source/result | 只拥有自身 product/service facts |
| Support | best-effort 或声明的维护范围 | 可通过独立合同提供 |
| Data | synthetic/public-safe fixtures | 受合同、隐私和安全控制 |
| Conformance | version-bound independent result | 同样需要独立、版本绑定结果 |
| Licensing | 由 exact repository LICENSE 决定 | 独立商业许可/合同，不能重写开放规范 |

```text
REFERENCE_IMPLEMENTATION_NE_SPECIFICATION_AUTHORITY=true
COMMERCIAL_IMPLEMENTATION_NE_OPEN_SPECIFICATION_OWNERSHIP=true
PAYMENT_NE_CERTIFICATION=true
```

## 6. Implementation Declaration Contract（实现声明契约）

未来每项实现至少声明：

```yaml
implementation_id:
implementation_class:
owner_ref:
source_ref:
source_version:
license_ref:
implemented_specification_refs: []
supported: []
partial: []
unsupported: []
unknown: []
security_review_ref:
conformance_result_refs: []
known_limitations: []
release_status:
commercial_availability: NOT_CLAIMED
```

缺失字段按 `UNKNOWN`，不得由 README、测试数量或包版本推断。

## 7. Promotion Gate（推进闸门）

Reference Implementation Candidate 需要：

1. exact Experimental/Candidate specification；
2. Specification Owner 与 Implementation Owner 分离；
3. implementation authorization；
4. license、supply-chain、security 和 vulnerability path；
5. supported/partial/unsupported/unknown 声明；
6. independent conformance plan；
7. lifecycle、maintenance、deprecation 和 archive；
8. Human Architecture Decision。

Production Deployment 或 Commercial Offering 需要额外的产品、服务、安全、法律和发布决定。

## 8. Human Decision Candidate（人工决定候选）

```yaml
decision_id: RI-D01
question: Adopt the open/protected and reference/commercial implementation boundary?
recommended_result: ADOPT_BOUNDARY_ONLY_AFTER_ARCHITECTURE_REVIEW
explicit_non_authorizations:
  - repository_or_code_creation
  - implementation
  - release
  - commercial_offering
decision_status: NOT_DECIDED
```

接受边界战略仍不授权任何具体实现；每个 Example、SDK、Adapter、Validator 和 Test Suite
需要独立 source、Owner、license 和 implementation Decision。

## 9. Final State（最终状态）

```text
TITMAS_REFERENCE_IMPLEMENTATION_STRATEGY_DEFINED=true
TITMAS_OPEN_IMPLEMENTATION_SURFACES_DEFINED=5
TITMAS_PROTECTED_SURFACE_DEFINED=true
TITMAS_REFERENCE_IMPLEMENTATION_CREATED=false
TITMAS_COMMERCIAL_IMPLEMENTATION_CREATED=false
TITMAS_IMPLEMENTATION_AUTHORIZED=false
TITMAS_RELEASE_AUTHORIZED=false
SAEE_PROTECTED_DOMAIN_PRESERVED=true
```
