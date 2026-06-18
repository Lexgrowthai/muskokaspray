import type { Metadata } from "next";
import SchemaScript from "@/components/schema/SchemaScript";
import { generatePageMetadata } from "@/lib/metadata";
import { webPageSchema, SITE_URL } from "@/lib/schema";
import MissedCallClient from "./MissedCallClient";

export const metadata: Metadata = generatePageMetadata({
  title: "Missed Call Revenue Calculator for Law Firms",
  description:
    "Calculate how much revenue your law firm loses every year to missed calls — and how many cases you're leaving on the table each month.",
  slug: "tools/missed-call-calculator",
});

export default function MissedCallCalculatorPage() {
  return (
    <>
      <SchemaScript
        schema={webPageSchema(
          "Missed Call Revenue Calculator for Law Firms",
          "Calculate how much revenue your law firm loses every year to missed calls.",
          `${SITE_URL}/tools/missed-call-calculator`
        )}
      />
      <MissedCallClient />
    </>
  );
}
