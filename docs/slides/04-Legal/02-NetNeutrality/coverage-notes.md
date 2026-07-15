# 04-Legal/02-NetNeutrality — instructor notes

## Current-events updates made (point 2)
- 2026-06-03: Added the freshest verified hook in a `.vignette`: *Ohio Telecom
  Association v. FCC*, **Sixth Circuit, Jan 2, 2025**, which vacated the FCC's 2024
  net neutrality reinstatement by applying *Loper Bright* (end of Chevron deference)
  and holding broadband is an "information service," not a Title II
  "telecommunications service." Verified against the Sixth Circuit opinion and CRS
  report LSB11264.
- 2026-06-03: Updated the regulatory-history timeline to the current state:
  2015 adopt → 2017 repeal → 2024 reinstate → **2025 struck down**. Old deck stopped
  at "2015 (Invalidated)" and called regulation "dead" without the post-2024 events.
- 2026-06-03: Added that **state net neutrality laws persist** (California's 2018 Act,
  upheld by the Ninth Circuit) and that the 2025 ruling weakens federal preemption of
  states. Verified via CPUC Public Advocates commentary and CRS.
- 2026-06-03: Added a **common-carriage → end-to-end lineage** slide (item 1):
  telegraph/telephone common carriage under the **1934 Communications Act, Title II**
  paired with the **Saltzer, Reed & Clark (1984)** "End-to-End Arguments in System
  Design." Frames Title II as the *legal* lever and end-to-end as the *technical*
  reason it fits broadband. Sources: Saltzer/Reed/Clark, ACM TOCS 2(4):277–288, Nov
  1984; Communications Act of 1934, Title II (historical, non-time-sensitive).
- 2026-06-03: Integrated the **no-competition last-mile** caveat (item 2) into the
  "Why the 2014 Disputes Faded" slide as an on-slide qualifier: the market-incentive
  argument is contingent on a competitive last mile and on ISPs not being vertically
  integrated with competing content. Drawn from the book's incentive argument (§4.3);
  structural framing, no new external claim.
- 2026-06-03: Added an **international contrast** slide (items 3 + 4): **EU Open
  Internet Regulation (EU) 2015/2120** with **BEREC** guidelines (updated **9 June
  2022** after EU Court of Justice rulings against Telekom Deutschland/Vodafone) as a
  statute-backed contrast to the US classification ping-pong, and **India TRAI's
  Prohibition of Discriminatory Tariffs for Data Services Regulations, 2016** (Feb
  2016) banning content-based differential pricing and effectively ending Free Basics.
  Includes a one-line **zero-rating cross-reference** to the zero-rating deck (Ch. 4).
  Verified via BEREC ("All you need to know about the Open Internet rules in the EU";
  BoR (22) 81 guidelines update, 9 June 2022) and TRAI/PIB press release on the 2016
  regulations.

## Suggested missing coverage on broad themes (point 3)
- *(Integrated 2026-06-03 — see "Current-events updates made":* end-to-end /
  common-carriage lineage; no-competition last-mile caveat; EU BEREC + India TRAI
  international contrast with a zero-rating cross-reference.*)*
- **DEFERRED — deep zero-rating mechanics / Kenya–South Africa field study.** Kept to a
  one-line cross-reference plus the India TRAI contrast; the empirical behavior-change
  results (Cell C/WhatsApp, MTN/Twitter) belong to the dedicated zero-rating deck, not
  here. Adding them would duplicate that deck and bloat this one beyond scope.
- Cross-links remain a one-liner only: the separate **paid-prioritization mechanics**
  deck (kept distinct per scope) and **Ch. 3 platform consolidation** (the "threat
  moved up the stack" thread) are referenced on-slide / in notes, not given a slide.

## Next-year refresh notes
- **Vignette (Sixth Circuit, Jan 2, 2025):** Will go stale if (a) the Supreme Court
  takes/decides an appeal, (b) Congress legislates net neutrality, or (c) the FCC's
  composition shifts and it tries again. Re-verify the case status each year; if a
  higher court acts, that becomes the new hook.
- **Timeline table:** add any new row (legislation, cert grant, new FCC order). The
  "struck down 2025" line is the current endpoint — update if superseded.
- **State-law claim:** confirm California's 2018 Act and Ninth Circuit ruling remain
  good law; watch for new state laws or preemption fights post-2025.
- **2014 Comcast/Netflix material** is intentionally historical (it's the book's
  teaching case) and does NOT need refreshing — it is an anchor, not a current event.
- **EU BEREC guidelines (June 2022 update):** confirm whether BEREC has issued a newer
  guidelines revision and whether the EU's zero-rating stance (application-specific =
  violation, post-2021 ECJ rulings) still holds; update the "June 2022" date if so.
- **India TRAI 2016 ban:** confirm the Prohibition of Discriminatory Tariffs
  regulation remains in force and that Free Basics is still effectively barred; watch
  for any new TRAI net-neutrality framework. Date literal "Feb 2016" is historical.
- **End-to-end / common-carriage lineage** (Saltzer/Reed/Clark 1984; 1934 Act Title
  II) is historical and does NOT need annual refreshing — it is an anchor.

## Curated images
- **Used** `images/slide011_img012.png` — real M-Lab data plot: median download
  throughput across transit provider Cogent by ISP (2013–2014), showing the collapse
  and the sharp recovery after interconnect upgrades. Strong teaching artifact for the
  congestion-vs-censorship distinction.
- **Dropped** `slide013_img014.png` (Cogent "M-Labs data and DSCP markings" email) —
  genuinely interesting (admits retail-vs-wholesale prioritization) but text-heavy and
  redundant with the speaker notes; flagged here as an optional deep-dive artifact.
- **Dropped** `slide009_img010.png`/`slide014_img015.png` (John Oliver screenshots) —
  decorative; the John Oliver reference is kept as a one-line cue in text instead.
- **Dropped** `slide003/004/005/016_*` (India screenshots, duplicated assorted
  images) — off the deck's policy/principle scope; India zero-rating is noted under
  missing coverage instead.
- The Internet-business-model diagram lives only in the book
  (`legal/figures/Internet-business`), not in the extracted `images/`, so the
  interconnection slide uses a two-column text layout rather than a figure.

## Source
- rebuilt from _source-extract.md (17 slides) + censorship-book Ch. 4 Legal and
  Economic Controls, §4.3 (Net Neutrality) + agenda.md (no dedicated net-neutrality
  meeting row found).
