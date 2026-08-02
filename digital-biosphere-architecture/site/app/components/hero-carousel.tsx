"use client";

import { useEffect, useRef, useState } from "react";
import type { Locale } from "../site-content";

const AUTO_ADVANCE_MS = 8000;

const slides = {
  zh: [
    {
      id: "titmas-infrastructure",
      eyebrow: "TITMAS / 开放可信互操作基础设施",
      title: "TITMAS 可信多智能体基础设施",
      description: "让智能体的身份、授权、执行、证据和决定可以被描述、验证和复核。",
      primary: ["了解 TITMAS", "#about"],
      secondary: ["查看当前状态", "/status/"],
      status: "基础设施入口",
    },
    {
      id: "media-evidence",
      eyebrow: "媒体证据 / 本地合成参考实现",
      title: "让人工智能生成内容拥有可复核的责任链",
      description: "TITMAS 媒体证据记录生成请求、授权、智能体执行、多来源证据、异议处理和审核决定。",
      primary: ["运行媒体证据演示", "/demo/media-evidence/"],
      secondary: ["查看广电视听应用", "/industry/media-evidence/"],
      status: "媒体证据场景配置",
    },
    {
      id: "medical-evidence",
      eyebrow: "医疗证据 / 行业方向",
      title: "医疗影像与设备证据基础设施",
      description: "通过医疗器械唯一标识、医学数字成像和通信元数据及证据对象，支持医疗影像流程的离线复核。",
      primary: ["运行医疗证据演示", "/demo/medical-evidence/"],
      secondary: ["查看医疗行业应用", "/industry/medical-evidence/"],
      status: "医疗证据行业方向",
    },
  ],
  en: [
    {
      id: "titmas-infrastructure",
      eyebrow: "TITMAS / OPEN TRUST INTEROPERABILITY INFRASTRUCTURE",
      title: "TITMAS trustworthy multi-agent infrastructure",
      description: "Make agent identity, authorization, execution, evidence, and decisions describable, verifiable, and reviewable.",
      primary: ["Understand TITMAS", "/en/#about"],
      secondary: ["View current status", "/en/status/"],
      status: "Infrastructure entry",
    },
    {
      id: "media-evidence",
      eyebrow: "MEDIA EVIDENCE / LOCAL SYNTHETIC REFERENCE",
      title: "Give AI-generated media a reviewable accountability chain",
      description: "TITMAS Media Evidence records creation requests, authorization records, agent execution, multi-source evidence, challenges, and review decisions.",
      primary: ["Run the media evidence demo", "/en/demo/media-evidence/"],
      secondary: ["View the media application", "/en/industry/media-evidence/"],
      status: "Media evidence profile",
    },
    {
      id: "medical-evidence",
      eyebrow: "MEDICAL EVIDENCE / INDUSTRY DIRECTION",
      title: "Medical imaging and device evidence infrastructure",
      description: "Use device identifiers, DICOM metadata, and evidence objects to support offline review of medical-imaging workflows.",
      primary: ["Run the medical evidence demo", "/en/demo/medical-evidence/"],
      secondary: ["View the medical application", "/en/industry/medical-evidence/"],
      status: "Medical evidence direction",
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
      aria-label={locale === "zh" ? "TITMAS 重点入口" : "TITMAS featured entries"}
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
            {slide.id === "titmas-infrastructure" && (
              <span
                className="hero-brand-logo"
                role="img"
                aria-label={locale === "zh" ? "夏日之海 Logo" : "titmas logo"}
              />
            )}
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
