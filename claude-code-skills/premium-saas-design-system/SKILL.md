---
name: premium-saas-design-system
description: >
  Premium SaaS design system for building Awwwards-level marketing pages. Use when building
  landing pages, hero sections, feature grids, pricing pages, about pages, brand pages, team
  pages, or any marketing/product page that needs exceptional design quality. Covers dramatic
  typography, purposeful motion, scroll composition, conversion patterns, and performance-optimized
  animation — works with any React/Next.js + Tailwind CSS + shadcn/ui stack.
---

# Premium SaaS Design System

Award-winning, immersive page design for premium SaaS products.
Stack: Next.js / React / Tailwind CSS / shadcn/ui.

**Prerequisites:** Next.js, Tailwind CSS, shadcn/ui. This skill requires a brand configuration file — see `brand-config.example.md` for the template. Copy it to `.claude/brand-config.md` in your project and fill in your brand identity, colors, fonts, and CTA copy.

---

## When to Use

- Landing pages, hero sections, feature grids, pricing pages
- Brand pages, about pages, how-it-works pages
- Product pages, team pages, sub-brand pages
- Category landing pages, marketplace pages
- Any page that needs to feel premium, intentional, and conversion-optimized
- Requests mentioning "premium", "Awwwards", "brand page", "landing page", "redesign"

---

## Brand Configuration

**Before using this skill**, read the project's brand configuration to understand the color palette, fonts, tone, and brand identity. Premium design requires intentional color choices — never default to generic blue/gray SaaS palettes.

**Look for the config file at:** `.claude/brand-config.md`, `brand-config.md`, or the project's design tokens.

If no brand config exists, prompt the user to create one. A template is provided at `brand-config.example.md` in this skill's directory. The template defines:

- **Brand identity** — name, positioning, audience, tone of voice
- **6 color roles** — `background`, `text-primary`, `accent`, `success`, `border`, `surface-alt`
- **3 font slots** — `font-display` (headlines), `font-sans` (body), `font-mono` (code)
- **Optional secondary brand variant** — for sub-brands with distinct gradient/color

**Key principle:** The display font is the single biggest lever for perceived quality. The brand config should specify a distinctive serif or display face, not a generic system font.

### Secondary Brand Variants

If the brand config defines a variant (sub-brand, secondary product line), apply strict scope rules:

- Variant styling appears ONLY on variant-specific routes
- It must NEVER leak into the core brand pages
- Differences might include: color accent, visual weight, tone, shape language, gradient

```tsx
{/* Variant gradient — only on variant routes */}
<section style={{ background: "linear-gradient(135deg, var(--variant-from), var(--variant-to))" }}>
```

---

## Palette Discipline Rules

Premium brands have distinctive palettes. Generic color choices instantly signal "template site." These rules prevent your brand from looking like every other SaaS.

| Rule | Why |
|------|-----|
| No purple/indigo gradients on the core brand | Universal AI-slop marker. Exception: only if purple is a deliberate brand variant. |
| No cool blue-tech palettes (steel blue, ice white) | Generic SaaS look — indistinguishable from 10,000 other products |
| Never use pure white (`#ffffff`) as page background | Use your `background` color. Pure white looks clinical; warm off-whites look premium. |
| Never use pure black (`#000000`) for text or backgrounds | Use your `text-primary` color or a near-black with warmth (e.g., `#0A0A0F`) |
| No neon/cyberpunk aesthetics (unless that IS your brand) | Off-brand for most SaaS — signals "demo project" |
| No generic AI illustrations (isometric people, blob shapes) | Signals lazy/template. Use real product screenshots or custom imagery. |
| No more than 2 gradient uses per page | Gradients lose impact when overused. Reserve for one signature element. |
| Keep warm color temperature | Even "cool" brands need warmth in their surfaces to feel premium. Cool grays feel corporate; warm grays feel intentional. |

**The "Would This Work Without Color?" Test:** Your layout, typography, and spacing should create a premium feel even in grayscale. If removing color makes it look generic, the design relies too heavily on color and not enough on structure.

---

## The Seven Pillars of Premium Design

### 1. Typography as Architecture

Typography IS the design — not decoration. It's the single biggest lever for perceived quality.

**Font Stack (configure in `tailwind.config.ts`):**
- `font-display` — your display/headline font — editorial headlines, hero text, section titles
- `font-sans` — your body sans-serif — body text, UI elements, buttons
- `font-mono` — your monospace font — code, data, technical labels

**Scale and Sizing:**

