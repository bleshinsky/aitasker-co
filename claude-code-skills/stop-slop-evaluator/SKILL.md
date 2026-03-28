---
name: stop-slop-evaluator
description: "Detects and removes AI slop from evaluation justifications. Flags generic filler, vague language, and banned phrases. Quality-checks text for specificity."
---

# Stop-Slop Evaluator

Detect and eliminate generic AI filler from evaluation justifications and written output.

## Trigger Keywords

check for slop, review my justification, is this specific enough, tighten this up, remove filler, anti-slop, quality check text, make this more specific

## Why This Matters

Evaluation justifications that use vague, formulaic language are:
- **Less useful** — they don't help the next person understand what's actually wrong
- **Less credible** — reviewers and QA teams recognize AI slop instantly
- **Less calibrated** — vague language masks whether the evaluator actually examined the image
- **Rejected more often** — platforms increasingly flag generic justifications for rework

## Slop Detection Rules

### Rule 1: Banned Phrases

**Never use these in evaluation justifications. Replace or delete.**

| Banned Phrase | Why It's Slop | Replace With |
|---------------|---------------|--------------|
| "It's worth noting that..." | Filler preamble | Just state the observation |
| "Importantly..." | Tells the reader what to think | Let the observation speak |
| "Overall..." | Vague summarizer | Be specific about what you're summarizing |
| "In terms of..." | Wordy nothing | Name the dimension directly |
| "It should be noted..." | Passive filler | State the fact |
| "This is a testament to..." | Sycophantic | Describe what's actually good |
| "A masterful blend of..." | Hyperbolic filler | Describe specific elements |
| "Adds a layer of..." | Vague depth claim | Specify what layer and how |
| "Speaks to the..." | Abstract attribution | Concrete cause → effect |
| "A sense of..." | Vague impression | Name the specific quality |
| "Quite" / "Rather" / "Fairly" | Hedge words that add nothing | Use the adjective alone or quantify |

### Rule 2: Banned Words

These words almost always signal AI-generated filler in evaluations:

**Verbs:** delve, foster, underscore, bolster, spearhead, navigate (metaphorical), leverage (as verb), utilize (use "use"), facilitate, synergize, unpack

**Adjectives:** robust, comprehensive, nuanced, multifaceted, holistic, cutting-edge, groundbreaking, innovative (unless literally true), seamless, meticulous

**Adverbs:** notably, significantly, fundamentally, essentially, undeniably, arguably, inherently

### Rule 3: Banned Patterns

| Pattern | Example | Problem |
|---------|---------|---------|
| "Not only X, but also Y" | "Not only is the lighting good, but also the composition" | Formulaic structure — just list both observations |
| "While X, Y" (false balance) | "While the hands are wrong, the overall quality is good" | Minimizes the defect. State both plainly. |
| Excessive em dashes | "The image — which features — a stunning landscape — really captures —" | One em dash per paragraph max |
| Triple adjective stacks | "A vibrant, dynamic, compelling composition" | Pick the ONE most accurate adjective |
| "The fact that..." | "The fact that the model rendered 6 fingers..." | Delete "The fact that" — start with "The model rendered 6 fingers" |
| Rhetorical questions | "But is this truly a failure?" | State your assessment directly |

### Rule 4: Specificity Test

Every justification sentence must pass the **Specificity Test**:

> Could this sentence apply to a DIFFERENT image with a DIFFERENT problem?

If yes → it's slop. Rewrite with image-specific details.

**FAILS specificity test:**
- "The image demonstrates good visual quality with minor issues"
- "Overall the aesthetic execution is competent"
- "There are some noticeable artifacts"

**PASSES specificity test:**
- "The bokeh rendering in the background is convincing but there's visible color banding in the sky gradient between the treeline and horizon"
- "The left hand of the foreground figure has 6 fingers, with the extra digit between the ring and pinky finger"
- "The neon sign reading 'OPEN' is misspelled as 'OEPN' — the E and P are transposed"

### Rule 5: Justification Length

| Context | Target Length |
|---------|--------------|
| Per-dimension justification | 2–3 sentences |
| First impression | 2–3 sentences |
| Overall justification | 3–4 sentences |
| Batch mode justification | 2–3 sentences total |
| Preference reason | 1–2 sentences |

If a justification exceeds target length, it probably contains filler. Cut.

## How to Apply

### As a Post-Processor

After generating evaluation justifications:

1. Read each justification sentence
2. Check against Rules 1–3 (banned phrases, words, patterns)
3. Apply Rule 4 specificity test to each sentence
4. Check Rule 5 length targets
5. Rewrite any failing sentences
6. Verify the rewritten version still supports the score

### As a Standalone Review

When the user asks to review text:

1. Scan for all Rule 1–3 violations — highlight each one
2. Apply Rule 4 to every sentence — mark failures
3. Provide a **Slop Score**: count of violations per 100 words
   - 0 violations = Clean
   - 1–2 = Acceptable
   - 3–5 = Needs revision
   - 6+ = Heavy slop — rewrite recommended
4. Suggest specific replacements for each violation

## Anti-Patterns in Evaluation Justifications

These patterns are unique to AI evaluation work:

**"The image successfully captures..."** → What specifically does it capture? Name elements.

**"The model demonstrates a strong understanding of..."** → Models don't "understand." Describe what was rendered correctly.

**"There is a good balance between X and Y"** → What IS the balance? Describe the specific ratio or relationship.

**"The composition effectively draws the eye to..."** → WHERE does the eye go? Describe the compositional device (leading lines, contrast, rule of thirds placement).

**"Minor issues notwithstanding, the overall quality is..."** → Name the minor issues. "Minor issues" is information-free.

**"The image could benefit from..."** → This is feedback for the model, not an evaluation. State what IS, not what could be.

## Self-Check Prompt

Before finalizing any evaluation output, ask yourself:

> "If I read this justification without seeing the image, would I know EXACTLY what the image looks like and what's wrong with it?"

If no → rewrite until yes.
