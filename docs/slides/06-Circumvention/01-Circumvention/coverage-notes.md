# 06-Circumvention/01-Circumvention — instructor notes

## Current-events updates made (point 2)
- 2026-06-03: Lead VPN vignette set to Russia's VPN crackdown — Roskomnadzor had
  confirmed blocking **469 VPN services** by Feb 2026, targets blocking **92% of VPNs by
  2030** (~20B rubles/year for permanent blocking infra), restricted **12,600 "VPN
  promotion" items** Jan–Apr 2025 (2x all of 2024), while **~41% of Russian users** still
  use a VPN. Sources: iz.ru (Jan 22 2026), TechRadar (2025). This is the freshest,
  best-sourced hook tied to the deck's cat-and-mouse theme.
- 2026-06-03: Added dated **Ross Ulbricht pardon** vignette (full pardon Jan 21 2025,
  Trump) on the onion-services / dark-web policy slide. Sources: NPR, CNBC (Jan 21 2025).
- 2026-06-03: Added current pluggable-transport detail — **WebTunnel** (introduced late
  2024, blends into TLS) became vital in Russia, then most bridges were blocked by
  mid-2025, pushing Tor to distribute bridges over Telegram. Source: Tor Project blog
  "Staying ahead of censors in 2025."
- 2026-06-03: Refreshed VPN-spike examples to Nigeria 2021 Twitter ban (persisted
  post-2022), India 2020 TikTok, and Pakistan 2024–25 X restrictions (HTTPS-layer
  blocking), per book §6.1.

## Suggested missing coverage on broad themes (point 3)
- **Snowflake & Conjure** (newer pluggable transports): Snowflake's volunteer-browser-proxy
  model and Conjure's use of unused ISP address space are increasingly central to the 2025
  Russia/Iran fight and worth one slide if pluggable transports get expanded.
- **I2P / garlic routing** mechanics: currently only a table row; a half-slide on garlic
  routing vs. onion routing and inbound/outbound tunnels would deepen the "beyond Tor" point.
- **Encrypted DNS (DoH/DoT) as a circumvention layer**: the book (§6.1) treats this at
  length (Iran 2022 Mahsa Amini, Russia post-2022); deck only gestures at it via Pakistan.
  Could be its own slide tying to the Measurement/Technical chapters.
- **Economics/incentives of circumvention infrastructure**: who pays for bridges, exit
  relays, decoy routers? The decoy-routing incentive problem could generalize into a
  broader "sustainability of circumvention" discussion.
- **Threat-model exercise**: an in-class activity matching personas (diaspora journalist,
  domestic activist, casual streamer) to tool portfolios would operationalize the chapter's
  central takeaway.

## Next-year refresh notes
- **Russia VPN vignette** (Feb 2026 figures): numbers will move fast — re-verify the
  blocked-VPN count, the 92%-by-2030 target, and the share of Russian VPN users. Check
  iz.ru / Roskomnadzor reporting and TechRadar each year.
- **Ulbricht pardon** (Jan 2025): durable as a *fact* but will read as older news over
  time; if a fresher dark-web/anonymity policy event arises (new marketplace takedown,
  major onion-service case), consider swapping.
- **WebTunnel / pluggable-transport status**: the obfs4 → meek → WebTunnel → Conjure line
  moves yearly; verify which transport is currently load-bearing in Russia/Iran via the Tor
  Project blog before teaching.
- **VPN-ban spike examples** (Nigeria/India/Pakistan): replace with the most recent
  high-profile national platform ban if one occurs.
- Stronger alternative vignette flagged but not used: **Iran wartime internet blackouts
  (2025)** and Tor's "most challenging year" framing — a good swap if the Russia hook goes
  stale.

## Curated images
- **Used** `slide007_img007.png` — VPN tunnel concept (you → encrypted tunnel → VPN server →
  blocked sites). Slightly clip-arty but teaches the tunnel idea cleanly; matches book
  Fig. vpn-concept.
- **Used** `slide056_img204.png` — Tor network diagram (entry guard / middle / exit, with
  the exit→destination hop shown as *not* Tor-encrypted). Excellent: carries both the
  onion-routing structure and the DNS/exit-leak risk in one figure.
- **Used** `slide074_img248.png` — domain-fronting / CDN diagram (allowed sites + hidden
  "evil" site behind the same CDN edge). Genuinely teaches the SNI-vs-Host mismatch.
- **Used** `slide082_img254.jpg` — classic steganography pair (two near-identical photos,
  one carries a hidden message). Perfectly makes the "you can't tell which" point.
- **Used** `slide107_img283.png` — decoy-routing flow (client / adversary / decoy router /
  decoy proxy / covert destination). Compact and accurate; matches book Fig. decoy.
- **Dropped**: the entire VPN-user-study screenshot series (slides 13–48, ~150 images) —
  conference-talk chrome, agenda slides, and redundant bar charts; the findings are better
  conveyed as 4 bullets. Dropped Tor circuit-setup step images (59–62) — the single network
  diagram suffices. Dropped Collage step-by-step screenshots, Mix clip art, GAN teaser,
  and all logos/headshots as decorative or redundant.

## Source
- rebuilt from _source-extract.md (111 slides) + censorship-book Ch. 6 Taking Back Control
  (whole chapter: circumvention.tex, vpn.tex, anonymous.tex, infohiding.tex,
  infrastructure.tex) + agenda.md.
