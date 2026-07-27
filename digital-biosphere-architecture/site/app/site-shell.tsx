import type { Locale } from "./site-content";
import { content } from "./site-content";

export function Brand() {
  return (
    <span className="brand" aria-label="TITMAS Infrastructure Developer Community">
      <span className="brand-mark" aria-hidden="true">
        <i />
        <i />
        <i />
        <i />
      </span>
      <span className="brand-name">
        <strong>TITMAS</strong>
        <small>Infrastructure Developer Community</small>
      </span>
    </span>
  );
}

type SiteSection = "home" | "industries" | "demo" | "status" | "community" | "commercial";

export function Header({ locale, section = "home" }: { locale: Locale; section?: SiteSection }) {
  const c = content[locale];
  const root = locale === "zh" ? "/" : "/en/";
  const status = locale === "zh" ? "/status/" : "/en/status/";
  const community = locale === "zh" ? "/community/" : "/en/community/";
  const industries = locale === "zh" ? "/industries/" : "/en/industries/";
  const demo = locale === "zh" ? "/digital-cell/" : "/en/digital-cell/";
  const commercial = locale === "zh" ? "/commercial-evaluation/" : "/en/commercial-evaluation/";
  const languageRoutes: Record<SiteSection, [string, string]> = {
    home: ["/en/", "/"],
    industries: ["/en/industries/", "/industries/"],
    demo: ["/en/digital-cell/", "/digital-cell/"],
    status: ["/en/status/", "/status/"],
    community: ["/en/community/", "/community/"],
    commercial: ["/en/commercial-evaluation/", "/commercial-evaluation/"],
  };
  const language = locale === "zh" ? languageRoutes[section][0] : languageRoutes[section][1];

  const nav = (
    <>
      <a href={`${root}#architecture`}>{c.nav.architecture}</a>
      <a href={industries} aria-current={section === "industries" ? "page" : undefined}>{c.nav.workflow}</a>
      <a href={demo} aria-current={section === "demo" ? "page" : undefined}>{c.nav.demo}</a>
      <a href={community}>{c.nav.developers}</a>
      <a href={commercial} aria-current={section === "commercial" ? "page" : undefined}>
        {locale === "zh" ? "商业评估" : "Evaluation"}
      </a>
      <a href={status}>{c.nav.status}</a>
      <a
        href="https://github.com/joy7758/digital-biosphere-architecture-specification"
        target="_blank"
        rel="noreferrer"
      >
        {c.nav.github}
      </a>
      <a className="language-link" href={language} hrefLang={locale === "zh" ? "en" : "zh-CN"}>
        {c.nav.language}
      </a>
    </>
  );

  return (
    <header className="site-header">
      <div className="nav-shell">
        <a className="brand-link" href={root}>
          <Brand />
        </a>
        <nav className="desktop-nav" aria-label={locale === "zh" ? "主导航" : "Primary navigation"}>
          {nav}
        </nav>
        <details className="mobile-nav">
          <summary aria-label={locale === "zh" ? "打开导航" : "Open navigation"}>
            <span />
            <span />
            <span />
          </summary>
          <nav aria-label={locale === "zh" ? "移动导航" : "Mobile navigation"}>{nav}</nav>
        </details>
      </div>
    </header>
  );
}

export function Footer({ locale }: { locale: Locale }) {
  const c = content[locale];
  return (
    <footer className="site-footer">
      <div className="footer-grid">
        <div>
          <Brand />
          <p>{c.footer}</p>
        </div>
        <div>
          <strong>{locale === "zh" ? "机器可读" : "Machine-readable"}</strong>
          <a href="/llms.txt">llms.txt</a>
          <a href="/agent-index.json">agent-index.json</a>
          <a href="/status.json">status.json</a>
          <a href="/titmas-community.json">titmas-community.json</a>
          <a href="/TITMAS-COMMERCIAL-EVALUATION-PACK-v0.2.json">commercial-evaluation-pack.json</a>
        </div>
        <div>
          <strong>{locale === "zh" ? "治理" : "Governance"}</strong>
          <a href="https://github.com/joy7758/digital-biosphere-architecture-specification/blob/main/PROGRAM-CHARTER.md">
            Program Charter
          </a>
          <a href="https://github.com/joy7758/digital-biosphere-architecture-specification/blob/main/DECISION-QUEUE.md">
            Decision Queue
          </a>
          <a href="https://github.com/joy7758/digital-biosphere-architecture-specification/blob/main/CLEAN-CLONE-VALIDATION-REPORT.md">
            Validation Report
          </a>
        </div>
      </div>
      <div className="footer-legal">
        <span>© 2026 Digital Biosphere Architecture</span>
        <span>{c.legal}</span>
      </div>
      <div className="footer-filing">
        <a href="https://beian.miit.gov.cn/" target="_blank" rel="noreferrer">
          晋ICP备2026006409号-1
        </a>
      </div>
    </footer>
  );
}
