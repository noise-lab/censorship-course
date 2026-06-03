# Slide tooling

Helper scripts for working with the original PowerPoint decks (archived in
`../ppt-archive/`).

- **`read_pptx.py`** — extract per-slide text, titles, and speaker notes from a `.pptx`
  into a deck folder's `_source-extract.md`, and dump every embedded image to
  `images/`. Usage: `python read_pptx.py <deck.pptx> <out-dir>`.
- **`add_notes_to_pptx.py`** — write speaker notes back into a `.pptx`.

Requires `python-pptx` (`pip install python-pptx`). Used during the migration to
Quarto; kept for re-extracting from the archived originals if needed.
