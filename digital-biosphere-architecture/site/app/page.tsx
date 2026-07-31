import type { Metadata } from "next";
import { PortalPage } from "./portal-page";

export const metadata: Metadata = {
  title: { absolute: "山西游骑兵电子商务有限公司" },
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
