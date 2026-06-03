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

## Suggested missing coverage on broad themes (point 3)
- **India's 2016 Free Basics ban** (TRAI differential-pricing prohibition) — mentioned
  only in a speaker note; could be a slide as the developing-world net-neutrality
  precedent and a counterpoint to the EU/US framing.
- **App-store / payment-rail prioritization** as the modern "up the stack" analog of
  fast lanes (Apple/Google fee tiers, payment-processor deplatforming) — ties §4.3 to
  the platform chapter; currently only gestured at.
- **CDN and cloud "free tier" effects** — Cloudflare/AWS as de facto zero-rating of
  hosting; who gets fast, cheap delivery and who doesn't. No deck covers this.
- **Sponsored-data / 5G network-slicing** — paid prioritization's likely next form;
  worth a forward-looking slide once a verified deployment example exists.
- **Updated zero-rating field data** — our Kenya/South Africa study is ~2014–2018;
  an A4AI/GSMA affordability-report refresh would modernize the empirics.

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
