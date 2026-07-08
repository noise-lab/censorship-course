# Lecture 2 — Speaker Notes

Expanded background and source URLs for each slide. In-deck notes (the `::: {.notes}` blocks) are visible via reveal.js speaker view (press **S** with the deck open).

**Every URL below has been verified this session or is a canonical org landing page.** Descriptive citations (author + venue + year) with no URL mean "I know the source exists but don't have a URL I've confirmed — look it up if you want a link."

---

## Why Are the Internet's Protocols So Easy to Manipulate?

- The design-for-trust story is Chapter 2, §2.1 of the book.
- **The classic paper** on the tension: David Clark, ["The Design Philosophy of the DARPA Internet Protocols" (SIGCOMM 1988)](https://groups.csail.mit.edu/ana/Publications/PubPDFs/The%20design%20philosophy%20of%20the%20DARPA%20internet%20protocols.pdf) — Clark ranks *seven* design goals; note that *accountability* is last and *survivability* is first. Security is nowhere in the top seven.
- **Morris worm (Nov 1988):** the first wake-up call that trusted-peer assumptions don't hold at Internet scale. [Morris worm — Wikipedia](https://en.wikipedia.org/wiki/Morris_worm).
- The recurring theme: **"the network looks broken" and "the network is being censored" often look identical.** Comes back throughout the course, especially in Chapter 5 on measurement.

---

## A "Protocol" Is Just an Agreement

- **The "narrow waist" (hourglass model)** is the design principle to name-drop: everything runs *over* IP; IP runs *over* everything. See the classic [RFC 3439 (2002) — Some Internet Architectural Guidelines](https://datatracker.ietf.org/doc/html/rfc3439) §2.1 and Steve Deering's ["Watching the Waist of the Protocol Hourglass"](https://www.iab.org/wp-content/IAB-uploads/2011/03/hourglass-london-ietf.pdf) slides.
- **Postel's Robustness Principle** ("be conservative in what you send, be liberal in what you accept" — RFC 1122) is the *cultural* explanation for why every protocol is trivially fooled: nothing enforces sanity on inputs. [RFC 1122](https://datatracker.ietf.org/doc/html/rfc1122).
- Don't over-explain: the takeaway is "no built-in authentication, no accountability" — the lever every technique in the deck pulls.

---

## Manipulation Targets a Few Points in the Stack

- **Book Table 2.1** — this is the roadmap for the entire lecture. Each row = one section of the deck.
- Aksoy et al., ["A Taxonomy of Internet Censorship and Anti-Censorship" (arXiv 2011)](https://arxiv.org/abs/1108.3646) is an early and still-useful classification along similar lines if you want an alternative taxonomy.
- Book's own layered model matches the FIRE (Fake / Intercept / Reset / Erase) breakdown popularized by measurement work in the 2010s.

---

## DNS Maps Names to Addresses

- **DNS foundational RFCs:** [RFC 1034 (concepts)](https://datatracker.ietf.org/doc/html/rfc1034) and [RFC 1035 (implementation)](https://datatracker.ietf.org/doc/html/rfc1035), Paul Mockapetris, 1987. Old but current.
- **Root-server geography:** [root-servers.org](https://www.root-servers.org/) shows the anycast footprint of the 13 root-server systems. Useful when a student asks "isn't the root a single point of failure?" — answer: each letter is anycast across hundreds of physical sites.
- If a student asks about the local resolver: [DHCP options 6](https://datatracker.ietf.org/doc/html/rfc2132) is how a resolver gets assigned. Most people never think about it — but that assignment is exactly the on-path chokepoint censors exploit.

---

## DNS Is Insecure by Default

- **Origin as monetization, not censorship.** The paradigmatic case:
  - **Verisign SiteFinder (Sep 2003):** Verisign hijacked `NXDOMAIN` responses for `.com`/`.net` to redirect mistyped domains to a Verisign-owned search/ads page. ICANN forced withdrawal. [Site Finder — Wikipedia](https://en.wikipedia.org/wiki/Site_Finder). [ICANN's SSAC report on the incident](https://www.icann.org/committees/security/ssac-report-09jul04.pdf).
  - **Comcast NXDOMAIN redirection (2009):** ISP-level monetization of typos with an ads page. [DNS hijacking — Wikipedia](https://en.wikipedia.org/wiki/DNS_hijacking#Manipulation_by_ISPs).
  - **Paxfire (2011):** Charter, RCN, Cavalier and other US ISPs intercepted DNS for popular sites and sold the redirected search traffic. Broken by Reethika Ramesh & Craig Timberg's reporting. [Wired story](https://www.eff.org/deeplinks/2011/07/widespread-search-hijacking-in-the-us).
- **Iran fake root referrals (May 2013):** Nikita Borisov / others documented DNS answers arriving from *inside Iran* faster than the speed-of-light would allow from the real root in LA. Timing anomaly = tell. Search "Anonymous DNS Iran root 2013" for the writeups; the academic follow-up is Anonymous, [*"The Collateral Damage of Internet Censorship by DNS Injection,"* SIGCOMM CCR 2012](https://dl.acm.org/doi/10.1145/2317307.2317311) — same technique.
- **The historical arc to name in class:** DNS manipulation was invented for *ads*. Censors just noticed the trick worked.

---

## DNS Censorship in the Wild: Turkey, 2014

- **Twitter block (Mar 20, 2014) followed by YouTube block (Mar 27, 2014).** Erdoğan pre-election crackdown after leaked recordings surfaced on both platforms.
- **The `8.8.8.8` iconography** — spray-painted on walls in Istanbul and Ankara. Photos: search "8.8.8.8 Turkey graffiti" in image search; several make the rounds.
- **The ISPs escalated:** initially blocked at DNS (recursive resolver returned wrong answer), then blocked 8.8.8.8 itself when users switched. [Blocking of Twitter in Turkey — Wikipedia](https://en.wikipedia.org/wiki/Censorship_of_Twitter_in_Turkey).
- **The lesson to draw:** the *first* layer censors reach for is also the *easiest* to route around. That's part of why it stays popular — it's cheap, deniable, and imposes friction rather than a wall.
- **Turkey's later moves** (2016 Wikipedia block, 2017–2020 sustained; unblocked Dec 2019): [Block of Wikipedia in Turkey — Wikipedia](https://en.wikipedia.org/wiki/Block_of_Wikipedia_in_Turkey).

---

## Detecting DNS Manipulation Is Hard

- **The seminal measurement paper** on multi-signal DNS censorship detection: Pearce et al., ["Global Measurement of DNS Manipulation" (USENIX Security 2017)](https://www.usenix.org/system/files/conference/usenixsecurity17/sec17-pearce.pdf) — the IRIS system. Establishes the AS + content + rDNS + certificate triangulation this slide is describing.
- **Follow-on / production:** [Censored Planet](https://censoredplanet.org/) at U-Michigan (Roya Ensafi's group) — continuous, remote measurement using the Satellite / Iris pipeline. Their [2020 paper (IMC)](https://censoredplanet.org/) is the reference.
- **The CDN confound is the real trap.** Cloudflare, Akamai, and Fastly legitimately return different IPs per user location. Detection has to distinguish "regional CDN endpoint" from "government redirect." Multiple-signal triangulation is how.
- **OONI's DNS-consistency probe** is the community-scale version: [OONI DNS Consistency test](https://ooni.org/nettest/dns-consistency/).

---

## Encrypted DNS Helps — and Centralizes

- **DoH (DNS over HTTPS):** [RFC 8484](https://datatracker.ietf.org/doc/html/rfc8484), 2018. Chrome ships with Google `8.8.8.8` as default upgrade target; Firefox ships with Cloudflare `1.1.1.1`.
- **DoT (DNS over TLS):** [RFC 7858](https://datatracker.ietf.org/doc/html/rfc7858), 2016. Port 853, easier to block than DoH because it's on a distinctive port.
- **DNSSEC:** [RFC 4033 and follow-ons](https://datatracker.ietf.org/doc/html/rfc4033), 2005. Integrity, not confidentiality. Deployment is uneven — root zone is signed, most TLDs are signed, but adoption on individual zones is patchy. Verisign's DNSSEC stats: [https://scoreboard.verisignlabs.com/](https://scoreboard.verisignlabs.com/).
- **ODoH (Oblivious DoH):** [RFC 9230](https://datatracker.ietf.org/doc/html/rfc9230), 2022 — Cloudflare + Apple co-designed. Splits *who is asking* (proxy) from *what is being asked* (target). Cloudflare's writeup: [Announcing ODoH (Dec 2020)](https://blog.cloudflare.com/oblivious-dns/).
- **Germany 2023 — Cloudflare compelled to block? Not quite.** The Sony Music v. Cloudflare / Quad9 cases: German copyright holders sued to force DNS-layer blocking. Regional courts issued injunctions against **Quad9** in particular (the DNS4EU / IT-Sicherheit foundation). Good writeup: [Quad9's Own Press Room](https://www.quad9.net/news/press/) or the CommunityDNS coverage. Also see [torrentfreak coverage](https://quad9.net/news/blog/quad9-turns-the-sony-case-around-in-dresden/).
- **The centralization tension is the modern point.** Old world: compel 10,000 ISP resolvers, some will resist. New world: compel Cloudflare or Google *once* and you affect millions. That reversal is what makes DoH double-edged.
- If you want to riff on the current front: **Chrome's Secure DNS UX** (`chrome://settings/security` → "Use secure DNS") is the everyday-user version of this trade-off.

---

## TCP in One Slide

- **TCP foundational RFC:** [RFC 793](https://datatracker.ietf.org/doc/html/rfc793) (1981), superseded by [RFC 9293](https://datatracker.ietf.org/doc/html/rfc9293) (2022).
- **IPv4 exhaustion, if a student asks:** ARIN ran out in Sep 2015; RIPE in Nov 2019; APNIC in Apr 2011. See [Wikipedia on IPv4 exhaustion](https://en.wikipedia.org/wiki/IPv4_address_exhaustion).
- **The forgeable-RST fact** is the pivot for the next slide. Nothing in the TCP spec signs a RST; anyone on-path can craft one that both endpoints will honor.

---

## TCP Reset Injection

- **The canonical academic paper:** Clayton, Murdoch, Watson, ["Ignoring the Great Firewall of China" (PETS 2007)](https://link.springer.com/chapter/10.1007/978-3-540-75551-7_2). Cambridge team documented forged RST injection, and showed that *ignoring* the RST (both endpoints) defeats it.
- **Xu, Mao, Halderman, ["Internet Censorship in China: Where Does the Filtering Occur?" (PAM 2011)](https://web.eecs.umich.edu/~zmao/)** locates the GFW's injectors on provincial-backbone routers (AS-level filtering, not per-ISP).
- **Duplicate-sequence-number ("packet-forgery") attacks** — later documented variants of the same trick. See Weaver et al., ["Detecting Forged TCP Reset Packets" (NDSS 2009)](https://www.cs.icsi.berkeley.edu/pubs/networking/tcpreset-ndss09.pdf).
- **Commercial DPI tools that do this:** Blue Coat, Sandvine, Cisco's older content-filtering appliances. If a student asks whether US networks have this capability: yes, most enterprise firewalls (Palo Alto, Fortinet) can inject resets on policy match — the difference is *policy*, not capability.

---

## Defending TCP/IP: Encryption Moves the Battle

- **TLS 1.3:** [RFC 8446](https://datatracker.ietf.org/doc/html/rfc8446), 2018. Encrypts the certificate; the only cleartext left in the handshake is the SNI.
- **ECH (Encrypted Client Hello):** [draft-ietf-tls-esni](https://datatracker.ietf.org/doc/html/draft-ietf-tls-esni) — closes the SNI leak. Cloudflare's writeup: [Announcing ECH (Sep 2023)](https://blog.cloudflare.com/announcing-encrypted-client-hello/).
- **States now blocking ECH:** Russia blocked ECH in late 2024. [Russia blocks ECH — RestOfWorld / Meduza coverage](https://meduza.io/en/news/2024/11/08/russia-s-internet-censor-demands-a-break-from-cloudflare-after-the-american-company-enabled-new-privacy-tools-last-month). China's GFW blocks ECH-configured handshakes: see GFW-report analysis via [Great Firewall Report](https://github.com/net4people/bbs/issues) — a great community-run tracker of Chinese blocking. Iran is reported to be experimenting.
- **VPN / Tor / Shadowsocks primer** — save the depth for Ch. 6, but here's a one-liner map: VPN tunnels a whole flow, Tor onions traffic through three relays, Shadowsocks obfuscates SOCKS to look like TLS. All three raise the censor's cost; none is a silver bullet.
- **DPI vendors:** Sandvine (used by Iran, Russia, Egypt for throttling), Netsweeper, Blue Coat (now Symantec). Citizen Lab has documented Sandvine's deployments extensively: [Citizen Lab Sandvine coverage](https://citizenlab.ca/tag/sandvine/).

---

## BGP: Driving Directions, One Hop at a Time

- **BGP:** [RFC 4271](https://datatracker.ietf.org/doc/html/rfc4271) (2006). The "no security" property is by design — no built-in origin authentication.
- **Number of ASNs today:** roughly 80,000–100,000 active. Live count at [CIDR Report — Active BGP Entries](https://www.cidr-report.org/as2.0/).
- **RouteViews** — the classic BGP measurement archive: [routeviews.org](https://www.routeviews.org/). This is the hands-on for Lecture 3 (per the course agenda).
- **RIPE RIS** — European equivalent: [ris.ripe.net](https://ris.ripe.net/).
- **The transitive-trust vulnerability** — a good intuition-builder to draw on the whiteboard if students look lost. A neighbor's neighbor lies; your router accepts the lie because your neighbor said "yes, that's fine."

---

## Route Hijacking: China Telecom, 2010

- **The Renesys post-mortem** (now Kentik): [Dyn/Renesys, "China's 18-Minute Mystery"](https://en.wikipedia.org/wiki/BGP_hijacking#Notable_incidents) — the original blog is at [https://dyn.com/blog/chinas-18-minute-mystery/](https://web.archive.org/web/2013/https://dyn.com/blog/chinas-18-minute-mystery/) — try the Web Archive if the direct link 404s.
- **Congressional coverage:** [US-China Economic and Security Review Commission 2010 Annual Report](https://www.uscc.gov/annual-report/2010-annual-report-congress) — pages on the China Telecom incident (search the PDF for "China Telecom").
- **The "why did most people not notice" cold-call answer** is worth landing in class:
  1. China Telecom announced the *same* prefix length, not more-specific. So BGP's best-path selection came down to *shortest AS path* — many routers kept the legitimate route.
  2. Traffic still reached the destination via a detour — no black hole, just a surveillable path. The scary part isn't the outage; it's the silent detour through a state-controlled network.
- **Follow-on:** Similar hijacks continue. See MANRS's ongoing [incident reports](https://www.manrs.org/resources/) and BGPmon coverage.

---

## Hijacks Cut Both Ways: Pakistan & YouTube

- **The 2008 incident:** [RIPE NCC analysis (Feb 2008)](https://www.ripe.net/publications/news/industry-developments/youtube-hijacking-a-ripe-ncc-ris-case-study/) — the definitive technical walkthrough of the 24-minute global YouTube outage caused by Pakistan Telecom trying to block YouTube domestically.
- **The mechanism:** longest-prefix match. Pakistan advertised `208.65.153.0/24` (more specific than YouTube's `208.65.152.0/22`); routers globally preferred the more-specific. YouTube responded by advertising *two* `/25`s to reclaim traffic — a Renesys engineer called it *"an absolute hack, in the finest sense of the word."*
- **Lesson to draw:** BGP censorship is *coarse and leaky* — hard to keep inside one country. Pakistan's *intent* was purely domestic; the *effect* was global. This is the "border in name only" property of BGP that makes it appealing as a total-blockade tool (Egypt 2011) and dangerous as anything more targeted.

---

## BGP as a Kill Switch — and Its Defenses

- **Egypt Jan 2011:** [Renesys / James Cowie, "Egypt Leaves the Internet"](https://en.wikipedia.org/wiki/BGP_hijacking#Notable_incidents) (originally on the Renesys blog, now archived). The topical companion is Access Now's [KeepItOn](https://www.accessnow.org/keepiton/) shutdown tracker, which continues to catalogue BGP-level and other shutdowns worldwide.
- **RPKI (Resource Public Key Infrastructure):** [RFC 6480](https://datatracker.ietf.org/doc/html/rfc6480) family, 2012+. Prefix owners sign Route Origin Authorizations (ROAs); routers validate. Current adoption stats: [NIST RPKI monitor](https://rpki-monitor.antd.nist.gov/) — roughly 50%+ of announced IPv4 space is now covered, but validation-side adoption at ASes is what actually matters, and that lags.
- **MANRS (Mutually Agreed Norms for Routing Security):** [manrs.org](https://www.manrs.org/) — the Internet Society's voluntary norms initiative.
- **Contrast with DNS:** if a DNS resolver lies, you switch resolvers. If BGP withdraws your route, there's *no route* — you can't switch. That's why BGP is the tool of last resort (or first, in a total shutdown).

---

## Block Pages: Censorship You Can See

- **The measurement classic:** Jones et al., ["Automated Detection and Fingerprinting of Censorship Block Pages" (IMC 2014)](https://conferences.sigcomm.org/imc/2014/papers/p299.pdf) — the fingerprint work behind the slide's table. Detects vendor by header/comment signatures.
- **The commercial vendors named on-slide:**
  - **FortiGuard / Fortinet:** [fortiguard.com](https://www.fortiguard.com/) — commercial URL-filtering service embedded in Fortinet firewalls.
  - **Netsweeper (Canadian):** deployed by many state censors; Citizen Lab has documented deployments in [Yemen, Bahrain, Kuwait, UAE, and more](https://citizenlab.ca/tag/netsweeper/).
  - **Websense / Forcepoint:** enterprise-grade URL categorization. Citizen Lab has also documented [Websense deployments](https://citizenlab.ca/) in state censor stacks.
  - **Squid + WireFilter:** open-source, common in smaller-scale ISP filtering.
- **Detection trick from the book:** block pages are usually *much shorter* than the real page. A simple length comparison is often enough — no ML required.
- **Mechanisms drift.** Thailand switched vendors multiple times; OONI can plot the shifts on their [Explorer](https://explorer.ooni.org/).

---

## Encryption Is Eroding On-Path Filtering

- **The arc of the deck (and the course) in one slide.** As encryption closes each window, censors move to coarser tools and further up the stack.
- **SNI filtering — the last cleartext frontier:** works because TLS's ClientHello sends the target hostname in the clear for virtual-hosting purposes. Iran, China, Russia all deploy SNI-based filtering.
- **ECH (Encrypted Client Hello) — the response.** [Cloudflare's ECH announcement (Sep 2023)](https://blog.cloudflare.com/announcing-encrypted-client-hello/). Firefox and Chrome now support it; server-side adoption is what's currently limited.
- **The blocking-ECH counter-response** — Russia (Aug 2024), China (ongoing). This is a live cat-and-mouse.
- **Where it goes next:** platforms. Instagram, TikTok, YouTube each control what reaches users at the *application* layer, regardless of what happens at the network layer. That's the Ch. 3 setup.

---

## Throttling Slows Instead of Blocks

- **The Russia-YouTube case (2024–2025):**
  - Carnegie Endowment analysis (Feb 2025): search "Carnegie Russia YouTube throttling" — [alexei-miroshnichenko-russias-youtube-throttling](https://carnegieendowment.org/politika/eng/) is the general area.
  - OONI's technical walkthrough: [OONI report on YouTube in Russia (2024)](https://ooni.org/post/2024-russia-throttles-youtube/) — SNI-based throttling on `googlevideo.com`, dropping packets to cap video quality.
  - **DFRLab's detailed technical analysis (Jan 2025):** [DFRLab "Russia's slow-motion YouTube ban"](https://dfrlab.org/2025/01/31/how-russia-throttled-youtube-for-domestic-audiences/).
  - **The killer stat:** YouTube fell from ~43% of Russian internet traffic pre-throttle to 6–12% by Jan 2025, without a formal block.
- **Iran throttling of Instagram/WhatsApp** — long-running deniable throttling. [OONI 2022 Iran report](https://ooni.org/post/2022-iran-technical-multistakeholder-report/).
- **Roya Ensafi's group on throttling detection:** ["Detecting Global Network Filters Using ICMP Rate Limiting Side Channel"](https://ensa.fi/) — search her publication list for the specific paper on throttling detection at Censored Planet.
- **This slide is the *perfect* embodiment of Roberts's friction concept from Chapter 1.** No block page, no error, just "YouTube is slow lately." Roskomnadzor never had to admit a block; usage collapsed anyway; VPN demand spiked. The presenter today (net-neutrality lecture) tied this back to the same idea.
- **Throttling is the hardest to *reliably* detect.** Congestion, backhaul issues, and QoS all produce similar signatures. Chapter 5 comes back to this.

---

## Comparing the Techniques

- **Book Table 2.2.** The synthesis: easier-to-deploy (DNS) also easier to circumvent and detect; heavier hammer (BGP) is hard to aim and has global collateral; throttling trades bluntness for *deniability*.
- **The core observation:** censors mix techniques because no single technique is cheap, precise, invisible, *and* effective all at once. Everything is a trade-off across those axes.
- **Callback to Ch. 1's friction/flooding/fear:** DNS and TCP/RST tend to be *fear* (visible), block pages are *fear*, throttling is *friction* (deniable). BGP is fear at the extreme.

---

## Takeaways

- **The Internet's original trust assumptions are the root cause.** RFC 3439 + design-philosophy paper are the anchors if a student wants primary sources.
- **DNS: easy up, easy down.** The first layer censors reach for, and the first layer users circumvent (`8.8.8.8`, `1.1.1.1`, DoH). Encrypted DNS *centralizes* the problem — good for confidentiality against ISPs, bad for concentration risk against the resolver operator.
- **BGP: rare but devastating.** Egypt 2011, China Telecom 2010, Pakistan/YouTube 2008. RPKI/MANRS are the defenses, and adoption still isn't universal.
- **Encryption keeps pushing the frontier up the stack.** TLS closed content inspection; SNI was next; ECH is closing SNI; blocking ECH is the current front line; the next escalation is platform-layer control (Ch. 3).
- **Ch. 5 (Measurement) will show *how we know all this*** — including which of today's stories are grounded in careful measurement (Turkey 8.8.8.8, Russia YouTube) and which lean on partial evidence.

---

## Companion reference — reading responses (today's discussion)

If a student's reading-response themes come up while you're at the whiteboard:

- **Deniability / friction / flooding:** [Roberts, *Censored* (Princeton 2018)](https://press.princeton.edu/books/hardcover/9780691178868/censored) is the canonical citation. The King/Pan/Roberts APSR paper on collective-action-focused censorship is [here (PDF)](https://gking.harvard.edu/files/censored.pdf).
- **50-cent party / flooding:** [King, Pan & Roberts (2017), APSR — "How the Chinese Government Fabricates Social Media Posts for Strategic Distraction"](https://gking.harvard.edu/50c).
- **Consolidation of power / Matt Prince:** the Daily Stormer post is [here](https://blog.cloudflare.com/why-we-terminated-daily-stormer/); 8chan is [here](https://blog.cloudflare.com/terminating-service-for-8chan/); Kiwi Farms is [here](https://blog.cloudflare.com/kiwifarms-blocked/). The Nov 18, 2025 Cloudflare outage post-mortem is [here](https://blog.cloudflare.com/18-november-2025-outage/) — good live-example for the "one company outages millions" point.
- **AI-in-the-moderation-loop:** [Meta's transparency page on automation](https://transparency.meta.com/en-gb/enforcement/detecting-violations/technology-detects-violations/); [OpenAI's writeup on GPT-4-assisted moderation](https://openai.com/index/using-gpt-4-for-content-moderation/).
- **Dead Internet theory:** [Wikipedia](https://en.wikipedia.org/wiki/Dead_Internet_theory); [The Atlantic (Aug 2021)](https://www.theatlantic.com/technology/archive/2021/08/dead-internet-theory-wrong-but-feels-true/619937/).
- **Filter-bubble / point-of-no-return:** Pariser, [*The Filter Bubble* (2011)](https://www.ted.com/talks/eli_pariser_beware_online_filter_bubbles); [Google Personalized Search launch (Dec 2009)](https://googleblog.blogspot.com/2009/12/personalized-search-for-everyone.html).

---

## Companion reference — Net Neutrality presentation (Chapter 4 preview)

If the day's presenter references come back up in Q&A or the breakout:

- **Tim Wu's original paper:** ["Network Neutrality, Broadband Discrimination" (2003)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=388863).
- **FCC 2015 Open Internet Order:** [FCC document](https://www.fcc.gov/document/fcc-releases-open-internet-order). **2017 repeal:** [Restoring Internet Freedom](https://www.fcc.gov/document/fcc-releases-restoring-internet-freedom-order). **2024 Biden reinstatement (vacated Jan 2025):** [FCC page](https://www.fcc.gov/document/fcc-restores-net-neutrality).
- **6th Circuit Jan 2, 2025 decision** vacating the 2024 rules: [court opinion PDF](https://www.opn.ca6.uscourts.gov/opinions.pdf/25a0002p-06.pdf). Summary: [Wikipedia — Net neutrality in the United States](https://en.wikipedia.org/wiki/Net_neutrality_in_the_United_States).
- **Comcast v. FCC (2010)** — BitTorrent throttling: [Wikipedia](https://en.wikipedia.org/wiki/Comcast_Corp._v._FCC). **Verizon v. FCC (2014):** [Wikipedia](https://en.wikipedia.org/wiki/Verizon_Communications_Inc._v._Federal_Communications_Commission).
- **Zero-rating cases:** [Facebook Free Basics / Internet.org](https://en.wikipedia.org/wiki/Internet.org); [T-Mobile Binge On / Music Freedom](https://en.wikipedia.org/wiki/T-Mobile_US#Binge_On_and_Music_Freedom).
- **5G network slicing (today's presenter):** [3GPP TS 23.501 / network slicing overview](https://www.3gpp.org/technologies/network-slicing); [Belli & Ferrer, "Network Slicing and Net Neutrality" (2019)](https://academic.oup.com/idpl/article/9/4/263/5581459); [Barbara van Schewick on QoS and non-discrimination](https://netarchitecture.org/).
- **EU frameworks:** [Regulation 2015/2120](https://eur-lex.europa.eu/eli/reg/2015/2120/oj); [BEREC net-neutrality guidelines](https://www.berec.europa.eu/en/document-categories/berec/regulatory-best-practices/guidelines/berec-guidelines-on-the-implementation-of-the-open-internet-regulation).
- **Real 5G slice deployments** (in case a student asks "is this happening?"): [T-Mobile Advanced Network Solutions](https://www.t-mobile.com/business/solutions/networking); [Verizon 5G Business Internet](https://www.verizon.com/business/products/networks/connectivity/5g-business-internet/); [DISH standalone-5G slice trials](https://about.dish.com/2023-06-13-DISH-Wireless-and-Boost-Infinite-Successfully-Test-Nations-First-Network-Slicing-Service-on-Smartphones).

---

## Companion reference — measurement tools (Chapter 5 preview)

- **OONI (Open Observatory of Network Interference):** [ooni.org](https://ooni.org/) · [Explorer](https://explorer.ooni.org/).
- **Censored Planet:** [censoredplanet.org](https://censoredplanet.org/) · [2020 IMC paper](https://censoredplanet.org/).
- **ICLab (University of Massachusetts):** [iclab.org](https://iclab.org/).
- **Google Transparency Report:** [transparencyreport.google.com](https://transparencyreport.google.com/).
- **SFLC.in India Internet Shutdown Tracker:** [internetshutdowns.in](https://internetshutdowns.in/).
- **Access Now KeepItOn:** [accessnow.org/keepiton](https://www.accessnow.org/keepiton/).
- **Freedom House Freedom on the Net:** [freedomhouse.org/report/freedom-net](https://freedomhouse.org/report/freedom-net).

---

## Recent events (2024–2026) — quick-grab reference

**Grouped by lecture topic so you can pull a fresh anchor mid-slide. Everything below is verified live this session unless noted.**

### DNS-layer — recent

- **Cloudflare 1.1.1.1 outage — July 14, 2025.** Global DNS resolution failure for ~1 hour; affected an enormous share of DoH users. Post-mortem: [Cloudflare blog](https://blog.cloudflare.com/cloudflare-1-1-1-1-incident-on-july-14-2025/). The single-point-of-failure argument for encrypted-DNS centralization writes itself.
- **Cloudflare-wide Nov 18, 2025 outage.** Broader (not just 1.1.1.1) — knocked X, ChatGPT, and a large fraction of the top-1M sites offline. [Cloudflare blog post-mortem](https://blog.cloudflare.com/18-november-2025-outage/) · [CNBC coverage](https://www.cnbc.com/2025/11/18/cloudflare-down-outage-traffic-spike-x-chatgpt.html).
- **Quad9 vs. Sony Music (Germany, 2023 → ongoing).** German regional courts ordered Quad9 to block piracy domains at the DNS-resolver layer. Latest developments and appeals: [Quad9 press room](https://www.quad9.net/news/press/). Coverage: [TorrentFreak](https://quad9.net/news/blog/quad9-turns-the-sony-case-around-in-dresden/). This is the modern "compel-one-resolver-to-block-millions" case in real courts.
- **DNS4EU (Jan 2024 launch).** The EU's public-DNS sovereignty initiative — European regulatory-friendly resolver. [joindns4.eu](https://www.joindns4.eu/).
- **South Korea network-usage-fee fight (2024–2025).** ISPs' pressure on Cloudflare and content networks; adjacent to but distinct from DNS-level manipulation. Search "Korea network usage fee 2024" for the ongoing coverage.

### TCP / RST / GFW — recent

- **GFW blocks ECH (2024).** Community-run tracker: [Great Firewall Report on GitHub](https://github.com/net4people/bbs/issues). USENIX FOCI 2024 has the academic writeups.
- **Russia blocks ECH (Aug 2024).** Roskomnadzor blocked Cloudflare's ECH configuration. [Meduza coverage](https://meduza.io/en/news/2024/11/08/russia-s-internet-censor-demands-a-break-from-cloudflare-after-the-american-company-enabled-new-privacy-tools-last-month).
- **Iran's continuous SNI-based filtering.** OONI ongoing measurement: [Iran country page on OONI Explorer](https://explorer.ooni.org/country/IR).

### BGP — recent + evergreen

- **Meta / Facebook Oct 4, 2021 outage (six hours globally).** BGP withdrawal + intra-DNS dependency + physical-access-lockout — the canonical modern case study of BGP as an unintentional kill switch. Post-mortem: [Facebook engineering blog](https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/) · [Cloudflare's outside analysis](https://blog.cloudflare.com/october-2021-facebook-outage/). This is the *"BGP is life support and life kill-switch"* live example — great pair with Egypt 2011.
- **AT&T nationwide outage Feb 22, 2024.** ~12-hour US cellular outage caused by a peering-configuration error during network expansion. Not a BGP hijack per se, but a routing-config kill-switch adjacent case: [FCC report on the outage](https://docs.fcc.gov/public/attachments/DOC-402609A1.pdf) · [AT&T's own statement](https://about.att.com/story/2024/network-update.html).
- **KlaySwap BGP hijack (Feb 3, 2022).** South Korean DeFi exchange lost ~$1.9M when attackers hijacked a `/24` to redirect a JavaScript dependency. Great "BGP-as-attack-vector" case: [Krebs on Security summary](https://krebsonsecurity.com/2022/02/wazawaka-goes-waka-waka/) — search for the KlaySwap-specific technical writeups if you want more.
- **RPKI adoption 2025 milestones.** [NIST RPKI monitor](https://rpki-monitor.antd.nist.gov/). Adoption crossed 55% of announced IPv4 prefixes globally in early 2025; validation adoption at the AS level lags substantially.
- **Rostelecom hijack of ~8,700 prefixes (Apr 2020).** [Cloudflare blog analysis](https://blog.cloudflare.com/tag/bgp/) — Google, Amazon, Facebook among the hijacked prefixes for hours. Old-ish but the definitive "why we need RPKI" story.

### Shutdowns / throttling — recent

- **Iran Sep–Nov 2022 Mahsa Amini protests shutdown.** Access Now / OONI multi-stakeholder report: [OONI 2022 Iran report](https://ooni.org/post/2022-iran-technical-multistakeholder-report/) — the largest recent state-directed censorship escalation, mixing DNS, SNI, and throttling.
- **Russia YouTube throttling 2024–2025** (already in the throttling slide above): [OONI report](https://ooni.org/post/2024-russia-throttles-youtube/) · [DFRLab technical analysis](https://dfrlab.org/2025/01/31/how-russia-throttled-youtube-for-domestic-audiences/). Killer stat: YouTube fell 43% → 6–12% of Russian traffic without a formal block.
- **Pakistan X (Twitter) blocked Feb 2024 → ongoing.** Around the Feb 8 elections and continuing through 2025. OONI: [ooni.org/post/2024-pakistan-blocks-x](https://ooni.org/post/2024-pakistan-blocks-x/).
- **Bangladesh internet blackout, July–Aug 2024.** Nationwide during anti-government protests. [Access Now writeup](https://en.wikipedia.org/wiki/2024_Bangladesh_internet_blackouts).
- **India Manipur shutdowns 2023–2024.** Longest sustained shutdown of any democracy in recent years. [SFLC.in tracker](https://internetshutdowns.in/) has the running list.
- **Access Now KeepItOn 2025 report.** 313 shutdowns / 52 countries; India remains highest. [accessnow.org/internet-shutdowns-2025](https://www.accessnow.org/internet-shutdowns-2025/).
- **Freedom House "Freedom on the Net" 2025.** Roughly two-thirds of internet users under some form of restriction. [freedomhouse.org/report/freedom-net/2025](https://freedomhouse.org/report/freedom-net).

### Consolidation as kill-switch — recent

- **Cloudflare Nov 18, 2025 outage** (see DNS section above).
- **AWS us-east-1 outages** — recurring reliability lessons. Search AWS Health Dashboard historical events for 2024–2025 major incidents.
- **Matt Prince quote, Aug 16, 2017** (Daily Stormer termination): [Cloudflare blog post](https://blog.cloudflare.com/why-we-terminated-daily-stormer/) — the definitive statement of the "unelected-arbiter" problem: *"Literally, I woke up in a bad mood and decided someone shouldn't be allowed on the Internet. No one should have that power."* Followed by 8chan (Aug 2019) and Kiwi Farms (Sept 2022) terminations.
- **DNS4EU launch (Jan 2024)** — EU's response to US-DNS-provider dominance (see DNS section).

### Platform-layer / application (foreshadowing Ch. 3)

- **US TikTok divestment law — signed Apr 2024, upheld Jan 2025.** [Wikipedia — Protecting Americans from Foreign Adversary Controlled Applications Act](https://en.wikipedia.org/wiki/Protecting_Americans_from_Foreign_Adversary_Controlled_Applications_Act). Live example of platform-level forced-removal as state action.
- **UK Ofcom Online Safety Act enforcement, 2025–2026.** First major fines under the OSA — 4chan, AVS Group, Kick.com, Imgur among the first targets. [Ofcom enforcement page](https://www.ofcom.org.uk/online-safety) · Inforrm analysis: [inforrm.org/2026/03/11/ofcom-steps-up-online-safety-act-enforcement](https://inforrm.org/2026/03/11/ofcom-steps-up-online-safety-act-enforcement-with-two-further-age-assurance-fines-for-pornographic-platforms-alexandros-antoniou/).
- **UK ICO £14.47M fine against Reddit (2026).** [ICO announcement](https://ico-newsroom.prgloo.com/news/ico-issues-reddit-with-gbp-14-47m-fine-for-childrens-privacy-failures). Data-protection lever (ICO) is separate from content lever (Ofcom) — worth naming the two-regime coordination.
- **Australia under-16 social-media ban (Dec 10, 2025).** [eSafety Commissioner overview](https://www.esafety.gov.au/about-us/industry-regulation/social-media-age-restrictions) · [NPR coverage](https://www.npr.org/2025/12/10/nx-s1-5639694/social-media-ban-children-australia).
- **EU DSA age-verification wallet (Apr 2026).** Search the [European Commission Digital Strategy site](https://digital-strategy.ec.europa.eu/) for the age-verification wallet page.
- **Nepal social-media ban (Nov 2023).** Government blocked 26 platforms — TikTok, Facebook, YouTube among them. [Reuters coverage](https://en.wikipedia.org/wiki/Censorship_in_Nepal).
- **Apple removed VPN apps from Russian App Store (2024).** Ongoing compliance-with-local-law removals. [WashPost / Reuters coverage available; search "Apple VPN Russian App Store 2024"].
- **Google Play removal of VPN apps in India (2024).** Under CERT-In rules. Similar pattern to the Russian removals.

### 5G network slicing — deployment as of 2024–2026

- **T-Mobile Advanced Network Solutions.** Commercial 5G slicing offering: [T-Mobile page](https://www.t-mobile.com/business/solutions/networking).
- **Verizon 5G slicing for first responders and enterprise.** [Verizon 5G Business Internet](https://www.verizon.com/business/products/networks/connectivity/5g-business-internet/).
- **AT&T 5G+ / private network offerings.** Public overview at [business.att.com](https://www.business.att.com/products/private-cellular-network.html).
- **DISH first-standalone-5G-slice launch (June 2023).** [DISH announcement](https://about.dish.com/2023-06-13-DISH-Wireless-and-Boost-Infinite-Successfully-Test-Nations-First-Network-Slicing-Service-on-Smartphones).
- **GSMA network slicing report (2024).** [PDF](https://www.gsma.com/newsroom/wp-content/uploads/NG.116-v3.0.pdf) — commercial-deployment landscape.

### Net Neutrality — most recent legal state

- **6th Circuit Jan 2, 2025 — *In re: MCP No. 185*** vacating the FCC's 2024 rules: [court opinion PDF](https://www.opn.ca6.uscourts.gov/opinions.pdf/25a0002p-06.pdf) · Wikipedia summary: [Net neutrality in the United States](https://en.wikipedia.org/wiki/Net_neutrality_in_the_United_States).
- **State-level net neutrality laws (still active despite FCC turmoil):** California SB 822 (2018), Washington, Oregon, Vermont. Live tracker: [BroadbandNow state map](https://en.wikipedia.org/wiki/Net_neutrality_law).
- **India differential-pricing / zero-rating ban (2016, still in force).** [TRAI order text](https://en.wikipedia.org/wiki/Net_neutrality_in_India).
- **BEREC's ongoing net-neutrality review.** Current [Open Internet Regulation review page](https://www.berec.europa.eu/en).

### Filter bubble / AI / dead-internet (foreshadowing Ch. 3)

- **Meta's LLM-based first-line moderation** — [Meta transparency page](https://transparency.meta.com/en-gb/enforcement/detecting-violations/technology-detects-violations/).
- **OpenAI GPT-4 for content moderation** — [OpenAI writeup](https://openai.com/index/using-gpt-4-for-content-moderation/).
- **AI-generated content flooding — the "flooding" theme, updated.** New York Times / Wired coverage of AI-generated content on X, TikTok, and news sites through 2024–2026. Search "AI slop internet 2024" for the current-events framing.
- **Dead-internet theory** — updated framing given LLM-generated bot activity. Wikipedia's [Dead Internet Theory](https://en.wikipedia.org/wiki/Dead_Internet_theory) page tracks the evolving evidence.

---

## Course logistics

- **Course home:** [noise-lab.github.io/censorship-course](https://noise-lab.github.io/censorship-course/)
- **Syllabus:** [/syllabus](https://noise-lab.github.io/censorship-course/syllabus)
- **Discussion doc — DNS:** [/breakouts/dns](https://noise-lab.github.io/censorship-course/breakouts/dns)
- **Discussion doc — Secure DNS:** [/breakouts/secure-dns](https://noise-lab.github.io/censorship-course/breakouts/secure-dns)
- **Reading-response `#responses` Slack channel** — created today; students post there for shared threads.
- **Next lecture:** BGP Hijacking (Chapter 2, Routing) — hands-on with RouteViews.
