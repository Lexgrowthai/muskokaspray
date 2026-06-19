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
  name: "Future of Search for Law Firms",
  description: "Search is becoming AI-first. Explore where legal marketing is heading, what AI-first search means for law firms, and how to build a durable advantage now.",
  slug: "future-of-search",
};

export const ARTICLES: SiloArticle[] = [
  {
    slug: "future-of-legal-search",
    title: "The Future of Legal Search: What Law Firms Need to Know",
    description: "AI-powered search is reshaping how potential clients find lawyers. Here is where legal search is heading over the next five years and what firms should do now.",
    readTime: "12 min read",
    date: "2026-06-18",
    stats: [
      { value: "2028", label: "predicted year AI handles majority of initial legal research" },
      { value: "60%", label: "of searches already zero-click \u2014 AI accelerates this" },
      { value: "5x", label: "faster growth projected for AI-visible law firms" },
    ],
    blocks: [
      { type: "h2", heading: "We Are in the Early Innings of an AI Search Revolution", text: "We Are in the Early Innings of an AI Search Revolution" },
      { type: "p", text: "The shift to AI-powered search is not complete \u2014 it is accelerating. In 2024, AI Overviews were a novelty. In 2026, they appear on 40% of all Google searches. By 2028, industry analysts project that AI will handle the majority of initial information-gathering for legal questions, with human Google searches reserved primarily for navigational queries ('Smith Law Firm Toronto') and complex research tasks." },
      { type: "p", text: "For law firms, this trajectory has clear implications. The firms investing in AI visibility today are building an advantage that will compound over the next three to five years. The firms waiting for 'AI to mature before doing anything about it' are falling further behind every month." },
      { type: "callout", text: "The early adopters of Google SEO in the early 2000s built dominant positions that their competitors spent a decade trying to catch up to. AI search is a similar inflection point \u2014 and it is happening right now." },
      { type: "h2", heading: "Where AI Legal Search Is Headed", text: "Where AI Legal Search Is Headed" },
      { type: "ul", heading: "Predictions for AI and legal search through 2030", items: ["AI will increasingly recommend specific law firms by name for local queries.", "Voice-first legal search will become the norm for common legal questions.", "AI will pre-screen legal questions and route prospects to specialized attorneys automatically.", "Multi-turn AI conversations will replace single-query searches for complex legal matters.", "Firms with strong entity profiles and structured data will earn recommendation preference.", "Zero-click searches will eliminate traffic for generic legal content with no entity signals."] },
      { type: "h2", heading: "What Firms Should Do Right Now", text: "What Firms Should Do Right Now" },
      { type: "p", text: "The actions that earn AI citations today are the same actions that will earn them in 2028 \u2014 they just become more valuable over time. Invest in entity authority by building and maintaining consistent profiles across legal directories. Implement complete schema markup on your website. Create comprehensive, jurisdiction-specific content that answers real client questions. These are durable investments that compound." },
    ],
    faqs: [
      { question: "Will AI replace Google for legal searches?", answer: "AI will not replace Google \u2014 Google is becoming AI. The shift is from classic blue-link results to AI-generated answers. Google's AI Overviews are the clearest example: the same Google interface, with AI answers sitting above the traditional results." },
      { question: "How will AI change the way law firms advertise?", answer: "Paid advertising will remain relevant, but it will increasingly appear within AI-generated results rather than alongside traditional blue links. Google's ad strategy is already adapting to include ads within AI Overviews. Organic AI citations will become a primary traffic driver that paid advertising cannot fully replicate." },
      { question: "Should law firms be worried about AI reducing demand for legal services?", answer: "Not in the near term. AI can explain legal concepts and help people understand their options \u2014 but it cannot provide legal advice, represent clients, or make the judgment calls that attorneys are trained to make. AI is more likely to expand access to legal services by helping more people understand when they need a lawyer." },
    ],
    related: ["ai-first-search-for-lawyers", "search-without-clicks-zero-click-search"],
  },
  {
    slug: "ai-first-search-for-lawyers",
    title: "AI-First Search: What It Means for Lawyers and Legal Marketing",
    description: "AI-first search is not a future trend \u2014 it is the present reality for millions of legal searches. Here is what lawyers need to understand and do right now.",
    readTime: "10 min read",
    date: "2026-06-18",
    stats: [
      { value: "AI-first", label: "is the default for Gen Z and Millennial legal research" },
      { value: "73%", label: "of users trust AI-cited sources more than organic results" },
      { value: "Now", label: "is the optimal time to begin AI-first optimization" },
    ],
    blocks: [
      { type: "h2", heading: "Defining AI-First Search", text: "Defining AI-First Search" },
      { type: "p", text: "AI-first search describes a search behavior where the user's first interaction with information about a topic comes through an AI platform \u2014 ChatGPT, Gemini, Perplexity \u2014 rather than a traditional search engine. The user types or speaks a complete question, receives a synthesized answer, and may or may not proceed to click through to a source." },
      { type: "p", text: "For lawyers, the significance is in what happens at the beginning of this process. If a prospect asks 'what should I do if I've been injured in a slip and fall in Seattle' and the AI answer references your firm as a trusted source or cites your content directly, you have captured mindshare before the prospect has ever seen your website. That is a qualitatively different kind of marketing than anything that existed before." },
      { type: "h2", heading: "Who Is Using AI for Legal Research?", text: "Who Is Using AI for Legal Research?" },
      { type: "p", text: "Younger generations are the most enthusiastic AI-first searchers \u2014 but the behavior is spreading rapidly across all age groups. Research from 2025 shows that AI-first legal research is now common among users under 45, and growing among users 45-65. The practical implication: if your firm's most valuable clients are under 50, they are likely using AI platforms for initial legal research already." },
      { type: "callout", text: "The law firms that dismiss AI search because 'our clients are older and don't use ChatGPT' are making a bet that is becoming riskier by the quarter. The demographic adoption curve for AI tools is steep and accelerating." },
    ],
    faqs: [
      { question: "How do I know if my target clients are using AI search?", answer: "Ask them. Include 'how did you first hear about us' and 'what resources did you use before contacting us' in your intake questions. You may be surprised how many clients mention ChatGPT, Gemini, or Perplexity \u2014 even if you've made no effort to optimize for these platforms." },
      { question: "Is AI-first search more common in some practice areas than others?", answer: "Yes. Complex, research-intensive areas like immigration, employment law, and estate planning see high AI-first usage because clients want to understand their situation before speaking to an attorney. Urgent, crisis-driven areas like DUI and personal injury see more direct calls \u2014 though AI is growing even there." },
      { question: "Does AI-first search affect which keywords I should target?", answer: "Yes, significantly. AI-first searchers use conversational, question-based queries rather than keyword phrases. Your content strategy should shift toward full questions and natural language answers, supplementing your existing keyword-optimized pages rather than replacing them." },
    ],
    related: ["future-of-legal-search", "search-without-clicks-zero-click-search"],
  },
  {
    slug: "search-without-clicks-zero-click-search",
    title: "Zero-Click Search: What It Means for Law Firm Visibility",
    description: "60% of searches end without a click. AI is accelerating this trend. Here is what zero-click search means for law firm traffic and how to adapt.",
    readTime: "9 min read",
    date: "2026-06-18",
    stats: [
      { value: "60%", label: "of all searches are zero-click" },
      { value: "AI Overviews", label: "are the primary driver of zero-click legal searches" },
      { value: "Citation", label: "in the zero-click result is the new first-page ranking" },
    ],
    blocks: [
      { type: "h2", heading: "What Is Zero-Click Search?", text: "What Is Zero-Click Search?" },
      { type: "p", text: "A zero-click search is one where the user finds the answer they need directly on the search results page \u2014 or in an AI platform's response \u2014 without clicking through to any website. They ask a question, get an answer, and close the browser. No website visit, no traffic recorded, no conversion opportunity \u2014 at least, not in the traditional sense." },
      { type: "p", text: "For law firms that have built their digital marketing around website traffic metrics, zero-click search is a structural challenge. If a potential client asks Perplexity 'do I need a lawyer for a simple will in Alberta' and gets a direct answer, they may reach out to the firm cited in that answer \u2014 but the firm's website analytics will show zero traffic from that interaction." },
      { type: "callout", text: "In a zero-click world, brand awareness and citation visibility matter more than raw traffic numbers. Being the source that AI cites is worth more than being the website that ranks fifth \u2014 because the user who never clicks still forms an impression based on who the AI trusts." },
      { type: "h2", heading: "Adapting Your Strategy to a Zero-Click World", text: "Adapting Your Strategy to a Zero-Click World" },
      { type: "ul", heading: "Strategic shifts for the zero-click era", items: ["Measure AI citation frequency, not just website traffic.", "Track branded search volume \u2014 AI awareness drives direct searches.", "Optimize for citation as the primary metric, click-through as secondary.", "Build content that earns citation even when not clicked \u2014 accurate, citable summaries.", "Ensure your firm name and contact information appear in AI answers, not just links.", "Monitor offline attribution: clients who arrive through phone calls or direct visits after AI research."] },
    ],
    faqs: [
      { question: "Does zero-click search mean SEO is dead?", answer: "No. SEO remains essential because AI systems draw from well-indexed, authoritative web content. But the goal of SEO is evolving \u2014 from generating clicks to earning citations and brand mentions. The firms treating citation as the KPI, not rank, are adapting correctly." },
      { question: "How do I track zero-click visibility?", answer: "Manual AI queries (checking ChatGPT, Gemini, Perplexity for your target keywords monthly), monitoring Google Search Console for impressions without clicks, tracking branded search volume trends, and asking new clients how they first encountered your firm." },
      { question: "Is zero-click worse for small firms or large firms?", answer: "It is worse for firms of any size that have not built AI visibility. For firms with strong AI citation presence, zero-click is actually an advantage \u2014 they gain brand awareness without having to earn a website visit. The penalty falls on firms that are invisible in AI answers." },
    ],
    related: ["future-of-legal-search", "ai-first-search-for-lawyers"],
  },
];

export const ARTICLE_SLUGS = ARTICLES.map((a) => a.slug);
