# Figure recovery: 07-Conclusion/01-Conclusion

Source: `docs/slides/ppt-archive/class/intro/18-Wrapup.pptx`, 55 slides, rendered 2026-10-16
(headless LibreOffice, 110 dpi contact sheet). No hidden slides, no pen-ink annotations.

**Outcome: nothing recovered.** Despite its file name, `18-Wrapup.pptx` is the legacy
"Chapter 8: Legal Aspects of Content Moderation" deck (CDA / Section 230, DMCA,
BitTorrent, net neutrality, zero rating, kill-switch proposals). The Quarto deck
"The Future of Information Control" was rebuilt from this extract plus the
`class/19-Conclusion` Marp governance deck and book Ch. 7, and it covers none of the
topics the pptx draws. Every drawn diagram in the pptx is a duplicate of a slide in
`ppt-archive/class/regulatory/11-Legal.pptx` or `12-NetNeutrality.pptx`, whose own
Quarto decks (`04-Legal/01-Legal`, `04-Legal/02-NetNeutrality`,
`04-Legal/03-PaidPrioritization`) are the right home and are handled by their own
recovery branches. Embedding them here would be off-topic padding.

| pptx slide | class | target Quarto slide | figure name | notes |
|---|---|---|---|---|
| 1–7 | skip | | | title, central questions, CDA / Reno v. ACLU bullets |
| 8 | media | | | "Stop SESTA/FOSTA" protest photo (`images/slide008_img001.png`); dated, someone else's, legal topic |
| 9–11 | skip | | | intermediary-liability summary, DMCA divider and bullets |
| 12 | media | | | EFF "critic uses DMCA" page screenshot (`slide012_img002/003`); legal topic |
| 13–14 | skip | | | copyright bullets, BitTorrent numbered steps |
| 15–21 | skip (duplicate) | | | drawn BitTorrent swarm animation (peers, tracker, pipes, "High Hopes" piece table); same diagram as `11-Legal.pptx` slides 23–30; copyright topic |
| 22–24 | skip | | | piece-selection bullets (`11-Legal.pptx` slide 31) |
| 25–27 | skip | | | P2P enforcement bullets |
| 28 | media | | | "Copyright Enforcement Process" with a notice-email screenshot; same as `11-Legal.pptx` slide 37 |
| 29 | media | | | ISP notification letter screenshot; dated |
| 30–32 | skip | | | questions, copyright summary, net-neutrality divider |
| 33 | skip (duplicate) | | | drawn "Internet Business Model (Simplified)" cloud diagram (provider / peer / customer / destination, local-pref callout); same as `12-NetNeutrality.pptx` slide 2 and `11-Legal.pptx` slide 42; `02-NetNeutrality` and `03-PaidPrioritization` already have the business-model slide |
| 34–35 | skip | | | Open Internet Order bullets |
| 36, 39 | media | | | John Oliver "Net Neutrality" stills; someone else's |
| 37–38 | media | | | home throughput and Cogent transit plots; `02-NetNeutrality` already embeds the Cogent plot (`slide011_img012.png`) |
| 40 | skip (duplicate) | | | drawn "What's Causing This?" clouds (Cablevision / Comcast → Cogent → Netflix, Theory 1 / Theory 2); same as `12-NetNeutrality.pptx` slide 12 and `11-Legal.pptx` slide 49 |
| 41–42 | skip | | | two-sides bullets, net-neutrality summary |
| 43 | media | | | Binge On banner; zero-rating topic |
| 44 | media | | | Free Basics phone screenshot and protest photo; someone else's |
| 45–47 | skip | | | zero-rating study bullets |
| 48–52 | media | | | WhatsApp / MTN zero-rating bar charts from a student thesis (`slide048–052`); coverage-notes already rejected these |
| 53–54 | skip | | | zero-rating summary, central questions repeat |
| 55 | media | | | Wired and Lawfare kill-switch article screenshots (2011–12); dated clippings |

## Why no figure was embedded

- The Conclusion deck's themes (walls to currents, paradox of openness, impossible
  tradeoffs, generative AI, ECH, splinternet, governance, paths forward) have no
  counterpart in the pptx; the drawn diagrams are all transit-economics or BitTorrent
  mechanics.
- Each drawn diagram exists verbatim in the Legal or NetNeutrality archive deck, so
  recovering it here would create a second copy under the wrong deck and a provenance
  comment pointing at a mislabelled source.
- `coverage-notes.md` already notes that if a diagram is ever wanted for this deck it
  should be a new two-tier "protocol layer routes around damage / above-layer
  consolidation is a choke point" figure, which the pptx does not contain.

## Pointers for the owning decks

- BitTorrent swarm (slides 15–21 here) → `11-Legal.pptx` slides 23–30.
- Internet business model (slide 33) → `12-NetNeutrality.pptx` slide 2, `11-Legal.pptx` 42.
- Netflix / Cogent congestion theories (slide 40) → `12-NetNeutrality.pptx` slide 12, `11-Legal.pptx` 49.
