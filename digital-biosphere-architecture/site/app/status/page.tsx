import type { Metadata } from "next";
import { StatusPage } from "../status-page";

export const metadata: Metadata = {
  title: "当前状态",
  description: "DCELL 研究方向、公开工程证据成熟度与保留的 TITMAS 历史状态。",
  alternates: {
    canonical: "/status/",
    languages: { "zh-CN": "/status/", en: "/en/status/" },
  },
};

export default function ChineseStatus() {
  return <StatusPage locale="zh" />;
}
