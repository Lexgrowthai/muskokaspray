"use client";

import { useState } from "react";
import {
  Sparkles,
  MessageSquare,
  Stars,
  Compass,
  Network,
  Code2,
  Quote,
  Target,
  TrendingUp,
  ShieldCheck,
  Users,
  RefreshCcw,
  Search,
  Zap,
  CheckCircle2,
} from "lucide-react";
import Tag from "@/components/ui/Tag";
import Button from "@/components/ui/Button";
import FAQ from "@/components/sections/FAQ";
import StickyCTA from "@/components/sections/StickyCTA";
import LeadFormModal from "@/components/sections/LeadFormModal";

const steps = [
  {
    title: "AI Visibility Audit",
    body: "We benchmark your firm across ChatGPT, Gemini, Perplexity, and Google AI Overviews using a prompt set built from real prospect questions — establishing exactly where you stand and where competitors beat you.",
  },
  {
    title: "Entity & Authority Foundation",
    body: "AI models only recommend firms they recognize and trust. We build your firm into a clearly defined entity with consistent data, structured markup, and authoritative external signals.",
  },
  {
    title: "Answer-Ready Content Engineering",
    body: "We restructure your practice-area and resource content into clear, extractable, citation-ready passages that AI engines prefer to quote — definitions, steps, eligibility, costs, and jurisdiction detail.",
  },
  {
    title: "Multi-Engine Reinforcement",
    body: "Each engine weighs signals differently. We tune Google ecosystem data for Gemini, source freshness for Perplexity, and authority depth for ChatGPT so you win across all of them.",
  },
  {
    title: "Track, Report & Compound",
    body: "We monitor your citation share every cycle, defend gains, attack new gaps, and report movement against your tracked prompts so your AI presence compounds month over month.",
  },
];

const benefits = [
  {
    icon: TrendingUp,
    title: "Capture Demand at the Source",
    body: "Prospects increasingly ask AI before Google. Being the recommended firm puts you in front of high-intent buyers at the exact moment they decide who to call.",
  },
  {
    icon: ShieldCheck,
    title: "Control the Narrative",
    body: "Left alone, AI describes your firm with generic or outdated detail. We make sure every engine repeats accurate, on-brand facts about your practice.",
  },
  {
    icon: Target,
    title: "Outflank Slow Competitors",
    body: "Most firms still ignore AI search. Moving now builds an authority lead that's expensive for rivals to overtake later.",
  },
  {
    icon: Users,
    title: "One Strategy, Every Engine",
    body: "We optimize ChatGPT, Gemini, Perplexity, and AI Overviews under one coordinated program — and the same work strengthens classic Google rankings too.",
  },
];

const engines = [
  {
    icon: MessageSquare,
    title: "ChatGPT",
    body: "Recommendation and authority optimization for the world's most-used AI assistant.",
    href: "/services/chatgpt-optimization",
  },
  {
    icon: Stars,
    title: "Google Gemini",
    body: "Visibility in Gemini and AI Overviews, anchored to your Google ecosystem.",
    href: "/services/gemini-optimization",
  },
  {
    icon: Compass,
    title: "Perplexity",
    body: "Citation-ready content that earns footnotes and referral traffic.",
    href: "/services/perplexity-optimization",
  },
  {
    icon: Network,
    title: "Entity SEO",
    body: "The recognized-entity foundation every AI recommendation depends on.",
    href: "/services/entity-seo",
  },
  {
    icon: Code2,
    title: "Structured Data",
    body: "Validated schema that makes your content machine-readable and citable.",
    href: "/services/structured-data",
  },
  {
    icon: Quote,
    title: "Citation Tracking",
    body: "Continuous measurement of your mentions and citation share across engines.",
    href: "/services/ai-citation-tracking",
  },
];

