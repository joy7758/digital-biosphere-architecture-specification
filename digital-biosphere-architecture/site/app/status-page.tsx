import { content, gateRows, repositoryBaselines, type Locale } from "./site-content";
import { Footer, Header } from "./site-shell";

export function StatusPage({ locale }: { locale: Locale }) {
  const c = content[locale];
  const copy = locale === "zh"
    ? {
        eyebrow: "VERIFIABLE STATUS / 可验证状态",
        title: "TITMAS Stage 5.2 外部开发者试用进行中",
        lead: "E01 已获得有界只读访问，当前等待参与者行动。试用进行中不等于完成、采用、认证或生产就绪。",
        observed: "观察时间",
        current: "当前 Stage 5.2 状态",
        baselines: "远程基线",
        gates: "验证闸门",
        visibility: "可见性",
        next: "下一步",
        nextBody: "等待 E01 参与者通过私有 Fork + Pull Request 路径行动；新的参与者名额、商业访问和标准变更均需单独 Human Decision。",
        back: "返回首页",
        groups: [
          {
            title: "技术基础设施",
            rows: [
              ["TITMAS_STAGE_5_PRIVATE_PREVIEW_OPERATIONAL", "true"],
              ["TITMAS_STAGE_5_1_PRIVATE_TRIAL_CHANNEL_READY", "true"],
            ],
          },
          {
            title: "当前外部试用",
            rows: [
              ["E01_STATUS", "IN_PROGRESS_WAITING_FOR_PARTICIPANT_ACTION"],
              ["E01_ACCESS_MODE", "ACTIVE_READ_ONLY"],
              ["E01_CONTRIBUTION_PATH", "PRIVATE_FORK_PULL_REQUEST"],
              ["FIRST_EXTERNAL_HUMAN_DEVELOPER_TRIAL_COMPLETE", "false"],
            ],
          },
          {
            title: "候选获取",
            rows: [
              ["PUBLIC_TRIAL_INTEREST_ENTRY_ACTIVE", "true"],
              ["COMPENSATED_RECRUITMENT_DEMAND_SUBMITTED", "true"],
              ["COMPENSATED_RECRUITMENT_PUBLICATION_CONFIRMED", "false"],
            ],
            note: "独立有偿开发者招募：需求已提交；平台发布审核等待中。",
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
        title: "TITMAS Stage 5.2 external developer trial in progress",
        lead: "E01 has bounded read-only access and is waiting for participant action. In progress does not mean complete, adopted, certified, or production-ready.",
        observed: "Observed at",
        current: "Current Stage 5.2 status",
        baselines: "Remote baselines",
        gates: "Validation gates",
        visibility: "Visibility",
        next: "Next step",
        nextBody: "Wait for E01 participant action through the private Fork + Pull Request path. Any new participant slot, commercial access, or standard change requires a separate Human Decision.",
        back: "Back to home",
        groups: [
          {
            title: "Technical infrastructure",
            rows: [
              ["TITMAS_STAGE_5_PRIVATE_PREVIEW_OPERATIONAL", "true"],
              ["TITMAS_STAGE_5_1_PRIVATE_TRIAL_CHANNEL_READY", "true"],
            ],
          },
          {
            title: "Current external trial",
            rows: [
              ["E01_STATUS", "IN_PROGRESS_WAITING_FOR_PARTICIPANT_ACTION"],
              ["E01_ACCESS_MODE", "ACTIVE_READ_ONLY"],
              ["E01_CONTRIBUTION_PATH", "PRIVATE_FORK_PULL_REQUEST"],
              ["FIRST_EXTERNAL_HUMAN_DEVELOPER_TRIAL_COMPLETE", "false"],
            ],
          },
          {
            title: "Candidate intake",
            rows: [
              ["PUBLIC_TRIAL_INTEREST_ENTRY_ACTIVE", "true"],
              ["COMPENSATED_RECRUITMENT_DEMAND_SUBMITTED", "true"],
              ["COMPENSATED_RECRUITMENT_PUBLICATION_CONFIRMED", "false"],
            ],
            note: "Independent compensated developer recruitment: Demand submitted; platform publication review pending.",
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
      <main>
        <section className="status-hero">
          <div className="section-shell">
            <p className="section-kicker">{copy.eyebrow}</p>
            <h1>{copy.title}</h1>
            <p>{copy.lead}</p>
            <div className="observed-chip"><span>{copy.observed}</span><strong>2026-07-29 · Asia/Shanghai</strong></div>
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
