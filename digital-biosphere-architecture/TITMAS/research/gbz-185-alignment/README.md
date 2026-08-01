# GB/Z 185《人工智能 智能体互联》与 TITMAS 衔接面 v0.1

```text
MAPPING_STATUS=MAPPING_IMPLEMENTED_LOCAL_VALIDATED
LOCAL_IMPLEMENTATION_VALIDATED=true
GBZ_185_MAPPING_READY_FOR_PUBLICATION=true
GBZ_185_MAPPING_PUBLICLY_DEPLOYED=false
PUBLICATION_AUTHORIZED=false
PUBLIC_LAUNCH_AUTHORIZED=false
GBZ_185_CONFORMANCE_ASSESSED=false
OFFICIAL_AFFILIATION=false
PRODUCTION_READY=false
```

## Standard facts

GB/Z 185.1—185.7 是国家标准化管理部门公开页面登记的现行指导性技术文件，发布日期均为
`2026-05-22`。第8部分“智能体审计”登记号为 `20264195-Z-469`，在本次观察时仍处于
`DRAFTING`。ACPs-community 是公开的协议参考与代码实现来源。本目录不复制标准全文。

## Layered relationship

```text
行业应用和智能体业务逻辑
            ↓
TITMAS 可信执行、授权、证据、验证与审计扩展层
            ↓
GB/Z 185 身份、描述、发现、交互和工具调用基础层
            ↓
智能体框架、模型、运行时、工具、设备和数据
```

> GB/Z 185 规定智能体如何识别、描述、发现、交互和调用工具；TITMAS 研究这些行为如何被授权、记录、转换为证据、验证和审计。

## Part 1—8 mapping

| part | official role | TITMAS relationship | implementation status |
|---|---|---|---|
| 1 总体架构 | 概念模型与功能架构 | `UPPER_LAYER_TRUST_EXTENSION_MAPPING` | `MAPPING_ONLY` |
| 2 身份码 | 身份码及其应用 | `EXTERNAL_IDENTIFIER_REFERENCE` | `MAPPING_ONLY` |
| 3 身份管理 | 身份管理框架与全生命周期 | `LIFECYCLE_AND_EVIDENCE_BOUNDARY_MAPPING` | `MAPPING_ONLY` |
| 4 智能体描述 | 描述方法与注册、变更、发布参考流程 | `DESCRIPTION_EXTENSION_CANDIDATE` | `DESIGN_CANDIDATE` |
| 5 智能体发现 | 智能体发现参考流程 | `DISCOVERY_RESULT_CONSUMER_EXTENSION` | `NOT_IMPLEMENTED` |
| 6 智能体交互 | 交互模式、基础元素与接口 | `PASSIVE_INTERACTION_EVIDENCE_CAPTURE` | `NOT_IMPLEMENTED` |
| 7 智能体工具调用 | 工具调用架构、流程与描述 | `TOOL_INVOCATION_EVIDENCE_EXTENSION` | `PARTIAL_ASSET_EXISTS_NO_GBZ_VALIDATION` |
| 8 智能体审计 | 正在起草的登记项目 | `HIGH_RELEVANCE_AUDIT_RESEARCH_MAPPING` | `RESEARCH_ASSETS_EXIST_NO_STANDARD_CONFORMANCE` |

## Existing TITMAS assets

- 执行记录和 Receipt（执行回执）结构；
- Evidence Object（证据对象）；
- 授权引用与工具调用记录；
- 完整性验证与正负验证思想；
- EEOAP、ARO、Agent Evidence 等研究资产。

这些资产尚未通过 GB/Z 185 映射验证。

## Current gaps

```text
ACPS_ADAPTER_IMPLEMENTED=false
GBZ_185_VERTICAL_SLICE_EXECUTED=false
GBZ_185_CONFORMANCE_CASES_EXECUTED=0
PART8_CONTRIBUTION_SUBMITTED=false
OFFICIAL_REVIEW_RECEIVED=false
STANDARD_ADOPTION_ESTABLISHED=false
```

## Next adapter direction

```text
ACPs leader agent
        ↓
ACPs discovery and interaction
        ↓
ACPs partner agent
        ↓
synthetic tool invocation
        ↓
passive TITMAS adapter
        ↓
EEOAP execution evidence
        ↓
independent verification
```

正常授权调用、缺失授权、身份引用不一致、工具参数被修改、结果替换、事件缺失、时间顺序
异常和证据链无法验证八类场景均为 `DEFINED_NOT_EXECUTED`。

## Non-claims

Conformance ≠ Certification; Reference ≠ Adoption; Mapping ≠ Compliance;
Relevance ≠ Contribution; Contribution ≠ Adoption; Evidence ≠ Truth;
Verification ≠ Authorization; Recommendation ≠ Decision; Decision ≠ Execution.

详见 [`LIMITATIONS.md`](LIMITATIONS.md) 与机器事实源
[`gbz-185-titmas-mapping-v0.1.json`](gbz-185-titmas-mapping-v0.1.json)。

## Provenance

- Observed at: `2026-08-01T19:37:04+08:00`
- Observer: `Codex acting within DBA governance scope`
- Repository commit: `269ab5899047503557f957ba0f7abbd61d8b18d3`
- Official part 1 record: <https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=CFF03D872963466AC7F03ED0E28B6702>
- Official part 8 record: <https://std.samr.gov.cn/gb/search/gbDetailed?id=574304045D075760E06397BE0A0AD7F5>
- ACPs reference implementation: <https://github.com/AIP-PUB/ACPs-community>
