import Link from "next/link";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import { ArrowLeft } from "lucide-react";
import { generatePageMetadata } from "@/lib/metadata";
import { webPageSchema, SITE_URL } from "@/lib/schema";
import SchemaScript from "@/components/schema/SchemaScript";
import Button from "@/components/ui/Button";

interface TermContent {
  term: string;
  shortDef: string;
  definition: string[];
  examples: string[];
  related: string[];
}

const content: Record<string, TermContent> = {
  "entity-seo": {
    term: "Entity SEO",
    shortDef:
      "Optimizing how search engines and AI models recognize your firm as a distinct, trusted entity.",
    definition: [
      "Entity SEO is the practice of making your law firm a clearly defined, machine-recognizable entity rather than just a collection of web pages. Search engines and AI models don't think in keywords alone anymore — they think in entities: people, organizations, places, and concepts, and the relationships between them.",
      "For a law firm, that means ensuring engines understand who you are, what practice areas you cover, where you operate, and why you're authoritative — consistently across your website, business profiles, directories, and knowledge graphs. When your entity is well-defined, AI models can confidently recommend and cite you in answers.",
    ],
    examples: [
      "A personal injury firm uses consistent name, address, and practice-area descriptions across its website, Google Business Profile, Justia, and Avvo so AI engines resolve them to one trusted entity.",
      "Adding Organization and Attorney schema that links the firm to its lawyers, locations, and areas served gives engines an unambiguous entity definition.",
    ],
    related: ["knowledge-graph", "structured-data", "schema-markup", "topical-authority"],
  },
  "knowledge-graph": {
    term: "Knowledge Graph",
    shortDef:
      "A structured map of entities and their relationships that AI uses to understand the world.",
    definition: [
      "A knowledge graph is a vast, structured database of entities — people, organizations, places, concepts — and the connections between them. Google's Knowledge Graph powers the information panels you see in search, and similar structures inform how AI models reason about the world.",
      "Being present and accurately represented in a knowledge graph is foundational for AI visibility. If a model can locate your firm as a verified entity with clear attributes and relationships, it's far more likely to surface and cite you confidently in generated answers.",
    ],
    examples: [
      "A firm earns a Google Knowledge Panel showing its name, logo, location, reviews, and attorneys — a direct signal of recognized entity status.",
      "Linking your firm to Wikidata and authoritative legal directories strengthens its node in the broader knowledge graph.",
    ],
    related: ["entity-seo", "structured-data", "semantic-search", "schema-markup"],
  },
  "ai-overviews": {
    term: "AI Overviews",
    shortDef:
      "Google's AI-generated answer summaries that appear above traditional search results.",
    definition: [
      "AI Overviews are Google's generative summaries that appear at the very top of search results for many queries, synthesizing information from multiple sources into a direct answer. For legal searches, they increasingly sit above the organic listings law firms have traditionally competed for.",
      "Because AI Overviews cite the sources they draw from, being one of those cited sources is the new prize. Firms that earn citations capture attention and trust before a user ever scrolls to the classic results — making AI Overview optimization a core part of modern legal marketing.",
    ],
    examples: [
      "Someone searches \"do I need a lawyer for a slip and fall claim\" and Google generates an overview citing a firm's detailed guide on the topic.",
      "A firm structures its FAQ and practice-area content to directly answer common questions, increasing the odds of being pulled into an AI Overview.",
    ],
    related: ["geo", "aiso", "schema-markup", "semantic-search"],
  },
  geo: {
    term: "GEO (Generative Engine Optimization)",
    shortDef:
      "Optimizing content to be surfaced and cited within generative AI responses.",
    definition: [
      "Generative Engine Optimization (GEO) is the discipline of structuring and writing content so that generative AI engines — ChatGPT, Gemini, Perplexity, and Google AI Overviews — pull it into and cite it within their answers. It's the AI-era successor to traditional SEO's link-ranking focus.",
      "GEO emphasizes clarity, factual density, authoritative signals, and machine-readable structure. Rather than chasing a single ranking position, the goal is to be the trusted source a model quotes when answering a relevant question.",
    ],
    examples: [
      "A family law firm publishes a clearly structured, citation-friendly explainer on divorce timelines that Perplexity references in its answers.",
      "Adding concise, factual summaries and statistics to a page increases the chance an LLM extracts and cites it.",
    ],
    related: ["aiso", "ai-overviews", "semantic-search", "topical-authority"],
  },
  "schema-markup": {
    term: "Schema Markup",
    shortDef:
      "Code added to a webpage that describes its content to search engines and AI in a machine-readable way.",
    definition: [
      "Schema markup is structured code, usually written in JSON-LD using the Schema.org vocabulary, that explicitly tells search engines and AI models what a page's content means. Instead of forcing machines to infer that a block of text is a law firm's address or an attorney's bio, schema labels it unambiguously.",
      "For law firms, schema markup unlocks rich results (like star ratings and FAQs) and strengthens entity recognition — both of which improve traditional rankings and AI citation odds. It's one of the highest-leverage technical foundations for AI search visibility.",
    ],
    examples: [
      "A firm adds LegalService and Attorney schema so engines clearly identify its practice areas, locations, and individual lawyers.",
      "FAQPage schema on a practice-area page makes its questions eligible for rich results and easier for AI to quote.",
    ],
    related: ["structured-data", "entity-seo", "knowledge-graph", "ai-overviews"],
  },
  "semantic-search": {
    term: "Semantic Search",
    shortDef:
      "Search that interprets meaning and intent rather than matching exact keywords.",
    definition: [
      "Semantic search is the ability of modern engines and AI models to understand the meaning and intent behind a query rather than just matching literal keywords. It relies on natural language processing and vector embeddings to grasp context, synonyms, and relationships.",
      "This shift means content should comprehensively answer the user's underlying question and demonstrate genuine expertise, not just repeat target phrases. Firms that write naturally and cover a topic in depth perform far better in a semantic, AI-driven search landscape.",
    ],
    examples: [
      "A query for \"someone hit my car and left\" surfaces hit-and-run content even though those exact words aren't on the page.",
      "An engine understands that \"attorney,\" \"lawyer,\" and \"legal counsel\" refer to the same concept and ranks comprehensive content accordingly.",
    ],
    related: ["knowledge-graph", "topical-authority", "geo", "entity-seo"],
  },
  "structured-data": {
    term: "Structured Data",
    shortDef:
      "Standardized, machine-readable information about a page that powers rich results and AI understanding.",
    definition: [
      "Structured data is information organized in a standardized, machine-readable format that lets search engines and AI models interpret content with precision. Schema markup is the most common way to implement it on the web.",
      "By describing your firm, services, locations, reviews, and FAQs in a structured way, you remove ambiguity for the systems deciding what to show and cite. Structured data is a backbone of both rich search results and reliable AI citations.",
    ],
    examples: [
      "Marking up reviews so star ratings appear in search results and feed AI assessments of trust.",
      "Defining a firm's offices as structured location data so AI can match it to local, intent-driven queries.",
    ],
    related: ["schema-markup", "entity-seo", "knowledge-graph", "ai-overviews"],
  },
  aiso: {
    term: "AISO (AI Search Optimization)",
    shortDef:
      "The practice of optimizing a brand to be understood and cited by AI answer engines.",
    definition: [
      "AI Search Optimization (AISO) is the umbrella discipline of making a business visible, understood, and recommended across AI answer engines like ChatGPT, Gemini, Perplexity, and Google AI Overviews. It combines entity SEO, structured data, authoritative content, and reputation signals.",
      "Where traditional SEO targets ranking positions, AISO targets being named inside the answer itself. For law firms, it's the path to capturing high-intent clients at the precise moment an AI is recommending who to call.",
    ],
    examples: [
      "A firm builds consistent entity signals and deep practice-area content so ChatGPT names it when asked for a recommendation.",
      "Optimizing for AISO, a firm tracks its citation rate across multiple AI engines as a core performance metric.",
    ],
    related: ["geo", "ai-overviews", "entity-seo", "topical-authority"],
  },
  "e-e-a-t": {
    term: "E-E-A-T",
    shortDef:
      "Experience, Expertise, Authoritativeness, and Trust — Google's quality framework.",
    definition: [
      "E-E-A-T stands for Experience, Expertise, Authoritativeness, and Trustworthiness — the framework Google's quality evaluators use to judge content, with extra weight for \"Your Money or Your Life\" topics like legal services.",
      "For law firms, strong E-E-A-T means clearly credentialed attorney authors, demonstrable real-world experience, authoritative citations and recognition, and trust signals like accurate contact details and genuine reviews. These same signals heavily influence whether AI models consider you a credible source worth citing.",
    ],
    examples: [
      "Attorney bios with bar admissions, case experience, and credentials reinforce expertise and trust on every page they author.",
      "Earning mentions from reputable legal publications and directories boosts authoritativeness in the eyes of both Google and AI.",
    ],
    related: ["topical-authority", "entity-seo", "aiso", "knowledge-graph"],
  },
  "topical-authority": {
    term: "Topical Authority",
    shortDef:
      "The depth and breadth of expertise a site demonstrates on a subject, boosting trust with AI and search.",
    definition: [
      "Topical authority is the degree to which a website is recognized as a comprehensive, expert source on a given subject. It's built by covering a topic deeply and broadly — answering the full range of questions a client might have — rather than publishing thin, scattered pages.",
      "For law firms, concentrated topical authority in specific practice areas often beats broad, shallow coverage. AI engines and search systems reward sources that demonstrably own a subject, making them far more likely to cite and recommend you.",
    ],
    examples: [
      "An immigration firm publishes an interconnected library covering visas, green cards, citizenship, and deportation defense, signaling deep authority.",
      "Internal linking between related practice-area articles reinforces the firm's expertise on a topic for both users and AI.",
    ],
    related: ["e-e-a-t", "semantic-search", "geo", "aiso"],
  },
};

