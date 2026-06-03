# 03-Platform/02-Propaganda — instructor notes

## Current-events updates made (point 2)
- 2026-06-03: Added freshest vignette — **OpenAI June 2025 threat report**
  (disrupted 10 malicious AI campaigns in the prior 3 months, 4 likely from China,
  incl. "Sneer Review" generating posts + their own replies for fake organic
  engagement; Russia/Iran ops also disrupted). Source: OpenAI, "Disrupting
  malicious uses of AI," June 5, 2025
  (https://openai.com/global-affairs/disrupting-malicious-uses-of-ai-june-2025/);
  corroborated by NPR, June 5, 2025
  (https://www.npr.org/2025/06/05/nx-s1-5423607/openai-china-influence-operations).
- 2026-06-03: Added "Grooming the Chatbots" slide — NewsGuard Mar 2025 report on
  the Kremlin-linked **Pravda network** (~150 sites, 3.6M+ articles in 2024;
  chatbots echoed claims in ~33% of relevant prompts), with the **contested**
  rebuttal from Harvard *Misinformation Review* (2025) arguing the effect reflects
  data voids, not successful "LLM grooming." Sources:
  https://www.axios.com/2025/03/06/exclusive-russian-disinfo-floods-ai-chatbots-study-finds ;
  https://misinforeview.hks.harvard.edu/article/llms-grooming-or-data-voids-llm-powered-chatbot-references-to-kremlin-disinformation-reflect-information-gaps-not-manipulation/
  (presented as an open, contested question, not settled fact).
- 2026-06-03: Replaced generic "examples abound" framing with the book's current
  international arc (Russia/IRA 2016, COVID-19 2020, Brazil TSE 1,000+ takedown
  orders + 2024 nationwide X block). Sourced from book §3.1 (platforms.tex).

## Suggested missing coverage on broad themes (point 3)
- **China's 50-cent army, with data.** King, Pan & Roberts (2017, APSR) reverse-
  engineered ~448M government social-media posts and found they overwhelmingly
  *cheerlead/distract* rather than argue. A single data slide would ground the
  "flooding = distraction, not rebuttal" claim empirically.
- **Downstream-effects skepticism.** Exposure ≠ persuasion. Worth a slide on the
  weak/contested evidence that influence operations change votes (e.g., Eady et al.
  2023 on IRA exposure and attitudes) to inoculate against "bots swung the election."
- **Coordinated inauthentic behavior detection at platform scale** (Meta's CIB
  takedown methodology, Graphika/Stanford IO reports) — complements the
  infrastructure-detection arc with the network/graph-based approach.
- **Generative-AI deepfakes in elections** (2024 was the global "election year";
  e.g., the Jan 2024 New Hampshire Biden robocall) — currently only implied.
- **EU DSA / Code of Practice on Disinformation** as the regulatory response — links
  this deck to the Legal chapter (Ch. 4).

## Next-year refresh notes
- **OpenAI June 2025 vignette** will read as dated by ~2027; OpenAI/Meta publish
  recurring threat reports — swap for the latest quarterly report with fresh
  numbers. Keep the "AI scales old tactics, doesn't invent new ones" teaching point.
- **Pravda / LLM-grooming slide**: the contested status is the teaching value; if the
  Harvard-vs-NewsGuard debate resolves, update accordingly. The 3.6M/2024 and ~33%
  figures are year-stamped and will go stale.
- **Brazil X block / India IT Rules** facts are from the book; verify case/law status
  (X block lifted Oct 2024; India fact-check-unit provision litigation) each year.
- Stronger alternative vignette flagged but not used: a single fresh **Doppelganger /
  Operation Overload** takedown (DFRLab tracks these; campaign expanded to Bluesky in
  2025) — good substitute if an OpenAI report isn't current.

## Curated images
- USED `slide007_img006.png` — Instagram-block backfire plot (Roberts data). Directly
  illustrates the book's "blocking backfires → regimes prefer flooding" argument. Best
  single figure in the deck.
- USED `slide018_img026.png` — CDF of tweets/user showing heavy skew. Grounds the
  "manufactured consensus from a few accounts" point quantitatively.
- USED `slide054_img057.png` — ROC + precision-recall for infrastructure-based
  disinformation detection (AUC ~0.95). Real results plot for the detection arc.
- DROPPED `slide042_img046/047`, `slide043`, `slide044` — additional #bias plots;
  redundant with the chosen CDF, kept the deck lean.
- DROPPED `slide020_img028/029` (Benkler media-sphere network maps) — visually dense,
  hard to read at slide scale without heavy explanation.
- DROPPED all clip-art / decorative / definitional-screenshot images (slide003–005,
  010–017, 024–035, 039–041, 048–053) — no teaching value or pure text screenshots.
- DROPPED `.wmf` files (slide035, 040, 041) — unsupported format, would not render.

## Source
- rebuilt from _source-extract.md (55 slides) + censorship-book §3.2 (flooding.tex)
  and §3.1/§3.4 framing (platforms.tex, propaganda.tex chapter root) + agenda.md
  (Platform Controls). Original deck was "Chapter 9: Flooding, Propaganda, and
  Disinformation"; reordered to the book's Fear/Friction/Flooding spine and the
  "information control / tax on access" vocabulary.
