---
lecture: 4
class: "BGP and Web Manipulation"
book_chapter: "2.2.3-2.2.4"
last_refreshed: 2026-07-06
---

# Breakout Discussions — Lecture 4: BGP and Web Manipulation

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

The book's BGP section is a parade of accidents that look like attacks (AS 7007, Pakistan Telecom, China Telecom, Facebook 2021) and attacks that look like accidents. The web-manipulation section is quieter but more intimate: block pages tell you exactly who is censoring you. These breakouts push on the two extremes — the coarsest tool (BGP) and the most user-visible one (block pages) — and ask what obligations flow from operating the pipes.

---

## Breakout A: Should Governments Mandate RPKI?
<!-- breakout id="A" status="stub" refreshed="2026-07-06" -->

**Motion.** *"National regulators should legally require every ISP operating in their jurisdiction to deploy RPKI-based route origin validation, with penalties for non-compliance."*

<!-- current-events:start topic="rpki-bgp-security-mandates" -->
**Prep reads (5–10 min).**
- *[Placeholder — refresh skill will populate with recent news on: FCC, EU, or other regulators moving on BGP security mandates; RPKI deployment progress and holdouts; MANRS adoption; or recent high-profile BGP hijacks/leaks with policy implications]*
- *[Placeholder — recent event or report on: BGP incidents in 2024-2026 — Rostelecom, China Telecom repeats, cloud-provider hijacks, or Ukraine/Russia routing manipulation]*
<!-- current-events:end -->

**Discussion prompts.**
- The book documents recurring BGP disasters from AS 7007 (1997) through Facebook's 2021 self-outage. RPKI has existed for over a decade and adoption is still partial. Is this a market failure that regulation can fix, or does mandated crypto make things worse (misconfiguration bricking routes, single points of failure in trust anchors)?
- RPKI's trust anchors are the five Regional Internet Registries. In a mandated deployment, a court order to RIPE or ARIN could invalidate an entire country's routes. Is this better or worse than the status quo, where BGP hijacks happen by accident every few months?
- The Pakistan Telecom / YouTube case (2008) was censorship that *leaked globally*. If RPKI had been widely deployed, YouTube's `/22` would have been protected — and Pakistan's domestic block would presumably have failed too. Is "RPKI stops censors from hijacking their own citizens' routes" a feature or a bug from the censor's perspective? From ours?
- Should the mandate distinguish between origin validation (RPKI ROV) and full path validation (BGPsec, which has essentially zero deployment)? Where is the right cost/benefit line?

**Bring back.** Whether your group would support such a mandate in your own country, and what one carve-out or safeguard is non-negotiable.

---

## Breakout B: Kill-Switch Orders and ISP Refusal
<!-- breakout id="B" status="stub" refreshed="2026-07-06" -->

**Motion.** *"ISPs served with a government order to withdraw BGP routes or block major services should refuse — even at the cost of their operating license."*

<!-- current-events:start topic="internet-shutdowns-isp-refusal" -->
**Prep reads (5–10 min).**
- *[Placeholder — refresh skill will populate with recent news on: recent national or regional Internet shutdowns — Iran, Pakistan, Ethiopia, Myanmar, India (Kashmir), or others — including any cases where ISPs pushed back or complied]*
- *[Placeholder — recent event or report on: Access Now's KeepItOn coalition or shutdown-tracking data, telecoms industry principles (GNI, Telecommunications Industry Dialogue), and any legal/civil challenges to shutdown orders]*
<!-- current-events:end -->

**Discussion prompts.**
- The book's Egypt example (Jan 2011) required only a handful of ISPs to withdraw about 3,500 BGP routes — 88% of Egyptian networks disappeared from the global routing table in minutes. If a single ISP had refused, would it have mattered? What would have happened to that ISP?
- India has shut down the Internet in Kashmir over 180 times since 2012, through licensed carriers who comply. Is compliance under license conditions morally different from Vodafone's compliance in Egypt? Is there a coherent line between "operating under local law" and "complicity in repression"?
- Some multinational telecoms (Vodafone, MTN, Orange) have published transparency reports about shutdown orders they received. Is transparency without refusal just laundering complicity, or is it a step on the ladder?
- Compare a BGP-based shutdown (Egypt-style) to a BART-style cell-service disable (Chapter 1, San Francisco 2011). The mechanisms differ; the effect is similar. Should the *ethical duty to refuse* be the same in both cases?

**Bring back.** The circumstances (if any) under which your group thinks an ISP is *obligated* to refuse a shutdown order, and how you'd operationalize that.

---

## Instructor notes

These map to §2.2.3's "all-or-nothing" characterization of BGP as a censorship tool and the Egypt/Pakistan case studies, plus the §2.2.4 point that block pages make censorship user-visible. Breakout A is the more technical debate; Breakout B is the more moral one. If the class has been engaging well with the "who gets to pull the lever" thread from Lecture 1, B lands with more force. If the class is technically inclined and has just read the RPKI/MANRS material, A is the better bet. Either way, the Pakistan Telecom hack (advertising /25s to reclaim traffic) is worth putting on the board — it's a great concrete illustration of how ad hoc BGP defense really is.
