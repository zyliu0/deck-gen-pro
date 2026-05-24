# Production Quality Gates

Use this reference before building, revising, or handing off a deck. These are judgment rules and QA steps, not fixed layouts, fixed dimensions, fixed image counts, or project-specific copy.

## Core Principles

- Never stretch an image. Preserve the source aspect ratio. Crop, contain, or redesign the frame instead.
- Do not use automatic text shrinking as the main solution. Shorten the visible text, adjust hierarchy, or change the layout so text fits naturally.
- Record project-specific constraints from the user, such as approved asset folders, rejected assets, forbidden phrases, required chapters, brand rules, or source decks. Keep those constraints in the project artifacts; do not bake them into the universal skill.
- Package checks are not visual QA. A deck can open, contain media, and pass archive validation while still having distorted images, overflowing text, awkward crops, or unreadable captions.

## Source Constraint Check

Before production, confirm the material base:

- approved asset sources are being used
- rejected or outdated assets are excluded
- forbidden phrases, claims, chapters, or imagery are absent
- required chapters, sections, or narrative beats remain present
- factual claims still point to source material

Write these constraints in the material audit, build notes, and QA notes so another agent can inspect them later.

## Image Placement Workflow

Choose the image behavior before placing each visual.

### Cover

Use cover when the image should fill a visual area.

- Preserve aspect ratio.
- Fill the frame by cropping excess edges.
- Crop deliberately so the important subject remains visible.
- Use when a photo, screenshot, room view, product image, material board, or hero image needs a strong filled frame.

QA: the image should look natural. People, rooms, screens, logos, products, circles, packaging, and furniture should not look wider, thinner, taller, or flatter than the source.

### Contain

Use contain when the whole image must remain visible.

- Preserve aspect ratio.
- Fit the entire image inside the available space.
- Accept empty space when needed.
- Make the empty space feel intentional with a frame, surface, alignment system, or caption.
- Use when cropping would remove necessary information, such as a logo lockup, diagram, contact sheet, full interface view, chart, or comparison object.

QA: the complete asset is visible, empty space looks designed, and the image has not been stretched to fill the area.

### Designed Frame

Use a designed frame when neither simple cover nor simple contain is elegant.

- Pair the image with a deliberate surface, caption, border, mat, crop window, or grid.
- Use the frame to resolve awkward aspect ratios, not to hide distortion.
- Reconsider the composition if the frame becomes a blank holding area.

## Text Placement Workflow

For every visible text block:

- Decide whether the text belongs on the slide or in speaker notes/supporting markdown.
- Shorten the visible phrase before resizing it.
- Check whether the container can support the likely wrapped lines.
- Give captions enough room to sit with their image.
- If text touches edges, overlaps, clips, or becomes fragile, revise the content or layout.
- Inspect rendered slides after export; do not assume the authoring view matches the final preview.

## Deck-Level QA Gates

Do not hand off the deck until these gates pass:

- Source constraints: approved sources used, rejected sources excluded, forbidden content absent, required structure preserved.
- Image distortion: every rendered image preserves aspect ratio and important content remains visible.
- Text fit: no clipped titles, overflowing boxes, unreadably small text, captions outside their designed area, or text overlapping visual content.
- Contact sheet: thumbnail review shows intentional rhythm, no repeated awkward crops, no dense text runs, no missing image-led moments where the story needs them.
- Individual slide review: readable-size preview confirms hierarchy, crop quality, caption placement, brand consistency, and chart/table legibility.
- Final file check: the deck opens, media is embedded, slide count is expected, final export path is recorded, and the visual QA actually happened.

## Mistakes To Avoid

- Do not stretch images to make them fill a shape.
- Do not solve poor layout by shrinking text until it becomes unreadable.
- Do not use rejected or outdated assets just because they are easy to find.
- Do not let captions float away from images or collide with image content.
- Do not treat generated mood imagery as factual evidence.
- Do not call a deck finished after only checking that the file opens.
- Do not leave intentional crops undocumented when they affect evidence, product detail, or brand presentation.
