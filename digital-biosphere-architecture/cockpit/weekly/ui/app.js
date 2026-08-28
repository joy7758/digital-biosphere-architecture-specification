(() => {
  "use strict";
  const snapshot = JSON.parse(document.getElementById("weekly-snapshot").textContent);
  const el = (id) => document.getElementById(id);
  const text = (value, fallback = "未知") => value === undefined || value === null || value === "" ? fallback : String(value);
  const escapeHtml = (value) => text(value).replace(/[&<>'"]/g, (char) => ({"&":"&amp;","<":"&lt;",">":"&gt;","'":"&#39;",'"':"&quot;"}[char]));
  const severity = (status) => {
    const value = text(status, "UNKNOWN").toUpperCase();
    if (["PASS", "NORMAL", "STABLE", "MONITORED", "AVAILABLE"].includes(value)) return ["normal", "正常"];
    if (["FRESH", "CURRENT_SNAPSHOT"].includes(value)) return ["normal", "当前证据"];
    if (["ATTENTION", "PASS_WITH_NOT_ASSESSED", "PARTIAL", "STALE"].includes(value)) return ["attention", value === "STALE" ? "已过期" : "需关注"];
    if (["BLOCKED", "FAILED", "DISCOVERY_UNAVAILABLE"].includes(value)) return ["blocked", "受阻"];
    if (value === "DISCOVERED") return ["unknown", "待确认候选"];
    return ["unknown", "未评估"];
  };
  const pill = (status) => { const [klass, label] = severity(status); return `<span class="status-pill ${klass}">${escapeHtml(label)} · ${escapeHtml(status)}</span>`; };
  const first = (...values) => values.find((item) => item !== undefined && item !== null && item !== "") || "未知";

  const projects = snapshot.projects || snapshot.project_views || [];
  const discoveries = snapshot.discoveries || [];
  const decisions = snapshot.decisions || [];
  const changes = Array.isArray(snapshot.changes) ? snapshot.changes : Object.entries(snapshot.changes || {}).flatMap(([group, items]) => (items || []).map((summary) => ({group, summary})));
  const blindSpots = snapshot.blind_spots || [];
  const cells = snapshot.cell_runs || [];

  const [overallClass, overallLabel] = severity(snapshot.overall_status);
  el("overall-signal").innerHTML = `${pill(snapshot.overall_status)}<div style="margin-top:16px">${escapeHtml(overallLabel)}，等待人工判断</div>`;
  el("weekly-sentence").textContent = text(snapshot.weekly_sentence_zh);
  el("hero-metrics").innerHTML = [
    ["项目", projects.length], ["新发现", discoveries.length], ["待决定", decisions.length], ["盲区", blindSpots.length]
  ].map(([label, value]) => `<div><dt>${label}</dt><dd>${value}</dd></div>`).join("");
  const firstDecision = decisions[0] || {};
  el("hero-decision").innerHTML = `<strong>最先查看：</strong>${escapeHtml(first(firstDecision.title_zh, "当前没有登记的决定"))}`;
  el("as-of").textContent = `观察时间 ${text(first(snapshot.observed_at, snapshot.as_of))}`;

  el("decision-list").innerHTML = decisions.length ? decisions.map((item, index) => `
    <article class="decision-card">
      <div class="meta-row"><span>决定 ${String(index + 1).padStart(2, "0")}</span><span>需人工判断</span></div>
      <h3>${escapeHtml(first(item.title_zh, item.title, item.decision_needed, "待人工决定"))}</h3>
      <p>${escapeHtml(first(item.why_zh, item.why, item.summary, item.human_explanation, "查看来源证据后决定。"))}</p>
      <div class="meta-row"><span>负责人 ${escapeHtml(first(item.owner_conversation, "DBA 专用对话"))}</span></div>
    </article>`).join("") : `<article class="decision-card"><h3>本周没有登记的决定</h3><p>这不表示没有风险；请同时查看盲区。</p></article>`;

  const querySource = snapshot.preset_queries || [
    {question:"哪些项目需要关注？", answer:"查看项目卡片中的“需关注”和“未评估”状态。"},
    {question:"本周出现了什么新信号？", answer:"查看新发现与变化章节。"},
    {question:"哪些内容仍不可见？", answer:"查看盲区与边界章节。"}
  ];
  const queries = Array.isArray(querySource) ? querySource : Object.entries(querySource).map(([question, answer]) => ({question, answer}));
  el("preset-query").innerHTML = queries.map((item, index) => `<option value="${index}">${escapeHtml(first(item.question, item.label, `固定问题 ${index + 1}`))}</option>`).join("");
  el("run-query").addEventListener("click", () => {
    const item = queries[Number(el("preset-query").value)] || {};
    el("query-answer").textContent = text(first(item.answer, item.response, item.summary), "当前快照没有可回答证据。");
    el("query-answer").classList.add("visible");
  });

  el("discovery-list").innerHTML = discoveries.slice(0, 9).map((item) => `
    <article class="signal-card">
      ${pill(first(item.current_state, item.observed_state, item.status))}
      <h3>${escapeHtml(first(item.title_zh, item.display_name_zh, item.display_name, item.subject, item.title, item.project_id, "发现信号"))}</h3>
      <p>${escapeHtml(first(item.note, item.kind, item.relationship, "仅作为候选观察。"))}</p>
      <div class="meta-row"><span>${escapeHtml(first(item.source_reference))}</span></div>
    </article>`).join("") || `<p>当前没有已准入的新发现。</p>`;

  el("change-list").innerHTML = changes.map((item) => `
    <article class="timeline-item">
      <time>${escapeHtml(first(item.observed_at, snapshot.observed_at, snapshot.as_of))}</time>
      <div><h3>${escapeHtml(first(item.title, item.change, item.group === "improved" ? "已改善" : item.group === "worsened" ? "需关注变化" : "仍未知"))}</h3><p>${escapeHtml(first(item.human_explanation, item.summary, item.detail, "没有补充说明。"))}</p></div>
    </article>`).join("") || `<article class="timeline-item"><time>${escapeHtml(first(snapshot.observed_at, snapshot.as_of))}</time><div><h3>首次快照，无周间比较</h3><p>状态为未评估，不推测变化趋势。</p></div></article>`;

  el("project-grid").innerHTML = projects.map((project, index) => `
    <article class="project-card">
      <h3>${escapeHtml(first(project.display_name_zh, project.display_name, project.name, project.project_id))}</h3>
      ${pill(first(project.status, project.state))}
      <p><strong>${escapeHtml(first(project.status_zh, "状态待解释"))}</strong><br>${escapeHtml(first(project.why_zh, project.human_summary, project.summary, project.explanation, "没有可用的人类解释。"))}<br><br>${escapeHtml(first(project.attention_zh, project.impact_zh, ""))}</p>
    </article>`).join("");

  el("blindspot-list").innerHTML = blindSpots.map((item) => `
    <article class="blindspot"><h3>${escapeHtml(first(item.title_zh, item.title, item.subject, "未评估盲区"))}</h3><p>${escapeHtml(first(item.impact_zh, item.human_explanation, item.summary, item.reason, "缺少足够证据。"))}</p></article>`).join("") || `<article class="blindspot"><h3>盲区清单为空</h3><p>空清单不构成全面覆盖证明。</p></article>`;

  const projectEvidence = projects.map((project) => `<div class="cell-row">项目标识 · ${escapeHtml(first(project.project_id))}<br>证据 · ${escapeHtml((project.technical_evidence || []).join(" · "))}</div>`).join("");
  const cellEvidence = cells.map((cell) => `<div class="cell-row">细胞标识 · ${escapeHtml(first(cell.cell_id, cell.id))}<br>${pill(first(cell.status))}</div>`).join("");
  el("technical-evidence").innerHTML = `<div class="cell-row">快照编号 · ${escapeHtml(snapshot.snapshot_id)}</div>${projectEvidence}${cellEvidence}`;
})();
