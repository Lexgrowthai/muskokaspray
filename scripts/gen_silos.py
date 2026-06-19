#!/usr/bin/env python3
"""Generate all 9 SEO silo data.ts, page.tsx, and [slug]/page.tsx files."""
import os

ROOT = "/home/user/lexscale/app"

# ---------------------------------------------------------------------------
# Silo definitions
# ---------------------------------------------------------------------------
SILOS = [
  {
    "slug": "gemini",
    "name": "Google Gemini for Law Firms",
    "description": "Google is weaving Gemini into Search, Maps, Android, and Workspace. Understand how to appear inside Google's AI-generated answers before your competitors do.",
    "articles": [
      {
        "slug": "google-gemini-for-law-firms",
        "title": "Google Gemini for Law Firms: The Complete Visibility Guide",
        "description": "Google Gemini is now embedded in Search, Maps, Gmail, and Chrome. Here is how law firms earn visibility inside Google's AI ecosystem.",
        "readTime": "13 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "8.5B", "label": "Google searches per day"},
          {"value": "40%", "label": "of searches now show AI Overviews"},
          {"value": "3", "label": "sources cited per AI Overview on average"},
        ],
        "blocks": [
          {"type": "h2", "heading": "What Google Gemini Means for Law Firms", "text": "What Google Gemini Means for Law Firms"},
          {"type": "p", "text": "For two decades, winning in Google meant optimizing page titles, building backlinks, and earning positions in the classic blue-link results. That playbook still matters — but it is no longer the whole game. Google is integrating Gemini, its most advanced AI model, across every surface it controls. The firms that understand this transition early will hold a durable advantage."},
          {"type": "p", "text": "Gemini is not a separate product people need to discover. It is woven directly into the search interface billions of people use every day. When a potential client types 'family lawyer near me' or 'what to do after a car accident in Toronto,' they increasingly see an AI-generated summary at the top of the page — before any blue links appear. That summary cites a small number of sources. Being one of those sources is the new front page."},
          {"type": "callout", "text": "Google processes 8.5 billion searches every day. As Gemini becomes the primary interface for those searches, firms cited in AI Overviews receive visibility that no paid ad can replicate — and it compounds over time."},
          {"type": "h2", "heading": "Where Gemini Lives Inside Google's Ecosystem", "text": "Where Gemini Lives Inside Google's Ecosystem"},
          {"type": "ul", "heading": "Gemini appears across all of Google's platforms", "items": [
            "Google Search — AI Overviews above the blue links on billions of queries.",
            "Google Maps — AI-powered answers for 'lawyers near me' and practice area searches.",
            "Google Assistant on Android — voice queries answered with Gemini intelligence.",
            "Gmail and Workspace — AI writing assistance drawing on Gemini's knowledge.",
            "Chrome — in-browser AI help for users researching legal questions.",
          ]},
          {"type": "h2", "heading": "How to Earn Citations in Google AI Overviews", "text": "How to Earn Citations in Google AI Overviews"},
          {"type": "p", "text": "AI Overviews draw on Google's existing index, which means traditional SEO signals still matter. But they add a new dimension: Google must be able to quickly understand what your firm does, where you practice, and whether your content directly answers the question being asked. Structured data, entity signals, and authoritative content work together to earn that trust."},
          {"type": "ul", "heading": "Priority actions for Gemini visibility", "items": [
            "Build deep topical authority across your specific practice areas.",
            "Implement LegalService, Attorney, and FAQPage schema on every relevant page.",
            "Strengthen your Google Business Profile with accurate NAP, reviews, and photos.",
            "Answer conversational legal questions directly in your content — not just keywords.",
            "Earn citations in legal directories, bar association sites, and trusted publications.",
          ]},
        ],
        "faqs": [
          {"question": "Is Google Gemini the same as AI Overviews?", "answer": "Gemini is Google's underlying AI model. AI Overviews are one of the most visible outputs — the AI-generated summaries that appear at the top of search results. Gemini powers many other Google features as well."},
          {"question": "Does traditional SEO still matter for Gemini visibility?", "answer": "Yes. Gemini draws on Google's existing index, so page authority, backlinks, and on-page optimization all feed into which sources get cited. AI visibility and traditional SEO reinforce each other."},
          {"question": "How can a small law firm compete for AI Overview citations?", "answer": "Focus on depth and specificity. A detailed, accurate answer to 'what happens during a divorce in Ontario' can earn a citation even for a small firm, because the AI rewards relevance over domain authority alone."},
        ],
        "related": ["gemini-ai-overviews-explained", "how-to-rank-in-google-ai-overviews"],
      },
      {
        "slug": "gemini-ai-overviews-explained",
        "title": "Google AI Overviews Explained: What Law Firms Need to Know",
        "description": "AI Overviews now appear on billions of searches. Here is exactly how they work, what they cite, and how law firms can influence them.",
        "readTime": "10 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "1B+", "label": "monthly AI Overview impressions"},
          {"value": "56%", "label": "of users read AI Overviews before clicking"},
          {"value": "3–5", "label": "cited sources per AI Overview"},
        ],
        "blocks": [
          {"type": "h2", "heading": "What Is a Google AI Overview?", "text": "What Is a Google AI Overview?"},
          {"type": "p", "text": "A Google AI Overview is an AI-generated summary that appears at the very top of a search results page — above all organic links, above ads, and above featured snippets. It synthesizes information from multiple sources to provide a direct answer to a user's question. Each overview cites a handful of sources, displayed as links below the summary text."},
          {"type": "p", "text": "For law firms, AI Overviews represent an entirely new category of visibility. When a potential client searches for 'do I need a lawyer for probate in Texas' or 'how to file for divorce in Ontario,' the AI Overview may be the only result they read. If your firm is cited as a source, you receive exposure before the user ever reaches a blue link."},
          {"type": "callout", "text": "Being cited in an AI Overview is not about having the highest-ranking page. It is about having content that Google's AI judges as the most direct, accurate, and authoritative answer to a specific question."},
          {"type": "h2", "heading": "How Google Chooses What to Cite", "text": "How Google Chooses What to Cite"},
          {"type": "ul", "heading": "What influences AI Overview citations", "items": [
            "Direct question-and-answer structure that maps to the user's intent.",
            "E-E-A-T signals: Experience, Expertise, Authoritativeness, and Trustworthiness.",
            "Schema markup that tells Google exactly what the content covers.",
            "Page authority from backlinks and domain trust.",
            "Freshness — recently updated content is often preferred for evolving legal topics.",
          ]},
          {"type": "h2", "heading": "Practical Steps to Appear in AI Overviews", "text": "Practical Steps to Appear in AI Overviews"},
          {"type": "p", "text": "Start by identifying the specific questions your prospective clients ask Google before hiring a lawyer. Tools like Google Search Console, People Also Ask, and Answer the Public reveal these queries. For each high-value question, create a dedicated page or section that answers it directly, accurately, and completely — then mark it up with FAQPage or Q&A schema."},
        ],
        "faqs": [
          {"question": "Can I opt out of having my content used in AI Overviews?", "answer": "Yes. You can use the nosnippet meta tag or Google Search Console to limit how Google uses your content. However, opting out also removes you from citation consideration."},
          {"question": "Do AI Overviews drive traffic to cited websites?", "answer": "Citations include clickable links. While some users read only the summary, many click through — especially for complex legal questions where they want to verify information or contact the firm directly."},
          {"question": "How long does it take to start appearing in AI Overviews?", "answer": "There is no set timeline. Some firms see citations within weeks of improving their content and schema; others take several months. Consistency and specificity tend to accelerate results."},
        ],
        "related": ["google-gemini-for-law-firms", "how-to-rank-in-google-ai-overviews"],
      },
      {
        "slug": "how-to-rank-in-google-ai-overviews",
        "title": "How Law Firms Rank in Google AI Overviews",
        "description": "A practical, step-by-step guide for law firms that want to earn citations in Google's AI-generated search summaries.",
        "readTime": "11 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "68%", "label": "of AI Overview sources rank in the top 10 organically"},
          {"value": "FAQPage", "label": "schema increases citation rate by 2.4x"},
          {"value": "90 days", "label": "average timeline to first AI Overview citation"},
        ],
        "blocks": [
          {"type": "h2", "heading": "The Foundation: Topical Authority", "text": "The Foundation: Topical Authority"},
          {"type": "p", "text": "Google's AI does not cherry-pick individual pages from random websites. It draws from sources it has determined to be authoritative on a topic. For a family law firm in Vancouver, that means publishing comprehensive, accurate content about family law in British Columbia — not a single page, but a network of pages that collectively demonstrate deep expertise."},
          {"type": "p", "text": "Topical authority is built over time through consistent, specific, expert-level content. A firm that has 40 pages answering real family law questions signals depth. A firm with one generic 'family law services' page does not. The former earns AI citations. The latter does not."},
          {"type": "h2", "heading": "Technical Requirements: Schema and Structure", "text": "Technical Requirements: Schema and Structure"},
          {"type": "ul", "heading": "Must-have technical elements for AI Overview eligibility", "items": [
            "LegalService schema with accurate practice areas, jurisdiction, and contact data.",
            "FAQPage schema wrapping every Q&A section on your site.",
            "BreadcrumbList schema on all pages for clear site hierarchy signals.",
            "Attorney or Person schema for every lawyer on your team.",
            "LocalBusiness schema reinforcing your geographic service area.",
          ]},
          {"type": "callout", "text": "Schema markup does not guarantee citation — but its absence almost guarantees exclusion. Google's AI needs machine-readable signals to quickly understand what your content covers and whether it is trustworthy."},
          {"type": "h2", "heading": "Content Strategy: Answer the Question Behind the Question", "text": "Content Strategy: Answer the Question Behind the Question"},
          {"type": "p", "text": "When someone searches 'do I need a lawyer for a DUI in California,' the literal question is about necessity. But the question behind it is: what happens if I get a DUI, what are the consequences, and how do I protect myself? The firms that answer both questions — and answer them thoroughly — are the ones that appear in AI Overviews. Write for the person behind the query, not just the keyword."},
        ],
        "faqs": [
          {"question": "Does page 1 ranking guarantee an AI Overview citation?", "answer": "No, but it helps significantly. About 68% of AI Overview citations come from top-10 organically ranking pages. Building both organic rank and content quality gives you the best odds."},
          {"question": "Should I create separate pages for each legal question?", "answer": "For high-volume questions, yes. Dedicated pages signal topical relevance more strongly than a single page that briefly mentions many topics. Use your practice area pages as hubs and create supporting content for specific questions."},
          {"question": "What content format does Google prefer for AI Overviews?", "answer": "Clear, direct answers in plain language. Structured formats like numbered steps, bullet lists, and Q&A sections perform well. Avoid jargon-heavy writing that obscures the core answer."},
        ],
        "related": ["google-gemini-for-law-firms", "gemini-ai-overviews-explained"],
      },
    ],
  },
  {
    "slug": "perplexity",
    "name": "Perplexity AI for Law Firms",
    "description": "Perplexity is the answer engine for research-minded users — and it shows its sources on every answer. Learn how to become one of the cited sources.",
    "articles": [
      {
        "slug": "perplexity-ai-for-law-firms",
        "title": "Perplexity AI for Law Firms: Why It Matters and How to Get Cited",
        "description": "Perplexity answers millions of legal questions every month and cites its sources visibly. Here is how law firms earn those citations and the authority that follows.",
        "readTime": "11 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "100M+", "label": "monthly Perplexity users"},
          {"value": "5–8", "label": "sources shown per Perplexity answer"},
          {"value": "3x", "label": "higher trust when a source is visibly cited"},
        ],
        "blocks": [
          {"type": "h2", "heading": "What Makes Perplexity Different from ChatGPT and Google", "text": "What Makes Perplexity Different from ChatGPT and Google"},
          {"type": "p", "text": "Perplexity is often called an 'answer engine' rather than a search engine or chatbot. The distinction matters for law firms. Unlike Google, which returns a list of links for users to evaluate, Perplexity synthesizes an answer and cites the specific sources it drew from — displayed prominently alongside the answer. Unlike ChatGPT, which primarily uses training data, Perplexity retrieves live web content and attributes it directly."},
          {"type": "p", "text": "For a law firm, this means Perplexity citations are visible endorsements. When a prospective client asks 'what should I do after a car accident in Georgia' and Perplexity's answer prominently cites your firm's content, that exposure carries more trust weight than a blue link buried in a search results page."},
          {"type": "callout", "text": "Perplexity's users skew toward research-minded professionals and educated consumers — exactly the profile of someone who is seriously considering hiring a lawyer rather than casually browsing."},
          {"type": "h2", "heading": "How Perplexity Selects Its Sources", "text": "How Perplexity Selects Its Sources"},
          {"type": "ul", "heading": "Source selection factors for Perplexity", "items": [
            "Content freshness — Perplexity crawls and indexes recent content heavily.",
            "Direct relevance — pages that answer the exact question asked are strongly preferred.",
            "Domain authority — established legal websites with backlinks earn preference.",
            "Content clarity — well-structured, scannable content is easier for AI to parse and cite.",
            "Lack of fluff — concise, information-dense pages outperform padded content.",
          ]},
          {"type": "h2", "heading": "Strategies to Earn Perplexity Citations", "text": "Strategies to Earn Perplexity Citations"},
          {"type": "p", "text": "The most effective approach combines fresh, specific content with strong technical signals. Publish regular updates to your practice area pages — even minor updates signal freshness. Create dedicated FAQ pages for the most common questions in your practice area. Use structured data so Perplexity's crawlers can efficiently parse your content. Earn backlinks from legal directories, local bar associations, and reputable media."},
        ],
        "faqs": [
          {"question": "Is Perplexity used enough to matter for law firm marketing?", "answer": "Yes. With over 100 million monthly users and a fast-growing base of educated, research-oriented users, Perplexity represents a meaningful and underserved opportunity for law firms."},
          {"question": "Does Perplexity use the same signals as Google?", "answer": "Partially. Perplexity uses live web crawling and values many of the same signals as Google — domain authority, backlinks, content quality. But it places heavier weight on freshness and direct relevance than traditional SEO does."},
          {"question": "Can a small firm with a new website earn Perplexity citations?", "answer": "Yes, especially for hyper-specific local queries. A detailed, accurate page answering 'what are the grounds for divorce in Manitoba' from a local family law firm can outperform a large national site that only covers the topic superficially."},
        ],
        "related": ["how-to-get-cited-on-perplexity", "perplexity-vs-chatgpt-for-legal-research"],
      },
      {
        "slug": "how-to-get-cited-on-perplexity",
        "title": "How to Get Your Law Firm Cited on Perplexity AI",
        "description": "A practical playbook for earning visible citations on Perplexity — the answer engine that shows its sources to millions of research-minded users.",
        "readTime": "10 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "Fresh", "label": "content crawled within 48 hours gets priority"},
          {"value": "FAQPage", "label": "schema pages cited 2.1x more often"},
          {"value": "6–12", "label": "months to build consistent citation presence"},
        ],
        "blocks": [
          {"type": "h2", "heading": "The Content Blueprint for Perplexity Citations", "text": "The Content Blueprint for Perplexity Citations"},
          {"type": "p", "text": "Perplexity rewards content that is specific, accurate, and immediately useful. Generic law firm content — 'We are a dedicated team of experienced attorneys committed to your success' — is invisible to answer engines. What earns citations is content that directly answers the question a prospective client is asking right now."},
          {"type": "ul", "heading": "Content types that earn Perplexity citations", "items": [
            "Specific legal Q&A pages: 'What happens at a first DUI hearing in Texas?'",
            "Process explanations: step-by-step guides through legal procedures in your jurisdiction.",
            "Statute and case law summaries written in plain language for consumers.",
            "Comparison pages: 'Mediation vs. litigation for divorce — which is right for you?'",
            "Updated resource pages that reflect recent law changes.",
          ]},
          {"type": "h2", "heading": "Technical Optimizations for Perplexity", "text": "Technical Optimizations for Perplexity"},
          {"type": "p", "text": "Ensure your site is crawlable and fast. Perplexity prioritizes pages that load quickly, are mobile-friendly, and have no crawl blocks in robots.txt. Submit a sitemap to Google Search Console — Perplexity uses Google's index as one of its sources. Add FAQPage and Q&A schema to any page with question-and-answer content."},
          {"type": "callout", "text": "Update your key content pages regularly. Even minor updates signal freshness to Perplexity's crawler, improving your odds of being pulled into real-time answer generation."},
        ],
        "faqs": [
          {"question": "Do I need to submit my site directly to Perplexity?", "answer": "There is no direct submission mechanism. Perplexity discovers content through its own crawls and through Google's index. Ensuring your site is indexed on Google is the most reliable path to Perplexity discovery."},
          {"question": "How often should I update my practice area pages?", "answer": "At minimum, review and update key pages quarterly. For areas where law changes frequently — tax law, immigration, employment law — monthly updates are worth the investment."},
          {"question": "Does having lots of pages help?", "answer": "Quality over quantity. Ten detailed, specific, well-structured pages will outperform 100 thin pages. Focus on answering the most important questions in your practice area comprehensively."},
        ],
        "related": ["perplexity-ai-for-law-firms", "perplexity-vs-chatgpt-for-legal-research"],
      },
      {
        "slug": "perplexity-vs-chatgpt-for-legal-research",
        "title": "Perplexity vs ChatGPT for Legal Research: Key Differences for Law Firms",
        "description": "How do Perplexity and ChatGPT differ when clients use them to research legal questions? What those differences mean for your firm's AI visibility strategy.",
        "readTime": "9 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "Live", "label": "Perplexity uses real-time web data"},
          {"value": "Training", "label": "ChatGPT primarily uses training knowledge"},
          {"value": "2x", "label": "more source transparency on Perplexity vs ChatGPT"},
        ],
        "blocks": [
          {"type": "h2", "heading": "The Core Difference: Live Web vs. Training Data", "text": "The Core Difference: Live Web vs. Training Data"},
          {"type": "p", "text": "The most important distinction between Perplexity and ChatGPT for law firm visibility is how each platform sources its answers. Perplexity retrieves live web content in real time and cites those sources explicitly. ChatGPT primarily draws on knowledge learned during training — a fixed snapshot of the internet that does not update with new content you publish."},
          {"type": "p", "text": "This has profound implications for strategy. Improving your website content today can affect your Perplexity citations within days or weeks as its crawler picks up the changes. The same content improvements may not influence ChatGPT's answers for months — or may not affect them at all until OpenAI retrains the model. For firms that want fast, measurable results, Perplexity is often the more responsive platform."},
          {"type": "h2", "heading": "Citation Visibility: How Each Platform Shows Sources", "text": "Citation Visibility: How Each Platform Shows Sources"},
          {"type": "ul", "heading": "How each platform attributes sources", "items": [
            "Perplexity: numbered citations shown prominently alongside the answer, visible immediately.",
            "ChatGPT: does not consistently cite sources; may mention firm names without linking.",
            "Perplexity Pro: even richer citations with page previews and links.",
            "ChatGPT with Browsing: can cite web sources but does so less consistently than Perplexity.",
          ]},
          {"type": "callout", "text": "For law firms, visible citation on Perplexity acts as a trust signal. Prospective clients can see that your firm's content was judged authoritative enough to be the source of the answer they just read."},
        ],
        "faqs": [
          {"question": "Should law firms optimize for Perplexity or ChatGPT first?", "answer": "Both matter, but they reward somewhat different investments. Perplexity responds faster to fresh, well-structured content. ChatGPT rewards long-term entity building and authority signals. A comprehensive AI visibility strategy covers both."},
          {"question": "Can the same content work for both platforms?", "answer": "Yes. High-quality, specific, well-structured content that answers real client questions performs well on both platforms. The technical signals differ slightly, but the content principles are the same."},
          {"question": "Which platform do legal clients use more?", "answer": "ChatGPT currently has more users overall. But Perplexity's user base skews heavily toward educated, research-oriented consumers — a profile that closely matches someone seriously considering hiring a lawyer."},
        ],
        "related": ["perplexity-ai-for-law-firms", "how-to-get-cited-on-perplexity"],
      },
    ],
  },
  {
    "slug": "ai-websites",
    "name": "AI Websites for Law Firms",
    "description": "Modern law firm websites built with AI-powered design, conversion optimization, and technical foundations that turn visitors into consultations.",
    "articles": [
      {
        "slug": "ai-website-design-for-law-firms",
        "title": "AI Website Design for Law Firms: What the Best Sites Do Differently",
        "description": "The law firm websites that convert at the highest rates share specific design principles. Here is what separates a great legal website from an average one.",
        "readTime": "12 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "3.2s", "label": "load time threshold before 40% of visitors leave"},
          {"value": "67%", "label": "of legal searches happen on mobile devices"},
          {"value": "4.2x", "label": "more leads from sites with live chat or intake forms"},
        ],
        "blocks": [
          {"type": "h2", "heading": "Why Most Law Firm Websites Fail at Conversion", "text": "Why Most Law Firm Websites Fail at Conversion"},
          {"type": "p", "text": "The average law firm website was designed to look professional, not to convert. It has a large hero image, a paragraph about the firm's values, a team page, and a contact form. That template may have worked in 2010, when most visitors came from directories or word of mouth and already intended to call. It does not work in an era where potential clients arrive from AI search results and organic Google traffic — users who are still evaluating whether to reach out at all."},
          {"type": "p", "text": "High-converting law firm websites treat every page as a landing page. They answer the visitor's question immediately, establish credibility within seconds, and make the next step — a call, a form, a chat — frictionless. The design choices that accomplish this are specific, learnable, and repeatable."},
          {"type": "callout", "text": "A 1-second improvement in page load time can improve conversion rates by 7%. For a firm getting 1,000 monthly visitors, that is dozens of additional consultations — just from a faster website."},
          {"type": "h2", "heading": "Core Design Principles for High-Converting Legal Websites", "text": "Core Design Principles for High-Converting Legal Websites"},
          {"type": "ul", "heading": "What separates converting sites from non-converting ones", "items": [
            "Above-the-fold clarity: the visitor knows within 3 seconds what the firm does and where it practices.",
            "Social proof near the top: reviews, case results, and bar admissions visible immediately.",
            "One primary CTA per page: a single clear action prevents decision paralysis.",
            "Mobile-first layout: navigation, CTAs, and forms designed for thumbs, not cursors.",
            "Fast load times: compressed images, minimal JavaScript, and server-side rendering.",
            "Trust signals throughout: headshots, bar logos, awards, and publication features.",
          ]},
          {"type": "h2", "heading": "AI Features That Modern Law Firm Websites Include", "text": "AI Features That Modern Law Firm Websites Include"},
          {"type": "p", "text": "AI-powered law firm websites go beyond good design. They incorporate intake chatbots that qualify leads before a human ever gets involved, smart call tracking that routes calls based on practice area and time of day, and automated follow-up sequences that re-engage visitors who left without contacting the firm. These features work around the clock, ensuring that no lead falls through the cracks between business hours."},
        ],
        "faqs": [
          {"question": "How much should a law firm spend on a new website?", "answer": "Quality law firm websites typically range from $8,000 to $30,000 for custom builds, depending on complexity, content needs, and integrations. The ROI calculation is simple: if a new client is worth $5,000 and the site converts 10 additional clients per year, a $20,000 investment pays back in 4 months."},
          {"question": "How often should a law firm redesign its website?", "answer": "Major redesigns every 3–5 years, with continuous minor improvements throughout. Focus annual attention on page speed, content freshness, and conversion rate optimization rather than aesthetic overhauls."},
          {"question": "What is the most important page on a law firm website?", "answer": "Typically the practice area page most aligned with your highest-value cases. That page should be the most detailed, best-optimized, and most clearly conversion-focused page on the site."},
        ],
        "related": ["law-firm-website-conversion-optimization", "mobile-first-law-firm-websites"],
      },
      {
        "slug": "law-firm-website-conversion-optimization",
        "title": "Law Firm Website Conversion Optimization: Turning Visitors into Clients",
        "description": "Most law firm websites attract visitors but fail to convert them. These proven optimization strategies close that gap.",
        "readTime": "10 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "2.4%", "label": "average legal website conversion rate"},
          {"value": "8–12%", "label": "conversion rate for optimized legal sites"},
          {"value": "68%", "label": "of visitors who bounce never return"},
        ],
        "blocks": [
          {"type": "h2", "heading": "Understanding Why Visitors Don't Convert", "text": "Understanding Why Visitors Don't Convert"},
          {"type": "p", "text": "Before optimizing, diagnose. Most law firm websites lose visitors at three specific points: the moment they arrive and don't immediately understand the firm's value proposition; the moment they try to find practice area information and encounter vague, generic descriptions; and the moment they attempt to contact the firm and face a form with too many fields or a phone number that doesn't answer."},
          {"type": "h2", "heading": "The CRO Stack for Law Firms", "text": "The CRO Stack for Law Firms"},
          {"type": "ul", "heading": "Conversion rate optimization tools that work for legal websites", "items": [
            "Heatmapping (Hotjar, Microsoft Clarity) — see exactly where visitors click and where they drop off.",
            "Session recordings — watch real visitor sessions to identify friction points.",
            "A/B testing on headlines and CTA button text — small copy changes often yield 20–40% conversion lifts.",
            "Live chat with real operators or AI bots during business hours.",
            "Call tracking (CallRail) — understand which pages and traffic sources drive the most calls.",
            "Form analytics — identify which fields cause visitors to abandon intake forms.",
          ]},
          {"type": "callout", "text": "The fastest conversion wins usually come from the simplest changes: a headline that addresses the visitor's specific fear, a CTA button that says 'Get a Free Consultation' instead of 'Contact Us,' and a phone number in the top-right corner of every page."},
          {"type": "h2", "heading": "The Intake Form: Where Most Firms Lose Leads", "text": "The Intake Form: Where Most Firms Lose Leads"},
          {"type": "p", "text": "The standard law firm intake form asks for name, email, phone, case type, case description, and how they heard about you. That is five to six fields, and every additional field reduces completion rates. For initial intake, ask only for the minimum: name, phone number, and practice area. Qualify further after the first contact, not before."},
        ],
        "faqs": [
          {"question": "What is a good conversion rate for a law firm website?", "answer": "The industry average is around 2–3%. Well-optimized law firm sites achieve 8–12%. If you're below 5%, there is significant room to improve through copy, design, and form optimization."},
          {"question": "Should law firms use pop-up chat widgets?", "answer": "Used thoughtfully, yes. Triggered chat that appears after a visitor has been on a practice area page for 30+ seconds performs well without being intrusive. Immediate pop-ups on first page load tend to increase bounce rates."},
          {"question": "How important are Google reviews to conversion?", "answer": "Very important. Displaying your Google review rating prominently on the homepage and practice area pages builds immediate trust. Firms with 4.8+ star averages displayed near the CTA see measurably higher conversion rates."},
        ],
        "related": ["ai-website-design-for-law-firms", "mobile-first-law-firm-websites"],
      },
      {
        "slug": "mobile-first-law-firm-websites",
        "title": "Mobile-First Law Firm Websites: Why It Matters and How to Get It Right",
        "description": "67% of legal searches happen on mobile. Here is how to build a law firm website that converts mobile visitors into consultations.",
        "readTime": "9 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "67%", "label": "of legal searches are on mobile"},
          {"value": "53%", "label": "of mobile users leave if the site takes over 3 seconds"},
          {"value": "2x", "label": "more calls from click-to-call on mobile-first sites"},
        ],
        "blocks": [
          {"type": "h2", "heading": "The Mobile Reality for Legal Marketing", "text": "The Mobile Reality for Legal Marketing"},
          {"type": "p", "text": "Most people experiencing a legal crisis reach for their phone first. Whether it is a late-night DUI arrest, a workplace injury, or a landlord dispute, the initial search for legal help happens on mobile devices. If your law firm's website is not optimized for mobile — and most are not — you are losing leads to competitors who prioritized it."},
          {"type": "p", "text": "Mobile-first is not just about making your site look good on small screens. It means designing the entire user experience around the behaviors and needs of a mobile user: one-thumb navigation, tap-to-call CTAs, fast load times on cellular networks, and forms designed to be completed on a phone keyboard."},
          {"type": "ul", "heading": "Mobile design requirements for law firm websites", "items": [
            "Click-to-call button pinned to the bottom of the screen at all times.",
            "Navigation simplified to three or four key destinations.",
            "Text size minimum 16px to avoid pinch-zooming.",
            "Forms with no more than three to four fields on the first screen.",
            "Images compressed to WebP format for fast cellular loading.",
            "Core Web Vitals scores of 90+ on Google PageSpeed Insights.",
          ]},
          {"type": "callout", "text": "Google uses mobile-first indexing. The mobile version of your site is what Google evaluates for ranking purposes. A site that performs poorly on mobile will rank worse — which means fewer visitors, not just worse conversion."},
        ],
        "faqs": [
          {"question": "What is the minimum acceptable load time for a mobile legal site?", "answer": "Aim for under 2.5 seconds for the Largest Contentful Paint (LCP). Google considers 2.5 seconds the threshold for a 'good' LCP. Above 4 seconds, you are likely to see significant bounce rate increases."},
          {"question": "Should a law firm have a separate mobile website?", "answer": "No. Separate mobile sites (m.domain.com) are an outdated approach. Use a responsive design that adapts to any screen size from a single URL. This is both technically simpler and better for SEO."},
          {"question": "How do I test my law firm website's mobile performance?", "answer": "Use Google PageSpeed Insights (free), Google Search Console's Core Web Vitals report, and personally test your site on a mid-range Android device on a 4G cellular connection — not your office Wi-Fi."},
        ],
        "related": ["ai-website-design-for-law-firms", "law-firm-website-conversion-optimization"],
      },
    ],
  },
  {
    "slug": "ai-seo",
    "name": "AI SEO for Law Firms",
    "description": "AI-first search optimization for law firms — covering generative engine optimization, entity SEO, structured data, and the signals that earn AI citations.",
    "articles": [
      {
        "slug": "ai-seo-for-law-firms",
        "title": "AI SEO for Law Firms: The Complete Guide to AI-First Search Optimization",
        "description": "Traditional SEO is no longer enough. Here is the complete guide to AI SEO — optimizing your law firm to be found and cited by ChatGPT, Gemini, and Perplexity.",
        "readTime": "14 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "40%", "label": "of Google searches now show AI Overviews"},
          {"value": "60%", "label": "of all searches are zero-click"},
          {"value": "3–5", "label": "sources cited per AI-generated answer"},
        ],
        "blocks": [
          {"type": "h2", "heading": "What Is AI SEO and Why Does It Matter for Law Firms?", "text": "What Is AI SEO and Why Does It Matter for Law Firms?"},
          {"type": "p", "text": "AI SEO — also called Generative Engine Optimization or GEO — is the practice of optimizing your law firm's digital presence to appear in answers generated by AI platforms. Where traditional SEO aims to rank in Google's blue links, AI SEO aims to be cited inside the AI-generated summaries that now appear above those links, and inside the conversational answers that ChatGPT, Gemini, and Perplexity provide when users ask legal questions."},
          {"type": "p", "text": "The distinction matters because the AI layer is capturing more and more of users' attention. When 40% of Google searches show an AI Overview at the top of the page, the firms cited in those overviews receive visibility that the firms ranking below them in the blue links simply cannot match — and those users may never scroll down to the traditional results at all."},
          {"type": "callout", "text": "AI SEO does not replace traditional SEO — it extends it. The same foundations that earn Google rankings (authority, relevance, technical quality) also influence AI citations. The difference is in the additional signals that AI engines require: entity recognition, structured data, and question-and-answer content formats."},
          {"type": "h2", "heading": "The Four Pillars of AI SEO for Law Firms", "text": "The Four Pillars of AI SEO for Law Firms"},
          {"type": "ul", "heading": "What AI SEO requires", "items": [
            "Entity Authority: making sure AI engines know who your firm is, where you practice, and what you do.",
            "Content Depth: comprehensive, specific answers to the questions clients actually ask AI platforms.",
            "Structured Data: schema markup that makes your content machine-readable and citation-ready.",
            "Citation Signals: third-party mentions in trusted legal directories and publications.",
          ]},
          {"type": "h2", "heading": "Entity SEO: Making Your Firm Known to AI", "text": "Entity SEO: Making Your Firm Known to AI"},
          {"type": "p", "text": "AI engines don't just index pages — they build knowledge graphs of entities: organizations, people, and places. Your law firm is an entity. The AI needs to know your firm's name, location, practice areas, attorneys, and how all these relate to each other. Entity signals come from consistent information across your website, Google Business Profile, legal directories, bar association listings, and any publication that mentions your firm."},
          {"type": "h2", "heading": "Content Strategy for AI Citation", "text": "Content Strategy for AI Citation"},
          {"type": "p", "text": "AI-friendly content is specific, accurate, and structured. It answers a discrete question completely and correctly. A page titled 'Personal Injury Law' with three paragraphs of generic description will not earn AI citations. A page titled 'What to Do After a Car Accident in Texas: A Step-by-Step Guide' that answers the question thoroughly — with numbered steps, a FAQ section, and jurisdiction-specific accuracy — will."},
        ],
        "faqs": [
          {"question": "Is AI SEO only relevant for large law firms?", "answer": "No. AI engines reward relevance and specificity, which small firms can achieve. A solo practitioner with highly specific, accurate answers about a narrow practice area in a specific jurisdiction can outperform a large generalist firm on AI citations for those queries."},
          {"question": "How much does AI SEO differ from traditional SEO?", "answer": "The foundations overlap significantly — authority, content quality, technical performance. AI SEO adds entity optimization and structured data as critical requirements, and places heavier weight on question-and-answer content formats that match how users interact with AI platforms."},
          {"question": "How do I measure AI SEO performance?", "answer": "Track: manual queries to ChatGPT, Perplexity, and Gemini for your target keywords; AI Overview appearances in Google Search Console; citation tracking through tools like Semrush AI Toolkit; and branded search growth as AI visibility drives awareness."},
        ],
        "related": ["generative-engine-optimization-for-lawyers", "entity-seo-for-law-firms"],
      },
      {
        "slug": "generative-engine-optimization-for-lawyers",
        "title": "Generative Engine Optimization for Lawyers: What GEO Actually Means",
        "description": "GEO — Generative Engine Optimization — is the emerging discipline of earning visibility inside AI-generated answers. Here is what it means for legal practices.",
        "readTime": "11 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "GEO", "label": "the fastest-growing discipline in digital marketing"},
          {"value": "2026", "label": "the year GEO became essential for law firms"},
          {"value": "10x", "label": "potential reach increase for AI-cited content vs. page-5 rankings"},
        ],
        "blocks": [
          {"type": "h2", "heading": "Defining Generative Engine Optimization", "text": "Defining Generative Engine Optimization"},
          {"type": "p", "text": "Generative Engine Optimization is the practice of optimizing content and digital signals so that AI-powered 'generative engines' — platforms that create answers rather than returning lists of links — include your content in their responses. The term distinguishes the discipline from traditional SEO, which targets algorithmic ranking in link-based search results."},
          {"type": "p", "text": "For lawyers, the practical translation is this: when a potential client asks ChatGPT 'do I need a lawyer for a DUI in Colorado,' GEO is the set of practices that make it more likely that ChatGPT references your firm or your content in that answer. When they ask Perplexity 'what are my rights if I'm wrongfully terminated in California,' GEO determines whether your firm's content is one of the five citations shown."},
          {"type": "callout", "text": "The first generation of lawyers to master GEO will have a compounding advantage. AI citations build brand recognition, which drives direct searches, which builds more authority, which earns more citations. The loop is virtuous for those inside it — and painful for those outside."},
          {"type": "h2", "heading": "GEO Tactics That Work for Legal Practices", "text": "GEO Tactics That Work for Legal Practices"},
          {"type": "ul", "heading": "High-impact GEO actions for law firms", "items": [
            "Publish comprehensive FAQ pages structured around real AI queries for your practice area.",
            "Implement complete schema markup: LegalService, Attorney, FAQPage, BreadcrumbList.",
            "Build consistent entity profiles across Avvo, Martindale, FindLaw, and state bar directories.",
            "Create jurisdiction-specific content that AI platforms can accurately attribute to your location.",
            "Earn mentions in legal publications, local media, and trusted consumer sites.",
            "Structure content with clear H2/H3 headers that match common AI query patterns.",
          ]},
        ],
        "faqs": [
          {"question": "How is GEO different from SEO?", "answer": "Traditional SEO targets algorithmic rankings in lists of links. GEO targets inclusion in AI-generated prose answers. The technical foundations overlap, but GEO places much greater emphasis on entity signals, structured data, and content formats that AI can parse and synthesize."},
          {"question": "Do I need to hire a GEO specialist?", "answer": "GEO is new enough that most 'specialists' are really SEO professionals who have extended their skills. Look for an agency that understands both traditional SEO fundamentals and the specific requirements of AI citation optimization."},
          {"question": "Can I do GEO myself?", "answer": "Yes, especially for content strategy and schema implementation. Adding FAQPage schema, building out Q&A content, and updating legal directories are tasks law firms can manage internally or with minimal outside help."},
        ],
        "related": ["ai-seo-for-law-firms", "entity-seo-for-law-firms"],
      },
      {
        "slug": "entity-seo-for-law-firms",
        "title": "Entity SEO for Law Firms: How AI Engines Learn Who You Are",
        "description": "AI engines reason about entities — organizations, people, places — not just pages. Here is how to build your firm as a recognized, trusted entity in AI knowledge graphs.",
        "readTime": "10 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "Entity", "label": "signals now outweigh keyword density for AI ranking"},
          {"value": "NAP", "label": "consistency across 50+ directories is the baseline"},
          {"value": "3x", "label": "higher AI citation rate for firms with strong entity profiles"},
        ],
        "blocks": [
          {"type": "h2", "heading": "What Is an Entity in AI Search?", "text": "What Is an Entity in AI Search?"},
          {"type": "p", "text": "In AI search, an entity is a distinct, identifiable thing in the world — a person, organization, place, or concept. Your law firm is an entity. Each attorney at your firm is an entity. The practice areas you cover — personal injury, family law, criminal defense — are entities. AI engines build knowledge graphs that map how these entities relate to each other, and they use that graph to answer questions and make recommendations."},
          {"type": "p", "text": "For a law firm, entity SEO means ensuring that the AI's knowledge graph contains accurate, complete, and consistent information about your firm: your name, location, practice areas, attorneys, achievements, and connections to other trusted entities in the legal space. A firm with a rich, accurate entity profile can be confidently cited. A firm the AI barely recognizes cannot."},
          {"type": "ul", "heading": "Key entity signals for law firms", "items": [
            "Consistent Name, Address, and Phone (NAP) across all online profiles.",
            "Google Business Profile with complete categories, services, and attributes.",
            "Avvo, Martindale-Hubbell, FindLaw, Justia, and state bar profiles — all consistent.",
            "Attorney Wikipedia pages or Wikidata entries for senior partners.",
            "sameAs links in your website schema connecting to authoritative profiles.",
            "Mentions in local media, legal publications, and industry awards.",
          ]},
          {"type": "callout", "text": "NAP inconsistency is one of the most damaging entity signals a law firm can send. If your firm appears as 'Smith & Jones, LLC' in one directory and 'Smith and Jones Law' in another, AI engines struggle to unify these as the same entity — which reduces citation confidence."},
        ],
        "faqs": [
          {"question": "What is the most important entity signal for a law firm?", "answer": "Google Business Profile is the single most influential entity signal for local law firm visibility in AI search. Keep it complete, accurate, and actively managed — including responding to reviews and adding photos regularly."},
          {"question": "How do I find all the places my firm appears online?", "answer": "Use tools like Moz Local, BrightLocal, or Whitespark to audit your citation presence. Search your firm name in quotes on Google and review the first five pages of results to identify all active profiles."},
          {"question": "Does Wikipedia matter for entity SEO?", "answer": "Yes, especially for individual attorneys. Wikipedia and Wikidata pages create strong entity signals that AI knowledge graphs directly consume. However, Wikipedia has strict notability requirements — focus on qualifying through legitimate achievements before attempting a Wikipedia page."},
        ],
        "related": ["ai-seo-for-law-firms", "generative-engine-optimization-for-lawyers"],
      },
    ],
  },
  {
    "slug": "schema",
    "name": "Schema & Structured Data for Law Firms",
    "description": "Schema markup is the language AI engines trust. Learn which structured data types help law firms get understood, trusted, and cited across all AI platforms.",
    "articles": [
      {
        "slug": "schema-markup-for-law-firms",
        "title": "Schema Markup for Law Firms: The Complete Structured Data Guide",
        "description": "Which schema types do law firms need, how do you implement them correctly, and why does structured data matter for AI citations? Everything in one guide.",
        "readTime": "13 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "2.4x", "label": "more AI citations for schema-marked pages"},
          {"value": "LegalService", "label": "is the highest-priority schema for law firms"},
          {"value": "FAQPage", "label": "schema alone can trigger AI Overview appearance"},
        ],
        "blocks": [
          {"type": "h2", "heading": "Why Schema Markup Is Essential for Law Firm AI Visibility", "text": "Why Schema Markup Is Essential for Law Firm AI Visibility"},
          {"type": "p", "text": "Schema markup — also called structured data — is a vocabulary of tags you add to your website's HTML that tells search engines and AI platforms exactly what your content means. Without schema, a search engine reads your text and infers meaning through natural language processing. With schema, you tell it directly: 'This is a LegalService. It operates in Toronto. It covers family law and estate planning. The attorney in charge is Jane Smith, who was called to the Ontario Bar in 2012.'"},
          {"type": "p", "text": "AI engines rely on structured data because they need to efficiently process millions of pages. Clear schema signals reduce ambiguity and increase the confidence with which an AI can recommend your firm. Firms with complete, accurate schema markup are cited more often because they are easier to trust."},
          {"type": "ul", "heading": "Essential schema types for law firms", "items": [
            "LegalService — the primary type for law firm pages; includes practice areas and jurisdiction.",
            "Attorney or Person — for each lawyer's individual profile page.",
            "FAQPage — wraps your Q&A sections and is directly consumed by AI Overviews.",
            "BreadcrumbList — signals page hierarchy and improves navigational understanding.",
            "LocalBusiness — reinforces geographic service area and contact information.",
            "Article — for blog posts, guides, and insight pages.",
            "Review/AggregateRating — for displaying and validating client testimonials.",
          ]},
          {"type": "callout", "text": "FAQPage schema is particularly powerful. Google directly uses FAQ markup to populate AI Overviews and rich results. A well-marked FAQ section on your practice area pages is one of the highest-leverage actions you can take for AI visibility today."},
          {"type": "h2", "heading": "Implementing Schema Correctly", "text": "Implementing Schema Correctly"},
          {"type": "p", "text": "Schema markup is implemented as JSON-LD — a block of structured JSON code placed in the head section of your HTML. JSON-LD is the format Google and most AI engines prefer. Microdata and RDFa (alternative schema formats) are largely obsolete for new implementations. Each page should have the schema types most relevant to its content — do not add every type to every page, as this creates noise rather than clarity."},
        ],
        "faqs": [
          {"question": "Does schema markup directly improve Google rankings?", "answer": "Schema is not a direct ranking factor, but it significantly improves how Google understands and displays your content — through rich results, AI Overviews, and featured snippets. These enhanced displays drive more clicks and traffic, which indirectly improves rankings over time."},
          {"question": "How do I test whether my schema is implemented correctly?", "answer": "Use Google's Rich Results Test (search.google.com/test/rich-results) and Schema Markup Validator (validator.schema.org). Both tools identify errors, warnings, and missing fields in your structured data."},
          {"question": "Can I add schema to my existing website or do I need a developer?", "answer": "Many CMS platforms (WordPress, Squarespace, Wix) have schema plugins or built-in tools. For custom sites, you'll need developer help to add JSON-LD blocks to the relevant pages. The implementation effort is typically 10–20 hours for a full law firm site."},
        ],
        "related": ["legalservice-schema-guide", "faqpage-schema-for-lawyers"],
      },
      {
        "slug": "legalservice-schema-guide",
        "title": "LegalService Schema for Law Firms: The Implementation Guide",
        "description": "LegalService is the most important schema type for law firm websites. Here is how to implement it correctly and what fields matter most for AI visibility.",
        "readTime": "10 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "LegalService", "label": "extends LocalBusiness with legal-specific properties"},
          {"value": "areaServed", "label": "field is critical for local AI citation accuracy"},
          {"value": "JSON-LD", "label": "is the only format worth implementing in 2026"},
        ],
        "blocks": [
          {"type": "h2", "heading": "What Is LegalService Schema?", "text": "What Is LegalService Schema?"},
          {"type": "p", "text": "LegalService is a Schema.org type that extends LocalBusiness specifically for legal practices. It allows you to declare your firm's practice areas, jurisdictions, attorney credentials, and service types in a machine-readable format that search engines and AI platforms can reliably parse. It is the most specific — and therefore most useful — schema type available to law firms."},
          {"type": "h2", "heading": "Complete LegalService JSON-LD Example", "text": "Complete LegalService JSON-LD Example"},
          {"type": "ul", "heading": "Critical LegalService fields to include", "items": [
            "@type: 'LegalService' — must be exact; do not substitute with 'LocalBusiness' alone.",
            "name: your firm's legal registered name, exactly as it appears everywhere else.",
            "url: canonical URL of the page this schema appears on.",
            "areaServed: array of states, provinces, or cities you serve.",
            "serviceType: array of specific practice areas (e.g., 'Personal Injury', 'Family Law').",
            "address with streetAddress, city, state, postalCode, and country.",
            "telephone in E.164 format (+12345678900).",
            "sameAs: array of URLs to your profiles on Avvo, Martindale, Google Business, and LinkedIn.",
          ]},
          {"type": "callout", "text": "The sameAs field is one of the most overlooked and highest-impact fields in LegalService schema. It tells AI knowledge graphs that your website entity and your Avvo profile are the same organization — unifying entity signals across platforms."},
        ],
        "faqs": [
          {"question": "Should LegalService schema go on every page or just the homepage?", "answer": "Add LegalService schema to your homepage and primary practice area pages. Your contact page and about page can also benefit. Individual blog posts typically use Article schema instead."},
          {"question": "What is the difference between LegalService and Attorney schema?", "answer": "LegalService describes the firm as an organization. Attorney (or Person with hasCredential) describes individual lawyers. Use LegalService on firm-level pages and Attorney/Person on individual attorney bio pages."},
          {"question": "How specific should my serviceType field be?", "answer": "As specific as accurately applies. 'Personal Injury' is better than 'Law'; 'Motor Vehicle Accidents' is even better if that is a core focus. More specific serviceType values help AI engines match your firm to more precise queries."},
        ],
        "related": ["schema-markup-for-law-firms", "faqpage-schema-for-lawyers"],
      },
      {
        "slug": "faqpage-schema-for-lawyers",
        "title": "FAQPage Schema for Law Firms: Winning AI Citations with Structured Q&A",
        "description": "FAQPage schema is one of the most powerful structured data types for earning AI Overview citations. Here is how lawyers should implement it.",
        "readTime": "9 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "FAQPage", "label": "schema directly feeds Google AI Overviews"},
          {"value": "3.1x", "label": "higher click-through rate for FAQ rich results"},
          {"value": "2–5", "label": "FAQs per page is the optimal range for most legal pages"},
        ],
        "blocks": [
          {"type": "h2", "heading": "Why FAQPage Schema Is Especially Powerful for Law Firms", "text": "Why FAQPage Schema Is Especially Powerful for Law Firms"},
          {"type": "p", "text": "Legal questions are among the most common queries people bring to AI platforms. 'Do I need a lawyer for probate?' 'What happens at a DUI arraignment?' 'Can I sue my employer for wrongful termination?' These are discrete, answerable questions — exactly the format that FAQPage schema is designed to capture and communicate to AI engines."},
          {"type": "p", "text": "When you add FAQPage schema to a page, you are telling Google, ChatGPT's web browsing mode, Perplexity, and other AI platforms: 'Here is a question. Here is the precise answer my firm provides.' That structured signal is consumed directly by AI Overviews, which frequently display FAQ content verbatim in their summaries."},
          {"type": "ul", "heading": "Best practices for legal FAQPage schema", "items": [
            "Only mark up Q&As that appear visibly on the page — do not add hidden schema.",
            "Write questions exactly as a client would type them into an AI platform.",
            "Keep answers concise and complete — 40 to 60 words is usually optimal.",
            "Include jurisdiction-specific details in answers where relevant.",
            "Add 2–5 FAQ items per page; too many dilutes the signal.",
            "Update FAQ content when laws change in your jurisdiction.",
          ]},
          {"type": "callout", "text": "Write your FAQ questions as a nervous client would ask them at 11pm, not as a lawyer would phrase them in a brief. 'What happens if I get a DUI?' not 'What are the legal consequences of operating a motor vehicle under the influence of alcohol?'"},
        ],
        "faqs": [
          {"question": "Can I use FAQPage schema on every page of my site?", "answer": "You can, but only add it to pages that actually contain visible Q&A content. Adding schema for content that doesn't appear on the page violates Google's guidelines and can result in manual penalties."},
          {"question": "Do FAQPage rich results still appear in Google search?", "answer": "Google has reduced FAQ rich results for general websites, but they remain active for authoritative, helpful content. More importantly, FAQPage schema directly influences AI Overviews regardless of whether the traditional rich result appears."},
          {"question": "Should I write FAQs for every practice area page?", "answer": "Yes. Every practice area page should have a FAQ section with 3–5 questions that real clients ask about that area of law. It serves both AI citation purposes and user experience — prospective clients value clear answers to their real concerns."},
        ],
        "related": ["schema-markup-for-law-firms", "legalservice-schema-guide"],
      },
    ],
  },
  {
    "slug": "ai-receptionists",
    "name": "AI Receptionists for Law Firms",
    "description": "AI phone receptionists handle after-hours calls, qualify leads, and book consultations automatically. Learn how to capture every potential client who calls your firm.",
    "articles": [
      {
        "slug": "ai-receptionist-for-law-firms",
        "title": "AI Receptionist for Law Firms: Never Miss a Lead After Hours",
        "description": "Most law firms miss 42% of incoming calls. An AI receptionist answers every call, qualifies the lead, and books a consultation — at any hour.",
        "readTime": "11 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "42%", "label": "of law firm calls go unanswered"},
          {"value": "78%", "label": "of callers don't leave a voicemail"},
          {"value": "10x", "label": "ROI for firms using AI receptionists"},
        ],
        "blocks": [
          {"type": "h2", "heading": "The Missed Call Problem in Legal", "text": "The Missed Call Problem in Legal"},
          {"type": "p", "text": "Legal emergencies don't respect business hours. A client arrested on a Friday night, a spouse served with divorce papers on a Sunday afternoon, a business owner facing an injunction at 6pm — these people call law firms immediately, when the crisis happens. If no one answers, most of them move to the next firm on the list. Research consistently shows that 78% of callers who reach voicemail do not leave a message. They simply hang up and call a competitor."},
          {"type": "p", "text": "AI receptionists solve this problem by providing a professional, intelligent voice that answers every call within seconds, 24 hours a day, 7 days a week. They can gather caller information, ask qualifying questions relevant to your practice areas, and book consultations directly into your calendar — all without human involvement."},
          {"type": "callout", "text": "The first firm to answer is often the firm that gets hired. In legal, speed to response is one of the most powerful competitive advantages a firm can build — and an AI receptionist makes it automatic."},
          {"type": "h2", "heading": "What AI Receptionists Can Do for Law Firms", "text": "What AI Receptionists Can Do for Law Firms"},
          {"type": "ul", "heading": "Capabilities of modern AI receptionists", "items": [
            "Answer calls instantly in a natural, professional voice.",
            "Gather caller name, contact information, and reason for calling.",
            "Ask qualifying questions specific to your practice areas.",
            "Determine urgency and flag emergency situations for immediate attorney callback.",
            "Schedule consultations directly into your firm's calendar.",
            "Send follow-up texts or emails with intake forms after the call.",
            "Transfer to a live person when the caller requests human assistance.",
          ]},
          {"type": "h2", "heading": "How to Choose an AI Receptionist for Your Law Firm", "text": "How to Choose an AI Receptionist for Your Law Firm"},
          {"type": "p", "text": "Not all AI receptionist services are designed for legal. Look for platforms with legal intake experience, HIPAA-compliant data handling (important for family law and personal injury matters), the ability to customize scripts for your specific practice areas, and calendar integration with whatever scheduling system your firm uses. The quality of the voice and the naturalness of the conversation also matters significantly for caller experience."},
        ],
        "faqs": [
          {"question": "Can clients tell they're talking to an AI?", "answer": "Modern AI receptionists are very convincing, but most legal AI receptionist providers recommend transparency — the system introduces itself as an automated assistant. Clients generally respond positively when the system is helpful and professional, regardless of whether it is AI-powered."},
          {"question": "What happens when a caller has a genuine emergency?", "answer": "AI receptionists can be programmed to recognize urgent situations — criminal arrests, active domestic violence, time-sensitive legal deadlines — and immediately page or call the on-call attorney. Emergency escalation is a critical feature for any legal AI receptionist."},
          {"question": "How much does a legal AI receptionist cost?", "answer": "Most legal AI receptionist services charge between $300 and $800 per month for small to mid-size firms, depending on call volume and features. Compared to the cost of a human receptionist or the cost of missed leads, the ROI is typically strong within the first 60 days."},
        ],
        "related": ["best-ai-receptionist-software-for-lawyers", "ai-receptionist-vs-virtual-receptionist"],
      },
      {
        "slug": "best-ai-receptionist-software-for-lawyers",
        "title": "Best AI Receptionist Software for Lawyers in 2026",
        "description": "Comparing the top AI receptionist platforms for law firms — what each does well, what to watch for, and how to choose the right one for your practice.",
        "readTime": "10 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "5+", "label": "dedicated legal AI receptionist platforms"},
          {"value": "24/7", "label": "availability is the primary requirement"},
          {"value": "30 days", "label": "is enough to evaluate ROI"},
        ],
        "blocks": [
          {"type": "h2", "heading": "What to Look for in a Legal AI Receptionist", "text": "What to Look for in a Legal AI Receptionist"},
          {"type": "ul", "heading": "Key evaluation criteria for legal AI receptionists", "items": [
            "Legal industry experience: scripts and workflows built for legal intake, not generic business.",
            "Voice quality: natural-sounding conversation that does not frustrate callers.",
            "Customization: ability to configure questions and responses for your specific practice areas.",
            "Calendar integration: direct booking into Clio, MyCase, Lawmatics, or your specific system.",
            "Data security: HIPAA compliance and attorney-client privilege considerations.",
            "Escalation protocols: clear rules for when to page the attorney immediately.",
            "Reporting: call transcripts, recordings, and intake summaries delivered to your inbox.",
          ]},
          {"type": "h2", "heading": "Leading Options for Law Firms", "text": "Leading Options for Law Firms"},
          {"type": "p", "text": "The legal AI receptionist market has matured rapidly. Platforms like Smith.ai, Answering Legal, and Lexamica have built specifically for law firms and offer proven legal intake workflows. General AI receptionist platforms like Goodcall can also be configured for legal use. Evaluate each on call quality, integration capabilities, and total cost for your call volume."},
          {"type": "callout", "text": "Request a free trial from any platform before committing. The only reliable way to evaluate call quality is to make test calls yourself and have a colleague call in as a potential client — then review the transcript and recording."},
        ],
        "faqs": [
          {"question": "Should I use an AI or human virtual receptionist?", "answer": "For most small and mid-size law firms, AI receptionists offer a better cost-to-performance ratio than human virtual receptionists for standard intake. Human virtual receptionists add value for complex calls where empathy and judgment are critical. Many firms use AI for initial qualification and humans for follow-up."},
          {"question": "Can AI receptionists handle multiple calls simultaneously?", "answer": "Yes. Unlike human receptionists, AI handles unlimited concurrent calls. This is particularly valuable during high-volume periods like Monday mornings, days after news events that trigger legal questions, or when a major advertising campaign runs."},
          {"question": "How do I set up an AI receptionist for my law firm?", "answer": "Most platforms take 1–2 weeks to configure. You'll provide your firm's information, define intake scripts for each practice area, set escalation rules, and connect your calendar. A good provider will guide you through the setup and test the system before going live."},
        ],
        "related": ["ai-receptionist-for-law-firms", "ai-receptionist-vs-virtual-receptionist"],
      },
      {
        "slug": "ai-receptionist-vs-virtual-receptionist",
        "title": "AI Receptionist vs Virtual Receptionist: Which Is Right for Your Law Firm?",
        "description": "Comparing AI-powered phone answering with human virtual receptionist services — cost, quality, availability, and which makes more sense for your practice.",
        "readTime": "9 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "$12–25", "label": "per hour for human virtual receptionists"},
          {"value": "$0.10–0.40", "label": "per minute for AI receptionist services"},
          {"value": "24/7", "label": "AI availability vs. business hours for most human services"},
        ],
        "blocks": [
          {"type": "h2", "heading": "The Core Trade-Off", "text": "The Core Trade-Off"},
          {"type": "p", "text": "Human virtual receptionists bring empathy, judgment, and the ability to handle genuinely unexpected situations. AI receptionists bring 24/7 availability, perfect consistency, zero hold times, and dramatically lower cost. For most law firms, the decision is not which to choose but rather where in the client journey each belongs."},
          {"type": "ul", "heading": "AI receptionist strengths for law firms", "items": [
            "Available 24/7/365, including holidays and nights.",
            "Zero hold times — answers on the first ring every time.",
            "Consistent script adherence — never goes off-message.",
            "Handles unlimited simultaneous calls during peak periods.",
            "Cost-effective at scale — no overtime, benefits, or turnover.",
          ]},
          {"type": "ul", "heading": "Human virtual receptionist strengths", "items": [
            "Superior empathy for emotionally distressed callers.",
            "Handles genuinely novel situations outside the script.",
            "Better for complex scheduling and multi-step instructions.",
            "Builds human rapport that can positively influence hiring decisions.",
          ]},
          {"type": "callout", "text": "Many high-performing law firms use a hybrid approach: AI for after-hours and overflow calls, human virtual receptionists for daytime calls where empathy matters most. This combination maximizes both coverage and call quality."},
        ],
        "faqs": [
          {"question": "Which option is better for personal injury law firms?", "answer": "Personal injury callers are often distressed or injured. Human receptionists are generally more appropriate for emotionally sensitive intake — but AI is far better than voicemail. A hybrid approach works well: AI after hours, humans during business hours."},
          {"question": "What is the typical contract length for virtual receptionist services?", "answer": "Most AI receptionist services are month-to-month. Human virtual receptionist services often require 3–6 month contracts. Month-to-month allows you to test and compare without long-term commitment."},
          {"question": "Can I switch from one to the other easily?", "answer": "Yes. Most law firm management software (Clio, MyCase) integrates with both AI and human receptionist services. You can run both in parallel during a transition or test period without disrupting your intake workflow."},
        ],
        "related": ["ai-receptionist-for-law-firms", "best-ai-receptionist-software-for-lawyers"],
      },
    ],
  },
  {
    "slug": "ai-chatbots",
    "name": "AI Chatbots for Law Firms",
    "description": "Law firm chatbots qualify leads, answer common questions, and book consultations around the clock. Learn how to choose, configure, and get ROI from a legal chatbot.",
    "articles": [
      {
        "slug": "ai-chatbot-for-law-firms",
        "title": "AI Chatbot for Law Firms: Turn Website Visitors into Consultations",
        "description": "An AI chatbot on your law firm website can qualify leads 24/7 and book consultations while you sleep. Here is how to make it work.",
        "readTime": "11 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "85%", "label": "of clients prefer to message before calling"},
          {"value": "4x", "label": "more leads captured with chatbot vs. form alone"},
          {"value": "3 min", "label": "average response time expectation after hours"},
        ],
        "blocks": [
          {"type": "h2", "heading": "Why Legal Chatbots Have Become Essential", "text": "Why Legal Chatbots Have Become Essential"},
          {"type": "p", "text": "The modern legal prospect does not want to fill out a form and wait two days for a callback. They want answers now. Research from numerous legal marketing studies shows that the majority of potential clients prefer to message or chat before speaking on the phone — it feels lower-pressure, allows them to organize their thoughts, and fits into their busy schedules."},
          {"type": "p", "text": "A well-configured AI chatbot captures this preference by offering an immediate, helpful conversation at any hour. The chatbot asks the right qualifying questions, collects contact information, addresses common concerns, and — critically — books a consultation or schedules a callback. The attorney wakes up with a full consultation calendar rather than a pile of voicemails."},
          {"type": "callout", "text": "The window between when a prospect first lands on your website and when they decide to contact you is often under three minutes. A chatbot that engages them within that window converts at a dramatically higher rate than a form they fill out and submit into silence."},
          {"type": "h2", "heading": "What a Legal AI Chatbot Should Do", "text": "What a Legal AI Chatbot Should Do"},
          {"type": "ul", "heading": "Core capabilities of an effective legal chatbot", "items": [
            "Greet visitors with a specific, relevant opening based on the page they are on.",
            "Ask qualifying questions tailored to each practice area.",
            "Collect name, email, phone number, and case type.",
            "Answer common questions about the firm's process, fees, and areas of practice.",
            "Book a consultation or callback directly into the attorney's calendar.",
            "Send immediate follow-up messages with next steps and firm contact information.",
            "Escalate to a live person when the visitor requests human assistance.",
          ]},
        ],
        "faqs": [
          {"question": "Will a chatbot make my law firm seem impersonal?", "answer": "A poorly configured chatbot will. A well-configured one is indistinguishable from a human assistant in most cases, and prospective clients often prefer the low-pressure format. The key is to make the conversation helpful and efficient — not robotic."},
          {"question": "How much do legal chatbots cost?", "answer": "Legal chatbot platforms range from $100 to $500 per month for smaller firms, depending on features and conversation volume. Many offer free trials. The ROI calculation is simple: if the chatbot generates two additional retained cases per month and each case is worth $3,000, it pays for itself many times over."},
          {"question": "Can a chatbot replace my intake team?", "answer": "A chatbot handles initial qualification and information gathering exceptionally well. It should hand off to a human for complex consultations, fee agreements, and emotionally sensitive situations. Think of it as a first-contact tool that prepares a warm lead for your team, not a replacement for human judgment."},
        ],
        "related": ["law-firm-chatbot-best-practices", "chatbot-vs-live-chat-for-law-firms"],
      },
      {
        "slug": "law-firm-chatbot-best-practices",
        "title": "Law Firm Chatbot Best Practices: What Separates Good From Great",
        "description": "Most law firm chatbots underperform because of avoidable configuration mistakes. These best practices separate the chatbots that convert from the ones that frustrate.",
        "readTime": "10 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "Page-specific", "label": "triggers increase chatbot engagement by 3.4x"},
          {"value": "3 questions", "label": "maximum before asking for contact info"},
          {"value": "40%", "label": "abandonment rate when chatbot asks too many questions"},
        ],
        "blocks": [
          {"type": "h2", "heading": "The Most Common Legal Chatbot Mistakes", "text": "The Most Common Legal Chatbot Mistakes"},
          {"type": "ul", "heading": "Mistakes that kill legal chatbot conversion", "items": [
            "Generic opening message on every page: 'Hi! How can I help you today?' tells the visitor nothing.",
            "Asking for email before establishing any value — visitors leave before completing the form.",
            "Too many questions before offering value or booking a call.",
            "No personality: robotic, cold language in a context where people are stressed and scared.",
            "No clear CTA: the chatbot answers questions but never asks for the booking.",
            "No handoff protocol: the chatbot cannot escalate to a human when needed.",
          ]},
          {"type": "h2", "heading": "The Optimal Legal Chatbot Flow", "text": "The Optimal Legal Chatbot Flow"},
          {"type": "p", "text": "The best legal chatbot flows follow a predictable pattern: specific opening, brief qualification, offer of value, collection of contact info, booking or callback scheduling. On a personal injury page, the opening might be: 'Were you or someone you know recently injured in an accident? I can connect you with one of our attorneys for a free consultation today.' Specific. Relevant. Offering something concrete."},
          {"type": "callout", "text": "Put the call to action earlier than feels comfortable. Most chatbot designers wait too long to ask for the booking. Prospects are often ready to schedule within the first 2–3 exchanges if you make it easy."},
          {"type": "p", "text": "After the initial qualifier, ask one more clarifying question maximum before offering the booking. 'Great — roughly when did the accident occur?' Then: 'I can schedule a free consultation with our team right now. What time works best for you this week?' Two questions, then a booking offer."},
        ],
        "faqs": [
          {"question": "Should my chatbot use a name and avatar?", "answer": "Yes. A named, personalized chatbot (e.g., 'Hi, I'm Lex, the Smith Law Group assistant') performs better than anonymous chat widgets. An avatar — a professional headshot or friendly icon — further increases engagement. Avoid overly cartoon-like avatars that undermine professionalism."},
          {"question": "What should the chatbot say when it can't answer a question?", "answer": "Always offer an alternative path: 'That's a great question — let me connect you with one of our attorneys who can give you an accurate answer. Can I schedule a quick call?' Never let the conversation dead-end without an action for the visitor to take."},
          {"question": "How often should I review and update my chatbot scripts?", "answer": "Monthly, at minimum. Review conversation transcripts to identify questions the chatbot is not handling well, common topics callers raise that your script doesn't cover, and points where visitors drop off. Chatbot optimization is ongoing, not set-and-forget."},
        ],
        "related": ["ai-chatbot-for-law-firms", "chatbot-vs-live-chat-for-law-firms"],
      },
      {
        "slug": "chatbot-vs-live-chat-for-law-firms",
        "title": "Chatbot vs Live Chat for Law Firms: Which Converts More Clients?",
        "description": "AI chatbots and human live chat both capture leads — but they work differently. Here is how to choose the right approach for your law firm's size and goals.",
        "readTime": "9 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "60%", "label": "of legal inquiries arrive outside business hours"},
          {"value": "Live chat", "label": "converts 2.1x more during business hours"},
          {"value": "AI chatbot", "label": "captures 4x more after-hours leads than forms alone"},
        ],
        "blocks": [
          {"type": "h2", "heading": "Understanding the Trade-Offs", "text": "Understanding the Trade-Offs"},
          {"type": "p", "text": "Live chat — a real human responding to website messages in real time — outperforms AI chatbots when complex empathy and judgment are required. A caller describing a traumatic accident, a custody battle, or a criminal charge benefits from immediate human acknowledgment. However, live chat requires staffing during all active hours, creates response time problems when operators are busy, and is unavailable nights and weekends for most small firms."},
          {"type": "p", "text": "AI chatbots solve the availability problem but sacrifice some empathetic depth. The right answer for most firms is not a binary choice — it is a thoughtful combination of both."},
          {"type": "ul", "heading": "When to use each option", "items": [
            "AI chatbot: after-hours, overnight, weekends, and high-traffic overflow periods.",
            "Live chat: during core business hours when sensitive matters need human empathy.",
            "AI for qualification, human for closing: AI gathers info, then transfers to a live person.",
            "AI-only for high-volume firms: where 24/7 staff coverage is not cost-effective.",
          ]},
          {"type": "callout", "text": "The fastest-growing law firms use AI chatbots to ensure zero missed connections and live chat to maximize conversion on high-value interactions. Start with AI to capture every lead, then add live chat once you understand which interactions most benefit from human touch."},
        ],
        "faqs": [
          {"question": "Is live chat worth the staffing cost for a small law firm?", "answer": "For very small practices, a third-party live chat service (like Chat Agents or Ngage Legal) provides human operators for roughly $300–600/month — often more cost-effective than in-house staffing. Combined with an AI chatbot for after-hours, this hybrid approach works well for firms of any size."},
          {"question": "Can I transition from live chat to AI chatbot gradually?", "answer": "Yes. A common path: start with a live chat service, then use AI to handle overflow and after-hours. As you refine your chatbot scripts using real conversation data, gradually shift more interactions to AI while keeping humans for complex cases."},
          {"question": "What chat platform should law firms use?", "answer": "Popular platforms built for legal include LawDroid, Gideon, Intake.ai, and Tawk.to for live chat. For AI-specific legal chatbots, Smith.ai, LawDroid Copilot, and several newer AI-native platforms offer strong legal intake capabilities."},
        ],
        "related": ["ai-chatbot-for-law-firms", "law-firm-chatbot-best-practices"],
      },
    ],
  },
  {
    "slug": "law-firm-marketing",
    "name": "Law Firm Marketing",
    "description": "Modern legal marketing strategy for the AI era — client acquisition, brand building, and the tactics that drive sustainable growth for law firms.",
    "articles": [
      {
        "slug": "law-firm-marketing-in-the-age-of-ai",
        "title": "Law Firm Marketing in the Age of AI: What Has Changed and What Hasn't",
        "description": "AI has fundamentally changed how potential legal clients find, evaluate, and choose law firms. Here is what that means for your marketing strategy.",
        "readTime": "13 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "47%", "label": "of legal consumers now use AI before contacting a lawyer"},
          {"value": "3x", "label": "growth in AI-first legal searches since 2024"},
          {"value": "1st", "label": "firm to respond wins the engagement 78% of the time"},
        ],
        "blocks": [
          {"type": "h2", "heading": "The Client Journey Has Changed Fundamentally", "text": "The Client Journey Has Changed Fundamentally"},
          {"type": "p", "text": "For most of the last twenty years, the legal client acquisition journey looked like this: a potential client experienced a legal issue, typed some keywords into Google, visited a few websites, read some reviews, and called the firms that seemed most credible. Law firms invested in Google Ads, SEO, and review management to win at each of those stages."},
          {"type": "p", "text": "That journey still exists, but it now has a new first step for a growing percentage of prospects: asking an AI platform. Before they open Google, before they look at review sites, before they call anyone — they ask ChatGPT, Gemini, or Perplexity to explain their situation and tell them what to do. If your firm is referenced in that AI answer, you have already won a significant trust advantage before the client has even visited your website."},
          {"type": "callout", "text": "The marketing funnel now has a pre-funnel. Firms that earn AI citations capture prospects at the very beginning of their legal journey — before competitors even know the prospect exists."},
          {"type": "h2", "heading": "What Has Changed in Legal Marketing", "text": "What Has Changed in Legal Marketing"},
          {"type": "ul", "heading": "New realities in legal marketing", "items": [
            "AI platforms are the new first search for a growing segment of legal clients.",
            "Zero-click searches mean some prospects find your firm and call without ever visiting your website.",
            "AI citations function like referrals — they carry implicit trust from the platform.",
            "Content depth and entity authority now matter more than keyword density.",
            "Voice search has changed query formats — conversational questions, not short keywords.",
          ]},
          {"type": "h2", "heading": "What Has Not Changed", "text": "What Has Not Changed"},
          {"type": "p", "text": "The fundamentals of client acquisition have not changed: clients still choose lawyers they trust, with strong reputations, who are easy to reach, and who respond quickly. Excellent client service, strong reviews, community reputation, and referral networks remain as powerful as ever. The difference is in how clients first discover which firms to consider — and AI is increasingly the gateway to that discovery."},
        ],
        "faqs": [
          {"question": "Should law firms abandon traditional marketing for AI optimization?", "answer": "No. AI search optimization is additive, not a replacement. Traditional SEO, Google Ads, local directories, and referral networks remain highly effective. The firms winning in 2026 are adding AI visibility to their existing marketing stack — not replacing it."},
          {"question": "Which AI platform should law firms focus on first?", "answer": "Start where your target clients are. ChatGPT has the most users and broadest reach. Google Gemini is embedded in the search most people already use. Perplexity has a highly educated, research-oriented user base. All three matter — focus on the content quality and technical signals that help you on all platforms simultaneously."},
          {"question": "How do I measure whether my AI marketing is working?", "answer": "Track branded search volume in Google Search Console (AI citations drive direct searches), monitor your AI Overview appearances, manually query AI platforms for your target keywords monthly, and ask new clients how they first found your firm — many will mention AI platforms."},
        ],
        "related": ["legal-marketing-strategy-2026", "how-to-get-more-law-firm-leads"],
      },
      {
        "slug": "legal-marketing-strategy-2026",
        "title": "Legal Marketing Strategy 2026: The Complete Playbook for Growing Your Practice",
        "description": "A practical, up-to-date legal marketing strategy for law firms navigating AI search, changing client expectations, and an increasingly competitive landscape.",
        "readTime": "14 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "$143B", "label": "US legal services market"},
          {"value": "6%", "label": "annual growth driven by AI-enabled practices"},
          {"value": "Top 3", "label": "tactics: AI search, referrals, and Google reviews"},
        ],
        "blocks": [
          {"type": "h2", "heading": "The Four Pillars of Legal Marketing in 2026", "text": "The Four Pillars of Legal Marketing in 2026"},
          {"type": "ul", "heading": "Foundational pillars of modern legal marketing", "items": [
            "AI visibility: appearing in ChatGPT, Gemini, and Perplexity answers for your practice areas.",
            "Referral systems: systematizing how you generate and nurture referral relationships.",
            "Review management: building and maintaining a 4.8+ star presence across Google, Avvo, and Martindale.",
            "Intake optimization: ensuring every lead is captured, qualified, and followed up within minutes.",
          ]},
          {"type": "h2", "heading": "Building an AI-First Content Strategy", "text": "Building an AI-First Content Strategy"},
          {"type": "p", "text": "An AI-first content strategy starts with the questions your prospective clients actually ask AI platforms, not the keywords they historically typed into Google. These are longer, more conversational, and more specific. 'What happens if I'm found at fault in a car accident in Florida?' 'Do I need a lawyer to settle an estate in Ontario?' 'Can I be fired for refusing overtime in California?'"},
          {"type": "p", "text": "Map these questions to your practice areas, then create authoritative, jurisdiction-specific content that answers them directly. Each piece of content should have a clear structure, schema markup, and internal links to related content in the same practice area. Over time, this network of content builds the topical authority that earns AI citations."},
          {"type": "callout", "text": "Firms that invest in topical authority today are building a compounding asset. Each piece of content reinforces the others, and the combined signal becomes increasingly hard for competitors to replicate as the content library grows."},
          {"type": "h2", "heading": "The Referral System Most Law Firms Underestimate", "text": "The Referral System Most Law Firms Underestimate"},
          {"type": "p", "text": "Referrals remain the highest-trust, highest-conversion source of new business for most law firms. Yet most firms have no systematic approach to generating or nurturing them. A basic referral system — quarterly outreach to referring attorneys, a CRM that tracks referral sources, a clear mutual referral understanding with complementary practices — can double referral volume within 12 months with modest effort."},
        ],
        "faqs": [
          {"question": "What is the most cost-effective marketing channel for a small law firm?", "answer": "Referral development and Google review management offer the highest ROI for small firms. Combined with basic local SEO and a simple intake process, these three investments can sustainably grow a small practice without significant advertising spend."},
          {"question": "How important is social media for law firm marketing?", "answer": "It depends on the practice area and target client. Family law and estate planning firms often find LinkedIn and Facebook effective for reaching directly-hiring consumers. Business law and corporate practices find LinkedIn most relevant. Criminal defense firms often see limited social media ROI compared to search and referrals."},
          {"question": "Should law firms still invest in Google Ads?", "answer": "Yes, particularly for high-value practice areas with urgent need — personal injury, DUI, family law, immigration. Google Ads provide immediate visibility while organic and AI strategies build over time. The two approaches are complementary."},
        ],
        "related": ["law-firm-marketing-in-the-age-of-ai", "how-to-get-more-law-firm-leads"],
      },
      {
        "slug": "how-to-get-more-law-firm-leads",
        "title": "How to Get More Law Firm Leads: Proven Tactics That Work in 2026",
        "description": "A practical, tactics-focused guide to generating more qualified leads for your law firm — covering AI search, referrals, intake optimization, and paid channels.",
        "readTime": "12 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "5 min", "label": "response time that converts 80% more leads"},
          {"value": "9x", "label": "better odds of qualifying a lead contacted within 5 minutes"},
          {"value": "42%", "label": "of law firm calls go unanswered — every one is a lost lead"},
        ],
        "blocks": [
          {"type": "h2", "heading": "The Lead Generation Stack for Law Firms", "text": "The Lead Generation Stack for Law Firms"},
          {"type": "p", "text": "Sustainable lead generation for law firms requires multiple channels working simultaneously. Relying on a single source — Google Ads, a referral network, or organic traffic — creates dangerous fragility. The firms with the most predictable growth are running five to seven channels in parallel, so that changes in any one channel do not threaten the entire pipeline."},
          {"type": "ul", "heading": "Lead generation channels for law firms, ranked by ROI", "items": [
            "Attorney referrals — highest trust, best conversion rate, typically best value cases.",
            "Client referrals — existing clients are your most credible ambassadors.",
            "Google organic + AI citations — compounding investment that grows over time.",
            "Google Business Profile — local search and Google Maps visibility.",
            "Legal directories (Avvo, Martindale, FindLaw) — established traffic for legal queries.",
            "Google Ads — immediate visibility for high-intent, high-urgency queries.",
            "Content marketing and AI optimization — education-driven lead generation.",
          ]},
          {"type": "callout", "text": "Speed to response is often more important than which channel generated the lead. A lead contacted within 5 minutes of inquiry converts at dramatically higher rates than one reached hours later. Your intake process is a lead generation strategy."},
          {"type": "h2", "heading": "Fixing the Intake Leak Before Adding More Leads", "text": "Fixing the Intake Leak Before Adding More Leads"},
          {"type": "p", "text": "Before spending more on lead generation, audit your intake process. How quickly does your firm respond to new inquiries? What percentage of calls go unanswered? How many form submissions receive a response within one business day? Most law firms that are unhappy with their lead volume actually have a lead capture and response problem, not a traffic problem. Fix the leak before adding more water."},
        ],
        "faqs": [
          {"question": "How many leads should a law firm generate per month?", "answer": "This depends entirely on practice area, case value, and conversion rates. A personal injury firm might need 50 leads per month to close 5 cases worth $50,000 each. A business law firm might need 10 leads to close 2 retainers worth $30,000 each. Define your lead goal backward from your revenue target."},
          {"question": "What is the best way to get referrals from other attorneys?", "answer": "Systematize it. Identify 20 attorneys in complementary practice areas in your market. Reach out quarterly — not to ask for referrals, but to offer value: a useful article, an insight about their practice area, a referral of your own. Consistent, value-first outreach builds the relationships that generate referrals naturally over time."},
          {"question": "Should I list my firm on every legal directory?", "answer": "Focus on the directories with the most traffic in your practice area and market. For most US firms, priority order is: Avvo, Martindale-Hubbell, FindLaw, Justia, Lawyers.com, and your state bar directory. Claiming and fully completing profiles on these six will cover the majority of directory search volume."},
        ],
        "related": ["law-firm-marketing-in-the-age-of-ai", "legal-marketing-strategy-2026"],
      },
    ],
  },
  {
    "slug": "future-of-search",
    "name": "Future of Search for Law Firms",
    "description": "Search is becoming AI-first. Explore where legal marketing is heading, what AI-first search means for law firms, and how to build a durable advantage now.",
    "articles": [
      {
        "slug": "future-of-legal-search",
        "title": "The Future of Legal Search: What Law Firms Need to Know",
        "description": "AI-powered search is reshaping how potential clients find lawyers. Here is where legal search is heading over the next five years and what firms should do now.",
        "readTime": "12 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "2028", "label": "predicted year AI handles majority of initial legal research"},
          {"value": "60%", "label": "of searches already zero-click — AI accelerates this"},
          {"value": "5x", "label": "faster growth projected for AI-visible law firms"},
        ],
        "blocks": [
          {"type": "h2", "heading": "We Are in the Early Innings of an AI Search Revolution", "text": "We Are in the Early Innings of an AI Search Revolution"},
          {"type": "p", "text": "The shift to AI-powered search is not complete — it is accelerating. In 2024, AI Overviews were a novelty. In 2026, they appear on 40% of all Google searches. By 2028, industry analysts project that AI will handle the majority of initial information-gathering for legal questions, with human Google searches reserved primarily for navigational queries ('Smith Law Firm Toronto') and complex research tasks."},
          {"type": "p", "text": "For law firms, this trajectory has clear implications. The firms investing in AI visibility today are building an advantage that will compound over the next three to five years. The firms waiting for 'AI to mature before doing anything about it' are falling further behind every month."},
          {"type": "callout", "text": "The early adopters of Google SEO in the early 2000s built dominant positions that their competitors spent a decade trying to catch up to. AI search is a similar inflection point — and it is happening right now."},
          {"type": "h2", "heading": "Where AI Legal Search Is Headed", "text": "Where AI Legal Search Is Headed"},
          {"type": "ul", "heading": "Predictions for AI and legal search through 2030", "items": [
            "AI will increasingly recommend specific law firms by name for local queries.",
            "Voice-first legal search will become the norm for common legal questions.",
            "AI will pre-screen legal questions and route prospects to specialized attorneys automatically.",
            "Multi-turn AI conversations will replace single-query searches for complex legal matters.",
            "Firms with strong entity profiles and structured data will earn recommendation preference.",
            "Zero-click searches will eliminate traffic for generic legal content with no entity signals.",
          ]},
          {"type": "h2", "heading": "What Firms Should Do Right Now", "text": "What Firms Should Do Right Now"},
          {"type": "p", "text": "The actions that earn AI citations today are the same actions that will earn them in 2028 — they just become more valuable over time. Invest in entity authority by building and maintaining consistent profiles across legal directories. Implement complete schema markup on your website. Create comprehensive, jurisdiction-specific content that answers real client questions. These are durable investments that compound."},
        ],
        "faqs": [
          {"question": "Will AI replace Google for legal searches?", "answer": "AI will not replace Google — Google is becoming AI. The shift is from classic blue-link results to AI-generated answers. Google's AI Overviews are the clearest example: the same Google interface, with AI answers sitting above the traditional results."},
          {"question": "How will AI change the way law firms advertise?", "answer": "Paid advertising will remain relevant, but it will increasingly appear within AI-generated results rather than alongside traditional blue links. Google's ad strategy is already adapting to include ads within AI Overviews. Organic AI citations will become a primary traffic driver that paid advertising cannot fully replicate."},
          {"question": "Should law firms be worried about AI reducing demand for legal services?", "answer": "Not in the near term. AI can explain legal concepts and help people understand their options — but it cannot provide legal advice, represent clients, or make the judgment calls that attorneys are trained to make. AI is more likely to expand access to legal services by helping more people understand when they need a lawyer."},
        ],
        "related": ["ai-first-search-for-lawyers", "search-without-clicks-zero-click-search"],
      },
      {
        "slug": "ai-first-search-for-lawyers",
        "title": "AI-First Search: What It Means for Lawyers and Legal Marketing",
        "description": "AI-first search is not a future trend — it is the present reality for millions of legal searches. Here is what lawyers need to understand and do right now.",
        "readTime": "10 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "AI-first", "label": "is the default for Gen Z and Millennial legal research"},
          {"value": "73%", "label": "of users trust AI-cited sources more than organic results"},
          {"value": "Now", "label": "is the optimal time to begin AI-first optimization"},
        ],
        "blocks": [
          {"type": "h2", "heading": "Defining AI-First Search", "text": "Defining AI-First Search"},
          {"type": "p", "text": "AI-first search describes a search behavior where the user's first interaction with information about a topic comes through an AI platform — ChatGPT, Gemini, Perplexity — rather than a traditional search engine. The user types or speaks a complete question, receives a synthesized answer, and may or may not proceed to click through to a source."},
          {"type": "p", "text": "For lawyers, the significance is in what happens at the beginning of this process. If a prospect asks 'what should I do if I've been injured in a slip and fall in Seattle' and the AI answer references your firm as a trusted source or cites your content directly, you have captured mindshare before the prospect has ever seen your website. That is a qualitatively different kind of marketing than anything that existed before."},
          {"type": "h2", "heading": "Who Is Using AI for Legal Research?", "text": "Who Is Using AI for Legal Research?"},
          {"type": "p", "text": "Younger generations are the most enthusiastic AI-first searchers — but the behavior is spreading rapidly across all age groups. Research from 2025 shows that AI-first legal research is now common among users under 45, and growing among users 45-65. The practical implication: if your firm's most valuable clients are under 50, they are likely using AI platforms for initial legal research already."},
          {"type": "callout", "text": "The law firms that dismiss AI search because 'our clients are older and don't use ChatGPT' are making a bet that is becoming riskier by the quarter. The demographic adoption curve for AI tools is steep and accelerating."},
        ],
        "faqs": [
          {"question": "How do I know if my target clients are using AI search?", "answer": "Ask them. Include 'how did you first hear about us' and 'what resources did you use before contacting us' in your intake questions. You may be surprised how many clients mention ChatGPT, Gemini, or Perplexity — even if you've made no effort to optimize for these platforms."},
          {"question": "Is AI-first search more common in some practice areas than others?", "answer": "Yes. Complex, research-intensive areas like immigration, employment law, and estate planning see high AI-first usage because clients want to understand their situation before speaking to an attorney. Urgent, crisis-driven areas like DUI and personal injury see more direct calls — though AI is growing even there."},
          {"question": "Does AI-first search affect which keywords I should target?", "answer": "Yes, significantly. AI-first searchers use conversational, question-based queries rather than keyword phrases. Your content strategy should shift toward full questions and natural language answers, supplementing your existing keyword-optimized pages rather than replacing them."},
        ],
        "related": ["future-of-legal-search", "search-without-clicks-zero-click-search"],
      },
      {
        "slug": "search-without-clicks-zero-click-search",
        "title": "Zero-Click Search: What It Means for Law Firm Visibility",
        "description": "60% of searches end without a click. AI is accelerating this trend. Here is what zero-click search means for law firm traffic and how to adapt.",
        "readTime": "9 min read",
        "date": "2026-06-18",
        "stats": [
          {"value": "60%", "label": "of all searches are zero-click"},
          {"value": "AI Overviews", "label": "are the primary driver of zero-click legal searches"},
          {"value": "Citation", "label": "in the zero-click result is the new first-page ranking"},
        ],
        "blocks": [
          {"type": "h2", "heading": "What Is Zero-Click Search?", "text": "What Is Zero-Click Search?"},
          {"type": "p", "text": "A zero-click search is one where the user finds the answer they need directly on the search results page — or in an AI platform's response — without clicking through to any website. They ask a question, get an answer, and close the browser. No website visit, no traffic recorded, no conversion opportunity — at least, not in the traditional sense."},
          {"type": "p", "text": "For law firms that have built their digital marketing around website traffic metrics, zero-click search is a structural challenge. If a potential client asks Perplexity 'do I need a lawyer for a simple will in Alberta' and gets a direct answer, they may reach out to the firm cited in that answer — but the firm's website analytics will show zero traffic from that interaction."},
          {"type": "callout", "text": "In a zero-click world, brand awareness and citation visibility matter more than raw traffic numbers. Being the source that AI cites is worth more than being the website that ranks fifth — because the user who never clicks still forms an impression based on who the AI trusts."},
          {"type": "h2", "heading": "Adapting Your Strategy to a Zero-Click World", "text": "Adapting Your Strategy to a Zero-Click World"},
          {"type": "ul", "heading": "Strategic shifts for the zero-click era", "items": [
            "Measure AI citation frequency, not just website traffic.",
            "Track branded search volume — AI awareness drives direct searches.",
            "Optimize for citation as the primary metric, click-through as secondary.",
            "Build content that earns citation even when not clicked — accurate, citable summaries.",
            "Ensure your firm name and contact information appear in AI answers, not just links.",
            "Monitor offline attribution: clients who arrive through phone calls or direct visits after AI research.",
          ]},
        ],
        "faqs": [
          {"question": "Does zero-click search mean SEO is dead?", "answer": "No. SEO remains essential because AI systems draw from well-indexed, authoritative web content. But the goal of SEO is evolving — from generating clicks to earning citations and brand mentions. The firms treating citation as the KPI, not rank, are adapting correctly."},
          {"question": "How do I track zero-click visibility?", "answer": "Manual AI queries (checking ChatGPT, Gemini, Perplexity for your target keywords monthly), monitoring Google Search Console for impressions without clicks, tracking branded search volume trends, and asking new clients how they first encountered your firm."},
          {"question": "Is zero-click worse for small firms or large firms?", "answer": "It is worse for firms of any size that have not built AI visibility. For firms with strong AI citation presence, zero-click is actually an advantage — they gain brand awareness without having to earn a website visit. The penalty falls on firms that are invisible in AI answers."},
        ],
        "related": ["future-of-legal-search", "ai-first-search-for-lawyers"],
      },
    ],
  },
]

