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

## Web-page captures (not from the pptx), Oct 27 2026

Taken with headless Firefox (`/Applications/Firefox.app/Contents/MacOS/firefox
--headless --new-instance --profile /tmp/ffprof --screenshot out.png
--window-size=1280,1400 <url>`), cropped to masthead plus headline (and, for
Pew, the bar chart) with PIL, resized to 1000 px wide, saved as
`images/ce-<slug>.png` and force-added. Each is embedded inside a link to the
page it shows; the URL is in `coverage-notes.md` / `speaker-notes.md`.

| image | page | on slide |
|---|---|---|
| `ce-eucrim-dsa-fine.png` | eucrim, Jan 19 2026 | In the News: The Pressure |
| `ce-senate-sunset-230.png` | Senate Judiciary, Dec 18 2025 | In the News: The Pressure |
| `ce-engadget-kgm-verdict.png` | Engadget, Mar 25 2026 | In the News: The Pressure |
| `ce-wvik-durbin.png` | WVIK, Mar 25 2026 | In the News: The Pressure |
| `ce-meta-more-speech.png` | Meta Newsroom, Jan 7 2025 | In the News: Who Reviews Now |
| `ce-techpolicy-community-notes.png` | Tech Policy Press, Sep 22 2026 | In the News: Who Reviews Now |
| `ce-gifct-impact-2025.png` | GIFCT, May 21 2026 | Case Study: GIFCT |
| `ce-perspective-sunset.png` | perspectiveapi.com | In the News: The Classifiers |
| `ce-arxiv-bye-perspective.png` | arXiv 2604.25580 | In the News: The Classifiers |
| `ce-acl-fasching-lelkes.png` | ACL Anthology, Findings 2025 | In the News: The Classifiers |
| `ce-pew-ai-overviews.png` | Pew Research, Jul 22 2025 | From Search to Synthesis |
| `ce-pew-chart.png` | Pew Research chart, same page | The Freshest Hook |
| `ce-citizenlab-censorship-bias.png` | Citizen Lab, Aug 14 2025 | Censorship Baked Into the Model |
| `ce-khoury-deepseek.png` | Khoury College, Sep 10 2025 | Censorship Baked Into the Model |
| `ce-moderationbias.png` | moderationbias.com | Which AI You Pick Is the Policy |
| `ce-record-grok.png` | The Record, Jan 5 2026 | The Model Is Also the Target |
| `ce-bhrrc-kenya.png` | BHRRC, Feb 12 2026 | In the News: The Humans in Human Review |
| `ce-tbij-accra.png` | TBIJ, Apr 27 2025 | In the News: The Humans in Human Review |
| `ce-cloudflare-outage.png` | Cloudflare blog, Nov 18 2025 | Many Platforms Can Control Speech |
| `ce-npr-brazil-x.png` | NPR / AP, Aug 30 2024 | State Pressure Now Runs Through the Platforms |
| `ce-columbia-brazil-x.png` | Columbia Global Freedom of Expression case page | captured, linked from the State Pressure credit, not placed |
| `ce-npr-napalm-girl.png`, `ce-lawfare-brazil-x.png`, `ce-techcrunch-deepseek.png` | NPR 2016, Lawfare 2024, TechCrunch 2025 | captured, not placed (linked from the slides instead) |

Not captured: EC press release IP/26/203 (renders only with JavaScript; linked
from the Grok vignette), the Oversight Board PAO and Meta's integrity report
(block fetches), the Irish DPC inquiry (no verified URL). The legacy pptx has
no media for the AI-arbiter section (it was written in 2026), so nothing from
the extraction applies there.

Early slides (2–4) use inline Graphviz `{dot}` blocks rendered by Quarto, not
images; the legacy pptx early-slide media (`slide004_img001.png` SRUTI '06
banner, `slide005_img002.png` 201×95 clip art, `slide010_img010/012.png`
logos) were re-checked on Oct 27 2026 and remain out as decorative.
