import type { Locale } from "./site-content";
import { content } from "./site-content";

export function Brand({ locale }: { locale: Locale }) {
  const brandName = locale === "zh" ? "夏日之海" : "titmas";
  const brandDescriptor = locale === "zh" ? "可信多智能体基础设施" : "Trusted Multi-Agent Infrastructure";

  return (
    <span className="brand" aria-label={`${brandName} · ${brandDescriptor}`}>
      <span className="brand-mark" aria-hidden="true">
        {/* Static export uses the authorized public brand asset without an image-optimization runtime. */}
        {/* eslint-disable-next-line @next/next/no-img-element */}
        <img src="/titmas-logo.png" alt="" width="1024" height="1024" />
      </span>
      <span className="brand-name">
        <strong>{brandName}</strong>
        <small>{brandDescriptor}</small>
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
  | "mediaIndustry"
  | "spaceIndustry"
  | "medical"
  | "mediaDemo"
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
  const languageRoutes: Record<SiteSection, [string, string]> = {
    home: ["/en/", "/"],
    research: ["/en/research/", "/research/"],
    researchIndex: ["/en/research/index/", "/research/index/"],
    applications: ["/en/applications/", "/applications/"],
    demos: ["/en/demos/", "/demos/"],
    industries: ["/en/industries/", "/industries/"],
    medicalIndustry: ["/en/industry/medical-evidence/", "/industry/medical-evidence/"],
    mediaIndustry: ["/en/industry/media-evidence/", "/industry/media-evidence/"],
    spaceIndustry: ["/en/industry/space-agent-evidence/", "/industry/space-agent-evidence/"],
    medical: ["/en/demo/medical-evidence/", "/demo/medical-evidence/"],
    mediaDemo: ["/en/demo/media-evidence/", "/demo/media-evidence/"],
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
      <a href={community} aria-current={section === "community" ? "page" : undefined}>{c.nav.developers}</a>
      <a href={research} aria-current={section === "research" || section === "researchIndex" ? "page" : undefined}>
        {locale === "zh" ? "研究" : "Research"}
      </a>
      <a href={demos} aria-current={section === "demos" || section === "demo" || section === "medical" || section === "mediaDemo" ? "page" : undefined}>
        {locale === "zh" ? "Demo" : "Demos"}
      </a>
      <a href={applications} aria-current={section === "applications" || section === "industries" || section === "medicalIndustry" || section === "mediaIndustry" || section === "spaceIndustry" ? "page" : undefined}>
        {locale === "zh" ? "应用" : "Applications"}
      </a>
      <a href={status}>{c.nav.status}</a>
      <a className="language-link" href={language} hrefLang={locale === "zh" ? "en" : "zh-CN"}>
        {c.nav.language}
      </a>
    </>
  );

  return (
    <>
      <a className="skip-link" href="#main-content">
        {locale === "zh" ? "跳到主要内容" : "Skip to main content"}
      </a>
      <header className="site-header">
        <div className="nav-shell">
          <a className="brand-link" href={root}>
            <Brand locale={locale} />
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
    </>
  );
}

export function Footer({ locale }: { locale: Locale }) {
  const c = content[locale];
  return (
    <footer className="site-footer">
      <div className="footer-grid">
        <div>
          <Brand locale={locale} />
          <p>{c.footer}</p>
        </div>
        <div>
          <strong>{locale === "zh" ? "探索" : "Explore"}</strong>
          <a href={locale === "zh" ? "/research/" : "/en/research/"}>{locale === "zh" ? "研究" : "Research"}</a>
          <a href={locale === "zh" ? "/applications/" : "/en/applications/"}>{locale === "zh" ? "应用" : "Applications"}</a>
          <a href={locale === "zh" ? "/demos/" : "/en/demos/"}>{locale === "zh" ? "参考 Demo" : "Reference demos"}</a>
          <a href={locale === "zh" ? "/commercial-evaluation/" : "/en/commercial-evaluation/"}>
            {locale === "zh" ? "商业评估" : "Commercial evaluation"}
          </a>
          <a href={locale === "zh" ? "/updates/" : "/en/updates/"}>{locale === "zh" ? "更新" : "Updates"}</a>
        </div>
        <div>
          <strong>{locale === "zh" ? "机器可读" : "Machine-readable"}</strong>
          <a href="/llms.txt">llms.txt</a>
          <a href="/agent-index.json">agent-index.json</a>
          <a href="/site-catalog.json">site-catalog.json</a>
          <a href="/updates.json">updates.json</a>
          <a href="/titmas-community.json">titmas-community.json</a>
          <a href="/status.json">status.json</a>
        </div>
        <div>
          <strong>{locale === "zh" ? "治理" : "Governance"}</strong>
          <a href={locale === "zh" ? "/community/" : "/en/community/"}>
            {locale === "zh" ? "社区方向" : "Community direction"}
          </a>
          <a href={locale === "zh" ? "/status/" : "/en/status/"}>{locale === "zh" ? "当前状态" : "Current status"}</a>
          <a href={locale === "zh" ? "/updates/constitution/" : "/en/updates/constitution/"}>
            Website Update Constitution
          </a>
          <a href="/agent-index.json">Agent Index</a>
          <a href="https://github.com/joy7758">{locale === "zh" ? "公开 GitHub Profile" : "Public GitHub profile"}</a>
        </div>
      </div>
      <div className="footer-legal">
        <span>© 2026 山西游骑兵电子商务有限公司</span>
        <span>{c.legal}</span>
      </div>
      <div className="footer-filing">
        <span>{locale === "zh" ? "网站运营主体" : "Website operator"}：山西游骑兵电子商务有限公司</span>
        <strong>晋ICP备2026006409号-1</strong>
        <a href="https://beian.miit.gov.cn" target="_blank" rel="noreferrer">
          工业和信息化部备案管理系统
        </a>
      </div>
    </footer>
  );
}
