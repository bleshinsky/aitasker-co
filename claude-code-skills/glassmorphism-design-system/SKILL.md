---
name: glassmorphism-design-system
description: >
  Glassmorphism design system for building frosted-glass UI components. Use when building
  hero sections, feature grids, pricing cards, navbars, modals, or landing pages with blur,
  transparency, and layered depth effects. Works with any dark-themed project using
  Tailwind CSS and React/Next.js. Covers glass tokens, component patterns, accessibility,
  performance budgets, and anti-patterns.
---

# Glassmorphism Design System

Premium frosted-glass UI for dark-themed projects using Tailwind CSS, React, and Next.js.

**Prerequisites:** Tailwind CSS, React/Next.js. This skill requires a brand configuration file — see `brand-config.example.md` for the template. Copy it to `.claude/brand-config.md` in your project and fill in your colors and fonts.

---

## When to Use

- Hero sections, feature grids, pricing cards, profile cards, team cards
- Sticky navbars, modals, overlays, command palettes
- Landing pages, category pages, marketing pages
- Any request mentioning "glass", "frosted", "blur", "translucent", "premium UI", "depth"
- Dark-mode-first sections that need visual sophistication

## When NOT to Use

- Data-dense tables, forms, admin dashboards — use solid surfaces
- Light-mode content pages (blog posts, docs) — glass needs contrast
- Stacking glass on glass — never layer translucent elements

---

## Brand Configuration

**Before using this skill**, read the brand configuration file to understand the project's color palette, fonts, and brand tokens. The skill uses these CSS variables throughout all component patterns.

**Look for the config file at:** `.claude/brand-config.md`, `brand-config.md`, or the project's design tokens.

If no brand config exists, prompt the user to create one. A template is provided at `brand-config.example.md` in this skill's directory. The template defines 8 color roles (`--glass-dark`, `--glass-accent`, `--glass-glow-warm`, etc.) and 3 font slots (`font-display`, `font-sans`, `font-mono`).

> **Rule:** Never hardcode hex values in component code. Always reference CSS variables so the brand palette is the single source of truth.
```

---

## Glass Design Tokens

Add these to your `globals.css`. These are universal values that work across any brand palette.

```css
:root {
  /* ── Glass surfaces ── */
  --glass-bg-subtle:    rgba(255, 255, 255, 0.03);
  --glass-bg-light:     rgba(255, 255, 255, 0.05);
  --glass-bg:           rgba(255, 255, 255, 0.08);
  --glass-bg-medium:    rgba(255, 255, 255, 0.12);
  --glass-bg-heavy:     rgba(255, 255, 255, 0.18);

  /* ── Glass borders ── */
  --glass-border-subtle: rgba(255, 255, 255, 0.06);
  --glass-border:        rgba(255, 255, 255, 0.10);
  --glass-border-strong: rgba(255, 255, 255, 0.18);

  /* ── Glass shadows ── */
  --glass-shadow:          0 4px 24px rgba(0, 0, 0, 0.15);
  --glass-shadow-elevated: 0 8px 40px rgba(0, 0, 0, 0.25);
  --glass-shadow-glow-warm:  0 0 40px color-mix(in srgb, var(--glass-glow-warm) 15%, transparent);
  --glass-shadow-glow-cool:  0 0 40px color-mix(in srgb, var(--glass-glow-cool) 15%, transparent);

  /* ── Glass radius ── */
  --glass-radius:    12px;
  --glass-radius-lg: 20px;
  --glass-radius-xl: 24px;

  /* ── Glass blur ── */
  --glass-blur-light:  8px;
  --glass-blur:        16px;
  --glass-blur-strong: 24px;
  --glass-blur-heavy:  40px;
}
```

---

## Core Principles

### 1. Restraint Over Excess

Glass is a **hierarchy tool**, not a layout system. Apply to 2-4 key elements per view. The rest should be solid surfaces. The best glassmorphism sites (Superhuman, Origin, byCrawford) use glass sparingly — only on interactive overlays, nav bars, and hero cards.

**The #1 mistake is applying glass to everything.** When every element is translucent, nothing has visual priority. Reserve glass for elements that need to feel elevated or floating.

### 2. Dark Backgrounds Are Required

Glass effects only work over rich, colorful, or dark backgrounds. On light surfaces, glass becomes invisible. For glass sections:

```tsx
// CORRECT — dark canvas for glass
<section className="bg-[var(--glass-dark)]">
  {/* glass elements here */}
