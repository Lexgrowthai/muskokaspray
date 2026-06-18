"use client";

import { useMemo, useState } from "react";
import Link from "next/link";
import {
  ArrowRight,
  CalendarDays,
  CheckCircle2,
  Clock,
  List,
  Sparkles,
  TrendingUp,
} from "lucide-react";
import Button from "@/components/ui/Button";
import FAQ from "@/components/sections/FAQ";
import StickyCTA from "@/components/sections/StickyCTA";
import LeadFormModal from "@/components/sections/LeadFormModal";
import type { ArticleStat, ContentBlock } from "./content";

interface RelatedArticle {
  title: string;
  href: string;
}

interface ArticleClientProps {
  title: string;
  category: string;
  categoryHref: string;
  description: string;
  readTime: string;
  date: string;
  stats: ArticleStat[];
  blocks: ContentBlock[];
  faqs: { question: string; answer: string }[];
  related: RelatedArticle[];
}

function slugifyHeading(text: string): string {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, "")
    .trim()
    .replace(/\s+/g, "-");
}

function formatDate(date: string): string {
  return new Date(date).toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });
}

export default function ArticleClient({
  title,
  category,
  categoryHref,
  description,
  readTime,
  date,
  stats,
  blocks,
  faqs,
  related,
}: ArticleClientProps) {
  const [modalOpen, setModalOpen] = useState(false);

  const toc = useMemo(
    () =>
      blocks
        .filter((b) => b.type === "h2" && b.heading)
        .map((b) => ({
          label: b.heading as string,
          id: slugifyHeading(b.heading as string),
        })),
    [blocks]
  );

  return (
    <>
      <article>
        {/* Hero */}
        <section className="hero-gradient relative overflow-hidden">
          <div className="grid-bg absolute inset-0 opacity-40" />
          <div className="relative z-10 mx-auto max-w-[1100px] px-6 py-20 md:px-10">
            <Link
              href={categoryHref}
              className="mb-5 inline-flex items-center gap-1.5 rounded-full border border-pu/30 bg-pu/10 px-3 py-1 text-[12px] font-bold uppercase tracking-wide text-pu3 hover:text-white"
            >
              <Sparkles size={13} /> {category}
            </Link>
            <h1 className="max-w-[820px] text-[clamp(28px,3.6vw,46px)] font-extrabold leading-[1.12] tracking-tight text-white">
              {title}
            </h1>
            <p className="mt-5 max-w-[680px] text-[17px] leading-relaxed text-slate-300">
              {description}
            </p>
            <div className="mt-7 flex flex-wrap items-center gap-5 text-[13px] text-slate-400">
              <span className="inline-flex items-center gap-1.5">
                <Clock size={14} /> {readTime}
              </span>
              <span className="inline-flex items-center gap-1.5">
                <CalendarDays size={14} /> {formatDate(date)}
              </span>
              <span className="inline-flex items-center gap-1.5">
                <Sparkles size={14} /> LexScale Editorial Team
              </span>
            </div>
          </div>
        </section>

        {/* Body + sidebar */}
        <section>
          <div className="mx-auto grid max-w-[1100px] gap-12 px-6 py-16 md:px-10 lg:grid-cols-3">
            {/* Article body */}
            <div className="lg:col-span-2">
              <div className="flex flex-col gap-6">
                {blocks.map((block, i) => (
                  <ContentBlockView key={i} block={block} />
                ))}
              </div>

              <div className="mt-12 rounded-3xl border border-pu/10 bg-gradient-to-br from-pu/5 to-gold/5 p-8">
                <h3 className="text-[22px] font-extrabold tracking-tight text-navy">
                  See where your firm stands in AI search
                </h3>
                <p className="mt-2 max-w-[480px] text-[15px] text-slate-600">
                  Get a free AI visibility check and a strategy call tailored to
                  your practice areas.
                </p>
                <div className="mt-5">
                  <Button
                    variant="primary"
                    size="lg"
                    onClick={() => setModalOpen(true)}
                  >
                    Get a Free Strategy Call
                  </Button>
                </div>
              </div>
            </div>

            {/* Sidebar */}
            <aside className="lg:col-span-1">
              <div className="flex flex-col gap-6 lg:sticky lg:top-24">
                {/* TOC */}
                {toc.length > 0 && (
                  <div className="rounded-2xl border border-pu/10 bg-white p-6 shadow-[0_6px_28px_rgba(11,21,54,.08)]">
                    <h4 className="mb-4 flex items-center gap-2 text-[13px] font-extrabold uppercase tracking-wide text-navy">
                      <List size={15} className="text-pu" /> On this page
                    </h4>
                    <ul className="flex flex-col gap-2.5">
                      {toc.map((item) => (
                        <li key={item.id}>
                          <a
                            href={`#${item.id}`}
                            className="text-[13px] leading-snug text-slate-600 transition-colors hover:text-pu"
                          >
                            {item.label}
                          </a>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}

                {/* Stats */}
                <div className="rounded-2xl border border-pu/10 bg-navy p-6 text-white shadow-[0_6px_28px_rgba(11,21,54,.08)]">
                  <h4 className="mb-4 flex items-center gap-2 text-[13px] font-extrabold uppercase tracking-wide text-pu3">
                    <TrendingUp size={15} /> By the numbers
                  </h4>
                  <div className="flex flex-col gap-4">
                    {stats.map((s) => (
                      <div key={s.label}>
                        <div className="text-[26px] font-extrabold leading-none text-grad-gold">
                          {s.value}
                        </div>
                        <div className="mt-1 text-[12px] text-slate-300">
                          {s.label}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Related */}
                {related.length > 0 && (
                  <div className="rounded-2xl border border-pu/10 bg-white p-6 shadow-[0_6px_28px_rgba(11,21,54,.08)]">
                    <h4 className="mb-4 text-[13px] font-extrabold uppercase tracking-wide text-navy">
                      Related articles
                    </h4>
                    <ul className="flex flex-col gap-3">
                      {related.map((r) => (
                        <li key={r.href}>
                          <Link
                            href={r.href}
                            className="group flex items-start gap-2 text-[13px] font-semibold leading-snug text-navy transition-colors hover:text-pu"
                          >
                            <ArrowRight
                              size={14}
                              className="mt-0.5 flex-shrink-0 text-pu transition-transform group-hover:translate-x-0.5"
                            />
                            {r.title}
                          </Link>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}

                {/* CTA card */}
                <div className="rounded-2xl border border-gold/20 bg-gradient-to-br from-gold/10 to-pu/5 p-6">
                  <h4 className="text-[16px] font-extrabold tracking-tight text-navy">
                    Is your firm what AI recommends?
                  </h4>
                  <p className="mt-2 text-[13px] leading-relaxed text-slate-600">
                    Find out in minutes with a free AI visibility check.
                  </p>
                  <button
                    onClick={() => setModalOpen(true)}
                    className="mt-4 inline-flex w-full items-center justify-center gap-2 rounded-full bg-gradient-to-br from-gold3 to-gold2 px-5 py-2.5 text-[13px] font-bold text-navy shadow-[0_4px_20px_rgba(212,175,55,.3)] transition-all hover:-translate-y-0.5"
                  >
                    Check My Visibility
                    <ArrowRight size={15} />
                  </button>
                </div>
              </div>
            </aside>
          </div>
        </section>

        {/* FAQ */}
        <section className="bg-slate-50/60">
          <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
            <FAQ faqs={faqs} title="Frequently Asked Questions" />
          </div>
        </section>
      </article>

      <StickyCTA
        message="See where your firm ranks in AI search"
        ctaText="Get a Free Strategy Call"
        onCtaClick={() => setModalOpen(true)}
      />

      <LeadFormModal
        isOpen={modalOpen}
        onClose={() => setModalOpen(false)}
        offer="Free AI Visibility Check"
        title="Get Your Free AI Visibility Check"
        description="Tell us about your firm and we'll show you exactly where you stand across ChatGPT, Gemini, and Google AI."
      />
    </>
  );
}

function ContentBlockView({ block }: { block: ContentBlock }) {
  if (block.type === "h2" && block.heading) {
    return (
      <h2
        id={slugifyHeading(block.heading)}
        className="scroll-mt-24 text-[clamp(22px,2.6vw,30px)] font-extrabold tracking-tight text-navy"
      >
        {block.heading}
      </h2>
    );
  }

  if (block.type === "p") {
    return (
      <p className="text-[16px] leading-[1.75] text-slate-700">{block.text}</p>
    );
  }

  if (block.type === "callout") {
    return (
      <div className="rounded-2xl border-l-4 border-pu bg-pu/5 p-6">
        <div className="mb-1 flex items-center gap-2 text-[12px] font-extrabold uppercase tracking-wide text-pu">
          <Sparkles size={14} /> Key insight
        </div>
        <p className="text-[15px] leading-relaxed text-navy">{block.text}</p>
      </div>
    );
  }

  if (block.type === "ul" && block.items) {
    return (
      <div>
        {block.heading && (
          <p className="mb-3 text-[16px] font-bold text-navy">
            {block.heading}
          </p>
        )}
        <ul className="flex flex-col gap-3">
          {block.items.map((item, i) => (
            <li
              key={i}
              className="flex items-start gap-3 text-[15px] leading-relaxed text-slate-700"
            >
              <CheckCircle2
                size={18}
                className="mt-0.5 flex-shrink-0 text-pu"
              />
              {item}
            </li>
          ))}
        </ul>
      </div>
    );
  }

  return null;
}
