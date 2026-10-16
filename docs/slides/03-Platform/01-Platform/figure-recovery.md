# Figure recovery: 03-Platform/01-Platform

Source: `docs/slides/ppt-archive/class/platform/09-Platform.pptx`, 46 slides,
rendered 2026-10-16 (headless LibreOffice, 110 dpi contact sheet, 220 dpi
captures).

This deck was almost entirely text plus embedded media; the only composition
drawn in PowerPoint itself is slide 20. The rest of the figures are pictures
the earlier media extraction already saved under `images/slideNNN_imgNNN.*`.

| pptx slide | class | target Quarto slide | figure name | notes |
|---|---|---|---|---|
| 1, 2, 16, 26, 36 | skip | | | title and section dividers |
| 3, 8, 12, 14, 15, 17, 18, 22, 25, 28, 30, 31, 35, 37, 38, 45, 46 | skip | | | bullets only; covered by existing Quarto slides |
| 4 | skip | | | SRUTI '06 workshop banner, decorative |
| 5 | skip | | | spam-filtering bullets plus clip art; the "spam arc" was retired from the Quarto deck |
| 6 | skip | | | WMF table of SNARE spam features (renders fine through LibreOffice), but the Quarto deck dropped the spam arc |
| 7 | skip | | | four paper-title screenshots with drawn date labels; the "security lineage" bullet already carries this |
| 9 | media | "A Map of Real Moderation Systems" | `slide009_img008.png` | already embedded |
| 10, 11, 13, 29, 32, 44 | skip | | | dated news screenshots (NPR, NYT, Napalm Girl, Jigsaw launch, Zuckerberg/Dorsey) |
| 19 | media | | `slide019_img017/018.png` | Microsoft PhotoDNA infographic; left out, vendor graphic, text already covers it |
| 20 | **keep** | new, after "Family 1: Fingerprinting" | `spectral-fingerprint-match.png` | drawn composite: two spectrograms, "Downloaded File / Reference File" labels, title bars, red match frames. Stripped the two yellow playhead connectors ("Straight Connector 5", "Straight Connector 36") that the build animates across and exits |
| 21 | media | | `slide021_img021.png` | Echoprint pipeline (Leiden media-technology PDF). Left out: third-party figure, more mechanism than the deck's one-slide treatment of fingerprinting needs |
| 23 | **keep (media)** | new, after the spectral slide | `slide023_img022.png` | cryptographic vs. perceptual hash diagram; credited to the bertolami.com post in the pptx notes (URL verified 200, Oct 2026). Embedded the extracted copy (700×399) as-is |
| 24 | skip | | | mountain photo and its hash-noise image; decorative (already dropped in coverage-notes) |
| 27 | skip | | | Fast Company article screenshot plus bullets |
| 33 | media | "Prediction Is Brittle: Evasion" | `slide033_img032.png` | already embedded |
| 34 | media | "Prediction Is Brittle: Bias" | `slide034_img034.png` | already embedded |
| 39, 40 | skip | | | example ad screenshots from the audit study; inputs, not results |
| 41, 42 | media | | `slide041_img037/038.png`, `slide042_img039.png` | audit-study dot plots (Facebook vs. Google publication rates). Left out: no attribution on the pptx slide, and the table from slide 43 already carries the over/under-blocking point |
| 43 | media | "Auditing the Black Box" | `slide043_img040.png` | already embedded |

## Captured

- `images/spectral-fingerprint-match.png` (1600×683)
  source: `ppt-archive/class/platform/09-Platform.pptx` slide 20, shapes
  "Straight Connector 5" and "Straight Connector 36" stripped, cropped to the
  figure region at 220 dpi, white border added, downscaled from 2852×1194.
- `images/slide023_img022.png` (700×399, pre-existing extraction, now embedded)
  source: `ppt-archive/class/platform/09-Platform.pptx` slide 23, embedded
  picture; original source per the pptx notes:
  <https://bertolami.com/index.php?engine=blog&content=posts&detail=perceptual-hashing>.
