"use client";

import { useEffect, useRef, useState } from "react";
import type { Locale } from "../site-content";

const AUTO_ADVANCE_MS = 8000;

const slides = {
  zh: [
    {
      id: "dcell-research-direction",
      eyebrow: "BIN ZHANG / RESEARCH ENGINEER",
      title: "为自主 AI 系统构建可信基础设施",
      description: "DCELL 是研究方向：探索证据驱动、有界、可独立识别、经验连续、可替换且可演化的自主 AI 系统。这里区分已实现证据、实验支持、原型、研究方向与未来假设。",
      primary: ["查看公开证据", "#public-evidence"],
      secondary: ["理解 DCELL", "#dcell"],
      status: "DCELL · RESEARCH_DIRECTION",
    },
    {
      id: "autonomous-experimental-loops",
      eyebrow: "AUTONOMOUS EXPERIMENTAL LOOPS / 自主实验循环",
      title: "让自主实验循环可检查、可复现、可约束",
      description: "公开工作聚焦执行证据、Agent 评价、身份与来源、受限行动，以及失败和经验如何被保留；不把实验结果升级为自治演化已经实现。",
      primary: ["研究问题", "#problem"],
      secondary: ["研究索引", "/research/"],
      status: "EVIDENCE · EVALUATION · BOUNDED ACTION",
    },
    {
      id: "maturity-boundaries",
      eyebrow: "IMPLEMENTED ≠ RESEARCH_DIRECTION",
      title: "成熟度标签是公开叙事的一部分",
      description: "IMPLEMENTED、EXPERIMENTALLY_SUPPORTED、PROTOTYPE、RESEARCH_DIRECTION 与 FUTURE_HYPOTHESIS 分别陈述，避免把仓库、演示或研究设想混写成完整系统。",
      primary: ["查看成熟度边界", "#dcell"],
      secondary: ["读取机器入口", "/llms.txt"],
      status: "NO DIGITAL-LIFE OR AGI CLAIM",
    },
  ],
  en: [
    {
      id: "dcell-research-direction",
      eyebrow: "BIN ZHANG / RESEARCH ENGINEER",
      title: "Building trustworthy infrastructure for autonomous AI systems",
      description: "DCELL is a research direction exploring evidence-driven, bounded, independently identifiable, experience-preserving, replaceable, and evolvable autonomous AI systems. Implemented evidence, experimental support, prototypes, research directions, and future hypotheses remain distinct.",
      primary: ["View public evidence", "#public-evidence"],
      secondary: ["Understand DCELL", "#dcell"],
      status: "DCELL · RESEARCH_DIRECTION",
    },
    {
      id: "autonomous-experimental-loops",
      eyebrow: "AUTONOMOUS EXPERIMENTAL LOOPS",
      title: "Make autonomous experimental loops inspectable, reproducible, and bounded",
      description: "The public work focuses on execution evidence, agent evaluation, identity and provenance, bounded action, and retention of failures and experience. It does not claim autonomous evolution has been achieved.",
      primary: ["See the research problem", "#problem"],
      secondary: ["Open research index", "/en/research/"],
      status: "EVIDENCE · EVALUATION · BOUNDED ACTION",
    },
    {
      id: "maturity-boundaries",
      eyebrow: "IMPLEMENTED ≠ RESEARCH_DIRECTION",
      title: "Maturity labels are part of the public argument",
      description: "IMPLEMENTED, EXPERIMENTALLY_SUPPORTED, PROTOTYPE, RESEARCH_DIRECTION, and FUTURE_HYPOTHESIS are stated separately, so repositories, demos, and hypotheses are not presented as one complete system.",
      primary: ["Review maturity boundaries", "#dcell"],
      secondary: ["Read the machine entry", "/llms.txt"],
      status: "NO DIGITAL-LIFE OR AGI CLAIM",
    },
  ],
} as const;

