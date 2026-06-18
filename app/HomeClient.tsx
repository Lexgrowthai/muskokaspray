"use client";

import { useEffect, useRef, useState } from "react";
import Link from "next/link";
import {
  Sparkles,
  ArrowRight,
  Search,
  Globe,
  MessageSquare,
  PhoneCall,
  Network,
  Target,
  ShieldCheck,
  Handshake,
  Bot,
  CheckCircle2,
  Star,
} from "lucide-react";
import Button from "@/components/ui/Button";
import Tag from "@/components/ui/Tag";
import StickyCTA from "@/components/sections/StickyCTA";
import LeadFormModal from "@/components/sections/LeadFormModal";

const STATS = [
  { value: 4800, suffix: "+", label: "Leads Generated" },
  { value: 432, suffix: "%", label: "Avg Traffic Increase" },
  { value: 3200, suffix: "+", label: "Calls Generated" },
  { value: 12, prefix: "$", suffix: "M+", label: "Revenue Added" },
];

const SERVICES = [
  {
    slug: "ai-search-optimization",
    icon: Sparkles,
    title: "AI Search Optimization",
    desc: "Get your firm cited and recommended across ChatGPT, Gemini, Perplexity, and Google AI Overviews — where clients now ask for lawyers.",
  },
  {
    slug: "ai-seo",
    icon: Search,
    title: "AI SEO",
    desc: "Rank higher on Google and earn AI citations with content architecture, entities, and structured data engineered for legal search.",
  },
  {
    slug: "ai-websites",
    icon: Globe,
    title: "AI Websites",
    desc: "High-converting, mobile-first law firm websites with built-in AI assistants, fast load times, and conversion tracking baked in.",
  },
  {
    slug: "ai-chatbots",
    icon: MessageSquare,
    title: "AI Chatbots",
    desc: "Convert more website visitors into consultations with AI intake assistants that answer questions and book calls 24/7.",
  },
  {
    slug: "ai-receptionists",
    icon: PhoneCall,
    title: "AI Receptionists",
    desc: "Never miss another client call. AI voice receptionists answer, qualify, and book consultations around the clock.",
  },
  {
    slug: "entity-seo",
    icon: Network,
    title: "Entity SEO",
    desc: "Build the authority signals and knowledge-graph entities that make AI platforms trust and surface your firm by name.",
  },
];

const WHY = [
  {
    icon: Target,
    title: "Law Firms Only",
    desc: "Every system we build is engineered around how legal clients search, evaluate, and hire. We don't serve every industry — we master one.",
  },
  {
    icon: ShieldCheck,
    title: "AI-First Methodology",
    desc: "We optimize your firm for every AI search platform, not just traditional Google rankings — positioning you where search is heading.",
  },
  {
    icon: Handshake,
    title: "Long-Term Partnerships",
    desc: "Direct access to your team, transparent reporting, and no junior account managers. We grow with your practice, not in transactions.",
  },
];

const INSIGHTS = [
  {
    href: "/insights/chatgpt",
    tag: "ChatGPT",
    title: "ChatGPT for Law Firms: Why AI Visibility Now Decides Who Gets the Client",
    desc: "More than 100M people ask ChatGPT for recommendations every day. Here's how legal clients use it to find lawyers — and how to get your firm cited.",
  },
  {
    href: "/insights/gemini",
    tag: "Google Gemini",
    title: "Google Gemini for Law Firms: Winning the New AI Overview",
    desc: "Gemini now powers AI Overviews shown across billions of Google searches. Learn what it takes to appear as the answer for legal queries.",
  },
];

const CASES = [
  {
    initials: "PI",
    firm: "Personal Injury Firm — Texas",
    result: "+432% Organic Traffic",
    desc: "Rebuilt their AI website, deployed entity SEO, and optimized for AI search. Within 9 months the firm tripled qualified consultations.",
    stats: [
      { v: "+432%", l: "Traffic" },
      { v: "3.1x", l: "Consults" },
      { v: "$4.2M", l: "Revenue" },
    ],
  },
  {
    initials: "FL",
    firm: "Family Law Practice — Ontario",
    result: "+218 Calls / Month",
    desc: "Added an AI receptionist and chatbot to stop missed calls. Captured after-hours intake and lifted booked consultations dramatically.",
    stats: [
      { v: "+218", l: "Calls/mo" },
      { v: "0", l: "Missed" },
      { v: "+64%", l: "Bookings" },
    ],
  },
];

