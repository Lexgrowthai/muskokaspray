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
  name: "AI Chatbots for Law Firms",
  description: "Law firm chatbots qualify leads, answer common questions, and book consultations around the clock. Learn how to choose, configure, and get ROI from a legal chatbot.",
  slug: "ai-chatbots",
};

export const ARTICLES: SiloArticle[] = [
  {
    slug: "ai-chatbot-for-law-firms",
    title: "AI Chatbot for Law Firms: Turn Website Visitors into Consultations",
    description: "An AI chatbot on your law firm website can qualify leads 24/7 and book consultations while you sleep. Here is how to make it work.",
    readTime: "11 min read",
    date: "2026-06-18",
    stats: [
      { value: "85%", label: "of clients prefer to message before calling" },
      { value: "4x", label: "more leads captured with chatbot vs. form alone" },
      { value: "3 min", label: "average response time expectation after hours" },
    ],
    blocks: [
      { type: "h2", heading: "Why Legal Chatbots Have Become Essential", text: "Why Legal Chatbots Have Become Essential" },
      { type: "p", text: "The modern legal prospect does not want to fill out a form and wait two days for a callback. They want answers now. Research from numerous legal marketing studies shows that the majority of potential clients prefer to message or chat before speaking on the phone \u2014 it feels lower-pressure, allows them to organize their thoughts, and fits into their busy schedules." },
      { type: "p", text: "A well-configured AI chatbot captures this preference by offering an immediate, helpful conversation at any hour. The chatbot asks the right qualifying questions, collects contact information, addresses common concerns, and \u2014 critically \u2014 books a consultation or schedules a callback. The attorney wakes up with a full consultation calendar rather than a pile of voicemails." },
      { type: "callout", text: "The window between when a prospect first lands on your website and when they decide to contact you is often under three minutes. A chatbot that engages them within that window converts at a dramatically higher rate than a form they fill out and submit into silence." },
      { type: "h2", heading: "What a Legal AI Chatbot Should Do", text: "What a Legal AI Chatbot Should Do" },
      { type: "ul", heading: "Core capabilities of an effective legal chatbot", items: ["Greet visitors with a specific, relevant opening based on the page they are on.", "Ask qualifying questions tailored to each practice area.", "Collect name, email, phone number, and case type.", "Answer common questions about the firm's process, fees, and areas of practice.", "Book a consultation or callback directly into the attorney's calendar.", "Send immediate follow-up messages with next steps and firm contact information.", "Escalate to a live person when the visitor requests human assistance."] },
    ],
    faqs: [
      { question: "Will a chatbot make my law firm seem impersonal?", answer: "A poorly configured chatbot will. A well-configured one is indistinguishable from a human assistant in most cases, and prospective clients often prefer the low-pressure format. The key is to make the conversation helpful and efficient \u2014 not robotic." },
      { question: "How much do legal chatbots cost?", answer: "Legal chatbot platforms range from $100 to $500 per month for smaller firms, depending on features and conversation volume. Many offer free trials. The ROI calculation is simple: if the chatbot generates two additional retained cases per month and each case is worth $3,000, it pays for itself many times over." },
      { question: "Can a chatbot replace my intake team?", answer: "A chatbot handles initial qualification and information gathering exceptionally well. It should hand off to a human for complex consultations, fee agreements, and emotionally sensitive situations. Think of it as a first-contact tool that prepares a warm lead for your team, not a replacement for human judgment." },
    ],
    related: ["law-firm-chatbot-best-practices", "chatbot-vs-live-chat-for-law-firms"],
  },
  {
    slug: "law-firm-chatbot-best-practices",
    title: "Law Firm Chatbot Best Practices: What Separates Good From Great",
    description: "Most law firm chatbots underperform because of avoidable configuration mistakes. These best practices separate the chatbots that convert from the ones that frustrate.",
    readTime: "10 min read",
    date: "2026-06-18",
    stats: [
      { value: "Page-specific", label: "triggers increase chatbot engagement by 3.4x" },
      { value: "3 questions", label: "maximum before asking for contact info" },
      { value: "40%", label: "abandonment rate when chatbot asks too many questions" },
    ],
    blocks: [
      { type: "h2", heading: "The Most Common Legal Chatbot Mistakes", text: "The Most Common Legal Chatbot Mistakes" },
      { type: "ul", heading: "Mistakes that kill legal chatbot conversion", items: ["Generic opening message on every page: 'Hi! How can I help you today?' tells the visitor nothing.", "Asking for email before establishing any value \u2014 visitors leave before completing the form.", "Too many questions before offering value or booking a call.", "No personality: robotic, cold language in a context where people are stressed and scared.", "No clear CTA: the chatbot answers questions but never asks for the booking.", "No handoff protocol: the chatbot cannot escalate to a human when needed."] },
      { type: "h2", heading: "The Optimal Legal Chatbot Flow", text: "The Optimal Legal Chatbot Flow" },
      { type: "p", text: "The best legal chatbot flows follow a predictable pattern: specific opening, brief qualification, offer of value, collection of contact info, booking or callback scheduling. On a personal injury page, the opening might be: 'Were you or someone you know recently injured in an accident? I can connect you with one of our attorneys for a free consultation today.' Specific. Relevant. Offering something concrete." },
      { type: "callout", text: "Put the call to action earlier than feels comfortable. Most chatbot designers wait too long to ask for the booking. Prospects are often ready to schedule within the first 2\u20133 exchanges if you make it easy." },
      { type: "p", text: "After the initial qualifier, ask one more clarifying question maximum before offering the booking. 'Great \u2014 roughly when did the accident occur?' Then: 'I can schedule a free consultation with our team right now. What time works best for you this week?' Two questions, then a booking offer." },
    ],
    faqs: [
      { question: "Should my chatbot use a name and avatar?", answer: "Yes. A named, personalized chatbot (e.g., 'Hi, I'm Lex, the Smith Law Group assistant') performs better than anonymous chat widgets. An avatar \u2014 a professional headshot or friendly icon \u2014 further increases engagement. Avoid overly cartoon-like avatars that undermine professionalism." },
      { question: "What should the chatbot say when it can't answer a question?", answer: "Always offer an alternative path: 'That's a great question \u2014 let me connect you with one of our attorneys who can give you an accurate answer. Can I schedule a quick call?' Never let the conversation dead-end without an action for the visitor to take." },
      { question: "How often should I review and update my chatbot scripts?", answer: "Monthly, at minimum. Review conversation transcripts to identify questions the chatbot is not handling well, common topics callers raise that your script doesn't cover, and points where visitors drop off. Chatbot optimization is ongoing, not set-and-forget." },
    ],
    related: ["ai-chatbot-for-law-firms", "chatbot-vs-live-chat-for-law-firms"],
  },
  {
    slug: "chatbot-vs-live-chat-for-law-firms",
    title: "Chatbot vs Live Chat for Law Firms: Which Converts More Clients?",
    description: "AI chatbots and human live chat both capture leads \u2014 but they work differently. Here is how to choose the right approach for your law firm's size and goals.",
    readTime: "9 min read",
    date: "2026-06-18",
    stats: [
      { value: "60%", label: "of legal inquiries arrive outside business hours" },
      { value: "Live chat", label: "converts 2.1x more during business hours" },
      { value: "AI chatbot", label: "captures 4x more after-hours leads than forms alone" },
    ],
    blocks: [
      { type: "h2", heading: "Understanding the Trade-Offs", text: "Understanding the Trade-Offs" },
      { type: "p", text: "Live chat \u2014 a real human responding to website messages in real time \u2014 outperforms AI chatbots when complex empathy and judgment are required. A caller describing a traumatic accident, a custody battle, or a criminal charge benefits from immediate human acknowledgment. However, live chat requires staffing during all active hours, creates response time problems when operators are busy, and is unavailable nights and weekends for most small firms." },
      { type: "p", text: "AI chatbots solve the availability problem but sacrifice some empathetic depth. The right answer for most firms is not a binary choice \u2014 it is a thoughtful combination of both." },
      { type: "ul", heading: "When to use each option", items: ["AI chatbot: after-hours, overnight, weekends, and high-traffic overflow periods.", "Live chat: during core business hours when sensitive matters need human empathy.", "AI for qualification, human for closing: AI gathers info, then transfers to a live person.", "AI-only for high-volume firms: where 24/7 staff coverage is not cost-effective."] },
      { type: "callout", text: "The fastest-growing law firms use AI chatbots to ensure zero missed connections and live chat to maximize conversion on high-value interactions. Start with AI to capture every lead, then add live chat once you understand which interactions most benefit from human touch." },
    ],
    faqs: [
      { question: "Is live chat worth the staffing cost for a small law firm?", answer: "For very small practices, a third-party live chat service (like Chat Agents or Ngage Legal) provides human operators for roughly $300\u2013600/month \u2014 often more cost-effective than in-house staffing. Combined with an AI chatbot for after-hours, this hybrid approach works well for firms of any size." },
      { question: "Can I transition from live chat to AI chatbot gradually?", answer: "Yes. A common path: start with a live chat service, then use AI to handle overflow and after-hours. As you refine your chatbot scripts using real conversation data, gradually shift more interactions to AI while keeping humans for complex cases." },
      { question: "What chat platform should law firms use?", answer: "Popular platforms built for legal include LawDroid, Gideon, Intake.ai, and Tawk.to for live chat. For AI-specific legal chatbots, Smith.ai, LawDroid Copilot, and several newer AI-native platforms offer strong legal intake capabilities." },
    ],
    related: ["ai-chatbot-for-law-firms", "law-firm-chatbot-best-practices"],
  },
];

export const ARTICLE_SLUGS = ARTICLES.map((a) => a.slug);