</section>

// ALSO CORRECT — gradient canvas
<section className="bg-gradient-to-br from-[var(--glass-dark)] via-[var(--glass-dark-alt)] to-[var(--glass-dark)]">
  {/* glass elements here */}
</section>

// WRONG — glass on light surface (effect disappears)
<section className="bg-white">
  {/* glass is invisible here */}
</section>
```

### 3. Brand-Colored Glow, Not Generic Gradients

The ambient glow orbs behind glass content should use your brand colors — not generic cyan/purple/pink gradients that look like every AI landing page.

```tsx
// CORRECT — your brand glow orbs via CSS variables
<div className="absolute -top-40 -right-40 h-[500px] w-[500px] rounded-full bg-[var(--glass-glow-warm)]/15 blur-[80px]" />
<div className="absolute -bottom-40 -left-40 h-[400px] w-[400px] rounded-full bg-[var(--glass-glow-cool)]/12 blur-[80px]" />

// WRONG — generic gradients with no brand identity
<div className="bg-cyan-500/30 blur-3xl" />
<div className="bg-purple-500/30 blur-3xl" />
```

### 4. Two-Tier Blur Strategy

Use **heavier blur for primary elements** (cards, modals) and **lighter blur for secondary elements** (nav, buttons):

| Element | Blur | Background | Border |
|---------|------|------------|--------|
| **Card / Hero panel** | `backdrop-blur-xl` (24px) | `bg-white/[0.05]` | `border-white/[0.08]` |
| **Modal** | `backdrop-blur-xl` (24px) | `bg-white/[0.08]` | `border-white/[0.10]` |
| **Sticky navbar** | `backdrop-blur-md` (12px) | `bg-white/[0.05]` | `border-white/[0.08]` |
| **Button (primary)** | `backdrop-blur-sm` (4px) | `bg-white/[0.10]` | `border-white/[0.12]` |
| **Button (secondary)** | `backdrop-blur-sm` (4px) | `bg-black/20` | `border-white/[0.08]` |
| **Badge / chip** | none | `bg-white/[0.06]` | `border-white/[0.06]` |

### 5. Text Contrast Is Non-Negotiable

Glass surfaces make text contrast unpredictable. Rules:

- **Headings:** `text-white` or `text-white/95` — always full or near-full opacity
- **Body text:** `text-white/75` minimum — never below 70% opacity
- **Muted/secondary:** `text-white/60` — acceptable only for labels, not body copy
- **Accent text:** Use `text-[var(--glass-accent)]` for highlights
- **Never use** `text-white/40` or lower on glass — it's unreadable

---

## Component Patterns

### Glass Card

The workhorse component. Used for feature grids, pricing tiers, profile cards, team cards.

```tsx
<div className="rounded-2xl border border-white/[0.08] bg-white/[0.05] backdrop-blur-xl shadow-[0_8px_32px_rgba(0,0,0,0.2)] p-6 md:p-8">
  <h3 className="text-xl font-semibold text-white">Card Title</h3>
  <p className="mt-2 text-white/75">Card description text with sufficient contrast.</p>
</div>
```

**Hover state** — subtle lift + border brightening:
```tsx
<div className="rounded-2xl border border-white/[0.08] bg-white/[0.05] backdrop-blur-xl shadow-[0_8px_32px_rgba(0,0,0,0.2)] p-6 transition-all duration-300 hover:-translate-y-1 hover:border-white/[0.15] hover:shadow-[0_16px_48px_rgba(0,0,0,0.25)]">
```

**Glow variant** — for featured/highlighted cards:
```tsx
<div className="relative rounded-2xl border border-white/[0.08] bg-white/[0.05] backdrop-blur-xl p-6">
  {/* Accent glow ring behind the card */}
  <div className="absolute -inset-px rounded-2xl bg-gradient-to-br from-[var(--glass-accent)]/20 via-transparent to-[var(--glass-glow-cool)]/10 -z-10 blur-sm" />
  {/* Card content */}