function useCountUp(target: number, run: boolean, duration = 1600) {
  const [value, setValue] = useState(0);
  useEffect(() => {
    if (!run) return;
    let raf = 0;
    let start: number | null = null;
    const step = (ts: number) => {
      if (start === null) start = ts;
      const progress = Math.min((ts - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      setValue(Math.round(eased * target));
      if (progress < 1) raf = requestAnimationFrame(step);
    };
    raf = requestAnimationFrame(step);
    return () => cancelAnimationFrame(raf);
  }, [target, run, duration]);
  return value;
}

function StatCounter({
  value,
  prefix,
  suffix,
  label,
  run,
}: {
  value: number;
  prefix?: string;
  suffix?: string;
  label: string;
  run: boolean;
}) {
  const count = useCountUp(value, run);
  return (
    <div className="px-5 py-8 text-center transition-colors hover:bg-pu/10">
      <div className="mb-2 text-[clamp(24px,2.8vw,38px)] font-black leading-none tracking-tight text-white">
        {prefix}
        {count.toLocaleString()}
        {suffix}
      </div>
      <div className="text-[12px] font-semibold text-white/45">{label}</div>
    </div>
  );
}

export default function HomeClient() {
  const [isOpen, setIsOpen] = useState(false);
  const [statsRun, setStatsRun] = useState(false);
  const statsRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const node = statsRef.current;
    if (!node) return;
    const observer = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting) {
          setStatsRun(true);
          observer.disconnect();
        }
      },
      { threshold: 0.3 }
    );
    observer.observe(node);
    return () => observer.disconnect();
  }, []);

  return (
    <>
      {/* HERO */}
      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto flex max-w-[760px] flex-col items-center px-6 py-24 text-center md:px-10">
          <span className="mb-6 inline-flex items-center gap-2 rounded-full border border-pu/25 bg-pu/10 px-4 py-2 text-[11px] font-bold uppercase tracking-[0.6px] text-pu3">
            <span className="h-1.5 w-1.5 animate-pulse rounded-full bg-pu" />
            Built For Law Firms, Powered By AI
          </span>
          <h1 className="text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight text-white">
            The AI Growth Platform for{" "}
            <span className="text-grad-purple">Law Firms</span>
          </h1>
          <p className="mt-5 max-w-[480px] text-[clamp(14px,1.5vw,16px)] leading-relaxed text-white/60">
            LexScale.ai helps law firms generate more leads, automate intake,
            reduce missed calls, climb Google rankings, and dominate AI search
            across ChatGPT, Gemini, Perplexity, and Google AI.
          </p>
          <div className="mt-8 flex flex-wrap justify-center gap-3">
            <Button variant="primary" size="lg" onClick={() => setIsOpen(true)}>
              Get a Free Strategy Call
            </Button>
            <Button
              href="/services"
              variant="outline"
              size="lg"
              className="border-white/30 text-white hover:border-pu hover:text-pu3"
            >
              See Our Services <ArrowRight size={16} />
            </Button>
          </div>
          <div className="mt-9 flex flex-wrap justify-center gap-x-5 gap-y-2">
            {[
              "AI Websites",
              "AI Receptionists",
              "AI Chatbots",
              "AI SEO",
              "AI Search Optimization",
            ].map((t) => (
              <span
                key={t}
                className="flex items-center gap-1.5 text-[12px] font-medium text-white/55"
              >
                <span className="flex h-[18px] w-[18px] items-center justify-center rounded-full bg-pu/25 text-pu3">
                  <CheckCircle2 size={11} />
                </span>
                {t}
              </span>
            ))}
          </div>
        </div>

        {/* AI platforms strip */}
        <div className="relative z-10 border-t border-white/10 px-6 py-7 md:px-10">
          <div className="mx-auto max-w-[900px]">
            <p className="mb-5 text-center text-[10px] font-bold uppercase tracking-[0.18em] text-white/25">
              We Optimize Your Firm For Every AI Search Platform
            </p>
            <div className="grid grid-cols-2 gap-3 md:grid-cols-4">
              {[
                { name: "ChatGPT", sub: "100M+ daily users" },
                { name: "Google AI Overviews", sub: "On 1B+ searches" },
                { name: "Gemini", sub: "Built into Google" },
                { name: "Perplexity", sub: "Fastest-growing AI" },
              ].map((p) => (
                <div
                  key={p.name}
                  className="flex items-center gap-3 rounded-2xl border border-white/10 bg-white/5 px-4 py-3.5 transition-colors hover:border-pu/35 hover:bg-pu/15"
                >
                  <span className="flex h-9 w-9 flex-shrink-0 items-center justify-center rounded-xl bg-pu/20 text-pu3">
                    <Sparkles size={16} />
                  </span>
                  <div>
                    <div className="text-[13px] font-bold leading-tight text-white">
                      {p.name}
                    </div>
                    <div className="mt-0.5 text-[10px] text-white/35">
                      {p.sub}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* STATS */}
      <section className="bg-gradient-to-br from-navy via-[#162050] to-[#0d1a3a]">
        <div className="mx-auto max-w-[1100px] px-6 py-16 md:px-10">
          <div
            ref={statsRef}
            className="grid grid-cols-2 gap-px overflow-hidden rounded-3xl border border-pu/15 bg-pu/10 md:grid-cols-4"
          >
            {STATS.map((s) => (
              <div key={s.label} className="bg-white/[0.03]">
                <StatCounter
                  value={s.value}
                  prefix={s.prefix}
                  suffix={s.suffix}
                  label={s.label}
                  run={statsRun}
                />
              </div>
            ))}
          </div>
          <div className="mt-8 flex flex-wrap items-center justify-center gap-x-7 gap-y-2 text-center">
            {[
              "Law firm exclusive",
              "Serving firms since 2013",
              "US & Canada",
            ].map((t) => (
              <span
                key={t}
                className="text-[12px] font-medium text-white/30"
              >
                {t}
              </span>
            ))}
          </div>
        </div>
      </section>

      {/* SERVICES */}
      <section className="bg-gradient-to-b from-[#f8f7ff] to-white">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="mx-auto mb-12 max-w-[520px] text-center">
            <Tag variant="purple" className="mb-4">
              Our Services
            </Tag>
            <h2 className="text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
              AI Systems Built For{" "}
              <span className="text-pu">Law Firms</span>
            </h2>
            <p className="mt-3 text-[16px] leading-relaxed text-slate-500">
              Everything your firm needs to attract clients, capture leads, and
              grow across every search platform that matters.
            </p>
          </div>
          <div className="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {SERVICES.map((svc) => {
              const Icon = svc.icon;
              return (
                <Link
                  key={svc.slug}
                  href={`/services/${svc.slug}`}
                  className="group relative overflow-hidden rounded-2xl border border-pu/10 bg-white p-7 shadow-[0_6px_28px_rgba(11,21,54,.08)] transition-all duration-300 hover:-translate-y-1.5 hover:border-pu/30 hover:shadow-[0_20px_56px_rgba(106,92,255,.13)]"
                >
                  <span className="mb-4 flex h-12 w-12 items-center justify-center rounded-xl bg-pu/10 text-pu transition-colors group-hover:bg-gradient-to-br group-hover:from-pu group-hover:to-pu2 group-hover:text-white">
                    <Icon size={22} />
                  </span>
                  <h3 className="mb-2 text-[16px] font-bold text-navy transition-colors group-hover:text-pu">
                    {svc.title}
                  </h3>
                  <p className="mb-4 text-[13px] leading-relaxed text-slate-500">
                    {svc.desc}
                  </p>
                  <span className="inline-flex items-center gap-1.5 text-[13px] font-semibold text-pu">
                    Learn More <ArrowRight size={14} />
                  </span>
                </Link>
              );
            })}
          </div>
        </div>
      </section>

      {/* WHY LEXSCALE */}
      <section className="bg-white">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="mx-auto mb-12 max-w-[520px] text-center">
            <Tag variant="purple" className="mb-4">
              Why LexScale.ai
            </Tag>
            <h2 className="text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
              A Different Kind of{" "}
              <span className="text-pu">Growth Partner</span>
            </h2>
          </div>
          <div className="grid gap-5 md:grid-cols-3">
            {WHY.map((w) => {
              const Icon = w.icon;
              return (
                <div
                  key={w.title}
                  className="rounded-2xl border border-pu/25 bg-gradient-to-br from-navy to-[#162050] p-7 text-white transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_20px_56px_rgba(106,92,255,.25)]"
                >
                  <span className="mb-4 flex h-12 w-12 items-center justify-center rounded-xl bg-pu/20 text-pu3">
                    <Icon size={22} />
                  </span>
                  <h3 className="mb-2.5 text-[17px] font-extrabold">
                    {w.title}
                  </h3>
                  <p className="text-[13.5px] leading-relaxed text-white/55">
                    {w.desc}
                  </p>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* INSIGHTS */}
      <section className="bg-gradient-to-b from-white to-[#f8f7ff]">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="mb-12 flex flex-wrap items-end justify-between gap-4">
            <div className="max-w-[520px]">
              <Tag variant="purple" className="mb-4">
                Insights
              </Tag>
              <h2 className="text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
                The Future of <span className="text-pu">Legal Search</span>
              </h2>
            </div>
            <Link
              href="/insights"
              className="inline-flex items-center gap-1.5 text-[14px] font-semibold text-pu"
            >
              All insights <ArrowRight size={15} />
            </Link>
          </div>
          <div className="grid gap-5 md:grid-cols-2">
            {INSIGHTS.map((a) => (
              <Link
                key={a.href}
                href={a.href}
                className="group rounded-2xl border border-pu/10 bg-white p-7 shadow-[0_6px_28px_rgba(11,21,54,.08)] transition-all duration-300 hover:-translate-y-1 hover:border-pu/30 hover:shadow-[0_20px_56px_rgba(106,92,255,.13)]"
              >
                <Tag variant="purple" className="mb-4">
                  {a.tag}
                </Tag>
                <h3 className="mb-2.5 text-[18px] font-extrabold leading-snug text-navy transition-colors group-hover:text-pu">
                  {a.title}
                </h3>
                <p className="mb-4 text-[13.5px] leading-relaxed text-slate-500">
                  {a.desc}
                </p>
                <span className="inline-flex items-center gap-1.5 text-[13px] font-semibold text-pu">
                  Read article <ArrowRight size={14} />
                </span>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* CASE STUDIES */}
      <section className="bg-white">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="mx-auto mb-12 max-w-[520px] text-center">
            <Tag variant="gold" className="mb-4">
              Proven Results
            </Tag>
            <h2 className="text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
              Real Growth For{" "}
              <span className="text-grad-gold">Real Firms</span>
            </h2>
          </div>
          <div className="grid gap-5 md:grid-cols-2">
            {CASES.map((c) => (
              <Link
                key={c.firm}
                href="/case-studies"
                className="group rounded-2xl border border-gold/25 bg-gradient-to-br from-[#1a0808] to-[#2a1505] p-7 text-white transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_20px_56px_rgba(212,175,55,.2)]"
              >
                <div className="mb-5 flex items-center gap-3">
                  <span className="flex h-11 w-11 items-center justify-center rounded-xl bg-gradient-to-br from-gold3 to-gold2 text-[14px] font-extrabold text-navy">
                    {c.initials}
                  </span>
                  <div>
                    <div className="text-[14px] font-bold text-white">
                      {c.firm}
                    </div>
                    <div className="text-[13px] font-bold text-gold2">
                      {c.result}
                    </div>
                  </div>
                </div>
                <p className="mb-5 text-[13.5px] leading-relaxed text-white/60">
                  {c.desc}
                </p>
                <div className="grid grid-cols-3 gap-2.5">
                  {c.stats.map((s) => (
                    <div
                      key={s.l}
                      className="rounded-xl border border-white/8 bg-white/5 p-3 text-center"
                    >
                      <div className="text-[18px] font-extrabold tracking-tight text-gold2">
                        {s.v}
                      </div>
                      <div className="mt-0.5 text-[10px] font-semibold text-white/45">
                        {s.l}
                      </div>
                    </div>
                  ))}
                </div>
                <span className="mt-5 inline-flex items-center gap-1.5 text-[13px] font-semibold text-gold2">
                  View case studies <ArrowRight size={14} />
                </span>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* BOTTOM CTA */}
      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[760px] px-6 py-24 text-center md:px-10">
          <div className="mb-3 flex justify-center gap-1 text-gold2">
            {Array.from({ length: 5 }).map((_, i) => (
              <Star key={i} size={16} fill="currentColor" />
            ))}
          </div>
          <p className="mb-7 text-[13px] font-medium text-white/40">
            Trusted by law firms across the United States and Canada
          </p>
          <h2 className="text-[clamp(30px,4vw,52px)] font-black leading-[1.05] tracking-tight text-white">
            Ready to dominate{" "}
            <span className="text-grad-purple">AI search?</span>
          </h2>
          <p className="mx-auto mt-5 max-w-[480px] text-[clamp(15px,2vw,18px)] leading-relaxed text-white/50">
            Get a free strategy call and see exactly where your firm stands in
            AI search — and the fastest path to more clients.
          </p>
          <div className="mt-9 flex flex-wrap justify-center gap-3">
            <Button variant="primary" size="lg" onClick={() => setIsOpen(true)}>
              <Bot size={17} /> Get a Free Strategy Call
            </Button>
            <Button
              href="/services"
              variant="outline"
              size="lg"
              className="border-white/30 text-white hover:border-pu hover:text-pu3"
            >
              Explore Our AI Systems
            </Button>
          </div>
        </div>
      </section>

      <StickyCTA
        message="Ready to dominate AI search?"
        ctaText="Free Strategy Call"
        onCtaClick={() => setIsOpen(true)}
      />
      <LeadFormModal
        isOpen={isOpen}
        onClose={() => setIsOpen(false)}
        offer="Free Strategy Call"
      />
    </>
  );
}
