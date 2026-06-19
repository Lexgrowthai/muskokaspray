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
  name: "Schema Markup for Law Firms",
  description:
    "Schema markup is the fastest technical lever for improving both AI citations and Google rich results. Learn how to implement LegalService, FAQPage, and Attorney schema for maximum visibility.",
  slug: "schema",
};

export const ARTICLES: SiloArticle[] = [
  {
    slug: "schema-markup-for-law-firms",
    title: "Schema Markup for Law Firms: The Complete Technical Guide",
    description:
      "Schema markup helps AI systems and search engines understand your law firm's identity, services, and content. Here is a complete implementation guide for legal websites.",
    readTime: "13 min read",
    date: "2026-01-12",
    stats: [
      { value: "2.5x", label: "more AI citations for law firms with complete schema markup" },
      { value: "35%", label: "higher click-through rates for pages with FAQ rich results" },
      { value: "6", label: "key schema types every law firm website should implement" },
    ],
    blocks: [
      {
        type: "h2",
        heading: "Why Schema Markup Matters More Than Ever for Law Firms",
        text: "Why Schema Markup Matters More Than Ever for Law Firms",
      },
      {
        type: "p",
        text: "Schema markup — structured data embedded in your website's code that explicitly describes your content to machines — has been a best practice in legal SEO for years. But in the era of AI-powered search, its importance has multiplied. AI systems like Google Gemini, ChatGPT, and Perplexity use structured data as a primary signal for understanding what your law firm is, what services it offers, who its attorneys are, and which questions its content answers.",
      },
      {
        type: "p",
        text: "Law firms with complete, accurate schema markup earn AI citations at roughly 2.5 times the rate of equivalent firms without structured data. They appear in Google's FAQ rich results, which display expanded question-and-answer pairs directly in search results. And their attorney and firm information appears more accurately in AI-generated recommendations. Schema is no longer optional for competitive legal markets — it is a foundational requirement.",
      },
      {
        type: "h2",
        heading: "The Six Essential Schema Types for Law Firm Websites",
        text: "The Six Essential Schema Types for Law Firm Websites",
      },
      {
        type: "ul",
        heading: "Required schema types for law firms",
        items: [
          "LegalService: describes your firm's legal services, practice areas, and service area — the most important schema type for law firms",
          "Attorney / Person: documents each attorney's name, credentials, bar membership, and specialties",
          "Organization: describes your firm as a business entity with name, address, contact information, and founding date",
          "LocalBusiness: handles geographic and contact information with rich local search integration",
          "FAQPage: marks up question-and-answer content for Google FAQ rich results and AI citation signals",
          "Article: marks up blog posts, guides, and resource pages with author, publication date, and topic metadata",
        ],
      },
      {
        type: "callout",
        text: "Start with LegalService, Organization, and FAQPage schema — these three types alone can significantly improve your AI visibility and Google rich results within 30 days of correct implementation.",
      },
      {
        type: "h2",
        heading: "Implementing LegalService Schema: Step by Step",
        text: "Implementing LegalService Schema: Step by Step",
      },
      {
        type: "p",
        text: "LegalService schema is the foundational structured data type for law firm websites. It tells search engines and AI systems that you are a legal services provider, specifies your practice areas, identifies your service area (geographic region you serve), and connects your firm's identity to its physical location. Every law firm website should implement LegalService schema on its homepage and practice area pages.",
      },
      {
        type: "p",
        text: "The most important fields in LegalService schema are: name (your exact canonical firm name), description (a clear 1-2 sentence description of your firm and practice areas), areaServed (the geographic area you serve), and hasOfferCatalog (a nested list of your specific legal services). Many firms implement only the basic fields and miss the opportunity to describe their full service offering in structured data.",
      },
      {
        type: "h2",
        heading: "FAQPage Schema: The Highest-Impact Implementation for AI Visibility",
        text: "FAQPage Schema: The Highest-Impact Implementation for AI Visibility",
      },
      {
        type: "p",
        text: "FAQPage schema wraps your question-and-answer content in a structure that AI systems can parse and use directly. When a user asks an AI tool a legal question, the AI's retrieval system looks for content that explicitly contains the question and a clear answer. FAQPage schema makes that connection explicit, increasing the probability that your content is selected for citation.",
      },
      {
        type: "p",
        text: "For Google, FAQPage schema can trigger rich results that display your Q&A pairs directly in the search results page, increasing your visibility without requiring a click. These expanded FAQ results can nearly double the search result real estate your page occupies, significantly increasing click-through rates for targeted queries.",
      },
    ],
    faqs: [
      {
        question: "How do I add schema markup to my law firm website?",
        answer:
          "Schema markup is added as JSON-LD code in your page's HTML — typically in the head section or as a script tag in the body. Many CMS platforms (WordPress with Yoast SEO, for example) offer schema plugins. Custom implementations can be hand-coded using Google's Structured Data Markup Helper as a starting point.",
      },
      {
        question: "How do I verify my schema markup is working correctly?",
        answer:
          "Use Google's Rich Results Test (search.google.com/test/rich-results) to test your schema implementation. It will show which schema types Google detects, flag errors, and preview how your page might appear in rich results. Google Search Console also shows schema errors and coverage data once your pages are indexed.",
      },
      {
        question: "Can incorrect schema markup hurt my law firm's SEO?",
        answer:
          "Yes — incorrect or misleading schema can trigger a manual action from Google, which can harm your rankings. Common mistakes include marking up content that is not visible on the page, misusing schema types, or including inaccurate information. Always validate implementations with Google's testing tools before publishing.",
      },
      {
        question: "How often should I update my schema markup?",
        answer:
          "Schema should be updated whenever the underlying information changes: attorney roster changes, practice area additions, address or phone changes, or new FAQ content. Static organization and firm schema can remain stable for months; dynamic content like attorneys and FAQs should be reviewed quarterly.",
      },
    ],
    related: ["legalservice-schema-guide", "faqpage-schema-for-lawyers"],
  },
  {
    slug: "legalservice-schema-guide",
    title: "LegalService Schema Guide for Law Firms: Implementation and Best Practices",
    description:
      "A detailed implementation guide for LegalService schema markup — the most important structured data type for law firm websites seeking AI visibility and Google rich results.",
    readTime: "11 min read",
    date: "2026-01-28",
    stats: [
      { value: "3x", label: "more accurate AI entity recognition with proper LegalService schema" },
      { value: "45%", label: "of law firms have errors in their existing LegalService schema" },
      { value: "14", label: "LegalService schema fields that materially impact AI visibility" },
    ],
    blocks: [
      {
        type: "h2",
        heading: "Understanding LegalService Schema in the Schema.org Hierarchy",
        text: "Understanding LegalService Schema in the Schema.org Hierarchy",
      },
      {
        type: "p",
        text: "LegalService is a schema.org type that inherits from LocalBusiness > ProfessionalService > LegalService. This hierarchy means that a correctly implemented LegalService schema automatically carries all the properties of its parent types — making it the most comprehensive way to describe a law firm to search engines and AI systems simultaneously.",
      },
      {
        type: "p",
        text: "The key advantage of using LegalService specifically (rather than the parent Organization or LocalBusiness types) is that it signals unambiguously to AI systems that your firm provides legal services. This specificity matters: AI systems handling legal queries actively look for content from LegalService entities when constructing responses about finding lawyers or legal help.",
      },
      {
        type: "h2",
        heading: "The 14 LegalService Schema Fields That Drive AI Visibility",
        text: "The 14 LegalService Schema Fields That Drive AI Visibility",
      },
      {
        type: "ul",
        heading: "High-impact LegalService schema fields",
        items: [
          "@type: always 'LegalService' — do not use generic 'Organization' or 'LocalBusiness'",
          "name: your canonical firm name — must match exactly across all platforms",
          "description: 1-3 sentence description including primary practice areas and geographic focus",
          "url: your canonical homepage URL",
          "telephone: primary phone number in E.164 format",
          "address: PostalAddress with streetAddress, addressLocality, addressRegion, postalCode, addressCountry",
          "geo: GeoCoordinates with latitude and longitude for precise location mapping",
          "areaServed: geographic area you serve — can be a city, state, or region",
          "priceRange: use '$$' or 'Free Consultation' to signal pricing context",
          "openingHours: business hours in schema format",
          "foundingDate: year the firm was established — signals longevity and credibility",
          "numberOfEmployees: approximate staff size",
          "hasOfferCatalog: nested OfferCatalog with each practice area as an Offer",
          "memberOf: bar associations and legal organizations your firm belongs to",
        ],
      },
      {
        type: "callout",
        text: "The hasOfferCatalog field is the most commonly omitted high-impact field in law firm LegalService schema. This nested structure explicitly lists each of your practice areas in a machine-readable format — dramatically improving the precision with which AI systems understand what legal services your firm actually provides.",
      },
      {
        type: "h2",
        heading: "Common LegalService Schema Errors and How to Fix Them",
        text: "Common LegalService Schema Errors and How to Fix Them",
      },
      {
        type: "p",
        text: "Analysis of law firm schema implementations consistently reveals the same categories of errors. Understanding these common mistakes helps you avoid them and fix existing implementations quickly.",
      },
      {
        type: "ul",
        heading: "Most common LegalService schema errors",
        items: [
          "Wrong @type: using 'Organization' instead of 'LegalService' — always use the most specific type",
          "Inconsistent name: firm name in schema does not match the canonical name used on the website and in directories",
          "Missing areaServed: omitting geographic service area leaves a critical AI signal blank",
          "Incomplete address: missing addressRegion or postalCode fields reduce location signal precision",
          "No hasOfferCatalog: not listing specific practice areas in machine-readable format",
          "Invalid telephone format: phone numbers must be in E.164 format (+12125551234) for full compatibility",
        ],
      },
    ],
    faqs: [
      {
        question: "Should I put LegalService schema on every page or just the homepage?",
        answer:
          "LegalService schema for the firm as a whole belongs on the homepage. Practice area-specific LegalService schemas (describing the specific service, not the whole firm) can be added to practice area pages. FAQPage schema should be added to any page with explicit Q&A content.",
      },
      {
        question: "Can I have multiple @type values in one schema block?",
        answer:
          "Yes — you can use '@type': ['LegalService', 'LocalBusiness'] to declare multiple types simultaneously. This is useful for ensuring compatibility with systems that may look for either type. However, LegalService alone is typically sufficient for law firms.",
      },
      {
        question: "How does LegalService schema interact with Google Business Profile?",
        answer:
          "They are complementary signals. Google Business Profile provides local search signals through Google's proprietary system. LegalService schema provides structured data signals to Google's web index and to third-party AI systems. Both should be complete and consistent — NAP information especially must match exactly.",
      },
    ],
    related: ["schema-markup-for-law-firms", "faqpage-schema-for-lawyers"],
  },
  {
    slug: "faqpage-schema-for-lawyers",
    title: "FAQPage Schema for Lawyers: How to Win Rich Results and AI Citations",
    description:
      "FAQPage schema is the highest-impact schema type for law firm AI visibility and Google rich results. Here is how to implement it correctly and write FAQ content that gets cited.",
    readTime: "10 min read",
    date: "2026-02-05",
    stats: [
      { value: "3x", label: "higher AI citation rate for pages with FAQPage schema vs pages without" },
      { value: "48%", label: "average increase in search result click-through rate from FAQ rich results" },
      { value: "5–8", label: "ideal number of FAQ pairs per practice area page" },
    ],
    blocks: [
      {
        type: "h2",
        heading: "Why FAQPage Schema Is the Most Valuable Schema Type for Law Firms",
        text: "Why FAQPage Schema Is the Most Valuable Schema Type for Law Firms",
      },
      {
        type: "p",
        text: "FAQPage schema is uniquely powerful for law firms because it creates a direct bridge between how your clients ask questions and how AI systems answer them. Legal queries — both in traditional search and AI-powered search — are overwhelmingly phrased as questions: 'How much does a personal injury lawyer cost?' 'What happens if I don't pay my traffic ticket?' 'Can I get divorced without a lawyer?' FAQPage schema explicitly marks up your answers to these questions in a format that AI systems can directly use.",
      },
      {
        type: "p",
        text: "Google uses FAQPage schema to generate FAQ rich results — expanded accordions in the search results page that show your question-and-answer pairs directly, without requiring a click. These rich results can more than double the vertical space your result occupies on the search page, significantly increasing visibility and click-through rates. For high-competition legal queries, FAQ rich results can be the difference between generating clicks and being invisible.",
      },
      {
        type: "h2",
        heading: "Writing FAQ Content That AI Systems Will Cite",
        text: "Writing FAQ Content That AI Systems Will Cite",
      },
      {
        type: "p",
        text: "The content quality of your FAQ pairs matters as much as the schema implementation. AI systems evaluate the quality, accuracy, and specificity of your answers when deciding whether to cite them. Generic answers that restate the question without providing real information — 'It depends on your specific situation; contact a lawyer' — are rarely cited. Specific, informative answers that genuinely address the question perform significantly better.",
      },
      {
        type: "ul",
        heading: "Characteristics of high-performing FAQ content for AI citation",
        items: [
          "Specific and direct: answer the exact question asked without preamble or evasion",
          "Appropriately detailed: 50 to 150 words per answer — enough to be substantive, short enough to be citable",
          "Jurisdiction-aware: where law varies by state, specify the jurisdiction your answer applies to",
          "Statistic-inclusive: include relevant data points where available",
          "Action-oriented: conclude with what the reader should do next",
        ],
      },
      {
        type: "callout",
        text: "The best FAQ content for AI citations is the same as the best FAQ content for human readers: honest, specific, useful, and appropriately qualified. Write for a potential client who needs real information, not for an algorithm.",
      },
      {
        type: "h2",
        heading: "Implementing FAQPage Schema: Technical Requirements",
        text: "Implementing FAQPage Schema: Technical Requirements",
      },
      {
        type: "p",
        text: "FAQPage schema requires that each FAQ pair be visible on the page — Google will penalize implementations where the schema content is not reflected in the actual page content. The schema should be implemented as JSON-LD in a script tag, with each Question entity specifying the question text in 'name' and the answer in 'acceptedAnswer.text'. The text values must match the visible page content.",
      },
      {
        type: "h2",
        heading: "How Many FAQs to Add Per Page",
        text: "How Many FAQs to Add Per Page",
      },
      {
        type: "p",
        text: "Research on FAQ rich result performance suggests that 5 to 8 FAQ pairs per page is the optimal range for most law firm practice area pages. Fewer than 5 reduces the diversity of questions you can rank for; more than 10 can dilute the focus of the page and make it harder for AI systems to identify the primary topic. Prioritize the most common genuine questions your clients ask, not the questions you wish they would ask.",
      },
    ],
    faqs: [
      {
        question: "Can I use FAQPage schema on every page of my law firm website?",
        answer:
          "FAQPage schema should only be added to pages that actually contain FAQ content with visible question-and-answer pairs. Adding it to pages without this content violates Google's guidelines. Good candidates: practice area pages, attorney profile pages, process overview pages, and resource guides.",
      },
      {
        question: "Does Google always show FAQ rich results when I have FAQPage schema?",
        answer:
          "No — Google decides whether to show rich results based on quality and relevance signals, not just schema presence. FAQ rich results are more likely when the FAQ content is high-quality and the page has good organic authority. Google may show rich results on some queries and not others for the same page.",
      },
      {
        question: "Should FAQ answers include legal disclaimers?",
        answer:
          "Include a brief general disclaimer where necessary for accuracy, but avoid burying every answer in boilerplate disclaimer text. Answers padded with excessive disclaimers are rarely cited by AI systems and perform poorly in rich results. Balance legal accuracy with content usability.",
      },
    ],
    related: ["schema-markup-for-law-firms", "legalservice-schema-guide"],
  },
];

export const ARTICLE_SLUGS = ARTICLES.map((a) => a.slug);
