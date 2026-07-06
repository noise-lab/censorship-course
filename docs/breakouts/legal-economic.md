# Breakout Discussions — Measuring Legal and Economic Controls

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

Chapter 5.4 makes the case that legal and economic controls — takedown demands, demonetization, app-store removals, payment processor cutoffs, zero-rating — shape *what speech is viable*, not just what speech is reachable. That's a much harder measurement problem than DNS injection, because the effect is behavioral: it shows up in what people don't say and what business models don't launch. Both breakouts today wrestle with what counts as evidence when the thing you're trying to measure is an absence.

---

## Breakout A: Can You Measure a Chill?
<!-- breakout id="A" status="current" refreshed="2026-07-06" -->

**Motion.** *"'Chilling effects' — self-censorship, demonetization-driven topic avoidance, creators leaving platforms — should be treated as a measurable form of censorship. Studies that fail to quantify them are undercounting information control, not being appropriately cautious."*

<!-- current-events:start topic="chilling-effects-self-censorship" -->
**Prep reads (5–10 min).**
- [Jonathon W. Penney, Chilling Effects: Repression, Conformity, and Power in the Digital Age](https://newbooksnetwork.com/chilling-effects) — Cambridge University Press, 2025 (New Books Network interview). Consolidates the empirical case that chilling effects are measurable — via surveys, behavioral traces, and natural experiments — and offers a "conformity theory" framework courts and regulators can use.
- ["Am I Being Silenced by a Machine?" AI-Driven Content Moderation and the Chilling Effect on Freedom of Expression](https://www.researchgate.net/publication/394554979_Am_I_Being_Silenced_by_a_Machine_AI-Driven_Content_Moderation_and_The_Chilling_Effect_on_Freedom_of_Expression) — Elmimouni et al., 2025. Documents that creators from marginalized groups over-experience automated takedowns and self-censor as a direct result, especially around LGBTQ, political, and public-health topics.
- [Lumen's Quiet Veto on DMCA Abuse Investigations](https://www.hackingbutlegal.com/p/lumens-quiet-veto-on-dmca-abuse-investigations) — Hacking But Legal, February 2026. A working journalist was denied access to Lumen to investigate a prolific DMCA-abuse sender — a concrete example of how the infrastructure for measuring chilling effects itself narrows.
- [Toxic By Design: The FTC and FCC's New Plans to Sabotage Content Moderation](https://progresschamber.org/research/toxic-by-design-ftc-fcc-content-moderation-230/) — Chamber of Progress, 2025. Analyzes the FTC's February 2025 RFI on "censorship" and "demonetization," which explicitly treats platform moderation as a suppressive act — a live example of governments trying to weaponize the chilling-effects vocabulary in the opposite direction.
<!-- current-events:end -->

**Discussion prompts.**
- The book highlights natural experiments — FOSTA/SESTA killed Craigslist personals overnight; GDPR made US news sites geo-block the EU. Those are directly observable. But the harder claim is that *creators* changed what they *made* in response. What research design would convince a skeptic that a measured drop in LGBTQ political content on YouTube after the 2017 Adpocalypse is chilling and not just changing audience taste?
- Chapter 5.4 notes that demonetization data mostly comes from creator self-reports, third-party monetization checkers, and platform policy timing. All three have serious selection problems. If a creator never uploads a video because they anticipated demonetization, no measurement can catch it. Is that unmeasurable in principle, or just unmeasurable with today's tools?
- Compare two claims: (1) "Turkey's Twitter takedown requests chill journalism," measured by counting takedowns in the transparency report. (2) "Turkey's takedown requests chill journalism," measured by surveying journalists about what stories they killed. Which is the stronger evidence? Which would a court accept? Which would a political scientist accept?
- Suppose Freedom House added a "measured chilling effect" score to its country reports. What would that measurement have to include for you to trust it, and what's the risk of formalizing a metric that's inherently squishy?

**Bring back.** Your group's best operational definition of a "chilling effect" — something narrow enough to actually measure, and one specific case it would fail to catch.

---

## Breakout B: Country Rankings — Useful Simplification or Harmful Fiction?
<!-- breakout id="B" status="current" refreshed="2026-07-06" -->

**Motion.** *"Country-level information-control rankings — Freedom on the Net, RSF's World Press Freedom Index, V-Dem's Digital Society Project — do more harm than good. They flatten within-country variation, get gamed by governments, and let researchers and journalists substitute a color-coded map for actual analysis."*

<!-- current-events:start topic="country-freedom-rankings-critique" -->
**Prep reads (5–10 min).**
- [Freedom on the Net 2025: An Uncertain Future for the Global Internet](https://freedomhouse.org/report/freedom-net/2025/uncertain-future-global-internet) — Freedom House, November 2025. The 15th consecutive year of decline; US dropped 3 points (still "Free"), Kenya –6, Georgia –4, Bangladesh +5 — a good text to interrogate for what a national score does and doesn't capture.
- [2026 RSF Index: press freedom at a 25-year low](https://rsf.org/en/2026-rsf-index-press-freedom-25-year-low) — Reporters Without Borders, April 2026. First time more than half the world's countries fall into "difficult" or "very serious"; US down 14 points since 2022 (now 64th); India at 157.
- [India is 157th Out of 180 Countries on RSF's 2026 World Press Freedom Index](https://m.thewire.in/article/media/india-is-157th-out-of-180-countries-on-rsfs-2026-world-press-freedom-index) — The Wire, May 2026. Government reaction and methodology critique from a country whose ranking has become a diplomatic flashpoint — the case study for whether rankings shape or distort politics.
- [Rising repression meets global resistance: Internet shutdowns in 2025](https://www.accessnow.org/wp-content/uploads/2026/03/KeepItOn-Internet-Shutdowns-2025-Annual-Report.pdf) — Access Now / #KeepItOn, March 2026. 313 shutdowns across 52 countries, most sub-national (Myanmar 95, India 65) — the clearest recent evidence that national scores erase enormous within-country variation.
<!-- current-events:end -->

**Discussion prompts.**
- Chapter 5.4 argues that the same moderation decision "may be reported transparently when it affects someone in France but remain opaque when it affects someone in California." Freedom House rates France and California-the-US as broadly comparable ("Free"). If the DSA-vs-nothing gap is that large, what is a single national score actually measuring?
- The book's technical chapter shows measurement resolution down to the AS level (Nepal blocked Telegram on some ISPs but not others; El Salvador saw AS-specific anomalies). A national rank collapses all of that. Is the right response (a) publish AS-level or region-level ranks, (b) publish continuous distributions instead of scores, (c) keep the national score because policymakers need something they can act on, or (d) abandon ranking altogether and just publish the underlying measurements?
- Rankings shape aid, sanctions, and journalists' framing. When India drops from "Free" to "Partly Free" or Kashmir gets its own footnote, real diplomatic consequences follow. Does that argue for more caution in ranking, or for taking rankings even more seriously as a form of governance?
- Compare Freedom on the Net's methodology (expert scoring on ~21 questions) with OONI's methodology (running probes and publishing results). One is interpretive and comparable across countries; the other is direct and only tells you what's blocked from specific vantage points. Which is more useful for a human-rights lawyer? For a circumvention-tool developer? For a policymaker?

**Bring back.** Whether your group would keep, kill, or reform national rankings — and one concrete change (methodology, presentation, or use) that follows.

---

## Instructor notes

These breakouts map to Chapter 5.4's two hardest measurement problems: the invisibility of legal/economic controls (which the "chilling effects" debate in Breakout A targets) and the aggregation problem in comparative studies (which Breakout B targets). Breakout A is the harder debate — it forces students to grapple with what counts as evidence when the phenomenon is behavioral rather than technical, and it pairs well with the FOSTA/SESTA and GDPR natural-experiment material. Breakout B is the more approachable debate and works well as a bridge to the policy chapter, since it puts pressure on the tools students will actually see cited in the wild.

<!--
breakout-metadata:
  lecture: 16
  class: "Measuring Legal and Economic Controls"
  book_chapter: "5.4"
  last_refreshed: 2026-07-06
-->
