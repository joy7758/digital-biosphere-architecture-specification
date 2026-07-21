import { content, gateRows, type Locale } from "./site-content";
import { Footer, Header } from "./site-shell";

export function PortalPage({ locale }: { locale: Locale }) {
  const c = content[locale];
  const statusPath = locale === "zh" ? "/status/" : "/en/status/";
  const architectureHref =
    "https://github.com/joy7758/digital-biosphere-architecture-specification";

  const structuredData = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    name: "Trusted Multi-Agent Infrastructure",
    alternateName: "可信多智能体基础设施",
    url: locale === "zh" ? "https://redcrag.cn/" : "https://redcrag.cn/en/",
    inLanguage: c.lang,
    description: c.lead,
    isBasedOn: architectureHref,
  };

  return (
    <div className="site" lang={c.lang}>
      <Header locale={locale} />
      <main>
        <section className="hero" data-section-id="hero">
          <div className="hero-grid" aria-hidden="true">
            <div className="orbit orbit-a" />
            <div className="orbit orbit-b" />
            <div className="node node-a" />
            <div className="node node-b" />
            <div className="node node-c" />
          </div>
          <div className="hero-content">
            <div className="hero-badge"><span />{c.badge}</div>
            <p className="eyebrow">{c.eyebrow}</p>
            <h1>{c.title}</h1>
            <p className="hero-lead">{c.lead}</p>
            <div className="hero-actions">
              <a className="button button-primary" href="#architecture">{c.primaryCta}</a>
              <a className="button button-secondary" href={statusPath}>{c.secondaryCta}</a>
            </div>
            <p className="truth-notice"><span>i</span>{c.notice}</p>
          </div>
        </section>

        <section className="intro section" data-section-id="intro">
          <div className="section-shell intro-grid">
            <div>
              <p className="section-kicker">WHY / 为什么</p>
              <h2>{c.introTitle}</h2>
            </div>
            <p className="intro-copy">{c.introBody}</p>
          </div>
        </section>

        <section className="section layers-section" id="architecture" data-section-id="architecture">
          <div className="section-shell">
            <div className="section-heading">
              <p className="section-kicker">STACK / 技术栈</p>
              <h2>{c.layersTitle}</h2>
              <p>{c.layersLead}</p>
            </div>
            <div className="layer-stack">
              {c.layers.map((layer) => (
                <article className="layer-card" key={layer.name}>
                  <div className="layer-index">{layer.index}</div>
                  <div className="layer-name">{layer.name}</div>
                  <div className="layer-copy">
                    <span>{layer.tag}</span>
                    <h3>{layer.title}</h3>
                    <p>{layer.body}</p>
                  </div>
                </article>
              ))}
            </div>
          </div>
        </section>

        <section className="section trust-section" id="trust" data-section-id="trust">
          <div className="section-shell">
            <div className="section-heading light">
              <p className="section-kicker">TRUST BOUNDARIES / 可信边界</p>
              <h2>{c.trustTitle}</h2>
              <p>{c.trustLead}</p>
            </div>
            <div className="boundary-grid">
              {c.trustCards.map(([left, right, description], index) => (
                <article className="boundary-card" key={left}>
                  <span className="boundary-number">0{index + 1}</span>
                  <div className="boundary-equation">
                    <strong>{left}</strong><b>≠</b><strong>{right}</strong>
                  </div>
                  <p>{description}</p>
                </article>
              ))}
            </div>
          </div>
        </section>

        <section className="section workflow-section" id="workflow" data-section-id="workflow">
          <div className="section-shell">
            <div className="section-heading">
              <p className="section-kicker">LIFECYCLE / 生命周期</p>
              <h2>{c.workflowTitle}</h2>
              <p>{c.workflowLead}</p>
            </div>
            <ol className="workflow-list">
              {c.workflow.map((step, index) => (
                <li key={step}>
                  <span>{String(index + 1).padStart(2, "0")}</span>
                  <strong>{step}</strong>
                </li>
              ))}
            </ol>
          </div>
        </section>

        <section className="section signals-section" data-section-id="signals">
          <div className="section-shell">
            <div className="section-heading centered">
              <p className="section-kicker">INFRASTRUCTURE / 基础设施</p>
              <h2>{c.signalsTitle}</h2>
            </div>
            <div className="signal-grid">
              {c.signals.map(([name, title, description], index) => (
                <article className="signal-card" key={name}>
                  <div className={`signal-symbol signal-${index + 1}`} aria-hidden="true"><i /><i /><i /></div>
                  <span>{name}</span>
                  <h3>{title}</h3>
                  <p>{description}</p>
                </article>
              ))}
            </div>
          </div>
        </section>

        <section className="section status-section" id="status" data-section-id="status">
          <div className="section-shell">
            <div className="section-heading light">
              <p className="section-kicker">STATUS / 状态</p>
              <h2>{c.statusTitle}</h2>
              <p>{c.statusLead}</p>
            </div>
            <div className="gate-grid">
              {gateRows.map((gate) => (
                <article className="gate-card" key={gate.id}>
                  <div>
                    <span className={`state state-${gate.state.toLowerCase()}`}>{gate.state}</span>
                    <code>{gate.id}</code>
                  </div>
                  <p>{gate[locale]}</p>
                </article>
              ))}
            </div>
            <a className="text-link light-link" href={statusPath}>{c.statusCta}<span>→</span></a>
          </div>
        </section>

        <section className="section developer-section" id="developers" data-section-id="developers">
          <div className="section-shell developer-grid">
            <div>
              <p className="section-kicker">DEVELOPERS / 开发者</p>
              <h2>{c.developersTitle}</h2>
              <p>{c.developersBody}</p>
              <div className="developer-links">
                <a href={architectureHref}>{c.developerLinks[0]}<span>↗</span></a>
                <a href="/status.json">{c.developerLinks[1]}<span>↗</span></a>
                <a href="/llms.txt">{c.developerLinks[2]}<span>↗</span></a>
              </div>
            </div>
            <aside className="governance-card">
              <span className="governance-label">RELEASE GATE</span>
              <h3>{c.governanceTitle}</h3>
              <ul>
                {c.governanceItems.map((item) => <li key={item}>{item}</li>)}
              </ul>
            </aside>
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
