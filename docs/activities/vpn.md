# Virtual Private Networks

## Learning Objective

You will understand how Virtual Private Networks (VPNs) function as a
circumvention tool for censorship by gaining firsthand experience using a VPN.
Through empirical measurements and traffic inspection, you will explore
how VPNs affect network paths, performance (e.g., ping and page load time),
and traffic visibility.

## Part 1: Experience with Virtual Private Networks

### Step 1: Install a Free VPN

- Choose and install a free VPN such as [ProtonVPN](https://protonvpn.com),
  [Windscribe](https://windscribe.com), or [TunnelBear](https://www.tunnelbear.com).
  - Register for a free account and install the VPN on your laptop (desktop
    preferred for the next steps).  **Note**: Free versions may limit server
    selection, but that’s fine for this assignment.

### Step 2: Select a Server and Connect

- Connect to a VPN server in another country (e.g., Netherlands or Japan).
  Take note of which server location you choose.

### Step 3: Measure Latency and Load Time

For each of the tests below, perform them once **with the VPN disabled** and
once **with the VPN enabled**.

#### Ping Test

- Open a terminal and run:

  ```bash
    ping -c 5 www.google.com
    ping -c 5 www.bbc.com
  ```

- Record the average round-trip time (RTT).

#### Page Load Time

- Open a browser and load a news website (e.g.,
  [https://www.bbc.com](https://www.bbc.com) or [https://www.nytimes.com](https://www.nytimes.com)).
  - Use the browser's Developer Tools (usually under “Network”) to measure how
    long the page takes to fully load.
    - Record the total load time.

#### Traceroute

- Run a traceroute to a site like `www.wikipedia.org`:

  - On Mac/Linux:
      ```bash traceroute www.wikipedia.org ```

  - On Windows:
   ```cmd tracert www.wikipedia.org ```

- Compare the number of hops and the intermediate
      IPs between VPN and non-VPN connections.

### Step 4: Capture and Inspect Network Traffic

- Open **Wireshark** (install it if you haven’t already).
- Start a capture on your primary network interface (typically Wi-Fi or
  Ethernet).
- Browse to a site like `www.bbc.com` with and without the VPN.
- Stop the capture after each session and examine:

- Destination IP addresses (filter using `ip.dst`)
- Whether DNS queries or HTTP/HTTPS traffic are visible
- Whether the destination IPs differ with the VPN on vs. off

 **Optional Bonus**: Try accessing a site that is known to be blocked
 in some countries (e.g., [Deutsche Welle](https://www.dw.com) or
 [Radio Free Asia](https://www.rfa.org)) and note whether access
 changes when connected to different VPN locations.

## Part 2: Discussion

Answer the following questions based on your experiment:

1. **Performance**: How did latency and page load times change when the VPN
   was enabled? Were they consistent across multiple trials?
2. **Routing**: How did the network path (number of hops and route) change
   when using the VPN? Why do you think that is?
3. **Visibility**: What differences did you observe in the Wireshark
   capture with and without the VPN?
4. **IP Addressing**: How did the destination IPs or domains differ
   between the two cases? Were you able to identify the VPN endpoint?
5. **Security and Privacy**: Based on your traffic inspection,
   what does the VPN appear to encrypt or obscure? What remains
   visible?
6. **Censorship Circumvention**: Reflecting on this experience,
   how might a VPN help users bypass censorship in a
   restrictive regime? What limitations or risks might still
   remain?

