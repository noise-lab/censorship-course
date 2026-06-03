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
- 2026-06-03: Kept canonical anchors that the book treats as core history: **Mirai/Dyn
  (Oct 21, 2016)**, **Great Cannon (2015)**, **Spamhaus DNS amplification (2013)**,
  **Netflix/peering "throttling" (~2014)**. These are taught as history, not as "current
  events," so they don't go stale.

## Suggested missing coverage on broad themes (point 3)
- **Throttling-detection hands-on (Wehe):** agenda Lecture 4 pairs throttling with a
  hands-on detection lab. A short demo deck or appendix walking through Wehe's
  replay-with/without-tunnel methodology and its noise problems would land the
  epistemics point harder than slides alone.
- **ECH / Encrypted ClientHello status:** the classification arms race hinges on this.
  A one-slide "state of SNI encryption in 2026" (browser/CDN rollout, where it's blocked)
  would date well as an annual refresh target.
- **Net-neutrality bridge:** the Netflix/peering nuance is introduced here but resolved in
  Ch. 4. Worth an explicit forward-pointer / shared example so the two decks reinforce.
- **Low-rate / application-layer DoS (Layer 7):** Cloudflare data shows ~93% of attacks on
  journalism orgs are L7. Current deck mentions low-rate DoS in notes only; a dedicated
  slide could connect to the asymmetry theme.
- **Sovereign-internet / RuNet throttling:** Russia's selective slowdowns (e.g., the 2021
  Twitter throttling and 2025 WhatsApp/FaceTime call interruptions) are a strong
  state-throttling case study not yet on a slide.
- **Botnets deep-dive:** book defers botnet mechanics to the next chapter; ensure the
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
