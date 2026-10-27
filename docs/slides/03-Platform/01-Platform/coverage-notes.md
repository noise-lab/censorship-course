# 03-Platform/01-Platform — instructor notes

## Current-events updates made (point 2)
- 2026-10-27 (late afternoon): **Early slides (2–7) given graphics.** Inline
  Graphviz (`{dot}`) diagrams on "From the Pipes to the Platforms" (wire vs.
  feed), "The Real Lever Is the Choice Set" (funnel, delete vs. bury), and
  "Three Places to Manipulate the Pipeline" (production, dissemination,
  discovery); linked captures of the Cloudflare Nov 18 2025 outage post on
  "Many Platforms Can Control Speech" (`ce-cloudflare-outage.png`) and NPR /
  AP Aug 30 2024 on "State Pressure" (`ce-npr-brazil-x.png`, credit links the
  Columbia Global Freedom of Expression case record). The section divider
  "Platforms as Points of Control" was left as a divider. The legacy pptx
  early-slide media (`slide004_img001` SRUTI banner, `slide005_img002` clip
  art, `slide010_img010/012` 128-px logos) are decorative and were not used.
- 2026-10-27 (afternoon): **Links and screenshots.** Every dated source in a
  vignette on slides 7–33 is now a Markdown link to a URL that returned 200 to
  `curl -sIL -A Mozilla/5.0` the same day; the Oversight Board (403), Meta's
  H1 2026 integrity report (400) and the Irish DPC stay plain text, and the EC
  press release IP/26/203 is linked but not captured (page is JavaScript-only).
  Page captures were taken with headless Firefox (`--headless --screenshot`,
  1280 px wide, throwaway profile), cropped to masthead plus headline with PIL,
  saved as `images/ce-<slug>.png` (1000 px wide) and force-added (images/ is
  gitignored); each capture on a slide is wrapped in a link to its page. Four
  new "In the News" slides (after Why Automate, after the systems map, after
  Bias, after Genuinely Hard) hold the captures where a slide already had a
  figure. Captures: `ce-eucrim-dsa-fine`, `ce-senate-sunset-230`,
  `ce-engadget-kgm-verdict`, `ce-wvik-durbin`, `ce-meta-more-speech`,
  `ce-techpolicy-community-notes`, `ce-gifct-impact-2025`,
  `ce-perspective-sunset`, `ce-arxiv-bye-perspective`, `ce-acl-fasching-lelkes`,
  `ce-pew-ai-overviews`, `ce-pew-chart`, `ce-citizenlab-censorship-bias`,
  `ce-khoury-deepseek`, `ce-moderationbias`, `ce-record-grok`, `ce-bhrrc-kenya`,
  `ce-tbij-accra`. Captured but not placed: `ce-npr-napalm-girl` (the slide
  already carries the legacy NPR headline), `ce-npr-brazil-x`,
  `ce-lawfare-brazil-x` (slide 7 is text-heavy; linked instead),
  `ce-techcrunch-deepseek` (linked from the credit on the Baked-In slide).
- 2026-10-27 (afternoon): **AI-arbiter section graphics.** Pew headline capture
  (From Search to Synthesis) and Pew's own bar chart (Freshest Hook); Citizen
  Lab page for Ahmed, Knockel & Greenstadt, PoPETs 2025 (the "Ahmed et al."
  citation, now resolved: Simplified-character prompts are more susceptible to
  censorship bias than Traditional) plus the Khoury College DeepSeek-R1 story
  (Baked Into the Model); moderationbias.com, the standing benchmark that grew
  out of Jacob Kandel's Dec 2024 UChicago audit (Which AI You Pick; citation
  resolved from the book's ref.bib); The Record, Jan 5 2026, on the Grok
  proceedings (The Model Is Also the Target). No chatbot transcripts were
  fabricated or generated; every visual is a published page.
- 2026-10-27: Second graphics pass from the legacy pptx (see figure-recovery.md):
  added the PhotoDNA infographic, Echoprint pipeline, SNARE feature table plus
  four paper-title captures, the 2017–2020 "pressure" headlines, The Atlantic
  2016 beheading-video headline, Napalm Girl + NPR, the Jigsaw 2021 headline,
  and the audit-study probes and dot plots (now credited to Matias, Hounsel &
  Feamster, CSCW 2022). Four new image slides: "Where the Machinery Came From,"
  "How PhotoDNA Works," "Inside an Audio Fingerprinter: Echoprint," "Mission
  Creep in One Headline," "The Audit, Probe by Probe."
