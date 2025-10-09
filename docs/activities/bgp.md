# Border Gateway Protocol

Border Gateway Protocol (BGP) is a standardized exterior gateway protocol
designed to exchange routing and reachability information among autonomous
systems (AS) on the Internet. BGP is the protocol used to exchange routing
information for the Internet and is the protocol used between Internet service
providers (ISPs) to establish routing between one another. BGP is the protocol
used to route traffic across the Internet.

## BGP Basics: RouteViews

One good way to learn about the information that the Border Gateway Protocol
is from the [RouteViews](https://routeviews.org/) project, which maintains
various ways to explore Internet routing data.

You can explore the data in a variety of ways, including:
- Login to the Routeviews servers via telnet.

In this brief hands on, you will log in to RouteViews and explore the routes
available from the RouteViews server to the University of Chicago.

1. Using a command like `dig`, find the IP address for the University of Chicago web server and for YouTube (e.g., `youtube.com`).
2. Log in to one of the [Routeviews
   collectors](https://www.routeviews.org/routeviews/index.php/collectors/) using telnet. For example:
   ```bash
   telnet route-views.chicago.routeviews.org
   ```
   (You can choose any collector from the [full list](https://www.routeviews.org/routeviews/index.php/collectors/).)

   **Working with a partner?** Try using two different RouteViews collectors to compare the routing information from different vantage points on the Internet.
3. At the Routeviews collector prompt use the command `show ip bgp <IP
   address>` to list all of the routes to the University of Chicago and to YouTube.
   
The output includes a significant amount of information, including (among
other things) the list of autonomous systems corresponding to each advertised
route.  

**Going Further.** Those autonomous systems are listed as numbers, which you can look up
using the [HackerTarget AS IP Lookup](https://hackertarget.com/as-ip-lookup/) tool.
Try to explore some of the available advertised paths and routes.

## BGP Security: Route Hijacks

Note that the information above is not authenticated and could thus be easily
spoofed.

**Discussion Questions:**

1. Review the [Pakistan Telecom YouTube hijack case from February 2008](https://www.ripe.net/publications/news/industry-developments/youtube-hijacking-a-ripe-ncc-ris-case-study). In this incident, Pakistan Telecom attempted to censor YouTube within Pakistan by advertising a more specific prefix (208.65.153.0/24) than YouTube's legitimate prefix (208.65.153.0/22), but the route announcement leaked globally.

   Think about the routing data you just examined for the University of Chicago:
   - What would the BGP routing table data have looked like during the Pakistan Telecom hijack for someone querying YouTube's IP addresses?
   - How would the AS path information differ from normal operation?
   - Why was the more specific /24 prefix preferred over YouTube's legitimate /22 prefix?

2. How might a censor use route hijacks to disrupt Internet connectivity?

3. How might you go about detecting (or preventing) BGP route hijacks?

---

## Automation Tool

For those interested in automating this analysis, we've provided a Python script that performs all the steps above: connecting to RouteViews, extracting AS paths, looking up ASN information, and generating markdown tables.

See [`src/bgp.py`](src/bgp.py) for a tool that automates this entire process. Run `python3 src/bgp.py --help` for usage information.
