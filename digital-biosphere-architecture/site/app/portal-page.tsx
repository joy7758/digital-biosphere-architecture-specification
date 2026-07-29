import { content, type Locale } from "./site-content";
import { Footer, Header } from "./site-shell";
import { serializeJsonLd } from "./json-ld";

export function PortalPage({ locale }: { locale: Locale }) {
  const c = content[locale];
  const statusPath = locale === "zh" ? "/status/" : "/en/status/";
  const publicProfileHref = "https://github.com/joy7758";
  const trialInterestHref =
    "https://github.com/joy7758/joy7758/issues/new?template=titmas-private-trial-interest.yml";

  const structuredData = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    name: "TITMAS Infrastructure Developer Community",
    alternateName: "TITMAS 可信多智能体基础设施开发者社区",
    url: locale === "zh" ? "https://redcrag.cn/" : "https://redcrag.cn/en/",
    inLanguage: c.lang,
    description: c.lead,
    isBasedOn: "https://redcrag.cn/llms.txt",
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
              <a
                className="button button-primary"
                href={trialInterestHref}
                target="_blank"
                rel="noreferrer"
              >
                {c.primaryCta}
              </a>
              <a className="button button-secondary" href={statusPath}>{c.secondaryCta}</a>
            </div>
            <div className="trial-meta" aria-label={c.trialMetaLabel}>
              {c.trialMeta.map((item) => <span key={item}>{item}</span>)}
            </div>
            <p className="truth-notice"><span>i</span>{c.notice}</p>
          </div>
        </section>

        <section className="section trial-entry-section" id="trial-entry" data-section-id="trial-entry">
          <div className="section-shell">
            <div className="section-heading">
              <p className="section-kicker">DEVELOPER ENTRY / 开发者入口</p>
              <h2>{c.developerPathTitle}</h2>
              <p>{c.developerPathLead}</p>
            </div>
            <ol className="developer-path" aria-label={c.developerPathTitle}>
              {c.developerPath.map((step, index) => (
                <li key={step}>
                  <span>{String(index + 1).padStart(2, "0")}</span>
                  <strong>{step}</strong>
                </li>
              ))}
            </ol>
            <div className="public-sdk-panel">
              <div>
                <span>PUBLIC-SAFE SDK / 公开安全 SDK</span>
                <h3>{c.publicSdkTitle}</h3>
                <p>{c.publicSdkLead}</p>
                <nav aria-label={c.publicSdkTitle}>
                  {c.publicSdkLinks.map(([label, href]) => (
                    <a href={href} key={href}>{label}<span>→</span></a>
                  ))}
                </nav>
              </div>
              <pre aria-label={c.publicSdkTitle}><code>{c.publicSdkCommands.join("\n")}</code></pre>
            </div>
            <div className="developer-access-grid">
              <article>
                <span>AVAILABLE / 可获得</span>
                <h3>{c.developerGetsTitle}</h3>
                <ul>{c.developerGets.map((item) => <li key={item}>{item}</li>)}</ul>
              </article>
              <article className="developer-access-denied">
                <span>NOT GRANTED / 不授予</span>
                <h3>{c.developerDoesNotGetTitle}</h3>
                <ul>{c.developerDoesNotGet.map((item) => <li key={item}>{item}</li>)}</ul>
              </article>
            </div>
            <p className="trial-disclaimer">{c.trialDisclaimer}</p>
          </div>
        </section>

        <section className="section community-section" id="community" data-section-id="community">
          <div className="section-shell">
            <div className="community-heading">
              <div className="section-heading">
                <p className="section-kicker">COMMUNITY / 开发者社区</p>
                <h2>{c.communityTitle}</h2>
                <p>{c.communityLead}</p>
              </div>
              <blockquote>{c.communityPromise}</blockquote>
            </div>

            <div className="community-surface-grid">
              {c.communitySurfaces.map(([kind, title, description, state]) => (
                <article className="community-surface-card" key={kind}>
                  <div>
                    <span>{kind}</span>
                    <code>{state}</code>
                  </div>
                  <h3>{title}</h3>
                  <p>{description}</p>
                </article>
              ))}
            </div>

            <div className="community-state-heading">
              <h3>{c.communityStateTitle}</h3>
              <p>{c.communityStateLead}</p>
            </div>
            <div className="community-state-grid">
              {c.communityStates.map(([label, state, detail]) => (
                <article key={label}>
                  <span>{label}</span>
                  <strong>{state}</strong>
                  <p>{detail}</p>
                </article>
              ))}
            </div>
            <div className="community-boundaries">
              {c.communityBoundaries.map((boundary) => <code key={boundary}>{boundary}</code>)}
            </div>
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

        <section className="section validation-section" id="validation" data-section-id="validation">
          <div className="section-shell">
            <div className="validation-heading">
              <div className="section-heading">
                <p className="section-kicker">TECHNICAL VALIDATION / 技术验证</p>
                <h2>{c.validationTitle}</h2>
                <p>{c.validationLead}</p>
              </div>
              <div className="validation-question">
                <span>PILOT QUESTION</span>
                <p>{c.validationQuestion}</p>
              </div>
            </div>

            <div className="validation-state-grid">
              {c.validationState.map(([label, state, detail]) => (
                <article key={label}>
                  <span>{label}</span>
                  <strong>{state}</strong>
                  <p>{detail}</p>
                </article>
              ))}
            </div>

            <ol className="validation-flow" aria-label={c.validationTitle}>
              {c.validationFlow.map(([index, owner, title, boundary]) => (
                <li key={index}>
                  <span>{index}</span>
                  <div>
                    <small>{owner}</small>
                    <h3>{title}</h3>
                    <p>{boundary}</p>
                  </div>
                </li>
              ))}
            </ol>

            <div className="validation-boundaries">
              {c.validationBoundaries.map((boundary) => <code key={boundary}>{boundary}</code>)}
            </div>

            <div className="validation-detail-grid">
              <article className="validation-detail">
                <span className="validation-label">SUCCESS CRITERIA</span>
                <h3>{c.validationCriteriaTitle}</h3>
                <ul>
                  {c.validationCriteria.map((item) => <li key={item}>{item}</li>)}
                </ul>
              </article>
              <article className="validation-detail blocker-detail">
                <span className="validation-label">PRE-EXECUTION GATE</span>
                <h3>{c.validationBlockersTitle}</h3>
                <ul>
                  {c.validationBlockers.map((item) => <li key={item}>{item}</li>)}
                </ul>
              </article>
            </div>

            <div className="validation-materials">
              <div className="validation-materials-title">
                <span className="validation-label">DISCLOSURE</span>
                <h3>{c.validationMaterialsTitle}</h3>
              </div>
              <div>
                {c.validationMaterials.map(([artifact, state, detail]) => (
                  <article key={artifact}>
                    <strong>{artifact}</strong>
                    <span>{state}</span>
                    <p>{detail}</p>
                  </article>
                ))}
              </div>
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
            <div className="gate-grid progress-grid">
              {c.progressStates.map(([label, state, detail]) => (
                <article className="gate-card" key={label}>
                  <div>
                    <span className={`state state-${state.toLowerCase().replaceAll(" ", "_")}`}>{state}</span>
                    <code>{label}</code>
                  </div>
                  <p>{detail}</p>
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
                <a href={publicProfileHref}>{c.developerLinks[0]}<span>↗</span></a>
                <a href="/status.json">{c.developerLinks[1]}<span>↗</span></a>
                <a href="/llms.txt">{c.developerLinks[2]}<span>↗</span></a>
                <a href="/agent-customer-package.json">{c.developerLinks[3]}<span>↗</span></a>
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
        dangerouslySetInnerHTML={{ __html: serializeJsonLd(structuredData) }}
      />
    </div>
  );
}
