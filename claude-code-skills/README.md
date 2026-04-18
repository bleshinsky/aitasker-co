# Claude Code Skills Collection

A collection of open-source skills for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) — Anthropic's agentic coding tool. Skills are reusable instruction sets that teach Claude how to perform specific tasks with consistency and quality.

## What Are Skills?

Skills are markdown files (`SKILL.md`) that give Claude Code specialized knowledge for specific tasks. When you ask Claude to do something that matches a skill's description, it loads the skill and follows its methodology. Think of them as expert playbooks.

**Skills are not plugins or code.** They're structured prompts that Claude reads and follows. No installation, no dependencies, no build step.

## Quick Start

### 1. Pick a skill

Browse the folders below and pick the skill(s) you want.

### 2. Copy the skill folder into your project

```bash
# Copy a single skill
cp -r glassmorphism-design-system/ /path/to/your-project/.claude/skills/

# Or copy multiple
cp -r saas-positioning/ seo-landing-pages/ /path/to/your-project/.claude/skills/
```

Skills go in your project's `.claude/skills/` directory (or wherever your Claude Code setup looks for skills).

### 3. Configure (if needed)

Some skills read from a brand configuration file. If a skill folder contains a `brand-config.example.md`, copy it to your project and fill in your values:

```bash
cp .claude/skills/glassmorphism-design-system/brand-config.example.md .claude/brand-config.md
# Edit .claude/brand-config.md with your brand colors, fonts, etc.
```

### 4. Use it

Just ask Claude to do the thing the skill covers. For example:
- "Build a glassmorphism hero section" (triggers glassmorphism-design-system)
- "Write a LinkedIn recommendation for my colleague Sarah" (triggers linkedin-recommendation)
- "Create positioning for my SaaS product" (triggers saas-positioning)

Claude automatically matches your request to the right skill based on the skill's description.

---

## Available Skills

### Design Systems

| Skill | What It Does | Config Needed? |
|-------|-------------|----------------|
| [glassmorphism-design-system](./glassmorphism-design-system/) | Frosted-glass UI components — cards, navbars, modals, hero sections with blur, transparency, and depth effects. Includes design tokens, accessibility, performance budgets. | Yes — `brand-config.example.md` |
| [premium-saas-design-system](./premium-saas-design-system/) | Awwwards-level marketing pages — typography as architecture, motion choreography, conversion patterns, 68-item quality checklist. The Seven Pillars framework. | Yes — `brand-config.example.md` |

### Marketing & Strategy

| Skill | What It Does | Config Needed? |
|-------|-------------|----------------|
| [saas-positioning](./saas-positioning/) | Complete April Dunford positioning methodology for SaaS. 14-section positioning document covering competitive analysis, messaging hierarchy, sales narrative, and 30/60/90 day plan. | No |
| [seo-landing-pages](./seo-landing-pages/) | SEO-optimized landing pages in Next.js. Keyword strategy, JSON-LD structured data, 9-section page template, CRO patterns, post-build audit. | No |
| [website-redesign](./website-redesign/) | Audit and redesign websites with combined design excellence + CRO scoring. 7-dimension analysis, experiment bank, actionable recommendations. | No |

### Writing

| Skill | What It Does | Config Needed? |
|-------|-------------|----------------|
| [linkedin-recommendation](./linkedin-recommendation/) | Write authentic, specific LinkedIn recommendations. 5-beat structure, anti-cliche rules, tone matching. | Optional — `writing-style.md` template |

### Writing Quality

| Skill | What It Does | Config Needed? |
|-------|-------------|----------------|
| [stop-slop-evaluator](./stop-slop-evaluator/) | Detect and eliminate generic AI filler from written output. 45+ banned phrases, specificity test, slop score. Works on evaluation justifications or any text. | No |
---

## Skill Anatomy

Every skill is a folder containing:

```
skill-name/
  SKILL.md                    # The skill itself (required)
  brand-config.example.md     # Config template (if skill needs customization)
  references/                 # Supporting reference files (optional)
    detailed-guide.md
    templates.md
    examples.md
```

- **`SKILL.md`** — The main skill file. Contains the methodology, rules, patterns, and instructions Claude follows. You should never need to edit this file.
- **`brand-config.example.md`** — A template for project-specific configuration. Copy to your project's `.claude/` directory and fill in your values. The skill reads this at runtime.
- **`references/`** — Detailed reference material the skill loads on demand (rubric dimensions, code templates, example banks). These are read-only supporting files.

## Configuration Pattern

Skills that need project-specific input (colors, fonts, brand identity) use an **external config file** pattern:

1. The skill ships with a `brand-config.example.md` template
2. You copy the template to `.claude/brand-config.md` in your project
3. You fill in your brand's values (hex colors, font names, CTA text, etc.)
4. The skill reads this file at runtime — the skill itself stays untouched

This means you can update skills without losing your configuration, and multiple skills can share the same brand config.

## Contributing

Found a bug? Have an improvement? PRs welcome. When contributing:

- Skills should be **generic** — no project-specific brand references
- Configuration should be **external** — never require editing SKILL.md
- Include **reference files** for detailed criteria that would bloat the main skill
- Write clear **trigger descriptions** in the frontmatter so Claude knows when to activate the skill

## License

MIT
