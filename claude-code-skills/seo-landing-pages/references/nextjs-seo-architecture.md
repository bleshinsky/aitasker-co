# Next.js SEO Architecture Patterns

Implementation patterns for building SEO-optimized pages in Next.js App Router.
All patterns assume Next.js 15 with the App Router (where `params` is a
`Promise` that must be awaited).

## Server Component Pattern (Non-Negotiable)

The page component must be a server component. `generateMetadata()` only works
in server components. A page with `"use client"` at the top cannot set dynamic
meta tags — making it invisible to search engines.

### Correct Structure

```typescript
// app/categories/[slug]/[taskType]/page.tsx
// NO "use client" directive

import type { Metadata } from "next";

export async function generateStaticParams() {
  return getAllSlugs(); // SSG at build time
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string; taskType: string }>;
}): Promise<Metadata> {
  const { slug, taskType } = await params;
  const data = getPageData(slug, taskType);
  if (!data) return { title: "Not Found" };

  const url = `https://example.com/categories/${slug}/${taskType}`;

  return {
    title: data.seo.title,
    description: data.seo.description,
    keywords: data.seo.keywords,
    openGraph: {
      title: data.hero.h1,
      description: data.seo.description,
      type: "website",
      url,
      images: [{ url: "https://example.com/og/image.png", width: 1200, height: 630 }],
    },
    twitter: { card: "summary_large_image" },
    alternates: { canonical: url },
  };
}

export default async function Page({ params }: { params: Promise<...> }) {
  const { slug, taskType } = await params;
  const data = getPageData(slug, taskType);
  if (!data) notFound();

  return <main>...</main>;
}
```

### Client Component Composition

For interactive elements (animations, accordions), extract small client
wrappers and compose them inside the server page:

```typescript
// components/ui/RevealClient.tsx
"use client";

import { useRef, useEffect, useState, type ReactNode } from "react";

export function RevealClient({
  children,
  className = "",
  delay = 0,
}: {
  children: ReactNode;
  className?: string;
  delay?: number;
}) {
  const ref = useRef<HTMLDivElement>(null);
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    const obs = new IntersectionObserver(
      ([entry]) => { if (entry.isIntersecting) setVisible(true); },
      { threshold: 0.06, rootMargin: "0px 0px -40px 0px" },
    );
    obs.observe(el);
    return () => obs.disconnect();
  }, []);

  return (
    <div
      ref={ref}
      className={`transition-all duration-700 ease-[cubic-bezier(0.16,1,0.3,1)] ${
        visible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-12"
      } ${className}`}
      style={{ transitionDelay: `${delay}ms` }}
    >
      {children}
    </div>
  );
}
```

Use in the server page:
```tsx
<RevealClient delay={100}>
  <div>Server-rendered content with client-side animation</div>
</RevealClient>
```

The page shell renders fully on the server. Only the animation behavior
hydrates on the client.

## Data-Driven Architecture

### Static Data File Pattern

Store all page content in a TypeScript file co-located with other data:

```
lib/
├── category-pages.ts      // Category hub data
├── task-type-pages.ts     // Task type page data (NEW)
└── task-type-index.ts     // Search index
```

The data file exports:
1. **Interface** — type-safe shape for all page variants
2. **Data array** — all page entries
3. **Lookup functions** — find by slug, list all, filter by category

```typescript
export interface PageData {
  slug: string;
  categorySlug: string;
  seo: { title: string; description: string; keywords: string[] };
  hero: { h1: string; tagline: string; ctaText: string; stats: Stats };
  // ... all section data
}

export const PAGES: PageData[] = [
  { slug: "n8n-workflow", categorySlug: "automation-workflows", ... },
];

export function getPageData(catSlug: string, typeSlug: string) {
  return PAGES.find(p => p.categorySlug === catSlug && p.slug === typeSlug);
}

export function getAllSlugs() {
  return PAGES.map(p => ({ slug: p.categorySlug, taskType: p.slug }));
}
```

### Why Static Data Files

- **SSG-compatible** — `generateStaticParams()` can read them at build time
- **Type-safe** — TypeScript catches missing fields
- **Version-controlled** — every content change is a git diff
- **No CMS dependency** — no API calls, no runtime failures
- **SEO improvements = data edits** — change an H2 without touching the component

## JSON-LD Injection Pattern

Render JSON-LD as `<script>` tags in the server component:

```tsx
const jsonLd = { "@context": "https://schema.org", "@type": "Product", ... };

