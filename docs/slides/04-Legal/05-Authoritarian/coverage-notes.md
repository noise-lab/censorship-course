# 04-Legal/05-Authoritarian — instructor notes

New deck for one segment of Meeting 13 (Tue Nov 10, 2026), alongside economic controls.
Its narration will become book §4.1.1 (law as information control in authoritarian
states). It answers a press reviewer's request for "a small section of rules and laws from
authoritarian regimes." No book text about authoritarian law was used as a source; the
section is to be written from the lecture.

## Current-events updates made (point 2)
- 2026-11-05 (initial build): all facts below were verified by web search on this date.
  - **China**
    - 1996 State Council Interim Provisions (Decree 195, Feb 1, 1996), Art. 6: international traffic only through state channels.
    - MIIT notice on VPNs and cross-border channels: Jan 2017.
    - Cybersecurity Law: adopted Nov 7, 2016; in force June 1, 2017. Arts. 12, 24, 37, 47, 50, 58 checked against the DigiChina translation.
    - CSL amendment: adopted Oct 28, 2025; in force Jan 1, 2026 (law-firm summaries: Latham, DLA Piper, Reed Smith).
    - Generative-AI Interim Measures: in force Aug 15, 2023; Art. 4(1) "Uphold the Core Socialist Values" (China Law Translate).
    - Cyberspace ID measures: in force July 15, 2025 (Library of Congress).
  - **Russia**
    - Sovereign Internet law 90-FZ: May 1, 2019; in force Nov 1, 2019 (HRW).
    - "Fakes" law, Art. 207.3: Mar 4, 2022; up to 15 years (TASS).
    - Foreign agents 255-FZ: in force Dec 1, 2022 (HRW, Roskomnadzor register).
    - Search and VPN-ad fines: signed July 31, 2025; in force Sept 1, 2025 (Meduza, TASS).
    - Max preinstall: Sept 1, 2025. Calls on WhatsApp/Telegram restricted Aug 2025 (HRW, Mar 12, 2026).
    - Feb 2026: YouTube, WhatsApp and others removed from the national DNS (Meduza, Feb 12, 2026). FSB shutdown amendments signed Feb 2026 (HRW; Freedom House).
    - Telegram: OONI anomalies at 95% on Apr 10, 2026 (Meduza); no formal ban announced.
  - **Iran**
    - Computer Crimes Law (2009), Arts. 21–23 (UNODC text); Supreme Council of Cyberspace (2012).
    - Sept 21, 2022: WhatsApp and Instagram blocked (OONI).
    - Jan 8, 2026: nationwide shutdown begins (TechCrunch, Cloudflare).
    - Freedom on the Net 2026 (Oct 2026): 20-day protest shutdown; ~88-day shutdown from late Feb 2026; score 13 → 9; "Internet Pro" at ~5× price.
  - **Vietnam:** Decree 147, issued Nov 9, 2024; in force Dec 25, 2024 (VietnamNet, AFP).
  - **Turkey:** Law 5651 amendments of July 2020 (Law 7253) and Oct 2022 (Law 7418, Art. 217/A) (HRW, EFF, Article 19).
  - **India:** IT Rules amendment, G.S.R. 120(E), notified Feb 10, 2026; in force Feb 20, 2026; 3-hour clock (Rödl & Partner, Legal500; Freedom House 2026).

## Could not verify / handle with care
- **Start of Iran's ~88-day shutdown.** Freedom House says February 2026; IranWire says March; Wikipedia treats Jan 8–May 26 as one blackout. The slide says "late Feb, per Freedom House."
- **Kremlin confirmation of the WhatsApp block (Feb 12, 2026).** From the CNN headline and search summaries; the CNN page returned HTTP 451 to the fetcher. HRW and Meduza confirm the DNS removal.
- **Iran content list (9 categories, 78 items).** From a secondary source (University of Tehran journal, citing the Filtering Committee, 2021). It is in the speaker notes only, not on a slide.
- **Max user count (77.5M monthly, Feb 2026).** HRW figure, attributed to Russian sources; in the notes only.
- **"Internet Pro" pricing (~5×).** Freedom House only; no independent source checked.

## Corrections to flag in other decks
- None found. Existing Russia and Iran facts in `02-Technical/*` and `06-Circumvention/01` are consistent with this deck.
  - 469 VPN services blocked: HRW confirms.
  - YouTube throttling from July 2024: consistent with Meduza.
- `02-Technical/02-Throttling-DoS` says WhatsApp was throttled in 2025 "as a soft precursor to a full ban." That ban came in Feb 2026. Worth a one-line update at the next refresh.

## Suggested missing coverage on broad themes (point 3)
- **Export of the legal template.** This deck shows Vietnam copying China. A slide on Russia's laws spreading to Central Asia (Kyrgyzstan, Kazakhstan foreign-agent and "false information" laws) would make the diffusion point from the intro deck legal rather than technical. Not researched this session.
- **Courts as a counterweight inside hybrid regimes.** Turkey's Constitutional Court has struck down blocks (Wikipedia 2019, Twitter 2014). This would sharpen the "recourse" row on the comparison slide. Not verified this session.
- **Myanmar and Ethiopia.** These are the shutdown-by-decree cases outside the big three. Freedom House 2026 ranks Myanmar with China among the worst.
- **Belarus,** as the closest copy of the Russian model.

## Next-year refresh notes
- **Iran.** Whether "Internet Pro" persists, and whether global access returns for ordinary users. Freedom on the Net 2027 will have a new shutdown count.
- **Russia.**
  - Telegram's status: still no formal ban.
  - Whether WhatsApp remains blocked.
  - Any use of the Feb 2026 FSB shutdown powers.
  - Max adoption figures.
- **China.** First enforcement of the CSL's extraterritorial clause (none announced as of Nov 2026). Also the draft rules on content "harmful" to minors (June 2025 draft, per Freedom House).
- **India.** Court challenges to the 3-hour rule.
- **Turkey.** The under-15 social-media bill (April 2026, e-Devlet age gating), per Freedom House.

## Curated images
- None. The deck is text and tables. Candidates if wanted:
  - Cloudflare Radar's Iran traffic graph for Jan 8, 2026;
  - OONI's Telegram-in-Russia anomaly chart (Apr 2026);
  - a capture of the Roskomnadzor foreign-agent register.

## Source
- **New deck.** No pptx or `_source-extract.md`.
- **Built from primary and reputable sources** (above) and from the instructor's own decks:
  - `01-Intro/01-Overview`: GFW history, Turkey 2014, India's 65 shutdowns, Freedom House diffusion.
  - `02-Technical/01-Protocols`: Iran's June 2025 stealth blackout, Russia's YouTube throttling.
  - `02-Technical/02-Throttling-DoS`: Twitter throttling and TSPU, the WhatsApp throttle and Max, ECH blocking.
  - `03-Platform/01-Platform`: India IT Rules, state pressure through platforms.
  - `04-Legal/01-Legal`: §230, DSA, NetzDG, Australia's under-16 ban.
  - `06-Circumvention/01-Circumvention`: Russia's VPN blocking.
- **Not used:** the book repo's `reviewer-draft-2026-11` branch, or any book text on authoritarian law.
