"""
Ultra Privacy Scan

A privacy-focused tool for detecting third-party trackers in apps and websites.
Generates a JSON report detailing trackers found, their type, and permissions requested.

Usage:
    python scan.py --target <app_or_website> [--mode normal|ultra|pro] [--report output.json]

License:
    MIT License (core open source)
"""

import argparse
import json
import requests
from bs4 import BeautifulSoup
import tldextract

# Base tracker lists
BASE_TRACKERS = [
    "google-analytics.com",
    "facebook.com",
    "doubleclick.net",
    "ads.yahoo.com"
]

ULTRA_TRACKERS = [
    "linkedin.com",
    "twitter.com",
    "bing.com",
    "quantserve.com",
    "matomo.org"
]

PRO_TRACKERS = [
    # Reserved for future expansion
]

def load_trackers(mode="normal"):
    trackers = BASE_TRACKERS.copy()
    if mode == "ultra":
        trackers.extend(ULTRA_TRACKERS)
    elif mode == "pro":
        trackers.extend(ULTRA_TRACKERS)
        trackers.extend(PRO_TRACKERS)
    return trackers

def extract_domain(url):
    """Extract main domain for reporting"""
    ext = tldextract.extract(url)
    domain = f"{ext.domain}.{ext.suffix}" if ext.suffix else ext.domain
    return domain

def scan_url(url, trackers):
    """Scan a URL for known trackers"""
    report = []
    try:
        resp = requests.get(url, timeout=10)
        soup = BeautifulSoup(resp.text, "lxml")
        tags = soup.find_all(["script", "img", "iframe", "link", "embed", "object"])
        for tag in tags:
            src = tag.get("src") or tag.get("href") or ""
            for tracker in trackers:
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
    parser.add_argument("--mode", choices=["normal", "ultra", "pro"], default="normal", help="Scan mode")
    args = parser.parse_args()

    trackers = load_trackers(args.mode)
    domain = extract_domain(args.target)
    print(f"Scanning {domain} in {args.mode.upper()} mode...")

    results = scan_url(args.target, trackers)

    output = {
        "target": args.target,
        "domain": domain,
        "scan_mode": args.mode,
        "trackers_found": results,
        "total": len(results)
    }

    with open(args.report, "w") as f:
        json.dump(output, f, indent=4)

    print(f"Scan complete. {len(results)} trackers found. Report saved to {args.report}")

if __name__ == "__main__":
    main()
"""
Ultra Privacy Scan

A privacy-focused tool for detecting third-party trackers in apps and websites.
Generates a JSON report detailing trackers found, their type, and permissions requested.

Usage:
    python scan.py --target <app_or_website> [--mode normal|ultra|pro] [--report output.json]

License:
    MIT License (core open source)
"""

import argparse
import json
import requests
from bs4 import BeautifulSoup
import tldextract

# Base tracker lists
BASE_TRACKERS = [
    "google-analytics.com",
    "facebook.com",
    "doubleclick.net",
    "ads.yahoo.com"
]

ULTRA_TRACKERS = [
    "linkedin.com",
    "twitter.com",
    "bing.com",
    "quantserve.com",
    "matomo.org"
]

PRO_TRACKERS = [
    # Reserved for future expansion
]

def load_trackers(mode="normal"):
    trackers = BASE_TRACKERS.copy()
    if mode == "ultra":
        trackers.extend(ULTRA_TRACKERS)
    elif mode == "pro":
        trackers.extend(ULTRA_TRACKERS)
        trackers.extend(PRO_TRACKERS)
    return trackers

def extract_domain(url):
    """Extract main domain for reporting"""
    ext = tldextract.extract(url)
    domain = f"{ext.domain}.{ext.suffix}" if ext.suffix else ext.domain
    return domain

def scan_url(url, trackers):
    """Scan a URL for known trackers"""
    report = []
    try:
        resp = requests.get(url, timeout=10)
        soup = BeautifulSoup(resp.text, "lxml")
        tags = soup.find_all(["script", "img", "iframe", "link", "embed", "object"])
        for tag in tags:
            src = tag.get("src") or tag.get("href") or ""
            for tracker in trackers:
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
    parser.add_argument("--mode", choices=["normal", "ultra", "pro"], default="normal", help="Scan mode")
    args = parser.parse_args()

    trackers = load_trackers(args.mode)
    domain = extract_domain(args.target)
    print(f"Scanning {domain} in {args.mode.upper()} mode...")

    results = scan_url(args.target, trackers)

    output = {
        "target": args.target,
        "domain": domain,
        "scan_mode": args.mode,
        "trackers_found": results,
        "total": len(results)
    }

    with open(args.report, "w") as f:
        json.dump(output, f, indent=4)

    print(f"Scan complete. {len(results)} trackers found. Report saved to {args.report}")

if __name__ == "__main__":
    main()