| Element | Size | Weight | Tracking | Line Height | Font |
|---------|------|--------|----------|-------------|------|
| Hero headline | `text-5xl md:text-7xl` (48-72px) | `font-bold` | `tracking-tight` (-0.025em) | `leading-[1.05]` | `font-display` |
| Section headline | `text-3xl md:text-5xl` (30-48px) | `font-bold` | `tracking-tight` | `leading-[1.1]` | `font-display` |
| Card title | `text-xl md:text-2xl` (20-24px) | `font-semibold` | `tracking-tight` | `leading-snug` | `font-sans` |
| Body text | `text-base md:text-lg` (16-18px) | `font-normal` | normal | `leading-relaxed` (1.625) | `font-sans` |
| Supporting text | `text-sm` (14px) | `font-normal` | normal | `leading-relaxed` | `font-sans` |
| Label / overline | `text-xs` (12px) | `font-medium` | `tracking-widest` (+0.1em) | `leading-normal` | `font-sans uppercase` |
| Data / mono | `text-sm` (14px) | `font-normal` | normal | `leading-normal` | `font-mono tabular-nums` |

**Key Rules:**
- Hero headline must use `font-display` — this single choice creates editorial gravity
- Minimum 3:1 scale ratio between hero headline and body text
- Negative tracking on large type (`tracking-tight` or `tracking-tighter`)
- Positive tracking on uppercase labels (`tracking-widest`)
- `text-balance` on all headings, `text-pretty` on all body text
- Max line length: `max-w-[65ch]` for body paragraphs
- Headlines: confident declarations, not questions. Under 8 words for hero.

**Typography Stare Test:** Blur your eyes. If the hierarchy doesn't read at a squint, the scale contrast is insufficient.

### 2. Layout and Spatial Composition

White space is the single strongest premium signal. It reduces cognitive load, forces focus, and communicates confidence.

**Spacing Scale (8-point grid):**

| Token | Value | Usage |
|-------|-------|-------|
| Section padding | `py-20 md:py-28 lg:py-32` (80-128px) | Between major page sections |
| Block spacing | `space-y-12 md:space-y-16` (48-64px) | Between content blocks within sections |
| Card padding | `p-6 md:p-8` (24-32px) | Internal card padding |
| Card gap | `gap-5 md:gap-6` (20-24px) | Between cards in a grid |
| Component spacing | `space-y-4` (16px) | Between related elements |
| Micro spacing | `space-y-2` (8px) | Between tightly related items |

**Container:** `max-w-7xl mx-auto px-5 md:px-8` (1280px max, 20-32px horizontal padding).

**Layout Principles:**
- Asymmetric balance over center-alignment for visual interest
- Single goal per section — never compete for attention
- Progressive disclosure — reveal information gradually
- Grid-based with intentional breaks — master the grid to break it purposefully
- Cards float: `rounded-2xl border border-[var(--color-border)] shadow-sm` with warm shadows

**Section Rhythm Pattern:**
```
Hero (dark bg, dramatic) →
Social Proof (logos, light bg) →
Problem/Agitation (surface-alt bg) →
Solution / How It Works (background bg) →
Feature Grid (alternating) →
Social Proof (testimonials, surface-alt bg) →
Pricing (background bg) →
FAQ (background bg) →
Final CTA (dark bg, mirrors hero)
```

### 3. Color and Atmosphere

Colors should feel "invented for this project." The palette should be distinctive, not generic.

**The 60-30-10 Rule:**
- 60% `background` + `surface-alt` (surfaces)
- 30% `text-primary` (text, dark sections)
- 10% `accent` (CTAs, accents, emphasis)

**Dark Section Treatment (Hero, Final CTA, Feature Showcases):**
```tsx
<section className="bg-[var(--color-text-primary)] text-white">
  {/* Content with inverted color treatment */}
  {/* Body text: text-white/75 */}
  {/* Muted text: text-white/60 */}
  {/* Borders: border-white/10 */}
  {/* Cards: bg-white/[0.05] backdrop-blur-xl border border-white/[0.08] */}
</section>
```

**Light Section Treatment (Default):**
```tsx
<section className="bg-[var(--color-background)]">
  {/* Text: text-[var(--color-text-primary)] */}
  {/* Muted: text-slate-500 */}
  {/* Cards: bg-white rounded-2xl border border-[var(--color-border)] shadow-sm */}
</section>
```

**Alternating Section Treatment:**
```tsx
<section className="bg-[var(--color-surface-alt)]">
  {/* Surface-alt background for visual rhythm */}
</section>
```

**Off-White Rule:** NEVER use `bg-white` as a page background. Always use your `background` color. Pure white looks clinical; a warm or tinted off-white looks premium. Cards CAN use `bg-white` because they sit above the tinted surface, creating layered depth.

**Brand-Colored Shadows (Premium Detail):**
```tsx
{/* Accent shadow on CTAs */}
<button className="shadow-[0_4px_16px_var(--color-accent)/0.2]">

{/* Warm shadow on cards — use text-primary at very low opacity */}
<div className="shadow-[0_2px_12px_var(--color-text-primary)/0.06]">

{/* Success shadow on trust states */}
<div className="shadow-[0_4px_16px_var(--color-success)/0.15]">
```

