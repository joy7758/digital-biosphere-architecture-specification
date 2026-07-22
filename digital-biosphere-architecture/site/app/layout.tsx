import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  metadataBase: new URL("https://redcrag.cn"),
  title: {
    default: "可信多智能体基础设施",
    template: "%s · TMAI",
  },
  description:
    "面向长期运行、协作和可验证数字主体的基础设施。",
  openGraph: {
    type: "website",
    siteName: "Trusted Multi-Agent Infrastructure",
    title: "可信多智能体基础设施",
    description:
      "面向长期运行、协作和可验证数字主体的基础设施。",
    images: [
      {
        url: "/og.png",
        width: 1731,
        height: 909,
        alt: "Trusted Multi-Agent Infrastructure / 可信多智能体基础设施",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "Trusted Multi-Agent Infrastructure",
    description:
      "Infrastructure for long-running, collaborative, and verifiable digital entities.",
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
