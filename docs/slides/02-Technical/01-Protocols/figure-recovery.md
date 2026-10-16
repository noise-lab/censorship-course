# Figure recovery: 02-Technical/01-Protocols

Source: `docs/slides/ppt-archive/class/technical/04-Protocols.pptx`, 46 slides (slide 26 hidden), rendered 2026-10-16 with `pptx-figures.py` at 220 dpi.

Already handled elsewhere: the leaky-bucket and token-bucket shapers (pptx 42–43) were pulled by hand on 2026-10-13 into `02-Technical/02-Throttling-DoS/images/`, so they are not duplicated here. Earlier media extraction (`images/slideNNN_imgNNN.*`) already embedded pptx 4 (DNS hierarchy), 28 (China Telecom hijack) and 37 (block-page fingerprints).

| pptx slide | class | target Quarto slide | figure name | notes |
|---|---|---|---|---|
| 1–3, 5 | skip | | | title, forms-of-interference bullets, divider, DNS bullets |
| 4 | media | "DNS Maps Names to Addresses" | (slide004_img001.png) | already embedded |
| 6 | skip | | | Cox NXDOMAIN-ads screenshot (dated) and a small User/Censorship Node/DNS Server timeline (426 px, unattributed paper figure; slide 7 covers the mechanism better) |
| 7 | media | new, "Three Places to Forge a DNS Answer" | dns-injection-points.png | ISP resolver / on-path injection / fake root; extracted copy slide007_img004.png, never embedded |
| 8 | skip | | | Mashable news screenshot of the 8.8.8.8 graffiti; someone else's photo, no attribution |
| 9–13 | skip | | | DNSSEC RRs and the verification-tree diagram (slide 12); DNSSEC is out of this deck's scope per coverage-notes |
| 14–15 | skip | | | dig terminal screenshot; divider |
| 16 | keep | new, "An Address Is a Network Prefix Plus a Host" | ipv4-prefix-bits.png | dotted-quad bits with network/host split; builds are additive, final state captured |
| 17 | skip | | | three-way-handshake and sliding-window figures are Tanenbaum & Wetherall textbook figures; bullets on "TCP in One Slide" already carry the handshake |
| 18 | keep | new, "Blocking Needs a Topological Chokepoint" | firewall-chokepoint.png | Alice / censored net / firewall / uncensored net / Bob banner; final animation state (bounced arrow) kept |
| 19 | media | new, "The Forged Reset Gives Itself Away" | tcp-reset-trace.png | Clayton, Murdoch & Watson 2006 "Connection Reset" trace (slide019_img014.png); attributed on the slide. "Normal Web Download" trace (img013) left out for space |
| 20–22 | skip | | | packet-injection bullets, summary, divider |
| 23 | keep | new, "BGP in One Picture" | bgp-route-advertisement.png | stripped "Group 60" and "Group 71" (the routing-table overlay, builds 36–37) and cropped the base diagram |
| 24 | skip | | | BGP bullets |
| 25–27 | skip | | | 1997 CNET clipping, hidden Renesys screenshot, China-hijack bullets with an unattributed world map |
| 28 | media | "Route Hijacking: China Telecom, 2010" | (slide028_img019.png) | already embedded |
| 29 | skip | | | hijack-events bullets |
| 30 | media | new, "The YouTube Hijack at the AS Level" | pakistan-youtube-hijack.png | AS-level diagram (slide030_img020.png), same style/source as the China Telecom figure already in the deck; original footnote source not recoverable |
| 31 | skip | | | BGPlay-style screenshot, unlabelled, dated |
| 32–36 | skip | | | summary, divider, CNN block-page screenshots (dropped earlier as redundant) |
| 37 | media | "Block Pages: Censorship You Can See" | (slide037_img028.png) | already embedded |
| 38 | skip | | | Jones et al. 2014 "mechanisms over time" scatter plots (paper figure); the fingerprint table from the same paper already carries the point |
| 39–41 | skip | | | summary, divider, throttling bullets |
| 42–44 | skip | | | leaky/token bucket already in 02-Throttling-DoS; TB-vs-LB comparison is a text table |
| 45–46 | skip | | | throttling screenshot (replaced by the Russia vignette), summary |

## Sources

- `images/dns-injection-points.png` — source: ppt-archive/class/technical/04-Protocols.pptx slide 7, embedded picture (extracted as slide007_img004.png), 935×366
- `images/ipv4-prefix-bits.png` — source: ppt-archive/class/technical/04-Protocols.pptx slide 16, render crop box 500,650,2330,1075 at 220 dpi, 1830×425
- `images/firewall-chokepoint.png` — source: ppt-archive/class/technical/04-Protocols.pptx slide 18, render crop box 1100,40,2890,430 at 220 dpi, final build state, 1790×390
- `images/tcp-reset-trace.png` — source: ppt-archive/class/technical/04-Protocols.pptx slide 19, embedded picture (extracted as slide019_img014.png), 466×189; figure from Clayton, Murdoch & Watson, PET 2006
- `images/bgp-route-advertisement.png` — source: ppt-archive/class/technical/04-Protocols.pptx slide 23, shapes "Group 60" and "Group 71" stripped, render crop box 470,345,2600,1545 at 220 dpi, 2130×1200
- `images/pakistan-youtube-hijack.png` — source: ppt-archive/class/technical/04-Protocols.pptx slide 30, embedded picture (extracted as slide030_img020.png), 824×518