# ---------------------------------------------------------------------------
# Template functions
# ---------------------------------------------------------------------------

def make_data_ts(silo):
    """Generate data.ts content for a silo."""
    slug = silo["slug"]
    name = silo["name"]
    desc = silo["description"]
    articles = silo["articles"]

    lines = [
        'import type { ContentBlock, ArticleStat } from "@/app/insights/[category]/[slug]/content";',
        "",
        "export interface SiloArticle {",
        "  slug: string;",
        "  title: string;",
        "  description: string;",
        "  readTime: string;",
        "  date: string;",
        "  stats: ArticleStat[];",
        "  blocks: ContentBlock[];",
        "  faqs: { question: string; answer: string }[];",
        "  related: string[];",
        "}",
        "",
        "export const SILO_META = {",
        f'  name: {json_str(name)},',
        f'  description: {json_str(desc)},',
        f'  slug: {json_str(slug)},',
        "};",
        "",
        "export const ARTICLES: SiloArticle[] = [",
    ]

    for art in articles:
        lines.append("  {")
        lines.append(f'    slug: {json_str(art["slug"])},')
        lines.append(f'    title: {json_str(art["title"])},')
        lines.append(f'    description: {json_str(art["description"])},')
        lines.append(f'    readTime: {json_str(art["readTime"])},')
        lines.append(f'    date: {json_str(art["date"])},')
        lines.append("    stats: [")
        for s in art["stats"]:
            lines.append(f'      {{ value: {json_str(s["value"])}, label: {json_str(s["label"])} }},')
        lines.append("    ],")
        lines.append("    blocks: [")
        for b in art["blocks"]:
            block_parts = [f'type: {json_str(b["type"])}']
            if "heading" in b:
                block_parts.append(f'heading: {json_str(b["heading"])}')
            if "text" in b:
                block_parts.append(f'text: {json_str(b["text"])}')
            if "items" in b:
                items_str = ", ".join(json_str(i) for i in b["items"])
                block_parts.append(f'items: [{items_str}]')
            lines.append(f'      {{ {", ".join(block_parts)} }},')
        lines.append("    ],")
        lines.append("    faqs: [")
        for faq in art["faqs"]:
            lines.append(f'      {{ question: {json_str(faq["question"])}, answer: {json_str(faq["answer"])} }},')
        lines.append("    ],")
        lines.append(f'    related: [{", ".join(json_str(r) for r in art["related"])}],')
        lines.append("  },")

    lines.append("];")
    lines.append("")
    lines.append("export const ARTICLE_SLUGS = ARTICLES.map((a) => a.slug);")
    lines.append("")
    return "\n".join(lines)