**Note:** If your CSS setup doesn't support `var()` in shadow shorthand, use `rgba()` with your actual hex values. The principle is the same: shadows should be tinted with your brand colors, not generic gray.

### 4. Motion and Animation

Every animation must answer "why does this move?" Motion is a hierarchy tool, not decoration.

**Easing (Custom — NEVER use default `ease` or `linear`):**

| Name | Value | Use |
|------|-------|-----|
| Expo Out | `cubic-bezier(0.16, 1, 0.3, 1)` | Primary entrance, page elements |
| Quart Out | `cubic-bezier(0.25, 1, 0.5, 1)` | Secondary entrance, cards |
| Expo In-Out | `cubic-bezier(0.87, 0, 0.13, 1)` | Scroll-triggered transforms |
| Spring | `cubic-bezier(0.22, 1, 0.36, 1)` | Interactive feedback, buttons |

**Duration Scale:**

| Type | Duration | Use |
|------|----------|-----|
| Micro | 100-150ms | Hover color, opacity |
| Interaction | 150-250ms | Button press, toggle, menu |
| Transition | 250-400ms | Card entrance, section reveal |
| Emphasis | 400-600ms | Hero entrance, scroll animations |
| Never exceed | 600ms | UI interactions |

**Page Load Choreography (Hero):**

```
0-200ms:   Background gradient/orbs fade in (opacity 0→1)
200-400ms: Overline label slides up + fades in
300-600ms: Hero headline slides up + fades in (stagger per line if multi-line)
400-700ms: Subheadline fades in
500-800ms: CTA buttons fade in + slide up
600-900ms: Navigation fades in
800-1200ms: Supporting visuals (product screenshot, animation) enter
```

Implement via CSS `@keyframes fadeUp` with `animation-delay`:

```tsx
<div className="animate-[fadeUp_0.6s_ease-out_0.2s_both]">Overline</div>
<h1 className="animate-[fadeUp_0.7s_ease-out_0.3s_both]">Headline</h1>
<p className="animate-[fadeUp_0.6s_ease-out_0.4s_both]">Subheadline</p>
<div className="animate-[fadeUp_0.6s_ease-out_0.5s_both]">CTAs</div>
```

**Required `@keyframes` in your `globals.css`:**

```css
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(16px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes marquee {
  from { transform: translateX(0); }
  to { transform: translateX(-50%); }
}

@keyframes shimmer {
  from { transform: translateX(-100%); }
  to { transform: translateX(100%); }
}
```

**Scroll-Triggered Animations:**

Use Intersection Observer (lightweight) or GSAP ScrollTrigger (advanced). Elements should fade in + translate up on scroll:

```tsx
"use client";
import { useRef, useEffect, useState } from "react";

function useInView(threshold = 0.15) {
  const ref = useRef<HTMLDivElement>(null);
  const [isInView, setIsInView] = useState(false);
  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    const obs = new IntersectionObserver(
      ([entry]) => { if (entry.isIntersecting) { setIsInView(true); obs.disconnect(); } },
      { threshold }
    );
    obs.observe(el);
    return () => obs.disconnect();
  }, [threshold]);
  return { ref, isInView };
}

// Usage
function Section() {
  const { ref, isInView } = useInView();
  return (
    <div
      ref={ref}
      className={`transition-all duration-700 ${
        isInView
          ? "opacity-100 translate-y-0"
          : "opacity-0 translate-y-8"
      }`}
      style={{ transitionTimingFunction: "cubic-bezier(0.16, 1, 0.3, 1)" }}
    >
      {/* Content */}
    </div>
  );
}
```

**Staggered Card Grid Reveal:**

```tsx
{features.map((f, i) => (
  <div
    key={f.title}
    ref={ref}
    className={`transition-all duration-700 ${isInView ? "opacity-100 translate-y-0" : "opacity-0 translate-y-8"}`}
    style={{
      transitionDelay: `${i * 80}ms`,
      transitionTimingFunction: "cubic-bezier(0.16, 1, 0.3, 1)",
    }}
  >
    {/* Card content */}
  </div>
))}
```

**Logo Carousel (Social Proof):**

```tsx
<div className="overflow-hidden">
  <div className="flex animate-[marquee_30s_linear_infinite]">
    {[...logos, ...logos].map((logo, i) => (
      <div key={i} className="flex-shrink-0 px-8 opacity-50 hover:opacity-100 transition-opacity">
        <img src={logo.src} alt={logo.name} className="h-8 w-auto grayscale" />
      </div>
    ))}
  </div>
</div>
```

**GPU-Only Animations:** Only animate `transform` and `opacity`. Never animate `width`, `height`, `margin`, `padding`, `background-color`, `blur()`.

