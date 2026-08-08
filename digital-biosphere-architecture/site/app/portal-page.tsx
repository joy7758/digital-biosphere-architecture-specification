import { HeroCarousel } from "./components/hero-carousel";
import { type Locale } from "./site-content";
import { Footer, Header } from "./site-shell";
import { serializeJsonLd } from "./json-ld";

const copy = {
  zh: {
    problemKicker: "RESEARCH PROBLEM / 研究问题",
    problemTitle: "自主系统需要循环，也需要可验证的边界",
    problemLead: "自主实验循环把提出假设、执行行动、观察结果、评价证据与下一步决策连接起来。研究问题不是如何制造一个无边界自治体，而是如何让每一步保留来源、身份、范围、失败和可复现记录。",
    problemSteps: [
      ["01", "提出假设", "目标与假设必须可引用，并与后续证据分离。"],
      ["02", "有界执行", "行动需要显式权限边界、输入来源与可验证回执。"],
      ["03", "评价与保留", "评价输出建议而非命令；失败与经验进入连续记录。"],
      ["04", "审查后迭代", "新一轮建立在可检查证据上，不把变化自动称为演化。"],
    ],
    evidenceKicker: "PUBLIC EVIDENCE / 公开证据",
    evidenceTitle: "三个可检查入口，分别证明有限能力",
    evidenceLead: "这些仓库是现有工程证据，不共同构成一个已完成的 DCELL 系统。每个入口都标注存在内容、成熟度与限制。",
    evidence: [
      {
        name: "verifiable-agent-demo",
        problem: "Agent 执行结果如何形成可检查、可重放的证据。",
        exists: "公开的最小执行证据演示与验证路径。",
        maturity: "IMPLEMENTED",
        limit: "演示不证明通用智能、生产可靠性或自主演化。",
        href: "https://github.com/joy7758/verifiable-agent-demo",
      },
      {
        name: "SAEE",
        problem: "如何评价 Agent 行为，同时阻止评价结果越权成为执行命令。",
        exists: "评价与演化建议的工程研究基线，以及只读边界。",
        maturity: "EXPERIMENTALLY_SUPPORTED",
        limit: "评价证据不等于授权，也不是 post-training system。",
        href: "https://github.com/joy7758/SAEE",
      },
      {
        name: "titmas-agent-action-gate",
        problem: "Agent 行动如何在执行前经过显式、有界的决策闸门。",
        exists: "行动闸门原型与可验证决策记录。",
        maturity: "PROTOTYPE",
        limit: "原型不是中央控制器、生产服务或完整信任权威。",
        href: "https://github.com/joy7758/titmas-agent-action-gate",
      },
    ],
    dcellKicker: "DCELL / RESEARCH_DIRECTION",
    dcellTitle: "把可信基础设施研究组织成可检验的 DCELL 方向",
    dcellLead: "DCELL 探索证据驱动、有界、可独立识别、经验连续、可替换且可演化的自主 AI 系统。它是连接问题与实验的研究方向，不是已完成的平台、数字生命实现、完整 Cell 生态或中央操作系统。",
    maturity: [
      ["IMPLEMENTED", "可验证执行证据的最小公开路径。"],
      ["EXPERIMENTALLY_SUPPORTED", "Agent 评价和证据基础设施已获得有限实验支持。"],
      ["PROTOTYPE", "受限行动基础设施与连续性对象仍是原型。"],
      ["RESEARCH_DIRECTION", "DCELL 组织身份、证据、评价、行动和经验连续性研究。"],
      ["FUTURE_HYPOTHESIS", "可替换组件与长期经验连续性可能支持更可靠的自主系统。"],
    ],
    titmasKicker: "TITMAS / 早期工程种子",
    titmasTitle: "保留工程历史，但不让历史成为中央控制权",
    titmasLead: "TITMAS 是更广泛 DCELL 研究方向下的早期工程种子和第一个实验实例。它为身份、边界、执行证据、健康、记忆与声誉等问题提供了初始工程材料；它不是控制器、操作系统、大脑、生态所有者或信任权威。",
    titmasLinks: [["历史 Demo", "/digital-cell/"], ["历史材料", "/community/"], ["公开 GitHub", "https://github.com/joy7758"]],
    researcherKicker: "RESEARCHER / 研究者",
    researcherTitle: "Bin Zhang · 张斌",
    researcherLead: "Research Engineer building trustworthy infrastructure for autonomous AI systems. 研究关注 agents、infrastructure、environments 与 evaluations，尤其是执行来源、身份连续性、受限行动和自主实验循环的可靠性。",
    researcherLinks: [["GitHub", "https://github.com/joy7758"], ["ORCID", "https://orcid.org/0009-0002-8861-1481"], ["Research index", "/research/"]],
  },
  en: {
    problemKicker: "RESEARCH PROBLEM",
    problemTitle: "Autonomous systems need loops—and verifiable boundaries",
    problemLead: "Autonomous experimental loops connect hypothesis formation, bounded action, observation, evidence evaluation, and the next decision. The question is not how to create an unbounded autonomous entity, but how every step can retain provenance, identity, scope, failure, and reproducible records.",
    problemSteps: [
      ["01", "Form a hypothesis", "Goals and hypotheses remain referenceable and separate from later evidence."],
      ["02", "Execute within bounds", "Actions carry explicit permission boundaries, input provenance, and verifiable receipts."],
      ["03", "Evaluate and retain", "Evaluations produce recommendations, not commands; failures and experience enter a continuous record."],
      ["04", "Iterate after review", "A new loop builds on inspectable evidence without automatically calling change evolution."],
    ],
    evidenceKicker: "PUBLIC EVIDENCE",
    evidenceTitle: "Three inspectable entry points, each supporting a bounded claim",
    evidenceLead: "These repositories are existing engineering evidence. Together they do not constitute a complete DCELL system. Each entry states what exists, its maturity, and its limitation.",
    evidence: [
      {
        name: "verifiable-agent-demo",
        problem: "How agent execution can produce inspectable, replayable evidence.",
        exists: "A public minimal execution-evidence demo and verification path.",
        maturity: "IMPLEMENTED",
        limit: "The demo does not establish general intelligence, production reliability, or autonomous evolution.",
        href: "https://github.com/joy7758/verifiable-agent-demo",
      },
      {
        name: "SAEE",
        problem: "How to evaluate agent behavior without allowing evaluation to become an execution command.",
        exists: "An engineering research baseline for evaluation and evolution recommendations, with read-only boundaries.",
        maturity: "EXPERIMENTALLY_SUPPORTED",
        limit: "Evaluation evidence is not authorization and this is not a post-training system.",
        href: "https://github.com/joy7758/SAEE",
      },
      {
        name: "titmas-agent-action-gate",
        problem: "How agent actions can pass through an explicit, bounded decision gate before execution.",
        exists: "An action-gate prototype with verifiable decision records.",
        maturity: "PROTOTYPE",
        limit: "The prototype is not a central controller, production service, or complete trust authority.",
        href: "https://github.com/joy7758/titmas-agent-action-gate",
      },
    ],
    dcellKicker: "DCELL / RESEARCH_DIRECTION",
    dcellTitle: "Organizing trustworthy-infrastructure research as a testable DCELL direction",
    dcellLead: "DCELL explores evidence-driven, bounded, independently identifiable, experience-preserving, replaceable, and evolvable autonomous AI systems. It connects research questions to experiments; it is not a finished platform, implemented digital life, a complete Cell ecosystem, or a central operating system.",
    maturity: [
      ["IMPLEMENTED", "A minimal public path for verifiable execution evidence."],
      ["EXPERIMENTALLY_SUPPORTED", "Agent evaluation and evidence infrastructure with bounded experimental support."],
      ["PROTOTYPE", "Bounded-action infrastructure and continuity objects remain prototypes."],
      ["RESEARCH_DIRECTION", "DCELL organizes research on identity, evidence, evaluation, action, and experience continuity."],
      ["FUTURE_HYPOTHESIS", "Replaceable components and long-term experience continuity may support more dependable autonomous systems."],
    ],
    titmasKicker: "TITMAS / EARLY ENGINEERING SEED",
    titmasTitle: "Preserve the engineering history without turning it into central authority",
    titmasLead: "TITMAS is an early engineering seed and first experimental instance under the broader DCELL research direction. It supplied initial engineering material for identity, boundaries, execution evidence, health, memory, and reputation. It is not a controller, operating system, brain, ecosystem owner, or trust authority.",
    titmasLinks: [["Historical demo", "/en/digital-cell/"], ["Historical material", "/en/community/"], ["Public GitHub", "https://github.com/joy7758"]],
    researcherKicker: "RESEARCHER",
    researcherTitle: "Bin Zhang · 张斌",
    researcherLead: "Research Engineer building trustworthy infrastructure for autonomous AI systems. The work focuses on agents, infrastructure, environments, and evaluations—especially execution provenance, identity continuity, bounded action, and the reliability of autonomous experimental loops.",
    researcherLinks: [["GitHub", "https://github.com/joy7758"], ["ORCID", "https://orcid.org/0009-0002-8861-1481"], ["Research index", "/en/research/"]],
  },
} as const;

