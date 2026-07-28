import type { Locale } from "./site-content";
import { Footer, Header } from "./site-shell";

const PRODUCT_OBJECT = "/products/agent-immune.json";
const NPM_URL = "https://www.npmjs.com/package/agent-health";
const REPOSITORY_URL = "https://github.com/joy7758/agent-health";

const copy = {
  zh: {
    home: "TITMAS 首页",
    products: "产品",
    eyebrow: "PRODUCT / 静态仓库健康评估",
    intro: "Agent Immune 是一个 AI Agent 项目静态健康评估工具。",
    scopeNotice: "仅分析仓库静态信号，不提供运行时免疫或持续监控。",
    installTitle: "一次命令，先看清项目健康信号",
    installBody: "在 AI Agent 项目根目录运行。报告保留可检查的诊断路径，不修改项目、不连接生产环境。",
    installLabel: "安装并运行",
    capabilitiesTitle: "从健康结果走到可执行修正",
    capabilitiesLead: "输出不只给出分数，还解释问题、原因、修复方向，以及建议在什么条件下适用。",
    capabilities: [
      ["01", "Health", "汇总仓库中可观察的静态健康信号。"],
      ["02", "Diagnosis", "把信号组织成可检查的诊断结果。"],
      ["03", "Problem / Cause / Fix", "说明发现了什么、可能原因与建议修复方式。"],
      ["04", "Recommendation Applicability", "解释建议为何触发、何时适用，以及何时不适用。"],
    ],
    boundaryEyebrow: "INTERPRETATION BOUNDARY / 解释边界",
    boundaryTitle: "它分析什么，也明确不证明什么",
    includedTitle: "分析范围",
    included: ["仓库中的静态文件与配置信号", "可追溯的健康诊断与修复建议", "建议适用性说明"],
    excludedTitle: "不声称",
    excluded: ["Runtime 监控", "安全认证", "可靠性证明", "合规认证", "部署保证"],
    relationTitle: "产品与 TITMAS 的边界",
    relationBody: "Agent Immune 是 RedCrag 产品目录中的独立工具产品，不是 TITMAS、DBOS 或 SAEE 的核心组件，也不把静态评估结果升级为治理决定或生产证明。",
    npm: "查看 npm",
    repository: "查看源码",
    machine: "机器可读产品对象",
  },
  en: {
    home: "TITMAS home",
    products: "Products",
    eyebrow: "PRODUCT / STATIC REPOSITORY HEALTH ASSESSMENT",
    intro: "Agent Immune is a static health assessment tool for AI Agent projects.",
    scopeNotice: "It analyzes static repository signals only. It does not provide runtime immunity or continuous monitoring.",
    installTitle: "See project health signals with one command",
    installBody: "Run it at the root of an AI Agent project. The report keeps the diagnostic path inspectable without modifying the project or connecting to production.",
    installLabel: "Install and run",
    capabilitiesTitle: "Move from health results to actionable corrections",
    capabilitiesLead: "The output goes beyond a score to explain the problem, likely cause, suggested fix, and when a recommendation does or does not apply.",
    capabilities: [
      ["01", "Health", "Summarizes observable static health signals in the repository."],
      ["02", "Diagnosis", "Organizes signals into an inspectable diagnosis."],
      ["03", "Problem / Cause / Fix", "Explains what was found, the likely cause, and a suggested correction."],
      ["04", "Recommendation Applicability", "Explains why a recommendation triggered, when it applies, and when it does not."],
    ],
    boundaryEyebrow: "INTERPRETATION BOUNDARY",
    boundaryTitle: "What it analyzes—and what it does not prove",
    includedTitle: "Analysis scope",
    included: ["Static files and configuration signals in a repository", "Traceable health diagnoses and correction suggestions", "Recommendation applicability explanations"],
    excludedTitle: "No claim of",
    excluded: ["Runtime monitoring", "Security certification", "Reliability proof", "Compliance certification", "Deployment guarantee"],
    relationTitle: "Product boundary with TITMAS",
    relationBody: "Agent Immune is an independent tool product listed in the RedCrag product catalog. It is not a core TITMAS, DBOS, or SAEE component, and a static assessment does not become a governance decision or production proof.",
    npm: "View on npm",
    repository: "View source",
    machine: "Machine-readable product object",
  },
} as const;

