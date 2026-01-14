#!/usr/bin/env python3
import subprocess
import argparse
import os
import sys

class Color:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

def banner():
    print(f"""{Color.CYAN}
==================================================
 DNS ZONE TRANSFER MISCONFIGURATION SCANNER
=================================================={Color.RESET}
""")

def run_cmd(cmd):
    try:
        return subprocess.check_output(
            cmd,
            shell=True,
            stderr=subprocess.STDOUT,
            timeout=15
        ).decode()
    except subprocess.CalledProcessError as e:
        return e.output.decode()
    except subprocess.TimeoutExpired:
        return ""

def get_nameservers(domain):
    output = run_cmd(f"dig {domain} NS +short")
    return [ns.strip('.') for ns in output.splitlines() if ns]

def is_zone_transfer_misconfigured(output):
    error_indicators = [
        "Transfer failed",
        "no servers could be reached",
        "communications error",
        "connection timed out",
        "REFUSED",
        "NOTAUTH",
        "SERVFAIL",
        "NXDOMAIN"
    ]

    for err in error_indicators:
        if err.lower() in output.lower():
            return False

    record_indicators = [
        " IN SOA ",
        " IN NS ",
        " IN A ",
        " IN MX ",
        " IN TXT ",
        " IN CNAME "
    ]

    record_count = sum(1 for r in record_indicators if r in output)
    return record_count >= 2

def check_domain(domain):
    print(f"\n{Color.CYAN}[+] Target Domain: {domain}{Color.RESET}")

    nameservers = get_nameservers(domain)

    if not nameservers:
        print(f"{Color.YELLOW}[-] No NS records found{Color.RESET}")
        return

    vulnerable = False

    for ns in nameservers:
        print(f"{Color.YELLOW}[+] Testing AXFR @ {ns}{Color.RESET}")
        output = run_cmd(f"dig axfr @{ns} {domain}")

        if is_zone_transfer_misconfigured(output):
            print(
                f"{Color.RED}[VULNERABLE] DNS Zone Transfer Misconfiguration "
                f"confirmed on {ns}{Color.RESET}"
            )
            print(output)
            vulnerable = True
        else:
            print(
                f"{Color.GREEN}[SECURE] DNS Zone Transfer properly restricted "
                f"on {ns}{Color.RESET}"
            )

    if vulnerable:
        print(
            f"\n{Color.RED}[RESULT] ❌ DNS Zone Transfer Misconfiguration FOUND{Color.RESET}"
        )
    else:
        print(
            f"\n{Color.GREEN}[RESULT] ✅ DNS Zone Transfer is Properly Restricted{Color.RESET}"
        )

def main():
    banner()

    parser = argparse.ArgumentParser(
        description="DNS Zone Transfer Misconfiguration Scanner"
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-d", "--domain", help="Single domain (example.com)")
    group.add_argument("-t", "--txt", help="Text file with multiple domains")

    args = parser.parse_args()

    if args.domain:
        check_domain(args.domain)

    elif args.txt:
        if not os.path.exists(args.txt):
            print(f"{Color.RED}[-] Domain file not found{Color.RESET}")
            sys.exit(1)

        with open(args.txt, "r") as f:
            domains = [d.strip() for d in f if d.strip()]

        for domain in domains:
            check_domain(domain)

if __name__ == "__main__":
    main()
