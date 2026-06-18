import {
  Compass,
  Quote,
  FileText,
  Link2,
  RefreshCcw,
  TrendingUp,
  ShieldCheck,
  Award,
} from "lucide-react";
import Tag from "@/components/ui/Tag";
import Button from "@/components/ui/Button";
import FAQ from "@/components/sections/FAQ";
import SchemaScript from "@/components/schema/SchemaScript";
import { generatePageMetadata } from "@/lib/metadata";
import { serviceSchema, SITE_URL } from "@/lib/schema";

const NAME = "Perplexity Optimization for Law Firms";
const DESCRIPTION =
  "Perplexity cites its sources on every answer. LexScale optimizes your firm's content and authority so Perplexity links to and recommends you when prospects research legal questions.";

export const metadata = generatePageMetadata({
  title: NAME,
  description: DESCRIPTION,
  slug: "services/perplexity-optimization",
});

const steps = [
  {
    title: "Citation Baseline Audit",
    body: "Perplexity footnotes every claim with sources. We run your prospects' legal questions and record which firms and pages get cited — and where yours is absent — to set a clear baseline.",
  },
  {
    title: "Source-Worthy Content",
    body: "Perplexity favors concise, factual, well-sourced pages it can quote directly. We sharpen your content into authoritative, citation-ready passages with clear claims and supporting detail.",
  },
  {
    title: "Freshness & Indexing",
    body: "Perplexity weights recency heavily. We ensure your key pages are crawlable, fast, and regularly updated so they stay in the pool of sources Perplexity pulls from.",
  },
  {
    title: "Authority Reinforcement",
    body: "We build the external signals Perplexity respects — quality backlinks, directory presence, and consistent entity data — so your pages are seen as trustworthy enough to cite.",
  },
  {
    title: "Track Citations & Refine",
    body: "We monitor your citation share across priority queries, watch which competing sources Perplexity prefers, and refine your content each cycle to win more footnotes over time.",
  },
];

const benefits = [
  {
    icon: Quote,
    title: "Earn Direct Citations",
    body: "Unlike opaque chatbots, Perplexity shows exactly which sources it used and links to them. Getting cited drives qualified referral traffic straight to your site.",
  },
  {
    icon: Award,
    title: "Built-In Credibility",
    body: "Being named as a Perplexity source positions your firm as an authority. Researchers and journalists who use Perplexity see you as the trusted answer.",
  },
  {
    icon: TrendingUp,
    title: "Reach Research-Mode Users",
    body: "Perplexity attracts people doing serious research before they commit. Capturing them early in the journey builds trust long before they pick up the phone.",
  },
];

const faqs = [
  {
    question: "Why is Perplexity different from ChatGPT or Gemini?",
    answer:
      "Perplexity is built as an answer engine that cites its sources on every response, with visible footnotes and links. That makes source selection — and earning a citation — central, so optimization focuses heavily on being a concise, fresh, authoritative page Perplexity can quote and link.",
  },
  {
    question: "Does getting cited in Perplexity send me traffic?",
    answer:
      "Yes. Because Perplexity links each cited source, appearing as a footnote drives referral clicks from users who want to verify or go deeper. It's one of the more directly measurable forms of AI search visibility.",
  },
  {
    question: "What kind of content does Perplexity prefer to cite?",
    answer:
      "Clear, factual, well-structured pages with concrete claims, recent updates, and credible authorship. We rewrite practice-area and resource content into citation-ready passages that answer questions directly and signal expertise.",
  },
  {
    question: "How does freshness affect Perplexity rankings?",
    answer:
      "Perplexity weights recency more than many engines. We keep your priority pages updated, ensure fast crawlability, and maintain clear publish and update dates so your content stays in the active source pool.",
  },
  {
    question: "How do you measure success in Perplexity?",
    answer:
      "We track a fixed set of legal queries, record your citation share and the position of your links, and report changes each cycle alongside any referral traffic Perplexity sends to your site.",
  },
];

export default function Page() {
  return (
    <>
      <SchemaScript
        schema={serviceSchema(
          NAME,
          DESCRIPTION,
          SITE_URL + "/services/perplexity-optimization"
        )}
      />

      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[1100px] px-6 py-24 text-white md:px-10">
          <Tag variant="blue">
            <Compass size={13} /> Perplexity Optimization
          </Tag>
          <h1 className="mt-5 max-w-[820px] text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight">
            Become a Source Perplexity Cites & Links
          </h1>
          <p className="mt-5 max-w-[640px] text-[17px] leading-relaxed text-white/75">
            Perplexity footnotes every answer with its sources. We make your
            firm one of them — turning your pages into citation-ready,
            authoritative content that Perplexity quotes, links, and sends
            qualified researchers to.
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
              className="border-white/25 text-white hover:border-white hover:text-white"
            >
              Explore AI Search Optimization
            </Button>
          </div>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <Tag variant="blue">What We Do</Tag>
          <h2 className="mt-4 max-w-[760px] text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
            We turn your pages into Perplexity citations
          </h2>
          <p className="mt-5 max-w-[720px] text-[16px] leading-relaxed text-slate-600">
            Perplexity is winning over the most valuable searchers — people who
            want real answers backed by real sources. Every response it gives
            footnotes the pages it trusted, and those citations drive referral
            traffic and authority. Our Perplexity program engineers your content
            to be exactly what the engine wants to cite: concise, factual,
            fresh, and authoritative. We reinforce the external signals that
            establish trust and track your citation share so your footnotes grow
            query by query.
          </p>
        </div>
      </section>

      <section className="bg-navy/[0.02]">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <Tag variant="gold">How It Works</Tag>
          <h2 className="mt-4 text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
            Our five-step Perplexity program
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
          <Tag variant="blue">Why It Matters</Tag>
          <h2 className="mt-4 text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
            Citations are visibility you can measure
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
              <FileText size={20} className="text-pu" />
              <span className="text-[14px] font-semibold text-navy">
                Citation-ready content
              </span>
            </div>
            <div className="flex items-center gap-3 rounded-2xl border border-pu/10 bg-white p-5">
              <Link2 size={20} className="text-pu" />
              <span className="text-[14px] font-semibold text-navy">
                Authority signal building
              </span>
            </div>
            <div className="flex items-center gap-3 rounded-2xl border border-pu/10 bg-white p-5">
              <Quote size={20} className="text-pu" />
              <span className="text-[14px] font-semibold text-navy">
                Citation share tracking
              </span>
            </div>
          </div>
        </div>
      </section>

      <section className="bg-navy/[0.02]">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="overflow-hidden rounded-3xl bg-gradient-to-br from-pu to-pu2 p-10 text-white md:p-14">
            <div className="flex items-center gap-2 text-[12px] font-bold uppercase tracking-[1px] text-white/70">
              <RefreshCcw size={15} /> Ongoing Perplexity Program
            </div>
            <h2 className="mt-3 max-w-[640px] text-[clamp(24px,2.8vw,36px)] font-extrabold leading-tight">
              Perplexity optimization for law firms
            </h2>
            <p className="mt-4 max-w-[600px] text-[16px] leading-relaxed text-white/80">
              Programs start at $1,500/month and include citation tracking,
              content engineering, freshness management, authority building, and
              monthly reporting on your citation share. Month-to-month, no
              long-term contracts.
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
                href="/case-studies"
                variant="outline"
                size="lg"
                className="border-white/30 text-white hover:border-white hover:text-white"
              >
                See Results
              </Button>
            </div>
          </div>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <FAQ faqs={faqs} title="Perplexity Optimization FAQs" />
        </div>
      </section>
    </>
  );
}
