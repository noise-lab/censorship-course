## Agenda — Autumn 2026 (Chicago)

Two 80-minute meetings per week, Tuesdays and Thursdays. Notes are reconstructed from the class recordings after each meeting; where a recording did not capture something (small-group discussion, report-backs) the entry says so rather than guessing.

### Meeting 1 (Tue Sep 29)

* **Introductions and setup**
    * Course TA: Anna Lorimer, who researches in this area and is the first stop for project ideas. She will also give some lectures
    * Done in class: join Slack, create a private GitHub repository, give `feamster` read access (Settings, Collaborators), and fill out the intake form
* **Course mechanics**
    * The course page is a GitHub page embedded in Canvas. The only thing to take from Canvas is the book PDF; a newer copy will be posted
    * Eighteen class topics, taken in sequence, roughly one per meeting. No dates on the schedule, on purpose
    * Each topic has a discussion (breakout) and a hands-on activity. With 80 minutes we usually do one; the class can say which it prefers
    * **Reading responses:** one per week, due Tuesday 9 am (this first week only, Thursday). No summary. Just the questions you had after reading, a technical clarification you want, or something you want discussed. One sentence is enough. Graded done or not done. They set the agenda for that day's discussion
    * **Presentations:** done in groups, on a topic of your choosing (a suggested list or a current event). Sign up in the linked sheet, three or four people per slot, starting in about two weeks. Link your slides in the sheet; past terms' slides are there as examples
    * **Participation:** this is a discussion class. Show up and take part
    * **Group research project:** a proposal is due **Friday October 23** (end of week 4): what you will do, with whom, why it is interesting, what has been done before, and what you need (data, tools) to finish. Talk to Anna before writing it. Past projects are on the linked YouTube playlist
        * If stuck for ideas: measurement projects (transparency reports, firewall, VPN, and Tor measurements; look ahead to chapter 5), or how AI models moderate prompts and outputs
    * Typical meeting: reading-response questions, a student presentation when one is scheduled, a short lecture, then a breakout or hands-on
    * **Discussion norms:** topics here touch contested issues. Respect differing views and approach them with curiosity. The instructor will not offer personal opinions on normative questions, so as not to put a thumb on the scale
* **Course overview**
    * History: the topic began around 2000 as the Great Firewall of China blocking web pages, then spread to other countries
    * **Technical controls** (weeks 1 to 3, the most technical part; no prerequisites): manipulating name lookups (DNS), connections (transport), and routes; slowing traffic (throttling); taking services offline (denial of service)
    * **Platform controls:** content moderation, flooding, propaganda, disinformation, personalization
    * **Legal and economic controls:** copyright, net neutrality, zero rating, demonetization
    * **Measurement:** tools for technical measurement; transparency reports
    * **Responses:** circumvention with VPNs and Tor
* **Chapter 1 framing: from censorship to information control**
    * Outright blocking is the crudest form. The broader idea is anything that makes information harder to get: a tax on access
    * Margaret Roberts, *Censored*: **fear** (deterring people from publishing or reading), **friction** (making access slow or costly), and **flooding** (burying information under other content)
    * Blocking is obvious and provokes a reaction. If the goal is to stay in power, friction and flooding can work better because people may never notice
    * Not only authoritarian states: by one widely cited estimate about two thirds of the world's internet users are subject to some form of information control, and democracies order shutdowns too (India was the example)
* **Breakout (short): age verification**
    * Prompt: *Age verification requirements for online platforms are legitimate and should not be considered a form of information control.* Agree, disagree, or "it depends, on what?"
    * Context given: rules aimed at under-13 and under-16 users, Australia's under-16 ban, and recent US litigation against Meta
    * Verification is imperfect: self-declared birthdays, guessing from posted content, facial age estimation that works poorly near 13 and 16. A wrong call removes a legitimate speaker, the same problem as a spam filter's false positives
    * Points from the report-back: ID requirements raise privacy problems, especially for minors; users who are blocked go elsewhere
* **For Thursday:** a reading response, and read section 2.2.1 on DNS

### Meeting 2 (Thu Oct 1)

