import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  metadataBase: new URL("https://redcrag.cn"),
  title: {
    default: "TITMAS 可信多智能体基础设施开发者社区",
    template: "%s · TITMAS",
  },
  description:
    "为长期运行的多智能体系统共同建设开放、可验证的可信基础设施规则。",
  openGraph: {
    type: "website",
    siteName: "TITMAS Infrastructure Developer Community",
    title: "TITMAS 可信多智能体基础设施开发者社区",
    description:
      "为长期运行的多智能体系统共同建设开放、可验证的可信基础设施规则。",
  },
  twitter: {
    card: "summary_large_image",
    title: "TITMAS Infrastructure Developer Community",
    description:
      "Build the shared trust layer for long-running multi-agent systems.",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="zh-CN">
      <body>{children}</body>
    </html>
  );
}
