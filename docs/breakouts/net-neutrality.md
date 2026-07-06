---
lecture: 12
class: "Net Neutrality"
book_chapter: "4.3"
last_refreshed: 2026-07-06
---

# Breakout Discussions — Lecture 12: Net Neutrality

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

Chapter 4.3 argues that net neutrality is fundamentally about whether ISPs can discriminate among content sources — via blocking, throttling, or paid prioritization — and that each of those levers is a soft form of information control. But it also argues that market incentives have shifted: today's most acute threats to open access have moved *up the stack*, to platforms, CDNs, and cloud hosts. Both breakouts push on that tension.

---

## Breakout A: Common Carrier or Not — Is Title II Still the Right Frame?
<!-- breakout id="A" status="stub" refreshed="2026-07-06" -->

**Motion.** *"Broadband ISPs should be classified as Title II common carriers and regulated like utilities — the 2015 Open Internet Order was correct, and every repeal since has been a mistake."*

<!-- current-events:start topic="net-neutrality-title-ii" -->
**Prep reads (5–10 min).**
- *[Placeholder — refresh skill will populate with the most recent FCC action on broadband classification (reinstatement, repeal, court challenges to the 2024 Open Internet Order, or state-level equivalents like California's SB 822).]*
- *[Placeholder — recent story on ISP blocking / throttling incidents, ISP-vs-content-provider peering disputes, or empirical net-neutrality measurement studies documenting differential treatment of traffic.]*
<!-- current-events:end -->

**Discussion prompts.**
- The FCC has now flipped Title II three times (2015 on, 2017 off, 2024 on, and probably again by the time you read this). Is that instability an argument for congressional action, an argument that the rule doesn't matter much in practice, or an argument that the FCC is the wrong regulator entirely?
- The 2014 Netflix–Comcast dispute was framed in the press as a net-neutrality violation, but the book argues it was a classic peering dispute — an economic disagreement between transit provider (Cogent) and access ISP (Comcast). If you can't reliably distinguish "congestion from underprovisioned interconnects" from "throttling for competitive advantage," what does that do to the enforceability of Title II?
- The book claims market incentives have realigned: Comcast now *needs* Netflix to work well because subscribers demand it. If that's true, is Title II solving a 2014 problem in a 2026 market? Or is the whole point of common-carrier rules to constrain future misbehavior when incentives shift back?
- Rural fixed-wireless, satellite (Starlink), and 5G home Internet don't look much like the DOCSIS cable plant Title II was written around. Should classification depend on the *service* (broadband) or the *infrastructure* (cable vs. wireless vs. LEO)?

**Bring back.** Your group's one-sentence rule you would actually write into statute — not FCC order — to bind future administrations.

---

## Breakout B: 5G Network Slicing and the "Specialized Services" Loophole
<!-- breakout id="B" status="stub" refreshed="2026-07-06" -->

**Motion.** *"5G network slicing and 'specialized services' carve-outs are incompatible with net neutrality in practice — they are paid prioritization by another name."*

<!-- current-events:start topic="5g-network-slicing" -->
**Prep reads (5–10 min).**
- *[Placeholder — refresh skill will populate with a recent story on 5G / 6G network slicing deployments by U.S. or EU carriers, enterprise slicing offerings, or slicing tied to specific applications (gaming, AR/VR, cloud services).]*
- *[Placeholder — recent regulator statement (FCC, BEREC, Ofcom) on how "specialized services" or "reasonable network management" exceptions interact with slicing, or academic measurement of differential treatment on 5G networks.]*
<!-- current-events:end -->

**Discussion prompts.**
- Network slicing lets a carrier sell a dedicated logical slice — guaranteed latency, guaranteed bandwidth — to a particular app or customer. The book notes it has always been fine to prioritize all video over all bulk transfer; the bright-line rules only prohibit prioritizing *FaceTime over Skype*. Does slicing cross that line? Does the answer depend on who buys the slice — Netflix, John Deere, a hospital, or the local police?
- The 2015 order preserved "reasonable network management practices" — an exception the book says is famously hard to define. Slicing vendors argue it is just an efficient form of network management. Where does management end and discrimination begin? Give a technical test, not a legal one.
- If a carrier sells a "gaming slice" to Fortnite and not to Roblox, is that different from zero-rating Fortnite? (Yes, Lecture 13 is next week, but the mechanisms rhyme.) Is the harm to *users*, to *competitors*, or to *the network* as a shared resource?
- The book argues that the acute threats have moved up the stack — to CDNs, clouds, and platforms. If Cloudflare and AWS can already prioritize (or drop) whoever they want, does bright-line neutrality *at the ISP layer* still buy you anything? Or is it fighting the last war?

**Bring back.** Your group's proposed definition — in one sentence — of the line between "specialized service" (allowed) and "paid prioritization" (not).

---

## Instructor notes

These breakouts map to Section 4.3's takeaways that (1) blocking/throttling/paid-prioritization are the three levers of ISP-layer information control and (2) the threats have shifted up the stack. Breakout A tends to attract the students who want a clean regulatory answer; Breakout B tends to attract the students who read the technical primer and want to argue about QoS. If the group polarizes too fast on A, push them with the peering-dispute detail from Section 4.3 — most students will not have the distinction between "congestion at an IXP" and "throttling by an ISP" straight, and it usefully complicates the debate. Breakout B sets up Lecture 13 (zero rating) cleanly.
