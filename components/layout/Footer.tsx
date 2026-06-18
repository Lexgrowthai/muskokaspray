import Link from "next/link";

const COLUMNS: { title: string; links: { label: string; href: string }[] }[] = [
  {
    title: "Services",
    links: [
      { label: "AI Search Optimization", href: "/services/ai-search-optimization" },
      { label: "AI SEO", href: "/services/ai-seo" },
      { label: "AI Websites", href: "/services/ai-websites" },
      { label: "AI Chatbots", href: "/services/ai-chatbots" },
      { label: "AI Receptionists", href: "/services/ai-receptionists" },
      { label: "All Services", href: "/services" },
    ],
  },
  {
    title: "Insights",
    links: [
      { label: "ChatGPT", href: "/insights/chatgpt" },
      { label: "Gemini", href: "/insights/gemini" },
      { label: "Perplexity", href: "/insights/perplexity" },
      { label: "AI Overviews", href: "/insights/ai-overviews" },
      { label: "Entity SEO", href: "/insights/entity-seo" },
      { label: "All Insights", href: "/insights" },
    ],
  },
  {
    title: "Resources",
    links: [
      { label: "Glossary", href: "/resources/glossary" },
      { label: "Guides", href: "/resources/guides" },
      { label: "FAQ", href: "/resources/faq" },
      { label: "Comparisons", href: "/resources/comparisons" },
    ],
  },
  {
    title: "Company",
    links: [
      { label: "About", href: "/about" },
      { label: "Contact", href: "/tools/ai-visibility-checker" },
      { label: "Privacy", href: "/about" },
      { label: "Terms", href: "/about" },
    ],
  },
];

export default function Footer() {
  return (
    <footer className="bg-[#04070f] px-6 py-14 md:px-10">
      <div className="mx-auto max-w-[1100px]">
        <div className="grid gap-10 md:grid-cols-[1.4fr_repeat(4,1fr)]">
          <div>
            <div className="text-[18px] font-extrabold tracking-[-0.4px] text-white">
              Lex<span className="text-pu">Scale</span>.ai
            </div>
            <p className="mt-2 max-w-[220px] text-[12px] leading-relaxed text-white/30">
              AI Growth Systems For Law Firms
            </p>
          </div>
          {COLUMNS.map((col) => (
            <div key={col.title}>
              <h4 className="mb-4 text-[12px] font-bold uppercase tracking-[0.7px] text-white/50">
                {col.title}
              </h4>
              <ul className="flex flex-col gap-2.5">
                {col.links.map((link) => (
                  <li key={link.label}>
                    <Link
                      href={link.href}
                      className="text-[12px] font-medium text-white/35 transition-colors hover:text-pu3"
                    >
                      {link.label}
                    </Link>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        <div className="mt-12 flex flex-col items-center justify-between gap-4 border-t border-white/[0.08] pt-6 sm:flex-row">
          <p className="text-[11px] text-white/25">
            © {new Date().getFullYear()} LexScale.ai. All rights reserved.
          </p>
          <p className="text-[11px] text-white/25">
            Built with AI · Optimized for AI
          </p>
        </div>
      </div>
    </footer>
  );
}
