import { content, gateRows, repositoryBaselines, type Locale } from "./site-content";
import { Footer, Header } from "./site-shell";

export function StatusPage({ locale }: { locale: Locale }) {
  const c = content[locale];
  const copy = locale === "zh"
    ? {
        eyebrow: "VERIFIABLE STATUS / 可验证状态",
        title: "当前不是正式发布",
        lead: "本页只记录已经观察到的事实、失败关闭结果和下一道人工闸门。",
        observed: "观察时间",
        baselines: "远程基线",
        gates: "验证闸门",
        visibility: "可见性",
        next: "下一步",
        nextBody: "先修复智能体客户包并用同一阈值复测，再由人工决定 DBOS 智能体访问路线和正式发布。",
        back: "返回首页",
      }
    : {
        eyebrow: "VERIFIABLE STATUS",
        title: "This is not a release",
        lead: "This page records observed facts, fail-closed results, and the next human gate—nothing more.",
        observed: "Observed at",
        baselines: "Remote baselines",
        gates: "Validation gates",
        visibility: "Visibility",
        next: "Next step",
        nextBody: "Remediate the agent customer package and rerun under the same thresholds, then make explicit human decisions on DBOS agent access and formal release.",
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
            <div className="observed-chip"><span>{copy.observed}</span><strong>2026-07-21 · Asia/Shanghai</strong></div>
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
            <span>DP-5C</span>
            <div><h2>{copy.next}</h2><p>{copy.nextBody}</p></div>
            <a className="button button-secondary" href={locale === "zh" ? "/" : "/en/"}>{copy.back}</a>
          </div>
        </section>
      </main>
      <Footer locale={locale} />
    </div>
  );
}
