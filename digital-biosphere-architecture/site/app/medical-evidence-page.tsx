"use client";

import { useState } from "react";
import type { Locale } from "./site-content";
import { Footer, Header } from "./site-shell";
import styles from "./medical-evidence/medical-evidence.module.css";

const SAMPLE_UDI = "999.TEST.UDI.DICOM.0001";

const copy = {
  zh: {
    breadcrumb: ["TITMAS 首页", "行业应用", "医疗证据 Demo"],
    eyebrow: "BOUNDED APPLICATION DEMO / 有界应用演示",
    title: "UDI-DICOM 证据链验证器",
    lead: "输入一个模拟 UDI，直观查看设备身份、影像对象与外部证据是否形成结构闭合。",
    banner: "概念演示 · 仅含模拟数据 · 非生产就绪 · 不代表真实合规或认证",
    label: "模拟 UDI",
    helper: "仅在当前浏览器中使用；不会上传，也不会查询真实登记库。",
    button: "验证证据链",
    reset: "重置",
    idle: "等待验证",
    closed: "结构闭合",
    invalid: "请输入一个模拟 UDI。",
    steps: [
      ["Identity", "设备身份", "解析模拟 UDI，并建立设备身份锚点。"],
      ["Imaging", "影像对象", "检查 DICOM 元数据与身份引用的映射。"],
      ["Evidence", "外部证据", "检查 Manifest 对影像与证据引用的闭合。"],
    ],
    resultTitle: "三段证据链结构闭合",
    resultBody: "该结果只说明演示数据之间的引用关系完整，不评价设备、临床流程或 AI 决策是否安全、正确或合规。",
    boundariesTitle: "这个 Demo 明确不证明什么",
    boundaries: ["不证明设备物理或临床安全", "不构成监管认证或合规背书", "不代表真实医院部署或生产就绪"],
  },
  en: {
    breadcrumb: ["TITMAS home", "Applications", "Medical Evidence Demo"],
    eyebrow: "BOUNDED APPLICATION DEMO",
    title: "UDI-DICOM Evidence Chain Validator",
    lead: "Enter a synthetic UDI to see whether device identity, an imaging object, and external evidence form a structurally closed chain.",
    banner: "Concept demo · Synthetic data only · Not production-ready · No compliance or certification claim",
    label: "Synthetic UDI",
    helper: "Used only in this browser. Nothing is uploaded and no real registry is queried.",
    button: "Validate evidence chain",
    reset: "Reset",
    idle: "Awaiting validation",
    closed: "Structurally closed",
    invalid: "Enter a synthetic UDI.",
    steps: [
      ["Identity", "Device identity", "Parse the synthetic UDI and establish an identity anchor."],
      ["Imaging", "Imaging object", "Check the mapping between DICOM metadata and the identity reference."],
      ["Evidence", "External evidence", "Check whether the Manifest closes its imaging and evidence references."],
    ],
    resultTitle: "Three-part evidence chain structurally closed",
    resultBody: "This result only shows that references in the demo data are complete. It does not assess whether a device, clinical workflow, or AI decision is safe, correct, or compliant.",
    boundariesTitle: "What this demo explicitly does not prove",
    boundaries: ["No physical or clinical safety claim", "No regulatory certification or compliance endorsement", "No real hospital deployment or production-readiness claim"],
  },
} as const;

export function MedicalEvidencePage({ locale }: { locale: Locale }) {
  const c = copy[locale];
  const root = locale === "zh" ? "/" : "/en/";
  const industries = locale === "zh" ? "/industries/" : "/en/industries/";
  const [udi, setUdi] = useState(SAMPLE_UDI);
  const [state, setState] = useState<"idle" | "complete" | "invalid">("idle");

  function validate() {
    setState(udi.trim() ? "complete" : "invalid");
  }

  function reset() {
    setUdi(SAMPLE_UDI);
    setState("idle");
  }

  return (
    <div className="site" lang={locale === "zh" ? "zh-CN" : "en"}>
      <Header locale={locale} section="medical" />
      <main className={styles.page}>
        <div className={styles.banner} role="note">{c.banner}</div>
        <section className={styles.hero}>
          <div className={styles.heroCopy}>
            <nav className={styles.breadcrumb} aria-label={locale === "zh" ? "面包屑导航" : "Breadcrumb"}>
              <a href={root}>{c.breadcrumb[0]}</a><span>/</span>
              <a href={industries}>{c.breadcrumb[1]}</a><span>/</span>
              <span aria-current="page">{c.breadcrumb[2]}</span>
            </nav>
            <p className={styles.eyebrow}>{c.eyebrow}</p>
            <h1>{c.title}</h1>
            <p className={styles.lead}>{c.lead}</p>
            <div className={styles.truthRow}>
              <code>SYNTHETIC_DATA_ONLY</code>
              <code>REAL_REGISTRY_LOOKUP=false</code>
            </div>
          </div>

          <div className={styles.validator}>
            <label htmlFor="medical-evidence-udi">{c.label}</label>
            <div className={styles.inputRow}>
              <input
                id="medical-evidence-udi"
                value={udi}
                onChange={(event) => {
                  setUdi(event.target.value);
                  setState("idle");
                }}
                aria-describedby="medical-evidence-helper medical-evidence-status"
                autoComplete="off"
                spellCheck={false}
              />
              <button type="button" onClick={validate}>{c.button}</button>
            </div>
            <p id="medical-evidence-helper" className={styles.helper}>{c.helper}</p>
            {state === "invalid" && <p id="medical-evidence-status" className={styles.error} role="alert">{c.invalid}</p>}

            <ol className={styles.chain} aria-live="polite">
              {c.steps.map(([name, label, description], index) => (
                <li key={name} className={state === "complete" ? styles.complete : ""}>
                  <span className={styles.stepIndex}>0{index + 1}</span>
                  <div>
                    <code>{name}</code>
                    <strong>{label}</strong>
                    <p>{description}</p>
                  </div>
                  <span className={styles.stepState}>{state === "complete" ? "✓" : "·"}</span>
                </li>
              ))}
            </ol>

            <div className={`${styles.result} ${state === "complete" ? styles.resultVisible : ""}`}>
              <span>{state === "complete" ? c.closed : c.idle}</span>
              <strong>{c.resultTitle}</strong>
              <p>{c.resultBody}</p>
              {state === "complete" && <button type="button" onClick={reset}>{c.reset}</button>}
            </div>
          </div>
        </section>

        <section className={styles.boundaries}>
          <p>INTERPRETATION BOUNDARY</p>
          <h2>{c.boundariesTitle}</h2>
          <div>{c.boundaries.map((item) => <span key={item}>{item}</span>)}</div>
        </section>
      </main>
      <Footer locale={locale} />
    </div>
  );
}