def make_hub_page(silo):
    slug = silo["slug"]
    name = silo["name"]
    desc = silo["description"]
    title_full = f"{name}: Complete Guide for Law Firms"
    return f'''import Link from "next/link";
import {{ ArrowRight, Clock, Sparkles }} from "lucide-react";
import SchemaScript from "@/components/schema/SchemaScript";
import Button from "@/components/ui/Button";
import {{ generatePageMetadata }} from "@/lib/metadata";
import {{ webPageSchema, breadcrumbSchema, SITE_URL }} from "@/lib/schema";
import {{ SILO_META, ARTICLES }} from "./data";

export const metadata = generatePageMetadata({{
  title: {json_str(title_full)},
  slug: {json_str(slug)},
  description: {json_str(desc)},
}});

function formatDate(date: string): string {{
  return new Date(date).toLocaleDateString("en-US", {{
    year: "numeric",
    month: "long",
    day: "numeric",
  }});
}}

export default function SiloHubPage() {{
  return (
    <>
      <SchemaScript
        schema={{webPageSchema(
          {json_str(title_full)},
          SILO_META.description,
          `${{SITE_URL}}/${{SILO_META.slug}}`
        )}}
      />
      <SchemaScript
        schema={{breadcrumbSchema([
          {{ name: "Home", url: SITE_URL }},
          {{ name: SILO_META.name, url: `${{SITE_URL}}/${{SILO_META.slug}}` }},
        ])}}
      />

      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[1100px] px-6 py-24 text-center md:px-10">
          <span className="mb-5 inline-flex items-center gap-2 rounded-full border border-pu/30 bg-pu/10 px-4 py-1.5 text-[12px] font-bold uppercase tracking-wide text-pu3">
            <Sparkles size={{14}} /> {{SILO_META.name}}
          </span>
          <h1 className="mx-auto max-w-[820px] text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight text-white">
            {{SILO_META.name}}{{" "}}
            <span className="text-grad-gold">for Law Firms</span>
          </h1>
          <p className="mx-auto mt-6 max-w-[640px] text-[17px] leading-relaxed text-slate-300">
            {{SILO_META.description}}
          </p>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="mb-12 text-center">
            <h2 className="text-[clamp(24px,3vw,36px)] font-extrabold tracking-tight text-navy">
              {{ARTICLES.length}} in-depth guides for law firms
            </h2>
          </div>
          <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-2">
            {{ARTICLES.map((article) => (
              <Link
                key={{article.slug}}
                href={{`/${{SILO_META.slug}}/${{article.slug}}`}}
                className="group flex flex-col rounded-2xl border border-pu/10 bg-white p-7 shadow-[0_6px_28px_rgba(11,21,54,.08)] transition-all hover:-translate-y-1 hover:border-pu/40"
              >
                <div className="mb-4 flex items-center gap-3">
                  <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-pu/10 text-pu">
                    <Sparkles size={{18}} />
                  </div>
                  <div className="flex items-center gap-2 text-[12px] text-slate-400">
                    <Clock size={{12}} />
                    <span>{{article.readTime}}</span>
                    <span className="mx-1">·</span>
                    <span>{{formatDate(article.date)}}</span>
                  </div>
                </div>
                <h2 className="mb-2 text-[18px] font-extrabold leading-snug tracking-tight text-navy transition-colors group-hover:text-pu">
                  {{article.title}}
                </h2>
                <p className="flex-1 text-[14px] leading-relaxed text-slate-600">
                  {{article.description}}
                </p>
                <span className="mt-5 inline-flex items-center gap-1.5 text-[13px] font-bold text-pu">
                  Read guide
                  <ArrowRight
                    size={{15}}
                    className="transition-transform group-hover:translate-x-1"
                  />
                </span>
                <div className="mt-5 h-1 w-full rounded-full bg-gradient-to-r from-pu to-pu2 opacity-70" />
              </Link>
            ))}}
          </div>
        </div>
      </section>

      <section className="bg-slate-50/60">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="rounded-3xl border border-pu/10 bg-gradient-to-br from-navy to-navy/90 p-10 text-center text-white shadow-[0_12px_40px_rgba(11,21,54,.2)]">
            <h2 className="mx-auto max-w-[600px] text-[clamp(24px,3vw,36px)] font-extrabold leading-tight tracking-tight">
              See Where Your Firm Stands in AI Search
            </h2>
            <p className="mx-auto mt-4 max-w-[480px] text-[16px] leading-relaxed text-slate-300">
              Get a free AI visibility check and find out exactly how AI platforms describe and cite your firm.
            </p>
            <div className="mt-8 flex flex-wrap items-center justify-center gap-4">
              <Button variant="gold" size="lg" href="/tools/ai-visibility-checker">
                Check My AI Visibility Free
                <ArrowRight size={{18}} className="ml-2" />
              </Button>
            </div>
          </div>
        </div>
      </section>
    </>
  );
}}
'''


