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

1. Explore a handful of fake news sites. One possible source is from a paper
   that attempted to automatically characterize these sites according to
   infrastructure features. The dataset is
   [here](https://github.com/ahounsel/disinfo-infra-public/blob/master/src/system/data/training/disinformation_domains.csv).

2. What are some of the common features of these sites? What are some of the
   differences?
   
3. What are some of the ways that these sites may be similar to authentic news
   sites? What are some of the ways that they may be different?
   
4. You might also consider exploring where and how these sites are hosted.
   With some technical know-how, you can use the `whois` command to findwhere
   a domain is registered. For example, `whois example.com` will tell you who
   registered the domain `example.com`. You can also use the `dig` command to
   find the IP address of a domain, as well as the authoritative name servers
   for the domain. 

5. What other infrastructure features can you think of? Could you design a
   machine learning-based classifer to automatically detect these sites? Be
   careful to think about what might distinguish a fake news site not only
   from a legitimate news site but also a poorly-designed or implemented
   website.   
   
## Part 2: Discussion Questions

1. What could be the role of crowdsourcing in detecting disinformation? What
   are some of the challenges of crowdsourcing in this context?

2. To what extent are users themselves responsible for identifying
   disinformation? Are users responsible for avoiding disinformation?

3. What are some of the ways that disinformation can be used to manipulate
   public debate and influence political decisions?
