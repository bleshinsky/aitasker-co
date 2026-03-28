# CRO Patterns for Landing Pages

Conversion rate optimization patterns discovered through building and auditing
SEO landing pages. Each pattern includes the problem, why it matters, and the
implementation approach.

## Pattern 1: Social Proof Section

### Problem
Pages without social proof ask visitors to trust an unknown brand. Organic
search visitors have zero prior relationship — trust must be established before
requesting any action.

### Why It Matters
Social proof near the top of a landing page typically improves conversion
15-30%. For commercial pages, this is the difference between profitable and
break-even.

### Implementation
Place between "What You Get" and "Use Cases" sections:

**Stat bar** (4 items in a 2x2 grid on mobile, 4-col on desktop):
- Delivery time ("90s")
- Number of competing prototypes ("3-5")
- Quality score ("4.8/5")
- Cost to try ("$0")

**Testimonial card** below the stat bar:
- Star rating (5 stars visual)
- Quote that names specific tools/outcomes (not generic praise)
- Attribution with name, role, company type
- Initials avatar with category gradient

**Critical rule:** The testimonial must be specific. "Got 4 competing JSON
files in about a minute. The one I picked imported perfectly" converts 3-5x
better than "Great service, highly recommend."

### Data Structure
```typescript
socialProof: {
  stats: Array<{ value: string; label: string }>;
  testimonial?: {
    quote: string;       // Specific outcome, not generic
    name: string;
    role: string;
    initials: string;
  };
}
```

## Pattern 2: Mobile Stats Visibility

### Problem
Stats cards using `hidden lg:block` are invisible to 55-70% of traffic (mobile
+ tablet). The most compelling value props (price, speed, prototypes count) are
hidden from the majority of visitors.

### Why It Matters
Mobile visitors who don't see pricing, delivery time, or value propositions in
the hero have no anchor for the page's value. They scroll past the hero with
less context than desktop visitors.

### Implementation
Add a compact mobile-specific stats layout below the hero CTA, visible only
below the `lg` breakpoint:

```
<div className="lg:hidden mt-8 grid grid-cols-2 gap-3">
  {/* 4 compact stat cards */}
</div>

{/* Desktop stats card (visible at lg+) */}
<div className="hidden lg:block">
  {/* Full stats card */}
</div>
```

Mobile stat cards use smaller typography (`text-xl` vs `text-3xl`), tighter
padding (`px-4 py-3` vs `p-7`), and rounded-xl instead of rounded-2xl.

## Pattern 3: Mid-Page CTA After Example Output

### Problem
The Example Output section is the highest-intent moment — the visitor just SAW
what they'd get. But the next section ("How It Works") is a deceleration step.
Intent peaks after the preview and bleeds with every scroll.

### Why It Matters
"Strike while the iron is hot." After the code/content preview, intent is at
its peak. Every section between that preview and a CTA is friction that costs
conversions.

### Implementation
Add a CTA directly after the example output's caption, within the same section:

```
<p>{caption}</p>

{/* Mid-page CTA — highest intent moment */}
<div className="mt-8 text-center">
  <Link href={ctaHref} className="...button styles...">
    Get a Custom [Product] Like This
    <ArrowRight />
  </Link>
  <p className="text-xs text-slate-400 mt-2.5">
    From $XX · Prototypes in ~90 seconds
  </p>
</div>
```

The CTA copy should reference what was just shown ("Like This") and include
price + speed as reinforcement text below the button.

## Pattern 4: Keyword-Rich H2 Tags

### Problem
Generic H2s like "Frequently Asked Questions", "How It Works", and "What
People Automate" waste the second most important on-page ranking signal. H2s
are how Google understands page structure and topic relevance.

### Why It Matters
When 5 of 7 H2s contain zero target keywords, the page signals topical
weakness. Competitor pages with keyword-rich H2s will outrank on the same
queries.

### Implementation
Make H2 content data-driven so each page variant has unique, keyword-rich H2s:

| Generic H2 | Keyword-Rich H2 |
|---|---|
| "What People Automate" | "n8n Workflow Use Cases" |
| "See What You'll Get" | "Example n8n Workflow JSON Output" |
| "Three steps. Under two minutes." | "How to Get Your n8n Workflow" |
| "Custom Workflows, Not Generic Templates" | "Why Custom n8n Workflows Beat Templates" |
| "Frequently Asked Questions" | "n8n Workflow JSON — Common Questions" |

