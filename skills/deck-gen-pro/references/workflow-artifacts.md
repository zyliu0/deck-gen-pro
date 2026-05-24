# Workflow Artifacts

Use these markdown artifacts as the default scaffold after the user approves the initial plan-mode path. For a new or high-stakes deck, keep the artifacts separate so the process stays slow, inspectable, and user-confirmable. For a small revision, QA-only pass, or user-authorized autonomous run, combine or skip artifacts when that reduces noise; record the reason in build or QA notes.

## 00-plan-mode-brief.md

Purpose: start the deck project with an explicit planning gate before any files, research, style references, or slides are created.

Use the platform's Plan Mode control when available. If no explicit control is available, produce the brief conversationally and ask for approval before execution.

Recommended content:

```markdown
# Plan Mode Brief

## Deck Request
- Topic:
- Audience:
- Desired outcome:
- Preferred output format:

## Proposed Workflow
1. Brief: confirm goal, audience, constraints, and output format.
2. Material: audit local sources and gather missing evidence/assets only when needed.
3. Direction: choose a visual direction and test it with real slide-like comps.
4. Structure: write the slide-by-slide story plan.
5. Assets: assign visuals by role, provenance, fit behavior, and fallback.
6. Build: produce the editable deck in the best format for the request.
7. QA: render previews, review the contact sheet, fix issues, and hand off.

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

Recommended sections:

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

## Source Constraints
- Approved source sets:
- Rejected or outdated source sets:
- Forbidden phrases, claims, or visual treatments:
- Required sections, chapters, or narrative beats:
- Source deck/template rules:

## Missing Material
| Need | Why it matters | How to obtain |
|---|---|---|

## Initial Deck Hypothesis
- Likely narrative:
- Likely proof objects:
- Likely visual direction:
- Likely visual roles:
  - Proof:
  - Mood:
  - Metaphor:
  - Texture:
  - Generated-reference:

## Risks
- Evidence risk:
- Asset risk:
- Source-constraint risk:
- Visual rhythm risk:
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

Recommended sections:

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
| Asset idea | Source/generation plan | Visual role | Use case | Risk |
|---|---|---|---|---|

## Open Questions
- 
```

Stage gate question:

```text
I have enough source material to proceed. The main evidence base is [summary]. The unresolved questions are [list]. Should I move to visual style recommendations?
```

## 03-style-direction.md

Purpose: record the selected style, practical layout rules, rendered comp QA, and reference-image/composition approval.

Recommended sections:

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
- Palette logic:
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
- Image fit behavior:
- Diagram/proof-object handling:
- Text fit behavior:
- Visual rhythm principles:
- Generated-image boundaries:

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
- When to use cover:
- When to use contain:
- When to use a designed frame:
- How captions align to images/cards:
- Where captions should not appear:
- How blank space should be handled:
- How proof-object framing should work:
- How mood, metaphor, and texture images differ from proof images:

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

Pause before slide-structure generation until this file includes both visual mood rules and practical layout rules for long text, screenshots, captions, cards, diagrams, and proof objects. For a narrow revision, record which rules already exist and which ones are unnecessary for the requested change.

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
- Arc type:
- Opening move:
- Core tension or question:
- Development path:
- Proof, texture, or demonstration:
- Closing action or feeling:
- Notes on why this arc fits:
```

For every slide:

```markdown
## Slide NN: [Topic]

- Topic: [single topic only]
- Claim/title: [clear sentence title]
- Narrative role: [context/tension/insight/proof/recommendation/close/appendix]
- Audience takeaway: [what the viewer should remember]
- Layout: [chosen style layout pattern]
- Composition mode: [common modes include image-led, text-led, diagram-led, data-led, split image-text, full-bleed image with restrained text, proof-led, mostly negative space, or a custom mode]
- Visual rhythm intent: [why this slide should feel this way in the sequence]
- Practical style rules:
  - Long-text handling:
  - Screenshot/caption handling:
  - Card/proof-object handling:
  - Image fit behavior:
  - Text fit risk:
- Text hierarchy:
  - Title:
  - Primary copy:
  - Secondary copy:
  - Caption/footer:
- Proof object: [chart/image/table/quote/diagram/comparison/timeline/big number/other support object]
- Source references:
  - [source id or URL]
