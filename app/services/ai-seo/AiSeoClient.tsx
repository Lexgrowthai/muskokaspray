"use client";

import { useState } from "react";
import { Shield, Briefcase, Clock, MapPin, Users, FileText } from "lucide-react";
import StickyCTA from "@/components/sections/StickyCTA";
import LeadFormModal from "@/components/sections/LeadFormModal";
import FAQ from "@/components/sections/FAQ";
import {
  Section,
  P,
  H3,
  Pull,
  BulletList,
  InfoCard,
  FeatCard,
  DarkBox,
  DataTable,
  MistakeList,
  ProcessSteps,
  ServiceHero,
  TrustBar,
  IntroBox,
  FinalCta,
} from "@/components/sections/ServicePageKit";

/* ---------- page data ---------- */

const FAQS = [
  {
    question: "What is AI SEO for law firms?",
    answer:
      "AI SEO for law firms is the practice of optimising your firm's online presence to rank in traditional Google search results and to be cited by AI search platforms like ChatGPT, Google AI Overviews, Gemini, and Perplexity. It combines technical SEO, local SEO, structured content strategy, and AI-specific optimisation signals into a unified approach.",
  },
  {
    question: "How long does law firm SEO take to show results?",
    answer:
      "Most law firms start seeing meaningful ranking movement within three to six months of consistent SEO work. Highly competitive markets — personal injury in major metros, for example — can take nine to twelve months before you're competing for top positions. The gains compound over time, which is why starting early is always the right call.",
  },
  {
    question: "What makes legal SEO different from other industries?",
    answer:
      "Legal content falls under Google's YMYL category, which means it's held to higher quality standards than most industries. Google's quality raters explicitly evaluate E-E-A-T signals for legal pages. On top of that, bar advertising rules govern what you can say about your results and credentials — an SEO strategy for law firms has to account for both Google's standards and professional ethics rules.",
  },
  {
    question: "Does local SEO still matter for law firms?",
    answer:
      "Absolutely. Most legal matters are geographically bound — clients want an attorney licensed in their jurisdiction and familiar with their local courts. The Google Maps pack (the three results that appear prominently for local searches) drives a substantial share of legal leads online, and appearing there requires deliberate local SEO work: optimised Google Business Profile, consistent citations, and location-specific content.",
  },
  {
    question: "How do I get my law firm cited by ChatGPT or Perplexity?",
    answer:
      "AI platforms draw from web content they evaluate as authoritative and well-structured. To be cited, your firm needs content that directly answers legal questions, is attributed to named attorneys with verifiable credentials, uses proper schema markup, references authoritative sources, and is published on a technically sound website. Entity consistency across all your online profiles also matters.",
  },
  {
    question: "What is E-E-A-T and why does it matter for law firm SEO?",
    answer:
      "E-E-A-T stands for Experience, Expertise, Authoritativeness, and Trustworthiness. These are the four qualities Google's quality raters explicitly evaluate for legal content. Experience means demonstrated real-world practice in the area. Expertise means qualified authors with verifiable credentials. Authoritativeness means the firm is recognised by others in its field. Trustworthiness means the content is accurate, honest, and doesn't mislead. All four need to be demonstrated throughout your website — you can't just claim them.",
  },
  {
    question: "How important is Google Business Profile for attorney SEO?",
    answer:
      "Extremely important. Your Google Business Profile determines whether you appear in the Google Maps pack — the three local results that dominate for location-specific searches. A well-optimised profile with complete information, regular posts, photos, and active review management consistently outranks neglected profiles, often regardless of website quality. It's the single highest-leverage local SEO asset most law firms have, and it's free.",
  },
  {
    question: "Should I worry about Google AI Overviews reducing my traffic?",
    answer:
      "For some informational queries, AI Overviews do reduce click-through rates — the question gets answered before anyone visits your site. The strategic response is twofold: make sure your content is what Google cites as a source (brand exposure even without a click), and prioritise content that drives decisions rather than just informs.",
  },
  {
    question: "What is schema markup and which types matter for law firms?",
    answer:
      "Schema markup is structured code that tells search engines and AI platforms exactly what your content represents. For law firms, the most valuable types are LegalService, LocalBusiness, Attorney, FAQPage, and AggregateRating. Most law firm websites either lack schema entirely or have validation errors.",
  },
  {
    question: "How much does law firm SEO cost?",
    answer:
      "This varies considerably depending on your market's competitiveness, the number of practice areas, whether you need new content created or existing content improved, and the scope of technical work required. The more useful question is what a consistent source of qualified organic leads is worth compared to what you're currently paying per lead through paid advertising. We'll show you that comparison after a proper audit.",
  },
  {
    question: "What's the difference between law firm SEO and paid search?",
    answer:
      "Paid search produces leads immediately but stops the moment you stop paying — and legal clicks can cost $50–$200 each in competitive markets. SEO builds an asset over time; it takes months to show results but the traffic doesn't evaporate when you stop paying. The best-performing firms use both: paid search for immediate volume while building the organic foundation that becomes their most cost-efficient long-term channel.",
  },
];

