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
- 2026-06-03: Added **GIFCT case study** slide ("One Hash, Every Platform") as the
  "centralization = takedown risk, no appeal" anchor. Verified figures from the
  **2024 GIFCT Annual & Transparency Report**: 408,000 distinct hashed items, 33
  member platforms; founded 2017 by Facebook/Microsoft/Twitter/YouTube. Opacity of
  inclusion criteria + absence of appeal per Brennan Center / Statewatch / EDRi.
- 2026-06-03: Added **"The Model Is Also the Target"** slide — generative AI as a
  moderation *target*, now web-verifiable. Sources: European Commission **DSA
  formal proceedings against X over Grok, 26 Jan 2026** (press release IP/26/203);
  **Ireland DPC GDPR inquiry, 17 Feb 2026**. Includes the detail that X restricted
  Grok image generation to **paying subscribers**, which doubles as the
  stratification example. (Backlog item 2 — previously deferred for fuzzy dates,
  now shipped.)
- 2026-06-03: Added explicit **Section 230 / DSA (Ch. 4)** cross-links where state
  pressure leverages safe-harbor: one line on the new Grok slide + speaker-note
  pointers on the Brazil/India state-pressure slide and the GIFCT slide. (Backlog
  item 3.)
- 2026-06-03: Expanded the **economic-stratification** bullet on "Content
  Moderation Is Genuinely Hard" to name the concrete Grok-paywall instance and the
  zero-rating parallel (book ai-arbiter §"stratification of access"). (Backlog
  item 4, integrated rather than given its own slide to stay lean.)

## Suggested missing coverage on broad themes (point 3)
- **Propaganda / disinformation deck** (book Propaganda + Disinformation sections):
  the four behavioral signatures (high volume, high retweet ratio, fast retweets,
  collusion), Benkler's *Network Propaganda* finding (bots did not displace
  mainstream sources in 2016), deepfakes (Argentina 2023), and LLM-at-scale
  propaganda. Currently only previewed here — deserves its own deck.
- *(INTEGRATED 2026-06-03)* GIFCT shared-hash database — now its own case-study
  slide.
- *(INTEGRATED 2026-06-03)* Generative AI as a moderation *target* — Grok slide
  added with verified EC/DPC dates.
- *(INTEGRATED 2026-06-03)* Section 230 / DSA cross-links — added as on-slide line
  + speaker-note pointers (kept as pointers, not a slide; the substance is Ch. 4).
- *(INTEGRATED 2026-06-03)* Economic stratification of AI access — expanded on the
  "Genuinely Hard" slide with the Grok-paywall instance.
- **Grok/Online Safety Act (UK Ofcom) and California AG** — *deferred*: Ofcom only
  "signaled" an investigation and the CA AG probe is early; ship once those have
  firm dockets/dates. The EC + Ireland actions carry the slide for now.

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
- **Grok DSA/GDPR vignette (Jan–Feb 2026):** now SHIPPED. Track outcomes — EC
  DSA proceedings (IP/26/203, 26 Jan 2026) and Ireland DPC inquiry (17 Feb 2026)
  may produce findings/fines or fold in UK Ofcom + California AG. Update with the
  resolution and add a hard number if the "3M images in 11 days" figure is
  confirmed by a primary source (currently press-reported).
- **GIFCT figures (2024 report: 408k items, 33 members):** refresh from the next
  GIFCT Annual & Transparency Report; the mission-creep / no-appeal framing is
  durable regardless of the headline count.

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
