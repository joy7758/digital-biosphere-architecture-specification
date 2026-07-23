import type { Metadata } from "next";
import { PortalPage } from "./portal-page";

export const metadata: Metadata = {
  title: "TITMAS 可信多智能体基础设施开发者社区",
  description:
    "围绕开放规范、适配器契约、符合性测试和参考实现边界建设可信多智能体基础设施。",
  alternates: {
    canonical: "/",
    languages: { "zh-CN": "/", en: "/en/" },
  },
};

export default function Home() {
  return <PortalPage locale="zh" />;
}