Add headline fields to the data interface for every section:
```typescript
useCasesHeadline: string;
howItWorksHeadline: string;
whyUsHeadline: string;
faqHeadline: string;
```

**Rule:** Primary keyword should appear in at least 4 of 7 H2s. Each must
still read naturally — no stuffing.

## Pattern 5: OG Image for Social Sharing

### Problem
Missing OpenGraph images mean plain text cards when shared on Twitter, LinkedIn,
Slack, or Google Discover. No visual = lower engagement.

### Why It Matters
Social shares with images get 2-3x more engagement. Google Discover requires
images. Every share without a branded image is a missed impression.

### Implementation
Add to `generateMetadata()`:
```typescript
openGraph: {
  images: [{
    url: `https://example.com/og/task-type.png`,
    width: 1200,
    height: 630,
    alt: data.hero.h1,
  }],
},
twitter: {
  card: "summary_large_image",
  title: data.hero.h1,
  description: data.seo.description,
},
```

For v1, use a single branded OG image. For v2, generate dynamic images with
task type name overlaid (Next.js `ImageResponse` API or external service).

## Pattern 6: Footer on Every Page

### Problem
Pages that end with just a dark CTA section feel incomplete. No site
navigation, no legal links, no "About" context. Visitors who scroll to the
bottom without converting hit a dead end.

### Why It Matters
- **SEO:** Footer links are key internal linking. Google crawls them.
- **CRO:** Bottom-scrollers need an escape hatch. No footer = bounce.
- **Trust:** Missing footer feels unfinished. Legal links (Terms, Privacy) are
  trust signals.

### Implementation
Import and render the shared Footer component at the end of `<main>`:
```tsx
import { Footer } from "@/components/ui/Footer";
// At the end of JSX, after the bottom CTA section:
<Footer />
```

## Pattern 7: Product Schema with aggregateRating

### Problem
Product JSON-LD with just price but no rating misses the star display in Google
search results. A product listing with stars gets dramatically higher CTR.

### Why It Matters
Star ratings in SERPs increase click-through rate by 25-35%. The visual
differentiation in a list of blue links is significant.

### Implementation
Add rating data conditionally to Product schema:
```typescript
const productJsonLd = {
  "@type": "Product",
  // ... existing fields
  ...(data.rating ? {
    aggregateRating: {
      "@type": "AggregateRating",
      ratingValue: data.rating.value,
      reviewCount: data.rating.count,
      bestRating: "5",
      worstRating: "1",
    },
  } : {}),
};
```

**Important:** These must be real, verifiable numbers. Google penalizes
fabricated review schema. Omit `rating` from the data file until real data
exists. Build the pipeline now so it's ready when threshold is reached.

## Section Background Alternation

Maintain visual rhythm with alternating background colors:

```
Hero:            Dark (--ink)
What You Get:    White (bg-white)
Social Proof:    Cream (default)
Use Cases:       Cream (default) — cards are white on cream
Example Output:  White (bg-white)
How It Works:    Cream (default)
Why [Brand]:     White (bg-white)
FAQ:             Cream (default)
Related:         White (bg-white)
Bottom CTA:      Dark (--ink)
Footer:          Dark (--ink)
```

When inserting new sections, maintain the alternation. Two same-colored
sections back-to-back are acceptable only if they have distinct visual
structures (e.g., stat bar + testimonial card in Social Proof flowing into
use case cards).

## CTA Copy Patterns

| Location | Pattern | Example |
|----------|---------|---------|
| Hero | "[Action] — From $[price]" | "Get Your n8n Workflow — From $22" |
| Mid-page | "Get a Custom [Product] Like This" | "Get a Custom Workflow Like This" |
| Use case cards | "[Action] this [thing]" | "Build this workflow" |
| Bottom | Same as hero CTA | "Get Your n8n Workflow — From $22" |
| Below CTA | "From $[X] [currency] · Prototypes in [time]" | "From $22 AUD · Prototypes in ~90 seconds" |

**Rule:** Never use generic CTAs like "Get Started", "Learn More", or "Submit".
Every CTA should communicate what the user gets.
