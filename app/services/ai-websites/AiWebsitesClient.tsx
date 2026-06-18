"use client";

import { useState } from "react";
import { Smartphone, Gauge, Code2, Search, Layout, ShieldCheck } from "lucide-react";
import StickyCTA from "@/components/sections/StickyCTA";
import LeadFormModal from "@/components/sections/LeadFormModal";
import FAQ from "@/components/sections/FAQ";
import {
  Section,
  P,
  Pull,
  BulletList,
  InfoCard,
  FeatCard,
  DarkBox,
  MistakeList,
  ProcessSteps,
  ServiceHero,
  TrustBar,
  IntroBox,
  FinalCta,
} from "@/components/sections/ServicePageKit";

const FAQS = [
  {
    question: "What makes an AI-optimised law firm website different?",
    answer:
      "An AI-optimised website is built so that both Google and AI search platforms — ChatGPT, Gemini, Perplexity, and Google AI Overviews — can read, understand, and cite it. That means clean semantic HTML, complete schema markup, fast Core Web Vitals, mobile-first design, and content structured to answer the questions real clients ask. A pretty website that AI can't parse is invisible in the channels that increasingly drive legal leads.",
  },
  {
    question: "Will a new website hurt my existing Google rankings?",
    answer:
      "Not when the migration is handled correctly. We preserve URL structures where possible, implement 301 redirects for any that change, retain and improve existing content, and submit updated sitemaps to Search Console. Done right, a rebuild typically improves rankings because the new site fixes the technical and content issues that were holding the old one back.",
  },
  {
    question: "How long does it take to build a law firm website?",
    answer:
      "Most firm websites launch within four to eight weeks, depending on the number of practice areas, the amount of content to write, and how much custom design is involved. We work in clear phases — strategy, design, content, build, and launch — so you always know where the project stands.",
  },
  {
    question: "Do you write the content or do I have to?",
    answer:
      "We write it. Our team produces practice-area pages, attorney bios, and supporting content built to E-E-A-T standards and structured for both Google and AI extractability. You review and approve everything; you're never handed a blank page and told to fill it in.",
  },
  {
    question: "Is the website mobile-friendly?",
    answer:
      "Every site we build is mobile-first. Google uses your mobile version for ranking, and the majority of legal searches now happen on phones — often by people in urgent situations. The mobile experience is the primary experience, not an afterthought.",
  },
  {
    question: "What is schema markup and why does my site need it?",
    answer:
      "Schema markup is structured code that tells search engines and AI platforms exactly what your content represents — that you're a law firm, who your attorneys are, what services you offer, and how clients rate you. For law firms the key types are LegalService, Attorney, LocalBusiness, FAQPage, and AggregateRating. It's one of the strongest signals that helps AI platforms cite you accurately.",
  },
  {
    question: "Do you handle hosting and maintenance?",
    answer:
      "Yes. We can manage hosting, security, performance monitoring, and ongoing updates so your site stays fast, secure, and current. A law firm website is an asset that needs maintenance — neglected sites slowly decay in performance and rankings.",
  },
];

