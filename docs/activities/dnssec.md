# Exploring DNS: Security and Privacy Enhancements

The Domain Name System (DNS) is a hierarchical, decentralized naming system
for computers, services, or other resources connected to the Internet or a
private network. It associates various information with domain names
assigned to each of the participating entities. Most prominently, it
translates domain names into the numerical IP addresses needed for locating
and identifying computer services and devices. DNS is a critical part of
the Internet's functionality, but its default operation is vulnerable to
manipulation and privacy breaches.

In this exercise, you will explore two security enhancements for DNS: 
   1. DNS over HTTPS (DoH) – aimed at improving privacy by encrypting DNS traffic. 
   2. DNSSEC – aimed at improving security by authenticating DNS data.

## Part 1: DNS over HTTPS (DoH) and DNS Traffic Analysis

In this section, you'll explore how DNS traffic can be encrypted using DNS
over HTTPS (DoH) and compare it with standard DNS traffic that is not
encrypted.

1. **Capture DNS Traffic without Encryption**  
a. Open your web browser and disable any encrypted DNS settings. For
example, in Firefox, navigate to **Settings > General > Network Settings**
and uncheck **Enable DNS over HTTPS**.  
b. Open Wireshark and capture traffic on your active network interface.  
c. Filter for DNS traffic by using the following display filter: dns 
d. Visit a few websites in your browser and observe the DNS queries and
responses in the Wireshark capture.  

*What do you notice about the information in these DNS packets? Is it
readable? What domains can you see in the clear?*

2. **Enable Encrypted DNS (DNS-over-HTTPS)**  
a. Go back to your web browser and enable DNS over HTTPS (DoH). In Firefox,
navigate to **Settings > General > Network Settings** and check **Enable DNS
over HTTPS**.  
b. Start a new Wireshark capture.  
c. Use the same display filter as before:  dns
d. Visit the same websites as in step 1 and observe the DNS traffic.
3. **Compare the Results**  
Compare the Wireshark captures from steps 1 and 2.  

*What differences do you observe between the unencrypted DNS traffic and the
DNS-over-HTTPS traffic? Can you still see the domain names or query details in
the clear? How does encryption affect the visibility of DNS information?*

## Part 2: DNSSEC (Domain Name System Security Extensions)

DNSSEC (Domain Name System Security Extensions) is a set of security
extensions to the DNS protocol that provides authentication of DNS data.
DNSSEC is designed to protect Internet applications from certain attacks, such
as DNS cache poisoning, by authenticating DNS data received from remote DNS
servers. DNSSEC uses digital signatures and public-key cryptography to
authenticate DNS data and prevent attackers from spoofing or tampering with
DNS data.

**Explore DNSSEC-enabled Domains**  
Some domains have deployed DNSSEC records to allow clients to validate the
records that are returned.  

The `RRSIG` record includes a signature of the DNS record that is being
returned with the query. The signature is signed by the DNSKEY of the
authoritative name server returning the record (or referral).

Explore some domains to see if DNSSEC records are deployed. The following
commands may be useful:
- `dig any`
- `dig +dnssec rrsig`

**Discussion**  
DNS can still be manipulated even if records are signed. Where is the root of
trust, and how might that be manipulated?