**Reduced Motion:** Always wrap animations:
```tsx
className="motion-safe:animate-[fadeUp_0.6s_ease-out_both] motion-reduce:opacity-100"
```

### 5. Hero Section Patterns

The hero is the most important piece of real estate. Visitors form quality judgments in 50 milliseconds.

**5-Second Test:** In 5 seconds a visitor must understand: What is this? Who is it for? What should I do next?

**Hero Anatomy:**

```
┌─────────────────────────────────────────────┐
│  [Overline Badge]  "[Your Category]"        │
│                                             │
│  [Hero Headline — font-display]             │
│  "[Your Value Prop]"                        │
│                                             │
│  [Subheadline — font-sans, 60-70% opacity]  │
│  Supporting copy that expands on the value  │
│  proposition with specifics.                │
│                                             │
│  [Primary CTA]  [Secondary CTA]            │
│  "[Your CTA]"   "Watch Demo"               │
│                                             │
│  [Social proof snippet]                     │
│  "Trusted by N+ teams"  [logos]            │
└─────────────────────────────────────────────┘
```

**Dark Hero (Editorial, Dramatic):**

```tsx
<section className="relative bg-[var(--color-text-primary)] overflow-hidden">
  {/* Warm ambient glow (optional) */}
  <div className="absolute inset-0 pointer-events-none" aria-hidden="true">
    <div className="absolute top-[-10%] right-[-5%] h-[500px] w-[500px] rounded-full bg-[var(--color-accent)]/8 blur-[120px]" />
  </div>

  <div className="relative mx-auto max-w-7xl px-5 md:px-8 py-24 md:py-36 text-center">
    {/* Overline */}
    <span className="inline-flex items-center rounded-full px-4 py-1.5 text-xs font-medium tracking-widest uppercase text-[var(--color-accent)] bg-[var(--color-accent)]/10 border border-[var(--color-accent)]/20 animate-[fadeUp_0.6s_ease-out_0.1s_both]">
      [Your Category]
    </span>

    {/* Headline */}
    <h1 className="mt-8 text-5xl md:text-7xl font-bold tracking-tight text-white font-display text-balance leading-[1.05] animate-[fadeUp_0.7s_ease-out_0.25s_both]">
      [Your Value Prop.]
    </h1>

    {/* Subheadline */}
    <p className="mt-6 text-lg md:text-xl text-white/70 max-w-2xl mx-auto text-pretty leading-relaxed animate-[fadeUp_0.6s_ease-out_0.4s_both]">
      [Supporting copy that expands on the value proposition with specific, concrete details.]
    </p>

    {/* Dual CTA */}
    <div className="mt-10 flex flex-col sm:flex-row items-center justify-center gap-4 animate-[fadeUp_0.6s_ease-out_0.55s_both]">
      <a href="/[cta-route]" className="rounded-full px-8 py-4 text-sm font-semibold text-white bg-[var(--color-accent)] hover:brightness-110 shadow-[0_4px_20px_var(--color-accent)/0.25] hover:shadow-[0_6px_28px_var(--color-accent)/0.35] transition-all duration-200">
        [Your CTA]
      </a>
      <a href="/[secondary-route]" className="rounded-full px-8 py-4 text-sm font-semibold text-white/85 hover:text-white bg-white/[0.06] hover:bg-white/[0.10] border border-white/[0.10] hover:border-white/[0.15] transition-all duration-200">
        [Secondary Action]
      </a>
    </div>

    {/* Social proof snippet */}
    <div className="mt-12 flex items-center justify-center gap-3 text-sm text-white/50 animate-[fadeUp_0.6s_ease-out_0.7s_both]">
      <span>[Trust metric 1]</span>
      <span className="h-1 w-1 rounded-full bg-white/30" />
      <span>[Trust metric 2]</span>
      <span className="h-1 w-1 rounded-full bg-white/30" />
      <span>[Trust metric 3]</span>
    </div>
  </div>
</section>
```

**More Authoritative Variant (Executive Feel):**

Same structure but:
- More whitespace (py-28 md:py-40)
- Heavier use of dark backgrounds — more "executive" feel
- No emoji, no playful language
- Slightly more elevated card shadows — cards feel more substantial
- CTA: specific to business outcome ("Start Free Trial" + "See Product Catalog")

**Brand Variant Hero (Gradient, Warmer, More Personal):**

```tsx
<section className="relative overflow-hidden" style={{ background: "linear-gradient(135deg, var(--variant-from), var(--variant-to))" }}>
  <div className="relative mx-auto max-w-7xl px-5 md:px-8 py-24 md:py-36 text-center">
    <h1 className="text-5xl md:text-7xl font-bold tracking-tight text-white font-display leading-[1.05]">
      [Variant Headline.]
    </h1>
    <p className="mt-6 text-lg text-white/80 max-w-2xl mx-auto">
      [Variant supporting copy — more personal, more emotional.]
    </p>
    <a href="/[variant-cta-route]" className="mt-10 inline-flex rounded-full px-8 py-4 text-sm font-semibold text-[var(--color-text-primary)] bg-white hover:bg-white/90 shadow-lg transition">
      [Variant CTA]
    </a>
  </div>
</section>
```

