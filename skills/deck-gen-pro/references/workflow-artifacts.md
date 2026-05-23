# Workflow Artifacts

Create these markdown artifacts in order after the user approves the initial plan-mode path. Do not combine them into one file; the separation is what keeps the deck process slow, inspectable, and user-confirmable.

## 00-plan-mode-brief.md

Purpose: start the deck project with an explicit planning gate before any files, research, style references, or slides are created.

Use the platform's Plan Mode control when available. If no explicit control is available, produce the brief conversationally and ask for approval before execution.

Required content:

```markdown
# Plan Mode Brief

## Deck Request
- Topic:
- Audience:
- Desired outcome:
- Preferred output format:

## Proposed Workflow
1. Create workspace and audit materials.
2. Research or collect missing evidence/assets if needed.
3. Recommend visual styles.
4. Generate style reference images or comps.
5. Write slide-structure markdown.
6. Assign images through an asset manifest.
7. Build the deck.
8. Render and QA.

## First Execution Step
- What I will inspect first:
- What I will not do yet:
```

Stage gate question:

```text
I will start this deck in plan mode and pause production until you approve the workflow. Should I create the workspace and audit available material first?
```

## 01-material-audit.md

Purpose: decide whether the working environment already has enough material.

Required sections:

```markdown
# Material Audit

## User Request
- Topic:
- Audience:
- Desired outcome:
- Requested format:

## Available Material
| Item | Path/URL | Type | Usefulness | Notes |
|---|---|---|---|---|

## Missing Material
| Need | Why it matters | How to obtain |
|---|---|---|

## Initial Deck Hypothesis
- Likely narrative:
- Likely proof objects:
- Likely visual direction:

## Risks
- Evidence risk:
- Asset risk:
- Brand risk:
- Timeline/tooling risk:

## Decision
enough-material: yes/no/partial
next-stage:
```

Stage gate question:

```text
I found [enough/not enough/partial] material for the deck. Here is the base I would use: [short summary]. Should I continue to [style interview/research], or would you like to add or change source material first?
```

## 02-research-notes.md

Purpose: capture source-backed facts and asset candidates.

Required sections:

```markdown
# Research Notes

## Research Goal
- What needs to be resolved:
- Why current materials are insufficient:

## Source Log
| Source | URL/path | Date accessed | Reliability | Relevant facts/assets |
|---|---|---:|---|---|

## Facts And Claims
| Claim | Evidence | Source | Slide candidate | Confidence |
|---|---|---|---|---|

## Visual Asset Candidates
| Asset idea | Source/generation plan | Use case | Risk |
|---|---|---|---|

## Open Questions
- 
```

Stage gate question:

```text
I have enough source material to proceed. The main evidence base is [summary]. The unresolved questions are [list]. Should I move to visual style recommendations?
```

## 03-style-direction.md

Purpose: record the selected style, practical layout rules, rendered comp QA, and reference-image/composition approval.

Required sections:

```markdown
# Style Direction

## Recommended Options
| Option | Why it fits | Tradeoffs |
|---|---|---|

## User Selection
- Selected style:
- User modifications:
- Rejected directions:

## Design System
- Palette:
- Typography:
- Layout grammar:
- Chart/diagram style:
- Image treatment:
- Accent rules:

## Practical Layout Rules
- Spacing system:
- Card interiors:
- Outer margins and object gaps:
- Title and subtitle behavior:
- Caption placement:
- Long-text handling:
- Screenshot handling:
- Photo crop handling:
- Diagram/proof-object handling:

## Typography Behavior
- Font weight and density:
- Wrap risks:
- CJK or multilingual risks:
- Baseline/overflow risks:
- Hierarchy adjustments:

## Text Economy Rules
- On-slide copy limit principles:
- What moves to speaker notes:
- What moves to supporting markdown:
- When to simplify a card or diagram:

## Image And Caption Rules
- How captions align to images/cards:
- Where captions should not appear:
- How blank space should be handled:
- How proof-object framing should work:

## Reference Images Or Comps
| Ref | Path/URL | What to borrow | What to avoid |
|---|---|---|---|

## Visual QA Before Approval
- Rendered output inspected:
- Text overlap/overflow fixed:
- Spacing and padding consistency checked:
- Caption/image relationship checked:
- Hierarchy checked:
- Awkward empty space checked:
- Fixes made:

## Iteration Archive
| Iteration | Path | What changed | Why it changed |
|---|---|---|---|

## Application Rules
- Titles:
- Body text:
- Charts:
- Images:
- Section dividers:
```

