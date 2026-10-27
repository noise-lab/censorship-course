# Figure recovery: 03-Platform/01-Platform

Source: `docs/slides/ppt-archive/class/platform/09-Platform.pptx`, 46 slides,
rendered 2026-10-16 (headless LibreOffice, 110 dpi contact sheet, 220 dpi
captures).

This deck was almost entirely text plus embedded media; the only composition
drawn in PowerPoint itself is slide 20. The rest of the figures are pictures
the earlier media extraction already saved under `images/slideNNN_imgNNN.*`.

**2026-10-27 second pass.** The instructor asked for more of the extracted
media in the deck. Rows below marked *embedded (Oct 27)* were flipped from
skip/left-out; the new Quarto slides are listed in the target column.

| pptx slide | class | target Quarto slide | figure name | notes |
|---|---|---|---|---|
| 1, 2, 16, 26, 36 | skip | | | title and section dividers |
| 3, 8, 12, 14, 15, 17, 18, 22, 25, 28, 30, 31, 35, 37, 38, 45, 46 | skip | | | bullets only; covered by existing Quarto slides |
| 4 | skip | | | SRUTI '06 workshop banner, decorative |
| 5 | skip | | | spam-filtering bullets plus clip art; the "spam arc" was retired from the Quarto deck |
| 6 | **embedded (Oct 27)** | new "Where the Machinery Came From" (after "Why Platforms Turn to Automated Filtering") | `snare-features-table.png` | WMF rendered with `soffice --headless --convert-to png`, cropped to the table with `sips` (745×350); credited to Hao et al., USENIX Security 2009 |
| 7 | **embedded (Oct 27)** | same new slide | `slide007_img004..007.png` | the four paper-title captures (SNARE, HTTP-malware clustering, ASwatch, PREDATOR) as a two-column strip |
| 9 | media | "A Map of Real Moderation Systems" | `slide009_img008.png` | already embedded |
| 10, 11 | **embedded (Oct 27)** | "Why Platforms Turn to Automated Filtering" (right column) | `nyt-ecj-headline-2019.png`, `slide010_img011.png`, `nyt-deepfakes-headline-2020.png` | the two NYT captures were cropped to headline+subhead with `sips` (691×235, 714×150); NPR 2017 headline used as extracted. Still out: `slide010_img009` (Deadline headline, duplicates the NYT ECJ story), `slide010_img010/012` (logos) |
| 13 | **embedded (Oct 27)** | new "Mission Creep in One Headline" (after the GIFCT case study) | `slide013_img016.png`, `slide013_img015.png` | The Atlantic Jun 22 2016 headline plus the news-page screenshot of a 2015 ISIS hostage video |
| 29 | **embedded (Oct 27)** | "Content Moderation Is Genuinely Hard" (right column) | `slide029_img028.png`, `slide029_img029.png` | Napalm Girl (Nick Ut / AP) and the NPR Sep 10 2016 headline |
| 32 | **embedded (Oct 27)** | "Family 2: ML Prediction" (right column) | `slide032_img030.png` | Jigsaw Feb 2021 "500M requests daily" headline, paired with the Dec 31 2026 sunset. Still out: `slide032_img031` (body text of the same release) |
| 44 | skip | | | Zuckerberg/Dorsey hearing headline; the personalization close was retired |
| 19 | **embedded (Oct 27)** | new "How PhotoDNA Works" (after "Family 1: Fingerprinting") | `slide019_img018.png` | Microsoft's five-panel infographic, credited to microsoft.com/photodna. Still out: `slide019_img017` (the PhotoDNA landing-page banner, marketing only) |
| 20 | **keep** | new, after "Family 1: Fingerprinting" | `spectral-fingerprint-match.png` | drawn composite: two spectrograms, "Downloaded File / Reference File" labels, title bars, red match frames. Stripped the two yellow playhead connectors ("Straight Connector 5", "Straight Connector 36") that the build animates across and exits |
| 21 | **embedded (Oct 27)** | new "Inside an Audio Fingerprinter: Echoprint" (after the spectral slide) | `slide021_img021.png` | Echoprint pipeline, credited to The Echo Nest / Leiden Media Technology 2015 (source PDF verified 200) |
| 23 | **keep (media)** | new, after the spectral slide | `slide023_img022.png` | cryptographic vs. perceptual hash diagram; credited to the bertolami.com post in the pptx notes (URL verified 200, Oct 2026). Embedded the extracted copy (700×399) as-is |
| 24 | skip | | | mountain photo and its hash-noise image; decorative (already dropped in coverage-notes) |
| 27 | skip | | | Fast Company article screenshot plus bullets |
| 33 | media | "Prediction Is Brittle: Evasion" | `slide033_img032.png` | already embedded |
| 34 | media | "Prediction Is Brittle: Bias" | `slide034_img034.png` | already embedded |
| 39, 40 | **embedded (Oct 27)** | new "The Audit, Probe by Probe" (after "Auditing the Black Box") | `slide039_img035.png`, `slide040_img036.png` | the probe ads, shown as the left "inputs" column |
| 41, 42 | **embedded (Oct 27)** | same new slide (right column) | `slide041_img037/038.png`, `slide042_img039.png` | audit-study dot plots; attribution resolved: Matias, Hounsel & Feamster, CSCW 2022 (arXiv 2103.00064), also added to the slide-43 caption |
| 43 | media | "Auditing the Black Box" | `slide043_img040.png` | already embedded |

