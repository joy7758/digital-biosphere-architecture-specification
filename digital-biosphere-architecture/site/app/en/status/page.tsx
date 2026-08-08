import type { Metadata } from "next";
import { StatusPage } from "../../status-page";

export const metadata: Metadata = {
  title: "Current status",
  description:
    "DCELL research-direction status, public engineering-evidence maturity, and retained TITMAS history.",
  alternates: {
    canonical: "/en/status/",
    languages: { "zh-CN": "/status/", en: "/en/status/" },
  },
};

export default function EnglishStatus() {
  return <StatusPage locale="en" />;
}