</div>
```

### Glass Navbar (Sticky)

Lighter blur to stay performant during scroll.

```tsx
<header className="sticky top-0 z-50">
  <div className="mx-auto max-w-7xl px-4 pt-4">
    <nav className="rounded-2xl border border-white/[0.08] bg-white/[0.05] backdrop-blur-md shadow-[0_4px_24px_rgba(0,0,0,0.15)]">
      <div className="flex items-center justify-between px-5 py-3">
        {/* Logo */}
        <a href="/" className="flex items-center gap-2 text-white font-semibold">
          <span className="inline-flex h-9 w-9 items-center justify-center rounded-xl border border-white/[0.10] bg-white/[0.06] backdrop-blur-sm">
            <span className="text-sm font-bold text-[var(--glass-accent)]">[B]</span>
          </span>
          <span className="text-sm tracking-tight">[Brand]</span>
        </a>

        {/* Nav links */}
        <div className="hidden md:flex items-center gap-1">
          <a className="rounded-xl px-3 py-2 text-sm text-white/70 hover:text-white hover:bg-white/[0.06] transition" href="#">Features</a>
          <a className="rounded-xl px-3 py-2 text-sm text-white/70 hover:text-white hover:bg-white/[0.06] transition" href="#">Pricing</a>
        </div>

        {/* CTA */}
        <button className="rounded-xl px-4 py-2 text-sm font-medium text-white bg-[var(--glass-accent)]/90 hover:bg-[var(--glass-accent)] border border-[var(--glass-accent)]/30 transition">
          [Your CTA]
        </button>
      </div>
    </nav>
  </div>
</header>
```

### Glass Modal / Overlay

```tsx
{/* Backdrop with blur */}
<div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40 backdrop-blur-sm">
  {/* Modal panel */}
  <div className="w-full max-w-lg rounded-2xl border border-white/[0.10] bg-white/[0.08] backdrop-blur-xl shadow-[0_8px_40px_rgba(0,0,0,0.3)] p-8">
    <h2 className="text-2xl font-semibold text-white">Modal Title</h2>
    <p className="mt-3 text-white/75">Modal content here.</p>
  </div>
</div>
```

### Glass Button

Two variants: **primary** (brand-colored) and **ghost** (transparent glass).

```tsx
{/* Primary — accent CTA */}
<button className="rounded-xl px-5 py-3 text-sm font-medium text-white bg-[var(--glass-accent)]/90 hover:bg-[var(--glass-accent)] border border-[var(--glass-accent)]/30 shadow-[0_0_20px_rgba(0,0,0,0.15)] backdrop-blur-sm transition">
  [Your CTA]
</button>

{/* Ghost — glass surface */}
<button className="rounded-xl px-5 py-3 text-sm font-medium text-white/90 bg-white/[0.08] hover:bg-white/[0.12] border border-white/[0.10] hover:border-white/[0.15] backdrop-blur-sm transition">
  Learn More
</button>

{/* Outline — minimal */}
<button className="rounded-xl px-5 py-3 text-sm font-medium text-white/80 hover:text-white bg-transparent hover:bg-white/[0.05] border border-white/[0.10] hover:border-white/[0.15] transition">
  Watch Demo
</button>
```

### Glass Badge / Chip

No blur — too small. Just semi-transparent fill.

```tsx
<span className="inline-flex items-center rounded-full px-3 py-1 text-xs font-medium text-[var(--glass-accent)] bg-[var(--glass-accent)]/10 border border-[var(--glass-accent)]/20">
  New
</span>

<span className="inline-flex items-center rounded-full px-3 py-1 text-xs font-medium text-white/70 bg-white/[0.06] border border-white/[0.06]">
  Label
