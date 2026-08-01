import mapping from "../public/gbz-185-mapping.json";
import { content, type Locale } from "./site-content";
import { Footer, Header } from "./site-shell";
import { StructuredPageData } from "./structured-page-data";

const copy = {
  zh: {
    title: "GB/Z 185 智能体互联与 TITMAS 可信执行、证据和审计衔接",
    lead: "GB/Z 185 定义智能体如何识别、描述、发现、交互和调用工具。TITMAS 不替代这些基础协议，而研究互联行为如何被授权、记录、验证和审计。",
    factsKicker: "STANDARD FACTS / 标准事实",
    factsTitle: "先区分已发布标准与正在起草的审计项目",
    factsBody: "第1—7部分均为 2026年5月22日发布的现行国家标准化指导性技术文件；第8部分是正在起草的登记项目。这里仅引用公开题录与公开说明，不复制标准全文。",
    currentParts: "第1—7部分",
    current: "现行 · 2026-05-22",
    draftingPart: "第8部分 · 智能体审计",
    drafting: "DRAFTING · 20264195-Z-469",
    layerKicker: "LAYER BOUNDARY / 分层边界",
    layerTitle: "互联基础由 GB/Z 185 定义，TITMAS 只研究上层可信扩展",
    matrixKicker: "PART 1—8 MAPPING / 衔接矩阵",
    matrixTitle: "每一部分的采用、扩展与不重复建设边界",
    part: "部分",
    role: "标准公开角色",
    relationship: "TITMAS 关系",
    implementation: "实现状态",
    assetsKicker: "CURRENT ASSETS / 当前已有资产",
    assetsTitle: "已有表达能力，不等于已经通过 GB/Z 185 验证",
    missingKicker: "NOT COMPLETED / 当前尚未完成",
    missingTitle: "本地映射已验证，但尚未发布、部署或抬升符合性与采纳状态",
    nextKicker: "NEXT VALIDATION SLICE / 下一验证切片",
    nextTitle: "ACPs 被动证据适配路径已定义，但尚未执行",
    scenarios: "正负场景",
    boundaryKicker: "AUTHORITY + TRUTH / 权力和事实边界",
    boundaryTitle: "研究映射不产生认证、官方关系或执行权",
    sourcesKicker: "OFFICIAL SOURCES / 官方来源",
    sourcesTitle: "标准事实只锚定到一手公开来源",
    sourceNote: "机器映射中的 source baseline revision 是编制基线，不是包含该映射的提交；实际部署制品版本由 release.json 的 source_revision 提供。TITMAS 关系是本项目的架构判断，不是标准机构结论。",
    officialRecord: "打开一手来源",
  },
  en: {
    title: "GB/Z 185 Agent Interconnection and TITMAS Trusted Execution, Evidence, and Audit Alignment",
    lead: "GB/Z 185 defines how agents are identified, described, discovered, interact, and invoke tools. TITMAS does not replace these foundation protocols; it researches how interconnection behavior is authorized, recorded, verified, and audited.",
    factsKicker: "STANDARD FACTS",
    factsTitle: "Separate published documents from the drafting audit project",
    factsBody: "Parts 1–7 are current national standardization guidance technical documents published on 22 May 2026. Part 8 is a registered drafting project. This page cites public records and summaries only; it does not reproduce the standard text.",
    currentParts: "Parts 1–7",
    current: "CURRENT · 2026-05-22",
    draftingPart: "Part 8 · Agent audit",
    drafting: "DRAFTING · 20264195-Z-469",
    layerKicker: "LAYER BOUNDARY",
    layerTitle: "GB/Z 185 defines the interconnection foundation; TITMAS only researches a trust extension above it",
    matrixKicker: "PART 1—8 MAPPING",
    matrixTitle: "Adoption, extension, and non-duplication boundaries for every part",
    part: "Part",
    role: "Public standard role",
    relationship: "TITMAS relationship",
    implementation: "Implementation status",
    assetsKicker: "CURRENT ASSETS",
    assetsTitle: "Existing expression capabilities are not GB/Z 185 validation",
    missingKicker: "NOT COMPLETED",
    missingTitle: "The local mapping is validated but not released or deployed, and it elevates no conformance or adoption state",
    nextKicker: "NEXT VALIDATION SLICE",
    nextTitle: "The passive ACPs evidence-adapter path is defined but not executed",
    scenarios: "Positive and negative scenarios",
    boundaryKicker: "AUTHORITY + TRUTH",
    boundaryTitle: "A research mapping creates no certification, official relationship, or execution authority",
    sourcesKicker: "OFFICIAL SOURCES",
    sourcesTitle: "Standard facts are anchored only to primary public sources",
    sourceNote: "The machine mapping's source baseline revision is its preparation baseline, not the commit containing the mapping. release.json source_revision identifies an actual deployed artifact. The TITMAS relationship is this project's architecture judgment, not a standards-body conclusion.",
    officialRecord: "Open primary source",
  },
} as const;

