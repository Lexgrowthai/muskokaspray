import type { Metadata } from "next";
import SchemaScript from "@/components/schema/SchemaScript";
import { generatePageMetadata } from "@/lib/metadata";
import { webPageSchema, SITE_URL } from "@/lib/schema";
import ROICalculatorClient from "./ROICalculatorClient";

export const metadata: Metadata = generatePageMetadata({
  title: "Law Firm Growth ROI Calculator",
  description:
    "Project the additional revenue your law firm could earn each year by increasing your monthly leads with an AI growth system.",
  slug: "tools/roi-calculator",
});

export default function ROICalculatorPage() {
  return (
    <>
      <SchemaScript
        schema={webPageSchema(
          "Law Firm Growth ROI Calculator",
          "Project the additional revenue your law firm could earn each year by increasing your monthly leads.",
          `${SITE_URL}/tools/roi-calculator`
        )}
      />
      <ROICalculatorClient />
    </>
  );
}
