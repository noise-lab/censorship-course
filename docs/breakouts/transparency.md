# Breakout Discussions — Measuring Platform Controls

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

Chapter 5.3 makes a blunt claim: voluntary transparency reports are self-selected, inconsistently formatted, and omit exactly the categories researchers most want (who requested removal, automated vs. manual, appeals). The DSA is the first regime to force structured, machine-readable disclosure — but the gap between *visibility* and *accountability* is still large. Both breakouts push on that gap.

---

## Breakout A: Transparency Report or Press Release?
<!-- breakout id="A" status="current" refreshed="2026-07-06" -->

**Motion.** *"Voluntary platform transparency reports — from X's post-2017 decline, to Meta's quarterly PDFs, to Reddit's country tables — are primarily reputation management. Meaningful transparency requires DSA-style mandatory, structured disclosure everywhere, or it isn't real."*

<!-- current-events:start topic="platform-transparency-reports" -->
**Prep reads (5–10 min).**
- [X releases first transparency report since Musk takeover](https://thehill.com/policy/technology/4898799-x-transparency-report-elon-musk/) — The Hill, September 2024. X's first post-2017 report — much thinner than Twitter's earlier tables — showed 72,703 government takedown requests with a 71% action rate, but critics flagged it as reputation-repair for the DSA rather than substantive disclosure.
- [A Year of the DSA Transparency Database: What it (Does Not) Reveal About Platform Moderation During the 2024 European Parliament Election](https://arxiv.org/abs/2504.06976) — Shahi et al., preprint (updated 2026). Empirical audit of 1.58 billion Statements of Reasons across eight platforms; finds incomplete records, vague categories, and implausible submissions (especially from X) despite the mandatory format.
- [Opacified transparency? Assessing the DSA transparency database via TikTok's moderation during the 2024 Romanian presidential election](https://www.tandfonline.com/doi/full/10.1080/13600869.2026.2654237) — Monaghan et al., International Review of Law, Computers & Technology, 2026. Coins "opacified transparency": the database shows what platforms say they did, but researchers still can't verify whether specific decisions were justified because they can't see the underlying content.
- [Commission harmonises transparency reporting rules under the Digital Services Act](https://digital-strategy.ec.europa.eu/en/news/commission-harmonises-transparency-reporting-rules-under-digital-services-act) — European Commission, 2025. New Implementing Regulation forces machine-readable templates from 1 July 2025; first harmonised reports were published in February 2026, giving the field its first apples-to-apples cross-platform dataset.
<!-- current-events:end -->

**Discussion prompts.**
- Chapter 5.3 documents that X's last comprehensive transparency report was 2017, that Spotify quietly reported 22,000+ Russian requests in a single period with no explanation, and that YouTube aggregates copyright and community-guidelines removals so you can't tell them apart. Is there any voluntary transparency report today you'd trust as ground truth? For what?
- The DSA forces VLOPs to file Statements of Reasons for every moderation action. Early data shows platforms are filing at massive volume — Google Shopping alone generates millions of SoRs. Is that a win (finally, structured data!) or a symptom (dumping so much noise that no one can find the signal)?
- Meta shut down CrowdTangle in August 2024 and replaced it with the more restrictive Content Library. The stated reason was to protect user privacy; researchers say it was to hide election-year data. Under DSA Article 40, vetted researchers are supposed to get access anyway. Are they? What would evidence of success or failure look like?
- Suppose your group is on a congressional staff drafting a US-side DSA-equivalent. Do you (a) copy DSA whole-cloth, (b) require only high-level statistics like the old X reports, (c) require case-level disclosure like the DSA database, or (d) require nothing and rely on FTC enforcement of "unfair and deceptive" claims in existing voluntary reports? Defend the choice.

**Bring back.** One thing your group thinks is *worse* about mandatory transparency than voluntary transparency — even if you support the mandate overall.

---

## Breakout B: Scraping, CFAA, and the Right to Audit
<!-- breakout id="B" status="current" refreshed="2026-07-06" -->

**Motion.** *"Independent researchers — journalists, academics, civil-society auditors — should have a legal right to collect public platform data over a platform's objection, up to and including automated scraping, whenever the research addresses a documented public interest. Platforms should not be able to use the CFAA, ToS, or Meta v. Bright Data-style suits to gate algorithm auditing."*

<!-- current-events:start topic="researcher-platform-data-access" -->
**Prep reads (5–10 min).**
- [If at first you don't succeed: Reflections on a rejected Art. 40 DSA data access request](https://dsa-observatory.eu/2026/03/12/if-at-first-you-dont-succeed-reflections-on-a-rejected-art-40-dsa-data-access-request/) — DSA Observatory, March 2026. Dutch researchers waited 80 working days to have their TikTok/Romanian-election data request rejected on 5 of 7 grounds — a concrete look at what "vetted researcher" access actually means in practice.
- [Meta and TikTok are obstructing researchers' access to data, European Commission rules](https://www.science.org/content/article/meta-and-tiktok-are-obstructing-researchers-access-data) — Science (AAAS), October 2025. Commission's preliminary finding that both VLOPs breached DSA Article 40; in December 2025 X was fined EUR 120M partly for the same failure to allow independent access to public data.
- [The Stakes of "Publicly Accessible": Researchers' Rights to Data under the DSA](https://verfassungsblog.de/dsa-fine-x-research-data/) — Daphne Keller, Verfassungsblog / Tech Policy Press, December 2025. Argues Article 40(12) is the closest thing to a legal right to scrape public platform data, and connects it back to CrowdTangle's shutdown and the failed NYU Ad Observatory model.
- [Court Rules in Favor of Bright Data in Meta v. Bright Data Case](https://brightdata.com/blog/web-data/court-rules-in-favor-of-bright-data-in-meta-v-bright-data-case) — Bright Data, 2024 (still the leading US precedent). Judge Chen held Meta's terms don't reach logged-off scraping of public data; a win for commercial scrapers that researchers now cite in their own defense.
<!-- current-events:end -->

**Discussion prompts.**
- The book cites Google's Transparency Report as the most detailed of the voluntary regime — yet even it aggregates "insufficient information" as the top right-to-be-forgotten category. If platforms won't tell us, and DSA data lags, is scraping the only real audit tool left? Or does that path lead somewhere worse?
- Meta shut down NYU's Ad Observatory in 2021 by disabling researcher accounts and citing ToS. Under the DSA, an EU researcher could theoretically compel access to the same data. Is the right answer to make US law look more like DSA Article 40, or to make ToS violations non-actionable when the researcher is auditing systemic risk? These aren't the same fix.
- Meta v. Bright Data (2024) let a commercial scraper win against Meta on public data. Do you want that precedent to also protect academic researchers? What about journalists? What about a partisan think tank running an "audit" that's really opposition research?
- Chapter 5.3 argues that "visibility does not automatically translate into better moderation outcomes." If researchers get full access tomorrow and find that platforms are moderating in embarrassing ways, what's the enforcement mechanism? Regulators? Advertisers? Users leaving? Which of these has actually worked?

**Bring back.** Your group's answer to: who should be a "vetted researcher"? Give one concrete criterion you'd include and one you'd explicitly reject.

---

## Instructor notes

These breakouts map to Chapter 5.3's core argument — that voluntary transparency is structurally limited — and to the DSA subsection at the end of 5.3 plus the DSA-database material in 5.4. Breakout A tends to draw students who care about regulatory design; Breakout B tends to draw students who care about researcher freedom and CFAA history. If students haven't yet read the ethics section, Breakout B is a natural bridge to it, since it re-raises the "who bears the risk" question in a platform context rather than a probe-volunteer context.

<!--
breakout-metadata:
  lecture: 15
  class: "Measuring Platform Controls"
  book_chapter: "5.3"
  last_refreshed: 2026-07-06
-->