* **Reading-response discussion**
    * **Who decides what is acceptable to censor?** The Cloudflare and Daily Stormer example from the reading. A student's framing: the only practical difference between cases we approve of and cases we would not is that one company's chief executive agreed. Is there a principled line, and should any single party hold it?
    * **Platform, publisher, or pipe?** Cloudflare is infrastructure, not a publisher. Platforms argue whichever role suits the moment: "just a platform" for liability (Section 230, later in the course), "entertainment" in a current tax dispute with the City of Chicago
    * **Current events:** European regulators, at the request of sports rights holders, have ordered the public resolvers run by Cloudflare, Google, and Cisco to stop resolving piracy sites
    * **Consolidation cuts both ways.** A few companies now resolve names for most users, which was not always so. Ideas for re-decentralizing came up (radio mesh networks, blockchain-based naming). Counterpoint raised by a student: Starlink in Iran is a highly consolidated provider that helps people get around state blocking, yet access then depends on that one company's choices
    * **Can ordinary variation be mistaken for manipulation?** DNS answers differ by location by design. This led into the hands-on
* **Hands-on: DNS lookups from different locations** (about 10 minutes)
    * Look up google.com with `dig`, then again through a VPN in another location. The answers differ
* **Discussion: how would you detect DNS manipulation, given that answers legitimately vary?**
    * Check whether the answer is plausibly nearby, using latency (`ping`) or the path (`traceroute`); a "local" answer that is far away is suspicious
    * Check consistency within one geography. Load balancing and failover still cause some change
    * Check who owns the returned address (`whois`)
    * Fetch the content and compare; personalization makes this unreliable
    * Compare the TLS certificate presented
    * None is perfect. In general this is hard, which is why measurement studies of DNS manipulation are difficult
    * DNSSEC was set aside for time
* **Encrypted DNS (DNS over HTTPS)**
    * By default your operating system sends unencrypted lookups to a local resolver supplied by the network you joined. Anyone on the path can see and alter them
    * DNS over HTTPS moves lookups into the browser and encrypts them to a chosen provider: Cloudflare by default in Firefox, Google in Chrome. Introduced roughly ten years ago by Mozilla and Cloudflare; turning it on by default was controversial
    * Benefit: on-path parties can no longer see or tamper with lookups
    * Cost: you must trust the resolver operator, and resolution that used to be spread across many networks is concentrated in a few companies, a new chokepoint
    * Usability: only two students had heard of it. The settings are hard to interpret, and an attempt in class to point the browser at a different public resolver did not work. Left as an exercise
* **Breakout: is centralized encrypted DNS a net gain or a net loss for user autonomy?**
    * For: encryption, and cases like Turkey where a large public resolver helped users get around local blocking
    * Against: one operator can refuse to resolve a name for everyone, and most users would never know why a page failed to load
    * The recording did not capture the group discussion or report-back

### Meeting 3 (Tue Oct 6)

(The recording begins partway into the reading-response recap.)

* **Reading-response themes**
    * The same mechanism serves protection and censorship: a firewall at a school, a hospital, or a national border looks identical to the user whose connection fails. How do we disambiguate protection from censorship?
    * Encryption removes the fine-grained signals a censor used to have, so the response is coarser: block all encrypted traffic, or a whole site rather than one page. Is that a win?
    * As traffic concentrates in fewer content delivery networks and hosting providers, each chokepoint becomes more powerful
    * The arms race: if the censor can always find another way, is it worth raising the cost? This is where the course's wider framing returns: when blocking gets expensive, control shifts to friction, flooding, and platforms
    * About half the class had responses in by Tuesday; updates before Thursday are welcome and still shape the discussion
* **TCP mechanics (for the questions asked)**
    * The three-way handshake: SYN (synchronize), SYN-ACK, ACK. Drawn as two machines, client on the left, server on the right
    * It is the Two Generals problem: nobody ever learns whether the final ACK arrived. The sender simply starts sending data. Teardown (FIN, acknowledgments in both directions) has the same property
    * A reset (RST) aborts a connection or refuses one. Normal uses: a SYN sent to a port with no listener gets a reset ("go away"); a killed process; any fast teardown
    * Forged resets: the Great Firewall watches for a SYN to a blocked destination and sends a reset to the client, which aborts regardless of what the server later replies
    * "Ignoring the Great Firewall of China" (Cambridge, 2006): if the client simply ignores resets, the connection proceeds. It worked because the firewall was stateless, sending a reset and forgetting the connection. The firewall later reset both ends
    * Injecting a duplicate or a reset requires being **on the path**: a router or other equipment between client and server, which in practice means a government or an ISP. The forged packet must carry a plausible sequence number; sequence numbers are 32-bit, visible in the clear (TLS does not encrypt TCP headers), and because a reset is accepted anywhere inside the receiver's window they can be brute-forced if necessary (correction: 16-bit was said in class)
    * The economics: an on-path censor only has to win a race, sending its packet before the real reply, so the manipulation is cheap once the vantage point exists
