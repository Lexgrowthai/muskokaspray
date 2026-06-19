import type { ContentBlock, ArticleStat } from "@/app/insights/[category]/[slug]/content";

export interface SiloArticle {
  slug: string;
  title: string;
  description: string;
  readTime: string;
  date: string;
  stats: ArticleStat[];
  blocks: ContentBlock[];
  faqs: { question: string; answer: string }[];
  related: string[];
}

export const SILO_META = {
  name: "Law Firm Marketing",
  description: "Modern legal marketing strategy for the AI era \u2014 client acquisition, brand building, and the tactics that drive sustainable growth for law firms.",
  slug: "law-firm-marketing",
};

export const ARTICLES: SiloArticle[] = [
  {
    slug: "law-firm-marketing-in-the-age-of-ai",
    title: "Law Firm Marketing in the Age of AI: What Has Changed and What Hasn't",
    description: "AI has fundamentally changed how potential legal clients find, evaluate, and choose law firms. Here is what that means for your marketing strategy.",
    readTime: "13 min read",
    date: "2026-06-18",
    stats: [
      { value: "47%", label: "of legal consumers now use AI before contacting a lawyer" },
      { value: "3x", label: "growth in AI-first legal searches since 2024" },
      { value: "1st", label: "firm to respond wins the engagement 78% of the time" },
    ],
    blocks: [
      { type: "h2", heading: "The Client Journey Has Changed Fundamentally", text: "The Client Journey Has Changed Fundamentally" },
      { type: "p", text: "For most of the last twenty years, the legal client acquisition journey looked like this: a potential client experienced a legal issue, typed some keywords into Google, visited a few websites, read some reviews, and called the firms that seemed most credible. Law firms invested in Google Ads, SEO, and review management to win at each of those stages." },
      { type: "p", text: "That journey still exists, but it now has a new first step for a growing percentage of prospects: asking an AI platform. Before they open Google, before they look at review sites, before they call anyone \u2014 they ask ChatGPT, Gemini, or Perplexity to explain their situation and tell them what to do. If your firm is referenced in that AI answer, you have already won a significant trust advantage before the client has even visited your website." },
      { type: "callout", text: "The marketing funnel now has a pre-funnel. Firms that earn AI citations capture prospects at the very beginning of their legal journey \u2014 before competitors even know the prospect exists." },
      { type: "h2", heading: "What Has Changed in Legal Marketing", text: "What Has Changed in Legal Marketing" },
      { type: "ul", heading: "New realities in legal marketing", items: ["AI platforms are the new first search for a growing segment of legal clients.", "Zero-click searches mean some prospects find your firm and call without ever visiting your website.", "AI citations function like referrals \u2014 they carry implicit trust from the platform.", "Content depth and entity authority now matter more than keyword density.", "Voice search has changed query formats \u2014 conversational questions, not short keywords."] },
      { type: "h2", heading: "What Has Not Changed", text: "What Has Not Changed" },
      { type: "p", text: "The fundamentals of client acquisition have not changed: clients still choose lawyers they trust, with strong reputations, who are easy to reach, and who respond quickly. Excellent client service, strong reviews, community reputation, and referral networks remain as powerful as ever. The difference is in how clients first discover which firms to consider \u2014 and AI is increasingly the gateway to that discovery." },
    ],
    faqs: [
      { question: "Should law firms abandon traditional marketing for AI optimization?", answer: "No. AI search optimization is additive, not a replacement. Traditional SEO, Google Ads, local directories, and referral networks remain highly effective. The firms winning in 2026 are adding AI visibility to their existing marketing stack \u2014 not replacing it." },
      { question: "Which AI platform should law firms focus on first?", answer: "Start where your target clients are. ChatGPT has the most users and broadest reach. Google Gemini is embedded in the search most people already use. Perplexity has a highly educated, research-oriented user base. All three matter \u2014 focus on the content quality and technical signals that help you on all platforms simultaneously." },
      { question: "How do I measure whether my AI marketing is working?", answer: "Track branded search volume in Google Search Console (AI citations drive direct searches), monitor your AI Overview appearances, manually query AI platforms for your target keywords monthly, and ask new clients how they first found your firm \u2014 many will mention AI platforms." },
    ],
    related: ["legal-marketing-strategy-2026", "how-to-get-more-law-firm-leads"],
  },
  {
    slug: "legal-marketing-strategy-2026",
    title: "Legal Marketing Strategy 2026: The Complete Playbook for Growing Your Practice",
    description: "A practical, up-to-date legal marketing strategy for law firms navigating AI search, changing client expectations, and an increasingly competitive landscape.",
    readTime: "14 min read",
    date: "2026-06-18",
    stats: [
      { value: "$143B", label: "US legal services market" },
      { value: "6%", label: "annual growth driven by AI-enabled practices" },
      { value: "Top 3", label: "tactics: AI search, referrals, and Google reviews" },
    ],
    blocks: [
      { type: "h2", heading: "The Four Pillars of Legal Marketing in 2026", text: "The Four Pillars of Legal Marketing in 2026" },
      { type: "ul", heading: "Foundational pillars of modern legal marketing", items: ["AI visibility: appearing in ChatGPT, Gemini, and Perplexity answers for your practice areas.", "Referral systems: systematizing how you generate and nurture referral relationships.", "Review management: building and maintaining a 4.8+ star presence across Google, Avvo, and Martindale.", "Intake optimization: ensuring every lead is captured, qualified, and followed up within minutes."] },
      { type: "h2", heading: "Building an AI-First Content Strategy", text: "Building an AI-First Content Strategy" },
      { type: "p", text: "An AI-first content strategy starts with the questions your prospective clients actually ask AI platforms, not the keywords they historically typed into Google. These are longer, more conversational, and more specific. 'What happens if I'm found at fault in a car accident in Florida?' 'Do I need a lawyer to settle an estate in Ontario?' 'Can I be fired for refusing overtime in California?'" },
      { type: "p", text: "Map these questions to your practice areas, then create authoritative, jurisdiction-specific content that answers them directly. Each piece of content should have a clear structure, schema markup, and internal links to related content in the same practice area. Over time, this network of content builds the topical authority that earns AI citations." },
      { type: "callout", text: "Firms that invest in topical authority today are building a compounding asset. Each piece of content reinforces the others, and the combined signal becomes increasingly hard for competitors to replicate as the content library grows." },
      { type: "h2", heading: "The Referral System Most Law Firms Underestimate", text: "The Referral System Most Law Firms Underestimate" },
      { type: "p", text: "Referrals remain the highest-trust, highest-conversion source of new business for most law firms. Yet most firms have no systematic approach to generating or nurturing them. A basic referral system \u2014 quarterly outreach to referring attorneys, a CRM that tracks referral sources, a clear mutual referral understanding with complementary practices \u2014 can double referral volume within 12 months with modest effort." },
    ],
    faqs: [
      { question: "What is the most cost-effective marketing channel for a small law firm?", answer: "Referral development and Google review management offer the highest ROI for small firms. Combined with basic local SEO and a simple intake process, these three investments can sustainably grow a small practice without significant advertising spend." },
      { question: "How important is social media for law firm marketing?", answer: "It depends on the practice area and target client. Family law and estate planning firms often find LinkedIn and Facebook effective for reaching directly-hiring consumers. Business law and corporate practices find LinkedIn most relevant. Criminal defense firms often see limited social media ROI compared to search and referrals." },
      { question: "Should law firms still invest in Google Ads?", answer: "Yes, particularly for high-value practice areas with urgent need \u2014 personal injury, DUI, family law, immigration. Google Ads provide immediate visibility while organic and AI strategies build over time. The two approaches are complementary." },
    ],
    related: ["law-firm-marketing-in-the-age-of-ai", "how-to-get-more-law-firm-leads"],
  },
  {
    slug: "how-to-get-more-law-firm-leads",
    title: "How to Get More Law Firm Leads: Proven Tactics That Work in 2026",
    description: "A practical, tactics-focused guide to generating more qualified leads for your law firm \u2014 covering AI search, referrals, intake optimization, and paid channels.",
    readTime: "12 min read",
    date: "2026-06-18",
    stats: [
      { value: "5 min", label: "response time that converts 80% more leads" },
      { value: "9x", label: "better odds of qualifying a lead contacted within 5 minutes" },
      { value: "42%", label: "of law firm calls go unanswered \u2014 every one is a lost lead" },
    ],
    blocks: [
      { type: "h2", heading: "The Lead Generation Stack for Law Firms", text: "The Lead Generation Stack for Law Firms" },
      { type: "p", text: "Sustainable lead generation for law firms requires multiple channels working simultaneously. Relying on a single source \u2014 Google Ads, a referral network, or organic traffic \u2014 creates dangerous fragility. The firms with the most predictable growth are running five to seven channels in parallel, so that changes in any one channel do not threaten the entire pipeline." },
      { type: "ul", heading: "Lead generation channels for law firms, ranked by ROI", items: ["Attorney referrals \u2014 highest trust, best conversion rate, typically best value cases.", "Client referrals \u2014 existing clients are your most credible ambassadors.", "Google organic + AI citations \u2014 compounding investment that grows over time.", "Google Business Profile \u2014 local search and Google Maps visibility.", "Legal directories (Avvo, Martindale, FindLaw) \u2014 established traffic for legal queries.", "Google Ads \u2014 immediate visibility for high-intent, high-urgency queries.", "Content marketing and AI optimization \u2014 education-driven lead generation."] },
      { type: "callout", text: "Speed to response is often more important than which channel generated the lead. A lead contacted within 5 minutes of inquiry converts at dramatically higher rates than one reached hours later. Your intake process is a lead generation strategy." },
      { type: "h2", heading: "Fixing the Intake Leak Before Adding More Leads", text: "Fixing the Intake Leak Before Adding More Leads" },
      { type: "p", text: "Before spending more on lead generation, audit your intake process. How quickly does your firm respond to new inquiries? What percentage of calls go unanswered? How many form submissions receive a response within one business day? Most law firms that are unhappy with their lead volume actually have a lead capture and response problem, not a traffic problem. Fix the leak before adding more water." },
    ],
    faqs: [
      { question: "How many leads should a law firm generate per month?", answer: "This depends entirely on practice area, case value, and conversion rates. A personal injury firm might need 50 leads per month to close 5 cases worth $50,000 each. A business law firm might need 10 leads to close 2 retainers worth $30,000 each. Define your lead goal backward from your revenue target." },
      { question: "What is the best way to get referrals from other attorneys?", answer: "Systematize it. Identify 20 attorneys in complementary practice areas in your market. Reach out quarterly \u2014 not to ask for referrals, but to offer value: a useful article, an insight about their practice area, a referral of your own. Consistent, value-first outreach builds the relationships that generate referrals naturally over time." },
      { question: "Should I list my firm on every legal directory?", answer: "Focus on the directories with the most traffic in your practice area and market. For most US firms, priority order is: Avvo, Martindale-Hubbell, FindLaw, Justia, Lawyers.com, and your state bar directory. Claiming and fully completing profiles on these six will cover the majority of directory search volume." },
    ],
    related: ["law-firm-marketing-in-the-age-of-ai", "legal-marketing-strategy-2026"],
  },
];

export const ARTICLE_SLUGS = ARTICLES.map((a) => a.slug);
