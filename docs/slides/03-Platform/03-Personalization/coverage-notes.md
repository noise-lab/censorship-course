# 03-Platform/03-Personalization — instructor notes

## Current-events updates made (point 2)
- 2026-06-03: Added a verified vignette on the **European Commission's preliminary DSA
  finding against TikTok and Meta (October 24, 2025)** for failing to give vetted
  researchers adequate data access (Article 40) — framed as the live fight over whether
  the recommendation algorithm can even be *measured*. Source: EC press release
  IP/25/2503; delegated act on researcher data access in force October 29, 2025.
- 2026-06-03: Updated the filter-bubble framing to the book's current treatment — Pariser
  (2011) thesis partly walked back; engagement-driven **passive-signal** feeds (TikTok
  "For You") and **group-membership** bubbles on WhatsApp/Telegram (book's newer framing).
- 2026-06-03: Added a data-voids note that a 2025 arXiv study ("Data Voids and Warning
  Banners on Google Search") found Google surfaces a warning banner for only ~1% of
  queries — voids largely go unflagged. (Used in speaker notes, not as a hard on-slide
  statistic.)
- 2026-06-03: Replaced the original deck's stand-alone "Content Moderation at Scale"
  material (old Ch. 7.1) — that belongs to the Moderation deck; this deck is scoped to
  §3.7 personalization/curation/filter bubbles per the book.
- 2026-06-03 (depth pass, issue #7 item 1): Added a new slide **"Chatbots: The New Surface
  for Voids"** — generative-AI assistants answer *into* data voids. Verified: NewsGuard
  (March 2025) audit of 10 leading chatbots found ~one-third repetition of pro-Kremlin
  "Pravda" network falsehoods; paired with the *HKS Misinformation Review* (2025)
  counter-analysis ("LLMs grooming or data voids?") arguing the references reflect
  information gaps on narrow queries rather than deliberate grooming. Sources: NewsGuard
  special report; france24/axios (2025-03); misinforeview.hks.harvard.edu (2025).
- 2026-06-03 (item 2): Folded the **engagement-optimization economics** root cause into
  the "Not All Control Is Overt" slide (one line + Ch. 4 Economic Controls cross-link) —
  bubble formation as a business model, not a bug. No new slide.
- 2026-06-03 (item 3): Strengthened the decade-old 2012 Bobble "geography dominates"
  slide with verified modern audits — Hannak et al. (~11.7% of results differ, driven by
  login + location) and donated-search studies (room for a profile bubble <~2 of 10
  results). Reframes the durable finding as geography/location, not personal ideological
  enclosure. Sources: Hannak et al. arXiv:1706.05011; arXiv:1812.10943.
- 2026-06-03 (item 4): Added a new slide **"The 'Rabbit Hole': Contested Evidence"** on
  YouTube recommendation-radicalization research and its genuinely mixed findings.
  Verified: Haroon et al., PNAS 2023 (100k sock puppets; congenial + more *problematic*
  deeper, but no meaningful rise in *extremity*) vs. naturalistic/counter audits finding
  limited polarization and a strong role for user subscriptions. Sources:
  pnas.org/doi/10.1073/pnas.2213020120; pnas.org/doi/10.1073/pnas.2318127122.
- 2026-06-03 (item 5): Balanced the EU/DSA regulator slide with **US state law** —
  verified NY **SAFE for Kids Act** (algorithmic feeds for minors require parental
  consent; AG proposed rules in public comment through Dec. 1, 2025) and a companion NY
  **warning-label** law (S4505/A5346, signed Dec. 2025). Framed as the design-mandate
  lever vs. the EU transparency/data-access lever. Sources: ag.ny.gov SAFE for Kids NPRM
  (2025); nysenate.gov S4505/A5346 (Dec. 2025).

## Suggested missing coverage on broad themes (point 3)
- *(All five issue-#7 backlog items integrated in the 2026-06-03 depth pass — see
  "Current-events updates made" above. Items 1 and 4 became new slides; items 2, 3, 5
  were folded into existing slides.)*
- **Search Engine Manipulation Effect (SEME)** — Epstein & Robertson's claim that biased
  rankings can shift undecided voters, and its replication debate (PLOS ONE 2024), would
  deepen the "adversarial personalization" slide if a future pass wants more on
  ranking-as-persuasion. Deferred this pass to keep the deck lean.
- **Recommender design alternatives** (bridging-based ranking, "middleware," chronological
  defaults) — the *solutions* side of the policy story. Currently only implied via the NY
  chronological-feed mandate; could be a forward pointer if the Ch. 4 deck doesn't cover it.

## Next-year refresh notes
- **DSA TikTok/Meta vignette (Oct 24, 2025 preliminary finding):** check status. By the
  next term this may have moved to a confirmed non-compliance decision and an actual fine
  (up to 6% turnover), or been settled — update from EC pressroom. The "preliminary"
  wording will go stale fast.
- **TikTok "For You" passive-signals** claim: stable for now, but verify TikTok hasn't
  materially changed its disclosed recommender inputs (DSA transparency reports).
- **Data-voids ~1% warning-banner figure** (2025 arXiv): a single study; replace if a
  larger or more recent audit appears.
- **Bobble 2012 numbers** (>85% top-10 inconsistency; geography > profile): explicitly
  caveated as decade-old, now paired with verified modern audit estimates (Hannak ~12%;
  donated-search <~2/10 profile effect). If a fresher large-scale search audit appears,
  swap in for the Hannak/donated-search figures.
- **NewsGuard "~one-third / 10 chatbots" chatbot-disinfo figure (Mar. 2025):** a single
  vendor audit; chatbot lineup and rates will move fast. Re-check NewsGuard's later audits
  (an Axios piece flagged worsening rates in Sept. 2025) and keep the HKS data-void
  counter-framing so the slide stays a *debate*, not a verdict.
- **NY SAFE for Kids Act + warning-label law:** status will move. As of June 2026 the SAFE
  for Kids rules were post-comment (closed Dec. 1, 2025) and pending finalization (effective
  180 days after final rules); the warning-label law was signed Dec. 2025. Expect
  First-Amendment litigation — verify whether either is enjoined or in force, and whether
  other states (e.g., CA, MN) have comparable algorithmic-feed laws to cite instead.
- **YouTube rabbit-hole evidence:** the "contested" framing is stable, but check for newer
  causal/naturalistic audits (PNAS line) that might shift the balance of evidence.

## Curated images
- **Used `images/slide024_img040.png`** (Bobble UI) — a real, teaching screenshot showing
  filtered-out results highlighted in yellow; directly illustrates "the results you
  didn't see."
- **Used `images/slide039_img043.png`** (news-source diversity bar chart by country) — a
  real data plot that makes the data-void / lack-of-diversity finding concrete.
- **Considered, dropped `images/slide037_img042.png`** (RSS→extract→query study pipeline) —
  accurate but a methodology schematic that the prose already conveys; cut for leanness.
- **Considered, dropped `images/slide028_img041.png`** (geographic query-distribution map)
  — low-resolution and only illustrative of method, not a result.
- **Dropped** `slide023_img031–039.png` (clip-art user/laptop icons and duplicated
  architecture fragments), `slide017/018` (huge raw search-result screenshots, illegible
  at slide scale), `slide013/014` (decorative product-logo collages), `slide003/004/008`
  (belong to the moderation deck), per the curate-don't-dump rule.

## Source
- rebuilt from _source-extract.md (43 slides; the personalization half, slides 11–43) +
  censorship-book §3.7 (platform/personalization.tex, personalization/filter-bubble.tex,
  personalization/curation.tex) + agenda.md. Old slides' "Content Moderation at Scale"
  intro (slides 1–10) intentionally excluded as out of scope for this deck.