export function AgentImmuneProductPage({ locale }: { locale: Locale }) {
  const c = copy[locale];
  const root = locale === "zh" ? "/" : "/en/";

  return (
    <div className="site product-page" lang={locale === "zh" ? "zh-CN" : "en"}>
      <Header locale={locale} section="product" />
      <main>
        <section className="product-hero">
          <div className="section-shell">
            <nav className="breadcrumb" aria-label={locale === "zh" ? "面包屑导航" : "Breadcrumb"}>
              <a href={root}>{c.home}</a><span>/</span><span>{c.products}</span><span>/</span>
              <span aria-current="page">Agent Immune</span>
            </nav>
            <p className="section-kicker">{c.eyebrow}</p>
            <h1>Agent Immune</h1>
            <p className="product-tagline">Give your AI Agent an Immune System.</p>
            <p className="product-intro">{c.intro}</p>
            <div className="product-scope-notice" role="note">
              <code>STATIC_REPOSITORY_SIGNALS_ONLY</code>
              <strong>{c.scopeNotice}</strong>
            </div>
            <div className="product-actions">
              <a className="button button-primary" href={NPM_URL} target="_blank" rel="noreferrer">{c.npm} ↗</a>
              <a className="button product-button-secondary" href={REPOSITORY_URL} target="_blank" rel="noreferrer">{c.repository} ↗</a>
            </div>
          </div>
        </section>

        <section className="section product-install">
          <div className="section-shell product-install-grid">
            <div>
              <p className="section-kicker">QUICK START</p>
              <h2>{c.installTitle}</h2>
              <p>{c.installBody}</p>
            </div>
            <div className="product-command" aria-label={c.installLabel}>
              <span>{c.installLabel}</span>
              <pre><code>npx agent-health .</code></pre>
              <small>PACKAGE=agent-health · VERSION=0.2.1</small>
            </div>
          </div>
        </section>

        <section className="section product-capabilities">
          <div className="section-shell">
            <div className="section-heading">
              <p className="section-kicker">OUTPUT MODEL</p>
              <h2>{c.capabilitiesTitle}</h2>
              <p>{c.capabilitiesLead}</p>
            </div>
            <div className="product-capability-grid">
              {c.capabilities.map(([number, title, description]) => (
                <article key={number}>
                  <span>{number}</span>
                  <h3>{title}</h3>
                  <p>{description}</p>
                </article>
              ))}
            </div>
          </div>
        </section>

        <section className="section product-boundary">
          <div className="section-shell">
            <p className="section-kicker">{c.boundaryEyebrow}</p>
            <h2>{c.boundaryTitle}</h2>
            <div className="product-boundary-grid">
              <article>
                <strong>{c.includedTitle}</strong>
                <ul>{c.included.map((item) => <li key={item}>{item}</li>)}</ul>
              </article>
              <article>
                <strong>{c.excludedTitle}</strong>
                <ul>{c.excluded.map((item) => <li key={item}>{item}</li>)}</ul>
              </article>
            </div>
            <div className="product-truth-row">
              <code>RUNTIME_MONITORING=false</code>
              <code>SECURITY_CERTIFICATION=false</code>
              <code>RELIABILITY_PROOF=false</code>
              <code>COMPLIANCE_CERTIFICATION=false</code>
              <code>DEPLOYMENT_GUARANTEE=false</code>
            </div>
          </div>
        </section>

        <section className="section product-relation">
          <div className="section-shell product-relation-grid">
            <div>
              <p className="section-kicker">PRODUCT RELATIONSHIP</p>
              <h2>{c.relationTitle}</h2>
              <p>{c.relationBody}</p>
            </div>
            <a href={PRODUCT_OBJECT}>
              <code>agent-immune.json</code>
              <strong>{c.machine} →</strong>
            </a>
          </div>
        </section>
      </main>
      <Footer locale={locale} />
    </div>
  );
}
