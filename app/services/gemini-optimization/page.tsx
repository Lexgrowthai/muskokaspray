import {
  Stars,
  Search,
  FileText,
  Globe,
  RefreshCcw,
  TrendingUp,
  ShieldCheck,
  Users,
  Layers,
} from "lucide-react";
import Tag from "@/components/ui/Tag";
import Button from "@/components/ui/Button";
import FAQ from "@/components/sections/FAQ";
import SchemaScript from "@/components/schema/SchemaScript";
import { generatePageMetadata } from "@/lib/metadata";
import { serviceSchema, SITE_URL } from "@/lib/schema";

const NAME = "Google Gemini Optimization for Law Firms";
const DESCRIPTION =
  "Win visibility in Google Gemini and AI Overviews. LexScale optimizes your firm's content, entities, and Google Business signals so Gemini surfaces and recommends your practice.";

export const metadata = generatePageMetadata({
  title: NAME,
  description: DESCRIPTION,
  slug: "services/gemini-optimization",
});

const steps = [
  {
    title: "Gemini & AI Overview Audit",
    body: "We test how Gemini and Google's AI Overviews respond to your prospects' real legal queries, capturing which firms get surfaced, which sources are cited, and where your firm is missing.",
  },
  {
    title: "Google Ecosystem Alignment",
    body: "Gemini leans heavily on Google's own signals. We tighten your Google Business Profile, reviews, Knowledge Panel, and indexed content so the model has a consistent, trusted picture of your firm.",
  },
  {
    title: "Passage-Optimized Content",
    body: "Gemini extracts specific passages to compose answers. We restructure your practice pages into clear, self-contained sections — eligibility, process, timelines, costs — that map cleanly to query intent.",
  },
  {
    title: "Authority & Freshness Signals",
    body: "We strengthen the E-E-A-T signals Google rewards: author expertise, citations, updated dates, and structured data, so Gemini treats your pages as current, authoritative legal sources.",
  },
  {
    title: "Monitor & Iterate",
    body: "AI Overviews shift constantly. We track your appearance across priority queries, watch competitor displacement, and refine content each cycle to defend and grow your share of the answer.",
  },
];

const benefits = [
  {
    icon: TrendingUp,
    title: "Own the Top of Google",
    body: "AI Overviews now sit above traditional results. Being cited there captures attention before a single blue link is seen — the most valuable real estate in search.",
  },
  {
    icon: Layers,
    title: "One Effort, Two Wins",
    body: "Optimizing for Gemini reinforces classic Google rankings. The same clarity and authority that earns AI citations also lifts your organic positions.",
  },
  {
    icon: ShieldCheck,
    title: "Accurate, Trusted Representation",
    body: "We ensure Gemini draws on your verified Google data, so the firm details, practice areas, and locations it presents are correct and conversion-ready.",
  },
  {
    icon: Users,
    title: "Reach Mobile & Voice Users",
    body: "Gemini powers answers across Android, Chrome, and voice. Optimization puts your firm in front of prospects no matter how they ask.",
  },
];

const faqs = [
  {
    question: "What is the difference between Gemini and Google AI Overviews?",
    answer:
      "Gemini is Google's conversational AI model; AI Overviews are the AI-generated summaries that appear at the top of Google Search, often powered by Gemini. Our program optimizes for both, since they share underlying signals and source-selection logic.",
  },
  {
    question: "How important is my Google Business Profile for Gemini?",
    answer:
      "Very. Gemini and AI Overviews draw on Google's own entity graph, so an accurate, active Google Business Profile with strong reviews and consistent NAP data significantly improves how — and how often — your firm is surfaced.",
  },
  {
    question: "Can you get my firm into AI Overviews for competitive queries?",
    answer:
      "We target the queries where you can realistically win first — local and long-tail legal questions — then expand. Citation in AI Overviews favors clear, well-structured, authoritative passages, which is exactly what we engineer.",
  },
  {
    question: "Does optimizing for Gemini risk my existing rankings?",
    answer:
      "No. Everything we do — content clarity, schema, E-E-A-T, and Google Business signals — aligns with Google's published quality guidelines and strengthens organic performance alongside AI visibility.",
  },
  {
    question: "How do you prove results?",
    answer:
      "We track a defined set of queries across Gemini and AI Overviews, screenshot appearances, and report citation share and changes each cycle so you can see exactly where your firm shows up over time.",
  },
];

export default function Page() {
  return (
    <>
      <SchemaScript
        schema={serviceSchema(
          NAME,
          DESCRIPTION,
          SITE_URL + "/services/gemini-optimization"
        )}
      />

      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[1100px] px-6 py-24 text-white md:px-10">
          <Tag variant="blue">
            <Stars size={13} /> Google Gemini Optimization
          </Tag>
          <h1 className="mt-5 max-w-[820px] text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight">
            Be the Firm Google Gemini Recommends
          </h1>
          <p className="mt-5 max-w-[640px] text-[17px] leading-relaxed text-white/75">
            Gemini and AI Overviews now answer legal questions before the first
            blue link. We position your firm inside those answers — anchored to
            your Google profile, your content, and the authority signals Google
            trusts.
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
            We make your firm a source Gemini trusts
          </h2>
          <p className="mt-5 max-w-[720px] text-[16px] leading-relaxed text-slate-600">
            Google&apos;s AI doesn&apos;t invent recommendations — it composes
            them from sources it deems authoritative and relevant. Our Gemini
            optimization program aligns your firm with the signals Google
            rewards: an accurate Google Business Profile, passage-ready content,
            structured data, and genuine demonstrated expertise. The result is a
            firm that surfaces in AI Overviews and Gemini conversations for the
            legal questions your future clients are actually asking.
          </p>
        </div>
      </section>

      <section className="bg-navy/[0.02]">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <Tag variant="gold">How It Works</Tag>
          <h2 className="mt-4 text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
            Our five-step Gemini program
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
            AI Overviews are the new top of search
          </h2>
          <div className="mt-10 grid gap-6 md:grid-cols-2">
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
              <Globe size={20} className="text-pu" />
              <span className="text-[14px] font-semibold text-navy">
                Google Business optimization
              </span>
            </div>
            <div className="flex items-center gap-3 rounded-2xl border border-pu/10 bg-white p-5">
              <FileText size={20} className="text-pu" />
              <span className="text-[14px] font-semibold text-navy">
                Passage-ready content
              </span>
            </div>
            <div className="flex items-center gap-3 rounded-2xl border border-pu/10 bg-white p-5">
              <Search size={20} className="text-pu" />
              <span className="text-[14px] font-semibold text-navy">
                AI Overview tracking
              </span>
            </div>
          </div>
        </div>
      </section>

      <section className="bg-navy/[0.02]">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="overflow-hidden rounded-3xl bg-gradient-to-br from-pu to-pu2 p-10 text-white md:p-14">
            <div className="flex items-center gap-2 text-[12px] font-bold uppercase tracking-[1px] text-white/70">
              <RefreshCcw size={15} /> Ongoing Gemini Program
            </div>
            <h2 className="mt-3 max-w-[640px] text-[clamp(24px,2.8vw,36px)] font-extrabold leading-tight">
              Gemini & AI Overview optimization for law firms
            </h2>
            <p className="mt-4 max-w-[600px] text-[16px] leading-relaxed text-white/80">
              Programs start at $1,500/month and include Gemini and AI Overview
              tracking, Google ecosystem alignment, content engineering, and
              monthly reporting. Month-to-month, no long-term contracts.
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
          <FAQ faqs={faqs} title="Google Gemini Optimization FAQs" />
        </div>
      </section>
    </>
  );
}
