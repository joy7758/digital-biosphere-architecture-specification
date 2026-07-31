import { communityGateRows, content, type Locale } from "./site-content";
import { Footer, Header } from "./site-shell";

export function PortalPage({ locale }: { locale: Locale }) {
  const c = content[locale];
  const statusPath = locale === "zh" ? "/status/" : "/en/status/";
  const researchPath = locale === "zh" ? "/research/" : "/en/research/";
  const demosPath = locale === "zh" ? "/demos/" : "/en/demos/";
  const digitalCellPath = locale === "zh" ? "/digital-cell/" : "/en/digital-cell/";
  const architectureHref =
    "https://github.com/joy7758/digital-biosphere-architecture-specification";
  const agentDirectory = [
    {
      id: "research",
      label: locale === "zh" ? "研究" : "Research",
      description: locale === "zh" ? "方向、架构与证据治理" : "Directions, architecture, and evidence governance",
      href: researchPath,
    },
    {
      id: "applications",
      label: locale === "zh" ? "行业应用" : "Applications",
      description: locale === "zh" ? "基础设施如何进入行业" : "How the infrastructure enters industries",
      href: locale === "zh" ? "/applications/" : "/en/applications/",
    },
    {
      id: "demos",
      label: "Demos",
      description: locale === "zh" ? "有边界的参考实现" : "Bounded reference implementations",
      href: demosPath,
    },
    {
      id: "developers",
      label: locale === "zh" ? "开发者" : "Developers",
      description: locale === "zh" ? "规范、边界与贡献入口" : "Specifications, boundaries, and contribution entry",
      href: locale === "zh" ? "/community/" : "/en/community/",
    },
    {
      id: "updates",
      label: locale === "zh" ? "更新" : "Updates",
      description: locale === "zh" ? "公告、版本与变更来源" : "Announcements, versions, and change provenance",
      href: locale === "zh" ? "/updates/" : "/en/updates/",
    },
  ];
  const agentMachineEntries = [
    {
      label: "llms.txt",
      href: "/llms.txt",
      description: locale === "zh" ? "快速理解与边界" : "Quick orientation and boundaries",
    },
    {
      label: "agent-index.json",
      href: "/agent-index.json",
      description: locale === "zh" ? "完整智能体发现索引" : "Complete agent discovery index",
    },
    {
      label: "site-catalog.json",
      href: "/site-catalog.json",
      description: locale === "zh" ? "网站栏目与扩展接口" : "Site surfaces and extension interfaces",
    },
  ];

  const structuredData = {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Organization",
        "@id": "https://redcrag.cn/#organization",
        name: "山西游骑兵电子商务有限公司",
        legalName: "山西游骑兵电子商务有限公司",
        alternateName: ["夏日之海", "titmas", "TITMAS"],
        url: "https://redcrag.cn/",
        logo: "https://redcrag.cn/titmas-logo.png",
      },
      {
        "@type": "WebSite",
        "@id": "https://redcrag.cn/#website",
        name: "山西游骑兵电子商务有限公司",
        alternateName: ["夏日之海", "titmas", "TITMAS"],
        url: "https://redcrag.cn/",
        inLanguage: ["zh-CN", "en"],
        description: c.lead,
        image: "https://redcrag.cn/titmas-logo.png",
        publisher: { "@id": "https://redcrag.cn/#organization" },
        isBasedOn: architectureHref,
        hasPart: [
          ...agentDirectory.map((entry) => ({
            "@type": "WebPage",
            "@id": `https://redcrag.cn${entry.href}#webpage`,
            name: entry.label,
            url: `https://redcrag.cn${entry.href}`,
          })),
          ...agentMachineEntries.map((entry) => ({
            "@type": "DigitalDocument",
            "@id": `https://redcrag.cn${entry.href}#document`,
            name: entry.label,
            url: `https://redcrag.cn${entry.href}`,
            encodingFormat: entry.href.endsWith(".txt") ? "text/plain" : "application/json",
          })),
        ],
      },
      {
        "@type": "WebPage",
        "@id": `${locale === "zh" ? "https://redcrag.cn/" : "https://redcrag.cn/en/"}#webpage`,
        url: locale === "zh" ? "https://redcrag.cn/" : "https://redcrag.cn/en/",
        name: locale === "zh"
          ? "夏日之海"
          : "titmas",
        description: c.lead,
        inLanguage: c.lang,
        isPartOf: { "@id": "https://redcrag.cn/#website" },
      },
    ],
  };

  return (
    <div className="site" lang={c.lang}>
      <Header locale={locale} />
      <main id="main-content">
        <section className="hero" data-section-id="hero">
          <div className="hero-grid" aria-hidden="true">
            <div className="orbit orbit-a" />
            <div className="orbit orbit-b" />
            <div className="node node-a" />
            <div className="node node-b" />
            <div className="node node-c" />
          </div>
          <div className="hero-content">
            <span
              className="hero-brand-logo"
              role="img"
              aria-label={locale === "zh" ? "夏日之海 Logo" : "titmas logo"}
            />
            <div className="hero-badge"><span />{c.badge}</div>
            <p className="eyebrow">{c.eyebrow}</p>
            <h1>{c.title}</h1>
            <p className="hero-lead">
              {c.lead}{" "}
              {locale === "zh"
                ? "让身份、行为边界、执行历史与评估记录可理解、可核验。"
                : "Make identity, behavior boundaries, execution history, and evaluation records understandable and verifiable."}
            </p>
            <div className="hero-actions">
              <a className="button button-primary" href={researchPath}>{c.primaryCta}</a>
              <a className="button button-secondary" href={demosPath}>{c.secondaryCta}</a>
            </div>
            <p className="truth-notice">
              <span>i</span>
              <a href={statusPath}>{c.notice}</a>
            </p>
          </div>
        </section>

        <section
          className="agent-front-door"
          id="agent-start"
          data-section-id="agent-front-door"
          aria-labelledby="agent-start-title"
        >
          <div className="section-shell agent-front-door-shell">
            <div className="agent-front-door-intro">
              <p className="section-kicker">AGENT START HERE / 智能体从这里开始</p>
              <h2 id="agent-start-title">
                {locale === "zh" ? "一眼理解夏日之海" : "Understand titmas at a glance"}
              </h2>
              <p>
                {locale === "zh"
                  ? "TITMAS 是可信多智能体基础设施的开发者入口：研究定义方向，行业应用解释用途，Demo 展示参考实现，开发者入口提供规范与贡献路径。它不是 Agent Framework、托管 Runtime 或认证机构。"
                  : "TITMAS is a developer entry for trusted multi-agent infrastructure: research defines directions, applications explain uses, demos show references, and the developer entry provides specifications and contribution paths. It is not an Agent Framework, hosted Runtime, or certification body."}
              </p>
            </div>

            <nav
              className="agent-front-door-nav"
              aria-label={locale === "zh" ? "智能体网站导航" : "Agent site navigation"}
            >
              {agentDirectory.map((entry) => (
                <a href={entry.href} key={entry.id}>
                  <strong>{entry.label}</strong>
                  <span>{entry.description}</span>
                  <i aria-hidden="true">→</i>
                </a>
              ))}
            </nav>

            <aside
              className="agent-front-door-machine"
              aria-label={locale === "zh" ? "机器可读入口" : "Machine-readable entry points"}
            >
              <div>
                <span>{locale === "zh" ? "机器可读入口" : "Machine-readable"}</span>
                <code>NO JAVASCRIPT REQUIRED</code>
              </div>
              <nav aria-label={locale === "zh" ? "智能体机器入口" : "Agent machine entry points"}>
                {agentMachineEntries.map((entry) => (
                  <a href={entry.href} key={entry.href}>
                    <strong>{entry.label}</strong>
                    <small>{entry.description}</small>
                  </a>
                ))}
              </nav>
            </aside>
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
            <details className="commercial-entry-truth">
              <summary>{locale === "zh" ? "查看当前真实状态" : "Review current truth"}</summary>
              <code>PACKAGE_PREPARED=true</code>
              <code>REMOTE_VALIDATED=true</code>
              <code>AVAILABLE_OFFERING=false</code>
              <code>PRODUCTION_READY=false</code>
              <code>CUSTOMERS_VERIFIED=0</code>
            </details>
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
                <a className="button cell-feature-primary" href={digitalCellPath}>
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
              href={digitalCellPath}
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

        <section className="medical-entry" data-section-id="medical-evidence-application">
          <div className="section-shell">
            <div className="section-heading medical-entry-heading">
              <p className="section-kicker">INDUSTRY APPLICATION + REFERENCE DEMO</p>
              <h2>{locale === "zh" ? "从可信基础设施进入医疗证据场景" : "Bring trust infrastructure into medical evidence"}</h2>
              <p>
                {locale === "zh"
                  ? "医疗证据基础设施不是独立医疗软件，而是 TITMAS 在医疗设备、操作过程与 AI 智能体证据方向上的第一个行业应用。"
                  : "Medical Evidence Infrastructure is not standalone medical software. It is the first TITMAS industry application direction for evidence across medical devices, operations, and AI agents."}
              </p>
            </div>
            <div className="medical-entry-grid">
              <a className="medical-entry-card medical-entry-application" href={locale === "zh" ? "/industry/medical-evidence/" : "/en/industry/medical-evidence/"}>
                <span>INDUSTRY APPLICATION</span>
                <h3>{locale === "zh" ? "医疗证据基础设施" : "Medical Evidence Infrastructure"}</h3>
                <p>
                  {locale === "zh"
                    ? "基于 TITMAS 的医疗设备、操作流程和 AI 智能体可信证据体系。"
                    : "A TITMAS-based evidence system for medical devices, operations, and AI agents."}
                </p>
                <strong>{locale === "zh" ? "查看详情" : "Explore the direction"} <i>→</i></strong>
              </a>
              <a className="medical-entry-card medical-entry-demo" href={locale === "zh" ? "/demo/medical-evidence/" : "/en/demo/medical-evidence/"}>
                <span>REFERENCE DEMO</span>
                <h3>UDI-DICOM Evidence Validator</h3>
                <p>
                  {locale === "zh"
                    ? "使用模拟 UDI 展开 Identity → Imaging → Evidence 的预设引用关系。"
                    : "Use a synthetic UDI to inspect preset Identity → Imaging → Evidence references."}
                </p>
                <strong>{locale === "zh" ? "查看 Demo" : "Open the demo"} <i>→</i></strong>
                <code>SYNTHETIC_DATA_ONLY · VALIDATOR_IMPLEMENTED_HERE=false</code>
              </a>
            </div>
          </div>
        </section>

        <details className="home-deep-dive">
          <summary>
            <span>{locale === "zh" ? "深入了解" : "Go deeper"}</span>
            <strong>
              {locale === "zh"
                ? "查看 TITMAS 架构、可信边界与治理状态"
                : "Explore TITMAS architecture, trust boundaries, and governance status"}
            </strong>
          </summary>
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
        </details>

        <section className="site-operator-section" aria-labelledby="site-operator-title">
          <div className="section-shell site-operator-card">
            <p className="section-kicker">WEBSITE OPERATOR / 网站运营主体</p>
            <h2 id="site-operator-title">山西游骑兵电子商务有限公司</h2>
            <p>
              {locale === "zh"
                ? "本网站由山西游骑兵电子商务有限公司运营，用于展示公司公开发布的数字技术研究、可信基础设施说明、行业应用示例与有明确边界的参考演示。夏日之海是中文公开品牌，titmas 是英文公开品牌，TITMAS 是技术项目标识。"
                : "This website is operated by 山西游骑兵电子商务有限公司 and presents the company's public digital-technology research, trust-infrastructure materials, industry application examples, and explicitly bounded reference demos. 夏日之海 is the Chinese public brand, titmas is the English public brand, and TITMAS is the technical project identifier."}
            </p>
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
