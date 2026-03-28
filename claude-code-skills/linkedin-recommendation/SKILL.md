---
name: linkedin-recommendation
description: Write compelling, authentic LinkedIn recommendations for colleagues, direct reports, managers, clients, or other professional contacts. Use this skill whenever the user wants to write a LinkedIn recommendation, endorse someone on LinkedIn, draft a professional testimonial, or asks for help recommending a colleague. Also trigger when the user mentions "recommendation for [person]", "LinkedIn rec", "endorse someone", "write a testimonial", "recommend my colleague/boss/employee", or anything related to writing professional endorsements for LinkedIn profiles. Even if the user just says "I need to write something nice about someone at work for LinkedIn", use this skill.
---

# LinkedIn Recommendation Writer

## Purpose

Help the user write LinkedIn recommendations that are specific, authentic, and impactful. Great recommendations aren't generic praise — they tell a mini-story about the person that makes a reader think "I want to work with this person."

LinkedIn recommendations serve as social proof on someone's profile. Recruiters and hiring managers genuinely read them. A vague, cliché-filled recommendation actually hurts more than it helps — it signals the recommender didn't care enough to be specific. The goal is to write something that feels like it could only have been written about *this* person.

## Gathering Context

Before writing anything, Claude needs specific information. Ask the user for what's missing from this list (many users will provide some of this upfront — don't re-ask for what's already been shared):

1. **Who is this for?** Name and their current/relevant role
2. **Your relationship:** How did you work together? (managed them, they managed you, peers, cross-functional, client, etc.)
3. **Duration and context:** How long and where? (e.g., "3 years at Acme Corp on the marketing team")
4. **What made them stand out?** The single most impressive thing about working with them — a project, a trait, a result, a moment. Specificity is everything here.
5. **Skills or qualities to highlight:** What should someone reading this take away? (e.g., leadership, technical expertise, creativity, client management, mentoring)
6. **Any tangible results?** Numbers, awards, outcomes, growth metrics — anything concrete
7. **What's their personality like to work with?** The human side — what made them great to be around, not just effective
8. **What are they targeting?** If known, what kind of role or opportunity are they pursuing? This helps tailor emphasis.

If the user provides raw notes, bullet points, or stream-of-consciousness thoughts, that's perfect — work with whatever level of detail they give. The user doesn't need to answer every question formally.

Also check: does the user want to write in a particular tone? Refer to `writing-style.md` for the user's natural writing patterns and voice.

## Writing the Recommendation

### Structure (flexible, not rigid)

A great LinkedIn recommendation generally flows through these beats. They don't need headers or rigid formatting — this should read as natural prose, typically 3–5 short paragraphs:

**1. A hook that establishes context and sets the tone**
Open with something that immediately tells the reader *who* this person is and *why* you're recommending them. Avoid generic openings like "I'm pleased to recommend..." — instead, lead with what makes this person distinctive.

Strong openers often use one of these patterns:
- A defining characteristic framed memorably: *"Ridiculously efficient is the phrase that comes to mind when I think about Vivek."*
- A specific, attention-grabbing claim: *"In 4 years of working with Sarah, I never once saw her flustered — and we went through three reorgs."*
- A relationship-based setup that implies credibility: *"Few people have the opportunity to report to a manager who is also a coach and mentor — but I did when I worked for Susan."*

**2. Credibility context — your relationship**
Briefly establish how you know them, how long you worked together, and in what capacity. This doesn't need to be a full paragraph — often a sentence woven into the opening or second paragraph is enough. LinkedIn already shows job titles, so focus on the *nature* of the working relationship rather than restating titles.

**3. The standout — what makes them exceptional**
This is the heart of the recommendation. Pick 1–2 things this person does better than almost anyone else and go deep rather than wide. Specificity is what separates a great recommendation from a forgettable one:

- Instead of "great leader" → describe *how* they lead (coaching style, built a team from scratch, empowered people to grow beyond their roles)
- Instead of "hard worker" → describe *what* their work ethic looks like in practice (took on stretch projects, learned an entirely new domain in weeks, consistently delivered under pressure)
- Instead of "great communicator" → describe *a specific situation* where their communication made a difference

Include tangible results, growth stories, or concrete examples wherever possible. A recommendation that mentions "increased lead generation by 45%" or "grew from zero experience to managing a team in two years" is far more compelling than abstract praise.

**4. The human element**
What's it actually *like* to work with this person? This is where personality shines through. A touch of warmth, humor, or genuine affection makes the recommendation feel real rather than corporate. This can be a brief sentence or two — it doesn't need to dominate.

**5. A confident closing endorsement**
End with a clear, forward-looking statement that leaves no doubt about your recommendation. Good closings are enthusiastic but not over-the-top:
- Express that you'd want to work with them again
- State they'd be an asset to any team/organization  
- Say any company that hires them would be lucky
- Express excitement about their future

### What to Avoid

- **Cliché soup:** Strings of adjectives without substance ("dynamic, results-oriented, passionate team player"). Every adjective should be backed by evidence.
- **Covering everything:** Trying to mention every skill dilutes impact. Better to go deep on 1–2 things than shallow on 7.
- **Generic templates that could apply to anyone:** If you could swap in a different name and the recommendation still works perfectly, it's not specific enough.
- **Burying the lead:** Don't waste the opening on throat-clearing. The first sentence should make someone want to keep reading.
- **Excessive length:** LinkedIn recommendations should be 150–300 words (roughly 3–5 short paragraphs). Under 3,000 characters is the hard limit, but punchier is better. Aim for impactful, not exhaustive.
- **Sycophantic or over-the-top language** that undermines credibility. Phrases like "best person in the history of marketing" make the reader trust the recommendation less.
- **Starting every sentence with the person's name.** Vary sentence structure.

## Tone and Voice

The recommendation should sound like a real human wrote it — someone who genuinely knows and respects the person. It should feel:
- **Warm but professional** — not stiff corporate-speak, not overly casual
- **Confident and specific** — the writer clearly knows what they're talking about
- **Generous but credible** — high praise backed by real evidence

Read `writing-style.md` to understand the user's natural voice. The user tends to write with genuine warmth and uses vivid, confident language. Match that energy while tightening structure and specificity.

## Output Format

Present the recommendation as plain text (no markdown formatting, no headers, no bullet points) — exactly as it would appear on LinkedIn. After the draft, briefly note:
- Approximate word count
- A suggestion for which relationship type to select on LinkedIn (e.g., "Boris managed [Name] directly")
- One or two optional tweaks the user could consider

If the user asks for multiple options or variants, provide 2–3 with a brief note on how each differs in emphasis or tone.

## Reference Material

For the user's writing style and past examples, read: `writing-style.md`
