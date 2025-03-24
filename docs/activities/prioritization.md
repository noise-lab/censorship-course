# Traffic Prioritization

## Learning Objective

Understand how traffic prioritization affects network performance by simulating competing web and video traffic, measuring the resulting performance impacts, and analyzing traffic patterns using Wireshark.

## Part 1: Experience with Traffic Prioritization

### Step 1: Run a Baseline Speed Test

- Use a tool like [fast.com](https://fast.com) or [speedtest.net](https://www.speedtest.net) to measure:
  - Download speed
  - Upload speed
  - Latency
- Record these values to establish your baseline network performance.

### Step 2: Simulate Competing Traffic

- Open multiple browser tabs and begin streaming videos (e.g., YouTube or Vimeo).
- In parallel, begin downloading a large file from a site like [testfile.org](https://testfile.org/) or a university open dataset archive.
- While both are running, try accessing lightweight websites such as [https://www.wikipedia.org](https://www.wikipedia.org) or [https://text.npr.org](https://text.npr.org).
- Observe and record any delays, buffering, or performance degradation.

### Step 3: Capture Network Traffic

- Open **Wireshark** and begin capturing packets on your primary network interface (Wi-Fi or Ethernet).
- Use your web browser and video stream as described above.
- Stop the capture after a few minutes of simultaneous activity.
- Filter traffic using:
  - `ip.dst` to examine destination IPs
  - `http`, `tls`, or `tcp.port == 443` for web traffic
- Look for signs of congestion, retransmissions, or prioritization effects.

### Step 4: (Optional) Explore Manual Prioritization

- If you have access to a Linux system or programmable router, use tools such as `tc` (traffic control) or QoS features in OpenWRT.
- Set rules to prioritize video traffic (e.g., port 1935 or streaming domains) over HTTP.
- Use `iperf` or download tests to compare prioritized vs. throttled traffic streams.

## Part 2: Discussion

Answer the following questions based on your experiment:

1. How did network performance change when multiple types of traffic competed for bandwidth?
2. Which applications appeared to suffer most during congestion? Which were less affected?
3. Did you observe any evidence of prioritization or throttling in your packet captures?
4. Should video traffic receive higher priority than other types of traffic? Why or why not?
5. How might these traffic management practices affect innovation or fair access to services online?
