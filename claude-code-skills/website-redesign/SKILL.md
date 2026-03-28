---
name: website-redesign
description: Audit and redesign existing websites with a combined frontend design excellence and conversion rate optimization (CRO) approach. Use this skill whenever the user wants to redesign, re-assess, improve, restyle, or overhaul a website or web page — including homepages, landing pages, pricing pages, feature pages, blog layouts, or demo request pages. Also trigger when the user says "this page isn't converting," "improve conversions," "CRO," "the design looks generic," "make this look more professional," "redesign this," "audit this page," or shares a URL/screenshot/code asking for design feedback. Covers both visual identity (typography, color, layout, motion, depth) and conversion optimization (value proposition, CTAs, trust signals, objection handling). If the user only needs CRO without a visual redesign, this skill still applies — just skip the design implementation phase.
---

# Website Redesign & CRO

Audit an existing website and produce a redesign that is visually distinctive, production-grade, conversion-optimized, and free of generic "AI slop" aesthetics. Work in three phases: **Audit → Design Direction → Build & Recommend**.

## Core Principles

These apply to every decision throughout the process:

- **Design and CRO are not at odds.** The best converting pages are also beautifully designed. Visual hierarchy IS conversion optimization. Beautiful design that doesn't convert is just art — the aesthetic must guide the eye toward value propositions and CTAs.
- **Intentionality over intensity.** Bold maximalism and refined minimalism both work. The key is that every choice is deliberate and cohesive, not that everything is loud.
- **Match complexity to vision.** Maximalist designs need elaborate code with extensive animations. Minimalist designs need restraint, precision, and obsessive attention to spacing and typography.
- **Every element earns its place.** If it doesn't serve clarity, trust, conversion, or delight — remove it.
- **No design should be the same.** Vary themes, fonts, aesthetics. Never converge on common AI defaults.

---

## Phase 1: Audit

Before proposing any changes, perform a thorough audit across both design and conversion dimensions.

### 1A — Identify Context

Determine before analysis:

1. **Page Type**: Homepage, landing page, pricing, feature, blog, demo request, about, or other
2. **Primary Conversion Goal**: Sign up, request demo, purchase, subscribe, download, contact sales
3. **Traffic Context**: Where visitors come from (organic, paid, email, social) — ask if unknown

If a product marketing context file exists (e.g. `.claude/product-marketing-context.md`), read it first.

### 1B — Design Identity Audit

Evaluate and flag every failure:

- **Distinctiveness**: Clear aesthetic point-of-view, or template-like? Red flags: Inter/Roboto/Arial, purple gradients on white, excessive centered layouts, uniform rounded corners, cookie-cutter patterns.
- **Typography**: Distinctive and characterful with deliberate pairing (display + body font)? Or safe, forgettable defaults?
- **Color & Theme**: Cohesive palette with dominant colors and sharp accents? Or timid, evenly-distributed, says nothing? CSS variables for consistency?
- **Spatial Composition**: Surprising and intentional (asymmetry, overlap, diagonal flow, grid-breaking, generous negative space OR controlled density)? Or boring centered columns?
- **Motion & Micro-interactions**: Purposeful animations? Orchestrated page-load stagger? Scroll-triggered reveals? Surprising hover states? Or scattered random effects / no motion at all?
- **Backgrounds & Visual Depth**: Atmosphere through gradients, noise textures, geometric patterns, layered transparencies, shadows, grain overlays? Or flat solid colors?

### 1C — CRO Analysis (7 Dimensions, by Impact)

Score each dimension 🔴 Critical / 🟡 Needs Work / 🟢 Strong:

**1. Value Proposition Clarity** (highest impact) — Can a visitor understand what this is and why they should care within 5 seconds? Is the benefit clear, specific, differentiated, and in the customer's language? Common failures: feature-focused instead of benefit-focused; too vague or too clever; trying to say everything.

**2. Headline Effectiveness** — Does it communicate the core value proposition? Is it specific and meaningful? Does it match the traffic source? Strong patterns: outcome-focused ("Get [outcome] without [pain]"), specific numbers/timeframes, embedded social proof.

