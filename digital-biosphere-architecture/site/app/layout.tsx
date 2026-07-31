import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  metadataBase: new URL("https://redcrag.cn"),
  icons: {
    icon: "/favicon.svg",
  },
  title: {
    default: "山西游骑兵电子商务有限公司",
    template: "%s · 山西游骑兵电子商务有限公司",
  },
  description:
    "围绕开放规范、适配器契约、符合性测试和参考实现边界建设可信多智能体基础设施。",
  openGraph: {
    type: "website",
    siteName: "山西游骑兵电子商务有限公司",
    title: "山西游骑兵电子商务有限公司",
    description:
      "Developer Community for Trusted Multi-Agent Infrastructure.",
    images: [
      {
        url: "/og.png",
        width: 1731,
        height: 909,
        alt: "夏日之海 / TITMAS Infrastructure Developer Community",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "山西游骑兵电子商务有限公司",
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
