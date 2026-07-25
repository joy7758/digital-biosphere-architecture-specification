import type { Metadata } from "next";
import { PortalPage } from "./portal-page";

export const metadata: Metadata = {
  title: "TITMAS 可信多智能体基础设施开发者社区",
  description:
    "为长期运行的多智能体系统共同建设开放、可验证的可信基础设施规则。",
  alternates: {
    canonical: "/",
    languages: { "zh-CN": "/", en: "/en/" },
  },
};

export default function Home() {
  return <PortalPage locale="zh" />;
}
