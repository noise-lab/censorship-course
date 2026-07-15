# 07-Conclusion/01-Conclusion — instructor notes

## Current-events updates made (point 2)
- 2026-06-03: Vignette — Access Now/KeepItOn **2025** shutdown data (313 shutdowns,
  52 countries; conflict 125; Myanmar 95 > India 65; 75 persisting into 2026).
  Report released 2026-03-31. Replaces the older 2024 figures.
- 2026-06-03: Vignette — Encrypted-DNS/ECH arms race. China & Iran block the
  encrypted-DNS bootstrap rather than ECH itself (FOCI 2025 / PETS, July 2025;
  gfw.report USENIX Security 25). `quic-go` v0.52.0 SNI-slicing shipped 2025-05-23.
- 2026-06-03: Vignette — EU "Chat Control" (CSA Regulation): mandatory client-side
  scanning dropped (Council political agreement 2025-11-26); EU Parliament blocked
  extending voluntary mass-scanning (April 2026, per EFF). Age verification + trilogue
  still live.
- 2026-06-03: Governance examples refreshed to current framing — ICANN .io / Chagos
  return to Mauritius (2024); Australia v. X/Meta Sydney stabbing takedown (2024);
  India IT Rules 2021; EU DSA/DMA/AI Act "Brussels Effect"; Russia RuNet.
- 2026-06-03: AI epistemics slide — added **C2PA Content Credentials** as a partial,
  not-a-fix countermeasure (in-browser verify.contentauthenticity.org; native signing
  on Pixel 10 / Galaxy S25; OpenAI C2PA+SynthID; **EU AI Act Art. 50** disclosure
  enforcement begins Aug 2026). Provenance authenticates the manifest, not the truth;
  unsigned content is the common case. Source: contentauthenticity.org "State of
  Content Authenticity 2026"; EU AI Act Art. 50. (Backlog item 1.)
- 2026-06-03: NEW slide "Data Localization Has an Economics" — cloud sovereignty as a
  tax on access; **EU–U.S. Data Privacy Framework** survived *Latombe* (EU General
  Court, 2025-09-03) but is on **CJEU appeal C-703/25 P** (no hearing as of mid-2026);
  "Schrems III" risk. Sources: IAPP, Freshfields (2025–26). (Backlog item 2.)
- 2026-06-03: NEW slide "New Models for *Platform* Governance" — Meta Oversight Board
  (~200 decisions / ~320 recs over 5 yrs per Dec 2025 report; account-level review pilot
  2026; Meta funding committed through 2028, reported 2026-06); Bluesky composable
  moderation (labelers); Mastodon federation. Sources: Oversight Board H2-2025 / 5-year
  report; Bluesky "Moderation Architecture" docs; MediaPost (2026-06). (Backlog item 3.)
- 2026-06-03: Expanded the **paywalls** clause on "Tradeoffs All the Way Down" from one
  word to the informed-rich / misinformation-poor framing, with a cross-link to the
  Ch. 4 Legal-Economic deck (no new slide). (Backlog item 4.)

## Suggested missing coverage on broad themes (point 3)
- The course has no standalone **internet-governance deck**; this conclusion absorbs it.
  If governance grows, consider splitting it into its own section deck under 07.

## Next-year refresh notes
- **Shutdown vignette**: KeepItOn publishes a new annual report each spring — swap the
  313/52/Myanmar-95 figures for the 2026 numbers (expected ~March 2027). Year literal
  "2025" will read as stale.
- **ECH/encrypted-DNS vignette**: fast-moving. Check gfw.report and FOCI/PETS for the
  current GFW vs. ECH state; the quic-go SNI-slicing detail will date quickly.
- **Chat Control vignette**: in trilogue as of mid-2026 — outcome (final regulation,
  age-verification mandate, or collapse) will likely resolve before next term; update.
- **Australia v. X/Meta** and **ICANN .io**: confirm final dispositions; both were
  unresolved/precedent-setting when cited.
- **C2PA provenance vignette**: fast-moving. EU AI Act Art. 50 enforcement (Aug 2026),
  device/model adoption (Pixel/Galaxy/OpenAI), and the "verify in-browser" UX will all
  shift; re-confirm next term.
- **Data Privacy Framework slide**: track CJEU appeal C-703/25 P and any noyb "Schrems
  III" filing — a strike-down would change the example from "survived" to "struck down."
- **Platform-governance models slide**: confirm Oversight Board scope (account-level
  pilot, funding-through-2028) and that Bluesky/Mastodon are still the canonical
  composable/federated examples; decision/recommendation counts climb each report.

## Curated images
- Used: **none.** The extracted images/ are almost entirely (a) the BitTorrent
  "HIGH HOPES" animation clip-art (slide015–021, ~120 frames) and (b) zero-rating /
  WhatsApp-usage plots from an unrelated student thesis (slide048–052). Neither teaches
  a conclusion theme; a slide-of-clip-art would mislead. Per TEMPLATE.md, zero images is
  acceptable when none teach.
- If a diagram is wanted: a "protocol layer routes around damage / above-layer
  consolidation is a choke point" two-tier figure would support the Paradox section —
  noted here rather than invented.

## Source
- rebuilt from _source-extract.md (55 slides, 18-Wrapup.pptx) + merged "Internet
  Governance" Marp deck (class/19-Conclusion) + censorship-book Ch. 7 Conclusion: The
  Future of Information Control (whole chapter) + agenda.md (governance meeting).
