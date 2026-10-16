# Figure recovery: 06-Circumvention/01-Circumvention

Source: `docs/slides/ppt-archive/class/circumvention/16-Circumvention.pptx`, 111 slides
(8 hidden: 69, 70, 71, 74, 86, 87, 105, 110), rendered 2026-10-16 with
`src/pptx-figures.py` (LibreOffice headless, 110 dpi contact sheet, 220 dpi crops).

| pptx slide | class | target Quarto slide | figure name | notes |
|---|---|---|---|---|
| 1–3, 6, 12 | skip | | | title, section, and bullet slides |
| 4 | keep | "Why a Proxy at All?" (existing) | proxy-outside-firewall.png | final state incl. arrow (Freeform 20); 62% below the prose |
| 5, 9–11 | skip | | | news clippings, app-store screenshots, dated |
| 7 | media | already used (`slide007_img007.png`) | | |
| 8 | media | | | enterprise VPN clip art, not used |
| 13–48 | skip | | | VPN user-study talk: plan slides, bar charts, quotes, logos (instructor dropped these in coverage-notes); 48 "Conclusions" icons are the deck's four bullets |
| 49, 50, 53 | skip | | | section title, Chaum bullets, mixnet disadvantages (bullets) |
| 51 | keep | new "A Mix in One Picture" | chaum-mix-design.png | final build state incl. the adversary callout |
| 52 | keep | "Chaum's Mix: The Building Block" (existing) | mix-cascade.png | wide banner, 58% below the bullets |
| 54 | skip | | | Tor usage graph, dated |
| 55, 57, 64, 65, 68 | skip | | | bullets, logo, management issues |
| 56 | media | already used (`slide056_img204.png`) | | |
| 58 | media | not embedded | | onion-layers picture is a third-party figure (Wikimedia-style) with no attribution in the deck; left out |
| 59–62 | media | not embedded | | Tor circuit-setup steps; coverage-notes already chose the single network diagram |
| 63 | keep | new "Choosing a Tor Circuit" | tor-circuit-selection.png | no animation; full width above two bullets |
| 66 | keep | new "Node-Level vs. Link-Level Adversaries" | tor-node-level-adversary.png | stripped Picture 47, Cloud 48, Picture 49 (the Sybil-cloud final state) to leave the guard + destination adversaries |
| 67 | keep | same slide | tor-link-level-adversary.png | stripped Picture 90 (exits in the build) |
| 69–71 | media | not embedded | | EFF "How Tor Works" panels, hidden slides, third-party |
| 72, 73, 78, 79, 80, 81, 84–89 | skip | | | section titles and bullets |
| 74 | media | already used (`slide074_img248.png`) | | |
| 75, 76 | media | not embedded | | layered packet / SNI-vs-Host mismatch pictures, third-party, unattributed; superseded by slide 74's figure |
| 77 | skip | | | news clippings, dated |
| 82 | media | already used (`slide082_img254.jpg`) | | |
| 83 | media | not embedded | | Infranet trusted responders, superseded by slide 90 |
| 90 | keep | new "Infranet vs. Collage in One Picture" | infranet-dedicated-host.png | stripped TextBox 12 ("Firewall" label collided with "Unblocked host") |
| 91 | keep | same slide | collage-ugc-hosts.png | final state, no strip |
| 92, 94, 95, 98, 99, 102, 104 | skip | | | bullets |
| 93 | skip | | | Collage step-by-step: seven overlapping step textboxes; base diagram is slide 91 |
| 96 | keep | new "Collage: Task Mapping" | collage-task-mapping.png | stripped both Content Placeholder 3, Group 12, Oval 28/29, Pie 58, Straight Connector 59, TextBox 60/70, Arrow 33/35, Rounded Rectangle 30/31 (path-animated task labels that render on top of the ring) |
| 97 | skip | | | duplicate of 91 with design-goal bullets |
| 100 | keep | new "Collage in Numbers" | collage-case-study.png | native table incl. the DSL caption |
| 101 | skip | | | comparison table, superseded by "Beyond Tor: Pick a Portfolio" |
| 103 | media | not embedded | | dead-parrot cartoon, third-party |
| 105 | skip | | | hidden GAN teaser |
| 106, 107, 109, 111 | skip / used | | | section title; 107 already used (`slide107_img283.png`); bullets |
| 108 | media | new "Decoy Routing, Step by Step" | `slide108_img284.png` (existing extraction) | Curveball-terminology timeline; credited to Karlin et al. (FOCI 2011) in the caption |
| 110 | keep | new "Decoy Routing with Only a Passive Tap" | decoy-routing-passive-tap.png | hidden slide; final build state (all shapes); TapDance exchange |

## Captured

- source: `16-Circumvention.pptx` slide 4 → `images/proxy-outside-firewall.png` (1954×730)
- source: `16-Circumvention.pptx` slide 51 → `images/chaum-mix-design.png` (1972×1033)
- source: `16-Circumvention.pptx` slide 52 → `images/mix-cascade.png` (1692×280)
- source: `16-Circumvention.pptx` slide 63 → `images/tor-circuit-selection.png` (1999×692)
- source: `16-Circumvention.pptx` slide 66, Picture 47 / Cloud 48 / Picture 49 stripped → `images/tor-node-level-adversary.png` (1999×715)
- source: `16-Circumvention.pptx` slide 67, Picture 90 stripped → `images/tor-link-level-adversary.png` (2165×880)
- source: `16-Circumvention.pptx` slide 90, TextBox 12 stripped → `images/infranet-dedicated-host.png` (1440×772)
- source: `16-Circumvention.pptx` slide 91 → `images/collage-ugc-hosts.png` (1648×780)
- source: `16-Circumvention.pptx` slide 96, 13 build shapes stripped (see table) → `images/collage-task-mapping.png` (1010×1281)
- source: `16-Circumvention.pptx` slide 100 → `images/collage-case-study.png` (2012×1206)
- source: `16-Circumvention.pptx` slide 110 → `images/decoy-routing-passive-tap.png` (1971×1272)
- source: `16-Circumvention.pptx` slide 108 embedded picture → `images/slide108_img284.png` (existing extraction, now embedded)
