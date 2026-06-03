#!/usr/bin/env python3
"""Create a staged workspace for a DeckMason project."""

from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    slug = re.sub(r"-{2,}", "-", slug)
    return slug or "deck-project"


def write_if_missing(path: Path, content: str) -> None:
    if path.exists():
        return
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create DeckMason workspace files.")
    parser.add_argument("topic", help="Deck topic or short project name.")
    parser.add_argument("--root", default="outputs", help="Root directory for generated workspaces.")
    parser.add_argument("--slug", default="", help="Optional explicit workspace slug.")
    args = parser.parse_args()

    slug = slugify(args.slug or args.topic)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    workspace = Path(args.root).expanduser().resolve() / f"{stamp}-{slug}"

    for directory in [
        workspace,
        workspace / "assets",
        workspace / "assets" / "source",
        workspace / "assets" / "generated",
        workspace / "archive",
        workspace / "archive" / "style-iterations",
        workspace / "references",
        workspace / "previews",
        workspace / "qa",
        workspace / "output",
    ]:
        directory.mkdir(parents=True, exist_ok=True)

    write_if_missing(
        workspace / "00-plan-mode-brief.md",
        """# Plan Mode Brief

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
""",
    )

    write_if_missing(
        workspace / "01-material-audit.md",
        """# Material Audit

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

## Brand Identity Assets
- Approved logo, wordmark, or mark assets:
- Generated or mockup brand visuals that are not official identity assets:
- Typography direction:
- Known local font availability:
- Font fallback risks:
- Open logo or font questions:

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
enough-material:
next-stage:
""",
    )

    write_if_missing(
        workspace / "02-research-notes.md",
        """# Research Notes

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
""",
    )

    write_if_missing(
        workspace / "03-style-direction.md",
        """# Style Direction

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
- Production font roles:
- Font availability and fallback policy:
- Layout grammar:
- Chart/diagram style:
- Image treatment:
- Logo, wordmark, and recurring mark treatment:
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
- Brand/title font role:
- Body/UI/technical font role:
- Fallback disclosure:

## Text Economy Rules
- On-slide copy limit principles:
- What moves to speaker notes:
- What moves to supporting markdown:
- When to simplify a card or diagram:

## Image And Caption Rules
- When to use cover:
- When to use contain:
- When to use a designed frame:
- How official brand assets differ from mockups or generated visuals:
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
""",
    )

    write_if_missing(
        workspace / "04-slide-structure.md",
        """# Slide Structure

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

## Slide 01: [Topic]

- Topic:
- Claim/title:
- Narrative role:
- Audience takeaway:
- Layout:
- Composition mode:
- Visual rhythm intent:
- Practical style rules:
  - Long-text handling:
  - Screenshot/caption handling:
  - Card/proof-object handling:
  - Image fit behavior:
  - Text fit risk:
  - Brand/logo/font handling:
- Text hierarchy:
  - Title:
  - Primary copy:
  - Secondary copy:
  - Caption/footer:
- Proof object:
- Source references:
  - 
- Visual assets:
  - 
- Image assignment:
  - Visual role:
  - Fit behavior:
  - Brand role:
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
""",
    )

    write_if_missing(
        workspace / "assets" / "asset-manifest.md",
        """# Asset Manifest

| asset_id | Type | Path/URL | Source/provenance | Quality | Intended slides | Visual role | Fit behavior | Brand role | Fallback |
|---|---|---|---|---|---|---|---|---|---|
""",
    )

    write_if_missing(
        workspace / "05-build-notes.md",
        """# Build Notes

## Output Format

## Toolchain

## Slide Source Mapping

## Source Constraints Applied

## Fonts And Fallbacks

## Brand Identity Asset Usage

## Recurring Logo, Mark, Or Wordmark Handling

## Typography Role Decisions

## Image Placement Decisions

## Text Fit Decisions

## Asset Processing Notes

## Known Compromises

## Final Export Path
""",
    )

    write_if_missing(
        workspace / "06-qa-notes.md",
        """# QA Notes

## Preview Or Contact Sheet Paths

## Source Constraint QA

- Approved sources used:
- Rejected or outdated assets excluded:
- Forbidden content absent:
- Required sections preserved:
- Source deck/template rules followed:

## Brand Identity QA

- Official logo, wordmark, and mark assets used where identity is needed:
- Generated/mockup visuals are not treated as official identity assets:
- Recurring header or chapter marks are consistent:
- Wordmarks are not retyped or rebuilt without approval:
- Typography follows approved roles or documented fallback:
- Title, chapter, and brand-system slides inspected:

## Factual QA

## Deck-Level Visual Balance QA

- Contact sheet reviewed:
- Thumbnail sequence feels intentionally balanced:
- Text-heavy or card-heavy stretches found:
- Image-led moments checked for pacing:
- Proof images large enough to understand:
- Atmospheric/metaphor/generated visuals clarify the story:
- Text-only slides are intentional:

## Visual QA

- Image distortion/aspect-ratio checks:
- Text overlap, overflow, and wrapping checks:
- Spacing, padding, and margin consistency checks:
- Typography behavior checks:
- Font fallback checks:
- Logo, wordmark, and recurring mark checks:
- Image crop and caption relationship checks:

## Final File Check

- Deck opens:
- Media embedded:
- Expected slide count:
- Preview/contact sheet reviewed:
- Visual QA completed after rendering:

## Image Assignment QA

- Visual roles are correctly labeled:
- Generated images are not treated as factual proof:
- Package/file checks are not treated as visual QA:

## User Critique Applied To Style Rules

## Fixes Made

## Remaining Risks
""",
    )

    write_if_missing(
        workspace / "archive" / "style-iterations" / "index.md",
        """# Style Iteration Archive

| Iteration | Date | Path | Summary | User/design signal |
|---|---:|---|---|---|
""",
    )

    print(workspace)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
