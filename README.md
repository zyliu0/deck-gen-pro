# Deck Gen Pro

Deck Gen Pro is a Codex skill for making professional slide decks slowly, with deliberate approval gates. It is designed for deck work where the story, evidence, visual system, and image choices matter more than getting a pile of slides on the first try.

Instead of generating slides immediately, the skill guides the agent through material audit, research, visual style selection, reference comps, slide-structure planning, image assignment, production, and QA.

## What It Does

Deck Gen Pro turns a deck request into a staged workflow:

1. Audit the local working environment for source material, brand assets, notes, data, images, and prior decks.
2. Research or collect missing source material when the local environment is not enough.
3. Interview the user on visual direction using curated professional style systems.
4. Generate or collect style reference images before building slides.
5. Write a slide-structure markdown file that maps every slide topic, title, proof object, source, and image.
6. Assign images through an asset manifest so visuals are intentional and traceable.
7. Build the deck only after the material, style, structure, and image plan are approved.
8. Render and QA the output before calling it finished.

The default final deliverable is an editable PowerPoint deck, but the skill can route to Canva, HTML, PDF, image comps, or other formats when the user asks for them.

## Why This Exists

Most AI deck generation workflows fail in the same way: they start making slides before they understand the topic. Deck Gen Pro treats slide generation as the last step, not the first one.

The skill is built around three principles:

- Story before slides.
- Evidence before claims.
- Style before production.

That makes it useful for investor decks, board updates, strategy decks, sales decks, research presentations, creative pitches, product narratives, and image-led decks where asset quality matters.

## Project Structure

```text
deck-gen-pro/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── style-systems.md
│   ├── tooling-and-output.md
│   └── workflow-artifacts.md
└── scripts/
    └── init_deck_workspace.py
```

## Files

| File | Purpose |
|---|---|
| `SKILL.md` | Main skill workflow and trigger description. |
| `agents/openai.yaml` | UI metadata for Codex skill lists and default prompt insertion. |
| `references/style-systems.md` | Ten visual style systems for the style interview stage. |
| `references/workflow-artifacts.md` | Markdown schemas for material audit, research notes, style direction, slide structure, asset manifest, build notes, and QA notes. |
| `references/tooling-and-output.md` | Output-format router for PPTX, Canva, HTML, PDF, image comps, and supporting tools. |
| `scripts/init_deck_workspace.py` | Helper that creates a staged deck workspace with all required markdown artifacts. |

## Style Systems

The skill includes ten reusable visual directions:

1. Editorial Strategy
2. Founder Pitch Minimal
3. Premium Brand Monochrome
4. Data Room Executive
5. Product System Blueprint
6. Research Lab
7. Creative Campaign Pop
8. Consultancy Clarity
9. Immersive Place Story
10. Workshop Canvas

These are not rigid templates. They are decision aids for choosing layout rhythm, palette, typography, chart treatment, and image direction before production starts.

## Install

Place this folder in a Codex-readable skills directory, such as:

```bash
~/.codex/skills/deck-gen-pro
```

or:

```bash
~/.agents/skills/deck-gen-pro
```

Then restart or reload Codex so the skill index can pick it up.

## Use

Invoke the skill when asking for a deck:

```text
Use $deck-gen-pro to make an investor deck for my AI workflow product.
```

The skill should not immediately create slides. It should start by auditing available material and asking for confirmation before moving to the next stage.

## Create A Deck Workspace

The helper script creates the markdown files used during the staged process:

```bash
python3 scripts/init_deck_workspace.py "AI platform investor deck" --root outputs
```

It creates a timestamped folder containing:

```text
01-material-audit.md
02-research-notes.md
03-style-direction.md
04-slide-structure.md
05-build-notes.md
06-qa-notes.md
assets/asset-manifest.md
assets/source/
assets/generated/
previews/
qa/
output/
```

Use this workspace as the working record for one deck project.

## Workflow Artifacts

The skill depends on explicit planning artifacts:

| Artifact | Role |
|---|---|
| `01-material-audit.md` | Decides whether the available source material is enough. |
| `02-research-notes.md` | Records source-backed facts, links, visual candidates, and open questions. |
| `03-style-direction.md` | Captures the selected visual system and approved reference comps. |
| `04-slide-structure.md` | Defines each slide's topic, claim, proof object, source, layout, and visual assignment. |
| `assets/asset-manifest.md` | Tracks every image, screenshot, chart, logo, generated visual, and fallback. |
| `05-build-notes.md` | Records output format, toolchain, fonts, source mapping, and final path. |
| `06-qa-notes.md` | Records story, factual, visual, and image-assignment QA. |

## Output Guidance

Deck Gen Pro defaults to editable PPTX because most business decks need to be edited, shared, and reused. It routes to other formats when the user asks:

| Need | Output |
|---|---|
| Editable business deck | PPTX |
| Existing template/source deck | PPTX clone/edit |
| Branded Canva workflow | Canva |
| Interactive web-native slides | HTML/React |
| Static review artifact | PDF |
| Style exploration | Images or comps |
| Social/carousel adaptation | PNG/PDF plus source |

## Verify

Run the Python syntax check:

```bash
python3 -m py_compile scripts/init_deck_workspace.py
```

Create a temporary sample workspace:

```bash
python3 scripts/init_deck_workspace.py "sample deck" --root /tmp/deck-gen-pro-test
```

If you have Codex's system skill validator available, validate the skill folder:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

## Public Repo Notes

Generated deck workspaces are ignored by default through `outputs/`. Keep user source files, research downloads, generated images, and private deck outputs out of the public repository unless they are intentionally shareable.

## License

No license has been added yet. Add one before treating this as an open-source project.
