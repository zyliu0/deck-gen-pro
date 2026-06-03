---
name: deck-mason
description: Professional PowerPoint and deck-builder workflow for creating, planning, or upgrading product-grade presentations, slide decks, pitch decks, PowerPoint/PPTX decks, Canva presentations, or HTML slide prototypes. Use when the user asks for a deck or slides and wants the work to begin in plan mode, then slow down through research, narrative structure, visual direction, reference comps, image sourcing or generation, production, and QA instead of one-shot slide generation.
---

# Deck Mason

## Overview

Use this skill to make professional decks slowly and deliberately. The first action is to enter or initialize plan mode. Do not start by generating slides. Treat the deck as a real project that moves through seven broad phases: brief, material base, visual direction, slide structure, asset assignment, build, and QA.

This skill orchestrates the host agent's available deck tools. Prefer an editable source format for professional deliverables, commonly PPTX for business decks. Use template-preserving presentation tools when a source deck is supplied, use Canva or another design platform when requested or clearly best for the user's workflow, and use browser, file, screenshot, research, and image-generation tools when they are available and relevant.

## Non-Negotiables

- Use user confirmation at key stage gates before irreversible or high-judgment moves. If the user explicitly grants autonomy, batch nearby checkpoints while still recording decisions.
- Begin in plan mode before creating files, researching, choosing style, or building slides.
- Keep enough planning artifacts as markdown before final deck generation so sources, structure, style, asset choices, and QA remain inspectable.
- Inspect rendered outputs before showing them for approval; fix obvious visual defects first.
- Use exact source material for facts, names, dates, quotes, claims, and metrics.
- Never invent missing evidence, charts, logos, screenshots, or user-provided brand facts.
- Treat logos, wordmarks, and recurring identity marks as protected brand assets. Use user-provided or user-approved asset files; do not redraw or procedurally recreate them as approximate shapes unless the user explicitly approves that construction.
- Treat production font choice as a brand decision. Document the intended typography roles and any fallback before building; do not silently replace an approved type direction with generic defaults.
- Preserve image aspect ratios. Never stretch an image horizontally or vertically to fill a frame.
- Do not rely on automatic text shrinking as the main fix for crowded slides; revise copy, hierarchy, or layout first.
- Each slide must have one clear topic, one role in the story, and a logical connection to adjacent slides.
- Each slide must have an obvious title that states the point, not a vague label.
- Assign images systematically with an asset manifest before building slides.
- Review the deck as a viewed sequence before building; text-led, image-led, diagram-led, data-led, and proof-led moments should feel intentional.
- Generate or download images only when the deck structure says why that image is needed.
- Do not use generated images as factual proof of real products, teams, customers, facilities, events, metrics, or claims unless explicitly grounded in source material.
- Prefer an editable final source format unless the user only needs a static export; use PPTX as the common business-deck default, not as a universal requirement.

## Design Judgment Rules

Apply these rules throughout style exploration and deck production. They are judgment rules, not fixed templates.

- Treat style-reference comps as real slide layout tests, not moodboards. A useful comp proves whether typography, spacing, image crops, captions, card interiors, diagrams, charts, and other proof objects can actually work together on a slide.
- Establish a spacing system for each visual direction. Outer margins, card padding, gaps between objects, caption placement, title spacing, and proof-object breathing room should feel intentional and consistent across comps and slides.
- Account for font behavior. Serif faces, CJK typefaces, display titles, and dense labels can wrap, feel heavier, shift baselines, or overflow differently than expected. Adjust hierarchy, line breaks, and copy length to protect readability and elegance.
- Separate typography direction from production fonts. A style may call for editorial, technical, playful, or restrained typography, but the build needs approved font roles, available local fonts, and honest fallback notes before final production.
- Keep on-slide text economical. If a card, chart, or diagram needs cramped copy, simplify the visible phrase and move nuance into speaker notes, research notes, or supporting markdown instead of shrinking text until the layout becomes fragile.
- Treat screenshots and photos as proof objects. Choose cover, contain, or a designed frame before placing them; preserve aspect ratio, crop deliberately, keep important content visible, and align captions to the image or card system. Captions should not float arbitrarily, sit over important visual content, or create blank holding areas.
- Treat visuals as narrative tools, not only evidence. A visual may serve as proof, mood, metaphor, category context, product texture, or emotional pacing. Text-only slides are valid when intentional; they should not be the default for every conceptual slide.
- Use local multimodal material creatively before searching or generating: inspect images, videos, PDFs, screenshots, logos, prior decks, and still frames for motifs, crops, textures, rooms, people, workflows, product details, and category cues that can become slide anchors.
- Distinguish official brand assets from mockups, generated visuals, screenshots, and decorative motifs. A generated brand scene or mockup can support mood, but it should not become the source of truth for a logo, wordmark, or identity system unless approved.
- Permit generated images when local material is insufficient and the approved style direction is clear. Generated images are appropriate for atmosphere, metaphor, category framing, abstract concepts, and style-consistent continuity; keep their role distinct from factual evidence.
- Preserve visible iterations when exploring multiple directions. Save prior comps or rendered slide previews in an archive folder with a short index so the user can compare earlier directions later.
- Treat user critique as a design-system signal when appropriate. Feedback about padding, overflow, captions, hierarchy, image crop, or awkward empty space should update the style rules before more slides are generated, not just patch one local object.

