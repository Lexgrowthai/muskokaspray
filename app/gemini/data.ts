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
  name: "Google Gemini for Law Firms",
  description: "Google is weaving Gemini into Search, Maps, Android, and Workspace. Understand how to appear inside Google's AI-generated answers before your competitors do.",
  slug: "gemini",
};

export const ARTICLES: SiloArticle[] = [
  {
    slug: "google-gemini-for-law-firms",
    title: "Google Gemini for Law Firms: The Complete Visibility Guide",
    description: "Google Gemini is now embedded in Search, Maps, Gmail, and Chrome. Here is how law firms earn visibility inside Google's AI ecosystem.",
    readTime: "13 min read",
    date: "2026-06-18",
    stats: [
      { value: "8.5B", label: "Google searches per day" },
      { value: "40%", label: "of searches now show AI Overviews" },
      { value: "3", label: "sources cited per AI Overview on average" },
    ],
    blocks: [
      { type: "h2", heading: "What Google Gemini Means for Law Firms", text: "What Google Gemini Means for Law Firms" },
      { type: "p", text: "For two decades, winning in Google meant optimizing page titles, building backlinks, and earning positions in the classic blue-link results. That playbook still matters \u2014 but it is no longer the whole game. Google is integrating Gemini, its most advanced AI model, across every surface it controls. The firms that understand this transition early will hold a durable advantage." },
      { type: "p", text: "Gemini is not a separate product people need to discover. It is woven directly into the search interface billions of people use every day. When a potential client types 'family lawyer near me' or 'what to do after a car accident in Toronto,' they increasingly see an AI-generated summary at the top of the page \u2014 before any blue links appear. That summary cites a small number of sources. Being one of those sources is the new front page." },
      { type: "callout", text: "Google processes 8.5 billion searches every day. As Gemini becomes the primary interface for those searches, firms cited in AI Overviews receive visibility that no paid ad can replicate \u2014 and it compounds over time." },
      { type: "h2", heading: "Where Gemini Lives Inside Google's Ecosystem", text: "Where Gemini Lives Inside Google's Ecosystem" },
      { type: "ul", heading: "Gemini appears across all of Google's platforms", items: ["Google Search \u2014 AI Overviews above the blue links on billions of queries.", "Google Maps \u2014 AI-powered answers for 'lawyers near me' and practice area searches.", "Google Assistant on Android \u2014 voice queries answered with Gemini intelligence.", "Gmail and Workspace \u2014 AI writing assistance drawing on Gemini's knowledge.", "Chrome \u2014 in-browser AI help for users researching legal questions."] },
      { type: "h2", heading: "How to Earn Citations in Google AI Overviews", text: "How to Earn Citations in Google AI Overviews" },
      { type: "p", text: "AI Overviews draw on Google's existing index, which means traditional SEO signals still matter. But they add a new dimension: Google must be able to quickly understand what your firm does, where you practice, and whether your content directly answers the question being asked. Structured data, entity signals, and authoritative content work together to earn that trust." },
      { type: "ul", heading: "Priority actions for Gemini visibility", items: ["Build deep topical authority across your specific practice areas.", "Implement LegalService, Attorney, and FAQPage schema on every relevant page.", "Strengthen your Google Business Profile with accurate NAP, reviews, and photos.", "Answer conversational legal questions directly in your content \u2014 not just keywords.", "Earn citations in legal directories, bar association sites, and trusted publications."] },
    ],
    faqs: [
      { question: "Is Google Gemini the same as AI Overviews?", answer: "Gemini is Google's underlying AI model. AI Overviews are one of the most visible outputs \u2014 the AI-generated summaries that appear at the top of search results. Gemini powers many other Google features as well." },
      { question: "Does traditional SEO still matter for Gemini visibility?", answer: "Yes. Gemini draws on Google's existing index, so page authority, backlinks, and on-page optimization all feed into which sources get cited. AI visibility and traditional SEO reinforce each other." },
      { question: "How can a small law firm compete for AI Overview citations?", answer: "Focus on depth and specificity. A detailed, accurate answer to 'what happens during a divorce in Ontario' can earn a citation even for a small firm, because the AI rewards relevance over domain authority alone." },
    ],
    related: ["gemini-ai-overviews-explained", "how-to-rank-in-google-ai-overviews"],
  },
  {
    slug: "gemini-ai-overviews-explained",
    title: "Google AI Overviews Explained: What Law Firms Need to Know",
    description: "AI Overviews now appear on billions of searches. Here is exactly how they work, what they cite, and how law firms can influence them.",
    readTime: "10 min read",
    date: "2026-06-18",
    stats: [
      { value: "1B+", label: "monthly AI Overview impressions" },
      { value: "56%", label: "of users read AI Overviews before clicking" },
      { value: "3\u20135", label: "cited sources per AI Overview" },
    ],
    blocks: [
      { type: "h2", heading: "What Is a Google AI Overview?", text: "What Is a Google AI Overview?" },
      { type: "p", text: "A Google AI Overview is an AI-generated summary that appears at the very top of a search results page \u2014 above all organic links, above ads, and above featured snippets. It synthesizes information from multiple sources to provide a direct answer to a user's question. Each overview cites a handful of sources, displayed as links below the summary text." },
      { type: "p", text: "For law firms, AI Overviews represent an entirely new category of visibility. When a potential client searches for 'do I need a lawyer for probate in Texas' or 'how to file for divorce in Ontario,' the AI Overview may be the only result they read. If your firm is cited as a source, you receive exposure before the user ever reaches a blue link." },
      { type: "callout", text: "Being cited in an AI Overview is not about having the highest-ranking page. It is about having content that Google's AI judges as the most direct, accurate, and authoritative answer to a specific question." },
      { type: "h2", heading: "How Google Chooses What to Cite", text: "How Google Chooses What to Cite" },
      { type: "ul", heading: "What influences AI Overview citations", items: ["Direct question-and-answer structure that maps to the user's intent.", "E-E-A-T signals: Experience, Expertise, Authoritativeness, and Trustworthiness.", "Schema markup that tells Google exactly what the content covers.", "Page authority from backlinks and domain trust.", "Freshness \u2014 recently updated content is often preferred for evolving legal topics."] },
      { type: "h2", heading: "Practical Steps to Appear in AI Overviews", text: "Practical Steps to Appear in AI Overviews" },
      { type: "p", text: "Start by identifying the specific questions your prospective clients ask Google before hiring a lawyer. Tools like Google Search Console, People Also Ask, and Answer the Public reveal these queries. For each high-value question, create a dedicated page or section that answers it directly, accurately, and completely \u2014 then mark it up with FAQPage or Q&A schema." },
    ],
    faqs: [
      { question: "Can I opt out of having my content used in AI Overviews?", answer: "Yes. You can use the nosnippet meta tag or Google Search Console to limit how Google uses your content. However, opting out also removes you from citation consideration." },
      { question: "Do AI Overviews drive traffic to cited websites?", answer: "Citations include clickable links. While some users read only the summary, many click through \u2014 especially for complex legal questions where they want to verify information or contact the firm directly." },
      { question: "How long does it take to start appearing in AI Overviews?", answer: "There is no set timeline. Some firms see citations within weeks of improving their content and schema; others take several months. Consistency and specificity tend to accelerate results." },
    ],
    related: ["google-gemini-for-law-firms", "how-to-rank-in-google-ai-overviews"],
  },
  {
    slug: "how-to-rank-in-google-ai-overviews",
    title: "How Law Firms Rank in Google AI Overviews",
    description: "A practical, step-by-step guide for law firms that want to earn citations in Google's AI-generated search summaries.",
    readTime: "11 min read",
    date: "2026-06-18",
    stats: [
      { value: "68%", label: "of AI Overview sources rank in the top 10 organically" },
      { value: "FAQPage", label: "schema increases citation rate by 2.4x" },
      { value: "90 days", label: "average timeline to first AI Overview citation" },
    ],
    blocks: [
      { type: "h2", heading: "The Foundation: Topical Authority", text: "The Foundation: Topical Authority" },
      { type: "p", text: "Google's AI does not cherry-pick individual pages from random websites. It draws from sources it has determined to be authoritative on a topic. For a family law firm in Vancouver, that means publishing comprehensive, accurate content about family law in British Columbia \u2014 not a single page, but a network of pages that collectively demonstrate deep expertise." },
      { type: "p", text: "Topical authority is built over time through consistent, specific, expert-level content. A firm that has 40 pages answering real family law questions signals depth. A firm with one generic 'family law services' page does not. The former earns AI citations. The latter does not." },
      { type: "h2", heading: "Technical Requirements: Schema and Structure", text: "Technical Requirements: Schema and Structure" },
      { type: "ul", heading: "Must-have technical elements for AI Overview eligibility", items: ["LegalService schema with accurate practice areas, jurisdiction, and contact data.", "FAQPage schema wrapping every Q&A section on your site.", "BreadcrumbList schema on all pages for clear site hierarchy signals.", "Attorney or Person schema for every lawyer on your team.", "LocalBusiness schema reinforcing your geographic service area."] },
      { type: "callout", text: "Schema markup does not guarantee citation \u2014 but its absence almost guarantees exclusion. Google's AI needs machine-readable signals to quickly understand what your content covers and whether it is trustworthy." },
      { type: "h2", heading: "Content Strategy: Answer the Question Behind the Question", text: "Content Strategy: Answer the Question Behind the Question" },
      { type: "p", text: "When someone searches 'do I need a lawyer for a DUI in California,' the literal question is about necessity. But the question behind it is: what happens if I get a DUI, what are the consequences, and how do I protect myself? The firms that answer both questions \u2014 and answer them thoroughly \u2014 are the ones that appear in AI Overviews. Write for the person behind the query, not just the keyword." },
    ],
    faqs: [
      { question: "Does page 1 ranking guarantee an AI Overview citation?", answer: "No, but it helps significantly. About 68% of AI Overview citations come from top-10 organically ranking pages. Building both organic rank and content quality gives you the best odds." },
      { question: "Should I create separate pages for each legal question?", answer: "For high-volume questions, yes. Dedicated pages signal topical relevance more strongly than a single page that briefly mentions many topics. Use your practice area pages as hubs and create supporting content for specific questions." },
      { question: "What content format does Google prefer for AI Overviews?", answer: "Clear, direct answers in plain language. Structured formats like numbered steps, bullet lists, and Q&A sections perform well. Avoid jargon-heavy writing that obscures the core answer." },
    ],
    related: ["google-gemini-for-law-firms", "gemini-ai-overviews-explained"],
  },
];

export const ARTICLE_SLUGS = ARTICLES.map((a) => a.slug);