### 6. Conversion Architecture

Every page is a conversion machine. Design serves the conversion goal.

**Page Structure (Problem → Solution → Proof):**

```
1. HERO — Value prop + primary CTA (above fold)
2. SOCIAL PROOF — Logo carousel or trust metrics (immediately after hero)
3. PROBLEM — Agitate the pain ("[Describe the frustration your users feel today]")
4. SOLUTION — How it works (3-step process with icons)
5. FEATURES — Benefit-led cards (not feature lists)
6. SOCIAL PROOF — Named testimonials with photos + specific metrics
7. PRICING — Clear tiers with one recommended (accent highlight)
8. FAQ — Objection handling disguised as Q&A
9. FINAL CTA — Dark section that mirrors hero energy
```

**CTA Design Rules:**
- Button text = specific verb + benefit ("[Action] — [Benefit]" not "Get Started")
- One primary CTA per viewport, repeated every 2-3 scroll depths
- Risk reversal micro-copy near every CTA ("No credit card required", "Cancel anytime")
- Primary: `rounded-full` pill, accent bg, brand-colored shadow
- Secondary: `rounded-full` pill, ghost/outline, white text on dark / text-primary on light
- Never use "Submit", "Click Here", or "Learn More"

**Social Proof Hierarchy (strongest → weakest):**
1. Named case studies with specific metrics ("Saved 12 hours/week")
2. Named testimonials with photo + title + company
3. Company logos (recognizable names)
4. Quantified trust ("2,000+ teams", "99.9% uptime")
5. Media mentions ("Named Best X by Forbes")
6. Star ratings

**Trust Signal Placement:**
- After hero: logo carousel or quantified metric
- Near pricing: testimonial from a paying customer
- Near CTA: risk reversal ("Money-back guarantee", "No credit card")
- Footer: security badges, privacy policy link, contact info

### 7. Micro-Interactions and Craft

The gap between 8/10 and 10/10 is entirely in the details.

**Button Hover States (Three Visual Layers):**
```tsx
{/* Primary CTA — background + shadow + subtle transform */}
<button className="rounded-full px-8 py-4 text-sm font-semibold text-white bg-[var(--color-accent)]
  shadow-[0_4px_16px_var(--color-accent)/0.2]
  hover:brightness-110
  hover:shadow-[0_6px_24px_var(--color-accent)/0.3]
  hover:-translate-y-0.5
  active:translate-y-0 active:shadow-[0_2px_8px_var(--color-accent)/0.2]
  transition-all duration-200"
  style={{ transitionTimingFunction: "cubic-bezier(0.22, 1, 0.36, 1)" }}>
  [Your CTA]
</button>
```

**Card Hover (Lift + Border Brighten):**
```tsx
<div className="rounded-2xl border border-[var(--color-border)] bg-white p-6 shadow-sm
  hover:shadow-[0_8px_24px_var(--color-text-primary)/0.08]
  hover:-translate-y-1 hover:border-[var(--color-border)]/80
  transition-all duration-300"
  style={{ transitionTimingFunction: "cubic-bezier(0.25, 1, 0.5, 1)" }}>
```

**Link Underline Animation:**
```tsx
<a className="relative text-[var(--color-accent)] hover:brightness-110 transition-colors">
  Learn more
  <span className="absolute -bottom-0.5 left-0 h-px w-0 bg-[var(--color-accent)] transition-all duration-300 group-hover:w-full" />
</a>
```

**Focus States (Non-Negotiable):**
```tsx
className="focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--color-accent)]/50 focus-visible:ring-offset-2 focus-visible:ring-offset-[var(--color-background)]"
```

**Custom Selection Color:**
```css
::selection {
  background: var(--color-accent) / 0.2; /* or use rgba with your accent hex */
  color: var(--color-text-primary);
}
```

**Typed Text Effect (for hero — cycle through product examples):**
```tsx
// Show rotating examples of what your product does
// Use a simple interval with opacity transition, not a typewriter library
```

**Required States for Every Interactive Component:**
1. Default
2. Hover (color shift + shadow + subtle transform)
3. Focus-visible (ring)
4. Active/pressed (translate-y-0, reduced shadow)
5. Loading (skeleton or spinner)
6. Disabled (opacity-50, cursor-not-allowed)
7. Error (danger border + message)
8. Empty (illustration + clear next action)
9. Success (success color confirmation)

---

## Component Patterns