## Visual QA Before Approval

Before asking the user to approve style comps or final slides, render or preview the output and inspect it visually. Fix obvious problems first:

- text overlap, clipping, overflow, or fragile wrapping
- incorrect, recreated, distorted, or inconsistent logo/wordmark usage
- typography that ignores the approved direction or silently falls back to unrelated fonts
- distorted or stretched images
- inconsistent padding, uneven margins, cramped cards, or arbitrary gaps
- captions sitting on top of images or disconnected from their proof object
- unclear hierarchy between title, body, proof object, caption, and source
- awkward empty space that looks accidental rather than designed
- screenshots or photos cropped in a way that hides the important evidence
- chart, table, or diagram labels that cannot be read at presentation size

Record the QA pass in the relevant style, build, or QA notes. File-open checks, package checks, and media-embedded checks are useful but do not replace rendered visual inspection. If the render reveals that the style direction is not practical, revise the style rules before asking for approval.

## Adaptive Stage-Gated Workflow

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

Inspect visual material as visual material, not only as evidence. For images, videos, PDFs, screenshots, logos, and prior decks, note usable motifs, potential crops, textures, people, rooms, workflows, product details, brand cues, and moments that could become image-led anchors or generated-image references.

Record any user-specific source constraints without turning them into universal rules: approved asset folders, rejected assets, forbidden phrases, required chapters, source decks to preserve, brand rules, logo/wordmark files, font direction, or content exclusions.

Write `01-material-audit.md` with:

- available sources and assets
- missing information
- project-specific source constraints and exclusions
- approved brand identity assets and unresolved logo or font questions
- likely deck audience and purpose
- likely visual material roles: proof, mood, metaphor, texture, generated-reference, or unused
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
- asset-to-slide candidates and likely visual roles, even before the final slide structure is locked

Ask the user to approve the material base before recommending visual styles.

### 4. Visual Style Interview

Read `references/style-systems.md`. Recommend a small, focused set of style territories that fit the topic, audience, evidence density, and available assets. Present the recommendation as an interview-style prompt with:

- a short explanation of why each style fits
- color, layout, imagery, and chart implications
- a free-form option for the user to describe another direction

Pause here until the user chooses, modifies, or explicitly delegates the direction decision.

### 5. Style Reference Images

After style approval, create a small set of style reference images or comps. These are not the final deck and not HTML slides. They are real layout tests showing whether the visual system can support actual slide content: title hierarchy, proof objects, card interiors, screenshots, photos, captions, charts, diagrams, and source notes.

Write `03-style-direction.md` with:

- selected style territory
- palette logic and type direction
- practical spacing rules for margins, gaps, cards, captions, title areas, and proof objects
- typography behavior notes, including wrap risk, visual weight, and hierarchy adjustments
- production typography decisions: font roles, availability, and fallback policy
- text economy rules for cards, diagrams, long titles, and speaker-note overflow
- brand identity rules for official logos, wordmarks, marks, headers, chapter dividers, and mockups
- image and caption rules for screenshots, photos, crops, cards, and blank space
- image fit rules for cover, contain, and designed-frame behavior
- text fit rules for shortening visible copy before resizing
- visual rhythm principles for when the deck should become image-led, text-led, diagram-led, data-led, proof-led, or quiet
- generated-image boundaries, including when generated visuals are allowed and how they will be kept separate from proof
- reference-image prompts or source screenshots
- rendered-output QA notes and fixes made before presentation
- what the user approved or rejected
- rules for applying the style consistently

Archive each visible style iteration in `archive/style-iterations/` with a short `index.md` entry describing what changed and why. Do not overwrite earlier visual directions unless the user explicitly asks to discard them.

Ask the user to approve one direction before writing the deck structure.

### 6. Slide Structure Markdown

Before writing `04-slide-structure.md`, confirm that the selected style direction contains both mood rules and practical layout rules. It should explain how the deck will handle long text, screenshots, captions, cards, diagrams, charts, tables, and other proof objects. If those rules are missing or weak, revise `03-style-direction.md` and ask for approval first.

Write `04-slide-structure.md` before generating slides. Follow `references/workflow-artifacts.md`.

For each slide, specify:

