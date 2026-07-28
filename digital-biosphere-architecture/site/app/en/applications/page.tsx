import type { Metadata } from "next";
import { DirectoryPage } from "../../directory-page";

export const metadata: Metadata = {
  title: "Applications",
  description: "Index of TITMAS medical-evidence and manufacturing application directions.",
  alternates: {
    canonical: "/en/applications/",
    languages: { "zh-CN": "/applications/", en: "/en/applications/" },
  },
};

export default function EnglishApplications() {
  return <DirectoryPage locale="en" section="applications" />;
}