</span>
```

### Glass Hero Section

Full hero with background glow orbs, glass card, and CTA buttons.

```tsx
<section className="relative overflow-hidden bg-[var(--glass-dark)] min-h-[85vh]">
  {/* Animated glow orbs — your brand colors */}
  <div className="absolute inset-0 overflow-hidden pointer-events-none" aria-hidden="true">
    <div className="absolute top-[-15%] right-[-10%] h-[500px] w-[500px] rounded-full bg-[var(--glass-glow-warm)]/12 blur-[100px] animate-[meshDrift1_20s_ease-in-out_infinite]" />
    <div className="absolute bottom-[-10%] left-[-8%] h-[450px] w-[450px] rounded-full bg-[var(--glass-glow-cool)]/10 blur-[100px] animate-[meshDrift2_25s_ease-in-out_infinite]" />
    <div className="absolute top-[40%] left-[50%] h-[350px] w-[350px] -translate-x-1/2 rounded-full bg-[var(--glass-accent-alt)]/8 blur-[80px] animate-[meshDrift3_30s_ease-in-out_infinite]" />
  </div>

  {/* Content */}
  <div className="relative mx-auto max-w-7xl px-6 py-24 md:py-32">
    <div className="rounded-3xl border border-white/[0.08] bg-white/[0.04] backdrop-blur-xl shadow-[0_8px_40px_rgba(0,0,0,0.2)] p-10 md:p-16">
      <span className="inline-flex items-center rounded-full px-3 py-1 text-xs font-medium text-[var(--glass-accent)] bg-[var(--glass-accent)]/10 border border-[var(--glass-accent)]/20 mb-6">
        Your Tagline Badge
      </span>
      <h1 className="text-4xl md:text-6xl font-semibold tracking-tight text-white font-display">
        Your Hero Headline.
      </h1>
      <p className="mt-5 text-lg md:text-xl text-white/75 max-w-2xl font-sans">
        Your hero subheadline with a clear value proposition.
      </p>
      <div className="mt-8 flex flex-col sm:flex-row gap-3">
        <button className="rounded-xl px-6 py-3.5 text-sm font-medium text-white bg-[var(--glass-accent)]/90 hover:bg-[var(--glass-accent)] border border-[var(--glass-accent)]/30 shadow-[0_0_24px_rgba(0,0,0,0.2)] backdrop-blur-sm transition">
          [Your CTA]
        </button>
        <button className="rounded-xl px-6 py-3.5 text-sm font-medium text-white/85 bg-white/[0.08] hover:bg-white/[0.12] border border-white/[0.10] hover:border-white/[0.15] backdrop-blur-sm transition">
          Secondary Action
        </button>
      </div>
    </div>
  </div>
</section>
```

Add these keyframes to your `globals.css` for the animated glow orbs:

```css
@keyframes meshDrift1 {
  0%, 100% { transform: translate(0, 0) scale(1); }
  50% { transform: translate(-30px, 20px) scale(1.05); }
}
@keyframes meshDrift2 {
  0%, 100% { transform: translate(0, 0) scale(1); }
  50% { transform: translate(20px, -30px) scale(1.08); }
}
@keyframes meshDrift3 {
  0%, 100% { transform: translate(-50%, 0) scale(1); }
  50% { transform: translate(-50%, 15px) scale(1.03); }
}
```

### Glass Pricing Grid

```tsx
<section className="relative bg-[var(--glass-dark)] px-6 py-20">
  <div className="mx-auto max-w-6xl">
    <div className="text-center mb-12">
      <h2 className="text-3xl md:text-4xl font-semibold tracking-tight text-white font-display">Simple Pricing</h2>
      <p className="mt-3 text-white/70 font-sans">A clear, concise pricing subheadline.</p>
    </div>

    <div className="grid gap-6 md:grid-cols-3">
      {tiers.map((tier, i) => (
        <div
          key={tier.name}
          className={`rounded-2xl border bg-white/[0.05] backdrop-blur-xl p-7 transition-all duration-300 hover:-translate-y-1 ${
            tier.featured
              ? "border-[var(--glass-accent)]/30 shadow-[0_0_40px_rgba(0,0,0,0.12)]"
              : "border-white/[0.08] shadow-[0_8px_32px_rgba(0,0,0,0.2)]"
          }`}
        >
          {tier.featured && (
            <span className="inline-flex items-center rounded-full px-3 py-1 text-xs font-medium text-[var(--glass-accent)] bg-[var(--glass-accent)]/10 border border-[var(--glass-accent)]/20 mb-4">
              Most Popular
            </span>
          )}
          <h3 className="text-xl font-semibold text-white">{tier.name}</h3>
          <div className="mt-2 flex items-baseline gap-1">
            <span className="text-3xl font-bold text-white">{tier.price}</span>
            <span className="text-white/60 text-sm">/mo</span>
          </div>
          <p className="mt-3 text-white/70 text-sm">{tier.description}</p>
          <ul className="mt-6 space-y-3">
            {tier.features.map((f) => (
              <li key={f} className="flex items-start gap-2 text-sm text-white/75">
                <svg className="mt-0.5 h-4 w-4 shrink-0 text-[var(--glass-success)]" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                </svg>
                {f}
              </li>
            ))}
          </ul>
          <button className={`mt-8 w-full rounded-xl px-5 py-3 text-sm font-medium transition ${
            tier.featured
              ? "text-white bg-[var(--glass-accent)]/90 hover:bg-[var(--glass-accent)] border border-[var(--glass-accent)]/30"
              : "text-white/90 bg-white/[0.08] hover:bg-white/[0.12] border border-white/[0.10]"
          }`}>
            Get Started
          </button>
        </div>
      ))}
    </div>
  </div>