**3. CTA Placement, Copy & Hierarchy** — One clear primary action visible without scrolling? Button copy communicates value, not just action ("Start Free Trial" > "Submit")? Logical primary vs. secondary structure? CTAs repeated at decision points?

**4. Visual Hierarchy & Scannability** — Can someone scanning get the main message? Most important elements visually prominent? Enough white space? Images support or distract?

**5. Trust Signals & Social Proof** — Customer logos, specific attributed testimonials with photos, case study snippets with numbers, review scores, security badges. Placed near CTAs and after benefit claims?

**6. Objection Handling** — Addresses: price/value concerns, "will this work for me?", implementation difficulty, "what if it doesn't work?" Through FAQ, guarantees, comparisons, process transparency?

**7. Friction Points** — Too many form fields, unclear next steps, confusing nav, unnecessary required fields, mobile issues, slow load times?

### 1D — Page-Type-Specific Analysis

Apply the relevant framework:

| Page Type | Key Requirements |
|---|---|
| **Homepage** | Clear positioning for cold visitors; quick path to primary conversion; handle "ready to buy" AND "still researching" |
| **Landing Page** | Message match with traffic source; single CTA focus; remove nav if possible; complete argument on one page |
| **Pricing Page** | Clear plan comparison; recommended plan highlighted; address "which plan?" anxiety; price anchoring |
| **Feature Page** | Connect features to benefits; use cases and examples; clear path to try/buy |
| **Blog Post** | Contextual CTAs matching content; inline CTAs at natural stopping points |
| **Demo Request** | Benefits above/beside form; minimal fields; "What to Expect" section; testimonials near form |

---

## Phase 2: Design Direction

Commit to a direction before writing any code.

### 2A — Aesthetic Direction

Choose a BOLD, specific direction — not just "modern." Pick a flavor and commit:

*brutally minimal / maximalist chaos / retro-futuristic / organic/natural / luxury/refined / playful/toy-like / editorial/magazine / brutalist/raw / art deco/geometric / soft/pastel / industrial/utilitarian*

Choose what is TRUE to the brand. Justify the choice. Declare the one element that makes the design unforgettable. Verify: does the aesthetic SERVE the conversion goals?

### 2B — Typography Plan

**Banned**: Inter, Roboto, Arial, Space Grotesk, system fonts.

Choose distinctive, characterful fonts from Google Fonts or another CDN. Pair a display font (headings) with a refined body font. Name both and explain the pairing.

### 2C — Color System

The sweet spot: **sophisticated with character** — not screaming neon, not put-you-to-sleep grayscale.

For reference palettes and calibration notes, read [references/reference-palettes.md](reference-palettes.md).

Your custom palette must include:
- 4–6 colors with hex codes
- Clear roles: dominant, accent, dark anchor, light/neutral base, optional secondary
- CSS custom properties for consistency
- Sufficient contrast (WCAG AA minimum)

### 2D — Conversion Architecture

Describe the visitor flow:
1. What they see first (hero / above-fold)
2. What builds trust (proof section)
3. What drives action (CTA placement)
4. How objections are handled (FAQ / guarantees)

Identify the single most important conversion action.

---

## Phase 3: Build & Recommend

### 3A — Technical Stack

| Complexity | Stack |
|---|---|
| Simple pages | Semantic HTML + CSS custom properties + vanilla JS — single self-contained file |
| Complex apps | React 18 + TypeScript + Tailwind CSS 3.4 + shadcn/ui + Parcel bundling |

shadcn/ui components available: accordion, alert, avatar, badge, button, calendar, card, carousel, checkbox, command, dialog, drawer, dropdown-menu, form, hover-card, input, label, menubar, navigation-menu, popover, progress, radio-group, resizable, scroll-area, select, separator, sheet, skeleton, slider, sonner, switch, table, tabs, textarea, toast, toggle, toggle-group, tooltip.

### 3B — Design Execution Checklist

