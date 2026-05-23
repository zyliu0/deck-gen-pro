# Tooling And Output

Use this file to decide the final production format and supporting tools.

## Default Recommendation

Default to editable PPTX when the user asks for a professional deck, pitch deck, board deck, sales deck, strategy deck, report deck, or presentation. A final PPTX is the most useful default because business users can edit, share, present, and reuse it.

Use the installed `Presentations` skill for high-polish artifact-tool presentation JSX builds. If any `.pptx` file is read, edited, created, converted, or used as a template, also use the installed `pptx` skill.

## Format Router

| User need | Best output | Notes |
|---|---|---|
| Editable business deck | PPTX | Use artifact-tool through `Presentations`; render previews before final. |
| Existing template/source deck | PPTX clone/edit | Preserve typography, layout, and brand chrome; do not rebuild from blank unless required. |
| Branded Canva workflow | Canva | Use Canva skills; create candidates and ask user before final design. |
| Web-native interactive slides | HTML/React | Use only when user wants browser delivery, animation, scrolling, or interactive elements. |
| Static review artifact | PDF | Export after editable source exists unless user only needs PDF. |
| Style exploration only | Images/comps | Generate reference images or screenshots; do not treat them as final deck. |
| Social/carousel adaptation | PNG/PDF plus source | Build after deck story is approved; adapt aspect ratio intentionally. |

## HTML Guidance

Do not use HTML as the default final deck format. HTML is useful for:

- interactive prototypes
- browser-based storytelling
- animated or responsive experiences
- quick style reference comps
- image-heavy web presentation previews

If the final deliverable is PPTX, HTML may still be useful for temporary visual exploration, but the approved deck must be rebuilt or exported in the requested final format.

## Image Sourcing

Use real images when the audience needs to inspect a real product, place, person, venue, brand, interface, chart, or screenshot. Download or screenshot source assets only when permitted and record provenance in `assets/asset-manifest.md`.

Use generated images when:

- the topic is conceptual, speculative, creative, or fictional
- no real visual exists
- the user asks for a creative direction
- the visual is a mood/reference comp, not factual evidence

Never use generated imagery to imply a real event, person, product state, venue, or metric.

## Chart And Data Guidance

Use charts when comparisons, change over time, mix, ranking, contribution, funnel movement, or relationships matter. Use big text when the main point is a single number or takeaway. Use tables only when precise lookup is more important than pattern recognition.

Every chart slide needs:

- exact source
- unit
- time period
- comparison basis
- annotation that explains the point
- readable labels at presentation size

## Installed Skill Coordination

- `Presentations`: final high-polish editable PPTX build, previews, contact sheets, QA.
- `pptx`: any `.pptx` read/edit/create/convert workflow.
- `canva-branded-presentation`: Canva-specific generation with brand kits and candidate selection.
- `imagegen`: generated style references or creative imagery.
- Browser/web tools: current research, source verification, screenshots, image sourcing.

Load only the skill needed for the current stage. Keep `deck-gen-pro` as the process controller and the other skill as the production tool.
