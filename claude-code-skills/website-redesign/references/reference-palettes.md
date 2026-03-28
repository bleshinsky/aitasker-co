# Reference Palettes

Use these as **inspiration** for developing a custom palette. They originate from presentation/slide themes — adapt the mood and color relationships for web, don't copy the exact values.

## Palette Table

| Theme | Colors | Mood | Best For |
|---|---|---|---|
| Ocean Depths | `#1a2332` / `#2d8b8b` / `#a8dadc` / `#f1faee` | Professional, calming, trust-building | B2B SaaS, financial, consulting |
| Sunset Boulevard | `#264653` / `#e76f51` / `#f4a261` / `#e9c46a` | Warm, vibrant, creative energy | Marketing, lifestyle, creative tools |
| Forest Canopy | `#2d4a2b` / `#7d8471` / `#a4ac86` / `#faf9f6` | Grounded, natural, calm | Sustainability, wellness, outdoor |
| Midnight Galaxy | `#2b1e3e` / `#4a4e8f` / `#a490c2` / `#e6e6fa` | Dramatic, premium, cosmic | Entertainment, gaming, luxury |
| Botanical Garden | `#4a7c59` / `#f9a620` / `#b7472a` / `#f5f3ed` | Fresh, organic, lively | Food, natural products, gardening |
| Golden Hour | `#4a403a` / `#f4a900` / `#c1666b` / `#d4b896` | Warm, sophisticated, inviting | Hospitality, artisan, premium consumer |
| Desert Rose | `#5d2e46` / `#d4a5a5` / `#b87d6d` / `#e8d5c4` | Soft, elegant, refined | Fashion, beauty, interior design |
| Tech Innovation | `#1e1e1e` / `#0066ff` / `#00ffff` / `#ffffff` | Bold, cutting-edge | Dev tools, AI/ML, tech startups |
| Arctic Frost | `#4a6fa5` / `#d4e4f7` / `#c0c0c0` / `#fafafa` | Clean, precise, clinical | Healthcare, clean tech, pharma |
| Modern Minimalist | `#36454f` / `#708090` / `#d3d3d3` / `#ffffff` | Versatile, sophisticated | Architecture, design, data viz |

## Calibration Notes

The sweet spot is: **sophisticated with character** — not screaming neon, not put-you-to-sleep grayscale.

### Tech Innovation — too neon
The `#00ffff` cyan is overwhelming on screen. If going for a tech/modern direction:
- Mute the cyan significantly (try `#66d9ef` or `#5ecece`)
- Add warmth through a secondary accent or warmer neutral base
- Consider desaturating the blue slightly for longer reading comfort
- The dark background works well but needs more tonal variety (not just flat `#1e1e1e`)

### Arctic Frost — risks sterility
The palette is all cool tones with no warmth or energy:
- Must add at least one warm or saturated accent color (amber, coral, teal)
- Without an accent, everything feels like a medical form
- The steel blue is a good anchor but needs something to play against
- Consider warming the whites slightly (off-white instead of pure white)

### Modern Minimalist — needs a punch
Grayscale-only palettes fail to create visual hierarchy for CTAs and key elements:
- Add one saturated accent color that contrasts sharply (this becomes the CTA color)
- Without it, primary and secondary actions look the same
- The charcoal/slate base is solid — it just needs energy injected
- A single bold accent on a restrained palette can be more striking than a full colorful scheme

### Midnight Galaxy — AI-purple risk
Deep purple palettes have become strongly associated with AI-generated design:
- If using purples, shift toward blue-purple or warm-purple to differentiate
- Pair with an unexpected accent (gold, coral, emerald) rather than more purple/lavender
- Consider using the deep purple as a background-only color rather than as the identity color
- Test with non-technical users — they may perceive it as "another AI tool"

## Building Your Custom Palette

Your palette must include these roles:

| Role | Purpose | Example |
|---|---|---|
| **Dominant** | The color that defines the brand identity; used in headers, hero sections | Deep teal, warm charcoal, forest green |
| **Accent** | High-contrast, high-energy; used for CTAs, links, key highlights | Coral, amber, electric blue |
| **Dark Anchor** | Grounds the design; used for text, dark sections, footer | Near-black, dark navy, deep brown |
| **Light/Neutral Base** | Breathing room; used for backgrounds, cards, whitespace | Off-white, warm gray, cream |
| **Secondary** (optional) | Supports the dominant; used for secondary UI, borders, muted states | Sage, slate, dusty rose |

### Palette Quality Checks

- The accent color must have sufficient contrast against both light and dark backgrounds
- Test the CTA button color against the most common page background — it must pop immediately
- Headers in the dominant color must be readable at both large (hero) and medium (section title) sizes
- The palette should work in both light and dark contexts, or you should declare which mode you're designing for
- Print/paste the hex values into a row and squint — they should feel cohesive, not random
