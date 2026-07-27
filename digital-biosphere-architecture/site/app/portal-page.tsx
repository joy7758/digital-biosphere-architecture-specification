import { communityGateRows, content, type Locale } from "./site-content";
import { Footer, Header } from "./site-shell";

export function PortalPage({ locale }: { locale: Locale }) {
  const c = content[locale];
  const statusPath = locale === "zh" ? "/status/" : "/en/status/";
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
              <a className="button button-primary" href={locale === "zh" ? "/community/" : "/en/community/"}>{c.primaryCta}</a>
              <a className="button button-secondary" href={statusPath}>{c.secondaryCta}</a>
            </div>
            <p className="truth-notice"><span>i</span>{c.notice}</p>
          </div>
        </section>

        <section className="commercial-entry" data-section-id="commercial-evaluation">
          <div className="section-shell commercial-entry-grid">
            <div>
              <div className="commercial-entry-meta">
                <span>REMOTE VALIDATED</span>
                <code>v0.1</code>
                <code>PASS</code>
              </div>
              <p className="section-kicker">COMMERCIAL EVALUATION / 商业评估</p>
              <h2>
                {locale === "zh"
                  ? "10 分钟判断 TITMAS 是否适合你的多智能体系统"
                  : "Evaluate TITMAS for your multi-agent system in 10 minutes"}
              </h2>
              <p>
                {locale === "zh"
                  ? "公开安装、同源合成样例、只读验证和明确边界已经收敛为第一版商业评估包。国内访问者无需跳转 GitHub 即可读取完整材料。"
                  : "Public installation, a same-origin synthetic fixture, read-only validation, and explicit boundaries are now packaged as the first Commercial Evaluation Pack."}
              </p>
              <a className="button button-primary" href={locale === "zh" ? "/commercial-evaluation/" : "/en/commercial-evaluation/"}>
                {locale === "zh" ? "开始商业评估" : "Start evaluation"}
              </a>
            </div>
            <aside className="commercial-entry-truth">
              <span>{locale === "zh" ? "当前真实状态" : "Current truth"}</span>
              <code>PACKAGE_PREPARED=true</code>
              <code>REMOTE_VALIDATED=true</code>
              <code>AVAILABLE_OFFERING=false</code>
              <code>PRODUCTION_READY=false</code>
              <code>CUSTOMERS_VERIFIED=0</code>
            </aside>
          </div>
        </section>

        <section className="cell-feature" data-section-id="digital-cell-demo">
          <div className="section-shell cell-feature-grid">
            <div className="cell-feature-copy">
              <div className="cell-feature-meta">
                <span>REFERENCE DEMO</span>
                <code>v0.1.0</code>
                <code>REPLAY_PASS</code>
              </div>
              <p className="section-kicker">DIGITAL CELL / 数字细胞</p>
              <h2>
                {locale === "zh"
                  ? "让 Agent 的身份、边界与执行历史被看见"
                  : "Make agent identity, boundaries, and execution history visible"}
              </h2>
              <p>
                {locale === "zh"
                  ? "TITMAS Digital Cell Demo 是一个最小参考实现，展示 AI Agent 如何具备 Identity、Boundary、Evidence、Health、Memory 和 Reputation。"
                  : "TITMAS Digital Cell Demo is a minimal reference implementation showing Identity, Boundary, Evidence, Health, Memory, and Reputation around an AI agent."}
              </p>
              <div className="cell-feature-actions">
                <a className="button cell-feature-primary" href="/digital-cell/">
                  {locale === "zh" ? "查看 Digital Cell Demo" : "Explore the Digital Cell Demo"}
                  <span>→</span>
                </a>
                <a href="https://github.com/joy7758/titmas-demo/releases/tag/v0.1.0">
                  GitHub Release <span>↗</span>
                </a>
              </div>
              <p className="cell-feature-boundary">
                {locale === "zh"
                  ? "参考 Demo，不构成生产认证、数字生命或 AI 意识声明。"
                  : "Reference demo only. No production certification, digital-life, or AI-consciousness claim."}
              </p>
            </div>
            <a
              className="cell-feature-visual"
              href="/digital-cell/"
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
              {communityGateRows.map((gate) => (
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
              <p className="section-kicker">AGENTS / 智能体</p>
              <h2>{c.developersTitle}</h2>
              <p>{c.developersBody}</p>
              <div className="developer-links">
                <a href={locale === "zh" ? "/community/" : "/en/community/"}>{c.developerLinks[0]}<span>↗</span></a>
                <a href="/status.json">{c.developerLinks[1]}<span>↗</span></a>
                <a href="/llms.txt">{c.developerLinks[2]}<span>↗</span></a>
                <a href="/titmas-community.json">{c.developerLinks[3]}<span>↗</span></a>
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
