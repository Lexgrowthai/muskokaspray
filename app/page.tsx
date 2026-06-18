import { generatePageMetadata } from "@/lib/metadata";
import { webPageSchema, SITE_URL } from "@/lib/schema";
import SchemaScript from "@/components/schema/SchemaScript";
import HomeClient from "./HomeClient";

export const metadata = generatePageMetadata({
  title: "AI Growth Systems for Law Firms",
  description:
    "LexScale.ai is the AI growth platform built exclusively for law firms — AI search optimization, AI SEO, websites, chatbots, and receptionists that win clients across ChatGPT, Gemini, Perplexity, and Google AI.",
  slug: "",
});

export default function HomePage() {
  return (
    <>
      <SchemaScript
        schema={webPageSchema(
          "AI Growth Systems for Law Firms",
          "LexScale.ai is the AI growth platform built exclusively for law firms — AI search optimization, AI SEO, websites, chatbots, and receptionists.",
          SITE_URL
        )}
      />
      <HomeClient />
    </>
  );
}