* **Why transport-layer manipulation is becoming less attractive**
    * Encryption hides content, and shared hosting (one cloud or CDN address serving many sites) means an IP address no longer identifies a site
    * Censors answer with **website fingerprinting**: even encrypted, a page has a characteristic number of objects and sizes and a characteristic timing, which together act as a fingerprint of the site being visited
    * Questions from the room: oblivious DNS does not help here (it protects the lookup, not the transfer sizes); padding traffic with extra data does help and is the standard defense, with a large research literature behind it
    * Net: on-path manipulation needs a vantage point plus fingerprinting; friction, flooding, and platform-level controls are easier. Techniques for detecting TCP manipulation return in the measurement unit
* **Breakout B (short): is the cat-and-mouse game winnable?**
    * Prep-read tour: QUIC, a newer transport developed by Google and used by Chrome, encrypts more of the connection setup and can split a connection across paths, which raises new censorship questions. Tor's pluggable transports exist to protect the initial connection to the network, which is the sensitive moment for any VPN-like tool; each transport (obfs4, then Snowflake) gets fingerprinted in turn, and Russia recently blocked Snowflake. VPNs move the trust problem to the provider
    * Report-back: censors have many tools and take the path of least resistance, which can be economic or legal rather than technical. The asymmetry runs both ways: a circumventing user must hide every aspect of their traffic while the censor needs to spot one anomaly, but the censor must close every channel while the user needs one that works
    * Can traffic evade increasingly good machine-learning detection? Open question; flagged as a project direction (pit detection models against generative evasion). The role of AI in this race was deferred
* **DNSSEC (secure DNS, as distinct from encrypted DNS)**
    * The resolver walks the hierarchy: root, then the `.edu` servers, then the `uchicago.edu` servers; each step is a referral
    * With DNSSEC each referral is signed. A signature is made with a private key and checked with the matching public key; the referral carries the next zone's key, signed by the zone above it. This is **integrity**, not confidentiality: encrypted DNS hides queries, DNSSEC proves answers were not altered
    * The chain starts at the root key, which ships with the operating system or software. Same root-of-trust question as certificates: you have to start by trusting something
    * What it defends against: an on-path forged answer cannot carry a valid signature, so it is rejected. What it does not: a compromised root key, or a bad key added to the root store. Keys have been added to and removed from operating-system root stores over the years. This is a quieter form of consolidation: whoever holds a root key controls everything below it
    * Demo: the operating system's keychain lists the root certificates it trusts; most users never look
* **Hands-on: `dig` with DNSSEC**
    * `dig +dnssec` shows the signature records (RRSIG). `+trace` shows the full iteration from the root, with each referral, its signature, and a DS record pointing at the next zone's key
    * UChicago's domain is now signed, which it was not a year ago; so is a major news site. Deployment is far broader than when the exercise was written. Task: find a domain that is not signed
* **Parked for Thursday**
    * Why DNS manipulation is so much more common than routing (BGP) manipulation, and the other BGP questions from this week's responses
* **Logistics**
    * Presentations start in about two weeks; sign up if you have not

### Meeting 4 (Thu Oct 8)

* **Housekeeping**
    * Most week-2 responses are in; the few who have not should push them. Sign up for presentations, which start the week after next. Project proposals are due **Friday October 23**; Anna will help give feedback
    * Give Anna Lorimer read access to your response repository as well, if she is not already a collaborator
* **Reading-response follow-ups**
    * **Machine learning in the arms race** (asked several times): for protocol-level interference there is no obvious advantage to machine learning, as far as the instructor is aware. The question becomes much more pertinent at content moderation and platform decisions, later in the course
    * **Why DNS rather than BGP?** DNS is easier to manipulate: operate a resolver and get people to use it, then return the wrong answer. It is also harder to detect, because DNS answers vary naturally. Routing manipulation is a sledgehammer: brute force, and it works if it works. For a complete shutdown (Egypt) withdrawing routes is the easier tool, and India uses it more often than most. In general DNS is manipulated far more than routing
