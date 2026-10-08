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
2. Log in to one of the RouteViews collectors using telnet. For example:
   ```bash
   telnet route-views.chicago.routeviews.org
   ```
   Every collector accepts the same telnet login and the same `show ip bgp` commands. Pick one near a place you are curious about (the `route-viewsN` ones peer with networks all over the world and sit in Oregon):

   | Collector | Location |
   |---|---|
   | `route-views.chicago.routeviews.org` | Chicago (Equinix CH1) |
   | `route-views.ny.routeviews.org` | New York (DE-CIX New York) |
   | `route-views.eqix.routeviews.org` | Ashburn, Virginia (Equinix) |
   | `cix.atl.routeviews.org` | Atlanta (CIX-ATL) |
   | `route-views.telxatl.routeviews.org` | Atlanta (Digital Realty) |
   | `route-views.mwix.routeviews.org` | Indianapolis (FD-IX) |
   | `route-views.flix.routeviews.org` | Miami (FL-IX) |
   | `route-views.isc.routeviews.org` | Palo Alto (PAIX) |
   | `route-views.sfmix.routeviews.org` | San Francisco (SFMIX) |
   | `pacwave.lax.routeviews.org` | Los Angeles (Pacific Wave) |
   | `route-views.nwax.routeviews.org` | Portland (NWAX) |
   | `route-views2.routeviews.org` … `route-views8.routeviews.org` | Multi-hop collectors, University of Oregon |
   | `route-views.gorex.routeviews.org` | Guam (GOREX) |
   | `pitmx.qro.routeviews.org` | Querétaro, Mexico (PIT Chile MX) |
   | `crix.sjo.routeviews.org` | San José, Costa Rica (CRIX) |
   | `route-views.peru.routeviews.org` | Lima (Peru IX) |
   | `route-views.chile.routeviews.org` | Santiago (NIC.cl) |
   | `pit.scl.routeviews.org` | Santiago (PIT Chile) |
   | `ix-br2.gru.routeviews.org` | São Paulo (IX.br) |
   | `route-views.rio.routeviews.org` | Rio de Janeiro (IX.br) |
   | `route-views.fortaleza.routeviews.org` | Fortaleza, Brazil (IX.br) |
   | `route-views.linx.routeviews.org` | London (LINX) |
   | `amsix.ams.routeviews.org` | Amsterdam (AMS-IX) |
   | `decix.fra.routeviews.org` | Frankfurt (DE-CIX) |
   | `locix.fra.routeviews.org` | Frankfurt (LOCIX) |
   | `netnod.mmx.routeviews.org` | Malmö, Sweden (Netnod) |
   | `namex.fco.routeviews.org` | Rome (NAMEX) |
   | `interlan.otp.routeviews.org` | Bucharest (InterLAN-IX) |
   | `route-views.soxrs.routeviews.org` | Belgrade (SOX Serbia) |
   | `route-views.uaeix.routeviews.org` | Dubai (UAE-IX) |
   | `iraq-ixp.bgw.routeviews.org` | Baghdad (IRAQ-IXP) |
   | `route-views.gixa.routeviews.org` | Accra (GIXA) |
   | `ixpn.los.routeviews.org` | Lagos (IXPN) |
   | `route-views.kixp.routeviews.org` | Nairobi (KIXP) |
   | `route-views.napafrica.routeviews.org` | Johannesburg (NAPAfrica) |
   | `route-views.bdix.routeviews.org` | Dhaka (BDIX) |
   | `route-views.bknix.routeviews.org` | Bangkok (BKNIX) |
   | `decix.jhb.routeviews.org` | Johor Bahru, Malaysia (DE-CIX) |
   | `route-views.sg.routeviews.org` | Singapore (Equinix) |
   | `iix.cgk.routeviews.org` | Jakarta (IIX) |
   | `getafix.mnl.routeviews.org` | Manila (GetaFIX) |
   | `route-views.phoix.routeviews.org` | Quezon City, Philippines (PhOpenIX) |
   | `hkix.hkg.routeviews.org` | Hong Kong (HKIX) |
   | `kinx.icn.routeviews.org` | Seoul (KINX) |
   | `route-views.wide.routeviews.org` | Tokyo (DIX-IE) |
   | `route-views.perth.routeviews.org` | Perth (WA-IX) |
   | `route-views.sydney.routeviews.org` | Sydney (Equinix SYD1) |

   This list is taken from the collector menu of the [RouteViews Looking Glass](https://lg.routeviews.org/), which is the current authoritative list (the old collectors page on routeviews.org is gone). If you do not have `telnet` (recent macOS: `brew install telnet`, or use `nc <collector> 23`), the Looking Glass runs the same `show ip bgp` command from your browser.

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
