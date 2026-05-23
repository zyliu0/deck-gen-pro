# Deck Gen Pro

Deck Gen Pro is an agent skill for creating professional presentation decks through a slow, staged workflow. It is built for moments where the story, evidence, visual direction, and image choices matter too much for one-shot slide generation.

The skill starts in plan mode, confirms each stage with the user, and only builds slides after the material base, style direction, slide structure, and asset assignments are approved.

> [!NOTE]
> This is a platform-neutral Agent Skill. Install it with the `skills` CLI or copy `skills/deck-gen-pro` into any agent skill directory that supports `SKILL.md`.

## Features

- Starts every deck project in plan mode before execution
- Audits local source material before researching
- Collects missing facts, images, screenshots, and generated creative assets only when needed
- Recommends visual styles from 10 professional deck systems
- Creates style references before deck production
- Preserves visible style iterations for later comparison
- Writes a slide-by-slide structure markdown file before building
- Tracks every visual through an asset manifest
- Defaults to editable PPTX while supporting Canva, HTML, PDF, and image comps when requested
- Keeps QA notes for story flow, factual accuracy, layout, chart readability, and image assignment

## Installation

Install directly from GitHub:

```bash
npx skills add https://github.com/zyliu0/deck-gen-pro
```

Install from the direct skill path:

```bash
npx skills add https://github.com/zyliu0/deck-gen-pro/tree/main/skills/deck-gen-pro
```

Install non-interactively for a specific agent:

```bash
npx skills add https://github.com/zyliu0/deck-gen-pro --skill deck-gen-pro --agent universal -y
```

Install globally:

```bash
npx skills add https://github.com/zyliu0/deck-gen-pro --skill deck-gen-pro --agent universal --global -y
```

List the skills exposed by this repository:

```bash
npx skills add https://github.com/zyliu0/deck-gen-pro --list
```

## Usage

Ask your coding agent to use the skill:

```text
Use deck-gen-pro to create a board update deck for our Q2 operating review.
```

The first response should not be slides. It should be a plan-mode brief that restates the goal, names the staged workflow, identifies what the agent needs to inspect first, and asks for approval before creating files, researching, generating references, or building slides.

## How It Works

Deck Gen Pro keeps the process simple: understand the deck, choose a direction, outline the story, then build.

| Phase | What Happens | User Checkpoint |
|---|---|---|
| 1. Plan | Restate the goal, audience, output format, and first step. | Approve the workflow before work begins. |
| 2. Gather | Audit existing material, then research or collect assets only if needed. | Confirm the source material is enough. |
| 3. Style | Recommend a visual direction and create a few reference images or comps. | Choose or revise the style. |
| 4. Structure | Write the slide-by-slide markdown plan, including titles, proof, sources, and visuals. | Approve the slide flow before production. |
| 5. Build | Create the deck, render previews, QA it, and fix issues. | Review the final deck and QA summary. |

## Workspace Artifacts

The helper script creates the markdown files used to keep the process inspectable:

```bash
python3 skills/deck-gen-pro/scripts/init_deck_workspace.py "AI platform investor deck" --root outputs
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

## Included Style Systems

Deck Gen Pro includes 10 style systems for the visual interview stage:

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
deck-gen-pro/
├── README.md
└── skills/
    └── deck-gen-pro/
        ├── SKILL.md
        ├── references/
        │   ├── style-systems.md
        │   ├── tooling-and-output.md
        │   └── workflow-artifacts.md
        └── scripts/
            └── init_deck_workspace.py
```

The installable skill is `skills/deck-gen-pro/`.

## Verification

Check the helper script:

```bash
python3 -m py_compile skills/deck-gen-pro/scripts/init_deck_workspace.py
```

Create a sample workspace:

```bash
python3 skills/deck-gen-pro/scripts/init_deck_workspace.py "sample deck" --root /tmp/deck-gen-pro-test
```

Check that the `skills` CLI can discover the package:

```bash
npx skills add . --list
```

## Notes

Generated deck workspaces are ignored through `outputs/`. Keep private source files, research downloads, generated images, and client deck outputs out of the public repository unless they are intentionally shareable.
