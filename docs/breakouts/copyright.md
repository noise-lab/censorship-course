# Breakout Discussions — Copyright

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

Chapter 4.2 argues that copyright was not designed as a censorship regime but routinely functions as one: DMCA notice-and-takedown lets bad-faith claimants suppress lawful speech faster than the speaker can defend it, and automated matchers (Content ID, Rights Manager) cannot perform fair-use analysis. Both breakouts probe where the line between enforcement and censorship actually sits.

---

## Breakout A: Automated Takedown — Should False Claims Carry Real Costs?
<!-- breakout id="A" status="current" refreshed="2026-07-06" -->

**Motion.** *"Every party issuing a DMCA takedown (including automated Content ID matches) should face statutory penalties for demonstrably false claims — no more free shots at other people's speech."*

<!-- current-events:start topic="dmca-takedown-abuse" -->
**Prep reads (5–10 min).**
- [YouTube Processed 2.5 Billion Content ID Copyright Claims in 2025](https://torrentfreak.com/youtube-processed-2-5-billion-content-id-copyright-claims-in-2025/) — TorrentFreak, 2026. YouTube's own transparency data: rightsholders monetized 90% of Content ID claims, and >6% of webform DMCA notices were "likely false" — 10x the abuse rate of any other tool.
- [YouTube Copyright Transparency Report](https://transparencyreport.google.com/youtube-copyright/balanced-ecosystem) — Google, ongoing. Google's own dashboard: 12.8M Content ID disputes, and uploaders won 67% of the ones they contested in 2025.
- [A Guide to YouTube Removals](https://www.eff.org/issues/intellectual-property/guide-to-youtube-removals) — Electronic Frontier Foundation, updated 2025. EFF's running critique of keyword-based and purely automated takedowns and how Content ID sits outside the DMCA counter-notice regime.
- [Takedown Hall of Shame](https://www.eff.org/takedowns) — Electronic Frontier Foundation. Ongoing case file of specific abusive takedowns (Fox/"Homeland," SmellyOctopus, etc.) that instructors can use as concrete examples in class.
<!-- current-events:end -->

**Discussion prompts.**
- The WSJ 2020 investigation found Google had processed over 4 billion URL removal requests. What error rate is acceptable at that scale? Is 1% false positives 40 million pieces of wrongly-suppressed speech, or is it just the cost of doing business?
- DMCA Section 512(f) technically allows penalties for knowingly false takedowns, but has almost never been enforced. Would putting real teeth in 512(f) (statutory damages, no scienter requirement, fee-shifting) chill legitimate copyright enforcement — or just chill *abusive* enforcement? Who bears the risk today, and who would bear it under your proposal?
- Content ID is not the DMCA — it is a private contractual system YouTube built to keep Viacom-style lawsuits away. Should platform-built matchers be regulated as if they were DMCA notices, or is that a category error? Would forcing them into the DMCA regime just push platforms to take down more, not less?
- The Cox verdict ($1B in 2019 for failing to disconnect repeat infringers) points the incentive in one direction; the SIGCOMM peer-review-takedown episode points the other. Design an intermediary-liability rule that survives both incidents.

**Bring back.** Your group's proposed penalty structure for false takedowns, and one bright-line example of what should *not* count as a takedown-eligible claim at all.

---

## Breakout B: Sci-Hub, Shadow Libraries, and the Ethics of Bulk Defiance
<!-- breakout id="B" status="current" refreshed="2026-07-06" -->

**Motion.** *"Sci-Hub, LibGen, and other shadow libraries are a legitimate — even necessary — response to a scholarly-publishing system that paywalls publicly funded research."*

<!-- current-events:start topic="sci-hub-shadow-libraries" -->
**Prep reads (5–10 min).**
- [Publishers Ramp Up Pressure vs. Anna's Archive, Sci-Hub, Z-Library & Libgen](https://torrentfreak.com/publishers-ramp-up-pressure-vs-annas-archive-sci-hub-z-library-libgen-250203/) — TorrentFreak, February 2025. Coordinated escalation across jurisdictions — publisher suits, ISP blocks, and CDN/payment-processor pressure aimed at the shadow-library stack.
- [Anna's Archive Lawsuits: $322M Ruling and Active Cases](https://legalclarity.org/annas-archive-lawsuits-322m-ruling-and-active-cases/) — LegalClarity, 2026. Overview of the Spotify/UMG/Sony/Warner $322M default judgment, the separate 13-publisher $19.5M judgment, and the OCLC WorldCat ruling.
- [The plausible consequences for Anna's Archive, NVIDIA, and any other AI developer that trained on shadow libraries](https://p4sc4l.substack.com/p/the-plausible-consequences-for-annas) — Substack analysis, 2025. Traces the through-line from Bartz v. Anthropic ($1.5B settlement, September 2025) to the Meta LibGen disclosures to NVIDIA's pending Anna's-Archive claims.
- [Anna's Archive (Wikipedia)](https://en.wikipedia.org/wiki/Anna's_Archive) — updated 2026. Useful one-page overview of domain seizures (.org, .se), the Spotify metadata scrape, and the interaction with AI-training litigation.
<!-- current-events:end -->

**Discussion prompts.**
- Publicly funded research is often paywalled behind $30–$40 per-article fees. Is Sci-Hub civil disobedience, ordinary infringement, or a public-interest utility? Does the answer change if the researcher is at a well-funded U.S. university vs. a hospital in Nairobi?
- The 2024 Meta and Anthropic rulings held that *training* on copyrighted books was fair use, but settlements have hinged on whether the training corpus was *pirated* (LibGen/Books3). Is it coherent to say Sci-Hub is illegal but training on Sci-Hub is fair use? Who benefits from that gap?
- The EU Article 17 approach effectively requires platforms to filter uploads against rights-holder databases. Would an "Article 17 for research" — filter every upload against Elsevier's catalog — be a legitimate response, or does it prove the point that copyright at scale becomes a speech regulator?
- Compare shadow libraries to Napster (shut down), YouTube-DL (initially DMCA'd, then reinstated after EFF pressure), and Google Books (upheld as fair use). What actually predicts whether a system survives — the law, the users' political sympathy, or the defendant's legal budget?

**Bring back.** Your group's ranking of these access regimes from most to least legitimate: subscription paywalls, green open-access, gold open-access, Sci-Hub. Justify the top and bottom.

---

## Instructor notes

These breakouts map to the Section 4.2 takeaways on DMCA-as-censorship-tool and on automated matching's inability to perform fair-use analysis. Breakout A is the natural home for students who came in wanting to argue about YouTube demonetization (redirect that energy to Lecture 13); keep them on the *takedown* side of the pipeline here. Breakout B tends to divide students along whether they see themselves primarily as future creators (pro-copyright), future researchers (pro-access), or future platform engineers (they will tell you both sides are unworkable). If time is short, Breakout A produces a cleaner report-back; Breakout B produces the better cross-lecture connections to Chapter 4.5 on generative-AI copyright.

<!--
breakout-metadata:
  lecture: 11
  class: "Copyright"
  book_chapter: "4.2"
  last_refreshed: 2026-07-06
-->
