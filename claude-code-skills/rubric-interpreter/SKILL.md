---
name: rubric-interpreter
description: "Converts rubric PDFs and evaluation guidelines into structured scoring references. Use when starting new campaigns or interpreting scoring criteria."
---

# Rubric Interpreter

Convert evaluation rubric documents into structured, actionable scoring references.

## Trigger Keywords

new rubric, parse this rubric, convert rubric, interpret scoring guide, new campaign guidelines, rubric PDF, scoring criteria document, evaluation guidelines, help me understand this rubric, set up new campaign

## Why This Skill Exists

Every new evaluation campaign comes with rubric documents — PDFs, Google Docs, slide decks, or screenshot instructions. These documents are often:
- Long (10–50 pages)
- Inconsistently structured
- Mixed with platform instructions and logistics
- Using different terminology for similar concepts

This skill extracts the scoring-relevant content and produces standardized reference files that other evaluation skills can consume directly.

## Interpretation Workflow

### Step 1 — Ingest the Source Document

Accept rubric in any format:
- PDF (use `training-doc-converter` if needed)
- Google Doc (fetch content)
- Screenshots (read visible text)
- Pasted text
- URL to rubric page

Announce: "Interpreting rubric document. I'll extract scoring criteria, scale definitions, and edge case guidance."

### Step 2 — Identify Rubric Structure

Extract these components (not all will be present):

| Component | Description | Priority |
|-----------|-------------|----------|
| **Dimensions** | What aspects are being scored (e.g., accuracy, quality, safety) | Required |
| **Scale** | Score range and what each level means (e.g., 1–5, 0–7, thumbs up/down) | Required |
| **Criteria per level** | What distinguishes a 3 from a 4 on each dimension | Required |
| **Weights** | Are some dimensions more important? How is composite calculated? | If present |
| **Examples** | Sample evaluations showing correct scoring | If present |
| **Edge cases** | Special situations and how to handle them | If present |
| **Anti-patterns** | Common mistakes to avoid | If present |
| **Output format** | How to submit evaluations on the platform | If present |
| **Task flow** | Step-by-step process for completing a task | If present |

### Step 3 — Normalize Terminology

Map the rubric's terminology to the standard evaluation vocabulary:

| Rubric might say... | Standard term |
|---------------------|---------------|
| "Faithfulness" / "Adherence" / "Prompt alignment" | Instruction Following |
| "Correctness" / "Factual accuracy" / "Groundedness" | Object Accuracy or Citation Grounding |
| "Fluency" / "Naturalness" / "Readability" | Visual/Text Quality |
| "Helpfulness" / "Usefulness" / "Relevance" | Instruction Following (broader) |
| "Harmlessness" / "Safety" / "Toxicity" | Safety |
| "Preference" / "Better response" / "Side-by-side" | Preference Ranking |
| "Overall quality" / "General impression" | Composite / Aesthetic Quality |

Document any terminology that doesn't map cleanly — these are important for calibration.

### Step 4 — Generate Structured Output

Produce these files:

#### 4a. Rubric Summary (always)

```markdown
# [Campaign Name] — Rubric Summary

## Overview
- **Campaign:** [name]
- **Platform:** [platform name]
- **Task type:** [image eval / code eval / preference / etc.]
- **Scale:** [0–7 / 1–5 / binary / etc.]
- **Dimensions:** [count]

## Dimensions

### [Dimension 1 Name]
**Maps to:** [standard term]
**Weight:** [X or equal]
**Scale interpretation:**
- [Highest score]: [criteria]
- [Mid score]: [criteria]
- [Lowest score]: [criteria]
**Key differentiators:** [What separates adjacent scores]

[Repeat for each dimension]

## Composite Calculation
[How are dimension scores combined? Weighted mean? Gate logic?]

## Special Rules
[Any campaign-specific rules, e.g., "Safety 0 = auto-fail"]

## Terminology Map
| Rubric term | Standard term | Notes |
|-------------|---------------|-------|
| [term] | [standard] | [any nuance] |
```

#### 4b. Scoring Criteria Detail (if source has per-level criteria)

Full criteria table for each dimension with specific descriptions per score level, following the format in `image-eval-scoring/references/rubric-dimensions.md`.

#### 4c. Edge Cases & Calibration Notes (if source has examples or edge cases)

Extracted examples reformatted as calibration anchors, following the format in `image-eval-scoring/references/edge-cases.md`.

#### 4d. Platform Instructions (if source includes workflow/submission guidance)

Step-by-step task flow extracted and formatted for quick reference.

### Step 5 — Identify Gaps

After extraction, explicitly flag:
- Dimensions that are vaguely defined (no clear criteria per level)
- Score levels with no examples
- Missing edge case guidance for predictable ambiguities
- Contradictions between different parts of the rubric
- Terminology used inconsistently

Report these as: "⚠️ Rubric gaps identified — these may cause scoring inconsistency:"

### Step 6 — Suggest Calibration Questions

Based on the rubric, generate 3–5 calibration questions the evaluator should resolve before starting:

```
1. "The rubric says [X] for dimension [Y] — does this mean [interpretation A] or [interpretation B]?"
2. "Score level [N] and [N+1] overlap when [situation] — which should take priority?"
3. "The rubric doesn't address [common scenario] — should I score it as [X] or [Y]?"
```

These questions help the evaluator calibrate before real tasks arrive.

## Rubric Diff Mode

When an existing campaign's rubric is updated:

1. Load the previous rubric summary
2. Compare against the new document
3. Produce a diff highlighting:
   - New dimensions added
   - Removed dimensions
   - Changed criteria (with old → new)
   - Changed weights
   - New edge cases or rules
4. Flag anything that would change how previously-scored tasks would be evaluated

## Quick Rubric Templates

For campaigns that don't provide detailed rubrics, offer these starter templates:

- **Image Quality (6D)**: Safety, IF, Text, OA, VQ, AQ — link to image-eval-scoring
- **Code Quality (4D)**: Correctness, Efficiency, Style, Completeness
- **Response Quality (5D)**: Helpfulness, Accuracy, Safety, Clarity, Completeness
- **Binary Preference**: Which is better + strength + reason
- **Likert (5-point)**: Strongly disagree → Strongly agree per statement

## Integration with Other Skills

- Output files are formatted to be directly usable as reference files by evaluation skills (e.g., `image-eval-scoring`)
- Other skills can check for rubric interpreter output when configuring evaluation sessions
- Rubric summaries can be used as briefing material at the start of evaluation work
