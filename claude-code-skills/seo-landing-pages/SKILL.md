---
name: seo-landing-pages
version: 1.0.0
description: >
  This skill should be used when the user asks to "build a landing page",
  "create an SEO page", "make a task type page", "build a product page",
  "optimize a page for SEO", "add structured data", "add JSON-LD schema",
  "create a page template", "build pages at scale", "improve page conversion
  rate", "add breadcrumbs", or needs to create high-converting, SEO-optimized
  landing pages in Next.js. Covers keyword strategy, page structure, JSON-LD
  structured data, CRO patterns, and a post-build audit framework.
---

# SEO Landing Page Builder

Build SEO-optimized, high-converting landing pages in Next.js using a
data-driven architecture that scales to hundreds of pages.

## When to Use

- Creating commercial landing pages targeting purchase-intent keywords
- Building page templates that scale across many variants (task types, products, services)
- Adding structured data (JSON-LD) for rich SERP results
- Auditing existing pages for SEO and CRO issues
- Converting client-rendered pages to server-rendered for SEO

## Core Workflow

Follow these 6 phases in order. Each phase has a checklist — complete every
item before moving to the next phase.

### Phase 1: Keyword Strategy

Before writing any code, define the keyword map. Every content decision flows
from this.

1. Identify **primary keyword** (commercial intent, 2-4 words)
2. Identify **secondary keywords** (3-5 variants of primary)
3. Identify **long-tail keywords** (4+ words, purchase-ready, target use cases)
4. Identify **informational keywords** (research queries to capture via FAQ/examples)
5. Identify **competitive capture keywords** (terms where free alternatives dominate — differentiate)

Map each keyword tier to the page section where it will appear:

| Tier | Page Section |
|------|-------------|
| Primary | H1, title tag, first 100 words |
| Secondary | H2s, meta description, What You Get |
| Long-tail | Use Cases section |
| Informational | Example Output, FAQ |
| Competitive | FAQ differentiation questions |

### Phase 2: Meta & Structured Data

Define three things before building the page:

**Meta tags:**
- Title: ≤60 chars, primary keyword near start, brand at end
- Description: ≤155 chars, primary + secondary keyword, value prop, price if applicable
- H1: Primary keyword, benefit-oriented, different from title tag

**JSON-LD blocks (3 per page):**
1. **BreadcrumbList** — enables breadcrumb trails in SERPs
2. **FAQPage** — triggers FAQ rich snippets (2-3x CTR boost)
3. **Product** (if applicable) — surfaces pricing in SERPs, include `aggregateRating` when real data exists

**OpenGraph + Twitter:**
- OG image (1200x630), OG title, OG description, canonical URL
- Twitter card: `summary_large_image`

See `references/json-ld-templates.md` for copy-paste schema templates.

### Phase 3: Page Architecture

Use a **server component** (no `"use client"`). This is non-negotiable for SEO
because `generateMetadata()` only works in server components.

**Required exports:**
- `generateMetadata()` — dynamic meta tags per page
- `generateStaticParams()` — SSG at build time for instant TTFB
- Page component — renders full HTML server-side

**Client interactivity:** Extract into small client wrapper components (e.g.,
`RevealClient` for scroll animations, accordion for FAQ). The page shell stays
server-rendered.

**Data-driven architecture:** Store all page content in a static TypeScript
data file. The page component is 100% reusable — only data changes per variant.
This scales to hundreds of pages with zero component duplication.

See `references/nextjs-seo-architecture.md` for implementation patterns.

### Phase 4: Section Layout (9-Section Template)

This ordering is optimized for conversion funnel psychology:

| # | Section | Purpose | Background |
|---|---------|---------|-----------|
| 1 | **Hero** | H1, tagline, primary CTA, stats card | Dark |
| 2 | **What You Get** | Deliverables with icons | White |
| 3 | **Social Proof** | Stat bar + testimonial | Cream |
| 4 | **Use Cases** | 4 scenario cards with mini-CTAs | Cream |
| 5 | **Example Output** | Code/content preview + mid-page CTA | White |
| 6 | **How It Works** | 3 numbered steps | Cream |
| 7 | **Why [Brand]** | 3 differentiation cards | White |
| 8 | **FAQ** | 6 questions with FAQPage schema | Cream |
| 9 | **Bottom CTA** | Final conversion push | Dark |

