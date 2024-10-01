## Background

DNS reflection and amplification attacks are a type of Distributed Denial of
Service (DDoS) attack that leverages the DNS protocol to overwhelm a victim's
network with a large volume of traffic. In this assignment, you will simulate
the behavior of a DNS reflection and amplification attack to understand how it
works and its impact on a network.

## Learning Outcomes

By completing this assignment, students will:

   - Understand how DNS reflection and amplification attacks work.
   - Gain hands-on experience with network simulation tools such as Mininet or VirtualBox.
   - Analyze the impact of DDoS attacks on network performance.
   - Explore techniques for mitigating DDoS attacks and securing DNS servers.
   - Reflect on ethical considerations when simulating cyberattacks in controlled environments.

## Setup Instructions (Mininet Option)

To complete this activity using Mininet, follow the steps below:

1. Download and install Mininet (if not pre-installed).
2. Set up a virtual network topology that includes:
   - A DNS server.
   - A victim's machine (client).
   - An attacker's machine.
3. Configure IP addresses and DNS server settings on the virtual
   machines (VMs) in the Mininet environment.

If you prefer to use a full VM environment:

1. Download and install VirtualBox on your computer.
2. Create VMs for the DNS server, victim machine, and attacker machine.
3. Configure the network settings to use the "Internal
   Network" option for the network adapter, ensuring the
   machines are on the same subnet.

## Assignment

### Part 1: Setting up the Network Environment

1. Using Mininet or a VM software, create a network environment with a DNS
   server, a victim machine, and an attacker machine.
2. Configure the network settings (e.g., IP addresses and DNS server
   settings) for each machine.
3. Test the network connectivity between the machines.

### Part 2: Simulating a DNS Reflection and Amplification Attack

1. Install Scapy or Hping3 on the attacker’s machine.
2. Use Scapy or Hping3 to generate DNS queries with a spoofed source IP
   address, targeting the DNS server.
3. Observe the DNS server’s response as it sends large DNS responses to the
   victim machine.
4. Measure the volume of traffic generated and the impact on the victim
   machine’s network performance.

### Part 3: Mitigating the Attack

1. Implement security best practices for DNS servers:
   - Use firewalls to block traffic from unknown sources.
   - Limit recursive queries.
   - Enable DNS response rate limiting.
2. Configure the firewall on the victim's machine to block traffic
   from the attacker’s IP address.
3. Re-run the attack and observe how the mitigation measures
   affect the impact.

## Reflection Questions

1. What is the impact of a DNS reflection and amplification attack on a
   victim's network? How does it affect network availability and service
   performance?
2. What best practices can be applied to secure DNS servers and prevent DNS
   reflection and amplification attacks?
3. What ethical considerations should be taken into account when
   simulating an attack in a controlled environment? How can this
   activity be conducted in a responsible and ethical manner?

