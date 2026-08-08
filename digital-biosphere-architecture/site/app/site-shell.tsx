import type { Locale } from "./site-content";
import { content } from "./site-content";

export function Brand({ locale }: { locale: Locale }) {
  const brandName = "DCELL";
  const brandDescriptor = locale === "zh" ? "自主 AI 系统可信基础设施研究" : "Trustworthy infrastructure research";

  return (
    <span className="brand" aria-label={`${brandName} · ${brandDescriptor}`}>
      <span className="brand-mark" aria-hidden="true">
        <span className="brand-glyph">D</span>
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
  | "commercial"
  | "commercialEntry";

export function Header({ locale, section = "home", languageHref }: { locale: Locale; section?: SiteSection; languageHref?: string }) {
  const c = content[locale];
  const root = locale === "zh" ? "/" : "/en/";
  const research = locale === "zh" ? "/research/" : "/en/research/";
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
    commercialEntry: ["/en/products/gate/", "/products/gate/"],
  };
  const language = languageHref ?? (locale === "zh" ? languageRoutes[section][0] : languageRoutes[section][1]);

  const nav = (
    <>
      <a href={`${root}#public-evidence`}>{locale === "zh" ? "公开证据" : "Evidence"}</a>
      <a href={`${root}#dcell`}>DCELL</a>
      <a href={research} aria-current={section === "research" || section === "researchIndex" ? "page" : undefined}>{locale === "zh" ? "研究" : "Research"}</a>
      <a href={`${root}#titmas-history`}>{locale === "zh" ? "TITMAS 历史" : "TITMAS history"}</a>
      <a href={`${root}#researcher`}>{locale === "zh" ? "研究者" : "Researcher"}</a>
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
          <p>{locale === "zh" ? "Bin Zhang：为自主 AI 系统构建可信基础设施。DCELL 仅作为 RESEARCH_DIRECTION。" : "Bin Zhang: building trustworthy infrastructure for autonomous AI systems. DCELL is a RESEARCH_DIRECTION only."}</p>
        </div>
        <div>
          <strong>{locale === "zh" ? "研究与证据" : "Research and evidence"}</strong>
          <a href={locale === "zh" ? "/#public-evidence" : "/en/#public-evidence"}>{locale === "zh" ? "公开证据" : "Public evidence"}</a>
          <a href={locale === "zh" ? "/#dcell" : "/en/#dcell"}>DCELL · RESEARCH_DIRECTION</a>
          <a href={locale === "zh" ? "/research/" : "/en/research/"}>{locale === "zh" ? "研究索引" : "Research index"}</a>
          <a href={locale === "zh" ? "/#titmas-history" : "/en/#titmas-history"}>{locale === "zh" ? "TITMAS 工程历史" : "TITMAS engineering history"}</a>
        </div>
        <div>
          <strong>{locale === "zh" ? "机器可读" : "Machine-readable"}</strong>
          <a href="/llms.txt">llms.txt</a>
          <a href="/agent-index.json">agent-index.json</a>
          <a href="/status.json">status.json</a>
        </div>
        <div>
          <strong>{locale === "zh" ? "边界与历史" : "Boundaries and history"}</strong>
          <a href={locale === "zh" ? "/status/" : "/en/status/"}>{locale === "zh" ? "当前状态" : "Current status"}</a>
          <a href={locale === "zh" ? "/community/" : "/en/community/"}>{locale === "zh" ? "历史社区资料" : "Historical community material"}</a>
          <a href="https://github.com/joy7758">GitHub</a>
          <a href="https://orcid.org/0009-0002-8861-1481">ORCID</a>
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