const roles = {
  zh: [
    "互联环境概念模型与功能架构",
    "身份码定义、应用、代码结构与分配原则",
    "身份管理框架、全生命周期与技术要求",
    "描述方法及注册、变更和发布参考流程",
    "智能体发现参考流程",
    "交互模式、基础元素与接口定义",
    "工具调用架构、流程与工具描述",
    "智能体审计登记项目",
  ],
  en: mapping.parts.map((item) => item.standard_role),
} as const;

const assets = {
  zh: ["执行记录和 Receipt 结构", "Evidence Object", "授权引用", "工具调用记录", "完整性验证", "正负验证思想", "EEOAP、ARO 与 Agent Evidence 研究资产"],
  en: mapping.current_assets,
} as const;

const gaps = [
  "ACPS_ADAPTER_IMPLEMENTED=false",
  "GBZ_185_VERTICAL_SLICE_EXECUTED=false",
  "GBZ_185_CONFORMANCE_CASES_EXECUTED=0",
  "PART8_CONTRIBUTION_SUBMITTED=false",
  "OFFICIAL_REVIEW_RECEIVED=false",
  "STANDARD_ADOPTION_ESTABLISHED=false",
];

const equations = [
  "Conformance ≠ Certification",
  "Reference ≠ Adoption",
  "Mapping ≠ Compliance",
  "Relevance ≠ Contribution",
  "Contribution ≠ Adoption",
  "Evidence ≠ Truth",
  "Verification ≠ Authorization",
  "Recommendation ≠ Decision",
  "Decision ≠ Execution",
];