* **Lecture: routing and route hijacks** (book 2.2.3)
    * The internet is a collection of independently operated networks, **autonomous systems**. BGP, the Border Gateway Protocol, is simply the routing protocol those networks use to talk to one another. Directions one hop at a time: a network gets your traffic as far as its border, then the next network takes over. Not a full route the way a map app gives one; the reason is scalability (nobody can run a shortest-path computation over the whole internet), so BGP adds a layer of abstraction
    * Security is very limited. Efforts to secure routing have largely failed except for the **Resource PKI** (RPKI). Recommended easy read: Sharon Goldberg, "Why Is It Taking So Long to Secure Internet Routing?" (Communications of the ACM, 2014), the source of the diagram shown
    * **Hijacks.** Any autonomous system can advertise any block of addresses to its neighbors, and routers mostly believe what they hear and pass it on. Mistakes cause outages (at least one of the recent large cloud-provider outages was a routing misconfiguration); malicious parties can do the same deliberately
    * **Prefix arithmetic, on the board.** An address is 32 bits, four 8-bit numbers. `128.135.24.0/24` means the first 24 bits are fixed and the last 8 are a wildcard: 2^8 = 256 addresses. A `/23` fixes 23 bits and covers 2^9 = 512 addresses, so a `/24` is *more specific* (a *longer prefix*) than a `/23`. The table shows overlapping prefixes like these
    * **A student asked:** if several routers advertise the same addresses, which one does a router pick? The **most specific (longest) prefix wins**. Among routes of equal length a set of rules decides, one of the higher-priority ones being the fewest autonomous systems on the path, which is correlated with distance but need not be
    * **Fighting back.** A hijack is not something a user sees easily: a withdrawn route is obvious (no internet), but traffic quietly detouring through another country may go unnoticed. Step one is detection: a network can watch public route collectors for someone else advertising its addresses. Step two: you cannot order the hijacker to stop, but you can split your own prefix in two and advertise the halves, which are more specific and so win. This works only up to a point: if everyone advertised ever-longer prefixes the table would grow exponentially, so many routers filter or ignore prefixes longer than `/24`
    * **Questions from the room.** Could you advertise half the internet with a `/2`? You could try; it would lose to every more specific route. Is there a law against hijacking? The instructor knows of no prosecution or case law; there are legal theories but nothing tested. Who can actually do this? You need a router that another network's router is willing to believe. The barrier is not in the protocol but in the setup: convincing an operator to connect to you and speak BGP. Small ISPs enter such arrangements all the time (a university routing for a local library, for example), so it is not far-fetched. The 1997 AS 7007 incident from the reading was caused by a very small ISP
    * **A student asked:** if BGP only gives step-by-step directions, how does anything know where to send traffic? Drawn on the board from a real table entry: UChicago's `128.135.0.0/16`, reached through an intermediate provider and then Internet2, the US academic research backbone. Each network on the path only knows how to get the packet to the next border; `whois` turns the autonomous-system numbers into names
    * **A student asked:** why does withdrawing a route work; can't routers cache the old one? In theory they could and sometimes do, but a cached route cannot tell a deliberate withdrawal from a genuine failure, and reacting to failures is the whole point. The course theme again: distinguishing a legitimate failure or glitch from an intentional act, whether a route, a DNS answer, a moderation decision, or (Tuesday's topic) slow traffic
* **Hands-on: RouteViews** ([activity](../activities/bgp.md), about 20 minutes)
    * `telnet route-views.chicago.routeviews.org`, then `show ip bgp <address>` for UChicago and YouTube; `show ip bgp` alone dumps the whole table, which shows the overlapping prefixes. RouteViews is a public "telescope" of route collectors; the project also publishes historical routing data, a rich source for a project on routing manipulation
    * The old list of collectors on routeviews.org had disappeared; the activity was updated during class with the current list and a note to `brew install telnet` on recent macOS
    * The activity's discussion questions (how a censor could use hijacks, how to detect or prevent them) were covered by the lecture; the class had no further reactions to report
* **Not covered:** RPKI in detail, and the question from the responses about whether securing BGP concentrates power. Stated briefly: a centralized routing PKI means the root could revoke an autonomous system's certificate, after which other routers would drop its routes. That is a new problem that did not exist before RPKI. Breakout A (should governments mandate RPKI) was not done
* **Breakout: should an ISP refuse a government shutdown order?** ([breakout](../breakouts/bgp.md), Breakout B; about 10 minutes)
    * Framing: the same question will come back for platforms (China has asked Google to censor search results, and Google has gone back and forth on it). For ISPs: ordered to remove prefixes or shut down, should they comply? What can they do, given that refusing may cost a license or a fine? No ISP is known to have tried, or if one did, the discussions were never public. A student's earlier example of Starlink was raised as a provider that reaches into a country from outside and may not be bound the same way
    * Two variants to discuss: a complete shutdown, and the greyer case of a single prefix that is harder to notice
    * The recording did not capture the small-group discussion or the report-back
* **For Tuesday:** week-3 reading response by 9 am; read 2.3.1 on throttling