Plus: **Footer** (internal links, legal, trust signals) and **Related Pages**
(sibling internal links for SEO equity flow).

**Critical rules:**
- Every H2 must contain the primary keyword (not generic like "Frequently Asked Questions")
- Stats card must be visible on mobile (don't use `hidden lg:block` without a mobile fallback)
- Place a CTA immediately after the Example Output — this is the highest-intent moment
- Social proof must appear before the user is asked to act (above use cases)

### Phase 5: Sitemap & Internal Linking

After the page is built:

1. Add all new URLs to `sitemap.ts` with correct priorities:
   - Task type / product pages: priority 0.8 (highest-intent)
   - Category / hub pages: priority 0.7
   - Blog posts: priority 0.6
2. Verify `robots.ts` doesn't block the new URL paths
3. Update parent/hub pages to link to new child pages
4. Add "Related" section with sibling page links
5. Ensure breadcrumb links point to real, crawlable pages

### Phase 6: Post-Build Audit

Run the 7-point audit on every new page before shipping. These are the most
common issues found in real production pages:

| # | Check | Type | How to Fix |
|---|-------|------|-----------|
| 1 | **Social proof exists** | CRO | Add stat bar + testimonial section |
| 2 | **Stats visible on mobile** | CRO | Add mobile-specific layout below `lg` breakpoint |
| 3 | **Mid-page CTA after example** | CRO | CTA button + price immediately after code/preview |
| 4 | **H2s contain primary keyword** | SEO | Make all section headlines keyword-rich |
| 5 | **OG image set** | SEO | Add `images` to OpenGraph + Twitter card meta |
| 6 | **Footer present** | SEO+CRO | Import and render site footer component |
| 7 | **Product schema has rating** | SEO | Add `aggregateRating` when real data exists |

See `references/seo-checklist.md` for the full audit checklist.
See `references/cro-patterns.md` for detailed CRO pattern implementations.

## Data File Interface (Template)

Every page variant is defined by a single data object. The TypeScript interface
should include at minimum:

```
slug, categorySlug, categoryLabel
seo: { title, description, keywords }
hero: { h1, tagline, ctaText, stats }
whatYouGet: { headline, description, deliverables[] }
useCasesHeadline + useCases[]
exampleOutput: { headline, description, code, language, caption }
howItWorksHeadline + howItWorks[]
whyUsHeadline + whyUs[]
faqHeadline + faqs[]
socialProof: { stats[], testimonial? }
rating?: { value, count }
relatedTypes[]
```

Each headline field is a keyword-rich H2. Each section is independently
renderable. The component never changes — only the data file grows.

## Key Principles

1. **Server component or it doesn't rank.** Client components can't use `generateMetadata()`. No SSR metadata = invisible to Google.
2. **Every H2 is a ranking signal.** Generic H2s ("How It Works") waste the second most important on-page signal. Always include the primary keyword.
3. **Social proof before action.** Visitors from organic search have never heard of the brand. Trust must be established before asking for a click.
4. **Mobile users are the majority.** Any value prop hidden behind `hidden lg:block` without a mobile fallback is invisible to 55-70% of visitors.
5. **Data-driven scales.** One component + N data entries = N pages with zero code duplication. SEO improvements become data file edits.
6. **Price in SERPs pre-qualifies buyers.** Product schema with `offers.price` surfaces pricing in Google results, filtering out non-buyers before they click.

## Additional Resources

### Reference Files

- **`references/seo-checklist.md`** — Full SEO audit checklist (technical + on-page + content)
- **`references/cro-patterns.md`** — CRO patterns with implementation code
- **`references/nextjs-seo-architecture.md`** — Next.js server component patterns for SEO
- **`references/json-ld-templates.md`** — Copy-paste JSON-LD schema templates
