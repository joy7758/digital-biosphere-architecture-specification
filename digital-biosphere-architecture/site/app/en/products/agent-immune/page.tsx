import type { Metadata } from "next";
import { AgentImmuneProductPage } from "../../../agent-immune-product-page";

export const metadata: Metadata = {
  title: "Agent Immune | Static Health Assessment for AI Agent Projects",
  description: "Agent Immune assesses static repository signals and reports health, diagnosis, Problem / Cause / Fix, and Recommendation Applicability.",
  keywords: ["Agent Immune", "agent-health", "AI Agent Health", "Static Repository Assessment", "Recommendation Applicability"],
  alternates: {
    canonical: "/en/products/agent-immune/",
    languages: { "zh-CN": "/products/agent-immune/", en: "/en/products/agent-immune/" },
  },
};

export default function AgentImmuneProduct() {
  return <AgentImmuneProductPage locale="en" />;
}
