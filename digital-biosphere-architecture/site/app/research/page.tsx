import type { Metadata } from "next";
import { DirectoryPage } from "../directory-page";

export const metadata: Metadata = {
  title: "DCELL 研究方向",
  description: "自主 AI 系统的可信基础设施研究：agents、infrastructure、environments、evaluations 与自主实验循环。",
  alternates: {
    canonical: "/research/",
    languages: { "zh-CN": "/research/", en: "/en/research/" },
  },
};

export default function Research() {
  return <DirectoryPage locale="zh" section="research" />;
}
