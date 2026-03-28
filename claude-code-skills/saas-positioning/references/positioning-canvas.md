# Positioning Canvas Template

The positioning canvas is a one-page summary of all 6 positioning components
plus the positioning statement. It is the single artifact that gets printed,
pinned to the wall, and referenced in every strategy meeting.

---

## Blank Template

```
┌─────────────────────────┬─────────────────────────┬─────────────────────────┐
│    TARGET CUSTOMER      │    MARKET CATEGORY      │  COMPETITIVE            │
│                         │                         │  ALTERNATIVES           │
│ ICP:                    │ Category:               │                         │
│ ________________________│ ________________________│ 1. ____________________│
│                         │                         │    Weakness: _________ │
│ Buyer Persona:          │ Strategy:               │ 2. ____________________│
│ ________________________│ [ ] Head-to-Head        │    Weakness: _________ │
│                         │ [ ] Subcategory         │ 3. ____________________│
│ Key Trigger:            │ [ ] New Category        │    Weakness: _________ │
│ ________________________│                         │ 4. ____________________│
│                         │ Education Tax:          │    Weakness: _________ │
│ Anti-Persona:           │ [ ] None  [ ] Low       │ 5. ____________________│
│ ________________________│ [ ] Medium  [ ] High    │    Weakness: _________ │
│                         │                         │                         │
├─────────────────────────┼─────────────────────────┼─────────────────────────┤
│   UNIQUE ATTRIBUTES     │   POSITIONING           │   VALUE THEMES          │
│                         │   STATEMENT             │                         │
│ Cluster 1: ____________ │                         │ Theme 1: ______________ │
│   Evidence: ___________ │ For __________________ │   Proof: ______________ │
│                         │ Who __________________ │   Category: Revenue /   │
│ Cluster 2: ____________ │ [Product] is a _______ │   Cost / Time / Risk /  │
│   Evidence: ___________ │ That _________________ │   Strategic             │
│                         │ Unlike ________________│                         │
│ Cluster 3: ____________ │ We ___________________ │ Theme 2: ______________ │
│   Evidence: ___________ │                         │   Proof: ______________ │
│                         │ SHORT FORM (≤25 words): │   Category: __________ │
│ Cluster 4: ____________ │ _______________________ │                         │
│   Evidence: ___________ │ _______________________ │ Theme 3: ______________ │
│                         │                         │   Proof: ______________ │
│                         │                         │   Category: __________ │
├─────────────────────────┴─────────────────────────┴─────────────────────────┤
│   RELEVANT TRENDS                                                           │
│                                                                             │
│ Trend 1: ___________________________  Connection: ________________________ │
│ Trend 2: ___________________________  Connection: ________________________ │
│ Trend 3: ___________________________  Connection: ________________________ │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Worked Example 1: Developer Observability Platform

**Context:** A mid-stage SaaS company ($3M ARR) that started as a "monitoring tool"
but repositioned to "production reliability platform" to escape commoditized
monitoring category and target engineering leaders instead of individual devs.

```
┌─────────────────────────┬─────────────────────────┬─────────────────────────┐
│    TARGET CUSTOMER      │    MARKET CATEGORY      │  COMPETITIVE            │
│                         │                         │  ALTERNATIVES           │
│ ICP:                    │ Category:               │                         │
│ Series A-C SaaS         │ Production Reliability  │ 1. Datadog              │
│ companies, 50-500 eng,  │ Platform                │    Too expensive at     │
│ running microservices   │                         │    scale, alert fatigue  │
│ on AWS/GCP              │ Strategy:               │ 2. PagerDuty + Grafana  │
│                         │ [x] Subcategory         │    Fragmented, no       │
│ Buyer Persona:          │ (Reliability > Monitoring│   unified view         │
│ VP Engineering or       │  for SaaS teams)        │ 3. In-house scripts     │
│ Head of Platform Eng,   │                         │    Breaks at 20+        │
│ reports to CTO,         │ Education Tax:          │    services, no         │
│ measured on uptime SLA  │ [x] Low                 │    correlation          │
│                         │ (Reliability is known,  │ 4. AWS CloudWatch       │
│ Key Trigger:            │  "platform" adds scope) │    Basic, no cross-     │
│ Just breached SLA or    │                         │    service tracing       │
│ had a P1 incident that  │                         │ 5. Do nothing           │
│ cost revenue            │                         │    (accept downtime)    │
│                         │                         │                         │
│ Anti-Persona:           │                         │                         │
│ Pre-product-market-fit  │                         │                         │
│ startups (<10 eng) —    │                         │                         │
│ monitoring is enough    │                         │                         │
├─────────────────────────┼─────────────────────────┼─────────────────────────┤
│   UNIQUE ATTRIBUTES     │   POSITIONING           │   VALUE THEMES          │
│                         │   STATEMENT             │                         │
│ 1. Auto-instrumentation │                         │ 1. Zero Downtime        │
│    No code changes to   │ For engineering leaders │    Revenue             │
│    get full traces      │ at scaling SaaS         │    Proof: "Customers    │
│    Evidence: 5-min      │ companies               │    report 73% fewer     │
│    setup demo           │ Who cannot afford       │    P1 incidents in      │
│                         │ production incidents    │    first 90 days"       │
│ 2. AI root cause        │ that cost revenue       │    Category: Risk       │
│    analysis             │ ReliableOps is a        │                         │
│    Finds root cause in  │ production reliability  │ 2. Engineering Hours    │
│    <2 min vs 45 min avg │ platform                │    Back                 │
│    Evidence: Customer   │ That cuts P1            │    Proof: "Saves 12     │
│    benchmark data       │ resolution time from    │    hrs/eng/month on     │
│                         │ hours to minutes        │    incident response"   │
│ 3. SLA compliance       │ Unlike monitoring tools │    Category: Time       │
│    dashboard            │ that alert after damage │                         │
│    Real-time SLA burn   │ is done                 │ 3. Predictable          │
│    rate, not just       │ We predict and prevent  │    Scaling              │
│    uptime %             │ incidents before they   │    Proof: "Supports     │
│    Evidence: CFO loves  │ reach customers using   │    10x traffic growth   │
│    this (3 testimonials)│ auto-instrumentation    │    without re-arch"     │
│                         │ and AI root cause       │    Category: Strategic  │
│                         │ analysis                │                         │
│                         │                         │                         │
│                         │ SHORT FORM:             │                         │
│                         │ ReliableOps predicts    │                         │
│                         │ and prevents production │                         │
│                         │ incidents for scaling   │                         │
│                         │ SaaS teams.             │                         │
├─────────────────────────┴─────────────────────────┴─────────────────────────┤
│   RELEVANT TRENDS                                                           │
│                                                                             │
│ 1. AI-assisted ops — Connection: Our AI root cause analysis is built on     │
│    proprietary incident data from 200+ SaaS companies, not generic LLMs     │
│ 2. SLA-driven contracts — Connection: Enterprise customers increasingly     │
│    demand 99.99% SLAs; our SLA dashboard makes compliance visible to        │
│    CFOs, not just engineers                                                 │
│ 3. Platform engineering rise — Connection: Platform teams are the buyer;     │
│    our tool is built for platform eng workflows, not individual dev debugging│
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Worked Example 2: AI-Powered Hiring Platform

