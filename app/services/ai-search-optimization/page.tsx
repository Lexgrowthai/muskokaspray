import SchemaScript from "@/components/schema/SchemaScript";
import { generatePageMetadata } from "@/lib/metadata";
import { serviceSchema, SITE_URL } from "@/lib/schema";
import AISOClient from "./AISOClient";

const NAME = "AI Search Optimization (AISO) for Law Firms";
const DESCRIPTION =
  "AI Search Optimization gets your law firm recommended and cited across ChatGPT, Google Gemini, Perplexity, and AI Overviews. LexScale's flagship program wins the AI answer for your firm.";

export const metadata = generatePageMetadata({
  title: NAME,
  description: DESCRIPTION,
  slug: "services/ai-search-optimization",
});

export default function Page() {
  return (
    <>
      <SchemaScript
        schema={serviceSchema(
          NAME,
          DESCRIPTION,
          SITE_URL + "/services/ai-search-optimization"
        )}
      />
      <AISOClient />
    </>
  );
}
