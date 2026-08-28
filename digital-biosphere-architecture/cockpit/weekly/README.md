# DBA Weekly Cockpit v0.1

DBA 周检驾驶舱是张斌本人使用的内部只读原型。它先发现信号，再核验来源，最后生成通俗中文页面。页面不是事实源，也不授予任何项目执行权限。

## Discovery First

Discovery 只表示“发现了候选”。候选必须经过 Evidence Admission，且只有人工批准登记后才能成为 Monitored。发现不等于准入、建议、授权或整改。

## 多个小 Cell

12 个逻辑 Cell 在同一 Python 进程中运行。每个 Cell 只有一个职责、一个 Manifest 和一个可替换接口。某个 Cell 失败时，协调细胞记录 NOT_ASSESSED，并继续调用其他 Cell。三个发现 Cell 全部失败时，整体状态为 DISCOVERY_UNAVAILABLE。

## 职责边界

驾驶舱只观察、比较、解释、记忆和交接。它不修改来源项目，不创建 PR，不合并，不部署，不授权，不关闭问题，也不改变项目优先级。

## 本地生成候选页面

在 digital-biosphere-architecture 目录运行：

    python3 cockpit/weekly/run_weekly.py --demo --output-dir cockpit/weekly/demo

直接双击 cockpit/weekly/demo/dashboard.html 即可查看。页面不需要服务器、不访问外网、不加载 CDN 或外部字体。

## 测试

    python3 -m unittest discover -s cockpit/weekly/tests -v

## 人工工作流

在 GitHub Actions 中选择 DBA Weekly Cockpit Candidate，点击 Run workflow。人工触发始终允许生成候选制品包，工作流只拥有 read 权限。

## 为什么默认不启用定时运行

定时任务只有在仓库变量 DBA_WEEKLY_COCKPIT_ENABLED 精确等于 true 时才运行完整周检。原型不创建或修改该变量，因此默认只输出“定时周检未启用”。

## 为什么没有自动修复

Observation 不等于 Authorization，Recommendation 不等于 Command。周检只生成发现和交接包，自动修复会破坏项目仓库自身的责任与授权链。

## 为什么界面不是事实源

页面由 weekly snapshot 派生。任何结论都必须保留 source_reference、observed_at、freshness 和 authority boundary。界面只负责翻译，不创造新事实。

## 增加或替换只读 Cell

在 cells 中实现单一职责类，在 cell-registry.json 登记并创建 Manifest。所有写入、PR、合并、部署和授权能力必须为 false。替换时保持 interface_version 0.1、输入输出契约和 replacement_contract，不要求其他 Cell 共用内部状态。
