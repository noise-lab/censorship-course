# 07-Conclusion/01-Conclusion — instructor notes

## Current-events updates made (point 2)
- 2026-11-05: **Rework for the week-9 lecture (Dec 1–3, 2026), whose narration will
  replace the book's Ch. 7.** Deck no longer follows the book chapter's section
  structure or its text; the arc is now the course's own (look back, the two
  "Central Questions" from 18-Wrapup.pptx, where control is heading, who decides,
  taking back control, back to the breakouts) and is tied to Meetings 1–12 of
  `docs/agenda/2026-autumn.md`. Speaker notes are prompts, not scripted claims.
  Facts re-verified or added this pass:
  - Freedom on the Net 2026 (Freedom House, released 2026-10-22): 16th straight
    year of decline; 16 of 38 countries declined, 8 improved; 10 of 38 with
    age-assurance laws; Iran ~88-day nationwide shutdown; 34 countries paused for
    funding. Source: freedomhouse.org press release.
  - KeepItOn 2025: 313 shutdowns, 52 countries; **2024 figure now 304** (the deck
    said 296; Access Now revised it); Myanmar 95, India 65, conflict 125, satellite
    14 (up from 4). Source: accessnow.org/internet-shutdowns-2025 (2026-03-31).
  - Age verification: *Free Speech Coalition v. Paxton* (2025-06-27, 6–3; Oyez,
    SCOTUSblog); Australia under-16 minimum age from 2025-12-10, 4.7M accounts
    restricted (eSafety, Jan 2026).
  - EU AI Act Art. 50 applies from 2026-08-02; Digital Omnibus Reg. 2026/1744 in
    force 2026-07-27, delays high-risk rules (Dec 2027 / Aug 2028), not Art. 50;
    Art. 50(2) marking grace to 2026-12-02 only for systems already on the market
    (Gibson Dunn; secondary summaries). Pixel 10 signs every camera JPEG with C2PA
    (Google Security blog, Aug 2025). Dropped the Galaxy S25 and OpenAI SynthID
    claims (not re-verified).
  - ECH/QUIC: gfw.report USENIX Sec 2025 page: GFW QUIC SNI blocking since
    2024-04-07; as of Jan 2025 ECH not blocked unless outer SNI blocked; Uzbekistan
    blocked QUIC+ECH Dec 2024; quic-go v0.52.0 2025-05-23. The old vignette's
    "China and Iran block the encrypted-DNS bootstrap" claim was not re-verified and
    was dropped.
  - Chat Control: Council position 2025-11-26; trilogues through 2026-09-29 without
    a deal on detection; 7th trilogue scheduled 2026-12-08 (Breyer timeline);
    interim regulation lapsed April 2026 after the 2026-03-26 EP vote and was
    extended to April 2028 in July 2026 (Euronews 2026-07-23). Whether the E2EE
    carve-out survived in the final interim text is unresolved in the sources.
  - DSA Art. 40: delegated act July 2025; 49 applications, still under assessment,
    as of 2026-05-19 (European Commission news). No granted request found.
  - Cloudflare outage 2025-11-18 (Cloudflare post-mortem) and AWS us-east-1
    2025-10-20 (aws.amazon.com/message/101925).
  - Oversight Board: 347 recommendations through June 2026, 214 implemented (Meta
    H1 2026 bi-annual report); funding through 2028 announced 2026-05-28.
  - .io: Chagos treaty signed 2025-05-22; ratification frozen in 2026 (Domain
    Incite, ~April 2026); IANA still lists .io as active.
  - DPF: *Latombe* appeal C-703/25 P filed 2025-10-31, pending, no hearing found.
- Earlier refreshes (below) were for the previous deck; their figures are superseded
  where the 2026-11-05 bullet differs.
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
- **After Dec 8 2026:** update the Chat Control line with the 7th trilogue outcome.
- **Freedom on the Net 2027** (expected Oct 2027) and **KeepItOn 2026** (expected
  ~Mar 2027): swap the figures on the age-verification and shutdown slides.
- **Meeting numbers** in the notes refer to the Autumn 2026 agenda; re-map them.
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
- 2026-11-05 rework: _source-extract.md (18-Wrapup.pptx "Central Questions", zero
  rating, kill switch; merged governance deck for WSIS/ICANN/jurisdiction cases),
  Nick's intro framing (Gilmore, Roberts) as taught in Meeting 1, and
  `docs/agenda/2026-autumn.md` Meetings 1–12. **Not** built from censorship-book
  Ch. 7: that chapter (commit b410055) is to be replaced from this lecture's
  narration (book issue #14). This overrides TEMPLATE.md's "build from the book
  chapter" rule for this deck only. No 2025 conclusion-lecture transcript was
  found; the Dec 1 and Dec 2, 2025 class transcripts did not look like one (term
  scan only, not read in full).
- Previous build: rebuilt from _source-extract.md + governance Marp deck +
  censorship-book Ch. 7 + agenda.md (superseded).
