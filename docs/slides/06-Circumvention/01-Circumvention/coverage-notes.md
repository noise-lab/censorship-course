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
- 2026-06-03: Added **Snowflake & Conjure** slide ("The 2025 Front Line") with dated
  vignette — in its "most challenging year" Tor made **Snowflake the most-used obfuscation
  tool in Iran** (upgraded to Manifest V3, staging-server stress tests) and **deployed
  Conjure** (DNS/AMP-cache registration, unused-ISP-address-space decoys), with wider
  Conjure rollout slated next. Source: Tor Project blog, "Staying Ahead of Censors in 2025"
  (blog.torproject.org/staying-ahead-of-censors-2025). Snowflake mechanics (volunteer
  WebRTC browser proxies, ephemeral, broker rendezvous over domain fronting) per
  snowflake.torproject.org / EFF. NOT yet in the book — flagged for next edition.
- 2026-06-03: Added **Encrypted DNS as a Circumvention Layer** slide (DoH/DoT, port-53
  poisoning, 1.1.1.1/8.8.8.8) — Iran 2022 Mahsa Amini (Signal/Outline/Lantern) and Russia
  post-2022; key caveat that it falls to SNI inspection / IP blocking and only "buys time."
  Per book §6.1 (hounsel2019/2020, tai2025irblock, ramesh2023russia-ukraine).
- 2026-06-03: Added **I2P: Garlic Routing for Internal Services** half-slide — garlic
  routing vs. onion routing (bundled "cloves"), separate inbound/outbound tunnels, no exit
  relay / outproxy bottleneck, Tor-vs-I2P rule of thumb. Per book §6.2.
- 2026-06-03: Added **Who Pays for Circumvention?** slide integrating the economics/
  sustainability item — generalizes the decoy-router incentive problem to bridges, exit
  relays, and Snowflake's borrowed-browser model (donated public good; economic not
  cryptographic problem). Per book §6.4 incentives discussion + §6.1 free-VPN point.

## Suggested missing coverage on broad themes (point 3)
- **Threat-model exercise** (DEFERRED — in-class activity, not a slide): an activity matching
  personas (diaspora journalist, domestic activist, casual streamer) to tool portfolios would
  operationalize the chapter's central takeaway. Belongs in the agenda/handout, not the deck.
- (Integrated 2026-06-03: Snowflake & Conjure, I2P / garlic routing, Encrypted DNS as a
  circumvention layer, and economics/sustainability of circumvention infrastructure — see
  "Current-events updates made" above.)

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
- **Snowflake & Conjure 2025 vignette**: the "most-used in Iran" claim and "Conjure rollout
  next" status are from the Tor Project's 2025 retrospective — re-verify against the next
  annual Tor anti-censorship post (Conjure rollout should have a status update; Snowflake's
  primacy may shift to WebTunnel/Conjure). Watch for a wartime Iran-blackout or Russia
  allowlist event that could become the lead vignette.
- **Encrypted-DNS slide**: stable as mechanics, but ECH/encrypted-SNI adoption is the moving
  edge — add a line when ECH is widely deployed/blocked. Iran 2022 and Russia post-2022 will
  read as older over time; swap for a fresher DNS-manipulation event if one is verifiable.
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