</section>
```

### Glass Feature Grid

```tsx
<section className="relative bg-[var(--glass-dark)] px-6 py-20">
  <div className="mx-auto max-w-6xl">
    <div className="grid gap-5 md:grid-cols-2 lg:grid-cols-3">
      {features.map((f) => (
        <div key={f.title} className="group rounded-2xl border border-white/[0.08] bg-white/[0.04] backdrop-blur-xl p-6 transition-all duration-300 hover:border-white/[0.12] hover:bg-white/[0.06]">
          <div className="inline-flex h-10 w-10 items-center justify-center rounded-xl bg-[var(--glass-accent)]/10 text-[var(--glass-accent)] mb-4">
            {f.icon}
          </div>
          <h3 className="text-lg font-semibold text-white">{f.title}</h3>
          <p className="mt-2 text-sm text-white/70 leading-relaxed">{f.description}</p>
        </div>
      ))}
    </div>
  </div>
</section>
```

---

## Background Treatments

Glass requires a rich background. Here are three options using your brand variables:

### Option A: Gradient + Glow Orbs (Recommended)

```tsx
<div className="relative bg-gradient-to-br from-[var(--glass-dark)] via-[var(--glass-dark-alt)] to-[var(--glass-dark)] overflow-hidden">
  <div className="absolute inset-0 pointer-events-none" aria-hidden="true">
    <div className="absolute top-[-15%] right-[-10%] h-[500px] w-[500px] rounded-full bg-[var(--glass-glow-warm)]/12 blur-[100px]" />
    <div className="absolute bottom-[-10%] left-[-8%] h-[400px] w-[400px] rounded-full bg-[var(--glass-glow-cool)]/10 blur-[80px]" />
  </div>
  <div className="relative">{/* glass content here */}</div>
</div>
```

### Option B: Solid Dark + Subtle Noise

```tsx
<div className="bg-[var(--glass-dark)]">
  {/* Noise texture overlay */}
  <div className="absolute inset-0 bg-[url('/noise.svg')] opacity-[0.02] pointer-events-none" aria-hidden="true" />
  <div className="relative">{/* glass content here */}</div>
