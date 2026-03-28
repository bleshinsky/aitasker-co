# Glassmorphism Brand Configuration

This file tells the glassmorphism design system skill what colors, fonts, and brand tokens to use. Copy this file to your project and fill in your values.

**Where to place this file:** `.claude/brand-config.md` or `brand-config.md` in your project root.

---

## Colors

Define your brand's glass palette. Every component in the design system references these roles.

| Role | Hex Value | CSS Variable | Purpose |
|------|-----------|-------------|---------|
| Dark Background | `#0A0A0F` | `--glass-dark` | Primary dark surface behind glass elements |
| Dark Alt | `#141420` | `--glass-dark-alt` | Secondary dark surface, gradient endpoints |
| Light | `#FAFAF8` | `--glass-light` | Light text on dark backgrounds |
| Accent | `#FF8A00` | `--glass-accent` | Primary CTA buttons, accent highlights |
| Accent Alt | `#FFB347` | `--glass-accent-alt` | Hover states, secondary highlights |
| Glow Warm | `#FF8A00` | `--glass-glow-warm` | Warm ambient glow orb color |
| Glow Cool | `#6C5CE7` | `--glass-glow-cool` | Cool ambient glow orb color |
| Success | `#00B894` | `--glass-success` | Success states, positive indicators |

## Fonts

| Role | Font Family | Tailwind Class | Purpose |
|------|------------|---------------|---------|
| Display | Your Display Font | `font-display` | Hero headings, section titles |
| Sans | Your Sans Font | `font-sans` | Body text, UI labels, buttons |
| Mono | Your Mono Font | `font-mono` | Code snippets, technical values |

## Brand Name

- **Product name:** Your Product
- **CTA text:** Your primary call-to-action (e.g., "Start Free Trial")
- **Tagline:** Your one-line value prop

## CSS Variables Block

Copy this into your `globals.css` and replace the hex values with your brand colors:

```css
:root {
  --glass-dark:        #0A0A0F;
  --glass-dark-alt:    #141420;
  --glass-light:       #FAFAF8;
  --glass-accent:      #FF8A00;
  --glass-accent-alt:  #FFB347;
  --glass-glow-warm:   #FF8A00;
  --glass-glow-cool:   #6C5CE7;
  --glass-success:     #00B894;
}
```

## Tailwind Config

Add to your `tailwind.config.ts`:

```js
module.exports = {
  theme: {
    extend: {
      colors: {
        'glass-dark':       'var(--glass-dark)',
        'glass-dark-alt':   'var(--glass-dark-alt)',
        'glass-light':      'var(--glass-light)',
        'glass-accent':     'var(--glass-accent)',
        'glass-accent-alt': 'var(--glass-accent-alt)',
        'glass-glow-warm':  'var(--glass-glow-warm)',
        'glass-glow-cool':  'var(--glass-glow-cool)',
        'glass-success':    'var(--glass-success)',
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
