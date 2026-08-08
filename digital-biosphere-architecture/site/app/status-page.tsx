import { content, gateRows, repositoryBaselines, type Locale } from "./site-content";
import { Footer, Header } from "./site-shell";

export function StatusPage({ locale }: { locale: Locale }) {
  const c = content[locale];
  const copy = locale === "zh"
    ? {
        eyebrow: "VERIFIABLE STATUS / 可验证状态",
        title: "DCELL 是研究方向，公开工程证据保持有界",
        lead: "本页区分当前 DCELL 公开定位与保留的 TITMAS 历史工程状态。网站对齐候选尚未部署；公开仓库不构成完整 Cell 生态、自主演化或生产平台。",
        observed: "观察时间",
        current: "当前公开定位与保留工程状态",
        baselines: "远程基线",
        gates: "验证闸门",
        visibility: "可见性",
        next: "下一步",
        nextBody: "CR01-D02 已批准设计但未批准实施。下一步 CR01-D03 决定是否实施“不可变异常清单 + 租户级锚定清洁 epoch”及是否例外增加 PR 和部署额度；此前不修改 Gateway、不迁移数据库、不重启 CR-01 或 72 小时稳定性测试。",
        back: "返回首页",
        groups: [
          {
            title: "DCELL 公开对齐",
            rows: [
              ["DCELL_MATURITY", "RESEARCH_DIRECTION"],
              ["WEBSITE_ALIGNMENT", "LOCAL_CANDIDATE_NOT_DEPLOYED"],
              ["AUTONOMOUS_EXPERIMENTAL_LOOPS", "RESEARCH_FOCUS"],
              ["COMPLETE_CELL_ECOSYSTEM", "false"],
              ["AUTONOMOUS_EVOLUTION_ACHIEVED", "false"],
              ["POST_TRAINING_SYSTEM", "false"],
            ],
          },
          {
            title: "商业候选服务",
            rows: [
              ["SERVICE_READY", "true"],
              ["COMMERCIAL_TECHNICAL_READY", "false"],
              ["PAID_BETA_READY", "false"],
              ["PRODUCTION_READY", "false"],
              ["DATABASE_DEPLOYMENT_EVIDENCE_RECORDED", "true"],
              ["CR01_STATUS", "BLOCKED_LEDGER_INTEGRITY"],
              ["CR01_D02_STATUS", "ACCEPTED_DESIGN_ONLY"],
              ["LEDGER_TRANSITION_IMPLEMENTATION_AUTHORIZED", "false"],
              ["BACKUP_RESTORE_DRILL_PASS", "false"],
              ["RESTORE_RTO_STATUS", "NOT_ESTABLISHED"],
            ],
          },
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
        title: "DCELL is a research direction; public engineering evidence remains bounded",
        lead: "This page separates the current DCELL public positioning from retained TITMAS engineering history. The website-alignment candidate is not deployed, and public repositories do not constitute a complete Cell ecosystem, achieved autonomous evolution, or a production platform.",
        observed: "Observed at",
        current: "Current public alignment and retained engineering status",
        baselines: "Remote baselines",
        gates: "Validation gates",
        visibility: "Visibility",
        next: "Next step",
        nextBody: "CR01-D02 approved design, not implementation. CR01-D03 must decide whether to implement an immutable exception manifest plus Tenant-scoped anchored clean epochs and whether to grant PR and deployment-cap exceptions. Gateway changes, database migration, CR-01 restart, and the 72-hour soak remain closed.",
        back: "Back to home",
        groups: [
          {
            title: "DCELL public alignment",
            rows: [
              ["DCELL_MATURITY", "RESEARCH_DIRECTION"],
              ["WEBSITE_ALIGNMENT", "LOCAL_CANDIDATE_NOT_DEPLOYED"],
              ["AUTONOMOUS_EXPERIMENTAL_LOOPS", "RESEARCH_FOCUS"],
              ["COMPLETE_CELL_ECOSYSTEM", "false"],
              ["AUTONOMOUS_EVOLUTION_ACHIEVED", "false"],
              ["POST_TRAINING_SYSTEM", "false"],
            ],
          },
          {
            title: "Commercial candidate service",
            rows: [
              ["SERVICE_READY", "true"],
              ["COMMERCIAL_TECHNICAL_READY", "false"],
              ["PAID_BETA_READY", "false"],
              ["PRODUCTION_READY", "false"],
              ["DATABASE_DEPLOYMENT_EVIDENCE_RECORDED", "true"],
              ["CR01_STATUS", "BLOCKED_LEDGER_INTEGRITY"],
              ["CR01_D02_STATUS", "ACCEPTED_DESIGN_ONLY"],
              ["LEDGER_TRANSITION_IMPLEMENTATION_AUTHORIZED", "false"],
              ["BACKUP_RESTORE_DRILL_PASS", "false"],
              ["RESTORE_RTO_STATUS", "NOT_ESTABLISHED"],
            ],
          },
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
            <div className="observed-chip"><span>{copy.observed}</span><strong>2026-08-08 · Asia/Shanghai</strong></div>
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
