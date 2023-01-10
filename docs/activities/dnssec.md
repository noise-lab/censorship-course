# Secure DNS (DNSSEC)

DNSSEC (Domain Name System Security Extensions) is a set of security
extensions to the Domain Name System (DNS) protocol that provide
authentication of DNS data. DNSSEC is designed to protect Internet
applications from certain attacks, such as DNS cache poisoning, by
authenticating DNS data received from remote DNS servers. DNSSEC uses digital
signatures and public-key cryptography to authenticate DNS data and prevent
attackers from spoofing or tampering with DNS data.

## Part 1: DNSSEC Basics

Some domains have deployed DNSSEC records to allow clients to validate the
records that it returns.

The `RRSIG` record includes a signature of the DNS record that is being
returned with the query.  The signature is signed by the DNSKEY of the
authoritative name server returning the record (or referral).

Explore some domains to see if DNSSEC records deployed. The following commands
may be useful:
- `dig any`
- `dig +dnssec`

## Part 2: Discussion

DNS can still be manipulated even if records are signed. Where is the root of
trust, and how might that be manipulated?
