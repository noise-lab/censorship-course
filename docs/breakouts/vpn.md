---
lecture: 17
class: "VPNs"
book_chapter: "6.1"
last_refreshed: 2026-07-06
---

# Breakout Discussions — Lecture 17: VPNs

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

The chapter's core claim is that a VPN's protective value depends on who runs it and where it operates, not on the cryptography. Both breakouts push on that claim from opposite ends: consumer trust and state coercion.

---

## Breakout A: Who Actually Owns Your VPN?
<!-- breakout id="A" status="stub" refreshed="2026-07-06" -->

**Motion.** *"No consumer VPN whose ultimate corporate parent is opaque should be recommended to journalists, activists, or dissidents — full stop."*

<!-- current-events:start topic="vpn-ownership-consolidation" -->
**Prep reads (5–10 min).**
- *[Placeholder — refresh skill will populate with recent reporting on VPN ownership consolidation: Kape Technologies' acquisitions (ExpressVPN, CyberGhost, Private Internet Access, Zenmate), the Crossrider adware history, and any post-2025 ownership changes or audits.]*
- *[Placeholder — recent investigation or research report on "free" VPN apps with hidden Chinese, Russian, or Pakistani ownership on Google Play / the App Store, including any recent takedowns or FTC actions.]*
<!-- current-events:end -->

**Discussion prompts.**
- The book says "the protective value of a VPN depends on who runs it as much as on the cryptography." If you cannot reliably determine who runs a VPN, is a signed no-logs audit worth anything? What is the audit actually attesting to?
- Kape (formerly Crossrider) sits on top of ExpressVPN, CyberGhost, PIA, and Zenmate — and also on top of the review site vpnMentor. What does that concentration do to the market signal a normal user relies on ("I googled 'best VPN' and picked the top result")?
- Facebook's Onavo marketed itself as a privacy tool while Facebook harvested the traffic. Onavo got shut down. Why haven't the free-VPN-with-adware-parent-company cases produced the same outcome? What's different — regulation, visibility, journalism, or nothing?
- Suppose a Signal-using journalist in Istanbul asks you which VPN to buy. Do you (a) name a specific product, (b) refuse to name one and explain why, (c) tell them to skip commercial VPNs entirely and use Tor + bridges, or (d) something else? Defend your answer against the other three.

**Bring back.** Your group's shortlist of what a *minimum* trustworthy-VPN disclosure regime would require (ownership, jurisdiction, audit scope, logging, breach history), and one VPN — named — that would clear that bar today.

---

## Breakout B: Blocked, Registered, or Banned?
<!-- breakout id="B" status="stub" refreshed="2026-07-06" -->

**Motion.** *"A mandatory VPN registration regime (Iran/UAE-style, where 'approved' VPNs route through state-controlled infrastructure) is more dangerous to users than an outright ban (Russia/China-style), because it manufactures the illusion of safety."*

<!-- current-events:start topic="vpn-bans-and-registration" -->
**Prep reads (5–10 min).**
- *[Placeholder — refresh skill will populate with recent news on Russia's Roskomnadzor VPN enforcement escalation, including app-store removals, protocol blocks, and any 2025–2026 amendments to the 2017 law banning circumvention-tool "promotion."]*
- *[Placeholder — recent reporting on Iran, UAE, Pakistan, or China VPN policy: state-approved VPN whitelists, prosecutions for unauthorized VPN use, App Store removals under CAC pressure, or Pakistan's PTA VPN registration scheme.]*
<!-- current-events:end -->

**Discussion prompts.**
- The UAE's 2012 cybercrime law makes VPN use to commit "any crime" a multi-year prison offense. In practice, is that a VPN ban, a selective-prosecution tool, or something else? What does that ambiguity do to a user's threat model — is uncertainty itself the control mechanism?
- Iran tolerates "approved" VPNs that route through state-controlled infrastructure. From a censor's perspective, why is a registered VPN *better than* a blocked VPN? What does the state gain that it would not get from an outright ban?
- Russia's 2017 law targeted providers; the 2024 amendment targeted *promotion* of circumvention tools. That's a shift from blocking the pipes to criminalizing speech about the pipes. Is that a meaningful legal escalation, or the natural next step? Does the same trajectory apply to the U.S. debate around encryption?
- Apple removed dozens of VPN apps from the Chinese App Store under CAC pressure in 2017 — and has kept them off. Google made different choices. If you ran Apple in 2026, and Iran issued a similar demand tomorrow, what would you do — and how would you defend the answer to (a) shareholders, (b) Iranian users, (c) the U.S. State Department?

**Bring back.** Your group's ranking: (1) outright ban, (2) mandatory registration + state routing, (3) protocol whitelisting during protests only, (4) tolerated-but-monitored — from *least* to *most* dangerous for a domestic activist. Show your reasoning.

---

## Instructor notes

These breakouts map to the "Blocking the VPNs themselves" and "VPNs are not always secure or private" section takeaways in Chapter 6.1. Breakout A tends to surface the "you get what you pay for" argument and the Onavo case study; push groups that recommend a specific paid VPN to justify *why* an audit report resolves the trust problem the book identifies. Breakout B is subtler — students often initially rank outright bans as worst, but the chapter's framing (Iran turning "circumvention" into a surveillance channel) reliably flips at least one group. If time is short, Breakout B connects more directly to the following lecture on Tor and pluggable transports.
