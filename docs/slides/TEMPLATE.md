# Lecture Deck Template Spec

Every lecture deck follows this spec. The canonical worked example is
**`01-Intro/01-Overview/`** — read it before authoring a deck. Goal: a
**content-driven rebuild** in Quarto reveal.js (not a slide-for-slide port of the
old pptx).

> **The companion book is the spine.** This course tracks the book at
> **`noise-lab/censorship-book`** (a sibling directory: `../../../censorship-book`,
> a LaTeX book). Decks are organized by **book chapter → section**, and each deck
> aligns to the book's terminology, taxonomy, and ordering. Where a slide and the
> book disagree, defer to the book (or flag the divergence in `coverage-notes.md`).

## Folder layout (chapter → section)

Decks live in **chapter-numbered subtopic folders** with **section-numbered decks**
inside, in **book order** (not teaching order — the syllabus/`agenda.md` carry teaching
order):

```
NN-Chapter/MM-Deck/
  slides.qmd          # the Quarto reveal.js deck (authored)
  coverage-notes.md   # instructor-facing: current-events updates + missing-coverage
  images/             # extracted originals; reference the genuinely useful ones
  _source-extract.md  # raw pptx extraction (input only; gitignored)
```

Book chapters → folders: `01-Intro` (Ch 1), `02-Technical` (Ch 2), `03-Platform`
(Ch 3), `04-Legal` (Ch 4), `05-Measurement` (Ch 5), `06-Circumvention` (Ch 6),
`07-Conclusion` (Ch 7). See `../README.md` for the full deck → book-section map.

## Quarto setup

- Decks inherit `slides/_quarto.yml` (reveal.js defaults, footer, slide numbers) and
  `slides/theme.scss` (UChicago maroon). **Do not** restate format options already in
  the shared config. The `**/slides.qmd` render glob is depth-agnostic.
- Per-deck front matter is minimal:
  ```yaml
  ---
  title: "Deck Title"
  subtitle: "Internet Censorship and Online Speech"
  author: "Nick Feamster · University of Chicago"
  date: last-modified
  ---
  ```
- The deck **must `quarto render` cleanly** (`quarto render NN-Chapter/MM-Deck/slides.qmd`).

## Slide conventions

- **Titles in Title Case.** Capitalize principal words; lowercase short articles /
  conjunctions / prepositions (*a, an, the, and, or, for, to, of, in, on, by*); always
  capitalize the first and last word.
- `##` starts a slide; `#` starts a section divider. Use `{.center}` for divider/quote
  slides, `{.smaller}` for dense slides.
- Two-column layout:
  ```
  ::: {.columns}
  ::: {.column width="50%"} ... :::
  ::: {.column width="50%"} ... :::
  :::
  ```
- **Bold key terms** (the theme renders them maroon). Keep bullets tight — a slide is a
  cue, not a paragraph.
- **Current-events vignette box** (use at least one per deck, see point 2):
  ```
  ::: {.vignette}
  A short, dated, real-world hook tied to this lecture's theme.
  :::
  ```
- **Speaker notes inline** on most slides:
  ```
  ::: {.notes}
  What to say / the story / the cold-call. Not shown on the slide.
  :::
  ```
- Add a footer/speaker-note pointer to the relevant **book section** so students can
  read along (e.g., "see §2.3").

## Images (curate — don't dump)

- Reference only the **genuinely useful** images from `images/`: architecture diagrams,
  censorship/attack flows, real screenshots that teach something, data plots.
- **Drop** clip-art, logos, decorative headshots, and redundant screenshots.
- Caption figures with `![Caption](images/file.png)`. For multiple images use the
  columns layout.
- If a deck needs a diagram that doesn't exist, describe it in a `::: {.notes}` block or
  in `coverage-notes.md` rather than inventing a misleading one.

## Content approach (the three asks)

