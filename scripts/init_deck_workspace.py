#!/usr/bin/env python3
"""Create a staged workspace for a Deck Gen Pro project."""

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
    parser = argparse.ArgumentParser(description="Create Deck Gen Pro workspace files.")
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
| Asset idea | Source/generation plan | Use case | Risk |
|---|---|---|---|

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
- Palette:
- Typography:
- Layout grammar:
- Chart/diagram style:
- Image treatment:
- Accent rules:

## Reference Images Or Comps
| Ref | Path/URL | What to borrow | What to avoid |
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
1. Context:
2. Tension:
3. Insight:
4. Recommendation:
5. Proof:
6. Close:

## Slide 01: [Topic]

- Topic:
- Claim/title:
- Narrative role:
- Audience takeaway:
- Layout:
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
""",
    )

    write_if_missing(
        workspace / "assets" / "asset-manifest.md",
        """# Asset Manifest

| asset_id | Type | Path/URL | Source/provenance | Quality | Intended slides | Role | Fallback |
|---|---|---|---|---|---|---|---|
""",
    )

    write_if_missing(
        workspace / "05-build-notes.md",
        """# Build Notes

## Output Format

## Toolchain

## Slide Source Mapping

## Fonts And Fallbacks

## Asset Processing Notes

## Known Compromises

## Final Export Path
""",
    )

    write_if_missing(
        workspace / "06-qa-notes.md",
        """# QA Notes

## Preview Or Contact Sheet Paths

## Factual QA

## Visual QA

## Image Assignment QA

## Fixes Made

## Remaining Risks
""",
    )

    print(workspace)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