export function HeroCarousel({ locale }: { locale: Locale }) {
  const items = slides[locale];
  const [activeIndex, setActiveIndex] = useState(0);
  const [userPaused, setUserPaused] = useState(false);
  const [interactionPaused, setInteractionPaused] = useState(false);
  const [reducedMotion, setReducedMotion] = useState(true);
  const regionRef = useRef<HTMLElement>(null);

  useEffect(() => {
    const query = window.matchMedia("(prefers-reduced-motion: reduce)");
    const syncPreference = () => setReducedMotion(query.matches);
    syncPreference();
    query.addEventListener("change", syncPreference);
    return () => query.removeEventListener("change", syncPreference);
  }, []);

  useEffect(() => {
    if (reducedMotion || userPaused || interactionPaused) return;
    const timer = window.setInterval(() => {
      setActiveIndex((current) => (current + 1) % items.length);
    }, AUTO_ADVANCE_MS);
    return () => window.clearInterval(timer);
  }, [interactionPaused, items.length, reducedMotion, userPaused]);

  function select(index: number) {
    setActiveIndex((index + items.length) % items.length);
    setUserPaused(true);
  }

  function handleKeyDown(event: React.KeyboardEvent<HTMLElement>) {
    if (event.key !== "ArrowLeft" && event.key !== "ArrowRight") return;
    event.preventDefault();
    select(activeIndex + (event.key === "ArrowRight" ? 1 : -1));
  }

  const current = items[activeIndex];
  const currentLabel = locale === "zh"
    ? `第 ${activeIndex + 1} 张，共 ${items.length} 张：${current.status}`
    : `Slide ${activeIndex + 1} of ${items.length}: ${current.status}`;

  return (
    <section
      className="hero hero-carousel"
      data-section-id="hero-carousel"
      aria-roledescription={locale === "zh" ? "轮播" : "carousel"}
      aria-label={locale === "zh" ? "DCELL 研究重点" : "DCELL research highlights"}
      onMouseEnter={() => setInteractionPaused(true)}
      onMouseLeave={() => setInteractionPaused(false)}
      onFocusCapture={() => setInteractionPaused(true)}
      onBlurCapture={(event) => {
        if (!event.currentTarget.contains(event.relatedTarget as Node | null)) setInteractionPaused(false);
      }}
      onKeyDown={handleKeyDown}
      ref={regionRef}
    >
      <div className="hero-grid" aria-hidden="true">
        <div className="orbit orbit-a" />
        <div className="orbit orbit-b" />
        <div className="node node-a" />
        <div className="node node-b" />
        <div className="node node-c" />
      </div>

      <div className="hero-carousel-stage">
        {items.map((slide, index) => (
          <article
            className="hero-content hero-slide"
            hidden={index !== activeIndex}
            key={slide.id}
            aria-roledescription={locale === "zh" ? "幻灯片" : "slide"}
            aria-label={locale === "zh" ? `${index + 1}/${items.length}` : `${index + 1} of ${items.length}`}
          >
            <div className="hero-badge"><span />{slide.status}</div>
            <p className="eyebrow">{slide.eyebrow}</p>
            <h1>{slide.title}</h1>
            <p className="hero-lead">{slide.description}</p>
            <div className="hero-actions">
              <a className="button button-primary" href={slide.primary[1]}>{slide.primary[0]}</a>
              <a className="button button-secondary" href={slide.secondary[1]}>{slide.secondary[0]}</a>
            </div>
            {slide.id === "media-evidence" && (
              <p className="truth-notice">
                <span>i</span>
                {locale === "zh"
                  ? "本地合成参考实现；不提供内容真实性认证、身份认证、法律证据或生产审核服务。"
                  : "Local synthetic reference implementation; no content-truth, identity, legal-evidence, or production-review service."}
              </p>
            )}
          </article>
        ))}
      </div>

      <div className="hero-carousel-controls">
        <button type="button" onClick={() => select(activeIndex - 1)} aria-label={locale === "zh" ? "上一张" : "Previous slide"}>←</button>
        <div className="hero-carousel-dots" role="group" aria-label={locale === "zh" ? "选择轮播页" : "Choose a slide"}>
          {items.map((slide, index) => (
            <button
              type="button"
              key={slide.id}
              onClick={() => select(index)}
              aria-label={locale === "zh" ? `显示第 ${index + 1} 张：${slide.status}` : `Show slide ${index + 1}: ${slide.status}`}
              aria-current={index === activeIndex ? "true" : undefined}
            >
              <span aria-hidden="true">{String(index + 1).padStart(2, "0")}</span>
            </button>
          ))}
        </div>
        <button type="button" onClick={() => select(activeIndex + 1)} aria-label={locale === "zh" ? "下一张" : "Next slide"}>→</button>
        <span className="sr-only" aria-live={userPaused ? "polite" : "off"}>{currentLabel}</span>
      </div>
    </section>
  );
}

export const heroCarouselContract = {
  slideCount: 3,
  autoAdvanceMs: AUTO_ADVANCE_MS,
  pausesAfterUserAction: true,
  pausesOnHoverOrFocus: true,
  disablesAutoAdvanceForReducedMotion: true,
  serverRenderedFirstSlide: true,
} as const;
