# 03-Platform/01-Platform — instructor notes

## Current-events updates made (point 2)
- 2026-06-03: Replaced the old Zuckerberg/Dorsey "personalization" close with the
  **AI-as-arbiter** framing from the book. Freshest vignette is **Pew Research,
  22 Jul 2025**: AI Overviews cut click-through to 8% (vs. 15%), 26% session
  abandonment, 1% in-summary clicks (browsing data, Mar 2025) — verified at
  pewresearch.org.
- 2026-06-03: Added the **Brazil X block (30 Aug–8 Oct 2024)** as the verified
  state-pressure vignette, per the book's §3.1 takeaway; cross-checked dates
  (block imposed by de Moraes; lifted 8 Oct after X paid fines, named a legal
  rep, removed specific accounts).
- 2026-06-03: Added the **2024 cross-model moderation audit** (Gemini/GPT-4/
  Claude/Llama disagree on 36.5% of 96 prompts; "detective vs. referee"; ~\$1.58
  to replicate) and the **Simplified-vs-Traditional-Chinese LLM censorship**
  finding (Ahmed et al.) — both from the book's ai-arbiter section.
- 2026-06-03: Retired the standalone "spam is an old problem" arc; folded into one
  "why automate" slide that reframes security-style filtering as now adjudicating
  *speech*.

## Suggested missing coverage on broad themes (point 3)
- **Propaganda / disinformation deck** (book Propaganda + Disinformation sections):
  the four behavioral signatures (high volume, high retweet ratio, fast retweets,
  collusion), Benkler's *Network Propaganda* finding (bots did not displace
  mainstream sources in 2016), deepfakes (Argentina 2023), and LLM-at-scale
  propaganda. Currently only previewed here — deserves its own deck.
- **GIFCT and the shared-hash database** as cross-platform governance: who decides
  what enters the terrorism hash database, and the lack of appeal — a strong
  "centralization = takedown risk" case study.
- **Generative AI as a moderation *target*, not just a moderator** (e.g., the Grok
  NCII-deepfake controversy and Ofcom/EU Online Safety Act responses, early 2026).
  Verified that regulators opened probes, but precise per-regulator dates were
  fuzzy at authoring time — left out of slides to avoid stating unverifiable
  dates; revisit when primary timelines firm up.
- **Section 230 / intermediary liability and the DSA** belong to Ch. 4 but should
  be explicitly linked from here (state pressure → safe-harbor leverage).
- **Economic stratification of AI access** (paid vs. free tiers as a tax on
  access; parallel to zero rating) — mentioned on one bullet; could expand.

## Next-year refresh notes
- **Pew AI-Overviews vignette (Jul 2025):** will read as dated by ~2027; check for
  a newer Pew or first-party study and update the 8%/15%/26% figures. Google
  disputes the methodology — note the contest but keep a verified source.
- **Brazil X block (2024):** stable historical fact; keep as anchor unless a
  fresher independent-judiciary-vs-platform block (or a new Brazil episode)
  is better. Confirm the Aug 30–Oct 8 2024 dates still match the record.
- **Cross-model audit (2024, 36.5% disagreement):** refresh if a larger or newer
  multi-model moderation audit appears; the "detective vs. referee" framing is
  durable.
- **India IT Rules fact-check unit:** status was litigated; verify current legal
  standing before re-asserting "comply or lose safe harbor."
- **Grok/Online Safety Act:** strong candidate vignette once dates are
  pinned — flagged but deliberately not used this year.

## Curated images
- **USED** `slide009_img008.png` — Table 3, breakdown of notable algorithmic
  moderation systems (Content ID / PhotoDNA / GIFCT / Perspective). Real,
  teaches the hash-match vs. ML-prediction taxonomy.
- **USED** `slide033_img032.png` — Hosseini et al. Perspective API evasion table
  (84 → 20 with "idiiot"). Strong empirical demo of ML brittleness.
- **USED** `slide034_img034.png` — Binns et al. bias-by-training-set scatter plot.
  Real data; shows moderation accuracy depends on annotator composition.
- **USED** `slide043_img040.png` — political-ad audit (Facebook vs. Google
  approvals); illustrates over/under-blocking from an external audit.
- **DROPPED** decorative/marketing images (slide004/006/010/011/013 clip-art and
  screenshots), the mountain photo (slide024_img023, perceptual-hash demo art —
  decorative), redundant fingerprinting screenshots, and `*.wmf` (not renderable).
  None taught beyond what the kept figures and text convey.

## Source
- rebuilt from _source-extract.md (46 slides) + censorship-book Ch. 3 Platform
  Controls, §3.1 (platforms.tex "How Platforms Became Content-Manipulation Tools"
  + ai-arbiter.tex "AI as Information Arbiter") + agenda.md (platform power /
  government control over platforms discussion prompts).
