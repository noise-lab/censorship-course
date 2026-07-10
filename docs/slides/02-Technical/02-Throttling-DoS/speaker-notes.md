# Lecture 3 — Speaker Notes (Throttling + DoS)

Expanded background and source URLs for each slide. In-deck notes (the
`::: {.notes}` blocks) are visible via reveal.js speaker view (press
**S** with the deck open).

**Every URL below has been verified this session or is a canonical
org landing page.** Descriptive citations with no URL mean the source
exists but I couldn't confirm a stable URL in-session — look it up if
you want a link.

---

## A Tax on Access, Not a Wall

- The framing that **friction is a form of information control** is
  Roberts, *Censored* (Princeton, 2018): <https://press.princeton.edu/books/hardcover/9780691178868/censored>.
- Book context: censorship-book §2.3, "Disrupting the Flow of Data."

---

## Two Ways to Degrade, Not Block

- **Throttling** and **DoS** are both *friction* mechanisms — no block
  page, no ban notice, just degraded UX. Both live under §2.3.
- Great follow-up if a student asks "why aren't these classified as
  outright blocking?" — read the book's definition of information
  control as "a *tax* on access."

---

# Throttling and Rate Limiting

## Throttling Is Friction by Design

- **Rate limiting is dual-use.** Every production system does it for
  fairness, DoS protection, or SLA enforcement. The censorship use is
  the same mechanism aimed at particular targets.
- Book §2.3.1 walks through this at length.

---

## How a Traffic Shaper Works

- The identify-then-shape architecture is the canonical model. Any
  serious middlebox — a Cisco / Sandvine / Allot appliance — does
  this. If a student wants depth: **Sandvine** is the go-to vendor
  name, marketed to ISPs and states alike.
