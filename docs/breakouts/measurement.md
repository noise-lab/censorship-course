---
lecture: 14
class: "Measuring Technical Controls"
book_chapter: "5.2"
last_refreshed: 2026-07-06
---

# Breakout Discussions — Lecture 14: Measuring Technical Controls

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

Chapter 5.2 argues that measurement is hard precisely because censorship is hidden, intermittent, and hyper-localized — and every vantage-point choice trades off representativeness against risk to the humans on whose networks the probes run. Both breakouts today press on that tradeoff.

---

## Breakout A: Consent, Coercion, and the OONI Probe on Your Phone
<!-- breakout id="A" status="stub" refreshed="2026-07-06" -->

**Motion.** *"Distributing censorship-measurement software (OONI Probe, VPN reachability testers, side-channel probes) to volunteers in repressive jurisdictions is ethical only if the researchers can guarantee the probe's traffic is legally indistinguishable from ordinary browsing — otherwise informed consent alone is not enough."*

<!-- current-events:start topic="ooni-probe-volunteer-risk" -->
**Prep reads (5–10 min).**
- *[Placeholder — refresh skill will populate with recent news on: arrests, detentions, or prosecutions of users who ran OONI Probe, VPNs, or other network-measurement tools, particularly in Iran, Russia, Belarus, or China.]*
- *[Placeholder — recent OONI, Censored Planet, or ICLab writeup on methodology changes, deployment tradeoffs, or ethics disclosures for volunteer-based measurement.]*
<!-- current-events:end -->

**Discussion prompts.**
- The book's "paradox of consent" argument: an explicit consent form creates documentary evidence of intent to test censored URLs, which may make the user *more* prosecutable than a silent background probe. Do you buy it? Under what threat model does it fail?
- OONI's web-connectivity test hits a curated list that includes political, LGBTQ, and religious content. In a country where accessing that content is criminalized, is running the test a form of civil disobedience *by the volunteer*, or a risk that researchers offloaded onto them? Who owes whom a duty of care?
- Censored Planet's side-channel measurements (idle scan, Encore-style cross-origin requests) can measure blocking *without* a local volunteer at all — they turn ordinary infrastructure hosts into unwitting reflectors. Is this actually more ethical (no volunteer at greater risk than they already were) or less (no one consented, period)?
- Suppose an OONI volunteer is arrested and the local NGO asks the OONI team to pull all recent measurements from that ISP off the public Explorer. Should they? Does the answer change if a court has subpoenaed the data?

**Bring back.** Your group's minimum ethical bar for shipping a censorship probe to volunteers in a Freedom-on-the-Net "Not Free" country — one concrete requirement, and one thing you decided *not* to require and why.

---

## Breakout B: The Right to a Blocklist
<!-- breakout id="B" status="stub" refreshed="2026-07-06" -->

**Motion.** *"Governments that filter Internet traffic should be legally required to publish, in machine-readable form, the current list of blocked domains and the legal authority for each entry — the way Turkey has at times done, and the way Germany's NetzDG orders are logged."*

<!-- current-events:start topic="government-blocklist-disclosure" -->
**Prep reads (5–10 min).**
- *[Placeholder — refresh skill will populate with recent news on: government transparency around blocklists, court orders forcing disclosure of blocked-site lists, or FOIA/leaked blocklists in Turkey, India, Russia, Pakistan, or the UK Online Safety Act context.]*
- *[Placeholder — recent OONI, Access Now KeepItOn, or Citizen Lab report documenting a filtering event where the government refused to confirm what was blocked or why.]*
<!-- current-events:end -->

**Discussion prompts.**
- If a censor must publish its blocklist, we no longer need indirect measurement (idle scan, Encore, DNS consistency checks) to reconstruct it. Does mandatory disclosure make the whole field of technical measurement obsolete — or just shift what it's measuring? What would OONI's job become?
- The counter-argument: publishing a blocklist is a *sales catalog* for circumvention. If Russia's Roskomnadzor publishes the list, every VPN and Tor bridge operator can prioritize what to unblock next. Is this a bug or a feature?
- Democratic countries do this too, sort of. UK ISPs run the Internet Watch Foundation list; Germany logs NetzDG takedowns; the EU's DSA Transparency Database records SoRs. Are these actually comparable to a state blocklist, or is the equivalence a rhetorical trick?
- Chapter 5.2's DNS-manipulation section shows that even careful researchers struggle to distinguish blocking from misconfiguration or CDN behavior. Would mandatory disclosure by governments actually reduce that ambiguity, or would governments just get better at plausibly-deniable filtering (throttling, injecting RSTs, "network errors") that the disclosure regime doesn't cover?

**Bring back.** A one-sentence rule for what a blocklist-disclosure law should require, plus one specific loophole your group predicts governments would exploit.

---

## Instructor notes

These breakouts map to the section takeaways on vantage-point tradeoffs (5.2.1–5.2.3) and to the ethics chapter (5.5) — specifically the "paradox of consent" and "co-opted devices" arguments. Breakout A tends to produce sharper disagreement (students split on whether consent is a floor or a ceiling); Breakout B tends to surface the tension between measurement researchers (who benefit from opacity being expensive) and civil-society groups (who benefit from opacity being illegal). If time is tight, A is the more directly technical debate and pairs better with the walkthrough in section 5.2.
