import { generatePageMetadata } from "@/lib/metadata";
import { serviceSchema, SITE_URL } from "@/lib/schema";
import SchemaScript from "@/components/schema/SchemaScript";
import AiWebsitesClient from "./AiWebsitesClient";

const NAME = "AI Website Design For Law Firms";
const DESCRIPTION =
  "AI-optimised law firm website design that ranks on Google, gets cited by ChatGPT, Gemini, and Perplexity, and converts visitors into consultations — built mobile-first with schema markup and Core Web Vitals compliance.";

export const metadata = generatePageMetadata({
  title: NAME,
  slug: "services/ai-websites",
  description: DESCRIPTION,
});

export default function AiWebsitesPage() {
  return (
    <>
      <SchemaScript
        schema={serviceSchema(
          NAME,
          DESCRIPTION,
          `${SITE_URL}/services/ai-websites`
        )}
      />
      <AiWebsitesClient />
    </>
  );
}
