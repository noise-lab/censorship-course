# Net Neutrality

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

Chapter 4.3 argues that [net neutrality](https://en.wikipedia.org/wiki/Net_neutrality) is fundamentally about whether ISPs can discriminate among content sources — via blocking, throttling, or [paid prioritization](https://en.wikipedia.org/wiki/Net_neutrality#Paid_prioritization) — and that each of those levers is a soft form of information control. But it also argues that market incentives have shifted: today's most acute threats to open access have moved *up the stack*, to platforms, CDNs, and cloud hosts. Both breakouts push on that tension.

---

## Breakout A: Common Carrier or Not — Is Title II Still the Right Frame?
<!-- breakout id="A" status="current" refreshed="2026-07-06" -->

**Motion.** *"Broadband ISPs should be classified as [Title II common carriers](https://en.wikipedia.org/wiki/Common_carrier) and regulated like utilities — the 2015 Open Internet Order was correct, and every repeal since has been a mistake."*

<!-- current-events:start topic="net-neutrality-title-ii" -->
**Prep reads (5–10 min).**
- [Ohio Telecom Ass'n v. FCC (Sixth Circuit opinion)](https://law.justia.com/cases/federal/appellate-courts/ca6/24-3449/24-3449-2025-01-02.html) — U.S. Court of Appeals for the Sixth Circuit, 2 January 2025. The opinion itself: unanimously vacates the 2024 Safeguarding Order, holding broadband is an "information service" and the FCC lacks statutory authority for Title II reclassification post-*Loper Bright*.
- [No More Deference: Sixth Circuit Relies on Loper Bright to Strike Down Net Neutrality Rules](https://www.congress.gov/crs-product/LSB11264) — Congressional Research Service, 2025. CRS's plain-English explainer of how *Loper Bright* and the *Brand X* precedent interact with the ruling.
- [Sixth Circuit Ruling on FCC Authority Threatens Consumer Protections and Open Internet](https://publicknowledge.org/sixth-circuit-ruling-on-fcc-authority-threatens-consumer-protections-and-open-internet/) — Public Knowledge, January 2025. Advocacy-side reaction, and the pivot to state-level rules as the remaining vehicle.
- [Recent Federal Actions Open the Door for Affordable and Reliable State Broadband Regulation](https://www.publicadvocates.cpuc.ca.gov/press-room/commentary/250218-federal-actions-open-door-for-affordable-state-broadband-regulation) — CPUC Public Advocates Office, February 2025. California's read: the Sixth Circuit ruling actually strengthens the state case for enforcing SB 822 and follow-on affordability rules.
<!-- current-events:end -->

**Discussion prompts.**
- The [FCC](https://www.fcc.gov/) has now flipped Title II three times (2015 on, 2017 off, 2024 on, and probably again by the time you read this — see [*Ohio Telecom Ass'n v. FCC*](https://law.justia.com/cases/federal/appellate-courts/ca6/24-3449/24-3449-2025-01-02.html) and [*Loper Bright v. Raimondo*](https://en.wikipedia.org/wiki/Loper_Bright_Enterprises_v._Raimondo)). Is that instability an argument for congressional action, an argument that the rule doesn't matter much in practice, or an argument that the FCC is the wrong regulator entirely?
- The [2014 Netflix–Comcast dispute](https://en.wikipedia.org/wiki/Comcast_Corp._v._FCC) was framed in the press as a net-neutrality violation, but the book argues it was a classic peering dispute — an economic disagreement between transit provider (Cogent) and access ISP (Comcast). If you can't reliably distinguish "congestion from underprovisioned interconnects" from "throttling for competitive advantage," what does that do to the enforceability of Title II?
- The book claims market incentives have realigned: Comcast now *needs* Netflix to work well because subscribers demand it. If that's true, is Title II solving a 2014 problem in a 2026 market? Or is the whole point of common-carrier rules to constrain future misbehavior when incentives shift back?
- Rural fixed-wireless, satellite (Starlink), and 5G home Internet don't look much like the DOCSIS cable plant Title II was written around. Should classification depend on the *service* (broadband) or the *infrastructure* (cable vs. wireless vs. LEO)?

**Bring back.** Your group's one-sentence rule you would actually write into statute — not FCC order — to bind future administrations.

---

## Breakout B: 5G Network Slicing and the "Specialized Services" Loophole
<!-- breakout id="B" status="current" refreshed="2026-07-06" -->

**Motion.** *"[5G network slicing](https://en.wikipedia.org/wiki/Network_slicing) and 'specialized services' carve-outs are incompatible with net neutrality in practice — they are paid prioritization by another name."*

<!-- current-events:start topic="5g-network-slicing" -->
**Prep reads (5–10 min).**
- [BEREC — 5G topic page](https://www.berec.europa.eu/en/all-topics/5g?language_content_entity=en) — Body of European Regulators for Electronic Communications, 2026. BEREC's evolving position: slicing "seems to leave room" under Regulation 2015/2120, with case-by-case determinations left to national regulators.
- [CCIA Europe response to BEREC Call for Input on 5G network slicing](https://ccianet.org/wp-content/uploads/2026/02/CCIA-response-to-BEREC-Call-for-Input-for-further-guidance-on-5G-network-slicing.pdf) — Computer & Communications Industry Association, February 2026. Industry filing arguing slicing is compatible with the Open Internet Regulation "where adequate safeguards" prevent pay-to-prioritize deals with content providers.
- [5G slices are a net neutrality loophole, critics argue](https://www.lightreading.com/regulatory-politics/5g-slices-are-a-net-neutrality-loophole-critics-argue) — Light Reading, 2024. Public-interest critique of slicing as specialized-services relabeling — cites AT&T (gaming), Verizon (video), and T-Mobile (Zoom/Meet) slice trials.
- [Efficiency and Effectiveness of Net Neutrality Rules in the Mobile Sector (Briglauer & Yoo)](https://www.wu.ac.at/fileadmin/wu/d/ri/regulation/WPs_und_GAs/Briglauer_Yoo_February_2025.pdf) — WU Vienna working paper, February 2025. Empirical/economic analysis of mobile net-neutrality regimes and their interaction with 5G quality-of-service tiers.
<!-- current-events:end -->

**Discussion prompts.**
- Network slicing lets a carrier sell a dedicated logical slice — guaranteed latency, guaranteed bandwidth — to a particular app or customer. The book notes it has always been fine to prioritize all video over all bulk transfer; the bright-line rules only prohibit prioritizing *FaceTime over Skype*. Does slicing cross that line? Does the answer depend on who buys the slice — Netflix, John Deere, a hospital, or the local police?
- The 2015 order preserved "reasonable network management practices" — an exception the book says is famously hard to define. Slicing vendors argue it is just an efficient form of network management. Where does management end and discrimination begin? Give a technical test, not a legal one.
- If a carrier sells a "gaming slice" to Fortnite and not to Roblox, is that different from [zero-rating](https://en.wikipedia.org/wiki/Zero-rating) Fortnite? (Yes, Lecture 13 is next week, but the mechanisms rhyme.) Is the harm to *users*, to *competitors*, or to *the network* as a shared resource?
- The book argues that the acute threats have moved up the stack — to CDNs, clouds, and platforms. If Cloudflare and AWS can already prioritize (or drop) whoever they want, does bright-line neutrality *at the ISP layer* still buy you anything? Or is it fighting the last war?

**Bring back.** Your group's proposed definition — in one sentence — of the line between "specialized service" (allowed) and "paid prioritization" (not).

---

## Instructor notes

These breakouts map to Section 4.3's takeaways that (1) blocking/throttling/paid-prioritization are the three levers of ISP-layer information control and (2) the threats have shifted up the stack. Breakout A tends to attract the students who want a clean regulatory answer; Breakout B tends to attract the students who read the technical primer and want to argue about QoS. If the group polarizes too fast on A, push them with the peering-dispute detail from Section 4.3 — most students will not have the distinction between "congestion at an IXP" and "throttling by an ISP" straight, and it usefully complicates the debate. Breakout B sets up Lecture 13 (zero rating) cleanly.

<!--
breakout-metadata:
  lecture: 12
  class: "Net Neutrality"
  book_chapter: "4.3"
  last_refreshed: 2026-07-06
-->
