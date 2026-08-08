import { content, type Locale } from "./site-content";
import { directoryItems, type PublicDirectory } from "./site-directory";
import { Footer, Header } from "./site-shell";
import { StructuredPageData } from "./structured-page-data";

const copy = {
  zh: {
    research: {
      eyebrow: "RESEARCH / 研究",
      title: "DCELL：自主 AI 系统的可信基础设施研究",
      lead: "研究聚焦 agents、infrastructure、environments 与 evaluations，探索自主实验循环如何保留来源、身份、边界、失败和经验连续性。DCELL 始终标注为 RESEARCH_DIRECTION。",
      current: "研究",
      indexLabel: "研究索引",
    },
    applications: {
      eyebrow: "APPLICATIONS / 行业应用",
      title: "可信基础设施如何进入行业",
      lead: "行业应用说明 TITMAS 解决哪些问题、由谁实现业务逻辑，以及基础设施与行业软件之间的边界。",
      current: "行业应用",
      indexLabel: "已发布应用方向",
    },
    demos: {
      eyebrow: "DEMOS / 参考演示",
      title: "用可检查的演示理解基础设施",
      lead: "Demo 展示可运行或可交互的参考路径，并显式标注数据、验证、生产与权力边界。",
      current: "Demo",
      indexLabel: "已发布 Demo",
    },
    home: "DCELL 研究首页",
    overview: "Overview",
    index: "Index",
    open: "打开",
    machine: "机器目录",
    researchPillars: [
      ["01", "Agents", "研究可独立识别、可评价且行动有界的 Agent。"],
      ["02", "Infrastructure & Environments", "让执行环境生成可验证、可复现的来源记录。"],
      ["03", "Evaluations", "评价保持只读建议边界，不自动成为授权或执行。"],
    ],
    evidenceTitle: "执行证据是自主实验循环的共同基础",
    evidenceBody: "不同 Agent 与环境可以使用不同工具，但都需要保留来源、过程、完整性、验证、失败和权限边界。公开仓库支持有限工程结论，不证明完整 DCELL 系统或自主演化已经实现。",
    evidenceRules: ["Evidence ≠ Truth", "Evaluation ≠ Authority", "Recommendation ≠ Decision", "Decision ≠ Execution"],
  },
  en: {
    research: {
      eyebrow: "RESEARCH",
      title: "DCELL: trustworthy-infrastructure research for autonomous AI systems",
      lead: "The work focuses on agents, infrastructure, environments, and evaluations, asking how autonomous experimental loops can retain provenance, identity, boundaries, failure, and experience continuity. DCELL remains a RESEARCH_DIRECTION.",
      current: "Research",
      indexLabel: "Research index",
    },
    applications: {
      eyebrow: "APPLICATIONS",
      title: "How trust infrastructure enters industries",
      lead: "Applications explain the problem, who owns the business logic, and the boundary between infrastructure and industry software.",
      current: "Applications",
      indexLabel: "Published application directions",
    },
    demos: {
      eyebrow: "DEMOS",
      title: "Understand the infrastructure through inspectable demos",
      lead: "Demos expose runnable or interactive reference paths with explicit data, validation, production, and authority boundaries.",
      current: "Demos",
      indexLabel: "Published demos",
    },
    home: "DCELL research home",
    overview: "Overview",
    index: "Index",
    open: "Open",
    machine: "Machine catalog",
    researchPillars: [
      ["01", "Agents", "Independently identifiable, evaluable agents with bounded actions."],
      ["02", "Infrastructure & Environments", "Execution environments that produce verifiable, reproducible provenance records."],
      ["03", "Evaluations", "Read-only recommendations that do not automatically become authorization or execution."],
    ],
    evidenceTitle: "Execution evidence is shared infrastructure for autonomous experimental loops",
    evidenceBody: "Agents and environments may use different tools, but all need provenance, process, integrity, verification, failure retention, and permission boundaries. Public repositories support bounded engineering claims; they do not establish a complete DCELL system or achieved autonomous evolution.",
    evidenceRules: ["Evidence ≠ Truth", "Evaluation ≠ Authority", "Recommendation ≠ Decision", "Decision ≠ Execution"],
  },
} as const;

