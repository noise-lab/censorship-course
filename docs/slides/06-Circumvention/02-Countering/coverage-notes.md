# 06-Circumvention/02-Countering — instructor notes

New deck for Week 9 (Dec 1–3, 2026). Its narration will become the text of book §6.3 (Countering Platform
Controls) and §6.4 (Countering Legal and Economic Controls). Ch. 6 is being reorganized
as 6.1 introduction, 6.2 getting around technical controls, 6.3 platform, 6.4 legal and economic. The deck answers a reviewer's question: Ch. 6's tools defeat Ch. 2's network
controls, so what counters the platform, legal, and economic controls of Ch. 3 and Ch. 4?
The earlier §6.5 draft text was **not** used as a source. The deck is organized around seven
levers instead.

## Current-events updates made (point 2)
- 2026-11-05 (initial build): all facts below were verified by web search on this date.
  - **Vignette:** Appeals Centre Europe's second transparency report (May 28, 2026).
    - 24,000+ disputes, Apr 2025–Mar 2026.
    - 59% disagreement with the platform where the content was reviewed.
    - 7,300+ default decisions.
  - **DSA Art. 40 status:** delegated act in force Oct 29, 2025; preliminary breach findings against TikTok and Meta on Oct 24, 2025; Commission roundtable to launch the first vetted requests on May 19, 2026 (49 applications). No public record was found of the first data actually delivered.
  - **Santa Clara Principles 2.0:** published Dec 8, 2021.
  - **DSA Art. 17(1):** requires a statement of reasons for (a) visibility restrictions, demotion included, and (b) restrictions of monetary payments.
  - **Federation and interoperability:**
    - Mastodon: about 10.5M accounts and about 785k monthly active users (2026).
    - Bluesky: 47M registered (Oct 2026). The roughly 10M mobile monthly-active figure is a Similarweb estimate; Bluesky publishes no official count.
    - WhatsApp third-party chats under the DMA: BirdyChat and Haiket, announced Nov 2025.
  - **youtube-dl:** RIAA §1201 notice in Oct 2020; GitHub reinstated the repo on Nov 16, 2020 and pledged a $1M defense fund.
  - **§1201 ninth triennial rule:** issued Oct 25, 2024, effective Oct 28, 2024. The security-research exemption was renewed; the AI-bias exemption was denied.
  - **Archiving:**
    - Hachette v. Internet Archive: 2d Cir. ruled Sept 4, 2024; no cert petition.
    - UMG v. Internet Archive (Great 78): $621M claimed; settled Sept 15, 2025.
    - End of Term 2024/25 crawl reported complete on Aug 24, 2026.
  - **Zero rating (CJEU):**
    - Telenor: **Sept 15, 2020**.
    - Vodafone and Telekom Deutschland: Sept 2, 2021.
    - Telekom România (C-367/24): July 10, 2025.
  - **Payment rails:** Steam changed its policy Jul 16, 2025; itch.io de-indexed adult content Jul 24, 2025.
  - **Cloudflare:** dropped Kiwi Farms Sept 3, 2022.

## Corrections to flag in other decks
- `04-Legal/01-Legal`, "What the DSA Still Misses", lists **demonetization** and
  **shadow bans/downranking** as missing.
  - DSA Art. 17(1)(a)–(b) covers both on paper: demotion, and "suspension, termination or other restriction of monetary payments."
  - Suggest rewording the slide to say that reporting and enforcement for these cases are untested. This deck labels the correction on the "Lever 3" slide.
- The original brief cited a "CJEU 2021 zero-rating ruling."
  - **Telenor** was Sept 15, 2020.
  - The Sept 2, 2021 rulings are the German Vodafone and Telekom Deutschland cases.
  - The deck uses both dates.

## Suggested missing coverage on broad themes (point 3)
- **Middleware and user-chosen ranking.** Third-party feeds and Bluesky custom feeds and labelers are a lever between exit and transparency. The deck mentions labelers only in passing.
- **Algorithmic-choice mandates.**
  - DSA Art. 38: the option of a feed that is not based on profiling.
  - NY SAFE for Kids Act, from the personalization deck.
  - These could be a "design mandate" lever.
- **Collective action by creators.** Unions and coalitions (for example, YouTubers Union) as a demonetization counter. Not verified this session.
- **Non-EU counters.** The deck's levers skew European. Worth one slide on India (TRAI), Brazil, or other jurisdictions if time allows.

## Next-year refresh notes
- **ACE figures:** a third report focused on scams was announced for Nov 2026. Swap the vignette when it is out.
- **DSA Art. 40:**
  - Check whether vetted researchers have received data, and whether the TikTok/Meta preliminary findings became fines.
  - Replace "first requests in the pipeline."
- **DSA fines:**
  - Verified: X, €120M (Dec 5, 2025); Temu, €200M (May 28, 2026).
  - A €550M AliExpress fine (Jul 2026) appeared in one secondary source but was **not verified**. Do not use it without the Commission press release.
- **Mastodon and Bluesky user counts** change quarterly.
- **Lumen:** sources conflict on the notice count (43M in mid-2025 vs 75M in June 2026). The slide says "tens of millions." Check lumendatabase.org for an official figure.
- **Next §1201 triennial rulemaking:** due Oct 2027.

## Curated images
- None. The deck is text and tables. Candidates if wanted:
  - a capture of the DSA Transparency Database;
  - the ACE report's headline chart;
  - the Wayback capture of a removed federal page (the National Security Archive briefing book has before/after screenshots).

## Source
- **New deck.** No pptx or `_source-extract.md`.
- **Built from the instructor's own materials:**
  - `03-Platform/01-Platform`: audit slides, GIFCT, DSA fine on X, Oversight Board.
  - `03-Platform/03-Personalization`: Bobble, the DSA Art. 40 vignette.
  - `04-Legal/01-Legal`: DMCA notice/counter-notice, Felten/SDMI, Sandvig v. Barr, ~40% researcher survey, Stop SESTA, Moody, Murthy, Australia ban, the DSA slides.
  - `04-Legal/03-PaidPrioritization`: Free Basics/TRAI, Cell C and MTN natural experiments, C-367/24, Sixth Circuit 2025.
  - `05-Measurement/01-Measurement`: transparency reports, Lumen, natural experiments, DSA database.
  - `06-Circumvention/01-Circumvention`: "who pays for circumvention."
  - `docs/agenda/2026-autumn.md`: the youtube-dl presentation and the notice-and-takedown discussion.
  - Book outside §6.5: Ch. 4 "Demonetization and Infrastructure Censorship" (payment processors, Daily Stormer, Cloudflare); Ch. 5 §5.3–5.4; the Ch. 6 intro (Mastodon legality).
- **Sources for new facts** are linked row by row in `speaker-notes.md`.