- 2026-10-27: **Pressure slide vignette** — first DSA fine, **€120M on X, Dec 5
  2025** (eucrim.eu); **Durbin–Graham Sunset Section 230 Act, Dec 18 2025**
  (judiciary.senate.gov); **K.G.M. v. Meta jury verdict, Mar 25 2026** ($6M,
  LA Superior Court; Engadget) and Durbin's same-day call for the sunset (WVIK).
- 2026-10-27: **Map slide vignette** — Meta Community Notes scorecard: 1.4M
  contributors, ~50,000 published notes vs. 49.34M EU fact-check labels in 2025
  (Tech Policy Press, Sep 22 2026); Oversight Board PAO Mar 26 2026 "not a
  proper substitute" (descriptive, site blocks fetches); Meta H1 2026 integrity
  report, LLMs "13% fewer mistakes," "10% more violations" (descriptive, site
  returns 400 to curl). YouTube's Sep 23 2025 reinstatement letter to Rep.
  Jordan is in the speaker notes (TechCrunch).
- 2026-10-27: **GIFCT figures refreshed** from the 2025 Annual & Transparency
  Report (published May 21 2026, PDF verified): ≈408,000 distinct items, ≈2.4M
  hashes (+123,500 in 2025), **39** members after seven joined in 2025 (TikTok,
  Snap, Roblox, GitHub, SoundCloud, Anthropic, 4D Hype).
- 2026-10-27: **Evasion vignette** — Perspective API sunset Dec 31 2026, no
  migration support (perspectiveapi.com); "Bye Bye Perspective API" (arXiv
  2604.25580, Apr 2026). **Bias vignette** — Fasching & Lelkes, Findings of ACL
  2025 (aclanthology), 1.3M sentences, 125 groups, seven systems.
- 2026-10-27: **Genuinely Hard vignette** — Kenya moderator cases (BHRRC, Feb
  2026 postponement) and Teleperformance Accra reporting (TBIJ, Apr 27 2025:
  ~150 moderators, ~$80/month base, 20 seconds per decision).
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
- **Page captures (`images/ce-*.png`, Oct 27 2026):** re-capture before
  reuse; mastheads and cookie banners change, and the Perspective sunset page
  will read as history after Dec 31 2026. Re-check every link with
  `curl -sIL -A Mozilla/5.0` and keep the "In the News" slides in sync with the
  vignettes they illustrate.
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
- **Perspective API sunset (Dec 31 2026):** after that date the Evasion and
  Family 2 vignettes become history; reword to past tense and check whether
  Jigsaw named a successor.
- **Meta Community Notes figures (Sep 2026) and LLM-reviewer claim (Oct 2026):**
  refresh from the next Tech Policy Press / Meta integrity report; the Oversight
  Board PAO is the stable anchor.
- **K.G.M. v. Meta (Mar 2026) and the Sunset Section 230 Act:** track the
  appeal and whether the bill moved; the Jan 2027 sunset date floated in press
  coverage is not in the bill text (two years after enactment).
- **Kenya moderator cases:** rulings were postponed Feb 12 2026; update once
  Justice Nderi rules.
- **Grok DSA/GDPR vignette (Jan–Feb 2026):** now SHIPPED. Track outcomes — EC
  DSA proceedings (IP/26/203, 26 Jan 2026) and Ireland DPC inquiry (17 Feb 2026)
  may produce findings/fines or fold in UK Ofcom + California AG. Update with the
  resolution and add a hard number if the "3M images in 11 days" figure is
  confirmed by a primary source (currently press-reported).
- **GIFCT figures (2024 report: 408k items, 33 members):** refresh from the next
  GIFCT Annual & Transparency Report; the mission-creep / no-appeal framing is
  durable regardless of the headline count.

## Curated images
- **USED (Oct 27 2026)** `slide019_img018.png` PhotoDNA infographic;
  `slide021_img021.png` Echoprint pipeline; `snare-features-table.png` (from the
  WMF) + `slide007_img004..007.png` paper titles; `nyt-ecj-headline-2019.png`,
  `slide010_img011.png`, `nyt-deepfakes-headline-2020.png` pressure headlines;
  `slide013_img015/016.png` Atlantic 2016 + ISIS news page; `slide029_img028/029.png`
  Napalm Girl + NPR; `slide032_img030.png` Jigsaw 2021; `slide039_img035.png`,
  `slide040_img036.png`, `slide041_img037/038.png`, `slide042_img039.png` audit
  probes and dot plots. The "DROPPED" line below predates this pass; see
  figure-recovery.md for what is still out and why.
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