- slide number and topic
- claim/title
- narrative role
- composition mode: image-led, text-led, diagram-led, data-led, split image/text, full-bleed image with restrained text, proof-led, mostly negative space, or another mode that fits the story
- body text hierarchy
- proof object: chart, image, table, quote, diagram, comparison, timeline, big-number callout, or another support type that fits the claim
- exact source references for factual claims
- image requirements and asset IDs from `asset-manifest.md`
- visual role for each asset: proof, mood, metaphor, texture, generated, none, or another useful narrative role
- image fit behavior for each visual: cover, contain, designed frame, none, or another aspect-ratio-safe treatment
- brand identity requirements for slides that use logos, wordmarks, recurring marks, or brand typography
- text fit risks and what will move to speaker notes if needed
- layout notes from the chosen style

Ask the user to approve or revise the structure. Do not build slides before approval unless the user has explicitly granted autonomy for this stage.

### 7. Visual Rhythm And Image Assignment Pass

Before building, review the approved slide structure as thumbnails-in-your-head or rendered planning thumbnails if available. Describe the role of each slide in the sequence using the common composition modes or a better label if the story calls for one.

Judge the rhythm without quotas. Ask whether the audience will experience enough visual variety, emotional pacing, and visual proof for the story. If too many neighboring slides feel text-forward or card-heavy, consider a stronger local image crop, a dominant image treatment, a simpler text hierarchy, or a generated visual that follows the approved style direction. If a slide has no image, record why that restraint is intentional.

Write or update `assets/asset-manifest.md` so every visual asset has:

- `asset_id`
- source path or URL
- license/provenance note when available
- quality notes
- intended slide(s)
- crop/layout role
- fit behavior: cover, contain, designed frame, undecided, or another aspect-ratio-safe treatment
- narrative role: proof, mood, metaphor, texture, category context, generated-reference, generated-final, or another useful role
- brand role: official identity asset, approved mockup, generated mood visual, or not applicable
- fallback plan if the asset fails QA

For slides with multiple images, define grid rules and image hierarchy. Avoid decorative images that do not prove, clarify, pace, or emotionally frame the slide topic. If using generated imagery, record the prompt or generation source and keep it labeled internally so it cannot be confused with real-world proof or official brand identity.

### 8. Deck Build

Choose output format using `references/tooling-and-output.md`.
Before producing or revising slides, read `references/production-quality-gates.md` and apply its source constraint, image placement, text placement, and handoff checks.

Default to an editable source format through the best available presentation toolchain. For most business decks this will be PPTX, but choose Canva, HTML, PDF-plus-source, or another format when the user request, source material, or distribution workflow makes it a better fit. If the user requested a source/template deck, route to template-following and preserve the template structure. If Canva or another design platform is requested, generate candidates and ask the user before creating the final deck.

Before building, confirm the production components that affect brand identity: which logo/wordmark files are approved, where recurring marks should appear, which typography roles are intended, which fonts are available, and what fallback should be disclosed if a font is missing.

Build only after the material, style, structure, and image assignment decisions are approved or the user has explicitly granted autonomy to continue.

### 9. QA And Iteration

Render the deck to preview images or a contact sheet. Check:

- story flow and slide topic uniqueness
- source constraints, rejected assets, and forbidden content
- logo, wordmark, recurring mark, and brand-asset consistency
- factual accuracy and source coverage
- title clarity
- deck-level visual rhythm and thumbnail balance
- whether the sequence feels too text-heavy, visually monotonous, or card-heavy
- whether image-led moments are missing for long stretches or clustered awkwardly
- visual hierarchy and contrast
- text overflow and spacing
- chart readability
- image quality, crop, aspect ratio preservation, and correct slide assignment
- whether proof images are large enough to be understood
- whether atmospheric, metaphorical, or generated visuals clarify the story instead of merely decorating it
- whether text fits naturally without fragile shrinking, clipping, or overflow
- whether title, chapter, brand-system, and technical text follow the approved typography roles or documented fallbacks
- consistency with the approved style direction
- whether user critiques have been promoted into updated style rules when they affect the system

Fix issues, rerender affected slides, and ask for final user review.

## Reference Files

- `references/style-systems.md`: reusable visual style territories inspired by modern professional template galleries and presentation design guidance.
- `references/workflow-artifacts.md`: required markdown artifacts and schemas for the slow deck workflow.
- `references/tooling-and-output.md`: when to use PPTX, Canva, HTML, PDF, images, and supporting deck tools.
- `references/production-quality-gates.md`: universal production QA steps and mistakes to avoid for image placement, text fit, source constraints, contact sheets, and final handoff.

## Completion Standard

Finish with the final deck path or link, the approved style name, source/asset notes, and a concise QA summary. If a stage could not be completed, name the missing input or tool clearly and leave the next required question for the user.
