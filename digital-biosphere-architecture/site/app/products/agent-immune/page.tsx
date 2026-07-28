import type { Metadata } from "next";
import { AgentImmuneProductPage } from "../../agent-immune-product-page";

export const metadata: Metadata = {
  title: "Agent Immune | AI Agent 项目静态健康评估",
  description: "Agent Immune 使用静态仓库信号评估 AI Agent 项目健康状态，提供诊断、Problem / Cause / Fix 与 Recommendation Applicability。",
  keywords: ["Agent Immune", "agent-health", "AI Agent Health", "Static Repository Assessment", "Recommendation Applicability"],
  alternates: {
    canonical: "/products/agent-immune/",
    languages: { "zh-CN": "/products/agent-immune/", en: "/en/products/agent-immune/" },
  },
};

export default function AgentImmuneProduct() {
  return <AgentImmuneProductPage locale="zh" />;
}
