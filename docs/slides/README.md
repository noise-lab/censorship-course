# Lecture Slides

Quarto reveal.js lecture decks for **Internet Censorship and Online Speech**
(CMSC 33260 / PARR 33260 / MADD 23620 / CMSC 23260, University of Chicago).

Decks are a **content-driven rebuild** of the original PowerPoint decks, organized to
mirror the spine of the companion book **[`noise-lab/censorship-book`](https://github.com/noise-lab/censorship-book)**:
subtopic folders are numbered by **book chapter**, and decks within each are numbered by
**book section**. This is *book order*, not teaching order — the syllabus and
[`../agenda.md`](../agenda.md) carry the teaching sequence.

## Authoring

Read **[`TEMPLATE.md`](TEMPLATE.md)** before writing or editing a deck — it is the
binding spec (slide conventions, the three content asks, the annual current-events
refresh loop). The canonical worked example is **`01-Intro/01-Overview/`**.

- Shared config: `_quarto.yml` (reveal.js defaults) and `theme.scss` (UChicago maroon).
- Render a deck: `quarto render 02-Technical/01-Protocols/slides.qmd`.
- Helper scripts live in `src/`; original decks are archived in `ppt-archive/`.
- Build artifacts (`.quarto/`, `slides_files/`, `slides.html`, `_source-extract.md`,
  `images/`) are gitignored; only the images a `slides.qmd` actually references are
  force-added.

## Deck → book-section map

| Deck | Book source | Rebuilt from (original) |
|---|---|---|
| `01-Intro/01-Overview/` | **Ch 1** From Censorship to Information Control (whole) | `class/intro/01-Overview.pptx` |
| `02-Technical/01-Protocols/` | **Ch 2** Technical Controls — §2.1–2.2 (manipulating / disrupting protocols) | `class/technical/04-Protocols.pptx` |
| `02-Technical/02-DoS/` | **Ch 2** Technical Controls — §2.3 (disrupting the flow of data; throttling/DoS) | `class/technical/07-DoS.pptx` |
| `03-Platform/01-Platform/` | **Ch 3** Platform Controls — §3.1 (platforms as content-manipulation tools) | `class/platform/09-Platform.pptx` |
| `03-Platform/02-Propaganda/` | **Ch 3** Platform Controls — §3.4 (propaganda) | `class/platform/14-Propaganda.pptx` |
| `03-Platform/03-Personalization/` | **Ch 3** Platform Controls — §3.7 (personalization) | `class/platform/10-Personalization.pptx` |
| `04-Legal/01-Legal/` | **Ch 4** Legal & Economic Controls — §4.1 (law as information control; incl. EU DSA) | `class/regulatory/11-Legal.pptx` + `class/regulatory/dsa/dsa.md` |
| `04-Legal/02-NetNeutrality/` | **Ch 4** Legal & Economic Controls — §4.3 (net neutrality) | `class/regulatory/12-NetNeutrality.pptx` |
| `04-Legal/03-PaidPrioritization/` | **Ch 4** Legal & Economic Controls — §4.3 (paid prioritization) | `class/regulatory/13-PaidPrioritization.pptx` |
| `05-Measurement/01-Measurement/` | **Ch 5** Measuring Information Controls (whole) | `class/measurement/02-Measurement.pptx` |
| `06-Circumvention/01-Circumvention/` | **Ch 6** Taking Back Control (whole) | `class/circumvention/16-Circumvention.pptx` |
| `07-Conclusion/01-Conclusion/` | **Ch 7** Conclusion: The Future of Information Control (whole) | `class/intro/18-Wrapup.pptx` + `class/19-Conclusion/slides.md` |

**Notes.** The EU **DSA** deck is folded into `04-Legal/01-Legal` (book §4.1), not a
standalone deck. The course **wrap-up** and **Internet-governance conclusion** are
merged into the single `07-Conclusion/01-Conclusion` deck. The two source decks that
were already Markdown (Marp) — `dsa.md` and `19-Conclusion/slides.md` — are converted to
`slides.qmd` rather than extracted from PowerPoint.

### Out of scope
`other/` holds old talks (WWS/Princeton 2017–18, guest decks) that are **not** course
lectures; they are archived as-is and not converted.

### Book sections without a deck (candidate future decks)
Tracked as missing-coverage suggestions in the relevant `coverage-notes.md`; several
already have hands-on activities under [`../activities/`](../activities/): §3.2 Flooding,
§3.3 AI as Information Arbiter, §3.5 Disinformation, §3.6 Content Moderation; §4.2
Copyright, §4.4 Zero Rating, §4.5 Demonetization; Ch 6 sub-techniques (VPNs, Tor,
information hiding, infrastructure).
