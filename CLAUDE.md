# LexScale.ai — Developer Rules

## SEO IS NOT OPTIONAL

Every page created for this project must ship with complete backend SEO. A page is not finished until both content AND technical SEO are done. No exceptions.

---

## Required on Every Page

### 1. Metadata — use `generatePageMetadata()`

```ts
import { generatePageMetadata } from "@/lib/metadata";

export const metadata = generatePageMetadata({
  title: "Unique Page Title",           // No site name — template adds it
  description: "Unique 140-160 char description with primary keyword.",
  slug: "path/to/page",                 // No leading slash
  type: "website",                      // "article" for blog/insights posts
  publishedAt: "2026-01-15",            // Only for articles
});
```

This automatically generates: title tag, meta description, canonical URL, Open Graph, Twitter card, robots directives, and googleBot hints.

### 2. JSON-LD Schema — inject via `<SchemaScript>`

```tsx
import SchemaScript from "@/components/schema/SchemaScript";
import { breadcrumbSchema, webPageSchema, SITE_URL } from "@/lib/schema";

// Always include at minimum:
<SchemaScript schema={webPageSchema(title, description, `${SITE_URL}/path`)} />
<SchemaScript schema={breadcrumbSchema([
  { name: "Home", url: SITE_URL },
  { name: "Parent Section", url: `${SITE_URL}/parent` },
  { name: "This Page", url: `${SITE_URL}/parent/this-page` },
])} />
```

**Additional schemas by page type:**

| Page type | Schema to add |
|---|---|
| Service page | `serviceSchema(name, description, url)` |
| Blog / article | `articleSchema(title, desc, url, date, author)` |
| Page with FAQ section | Use `<FAQ faqs={faqs} />` — it auto-injects FAQPage schema |
| Free tool / app | `softwareApplicationSchema(name, desc, url)` |
| Root / hub page | `webPageSchema()` + breadcrumb |

All schema builders live in `/lib/schema.ts`. Add new ones there, never inline.

### 3. H1/H2/H3 Hierarchy

- **Exactly one H1** per page — the primary keyword phrase
- **H2** for major sections (What We Do, How It Works, FAQ, etc.)
- **H3** for subsection headings or card titles
- Never skip levels (H1 → H3 without H2)

### 4. Internal Links

Every page must link to at least 2–3 related pages:
- Back to the parent section (e.g., `/services` on a service page)
- At least one related service, article, or tool
- A CTA link to `/tools/ai-visibility-checker` or `/case-studies`

### 5. Image Alt Text

Every `<img>` and Next.js `<Image>` must have a descriptive `alt` attribute:
- Describe what the image shows, not "image" or "photo"
- Include the primary keyword where natural
- Decorative images: `alt=""`

### 6. Mobile-First Structure

- No fixed widths that break below 375px
- Use `px-4 sm:px-6 lg:px-8` padding patterns
- Touch targets minimum 44×44px
- Font size minimum 14px

---

## Page Template (copy-paste starting point)

```tsx
import { generatePageMetadata } from "@/lib/metadata";
import {
  webPageSchema,
  breadcrumbSchema,
  serviceSchema,   // swap for articleSchema / softwareApplicationSchema as needed
  SITE_URL,
} from "@/lib/schema";
import SchemaScript from "@/components/schema/SchemaScript";
import Button from "@/components/ui/Button";
import Tag from "@/components/ui/Tag";
import FAQ from "@/components/sections/FAQ";

const NAME = "Page Title Here";
const DESCRIPTION = "140–160 character meta description with primary keyword.";
const URL = `${SITE_URL}/path/to/page`;

export const metadata = generatePageMetadata({
  title: NAME,
  description: DESCRIPTION,
  slug: "path/to/page",
});

const faqs = [
  { question: "...", answer: "..." },
];

export default function PageName() {
  return (
    <>
      {/* Schema — all injected server-side */}
      <SchemaScript schema={webPageSchema(NAME, DESCRIPTION, URL)} />
      <SchemaScript schema={serviceSchema(NAME, DESCRIPTION, URL)} />
      <SchemaScript
        schema={breadcrumbSchema([
          { name: "Home", url: SITE_URL },
          { name: "Parent", url: `${SITE_URL}/parent` },
          { name: NAME, url: URL },
        ])}
      />

      {/* H1 — exactly one per page */}
      <section className="hero-gradient py-24 px-6 text-center relative overflow-hidden">
        <div className="grid-bg absolute inset-0" />
        <div className="relative z-10 max-w-3xl mx-auto">
          <Tag variant="purple" className="mb-5">Category Label</Tag>
          <h1 className="text-4xl md:text-6xl font-black text-white leading-tight tracking-tight mb-5">
            Primary Keyword <span className="text-grad-purple">Phrase Here</span>
          </h1>
          <p className="text-lg text-white/60 leading-relaxed mb-8 max-w-2xl mx-auto">
            {DESCRIPTION}
          </p>
          <div className="flex gap-4 justify-center flex-wrap">
            <Button href="/tools/ai-visibility-checker" variant="primary" size="lg">
              Primary CTA
            </Button>
            <Button href="/services" variant="outline" size="lg">
              Secondary CTA
            </Button>
          </div>
        </div>
      </section>

      {/* H2 sections */}
      <section className="py-20 px-6 bg-white">
        <div className="max-w-5xl mx-auto">
          <h2 className="text-3xl font-black text-navy tracking-tight mb-4">
            Section Heading
          </h2>
          {/* content */}
        </div>
      </section>

      {/* FAQ — auto-injects FAQPage JSON-LD */}
      <section className="py-20 px-6 bg-white">
        <div className="max-w-3xl mx-auto">
          <h2 className="text-3xl font-black text-navy tracking-tight mb-10 text-center">
            Common Questions
          </h2>
          <FAQ faqs={faqs} />
        </div>
      </section>
    </>
  );
}
```

---

## Checklist Before Marking Any Page Done

- [ ] `generatePageMetadata()` called with unique title + description + slug
- [ ] `webPageSchema()` injected
- [ ] `breadcrumbSchema()` injected with correct hierarchy
- [ ] Page-type schema injected (service / article / softwareApp)
- [ ] Exactly one `<h1>` on the page
- [ ] H2s used for all major sections
- [ ] H3s used for card/item titles (never as first-level section)
- [ ] At least 2 internal links to related pages
- [ ] All images have descriptive `alt` text
- [ ] Mobile layout tested at 375px
- [ ] Page renders with no TypeScript errors (`npm run build` passes)

---

## Available Schema Builders (`/lib/schema.ts`)

| Function | Use for |
|---|---|
| `organizationSchema()` | Root layout only (already in place) |
| `websiteSchema()` | Root layout only (already in place) |
| `webPageSchema(name, desc, url)` | Every page |
| `breadcrumbSchema(items[])` | Every page (except homepage) |
| `serviceSchema(name, desc, url)` | All service pages |
| `articleSchema(title, desc, url, date, author)` | All insights/blog articles |
| `faqSchema(faqs[])` | Auto-called by `<FAQ>` component — do not call manually |
| `softwareApplicationSchema(name, desc, url)` | Tool/app pages |

---

## File Locations

```
/lib/metadata.ts          → generatePageMetadata() factory
/lib/schema.ts            → all JSON-LD builders + SITE_URL
/components/schema/SchemaScript.tsx  → server component that renders <script type="application/ld+json">
/components/sections/FAQ.tsx         → auto-injects FAQPage schema
/components/ui/Button.tsx            → primary/gold/outline/ghost variants
/components/ui/Tag.tsx               → purple/gold/blue label chips
```