1. **Book + agenda alignment.** Build from `_source-extract.md` **and** the matching
   **book chapter/section** (read the chapter `.tex` in `../../../censorship-book/`),
   plus the relevant Meeting in `../../agenda.md` (what was *actually* covered). Prefer
   the book's framing/terminology and what was actually taught over the old slide order.
2. **Update examples to current events.** Replace dated examples with current ones
   (today is 2026). **Use web search** to ground at least one fresh, accurate, dated
   example per deck; put the freshest hook in a `.vignette`. Don't fabricate facts —
   verify before stating.
3. **Suggest missing coverage.** In `coverage-notes.md`, list (a) the current-events
   updates you made and (b) concrete suggestions for missing coverage on the lecture's
   broad themes (including book sections with no deck yet). Keep slides focused.

## coverage-notes.md format

```
# NN-Chapter/MM-Deck — instructor notes
## Current-events updates made (point 2)
- <YEAR>: ... (date-stamp each refresh so the history is legible)
## Suggested missing coverage on broad themes (point 3)
- ...
## Next-year refresh notes
- Hooks/figures with a shelf life (what will go stale and when)
- Stronger alternative vignettes flagged but not yet used
## Curated images
- which images were used / dropped and why
## Source
- rebuilt from _source-extract.md (N slides) + censorship-book §X.Y + agenda.md Meeting M
```

The **Next-year refresh notes** section is the to-do list the annual refresh (below)
reads first.

## Length guidance

Lean. A rebuilt deck is typically **15–30 slides** even if the original had 70–150 —
consolidate, cut redundancy, keep one idea per slide. The old slide count is not a target.

## Annual current-events refresh

The decks are built to be **re-pointed at the present each year** without a rebuild.
Run this at the start of each term. It is a *surgical refresh of time-sensitive
content*, **not** a re-authoring — structure, pedagogy, and slide order stay put.

**What to refresh (and only this):**

- The **`.vignette`** hook(s) — swap any example a new student would read as "old news"
  for the freshest equivalent on the same teaching point.
- **Dated facts and figures** — blocking/throttling incidents, law statuses, adoption
  stats, "as of <date>" phrasing, and any year literal.
- **Broken or superseded links**, and case/law statuses that have moved.

**How (the loop):**

1. Read the deck's `coverage-notes.md` **Next-year refresh notes** and **Current-events
   updates made** first.
2. **Web-search to verify every change.** Replace a fact only with a more current,
   *verified* one. **Never fabricate** a case, date, or figure; if you can't verify a
   fresher example, keep the existing one and note it.
3. Keep the *teaching point* identical — change the illustration, not the argument.
4. Re-stamp `coverage-notes.md`: dated bullet under **Current-events updates made**;
   refresh **Next-year refresh notes**.
5. `quarto render NN-Chapter/MM-Deck/slides.qmd` and confirm it builds clean.

**Scope guardrails:** don't add/remove slides, restructure, or chase "missing coverage"
during a refresh. Touch only `slides.qmd` and `coverage-notes.md`. Leave `_quarto.yml`,
`theme.scss`, and this file alone.

### Reusable annual-refresh prompt

Paste this to a fresh Claude session each year (edit the year):

> Refresh the current-events content of the lecture decks in `docs/slides/` for the
> **<YEAR>** academic year, following the "Annual current-events refresh" section of
> `docs/slides/TEMPLATE.md`. For each deck `NN-Chapter/MM-Deck/`: read its
> `coverage-notes.md` first; web-search to verify; update only the `.vignette` hooks,
> dated facts/figures, and stale links/case statuses; keep structure and teaching points
> unchanged; re-stamp `coverage-notes.md`; and `quarto render` each deck to confirm it
> builds. Don't fabricate facts — if you can't verify a fresher example, keep the current
> one and say so. Use one agent per deck and parallelize. When done, give me a per-deck
> summary of what changed, and flag any deck whose core example is now genuinely outdated.
