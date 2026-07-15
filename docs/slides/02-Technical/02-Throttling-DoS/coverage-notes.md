# 02-Technical/02-DoS — instructor notes

## Current-events updates made (point 2)
- 2026-06-03: Refreshed the macro-trend vignette to Access Now **#KeepItOn 2025**
  annual report (released **Mar 31, 2026**): **313 shutdowns / 52 countries** in 2025
  (record; up from 304 in 2024), with a documented shift from total blackouts to
  **targeted throttling/blocking** of single platforms (Telegram, WhatsApp, TikTok);
  Turkey called out for social-media throttling.
- 2026-06-03: Added a private-actor friction vignette — **X (Twitter) ~5-second link
  delays** to disfavored sites (NYT, Reuters, Bluesky, Threads, Substack, Meta),
  *Washington Post* analysis, **Aug 2023**. Used to show "throttling" is not only a
  state tool and to reinforce the "tax on access" framing.
- 2026-06-03: Added **Cloudflare Project Galileo** governance vignette — **108.9 B**
  threats blocked **May 2024–Mar 2025**, **+241% YoY**, journalism orgs hardest hit
  (Cloudflare 2025 Impact Report, June 2025). Replaces a generic "defenses" closer with
  the book's who-gets-protected governance question.
- 2026-06-03: Added **"The Classification Arms Race in 2026: SNI vs. ECH"** slide.
  Verified: Firefox ECH default since **v119 (Oct 2023)**, Chrome **v117+**; **Cloudflare**
  default ECH **Oct 2024**; **Russia (Roskomnadzor/TSPU)** began dropping ECH ClientHellos
  **Nov 5, 2024**, triggered by the shared outer SNI `cloudflare-ech.com` (one filter rule
  caught all of it); **China** censors the DNS ECH relies on instead (blocked ESNI in 2020).
  Sources: Cloudflare ECH announcement; CDT "Do Not Stick Out" (2025); gfw.report USENIX
  Security 2025. Integrates backlog item 3.
- 2026-06-03: Added **"Case Study: Russia's Sovereign Internet Throttle"** slide.
  Verified: **March 2021** Roskomnadzor Twitter throttle (100% mobile / 50% desktop;
  matched `t.co` → over-throttled Reddit/Microsoft), first documented selective on-demand
  state throttling — **Xue et al., ACM IMC 2021**; **2025** WhatsApp throttled ~**70–80%**
  via DPI under the RuNet/TSPU sovereign-internet regime, steering users to state **Max**
  messenger (**HRW**, July 2025; intellinews). Integrates backlog item 2; doubles as a
  concrete instance of the SNI-classification over-blocking weakness.
- 2026-06-03: Added **"Low-Rate and Layer-7 DoS"** slide (after the asymmetry slide).
  Verified: **~93% (92.88%)** of mitigated attack traffic against **journalism orgs** was
  **Layer-7 HTTP**, per Cloudflare's **Project Galileo** report (window **May 2024–Mar
  2025**, released **June 2025**) — same source as the 108.9 B / +241% governance figures.
  Integrates backlog item 1; reinforces the asymmetry/indistinguishability theme.
- 2026-06-03: Strengthened the **net-neutrality forward-pointer** (backlog item 4): the
  Netflix/peering vignette now carries an explicit on-slide line that the case is resolved
  in the **net-neutrality deck (Ch. 4)** as a commercial interconnection fight, not
  censorship. One-line cross-link, no new slide.
- 2026-06-03: Kept canonical anchors that the book treats as core history: **Mirai/Dyn
  (Oct 21, 2016)**, **Great Cannon (2015)**, **Spamhaus DNS amplification (2013)**,
  **Netflix/peering "throttling" (~2014)**. These are taught as history, not as "current
  events," so they don't go stale.

## Suggested missing coverage on broad themes (point 3)
- **Throttling-detection hands-on (Wehe) (DEFERRED):** agenda Lecture 4 pairs throttling with a
  hands-on detection lab. A short demo deck or appendix walking through Wehe's
  replay-with/without-tunnel methodology and its noise problems would land the
  epistemics point harder than slides alone.
- ~~**ECH / Encrypted ClientHello status**~~ — DONE 2026-06-03 (dedicated SNI-vs-ECH slide).
  Keep as an *annual refresh* target: re-verify browser/CDN defaults and which states block
  ECH (Russia/China) each year.
- ~~**Net-neutrality bridge**~~ — DONE 2026-06-03 (explicit on-slide forward-pointer to Ch. 4
  on the Netflix/peering vignette).