return (
  <main>
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
    />
    {/* Page content */}
  </main>
);
```

Place JSON-LD scripts at the top of `<main>`, before visible content. Google
finds them regardless of position, but top placement makes auditing easier.

## Sitemap Integration

### Adding New Page Types

```typescript
// app/sitemap.ts
import type { MetadataRoute } from "next";
import { CATEGORIES } from "@/lib/category-pages";
import { getAllPages } from "@/lib/task-type-pages";

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const baseUrl = "https://example.com";

  const staticPages = [...];

  // Hub pages
  const categoryPages = CATEGORIES.map(cat => ({
    url: `${baseUrl}/categories/${cat.slug}`,
    lastModified: new Date(),
    changeFrequency: "weekly" as const,
    priority: 0.7,
  }));

  // Product/task pages (HIGHER priority than hubs)
  const taskPages = getAllPages().map(p => ({
    url: `${baseUrl}/categories/${p.categorySlug}/${p.slug}`,
    lastModified: new Date(),
    changeFrequency: "weekly" as const,
    priority: 0.8,
  }));

  return [...staticPages, ...categoryPages, ...taskPages, ...blogPages];
}
```

### Priority Guidelines

| Page Type | Priority | Rationale |
|-----------|----------|-----------|
| Homepage | 1.0 | Root authority |
| How it works / Pricing | 0.9 | High-value informational |
| Task type pages | 0.8 | Highest commercial intent |
| Category hub pages | 0.7 | Topical authority hubs |
| Blog posts | 0.6 | Informational content |
| Legal pages | 0.3 | Required but low-value |

## Internal Linking Architecture

### Hub-Spoke Model

```
Homepage (1.0)
  └── Category hub (/categories/automation-workflows) (0.7)
        ├── Task type (/categories/automation-workflows/n8n-workflow) (0.8)
        ├── Task type (/categories/automation-workflows/make-blueprint) (0.8)
        └── Task type (/categories/automation-workflows/zapier-template) (0.8)
```

**Downward links:** Category hub links to all task type children
**Lateral links:** Each task type links to 4-6 siblings ("Related")
**Upward links:** Breadcrumbs + "View all [category] task types" link

### Updating Hub Pages

When task type pages exist, hub page cards should link to the landing page
(not directly to task creation):

```typescript
const hasLandingPage = LANDING_PAGES.has(`${catSlug}/${taskSlug}`);
const href = hasLandingPage
  ? `/categories/${catSlug}/${taskSlug}`
  : `/tasks/new?taskType=${taskSlug}&category=${catSlug}`;
```

This keeps the task creation as the end of the funnel while the landing page
handles education and trust-building.

## FAQ Accordion Pattern

Use native HTML `<details>/<summary>` for FAQ items. No JavaScript needed,
fully accessible, and SEO-friendly:

```tsx
<details className="group">
  <summary className="flex items-center justify-between cursor-pointer px-7 py-5 [&::-webkit-details-marker]:hidden">
    {question}
    <ChevronRight className="w-4 h-4 transition-transform group-open:rotate-90" />
  </summary>
  <div className="px-7 pb-6">
    {answer}
  </div>
</details>
```

The `[&::-webkit-details-marker]:hidden` removes the default browser triangle.
`group-open:rotate-90` on the chevron provides visual feedback.

## Responsive Typography

Use `clamp()` for all heading sizes to avoid fixed breakpoints:

```
H1: text-[clamp(2.2rem,4.5vw,3.4rem)]
H2: text-[clamp(1.8rem,3.5vw,2.6rem)]
```

This scales smoothly between mobile and desktop without media query jumps.

## Build-Time Verification

After building a new page, run:

```bash
# TypeScript check (catches missing data fields)
npx tsc --noEmit

# Verify the page builds without errors
npx next build

# Check structured data
# Visit https://validator.schema.org/ with the page URL
# Or use: npx next dev, then check page source for JSON-LD blocks
```
