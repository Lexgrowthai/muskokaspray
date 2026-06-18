export interface NavDropdownItem {
  label: string;
  href: string;
  description: string;
  iconName?: string;
}

export interface NavItem {
  label: string;
  href?: string;
  dropdown?: NavDropdownItem[];
  columns?: number;
}

export const SERVICES_ITEMS: NavDropdownItem[] = [
  {
    label: "AI Websites",
    href: "/services/ai-websites",
    description: "Conversion-built sites for law firms",
    iconName: "Globe",
  },
  {
    label: "AI SEO",
    href: "/services/ai-seo",
    description: "Rank for high-intent legal searches",
    iconName: "Search",
  },
  {
    label: "AI Search Optimization",
    href: "/services/ai-search-optimization",
    description: "Win answers across every AI engine",
    iconName: "Sparkles",
  },
  {
    label: "ChatGPT Optimization",
    href: "/services/chatgpt-optimization",
    description: "Get cited inside ChatGPT answers",
    iconName: "MessageSquare",
  },
  {
    label: "Gemini Optimization",
    href: "/services/gemini-optimization",
    description: "Visibility in Google Gemini & AI Overviews",
    iconName: "Stars",
  },
  {
    label: "Perplexity Optimization",
    href: "/services/perplexity-optimization",
    description: "Become a Perplexity source",
    iconName: "Compass",
  },
  {
    label: "Entity SEO",
    href: "/services/entity-seo",
    description: "Build your firm as a known entity",
    iconName: "Network",
  },
  {
    label: "Structured Data",
    href: "/services/structured-data",
    description: "Schema markup AI engines trust",
    iconName: "Code2",
  },
  {
    label: "AI Chatbots",
    href: "/services/ai-chatbots",
    description: "24/7 intake that converts visitors",
    iconName: "Bot",
  },
  {
    label: "AI Receptionists",
    href: "/services/ai-receptionists",
    description: "Never miss another client call",
    iconName: "PhoneCall",
  },
  {
    label: "AI Dashboards",
    href: "/services/ai-dashboards",
    description: "See every lead, call, and dollar",
    iconName: "LayoutDashboard",
  },
  {
    label: "AI Citation Tracking",
    href: "/services/ai-citation-tracking",
    description: "Track where AI mentions your firm",
    iconName: "Quote",
  },
];

export const INSIGHTS_ITEMS: NavDropdownItem[] = [
  {
    label: "ChatGPT",
    href: "/insights/chatgpt",
    description: "Winning visibility inside ChatGPT",
  },
  {
    label: "Gemini",
    href: "/insights/gemini",
    description: "Google Gemini & AI Overviews",
  },
  {
    label: "Perplexity",
    href: "/insights/perplexity",
    description: "The answer engine for research",
  },
  {
    label: "AI Overviews",
    href: "/insights/ai-overviews",
    description: "Google's AI answer boxes",
  },
  {
    label: "Entity SEO",
    href: "/insights/entity-seo",
    description: "Entities, not just keywords",
  },
  {
    label: "Structured Data",
    href: "/insights/structured-data",
    description: "Schema strategy for law firms",
  },
  {
    label: "Semantic Search",
    href: "/insights/semantic-search",
    description: "Meaning-based ranking",
  },
  {
    label: "GEO",
    href: "/insights/geo",
    description: "Generative engine optimization",
  },
  {
    label: "Knowledge Graphs",
    href: "/insights/knowledge-graphs",
    description: "How AI maps your firm",
  },
  {
    label: "Voice Search",
    href: "/insights/voice-search",
    description: "Optimizing for spoken queries",
  },
  {
    label: "Future of Search",
    href: "/insights/future-of-search",
    description: "Where legal marketing is heading",
  },
];

export const TOOLS_ITEMS: NavDropdownItem[] = [
  {
    label: "AI Visibility Checker",
    href: "/tools/ai-visibility-checker",
    description: "See how AI engines rank your firm",
    iconName: "ScanSearch",
  },
  {
    label: "Missed Call Calculator",
    href: "/tools/missed-call-calculator",
    description: "Revenue lost to missed calls",
    iconName: "PhoneMissed",
  },
  {
    label: "ROI Calculator",
    href: "/tools/roi-calculator",
    description: "Project your growth ROI",
    iconName: "TrendingUp",
  },
  {
    label: "Schema Generator",
    href: "/tools/ai-visibility-checker",
    description: "Generate legal schema markup",
    iconName: "Code2",
  },
  {
    label: "Keyword Explorer",
    href: "/tools/ai-visibility-checker",
    description: "Find high-intent legal queries",
    iconName: "Search",
  },
  {
    label: "Citation Audit",
    href: "/tools/ai-visibility-checker",
    description: "Audit your AI citations",
    iconName: "Quote",
  },
];

export const RESOURCES_ITEMS: NavDropdownItem[] = [
  {
    label: "FAQ",
    href: "/resources/faq",
    description: "Answers to common questions",
    iconName: "HelpCircle",
  },
  {
    label: "Glossary",
    href: "/resources/glossary",
    description: "AI search terms, explained",
    iconName: "BookOpen",
  },
  {
    label: "Guides",
    href: "/resources/guides",
    description: "Deep-dive playbooks",
    iconName: "FileText",
  },
  {
    label: "Comparisons",
    href: "/resources/comparisons",
    description: "Side-by-side breakdowns",
    iconName: "GitCompare",
  },
];

export const NAV_ITEMS: NavItem[] = [
  { label: "Home", href: "/" },
  { label: "Services", dropdown: SERVICES_ITEMS, columns: 2 },
  { label: "Insights", dropdown: INSIGHTS_ITEMS },
  { label: "Tools", dropdown: TOOLS_ITEMS },
  { label: "Case Studies", href: "/case-studies" },
  { label: "Resources", dropdown: RESOURCES_ITEMS },
  { label: "About", href: "/about" },
];
