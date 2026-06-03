# 02-Technical/01-Protocols — instructor notes

## Current-events updates made (point 2)
- 2026-06-03: Added a `.vignette` on **Russia's YouTube throttling (2024–2025)** as the
  freshest, verified illustration of throttling-as-friction and SNI-keyed degradation.
  Figures: throttling began July 2024; YouTube fell from ~43% to 6–12% of Russian
  Internet traffic by Jan 2025 (Carnegie Endowment, Feb 2025); SNI/`googlevideo.com`
  packet-dropping mechanism from OONI / DFRLab technical analysis (Jan 2025).
- 2026-06-03: Threaded **TLS 1.3 + ECH** through the HTTP/SNI and TCP slides — censors
  blocking ECH itself is the current front line as SNI cleartext closes.
- 2026-06-03: Kept the classic, book-anchored case studies (Turkey DNS 2014, China
  Telecom BGP 2010, Pakistan/YouTube 2008, Egypt 2011) as historical spine; refreshed
  them with the book's current framing rather than the old slide order.

## Suggested missing coverage on broad themes (point 3)
- **Iran's June 2025 "stealth blackout"** (arXiv 2507.14183): prefixes stayed announced
  in BGP while domestic connectivity collapsed via DNS + VPN-signature dropping on 443.
  A strong alternative/companion vignette and a nice contrast to Egypt-style BGP
  withdrawal — could become its own short case study.
- **Encrypted-DNS arms race**: DoH/DoT *blocking* and fingerprinting (book mentions, deck
  only gestures). Worth a fuller treatment alongside Ch. 6 circumvention.
- **RPKI adoption data**: a live figure (e.g., % of routes with valid ROAs) would make the
  "needs wide adoption" point concrete; currently asserted, not quantified.
- **Shutdowns as the blunt instrument**: Access Now KeepItOn reports **313 shutdowns / 52
  countries in 2025** (released Mar 31 2026) — belongs in the Intro deck but could be
  referenced here when motivating BGP-level cutoffs.
- **QUIC / HTTP/3** filtering is only implied; the Russia case throttled QUIC separately
  (512 kbps) — a dedicated slide could cover UDP-based transport censorship.

## Next-year refresh notes
- **Russia YouTube throttling vignette** (July 2024 / Jan 2025 figures): will go stale if
  Russia formally blocks YouTube or replaces it with RuTube/VK at scale. Verify whether
  the 6–12% traffic share figure has moved; check for a 2026 Carnegie/OONI update before
  reusing.
- **Access Now figure (313/52, 2025)** if pulled in: re-verify against the next annual
  report (expect ~Mar 2027).
- **ECH-blocking framing**: fast-moving; confirm which states block ECH and whether ECH is
  default-on in Chrome/Firefox at refresh time.
- Stronger alternative vignette flagged but not used: **Iran stealth blackout, June 2025**
  — swap in if the Russia case ages out.

## Curated images
- **Used** `slide004_img001.png` — clean hierarchical DNS-resolution diagram; teaches the
  name→address lookup that every DNS-manipulation point depends on.
- **Used** `slide028_img019.png` — China Telecom→Verizon BGP hijack flow; shows the
  AS-path split (AT&T takes bogus path, Level 3 keeps legit) that explains "why most
  people didn't notice."
- **Used** `slide037_img028.png` — real block-page fingerprint table (vendor / country /
  HTTP signature); concrete measurement data, not clip-art.
- **Dropped** `slide018_img010.png`, `slide018_img011.png` (decorative Alice/Bob clip-art
  headshots); `slide019_img013/014.png`, `slide017_img008/009.png` (text packet traces —
  the bullets convey the handshake/reset more clearly); DNSSEC RR slides (slide008–014 —
  out of scope per book, which keeps DNSSEC brief); leaky/token-bucket shaper diagrams
  (slide042/043 — too low-level for this deck's altitude); `slide023_img015.wmf`
  (unrenderable WMF); redundant CNN block-page screenshots (slide034–036) and throttling
  screenshot (slide045 — replaced by live Russia vignette).

## Source
- rebuilt from _source-extract.md (46 slides) + censorship-book Ch. 2 Technical Controls,
  §2.1 (easy-to-manipulate) and §2.2 (disrupting-protocols) + agenda.md Lectures 2–4
  (DNS, BGP hijacking, throttling).