export function Gbz185Page({ locale }: { locale: Locale }) {
  const c = content[locale];
  const t = copy[locale];
  const path = locale === "zh" ? "/standards/gbz-185/" : "/en/standards/gbz-185/";

  return (
    <div className="site gbz-page" lang={c.lang}>
      <Header locale={locale} section="gbz185" />
      <StructuredPageData
        locale={locale}
        path={path}
        title={t.title}
        description={t.lead}
        type="TechArticle"
        dateModified="2026-08-01T19:37:04+08:00"
        isBasedOn={mapping.official_sources.map((source) => source.url)}
      />
      <main id="main-content">
        <header className="gbz-hero">
          <div className="section-shell">
            <p className="section-kicker">GB/Z 185 ALIGNMENT · v0.1</p>
            <h1>{t.title}</h1>
            <p>{t.lead}</p>
            <div className="gbz-status-row" aria-label={locale === "zh" ? "映射状态" : "Mapping status"}>
              <code>LOCAL_IMPLEMENTATION_VALIDATED=true</code>
              <code>GBZ_185_MAPPING_READY_FOR_PUBLICATION=true</code>
              <code>GBZ_185_MAPPING_PUBLICLY_DEPLOYED=false</code>
              <code>PUBLIC_LAUNCH_AUTHORIZED=false</code>
              <code>GBZ_185_CONFORMANCE_ASSESSED=false</code>
              <code>OFFICIAL_AFFILIATION=false</code>
              <code>PRODUCTION_READY=false</code>
            </div>
          </div>
        </header>

        <section className="section gbz-facts">
          <div className="section-shell">
            <div className="section-heading">
              <p className="section-kicker">{t.factsKicker}</p>
              <h2>{t.factsTitle}</h2>
              <p>{t.factsBody}</p>
            </div>
            <div className="gbz-fact-grid">
              <article><span>{t.currentParts}</span><strong>{t.current}</strong><code>GUIDANCE_DOCUMENTS</code></article>
              <article><span>{t.draftingPart}</span><strong>{t.drafting}</strong><code>NOT_PUBLISHED_STANDARD</code></article>
              <article><span>Mapping provenance</span><strong>{mapping.observed_at}</strong><code>{mapping.source_baseline_revision.slice(0, 12)}</code></article>
            </div>
          </div>
        </section>

        <section className="section gbz-layers">
          <div className="section-shell">
            <div className="section-heading">
              <p className="section-kicker">{t.layerKicker}</p>
              <h2>{t.layerTitle}</h2>
            </div>
            <div className="gbz-layer-stack">
              <div>{locale === "zh" ? "行业应用和智能体业务逻辑" : "Industry applications and agent business logic"}</div>
              <div>{locale === "zh" ? "TITMAS 可信执行、授权、证据、验证与审计扩展层" : "TITMAS trusted execution, authorization, evidence, verification, and audit extension"}</div>
              <div>{locale === "zh" ? "GB/Z 185 身份、描述、发现、交互和工具调用基础层" : "GB/Z 185 identity, description, discovery, interaction, and tool-invocation foundation"}</div>
              <div>{locale === "zh" ? "智能体框架、模型、运行时、工具、设备和数据" : "Agent frameworks, models, runtimes, tools, devices, and data"}</div>
            </div>
          </div>
        </section>

        <section className="section gbz-matrix">
          <div className="section-shell">
            <div className="section-heading">
              <p className="section-kicker">{t.matrixKicker}</p>
              <h2>{t.matrixTitle}</h2>
            </div>
            <div className="gbz-table-wrap">
              <table>
                <thead><tr><th>{t.part}</th><th>{t.role}</th><th>{t.relationship}</th><th>{t.implementation}</th></tr></thead>
                <tbody>
                  {mapping.parts.map((item, index) => (
                    <tr key={item.part}>
                      <th scope="row"><span>{item.part}</span><strong>{locale === "zh" ? item.title_zh.replace(/^.*：/, "") : item.title_en.replace(/^.*: /, "")}</strong><small>{item.standard_id}</small></th>
                      <td>{roles[locale][index]}</td>
                      <td><code>{item.titmas_relationship}</code></td>
                      <td><code>{item.implementation_status}</code><small>{item.official_status}</small></td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </section>

        <section className="section gbz-assets">
          <div className="section-shell gbz-two-column">
            <div>
              <p className="section-kicker">{t.assetsKicker}</p>
              <h2>{t.assetsTitle}</h2>
              <ul className="gbz-check-list">{assets[locale].map((asset) => <li key={asset}>{asset}</li>)}</ul>
            </div>
            <aside>
              <p className="section-kicker">{t.missingKicker}</p>
              <h2>{t.missingTitle}</h2>
              <div className="gbz-code-list">{gaps.map((gap) => <code key={gap}>{gap}</code>)}</div>
            </aside>
          </div>
        </section>

        <section className="section gbz-next">
          <div className="section-shell">
            <div className="section-heading">
              <p className="section-kicker">{t.nextKicker}</p>
              <h2>{t.nextTitle}</h2>
            </div>
            <ol className="gbz-flow">{mapping.next_validation_slice.steps.map((step) => <li key={step}><span>{step}</span></li>)}</ol>
            <h3>{t.scenarios} <code>DEFINED_NOT_EXECUTED</code></h3>
            <div className="gbz-scenario-grid">{mapping.next_validation_slice.scenarios.map((scenario) => <article key={scenario.id}><strong>{locale === "zh" ? scenario.title_zh : scenario.id.replaceAll("_", " ")}</strong><code>{scenario.status}</code></article>)}</div>
          </div>
        </section>

        <section className="section gbz-boundaries">
          <div className="section-shell">
            <div className="section-heading">
              <p className="section-kicker">{t.boundaryKicker}</p>
              <h2>{t.boundaryTitle}</h2>
            </div>
            <div className="gbz-equations">{equations.map((equation) => <code key={equation}>{equation}</code>)}</div>
            <div className="gbz-nonclaims">
              <code>TITMAS_REPLACES_GBZ_185=false</code>
              <code>GBZ_185_CERTIFICATION_CLAIM=false</code>
              <code>GBZ_185_ADOPTION_CLAIM=false</code>
              <code>PART8_CONTRIBUTION_SUBMITTED=false</code>
              <code>PUBLICLY_DEPLOYED=false</code>
            </div>
          </div>
        </section>

        <section className="section gbz-sources">
          <div className="section-shell">
            <div className="section-heading">
              <p className="section-kicker">{t.sourcesKicker}</p>
              <h2>{t.sourcesTitle}</h2>
              <p>{t.sourceNote}</p>
            </div>
            <div className="gbz-source-grid">{mapping.official_sources.map((source) => <a href={source.url} key={source.id} target="_blank" rel="noreferrer"><code>{source.id}</code><strong>{source.role.replaceAll("_", " ")}</strong><span>{t.officialRecord} →</span></a>)}</div>
          </div>
        </section>
      </main>
      <Footer locale={locale} />
    </div>
  );
}
