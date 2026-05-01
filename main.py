import argparse
from scanner.engine import ScannerEngine
from scanner.sqli import SQLiScanner
from scanner.xss import XSSScanner
from scanner.headers import HeaderScanner
from scanner.subdomain import SubdomainScanner
from scanner.report import generate_report


def main():
    parser = argparse.ArgumentParser(description="Web Vulnerability Scanner")
    parser.add_argument("url", help="Target URL to scan")
    parser.add_argument("--output", choices=["console", "json"], default="console")
    parser.add_argument("--subdomains", action="store_true", help="Enable subdomain enumeration")
    args = parser.parse_args()

    print(f"[*] Starting scan on: {args.url}")
    engine = ScannerEngine(args.url)
    findings = []
    discovered_subdomains = []

    if args.subdomains:
        print("[*] Enumerating subdomains...")
        sub_findings, discovered_subdomains = SubdomainScanner(engine).scan(args.url)
        # Don't add INFO findings to main vuln list

    print("[*] Checking security headers...")
    findings += HeaderScanner(engine).scan(args.url)

    print("[*] Testing for SQL injection...")
    findings += SQLiScanner(engine).scan(args.url)

    print("[*] Testing for XSS...")
    findings += XSSScanner(engine).scan(args.url)

    generate_report(args.url, findings, args.output, subdomains=discovered_subdomains)


if __name__ == "__main__":
    main()
