# Measuring Technical Controls

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

Chapter 5.2 argues that measurement is hard precisely because censorship is hidden, intermittent, and hyper-localized — and every vantage-point choice trades off representativeness against risk to the humans on whose networks the probes run. Both breakouts today press on that tradeoff.

---

## Breakout A: Consent, Coercion, and the OONI Probe on Your Phone
<!-- breakout id="A" status="current" refreshed="2026-07-06" -->

**Motion.** *"Distributing censorship-measurement software ([OONI Probe](https://ooni.org/), VPN reachability testers, side-channel probes) to volunteers in repressive jurisdictions is ethical only if the researchers can guarantee the probe's traffic is legally indistinguishable from ordinary browsing — otherwise informed consent alone is not enough."*

<!-- current-events:start topic="ooni-probe-volunteer-risk" -->
**Prep reads (5–10 min).**
- [Search and be fined: New Russian law targets VPN usage and mere access to "extremist" content](https://en.zona.media/article/2025/07/15/searchban) — Mediazona, July 2025. Russia's September 2025 law criminalizes even searching for "extremist" content via a VPN — a threat model that turns any censorship probe running from a volunteer's device into potential evidence.
- [Russia: Digital Iron Curtain Falls on Internet Freedom Protection Day](https://www.hrw.org/news/2026/03/12/russia-digital-iron-curtain-falls-on-internet-freedom-protection-day) — Human Rights Watch, March 2026. HRW's overview of Russia's 2026 escalation: TSPU deep-packet inspection, 469+ blocked VPN services, and FSB-linked crackdowns tied to the "Scarlet Swan" anti-censorship movement.
- [Internet Censorship in Iran: Trends and Outlook for 2026](https://amnezia.org/blog/internet-censorship-in-iran-q1-2026-and-forecast) — Amnezia, 2026. Post-January-2026 Iranian filtering with Russian technical assistance; warns that unsafe VPN configurations put users at direct prosecution risk.
- [Russia blocked OONI Explorer, a large open dataset on Internet censorship](https://ooni.org/post/2024-russia-blocked-ooni-explorer) — OONI, September 2024 (with 2026 update). Roskomnadzor blocked, then partially unblocked, the platform where volunteer measurements are published — the same data trail that a prosecutor could subpoena.
<!-- current-events:end -->

**Discussion prompts.**
- The book's "paradox of consent" argument: an explicit consent form creates documentary evidence of intent to test censored URLs, which may make the user *more* prosecutable than a silent background probe. Do you buy it? Under what threat model does it fail?
- OONI's web-connectivity test hits a curated list that includes political, LGBTQ, and religious content. In a country where accessing that content is criminalized, is running the test a form of civil disobedience *by the volunteer*, or a risk that researchers offloaded onto them? Who owes whom a duty of care?
- [Censored Planet](https://censoredplanet.org/)'s side-channel measurements (idle scan, [Encore](https://en.wikipedia.org/wiki/Encore_(software))-style cross-origin requests) can measure blocking *without* a local volunteer at all — they turn ordinary infrastructure hosts into unwitting reflectors. Is this actually more ethical (no volunteer at greater risk than they already were) or less (no one consented, period)?
- Suppose an OONI volunteer is arrested and the local NGO asks the OONI team to pull all recent measurements from that ISP off the public Explorer. Should they? Does the answer change if a court has subpoenaed the data?

**Bring back.** Your group's minimum ethical bar for shipping a censorship probe to volunteers in a [Freedom-on-the-Net](https://freedomhouse.org/report/freedom-net) "Not Free" country — one concrete requirement, and one thing you decided *not* to require and why.

---

## Breakout B: The Right to a Blocklist
<!-- breakout id="B" status="current" refreshed="2026-07-06" -->

**Motion.** *"Governments that filter Internet traffic should be legally required to publish, in machine-readable form, the current list of blocked domains and the legal authority for each entry — the way [Turkey](https://en.wikipedia.org/wiki/Internet_censorship_in_Turkey) has at times done, and the way Germany's [NetzDG](https://en.wikipedia.org/wiki/Network_Enforcement_Act) orders are logged."*

<!-- current-events:start topic="government-blocklist-disclosure" -->
**Prep reads (5–10 min).**
- [Russia's internet censorship in 2026: VPN crackdowns, mobile shutdowns, Telegram blocks and the state messenger Max](https://en.zona.media/article/2026/04/07/russian_internet_censorship_2026) — Mediazona, April 2026. Documents how Roskomnadzor uses TSPU deep-packet inspection under the "Sovereign Internet" law to filter opaquely, with no public list of what's blocked and providers themselves prosecuted when traffic slips through.
- [Throttling of Social Media in Türkiye During Protests: An Analysis of OONI Data](https://ooni.org/post/2025-turkiye-throttling-social-media/) — OONI, November 2025. Filtering events Turkish authorities never officially confirmed, reconstructed from probe measurements — exactly the gap a disclosure mandate would close (or paper over).
- [Rising repression meets global resistance: Internet shutdowns in 2025](https://www.accessnow.org/wp-content/uploads/2026/03/KeepItOn-Internet-Shutdowns-2025-Annual-Report.pdf) — Access Now / #KeepItOn, March 2026. 313 shutdowns across 52 countries in 2025 — most imposed with no legal authority cited, no target list published, and no post-hoc accountability.
- [Russia appears to block social media platform Bluesky amid wider internet restrictions](https://therecord.media/russia-cracks-down-bluesky-internet) — The Record (Recorded Future News), April 2026. Roskomnadzor added Bluesky to its registry of banned sites with no public explanation; the block was only surfaced by third-party OONI measurements and RKS Global — illustrating what mandatory disclosure would (and would not) reveal.
<!-- current-events:end -->

**Discussion prompts.**
- If a censor must publish its blocklist, we no longer need indirect measurement (idle scan, Encore, DNS consistency checks) to reconstruct it. Does mandatory disclosure make the whole field of technical measurement obsolete — or just shift what it's measuring? What would OONI's job become?
- The counter-argument: publishing a blocklist is a *sales catalog* for circumvention. If Russia's Roskomnadzor publishes the list, every VPN and Tor bridge operator can prioritize what to unblock next. Is this a bug or a feature?
- Democratic countries do this too, sort of. UK ISPs run the [Internet Watch Foundation](https://en.wikipedia.org/wiki/Internet_Watch_Foundation) list; Germany logs NetzDG takedowns; the EU's [DSA Transparency Database](https://transparency.dsa.ec.europa.eu/) records SoRs. Are these actually comparable to a state blocklist, or is the equivalence a rhetorical trick?
- Chapter 5.2's DNS-manipulation section shows that even careful researchers struggle to distinguish blocking from misconfiguration or CDN behavior. Would mandatory disclosure by governments actually reduce that ambiguity, or would governments just get better at plausibly-deniable filtering (throttling, injecting RSTs, "network errors") that the disclosure regime doesn't cover?

**Bring back.** A one-sentence rule for what a blocklist-disclosure law should require, plus one specific loophole your group predicts governments would exploit.

---

## Instructor notes

These breakouts map to the section takeaways on vantage-point tradeoffs (5.2.1–5.2.3) and to the ethics chapter (5.5) — specifically the "paradox of consent" and "co-opted devices" arguments. Breakout A tends to produce sharper disagreement (students split on whether consent is a floor or a ceiling); Breakout B tends to surface the tension between measurement researchers (who benefit from opacity being expensive) and civil-society groups (who benefit from opacity being illegal). If time is tight, A is the more directly technical debate and pairs better with the walkthrough in section 5.2.

<!--
breakout-metadata:
  lecture: 14
  class: "Measuring Technical Controls"
  book_chapter: "5.2"
  last_refreshed: 2026-07-06
-->
