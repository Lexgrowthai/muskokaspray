# LexScale.ai Build Reference (for sub-agents)

DELETE-able after build. Shared conventions for all pages.

## Design tokens (Tailwind v4 — colors registered in app/globals.css @theme)
Use these Tailwind color utilities directly: `navy` (#0B1536), `pu` (#6A5CFF), `pu2` (#8B7FFF), `pu3` (#a89fff), `gold` (#D4AF37), `gold2` (#F0C040), `gold3` (#b8962e).
- Examples: `bg-navy`, `text-pu`, `border-pu/10`, `bg-pu/8`, `from-pu to-pu2`.
- Helper classes in globals.css: `.hero-gradient` (dark navy hero bg), `.grid-bg` (subtle grid overlay), `.text-grad-gold`, `.text-grad-purple`.
- Font is Inter, applied globally. Body text color is navy.

## Layout conventions
- Page sections: wrap content in `<section>` then an inner `<div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">`.
- Dark hero sections: `<section className="hero-gradient relative overflow-hidden">` with `<div className="grid-bg absolute inset-0 opacity-40" />` and content in a relative z-10 container. Hero text is WHITE on dark.
- Headline: `text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight`.
- Section title: `text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy`.
- Cards on white: `rounded-2xl border border-pu/10 bg-white p-7 shadow-[0_6px_28px_rgba(11,21,54,.08)]`.

## Shared components (import with @/ alias)
- `import Button from "@/components/ui/Button"` — props: variant ('primary'|'gold'|'outline'|'ghost'), size ('sm'|'md'|'lg'), `href` (renders Link) OR onClick. e.g. `<Button href="/services" variant="primary" size="lg">Text</Button>`
- `import Tag from "@/components/ui/Tag"` — variant ('purple'|'gold'|'blue'|'green'). `<Tag variant="purple">LABEL</Tag>`
- `import Card from "@/components/ui/Card"` — variant ('default'|'dark'|'gold'), hover bool.
- `import FAQ from "@/components/sections/FAQ"` — `<FAQ faqs={[{question,answer}]} title="..." />` ('use client', injects FAQ schema). Use in server pages directly.
- `import StickyCTA from "@/components/sections/StickyCTA"` — 'use client'. props: message, ctaText, onCtaClick.
- `import LeadFormModal from "@/components/sections/LeadFormModal"` — 'use client'. props: isOpen, onClose, offer, title, description.
- `import SchemaScript from "@/components/schema/SchemaScript"` — `<SchemaScript schema={...} />` renders JSON-LD.
- `import Breadcrumb from "@/components/layout/Breadcrumb"` — auto from pathname.

## Metadata & schema (import with @/ alias)
- `import { generatePageMetadata } from "@/lib/metadata"` — returns Metadata. Call in `export const metadata` or `generateMetadata`.
  `generatePageMetadata({ title, description, slug, type?, publishedAt? })` — slug is path WITHOUT leading slash, e.g. "services/ai-seo".
- `import { serviceSchema, articleSchema, faqSchema, webPageSchema, SITE_URL } from "@/lib/schema"`.

## IMPORTANT RULES
1. Pages that use StickyCTA/LeadFormModal/onClick state MUST be split: keep the page.tsx as a server component with `export const metadata`, and put interactive parts in a sibling `'use client'` component (e.g. `PageClient.tsx`) imported into the page. SchemaScript and FAQ can render inside server pages.
   - Simplest pattern: page.tsx (server) exports metadata + renders <SchemaScript/> + a client component that holds the StickyCTA/modal wiring and all visual content.
2. Every page MUST `export const metadata = generatePageMetadata({...})` (static) OR `export async function generateMetadata()`. Dynamic [param] pages use generateMetadata.
3. Service pages: include `<SchemaScript schema={serviceSchema(name, description, SITE_URL + "/services/slug")} />`.
4. Use Tailwind classes; avoid inline styles except dynamic values (calculators, accordions).
5. All content must be real and complete — NO placeholder comments.
6. Use absolute-style internal links matching the route map.
7. Do NOT create layout.tsx/Nav/Footer — already done. Breadcrumb is added via section layout.tsx files.

## Route map
/ , /about , /services , /services/{ai-websites,ai-seo,ai-search-optimization,chatgpt-optimization,gemini-optimization,perplexity-optimization,entity-seo,structured-data,ai-chatbots,ai-receptionists,ai-dashboards,ai-citation-tracking}
/insights , /insights/[category] , /insights/[category]/[slug]
/tools , /tools/{ai-visibility-checker,missed-call-calculator,roi-calculator}
/case-studies , /case-studies/[slug]
/resources , /resources/{faq,glossary,guides,comparisons} , /resources/glossary/[term]

## Brand facts (use consistently)
- Founded 2013. Serves law firms in US & Canada.
- Headline stats: 4,800+ Leads Generated, 432% Avg Traffic Increase, 3,200+ Calls Generated, $12M+ Revenue Added.
- Tagline: "AI Growth Systems For Law Firms".
- Primary CTA: "Get a Free Strategy Call" -> /tools/ai-visibility-checker.
