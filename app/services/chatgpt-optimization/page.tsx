import {
  MessageSquare,
  Search,
  FileText,
  Link2,
  RefreshCcw,
  TrendingUp,
  ShieldCheck,
  Users,
} from "lucide-react";
import Tag from "@/components/ui/Tag";
import Button from "@/components/ui/Button";
import FAQ from "@/components/sections/FAQ";
import SchemaScript from "@/components/schema/SchemaScript";
import { generatePageMetadata } from "@/lib/metadata";
import { serviceSchema, breadcrumbSchema, SITE_URL } from "@/lib/schema";

const NAME = "ChatGPT Optimization for Law Firms";
const DESCRIPTION =
  "Get your law firm cited and recommended inside ChatGPT. LexScale optimizes your content, entities, and authority signals so ChatGPT names your firm when prospects ask for legal help.";

export const metadata = generatePageMetadata({
  title: NAME,
  description: DESCRIPTION,
  slug: "services/chatgpt-optimization",
});

const steps = [
  {
    title: "Prompt & Answer Audit",
    body: "We run the exact questions your prospects ask ChatGPT — from 'best DUI lawyer near me' to 'how long do I have to file an injury claim' — and capture whether your firm is mentioned, ignored, or misrepresented.",
  },
  {
    title: "Entity & Authority Mapping",
    body: "ChatGPT recommends firms it 'knows.' We build a consistent entity profile across your site, directories, and the open web so the model recognizes your firm as a credible, real-world legal authority.",
  },
  {
    title: "Answer-Ready Content",
    body: "We rewrite and expand your practice-area pages into clear, extractable answers ChatGPT can lift verbatim — definitions, steps, eligibility, and jurisdiction-specific detail that models prefer to cite.",
  },
  {
    title: "Source Reinforcement",
    body: "We strengthen the third-party sources ChatGPT leans on — legal directories, news mentions, and structured data — so the model finds corroborating evidence for your expertise.",
  },
  {
    title: "Track, Re-Prompt & Refine",
    body: "Model behavior changes weekly. We re-run priority prompts on a schedule, monitor mentions, and refine content so your firm's presence in ChatGPT answers compounds over time.",
  },
];

const benefits = [
  {
    icon: TrendingUp,
    title: "Capture Zero-Click Demand",
    body: "More prospects now ask ChatGPT before they ever open Google. If you're not in the answer, you're invisible at the exact moment intent is highest.",
  },
  {
    icon: ShieldCheck,
    title: "Control Your Narrative",
    body: "Without optimization, ChatGPT may describe your firm with outdated or generic detail. We make sure the model repeats accurate, on-brand facts about your practice.",
  },
  {
    icon: Users,
    title: "Win High-Intent Clients",
    body: "People who ask AI for a lawyer are ready to act. Being named as a recommended firm puts you in front of motivated buyers, not casual browsers.",
  },
];

const faqs = [
  {
    question: "Can you really influence what ChatGPT says about my firm?",
    answer:
      "Yes. ChatGPT generates answers from patterns in web content, structured data, and authority signals. By making your firm's expertise clear, consistent, and well-sourced across the web, we increase the probability the model recognizes and recommends you. We measure this against a fixed set of prospect prompts.",
  },
  {
    question: "Does this work for ChatGPT's web browsing and search features?",
    answer:
      "Especially well. ChatGPT Search and browsing pull live results, so on-page clarity, schema markup, and fresh authority signals directly affect whether your pages are retrieved and cited in real time.",
  },
  {
    question: "How is this different from traditional SEO?",
    answer:
      "Traditional SEO optimizes for ranked links a user clicks. ChatGPT optimization targets a single synthesized answer, which rewards extractable, well-structured, entity-rich content rather than keyword density. We do both because they reinforce each other.",
  },
  {
    question: "How soon will I see my firm mentioned?",
    answer:
      "Some prompt improvements appear within weeks as content is re-crawled; broader, durable presence builds over two to four months as authority signals accumulate. We report movement on your tracked prompts every reporting cycle.",
  },
  {
    question: "Will this hurt my Google rankings?",
    answer:
      "No. The clarity, structure, and authority work that helps ChatGPT also strengthens classic search rankings. Firms typically see gains in both channels at once.",
  },
];