const faqs = [
  {
    question: "What is AI Search Optimization (AISO)?",
    answer:
      "AISO is the practice of getting your firm surfaced, recommended, and cited by AI answer engines like ChatGPT, Google Gemini, Perplexity, and Google AI Overviews. As people increasingly ask AI instead of typing keywords into Google, AISO has become the new front line of legal marketing — making sure the synthesized answer names your firm.",
  },
  {
    question: "How is AISO different from traditional SEO?",
    answer:
      "Traditional SEO competes for ranked blue links a user clicks. AISO competes for inclusion in a single AI-generated answer, which rewards clear, extractable, entity-rich, well-sourced content over keyword density. The two are complementary — the authority and clarity work that wins AI citations also lifts classic rankings — so we run them together.",
  },
  {
    question: "Which AI engines do you optimize for?",
    answer:
      "ChatGPT (including ChatGPT Search), Google Gemini and AI Overviews, and Perplexity, supported by entity SEO, structured data, and continuous citation tracking. Each engine weighs signals differently, so our program tunes for all of them under one coordinated strategy.",
  },
  {
    question: "How do you measure AISO results?",
    answer:
      "We track a fixed set of prospect prompts across every major engine and report your citation share, the accuracy of what models say about your firm, and your position versus named competitors each cycle. You see exactly where your firm appears and how that visibility trends over time.",
  },
  {
    question: "How long until my firm shows up in AI answers?",
    answer:
      "Some prompt-level wins appear within weeks as content is re-crawled. Durable, broad presence builds over two to four months as entity recognition and authority signals accumulate. We report movement every cycle so you can see progress compounding.",
  },
];

