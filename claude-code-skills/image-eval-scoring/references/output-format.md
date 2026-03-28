# Output Formats — Platform-Specific Templates

## Table of Contents
1. [Generic (Default)](#1-generic-default)
2. [Compact Field Format](#2-compact-field-format)
3. [Platform Format A](#3-platform-format-a)
4. [Platform Format B (JSON)](#4-platform-format-b-json)
5. [Platform Format C (Table)](#5-platform-format-c-table)
6. [JSON Export](#6-json-export)
7. [Markdown Report](#7-markdown-report)
8. [Batch Processing](#8-batch-processing)

---

## 1. Generic (Default)

Use when no platform is specified. Readable, comprehensive, copy-pasteable.

```
═══════════════════════════════════════════
IMAGE EVALUATION REPORT
═══════════════════════════════════════════

Source Prompt: [full prompt text]
Rubric: standard-6D
Date: [YYYY-MM-DD]

───────────────────────────────────────────
FIRST IMPRESSION
───────────────────────────────────────────
[2–3 sentences]

───────────────────────────────────────────
SCORES
───────────────────────────────────────────

Safety:               X/7  [one-line summary]
Instruction Following: X/7  [one-line summary]
Text Rendering:        X/7  [one-line summary]
Object Accuracy:       X/7  [one-line summary]
Visual Quality:        X/7  [one-line summary]
Aesthetic Quality:     X/7  [one-line summary]

COMPOSITE:             X.X/7

───────────────────────────────────────────
DETAILED JUSTIFICATIONS
───────────────────────────────────────────

[Per-dimension block with Key Observations + Justification]

───────────────────────────────────────────
FLAGS & NOTES
───────────────────────────────────────────
[Edge cases, ambiguities, escalation flags]
```

---

## 2. Compact Field Format

Structured for evaluation platforms. Concise, field-aligned.

```
TASK_ID: [from platform]
IMAGE_ID: [from platform]
PROMPT: [source prompt]

SCORES:
  safety: X
  instruction_following: X
  text_rendering: X
  object_accuracy: X
  visual_quality: X
  aesthetic_quality: X
  composite: X.X

JUSTIFICATIONS:
  safety: "[1–2 sentences]"
  instruction_following: "[1–2 sentences]"
  text_rendering: "[1–2 sentences]"
  object_accuracy: "[1–2 sentences]"
  visual_quality: "[1–2 sentences]"
  aesthetic_quality: "[1–2 sentences]"

PREFERENCE: [A/B/TIE — if side-by-side]
PREFERENCE_STRENGTH: [strong/moderate/slight/tie]
PREFERENCE_REASON: "[1–2 sentences]"

FLAGS: [none / safety_concern / escalate / ambiguous_rubric]
NOTES: "[free text for edge cases]"
```

---

## 3. Platform Format A

For evaluation platforms with per-dimension fields. Keep justifications to 2–3 sentences max per field (many platforms have character limits on text boxes).

```
## Platform Evaluation Entry

### Overall Rating: X/7
### Preference: [Image A / Image B / Tie]

### Dimension Ratings:
- Safety: X/7
- Instruction Following: X/7
- Text Rendering: X/7
- Object Accuracy: X/7
- Visual Quality: X/7
- Aesthetic Quality: X/7

### Overall Justification:
[3–4 sentences covering the most important observations. Lead with the
strongest signal — what most distinguishes this image's quality. Reference
specific elements visible in the image.]

### Key Strengths:
- [Strongest positive aspect]
- [Second strength if applicable]

### Key Weaknesses:
- [Most significant issue]
- [Second issue if applicable]
```

**Platform tips:**
- Many platforms use radio buttons for scores — map directly to 0–7 scale
- Some campaigns use thumbs up/down instead of numerical — map: 0–3 = down, 4–7 = up
- Justification boxes often have 500-character limits — be concise
- Copy the "Overall Justification" section for the platform's main text field

---

## 4. Platform Format B (JSON)

For annotation platforms that accept JSON input. Typically structured as labeled annotations.

```
{
  "evaluation": {
    "task_id": "[from platform]",
    "image_id": "[from platform]",
    "prompt": "[source prompt]",
    "scores": {
      "safety": X,
      "instruction_following": X,
      "text_rendering": X,
      "object_accuracy": X,
      "visual_quality": X,
      "aesthetic_quality": X
    },
    "composite": X.X,
    "justification": "[Combined 3–4 sentence justification]",
    "flags": [],
    "preference": "[A/B/tie/null]",
    "confidence": "[high/medium/low]"
  }
}
```

---

## 5. Platform Format C (Table)

For evaluation platforms that prefer tabular layout.

```
## Image Evaluation

**Task ID:** [from platform]
**Evaluation Type:** [image_quality / preference_ranking / safety_review]

### Scores (0–7 scale)
| Dimension | Score |
|-----------|-------|
| Safety | X |
| Instruction Following | X |
| Text Rendering | X |
| Object Accuracy | X |
| Visual Quality | X |
| Aesthetic Quality | X |
| **Composite** | **X.X** |

### Rationale
[Combined justification paragraph — Scale typically wants a single
rationale field rather than per-dimension. Cover the 2–3 most significant
observations and the primary reason for the composite score.]

### Preference (if applicable)
**Selected:** [Image A / Image B]
**Confidence:** [Definitely / Probably / Slightly]
**Reason:** [1–2 sentences]
```

---

## 6. JSON Export

Machine-readable format for batch processing or data analysis.

```json
{
  "evaluation_id": "eval_YYYYMMDD_HHMMSS",
  "timestamp": "2026-02-20T10:30:00Z",
  "evaluator": "claude_image_eval_v1",
  "rubric": "standard-6D",
  "prompt": "[source prompt text]",
  "scores": {
    "safety": {"score": 7, "justification": "..."},
    "instruction_following": {"score": 6, "justification": "..."},
    "text_rendering": {"score": 7, "justification": "N/A — no text requested"},
    "object_accuracy": {"score": 5, "justification": "..."},
    "visual_quality": {"score": 6, "justification": "..."},
    "aesthetic_quality": {"score": 6, "justification": "..."}
  },
  "composite": 6.2,
  "first_impression": "...",
  "flags": [],
  "preference": {
    "selected": null,
    "strength": null,
    "reason": null
  },
  "metadata": {
    "scoring_order": ["safety", "instruction_following", "text_rendering", "object_accuracy", "visual_quality", "aesthetic_quality"],
    "consistency_check_passed": true,
    "edge_cases_referenced": false
  }
}
```

---

## 7. Markdown Report

For sharing evaluations as documents or in Obsidian notes.

```markdown
# Image Evaluation: [short description]

**Date:** YYYY-MM-DD
**Prompt:** `[source prompt]`
**Rubric:** standard-6D
**Composite Score:** X.X/7

## First Impression
[2–3 sentences]

## Scores

| Dimension | Score | Summary |
|-----------|-------|---------|
| Safety | X/7 | [one-line] |
| Instruction Following | X/7 | [one-line] |
| Text Rendering | X/7 | [one-line] |
| Object Accuracy | X/7 | [one-line] |
| Visual Quality | X/7 | [one-line] |
| Aesthetic Quality | X/7 | [one-line] |

## Detailed Justifications

### Safety (X/7)
[Full justification]

### Instruction Following (X/7)
[Full justification]

[...etc...]

## Notes
- [Any edge cases or flags]

---
*Evaluated using image-eval-scoring skill v1.0*
```

---

## 8. Batch Processing

When evaluating multiple images in sequence:

**Header (once per batch):**
```
BATCH: [batch name/ID]
CAMPAIGN: [campaign name]
RUBRIC: standard-6D
DATE: YYYY-MM-DD
EVALUATOR: claude_image_eval_v1
IMAGES_IN_BATCH: N
```

**Per-image (repeat N times):**
```
---
IMAGE [n/N]: [image_id]
PROMPT: [prompt text]
SCORES: S=X IF=X TR=X OA=X VQ=X AQ=X → C=X.X
JUSTIFICATION: [single paragraph, 3–4 sentences max]
FLAGS: [none / list]
---
```

**Footer (once per batch):**
```
BATCH SUMMARY:
  Images evaluated: N
  Score distribution: min=X.X, max=X.X, mean=X.X, median=X.X
  Safety flags: N
  Escalations: N
  Completion time: [HH:MM]
```

**Batch tips:**
- Process safety dimension first for ALL images before other dimensions — this lets you flag and skip unsafe images early
- Maintain consistent calibration across the batch — re-read calibration anchors from edge-cases.md every 10 images
- If you notice score drift (everything trending higher or lower), pause and re-anchor
