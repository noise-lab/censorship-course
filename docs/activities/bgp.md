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
- [RouteViews BGP Data](https://www.routeviews.org/bgpdata/)
- [RouteViews BGP Data Analysis](https://www.routeviews.org/bgpdata/analysis.html)
- Login to the Routeviews servers via telnet.

In this brief hands on, you will log in to RouteViews and explore the routes
available from the RouteViews server to the University of Chicago.

1. Using a command like `dig`, find the IP address for the University of Chicago web server.
2. Log in to one of the [Routeviews
   servers](https://www.routeviews.org/routeviews/index.php/collectors/).
3. At the Routeviews collector prompt use the command `show ip bgp <IP
   address>` to list all of the routes to the University of Chicago.
   
The output includes a significant amount of information, including (among
other things) the list of autonomous systems corresponding to each advertised
route.  

**Going Further.** Those autonomous systems are listed as numbers, which you can look up
using `whois -h whois.cymru.com as<#>`.  Try to explore some of the available
advertised paths and routes.

## BGP Security: Route Hijacks

Note that the information above is not authenticated and could thus be easily
spoofed. 

How might a censor use route hijacks to disrupt Internet connectivity?
How might you go about detecting (or preventing) BGP route hijacks?