export default function AiWebsitesClient() {
  const [modalOpen, setModalOpen] = useState(false);
  const open = () => setModalOpen(true);

  return (
    <>
      <ServiceHero
        tag="Service · AI Website Design"
        title="AI-Optimised Websites For"
        highlight="Law Firms"
        sub="A modern law firm website has two jobs: convert anxious visitors into booked consultations, and be readable by the AI platforms that now answer legal questions. We build sites that do both — fast, mobile-first, and engineered to be cited."
        pills={[
          "Mobile-First Design",
          "Core Web Vitals",
          "Legal Schema Markup",
          "Conversion-Focused",
          "AI-Readable Content",
        ]}
        primaryCta="Get A Free Website Audit"
        onPrimary={open}
      />

      <TrustBar
        items={[
          "Built to Be Cited by ChatGPT & Gemini",
          "Core Web Vitals Compliant",
          "Legal Schema Markup",
          "Mobile-First & Accessible",
          "Conversion-Optimised",
        ]}
      />

      <IntroBox>
        <P>
          Most law firm websites were built to look good in a portfolio, not to
          win clients or get found. They load slowly, bury the phone number,
          read like brochures, and carry almost no structured data. For years
          that was survivable. It no longer is. Search is splitting into two
          channels — traditional Google results and AI-generated answers — and a
          website that can&apos;t perform in both leaks leads from every side.
        </P>
        <P>
          We design and build websites specifically for law firms, with a single
          goal: turn the people who land on your site into consultations, while
          making your firm legible to the AI platforms that increasingly stand
          between a prospect and their lawyer.
        </P>
      </IntroBox>

      <Section
        tag="The Problem"
        title={
          <>
            Why Most Law Firm Websites{" "}
            <span className="text-pu">Quietly Underperform</span>
          </>
        }
      >
        <P>
          When we audit a firm&apos;s existing site, the same problems show up
          again and again. None of them are obvious from the outside — the site
          looks fine. But each one costs leads every single day.
        </P>
        <MistakeList
          items={[
            {
              title: "Slow load times",
              body: "Uncompressed images and bloated themes push Core Web Vitals into the red. Visitors leave before the page renders, and Google ranks you lower for it.",
            },
            {
              title: "No structured data",
              body: "Without schema markup, search engines and AI platforms have to guess what your firm is and does. Most legal sites have none — or have it implemented incorrectly.",
            },
            {
              title: "Brochure-style content",
              body: "Pages talk about the firm instead of answering the questions prospects actually ask. AI engines can't extract clear answers, so they cite someone else.",
            },
            {
              title: "Weak mobile experience",
              body: "Google ranks your mobile version. If it's clumsy, slow, or hard to navigate, your rankings reflect that — no matter how polished the desktop site looks.",
            },
            {
              title: "Hidden conversion paths",
              body: "The phone number, the consultation form, the next step — all buried. A motivated client shouldn't have to hunt for a way to reach you.",
            },
          ]}
        />
      </Section>

      <Section
        tag="Our Approach"
        title={
          <>
            Built For Clients{" "}
            <span className="text-pu">And For AI</span>
          </>
        }
      >
        <P>
          Every site we build balances two audiences: the human deciding whether
          to call you, and the AI deciding whether to cite you. These goals
          reinforce each other — the clarity, speed, and structure that help a
          stressed visitor also make your content easy for a model to read and
          recommend.
        </P>
        <div className="my-7 grid gap-4 sm:grid-cols-2">
          <InfoCard icon={<Gauge size={20} />} title="Performance First">
            Lightweight builds, optimised images, and clean code that pass Core
            Web Vitals and load fast on real-world mobile connections.
          </InfoCard>
          <InfoCard icon={<Code2 size={20} />} title="Complete Schema">
            LegalService, Attorney, LocalBusiness, FAQPage, and AggregateRating
            markup so engines and AI know exactly who you are.
          </InfoCard>
          <InfoCard icon={<Smartphone size={20} />} title="Mobile-First">
            Designed for the phone first, where most urgent legal searches
            happen, then scaled up to desktop.
          </InfoCard>
          <InfoCard icon={<Search size={20} />} title="AI-Readable Content">
            Practice pages structured as clear, extractable answers to the real
            questions prospects ask ChatGPT and Gemini.
          </InfoCard>
          <InfoCard icon={<Layout size={20} />} title="Conversion Design">
            Obvious next steps, prominent contact paths, and trust signals
            positioned exactly where decisions get made.
          </InfoCard>
          <InfoCard icon={<ShieldCheck size={20} />} title="Compliant & Secure">
            HTTPS, accessibility, and bar-advertising-aware copy baked in from
            the start, not bolted on later.
          </InfoCard>
        </div>
      </Section>

      <Section
        tag="What's Included"
        title={
          <>
            The Foundation Every{" "}
            <span className="text-pu">Page Is Built On</span>
          </>
        }
      >
        <div className="my-7 grid gap-3.5 sm:grid-cols-2 lg:grid-cols-3">
          <FeatCard emoji="⚡" title="Core Web Vitals">
            LCP, INP, and CLS optimised and monitored so performance never
            drifts back into the red.
          </FeatCard>
          <FeatCard emoji="🏷️" title="Schema Markup">
            Validated structured data across every page type that matters for a
            law firm.
          </FeatCard>
          <FeatCard emoji="📱" title="Mobile-First">
            Designed and tested on real devices, where the majority of legal
            searches begin.
          </FeatCard>
          <FeatCard emoji="✍️" title="Written Content">
            E-E-A-T-grade practice pages and attorney bios produced by our team.
          </FeatCard>
          <FeatCard emoji="🔒" title="Security & HTTPS">
            SSL, hardening, and monitoring as a baseline, not an upsell.
          </FeatCard>
          <FeatCard emoji="🗺️" title="Sitemaps & Indexing">
            Clean XML sitemaps submitted to Search Console so every page gets
            discovered.
          </FeatCard>
        </div>
        <Pull>
          A website is the only marketing asset you fully own. Built right, it
          works for your firm in Google, in AI answers, and in front of every
          visitor — every day, without an ad budget keeping it alive.
        </Pull>
      </Section>

      <Section
        tag="How It Works"
        title={
          <>
            From Strategy{" "}
            <span className="text-pu">To Launch</span>
          </>
        }
      >
        <ProcessSteps
          steps={[
            {
              title: "Strategy & Audit",
              body: "We map your practice areas, target markets, and the questions your prospects ask — then audit your current site for technical, content, and conversion gaps.",
            },
            {
              title: "Design & Structure",
              body: "We design a mobile-first layout around clear conversion paths and an information architecture that both visitors and AI engines can navigate intuitively.",
            },
            {
              title: "Content & Schema",
              body: "Our team writes answer-ready practice pages and bios, then implements complete, validated schema markup across the site.",
            },
            {
              title: "Build & Optimise",
              body: "We build on a fast, lightweight foundation, tune Core Web Vitals, and test across real devices before anything goes live.",
            },
            {
              title: "Launch & Monitor",
              body: "We migrate carefully with proper redirects, submit sitemaps, and monitor performance, rankings, and AI citations after launch.",
            },
          ]}
        />
        <DarkBox
          title="What you get when it's done right"
          items={[
            "A site that loads fast and passes Core Web Vitals on mobile.",
            "Complete, validated schema that helps AI platforms cite you accurately.",
            "Practice pages structured to win both Google rankings and AI answers.",
            "Clear conversion paths that turn anxious visitors into booked consultations.",
            "An owned asset that keeps working without ongoing ad spend.",
          ]}
        />
      </Section>

      <Section
        tag="Why It Matters"
        title={
          <>
            The Website Is Where{" "}
            <span className="text-pu">Visibility Becomes Revenue</span>
          </>
        }
      >
        <P>
          You can rank on Google and get named by ChatGPT, but if the prospect
          lands on a slow, confusing page, the lead is lost at the finish line.
          Your website is the conversion point for every other channel you
          invest in. It&apos;s also the single source AI platforms read most
          directly when deciding whether to recommend your firm.
        </P>
        <BulletList
          items={[
            "Most legal searches now happen on mobile, often in urgent situations.",
            "AI platforms read your site structure and schema to decide what to cite.",
            "A faster, clearer site converts more of the traffic you already earn.",
            "Owned assets compound — unlike ads, they don't stop the moment you stop paying.",
          ]}
        />
      </Section>

      <FAQ faqs={FAQS} title="Frequently Asked Questions" />

      <FinalCta
        title="Let's Build A Website That"
        highlight="Wins Clients"
        body="A free website audit takes less than 24 hours and shows you exactly where your current site is leaking leads — in speed, structure, content, and AI readability. No obligation. Just honest data."
        primaryCta="Get A Free Website Audit"
        onPrimary={open}
        note="No obligation. No hard sell. Just a straightforward look at how your website is performing."
      />

      <StickyCTA
        message="Is Your Website Costing You Clients?"
        ctaText="Get My Free Website Audit"
        onCtaClick={open}
      />
      <LeadFormModal
        isOpen={modalOpen}
        onClose={() => setModalOpen(false)}
        offer="Free Website Audit"
        title="Is Your Website Costing You Clients?"
        description="We'll run a full audit of your firm's website — speed, mobile experience, schema, content, and conversion paths — and show you exactly what to fix. Free, with no obligation."
      />
    </>
  );
}
