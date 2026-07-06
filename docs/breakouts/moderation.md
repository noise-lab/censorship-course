# Content Moderation

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

Section 3.4 argues that content moderation at scale forces "impossible choices" — speed vs. accuracy, automation vs. judgment, consistency vs. flexibility, expression vs. safety — and that no technical system resolves them. Both breakouts pick a load-bearing structural question: what legal regime governs the platforms, and who (or what) actually does the moderating.

---

## Breakout A: Section 230 — Repeal, Narrow, or Leave Alone?
<!-- breakout id="A" status="current" refreshed="2026-07-06" -->

**Motion.** *"[Section 230](https://en.wikipedia.org/wiki/Section_230) of the Communications Decency Act should be substantially narrowed — either to exclude algorithmically amplified content or to condition immunity on demonstrated moderation practices."*

<!-- current-events:start topic="section-230-reform" -->
**Prep reads (5–10 min).**
- [Section 230 in 2026: How Platform Immunity Is Changing](https://www.dynamisllp.com/knowledge/section-230-immunity-changes) — Dynamis LLP, 2026. Surveys the Third Circuit TikTok ruling and March 2026 decisions cutting algorithmic recommendation out of Section 230 protection.
- [Section 230 at 30: Internet's Legal Shield Faces Coordinated Repeal Push and Trial Threats](https://www.themeridiem.com/tech-policy-regulation/2026/2/8/section-230-at-30-internet-s-legal-shield-faces-coordinated-repeal-push-and-trial-threats) — The Meridiem, February 2026. Reports the Durbin-Graham sunset bill and Rep. Gephardt's public reversal on the 1996 law he helped pass.
- [Sunset and Renew: Section 230 Should Protect Human Speech, Not Algorithmic Virality](https://ash.harvard.edu/articles/sunset-and-renew-section-230-should-protect-human-speech-not-algorithmic-virality/) — Harvard Ash Center, 2026. Argues for the "product vs. speech" distinction — the exact carve-out at issue in the motion.
- [Yes, Section 230 Should Apply Equally To Algorithmic Recommendations](https://www.techdirt.com/2026/02/23/yes-section-230-should-apply-equally-to-algorithmic-recommendations/) — Techdirt, February 2026. The counterargument: recommendation is editorial and any carve-out collapses into publisher liability that entrenches incumbents.
<!-- current-events:end -->

**Discussion prompts.**
- The book's "entrenchment effect" argument: compliance obligations scale poorly for small platforms. If we narrow 230, who benefits — users? YouTube and Meta? Neither? Consider [Mastodon](https://en.wikipedia.org/wiki/Mastodon_(social_network)) and [BlueSky](https://en.wikipedia.org/wiki/Bluesky) specifically.
- Cloudflare's 2017 decision to drop [Daily Stormer](https://en.wikipedia.org/wiki/The_Daily_Stormer), and its subsequent unease about that power, is a 230-adjacent story: Cloudflare was never a "publisher," but it acted like one for a day. Does 230 reform reach infrastructure providers or only user-facing platforms?
- [Texas HB20](https://en.wikipedia.org/wiki/NetChoice_v._Paxton) and [Florida SB7072](https://en.wikipedia.org/wiki/Moody_v._NetChoice) tried to *forbid* viewpoint-based moderation. Most 230 reform proposals try to *require* more moderation. Are these the same problem or opposite problems — and can any single legal regime address both?
- The book notes that Twitter/Facebook's January 2021 deplatformings of a sitting president were "reactive and ad hoc." Under a narrowed 230, would those decisions have been easier or harder to make? Better or worse?

**Bring back.** Rank the three options (repeal / narrow / leave alone) and identify the one thing your group could not agree on.

---

## Breakout B: Traumatized Humans or Opaque AI — Pick Your Moderator
<!-- breakout id="B" status="current" refreshed="2026-07-06" -->

**Motion.** *"Neither outsourced human moderators nor AI moderation systems are ethically acceptable at current platform scale — the only defensible answer is to shrink the platforms."*

<!-- current-events:start topic="ai-vs-human-moderation" -->
**Prep reads (5–10 min).**
- [Kenya: Court postpones ruling in two cases against Meta brought by former content moderators](https://www.business-humanrights.org/en/latest-news/kenya-court-postpones-ruling-in-two-cases-against-meta-brought-by-former-content-moderators-delaying-trial-2/) — Business & Human Rights Resource Centre, February 2026. Status update on the Motaung and Arendse/Agada lawsuits: trafficking, unfair dismissal, and union-busting claims against Meta and Sama, ruling adjourned.
- [Suicide attempts, sackings and a vow of silence: Meta's new moderators face worst conditions yet](https://www.thebureauinvestigates.com/stories/2025-04-27/suicide-attempts-sackings-and-a-vow-of-silence-metas-new-moderators-face-worst-conditions-yet) — Bureau of Investigative Journalism, April 2025. Reporting from Meta's undisclosed Teleperformance site in Accra, Ghana, where moderation moved after Kenya sued.
- [AI Platforms Are Inconsistent in Detecting Hate Speech](https://www.asc.upenn.edu/ai-platforms-are-inconsistent-detecting-hate-speech) — Penn Annenberg (Fasching & Lelkes), 2025. First large-scale audit of seven moderation systems (Perspective, Claude 3.5, GPT-4o, Mistral, DeepSeek, OpenAI/Mistral endpoints) across 1.3M synthetic sentences — dramatic disagreement on identical content.
- [Bye Bye perspective api: Lessons for Measurement Infrastructure in NLP, CSS and LLM Evaluation](https://arxiv.org/html/2604.25580v1) — arXiv, 2026. Analyzes Google's decision to shut down Perspective API on Dec 31 2026 and the drift from transparent classifiers to opaque LLM moderation endpoints.
<!-- current-events:end -->

**Discussion prompts.**
- The book cites the ["napalm girl" removal](https://en.wikipedia.org/wiki/The_Terror_of_War) by Facebook's human moderators and the [Perspective API](https://www.perspectiveapi.com/)'s brittleness (small wording changes flip toxicity scores) as evidence *both* human and automated systems fail. Do they fail in ways that cancel out when layered, or in ways that compound?
- YouTube receives 300 hours of video per minute. Spotify receives 100,000 tracks per day. If neither humans nor AI can moderate this responsibly, is the correct policy response to (a) accept the errors, (b) mandate slower upload rates, (c) break up the platforms, or (d) something else?
- The 2024 study cited in the book found that Gemini, GPT-4, Claude, and Llama disagreed on 36.5% of moderation prompts. If a platform's choice of LLM *is* a moderation policy, should that choice be subject to public consultation? Regulatory approval? Disclosed?
- YouTube's 2017 "[Adpocalypse](https://en.wikipedia.org/wiki/Adpocalypse)" — advertisers fleeing after their ads appeared next to extremist content — pushed the platform toward aggressive demonetization, which then swept up LGBTQ+ creators, war reporting, and history channels. Is demonetization moderation, or is it something else?

**Bring back.** Your group's answer to the motion — plus one concrete moderation task where you'd trust an AI over a human, and one where you'd trust a human over an AI.

---

## Instructor notes

These map directly to Section 3.4's "impossible choices framework" and the "entrenchment effect" boxed takeaways. Breakout A gets legal-heavy fast — steer groups toward the practical downstream effects (small platforms, infrastructure providers) rather than 230 doctrine. Breakout B is the ethics-heavy one; the "shrink the platforms" motion is deliberately unpopular so groups have to defend something. Both benefit from students having done the reading on [GIFCT](https://gifct.org/) and [Content ID](https://en.wikipedia.org/wiki/Content_ID).

<!--
breakout-metadata:
  lecture: 9
  class: "Content Moderation"
  book_chapter: "3.4"
  last_refreshed: 2026-07-06
-->
