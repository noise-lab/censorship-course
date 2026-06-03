# 05-Measurement/01-Measurement — instructor notes

## Current-events updates made (point 2)
- 2026-06-03: Added Uganda **2026** election vignette to the Uganda case-study slide —
  OONI documented blocking of WhatsApp and Facebook on Ugandan networks after the
  January 2026 general election, echoing the 2021 event shown in the figure. Verified via
  OONI "Measuring Internet Censorship: Challenges, Trends, and Impact" (2026,
  ooni.org/post/2026-measuring-internet-censorship-trends-challenges-impact/; Internet
  Society Pulse, May 2026).
- 2026-06-03: Added DSA Transparency Database vignette — **9 billion+** moderation
  decisions logged in **H1 2025**, of which **~99%** were platform-initiated (own terms),
  not legal orders. Verified via European Commission "DSA brings transparency" pages
  (digital-strategy.ec.europa.eu, 2025).
- 2026-06-03: Replaced dated "Chapter 4" framing with the book's "Information Controls"
  framing; folded in the book's five-step investigation walkthrough, the platform/
  legal/economic measurement sections, and the Lumen/DSA/natural-experiment material that
  the original 2017-era pptx predated.

## Suggested missing coverage on broad themes (point 3)
- **Modern GFW / Iran / Kazakhstan measurement**: the book cites GFWeb, Iran multi-layer
  filtering (millions of domains), and Kazakhstan state HTTPS interception (rogue root CA
  / MITM). None are on slides yet — a strong "measurement meets real infrastructure" slide.
- **Encore demo / same-origin policy mechanics**: could add a live or animated example of
  onload/onerror as a one-bit side channel; currently text-only.
- **Statistical detection depth**: the original deck had max-likelihood / hypothesis-
  testing slides (IP ID acceleration as a stationary i.i.d. random variable). Dropped for
  lean-ness; revisit if the audience is technical and wants the detection math.
- **Salganik's principles-based ethics framework** (respect for persons, beneficence,
  justice, respect for law/public interest) — original slide 43. The ethics section uses
  the book's proportionality/transparency/harm-min/dialogue framing instead; could add
  Salganik (*Bit by Bit*) as the named scaffolding.
- **Zero-rating / demonetization case detail**: Chen-Feamster-Calandro South Africa/Kenya
  natural experiments and YouTube "Adpocalypse" are in §5.4 but only named on slides.
- **Censored Planet methodology depth** (Satellite/Iris for DNS, Augur for TCP/IP, Hyperquack
  for HTTP/S) — currently only named as a platform; could get its own slide.

## Next-year refresh notes
- **Uganda 2026 vignette**: verify whether a fresher election-time block (any country)
  is better documented by OONI for the upcoming term; the 2021 figure stays regardless.
  Will read as "old news" once a more recent flagship OONI case appears.
- **DSA "9 billion / H1 2025" figure**: the Commission updates totals each reporting
  period — re-pull the latest half-year number and the platform-initiated share (~99%).
  Confirm the VLOP threshold (45M EU users) and VLOP list haven't changed.
- **X transparency report "last full report 2017"**: re-verify; if X resumes structured
  reporting (or under new policy), update the durability point.
- **OONI "200+ countries / since 2012 / millions of measurements"**: low churn but
  re-confirm the headline numbers from ooni.org.

## Curated images
- **USED** `slide008_img006.png` — Google Transparency Report traffic collapse, Uganda
  Jan 2021. Real data plot; anchors the corroboration case study.
- **USED** `slide011_img008.png` — world map of IP addresses returned for google.com
  (Pearce et al. 2017). The definitive "no single right answer" visual for DNS.
- **USED** `slide014_img009.png` — DNS manipulation prevalence by country (manipulated vs.
  all responses). Real data plot showing Iran/China/etc. and within-country variation.
- **USED** `slide020_img018.png` — spooky/idle-scan diagram with IP ID 6→8. Matches the
  book's four-step TCP/IP walkthrough exactly; best teaching diagram in the set.
- **DROPPED** `slide018_img012.png` and other China-flag clip-art — decorative, no content.
- **DROPPED** redundant OONI/Google screenshots (slide006/007 logos, slide008_img007),
  duplicate scan-behavior images (slide018/019/021/023), heat maps and category bar charts
  (slide026–028) — superseded by the four kept plots or too low-resolution/redundant to teach.
- **DROPPED** `slide043_img029.png` (Salganik principles graphic) — ethics handled via the
  book's framing; flagged above as possible add-back.

## Source
- rebuilt from _source-extract.md (44 slides) + censorship-book Ch. 5 Measuring
  Information Controls (whole chapter: overview, technical, platform, legal-economic,
  ethics) + agenda.md (Ethics of censorship measurement).
