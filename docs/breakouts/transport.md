# Breakout Discussions — Transport Layer Manipulation

**Format.** Break into groups of 4–5. Each group picks **one** of the two breakouts below (or takes both if time allows). Spend ~5 minutes skimming the prep reads, then ~10 minutes debating. A designated reporter brings the group's position — and any dissents — back to the full class for a ~3-minute report-back.

The transport-layer story in §2.2.2 is a fight over metadata. TCP RSTs, SNI-based filtering, and DPI on the Great Firewall all work because the *envelope* is legible even when the *contents* are encrypted. Encrypted ClientHello (ECH), QUIC, and TLS 1.3 change that. These breakouts ask whether protocol designers should be picking sides — and whether the censor's side has already lost.

---

## Breakout A: Should Protocol Designers Pick Sides?
<!-- breakout id="A" status="current" refreshed="2026-07-06" -->

**Motion.** *"IETF working groups on ECH, QUIC, and DNS-over-HTTPS are effectively anti-censorship activism dressed up as engineering, and that is a good thing."*

<!-- current-events:start topic="ech-quic-anti-censorship-protocol-design" -->
**Prep reads (5–10 min).**
- [Russia's internet watchdog blocks thousands of websites that use Cloudflare's privacy service](https://therecord.media/russia-blocks-thousands-of-websites-that-use-cloudflare-service) — The Record, November 2024. Roskomnadzor blocks any TLS handshake carrying `cloudflare-ech.com` as its outer SNI, one month after Cloudflare's ECH re-launch.
- [Encrypted Client Hello (ECH) in Censorship Circumvention](https://petsymposium.org/foci/2025/foci-2025-0016.pdf) — Niere et al., FOCI 2025. Measurement paper showing ECH deployment is essentially Cloudflare-only, and censors can defeat it by blocking the small set of advertised outer SNIs.
- [Do Not Stick Out: The Dynamics of the ECH Rollout](https://cdt.org/insights/do-not-stick-out-the-dynamics-of-the-ech-rollout/) — Center for Democracy & Technology, 2025. Frames the paradox: ECH only works when it is ubiquitous, but to get ubiquitous it has to start somewhere — and early adopters get picked off.
- [Disrupted, Throttled, and Blocked: State Censorship in Russia](https://www.hrw.org/report/2025/07/30/disrupted-throttled-and-blocked/state-censorship-control-and-increasing-isolation) — Human Rights Watch, July 2025. Documents Cloudflare's, Mozilla's, Apple's, and Google's responses to Russian pressure over ECH, VPNs, and app-store takedown demands.
<!-- current-events:end -->

**Discussion prompts.**
- The book's Turkey and Great Firewall examples both depend on the censor seeing *something* in the clear — a DNS query, an SNI, an IP. TLS 1.3 with ECH closes the SNI hole. Is protocol standardization the right venue to make that choice, or is this a policy decision being smuggled into a technical body?
- Enterprise network admins and school-district filters use the exact same visibility that censors do. Chapter 1 flagged that the tools are the same; only the operator differs. Should ECH ship with a documented enterprise-bypass mode, or is that a backdoor by another name?
- QUIC runs on UDP and is much harder to reset with a mid-stream injection than TCP. If you were designing GFW v2, what would you do about QUIC? Block it entirely? Force downgrade to TCP? Something else?
- If protocol design becomes an explicit venue for anti-censorship advocacy, what stops the same body from being captured by governments that want the opposite (see: earlier IETF fights over lawful intercept)? Is a "neutral" IETF even coherent?

**Bring back.** One design decision (in ECH, QUIC, or DoH) your group would reverse, and why.

---

## Breakout B: Is the Cat-and-Mouse Game Winnable?
<!-- breakout id="B" status="current" refreshed="2026-07-06" -->

**Motion.** *"Deep packet inspection has already lost: within five years, no state-level censor will reliably distinguish circumvention traffic from ordinary HTTPS."*

<!-- current-events:start topic="gfw-dpi-vs-circumvention-arms-race" -->
**Prep reads (5–10 min).**
- [Exposing and Circumventing SNI-based QUIC Censorship of the Great Firewall of China](https://gfw.report/publications/usenixsecurity25/en/) — GFW Report, USENIX Security 2025. Since April 2024, the GFW decrypts QUIC Initial packets at line rate to recover the SNI — but SNI fragmentation across CRYPTO frames sidesteps it.
- [Staying ahead of censors in 2025: What we've learned from fighting censorship in Iran and Russia](https://blog.torproject.org/staying-ahead-of-censors-2025/) — Tor Project, 2025. Snowflake and WebTunnel are absorbing the load as obfs4 gets fingerprinted; Conjure ships to defeat bridge-list enumeration.
- [Snowflake-targeted DTLS filtering in Russia, starting 2026-03-30](https://github.com/net4people/bbs/issues/603) — net4people/bbs, March 2026. Russia begins DTLS ja3/ja4 fingerprint blocking of Snowflake after months of near-100% success, marking a fresh escalation.
- [Iran's January 2026 Internet Shutdown: Public Data, Censorship Methods, and Circumvention Techniques](https://arxiv.org/html/2603.28753v1) — arXiv, 2026. Layered DNS + HTTP(S) + protocol-level filtering during the January 2026 blackout, plus what actually kept working (obfs4, Snowflake, TLS fragmentation).
<!-- current-events:end -->

**Discussion prompts.**
- The book calls this "a continual cat-and-mouse game." What would it take for that game to actually *end*? Does either side have a plausible endgame, or is this a permanent standoff?
- GFW-style censors have started using machine-learning classifiers on traffic patterns (packet sizes, timing) rather than payload contents. If content is encrypted but *shape* is legible, has encryption really helped? What would "traffic-shape indistinguishability" cost in performance?
- The book notes that some censors don't beat obfuscation technically — they beat it by *coercing VPN providers* into compliance or by criminalizing their use. If the technical game is a stalemate, does the fight move entirely into the legal/economic layer?
- Rank these circumvention tools by five-year survivability against a well-resourced censor: commercial VPNs, Tor with obfs4, Shadowsocks, Snowflake, domain fronting via CDNs. Defend the top and the bottom.

**Bring back.** Your group's prediction on the state of censorship-circumvention in China (or another named censor) in 2030, in one sentence.

---

## Instructor notes

These map to the "Defending against TCP/IP manipulation" subsection and the section takeaway that encryption is "pushing censors toward coarser tools." Breakout A works better with students who have IETF/W3C exposure or who have thought about standards politics. Breakout B is more concrete and better for students who want to argue about specific tools. Consider running B first as a warmup and A as the more philosophical follow-on — the ECH/QUIC debate has more edges once students have named the tradeoffs in the arms race.

<!--
breakout-metadata:
  lecture: 3
  class: "Transport Layer Manipulation"
  book_chapter: "2.2.2"
  last_refreshed: 2026-07-06
-->
