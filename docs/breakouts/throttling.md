# Throttling and Rate Limiting

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

Throttling is the book's cleanest example of [Molly Roberts](https://en.wikipedia.org/wiki/Margaret_E._Roberts)'s *friction*: the site is not blocked, it is just slow enough that you give up. The chapter is honest that detection is genuinely hard — [Wehe](https://wehe.meddle.mobi/) results contradict themselves on the same network — and that's precisely why throttling is politically attractive. These breakouts push on accountability and on where "throttling" ends and "everyday network management" begins.

---

## Breakout A: Plausibly Deniable Censorship
<!-- breakout id="A" status="current" refreshed="2026-07-06" -->

**Motion.** *"Throttling is the most dangerous form of Internet censorship precisely because it is deniable — and detection tools like Wehe are too unreliable to hold anyone accountable."*

<!-- current-events:start topic="throttling-during-protests-detection" -->
**Prep reads (5–10 min).**
- [Censorship Chronicles: The systematic suppression of independent media in Russia](https://ooni.org/post/2024-russia-report/) — OONI, 2024. Documents Russia's YouTube throttling — accessible on mobile, blocked on broadband, same ISP — and the ~30% audience loss reported by independent media.
- [Government Internet Shutdowns Cost $19.7B in 2025](https://www.top10vpn.com/research/cost-of-internet-shutdowns/) — Top10VPN, 2026. Introduces Russia's "16 KB Curtain" — Cloudflare-hosted sites load their first 16 KB and then stall, preserving the appearance of connectivity while breaking the actual service.
- [What the End of U.S. Net Neutrality Means](https://www.scientificamerican.com/article/what-the-end-of-u-s-net-neutrality-means/) — Scientific American, 2025. Sixth Circuit strikes down the FCC's 2024 Safeguarding Order; David Choffnes (Wehe) argues measurement, not federal rule, is now the accountability layer.
- [Russia's internet censorship in 2026: VPN crackdowns, mobile shutdowns, Telegram blocks and the state messenger Max](https://en.zona.media/article/2026/04/07/russian_internet_censorship_2026) — Zona Media, April 2026. Roskomnadzor gains statutory authority in March 2026 to centrally reroute traffic and isolate the RuNet from external resources.
<!-- current-events:end -->

**Discussion prompts.**
- [Russia throttled Twitter for months in 2021](https://en.wikipedia.org/wiki/Block_of_Twitter_in_Russia) by degrading traffic to any domain containing "t.co." Officially it was "protecting minors." Politically, everyone knew. If both sides know the truth and the tools cannot prove it, does deniability still function? What is deniability *for*?
- The book describes Wehe as facing "fundamental detection challenges" — same user, same network, contradictory results. If we cannot even measure throttling reliably, what does an evidence-based accountability regime for it even look like? Is this a case where the standard of proof needs to *drop*, not rise?
- The [2014 US Netflix/ISP dispute](https://en.wikipedia.org/wiki/Net_neutrality_in_the_United_States) was technically peering-congestion, not traffic-shaping — but the effect on users was identical. Does *intent* matter for accountability? Should regulators care about outcomes only, or about mechanisms?
- Suppose your country's telecom regulator has authority to fine ISPs for throttling. What evidentiary standard would you set: (a) beyond reasonable doubt, (b) preponderance of evidence, (c) shifted burden — ISP must prove congestion, or (d) something else? Defend your choice.

**Bring back.** One accountability mechanism your group thinks could actually work against throttling — measurement, regulation, transparency, market pressure, or something else — and the strongest reason it might fail.

---

## Breakout B: Platform Throttling vs. ISP Throttling
<!-- breakout id="B" status="current" refreshed="2026-07-06" -->

**Motion.** *"When a platform (YouTube, TikTok, X) throttles or down-ranks content, that is worse than an ISP throttling the same content — because there is no regulatory backstop and no exit."*

<!-- current-events:start topic="platform-throttling-vs-isp-throttling" -->
**Prep reads (5–10 min).**
- [EC Issues First Non-Compliance Fine Under the DSA: X Fined €120 Million for Dark Patterns and Transparency Failures](https://www.goodwinlaw.com/en/insights/publications/2025/12/alerts-practices-antc-ec-issues-first-non-compliance-fine-under) — Goodwin Law, December 2025. First DSA non-compliance fine, on paid-verification "reply prioritization" that algorithmically boosts subscribers' visibility.
- [What the EU's X Decision Reveals About How the DSA Is Enforced](https://www.techpolicy.press/what-the-eus-x-decision-reveals-about-how-the-dsa-is-enforced/) — Tech Policy Press, 2025. Argues the fine is really about *transparency* — ad repository, researcher data access — more than direct throttling of competitors.
- [What the End of U.S. Net Neutrality Means](https://www.scientificamerican.com/article/what-the-end-of-u-s-net-neutrality-means/) — Scientific American, 2025. With the Sixth Circuit striking down federal no-throttling rules in January 2025, ISPs are now regulated less than platforms — inverting the 2015-era assumption.
- [How the Digital Services Act enhances transparency online](https://digital-strategy.ec.europa.eu/en/policies/dsa-brings-transparency) — European Commission, 2025. Official framing of the researcher data-access rules that took effect 29 October 2025.
<!-- current-events:end -->

**Discussion prompts.**
- The book frames throttling as a network-operator technique using token/leaky buckets. But platforms throttle too, at the application layer — X reportedly added 5-second delays to links pointing at Substack, Bluesky, and Threads in 2023. Same effect on users, different actor. Which is worse, and why?
- Net neutrality debates assume ISPs are the danger and platforms are the victims. Is that still coherent in 2026, when Meta, Google, and Amazon operate more infrastructure (private fiber, edge networks, CDNs) than most ISPs? Where does the "platform" end and the "ISP" begin?
- If you were forced to choose *one* regime — either ISPs are subject to strict no-throttling rules and platforms are unregulated, OR platforms are subject to algorithmic-transparency rules and ISPs are unregulated — which would you pick? Why?
- The book connects throttling to Molly Roberts's concept of *friction*: raise the cost enough and people go elsewhere. When a platform down-ranks a link, that's friction. When an ISP throttles a competitor, that's friction. When your phone's OS demotes a sideloaded app, that's friction. Is there a principled line here, or is friction just friction?

**Bring back.** Your group's ranking (worst to least-bad) of: ISP throttling, platform down-ranking, OS-level app friction, CDN de-platforming.

---

## Instructor notes

These map to §2.3.1's core arguments: throttling is a form of *friction* (Molly Roberts), detection is genuinely hard, and the line between intentional shaping and congestion is porous. Breakout A is the natural pairing with the Wehe discussion — students who took the technical detour on token buckets will engage with the evidentiary-standard question. Breakout B is looser and more current-events-driven; it works well if the class has been circling net-neutrality debates or platform regulation. If time is tight, A is the tighter fit to the book chapter; B is better if you want to bridge forward to later platform-power material.

<!--
breakout-metadata:
  lecture: 5
  class: "Throttling and Rate Limiting"
  book_chapter: "2.3.1"
  last_refreshed: 2026-07-06
-->
