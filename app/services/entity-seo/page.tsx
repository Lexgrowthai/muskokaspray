import {
  Network,
  Fingerprint,
  Database,
  Link2,
  RefreshCcw,
  ShieldCheck,
  Brain,
  Target,
} from "lucide-react";
import Tag from "@/components/ui/Tag";
import Button from "@/components/ui/Button";
import FAQ from "@/components/sections/FAQ";
import SchemaScript from "@/components/schema/SchemaScript";
import { generatePageMetadata } from "@/lib/metadata";
import { serviceSchema, SITE_URL } from "@/lib/schema";

const NAME = "Entity SEO for Law Firms";
const DESCRIPTION =
  "Entity SEO makes search engines and AI models understand who your firm is, what you do, and why you're authoritative. LexScale builds your firm's entity so it's recognized and recommended everywhere.";

export const metadata = generatePageMetadata({
  title: NAME,
  description: DESCRIPTION,
  slug: "services/entity-seo",
});

const steps = [
  {
    title: "Entity Discovery & Gap Analysis",
    body: "We map how Google and AI models currently understand your firm — your Knowledge Graph presence, attributes, relationships, and the gaps that keep you from being recognized as a distinct, authoritative entity.",
  },
  {
    title: "Canonical Entity Definition",
    body: "We define a single source of truth for your firm: official name, attorneys, practice areas, locations, and credentials — the facts every platform should agree on, encoded in structured data and your About content.",
  },
  {
    title: "Consistency & Disambiguation",
    body: "We align your name, address, and details across your site, directories, bar listings, and social profiles so machines can confidently distinguish your firm from similarly named businesses.",
  },
  {
    title: "Relationship & Authority Building",
    body: "Entities gain strength through connections. We link your firm to recognized people, places, organizations, and topics — attorney bios, sameAs links, citations, and topical content clusters.",
  },
  {
    title: "Monitor the Knowledge Graph",
    body: "We track your entity's presence in Google's Knowledge Panel and AI model responses, then continuously reinforce attributes so your firm's recognition deepens over time.",
  },
];

const benefits = [
  {
    icon: Brain,
    title: "AI Models Recognize You",
    body: "Generative engines recommend firms they 'understand' as real, credible entities. A strong entity profile is the foundation that makes ChatGPT, Gemini, and Perplexity confident enough to name you.",
  },
  {
    icon: ShieldCheck,
    title: "A Knowledge Panel of Your Own",
    body: "A well-built entity can earn a Google Knowledge Panel — branded, prominent, and trust-building real estate that displays your firm's verified facts directly in search.",
  },
  {
    icon: Target,
    title: "Topical Authority That Ranks",
    body: "When your firm is firmly associated with its practice areas, you rank and get cited for the topics that matter — not just exact-match keywords, but the full intent behind them.",
  },
];

const faqs = [
  {
    question: "What exactly is an 'entity' in SEO?",
    answer:
      "An entity is a distinct, identifiable thing — your firm, an attorney, a practice area — that search engines store in a knowledge graph with attributes and relationships. Entity SEO is the work of making your firm a clearly defined, well-connected entity that machines understand, not just a string of keywords.",
  },
  {
    question: "How is entity SEO different from keyword SEO?",
    answer:
      "Keyword SEO targets specific search phrases on a page. Entity SEO builds your firm's identity and authority across the entire web so you're surfaced for whole topics and recommended by AI. It's the structural layer beneath both classic rankings and AI visibility.",
  },
  {
    question: "Will entity SEO help me get a Google Knowledge Panel?",
    answer:
      "It's the primary way to earn one. By establishing a canonical entity definition, consistent structured data, authoritative sameAs links, and corroborating sources, we make it possible for Google to generate and trust a Knowledge Panel for your firm.",
  },
  {
    question: "How long does entity building take?",
    answer:
      "Foundational work — structured data, consistency cleanup, About content — is implemented in the first weeks. Knowledge Graph recognition and panel generation typically develop over three to six months as Google validates and corroborates your entity across sources.",
  },
  {
    question: "Do I need entity SEO if I already do AI search optimization?",
    answer:
      "Entity SEO is the foundation of AI search optimization. AI models can only recommend firms they recognize and trust as entities, so the two work together — entity work makes every other AI optimization effort more effective.",
  },
];

