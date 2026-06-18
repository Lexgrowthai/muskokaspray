import Link from "next/link";
import { ArrowUpRight } from "lucide-react";
import { generatePageMetadata } from "@/lib/metadata";
import { webPageSchema, SITE_URL } from "@/lib/schema";
import SchemaScript from "@/components/schema/SchemaScript";
import Button from "@/components/ui/Button";

export const metadata = generatePageMetadata({
  title: "AI Search & SEO Glossary",
  description:
    "A plain-English A–Z glossary of the AI search and SEO terms every law firm should know — from AI Overviews and entity SEO to schema markup and topical authority.",
  slug: "resources/glossary",
});

interface Term {
  term: string;
  definition: string;
  slug?: string;
}

const terms: Term[] = [
  {
    term: "AI Overviews",
    definition:
      "Google's AI-generated answer summaries that appear above traditional search results.",
    slug: "ai-overviews",
  },
  {
    term: "AISO (AI Search Optimization)",
    definition:
      "The practice of optimizing a brand to be understood and cited by AI answer engines.",
    slug: "aiso",
  },
  {
    term: "Answer Engine",
    definition:
      "A tool like ChatGPT or Perplexity that returns a direct answer rather than a list of links.",
  },
  {
    term: "Citation",
    definition:
      "A reference to your firm inside an AI-generated answer that signals trust and authority.",
  },
  {
    term: "Crawlability",
    definition:
      "How easily search and AI bots can access and read the content on your website.",
  },
  {
    term: "E-E-A-T",
    definition:
      "Experience, Expertise, Authoritativeness, and Trust — Google's quality framework.",
    slug: "e-e-a-t",
  },
  {
    term: "Entity",
    definition:
      "A uniquely identifiable thing — like your law firm — that AI systems recognize and reason about.",
  },
  {
    term: "Entity SEO",
    definition:
      "Optimizing how search engines and AI models recognize your firm as a distinct, trusted entity.",
    slug: "entity-seo",
  },
  {
    term: "GEO (Generative Engine Optimization)",
    definition:
      "Optimizing content to be surfaced and cited within generative AI responses.",
    slug: "geo",
  },
  {
    term: "Knowledge Graph",
    definition:
      "A structured map of entities and their relationships that AI uses to understand the world.",
    slug: "knowledge-graph",
  },
  {
    term: "LLM (Large Language Model)",
    definition:
      "The AI model, such as GPT or Gemini, that generates conversational answers.",
  },
  {
    term: "Natural Language Processing",
    definition:
      "The AI techniques that let machines interpret and respond to human language.",
  },
  {
    term: "Prompt",
    definition:
      "The question or instruction a user gives an AI tool to get a response.",
  },
  {
    term: "Schema Markup",
    definition:
      "Code added to a webpage that describes its content to search engines and AI in a machine-readable way.",
    slug: "schema-markup",
  },
  {
    term: "Semantic Search",
    definition:
      "Search that interprets meaning and intent rather than matching exact keywords.",
    slug: "semantic-search",
  },
  {
    term: "SERP",
    definition:
      "Search Engine Results Page — the page returned after a query, now often led by AI features.",
  },
  {
    term: "Structured Data",
    definition:
      "Standardized, machine-readable information about a page that powers rich results and AI understanding.",
    slug: "structured-data",
  },
  {
    term: "Topical Authority",
    definition:
      "The depth and breadth of expertise a site demonstrates on a subject, boosting trust with AI and search.",
    slug: "topical-authority",
  },
  {
    term: "Vector Embedding",
    definition:
      "A numerical representation of meaning that lets AI compare and retrieve related content.",
  },
  {
    term: "Zero-Click Search",
    definition:
      "A search resolved entirely on the results page or in an AI answer, with no click to a website.",
  },
];

export default function GlossaryPage() {
  // group by first letter
  const groups = terms.reduce<Record<string, Term[]>>((acc, t) => {
    const letter = t.term[0].toUpperCase();
    (acc[letter] ||= []).push(t);
    return acc;
  }, {});
  const letters = Object.keys(groups).sort();

  return (
    <>
      <SchemaScript
        schema={webPageSchema(
          "AI Search & SEO Glossary | LexScale.ai",
          "A plain-English glossary of AI search and SEO terms for law firms.",
          `${SITE_URL}/resources/glossary`
        )}
      />

      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[1100px] px-6 py-24 text-center md:px-10">
          <p className="mb-4 text-sm font-bold uppercase tracking-[0.2em] text-pu3">
            Resources
          </p>
          <h1 className="mx-auto max-w-[760px] text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight text-white">
            AI search &amp; SEO glossary
          </h1>
          <p className="mx-auto mt-6 max-w-[600px] text-[17px] leading-relaxed text-white/70">
            The language of AI search, explained in plain English. Terms with a
            full breakdown are linked — click through for examples and context.
          </p>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[860px] px-6 py-20 md:px-10">
          <div className="flex flex-col gap-12">
            {letters.map((letter) => (
              <div key={letter}>
                <h2 className="mb-4 text-[22px] font-extrabold text-pu">
                  {letter}
                </h2>
                <div className="flex flex-col gap-3">
                  {groups[letter].map((t) =>
                    t.slug ? (
                      <Link
                        key={t.term}
                        href={`/resources/glossary/${t.slug}`}
                        className="group flex items-start justify-between gap-4 rounded-2xl border border-pu/10 bg-white p-6 shadow-[0_6px_28px_rgba(11,21,54,.08)] transition-all duration-200 hover:-translate-y-0.5 hover:border-pu/30"
                      >
                        <div>
                          <h3 className="flex items-center gap-1.5 text-[17px] font-bold text-navy">
                            {t.term}
                            <ArrowUpRight
                              size={16}
                              className="text-pu transition-transform duration-200 group-hover:translate-x-0.5 group-hover:-translate-y-0.5"
                            />
                          </h3>
                          <p className="mt-1.5 text-[14px] leading-relaxed text-slate-600">
                            {t.definition}
                          </p>
                        </div>
                      </Link>
                    ) : (
                      <div
                        key={t.term}
                        className="rounded-2xl border border-pu/10 bg-white p-6"
                      >
                        <h3 className="text-[17px] font-bold text-navy">
                          {t.term}
                        </h3>
                        <p className="mt-1.5 text-[14px] leading-relaxed text-slate-600">
                          {t.definition}
                        </p>
                      </div>
                    )
                  )}
                </div>
              </div>
            ))}
          </div>

          <div className="mt-16 rounded-2xl bg-navy p-10 text-center shadow-[0_6px_28px_rgba(11,21,54,.16)]">
            <h2 className="text-[clamp(22px,2.4vw,30px)] font-extrabold tracking-tight text-white">
              Ready to put these concepts to work?
            </h2>
            <p className="mx-auto mt-4 max-w-[520px] text-[16px] leading-relaxed text-white/70">
              See how your firm currently shows up across AI engines with a free
              visibility check and strategy call.
            </p>
            <div className="mt-8 flex justify-center">
              <Button
                href="/tools/ai-visibility-checker"
                variant="gold"
                size="lg"
              >
                Get a Free Strategy Call
              </Button>
            </div>
          </div>
        </div>
      </section>
    </>
  );
}
