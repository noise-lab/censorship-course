# Denial of Service

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

The book's [DoS](https://en.wikipedia.org/wiki/Denial-of-service_attack) section is unusually blunt about two things: (1) DoS is not just an attack, it is a *censorship* mechanism when directed at journalists or activists (see the [Great Cannon](https://en.wikipedia.org/wiki/Great_Cannon) vs. [GreatFire](https://en.greatfire.org/) on GitHub); and (2) the defense — [Cloudflare](https://www.cloudflare.com/), Akamai, [Project Galileo](https://www.cloudflare.com/galileo/) — has quietly created a private arbitration system for who deserves to stay online. Both breakouts push on the political economy of DDoS: who launches, who defends, who decides.

---

## Breakout A: Booters, Takedowns, and the Definition of Speech
<!-- breakout id="A" status="current" refreshed="2026-07-06" -->

**Motion.** *"Law-enforcement takedowns of DDoS-for-hire ('booter') services are pure infrastructure hygiene and have no meaningful censorship dimension."*

<!-- current-events:start topic="booter-service-takedowns-ddos-for-hire" -->
**Prep reads (5–10 min).**
- [Operation PowerOFF Seizes 53 DDoS Domains, Exposes 3 Million Criminal Accounts](https://thehackernews.com/2026/04/operation-poweroff-seizes-53-ddos.html) — The Hacker News, April 2026. 21-country action week: 53 domains seized, 4 arrests, 75,000 warning messages sent to identified users.
- [Four arrested in latest 'PowerOFF' DDoS-for-hire takedown](https://therecord.media/ddos-hire-europol-doj-crackdown) — The Record, 2026. DOJ court documents describe an FBI undercover buy: $45/month for 40-minute attacks on three victim IPs.
- [Aisuru botnet sets new record with 31.4 Tbps DDoS attack](https://www.bleepingcomputer.com/news/security/aisuru-botnet-sets-new-record-with-314-tbps-ddos-attack/) — BleepingComputer, February 2026. The Mirai-descendant Aisuru/Kimwolf botnet, 1–4M compromised IoT devices, sets a new world record in December 2025.
- [2025 Q4 DDoS threat report](https://blog.cloudflare.com/ddos-threat-report-2025-q4/) — Cloudflare, February 2026. 47.1M total attacks in 2025 (+121% YoY); the "Night Before Christmas" campaign of 902 hyper-volumetric attacks over ~17 days.
<!-- current-events:end -->

**Discussion prompts.**
- The book opens with [Mafiaboy (2000)](https://en.wikipedia.org/wiki/MafiaBoy) and [Mirai/Dyn (2016)](https://en.wikipedia.org/wiki/2016_Dyn_cyberattack) as canonical DDoS events. Both were criminal, both took down speech infrastructure (CNN, Twitter, Reddit). Is a law-enforcement takedown of the *tools* used for such attacks censorship, ordinary law enforcement, or both?
- Some booter operators have argued in court that their services are "stress-testing tools" and shutting them down chills legitimate security research. Is there a principled line between a stresser and a DDoS-for-hire service? Who gets to draw it?
- Booter takedowns typically involve seizing domains and hosting — the same techniques used to seize dissident-run sites in other countries. Do the ends justify identical means, or do the means need separate scrutiny?
- Chapter 1 defined information control broadly, beyond intent-based censorship. If a takedown of a "legitimate" security-testing service also removes a tool that activists were using to test their own infrastructure, does that count? Does the FBI owe anyone an impact assessment?

**Bring back.** Your group's proposed test for when a DDoS-tool takedown crosses from "law enforcement" into "collateral censorship."

---

## Breakout B: Cloudflare as the Unelected Speech Arbiter
<!-- breakout id="B" status="current" refreshed="2026-07-06" -->

**Motion.** *"Cloudflare's decisions to drop [Daily Stormer](https://en.wikipedia.org/wiki/The_Daily_Stormer), [8chan](https://en.wikipedia.org/wiki/8chan), and [Kiwi Farms](https://en.wikipedia.org/wiki/Kiwi_Farms) proved that DDoS-protection providers cannot be neutral — and Project Galileo confirms they have already picked a side. That should be recognized in law, not left to CEO discretion."*

<!-- current-events:start topic="cloudflare-deplatforming-project-galileo" -->
**Prep reads (5–10 min).**
- [Celebrating 12 years of Project Galileo](https://blog.cloudflare.com/celebrating-12-years-of-project-galileo/) — Cloudflare, 2026. 2,900+ protected properties, 38.5B malicious requests blocked Feb 2025–Jan 2026, and attacks on civil society lasting days rather than the usual minutes.
- [Cyberattacks on Civil Society Hit 7 Times the Rate of Other Websites, Cloudflare Finds](https://www.techtimes.com/articles/318735/20260620/cyberattacks-civil-society-hit-7-times-rate-other-websites-cloudflare-finds.htm) — TechTimes, June 2026. Journalists in exile face 4x the malicious traffic of other journalism orgs; DDoS is 81.7% of the volume.
- [Cutting a Hydra's Head: Infrastructure-Level Content Moderation and the Case of Kiwi Farms](https://gnet-research.org/2025/12/23/cutting-a-hydras-head-infrastructure-level-content-moderation-and-the-case-of-kiwi-farms/) — GNET, December 2025. Kiwi Farms stayed online during the November 2025 Cloudflare outage — a determined adversary built a stack that no longer needs any single intermediary.
- [Italy Fines Cloudflare €14 Million for Refusing to Block Pirate Sites](https://torrentfreak.com/italy-fines-cloudflare-e14-million-for-refusing-to-filter-pirate-sites-on-public-1-1-1-1-dns/) — TorrentFreak, January 2026. Matthew Prince's 2026 framing: the same discretion he used to drop Kiwi Farms, he now refuses to use for Italian rightsholders — is that consistency or contradiction?
<!-- current-events:end -->

**Discussion prompts.**
- The book describes Project Galileo as delegating protection eligibility to civil-society partners (ACLU, EFF, Amnesty, ADL). That's a deliberate outsource of judgment. Is that a legitimate governance model, an abdication, or a laundering operation?
- Matthew Prince's 2017 line — quoted in the Lecture 1 breakouts — was that he shouldn't have the power he had. In 2019 (8chan) and 2022 (Kiwi Farms) he used it anyway. Is the right response (a) common-carrier regulation forbidding him from ever using it again, (b) formal governance structures at Cloudflare, (c) accepting his discretion because the alternative is worse, or (d) breaking up Cloudflare?
- Without Cloudflare-level protection, a small site facing a Mirai-scale attack is effectively offline. The book calls this "asymmetry" — attackers pay pennies, defenders pay millions. Does that asymmetry create a *positive obligation* on DDoS-protection providers to serve everyone, the way we treat electricity or water?
- The Great Cannon (2015) used the Great Firewall to *attack* GitHub. If a Western democracy did the same thing tomorrow — used its national firewall to DDoS a foreign disinformation site — would that be legitimate? What if it were a criminal marketplace instead?

**Bring back.** Whether your group would treat DDoS protection as a common carrier obligation, and one edge case that would break your rule.

---

## Instructor notes

These map to §2.3.2's coverage of Mirai/Dyn, the Great Cannon, and (importantly) the Project Galileo material that closes the section. Breakout A is technically grounded and works well right after the amplification/reflection material — students can debate the takedown while the SYN-cookie and DNS-amp mechanics are still fresh. Breakout B is the more consequential one for the arc of the course: it previews the platform-power and infrastructure-consolidation themes of later chapters. If you have room for only one, run B; it produces the strongest report-backs and connects most cleanly to the Chapter 1 Cloudflare-outage breakout.

<!--
breakout-metadata:
  lecture: 6
  class: "Denial of Service"
  book_chapter: "2.3.2"
  last_refreshed: 2026-07-06
-->
