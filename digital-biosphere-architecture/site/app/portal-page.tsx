import { content, type Locale } from "./site-content";
import { Footer, Header } from "./site-shell";

export function PortalPage({ locale }: { locale: Locale }) {
  const c = content[locale];
  const statusPath = locale === "zh" ? "/status/" : "/en/status/";
  const communityPath = locale === "zh" ? "/community/" : "/en/community/";
  const industriesPath = locale === "zh" ? "/industries/" : "/en/industries/";
  const demoPath = locale === "zh" ? "/digital-cell/" : "/en/digital-cell/";
  const architectureHref =
    "https://github.com/joy7758/digital-biosphere-architecture-specification";

  const structuredData = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    name: "TITMAS Infrastructure Developer Community",
    alternateName: "TITMAS 可信多智能体基础设施开发者社区",
    url: locale === "zh" ? "https://redcrag.cn/" : "https://redcrag.cn/en/",
    inLanguage: c.lang,
    description: c.lead,
    keywords: [
      "AI Agent Infrastructure",
      "Trusted Agent Execution",
      "Verifiable Execution Evidence",
      "Industrial AI Agent Governance",
      "Multi-Agent System Infrastructure",
      "Autonomous Digital Ecosystem",
    ],
    isBasedOn: architectureHref,
  };

  return (
    <div className="site" lang={c.lang}>
      <Header locale={locale} />
      <main>
        <section className="hero simple-hero" data-section-id="hero">
          <div className="hero-grid" aria-hidden="true">
            <div className="orbit orbit-a" />
            <div className="orbit orbit-b" />
            <div className="node node-a" />
            <div className="node node-b" />
            <div className="node node-c" />
          </div>
          <div className="hero-content">
            <div className="hero-badge"><span />{c.badge}</div>
            <p className="eyebrow">
              {locale === "zh"
                ? "TRUST INFRASTRUCTURE / 可信基础设施"
                : "TRUST INFRASTRUCTURE FOR AUTONOMOUS AGENTS"}
            </p>
            <h1>{c.title}</h1>
            <p className="hero-lead">{c.lead}</p>
            <p className="hero-strategy">{c.strategyLine}</p>
            <div className="hero-actions">
              <a className="button button-primary" href="#architecture">{c.primaryCta}</a>
              <a className="button button-secondary" href={demoPath}>{c.secondaryCta}</a>
            </div>
            <a className="truth-notice" href={statusPath}>
              <span>i</span>
              {locale === "zh"
                ? "Developer Preview · 查看当前状态与明确边界"
                : "Developer Preview · View current status and explicit boundaries"}
            </a>
          </div>
        </section>

        <section className="section infrastructure-section" id="architecture" data-section-id="infrastructure">
          <div className="section-shell">
            <div className="section-heading">
              <p className="section-kicker">INFRASTRUCTURE / 基础设施</p>
              <h2>{c.infrastructureTitle}</h2>
              <p>{c.infrastructureLead}</p>
            </div>
            <div className="capability-grid">
              {c.infrastructureCapabilities.map(([name, title, description], index) => (
                <article className="capability-card" key={name}>
                  <div>
                    <span>{String(index + 1).padStart(2, "0")}</span>
                    <code>{name}</code>
                  </div>
                  <h3>{title}</h3>
                  <p>{description}</p>
                </article>
              ))}
            </div>
            <div className="section-links">
              <a href={communityPath}>
                {locale === "zh" ? "查看开发者入口" : "Open the developer entry"} <span>→</span>
              </a>
              <a href={statusPath}>
                {locale === "zh" ? "核对当前状态" : "Check current status"} <span>→</span>
              </a>
            </div>
          </div>
        </section>

        <section className="section industries-section" id="industries" data-section-id="industry-applications">
          <div className="section-shell">
            <div className="section-heading industries-heading">
              <p className="section-kicker">INDUSTRY APPLICATIONS / 行业应用</p>
              <h2>{c.industriesTitle}</h2>
              <p>{c.industriesLead}</p>
            </div>
            <div className="industries-grid">
              <a className="manufacturing-card" href={industriesPath}>
                <span className="industry-label">
                  {locale === "zh" ? "APPLICATION EXAMPLE / 应用示例" : "APPLICATION EXAMPLE"}
                </span>
                <h3>{c.manufacturingTitle}</h3>
                <div className="agent-list">
                  {c.manufacturingAgents.map(([name, description]) => (
                    <div key={name}>
                      <code>{name}</code>
                      <span>{description}</span>
                    </div>
                  ))}
                </div>
                <p>
                  {locale === "zh"
                    ? "这些 Agent 由行业开发者和企业构建。TITMAS 只提供可信基础设施规则。"
                    : "These agents are built by industry developers and enterprises. TITMAS provides trust-infrastructure rules only."}
                </p>
                <strong className="industry-card-link">
                  {locale === "zh" ? "进入制造业应用示例" : "Explore the manufacturing example"}
                  <span>→</span>
                </strong>
              </a>

              <div
                className="ecosystem-stack"
                role="img"
                aria-label={locale === "zh"
                  ? "从行业应用、工业 AI Agent、TITMAS、Agent Framework 与 MCP 到模型、数据和设备的分层关系"
                  : "Layered relationship from industry applications and industrial AI agents through TITMAS, agent frameworks and MCP, to models, data, and devices"}
              >
                {c.stackLabels.map((label, index) => (
                  <div className={index === 2 ? "stack-core" : ""} key={label}>
                    <span>{String(index + 1).padStart(2, "0")}</span>
                    <strong>{label}</strong>
                    {index < c.stackLabels.length - 1 && <i aria-hidden="true">↓</i>}
                  </div>
                ))}
              </div>
            </div>
          </div>
        </section>

        <section className="cell-feature evidence-demo" data-section-id="industrial-agent-evidence-demo">
          <div className="section-shell cell-feature-grid">
            <div className="cell-feature-copy">
              <div className="cell-feature-meta">
                <span>REFERENCE DEMO</span>
                <code>v0.1.0</code>
                <code>REPLAY_PASS</code>
              </div>
              <p className="section-kicker">VERIFIABLE EXECUTION / 可核验执行</p>
              <h2>{c.demoTitle}</h2>
              <p>{c.demoLead}</p>
              <ol className="demo-steps">
                {c.demoSteps.map((step, index) => (
                  <li key={step}>
                    <span>{String(index + 1).padStart(2, "0")}</span>
                    <strong>{step}</strong>
                  </li>
                ))}
              </ol>
              <div className="cell-feature-actions">
                <a className="button cell-feature-primary" href={demoPath}>
                  {locale === "zh" ? "查看 Digital Cell Demo" : "Explore the Digital Cell Demo"}
                  <span>→</span>
                </a>
                <a href={statusPath}>
                  {locale === "zh" ? "查看边界与状态" : "Review boundaries and status"} <span>↗</span>
                </a>
              </div>
              <p className="cell-feature-boundary">{c.demoBoundary}</p>
            </div>
            <a
              className="cell-feature-visual"
              href={demoPath}
              aria-label={locale === "zh" ? "打开 TITMAS Digital Cell Demo" : "Open TITMAS Digital Cell Demo"}
            >
              <img
                src="/digital-cell/digital-cell-architecture.png"
                alt={locale === "zh"
                  ? "Digital Cell v0.1 架构图"
                  : "Digital Cell v0.1 architecture diagram"}
              />
              <span>
                <strong>Digital Cell v0.1</strong>
                <small>Observable · Verifiable · Health-assessable</small>
              </span>
            </a>
          </div>
        </section>
      </main>
      <Footer locale={locale} />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(structuredData) }}
      />
    </div>
  );
}