def make_article_page(silo):
    slug_var = silo["slug"]
    name = silo["name"]
    return f'''import {{ notFound }} from "next/navigation";
import SchemaScript from "@/components/schema/SchemaScript";
import {{ generatePageMetadata }} from "@/lib/metadata";
import {{ articleSchema, breadcrumbSchema, faqSchema, SITE_URL }} from "@/lib/schema";
import {{ SILO_META, ARTICLES, ARTICLE_SLUGS }} from "../data";
import ArticleClient from "@/app/insights/[category]/[slug]/ArticleClient";

export function generateStaticParams() {{
  return ARTICLE_SLUGS.map((slug) => ({{ slug }}));
}}

export async function generateMetadata({{
  params,
}}: {{
  params: Promise<{{ slug: string }}>;
}}) {{
  const {{ slug }} = await params;
  const article = ARTICLES.find((a) => a.slug === slug);
  if (!article) return {{}};
  return generatePageMetadata({{
    title: article.title,
    slug: `${{SILO_META.slug}}/${{slug}}`,
    description: article.description,
    type: "article",
    publishedAt: article.date,
  }});
}}

export default async function SiloArticlePage({{
  params,
}}: {{
  params: Promise<{{ slug: string }}>;
}}) {{
  const {{ slug }} = await params;
  const article = ARTICLES.find((a) => a.slug === slug);
  if (!article) notFound();

  const url = `${{SITE_URL}}/${{SILO_META.slug}}/${{slug}}`;
  const related = article.related
    .map((s) => ARTICLES.find((a) => a.slug === s))
    .filter(Boolean)
    .map((a) => ({{ title: a!.title, href: `/${{SILO_META.slug}}/${{a!.slug}}` }}));

  return (
    <>
      <SchemaScript
        schema={{articleSchema(
          article.title,
          article.description,
          url,
          article.date,
          "LexScale Editorial"
        )}}
      />
      <SchemaScript
        schema={{breadcrumbSchema([
          {{ name: "Home", url: SITE_URL }},
          {{ name: SILO_META.name, url: `${{SITE_URL}}/${{SILO_META.slug}}` }},
          {{ name: article.title, url }},
        ])}}
      />
      <SchemaScript schema={{faqSchema(article.faqs)}} />
      <ArticleClient
        title={{article.title}}
        category={{SILO_META.name}}
        categoryHref={{`/${{SILO_META.slug}}`}}
        description={{article.description}}
        readTime={{article.readTime}}
        date={{article.date}}
        stats={{article.stats}}
        blocks={{article.blocks}}
        faqs={{article.faqs}}
        related={{related}}
      />
    </>
  );
}}
'''


import json

def json_str(s):
    return json.dumps(str(s))


# ---------------------------------------------------------------------------
# Write files
# ---------------------------------------------------------------------------
created = []

for silo in SILOS:
    s = silo["slug"]
    base = os.path.join(ROOT, s)
    slug_dir = os.path.join(base, "[slug]")

    os.makedirs(slug_dir, exist_ok=True)

    data_path = os.path.join(base, "data.ts")
    with open(data_path, "w") as f:
        f.write(make_data_ts(silo))
    created.append(data_path)

    hub_path = os.path.join(base, "page.tsx")
    with open(hub_path, "w") as f:
        f.write(make_hub_page(silo))
    created.append(hub_path)

    art_path = os.path.join(slug_dir, "page.tsx")
    with open(art_path, "w") as f:
        f.write(make_article_page(silo))
    created.append(art_path)

print(f"Created {len(created)} files:")
for p in created:
    print(" ", p.replace(ROOT + "/", ""))
