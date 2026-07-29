import type { Metadata } from "next";
import { PortalPage } from "./portal-page";

export const metadata: Metadata = {
  title: { absolute: "夏日之海 · titmas" },
  description:
    "面向自治 AI 智能体生态的可信基础设施层；制造业等行业场景是基础设施应用示例。",
  alternates: {
    canonical: "/",
    languages: { "zh-CN": "/", en: "/en/" },
  },
};

export default function Home() {
  return <PortalPage locale="zh" />;
}
