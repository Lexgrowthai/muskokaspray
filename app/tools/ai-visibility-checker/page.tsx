import type { Metadata } from "next";
import SchemaScript from "@/components/schema/SchemaScript";
import { generatePageMetadata } from "@/lib/metadata";
import { webPageSchema, SITE_URL } from "@/lib/schema";
import VisibilityCheckerClient from "./VisibilityCheckerClient";

export const metadata: Metadata = generatePageMetadata({
  title: "AI Visibility Checker for Law Firms",
  description:
    "Check how visible your law firm is across ChatGPT, Gemini, Perplexity, and Google AI. Get an instant AI Visibility Score and see where you're losing clients.",
  slug: "tools/ai-visibility-checker",
});

export default function AIVisibilityCheckerPage() {
  return (
    <>
      <SchemaScript
        schema={webPageSchema(
          "AI Visibility Checker for Law Firms",
          "Check how visible your law firm is across ChatGPT, Gemini, Perplexity, and Google AI.",
          `${SITE_URL}/tools/ai-visibility-checker`
        )}
      />
      <VisibilityCheckerClient />
    </>
  );
}