</div>
```

### Option C: Mesh Gradient (Animated)

```tsx
<div className="relative bg-[var(--glass-dark)] overflow-hidden">
  <div className="absolute inset-0 pointer-events-none" aria-hidden="true">
    <div className="absolute top-0 right-0 h-[600px] w-[600px] rounded-full bg-[var(--glass-glow-warm)]/8 blur-[120px] animate-[meshDrift1_20s_ease-in-out_infinite]" />
    <div className="absolute bottom-0 left-0 h-[500px] w-[500px] rounded-full bg-[var(--glass-glow-cool)]/6 blur-[120px] animate-[meshDrift2_25s_ease-in-out_infinite]" />
    <div className="absolute top-1/2 left-1/2 h-[400px] w-[400px] -translate-x-1/2 -translate-y-1/2 rounded-full bg-[var(--glass-accent-alt)]/5 blur-[100px] animate-[meshDrift3_30s_ease-in-out_infinite]" />
  </div>
  <div className="relative">{/* glass content here */}</div>
</div>
```

### Glow Color Combinations by Context

| Page / Context | Primary Glow | Secondary Glow | Mood |
|----------------|-------------|----------------|------|
| Homepage / Hero | `--glass-glow-warm` | `--glass-glow-cool` | Warm confidence |
| Marketplace | `--glass-glow-cool` | `--glass-accent-alt` | Tech/trust |
| Pricing | `--glass-glow-warm` | `--glass-success` | Value + action |
| Developer | `--glass-accent-alt` | `--glass-glow-cool` | Technical cool |
| Premium | `--glass-accent` | `--glass-glow-cool` | Premium energy |

---

## Accessibility

### Contrast Requirements

- All body text over glass: minimum **4.5:1** contrast ratio
- `text-white` on `bg-white/[0.05]` over a near-black background passes — the effective background is nearly black
- Test contrast with the **worst-case scroll position** if the glass element moves over variable content

### Reduced Transparency

```css
@media (prefers-reduced-transparency: reduce) {
  .glass-card,
  .glass-nav,
  .glass-modal {
    background: rgba(20, 20, 32, 0.95);
    backdrop-filter: none;
    -webkit-backdrop-filter: none;
  }
}

@media (prefers-contrast: more) {
  .glass-card,
  .glass-nav {
    background: rgba(20, 20, 32, 0.92);
    border: 1px solid rgba(255, 255, 255, 0.25);
  }
}
```

### Focus States

All interactive glass elements must have visible focus rings:

```tsx
className="... focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--glass-accent)]/50 focus-visible:ring-offset-2 focus-visible:ring-offset-[var(--glass-dark)]"
```

### Semantic Structure

- Glass sections: `<section>` with descriptive `aria-label`
- Glass nav: `<nav>` with `<header>` parent
- Glass modals: use your dialog library (Radix, Headless UI, etc.) which handles focus trap + `role="dialog"` + `aria-modal`
- Decorative glow orbs: `aria-hidden="true"` + `pointer-events-none`

---

## Performance

### Blur Budget

`backdrop-filter: blur()` is GPU-accelerated but expensive on mobile. Limit to **3-4 simultaneously visible blurred elements** per viewport.

| Scenario | Recommendation |
|----------|---------------|
| Desktop (powerful GPU) | Up to `backdrop-blur-xl` (24px), multiple elements fine |
| Mobile / low-end | Cap at `backdrop-blur-md` (12px), max 2 blurred elements visible |
| Scroll-attached elements (sticky nav) | Use `backdrop-blur-sm` (4px) or `backdrop-blur-md` (12px) |
| Animated elements | Never animate the blur value itself — animate transform/opacity only |

### Reducing GPU Load

```tsx
{/* Contain blur compositing to the glass section */}
<section className="contain-paint">
  {/* glass elements */}
</section>