### Card (Light Background)

```tsx
<div className="rounded-2xl border border-[var(--color-border)] bg-white p-6 md:p-8 shadow-[0_2px_12px_var(--color-text-primary)/0.04] hover:shadow-[0_8px_24px_var(--color-text-primary)/0.08] hover:-translate-y-1 transition-all duration-300">
  <div className="inline-flex h-10 w-10 items-center justify-center rounded-xl bg-[var(--color-accent)]/10 text-[var(--color-accent)] mb-4">
    {/* Icon */}
  </div>
  <h3 className="text-xl font-semibold text-[var(--color-text-primary)] tracking-tight">{title}</h3>
  <p className="mt-2 text-sm text-slate-500 leading-relaxed">{description}</p>
</div>
```

### Card (Dark Background — Glass)

```tsx
<div className="rounded-2xl border border-white/[0.08] bg-white/[0.05] backdrop-blur-xl p-6 md:p-8 shadow-[0_8px_32px_rgba(0,0,0,0.2)] hover:-translate-y-1 hover:border-white/[0.12] transition-all duration-300">
  <h3 className="text-xl font-semibold text-white tracking-tight">{title}</h3>
  <p className="mt-2 text-sm text-white/70 leading-relaxed">{description}</p>
</div>
```

### Featured Card (Accent Glow — Highlighted Tier)

```tsx
<div className="relative rounded-2xl border border-[var(--color-accent)]/25 bg-white p-6 md:p-8 shadow-[0_4px_24px_var(--color-accent)/0.1]">
  <span className="absolute -top-3 left-6 inline-flex items-center rounded-full px-3 py-1 text-xs font-semibold text-white bg-[var(--color-accent)] shadow-sm">
    Most Popular
  </span>
  {/* Card content */}
</div>
```

### Section Header

```tsx
<div className="text-center max-w-2xl mx-auto mb-16">
  <span className="text-xs font-medium tracking-widest uppercase text-[var(--color-accent)]">
    [Section Label]
  </span>
  <h2 className="mt-3 text-3xl md:text-5xl font-bold tracking-tight text-[var(--color-text-primary)] font-display text-balance">
    [Section Headline]
  </h2>
  <p className="mt-4 text-lg text-slate-500 text-pretty leading-relaxed">
    [Section supporting text — one to two sentences.]
  </p>
</div>
```

### Sticky Navbar

```tsx
<header className="sticky top-0 z-50 border-b border-[var(--color-border)]/80 bg-[var(--color-background)]/80 backdrop-blur-md">
  <nav className="mx-auto max-w-7xl flex items-center justify-between px-5 md:px-8 h-16">
    {/* Logo */}
    <a href="/" className="text-[var(--color-text-primary)] font-display font-bold text-lg tracking-tight">
      [Your Logo]
    </a>

    {/* Nav links */}
    <div className="hidden md:flex items-center gap-1">
      <a className="px-3 py-2 text-sm text-slate-500 hover:text-[var(--color-text-primary)] rounded-lg hover:bg-[var(--color-surface-alt)] transition" href="#">
        Features
      </a>
      {/* ... */}
    </div>

    {/* CTAs */}
    <div className="flex items-center gap-3">
      <a className="text-sm text-slate-500 hover:text-[var(--color-text-primary)] transition hidden sm:block" href="/login">
        Sign in
      </a>
      <a className="rounded-full px-5 py-2.5 text-sm font-semibold text-white bg-[var(--color-accent)] hover:brightness-110 shadow-[0_2px_8px_var(--color-accent)/0.2] transition" href="/[cta-route]">
        [Your CTA]
      </a>
    </div>
  </nav>
</header>
```

### How It Works (3-Step Process)

```tsx
<section className="bg-[var(--color-background)] py-20 md:py-28">
  <div className="mx-auto max-w-7xl px-5 md:px-8">
    {/* Section header */}
    <div className="text-center max-w-2xl mx-auto mb-16">
      <h2 className="text-3xl md:text-5xl font-bold tracking-tight text-[var(--color-text-primary)] font-display">
        How It Works
      </h2>
    </div>

    <div className="grid gap-8 md:grid-cols-3">
      {steps.map((step, i) => (
        <div key={step.title} className="text-center">
          <div className="inline-flex h-14 w-14 items-center justify-center rounded-2xl bg-[var(--color-accent)]/10 text-[var(--color-accent)] text-xl font-bold font-display mb-5">
            {i + 1}
          </div>
          <h3 className="text-xl font-semibold text-[var(--color-text-primary)] tracking-tight">{step.title}</h3>
          <p className="mt-2 text-sm text-slate-500 leading-relaxed max-w-xs mx-auto">{step.description}</p>
        </div>
      ))}
    </div>
  </div>
</section>
```

### Testimonial Card

