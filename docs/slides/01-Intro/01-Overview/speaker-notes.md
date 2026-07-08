# Lecture 1 — Speaker Notes

Expanded background and source URLs for each slide. In-deck notes (the `::: {.notes}` blocks) are visible via reveal.js speaker view (press **S** with the deck open).

**Every URL below has been verified this session or is a canonical org landing page.** Descriptive citations (author + venue + year) with no URL mean "I know the source exists but don't have a URL I've confirmed — look it up if you want a link."

---

## "The Net Interprets Censorship as Damage"

- Quote is by [John Gilmore](https://en.wikipedia.org/wiki/John_Gilmore_(activist)), EFF co-founder.
- **The Time article itself** (full text in the official archive): [Philip Elmer-DeWitt, "First Nation in Cyberspace," *Time*, Dec 6, 1993](https://time.com/archive/6724389/first-nation-in-cyberspace/). The title is actually a David Farber quote about applying to the UN as "the first nation in cyberspace"; the Gilmore "censorship as damage" line is one of several standout quotes in the piece.
- **Provenance write-up** (Quote Investigator, with full receipts on when Gilmore first said it): <https://quoteinvestigator.com/2021/07/12/censor/>. Note: Gilmore himself can't pinpoint when he first said it; earliest independent record is Rheingold's *The Virtual Community* (Sept 1993), a few months before the *Time* article.
- Context: commercial-Internet dawn; AOL/Prodigy/CompuServe just starting to peer with the public Net; the founding libertarian optimism about routing around any single point of control.

---

## What This Course Is About

- Course home: <https://noise-lab.github.io/censorship-course/>
- Companion book (`censorship-book`) — read Chapter 1 for the framing.

---

## From "Censorship" to "Information Control"

- The definition on the vignette is straight from Chapter 1 of the book.
- **Margaret (Molly) Roberts, *Censored: Distraction and Diversion Inside China's Great Firewall*** (Princeton, 2018) is the canonical academic treatment — the book that introduces the fear/friction/flooding framework we use all term. Publisher: <https://press.princeton.edu/books/hardcover/9780691178868/censored>. Author's page: <https://margaretroberts.net/>.

---

## Why Control Information? / Roberts's Fear/Friction/Flooding

- [Roberts, *Censored*](https://press.princeton.edu/books/hardcover/9780691178868/censored), Chapters 1–2 — Section 1.2 "Distraction and Diversion" begins on p. 4 and lays out the friction/flooding move.
- If asked about alternative frames: Jack Balkin's "free speech triangle" (2018) — search "Balkin free speech triangle Knight First Amendment Institute" for the essay.

---

## Historical Anchor: The Great Firewall of China

- Overview: [Great Firewall — Wikipedia](https://en.wikipedia.org/wiki/Great_Firewall).
- **Modern GFW targeting TLS ECH / QUIC / DoH:** see Hoang et al., *GFWeb: Measuring the Great Firewall's Web Censorship at Scale*, USENIX Security 2024. Search the USENIX Security 2024 accepted-papers page.
- **PRC public-security law effective Jan 1, 2026:** widely covered but no single URL confirmed this session; search "PRC public security law January 2026" for RFA / Reuters coverage.
- The book's Chapter 1 refresh cites `gfweb2024`, `gfw2025aicensorship`, and `prc2026publicsecurity` in its bibliography — cross-reference there if you need the exact primary sources.

---

## Democracies Do This Too

- **Egypt Jan 2011 BGP withdrawal (88% of Egyptian networks disconnected):** the canonical post-mortem is Cowie/Renesys's "Egypt Leaves the Internet" — search that title. The book cites `bgpmon2011egypt`.
- **BART San Francisco, Aug 11, 2011 (cell service shut in 4 downtown stations):**
  - EFF public-interest FCC filing (Aug 2011): <https://www.eff.org/deeplinks/2011/08/public-interest-groups-fcc-bart-cell-phone>
  - EFF follow-up (2012): <https://www.eff.org/deeplinks/2012/05/eff-asks-fcc-forbid-cell-phone-shutdowns-wake-2011-bart-incident>
  - ACLU of Northern California retrospective: <https://www.aclunc.org/blog/five-years-later-barts-cell-service-shutdown-still-wakeup-call>
- **Turkey, 2014→:** the "spray-painted `8.8.8.8`" iconography is real; the retail-scale ISP DNS blocking is documented at [OONI Explorer](https://explorer.ooni.org/). For the Wikipedia-in-Turkey case study, see the Wikipedia article: [Block of Wikipedia in Turkey](https://en.wikipedia.org/wiki/Block_of_Wikipedia_in_Turkey).
- **Access Now KeepItOn 2025** (313 shutdowns / 52 countries / India-65): <https://www.accessnow.org/internet-shutdowns-2025/>
- **Freedom House 2025 (~2/3 of Internet users under restrictions):** <https://freedomhouse.org/report/freedom-net/2025>

---

## Case Study: The 2026 Age-Verification Wave

- **UK ICO — Reddit £14.47M fine (2026):** <https://ico-newsroom.prgloo.com/news/ico-issues-reddit-with-gbp-14-47m-fine-for-childrens-privacy-failures>
- **UK Ofcom escalating OSA enforcement (4chan, AVS Group, Kick.com, Imgur):** <https://inforrm.org/2026/03/11/ofcom-steps-up-online-safety-act-enforcement-with-two-further-age-assurance-fines-for-pornographic-platforms-alexandros-antoniou/>
- **Australia under-16 ban (Dec 10, 2025):**
  - eSafety Commissioner overview: <https://www.esafety.gov.au/about-us/industry-regulation/social-media-age-restrictions>
  - NPR: <https://www.npr.org/2025/12/10/nx-s1-5639694/social-media-ban-children-australia>
  - Al Jazeera: <https://www.aljazeera.com/news/2025/12/9/australias-social-media-ban-for-young-people-takes-effect>
- **EU DSA age-verification wallet (Apr 2026):** covered by the European Commission's "Age verification" policy page at <https://digital-strategy.ec.europa.eu/> — search the site for "age verification wallet."
- **Background note:** the ICO fine (data-protection regulator) is often confused with Ofcom fines (Online Safety Act) — separate regimes, coordinating on the same problem. Worth flagging in class if a student asks.

---

## Case Study: Consolidation as Chokepoint

### The **Nov 18, 2025** Cloudflare outage (the topical anchor)

- Official post-mortem: <https://blog.cloudflare.com/18-november-2025-outage/>
- CNBC coverage: <https://www.cnbc.com/2025/11/18/cloudflare-down-outage-traffic-spike-x-chatgpt.html>
- Forbes: <https://www.forbes.com/sites/siladityaray/2025/11/18/cloudflare-outage-knocks-x-and-chatgpt-offline/>

### The Matthew Prince quote — full context

- **Date:** August 16, 2017.
- **What happened:** Days after the Unite the Right rally in Charlottesville (Aug 11–12, 2017), Cloudflare terminated service to *The Daily Stormer* (neo-Nazi site). Prince — Cloudflare's CEO — announced the decision publicly and simultaneously published an internal email to Cloudflare employees explaining it.
- **The quote (widely paraphrased):**
  > "Literally, I woke up in a bad mood and decided someone shouldn't be allowed on the Internet. No one should have that power."
- **Primary source (Cloudflare blog, Prince's own writeup):** <https://blog.cloudflare.com/why-we-terminated-daily-stormer/>. Prince openly names the tension: infrastructure providers making content-hosting decisions with no due process, no accountability. Explicit quote from the post: *"Someone on our team asked after I announced we were going to terminate Daily Stormer: 'Is this the day the Internet dies?' He was half joking, but only half."*
- **Why the quote sticks:** Prince publicly agreeing that Cloudflare *shouldn't* have that power — but exercising it anyway — is the canonical statement of the unelected-arbiter problem. Cite whenever the "infrastructure providers as speech police" theme comes up (again in Ch. 3 moderation, Ch. 6 circumvention).
- **Related follow-ups:** Cloudflare eventually terminated 8chan (Aug 2019) and Kiwi Farms (Sept 2022); each round rekindled the same debate. Look up "Cloudflare 8chan blog" and "Cloudflare Kiwi Farms blog" for their respective posts.

---

## Economic Levers: Paywalls, Demonetization, Zero-Rating

- **Paywall data (Pew Research, 2024):** search "Pew Research most Americans paywalls news" — main dataset published on <https://www.pewresearch.org/journalism/>. Headlines: 74% encounter paywalls; 1% pay when they hit one; 30% highest-income vs 8% lowest-income pay for news.
- **YouTube "Adpocalypse" (2017):** [Wikipedia summary](https://en.wikipedia.org/wiki/Adpocalypse).
- **Caplan & Gillespie on demonetization as "tiered governance":** *Social Media + Society* (2020). Search DOI system for "Caplan Gillespie tiered governance" or check the article title *"Tiered Governance and Demonetization"*.
- **Facebook Free Basics / zero-rating pushback (India TRAI, 2016):** [Internet.org — Wikipedia](https://en.wikipedia.org/wiki/Internet.org) covers the zero-rating controversy.

---

## How Widespread Is It? / KeepItOn 2025 vignette

- **Primary:** <https://www.accessnow.org/internet-shutdowns-2025/>
- **Companion measurement resources:**
  - OONI Explorer: <https://explorer.ooni.org/>
  - Google Transparency Report: <https://transparencyreport.google.com/>
  - India shutdown tracker (SFLC.in): <https://internetshutdowns.in/>

---

## The Trend: From Protocols to Platforms

- **Zuckerberg "squirrel dying" quote:** originally reported in David Kirkpatrick's *The Facebook Effect* (2010).
- **Eli Pariser's filter bubble:** [Filter bubble — Wikipedia](https://en.wikipedia.org/wiki/Filter_bubble). Pariser's book: *The Filter Bubble* (2011).

---

## Why Bother, If It's Circumventable?

- "Porous censorship" — Roberts, *Censored*.
- VPN / Tor / circumvention preview: Chapter 6 of the book. Discussion docs: <https://noise-lab.github.io/censorship-course/breakouts/vpn> and <https://noise-lab.github.io/censorship-course/breakouts/tor>.

---

## Course Logistics

- **Course home:** <https://noise-lab.github.io/censorship-course/>
- **Syllabus:** <https://noise-lab.github.io/censorship-course/syllabus>
- **Agenda template (3-hour summer):** <https://noise-lab.github.io/censorship-course/agenda-template-summer>
- **Reading-response repo template:** <https://github.com/noise-courses/censorship-responses>
- **Response-repo submission form:** <https://docs.google.com/forms/d/e/1FAIpQLSfMxQDibaTuyZeYGhz3GWe3ko3GHrUWtJ7D4o3C9x0-yQwvbQ/viewform?usp=publish-editor>

---

## Let's Get Started (closing)

- Next lecture: **DNS Manipulation** — book §2.2.1.
- Discussion doc: <https://noise-lab.github.io/censorship-course/breakouts/dns>
