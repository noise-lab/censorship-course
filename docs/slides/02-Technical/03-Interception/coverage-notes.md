# 02-Technical/03-Interception — instructor notes

New deck (Nov 2026). It covers intercepting encryption (state root certificates, the browser
response, detection) and filtering inside applications (client- and server-side keyword
lists, super-apps and mini-programs, app stores), and what network measurement can't see.
Its dictated narration becomes book **§2.2.5**, which answers a press reviewer's request to
bring the technical chapter up to date on "TLS interception … microapps." The section is
being written fresh from that dictation: no existing or draft book text on this topic was
used as a source.

## Current-events updates made (point 2)
- 2026-11-05 (initial build): every fact below was verified by web search on this date.
  - **Vignette:** Aug 3, 2026, Russian banks (VTB, Sber, Alfa-Bank, Rosselkhozbank,
    Promsvyazbank, Uralsib, Bank Saint Petersburg) moved to the Ministry of Digital
    Development's CA; sites failed in Chrome, Safari, Edge. Sources: iXBT and RIA (Aug 4, 2026).
    iXBT names GlobalSign's June 2026 revocations as the trigger. Other outlets give
    different causes (a CA/Browser Forum sanctions-screening rule; TrustAsia as the
    previous CA); the slide says only "foreign CAs revoked their certificates."
  - **ECH:** RFC 9849, March 2026 (with RFC 9848 for the DNS bootstrapping).
  - **Kazakhstan:** July 17 – Aug 7, 2019 (21 days, intermittent), 37 domains, AS9198, 7–24%
    of 6,736 hosts (Raman et al., IMC 2020). Browsers blocked Aug 21, 2019 (Mozilla, Google;
    Apple by statement). Dec 6, 2020 exercise; Mozilla, Google, Apple, Microsoft blocked
    Dec 18, 2020. **No later attempt found** through Nov 2026.
  - **Mauritius:** ICTA consultation Apr 14, 2021; Mozilla/Google joint objection (May 2021).
    The Internet Society says it was removed from consideration; no official withdrawal found.
  - **Russia CA:** launched Mar 2022; not in any major root program.
  - **HTTPS interception prevalence:** Durumeric et al., NDSS 2017 (4.0% / 6.2% / 10.9%).
  - **Detection:** DigiNotar (Aug 2011), CNNIC (Apr 1–2, 2015), Chrome CT requirement for
    certificates issued after Apr 30, 2018. Chromium FAQ: pinning skipped for private trust
    anchors; Chrome CT policy exempts locally trusted CAs.
  - **In-app filtering:** TOM-Skype (Oct 1, 2008; FOCI 2011); YY and others (FOCI, Aug 10,
    2015); Censored Contagion (Mar 3, 2020: YY +45 keywords Dec 31, 2019); One App, Two
    Systems (Nov 30, 2016); We Chat, They Watch (May 2020); Missing Links (Apr 26, 2023);
    Engrave Danger (Aug 18, 2021).
  - **WeChat scale:** 1,439M combined MAU at June 30, 2026 (Tencent Q2 2026 results).
  - **Mini-programs:** MIIT filing notice published Aug 4, 2023; new apps from Sept 1, 2023,
    existing by Mar 31, 2024.
  - **Max:** preinstall mandate from Sept 1, 2025; InterSecLab report Sept 24, 2026 (v1.2 Oct 22).
  - **App stores:** China, Jul 29, 2017 (674 VPN apps in 2017, per Apple's reply to Senators
    Cruz and Leahy); Apr 19, 2024 (WhatsApp, Threads). Russia, Jul 4, 2024 (25 providers);
    98 unavailable at Sept 16, 2024 (AppleCensorship); Mar 28, 2026 (V2Box, v2RayTun,
    Streisand, Razze, Happ; Meduza).

## Not verified (kept off the slides or labelled)
- **Mini-program censorship measurement:** no published study measuring censorship *inside*
  WeChat or Alipay mini-programs was found (only privacy and security work, e.g. Citizen Lab
  2023, PoPETs 2025, CCS 2023/2024, and the MiniCrawler measurement study). The slide states
  this as an open question.
- **Apple removal counts in Russia for 2025 (1,213 apps)** and an Oct 27, 2026 removal of
  the Incy VPN client: found only in one outlet (The Riposte, Aug 2026). Not used. Check
  Apple's Transparency Report before using.
- **Google Play in Russia (212 orders, few complied with, Mar–Apr 2025):** secondary
  (TechRadar). Mentioned in notes as "reportedly" only.
- **Xiaomi list:** contested (Lithuania NCSC vs. German BSI, XDA's reading as an ad
  blocklist). Presented as contested.
- **Kazakhstan after 2020:** absence of evidence from English- and Russian-language searches,
  not proof none occurred.

## Suggested missing coverage on broad themes (point 3)
- **Client-side scanning** (EU Chat Control, Apple's 2021 CSAM proposal) as the democratic
  version of on-device filtering; the conclusion deck covers Chat Control, so a forward
  pointer may be enough.
- **Chinese AI chatbots** as a new in-app filter (refusals on political topics). Not
  researched for this deck.
- **Enterprise and school TLS inspection** in the US (e.g., student devices), to make
  interception concrete for students.
- **Iran** tiered or "white" internet and approved apps as a third app-store-style lever.
- **QUIC** and interception: the GFW decrypts QUIC Initial packets to read SNI (Apr 2024),
  covered in the protocols deck.

## Next-year refresh notes
- **Russian state CA:** will other sectors follow the banks? Whether any major root program
  ever accepts the root; whether Russia mandates installation.
- **ECH:** deployment after RFC 9849; whether China blocks ECH directly.
- **App store counts** (Russia, China) change monthly; recheck AppleCensorship.
- **Max:** adoption and whether in-app content filtering is documented.
- **WeChat MAU:** refresh from Tencent's latest quarterly results.
- **Mini-programs:** look again for a censorship measurement study.

## Curated images
- None. Candidates: Raman et al. Figure (interception over time, July–Aug 2019); a
  screenshot of the Firefox/Chrome Kazakhstan root error; Citizen Lab's client-side vs.
  server-side diagram from Censored Contagion; a capture of a bank's
  ERR_CERT_AUTHORITY_INVALID page from Aug 2026.

## Source
- **New deck.** No pptx or `_source-extract.md`.
- **Built from the instructor's own materials:**
  - `02-Technical/01-Protocols`: "Encryption Is Eroding On-Path Filtering," "Defending
    TCP/IP" (SNI and ECH as the front line).
  - `02-Technical/02-Throttling-DoS`: the SNI-vs-ECH slide (Russia TSPU, Nov 2024).
  - `05-Measurement/01-Measurement`: the Kazakhstan rogue-root bullet.
  - `07-Conclusion/01-Conclusion`: "Encryption at Both Ends" (client-side scanning).
  - `docs/agenda/2026-autumn.md`: the DNSSEC root-of-trust discussion and keychain demo.
  - `docs/breakouts/vpn.md`: Apple's 2017 China VPN removals.
- **Not used:** any book text on this topic (including the `reviewer-draft-2026-11`
  branch). Book chapter 2 headings were read only to place the section as §2.2.5.
- **Sources for new facts** are linked row by row in `speaker-notes.md`.
