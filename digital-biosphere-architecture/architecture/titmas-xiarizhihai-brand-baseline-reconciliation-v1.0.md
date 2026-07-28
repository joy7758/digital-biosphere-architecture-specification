---
document_id: DBA-TITMAS-XRZH-BRAND-BASELINE-1.0
title: TITMAS and Xiarizhihai Brand Baseline Reconciliation v1.0
title_zh: TITMAS 与夏日之海品牌基线核对 v1.0
status: accepted-brand-reconciliation-design
maturity: Development
owner_ref: zhangbin
direction_reference: USER_DIRECTION_2026-07-29_RETAIN_TITMAS_ENGLISH_NAME
source_revision: 57ca5c1e22815fe1640b72a69f41d54d9f746db5
authority_effect: none
implementation_effect: none
---

# TITMAS 与夏日之海品牌基线核对 v1.0

## 1. Current Human Owner direction

附件中的 `SUMMERSEA-BRAND-DIRECTION-D01` 原拟使用 `SummerSea` 作为英文名。Human
Owner 随后明确：

> 放弃 SummerSea 这个英文名，英文还是 TITMAS。

因此，原方向中的英文名称部分被后续指令覆盖；项目连续性、不得创建新项目、不得改变
Authority / Capability / Runtime / Schema / API 等边界继续有效。

```text
CHINESE_MASTER_BRAND=夏日之海
ENGLISH_MASTER_BRAND=TITMAS
SUMMERSEA_ACTIVE_NAME=false
TITMAS_TECHNICAL_IDENTITY_PRESERVED=true
```

中英文名是 parallel bilingual names（并行双语名称），不是逐字翻译关系。

## 2. Verified baseline

- source branch：`origin/codex/titmas-agent-native-standards-community-v1-1`；
- source revision：`57ca5c1e22815fe1640b72a69f41d54d9f746db5`；
- `agent-index.json` 是唯一 canonical machine entry（规范机器入口）；
- `TITMAS/README.md` 是既有开发者入口，`llms.txt` 指向机器入口；
- 基线不存在 `README.zh-CN.md`，本任务记录为 `MISSING`，不虚构既有文件；
- 实际 community、specification、conformance、reference 和 adapter 路径位于
  `TITMAS/` 下，不存在同名根目录。

包含 TITMAS 文本的受 Git 跟踪文件分布：

| Location | Matching tracked files | Type |
|---|---:|---|
| `README.md` | 1 | 人类项目与品牌入口 |
| `architecture/` | 270 | 规范、ADR、决策和历史记录 |
| `TITMAS/community/` | 8 | 兼容贡献与治理入口 |
| `TITMAS/conformance/` | 8 | 符合性工具和报告 |
| `TITMAS/reference/` | 5 | 非权威参考实现 |
| `TITMAS/adapters/` | 2 | Adapter 契约与模板 |
| `TITMAS/` other | 58 | 规范、智能体原生、试点与评审材料 |
| `agent-index.json` / `llms.txt` | 2 | 机器发现入口与指针 |

数字表示包含字符串的 tracked file 数，不是采用、社区或能力事实。

## 3. Classification and treatment

| Location | Current identity | Type | Treatment |
|---|---|---|---|
| `README.md` | TITMAS | 品牌入口 | 增加“夏日之海 / TITMAS”映射 |
| `TITMAS/README.md` | TITMAS | 开发者入口 | 增加中文品牌说明；路径不改 |
| `agent-index.json` | TITMAS | 唯一机器入口 | 增加双语品牌投影引用 |
| `llms.txt` | TITMAS | 发现指针 | 增加中文名与弃用名说明 |
| Schema / API / CLI / package | TITMAS | 技术标识 | 不修改 |
| TITMAS specification IDs | TITMAS | 规范标识 | 保留 |
| ADR / Decision / Report | TITMAS | 历史记录 | 原文保留 |
| Git history / citations | TITMAS | 来源连续性 | 保留 |
| SummerSea | proposed only | 已放弃候选名 | 不作为活动名称 |

## 4. Result

保持英文名 `TITMAS` 避免了 repository、path、Schema、API、CLI、package 与规范 ID
层面的迁移。当前工作仅为中文品牌映射和机器可发现元数据设计。

```text
BRAND_CHANGE_NE_PROJECT_CREATION=true
BRAND_CHANGE_NE_ARCHITECTURE_CHANGE=true
BRAND_CHANGE_NE_OWNERSHIP_CHANGE=true
BRAND_CHANGE_NE_AUTHORITY_CHANGE=true
BRAND_CHANGE_NE_CAPABILITY_CHANGE=true
TITMAS_HISTORY_PRESERVED=true
TITMAS_REFERENCES_VALID=true
OLD_DOCUMENTS_NOT_REWRITTEN=true
```
