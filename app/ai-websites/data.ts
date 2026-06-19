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
  name: "AI Websites for Law Firms",
  description: "Modern law firm websites built with AI-powered design, conversion optimization, and technical foundations that turn visitors into consultations.",
  slug: "ai-websites",
};

export const ARTICLES: SiloArticle[] = [
  {
    slug: "ai-website-design-for-law-firms",
    title: "AI Website Design for Law Firms: What the Best Sites Do Differently",
    description: "The law firm websites that convert at the highest rates share specific design principles. Here is what separates a great legal website from an average one.",
    readTime: "12 min read",
    date: "2026-06-18",
    stats: [
      { value: "3.2s", label: "load time threshold before 40% of visitors leave" },
      { value: "67%", label: "of legal searches happen on mobile devices" },
      { value: "4.2x", label: "more leads from sites with live chat or intake forms" },
    ],
    blocks: [
      { type: "h2", heading: "Why Most Law Firm Websites Fail at Conversion", text: "Why Most Law Firm Websites Fail at Conversion" },
      { type: "p", text: "The average law firm website was designed to look professional, not to convert. It has a large hero image, a paragraph about the firm's values, a team page, and a contact form. That template may have worked in 2010, when most visitors came from directories or word of mouth and already intended to call. It does not work in an era where potential clients arrive from AI search results and organic Google traffic \u2014 users who are still evaluating whether to reach out at all." },
      { type: "p", text: "High-converting law firm websites treat every page as a landing page. They answer the visitor's question immediately, establish credibility within seconds, and make the next step \u2014 a call, a form, a chat \u2014 frictionless. The design choices that accomplish this are specific, learnable, and repeatable." },
      { type: "callout", text: "A 1-second improvement in page load time can improve conversion rates by 7%. For a firm getting 1,000 monthly visitors, that is dozens of additional consultations \u2014 just from a faster website." },
      { type: "h2", heading: "Core Design Principles for High-Converting Legal Websites", text: "Core Design Principles for High-Converting Legal Websites" },
      { type: "ul", heading: "What separates converting sites from non-converting ones", items: ["Above-the-fold clarity: the visitor knows within 3 seconds what the firm does and where it practices.", "Social proof near the top: reviews, case results, and bar admissions visible immediately.", "One primary CTA per page: a single clear action prevents decision paralysis.", "Mobile-first layout: navigation, CTAs, and forms designed for thumbs, not cursors.", "Fast load times: compressed images, minimal JavaScript, and server-side rendering.", "Trust signals throughout: headshots, bar logos, awards, and publication features."] },
      { type: "h2", heading: "AI Features That Modern Law Firm Websites Include", text: "AI Features That Modern Law Firm Websites Include" },
      { type: "p", text: "AI-powered law firm websites go beyond good design. They incorporate intake chatbots that qualify leads before a human ever gets involved, smart call tracking that routes calls based on practice area and time of day, and automated follow-up sequences that re-engage visitors who left without contacting the firm. These features work around the clock, ensuring that no lead falls through the cracks between business hours." },
    ],
    faqs: [
      { question: "How much should a law firm spend on a new website?", answer: "Quality law firm websites typically range from $8,000 to $30,000 for custom builds, depending on complexity, content needs, and integrations. The ROI calculation is simple: if a new client is worth $5,000 and the site converts 10 additional clients per year, a $20,000 investment pays back in 4 months." },
      { question: "How often should a law firm redesign its website?", answer: "Major redesigns every 3\u20135 years, with continuous minor improvements throughout. Focus annual attention on page speed, content freshness, and conversion rate optimization rather than aesthetic overhauls." },
      { question: "What is the most important page on a law firm website?", answer: "Typically the practice area page most aligned with your highest-value cases. That page should be the most detailed, best-optimized, and most clearly conversion-focused page on the site." },
    ],
    related: ["law-firm-website-conversion-optimization", "mobile-first-law-firm-websites"],
  },
  {
    slug: "law-firm-website-conversion-optimization",
    title: "Law Firm Website Conversion Optimization: Turning Visitors into Clients",
    description: "Most law firm websites attract visitors but fail to convert them. These proven optimization strategies close that gap.",
    readTime: "10 min read",
    date: "2026-06-18",
    stats: [
      { value: "2.4%", label: "average legal website conversion rate" },
      { value: "8\u201312%", label: "conversion rate for optimized legal sites" },
      { value: "68%", label: "of visitors who bounce never return" },
    ],
    blocks: [
      { type: "h2", heading: "Understanding Why Visitors Don't Convert", text: "Understanding Why Visitors Don't Convert" },
      { type: "p", text: "Before optimizing, diagnose. Most law firm websites lose visitors at three specific points: the moment they arrive and don't immediately understand the firm's value proposition; the moment they try to find practice area information and encounter vague, generic descriptions; and the moment they attempt to contact the firm and face a form with too many fields or a phone number that doesn't answer." },
      { type: "h2", heading: "The CRO Stack for Law Firms", text: "The CRO Stack for Law Firms" },
      { type: "ul", heading: "Conversion rate optimization tools that work for legal websites", items: ["Heatmapping (Hotjar, Microsoft Clarity) \u2014 see exactly where visitors click and where they drop off.", "Session recordings \u2014 watch real visitor sessions to identify friction points.", "A/B testing on headlines and CTA button text \u2014 small copy changes often yield 20\u201340% conversion lifts.", "Live chat with real operators or AI bots during business hours.", "Call tracking (CallRail) \u2014 understand which pages and traffic sources drive the most calls.", "Form analytics \u2014 identify which fields cause visitors to abandon intake forms."] },
      { type: "callout", text: "The fastest conversion wins usually come from the simplest changes: a headline that addresses the visitor's specific fear, a CTA button that says 'Get a Free Consultation' instead of 'Contact Us,' and a phone number in the top-right corner of every page." },
      { type: "h2", heading: "The Intake Form: Where Most Firms Lose Leads", text: "The Intake Form: Where Most Firms Lose Leads" },
      { type: "p", text: "The standard law firm intake form asks for name, email, phone, case type, case description, and how they heard about you. That is five to six fields, and every additional field reduces completion rates. For initial intake, ask only for the minimum: name, phone number, and practice area. Qualify further after the first contact, not before." },
    ],
    faqs: [
      { question: "What is a good conversion rate for a law firm website?", answer: "The industry average is around 2\u20133%. Well-optimized law firm sites achieve 8\u201312%. If you're below 5%, there is significant room to improve through copy, design, and form optimization." },
      { question: "Should law firms use pop-up chat widgets?", answer: "Used thoughtfully, yes. Triggered chat that appears after a visitor has been on a practice area page for 30+ seconds performs well without being intrusive. Immediate pop-ups on first page load tend to increase bounce rates." },
      { question: "How important are Google reviews to conversion?", answer: "Very important. Displaying your Google review rating prominently on the homepage and practice area pages builds immediate trust. Firms with 4.8+ star averages displayed near the CTA see measurably higher conversion rates." },
    ],
    related: ["ai-website-design-for-law-firms", "mobile-first-law-firm-websites"],
  },
  {
    slug: "mobile-first-law-firm-websites",
    title: "Mobile-First Law Firm Websites: Why It Matters and How to Get It Right",
    description: "67% of legal searches happen on mobile. Here is how to build a law firm website that converts mobile visitors into consultations.",
    readTime: "9 min read",
    date: "2026-06-18",
    stats: [
      { value: "67%", label: "of legal searches are on mobile" },
      { value: "53%", label: "of mobile users leave if the site takes over 3 seconds" },
      { value: "2x", label: "more calls from click-to-call on mobile-first sites" },
    ],
    blocks: [
      { type: "h2", heading: "The Mobile Reality for Legal Marketing", text: "The Mobile Reality for Legal Marketing" },
      { type: "p", text: "Most people experiencing a legal crisis reach for their phone first. Whether it is a late-night DUI arrest, a workplace injury, or a landlord dispute, the initial search for legal help happens on mobile devices. If your law firm's website is not optimized for mobile \u2014 and most are not \u2014 you are losing leads to competitors who prioritized it." },
      { type: "p", text: "Mobile-first is not just about making your site look good on small screens. It means designing the entire user experience around the behaviors and needs of a mobile user: one-thumb navigation, tap-to-call CTAs, fast load times on cellular networks, and forms designed to be completed on a phone keyboard." },
      { type: "ul", heading: "Mobile design requirements for law firm websites", items: ["Click-to-call button pinned to the bottom of the screen at all times.", "Navigation simplified to three or four key destinations.", "Text size minimum 16px to avoid pinch-zooming.", "Forms with no more than three to four fields on the first screen.", "Images compressed to WebP format for fast cellular loading.", "Core Web Vitals scores of 90+ on Google PageSpeed Insights."] },
      { type: "callout", text: "Google uses mobile-first indexing. The mobile version of your site is what Google evaluates for ranking purposes. A site that performs poorly on mobile will rank worse \u2014 which means fewer visitors, not just worse conversion." },
    ],
    faqs: [
      { question: "What is the minimum acceptable load time for a mobile legal site?", answer: "Aim for under 2.5 seconds for the Largest Contentful Paint (LCP). Google considers 2.5 seconds the threshold for a 'good' LCP. Above 4 seconds, you are likely to see significant bounce rate increases." },
      { question: "Should a law firm have a separate mobile website?", answer: "No. Separate mobile sites (m.domain.com) are an outdated approach. Use a responsive design that adapts to any screen size from a single URL. This is both technically simpler and better for SEO." },
      { question: "How do I test my law firm website's mobile performance?", answer: "Use Google PageSpeed Insights (free), Google Search Console's Core Web Vitals report, and personally test your site on a mid-range Android device on a 4G cellular connection \u2014 not your office Wi-Fi." },
    ],
    related: ["ai-website-design-for-law-firms", "law-firm-website-conversion-optimization"],
  },
];

export const ARTICLE_SLUGS = ARTICLES.map((a) => a.slug);
