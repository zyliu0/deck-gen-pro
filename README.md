# DeckMason

DeckMason is a PowerPoint builder skill for making product-grade presentation decks with an LLM. It slows the process down so a deck feels like a real project: brief, evidence, style direction, structure, assets, build, and visual QA.

Instead of jumping straight into slides, the skill guides the agent through seven project stages and asks for human approval at the moments where direction, evidence, or design judgment can change the outcome.

> [!NOTE]
> This is a platform-neutral Agent Skill. Install it with the `skills` CLI or copy `skills/deck-mason` into any agent skill directory that supports `SKILL.md`.

## Features

- Starts every deck project in plan mode before execution
- Audits local source material before researching
- Collects missing facts, images, screenshots, and generated creative assets only when needed
- Recommends visual directions from reusable professional style territories
- Creates style references before deck production
- Reviews visual rhythm so image-led, text-led, diagram-led, data-led, and proof-led moments feel intentional
- Distinguishes proof, mood, metaphor, texture, and generated visuals
- Adds production gates for source constraints, image aspect ratio, text fit, contact sheets, and final file checks
- Preserves visible style iterations for later comparison
- Writes a slide-by-slide structure markdown file before building
- Tracks every visual through an asset manifest
- Chooses an editable source format by default, with PPTX as the common business-deck output
- Keeps QA notes for story flow, factual accuracy, layout, chart readability, and image assignment

## Installation

Install directly from GitHub:

```bash
npx skills add https://github.com/zyliu0/deck-mason
```

Install from the direct skill path:

```bash
npx skills add https://github.com/zyliu0/deck-mason/tree/main/skills/deck-mason
```

Install non-interactively for a specific agent:

```bash
npx skills add https://github.com/zyliu0/deck-mason --skill deck-mason --agent universal -y
```

Install globally:

```bash
npx skills add https://github.com/zyliu0/deck-mason --skill deck-mason --agent universal --global -y
```

List the skills exposed by this repository:

```bash
npx skills add https://github.com/zyliu0/deck-mason --list
```

## Usage

Ask your coding agent to use the skill:

```text
Use deck-mason to create a board update deck for our Q2 operating review.
```

The first response should not be slides. It should be a plan-mode brief that restates the goal, names the staged workflow, identifies what the agent needs to inspect first, and asks for approval before creating files, researching, generating references, or building slides.

## How It Works

DeckMason keeps the LLM in project-builder mode. The seven stages create enough friction to protect quality without turning the workflow into a rigid template.

| Phase | What Happens | User Checkpoint |
|---|---|---|
| 1. Brief | Restate the goal, audience, constraints, output format, and first move. | Approve the project path before production begins. |
| 2. Material | Audit local sources and gather missing facts or assets only when needed. | Confirm the evidence and asset base. |
| 3. Direction | Choose a visual direction and test it with real slide-like comps. | Approve or revise the style system. |
| 4. Structure | Write the slide-by-slide markdown plan with story, claims, proof, and rhythm. | Approve the flow before production. |
| 5. Assets | Assign visuals by role, crop logic, provenance, and fallback plan. | Confirm images are purposeful and usable. |
| 6. Build | Produce the editable deck in the best format for the request, usually PPTX for business use. | Review rendered previews. |
| 7. QA | Inspect the contact sheet and individual slides for content, layout, image, and text issues. | Approve the product-grade deck or request revisions. |

## Workspace Artifacts

The helper script creates the markdown files used to keep the process inspectable:

```bash
python3 skills/deck-mason/scripts/init_deck_workspace.py "AI platform investor deck" --root outputs
```

Generated workspace:

```text
00-plan-mode-brief.md
01-material-audit.md
02-research-notes.md
03-style-direction.md
04-slide-structure.md
05-build-notes.md
06-qa-notes.md
assets/asset-manifest.md
assets/source/
assets/generated/
archive/style-iterations/index.md
previews/
qa/
output/
```

## Included Style Territories

DeckMason includes a starter library of style territories for the visual interview stage. They are prompts for judgment, not fixed templates:

| Style | Best for |
|---|---|
| Editorial Strategy | Strategy narratives, market maps, thought leadership |
| Founder Pitch Minimal | Startup fundraising and product vision |
| Premium Brand Monochrome | Luxury, fashion, portfolio, architecture |
| Data Room Executive | Finance, board, analytics, market sizing |
| Product System Blueprint | SaaS, AI, developer tools, platform decks |
| Research Lab | Academic, science, policy, UX research |
| Creative Campaign Pop | Marketing, creator, entertainment, social launches |
| Consultancy Clarity | Proposals, transformation, recommendations |
| Immersive Place Story | Travel, real estate, hospitality, venues |
| Workshop Canvas | Training, facilitation, design sprints |

## Repository Layout

```text
deck-mason/
├── README.md
└── skills/
    └── deck-mason/
        ├── SKILL.md
        ├── references/
        │   ├── production-quality-gates.md
        │   ├── style-systems.md
        │   ├── tooling-and-output.md
        │   └── workflow-artifacts.md
        └── scripts/
            └── init_deck_workspace.py
```

The installable skill is `skills/deck-mason/`.

## Verification

Check the helper script:

```bash
python3 -m py_compile skills/deck-mason/scripts/init_deck_workspace.py
```

Create a sample workspace:

```bash
python3 skills/deck-mason/scripts/init_deck_workspace.py "sample deck" --root /tmp/deck-mason-test
```

Check that the `skills` CLI can discover the package:

```bash
npx skills add . --list
```

## Notes

Generated deck workspaces are ignored through `outputs/`. Keep private source files, research downloads, generated images, and client deck outputs out of the public repository unless they are intentionally shareable.