```tsx
<div className="rounded-2xl border border-[var(--color-border)] bg-white p-6 md:p-8">
  <div className="flex items-center gap-1 mb-4">
    {[...Array(5)].map((_, i) => (
      <svg key={i} className="h-4 w-4 text-[var(--color-accent)] fill-current" viewBox="0 0 20 20">
        <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
      </svg>
    ))}
  </div>
  <blockquote className="text-[var(--color-text-primary)] leading-relaxed">
    "{testimonial.quote}"
  </blockquote>
  <div className="mt-4 flex items-center gap-3">
    <img src={testimonial.avatar} alt="" className="h-10 w-10 rounded-full object-cover" />
    <div>
      <div className="text-sm font-semibold text-[var(--color-text-primary)]">{testimonial.name}</div>
      <div className="text-xs text-slate-400">{testimonial.title}, {testimonial.company}</div>
    </div>
  </div>
</div>
```

### FAQ Section (Accordion)

Use shadcn/ui `Accordion` component:
```tsx
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";

<section className="bg-[var(--color-background)] py-20 md:py-28">
  <div className="mx-auto max-w-3xl px-5 md:px-8">
    <h2 className="text-3xl md:text-4xl font-bold tracking-tight text-[var(--color-text-primary)] font-display text-center mb-12">
      Frequently Asked Questions
    </h2>
    <Accordion type="single" collapsible className="space-y-3">
      {faqs.map((faq, i) => (
        <AccordionItem key={i} value={`faq-${i}`} className="rounded-xl border border-[var(--color-border)] bg-white px-6 data-[state=open]:shadow-sm transition-shadow">
          <AccordionTrigger className="text-left text-[var(--color-text-primary)] font-semibold py-5 hover:no-underline">
            {faq.question}
          </AccordionTrigger>
          <AccordionContent className="text-slate-500 leading-relaxed pb-5">
            {faq.answer}
          </AccordionContent>
        </AccordionItem>
      ))}
    </Accordion>
  </div>
</section>
```

### Final CTA (Dark Mirror of Hero)

```tsx
<section className="bg-[var(--color-text-primary)] py-20 md:py-28">
  <div className="mx-auto max-w-3xl px-5 md:px-8 text-center">
    <h2 className="text-3xl md:text-5xl font-bold tracking-tight text-white font-display text-balance">
      [Closing Headline That Inspires Action]
    </h2>
    <p className="mt-4 text-lg text-white/70 text-pretty">
      [Risk reversal + benefit restatement. Keep it concise.]
    </p>
    <a href="/[cta-route]" className="mt-8 inline-flex rounded-full px-8 py-4 text-sm font-semibold text-white bg-[var(--color-accent)] hover:brightness-110 shadow-[0_4px_20px_var(--color-accent)/0.25] transition">
      [Your CTA]
    </a>
    <p className="mt-4 text-xs text-white/40">[Risk reversal micro-copy]</p>
  </div>
</section>
```

---

## Anti-Patterns (What Kills Premium Perception)

### Visual Anti-Patterns

| Anti-Pattern | Fix |
|-------------|-----|
| Pure white page backgrounds | Use your `background` color (warm off-white) |
| Pure black text/backgrounds | Use your `text-primary` color or a near-black with warmth |
| Purple/indigo gradients (unless brand variant) | Use your brand accent and warm tones |
| System fonts (Inter/Roboto/Arial) as headline font | Use your display font (`font-display`) |
| Default browser easing (`ease`, `linear`) | Use custom cubic-beziers from Pillar 4 |
| Center-aligning everything | Mix alignment, use asymmetry intentionally |
| Equal spacing everywhere | Vary spacing to create rhythm and hierarchy |
| Oversized padding on everything | Use the 8pt spacing scale consistently |
| Stock photos / generic AI illustrations | Use real product screenshots or custom imagery |
| Rounded-everything (`rounded-3xl` on all elements) | Use `rounded-2xl` for cards, `rounded-full` for pills, `rounded-xl` for buttons |
| Shadow-heavy design | Subtle warm shadows only, brand-colored for CTAs |
| Gradient text on everything | Reserve for one signature element max |

### Typography Anti-Patterns

| Anti-Pattern | Fix |
|-------------|-----|
| Same font for headlines and body | Display font for headlines, sans font for body |
| Small type scale (1.2x between levels) | Minimum 3:1 ratio hero-to-body |
| No tracking adjustment on large type | `tracking-tight` or `tracking-tighter` on hero text |
| Body text below 16px | Minimum `text-base` (16px) |
| Line length > 80 characters | `max-w-[65ch]` on prose blocks |
| All caps body text | Caps only for small labels with `tracking-widest` |
| Questions as headlines | Confident declarations: "[Benefit Statement.]" not "Want [benefit]?" |

### Motion Anti-Patterns

