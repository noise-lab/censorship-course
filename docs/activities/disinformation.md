# Disinformation

Disinformation is false or misleading information that is spread deliberately
to deceive people. It is often spread through social media, news outlets, and
other forms of communication. Disinformation can be used to manipulate public
opinion, influence political decisions, and create confusion. It can also be
used to discredit individuals or organizations.

In this activity, you will explore various sources of disinformation, and
discuss various ways to combat it.

## Part 1: Exploring Fake News Sites

In this activity, you will explore several fake news sites and discuss the
ways that they may be similar or different to authentic news sites.

A framing note before you start: the audience for these sites is increasingly
machines, not people. Few readers ever land on a site's front page (most arrive
via a direct link from a post), and now a site may not need a human reader at
all. It just has to be on the web where crawlers pick it up to feed AI search
and answer engines (Google AI Overviews, Perplexity, ChatGPT search, Copilot),
retrieval-augmented generation (RAG) pipelines, and training corpora such as
Common Crawl. Keep both audiences in mind as you work through the questions.

1. Explore a handful of fake news sites. Some places to find them:

    - [Hounsel et al. 2020 training set](https://github.com/ahounsel/disinfo-infra-public/blob/master/src/system/data/training/disinformation_domains.csv):
      the 539 domains used in "Identifying Disinformation Websites Using
      Infrastructure Features" (FOCI 2020). It is six years old: about a
      third no longer resolve, and many of the rest are parked or have been
      re-sold as spam sites, which is itself worth noticing.
    - [Iffy Index of Unreliable Sources](https://iffy.news/index/): about
      2,000 low-credibility domains, updated through 2025, with a public
      spreadsheet and CSV export. Each row links to its Media Bias/Fact
      Check review.
    - [Wikipedia: List of fake news websites](https://en.wikipedia.org/wiki/List_of_fake_news_websites):
      a smaller, cited list with an active/defunct status column, edited as
      recently as September 2026.
    - [VIGINUM "Portal Kombat" domain list](https://github.com/VIGINUM-FR/Rapports-Techniques/tree/main/202402%20-%20Portal%20Kombat)
      and the [American Sunlight Project Pravda database](https://www.americansunlight.org/portal-kombat-pravda-database):
      a few hundred domains of the pro-Russian "Pravda" network (2024–25),
      nearly all still live, run from shared infrastructure. Replace `[.]`
      with `.` in the VIGINUM file. The ASP sheet already includes WHOIS
      creation dates you can check against `whois`.
    - [Domain quality ratings (Lin et al. 2023)](https://github.com/hauselin/domain-quality-ratings):
      an aggregate 0–1 credibility score for about 11,500 domains, useful as
      labels if you try the classifier question below.

2. What are some of the common features of these sites? What are some of the
   differences? Separate the features a human visitor would notice (design,
   layout, ads, bylines, tone) from the features a crawler would "see" (the
   text of the article, its headline and metadata, the publication date,
   links to and from other sites, the volume of content, whether the text is
   rendered server-side or only by JavaScript). Which of these features
   matter if the goal is to be read by a person? Which matter if the goal is
   to be ingested by a crawler, retrieved by an answer engine, or included
   in a training set?

3. What are some of the ways that these sites may be similar to authentic news
   sites? What are some of the ways that they may be different? Consider
   how an answer engine or RAG pipeline would experience the two: it does
   not see the janky design, it sees a chunk of text with a URL attached.
   From that vantage point, what distinguishes a fake story from a real one?
   Does anything, if the fake story is written in a plausible news register?

4. You might also consider exploring where and how these sites are hosted.
   With some technical know-how, you can use the `whois` command to find where
   a domain is registered. For example, `whois example.com` will tell you who
   registered the domain `example.com`. You can also use the `dig` command to
   find the IP address of a domain, as well as the authoritative name servers
   for the domain. While you are at it, fetch `/robots.txt` for a few of the
   sites and check whether they allow or block known AI crawlers (for
   example, `GPTBot`, `ClaudeBot`, `PerplexityBot`, `CCBot`). You can also
   look a domain up in the
   [Common Crawl index](https://index.commoncrawl.org/) to see whether and
   how often it has been archived. Are these sites trying to be crawled?

5. What other infrastructure features can you think of? Could you design a
   machine learning-based classifier to automatically detect these sites? Be
   careful to think about what might distinguish a fake news site not only
   from a legitimate news site but also a poorly-designed or implemented
   website. Now ask the same question from the other side: if you ran a
   crawler or a RAG pipeline, which of your features could you compute
   cheaply at ingestion time to decide whether to include a page? Which
   features would a site operator find easy to fake once they knew you were
   using them?

6. Many sites in the dataset are no longer online, and in some cases
   another party has taken over the domain. Does a site need to be online
   today to still shape what an AI system says? Consider what it means for a
   domain to have been crawled, archived, and folded into a training set
   years ago.

## Part 2: Discussion Questions

1. What could be the role of crowdsourcing in detecting disinformation? What
   are some of the challenges of crowdsourcing in this context? Crowdsourced
   signals (community notes, fact-checker ratings, "report" buttons) assume
   that people see the content and react to it. If a false claim is picked
   up by an answer engine before any person reads the originating page, what
   is left for the crowd to react to, and where in the pipeline could a
   crowdsourced signal still be inserted?

2. To what extent are users themselves responsible for identifying
   disinformation? Are users responsible for avoiding disinformation? How
   does the answer change when the "user" never visits the site and instead
   receives a synthesized answer, possibly with a citation, possibly not?
   Who is the responsible party then: the person asking the question, the
   company operating the answer engine, the site that was ingested, or the
   crawler that ingested it?

3. What are some of the ways that disinformation can be used to manipulate
   public debate and influence political decisions? Note that the
   traditional playbook (get a story in front of many people, get it shared)
   is not the only one. A network can publish millions of articles that
   almost no human reads, with the aim of becoming a large enough share of
   what crawlers see on a topic that AI systems repeat its framing. Which
   playbook is cheaper? Which is harder to detect? Which is harder to
   counter once it has worked?

4. **Seeding the machines.** The Russia-aligned "Pravda" network (also known
   as Portal Kombat) publishes millions of auto-translated, near-identical
   articles across more than a hundred domains with negligible human
   readership. Researchers have argued that its purpose is "LLM grooming":
   saturating the web with content so that it is retrieved and repeated by
   chatbots, and reproduced in training data. Is this disinformation in the
   sense defined at the top of this page? How would you measure whether it
   is working? If you were an AI company, what would you do about it, and
   what would be the cost of your defense to legitimate low-traffic sites?

    Read/see:

    - American Sunlight Project, ["A Pro-Russia Content Network Foreshadows
      the Automated Future of Info Ops"](https://www.americansunlight.org/s/PK-Report.pdf)
      (Feb 2025), the report that coined "LLM grooming"; the accompanying
      [domain database](https://www.americansunlight.org/portal-kombat-pravda-database).
    - NewsGuard, ["A Well-Funded Moscow-Based Global 'News' Network has
      Infected Western Artificial Intelligence Tools"](https://www.newsguardtech.com/special-reports/moscow-based-global-news-network-infected-western-artificial-intelligence-russian-propaganda/)
      (Mar 2025), an audit in which ten chatbots repeated the network's
      false claims about a third of the time; see also NewsGuard's
      quarterly [AI False Claim Monitor](https://www.newsguardtech.com/ai-monitor/may-2026/)
      and its [AI Tracking Center](https://www.newsguardtech.com/special-reports/ai-tracking-center/)
      count of AI content-farm "news" sites, now in the thousands.
    - DFRLab, ["Pravda in the pipeline"](https://dfrlab.org/2026/04/08/pravda-in-the-pipeline/)
      (Apr 2026), which looked for the network's content in Common Crawl and
      tested whether a base model would reproduce it. Note the detail that
      JavaScript-rendered pages were archived as empty shells, while plain
      HTML was captured in full.

5. **Poisoning the pipeline.** The web is now an input to two different
   kinds of systems: retrieval at query time (RAG, AI search) and training
   at build time (pretraining corpora). Security researchers have shown that
   a handful of planted documents can steer a RAG system's answer to a
   targeted question, and that a fixed, small number of documents can
   backdoor a model regardless of its size. How do these results change the
   economics of running a disinformation site? What is the analogue of the
   infrastructure features from Part 1 for defending a crawler or a
   retrieval index? And who should decide what gets ingested in the first
   place: the site operator (via `robots.txt` or paid access), the crawler
   operator, or someone else?

    Read/see:

    - Zou, Geng, Wang, and Jia, ["PoisonedRAG: Knowledge Corruption Attacks
      to Retrieval-Augmented Generation of Large Language Models"](https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag)
      (USENIX Security 2025).
    - Carlini et al., ["Poisoning Web-Scale Training Datasets is
      Practical"](https://arxiv.org/abs/2302.10149) (IEEE S&P 2024), on
      buying expired domains that appear in crawled datasets.
    - Anthropic, UK AI Security Institute, and the Alan Turing Institute,
      ["A small number of samples can poison LLMs of any
      size"](https://www.anthropic.com/research/small-samples-poison) (Oct 2025).
    - Cloudflare, ["Content Independence Day: no AI crawl without
      compensation"](https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/)
      (Jul 2025), on blocking AI crawlers by default and charging per crawl.
      Ask what this does to the mix of sites that remain crawlable.
    - For the dataset used in Part 1: Hounsel, Holland, Kaiser, Borgolte,
      Feamster, and Mayer, ["Identifying Disinformation Websites Using
      Infrastructure Features"](https://www.usenix.org/conference/foci20/presentation/hounsel)
      (FOCI 2020).