## Still left out (Oct 27 pass)

- `slide004_img001.png` (SRUTI '06 banner), `slide005_img002.png` (clip art),
  `slide010_img010/012.png` (logos): decorative.
- `slide010_img009.png`: Deadline's headline on the same ECJ ruling the NYT
  capture covers.
- `slide019_img017.png`: PhotoDNA landing-page banner, marketing copy only.
- `slide020_img019/020.png`: the raw 8003×1010 spectrogram strips already
  composed into `spectral-fingerprint-match.png`.
- `slide024_img023/024.png`: the mountain photo and its hash-noise image;
  the hash recipe is already on the fingerprinting slide.
- `slide027_img025/026/027.png`: Fast Company 2017 anti-revenge-porn article
  (text block, headline, logo); the "store the hash, not the photo" point is
  already on the perceptual-vs-cryptographic slide.
- `slide032_img031.png`: body text of the Jigsaw press release.
- `slide033_img033.png`: Hosseini's second table (inserting "not" barely
  lowers scores); the first table makes the evasion point and the slide
  already carries a vignette.
- `slide044_img041.png`: Zuckerberg/Dorsey hearing headline (slide retired).

## Captured

- `images/spectral-fingerprint-match.png` (1600×683)
  source: `ppt-archive/class/platform/09-Platform.pptx` slide 20, shapes
  "Straight Connector 5" and "Straight Connector 36" stripped, cropped to the
  figure region at 220 dpi, white border added, downscaled from 2852×1194.
- `images/slide023_img022.png` (700×399, pre-existing extraction, now embedded)
  source: `ppt-archive/class/platform/09-Platform.pptx` slide 23, embedded
  picture; original source per the pptx notes:
  <https://bertolami.com/index.php?engine=blog&content=posts&detail=perceptual-hashing>.
- `images/snare-features-table.png` (745×350, new Oct 27 2026)
  source: `ppt-archive/class/platform/09-Platform.pptx` slide 6, the WMF
  `slide006_img003.wmf` rendered with LibreOffice headless (816×1056 page) and
  cropped to the table with `sips --cropOffset 355 25 -c 350 745`.
- `images/nyt-ecj-headline-2019.png` (691×235) and
  `images/nyt-deepfakes-headline-2020.png` (714×150), new Oct 27 2026:
  headline-plus-subhead crops of `slide011_img013.png` and `slide011_img014.png`
  (`sips --cropOffset 1 1`; an offset of 0 0 makes sips crop from the centre).
