import type { Metadata } from "next";
import type { CSSProperties } from "react";
import styles from "./digital-cell.module.css";

export const metadata: Metadata = {
  title: "TITMAS Digital Cell Demo v0.1",
  description: "一个展示 AI Agent 如何具备身份、边界、执行证据和健康状态的最小参考实现。",
  alternates: { canonical: "/digital-cell/" },
  openGraph: {
    title: "TITMAS Digital Cell Demo v0.1",
    description: "A minimal reference implementation of an observable, verifiable, and health-assessable digital agent.",
    images: ["/digital-cell/digital-cell-architecture.png"],
  },
};

const objects = [
  ["Identity", "身份", "标识主体、版本、用途与来源。"],
  ["Boundary", "边界", "声明允许行为、禁止行为与能力限制。"],
  ["Evidence", "证据", "记录意图、执行、结果与完整性摘要。"],
  ["Health", "健康", "从已有记录派生可观察状态，不构成认证。"],
  ["Memory", "记忆", "保留执行、失败、恢复与演化历史。"],
  ["Reputation", "信誉", "汇总可靠性和证据质量历史。"],
] as const;

export default function DigitalCellPage() {
  return (
    <main className={styles.page}>
      <header className={styles.header}>
        <a className={styles.brand} href="/" aria-label="返回 TITMAS 首页">
          <span className={styles.mark} aria-hidden="true"><i /><i /><i /><i /></span>
          <span><strong>TITMAS</strong><small>Infrastructure Developer Community</small></span>
        </a>
        <nav aria-label="Digital Cell 页面导航">
          <a href="#architecture">架构</a><a href="#evidence">验证</a><a href="#run">运行</a>
          <a href="https://github.com/joy7758/titmas-demo/releases/tag/v0.1.0">GitHub Release</a>
        </nav>
      </header>
      <section className={styles.hero}>
        <div>
          <p className={styles.eyebrow}>REFERENCE DEMO · v0.1.0</p>
          <h1>让 Agent 的存在<br />变得可观察。</h1>
          <p className={styles.lead}>TITMAS Digital Cell Demo 是一个最小参考实现，展示 AI Agent 如何具备身份、边界、执行证据和健康状态。</p>
          <div className={styles.actions}>
            <a className={styles.primary} href="https://github.com/joy7758/titmas-demo/releases/tag/v0.1.0">查看公开 Release</a>
            <a className={styles.secondary} href="#architecture">理解 Digital Cell</a>
          </div>
          <div className={styles.statusRow} aria-label="发布状态"><code>REFERENCE_COMPLETE</code><code>REPLAY_PASS</code><code>APACHE-2.0</code></div>
        </div>
        <div className={styles.cellVisual} aria-label="六个 Digital Cell 对象的组合示意">
          <div className={styles.core}>Digital<br />Cell</div>
          {objects.map(([name], index) => <span key={name} className={styles.orbitItem} style={{ "--index": index } as CSSProperties}>{name}</span>)}
        </div>
      </section>
      <section className={styles.problem}>
        <p className={styles.sectionTag}>WHY DIGITAL CELL</p>
        <div className={styles.problemLead}><h2>能执行，不等于能被理解。</h2><p>未来 Agent 系统需要回答四个基础问题：它是谁、允许做什么、实际做了什么、发生异常后处于什么状态。</p></div>
        <div className={styles.questionGrid}>
          <article><span>01</span><strong>Who?</strong><p>可追溯身份</p></article><article><span>02</span><strong>Within what boundary?</strong><p>明确行为边界</p></article><article><span>03</span><strong>What happened?</strong><p>执行证据</p></article><article><span>04</span><strong>What state now?</strong><p>健康观察</p></article>
        </div>
      </section>
      <section className={styles.architecture} id="architecture">
        <div className={styles.sectionHeading}><p className={styles.sectionTag}>DIGITAL CELL ARCHITECTURE</p><h2>六个简单、受限、可组合的对象</h2><p>Digital Cell 不创造无限自治中心。每个对象只有明确职责，Evidence 不等于 Permission，Health 不等于 Certification，Reputation 不等于 Authority。</p></div>
        <div className={styles.objectGrid}>{objects.map(([name, zh, description], index) => <article key={name}><span>0{index + 1}</span><h3>{name}</h3><strong>{zh}</strong><p>{description}</p></article>)}</div>
        <figure className={styles.figure}><img src="/digital-cell/digital-cell-architecture.png" alt="Digital Cell v0.1 架构：Identity、Boundary、Evidence、Health、Memory 和 Reputation" /><figcaption>Digital Cell v0.1 Architecture · 最小参考模型，不是生产架构。</figcaption></figure>
      </section>
      <section className={styles.lifecycle}>
        <div className={styles.sectionHeading}><p className={styles.sectionTag}>BOUNDED LIFECYCLE</p><h2>一次执行，成为一段可追溯历史。</h2></div>
        <div className={styles.lifecycleFlow}>{[["Birth", "出生"], ["Execution", "执行"], ["Evidence", "证据"], ["Health", "健康评估"], ["Recovery", "恢复"], ["Evolution", "演化状态"]].map(([en, zh], index) => <div key={en}><span>0{index + 1}</span><strong>{en}</strong><small>{zh}</small></div>)}</div>
        <figure className={styles.figure}><img src="/digital-cell/digital-cell-lifecycle.png" alt="Digital Cell 从出生、执行、证据、健康评估、恢复到演化状态的生命周期" /><figcaption>Lifecycle view · 状态变化有记录，但不产生认证或自治治理权力。</figcaption></figure>
      </section>
      <section className={styles.evidence} id="evidence">
        <div><p className={styles.sectionTag}>VERIFIED REFERENCE RUN</p><h2>可复现，不被过度解释。</h2><p>冻结的参考运行通过 7 项测试，生成 12 条证据记录，并通过确定性重放和 SHA-256 完整性检查。</p><div className={styles.metrics}><div><strong>7/7</strong><span>Tests passed</span></div><div><strong>12</strong><span>Evidence records</span></div><div><strong>PASS</strong><span>Deterministic replay</span></div></div></div>
        <figure className={styles.reportFigure}><img src="/digital-cell/digital-cell-report.png" alt="Digital Cell 参考执行报告，显示成功、证据数量、健康状态和重放结果" /></figure>
      </section>
      <section className={styles.run} id="run">
        <div><p className={styles.sectionTag}>RUN LOCALLY</p><h2>一个实现，一个入口，零第三方依赖。</h2><p>需要 Python 3。Release 和源码均位于公开 GitHub 仓库。</p></div>
        <pre><code>{`git clone https://github.com/joy7758/titmas-demo.git
cd titmas-demo/examples/digital-cell
python3 -m unittest discover -s tests -v
python3 run.py`}</code></pre><a href="https://github.com/joy7758/titmas-demo">打开 GitHub 仓库 →</a>
      </section>
      <section className={styles.boundary}>
        <p className={styles.sectionTag}>INTERPRETATION BOUNDARY</p><h2>这个 Demo 明确不证明什么</h2><div><span>NO DIGITAL LIFE CLAIM</span><span>NO AI CONSCIOUSNESS CLAIM</span><span>NO PRODUCTION CERTIFICATION</span><span>NO UNIVERSAL SAFETY CLAIM</span></div><p>它只展示一个 Agent 如何变得可观察、可验证并可进行健康状态评估。健康视图不是安全保证，证据完整不等于智能正确。</p>
      </section>
      <footer className={styles.footer}><div><strong>TITMAS Digital Cell Demo</strong><span>Reference implementation · Apache-2.0</span></div><div><a href="/">TITMAS 首页</a><a href="https://github.com/joy7758/titmas-demo/releases/tag/v0.1.0">Release v0.1.0</a></div></footer>
    </main>
  );
}
