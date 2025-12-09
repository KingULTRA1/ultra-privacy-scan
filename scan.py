"""
Ultra Privacy Scan - Updated

A privacy‑focused tool for detecting third‑party trackers in apps and websites.
Supports dynamic tracker lists, multi‑URL scanning, inline script detection, and concurrency.
Generates a JSON report detailing trackers found, their type, and source.

Usage:
    python scan.py --target <url1> [url2 ...] [--mode normal|ultra|pro]
                   [--tracker-file trackers.json] [--report output.json] [--concurrent]

License:
    MIT License (core open source)
"""

import argparse
import json
import requests
from bs4 import BeautifulSoup
import tldextract
from concurrent.futures import ThreadPoolExecutor, as_completed

# Base tracker lists (fallback)
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
    # reserved for dynamic fetching or future expansion
]

def load_trackers(mode="normal", tracker_file=None):
    """
    Load trackers from external JSON file or fallback to built‑in lists.
    Expected JSON format (example):
    {
        "normal": ["google-analytics.com", ...],
        "ultra": [...],
        "pro": [...]
    }
    """
    if tracker_file:
        try:
            with open(tracker_file, "r") as f:
                data = json.load(f)
            trackers = data.get(mode, [])
            if isinstance(trackers, list):
                return trackers
            else:
                print(f"Warning: trackers for mode '{mode}' in {tracker_file} not a list. Falling back.")
        except Exception as e:
            print(f"Error loading tracker file {tracker_file}: {e}")
            print("Falling back to built-in tracker lists.")

    trackers = BASE_TRACKERS.copy()
    if mode == "ultra":
        trackers.extend(ULTRA_TRACKERS)
    elif mode == "pro":
        trackers.extend(ULTRA_TRACKERS + PRO_TRACKERS)
    return trackers

def extract_domain(url):
    """Extract main domain for reporting."""
    ext = tldextract.extract(url)
    return f"{ext.domain}.{ext.suffix}" if ext.suffix else ext.domain

def scan_url(url, trackers):
    """Scan a URL for known trackers in tags and inline scripts."""
    report = []
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "lxml")
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return report

    # Check common tags
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

    # Check inline script content
    for script in soup.find_all("script"):
        content = script.string or ""
        for tracker in trackers:
            if tracker in content:
                snippet = (content[:200] + "...") if len(content) > 200 else content
                report.append({
                    "tracker": tracker,
                    "tag": "inline_script",
                    "source": snippet
                })

    return report

def main():
    parser = argparse.ArgumentParser(description="Ultra Privacy Scan")
    parser.add_argument("--target", nargs="+", required=True, help="One or more URLs to scan")
    parser.add_argument("--report", default="report.json", help="Output JSON report filename")
    parser.add_argument("--mode", choices=["normal", "ultra", "pro"], default="normal", help="Scan mode")
    parser.add_argument("--tracker-file", help="Optional JSON file with dynamic tracker lists")
    parser.add_argument("--concurrent", action="store_true", help="Scan multiple URLs concurrently")
    args = parser.parse_args()

    trackers = load_trackers(args.mode, args.tracker_file)
    results = []

    if args.concurrent and len(args.target) > 1:
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = {executor.submit(scan_url, u, trackers): u for u in args.target}
            for fut in as_completed(futures):
                url = futures[fut]
                report = fut.result()
                results.append({
                    "target": url,
                    "domain": extract_domain(url),
                    "scan_mode": args.mode,
                    "trackers_found": report,
                    "total": len(report)
                })
    else:
        for url in args.target:
            report = scan_url(url, trackers)
            results.append({
                "target": url,
                "domain": extract_domain(url),
                "scan_mode": args.mode,
                "trackers_found": report,
                "total": len(report)
            })

    with open(args.report, "w") as f:
        json.dump(results, f, indent=4)

    total = sum(r["total"] for r in results)
    print(f"Scan complete. {total} trackers found across {len(args.target)} target(s). "
          f"Report saved to {args.report}")

if __name__ == "__main__":
    main()
