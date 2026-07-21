import type { Metadata } from "next";
import { PortalPage } from "./portal-page";

export const metadata: Metadata = {
  title: "可信多智能体基础设施",
  description:
    "面向长期运行、多智能体协作和可验证演化的可信基础设施。",
  alternates: {
    canonical: "/",
    languages: { "zh-CN": "/", en: "/en/" },
  },
};

export default function Home() {
  return <PortalPage locale="zh" />;
}
