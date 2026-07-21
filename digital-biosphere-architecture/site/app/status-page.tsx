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
        nextBody: "继续观察匿名安装和智能体复用结果，并在索引刷新后复查规范名称发现。DBOS 整仓保持 private，开放网络状态继续是 PARTIAL_METADATA_ONLY。",
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
        nextBody: "Continue observing anonymous installation and agent reuse, then recheck canonical-name discovery after indexing refreshes. The full DBOS repository stays private and open-web status remains PARTIAL_METADATA_ONLY.",
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
            <span>ADR-022 / G8</span>
            <div><h2>{copy.next}</h2><p>{copy.nextBody}</p></div>
            <a className="button button-secondary" href={locale === "zh" ? "/" : "/en/"}>{copy.back}</a>
          </div>
        </section>
      </main>
      <Footer locale={locale} />
    </div>
  );
}
