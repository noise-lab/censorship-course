# Speaker Notes: Internet Governance

## Opening (Slides 1-3)

**Slide 1: Title**
- This is our final lecture, bringing together all the technical and policy concepts we've covered
- We're zooming out to ask the meta-question: who actually has the authority to make decisions about what happens online?

**Slide 2: The Meta-Question**
- Throughout the quarter, we've examined three types of controls:
  - Technical: DNS manipulation, BGP hijacking, throttling, DDoS attacks
  - Platform: Content moderation, algorithmic personalization, disinformation campaigns
  - Legal: Copyright takedowns, net neutrality rules, demonetization policies
- Today: Who gets to decide when and how these controls are used?
- This isn't just academic—it's about power, legitimacy, and the future of the internet

**Slide 3: A Tale of Two Internets**
- In the 1990s, there was genuine optimism that the internet would be ungovernable
- John Perry Barlow's ["Declaration of Independence of Cyberspace" (1996)](https://www.eff.org/cyberspace-independence) claimed governments had no sovereignty over it
- Fast forward to 2025: very different reality
- The "Splinternet" thesis: internet fragmenting along national, political, and regulatory lines
- Ask students: Do they think the internet feels more unified or more fragmented today?

## Internet Governance Basics (Slides 4-6)

**Slide 4: What is Internet Governance?**
- Read the WSIS definition carefully—notice it says "governments, private sector, AND civil society"
- This is the multi-stakeholder model we'll discuss
- Key insight: governance isn't just about laws—it's about standards, norms, technical protocols
- Examples: Who decides what a "valid" domain name is? Who sets email standards? Who controls IP address allocation?