export default function Page() {
  return (
    <>
      <SchemaScript
        schema={serviceSchema(
          NAME,
          DESCRIPTION,
          SITE_URL + "/services/entity-seo"
        )}
      />

      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[1100px] px-6 py-24 text-white md:px-10">
          <Tag variant="purple">
            <Network size={13} /> Entity SEO
          </Tag>
          <h1 className="mt-5 max-w-[820px] text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight">
            Make Search Engines & AI Understand Exactly Who You Are
          </h1>
          <p className="mt-5 max-w-[640px] text-[17px] leading-relaxed text-white/75">
            Modern search runs on entities, not just keywords. We build your
            firm into a recognized, authoritative entity in Google&apos;s
            Knowledge Graph and across the web — the foundation that makes every
            AI engine confident enough to recommend you.
          </p>
          <div className="mt-8 flex flex-wrap gap-3">
            <Button
              href="/tools/ai-visibility-checker"
              variant="gold"
              size="lg"
            >
              Get a Free Strategy Call
            </Button>
            <Button
              href="/services/structured-data"
              variant="outline"
              size="lg"
              className="border-white/25 text-white hover:border-white hover:text-white"
            >
              See Structured Data
            </Button>
          </div>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <Tag variant="purple">What We Do</Tag>
          <h2 className="mt-4 max-w-[760px] text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
            We build your firm into a recognized entity
          </h2>
          <p className="mt-5 max-w-[720px] text-[16px] leading-relaxed text-slate-600">
            Google and every major AI model maintain a knowledge graph — a web
            of entities and the facts that connect them. If your firm
            isn&apos;t clearly defined inside it, you&apos;re a fuzzy string of
            text the machine can&apos;t confidently surface. Our entity SEO
            program gives your firm a precise, consistent identity: a canonical
            definition, clean structured data, disambiguated listings, and a
            dense web of authoritative relationships. The payoff is durable —
            stronger rankings, a potential Knowledge Panel, and the recognition
            AI models need before they&apos;ll recommend you.
          </p>
        </div>
      </section>

      <section className="bg-navy/[0.02]">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <Tag variant="gold">How It Works</Tag>
          <h2 className="mt-4 text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
            Our five-step entity program
          </h2>
          <div className="mt-10 flex flex-col gap-5">
            {steps.map((step, i) => (
              <div
                key={i}
                className="flex gap-5 rounded-2xl border border-pu/10 bg-white p-7 shadow-[0_6px_28px_rgba(11,21,54,.08)]"
              >
                <span className="flex h-11 w-11 flex-shrink-0 items-center justify-center rounded-xl bg-gradient-to-br from-pu to-pu2 text-[17px] font-extrabold text-white">
                  {i + 1}
                </span>
                <div>
                  <h3 className="text-[18px] font-bold text-navy">
                    {step.title}
                  </h3>
                  <p className="mt-1.5 text-[15px] leading-relaxed text-slate-600">
                    {step.body}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <Tag variant="purple">Why It Matters</Tag>
          <h2 className="mt-4 text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
            Entities are the language of modern search
          </h2>
          <div className="mt-10 grid gap-6 md:grid-cols-3">
            {benefits.map((b, i) => {
              const Icon = b.icon;
              return (
                <div
                  key={i}
                  className="rounded-2xl border border-pu/10 bg-white p-7 shadow-[0_6px_28px_rgba(11,21,54,.08)]"
                >
                  <span className="flex h-12 w-12 items-center justify-center rounded-xl bg-pu/10 text-pu">
                    <Icon size={22} />
                  </span>
                  <h3 className="mt-5 text-[18px] font-bold text-navy">
                    {b.title}
                  </h3>
                  <p className="mt-2 text-[15px] leading-relaxed text-slate-600">
                    {b.body}
                  </p>
                </div>
              );
            })}
          </div>
          <div className="mt-10 grid gap-6 md:grid-cols-3">
            <div className="flex items-center gap-3 rounded-2xl border border-pu/10 bg-white p-5">
              <Fingerprint size={20} className="text-pu" />
              <span className="text-[14px] font-semibold text-navy">
                Canonical entity definition
              </span>
            </div>
            <div className="flex items-center gap-3 rounded-2xl border border-pu/10 bg-white p-5">
              <Database size={20} className="text-pu" />
              <span className="text-[14px] font-semibold text-navy">
                Knowledge Graph alignment
              </span>
            </div>
            <div className="flex items-center gap-3 rounded-2xl border border-pu/10 bg-white p-5">
              <Link2 size={20} className="text-pu" />
              <span className="text-[14px] font-semibold text-navy">
                sameAs & relationship links
              </span>
            </div>
          </div>
        </div>
      </section>

      <section className="bg-navy/[0.02]">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="overflow-hidden rounded-3xl bg-gradient-to-br from-pu to-pu2 p-10 text-white md:p-14">
            <div className="flex items-center gap-2 text-[12px] font-bold uppercase tracking-[1px] text-white/70">
              <RefreshCcw size={15} /> Foundational Entity Program
            </div>
            <h2 className="mt-3 max-w-[640px] text-[clamp(24px,2.8vw,36px)] font-extrabold leading-tight">
              Entity SEO built for law firms
            </h2>
            <p className="mt-4 max-w-[600px] text-[16px] leading-relaxed text-white/80">
              Entity foundations start at $1,200/month and include entity
              mapping, structured data, listing consistency, and Knowledge Graph
              monitoring. Often paired with our AI search optimization program
              for compounding results.
            </p>
            <div className="mt-8 flex flex-wrap gap-3">
              <Button
                href="/tools/ai-visibility-checker"
                variant="gold"
                size="lg"
              >
                Get a Free Strategy Call
              </Button>
              <Button
                href="/services/ai-search-optimization"
                variant="outline"
                size="lg"
                className="border-white/30 text-white hover:border-white hover:text-white"
              >
                AI Search Optimization
              </Button>
            </div>
          </div>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <FAQ faqs={faqs} title="Entity SEO FAQs" />
        </div>
      </section>
    </>
  );
}