- Visual assets:
  - [asset_id or needed asset]
- Image assignment:
- Visual role: [common roles include proof, mood, metaphor, texture, category context, generated, none, or custom]
- Fit behavior: [cover/contain/designed frame/none/other aspect-ratio-safe treatment]
  - Crop/framing:
  - Multiple-image grid rules:
  - Why image use or restraint is intentional:
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

Before production, add a deck-level pass:

```markdown
## Visual Rhythm Pass

| Slide | Composition mode | Visual role | Balance note | Revision needed |
|---|---|---|---|---|

## Rhythm Judgment
- Does the thumbnail sequence feel too text-heavy or card-heavy?
- Are strong visual moments present where the story needs emotional pacing or category presence?
- Are image-led slides clustered awkwardly or absent for too long?
- Are proof images large enough to understand?
- Are generated or atmospheric images clarifying the story rather than decorating it?
- Which text-only slides are intentionally text-only?
```

Stage gate question:

```text
Here is the proposed slide-by-slide structure. Should I build this deck as-is, revise the flow, or change the slide count before production?
```

## assets/asset-manifest.md

Purpose: prevent random image use and make visual assignment auditable.

Recommended format:

```markdown
# Asset Manifest

| asset_id | Type | Path/URL | Source/provenance | Quality | Intended slides | Visual role | Fit behavior | Fallback |
|---|---|---|---|---|---|---|---|---|
```

Rules:

- Use stable asset IDs such as `img-hero-venue-01`, `chart-market-02`, `logo-client-01`.
- Separate downloaded, generated, screenshot, and user-provided assets.
- Keep generated image prompts near the asset entry or in a linked prompt file.
- Distinguish proof assets from mood, metaphor, texture, category-context, and generated assets.
- Record whether each visual should use cover, contain, a designed frame, or remain undecided until composition.
- Mark any asset that is not approved or has unclear usage.

## 05-build-notes.md

Purpose: record implementation decisions.

Include:

- output format
- toolchain used
- slide source mapping
- source constraints applied
- fonts and fallbacks
- image placement decisions
- text fit decisions
- asset processing notes
- known compromises
- final export path

## 06-qa-notes.md

Purpose: prove the deck was reviewed after rendering.

Include:

- preview/contact sheet paths
- source constraint QA
- factual QA notes
- deck-level visual balance QA
- visual QA notes
- image distortion/aspect-ratio checks
- text overlap, overflow, and wrapping checks
- final file check
- spacing, padding, and margin consistency checks
- typography behavior checks
- image crop and caption relationship checks
- image assignment QA
- generated images are not treated as factual proof
- package/file checks are not treated as visual QA
- user critique translated into style-rule updates
- fixes made
- remaining risks

Deck-level visual balance QA should ask:

```markdown
## Deck-Level Visual Balance QA

- Contact sheet reviewed:
- Thumbnail sequence feels intentionally balanced:
- Text-heavy or card-heavy stretches found:
- Image-led moments checked for pacing:
- Proof images large enough to understand:
- Atmospheric/metaphor/generated visuals clarify the story:
- Text-only slides are intentional:
```

Source and production QA should ask:

```markdown
## Source Constraint QA

- Approved sources used:
- Rejected or outdated assets excluded:
- Forbidden content absent:
- Required sections preserved:
- Source deck/template rules followed:

## Image Distortion QA

- Rendered slides reviewed:
- Images preserve aspect ratio:
- Cover crops keep important content visible:
- Contained images use intentional framing/empty space:
- Logos, screenshots, products, rooms, people, and diagrams look natural:

## Final File Check

- Deck opens:
- Media embedded:
- Expected slide count:
- Preview/contact sheet reviewed:
- Visual QA completed after rendering:
```

## archive/style-iterations/index.md

Purpose: preserve visible iterations so earlier directions can be compared later.

Recommended format:

```markdown
# Style Iteration Archive

| Iteration | Date | Path | Summary | User/design signal |
|---|---:|---|---|---|
```

Rules:

- Save visible style comps or rendered previews when exploring multiple directions.
- Add a short index entry for each direction or meaningful revision.
- If user critique reveals a system-level issue, describe the updated style rule in the index or link to `03-style-direction.md`.
