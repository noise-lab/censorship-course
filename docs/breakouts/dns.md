---
lecture: 2
class: "DNS Manipulation"
book_chapter: "2.2.1"
last_refreshed: 2026-07-06
---

# Breakout Discussions — Lecture 2: DNS Manipulation

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

The book's DNS section makes one uncomfortable point again and again: DNS is trivially easy to manipulate (just return a different IP), and every "fix" — DoH, DNSSEC, ODoH — trades one trust problem for another. These breakouts push on where you would rather have the chokepoint.

---

## Breakout A: Did DoH Just Move the Chokepoint?
<!-- breakout id="A" status="stub" refreshed="2026-07-06" -->

**Motion.** *"Browser-default DNS-over-HTTPS to Cloudflare and Google is a net loss for user autonomy: it hides censorship from your ISP only by handing a global veto to three American companies."*

<!-- current-events:start topic="doh-centralization-court-orders" -->
**Prep reads (5–10 min).**
- *[Placeholder — refresh skill will populate with recent news on: court orders or regulatory demands compelling Cloudflare, Google, Quad9, or NextDNS to block or manipulate DNS responses for specific domains, especially in EU/UK piracy or child-safety cases]*
- *[Placeholder — recent event or report on: measurement studies or policy analyses of DoH resolver market share, browser defaults, or ISP responses to DoH rollout]*
<!-- current-events:end -->

**Discussion prompts.**
- The book's Turkey example (protesters spray-painting `8.8.8.8`) treats Google's public resolver as the *good* actor circumventing ISP censorship. But the same chapter warns that a single court order to Google or Cloudflare now censors "entire countries or regions." Which framing is right for the world we live in *now*, not the world of 2014?
- Chrome defaults to Google's resolver; Firefox defaults to Cloudflare's. Neither asked you. Is opt-out consent good enough for something that sees every domain you visit? What would meaningful consent look like?
- Oblivious DNS (ODoH) splits knowledge between a proxy and a resolver, so neither sees "who is asking what." If ODoH shipped by default tomorrow, would that solve the problem, or is the *takedown* power (not the surveillance power) the real issue?
- Rank the following as a resolver operator you would trust: your ISP, Cloudflare, Google, your government's public resolver, a nonprofit like Quad9, a resolver you run yourself. Defend the top and bottom of your ranking.

**Bring back.** Your group's rank-ordering of resolver operators, and the single strongest counterargument to your own top pick.

---

## Breakout B: Court-Ordered Takedowns vs. Un-Censorable Naming
<!-- breakout id="B" status="stub" refreshed="2026-07-06" -->

**Motion.** *"Democracies should be able to seize domain names by court order; anyone building 'un-censorable' naming systems (blockchain domains, alternate roots) is enabling fraud and abuse more than dissent."*

<!-- current-events:start topic="domain-seizure-blockchain-naming" -->
**Prep reads (5–10 min).**
- *[Placeholder — refresh skill will populate with recent news on: domain seizures by ICE, DOJ, EU regulators, or German courts targeting Cloudflare/Quad9 for piracy blocking, or the 2023 German ruling refusing to compel DNS providers]*
- *[Placeholder — recent event or report on: ENS, Handshake, Unstoppable Domains, or other alternative naming systems and their use (or abuse) in the wild]*
<!-- current-events:end -->

**Discussion prompts.**
- The book describes the 2023 German case where a court *refused* to force Cloudflare to block infringing sites, citing overblocking and freedom-of-expression concerns. Was the court right? What if the same logic were applied to CSAM or state-sponsored disinformation domains?
- DNSSEC signs answers but does not change *who* can answer. A blockchain-based naming system removes the trusted root entirely — no ICANN, no courts. What breaks in a world where domain names cannot be seized? What gets better?
- The Turkey example works because a *different* trusted resolver (Google) is a click away. If the alternative to state-controlled DNS is "run your own recursive resolver," how many people in this room actually could? Does a defense that only works for the technically sophisticated count as a defense at all?
- Suppose you are advising a mid-sized democracy writing new DNS-blocking legislation. Would you allow (a) ISP-level blocks only, (b) blocks on major public resolvers as well, (c) blocks against alternate-root providers, or (d) none of the above? Where do you draw the line and why?

**Bring back.** The one DNS-related power your group is *willing* to give a government, and the one your group would never give up.

---

## Instructor notes

These map to the two big takeaways from §2.2.1: (1) DNS is easy to manipulate because it lacks authentication, so the fight has shifted to *who runs the resolver*; and (2) DoH/DNSSEC don't fix the trust problem, they relocate it. Breakout A tends to land harder with students who use Chrome/Firefox daily (the "you already made this choice" beat is uncomfortable). Breakout B is better if you have students with policy or law backgrounds — the Germany case is a rich anchor. If time is short, run A; the Turkey/8.8.8.8 image in the chapter gives it immediate texture.