| Anti-Pattern | Fix |
|-------------|-----|
| Animating everything simultaneously | Choreograph with staggered delays |
| Entrance animation on every revisit | Trigger once via IntersectionObserver |
| Spinner for sub-1s operations | Skeleton loader or optimistic update |
| Bouncing / spinning / flashy effects | Subtle translate + opacity only |
| Animating width/height/margin | Only animate transform + opacity |
| No reduced-motion support | `motion-safe:` prefix or `prefers-reduced-motion` query |
| Parallax on text | Parallax only on decorative elements |

### Conversion Anti-Patterns

| Anti-Pattern | Fix |
|-------------|-----|
| "Get Started" / "Learn More" / "Submit" | Specific verb + benefit: "[Action] — [Benefit]" |
| No social proof above fold | Logo carousel or metric immediately after hero |
| Multiple competing CTAs per viewport | One primary per viewport |
| No risk reversal near CTA | "No credit card required" / "Cancel anytime" |
| Failing the 5-second test | Hero must answer: What? Who? What next? |
| Generic testimonials ("Great product!") | Named person + specific metric + photo |

---

## Performance Requirements

Premium means fast. A 1-second delay decreases conversions 7%.

| Metric | Target | How |
|--------|--------|-----|
| LCP | < 2.5s | Optimize hero image, preload fonts, avoid layout shift |
| FID | < 100ms | Minimal JS in initial load, defer non-critical scripts |
| CLS | < 0.1 | Fixed dimensions on images, font-display: swap |
| TTI | < 3.5s | Code-split pages, lazy-load below-fold sections |

**Font Loading:**
```tsx
// In layout.tsx — preload your display and body fonts via next/font (or equivalent)
// Use font-display: swap to prevent invisible text during load
```

**Image Optimization:**
- Use `next/image` (or equivalent optimized image component) with `priority` on hero images
- WebP/AVIF format via automatic optimization
- Responsive `srcset` with appropriate `sizes`
- Lazy load everything below fold

**Animation Performance:**
- Only animate `transform` and `opacity` (GPU-composited)
- `will-change: transform` only during active animation
- Cap at 3-4 simultaneously animating elements per viewport
- Pause off-screen animations (IntersectionObserver)

---

## Quality Checklist

### Before Shipping Any Page

**Design Quality:**
- [ ] Uses display font for headlines (not body/sans font)
- [ ] Brand `background` color, not pure white
- [ ] Brand-colored shadows on CTAs (accent glow)
- [ ] Custom easing on all transitions (no default `ease`)
- [ ] 80px+ section padding (generous whitespace)
- [ ] Passes the "typography stare test" (hierarchy reads at a squint)
- [ ] No off-brand colors (palette discipline rules followed)
- [ ] Maximum 2 typefaces visible

**Conversion:**
- [ ] Passes 5-second test (what, who, what next)
- [ ] Social proof within first 2 viewports
- [ ] Primary CTA repeated every 2-3 scroll depths
- [ ] Risk reversal near every CTA
- [ ] Specific verb + benefit on all button text
- [ ] Named testimonials with photos (not anonymous)

**Animation:**
- [ ] Hero load choreography (staggered entrance)
- [ ] Scroll-triggered reveals on sections below fold
- [ ] All transitions use custom cubic-bezier easing
- [ ] `motion-safe:` prefix on all animations
- [ ] GPU-only properties (transform, opacity)
- [ ] Logo carousel for social proof (if applicable)

**Accessibility:**
- [ ] WCAG AA contrast on all text (4.5:1 normal, 3:1 large)
- [ ] Focus-visible rings on all interactive elements
- [ ] Semantic HTML (`section`, `nav`, `header`, `main`, `article`)
- [ ] `text-balance` on headings, `text-pretty` on body
- [ ] `aria-hidden="true"` on decorative elements
- [ ] Keyboard navigable (Tab, Enter, Space, Escape)
- [ ] Touch targets >= 44px on mobile

**Responsive:**
- [ ] Works at 320px, 768px, 1024px, 1440px
- [ ] Mobile: single column, 16px+ body text, thumb-friendly CTAs
- [ ] No horizontal scroll at any breakpoint
- [ ] Images responsive with proper `sizes` attribute

**Performance:**
- [ ] LCP < 2.5s
- [ ] Hero image uses `priority` prop
- [ ] Fonts preloaded
- [ ] Below-fold content lazy loaded
- [ ] No layout shift on load

**Brand Consistency:**
- [ ] Correct brand treatment applied (core vs. variant if applicable)
- [ ] Accent color for action, success color for trust, text-primary for text
- [ ] Brand variant styling ONLY on variant-scoped pages
- [ ] Display font for editorial headlines
- [ ] Sans font for all body/UI text
- [ ] Warm color temperature throughout (no unintentional cool grays)
