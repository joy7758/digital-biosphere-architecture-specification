import { content, gateRows, repositoryBaselines, type Locale } from "./site-content";
import { Footer, Header } from "./site-shell";

export function StatusPage({ locale }: { locale: Locale }) {
  const c = content[locale];
  const copy = locale === "zh"
    ? {
        eyebrow: "VERIFIABLE STATUS / 可验证状态",
        title: "可信多智能体基础设施开发者预览版 v0.1 已发布",
        lead: "本页记录正式发布、已验证范围、保留限制和后续观察；Developer Preview 不等于生产就绪。",
        observed: "观察时间",
        baselines: "远程基线",
        gates: "验证闸门",
        visibility: "可见性",
        next: "下一步",
        nextBody: "下一生产架构闸门不是继续新增规范，而是通过统一决策就绪注册表分别人工处理 DQ-022 OTLP、DQ-023 OTel 语义、DQ-024 Schema／Resource／Entity、DQ-025 Collector inventory、ADR-024 分阶段生产路径和 DQ-018 DBOS 精确切片。每项必须独立 token；注册表、参考采纳和模型推荐均不自动授权实现。DBOS 整仓保持 private。",
        back: "返回首页",
      }
    : {
        eyebrow: "VERIFIABLE STATUS",
        title: "Trusted Multi-Agent Infrastructure Developer Preview v0.1 is released",
        lead: "This page records the formal release, validated scope, retained limitations, and follow-up observations. Developer Preview does not mean production-ready.",
        observed: "Observed at",
        baselines: "Remote baselines",
        gates: "Validation gates",
        visibility: "Visibility",
        next: "Next step",
        nextBody: "The next production-architecture gate is not another specification. The unified decision-readiness registry separates human action for DQ-022 OTLP, DQ-023 OTel semantics, DQ-024 Schema/Resource/Entity, DQ-025 Collector inventory, the ADR-024 staged production path, and the exact DQ-018 DBOS slice. Each requires its own token; the registry, reference adoption, and model recommendations authorize no implementation. The full DBOS repository remains private.",
        back: "Back to home",
      };

  return (
    <div className="site status-page" lang={c.lang}>
      <Header locale={locale} section="status" />
      <main>
        <section className="status-hero">
          <div className="section-shell">
            <p className="section-kicker">{copy.eyebrow}</p>
            <h1>{copy.title}</h1>
            <p>{copy.lead}</p>
            <div className="observed-chip"><span>{copy.observed}</span><strong>2026-07-22 · Asia/Shanghai</strong></div>
          </div>
        </section>
        <section className="section status-detail-section">
          <div className="section-shell">
            <h2>{copy.baselines}</h2>
            <div className="baseline-table" role="table">
              {repositoryBaselines.map((repo) => (
                <a className="baseline-row" href={repo.href} key={repo.key} role="row">
                  <strong role="cell">{repo.key}</strong>
                  <span role="cell">{locale === "zh" ? repo.labelZh : repo.label}</span>
                  <code role="cell">{repo.commit.slice(0, 12)}</code>
                  <span className={`visibility visibility-${repo.visibility}`} role="cell">{repo.visibility}</span>
                </a>
              ))}
            </div>
          </div>
        </section>
        <section className="section status-detail-section alt">
          <div className="section-shell">
            <h2>{copy.gates}</h2>
            <div className="gate-list">
              {gateRows.map((gate) => (
                <article key={gate.id}>
                  <span className={`state state-${gate.state.toLowerCase()}`}>{gate.state}</span>
                  <code>{gate.id}</code>
                  <p>{gate[locale]}</p>
                </article>
              ))}
            </div>
          </div>
        </section>
        <section className="section next-gate-section">
          <div className="section-shell next-gate-card">
            <span>DQ-022 / DQ-023 / DQ-024 / DQ-025 / ADR-024 / DQ-018</span>
            <div><h2>{copy.next}</h2><p>{copy.nextBody}</p></div>
            <a className="button button-secondary" href={locale === "zh" ? "/" : "/en/"}>{copy.back}</a>
          </div>
        </section>
      </main>
      <Footer locale={locale} />
    </div>
  );
}
