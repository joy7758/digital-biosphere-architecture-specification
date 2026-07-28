import type { Locale } from "./site-content";
import { content } from "./site-content";
import {
  formatUpdateDate,
  getActiveAnnouncement,
  updateCategoryLabels,
} from "./update-content";

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

type SiteSection =
  | "home"
  | "research"
  | "researchIndex"
  | "applications"
  | "demos"
  | "industries"
  | "medicalIndustry"
  | "spaceIndustry"
  | "medical"
  | "demo"
  | "updates"
  | "constitution"
  | "status"
  | "community"
  | "commercial";

export function Header({ locale, section = "home" }: { locale: Locale; section?: SiteSection }) {
  const c = content[locale];
  const root = locale === "zh" ? "/" : "/en/";
  const status = locale === "zh" ? "/status/" : "/en/status/";
  const community = locale === "zh" ? "/community/" : "/en/community/";
  const research = locale === "zh" ? "/research/" : "/en/research/";
  const applications = locale === "zh" ? "/applications/" : "/en/applications/";
  const demos = locale === "zh" ? "/demos/" : "/en/demos/";
  const updates = locale === "zh" ? "/updates/" : "/en/updates/";
  const commercial = locale === "zh" ? "/commercial-evaluation/" : "/en/commercial-evaluation/";
  const languageRoutes: Record<SiteSection, [string, string]> = {
    home: ["/en/", "/"],
    research: ["/en/research/", "/research/"],
    researchIndex: ["/en/research/index/", "/research/index/"],
    applications: ["/en/applications/", "/applications/"],
    demos: ["/en/demos/", "/demos/"],
    industries: ["/en/industries/", "/industries/"],
    medicalIndustry: ["/en/industry/medical-evidence/", "/industry/medical-evidence/"],
    spaceIndustry: ["/en/industry/space-agent-evidence/", "/industry/space-agent-evidence/"],
    medical: ["/en/demo/medical-evidence/", "/demo/medical-evidence/"],
    demo: ["/en/digital-cell/", "/digital-cell/"],
    updates: ["/en/updates/", "/updates/"],
    constitution: ["/en/updates/constitution/", "/updates/constitution/"],
    status: ["/en/status/", "/status/"],
    community: ["/en/community/", "/community/"],
    commercial: ["/en/commercial-evaluation/", "/commercial-evaluation/"],
  };
  const language = locale === "zh" ? languageRoutes[section][0] : languageRoutes[section][1];

  const nav = (
    <>
      <a href={research} aria-current={section === "research" || section === "researchIndex" ? "page" : undefined}>
        {locale === "zh" ? "研究" : "Research"}
      </a>
      <a href={applications} aria-current={section === "applications" || section === "industries" || section === "medicalIndustry" || section === "spaceIndustry" ? "page" : undefined}>
        {locale === "zh" ? "行业应用" : "Applications"}
      </a>
      <a href={demos} aria-current={section === "demos" || section === "demo" || section === "medical" ? "page" : undefined}>
        {locale === "zh" ? "Demo" : "Demos"}
      </a>
      <a href={community} aria-current={section === "community" ? "page" : undefined}>{c.nav.developers}</a>
      <a href={updates} aria-current={section === "updates" || section === "constitution" ? "page" : undefined}>
        {locale === "zh" ? "更新" : "Updates"}
      </a>
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
      <AnnouncementBar locale={locale} />
    </header>
  );
}

function AnnouncementBar({ locale }: { locale: Locale }) {
  const announcement = getActiveAnnouncement();
  if (!announcement) return null;
  const updates = locale === "zh" ? "/updates/" : "/en/updates/";

  return (
    <aside className="announcement-bar" aria-label={locale === "zh" ? "当前公告" : "Current announcement"}>
      <div>
        <a className="announcement-main" href={announcement.href[locale]}>
          <span>{updateCategoryLabels[announcement.category][locale]}</span>
          <time dateTime={announcement.effective_date}>{formatUpdateDate(locale, announcement.effective_date)}</time>
          <strong>{announcement.title[locale]}</strong>
          <i aria-hidden="true">→</i>
        </a>
        <a className="announcement-all" href={updates}>{locale === "zh" ? "全部更新" : "All updates"}</a>
      </div>
    </aside>
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
          <a href="/site-catalog.json">site-catalog.json</a>
          <a href="/space-agent-evidence-profile.json">space-agent-evidence-profile.json</a>
          <a href="/updates.json">updates.json</a>
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
          <a href={locale === "zh" ? "/updates/constitution/" : "/en/updates/constitution/"}>
            Website Update Constitution
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
