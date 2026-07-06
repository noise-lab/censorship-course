---
lecture: 6
class: "Denial of Service"
book_chapter: "2.3.2"
last_refreshed: 2026-07-06
---

# Breakout Discussions — Lecture 6: Denial of Service

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

The book's DoS section is unusually blunt about two things: (1) DoS is not just an attack, it is a *censorship* mechanism when directed at journalists or activists (see the Great Cannon vs. GreatFire on GitHub); and (2) the defense — Cloudflare, Akamai, Project Galileo — has quietly created a private arbitration system for who deserves to stay online. Both breakouts push on the political economy of DDoS: who launches, who defends, who decides.

---

## Breakout A: Booters, Takedowns, and the Definition of Speech
<!-- breakout id="A" status="stub" refreshed="2026-07-06" -->

**Motion.** *"Law-enforcement takedowns of DDoS-for-hire ('booter') services are pure infrastructure hygiene and have no meaningful censorship dimension."*

<!-- current-events:start topic="booter-service-takedowns-ddos-for-hire" -->
**Prep reads (5–10 min).**
- *[Placeholder — refresh skill will populate with recent news on: FBI, Europol, or NCA takedowns of booter/stresser services (Operation PowerOFF and similar), including domain seizures and arrests]*
- *[Placeholder — recent event or report on: academic studies of booter customer bases, or research on Mirai-variant botnets, IoT compromises, or amplification attacks (memcached, DNS, NTP)]*
<!-- current-events:end -->

**Discussion prompts.**
- The book opens with Mafiaboy (2000) and Mirai/Dyn (2016) as canonical DDoS events. Both were criminal, both took down speech infrastructure (CNN, Twitter, Reddit). Is a law-enforcement takedown of the *tools* used for such attacks censorship, ordinary law enforcement, or both?
- Some booter operators have argued in court that their services are "stress-testing tools" and shutting them down chills legitimate security research. Is there a principled line between a stresser and a DDoS-for-hire service? Who gets to draw it?
- Booter takedowns typically involve seizing domains and hosting — the same techniques used to seize dissident-run sites in other countries. Do the ends justify identical means, or do the means need separate scrutiny?
- Chapter 1 defined information control broadly, beyond intent-based censorship. If a takedown of a "legitimate" security-testing service also removes a tool that activists were using to test their own infrastructure, does that count? Does the FBI owe anyone an impact assessment?

**Bring back.** Your group's proposed test for when a DDoS-tool takedown crosses from "law enforcement" into "collateral censorship."

---

## Breakout B: Cloudflare as the Unelected Speech Arbiter
<!-- breakout id="B" status="stub" refreshed="2026-07-06" -->

**Motion.** *"Cloudflare's decisions to drop Daily Stormer, 8chan, and Kiwi Farms proved that DDoS-protection providers cannot be neutral — and Project Galileo confirms they have already picked a side. That should be recognized in law, not left to CEO discretion."*

<!-- current-events:start topic="cloudflare-deplatforming-project-galileo" -->
**Prep reads (5–10 min).**
- *[Placeholder — refresh skill will populate with recent news on: Cloudflare, Akamai, or Fastly decisions to drop or protect controversial sites; Project Galileo eligibility disputes; or CEO Matthew Prince's statements on infrastructure-layer moderation]*
- *[Placeholder — recent event or report on: sites forced offline by loss of DDoS protection, or academic/legal analyses of infrastructure-provider moderation (Section 230, DSA intermediary-liability rules, common-carrier arguments)]*
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
