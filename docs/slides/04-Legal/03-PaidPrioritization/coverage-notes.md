# 04-Legal/03-PaidPrioritization — instructor notes

## Current-events updates made (point 2)
- 2026-06-03: Added US net-neutrality vignette — Sixth Circuit struck down the FCC's
  2024 Open Internet Order on **Jan 2, 2025** (first major telecom ruling after the
  2024 *Loper Bright* decision ended *Chevron* deference); as of mid-2026 no federal
  net-neutrality rules are in force. (Verified via Davis Wright Tremaine, Gibson Dunn,
  CRS LSB11264.)
- 2026-06-03: Added EU zero-rating vignette — CJEU **Case C-367/24** (Romanian
  "unlimited internet bonus"), decided **July 10, 2025**, again holding zero rating
  violates the EU Net Neutrality Regulation 2015/2120; reinforced by BEREC guidelines.
  (Verified via Bird & Bird, EDRi, Pinsent Masons.) Framed as a transatlantic split:
  same mechanism, opposite legal answers.
- 2026-06-03: Replaced the old deck's thesis-defense framing (MySpeedTest methodology,
  thesis-progress slides) with the book's "pricing as friction / tax on access"
  framing. Kept the two natural experiments (Cell C WhatsApp 3×, MTN Twitter 2014) as
  the empirical core.
- 2026-06-03: Added "India Bans Free Basics (2016)" slide — TRAI **Prohibition of
  Discriminatory Tariffs for Data Services Regulations**, **Feb 8, 2016** ("no
  discriminatory tariffs on the basis of content"), which killed Free Basics and
  Airtel Zero. Framed as the developing-world net-neutrality precedent predating the
  US/EU rulings. (Verified via TRAI regulation coverage / Wikipedia "Net neutrality in
  India" / IFF.)
- 2026-06-03: Added "Paid Prioritization's Next Form: 5G Slicing" slide — **T-Mobile
  T-Priority** full commercial launch **Feb 20, 2025**, "first commercially available
  5G network-slicing service," up to **5×** average-user resources; **AT&T "Turbo"**
  **$7/mo** data prioritization (2024). Forward-looking but grounded in shipped
  deployments. (Verified via T-Mobile Newsroom, UrgentComm, Fierce Network.)
- 2026-06-03: Integrated **app-store / payment-rail prioritization** and **CDN/cloud
  "free tier" = de facto zero rating of hosting** into the existing "Threat Moved Up
  the Stack" slide (two new bullets) rather than new slides — book already frames the
  shift to "platforms, cloud hosts, and CDNs."
- 2026-06-03: Refreshed zero-rating affordability empirics on "What Is Zero Rating?" —
  A4AI: a **2GB** plan ≈ **5.8%** of average monthly income (5GB ≈ 10.1%) across
  low/middle-income countries, vs. the UN/A4AI **"1 for 2"** target; no low-income
  country has met it. (Verified via Alliance for Affordable Internet, a4ai.org.)

## Suggested missing coverage on broad themes (point 3)
- *(All five backlog items from issue #7 integrated as of 2026-06-03 — see "Current-
  events updates made" above. Two as new slides: India 2016 ban, 5G slicing. Three
  integrated in place: app-store/payment-rail + CDN/cloud free tier on the "up the
  stack" slide; A4AI affordability refresh on "What Is Zero Rating?".)*
- **Sponsored-data (deeper)** — the slicing slide uses T-Priority/AT&T Turbo; a
  classic *sponsored-data* example (carrier billing the content provider, à la AT&T
  Sponsored Data) could be added if a current, web-verifiable deployment surfaces.
  Deferred for now to keep the deck lean.

## Next-year refresh notes
- **US net-neutrality vignette (Jan 2, 2025 Sixth Circuit / "no rules in force as of
  mid-2026")** — re-verify each term. Will go stale if Congress legislates, the FCC
  re-attempts rules, or a state-level regime (e.g., California) becomes the live story.
- **EU vignette (CJEU C-367/24, July 10, 2025)** — durable as the controlling
  interpretation, but swap for any newer CJEU/BEREC development or national
  enforcement action that is fresher news.
- **"Regulatory pendulum" table (2015/2017/2024/2025)** — add the next row whenever the
  US status changes.
- **Binge On** as the US zero-rating example is dated (~2016); replace if a current US
  carrier zero-rating offer becomes the better-known case.
- **5G slicing slide (T-Priority Feb 20, 2025; AT&T Turbo $7/mo 2024)** — re-verify
  yearly; swap in the first *content-provider* slice if/when one ships (that's the
  net-neutrality flashpoint). Watch for content-provider premium slices.
- **A4AI affordability figure (2GB ≈ 5.8%, 5GB ≈ 10.1% of income; "1 for 2")** —
  refresh from the latest a4ai.org affordability data each year; numbers drift.
- **India 2016 TRAI ban** — stable historical precedent; no refresh needed, but watch
  for any TRAI move to *relax* differential-pricing rules.

## Curated images
- **Used** `slide008_img007.png` — the MTN/Twitter time series (Avg MB/device, red
  zero-rating window). A genuine data plot that carries the natural-experiment argument.
- **Dropped** `slide007_img004/005.png` (per-carrier WhatsApp bar charts) — redundant
  with the 3× number stated in text; small-N, hard to read on a slide.
- **Dropped** `slide007_img006.png`, `slide003_img002.png`, `slide002_img001.png`,
  `slide009_img008/009.png` — logos / news screenshots / "free Twitter ending"
  headlines; decorative, not instructive.
- **Dropped** `slide010_img010.tiff`, `slide011_img011.tiff` — survey-result figures in
  TIFF (Quarto/reveal prefers PNG/SVG; content captured as text in the survey slide).

## Source
- rebuilt from _source-extract.md (12 slides) + censorship-book Ch. 4 §4.3–4.4
  (net-neutrality.tex, zero-rating.tex) + agenda.md (no dedicated meeting; built from
  book spine).