export default function Page() {
  return (
    <>
      <SchemaScript
        schema={serviceSchema(
          NAME,
          DESCRIPTION,
          SITE_URL + "/services/chatgpt-optimization"
        )}
      />
      <SchemaScript
        schema={breadcrumbSchema([
          { name: "Home", url: SITE_URL },
          { name: "Services", url: `${SITE_URL}/services` },
          { name: NAME, url: `${SITE_URL}/services/chatgpt-optimization` },
        ])}
      />

      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[1100px] px-6 py-24 text-white md:px-10">
          <Tag variant="purple">
            <MessageSquare size={13} /> ChatGPT Optimization
          </Tag>
          <h1 className="mt-5 max-w-[820px] text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight">
            Get Your Law Firm Recommended Inside ChatGPT
          </h1>
          <p className="mt-5 max-w-[640px] text-[17px] leading-relaxed text-white/75">
            When prospects ask ChatGPT for a lawyer, the answer names a few
            firms. We make sure yours is one of them — accurately described,
            well-sourced, and ahead of competitors who still ignore AI search.
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
          <Tag variant="purple">What We Do</Tag>
          <h2 className="mt-4 max-w-[760px] text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
            We engineer your firm into ChatGPT&apos;s answers
          </h2>
          <p className="mt-5 max-w-[720px] text-[16px] leading-relaxed text-slate-600">
            ChatGPT has become a first stop for people with legal problems. They
            describe their situation in plain language and expect a direct,
            trustworthy recommendation. Our ChatGPT optimization program makes
            your firm the answer the model returns — combining extractable
            content, a strong entity footprint, and reinforced third-party
            sources. We don&apos;t chase tricks; we make your real expertise
            legible to the model so it cites you with confidence and accuracy.
          </p>
        </div>
      </section>

      <section className="bg-navy/[0.02]">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <Tag variant="gold">How It Works</Tag>
          <h2 className="mt-4 text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
            From invisible to cited in five steps
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
            The firms in the answer win the client
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
              <Search size={20} className="text-pu" />
              <span className="text-[14px] font-semibold text-navy">
                Prompt-level visibility tracking
              </span>
            </div>
            <div className="flex items-center gap-3 rounded-2xl border border-pu/10 bg-white p-5">
              <FileText size={20} className="text-pu" />
              <span className="text-[14px] font-semibold text-navy">
                Answer-ready practice pages
              </span>
            </div>
            <div className="flex items-center gap-3 rounded-2xl border border-pu/10 bg-white p-5">
              <Link2 size={20} className="text-pu" />
              <span className="text-[14px] font-semibold text-navy">
                Reinforced third-party sources
              </span>
            </div>
          </div>
        </div>
      </section>

      <section className="bg-navy/[0.02]">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="overflow-hidden rounded-3xl bg-gradient-to-br from-pu to-pu2 p-10 text-white md:p-14">
            <div className="flex items-center gap-2 text-[12px] font-bold uppercase tracking-[1px] text-white/70">
              <RefreshCcw size={15} /> Ongoing ChatGPT Program
            </div>
            <h2 className="mt-3 max-w-[640px] text-[clamp(24px,2.8vw,36px)] font-extrabold leading-tight">
              ChatGPT optimization built for law firms
            </h2>
            <p className="mt-4 max-w-[600px] text-[16px] leading-relaxed text-white/80">
              Programs start at $1,500/month and include prompt tracking,
              content engineering, entity reinforcement, and monthly reporting
              against your priority questions. No contracts — we earn the renewal
              every month.
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
          <FAQ faqs={faqs} title="ChatGPT Optimization FAQs" />
        </div>
      </section>
    </>
  );
}
