# BGP and Web Manipulation

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

The book's [BGP](https://en.wikipedia.org/wiki/Border_Gateway_Protocol) section is a parade of accidents that look like attacks ([AS 7007](https://en.wikipedia.org/wiki/AS_7007_incident), [Pakistan Telecom](https://en.wikipedia.org/wiki/BGP_hijacking#Pakistan_vs._YouTube), China Telecom, Facebook 2021) and attacks that look like accidents. The web-manipulation section is quieter but more intimate: block pages tell you exactly who is censoring you. These breakouts push on the two extremes — the coarsest tool (BGP) and the most user-visible one (block pages) — and ask what obligations flow from operating the pipes.

---

## Breakout A: Should Governments Mandate RPKI?
<!-- breakout id="A" status="current" refreshed="2026-07-06" -->

**Motion.** *"National regulators should legally require every ISP operating in their jurisdiction to deploy [RPKI](https://datatracker.ietf.org/doc/html/rfc6480)-based route origin validation, with penalties for non-compliance."*

<!-- current-events:start topic="rpki-bgp-security-mandates" -->
**Prep reads (5–10 min).**
- [FCC Advances BGP Security Rules for Broadband Providers](https://www.bankinfosecurity.com/fcc-advances-bgp-security-rules-for-broadband-providers-a-25476) — BankInfoSecurity, 2024. The FCC's NPRM would require the nine largest US broadband providers to file confidential BGP security plans with ROA goals and timetables.
- [Dissecting the FCC's Proposal to Improve BGP Security](https://www.kentik.com/blog/dissecting-the-fccs-proposal-to-improve-bgp-security/) — Kentik, 2024. Industry-side reading of the proposal, including the Internet Society's argument that regulation risks slowing the industry-led progress it is trying to catalyze.
- [Are We Actually There? Assessing RPKI Maturity](https://cacm.acm.org/research/are-we-actually-there-assessing-rpki-maturity/) — Communications of the ACM, 2025. Recent measurement work showing ROV cuts invalid-route propagation by roughly half to two-thirds — meaningful, but not a universal block.
- [RPKI vs social engineering: A case study in route hijacking](https://blog.lacnic.net/en/rpki-vs-social-engineering-a-case-study-in-route-hijacking/) — LACNIC, 2026. July 2025 hijack that bypassed RPKI entirely by exploiting weak identity verification during customer onboarding — a reminder that crypto only covers the parts it covers.
<!-- current-events:end -->

**Discussion prompts.**
- The book documents recurring BGP disasters from AS 7007 (1997) through Facebook's 2021 self-outage. RPKI has existed for over a decade and adoption is still partial. Is this a market failure that regulation can fix, or does mandated crypto make things worse (misconfiguration bricking routes, single points of failure in trust anchors)?
- RPKI's trust anchors are the five Regional Internet Registries. In a mandated deployment, a court order to RIPE or ARIN could invalidate an entire country's routes. Is this better or worse than the status quo, where BGP hijacks happen by accident every few months?
- The Pakistan Telecom / YouTube case (2008) was censorship that *leaked globally*. If RPKI had been widely deployed, YouTube's `/22` would have been protected — and Pakistan's domestic block would presumably have failed too. Is "RPKI stops censors from hijacking their own citizens' routes" a feature or a bug from the censor's perspective? From ours?
- Should the mandate distinguish between origin validation (RPKI ROV) and full path validation (BGPsec, which has essentially zero deployment)? Where is the right cost/benefit line?

**Bring back.** Whether your group would support such a mandate in your own country, and what one carve-out or safeguard is non-negotiable.

---

## Breakout B: Kill-Switch Orders and ISP Refusal
<!-- breakout id="B" status="current" refreshed="2026-07-06" -->

**Motion.** *"ISPs served with a government order to withdraw BGP routes or block major services should refuse — even at the cost of their operating license."*

<!-- current-events:start topic="internet-shutdowns-isp-refusal" -->
**Prep reads (5–10 min).**
- [When repression meets resistance: internet shutdowns in 2025](https://www.accessnow.org/internet-shutdowns-2025/) — Access Now / #KeepItOn, March 2026. 313 shutdowns in 52 countries in 2025 — the worst year on record — with Myanmar (95), India (65), Pakistan (20), and Iran (11) leading.
- [Iran: Internet Shutdown Violates Rights, Escalates Risks to Civilians](https://www.hrw.org/news/2026/03/06/iran-internet-shutdown-violates-rights-escalates-risks-to-civilians) — Human Rights Watch, March 2026. The January 2026 21-day blackout under cover of a mass protest crackdown; Iran's telecom minister acknowledged the cost at $35.7M/day.
- [Iran: Internet shutdown hides violations in escalating deadly crackdown on protesters](https://www.amnesty.org/en/latest/news/2026/01/internet-shutdown-in-iran-hides-violations-in-escalating-protests/) — Amnesty International, January 2026. The framing that shutdowns are not just a rights violation *in service of* atrocities but a rights violation *in themselves*.
- [Government Internet Shutdowns Cost $19.7B in 2025](https://www.top10vpn.com/research/cost-of-internet-shutdowns/) — Top10VPN / NetBlocks data, 2026. Russia leads the cost-by-country table, driven by sustained throttling of Cloudflare, YouTube, and messaging apps rather than one-shot blackouts.
<!-- current-events:end -->

**Discussion prompts.**
- The book's [Egypt example (Jan 2011)](https://en.wikipedia.org/wiki/2011_Egyptian_Internet_shutdown) required only a handful of ISPs to withdraw about 3,500 BGP routes — 88% of Egyptian networks disappeared from the global routing table in minutes. If a single ISP had refused, would it have mattered? What would have happened to that ISP?
- India has shut down the Internet in Kashmir over 180 times since 2012, through licensed carriers who comply. Is compliance under license conditions morally different from Vodafone's compliance in Egypt? Is there a coherent line between "operating under local law" and "complicity in repression"?
- Some multinational telecoms (Vodafone, MTN, Orange) have published transparency reports about shutdown orders they received. Is transparency without refusal just laundering complicity, or is it a step on the ladder?
- Compare a BGP-based shutdown (Egypt-style) to a BART-style cell-service disable (Chapter 1, San Francisco 2011). The mechanisms differ; the effect is similar. Should the *ethical duty to refuse* be the same in both cases?

**Bring back.** The circumstances (if any) under which your group thinks an ISP is *obligated* to refuse a shutdown order, and how you'd operationalize that.

---

## Instructor notes

These map to §2.2.3's "all-or-nothing" characterization of BGP as a censorship tool and the Egypt/Pakistan case studies, plus the §2.2.4 point that block pages make censorship user-visible. Breakout A is the more technical debate; Breakout B is the more moral one. If the class has been engaging well with the "who gets to pull the lever" thread from Lecture 1, B lands with more force. If the class is technically inclined and has just read the RPKI/[MANRS](https://www.manrs.org/) material, A is the better bet. Either way, the Pakistan Telecom hack (advertising /25s to reclaim traffic) is worth putting on the board — it's a great concrete illustration of how ad hoc BGP defense really is.

<!--
breakout-metadata:
  lecture: 4
  class: "BGP and Web Manipulation"
  book_chapter: "2.2.3-2.2.4"
  last_refreshed: 2026-07-06
-->