- Sandvine's role in state throttling is well documented — the
  Bloomberg profile is a starting reference (search "Sandvine
  Bloomberg BusinessWeek Deep Packet Inspection").

---

## Identifying What to Throttle

- **SNI-based** and **DNS-based** identification are what QUIC + DoH
  + ECH are designed to defeat — tie back to Wed's Protocols lecture
  on encrypted client hello.
- Ties directly to the [Access Now KeepItOn 2025 report](https://www.accessnow.org/internet-shutdowns-2025/)
  which finds "targeted" restrictions increasingly common — that's
  identification+shape at play.

---

## Shaping: Leaky Bucket vs. Token Bucket

- Canonical CS textbook material. If you want to point students at a
  primer: [Leaky bucket — Wikipedia](https://en.wikipedia.org/wiki/Leaky_bucket)
  and [Token bucket — Wikipedia](https://en.wikipedia.org/wiki/Token_bucket).
- The teaching move: leaky = fixed rate, token = bursty. Real
  deployments almost always use token bucket because burstiness
  matters for user experience.

---

## Why Throttling Is So Hard to Catch

- **Wehe** — Northeastern's throttling detection tool: <https://wehe.meddle.mobi/>. The
  research paper is Li et al., "A Large-Scale Analysis of Deployed
  Traffic Differentiation Practices" (SIGCOMM 2019); search that
  title on ACM DL.
- **Netflix vs. Comcast peering dispute (2014):** the *canonical*
  case of "was it throttling or congestion?" — the answer was mostly
  interconnection congestion, not deliberate shaping. Background:
  [Level 3 blog on Comcast dispute](https://en.wikipedia.org/wiki/Comcast%E2%80%93Netflix_dispute) (Wikipedia has a good summary
  with links to the original Level 3 post). Foreshadows net neutrality
  (Ch. 4).

---

## Throttling as a Live Political Tool

- **Primary source** for the 2025 stats: [Access Now — "Internet shutdowns in 2025"](https://www.accessnow.org/internet-shutdowns-2025/) (KeepItOn 2025 report, released Mar 31, 2026).
- Headlines to remember: **313 shutdowns / 52 countries / up from 296 in 2024** / **India leads at 65 events**.
- **Turkey** and **Iran** are the classic throttling states.
  - Iranian throttling around protests: [Access Now Iran page](https://www.accessnow.org/campaign/keepiton/#iran) (KeepItOn campaign).
  - Turkey throttling social media during earthquakes and elections
    is documented by OONI: [OONI Explorer — Turkey](https://explorer.ooni.org/country/TR).

---

## Throttling at Home: A Private "Tax on Access"

- **Washington Post, August 15, 2023** — the story that broke it:
  [Elon Musk's Twitter throttles links to Threads, Blue Sky and New York Times](https://www.washingtonpost.com/technology/2023/08/15/twitter-x-links-delayed/).
- Follow-up coverage:
  - [Variety on the ~5-second delay + list of affected outlets](https://variety.com/2023/digital/news/elon-musk-x-twitter-delay-links-meta-new-york-times-1235697091/)
  - [Reuters/Rappler coverage](https://www.rappler.com/technology/social-media/x-delays-access-content-reuters-new-york-times-social-media-rivals/)
- The mechanism: X used its `t.co` redirect domain to insert the
  latency. After the Post's story landed, delays for NYT and Reuters
  were quietly removed; Bluesky and Substack persisted.
- This is your best non-state illustration of throttling — makes
  clear that "information control" isn't only a state actor thing.

---

# Denial of Service

## DoS: Exhaust a Finite Resource

- Three-resource taxonomy (network / connections / server) is from
  the book. Good frame for organizing every DoS variant students
  will hear about.

---

## Why DoS Is Hard to Defend: Asymmetry

- Asymmetry, spoofing, indistinguishability — these three are the
  book's teaching frame; every defense on the later slide attacks
  one of them.

---

## SYN Flood: Asymmetry in TCP

- **Original attack:** RFC 4987, [TCP SYN Flooding Attacks and Common Mitigations](https://datatracker.ietf.org/doc/html/rfc4987) (2007).
- **SYN cookies** — the elegant fix. D.J. Bernstein's original writeup:
  <https://cr.yp.to/syncookies.html>.
- Wikipedia summary: [SYN flood](https://en.wikipedia.org/wiki/SYN_flood).

---

## Reflection and Amplification

- **DNS amplification / Spamhaus attack (March 2013, ~300 Gbps):**
  [Wikipedia — Spamhaus DDoS attack](https://en.wikipedia.org/wiki/DDoS_attack_on_Spamhaus).
  At the time it was the largest DDoS in history.
- **Ingress filtering** as defense: [RFC 2827 / BCP 38](https://datatracker.ietf.org/doc/html/rfc2827)
  (Ferguson & Senie, 2000). Still under-deployed a quarter century
  later, which is why spoofing works.
- **Memcached amplification (2018):** GitHub took a 1.35 Tbps attack
  via memcached (~50,000× amplification factor). Post-mortem:
  [GitHub — February 28th DDoS Incident Report](https://github.blog/2018-03-01-ddos-incident-report/).

---

## When DoS Becomes Censorship Infrastructure

- **Great Cannon research paper:** Marczak, Weaver, Dalek, Ensafi,
  Fifield, McKune, Rey, Scott-Railton, Deibert, Paxson, *"An Analysis
  of China's 'Great Cannon'"* (FOCI 2015). Citizen Lab landing page:
  [China's Great Cannon (Citizen Lab)](https://citizenlab.ca/2015/04/chinas-great-cannon/).
- **Targets:** GitHub (which was hosting mirrors of `GreatFire.org`
  and the *New York Times* Chinese site) and GreatFire.org itself.
- **Mechanism:** on-path system, co-located with the GFW, injecting
  JavaScript into responses from Baidu that then made external
  browsers issue attack requests. The paper is worth reading if you
  want the exact packet-level details.

---

## Whose Browsers Got Hijacked?

- The Citizen Lab paper contains the Taiwan / Hong Kong concentration
  chart shown on this slide.
- Teaching point: the *weapon was assembled from innocent
  third parties* — anyone outside China loading Baidu-hosted
  analytics — which is what makes the Great Cannon novel and
  disturbing.

---

## Centralization Makes One Target Enough

- **Dyn DDoS attack (Oct 21, 2016):** [Wikipedia](https://en.wikipedia.org/wiki/DDoS_attack_on_Dyn).
- **Mirai botnet — how it worked:** [Mirai (malware) — Wikipedia](https://en.wikipedia.org/wiki/Mirai_(malware)).
- **The academic paper:** Antonakakis et al., *"Understanding the
  Mirai Botnet"* (USENIX Security 2017): [USENIX Security 2017 — Understanding the Mirai Botnet](https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/antonakakis).
- If a student wants a modern rhyme, tie to the [Nov 18, 2025 Cloudflare outage](https://blog.cloudflare.com/18-november-2025-outage/):
  same centralization theme, different failure mode (internal
  misconfig instead of attack).

---

## Defending Against DoS

- **Anycast** — most students haven't seen the term. Quick explanation:
  same IP address advertised from many locations; BGP delivers each
  client to the topologically closest instance. All 13 DNS root
  "servers" are actually anycast constellations of hundreds of
  instances. [Anycast — Wikipedia](https://en.wikipedia.org/wiki/Anycast).
- **Scrubbing services** — worth naming: Cloudflare Magic Transit,
  Akamai Prolexic, Radware, Neustar UltraDDoS Protect.
- **Booter / stresser takedowns**: Operation PowerOFF is the FBI/
  Europol joint action against DDoS-for-hire services. Recent hook:
  [Europol Operation PowerOFF](https://www.europol.europa.eu/media-press/newsroom/news/law-enforcement-shuts-down-27-online-platforms-used-for-launching-ddos-attacks) (Dec 2024 operation, ongoing).

---

## Who Gets to Stay Online?

- **Cloudflare Project Galileo — 11th anniversary report (June 2025)**
  is where the 108.9 billion / 241% figures come from:
  [Celebrating 11 years of Project Galileo's global impact](https://blog.cloudflare.com/celebrating-11-years-of-project-galileo-global-impact/).
- **Cloudflare's 5th Impact Report (Dec 19, 2025)** — broader numbers
  including AI crawl controls, election protection: [press release](https://www.cloudflare.com/press/press-releases/2025/cloudflare-publishes-fifth-annual-impact-report/).
- **Two case studies from the Galileo report** worth naming in class:
  - **Belarusian Investigative Center** — onboarded Sep 27, 2024
    while under attack; 28B requests in a single day the next day.
  - **Tech4Peace** (digital rights) — 12-day attack starting March 10,
    2025, 2.7B requests, with adaptive intensity.
- **The uncomfortable question** the slide raises — who decides who
  gets Galileo protection? — is exactly the [Matthew Prince /
  "no one should have that power" quote](https://blog.cloudflare.com/why-we-terminated-daily-stormer/) from Lecture 1. Same
  Cloudflare, same question, different valence. Worth calling out.

---

## The Takeaway: Degrade, Don't Block

- Roberts's *friction* frame closes the arc.
- Bridge to Ch. 5 (Measurement): all of this is genuinely hard to
  measure. That's why we have OONI, Wehe, Censored Planet, and
  Access Now's KeepItOn dashboards.
- Bridge to Ch. 4 (Legal & Economic): peering disputes, Section 230,
  net neutrality, and Cloudflare-as-arbiter live at the intersection
  of infrastructure and regulation.
- **Next lecture:** Chapter 3 — Platform Controls. Reading due Mon
  9am.
