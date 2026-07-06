# Breakout Discussions — Lecture 16: Measuring Legal and Economic Controls

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

Chapter 5.4 makes the case that legal and economic controls — takedown demands, demonetization, app-store removals, payment processor cutoffs, zero-rating — shape *what speech is viable*, not just what speech is reachable. That's a much harder measurement problem than DNS injection, because the effect is behavioral: it shows up in what people don't say and what business models don't launch. Both breakouts today wrestle with what counts as evidence when the thing you're trying to measure is an absence.

---

## Breakout A: Can You Measure a Chill?
<!-- breakout id="A" status="stub" refreshed="2026-07-06" -->

**Motion.** *"'Chilling effects' — self-censorship, demonetization-driven topic avoidance, creators leaving platforms — should be treated as a measurable form of censorship. Studies that fail to quantify them are undercounting information control, not being appropriately cautious."*

<!-- current-events:start topic="chilling-effects-self-censorship" -->
**Prep reads (5–10 min).**
- *[Placeholder — refresh skill will populate with recent studies on: creator self-censorship on YouTube/TikTok due to demonetization, journalist self-censorship in India/Turkey/Hungary, FOSTA/SESTA follow-on effects on sex workers and harm-reduction sites, or survey research on user self-censorship after high-profile takedowns.]*
- *[Placeholder — recent Lumen Database analysis, DMCA-abuse study, or news story on a specific creator or newsroom explicitly citing chilling effects for changing what they publish.]*
<!-- current-events:end -->

**Discussion prompts.**
- The book highlights natural experiments — FOSTA/SESTA killed Craigslist personals overnight; GDPR made US news sites geo-block the EU. Those are directly observable. But the harder claim is that *creators* changed what they *made* in response. What research design would convince a skeptic that a measured drop in LGBTQ political content on YouTube after the 2017 Adpocalypse is chilling and not just changing audience taste?
- Chapter 5.4 notes that demonetization data mostly comes from creator self-reports, third-party monetization checkers, and platform policy timing. All three have serious selection problems. If a creator never uploads a video because they anticipated demonetization, no measurement can catch it. Is that unmeasurable in principle, or just unmeasurable with today's tools?
- Compare two claims: (1) "Turkey's Twitter takedown requests chill journalism," measured by counting takedowns in the transparency report. (2) "Turkey's takedown requests chill journalism," measured by surveying journalists about what stories they killed. Which is the stronger evidence? Which would a court accept? Which would a political scientist accept?
- Suppose Freedom House added a "measured chilling effect" score to its country reports. What would that measurement have to include for you to trust it, and what's the risk of formalizing a metric that's inherently squishy?

**Bring back.** Your group's best operational definition of a "chilling effect" — something narrow enough to actually measure, and one specific case it would fail to catch.

---

## Breakout B: Country Rankings — Useful Simplification or Harmful Fiction?
<!-- breakout id="B" status="stub" refreshed="2026-07-06" -->

**Motion.** *"Country-level information-control rankings — Freedom on the Net, RSF's World Press Freedom Index, V-Dem's Digital Society Project — do more harm than good. They flatten within-country variation, get gamed by governments, and let researchers and journalists substitute a color-coded map for actual analysis."*

<!-- current-events:start topic="country-freedom-rankings-critique" -->
**Prep reads (5–10 min).**
- *[Placeholder — refresh skill will populate with recent coverage of: a Freedom on the Net or RSF ranking release and reactions from ranked governments; academic critiques of country-index methodology; or a case where a country's ranking diverged sharply from measured on-the-ground events (India's decline, Hungary's, the US and UK in Freedom on the Net).]*
- *[Placeholder — recent OONI, Access Now KeepItOn, or Citizen Lab report showing within-country variation (regional shutdowns, ISP-level differences, event-driven filtering) that a national rank would obscure.]*
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
