import type { Metadata } from "next";
import { PortalPage } from "./portal-page";

export const metadata: Metadata = {
  title: { absolute: "Bin Zhang · DCELL 研究方向" },
  description:
    "为自主 AI 系统构建可信基础设施的研究工程师。DCELL 是以公开工程证据为基础的研究方向。",
  alternates: {
    canonical: "/",
    languages: { "zh-CN": "/", en: "/en/" },
  },
};

export default function Home() {
  return <PortalPage locale="zh" />;
}
