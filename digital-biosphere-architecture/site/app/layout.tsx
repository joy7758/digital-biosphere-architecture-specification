import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  metadataBase: new URL("https://redcrag.cn"),
  title: {
    default: "TITMAS 可信多智能体基础设施开发者社区",
    template: "%s · TITMAS",
  },
  description:
    "TITMAS 是面向自治 AI 智能体生态的可信基础设施层；制造业等行业场景是基础设施应用示例。",
  keywords: [
    "AI Agent Infrastructure",
    "Trusted Agent Execution",
    "Verifiable Execution Evidence",
    "Industrial AI Agent Governance",
    "Multi-Agent System Infrastructure",
    "Autonomous Digital Ecosystem",
    "Space Agent Evidence Profile",
    "Autonomous Space Systems",
    "AI Agent Governance",
    "Execution Evidence",
    "Digital Biosphere",
    "智能体基础设施",
    "AI执行证明",
    "智能体可信治理",
    "工业智能体可信运行",
    "多智能体系统基础设施",
    "数字生态基础设施",
    "自主航天智能体",
    "航天人工智能",
  ],
  openGraph: {
    type: "website",
    siteName: "TITMAS Infrastructure Developer Community",
    title: "TITMAS 可信多智能体基础设施开发者社区",
    description:
      "面向自治 AI 智能体生态的可信基础设施层，支撑跨行业的可信运行与可核验执行。",
  },
  twitter: {
    card: "summary_large_image",
    title: "TITMAS Infrastructure Developer Community",
    description:
      "A trust infrastructure layer for autonomous AI agent ecosystems across industries.",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="zh-CN">
      <head>
        <link
          rel="alternate"
          type="text/plain"
          href="https://redcrag.cn/llms.txt"
          title="TITMAS LLM-readable entry"
        />
        <link
          rel="alternate"
          type="application/json"
          href="https://redcrag.cn/agent-index.json"
          title="TITMAS agent discovery index"
        />
        <link
          rel="alternate"
          type="application/json"
          href="https://redcrag.cn/site-catalog.json"
          title="TITMAS public site catalog"
        />
      </head>
      <body>{children}</body>
    </html>
  );
}