export function PortalPage({ locale }: { locale: Locale }) {
  const c = copy[locale];
  const structuredData = {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Person",
        "@id": "https://redcrag.cn/#bin-zhang",
        name: "Bin Zhang",
        url: "https://redcrag.cn/",
        sameAs: ["https://github.com/joy7758", "https://orcid.org/0009-0002-8861-1481"],
        description: "Research Engineer building trustworthy infrastructure for autonomous AI systems.",
      },
      {
        "@type": "ResearchProject",
        "@id": "https://redcrag.cn/#dcell",
        name: "DCELL",
        url: "https://redcrag.cn/#dcell",
        description: "A research direction for evidence-driven, bounded, independently identifiable, experience-preserving, replaceable, and evolvable autonomous AI systems.",
        funder: { "@id": "https://redcrag.cn/#bin-zhang" },
      },
    ],
  };

  return (
    <div className="site" lang={locale === "zh" ? "zh-CN" : "en"}>
      <Header locale={locale} />
      <main id="main-content">
        <HeroCarousel locale={locale} />

        <section className="section home-overview" id="problem" data-section-id="autonomous-experimental-loop">
          <div className="section-shell">
            <div className="section-heading"><p className="section-kicker">{c.problemKicker}</p><h2>{c.problemTitle}</h2><p>{c.problemLead}</p></div>
            <div className="home-product-grid">
              {c.problemSteps.map(([number, title, body]) => <article key={number}><span>{number}</span><h3>{title}</h3><p>{body}</p></article>)}
            </div>
          </div>
        </section>

        <section className="section home-showcase" id="public-evidence" data-section-id="public-evidence">
          <div className="section-shell">
            <div className="section-heading"><p className="section-kicker">{c.evidenceKicker}</p><h2>{c.evidenceTitle}</h2><p>{c.evidenceLead}</p></div>
            <div className="home-showcase-grid">
              {c.evidence.map((item, index) => (
                <article className={`home-showcase-card${index === 0 ? " home-showcase-card-featured" : ""}`} key={item.name}>
                  <div><span>0{index + 1}</span><code>{item.maturity}</code></div><h3>{item.name}</h3><p><strong>Problem:</strong> {item.problem}</p><p><strong>Exists:</strong> {item.exists}</p><p><strong>Limitation:</strong> {item.limit}</p><nav><a href={item.href}>GitHub <span>↗</span></a></nav>
                </article>
              ))}
            </div>
          </div>
        </section>

        <section className="section home-developer" id="dcell" data-section-id="dcell-research-direction">
          <div className="section-shell home-developer-grid">
            <div><p className="section-kicker">{c.dcellKicker}</p><h2>{c.dcellTitle}</h2><p>{c.dcellLead}</p></div>
            <aside className="home-machine-entry">
              <div><span>MATURITY MODEL</span><code>PUBLIC CLAIM BOUNDARY</code></div>
              {c.maturity.map(([label, text]) => <div key={label}><strong>{label}</strong><small>{text}</small></div>)}
            </aside>
          </div>
        </section>

        <section className="section home-showcase" id="titmas-history" data-section-id="titmas-founding-engineering-experiment">
          <div className="section-shell home-developer-grid">
            <div><p className="section-kicker">{c.titmasKicker}</p><h2>{c.titmasTitle}</h2><p>{c.titmasLead}</p></div>
            <div className="home-entry-list">{c.titmasLinks.map(([label, href]) => <a href={href} key={href}><strong>{label}</strong><i>→</i></a>)}</div>
          </div>
        </section>

        <section className="section home-status" id="researcher" data-section-id="researcher">
          <div className="section-shell">
            <div className="section-heading"><p className="section-kicker">{c.researcherKicker}</p><h2>{c.researcherTitle}</h2><p>{c.researcherLead}</p></div>
            <div className="home-boundary-row"><p><code>Evidence ≠ Truth · Evaluation ≠ Authority · Recommendation ≠ Decision · Decision ≠ Execution</code></p><nav>{c.researcherLinks.map(([label, href]) => <a href={href} key={href}>{label}<span>→</span></a>)}</nav></div>
          </div>
        </section>
      </main>
      <Footer locale={locale} />
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: serializeJsonLd(structuredData) }} />
    </div>
  );
}
