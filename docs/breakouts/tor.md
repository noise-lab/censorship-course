# Anonymous Communication

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

Chapter 6.2 makes two claims that live in tension: (1) Tor's anonymity is only as strong as the infrastructure that hosts its relays and bridges, and (2) the same infrastructure — exit nodes, cloud front-ends for pluggable transports — is precisely where legal and commercial pressure lands. Both breakouts sit on that fault line.

---

## Breakout A: Exit Nodes and the Criminal Safe Harbor
<!-- breakout id="A" status="current" refreshed="2026-07-06" -->

**Motion.** *"Operating a Tor exit relay should carry an explicit criminal safe harbor, analogous to Section 230 for platforms — no country should be able to prosecute an operator for traffic they merely forwarded."*

<!-- current-events:start topic="tor-exit-node-legal-liability" -->
**Prep reads (5–10 min).**
- [German police raid Tor-linked group in bid to uncover Tor network users](https://cybernews.com/privacy/tor-exit-node-operator-raided-germany/) — Cybernews, August 2024. Essen police raid Article 5 eV, a non-profit that operates Tor exit nodes, under a child-pornography warrant; board member Gero Kühn describes the intimidation effect on volunteer operators.
- [The Legal FAQ for Tor Relay Operators](https://community.torproject.org/relay/community-resources/eff-tor-legal-faq/) — Tor Project / EFF, updated 2025. The community's reference document on U.S. exposure, DMCA handling, and why operators are advised not to run exits from home.
- [Tor Exit Guidelines](https://community.torproject.org/relay/community-resources/tor-exit-guidelines/) — Tor Project, 2025. Points to the 2014 Graz (Austria) conviction of an exit-relay operator as an accomplice — the leading cautionary precedent in the EU and still uncontested by any subsequent 2025–2026 ruling.
- [Staying ahead of censors in 2025: What we've learned from fighting censorship in Iran and Russia](https://blog.torproject.org/staying-ahead-of-censors-2025/) — Tor Project blog, December 2025. Context on how much the network now depends on volunteer exit and bridge capacity as pressure grows on operators worldwide.
<!-- current-events:end -->

**Discussion prompts.**
- The book notes that Tor has ~2.5M daily users and depends on volunteer relay operators. If exit-node operators can be raided, prosecuted, or bankrupted, what happens to the size and geographic diversity of the exit-relay pool — and therefore to the anonymity of every Tor user in the world?
- The Silk Road prosecution went after Ross Ulbricht as an *operator*, not against Tor infrastructure. Ulbricht was later pardoned (2025). What signal does that pardon send to (a) prospective dark-web marketplace operators, (b) prospective exit-relay volunteers, (c) prosecutors deciding whether to charge next time?
- Compare an exit-relay operator to (i) a coffee-shop offering open Wi-Fi, (ii) a residential ISP, (iii) a Cloudflare-style CDN, (iv) a Signal server operator. The law treats these very differently. Which analogy is closest, and why does the analogy you pick determine the policy answer?
- A safe harbor for exit operators would also protect people running exits *for* dark-web marketplaces, CSAM traffic, and ransomware C2. Is there a version of the safe harbor that carves those out without collapsing back into the current situation? Or is the point that you can't distinguish traffic without destroying the anonymity property?

**Bring back.** Your group's draft of a one-sentence safe-harbor clause — the actual text — that you would defend in front of both the EFF and a prosecutor.

---

## Breakout B: Compelled Takedown of Bridges and Pluggable Transports
<!-- breakout id="B" status="current" refreshed="2026-07-06" -->

**Motion.** *"Cloudflare, AWS, and Azure should refuse any government demand to take down Tor bridges, Snowflake broker infrastructure, or domain-fronted circumvention endpoints — even lawful demands from democracies."*

<!-- current-events:start topic="pluggable-transport-takedowns" -->
**Prep reads (5–10 min).**
- [Staying ahead of censors in 2025: What we've learned from fighting censorship in Iran and Russia](https://blog.torproject.org/staying-ahead-of-censors-2025/) — Tor Project blog, December 2025. WebTunnel bridges rolled out in 2024 were largely burned by Russia by mid-2025; Snowflake and Conjure now carry more of the load, and both depend on cloud-hosted brokers.
- [Advancing digital rights in 2026 will take all of us](https://blog.torproject.org/advancing-digital-rights-in-2026/) — Tor Project blog, December 2025. Sets out the 2026 roadmap: Conjure rollout, Snowflake efficiency work, and Tor VPN integration as hedges against pluggable-transport takedowns.
- [A new wave of blocks in Russia targets VPN apps and Cloudflare subnets](https://www.techradar.com/vpn/vpn-privacy-security/a-new-wave-of-blocks-in-russia-targets-vpn-apps-and-cloudflare-subnets) — TechRadar, 2025. March 2025 Roskomnadzor operation that briefly took out Cloudflare subnets across Russian regions — a preview of what compelled cloud takedowns look like at scale.
- [Domain fronting has a dwindling future as cloud providers ban the practice](https://cyberscoop.com/domain-fronting-future-amazon-google-microsoft-cloudflare-tor-signal/) — CyberScoop, updated coverage through 2024. Chronicles the Cloudflare (2015) → Google/Amazon (2018) → Microsoft Azure (Jan 2024) → Fastly (2024) takedowns and what remains for Signal and Psiphon.
<!-- current-events:end -->

**Discussion prompts.**
- The book describes how Google and Amazon disabled domain fronting "under the guise of improving security," effectively pulling the rug out from under meek. Was that a business decision, a security decision, or a censorship decision? Does it matter which — if the effect on Iranian and Chinese users is the same?
- Snowflake ephemeral proxies run in volunteer browsers; the *broker* runs on cloud infrastructure. If a government compels the cloud provider to shut down the broker, Snowflake breaks globally — not just in that country. Is that a proportionate exercise of national jurisdiction, or an extraterritorial takedown by design?
- Cloudflare hosts Tor bridges, hosts state-media sites, and has publicly grappled with "who should be allowed on the Internet." Is there a principled distinction between Cloudflare refusing service to 8chan (which they did) and Cloudflare refusing to host Tor bridges under Russian legal pressure (which they have not)? Or is it just a question of who is asking?
- Iran approved a state-controlled VPN whitelist while blocking Signal. Signal has historically used domain fronting to reach Iranian users. If AWS or Azure caved to a hypothetical Iranian pressure campaign, what's the fallback? Is there one that scales?

**Bring back.** A one-page decision tree your group would give to Cloudflare's trust-and-safety team for handling a government takedown demand aimed at circumvention infrastructure. What are the branches, and what triggers each?

---

## Instructor notes

These breakouts map to the "Pluggable Transports" and "Tracking and Deanonymization" section takeaways in Chapter 6.2, and pull threads from Chapter 6.4 (infrastructure) forward. Breakout A tends to divide cleanly along whether students think Tor's marginal utility to journalists and dissidents outweighs its marginal utility to criminals — press them to name the specific tradeoff rather than argue in the abstract. Breakout B is where the "infrastructure consolidation" theme from Lecture 1 pays off; the strongest report-backs will connect the dots between commercial cloud policy, national censorship, and the fragility of the Snowflake/obfs4/meek portfolio.

<!--
breakout-metadata:
  lecture: 18
  class: "Anonymous Communication"
  book_chapter: "6.2"
  last_refreshed: 2026-07-06
-->