Stage gate question:

```text
I have prepared the style direction, layout rules, reference comps, and visual QA notes. Does this feel like the right deck style, or should I revise the visual system before outlining slides?
```

Do not proceed to slide-structure generation until this file includes both visual mood rules and practical layout rules for long text, screenshots, captions, cards, diagrams, and proof objects.

## 04-slide-structure.md

Purpose: define the deck before any slide generation.

Start with:

```markdown
# Slide Structure

## Deck Thesis

## Audience And Decision
- Audience:
- Decision/action requested:
- Tone:

## Narrative Arc
1. Context:
2. Tension:
3. Insight:
4. Recommendation:
5. Proof:
6. Close:
```

For every slide:

```markdown
## Slide NN: [Topic]

- Topic: [single topic only]
- Claim/title: [clear sentence title]
- Narrative role: [context/tension/insight/proof/recommendation/close/appendix]
- Audience takeaway: [what the viewer should remember]
- Layout: [chosen style layout pattern]
- Practical style rules:
  - Long-text handling:
  - Screenshot/caption handling:
  - Card/proof-object handling:
- Text hierarchy:
  - Title:
  - Primary copy:
  - Secondary copy:
  - Caption/footer:
- Proof object: [chart/image/table/quote/diagram/comparison/timeline/big number]
- Source references:
  - [source id or URL]
- Visual assets:
  - [asset_id or needed asset]
- Image assignment:
  - Role:
  - Crop/framing:
  - Multiple-image grid rules:
- Data/chart instructions:
  - Metric:
  - Unit:
  - Comparison:
  - Annotation:
- Speaker/notes intent:
- QA checks:
  - Title states a point:
  - One topic only:
  - Evidence present:
  - Image assigned:
```

Stage gate question:

```text
Here is the proposed slide-by-slide structure. Should I build this deck as-is, revise the flow, or change the slide count before production?
```

## assets/asset-manifest.md

Purpose: prevent random image use and make visual assignment auditable.

Required format:

```markdown
# Asset Manifest

| asset_id | Type | Path/URL | Source/provenance | Quality | Intended slides | Role | Fallback |
|---|---|---|---|---|---|---|---|
```

Rules:

- Use stable asset IDs such as `img-hero-venue-01`, `chart-market-02`, `logo-client-01`.
- Separate downloaded, generated, screenshot, and user-provided assets.
- Keep generated image prompts near the asset entry or in a linked prompt file.
- Mark any asset that is not approved or has unclear usage.

## 05-build-notes.md

Purpose: record implementation decisions.

Include:

- output format
- toolchain used
- slide source mapping
- fonts and fallbacks
- asset processing notes
- known compromises
- final export path

## 06-qa-notes.md

Purpose: prove the deck was reviewed after rendering.

Include:

- preview/contact sheet paths
- factual QA notes
- visual QA notes
- text overlap, overflow, and wrapping checks
- spacing, padding, and margin consistency checks
- typography behavior checks
- image crop and caption relationship checks
- image assignment QA
- user critique translated into style-rule updates
- fixes made
- remaining risks

## archive/style-iterations/index.md

Purpose: preserve visible iterations so earlier directions can be compared later.

Required format:

```markdown
# Style Iteration Archive

| Iteration | Date | Path | Summary | User/design signal |
|---|---:|---|---|---|
```

Rules:

- Save visible style comps or rendered previews when exploring multiple directions.
- Add a short index entry for each direction or meaningful revision.
- If user critique reveals a system-level issue, describe the updated style rule in the index or link to `03-style-direction.md`.