**Slides 5-6: The Key Players**
- Technical organizations:
  - [ICANN](https://www.icann.org/): Controls DNS root zone, coordinates IP addresses
  - [IETF](https://www.ietf.org/): Develops technical standards (HTTP, TCP/IP, etc.)
  - RIRs: Five regional bodies that allocate IP addresses ([ARIN](https://www.arin.net/) for North America, [RIPE](https://www.ripe.net/) for Europe, etc.)
- Intergovernmental:
  - [ITU](https://www.itu.int/): UN's oldest specialized agency, wants greater control
  - UN General Assembly: Occasionally weighs in
  - Regional bodies: EU especially active with regulations
- Private sector: Platforms and infrastructure providers have enormous de facto power
- Civil society: Digital rights organizations, user advocacy groups, academic researchers

**Slide 7: ICANN**
- Founded 1998 to take over functions from US government's IANA
- Until 2016, US Commerce Department had oversight—this was controversial
- [2016 transition to "global multi-stakeholder community"](https://www.icann.org/stewardship) was supposed to address concerns
- But Russia, China, and others still see it as too US-influenced
- Key power: controlling the root zone file
- Example: When countries split (like Sudan/South Sudan), who decides domain ownership?
- The .io case study on next slide shows how technical decisions become political

## ICANN and Multi-Stakeholder Model (Slides 8-10)

**Slide 8: .io Domain Case**
- .io domains are hugely popular with tech companies (GitHub.io, etc.)
- British Indian Ocean Territory is/was controversial—Chagossians forcibly removed for US military base
- [UK announced return to Mauritius in 2024](https://www.theregister.com/2024/10/10/io_domain_uk_mauritius/)
- Technical question: If the country code changes or disappears, what happens to millions of domains?
- ICANN has precedent: .yu (Yugoslavia) was phased out, .su (Soviet Union) still exists
- **Read in class**: [ICANN's official statement on .io domain](https://www.icann.org/en/blogs/details/the-chagos-archipelago-and-the-io-domain-14-11-2024-en)
- This shows how seemingly technical decisions have major economic and political implications

**Slide 9: Multi-Stakeholder Model**
- This is the dominant model for internet governance today
- Four pillars work together—no one has absolute authority:
  - Governments: Can pass laws, regulate, but can't unilaterally control technical standards
  - Private sector: Operates infrastructure, makes day-to-day decisions
  - Civil society: Represents users, advocates for rights
  - Technical community: Sets standards based on technical merit
- Key insight: "Unequal power distribution"—in practice, some voices matter more than others

**Slide 10: Multilateral Challenge**
- Russia and China (and some others) prefer traditional multilateral model
- Multilateral = government-to-government, like UN voting
- They argue multi-stakeholder gives too much power to Western companies and NGOs
- "Cyber sovereignty" doctrine: each nation should control its internet space
- This is a fundamental ideological divide in internet governance
- Ask: What are the trade-offs? Control vs. openness, security vs. freedom

## National Models: Russia, China, EU (Slides 11-15)

**Slide 11: Russia's Sovereign Internet**
- [RuNet law passed 2019](https://en.wikipedia.org/wiki/Sovereign_Internet_Law), implemented gradually
- Required ISPs to install DPI (deep packet inspection) equipment at their own expense
- Government can theoretically cut Russia off from global internet during "emergencies"
- Centralized routing through state-controlled points
- Justification: "protecting critical infrastructure" from foreign threats
- **Key reading**: [Human Rights Watch analysis (2019)](https://www.hrw.org/news/2019/10/31/russia-new-law-expands-government-control-online)

**Slide 12: Russia's Sovereign Internet (continued)**
- By 2024, regular tests of disconnection capabilities
- VPN crackdowns—fines for VPN providers that don't block banned sites
- Some VPNs blocked entirely
- Moving toward parallel infrastructure (separate from global internet)
- Ukraine war accelerated these efforts
- This is the most extreme example of trying to build a sovereign internet
- **Updated analysis**: [HRW 2025 report on Russian internet isolation](https://www.hrw.org/report/2025/07/30/disrupted-throttled-and-blocked/state-censorship-control-and-increasing-isolation)

**Slide 13: China's Great Firewall**
- We covered GFW technical details earlier in the course
- Key point today: China isn't just blocking—it's building alternative governance
- Own DNS roots (some experiments with non-ICANN systems)
- Cybersecurity Law (2017) requires data localization
- "Internet sovereignty" as official doctrine
- Most importantly: exporting this model

**Slide 14: China's Digital Silk Road**
- Part of [Belt and Road Initiative's digital component](https://en.wikipedia.org/wiki/Digital_Silk_Road)
- Exporting surveillance technology, content filtering systems
- Training officials from other countries
- Countries adopting: Pakistan, Ethiopia, Uganda, others (over 80 countries total)
- This is about exporting a governance model, not just technology
- Contrast with US/EU export of internet freedom technologies
- **Key readings**:
  - [CFR overview of Digital Silk Road](https://www.cfr.org/china-digital-silk-road/)
  - [Recorded Future: "Digital Colonialism" report](https://www.recordedfuture.com/research/china-digital-colonialism-espionage-silk-road)
  - [VOA: Exporting internet controls](https://www.voanews.com/a/china-s-digital-silk-road-exports-internet-technology-controls/7626266.html)

**Slide 15: The EU's Third Way**
- EU positioning itself as middle path between US and China
- Not hands-off (like traditional US approach) but not authoritarian
- [GDPR (2018)](https://gdpr.eu/): Privacy as fundamental right, individual data control
- [Digital Services Act (2022)](https://digital-strategy.ec.europa.eu/en/policies/digital-services-act-package): Platform accountability for illegal content
- [Digital Markets Act (2022)](https://digital-markets-act.ec.europa.eu/index_en): Antitrust for digital gatekeepers
- [AI Act (2024)](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai): Risk-based regulation of AI systems
- "Brussels Effect": EU regulations become de facto global standards because companies comply globally

## Case Studies: Right to be Forgotten, Splinternet (Slides 16-18)

**Slide 16: Right to be Forgotten**
- [Google Spain v. AEPD (2014)](https://en.wikipedia.org/wiki/Google_Spain_v_AEPD_and_Mario_Costeja_Gonz%C3%A1lez) established this right in EU
- Individuals can request search engines remove links to information about them
- Google must comply for EU searches (google.de, google.fr, etc.)
- But should it apply to google.com globally?
- 2019 ruling said no—compliance only required in EU
- This creates interesting tensions: geo-blocking search results
- Also creates compliance complexity: different rules for different regions
- **Official case**: [EU Court of Justice judgment (C-131/12)](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:62012CJ0131)
- **Analysis**: [Columbia Global Freedom of Expression case summary](https://globalfreedomofexpression.columbia.edu/cases/google-spain-sl-v-agencia-espanola-de-proteccion-de-datos-aepd/)

**Slide 17: Splinternet Hypothesis**
- Are we seeing one internet or many?
- Evidence FOR fragmentation:
  - National firewalls (China, Russia, Iran all have different levels)
  - 60+ countries have data localization laws (data must be stored locally)
  - Regional content rules diverge (what's legal in US might not be in EU)
  - Platforms show different content by region
- Evidence AGAINST:
  - TCP/IP, HTTP, DNS still globally unified at technical level
  - Data does flow across borders (albeit with restrictions)
  - Platforms adapt rather than split (Facebook in Germany vs US is same platform)
- Reality: probably both—technical unity, regulatory fragmentation

**Slide 18: India's IT Rules 2021**
- [Information Technology (Intermediary Guidelines and Digital Media Ethics Code) Rules, 2021](https://www.meity.gov.in/content/information-technology-intermediary-guidelines-and-digital-media-ethics-code-rules-2021) represent India's approach
- 36-hour takedown requirement for illegal content
- Traceability requirements threaten end-to-end encryption (very controversial)
- Must have grievance officer physically in India
- "Significant social media intermediaries" = 5M+ users
- Result: WhatsApp, Facebook, Twitter hiring thousands of moderators in India
- This shows how large countries can force global platforms to adapt
- **Official text**: [MeitY PDF of IT Rules 2021](https://www.meity.gov.in/static/uploads/2024/02/Information-Technology-Intermediary-Guidelines-and-Digital-Media-Ethics-Code-Rules-2021-updated-06.04.2023-.pdf)
- **Summary**: [PRS Legislative Research overview](https://prsindia.org/billtrack/the-information-technology-intermediary-guidelines-and-digital-media-ethics-code-rules-2021)

## Jurisdictional Conflicts (Slides 19-23)

**Slide 19: Australia vs. Meta**
- 2024 case: [Wakeley church stabbing video in Sydney (April 2024)](https://www.itnews.com.au/news/meta-and-x-cop-takedown-orders-over-sydney-stabbing-videos-607119)
- Australia issued takedown order—demanded GLOBAL removal
- Meta complied in Australia but not worldwide; X refused entirely
- Court case about extraterritorial reach of Australian law
- Raises question: Can one country's laws apply globally?
- If yes: creates "race to the bottom" (most restrictive country wins)
- If no: makes enforcement difficult for individual countries
- **Key articles**:
  - [iTNews: Meta and X receive takedown orders](https://www.itnews.com.au/news/meta-and-x-cop-takedown-orders-over-sydney-stabbing-videos-607119)
  - [Al Jazeera: Court eventually lifts ban](https://www.aljazeera.com/news/2024/5/13/australian-court-lifts-social-media-ban-on-sydney-church-stabbing-video)
  - [VOA: Musk vs Australia clash](https://www.voanews.com/a/australia-and-x-s-elon-musk-clash-over-church-stabbing-video/7582784.html)

**Slide 20: DNS Wars**
- The root of the internet—literally
- US government historically oversaw ICANN through NTIA
- 2016 transition was supposed to internationalize
- But Russia and China remain skeptical
- Alternative roots: China has experimented with separate DNS infrastructure
- If this happens: websites might not be reachable depending on which DNS system you use
- Like telephone networks before they were interconnected—can't call between systems

**Slide 21: Content Moderation Governance**
- Who decides what's acceptable online?
- Current model: platforms decide within legal boundaries set by governments
- Users have very limited input (can report, appeal, but no real power)
- AI systems enforce rules, but opaquely
- This is unsatisfying to almost everyone
- Governments say platforms have too much power
- Platforms say they're doing their best with impossible task
- Users feel unheard

**Slide 22: Emerging Models**
- [Meta's Oversight Board](https://www.oversightboard.com/): independent body that reviews content decisions
  - Funded by Meta but supposedly independent
  - Has overturned some Meta decisions
  - Critics say it's window dressing; defenders say it's real accountability
  - **Show in class**: Browse recent cases at [oversightboard.com](https://www.oversightboard.com/)
- [Mastodon](https://joinmastodon.org/): federated, each instance sets own rules
  - If you don't like rules, move to different instance
  - But: most users on a few large instances
- [BlueSky](https://bsky.app/): user choice in algorithms
  - Can choose what algorithmic ranking you want
  - Custom feeds, community moderation

**Slide 23: Twitter/X Case Study**
- 2023-2024: Elon Musk takes over, changes moderation policies unilaterally
- Shows risk of centralized platforms with single owner
- Governments respond: [Brazil ban (briefly)](https://www.bbc.com/news/articles/c9vp4xrzznpo), India pressure, EU investigations
- Users migrate to Mastodon, BlueSky, Threads
- Advertisers pull back (some return later)
- Key lesson: centralized platforms = centralized governance
- One person can change rules for hundreds of millions of users

## Cross-Border Challenges (Slides 24-26)

**Slide 24: Cross-Border Enforcement**
- Fundamental problem: internet is global, laws are national
- French court ordering content removal—but US First Amendment protects it
- EU fines for global operations (Google, Meta pay billions)
- Chinese data localization vs. cloud computing architecture
- Jurisdiction shopping: bad actors operate from permissive jurisdictions
- No easy answers—this tension is inherent

**Slide 25: Encryption Governance**
- Who decides acceptable levels of encryption?
- US Crypto Wars (1990s): government tried to limit encryption, lost
- Then shift toward "going dark" problem (2000s-present)
- [UK Investigatory Powers Act (2016)](https://www.gov.uk/government/collections/investigatory-powers-bill): can compel assistance in accessing encrypted data
- [EU Chat Control proposals](https://www.patrick-breyer.de/en/posts/chat-control/): scan messages before encryption
- [Australia Assistance and Access Act (2018)](https://www.homeaffairs.gov.au/about-us/our-portfolios/national-security/lawful-access-telecommunications/data-encryption): can compel companies to create access
- Technical vs. political authority:
  - Cryptographers: "You can't build backdoors that only good guys can use"
  - Governments: "We need access to fight terrorism, child exploitation"
  - Platforms: caught in the middle, facing conflicting legal requirements
- **Key readings**:
  - [CSIS analysis of UK Act](https://www.csis.org/analysis/new-investigatory-powers-act-united-kingdom-enhances-government-surveillance-powers)
  - [Carnegie Endowment: Australia encryption debate](https://carnegieendowment.org/posts/2021/03/the-encryption-debate-in-australia-2021-update?lang=en)

**Slide 26: Emerging Challenges**

**AI and LLMs create new governance questions:**
- Who governs AI-generated content? Is it speech? Whose responsibility?
- Training data governance: who owns the data, who can use it?
- Algorithmic accountability: how do we audit black-box systems?
- Deepfakes and misinformation: existing laws don't quite fit

**Web3 and decentralization:**
- Blockchain governance models: code is law?
- DAOs: decentralized autonomous organizations with no legal entity
- Immutable content: what if illegal content is on blockchain?

**Key point:** These technologies challenge existing governance frameworks

## Governance Challenges and Future Models (Slides 27-30)

**Slide 27: Impossibility of Universal Governance**
- Why is universal internet governance so hard?
  - Different values: Free speech absolutism (US) vs. dignity/limits (EU) vs. social stability (China)
  - Competing interests: privacy vs. security, often zero-sum
  - Technical architecture: internet was designed decentralized, hard to control centrally
  - Economic incentives: advertising model vs. privacy protection
  - Speed of change: technology evolves faster than laws
- Reality: we'll have multiple overlapping governance regimes
- Question: Is that okay? Or should we keep trying for unified approach?

**Slide 28: Models for the Future - Part 1**
- Three broad paths forward:

**Option 1: Status Quo Plus**
- Multi-stakeholder model continues
- Incremental improvements (like ICANN transition)
- Regional variation accepted as reality
- **Pros:** works reasonably well, avoids radical change
- **Cons:** leaves existing power imbalances, doesn't resolve tensions

**Slide 29: Models for the Future - Part 2**

**Option 2: Re-centralization**
- Greater government role, maybe through ITU or UN
- Multilateral agreements (like climate treaties)
- More democratic (one country, one vote)?
- **Pros:** more national sovereignty, clearer accountability
- **Cons:** could enable authoritarian control, slow decision-making

**Option 3: Radical Decentralization**
- Technical solutions to governance (e.g., encryption, blockchain)
- End-to-end encryption for everything
- Federated/distributed architecture (like Mastodon at scale)
- **Pros:** harder to censor, user empowerment
- **Cons:** harder to address harms (child exploitation, terrorism), technical barriers

**Slide 30: What We've Learned This Quarter**
- Connect back to course themes:
  - Technical controls → protocol governance matters (DNS, BGP decisions shape what's possible)
  - Platform controls → private governance is real governance (Meta's decisions affect billions)
  - Legal controls → national laws shape global networks (GDPR, China's laws)
  - Measurement → transparency enables accountability (we can't govern what we can't see)
  - Circumvention → control is never absolute (VPNs, Tor show limits)
  - Governance → power is contested, always (no final answers)

## Course Synthesis and Discussion (Slides 31-35)

**Slide 31: The Core Tension**
- These tensions run through every topic we've covered:
  - Freedom vs. Safety: Tor enables both dissidents and criminals
  - Privacy vs. Accountability: Encryption protects both whistleblowers and terrorists
  - Innovation vs. Stability: New protocols enable progress but disrupt governance
  - Global vs. Local: Global platforms vs. national sovereignty
  - Public vs. Private: Should governments or companies make these decisions?
- Key insight: These aren't problems with solutions—they're permanent tensions to manage
- Different societies will balance them differently

**Slide 32: Discussion Questions**
- Break into these if time permits:

1. **Should internet governance be primarily technical or political?**
  - Technical: based on what works, merit-based, apolitical
  - Political: based on democratic legitimacy, values, representation
  - Most say "both" but where's the line?

2. **Is the "splinternet" inevitable? Desirable?**
  - Some argue it's already here
  - Others say technical unity remains
  - Is unified internet worth the cost of accepting different values?

3. **Can platforms be held accountable without government control?**
  - Oversight boards, transparency reports, user councils
  - Or do we need regulation?
  - What about competitive accountability (users can leave)?

4. **What role should users have in governance decisions?**
  - Currently very limited
  - Federated models give more power
  - But most users don't want to be governors

5. **How do we govern technologies that don't exist yet?**
  - AI, quantum computing, neural interfaces
  - Can't regulate specifics before they exist
  - But waiting allows harms to entrench

**Slide 33: Looking Forward**
- You now have tools to:
  - Understand HOW censorship works technically
  - Understand WHY it happens (motivations vary)
  - Understand WHO does it (states, platforms, infrastructure)
  - Measure it (OONI, Censored Planet, custom tools)
  - Resist it (VPNs, Tor, circumvention)
- Now: WHO SHOULD DECIDE?
- This is the normative question you'll grapple with in careers

**Slide 34: Final Thoughts**
- Core message: The internet is not ungoverned—it never was
- Even in the 1990s, there were norms, protocols, decisions
- But governance was informal, technical, US-dominated
- Now it's explicit, contested, multi-polar
- The real questions:
  - Who has legitimacy to govern?
  - How do they exercise that power?
  - For whom do they govern (whose interests)?
  - With what accountability mechanisms?
- These questions will define the next 30 years of internet

**Slide 35: Thank You**
- Remind about office hours and final project deadline
- Encourage students to stay engaged with these issues in their careers
- Whether they work on platforms, at ISPs, in government, or as researchers
- These governance questions will shape their work
- Stay curious: keep questioning whose interests are served
- Stay critical: don't accept "that's just how it works"
- Stay engaged: these decisions need diverse voices

## Potential Follow-Up Questions from Students

**Q: "Isn't the multi-stakeholder model just a way for US companies to maintain control?"**
- Fair criticism. In practice, US companies and technical community have outsized influence
- But alternative (multilateral) could enable authoritarian control
- Maybe need reforms to multi-stakeholder rather than replacement?

**Q: "Could we have different internets that are incompatible?"**
- Technically possible if DNS roots diverge
- Or if countries require separate physical infrastructure
- But expensive and inconvenient—strong incentives for interoperability
- More likely: one technical internet, many regulatory regimes

**Q: "What about blockchain/Web3 as governance solution?"**
- Interesting experiments but not panacea
- DAOs have governance issues (who writes the code?)
- Immutable ledgers make moderation impossible
- Still requires underlying internet infrastructure (controlled by others)
- Good to watch, but don't expect magic solution

**Q: "Should platforms be regulated like utilities?"**
- Compelling argument: they're essential infrastructure
- But: stifles innovation, creates regulatory capture risk
- Also: which platforms? Just big ones? Where's the line?
- Interoperability requirements might be better solution

**Q: "What happens to internet governance if US-China tensions escalate?"**
- Real risk of technological decoupling
- Already seeing this in 5G (Huawei bans)
- Could extend to internet protocols, standards
- Would be enormously costly and inefficient
- But political considerations might override economic ones

## Time Management Notes

- If running short on time:
  - Skip detailed case studies (India, Australia)
  - Focus on core governance models (slides 8-9, 13-14)
  - Ensure time for discussion questions (slide 31)

- If have extra time:
  - Deep dive into one case study (e.g., Right to be Forgotten)
  - Student presentations of their final projects
  - Open discussion on which future model they prefer

## Key Takeaways for Students

- Internet governance involves technical, legal, and political dimensions
- Power is distributed but unequally—some actors have more influence
- No consensus on who should have authority to govern
- Multi-stakeholder vs. multilateral is fundamental divide
- National regulation is fragmenting the internet
- These tensions are permanent features, not bugs to fix
- Their generation will shape the next era of internet governance

---

## Quick Reference: All Case Study Links

### Foundational Documents
- [John Perry Barlow's Declaration of Independence of Cyberspace (1996)](https://www.eff.org/cyberspace-independence)

### Technical Organizations
- [ICANN](https://www.icann.org/) - Domain names and IP addresses
- [IETF](https://www.ietf.org/) - Internet technical standards
- [ARIN](https://www.arin.net/) - North American IP registry
- [RIPE](https://www.ripe.net/) - European IP registry
- [ITU](https://www.itu.int/) - UN telecommunications agency

### .io Domain Case Study
- [The Register: .io domain not going anywhere soon](https://www.theregister.com/2024/10/10/io_domain_uk_mauritius/)
- [ICANN official statement on .io domain](https://www.icann.org/en/blogs/details/the-chagos-archipelago-and-the-io-domain-14-11-2024-en)

### Russia's Sovereign Internet
- [Wikipedia: Sovereign Internet Law](https://en.wikipedia.org/wiki/Sovereign_Internet_Law)
- [Human Rights Watch: Russia's 2019 law expands control](https://www.hrw.org/news/2019/10/31/russia-new-law-expands-government-control-online)
- [HRW 2025 report: Disrupted, throttled, and blocked](https://www.hrw.org/report/2025/07/30/disrupted-throttled-and-blocked/state-censorship-control-and-increasing-isolation)

### China's Digital Silk Road
- [Wikipedia: Digital Silk Road](https://en.wikipedia.org/wiki/Digital_Silk_Road)
- [Council on Foreign Relations: Digital Silk Road overview](https://www.cfr.org/china-digital-silk-road/)
- [Recorded Future: China's Digital Colonialism report](https://www.recordedfuture.com/research/china-digital-colonialism-espionage-silk-road)
- [VOA: Exporting internet controls](https://www.voanews.com/a/china-s-digital-silk-road-exports-internet-technology-controls/7626266.html)

### EU Regulations
- [GDPR official site](https://gdpr.eu/)
- [Digital Services Act (DSA)](https://digital-strategy.ec.europa.eu/en/policies/digital-services-act-package)
- [Digital Markets Act (DMA)](https://digital-markets-act.ec.europa.eu/index_en)
- [AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

### Right to be Forgotten
- [Wikipedia: Google Spain v AEPD case](https://en.wikipedia.org/wiki/Google_Spain_v_AEPD_and_Mario_Costeja_Gonz%C3%A1lez)
- [EU Court of Justice official judgment (C-131/12)](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:62012CJ0131)
- [Columbia Global Freedom of Expression case summary](https://globalfreedomofexpression.columbia.edu/cases/google-spain-sl-v-agencia-espanola-de-proteccion-de-datos-aepd/)

### India's IT Rules 2021
- [MeitY official page](https://www.meity.gov.in/content/information-technology-intermediary-guidelines-and-digital-media-ethics-code-rules-2021)
- [Official PDF of IT Rules 2021](https://www.meity.gov.in/static/uploads/2024/02/Information-Technology-Intermediary-Guidelines-and-Digital-Media-Ethics-Code-Rules-2021-updated-06.04.2023-.pdf)
- [PRS Legislative Research overview](https://prsindia.org/billtrack/the-information-technology-intermediary-guidelines-and-digital-media-ethics-code-rules-2021)

### Australia vs Meta (2024)
- [iTNews: Meta and X receive takedown orders](https://www.itnews.com.au/news/meta-and-x-cop-takedown-orders-over-sydney-stabbing-videos-607119)
- [Al Jazeera: Court lifts ban](https://www.aljazeera.com/news/2024/5/13/australian-court-lifts-social-media-ban-on-sydney-church-stabbing-video)
- [VOA: Musk vs Australia](https://www.voanews.com/a/australia-and-x-s-elon-musk-clash-over-church-stabbing-video/7582784.html)

### Encryption Governance
- [UK Investigatory Powers Act (GOV.UK)](https://www.gov.uk/government/collections/investigatory-powers-bill)
- [CSIS analysis of UK Investigatory Powers Act](https://www.csis.org/analysis/new-investigatory-powers-act-united-kingdom-enhances-government-surveillance-powers)
- [Australia Assistance and Access Act](https://www.homeaffairs.gov.au/about-us/our-portfolios/national-security/lawful-access-telecommunications/data-encryption)
- [Carnegie Endowment: Australia encryption debate](https://carnegieendowment.org/posts/2021/03/the-encryption-debate-in-australia-2021-update?lang=en)
- [EU Chat Control proposals (Patrick Breyer MEP)](https://www.patrick-breyer.de/en/posts/chat-control/)

### Alternative Governance Models
- [Meta's Oversight Board](https://www.oversightboard.com/)
- [Mastodon](https://joinmastodon.org/)
- [BlueSky](https://bsky.app/)

### Twitter/X Case Study
- [BBC: Brazil X ban](https://www.bbc.com/news/articles/c9vp4xrzznpo)
