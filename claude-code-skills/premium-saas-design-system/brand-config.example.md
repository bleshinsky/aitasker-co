# Premium SaaS Brand Configuration

This file tells the premium SaaS design system skill your brand identity. Copy this file to your project and fill in your values.

**Where to place this file:** `.claude/brand-config.md` or `brand-config.md` in your project root.

---

## Brand Identity

- **Product name:** Your Product
- **One-line positioning:** (under 8 words, e.g., "See the work before you pay.")
- **Target audience:** (e.g., "SMB operators spending $100-500/mo on tools")
- **Tone of voice:** (e.g., "Confident, casual-professional, slightly irreverent")

## Color Palette (6 roles)

| Role | Hex Value | CSS Variable | Purpose |
|------|-----------|-------------|---------|
| Background | `#FAF7F2` | `var(--color-background)` | Default page background (never pure white) |
| Text Primary | `#1A1A2E` | `var(--color-text-primary)` | Primary text, dark hero sections |
| Accent | `#E8930C` | `var(--color-accent)` | CTAs, emphasis, badges, quality scores |
| Success | `#5B8A72` | `var(--color-success)` | Checkmarks, trust signals, confirmations |
| Border | `#E5E0D8` | `var(--color-border)` | Borders, dividers, separators |
| Surface Alt | `#F3EFE8` | `var(--color-surface-alt)` | Alternating section backgrounds |

## Typography (3 slots)

| Slot | Font Family | Tailwind Class | Notes |
|------|------------|---------------|-------|
| Display | Your Display Font | `font-display` | Headlines, hero text. Choose something with editorial weight. |
| Sans | Your Sans Font | `font-sans` | Body text, UI elements, buttons. Clean and readable. |
| Mono | Your Mono Font | `font-mono` | Code, data, technical labels. Used sparingly. |

**Guidance:** The display font is the single biggest lever for perceived quality. Choose a distinctive serif (e.g., Playfair Display, DM Serif Display, Fraunces) or geometric display face (e.g., Clash Display, Cabinet Grotesk). Avoid Inter, Roboto, Arial, Space Grotesk as display fonts.

## Brand Shadows (Premium Detail)

```css
/* Accent shadow on CTAs */
box-shadow: 0 4px 16px rgba(YOUR_ACCENT_RGB, 0.2);

/* Warm shadow on cards */
box-shadow: 0 2px 12px rgba(YOUR_TEXT_PRIMARY_RGB, 0.06);

/* Success shadow on confirmations */
box-shadow: 0 4px 16px rgba(YOUR_SUCCESS_RGB, 0.15);
```

## Secondary Brand Variant (Optional)

If your product has a sub-brand or secondary product line:

- **Variant name:** (e.g., "Pro", "Personal", "Enterprise")
- **Gradient from:** `#6C5CE7`
- **Gradient to:** `#00D2FF`
- **Scope:** Only appears on variant-specific routes (e.g., `/pro/*`)
- **Differences:** (e.g., "Rounder shapes, more animation, lighter visual weight")

## Primary CTA

- **Button text:** (e.g., "Start Free Trial", "Get Started Free")
- **Risk reversal:** (e.g., "No credit card required", "Cancel anytime")

## Social Proof

- **Quantified trust:** (e.g., "Trusted by 2,000+ teams")
- **Key metric:** (e.g., "90-second delivery")
- **Differentiation:** (e.g., "Pay only for what you pick")

## CSS Variables Block

Copy into your `globals.css`:

```css
:root {
  --color-background:    #FAF7F2;
  --color-text-primary:  #1A1A2E;
  --color-accent:        #E8930C;
  --color-success:       #5B8A72;
  --color-border:        #E5E0D8;
  --color-surface-alt:   #F3EFE8;
}
```

## Tailwind Config

Add to your `tailwind.config.ts`:

```js
module.exports = {
  theme: {
    extend: {
      colors: {
        background:   'var(--color-background)',
        'text-primary': 'var(--color-text-primary)',
        accent:       'var(--color-accent)',
        success:      'var(--color-success)',
        border:       'var(--color-border)',
        'surface-alt': 'var(--color-surface-alt)',
      },
      fontFamily: {
        display: ['YourDisplayFont', 'serif'],
        sans:    ['YourSansFont', 'system-ui', 'sans-serif'],
        mono:    ['YourMonoFont', 'monospace'],
      },
    },
  },
};
```
