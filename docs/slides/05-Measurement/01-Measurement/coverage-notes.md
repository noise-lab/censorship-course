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
- 2026-06-03: Added new slide **"Measurement Meets Real Infrastructure"** (after Encore)
  covering China's multi-layered GFW (GFWeb), Iran's multi-layer filtering blocking
  millions of domains, and **Kazakhstan's state HTTPS interception** via a rogue **Qaznet
  root CA** (nationwide HTTPS MITM, July 2019; retried Dec 2020; browsers blocklisted the
  cert). Verified via Raman et al. "Investigating Large Scale HTTPS Interception in
  Kazakhstan" (IMC 2020, dl.acm.org/doi/10.1145/3419394.3423665); Mozilla policy blog
  (blog.mozilla.org/netpolicy/2020/12/18/kazakhstan-root-2020/); Kazakhstan MITM
  (en.wikipedia.org/wiki/Kazakhstan_man-in-the-middle_attack). Book §5.2 cites GFWeb
  (Hoang 2024), Iran (Tai 2025), Kazakhstan (Raman 2020). Also added a key-takeaways bullet.
- 2026-06-03: Folded **Censored Planet methodology depth** into the "Other Measurement
  Platforms" slide — named **Satellite/Iris** (DNS, open-vs-trusted resolvers),
  **Augur** (TCP/IP IP-ID side channel), **Hyperquack** (HTTP/S keyword injection), mapping
  each onto the techniques already taught earlier in the deck. Verified via Censored Planet
  docs (docs.censoredplanet.org) and Sundara Raman et al. "Censored Planet" (ACM CCS 2020,
  dl.acm.org/doi/10.1145/3372297.3417883). No new slide.
- 2026-06-03: Named **Salganik's *Bit by Bit*** four-principle ethics framework
  (respect for persons, beneficence, justice, respect for law & public interest —
  Belmont 1979 + Menlo 2011) as scaffolding on the "Toward Ethical Norms" slide,
  complementing the book's proportionality/transparency/harm-min/dialogue framing.
  Verified via bitbybitbook.com/en/1st-ed/ethics/principles/. No new slide.
- 2026-06-03: Added an **encrypted DNS (DoH/DoT) measurement tie-in** to the DNS-prevalence
  slide with a one-line cross-link to Ch. 2 / the Circumvention deck — censors now
  measurably block the encrypted resolvers themselves (Li et al. 2024: ~6% of encrypted
  DNS queries censored globally, ~36% from inside China; DoT/DoH/DoQ widely blocked in
  censored regions). Verified via FOCI/PETS 2025–2026 papers and the 2021 WWW
  "Understanding the Impact of Encrypted DNS on Internet Censorship" line of work. No new slide.

## Suggested missing coverage on broad themes (point 3)
- **Encore demo / same-origin policy mechanics**: could add a live or animated example of
  onload/onerror as a one-bit side channel; currently text-only. *(Deferred 2026-06-03:
  lean target; text treatment is sufficient and a live demo is a class exercise, not a slide.)*
- **Statistical detection depth**: the original deck had max-likelihood / hypothesis-
  testing slides (IP ID acceleration as a stationary i.i.d. random variable). Dropped for
  lean-ness; revisit if the audience is technical and wants the detection math.
  *(Deferred 2026-06-03: out of scope for the backlog pass; keep the one-line "detection
  is statistical" treatment.)*
- **Zero-rating / demonetization case detail**: Chen-Feamster-Calandro South Africa/Kenya
  natural experiments and YouTube "Adpocalypse" are in §5.4 but only named on slides.
  *(Deferred 2026-06-03: not in the backlog; the legal/economic slide already names the
  natural-experiment method, which is the teaching point.)*

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
- **Kazakhstan rogue-CA dates (2019 / Dec 2020)**: stable historical facts; only update if
  Kazakhstan (or another state) mounts a fresh nationwide rogue-root-CA / HTTPS-MITM push
  that becomes the better live example. The teaching point (state rogue CA) stays regardless.
- **Encrypted-DNS censorship stats (Li et al. 2024: ~6% global / ~36% in China)**: a
  research figure, not a headline; re-pull a fresher FOCI/PETS measurement each term if a
  cleaner global number appears. ECH (Encrypted Client Hello) blocking in RU/IR/CN is the
  emerging frontier — promote it if it matures.
- **Censored Planet scale ("tens of billions of measurements / ~95,000 vantage points
  weekly")**: in speaker notes only; re-confirm from censoredplanet.org if cited on-slide.

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