**Context:** An early-stage SaaS ($500K ARR) repositioning from "AI recruiting tool"
to "skills-based hiring platform" to differentiate from 50+ AI recruiting tools
and target mid-market companies struggling with bias and quality-of-hire.

```
┌─────────────────────────┬─────────────────────────┬─────────────────────────┐
│    TARGET CUSTOMER      │    MARKET CATEGORY      │  COMPETITIVE            │
│                         │                         │  ALTERNATIVES           │
│ ICP:                    │ Category:               │                         │
│ Mid-market companies    │ Skills-Based Hiring     │ 1. LinkedIn Recruiter   │
│ (200-2000 employees),   │ Platform                │    Resume-first, no     │
│ hiring 20+ roles/qtr,   │                         │    skills validation    │
│ in regulated industries │ Strategy:               │ 2. Greenhouse + HackerR │
│ (finance, healthcare,   │ [x] Subcategory         │    Fragmented, manual   │
│ govt contracting)       │ (Skills-based > general │    skills assessment    │
│                         │  recruiting for         │ 3. Internal recruiters  │
│ Buyer Persona:          │  regulated industries)  │    + spreadsheets       │
│ VP People / Head of TA, │                         │    Subjective, slow,    │
│ reports to CHRO,        │ Education Tax:          │    inconsistent         │
│ measured on quality-of- │ [x] Low                 │ 4. Hired/Vettery        │
│ hire and time-to-fill   │ ("Skills-based" is      │    Marketplace model,   │
│                         │  trending, understood)  │    expensive per-hire   │
│ Key Trigger:            │                         │ 5. Do nothing           │
│ Failed audit on hiring  │                         │    (accept bias risk    │
│ practices, or lawsuit   │                         │    and bad hires)       │
│ risk from bias          │                         │                         │
│                         │                         │                         │
│ Anti-Persona:           │                         │                         │
│ <50 employee startups — │                         │                         │
│ they hire by network    │                         │                         │
│ and don't need process  │                         │                         │
├─────────────────────────┼─────────────────────────┼─────────────────────────┤
│   UNIQUE ATTRIBUTES     │   POSITIONING           │   VALUE THEMES          │
│                         │   STATEMENT             │                         │
│ 1. Blind skills         │                         │ 1. Audit-Ready Hiring   │
│    assessments          │ For talent leaders at   │    Proof: "100% of      │
│    Removes name, school,│ mid-market regulated    │    customers passed     │
│    company from eval    │ companies               │    EEOC audit in first  │
│    Evidence: 40% more   │ Who need defensible,    │    year"                │
│    diverse shortlists   │ bias-free hiring at     │    Category: Risk       │
│                         │ scale                   │                         │
│ 2. Regulatory           │ SkillMatch is a skills- │ 2. Quality of Hire      │
│    compliance engine    │ based hiring platform   │    Proof: "87% of       │
│    Auto-generates EEOC, │ That makes every hiring │    hires rated 'exceeds │
│    OFCCP, and SOX       │ decision evidence-based │    expectations' at     │
│    compliant records    │ and audit-ready         │    12-month review"     │
│    Evidence: Built with │ Unlike recruiting tools │    Category: Strategic  │
│    employment lawyers   │ that digitize the       │                         │
│                         │ resume-first process    │ 3. 50% Faster Hiring    │
│ 3. Predictive job       │ We validate actual      │    Proof: "Time-to-fill │
│    performance scoring  │ skills before reviewing │    drops from 47 to 23  │
│    ML model trained on  │ any biographical data,  │    days on average"     │
│    200K+ hire outcomes  │ with built-in           │    Category: Time       │
│    Evidence: Peer-      │ regulatory compliance   │                         │
│    reviewed paper       │                         │                         │
│                         │ SHORT FORM:             │                         │
│                         │ SkillMatch replaces     │                         │
│                         │ resume-first recruiting │                         │
│                         │ with blind, skills-     │                         │
│                         │ based hiring for        │                         │
│                         │ regulated industries.   │                         │
├─────────────────────────┴─────────────────────────┴─────────────────────────┤
│   RELEVANT TRENDS                                                           │
│                                                                             │
│ 1. Skills-based hiring movement — Connection: We operationalize what others │
│    only talk about; our blind assessments actually remove bias, not just     │
│    claim to                                                                 │
│ 2. Regulatory pressure on hiring (EEOC, EU AI Act) — Connection: Our        │
│    compliance engine is the only one built with employment lawyers and       │
│    auto-generates audit-ready records                                        │
│ 3. AI scrutiny in HR — Connection: While competitors face backlash for      │
│    opaque AI, our skills assessments are fully explainable and auditable    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## How to Use the Canvas

1. **Fill it in last** — after completing all 6 components of the positioning framework.
   The canvas is a summary, not a starting point.

2. **Test it with the "new hire" test** — give the completed canvas to someone
   unfamiliar with the product. Can they explain what the company does, who it
   is for, and why it is different after 2 minutes of reading?

3. **Print it** — physically print it and put it where the team can see it.
   Digital documents get forgotten. Physical artifacts drive alignment.

4. **Review quarterly** — not to change it (positioning needs 6-12 months to
   work), but to verify that execution still aligns with the canvas. If
   marketing, sales, and product are drifting from the canvas, either the
   execution or the canvas needs adjustment.

5. **Use it as a decision filter** — when debating features, messaging, or
   partnerships, ask "does this reinforce our positioning canvas?" If not,
   either the opportunity is off-strategy or the canvas needs updating.
