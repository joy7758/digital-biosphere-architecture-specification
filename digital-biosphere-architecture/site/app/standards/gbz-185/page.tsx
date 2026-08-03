import type { Metadata } from "next";
import { Gbz185Page } from "../../gbz-185-page";

export const metadata: Metadata = {
  title: "GB/Z 185 智能体互联与 TITMAS 可信执行、证据和审计衔接",
  description: "GB/Z 185 智能体互联与 TITMAS 可信执行、执行证据、验证和智能体审计扩展的研究映射；不构成符合性、认证或官方关联声明。",
  alternates: {
    canonical: "/standards/gbz-185/",
    languages: { "zh-CN": "/standards/gbz-185/", en: "/en/standards/gbz-185/" },
  },
};

export default function Gbz185Alignment() {
  return <Gbz185Page locale="zh" />;
}