export default function AiSeoClient() {
  const [modalOpen, setModalOpen] = useState(false);
  const open = () => setModalOpen(true);

  return (
    <>
      <ServiceHero
        tag="Service · AI SEO"
        title="AI SEO For"
        highlight="Law Firms"
        sub="Ranking on Google is table stakes. The real opportunity now is showing up in Google AI Overviews, getting cited by ChatGPT, and becoming the source Perplexity recommends when someone asks a legal question in your market."
        pills={[
          "Law Firm SEO",
          "Local SEO",
          "AI Search Optimisation",
          "Attorney Content Strategy",
          "E-E-A-T Compliance",
        ]}
        primaryCta="Get A Free SEO Audit"
        onPrimary={open}
      />

      <TrustBar
        items={[
          "Ranked in ChatGPT & Gemini Answers",
          "E-E-A-T Content Standards",
          "Legal Schema Markup",
          "Built for North American Law Firms",
          "Transparent Monthly Reporting",
        ]}
      />

      <IntroBox>
        <P>
          Most law firms think about SEO the way it worked in 2015. You pick
          some keywords, write some pages, build a few links, and wait for
          Google to send you traffic. That approach still produces some results.
          But it&apos;s leaving most of the opportunity on the table.
        </P>
        <P>
          The search landscape for attorneys has changed materially in the last
          two years. Google&apos;s AI Overviews now appear at the top of
          millions of legal searches — synthesising answers before anyone sees a
          list of links. ChatGPT gets asked legal questions millions of times
          per day. Perplexity, Gemini, and other AI platforms are recommending
          law firms directly to people who describe their legal problem in plain
          language.
        </P>
        <P>
          If your firm isn&apos;t being cited in those answers, you&apos;re
          invisible to a growing segment of the market. The attorneys who
          understand this now — and build their content and technical foundation
          to address it — will have a measurable advantage over firms that catch
          up two years from now.
        </P>
        <P>
          That&apos;s what AI SEO for law firms is actually about. Not tricks.
          Not shortcuts. A thorough, technically grounded approach to making
          your firm the source that both Google and AI platforms trust and
          recommend when someone in your market needs a lawyer.
        </P>
      </IntroBox>

      <Section
        tag="The Difference"
        title={
          <>
            Why Law Firm SEO Is Different From{" "}
            <span className="text-pu">Other Industries</span>
          </>
        }
      >
        <P>
          You can take a general SEO playbook and apply it to an e-commerce
          store, a restaurant, or a software company and get decent results.
          Apply the same playbook to a law firm and you&apos;ll run into walls
          that don&apos;t exist in other industries.
        </P>
        <P>
          Legal content sits in what Google calls YMYL territory — Your Money or
          Your Life. These are topics where bad advice can genuinely harm
          someone. Legal, medical, and financial content is held to a higher
          evidentiary standard by Google&apos;s quality raters, which means
          thin, generic, or poorly attributed content gets downgraded where
          similar content in other industries might get a pass.
        </P>
        <P>
          On top of that, lawyer advertising rules — which vary by state and
          province — govern what you can and cannot say about your results, your
          credentials, and your services. An SEO strategy that&apos;s perfectly
          legal for a marketing agency can violate bar advertising rules when
          applied to a law firm.
        </P>
        <div className="my-7 grid gap-4 sm:grid-cols-2">
          <InfoCard icon={<Shield size={18} />} title="YMYL Content Standards">
            Google applies stricter quality evaluation to legal content than to
            most categories. Generic, thin, or unattributed pages will
            underperform regardless of keyword optimisation.
          </InfoCard>
          <InfoCard icon={<Briefcase size={18} />} title="Bar Advertising Rules">
            State and provincial bar associations govern what attorneys can
            claim in marketing materials. Your SEO content must comply —
            including testimonials, results claims, and specialty designations.
          </InfoCard>
          <InfoCard icon={<Clock size={18} />} title="E-E-A-T Is Non-Negotiable">
            Experience, Expertise, Authoritativeness, Trustworthiness.
            Google&apos;s quality raters assess these explicitly for legal
            content. They can&apos;t be faked — they need to be demonstrated
            throughout the site.
          </InfoCard>
          <InfoCard icon={<MapPin size={18} />} title="Hyper-Local Competition">
            Legal searches are intensely local. A family law firm in Denver
            doesn&apos;t compete nationally — it competes with forty other
            Denver family law firms for a relatively fixed pool of local
            searches.
          </InfoCard>
          <InfoCard
            icon={<Users size={18} />}
            title="High-Value, Low-Volume Keywords"
          >
            Legal keywords are expensive on paid search and contested in
            organic. A single personal injury client can be worth tens of
            thousands of dollars — which means competitors invest heavily in
            SEO.
          </InfoCard>
          <InfoCard
            icon={<FileText size={18} />}
            title="Practice Area Depth Required"
          >
            A general practice page doesn&apos;t rank against dedicated practice
            area pages. Legal SEO requires depth — individual pages for each area
            and often for specific case types within each area.
          </InfoCard>
        </div>
      </Section>

      <Section
        tag="Search Is Changing"
        title={
          <>
            How AI Has Changed <span className="text-pu">Legal Search</span>
          </>
        }
      >
        <P>
          Two years ago, if someone searched &quot;what to do after a car
          accident in Texas,&quot; they got a list of ten blue links and clicked
          the one that looked most relevant. Today, they often get a Google AI
          Overview that synthesises the key steps directly on the results page —
          and may not click any link at all.
        </P>
        <P>
          That&apos;s a meaningful shift in how traffic flows. Informational
          legal queries are being partially answered before anyone reaches a
          website. Here&apos;s what&apos;s actually happening:
        </P>
        <BulletList
          items={[
            <>
              <strong>AI Overviews cite sources.</strong> When Google
              synthesises an answer, it still links to the sources it drew from.
              Firms whose content is cited get brand exposure even when
              click-throughs decline.
            </>,
            <>
              <strong>Conversational search is growing.</strong> People are
              asking ChatGPT and Gemini questions they used to Google. These
              platforms need sources — and they pull from authoritative web
              content.
            </>,
            <>
              <strong>Decision-stage content still drives clicks.</strong>{" "}
              &quot;What to do after an accident&quot; might get answered by AI.
              &quot;How much does a car accident lawyer in Austin cost&quot; is
              more likely to send someone to your website.
            </>,
            <>
              <strong>E-E-A-T content wins both channels.</strong> The content
              that ranks well in traditional search is largely the same content
              that gets cited by AI platforms. The investment is not duplicated.
            </>,
          ]}
        />
        <Pull>
          The firms that will struggle are those doing nothing in response to
          these changes. The ones that will win are those building content
          deliberately designed to be the authoritative source — in both
          traditional search results and AI-generated answers.
        </Pull>
      </Section>

      <Section
        tag="Technical SEO"
        title={
          <>
            The Technical Foundation Every{" "}
            <span className="text-pu">Law Firm Needs</span>
          </>
        }
      >
        <P>
          Good content on a technically broken website won&apos;t rank.
          Technical SEO is the infrastructure layer — the work that makes sure
          search engines can find, crawl, index, and understand your site before
          any content strategy has a chance to work. The most common issues we
          find are surprisingly consistent:
        </P>
        <div className="my-7 grid gap-3.5 sm:grid-cols-2 lg:grid-cols-3">
          <FeatCard emoji="⚡" title="Core Web Vitals">
            Google&apos;s performance metrics — LCP, INP, and CLS — are ranking
            factors. Most law firm websites fail at least one. Uncompressed
            images are the most common culprit.
          </FeatCard>
          <FeatCard emoji="🔍" title="Crawlability">
            Pages accidentally blocked by robots.txt, noindex tags, or redirect
            chains can&apos;t be indexed. We regularly find pages invisible to
            Google for months.
          </FeatCard>
          <FeatCard emoji="🏷️" title="Schema Markup">
            LegalService, Attorney, LocalBusiness, FAQPage — structured data
            tells search engines and AI platforms exactly what your firm is.
            Most legal sites lack it or have it wrong.
          </FeatCard>
          <FeatCard emoji="🔒" title="HTTPS & Security">
            SSL is a baseline ranking factor and a trust signal. A browser
            security warning on a legal website kills your conversion rate
            before the page loads.
          </FeatCard>
          <FeatCard emoji="📱" title="Mobile-First Indexing">
            Google ranks you based on your mobile version. If your mobile
            experience is poor, your rankings reflect that — regardless of how
            polished your desktop site looks.
          </FeatCard>
          <FeatCard emoji="🗺️" title="Sitemap & Indexing">
            A properly structured XML sitemap submitted to Search Console
            ensures your pages are discovered and indexed. Missing pages are
            common on poorly maintained legal sites.
          </FeatCard>
        </div>
        <P>
          A technical SEO audit is always the starting point for our
          engagements. There&apos;s no point building content on a foundation
          that&apos;s sending mixed signals to Google or blocking the pages you
          want to rank.
        </P>
      </Section>

      <Section
        tag="Local SEO"
        title={
          <>
            Local SEO For Law Firms:{" "}
            <span className="text-pu">How It Actually Works</span>
          </>
        }
      >
        <P>
          The majority of legal matters are geographically bound. Someone
          looking for a criminal defense lawyer in Phoenix isn&apos;t going to
          hire a firm based in Boston. Local SEO is about making sure your firm
          dominates the search results in your actual service area.
        </P>
        <H3>Google Business Profile</H3>
        <P>
          Your Google Business Profile is the single most important local SEO
          asset most law firms have. It determines whether you appear in the
          Google Maps pack — the three results shown prominently above the
          organic listings for location-specific searches.
        </P>
        <BulletList
          items={[
            "Complete every field — including services, service areas, and the description",
            "Use your primary practice area as the main business category",
            "Post updates regularly — Google treats active profiles as more credible",
            "Respond to every review, positive and negative",
            "Add photos of your office, your team, and your community involvement",
          ]}
        />
        <H3>Local Citations and NAP Consistency</H3>
        <P>
          A citation is any online mention of your firm&apos;s name, address,
          and phone number. If your phone number is listed differently on Yelp
          than on Avvo than on your website, those inconsistencies reduce the
          confidence Google has in your location data. The legal industry has
          its own high-value citation sources: Avvo, Martindale-Hubbell, Justia,
          FindLaw, Super Lawyers, and state bar directories.
        </P>
        <H3>Multi-Location Strategy</H3>
        <P>
          Firms with multiple offices can dominate in multiple markets — but
          only if each location is treated as its own SEO entity: a separate
          Google Business Profile per location, location-specific pages with
          genuinely local content, and citation building for each office
          individually. Copy-pasting the same content with a different city name
          doesn&apos;t work.
        </P>
      </Section>

      <Section
        tag="Content Strategy"
        title={
          <>
            Content That Actually{" "}
            <span className="text-pu">Ranks and Converts</span>
          </>
        }
      >
        <P>
          The content that ranks well for legal keywords today looks very
          different from the keyword-stuffed practice area pages that worked a
          decade ago. E-E-A-T content for law firms means pages that demonstrate
          all four signals explicitly: Experience, Expertise, Authoritativeness,
          and Trustworthiness.
        </P>
        <H3>Thin Content vs Deep Content: The Performance Gap</H3>
        <DataTable
          headers={[
            "Signal",
            "Thin Content (Under 500 Words)",
            "Deep Content (1,200+ Words)",
          ]}
          rows={[
            [
              <strong key="a">Average ranking position</strong>,
              "Page 2–3 for competitive terms",
              "Page 1, positions 1–5",
            ],
            [
              <strong key="b">Featured snippet eligibility</strong>,
              "Rarely eligible",
              "Frequently eligible with proper structure",
            ],
            [
              <strong key="c">AI Overview citation</strong>,
              "Almost never cited",
              "Cited regularly when structured well",
            ],
            [
              <strong key="d">Time on page</strong>,
              "Under 45 seconds average",
              "2–4 minutes average",
            ],
            [
              <strong key="e">Bounce rate</strong>,
              "High (80%+)",
              "Lower (45–60%)",
            ],
            [
              <strong key="f">Conversion rate from organic</strong>,
              "Low — doesn't build enough trust",
              "Higher — answers questions and builds credibility",
            ],
          ]}
        />
        <P>
          This doesn&apos;t mean every page needs to be 2,000 words. But
          practice area pages, FAQ pages, and educational articles that compete
          for informational keywords need genuine depth.
        </P>
      </Section>

      <Section
        tag="AISO"
        title={
          <>
            AI Search Optimisation: Getting Cited by{" "}
            <span className="text-pu">ChatGPT, Gemini &amp; Perplexity</span>
          </>
        }
      >
        <P>
          AI search optimisation — AISO — is the deliberate practice of
          structuring your firm&apos;s content and technical presence to be
          recommended by AI platforms when someone asks a legal question. The
          firms whose content gets cited get brand exposure that wasn&apos;t
          possible three years ago.
        </P>
        <DarkBox
          title="AISO Signals That Get Law Firms Cited by AI Platforms"
          items={[
            <>
              <strong className="text-white">
                Direct, structured answers to specific questions.
              </strong>{" "}
              Paragraphs that open with a clear answer and expand into detail.
            </>,
            <>
              <strong className="text-white">Named attorney attribution.</strong>{" "}
              Content clearly attributed to a qualified attorney with verifiable
              credentials signals authenticity to AI models.
            </>,
            <>
              <strong className="text-white">
                Factual specificity with citations.
              </strong>{" "}
              References to specific statutes, deadlines, and procedures — with
              links to official sources.
            </>,
            <>
              <strong className="text-white">FAQPage schema markup.</strong>{" "}
              Properly implemented FAQ schema makes your Q&amp;A content readable
              directly by AI systems.
            </>,
            <>
              <strong className="text-white">Entity establishment.</strong> Your
              firm&apos;s name, attorneys&apos; names, and practice areas should
              appear consistently across every profile.
            </>,
            <>
              <strong className="text-white">External authority signals.</strong>{" "}
              Bar memberships, directory listings, and press mentions increase
              the credibility signals AI platforms evaluate.
            </>,
          ]}
        />
        <DataTable
          headers={["Dimension", "Traditional SEO", "AI-Optimised SEO"]}
          rows={[
            [
              <strong key="a">Primary goal</strong>,
              "Rank in Google's blue links",
              "Rank in Google + be cited by AI platforms",
            ],
            [
              <strong key="b">Content structure</strong>,
              "Keyword-rich prose with headings",
              "Direct Q&A structure, structured data, entity-rich",
            ],
            [
              <strong key="c">Attribution</strong>,
              "Often anonymous or generic",
              "Named attorney with credentials and bar membership",
            ],
            [
              <strong key="d">Schema markup</strong>,
              "Basic LocalBusiness and breadcrumbs",
              "LegalService, Attorney, FAQPage, Event, Person",
            ],
            [
              <strong key="e">Success metric</strong>,
              "Keyword rankings, organic traffic",
              "Rankings + AI citations + consultation rate",
            ],
          ]}
        />
      </Section>

      <Section
        tag="What We See"
        title={
          <>
            Common SEO Mistakes On{" "}
            <span className="text-pu">Law Firm Websites</span>
          </>
        }
      >
        <P>
          After auditing hundreds of law firm websites, the same problems show
          up again and again. Most are fixable — but they&apos;re holding these
          firms back from the rankings and leads they could be getting.
        </P>
        <MistakeList
          items={[
            {
              title: "Thin Practice Area Pages",
              body: "A 200-word description of your personal injury practice won't outrank a competitor's 1,500-word page that answers the questions prospective clients actually search. Thin pages are one of the most common reasons otherwise competitive firms don't rank for their primary terms.",
            },
            {
              title: "No Schema Markup — Or Broken Schema",
              body: "The majority of law firm websites we audit have either no schema markup or schema that triggers validation errors. Google and AI platforms are then interpreting your site from plain text alone, without the structured signals that confirm what your firm is.",
            },
            {
              title: "Duplicate Location Pages",
              body: "Creating location pages by swapping a city name into identical content is a well-known thin content pattern. Google identifies it easily. These pages rarely rank and can actually dilute the authority of your genuine content.",
            },
            {
              title: "Ignoring Google Business Profile",
              body: "A neglected profile — outdated hours, no photos, unanswered reviews — consistently underperforms in local pack rankings against competitors who maintain theirs actively. The profile is free and has an outsized impact on local visibility.",
            },
            {
              title: "Measuring Only Rankings, Not Revenue",
              body: "Ranking improvement is an intermediate outcome, not the goal. Firms that measure SEO only by rankings often can't connect their organic investment to actual client acquisition — which means they can't justify increased investment.",
            },
          ]}
        />
      </Section>

      <Section
        tag="Our Process"
        title={
          <>
            Our AI SEO <span className="text-pu">Process For Law Firms</span>
          </>
        }
      >
        <P>
          We don&apos;t sell SEO packages. We build a strategy specific to your
          firm&apos;s markets, practice areas, and competitive landscape — then
          execute it consistently over time.
        </P>
        <ProcessSteps
          steps={[
            {
              title: "Technical Audit and Foundation",
              body: "We start by examining your site's technical health — crawlability, Core Web Vitals, schema markup, indexing, site speed, and mobile performance. We fix foundational problems before any content or link work begins.",
            },
            {
              title: "Keyword Research and Competitive Analysis",
              body: "We map out the full keyword landscape for your practice areas and markets — primary terms, long-tail variations, question-based searches, and the queries your target clients type into Google and AI platforms.",
            },
            {
              title: "Content Strategy and Creation",
              body: "We build a content architecture that covers your practice areas in depth — pillar pages, case type pages, FAQ content, and educational articles. Every piece is attributed to named attorneys and structured for both search and AI citation.",
            },
            {
              title: "Local SEO and Citation Building",
              body: "We optimise your Google Business Profile, correct citation consistency across key directories, and build out location-specific content. For multi-location firms, each office gets individual attention.",
            },
            {
              title: "Ongoing Monitoring, Reporting, and Iteration",
              body: "SEO is an ongoing programme. We track rankings, organic traffic, consultation requests from organic, and AI Overview citations monthly — reporting on business outcomes, not just SEO metrics.",
            },
          ]}
        />
      </Section>

      <FAQ faqs={FAQS} title="Frequently Asked Questions" />

      <FinalCta
        title="Let's Talk About Your Firm's"
        highlight="Visibility"
        body="A free SEO audit takes less than 24 hours to produce and shows you exactly where your firm stands — in Google rankings, in local search, and in AI platform citations. No obligation. Just honest data."
        primaryCta="Get A Free SEO Audit"
        onPrimary={open}
        note="No obligation. No hard sell. Just a straightforward conversation about your firm's search visibility."
      />

      <StickyCTA
        message="Where Does Your Firm Show Up on Google?"
        ctaText="Get My Free SEO Report"
        onCtaClick={open}
      />
      <LeadFormModal
        isOpen={modalOpen}
        onClose={() => setModalOpen(false)}
        offer="Free SEO Report"
        title="Where Does Your Firm Show Up on Google?"
        description="We'll run a full SEO health check on your firm — keyword rankings, technical issues, local visibility, and where your competitors are beating you. Free, with no obligation attached."
      />
    </>
  );
}
