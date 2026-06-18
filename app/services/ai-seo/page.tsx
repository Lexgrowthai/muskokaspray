import { generatePageMetadata } from "@/lib/metadata";
import { serviceSchema, breadcrumbSchema, SITE_URL } from "@/lib/schema";
import SchemaScript from "@/components/schema/SchemaScript";
import AiSeoClient from "./AiSeoClient";

const NAME = "AI SEO For Law Firms";
const DESCRIPTION =
  "AI-powered SEO services built exclusively for law firms — technical SEO, local SEO, content strategy, link building, and AI search optimization to rank on Google and get cited by ChatGPT, Gemini, and Perplexity.";

export const metadata = generatePageMetadata({
  title: NAME,
  slug: "services/ai-seo",
  description: DESCRIPTION,
});

export default function AiSeoPage() {
  return (
    <>
      <SchemaScript
        schema={serviceSchema(NAME, DESCRIPTION, `${SITE_URL}/services/ai-seo`)}
      />
      <SchemaScript
        schema={breadcrumbSchema([
          { name: "Home", url: SITE_URL },
          { name: "Services", url: `${SITE_URL}/services` },
          { name: NAME, url: `${SITE_URL}/services/ai-seo` },
        ])}
      />
      <AiSeoClient />
    </>
  );
}