{/* Skip blur on mobile if needed */}
<div className="bg-[var(--glass-dark-alt)]/90 md:bg-white/[0.05] md:backdrop-blur-xl border border-white/[0.08] rounded-2xl">
```

### Glow Orbs

The large decorative blur orbs (`blur-[80px]`+) are `filter: blur()`, not `backdrop-filter`. They're cheaper because they blur a solid-color div, not the content behind them. Still, use `will-change: transform` if animating:

```tsx
<div className="absolute h-[500px] w-[500px] rounded-full bg-[var(--glass-glow-warm)]/12 blur-[100px] will-change-transform animate-[meshDrift1_20s_ease-in-out_infinite]" />
```

---

## Browser Support

| Feature | Chrome | Firefox | Safari | Edge |
|---------|--------|---------|--------|------|
| `backdrop-filter` | 76+ | 103+ | 9+ (`-webkit-`) | 79+ |
| `blur()` filter | All modern | All modern | All modern | All modern |

For Safari, always include `-webkit-backdrop-filter` alongside `backdrop-filter`. Tailwind's `backdrop-blur-*` utilities do this automatically.

### Fallback

```css
/* Tailwind generates both prefixed and unprefixed automatically */
/* For custom CSS, add the fallback manually: */
.glass-card {
  background: rgba(20, 20, 32, 0.85); /* solid fallback */
}
@supports (backdrop-filter: blur(1px)) {
  .glass-card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
  }
}
```

---

## Anti-Patterns (What NOT to Do)

| Anti-Pattern | Why | Fix |
|-------------|-----|-----|
| Glass on light backgrounds | Effect is invisible | Use `var(--glass-dark)` or dark gradient |
| Glass on glass (stacking) | Compounds opacity, destroys readability | One glass layer per z-level |
| Blur on every element | Kills GPU, destroys hierarchy | 2-4 blurred elements per viewport |
| Generic purple/cyan/pink gradients | Looks like every AI landing page | Use your `--glass-glow-warm` and `--glass-glow-cool` brand tokens |
| `text-white/40` on glass | Unreadable | Minimum `text-white/60` for labels, `text-white/75` for body |
| Animating blur values | Causes jank on mobile | Animate transform/opacity instead |
| Sharp corners on glass | Breaks the illusion | Minimum `rounded-xl` (12px) |
| Hardcoded hex colors | Breaks brand consistency | Always use CSS variables or Tailwind brand tokens |
| Glass in data-dense areas | Makes tables/forms unreadable | Use solid dark surfaces |
| Missing `-webkit-backdrop-filter` | Breaks Safari | Tailwind handles this; in custom CSS, add manually |

---

## Decision Tree

```
User wants glass UI?
+-- Is it a dark-background section? (hero, landing, showcase)
|  +-- YES -> Use glass cards + brand glow orbs
|  |  +-- How many glass elements visible at once?
|  |  |  +-- <= 4 -> Full blur treatment (backdrop-blur-xl)
|  |  |  +-- > 4  -> Reduce to backdrop-blur-md or skip blur on less important elements
|  |  +-- Is this mobile-critical?
|  |     +-- YES -> Cap at backdrop-blur-md, max 2 blurred elements
|  |     +-- NO  -> Full treatment is fine
|  +-- NO -> Don't use glass. Use solid surfaces with brand colors.
|
+-- Is it a sticky nav?
|  +-- Over dark content -> bg-white/[0.05] backdrop-blur-md
|  +-- Over light content -> bg-white/80 backdrop-blur-sm
|
+-- Is it a modal/overlay?
|  +-- Backdrop: bg-black/40 backdrop-blur-sm
|     Panel: bg-white/[0.08] backdrop-blur-xl
|
+-- Is it a badge/chip/small element?
   +-- bg-white/[0.06] border border-white/[0.06] — NO blur (too small to matter)
```

---

## Checklist

Before shipping any glass UI, verify:

- [ ] Dark background present behind all glass elements
- [ ] Text contrast passes 4.5:1 (test headings AND body text)
- [ ] Max 4 blurred elements visible simultaneously
- [ ] Glow orbs use brand variables (`--glass-glow-warm`, `--glass-glow-cool`), not generic colors
- [ ] Hover/focus/active states on all interactive elements
- [ ] `aria-hidden="true"` on decorative glow orbs
- [ ] Focus rings visible on buttons and links
- [ ] Mobile responsive (single column, spacing intact)
- [ ] Mobile blur reduced if > 2 blurred elements visible
- [ ] `prefers-reduced-transparency` fallback considered
- [ ] No glass stacked on glass
- [ ] No glass on light backgrounds
- [ ] Semantic HTML tags (`section`, `nav`, `header`, `main`)
- [ ] All colors use CSS variables or Tailwind brand tokens (no hardcoded hex)