function sectionName(section: PublicDirectory) {
  return section === "research" ? "research" : section;
}

export function DirectoryPage({
  locale,
  section,
  indexOnly = false,
}: {
  locale: Locale;
  section: PublicDirectory;
  indexOnly?: boolean;
}) {
  const c = content[locale];
  const t = copy[locale];
  const sectionCopy = t[section];
  const root = locale === "zh" ? "/" : "/en/";
  const overview = locale === "zh" ? `/${section}/` : `/en/${section}/`;
  const index = section === "research"
    ? (locale === "zh" ? "/research/index/" : "/en/research/index/")
    : `${overview}#index`;
  const pagePath = indexOnly ? index : overview;
  const pageTitle = indexOnly ? sectionCopy.indexLabel : sectionCopy.title;

  return (
    <div className="site directory-page" lang={c.lang}>
      <Header locale={locale} section={section === "research" && indexOnly ? "researchIndex" : sectionName(section)} />
      <StructuredPageData
        locale={locale}
        path={pagePath}
        title={pageTitle}
        description={sectionCopy.lead}
        type="CollectionPage"
      />
      <main id="main-content">
        <section className="directory-hero">
          <div className="section-shell">
            <nav className="breadcrumb" aria-label={locale === "zh" ? "面包屑导航" : "Breadcrumb"}>
              <a href={root}>{t.home}</a><span>/</span><span aria-current="page">{sectionCopy.current}</span>
            </nav>
            <p className="section-kicker">{sectionCopy.eyebrow}</p>
            <h1>{indexOnly ? sectionCopy.indexLabel : sectionCopy.title}</h1>
            <p>{sectionCopy.lead}</p>
            <nav className="directory-tabs" aria-label={locale === "zh" ? "页面分区" : "Page sections"}>
              <a href={overview} aria-current={!indexOnly ? "page" : undefined}>{t.overview}</a>
              <a href={index} aria-current={indexOnly ? "page" : undefined}>{t.index}</a>
              <a href="/site-catalog.json">{t.machine}</a>
            </nav>
          </div>
        </section>

        {section === "research" && !indexOnly && (
          <>
            <section className="section directory-pillars">
              <div className="section-shell">
                <div className="directory-pillar-grid">
                  {t.researchPillars.map(([number, title, description]) => (
                    <article key={number}>
                      <span>{number}</span><h2>{title}</h2><p>{description}</p>
                    </article>
                  ))}
                </div>
              </div>
            </section>
            <section className="section evidence-governance" id="evidence-governance">
              <div className="section-shell evidence-governance-grid">
                <div>
                  <p className="section-kicker">EVIDENCE GOVERNANCE</p>
                  <h2>{t.evidenceTitle}</h2>
                  <p>{t.evidenceBody}</p>
                </div>
                <div className="evidence-rule-list">
                  {t.evidenceRules.map((rule) => <code key={rule}>{rule}</code>)}
                </div>
              </div>
            </section>
          </>
        )}

        <section className="section directory-index" id="index">
          <div className="section-shell">
            <div className="section-heading">
              <p className="section-kicker">PUBLISHED INDEX</p>
              <h2>{sectionCopy.indexLabel}</h2>
            </div>
            <div className="directory-list">
              {directoryItems[section].map((item, itemIndex) => (
                <a id={item.id} href={item.href[locale]} key={item.id}>
                  <span>{String(itemIndex + 1).padStart(2, "0")}</span>
                  <div>
                    <div className="directory-item-meta">
                      <code>{item.type}</code><b>{item.status}</b>
                    </div>
                    <h3>{item.title[locale]}</h3>
                    <p>{item.description[locale]}</p>
                    <small>{item.metadata.join(" · ")}</small>
                  </div>
                  <strong>{t.open} ↗</strong>
                </a>
              ))}
            </div>
          </div>
        </section>
      </main>
      <Footer locale={locale} />
    </div>
  );
}
