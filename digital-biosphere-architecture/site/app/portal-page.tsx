import { HeroCarousel } from "./components/hero-carousel";
import { content, type Locale } from "./site-content";
import { Footer, Header } from "./site-shell";
import { serializeJsonLd } from "./json-ld";

export function PortalPage({ locale }: { locale: Locale }) {
  const c = content[locale];
  const paths = {
    research: locale === "zh" ? "/research/" : "/en/research/",
    applications: locale === "zh" ? "/applications/" : "/en/applications/",
    demos: locale === "zh" ? "/demos/" : "/en/demos/",
    community: locale === "zh" ? "/community/" : "/en/community/",
    status: locale === "zh" ? "/status/" : "/en/status/",
    commercial: locale === "zh" ? "/commercial-evaluation/" : "/en/commercial-evaluation/",
    mediaIndustry: locale === "zh" ? "/industry/media-evidence/" : "/en/industry/media-evidence/",
    mediaDemo: locale === "zh" ? "/demo/media-evidence/" : "/en/demo/media-evidence/",
    medicalIndustry: locale === "zh" ? "/industry/medical-evidence/" : "/en/industry/medical-evidence/",
    medicalDemo: locale === "zh" ? "/demo/medical-evidence/" : "/en/demo/medical-evidence/",
    digitalCell: locale === "zh" ? "/digital-cell/" : "/en/digital-cell/",
    gbz185: locale === "zh" ? "/standards/gbz-185/" : "/en/standards/gbz-185/",
  };

  const humanEntries = [
    [locale === "zh" ? "研究" : "Research", locale === "zh" ? "方向、架构与证据治理" : "Directions, architecture, and evidence governance", paths.research],
    [locale === "zh" ? "行业应用" : "Applications", locale === "zh" ? "基础设施如何进入行业" : "How infrastructure enters industries", paths.applications],
    [locale === "zh" ? "参考演示" : "Reference demos", locale === "zh" ? "可检查的合成参考路径" : "Inspectable synthetic reference paths", paths.demos],
    [locale === "zh" ? "开发者与社区" : "Developers and community", locale === "zh" ? "规范、边界与贡献入口" : "Specifications, boundaries, and contribution entry", paths.community],
  ];

  const machineEntries = [
    ["llms.txt", locale === "zh" ? "快速理解与能力边界" : "Fast orientation and boundaries", "/llms.txt"],
    ["agent-index.json", locale === "zh" ? "完整智能体发现索引" : "Complete agent discovery index", "/agent-index.json"],
    ["site-catalog.json", locale === "zh" ? "页面、行业与演示目录" : "Pages, applications, and demos", "/site-catalog.json"],
    ["media-evidence-profile.json", locale === "zh" ? "媒体证据机器可读场景配置" : "Machine-readable media evidence profile", "/media-evidence-profile.json"],
    ["gbz-185-mapping.json", locale === "zh" ? "GB/Z 185 与 TITMAS 机器可读衔接矩阵" : "Machine-readable GB/Z 185 and TITMAS mapping", "/gbz-185-mapping.json"],
  ];

  const structuredData = {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Organization",
        "@id": "https://redcrag.cn/#organization",
        name: "山西游骑兵电子商务有限公司",
        legalName: "山西游骑兵电子商务有限公司",
        alternateName: ["夏日之海", "TITMAS"],
        url: "https://redcrag.cn/",
      },
      {
        "@type": "WebSite",
        "@id": "https://redcrag.cn/#website",
        name: "山西游骑兵电子商务有限公司",
        alternateName: ["夏日之海", "TITMAS"],
        url: "https://redcrag.cn/",
        inLanguage: ["zh-CN", "en"],
        description: c.lead,
        publisher: { "@id": "https://redcrag.cn/#organization" },
        hasPart: [
          ...humanEntries.map(([name, , href]) => ({ "@type": "WebPage", name, url: `https://redcrag.cn${href}` })),
          ...machineEntries.map(([name, , href]) => ({ "@type": "DigitalDocument", name, url: `https://redcrag.cn${href}` })),
        ],
      },
    ],
  };

  return (
    <div className="site" lang={c.lang}>
      <Header locale={locale} />
      <main id="main-content">
        <HeroCarousel locale={locale} />

        <section className="section home-overview" id="about" data-section-id="overview">
          <div className="section-shell home-overview-grid">
            <div>
              <p className="section-kicker">{locale === "zh" ? "一眼理解（TITMAS AT A GLANCE）" : "TITMAS AT A GLANCE"}</p>
              <h2>{locale === "zh" ? "为不同智能体提供共同的可信互操作边界" : "A shared trust-interoperability boundary for different agents"}</h2>
              <p>
                {locale === "zh"
                  ? "TITMAS 提供开放规范、适配器契约、符合性资产和参考实现边界。它不是智能体框架、托管运行时、真相来源或认证机构。"
                  : "TITMAS provides open specifications, adapter contracts, conformance assets, and reference boundaries. It is not an agent framework, hosted runtime, truth source, or certification body."}
              </p>
              <a className="text-link" href={paths.research}>{locale === "zh" ? "查看研究与架构" : "Explore research and architecture"}<span>→</span></a>
            </div>
            <div className="home-principles" aria-label={locale === "zh" ? "核心边界" : "Core boundaries"}>
              <code>Evidence ≠ Truth</code>
              <code>Verification ≠ Authorization</code>
              <code>Recommendation ≠ Decision</code>
              <code>Decision ≠ Execution</code>
            </div>
          </div>
        </section>

        <section className="section home-gbz-alignment" data-section-id="gbz-185-alignment">
          <div className="section-shell home-gbz-grid">
            <div>
              <p className="section-kicker">{locale === "zh" ? "GB/Z 185 ALIGNMENT / 国家标准衔接" : "GB/Z 185 ALIGNMENT"}</p>
              <h2>{locale === "zh" ? "GB/Z 185 定义智能体如何互联，TITMAS 研究互联行为如何被授权、记录、验证和审计" : "GB/Z 185 defines how agents interconnect; TITMAS researches how interconnection behavior is authorized, recorded, verified, and audited"}</h2>
              <p>{locale === "zh" ? "TITMAS 不替代身份码、身份管理、智能体描述、发现、交互或工具调用规范。当前工作是建立机器可读映射、证据扩展边界和后续适配验证路径。" : "TITMAS does not replace identity-code, identity-management, agent-description, discovery, interaction, or tool-invocation specifications. The current work establishes a machine-readable mapping, evidence-extension boundaries, and a future adapter-validation path."}</p>
              <a className="text-link" href={paths.gbz185}>{locale === "zh" ? "查看 GB/Z 185 衔接矩阵" : "View the GB/Z 185 alignment matrix"}<span>→</span></a>
            </div>
            <aside className="home-gbz-status">
              <code>MAPPING_IMPLEMENTED_LOCAL_VALIDATED</code>
              <code>PUBLICLY_DEPLOYED=false</code>
              <code>CONFORMANCE_ASSESSED=false</code>
              <code>OFFICIAL_AFFILIATION=false</code>
            </aside>
          </div>
        </section>

        <section className="section home-showcase" data-section-id="applications-and-demos">
          <div className="section-shell">
            <div className="section-heading">
              <p className="section-kicker">{locale === "zh" ? "行业应用与参考演示（APPLICATIONS + DEMOS）" : "APPLICATIONS + DEMOS"}</p>
              <h2>{locale === "zh" ? "从共同基础设施进入有边界的行业场景" : "Move from shared infrastructure into bounded industry scenarios"}</h2>
              <p>{locale === "zh" ? "首页只保留入口；行业规则、演示数据和能力边界在独立页面展开。" : "The homepage keeps only the entry points; domain rules, demo data, and boundaries live on dedicated pages."}</p>
            </div>
            <div className="home-showcase-grid">
              <article className="home-showcase-card home-showcase-card-featured">
                <div><span>{locale === "zh" ? "媒体证据场景配置（MEDIA EVIDENCE PROFILE）" : "MEDIA EVIDENCE PROFILE"}</span><code>LOCAL_SYNTHETIC_REFERENCE_IMPLEMENTATION</code></div>
                <h3>{locale === "zh" ? "TITMAS 媒体证据" : "TITMAS Media Evidence"}</h3>
                <p>{locale === "zh" ? "面向人工智能生成内容安全的智能审核证据链参考实现。" : "A review-evidence-chain reference implementation for AI-generated-content safety."}</p>
                <nav aria-label={locale === "zh" ? "媒体证据入口" : "Media evidence entries"}>
                  <a href={paths.mediaIndustry}>{locale === "zh" ? "查看行业应用" : "View application"}<span>→</span></a>
                  <a href={paths.mediaDemo}>{locale === "zh" ? "运行在线演示" : "Run demo"}<span>→</span></a>
                </nav>
              </article>
              <article className="home-showcase-card">
                <div><span>{locale === "zh" ? "医疗证据（MEDICAL EVIDENCE）" : "MEDICAL EVIDENCE"}</span><code>DIRECTION + SYNTHETIC DEMO</code></div>
                <h3>{locale === "zh" ? "医疗证据基础设施" : "Medical Evidence Infrastructure"}</h3>
                <p>{locale === "zh" ? "医疗器械、影像元数据和证据对象的有界行业方向。" : "A bounded direction for medical devices, imaging metadata, and evidence objects."}</p>
                <nav><a href={paths.medicalIndustry}>{locale === "zh" ? "行业页面" : "Application"}<span>→</span></a><a href={paths.medicalDemo}>{locale === "zh" ? "参考演示" : "Demo"}<span>→</span></a></nav>
              </article>
              <article className="home-showcase-card">
                <div><span>{locale === "zh" ? "数字单元（DIGITAL CELL）" : "DIGITAL CELL"}</span><code>REFERENCE_COMPLETE</code></div>
                <h3>{locale === "zh" ? "TITMAS 数字单元演示（TITMAS Digital Cell Demo）" : "TITMAS Digital Cell Demo"}</h3>
                <p>{locale === "zh" ? "展示最小执行对象、确定性重放、证据记录与健康视图。" : "Shows minimal execution objects, deterministic replay, evidence records, and a health view."}</p>
                <nav><a href={paths.digitalCell}>{locale === "zh" ? "打开演示" : "Open demo"}<span>→</span></a><a href={paths.demos}>{locale === "zh" ? "全部演示" : "All demos"}<span>→</span></a></nav>
              </article>
            </div>
          </div>
        </section>

        <section className="section home-developer" id="agent-start" data-section-id="developer-and-machine-entry">
          <div className="section-shell home-developer-grid">
            <div>
              <p className="section-kicker">{locale === "zh" ? "智能体与开发者入口（AGENT START HERE）" : "AGENT START HERE"}</p>
              <h2>{locale === "zh" ? "人类阅读导航，智能体读取明确契约" : "Human navigation and explicit machine contracts"}</h2>
              <div className="home-entry-list">
                {humanEntries.map(([title, description, href]) => <a href={href} key={href}><strong>{title}</strong><span>{description}</span><i>→</i></a>)}
              </div>
            </div>
            <aside className="home-machine-entry">
              <div><span>{locale === "zh" ? "机器可读目录" : "Machine-readable catalog"}</span><code>{locale === "zh" ? "无需脚本（NO JAVASCRIPT REQUIRED）" : "NO JAVASCRIPT REQUIRED"}</code></div>
              {machineEntries.map(([title, description, href]) => <a href={href} key={href}><strong>{title}</strong><small>{description}</small></a>)}
            </aside>
          </div>
        </section>

        <section className="section home-status" id="status" data-section-id="status-and-boundaries">
          <div className="section-shell">
            <div className="section-heading">
              <p className="section-kicker">{locale === "zh" ? "当前状态与能力边界（CURRENT STATUS + BOUNDARIES）" : "CURRENT STATUS + BOUNDARIES"}</p>
              <h2>{locale === "zh" ? "保留失败、限制与未完成状态" : "Failures, limits, and incomplete states remain visible"}</h2>
            </div>
            <div className="home-status-grid">
              <article><span>{locale === "zh" ? "智能体基准（AGENT BENCHMARK）" : "AGENT BENCHMARK"}</span><strong>{locale === "zh" ? "第 5.7 阶段智能体原生选择（Stage 5.7 Agent-Native Selection）· 24/24" : "Stage 5.7 Agent-Native Selection · 24/24"}</strong><p>{locale === "zh" ? "合成基准选择信号，不是客户采用或投资回报。" : "Synthetic selection signal, not customer adoption or investment return."}</p></article>
              <article><span>{locale === "zh" ? "商业成熟度计划（COMMERCIAL MATURITY PROGRAM）" : "COMMERCIAL MATURITY PROGRAM"}</span><strong>CR-01 · BLOCKED_LEDGER_INTEGRITY</strong><p>{locale === "zh" ? "1,661 条历史 Receipt 中有 2 条签名无法验证；完整恢复仍阻塞。" : "2 of 1,661 historical Receipt signatures remain unverifiable; full recovery is blocked."}</p></article>
              <article><span>{locale === "zh" ? "社区（COMMUNITY）" : "COMMUNITY"}</span><strong>{locale === "zh" ? "未建立（NOT ESTABLISHED）" : "NOT ESTABLISHED"}</strong><p>{locale === "zh" ? "方向与入口存在，社区、认证和公共贡献运行不作成立声明。" : "Direction and entries exist; no established community, certification, or active public contribution claim."}</p></article>
              <article><span>{locale === "zh" ? "访问边界（ACCESS）" : "ACCESS"}</span><strong>{locale === "zh" ? "机密核心仍保持私有" : "Confidential core remains private"}</strong><p>{locale === "zh" ? "公开试用意向入口（Public Trial Interest Intake）· E01 人类兼容性观察（E01 Human Compatibility Observation）· 有偿人类试验策略已退出（COMPENSATED_HUMAN_TRIAL_STRATEGY=RETIRED）" : "Public Trial Interest Intake · E01 Human Compatibility Observation · COMPENSATED_HUMAN_TRIAL_STRATEGY=RETIRED"}</p></article>
            </div>
            <div className="home-boundary-row">
              <p>{locale === "zh" ? "测试通过只适用于声明范围，不等于生产就绪、客户采用、安全保证或外部认证。" : "A test pass applies only to its declared scope; it is not production readiness, customer adoption, a security guarantee, or external certification."}<br /><code>PRODUCTION_READY=false · COMMUNITY_ESTABLISHED=false</code></p>
              <nav><a href={paths.status}>{locale === "zh" ? "查看完整状态" : "Full status"}<span>→</span></a><a href={paths.commercial}>{locale === "zh" ? "查看商业成熟度详情" : "Commercial maturity detail"}<span>→</span></a></nav>
            </div>
          </div>
        </section>
      </main>
      <Footer locale={locale} />
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: serializeJsonLd(structuredData) }} />
    </div>
  );
}
