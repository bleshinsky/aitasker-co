# JSON-LD Schema Templates

Copy-paste templates for the three JSON-LD blocks used on SEO landing pages.
All templates follow schema.org specifications and validate at
https://validator.schema.org/.

## 1. BreadcrumbList

Enables breadcrumb trails in Google SERPs:
`example.com > Category > Product Page`

```typescript
const breadcrumbJsonLd = {
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  itemListElement: [
    {
      "@type": "ListItem",
      position: 1,
      name: "Home",
      item: "https://example.com",
    },
    {
      "@type": "ListItem",
      position: 2,
      name: "Category Name",        // e.g. "Automation & Workflow Files"
      item: "https://example.com/categories/category-slug",
    },
    {
      "@type": "ListItem",
      position: 3,
      name: "Page Title",           // e.g. "Custom n8n Workflow JSON"
      item: "https://example.com/categories/category-slug/page-slug",
    },
  ],
};
```

**Rules:**
- Position numbers must be sequential starting at 1
- Every `item` URL must be a real, crawlable page
- The last item's `name` should match the H1 (or a shortened version)
- Maximum 3-4 levels deep for commercial pages

## 2. FAQPage

Triggers FAQ rich snippets in SERPs — expands the SERP listing with
question/answer dropdowns, dramatically increasing CTR.

```typescript
const faqJsonLd = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  mainEntity: [
    {
      "@type": "Question",
      name: "What is an n8n workflow JSON file?",
      acceptedAnswer: {
        "@type": "Answer",
        text: "An n8n workflow JSON is a file that contains the complete definition of an automation workflow — all nodes, connections, parameters, and configuration. You import it directly into n8n and it renders as a visual workflow ready to activate.",
      },
    },
    {
      "@type": "Question",
      name: "How is this different from free n8n templates?",
      acceptedAnswer: {
        "@type": "Answer",
        text: "Free templates are generic starting points. Our product is custom-built to your exact specification — your specific requirements, your data, your business logic.",
      },
    },
    // ... 4-6 questions total
  ],
};
```

**Rules:**
- Minimum 4 questions, maximum 8 (Google may truncate beyond that)
- Questions must match exactly what's visible on the page
- Answers must match the visible FAQ content (Google penalizes mismatches)
- Include the primary keyword in at least 2 question/answer pairs
- One question should address competitive differentiation ("How is this different from...")
- One question should address pricing/speed ("How long does it take...")

### FAQ Content Strategy

| Question Type | Purpose | Example |
|---|---|---|
| Definitional | Capture "what is" queries | "What is an n8n workflow JSON?" |
| Differentiation | Convert template-seekers | "How is this different from free templates?" |
| Capability | Address scope concerns | "What node types are supported?" |
| Customization | Reduce risk anxiety | "Can I customize it after importing?" |
| Speed/Process | Set expectations | "How long does it take?" |
| Safety net | Handle failure fears | "What if it doesn't work?" |

## 3. Product

Surfaces pricing and star ratings in Google search results.

### Basic Product (no ratings yet)

```typescript
const productJsonLd = {
  "@context": "https://schema.org",
  "@type": "Product",
  name: "Custom n8n Workflow JSON — AI-Built, Ready to Import",
  description: "Get custom n8n workflow JSON files built by AI agents in 90 seconds.",
  url: "https://example.com/categories/automation-workflows/n8n-workflow",
  brand: {
    "@type": "Organization",
    name: "Your Brand",
  },
  offers: {
    "@type": "Offer",
    price: 22,
    priceCurrency: "AUD",
    availability: "https://schema.org/InStock",
    url: "https://example.com/categories/automation-workflows/n8n-workflow",
  },
};
```

### Product with aggregateRating

```typescript
const productJsonLd = {
  "@context": "https://schema.org",
  "@type": "Product",
  name: "Custom n8n Workflow JSON — AI-Built, Ready to Import",
  description: "Get custom n8n workflow JSON files built by AI agents in 90 seconds.",
  url: "https://example.com/categories/automation-workflows/n8n-workflow",
  brand: {
    "@type": "Organization",
    name: "Your Brand",
  },
  offers: {
    "@type": "Offer",
    price: 22,
    priceCurrency: "AUD",
    availability: "https://schema.org/InStock",
    url: "https://example.com/categories/automation-workflows/n8n-workflow",
  },
  aggregateRating: {
    "@type": "AggregateRating",
    ratingValue: "4.8",
    reviewCount: "47",
    bestRating: "5",
    worstRating: "1",
  },
};
```

**Rules:**
- `name` should match the H1 or be a close variant
- `price` is the starting/minimum price
- `priceCurrency` must be a valid ISO 4217 code
- `availability` should be one of: InStock, OutOfStock, PreOrder
- `aggregateRating` values must be REAL, verifiable data
- Google penalizes fabricated ratings — omit until real data exists

### Conditional Rating Pattern

Add rating only when data exists:

```typescript
const productJsonLd = {
  "@context": "https://schema.org",
  "@type": "Product",
  // ... base fields
  ...(data.rating
    ? {
        aggregateRating: {
          "@type": "AggregateRating",
          ratingValue: data.rating.value,
          reviewCount: data.rating.count,
          bestRating: "5",
          worstRating: "1",
        },
      }
    : {}),
};
```

## Rendering in Next.js

Place JSON-LD blocks as `<script>` tags at the top of the page component:

```tsx
return (
  <main>
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbJsonLd) }}
    />
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(faqJsonLd) }}
    />
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(productJsonLd) }}
    />
    {/* Visible page content */}
  </main>
);
```

Each schema gets its own `<script>` block. Do not combine them into a single
array — separate blocks are easier to audit and debug.

## Validation

After implementing, verify structured data:

1. **Schema.org Validator**: https://validator.schema.org/ — paste JSON-LD
2. **Google Rich Results Test**: https://search.google.com/test/rich-results — test live URL
3. **View Page Source**: Check that JSON-LD appears in the raw HTML (not hydrated JS)
4. **Google Search Console**: After indexing, check "Enhancements" for schema errors

Common validation errors:
- Missing `@context` field
- Invalid `availability` URL (must use full schema.org URL)
- `priceCurrency` not ISO 4217 (use "AUD" not "A$")
- FAQ `name` doesn't match visible question text
- BreadcrumbList `item` URLs point to non-existent pages