const allTerms: Record<string, string> = Object.fromEntries(
  Object.entries(content).map(([slug, c]) => [slug, c.term])
);

export function generateStaticParams() {
  return Object.keys(content).map((term) => ({ term }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ term: string }>;
}): Promise<Metadata> {
  const { term } = await params;
  const entry = content[term];
  if (!entry) {
    return generatePageMetadata({
      title: "Glossary Term Not Found",
      description: "This glossary term could not be found.",
      slug: `resources/glossary/${term}`,
    });
  }
  return generatePageMetadata({
    title: `${entry.term} — Definition`,
    description: entry.shortDef,
    slug: `resources/glossary/${term}`,
  });
}

export default async function GlossaryTermPage({
  params,
}: {
  params: Promise<{ term: string }>;
}) {
  const { term } = await params;
  const entry = content[term];
  if (!entry) notFound();

  return (
    <>
      <SchemaScript
        schema={webPageSchema(
          `${entry.term} | LexScale.ai Glossary`,
          entry.shortDef,
          `${SITE_URL}/resources/glossary/${term}`
        )}
      />

      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[760px] px-6 py-24 md:px-10">
          <Link
            href="/resources/glossary"
            className="mb-6 inline-flex items-center gap-1.5 text-[14px] font-semibold text-pu3 hover:text-white"
          >
            <ArrowLeft size={16} />
            Back to glossary
          </Link>
          <p className="mb-3 text-sm font-bold uppercase tracking-[0.2em] text-pu3">
            Glossary
          </p>
          <h1 className="text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight text-white">
            {entry.term}
          </h1>
          <p className="mt-6 text-[18px] leading-relaxed text-white/75">
            {entry.shortDef}
          </p>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[760px] px-6 py-20 md:px-10">
          <div className="prose-headings flex flex-col gap-5">
            {entry.definition.map((p, i) => (
              <p key={i} className="text-[17px] leading-relaxed text-slate-700">
                {p}
              </p>
            ))}
          </div>

          <div className="mt-12">
            <h2 className="text-[22px] font-extrabold tracking-tight text-navy">
              Examples
            </h2>
            <ul className="mt-5 flex flex-col gap-4">
              {entry.examples.map((ex, i) => (
                <li
                  key={i}
                  className="rounded-2xl border border-pu/10 bg-white p-6 text-[15px] leading-relaxed text-slate-700 shadow-[0_6px_28px_rgba(11,21,54,.08)]"
                >
                  {ex}
                </li>
              ))}
            </ul>
          </div>

          <div className="mt-12">
            <h2 className="text-[22px] font-extrabold tracking-tight text-navy">
              Related terms
            </h2>
            <div className="mt-5 flex flex-wrap gap-3">
              {entry.related.map((slug) => (
                <Link
                  key={slug}
                  href={`/resources/glossary/${slug}`}
                  className="rounded-full border border-pu/20 bg-pu/8 px-4 py-2 text-[14px] font-semibold text-pu transition-colors duration-200 hover:bg-pu hover:text-white"
                >
                  {allTerms[slug] ?? slug}
                </Link>
              ))}
            </div>
          </div>

          <div className="mt-16 rounded-2xl bg-navy p-10 text-center shadow-[0_6px_28px_rgba(11,21,54,.16)]">
            <h2 className="text-[clamp(22px,2.4vw,30px)] font-extrabold tracking-tight text-white">
              Turn this term into a competitive edge
            </h2>
            <p className="mx-auto mt-4 max-w-[520px] text-[16px] leading-relaxed text-white/70">
              We help law firms apply these concepts to win citations across
              ChatGPT, Gemini, Perplexity, and Google AI. Start with a free
              visibility check.
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