export default function AISOClient() {
  const [modalOpen, setModalOpen] = useState(false);

  return (
    <>
      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[1100px] px-6 py-28 text-white md:px-10">
          <Tag variant="gold">
            <Sparkles size={13} /> Flagship Program — AISO
          </Tag>
          <h1 className="mt-5 max-w-[860px] text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight">
            Be the Law Firm AI Recommends — Everywhere It Searches
          </h1>
          <p className="mt-5 max-w-[680px] text-[17px] leading-relaxed text-white/75">
            Your future clients are asking ChatGPT, Gemini, and Perplexity who
            to hire. AI Search Optimization makes sure the answer is your firm —
            accurately described, well-sourced, and ahead of competitors across
            every engine that matters.
          </p>
          <div className="mt-8 flex flex-wrap gap-3">
            <Button variant="gold" size="lg" onClick={() => setModalOpen(true)}>
              <Zap size={16} /> Free AI Visibility Audit
            </Button>
            <Button
              href="/tools/ai-visibility-checker"
              variant="outline"
              size="lg"
              className="border-white/25 text-white hover:border-white hover:text-white"
            >
              Get a Free Strategy Call
            </Button>
          </div>
          <div className="mt-10 grid max-w-[640px] grid-cols-2 gap-6 sm:grid-cols-4">
            {[
              ["4,800+", "Leads Generated"],
              ["432%", "Avg Traffic Increase"],
              ["3,200+", "Calls Generated"],
              ["$12M+", "Revenue Added"],
            ].map(([stat, label]) => (
              <div key={label}>
                <div className="text-[26px] font-extrabold text-gold2">
                  {stat}
                </div>
                <div className="mt-1 text-[12px] font-semibold uppercase tracking-wide text-white/55">
                  {label}
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <Tag variant="purple">What We Do</Tag>
          <h2 className="mt-4 max-w-[780px] text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
            We engineer your firm into the AI answer
          </h2>
          <p className="mt-5 max-w-[740px] text-[16px] leading-relaxed text-slate-600">
            AI Search Optimization is our flagship program — the coordinated
            strategy that gets your firm surfaced, recommended, and cited across
            every major answer engine. We start by measuring exactly where you
            stand, then build the foundation AI needs to trust you: a recognized
            entity, clean structured data, and authoritative sources. On top of
            that we engineer answer-ready content and tune each engine to its own
            signals. The outcome is a firm that shows up when prospects ask AI
            for a lawyer — and keeps showing up as we track and compound your
            citation share month over month.
          </p>
        </div>
      </section>

      <section className="bg-navy/[0.02]">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <Tag variant="purple">The AISO System</Tag>
          <h2 className="mt-4 text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
            One program, every engine
          </h2>
          <p className="mt-4 max-w-[680px] text-[16px] leading-relaxed text-slate-600">
            AISO unifies six disciplines into a single strategy. Each can run on
            its own, but together they compound.
          </p>
          <div className="mt-10 grid gap-6 md:grid-cols-3">
            {engines.map((e) => {
              const Icon = e.icon;
              return (
                <a
                  key={e.title}
                  href={e.href}
                  className="group rounded-2xl border border-pu/10 bg-white p-7 shadow-[0_6px_28px_rgba(11,21,54,.08)] transition-all hover:-translate-y-1 hover:border-pu/30"
                >
                  <span className="flex h-12 w-12 items-center justify-center rounded-xl bg-pu/10 text-pu">
                    <Icon size={22} />
                  </span>
                  <h3 className="mt-5 text-[18px] font-bold text-navy group-hover:text-pu">
                    {e.title}
                  </h3>
                  <p className="mt-2 text-[15px] leading-relaxed text-slate-600">
                    {e.body}
                  </p>
                </a>
              );
            })}
          </div>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <Tag variant="gold">How It Works</Tag>
          <h2 className="mt-4 text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
            Our five-step AISO program
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

      <section className="bg-navy/[0.02]">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <Tag variant="purple">Why It Matters</Tag>
          <h2 className="mt-4 text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
            AI is the new front door to your firm
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
              <Search size={20} className="text-pu" />
              <span className="text-[14px] font-semibold text-navy">
                Cross-engine prompt tracking
              </span>
            </div>
            <div className="flex items-center gap-3 rounded-2xl border border-pu/10 bg-white p-5">
              <Network size={20} className="text-pu" />
              <span className="text-[14px] font-semibold text-navy">
                Entity & authority foundation
              </span>
            </div>
            <div className="flex items-center gap-3 rounded-2xl border border-pu/10 bg-white p-5">
              <CheckCircle2 size={20} className="text-pu" />
              <span className="text-[14px] font-semibold text-navy">
                Monthly citation reporting
              </span>
            </div>
          </div>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="overflow-hidden rounded-3xl bg-gradient-to-br from-pu to-pu2 p-10 text-white md:p-14">
            <div className="flex items-center gap-2 text-[12px] font-bold uppercase tracking-[1px] text-white/70">
              <RefreshCcw size={15} /> Flagship AISO Program
            </div>
            <h2 className="mt-3 max-w-[660px] text-[clamp(24px,2.8vw,36px)] font-extrabold leading-tight">
              The complete AI search strategy for your firm
            </h2>
            <p className="mt-4 max-w-[620px] text-[16px] leading-relaxed text-white/80">
              Full AISO programs start at $2,500/month and bundle entity SEO,
              structured data, content engineering, multi-engine optimization,
              and citation tracking with monthly reporting. Month-to-month — we
              earn the renewal every cycle. Start with a free AI visibility
              audit to see exactly where your firm stands.
            </p>
            <div className="mt-8 flex flex-wrap gap-3">
              <Button
                variant="gold"
                size="lg"
                onClick={() => setModalOpen(true)}
              >
                <Zap size={16} /> Free AI Visibility Audit
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
          <FAQ faqs={faqs} title="AI Search Optimization FAQs" />
        </div>
      </section>

      <StickyCTA
        message="Is Your Firm Visible in AI Search?"
        ctaText="Free AI Visibility Audit"
        onCtaClick={() => setModalOpen(true)}
      />

      <LeadFormModal
        isOpen={modalOpen}
        onClose={() => setModalOpen(false)}
        offer="Free AI Visibility Audit"
        title="Claim Your Free AI Visibility Audit"
        description="Tell us about your firm and we'll show you exactly where you stand across ChatGPT, Gemini, and Perplexity — and what it takes to win the answer."
      />
    </>
  );
}
