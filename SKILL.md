---
name: deck-gen-pro
description: Professional staged deck-making workflow for creating, planning, or upgrading presentations, slide decks, pitch decks, PowerPoint/PPTX decks, Canva presentations, or HTML slide prototypes. Use when the user asks for a deck or slides and wants high-quality research, narrative structure, visual style selection, reference images, image sourcing or generation, and step-by-step approval instead of one-shot slide generation.
---

# Deck Gen Pro

## Overview

Use this skill to make professional decks slowly and deliberately. Do not start by generating slides. Move through gated stages: material audit, research and asset gathering, style interview, style references, slide-structure markdown, final deck production, and QA.

This skill orchestrates other deck tools. Use the installed `Presentations` skill for editable artifact-tool PPTX builds, `pptx` when a `.pptx` file is touched, Canva skills when the user explicitly wants Canva, and browser/image tools for research, screenshots, downloaded source assets, or generated reference imagery.

## Non-Negotiables

- Ask for user confirmation at every stage gate before moving to the next stage.
- Keep all planning artifacts as markdown before final deck generation.
- Use exact source material for facts, names, dates, quotes, claims, and metrics.
- Never invent missing evidence, charts, logos, screenshots, or user-provided brand facts.
- Each slide must have one clear topic, one role in the story, and a logical connection to adjacent slides.
- Each slide must have an obvious title that states the point, not a vague label.
- Assign images systematically with an asset manifest before building slides.
- Generate or download images only when the deck structure says why that image is needed.
- Prefer editable PPTX via artifact-tool for final professional deliverables unless the user requests Canva, HTML, PDF, or another format.

## Stage-Gated Workflow

### 0. Create Working Folder

Create a task folder and starter artifacts with:

```bash
python3 <skill-dir>/scripts/init_deck_workspace.py "<deck topic or task slug>" --root outputs
```

Use the generated folder for all notes, research, assets, style references, structure markdown, previews, and QA.

### 1. Material Audit

Inspect the working environment before researching. Look for user-provided files, existing notes, brand assets, previous decks, source documents, datasets, screenshots, images, and URLs.

Write `01-material-audit.md` with:

- available sources and assets
- missing information
- likely deck audience and purpose
- risks such as weak evidence, no visuals, unclear brand, or missing metrics
- decision: `enough-material: yes/no/partial`

If material is enough, ask the user to confirm the interpretation before style work. If not enough, propose the research or creative asset plan first.

### 2. Research And Asset Collection

Use this stage only when the audit is `no` or `partial`, or when the user asks for current facts, source links, real product/place/person imagery, charts, or creative art direction.

Write `02-research-notes.md` and `assets/asset-manifest.md`. Capture:

- source links, dates, and reliability notes
- facts and metrics with provenance
- downloaded images/screenshots and allowed usage constraints when known
- generated image prompts and outputs, if creative imagery is appropriate
- asset-to-slide candidates, even before the final slide structure is locked

Ask the user to approve the material base before recommending visual styles.

### 3. Visual Style Interview

Read `references/style-systems.md`. Recommend 2-3 style systems that fit the topic, audience, evidence density, and available assets. Present the recommendation as an interview-style prompt with:

- a short explanation of why each style fits
- color, layout, imagery, and chart implications
- a free-form option for the user to describe another direction

Do not proceed until the user chooses or modifies a direction.

### 4. Style Reference Images

After style approval, create 2-4 style reference images or comps. These are not the final deck and not HTML slides. They are visual direction checks showing layout rhythm, palette, typography mood, image treatment, and chart/diagram style.

Write `03-style-direction.md` with:

- selected style system
- exact palette and type direction
- reference-image prompts or source screenshots
- what the user approved or rejected
- rules for applying the style consistently

Ask the user to approve one direction before writing the deck structure.

### 5. Slide Structure Markdown

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

### 6. Image Assignment Pass

Write or update `assets/asset-manifest.md` so every visual asset has:

- `asset_id`
- source path or URL
- license/provenance note when available
- quality notes
- intended slide(s)
- crop/layout role
- fallback plan if the asset fails QA

For slides with multiple images, define grid rules and image hierarchy. Avoid decorative images that do not prove or clarify the slide topic.

### 7. Deck Build

Choose output format using `references/tooling-and-output.md`.

Default to editable PPTX through the installed `Presentations` skill. Use generated slide code or artifact-tool presentation JSX as appropriate for the current environment. If the user requested a source/template deck, route to template-following and preserve the template structure. If Canva is requested, use Canva skills and generate candidates before creating the final deck.

Build only after the material, style, structure, and image assignment stages are approved.

### 8. QA And Iteration

Render the deck to preview images or a contact sheet. Check:

- story flow and slide topic uniqueness
- factual accuracy and source coverage
- title clarity
- visual hierarchy and contrast
- text overflow and spacing
- chart readability
- image quality, crop, and correct slide assignment
- consistency with the approved style direction

Fix issues, rerender affected slides, and ask for final user review.

## Reference Files

- `references/style-systems.md`: 10 reusable visual style systems inspired by modern professional template galleries and presentation design guidance.
- `references/workflow-artifacts.md`: required markdown artifacts and schemas for the slow deck workflow.
- `references/tooling-and-output.md`: when to use PPTX, Canva, HTML, PDF, images, and installed deck skills.

## Completion Standard

Finish with the final deck path or link, the approved style name, source/asset notes, and a concise QA summary. If a stage could not be completed, name the missing input or tool clearly and leave the next required question for the user.
