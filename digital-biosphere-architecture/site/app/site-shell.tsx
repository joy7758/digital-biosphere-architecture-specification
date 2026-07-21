import type { Locale } from "./site-content";
import { content } from "./site-content";

export function Brand() {
  return (
    <span className="brand" aria-label="Trusted Multi-Agent Infrastructure">
      <span className="brand-mark" aria-hidden="true">
        <i />
        <i />
        <i />
        <i />
      </span>
      <span className="brand-name">
        <strong>TMAI</strong>
        <small>Trustworthy Multi-Agent Infrastructure</small>
      </span>
    </span>
  );
}

export function Header({ locale, section = "home" }: { locale: Locale; section?: "home" | "status" }) {
  const c = content[locale];
  const root = locale === "zh" ? "/" : "/en/";
  const status = locale === "zh" ? "/status/" : "/en/status/";
  const language =
    section === "status"
      ? locale === "zh"
        ? "/en/status/"
        : "/status/"
      : locale === "zh"
        ? "/en/"
        : "/";

  const nav = (
    <>
      <a href={`${root}#architecture`}>{c.nav.architecture}</a>
      <a href={`${root}#trust`}>{c.nav.trust}</a>
      <a href={`${root}#workflow`}>{c.nav.workflow}</a>
      <a href={status}>{c.nav.status}</a>
      <a href={`${root}#developers`}>{c.nav.developers}</a>
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
    </footer>
  );
}
