---
name: deck-gen-pro
description: Professional staged deck-making workflow for creating, planning, or upgrading presentations, slide decks, pitch decks, PowerPoint/PPTX decks, Canva presentations, or HTML slide prototypes. Use when the user asks for a deck or slides and wants the work to begin in plan mode, then proceed through high-quality research, narrative structure, visual style selection, reference images, image sourcing or generation, and step-by-step approval instead of one-shot slide generation.
---

# Deck Gen Pro

## Overview

Use this skill to make professional decks slowly and deliberately. The first action is to enter or initialize plan mode. Do not start by generating slides. Move through gated stages: plan-mode brief, material audit, research and asset gathering, style interview, style references, slide-structure markdown, final deck production, and QA.

This skill orchestrates the host agent's available deck tools. Prefer an editable PPTX-capable workflow for professional deliverables, use template-preserving presentation tools when a source deck is supplied, use Canva or another design platform only when requested, and use browser, file, screenshot, research, and image-generation tools when they are available and relevant.

## Non-Negotiables

- Ask for user confirmation at every stage gate before moving to the next stage.
- Begin in plan mode before creating files, researching, choosing style, or building slides.
- Keep all planning artifacts as markdown before final deck generation.
- Inspect rendered outputs before showing them for approval; fix obvious visual defects first.
- Use exact source material for facts, names, dates, quotes, claims, and metrics.
- Never invent missing evidence, charts, logos, screenshots, or user-provided brand facts.
- Each slide must have one clear topic, one role in the story, and a logical connection to adjacent slides.
- Each slide must have an obvious title that states the point, not a vague label.
- Assign images systematically with an asset manifest before building slides.
- Generate or download images only when the deck structure says why that image is needed.
- Prefer editable PPTX for final professional deliverables unless the user requests Canva, HTML, PDF, or another format.

## Design Judgment Rules

Apply these rules throughout style exploration and deck production. They are judgment rules, not fixed templates.

- Treat style-reference comps as real slide layout tests, not moodboards. A useful comp proves whether typography, spacing, image crops, captions, card interiors, diagrams, charts, and other proof objects can actually work together on a slide.
- Establish a spacing system for each visual direction. Outer margins, card padding, gaps between objects, caption placement, title spacing, and proof-object breathing room should feel intentional and consistent across comps and slides.
- Account for font behavior. Serif faces, CJK typefaces, display titles, and dense labels can wrap, feel heavier, shift baselines, or overflow differently than expected. Adjust hierarchy, line breaks, and copy length to protect readability and elegance.
- Keep on-slide text economical. If a card, chart, or diagram needs cramped copy, simplify the visible phrase and move nuance into speaker notes, research notes, or supporting markdown instead of shrinking text until the layout becomes fragile.
- Treat screenshots and photos as proof objects. Crop them deliberately, keep important content visible, and align captions to the image or card system. Captions should not float arbitrarily, sit over important visual content, or create blank holding areas.
- Preserve visible iterations when exploring multiple directions. Save prior comps or rendered slide previews in an archive folder with a short index so the user can compare earlier directions later.
- Treat user critique as a design-system signal when appropriate. Feedback about padding, overflow, captions, hierarchy, image crop, or awkward empty space should update the style rules before more slides are generated, not just patch one local object.

## Visual QA Before Approval

Before asking the user to approve style comps or final slides, render or preview the output and inspect it visually. Fix obvious problems first:

- text overlap, clipping, overflow, or fragile wrapping
- inconsistent padding, uneven margins, cramped cards, or arbitrary gaps
- captions sitting on top of images or disconnected from their proof object
- unclear hierarchy between title, body, proof object, caption, and source
- awkward empty space that looks accidental rather than designed
- screenshots or photos cropped in a way that hides the important evidence
- chart, table, or diagram labels that cannot be read at presentation size

Record the QA pass in the relevant style, build, or QA notes. If the render reveals that the style direction is not practical, revise the style rules before asking for approval.

## Stage-Gated Workflow

### 0. Initialize Plan Mode

Enter the platform's plan mode before doing deck work. If the environment has an explicit Plan Mode or EnterPlanMode control, use it immediately. If no explicit control is available, simulate plan mode by stating that production is paused, giving a short plan, and asking the user to approve the first execution step.

In plan mode:

- restate the deck topic, audience, output format, and known source material
- list the staged workflow you will follow
- identify what you need to inspect first
- ask only the minimum needed question if the request is too ambiguous to audit materials
- do not generate slides, style comps, downloaded assets, or final deck files

Leave plan mode only after the user approves the initial execution path. The first executable step after approval is workspace creation and material audit.

### 1. Create Working Folder

Create a task folder and starter artifacts with:

```bash
python3 <skill-dir>/scripts/init_deck_workspace.py "<deck topic or task slug>" --root outputs
```

Use the generated folder for all notes, research, assets, style references, structure markdown, previews, and QA.

### 2. Material Audit

