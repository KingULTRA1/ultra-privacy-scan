"""
Ultra Privacy Scan

A privacy-focused tool for detecting third-party trackers in apps and websites.
Generates a JSON report detailing trackers found, their type, and permissions requested.

Usage:
    python scan.py --target <app_or_website> [--report output.json]

License:
    MIT License (core open source)
"""

import argparse
import json
import requests
from bs4 import BeautifulSoup
import tldextract

# Minimal list of known trackers for demonstration
KNOWN_TRACKERS = [
    "google-analytics.com",
    "facebook.com",
    "doubleclick.net",
    "ads.yahoo.com"
]

def extract_domains(url):
    """Extract domain and subdomain for analysis"""
    ext = tldextract.extract(url)
    domain = f"{ext.domain}.{ext.suffix}" if ext.suffix else ext.domain
    return domain

def scan_url(url):
    """Scan a URL for known trackers"""
    report = []
    try:
        resp = requests.get(url, timeout=10)
        html_content = resp.text
        soup = BeautifulSoup(html_content, "lxml")
        
        # Simple tracker detection from <script> and <img> tags
        tags = soup.find_all(["script", "img", "iframe"])
        for tag in tags:
            src = tag.get("src") or ""
            for tracker in KNOWN_TRACKERS:
                if tracker in src:
                    report.append({
                        "tracker": tracker,
                        "tag": tag.name,
                        "source": src
                    })
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")

    return report

def main():
    parser = argparse.ArgumentParser(description="Ultra Privacy Scan")
    parser.add_argument("--target", required=True, help="App or website URL to scan")
    parser.add_argument("--report", default="report.json", help="Output JSON report filename")
    args = parser.parse_args()

    domain = extract_domains(args.target)
    print(f"Scanning {domain}...")

    results = scan_url(args.target)

    output = {
        "target": args.target,
        "domain": domain,
        "trackers_found": results,
        "total": len(results)
    }

    with open(args.report, "w") as f:
        json.dump(output, f, indent=4)

    print(f"Scan complete. Report saved to {args.report}")

if __name__ == "__main__":
    main()
