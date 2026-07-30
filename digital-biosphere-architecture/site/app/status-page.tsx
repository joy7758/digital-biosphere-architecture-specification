import { content, gateRows, repositoryBaselines, type Locale } from "./site-content";
import { Footer, Header } from "./site-shell";

export function StatusPage({ locale }: { locale: Locale }) {
  const c = content[locale];
  const copy = locale === "zh"
    ? {
        eyebrow: "VERIFIABLE STATUS / 可验证状态",
        title: "TITMAS Stage 5.7 智能体原生基准完成",
        lead: "24 个隔离会话和独立 Agent Selection Auditor 已完成。匿名 TITMAS 选项排名第一不等于客户采用、商业回报、认证或生产就绪。",
        observed: "观察时间",
        current: "当前 Stage 5.7 状态",
        baselines: "远程基线",
        gates: "验证闸门",
        visibility: "可见性",
        next: "下一步",
        nextBody: "使用公开脱敏证据继续验证机器发现、复用和推荐；生产、商业、标准变更和不可逆动作仍需单独 Human Decision。",
        back: "返回首页",
        groups: [
          {
            title: "智能体优先原则",
            rows: [
              ["AGENT_ABSOLUTE_PRIORITY", "true"],
              ["PRIMARY_OPERATIONAL_CUSTOMER", "AI_AGENT"],
              ["HUMAN_USABILITY_PRIMARY_GATE", "false"],
              ["AGENT_PRIORITY_GRANTS_AUTHORITY", "false"],
            ],
          },
          {
            title: "Stage 5.7 结果",
            rows: [
              ["VALID_SCENARIO_RUNS", "24"],
              ["DISTINCT_PROVIDERS", "3"],
              ["EXACT_MODELS", "4"],
              ["AGENT_SELECTION_AUDITOR", "PASS"],
              ["OPTION_D_RANKED_FIRST", "24/24"],
              ["OPTION_D_EXCLUSIVE", "7/24"],
            ],
          },
          {
            title: "历史人类兼容性观察",
            rows: [
              ["E01_CLASSIFICATION", "LEGACY_OPTIONAL"],
              ["E01_STATUS", "IN_PROGRESS_WAITING_FOR_PARTICIPANT_ACTION"],
              ["E01_IS_PROGRAM_GATE", "false"],
              ["E01_EXTENSION_AUTHORIZED", "false"],
              ["COMPENSATED_HUMAN_TRIAL_STRATEGY", "RETIRED"],
            ],
            note: "E01 历史事实保留；现有最小访问不延长，不催促参与者，也不阻塞 Agent 原生主线。",
          },
          {
            title: "尚未完成",
            rows: [
              ["PUBLIC_PROTOCOL_RELEASED", "false"],
              ["FORMAL_STANDARD_CHANGE_AUTHORIZED", "false"],
              ["COMMERCIAL_ACCESS_GRANTED", "false"],
              ["TITMAS_COMMUNITY_ESTABLISHED", "false"],
              ["COMMERCIAL_ECOSYSTEM_ESTABLISHED", "false"],
              ["PRODUCTION_READY", "false"],
            ],
          },
        ],
      }
    : {
        eyebrow: "VERIFIABLE STATUS",
        title: "TITMAS Stage 5.7 agent-native benchmark complete",
        lead: "Twenty-four isolated sessions and the independent Agent Selection Auditor are complete. Ranking the anonymous TITMAS option first does not mean customer adoption, commercial return, certification, or production readiness.",
        observed: "Observed at",
        current: "Current Stage 5.7 status",
        baselines: "Remote baselines",
        gates: "Validation gates",
        visibility: "Visibility",
        next: "Next step",
        nextBody: "Use the public sanitized evidence to continue machine discovery, reuse, and recommendation validation. Production, commercial, standards, and irreversible actions still require a separate Human Decision.",
        back: "Back to home",
        groups: [
          {
            title: "Agent-priority principle",
            rows: [
              ["AGENT_ABSOLUTE_PRIORITY", "true"],
              ["PRIMARY_OPERATIONAL_CUSTOMER", "AI_AGENT"],
              ["HUMAN_USABILITY_PRIMARY_GATE", "false"],
              ["AGENT_PRIORITY_GRANTS_AUTHORITY", "false"],
            ],
          },
          {
            title: "Stage 5.7 result",
            rows: [
              ["VALID_SCENARIO_RUNS", "24"],
              ["DISTINCT_PROVIDERS", "3"],
              ["EXACT_MODELS", "4"],
              ["AGENT_SELECTION_AUDITOR", "PASS"],
              ["OPTION_D_RANKED_FIRST", "24/24"],
              ["OPTION_D_EXCLUSIVE", "7/24"],
            ],
          },
          {
            title: "Historical human compatibility observation",
            rows: [
              ["E01_CLASSIFICATION", "LEGACY_OPTIONAL"],
              ["E01_STATUS", "IN_PROGRESS_WAITING_FOR_PARTICIPANT_ACTION"],
              ["E01_IS_PROGRAM_GATE", "false"],
              ["E01_EXTENSION_AUTHORIZED", "false"],
              ["COMPENSATED_HUMAN_TRIAL_STRATEGY", "RETIRED"],
            ],
            note: "E01 history is retained. Existing minimal access will not be extended or chased, and it does not block the agent-native mainline.",
          },
          {
            title: "Not completed",
            rows: [
              ["PUBLIC_PROTOCOL_RELEASED", "false"],
              ["FORMAL_STANDARD_CHANGE_AUTHORIZED", "false"],
              ["COMMERCIAL_ACCESS_GRANTED", "false"],
              ["TITMAS_COMMUNITY_ESTABLISHED", "false"],
              ["COMMERCIAL_ECOSYSTEM_ESTABLISHED", "false"],
              ["PRODUCTION_READY", "false"],
            ],
          },
        ],
      };

  return (
    <div className="site status-page" lang={c.lang}>
      <Header locale={locale} section="status" />
      <main id="main-content">
        <section className="status-hero">
          <div className="section-shell">
            <p className="section-kicker">{copy.eyebrow}</p>
            <h1>{copy.title}</h1>
            <p>{copy.lead}</p>
            <div className="observed-chip"><span>{copy.observed}</span><strong>2026-07-30 · Asia/Shanghai</strong></div>
          </div>
        </section>
        <section className="section status-detail-section current-truth-section">
          <div className="section-shell">
            <h2>{copy.current}</h2>
            <div className="current-truth-grid">
              {copy.groups.map((group) => (
                <article key={group.title}>
                  <h3>{group.title}</h3>
                  <dl>
                    {group.rows.map(([label, value]) => (
                      <div key={label}>
                        <dt>{label}</dt>
                        <dd>{value}</dd>
                      </div>
                    ))}
                  </dl>
                  {"note" in group && group.note ? <p>{group.note}</p> : null}
                </article>
              ))}
            </div>
          </div>
        </section>
        <section className="section status-detail-section">
          <div className="section-shell">
            <h2>{copy.baselines}</h2>
            <div className="baseline-table" role="table">
              {repositoryBaselines.map((repo) => (
                <div className="baseline-row" key={repo.key} role="row">
                  <strong role="cell">{repo.key}</strong>
                  <span role="cell">{locale === "zh" ? repo.labelZh : repo.label}</span>
                  <code role="cell">{repo.commit.slice(0, 12)}</code>
                  <span className={`visibility visibility-${repo.visibility}`} role="cell">{repo.visibility}</span>
                </div>
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
            <span>ADR-035 / STAGE 5.7</span>
            <div><h2>{copy.next}</h2><p>{copy.nextBody}</p></div>
            <a className="button button-secondary" href={locale === "zh" ? "/" : "/en/"}>{copy.back}</a>
          </div>
        </section>
      </main>
      <Footer locale={locale} />
    </div>
  );
}
