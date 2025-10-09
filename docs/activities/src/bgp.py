#!/usr/bin/env python3
"""
BGP RouteViews Analysis Tool

This script connects to a RouteViews collector, retrieves BGP routing information
for a specified IP address, and generates markdown tables showing:
1. ASN to Organization mapping
2. Complete AS paths with hop-by-hop details
"""

import subprocess
import sys
import re
import argparse
from typing import List, Dict, Set, Tuple


def query_routeviews(collector: str, ip_address: str) -> str:
    """
    Query a RouteViews collector for BGP information about an IP address.

    Args:
        collector: RouteViews collector hostname
        ip_address: IP address to query

    Returns:
        Raw output from the RouteViews session
    """
    # Prepare commands to send to telnet
    commands = f"show ip bgp {ip_address}\nexit\n"

    # Use subprocess to pipe commands to telnet
    try:
        process = subprocess.Popen(
            ['bash', '-c', f'(sleep 2; echo "show ip bgp {ip_address}"; sleep 3; echo "exit") | telnet {collector}'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        output, _ = process.communicate(timeout=30)
        return output
    except subprocess.TimeoutExpired:
        process.kill()
        print("Error: Telnet session timed out", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error connecting to RouteViews: {e}", file=sys.stderr)
        sys.exit(1)


def extract_as_paths(routeviews_output: str) -> List[Tuple[str, List[int]]]:
    """
    Extract AS paths from RouteViews output.

    Args:
        routeviews_output: Raw output from RouteViews

    Returns:
        List of tuples containing (prefix, as_path_list)
    """
    lines = routeviews_output.split('\n')
    as_paths = []
    current_prefix = None

    for line in lines:
        # Look for prefix line
        prefix_match = re.search(r'BGP routing table entry for ([\d.]+/\d+)', line)
        if prefix_match:
            current_prefix = prefix_match.group(1)
            continue

        # Look for AS path lines (they start with spaces and contain only numbers)
        # Format: "  199524 15169" or "  32709 14016 15169"
        as_path_match = re.match(r'^\s+(\d+(?:\s+\d+)*)\s*$', line)
        if as_path_match and current_prefix:
            as_numbers = [int(asn) for asn in as_path_match.group(1).split()]
            as_paths.append((current_prefix, as_numbers))

    return as_paths


def get_unique_asns(as_paths: List[Tuple[str, List[int]]]) -> Set[int]:
    """
    Extract unique ASNs from AS paths.

    Args:
        as_paths: List of (prefix, as_path) tuples

    Returns:
        Set of unique ASNs
    """
    asns = set()
    for _, path in as_paths:
        asns.update(path)
    return asns


def lookup_asn(asn: int) -> Tuple[str, str]:
    """
    Look up ASN information using whois.cymru.com.

    Args:
        asn: Autonomous System Number

    Returns:
        Tuple of (organization_name, country_code)
    """
    try:
        result = subprocess.run(
            ['whois', '-h', 'whois.cymru.com', f'AS{asn}'],
            capture_output=True,
            text=True,
            timeout=10
        )

        # Parse output - format is "AS Name\nORG_NAME, CC"
        lines = [line.strip() for line in result.stdout.strip().split('\n') if line.strip() and not line.startswith('#')]

        if len(lines) >= 2:
            # Second line contains "ORG_NAME, CC"
            org_line = lines[1]
            if ', ' in org_line:
                parts = org_line.rsplit(', ', 1)
                return parts[0].strip(), parts[1].strip()
            return org_line, "??"

        return "Unknown", "??"
    except Exception as e:
        print(f"Warning: Could not lookup AS{asn}: {e}", file=sys.stderr)
        return "Unknown", "??"


def generate_asn_table(asn_info: Dict[int, Tuple[str, str]]) -> str:
    """
    Generate markdown table of ASN to Organization mapping.

    Args:
        asn_info: Dictionary mapping ASN to (organization, country) tuples

    Returns:
        Markdown formatted table
    """
    table = "## ASN to Organization Mapping\n\n"
    table += "| ASN | Organization | Country |\n"
    table += "|-----|--------------|----------|\n"

    for asn in sorted(asn_info.keys()):
        org, country = asn_info[asn]
        table += f"| {asn} | {org} | {country} |\n"

    return table


def generate_path_table(as_paths: List[Tuple[str, List[int]]], asn_info: Dict[int, Tuple[str, str]]) -> str:
    """
    Generate markdown table showing AS paths with hop-by-hop details.

    Args:
        as_paths: List of (prefix, as_path) tuples
        asn_info: Dictionary mapping ASN to (organization, country) tuples

    Returns:
        Markdown formatted table
    """
    if not as_paths:
        return "No AS paths found.\n"

    # Find the maximum path length to determine number of columns
    max_hops = max(len(path) for _, path in as_paths)

    table = "## AS Path Details\n\n"

    # Build header
    table += "| Prefix |"
    for i in range(max_hops):
        table += f" Hop {i+1} |"
    table += "\n"

    # Build separator
    table += "|--------|"
    for i in range(max_hops):
        table += "---------|"
    table += "\n"

    # Build rows
    for prefix, path in as_paths:
        table += f"| {prefix} |"
        for asn in path:
            org, _ = asn_info.get(asn, ("Unknown", "??"))
            table += f" AS{asn} ({org}) |"
        # Fill empty columns if this path is shorter than max
        for _ in range(max_hops - len(path)):
            table += " |"
        table += "\n"

    return table


def main():
    parser = argparse.ArgumentParser(
        description='Query RouteViews BGP data and generate analysis tables',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                                    # Query YouTube IP from Chicago collector
  %(prog)s 1.1.1.1                           # Query specific IP
  %(prog)s --collector route-views.oregon.routeviews.org 8.8.8.8
        """
    )
    parser.add_argument(
        'ip_address',
        nargs='?',
        default='142.251.32.14',
        help='IP address to query (default: 142.251.32.14 - YouTube)'
    )
    parser.add_argument(
        '--collector',
        default='route-views.chicago.routeviews.org',
        help='RouteViews collector to use (default: route-views.chicago.routeviews.org)'
    )

    args = parser.parse_args()

    print(f"# BGP Analysis for {args.ip_address}\n", file=sys.stderr)
    print(f"Querying {args.collector}...\n", file=sys.stderr)

    # Query RouteViews
    output = query_routeviews(args.collector, args.ip_address)

    # Extract AS paths
    as_paths = extract_as_paths(output)

    if not as_paths:
        print("Error: No BGP paths found for this IP address", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(as_paths)} AS paths\n", file=sys.stderr)

    # Get unique ASNs
    unique_asns = get_unique_asns(as_paths)
    print(f"Looking up {len(unique_asns)} unique ASNs...\n", file=sys.stderr)

    # Look up all ASNs
    asn_info = {}
    for asn in unique_asns:
        asn_info[asn] = lookup_asn(asn)

    # Generate output
    print(f"# BGP Analysis for {args.ip_address}\n")
    print(f"**Collector:** {args.collector}\n")
    print(f"**Paths Found:** {len(as_paths)}\n")
    print()

    # Print ASN table
    print(generate_asn_table(asn_info))
    print()

    # Print path table
    print(generate_path_table(as_paths, asn_info))


if __name__ == '__main__':
    main()