Inspect the working environment before researching. Look for user-provided files, existing notes, brand assets, previous decks, source documents, datasets, screenshots, images, and URLs.

Write `01-material-audit.md` with:

- available sources and assets
- missing information
- likely deck audience and purpose
- risks such as weak evidence, no visuals, unclear brand, or missing metrics
- decision: `enough-material: yes/no/partial`

If material is enough, ask the user to confirm the interpretation before style work. If not enough, propose the research or creative asset plan first.

### 3. Research And Asset Collection

Use this stage only when the audit is `no` or `partial`, or when the user asks for current facts, source links, real product/place/person imagery, charts, or creative art direction.

Write `02-research-notes.md` and `assets/asset-manifest.md`. Capture:

- source links, dates, and reliability notes
- facts and metrics with provenance
- downloaded images/screenshots and allowed usage constraints when known
- generated image prompts and outputs, if creative imagery is appropriate
- asset-to-slide candidates, even before the final slide structure is locked

Ask the user to approve the material base before recommending visual styles.

### 4. Visual Style Interview

Read `references/style-systems.md`. Recommend 2-3 style systems that fit the topic, audience, evidence density, and available assets. Present the recommendation as an interview-style prompt with:

- a short explanation of why each style fits
- color, layout, imagery, and chart implications
- a free-form option for the user to describe another direction

Do not proceed until the user chooses or modifies a direction.

### 5. Style Reference Images

After style approval, create a small set of style reference images or comps. These are not the final deck and not HTML slides. They are real layout tests showing whether the visual system can support actual slide content: title hierarchy, proof objects, card interiors, screenshots, photos, captions, charts, diagrams, and source notes.

Write `03-style-direction.md` with:

- selected style system
- exact palette and type direction
- practical spacing rules for margins, gaps, cards, captions, title areas, and proof objects
- typography behavior notes, including wrap risk, visual weight, and hierarchy adjustments
- text economy rules for cards, diagrams, long titles, and speaker-note overflow
- image and caption rules for screenshots, photos, crops, cards, and blank space
- reference-image prompts or source screenshots
- rendered-output QA notes and fixes made before presentation
- what the user approved or rejected
- rules for applying the style consistently

Archive each visible style iteration in `archive/style-iterations/` with a short `index.md` entry describing what changed and why. Do not overwrite earlier visual directions unless the user explicitly asks to discard them.

Ask the user to approve one direction before writing the deck structure.

### 6. Slide Structure Markdown

Before writing `04-slide-structure.md`, confirm that the selected style direction contains both mood rules and practical layout rules. It must explain how the deck will handle long text, screenshots, captions, cards, diagrams, charts, tables, and other proof objects. If those rules are missing or weak, revise `03-style-direction.md` and ask for approval first.

Write `04-slide-structure.md` before generating slides. Follow `references/workflow-artifacts.md`.

For each slide, specify:

- slide number and topic
- claim/title
- narrative role
- body text hierarchy
- proof object: chart, image, table, quote, diagram, comparison, timeline, or big-number callout
- exact source references for factual claims
- image requirements and asset IDs from `asset-manifest.md`
- layout notes from the chosen style

Ask the user to approve or revise the structure. Do not build slides before approval.

### 7. Image Assignment Pass

Write or update `assets/asset-manifest.md` so every visual asset has:

- `asset_id`
- source path or URL
- license/provenance note when available
- quality notes
- intended slide(s)
- crop/layout role
- fallback plan if the asset fails QA

For slides with multiple images, define grid rules and image hierarchy. Avoid decorative images that do not prove or clarify the slide topic.

### 8. Deck Build

Choose output format using `references/tooling-and-output.md`.

Default to editable PPTX through the best available presentation toolchain. Use generated slide code, a presentation SDK, a native slide editor, or a platform-specific deck tool as appropriate for the current environment. If the user requested a source/template deck, route to template-following and preserve the template structure. If Canva or another design platform is requested, generate candidates and ask the user before creating the final deck.

Build only after the material, style, structure, and image assignment stages are approved.

### 9. QA And Iteration

Render the deck to preview images or a contact sheet. Check:

- story flow and slide topic uniqueness
- factual accuracy and source coverage
- title clarity
- visual hierarchy and contrast
- text overflow and spacing
- chart readability
- image quality, crop, and correct slide assignment
- consistency with the approved style direction
- whether user critiques have been promoted into updated style rules when they affect the system

Fix issues, rerender affected slides, and ask for final user review.

## Reference Files

- `references/style-systems.md`: 10 reusable visual style systems inspired by modern professional template galleries and presentation design guidance.
- `references/workflow-artifacts.md`: required markdown artifacts and schemas for the slow deck workflow.
- `references/tooling-and-output.md`: when to use PPTX, Canva, HTML, PDF, images, and supporting deck tools.

## Completion Standard

Finish with the final deck path or link, the approved style name, source/asset notes, and a concise QA summary. If a stage could not be completed, name the missing input or tool clearly and leave the next required question for the user.
