# Figure recovery: 02-Technical/02-Throttling-DoS

Source: `docs/slides/ppt-archive/class/technical/07-DoS.pptx`, 70 slides
(4 hidden: 20, 21, 23, 26), rendered 2026-10-16 with `pptx-figures.py` at
220 dpi. The throttling half of this deck was recovered by hand on 2026-10-13
from `04-Protocols.pptx` (`images/leaky-bucket.png`, `images/token-bucket.png`)
and is not revisited here. Slides 40–69 are the GFW-vs-Tor active-probing
research talk (Ensafi et al., IMC 2015) that `coverage-notes.md` already ruled
off-scope for this deck; they are skipped as a block.

| pptx slide | class | target Quarto slide | figure name | notes |
|---|---|---|---|---|
| 1 | skip | | | title |
| 2–5 | skip | | | news clippings, NYT page, IoT heat map, Mirai post-mortem quote: dated media |
| 6 | skip | | | attacker → victim boxes with four arrows; decorative, no intuition beyond the bullets |
| 7–9 | skip | | | bullets |
| 10 | skip | | | smurf broadcast amplification; same intuition as slide 22, which is the modern form. Mentioned in the notes row instead |
| 11 | skip | | | divider |
| 12, 13, 15, 16, 18 | skip | | | bullets |
| 14 | keep | new, "The SYN Flood in Pictures" (left) | tcp-handshake-timeline.png | C/S lifelines with Store data / Wait / Connected; no animation |
| 17 | keep | new, "The SYN Flood in Pictures" (right) | syn-flood-timeline.png | five spoofed SYNs, red queue bar grows; no animation |
| 19 | skip | | | divider |
| 20, 21 | skip | | | hidden; bullets on DNS DoS and 2007 root attack |
| 22 | keep | new, "Amplification in One Picture" | dns-amplification.png | builds are entrances of the base diagram; final state captured, prevention line cropped out |
| 23 | skip | | | hidden; RSA encrypt/decrypt 10× asymmetry is pre-TLS-1.3 and the L7 slide already carries the idea |
| 24 | skip | | | divider |
| 25, 27, 28 | skip | | | bullets |
| 26 | keep | new, "Ingress Filtering: Stop Spoofing at the Edge" | ingress-filtering.png | hidden slide; callout + dotted line are build steps but part of the base picture; bullets cropped out |
| 29 | keep | new, "SYN Cookies: Stateless Until Proven" (right, below bullets) | syn-cookie-layout.png | 32-bit layout bar; no animation |
| 30 | keep | new, "SYN Cookies: Stateless Until Proven" (left) | syn-cookie-exchange.png | four-message exchange with NO BUFFER / BUFFER ALLOCATED; builds are entrances only |
| 31, 32 | skip | | | uRPF strict-mode check and asymmetric-routing failure: router-operator detail beyond this course; mentioned in the ingress-filtering notes row |
| 33 | skip | | | bullets + NYT screenshot (already dropped in coverage-notes) |
| 34 | media | existing "When DoS Becomes Censorship Infrastructure" | slide034_img015.png | already embedded |
| 35, 36 | media | | | steps 1 and 2 of the Great Cannon sequence; superseded by slide 37, which contains both |
| 37 | media/keep | new, "The Great Cannon, Step by Step" | great-cannon-steps.png | embedded PNG (ppt/media/image18.png), not previously extracted; diagram follows Marczak et al. 2015, credited in the caption |
| 38 | media | existing "Whose Browsers Got Hijacked?" | slide038_img019.png | already embedded |
| 39 | media | | | Baidu referrer chart, dropped in coverage-notes as redundant |
| 40–69 | skip | | | GFW-vs-Tor active-probing talk, off-scope (Ch. 5/6) |
| 70 | skip | | | blank |

## Captured

- `images/tcp-handshake-timeline.png` (1084×821) — source: ppt-archive/class/technical/07-DoS.pptx slide 14, box 560,320,1680,1150 at 220 dpi, auto-trimmed
- `images/syn-flood-timeline.png` (1073×836) — source: slide 17, box 560,320,1680,1165, auto-trimmed
- `images/dns-amplification.png` (1414×523) — source: slide 22, box 420,360,1860,900, auto-trimmed
- `images/ingress-filtering.png` (1597×465) — source: slide 26, box 300,215,1920,680, auto-trimmed
- `images/syn-cookie-layout.png` (1343×305) — source: slide 29, box 400,910,1760,1215, auto-trimmed
- `images/syn-cookie-exchange.png` (495×775) — source: slide 30, box 1215,300,1720,1085, auto-trimmed
- `images/great-cannon-steps.png` (1612×660) — source: slide 37 (embedded picture), box 275,340,1925,1100, auto-trimmed; after Marczak et al., Citizen Lab 2015

## Embedded

Five new slides, all `{.smaller}`, no fragments; narration in the bullets and
`::: {.notes}`; five rows added to `speaker-notes.md` in slide order:

1. "The SYN Flood in Pictures" (after "SYN Flood: Asymmetry in TCP")
2. "SYN Cookies: Stateless Until Proven"
3. "Amplification in One Picture" (after "Reflection and Amplification")
4. "Ingress Filtering: Stop Spoofing at the Edge"
5. "The Great Cannon, Step by Step" (after "When DoS Becomes Censorship Infrastructure")