- ~~**Low-rate / application-layer DoS (Layer 7)**~~ — DONE 2026-06-03 (dedicated L7 slide;
  Cloudflare ~93% journalism-org L7 figure).
- ~~**Sovereign-internet / RuNet throttling**~~ — DONE 2026-06-03 (Russia case-study slide:
  2021 Twitter throttle + 2025 WhatsApp throttle).
- **Botnets deep-dive (DEFERRED):** book defers botnet mechanics to the next chapter; ensure the
  Platform/abuse deck picks up Mirai-style IoT botnets so this thread isn't dropped.

## Next-year refresh notes
- **KeepItOn vignette (2025 data, "313 shutdowns / 52 countries," Mar 31 2026 report):**
  will go stale when the **2026** annual report lands (~Q1 2027). Swap the figures and the
  "record" claim; keep the targeted-throttling trend point.
- **X link-throttling (Aug 2023):** already a couple of years old. Still the cleanest
  documented private-throttling case, but watch for a fresher dominant-platform example
  (e.g., a verified algorithmic-deprioritization or link-suppression finding) to swap in.
- **Cloudflare Galileo stat (108.9 B, +241%, May 2024–Mar 2025):** refresh with the next
  Impact Report figures annually; verify the window and percentage each time.
- **Turkey throttling call-out:** verify it remains current in the next KeepItOn report;
  substitute the year's most prominent social-media-throttling state if it shifts.
- **SNI/ECH slide (Russia TSPU blocking ECH, Nov 2024; Firefox v119 / Chrome v117 / Cloudflare
  Oct 2024 defaults):** re-verify each year — browser/CDN ECH defaults, whether Cloudflare
  still uses a shared `cloudflare-ech.com` outer SNI (the single-signature weakness), and
  which states block ECH. Update if China starts censoring ECH directly.
- **RuNet case-study slide (Twitter 2021, WhatsApp ~70–80% 2025):** the 2021 Twitter case
  (Xue et al., IMC 2021) is a durable scholarly anchor; the WhatsApp figure will age —
  refresh with the latest Russian throttling/ban status (Max messenger adoption, any full
  WhatsApp/Telegram ban) from the next HRW/Access Now reporting.
- **Cloudflare L7 figure (~93% / 92.88% of journalism-org attacks are Layer 7, May 2024–Mar
  2025):** refresh with each Project Galileo / Radar report; same source/window as the
  108.9 B / +241% Galileo governance stat, so update both together.
- **Stronger alternative vignettes flagged but not used:** Nepal's Sept 2025 block of 26
  platforms; Iran's Jan 2026 near-total blackout during protests — both better fit a
  *shutdowns* deck than this throttling/DoS one, so held in reserve.

## Curated images
- **Used** `slide034_img015.png` — Great Cannon architecture (inspect → reroute → inject
  RST/JS, same-TTL). Genuinely teaches the firewall-to-cannon evolution; clean diagram.
- **Used** `slide038_img019.png` — real bar chart of attacking-client origin (TW/HK
  dominate). Real data; makes the "weaponized bystanders" point concrete.
- **Dropped** `slide033_img014.png` — NYT headline screenshot (decorative, no teaching
  value).
- **Dropped** `slide039_img020.png` — Baidu-domain referrer chart (real, but redundant
  with the client-origin chart; one data plot per Great Cannon point is enough).
- **Dropped** all `.wmf` clip-art (smurf/DNS-amp/SSL cartoons, slides 10/22/23) — not
  renderable and purely decorative; the postcard analogy carries amplification better.
- **Dropped** the entire **GFW-vs-Tor active-probing** image set (slides 41–68) — that is
  a *circumvention/measurement* research talk (Ensafi et al., IMC 2015), off-scope for
  §2.3 "Disrupting the Flow of Data." Belongs in Ch. 6 (Circumvention) / Ch. 5
  (Measurement), not here.
- No invented diagrams. Leaky/token bucket and SYN-cookie figures exist in the book; the
  deck describes them in text/notes rather than fabricating a slide graphic.

## Source
- rebuilt from _source-extract.md (70 slides) + censorship-book Ch. 2 Technical Controls,
  §2.3 (Disrupting the Flow of Data: Throttling and Rate Limiting; Denial of Service) +
  agenda.md (Lecture 4: Throttling — Overview + Hands-On). Reframed from the original
  attack-survey order to the book's friction/"tax on access" taxonomy, dropped the bolted-on
  GFW-vs-Tor active-probing research talk as off-scope, and led with throttling (the book's
  ordering) before DoS.
