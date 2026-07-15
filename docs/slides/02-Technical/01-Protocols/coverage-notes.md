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
- 2026-06-03: Added a new slide **"Not Every Shutdown Withdraws the Route"** with an
  Iran **June 2025 "stealth blackout"** `.vignette`, contrasting routes-stay-announced /
  border-gateway chokepoint (DNS poisoning, TLS interception, protocol whitelisting; VPN
  searches ~707%) against Egypt-style BGP withdrawal. Framed as Roberts *friction*.
  Sources: Aryapour, arXiv 2507.14183 (Jul 2025); Filterwatch multi-stakeholder analysis
  (Oct 2025).
- 2026-06-03: Quantified the **RPKI "needs wide adoption"** point on the BGP-defenses
  slide with a verified figure: **~60% of IPv4 routes have valid ROAs** (world average,
  early–mid 2026), up from ~50–54% a year earlier. Sources: MANRS RPKI growth (Jan 2025),
  APNIC RPKI stats / Kentik (2025–26); NIST RPKI Monitor (rpki-monitor.antd.nist.gov)
  tracks it live — re-pull the headline % at refresh time.
- 2026-06-03: Added a new slide **"A New Transport to Police: QUIC / HTTP-3"** — UDP/443
  transport, why TCP `RST` injection doesn't apply, SNI-based QUIC blocking (GFW since
  Apr 2024; Russia TSPU), Russia's ~512 kbps QUIC throttle, and UDP/443 blocking as a
  blunt fallback. Sources: "Exposing and Circumventing SNI-based QUIC Censorship of the
  GFW" (USENIX Security 2025, gfw.report; ~58K FQDNs Oct 2024–Jan 2025).
- 2026-06-03: Gave **encrypted-DNS blocking/fingerprinting** a fuller gesture on the
  existing DoH slide (DoT port-853 blocked outright; DoH fingerprinted via DPI/active
  probing; bootstrap-blocking) with an explicit **Ch. 6** cross-link. Sources: OONI
  DoT/DoH blocking study; China "Shield-Cube"/DNS4CN; Iran ~50% DoT endpoints unreachable.

## Suggested missing coverage on broad themes (point 3)
- **Shutdowns as the blunt instrument**: Access Now KeepItOn reports **313 shutdowns / 52
  countries in 2025** (released Mar 31 2026) — belongs in the Intro deck but could be
  referenced here when motivating BGP-level cutoffs. *Deferred here: lives more naturally
  in the Intro deck; the new Iran/Egypt contrast already motivates BGP-level cutoffs.*
- *(Integrated 2026-06-03 — see "Current-events updates made": Iran June 2025 stealth
  blackout; encrypted-DNS blocking/fingerprinting; RPKI ROA-coverage figure; QUIC/HTTP-3
  filtering.)*

## Next-year refresh notes
- **Russia YouTube throttling vignette** (July 2024 / Jan 2025 figures): will go stale if
  Russia formally blocks YouTube or replaces it with RuTube/VK at scale. Verify whether
  the 6–12% traffic share figure has moved; check for a 2026 Carnegie/OONI update before
  reusing.
- **Access Now figure (313/52, 2025)** if pulled in: re-verify against the next annual
  report (expect ~Mar 2027).
- **ECH-blocking framing**: fast-moving; confirm which states block ECH and whether ECH is
  default-on in Chrome/Firefox at refresh time.
- **Iran stealth-blackout vignette** (June 2025, arXiv 2507.14183): now ON the deck as its
  own slide. Tied to a single 2025 conflict — at refresh, check for a newer "routes-up,
  users-cut" case and confirm the ~707% VPN-search figure / Filterwatch analysis still
  stand; the Egypt 2011 contrast is evergreen, so the slide survives even if the vignette
  is swapped.
- **RPKI ROA-coverage figure** (~60% IPv4, world avg, early–mid 2026): re-pull the live
  headline from NIST RPKI Monitor (rpki-monitor.antd.nist.gov) or MANRS/APNIC each year;
  it trends up, so the "still ~40% unprotected" framing may need softening over time.
- **QUIC/HTTP-3 slide**: GFW SNI-QUIC blocking (Apr 2024) and the Chrome-Initial-size
  circumvention are a live cat-and-mouse — confirm current GFW behavior and Russia's QUIC
  throttle rate at refresh; verify whether ECH-over-QUIC has shifted the front line.

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
