import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  metadataBase: new URL("https://redcrag.cn"),
  title: {
    default: "TITMAS 可信多智能体基础设施开发者社区",
    template: "%s · TITMAS",
  },
  description:
    "围绕开放规范、适配器契约、符合性测试和参考实现边界建设可信多智能体基础设施。",
  openGraph: {
    type: "website",
    siteName: "TITMAS Infrastructure Developer Community",
    title: "TITMAS 可信多智能体基础设施开发者社区",
    description:
      "Developer Community for Trusted Multi-Agent Infrastructure.",
    images: [
      {
        url: "/og.png",
        width: 1731,
        height: 909,
        alt: "TITMAS Infrastructure Developer Community / TITMAS 可信多智能体基础设施开发者社区",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "TITMAS Infrastructure Developer Community",
    description:
      "Open specifications, adapter contracts, conformance, and reference boundaries for trusted multi-agent infrastructure.",
    images: ["/og.png"],
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
