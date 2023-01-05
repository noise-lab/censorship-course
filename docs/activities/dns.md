# Domain Name System

The Domain Name System (DNS) is a hierarchical, decentralized naming system
for computers, services, or other resources connected to the Internet or a
private network. It associates various information with domain names assigned
to each of the participating entities. Most prominently, it translates more
domain names to the numerical IP addresses needed for locating and identifying
computer services and devices with the underlying network protocols. By
providing a worldwide, distributed directory service, the Domain Name System
is an essential component of the functionality of the Internet. It is safe to
say that just about all Internet communication between endpoints relies on the
DNS in some fashion.

## Part 1: DNS Basics

1. Find (or install) the software tool `dig` on your machine.
2. Use `dig` to look up the IP address of:

   - google.com
   - www.cs.uchicago.edu
   
   What do you notice about the differences in these responses.

3. If you have a Virtual Private Network (VPN) installed, enable it to change
   your endpoint to a different location, and repeat step 2 (work with a
   partner or neighbor if you need to).
  
   What do you notice about the similarities and differences between the data
   you see between the two domains, and how that information changes as you
   change locations?
   
## Part 2: Manipulation   

4. The Domain Name System (DNS) is, by default, neither encrypted nor signed
   (i.e., the validity of the responses is not guaranteed). This subjects the
   protocol to manipulation, which you can read more about
   [here](https://www.usenix.org/system/files/conference/usenixsecurity17/sec17-pearce.pdf).
   
   - Suppose a censoring adversary wanted to manipulate DNS responses. How or
     where could such manipulation occur?
   - In light of what you observed in Step 3, what are some of the challenges
     with *detecting* manipulation.
   