Verify every item before delivering:

**Typography**
- [ ] Distinctive header font loaded from CDN and applied
- [ ] Refined body font paired correctly
- [ ] Type scale: headline > subheading > body > caption
- [ ] Line-height and letter-spacing deliberately tuned

**Color & Theme**
- [ ] CSS custom properties for entire palette
- [ ] Dominant color with sharp accents
- [ ] Dark/light variants considered
- [ ] WCAG AA contrast minimum
- [ ] No purple gradients on white

**Layout & Composition**
- [ ] At least one unexpected layout element (asymmetry, overlap, diagonal, grid-break)
- [ ] Generous negative space where it counts
- [ ] Content blocks vary in rhythm and visual weight
- [ ] Mobile-responsive without losing character
- [ ] No uniform rounded corners everywhere

**Motion & Interaction**
- [ ] Orchestrated page-load stagger (`animation-delay`)
- [ ] Hover states that surprise (transforms, reveals, not just color changes)
- [ ] Scroll-triggered reveals for key sections
- [ ] CSS-only for HTML builds; Framer Motion for React
- [ ] Animations serve purpose: guide attention, create delight, indicate state
- [ ] Performant: `transform` and `opacity` preferred

**Backgrounds & Atmosphere**
- [ ] No flat solid backgrounds unless deliberately chosen
- [ ] Atmospheric effects: gradients, noise, patterns, transparencies
- [ ] Depth through layered shadows, overlaps, z-axis
- [ ] Decorative elements reinforce the aesthetic

**CRO (Non-Negotiable)**
- [ ] Value proposition clear within 5 seconds
- [ ] Headline specific, benefit-focused, meaningful
- [ ] Primary CTA above fold, high-contrast, value-communicating copy
- [ ] CTA hierarchy: clear primary, logical secondary
- [ ] CTAs repeated at decision points (after benefits, proof, page end)
- [ ] Trust signals near CTAs and after benefit claims
- [ ] Objections addressed (FAQ, guarantees, comparisons)
- [ ] Friction minimized (minimal fields, clear next steps)
- [ ] Scannable — quick scroll conveys core message
- [ ] Visuals support message, never distract
- [ ] Mobile CTAs thumb-friendly (44×44px minimum)
- [ ] Target < 3s load (lazy-load, minimize render-blocking)
- [ ] Sticky/floating CTA considered for long pages

### 3C — Anti-Patterns

For the full anti-pattern table with reasoning, read [references/anti-patterns.md](anti-patterns.md). Key hard blocks: no Inter/Roboto/Arial, no purple gradients on white, no "Submit"/"Learn More"/"Click Here" CTAs, no uniform rounded corners, no vague hero headlines, no flat backgrounds without texture.

### 3D — Experiment Roadmap

After the redesign, provide prioritized A/B test hypotheses. For the full experiment bank organized by page type (60+ test ideas), read [references/experiment-bank.md](experiment-bank.md).

---

## Output Format

Structure the complete response as:

### Part A: Audit Report
- Design Identity findings (flag every failure)
- CRO Analysis: each of 7 dimensions scored 🔴/🟡/🟢 with findings
- Page-type-specific findings
- Top 5 priority issues ranked by conversion impact

### Part B: Design Direction
- Aesthetic direction with justification
- Typography plan (font names, sources, pairing rationale)
- Color system (CSS custom properties with hex codes and role rationale)
- Conversion architecture (visitor flow)
- Key differentiator

### Part C: Recommendations
- **Quick Wins** — easy changes, immediate impact
- **High-Impact Changes** — bigger effort, significant conversion upside
- **Test Ideas** — A/B hypotheses from the experiment bank
- **Copy Alternatives** — 2–3 alternatives each for headline, subhead, primary CTA, with strategic rationale

### Part D: Implementation
- Full working code (single HTML or structured React)
- Responsive across mobile, tablet, desktop
- All animations and interactions functional
- All CTA and conversion elements implemented
- Confirm every item on the Design Execution Checklist (3B)
