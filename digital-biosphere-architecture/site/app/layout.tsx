import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  metadataBase: new URL("https://redcrag.cn"),
  icons: {
    icon: [{ url: "/favicon.svg", type: "image/svg+xml" }],
  },
  title: {
    default: "Bin Zhang · DCELL Research Direction",
    template: "%s · Bin Zhang",
  },
  description:
    "Research Engineer building trustworthy infrastructure for autonomous AI systems. DCELL is a research direction grounded in public engineering evidence.",
  openGraph: {
    type: "website",
    siteName: "Bin Zhang · DCELL Research Direction",
    title: "Trustworthy infrastructure for autonomous AI systems",
    description:
      "Public engineering evidence and the DCELL research direction for bounded, verifiable autonomous AI systems.",
    images: [
      {
        url: "/og-dcell.png",
        width: 1731,
        height: 909,
        alt: "Bin Zhang research website",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "Bin Zhang · DCELL Research Direction",
    description:
      "Research Engineer building trustworthy infrastructure for autonomous AI systems.",
    images: ["/og-dcell.png"],
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
