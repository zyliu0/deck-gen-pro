# Tooling And Output

Use this file to decide the final production format and supporting tools.

## Output Choice

Start by choosing the editable source format that best matches the user's workflow. PPTX is the common business-deck choice because many teams can edit, share, present, and reuse it, but it is a default preference rather than a hard requirement.

Use the host environment's best presentation workflow for high-polish editable builds. If a `.pptx` file is read, edited, created, converted, or used as a template, use the most reliable available PPTX reader/editor and preserve editability whenever possible.

## Format Router

| User need | Likely output | Notes |
|---|---|---|
| Editable business deck | PPTX | Use the best available PPTX-capable builder; render previews before final. |
| Existing template/source deck | PPTX clone/edit | Preserve typography, layout, and brand chrome; do not rebuild from blank unless required. |
| Branded Canva workflow | Canva | Use Canva or an equivalent design-platform connector; create candidates and ask user before final design. |
| Web-native interactive slides | HTML/React | Use only when user wants browser delivery, animation, scrolling, or interactive elements. |
| Static review artifact | PDF | Export after editable source exists unless user only needs PDF. |
| Style exploration only | Images/comps | Generate reference images or screenshots; do not treat them as final deck. |
| Social/carousel adaptation | PNG/PDF plus source | Build after deck story is approved; adapt aspect ratio intentionally. |

## HTML Guidance

Avoid HTML as the final deck format unless the user wants a web-native experience or HTML clearly fits the distribution context. HTML is useful for:

- interactive prototypes
- browser-based storytelling
- animated or responsive experiences
- quick style reference comps
- image-heavy web presentation previews

If the final deliverable is PPTX or another editable deck format, HTML may still be useful for temporary visual exploration, but the approved deck should be rebuilt or exported in the requested final format.

## Image Sourcing

Use real images when the audience needs to inspect a real product, place, person, venue, brand, interface, chart, or screenshot. Download or screenshot source assets only when permitted and record provenance in `assets/asset-manifest.md`.

Preserve image aspect ratio in every production format. If a visual needs to fill a frame, crop it deliberately. If the whole asset must remain visible, contain it and make the surrounding space feel designed. If neither is elegant, design a frame or choose another composition. Do not stretch images to satisfy a layout.

Treat images by narrative role:

- Proof: source-backed visuals that support factual claims.
- Mood: visuals that establish brand world, category, or emotional tone.
- Metaphor: visuals that help a conceptual slide become memorable.
- Texture: subtle visual material that adds depth without distracting.
- Generated: style-consistent visuals created when local assets are insufficient.

Use local project visuals first when they are semantically and visually useful. Inspect images, video stills, PDFs, screenshots, and prior decks for crops, details, rooms, workflows, people, materials, and style traits that can become slide anchors or generation references.

Use generated images when:

- the topic is conceptual, speculative, creative, or fictional
- no real visual exists
- the user asks for a creative direction
- the visual is a mood/reference comp, not factual evidence
- a slide needs atmosphere, metaphor, category framing, or style continuity and local assets are insufficient

Never use generated imagery to imply a real event, person, product state, venue, or metric.

## Text Fit Guidance

Visible slide text should fit by design, not by fragile shrinking. Shorten copy, split hierarchy, move nuance to notes, or change the composition when text clips, touches edges, overlaps other content, or becomes unreadable after rendering.

## Chart And Data Guidance

Use charts when comparisons, change over time, mix, ranking, contribution, funnel movement, or relationships matter. Use big text when the main point is a single number or takeaway. Use tables only when precise lookup is more important than pattern recognition.

Every chart slide needs:

- exact source
- unit
- time period
- comparison basis
- annotation that explains the point
- readable labels at presentation size

## Tool Coordination

- Presentation/PPTX tools: final high-polish editable deck build, previews, contact sheets, QA.
- Template or PPTX parsers/editors: any `.pptx` read/edit/create/convert workflow.
- Canva or design-platform connectors: brand-kit workflows and candidate generation when requested.
- Image-generation tools: generated style references or creative imagery.
- Browser/web tools: current research, source verification, screenshots, image sourcing.

Load only the tool or supporting skill needed for the current stage. Keep `deck-mason` as the process controller and use other tools as production tools.
