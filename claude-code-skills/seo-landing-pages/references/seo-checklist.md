# SEO Audit Checklist for Landing Pages

Run this checklist on every landing page before shipping. Items marked with
**(Critical)** must pass — they directly impact indexation and ranking.

## Technical SEO

### Server Rendering **(Critical)**
- [ ] Page is a **server component** (no `"use client"` on the page file)
- [ ] `generateMetadata()` is exported and returns unique metadata per page
- [ ] `generateStaticParams()` is exported for SSG at build time
- [ ] Full HTML is present in the initial server response (no hydration-dependent content)

### Meta Tags **(Critical)**
- [ ] `<title>` is unique per page, ≤60 chars, primary keyword near start
- [ ] `<meta name="description">` is unique per page, ≤155 chars, includes primary keyword
- [ ] Canonical URL is set explicitly via `alternates.canonical`
- [ ] No duplicate titles or descriptions across pages

### OpenGraph & Social
- [ ] `og:title` set (can differ slightly from `<title>`)
- [ ] `og:description` set
- [ ] `og:url` set to canonical URL
- [ ] `og:image` set (1200x630px recommended)
- [ ] `og:type` set to "website" (or "product" if applicable)
- [ ] `twitter:card` set to `summary_large_image`

### Structured Data (JSON-LD) **(Critical)**
- [ ] `BreadcrumbList` schema present — correct hierarchy, all URLs valid
- [ ] `FAQPage` schema present — at least 4-6 questions, answers match visible FAQ
- [ ] `Product` schema present (if applicable) — price, currency, availability
- [ ] `aggregateRating` included in Product schema when real review data exists
- [ ] All JSON-LD blocks validate at https://validator.schema.org/

### Sitemap
- [ ] Page URL added to `sitemap.ts`
- [ ] Priority set correctly (0.8 for product/task pages, 0.7 for hub pages)
- [ ] `changeFrequency` set to "weekly" for active pages
- [ ] `lastModified` set

### Robots
- [ ] `robots.ts` does not block the URL path
- [ ] No `noindex` meta tag on the page
- [ ] No canonical pointing to a different page

### URL Structure
- [ ] URL is lowercase, hyphen-separated, readable
- [ ] URL contains the primary keyword where natural
- [ ] Nested under a logical parent path (e.g., `/categories/parent/child`)
- [ ] No query parameters for indexable content (use path segments)

## On-Page SEO

### Heading Structure **(Critical)**
- [ ] Exactly one `<h1>` per page
- [ ] H1 contains the primary keyword
- [ ] All `<h2>` tags contain the primary or secondary keyword
- [ ] Heading hierarchy is logical (H1 → H2 → H3, no skipped levels)
- [ ] No generic H2s like "Frequently Asked Questions" or "How It Works"

### Keyword Placement
- [ ] Primary keyword in H1
- [ ] Primary keyword in at least 4 of 7 H2s
- [ ] Primary keyword in the first 100 words of body content
- [ ] Secondary keywords distributed naturally across sections
- [ ] Long-tail keywords in use case descriptions
- [ ] No keyword stuffing — every usage reads naturally

### Internal Linking **(Critical)**
- [ ] Breadcrumb links to real, crawlable parent pages
- [ ] "Related" section links to 4-6 sibling pages
- [ ] CTA links to the correct task creation URL with proper query params
- [ ] Parent/hub page links back to this page
- [ ] Footer present with site-wide navigation links

### Content Quality
- [ ] Each section has unique, descriptive content (not boilerplate)
- [ ] FAQ answers are substantial (2-4 sentences minimum)
- [ ] Example output shows real, representative content (not placeholder)
- [ ] Use case descriptions are specific (name real tools, real scenarios)
- [ ] No thin sections — every section adds value

### Images & Alt Text
- [ ] All images have descriptive `alt` text
- [ ] Images are optimized (WebP, lazy-loaded where appropriate)
- [ ] OG image exists and is branded

## Accessibility & Mobile

### Mobile Responsiveness
- [ ] All key content visible on mobile (no `hidden lg:block` without fallback)
- [ ] Stats/value props visible on all screen sizes
- [ ] Typography uses `clamp()` for responsive sizing
- [ ] Touch targets are ≥44px
- [ ] No horizontal scroll on any breakpoint

### Accessibility
- [ ] Breadcrumb `<nav>` has `aria-label="Breadcrumb"`
- [ ] FAQ uses semantic `<details>`/`<summary>` elements
- [ ] Color contrast meets WCAG AA (4.5:1 for text)
- [ ] Interactive elements are keyboard-navigable
- [ ] SVG icons have `aria-hidden="true"` when decorative

## Page Completeness

### Required Sections
- [ ] Hero with H1, tagline, CTA, stats
- [ ] What You Get / Deliverables
- [ ] Social Proof (stat bar + testimonial)
- [ ] Use Cases (4+ scenarios)
- [ ] Example Output with code/content preview
- [ ] How It Works (3 steps)
- [ ] Why [Brand] / Differentiation
- [ ] FAQ (6 questions with FAQPage schema)
- [ ] Bottom CTA
- [ ] Footer

### CTA Placement
- [ ] Primary CTA above the fold (in hero)
- [ ] Mid-page CTA after Example Output section
- [ ] Bottom CTA in dark section
- [ ] Each use case card has a mini-CTA link

## Competitive Differentiation

- [ ] At least one FAQ addresses "How is this different from [free alternative]?"
- [ ] "Why [Brand]" section explicitly contrasts with templates/free options
- [ ] Price anchoring present (compare to freelancer/agency costs if applicable)
- [ ] Testimonial mentions a specific outcome, not generic praise
