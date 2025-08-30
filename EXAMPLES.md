Ultra Privacy Scan – Examples
Description

Ultra Privacy Scan identifies trackers in websites and apps, providing JSON reports of metadata and network analysis. This file shows usage examples and JSON output structure.

Running the Scan
python scan.py --target <app_or_website> [--report output.json]


Parameters:

--target: App package name, URL, or domain to scan.

--report: (Optional) Path to save JSON output. Defaults to console.

Example:

python scan.py --target example.com --report report.json

Sample JSON Output
{
  "target": "example.com",
  "scan_date": "2025-08-29T18:00:00Z",
  "trackers_found": [
    {
      "name": "Google Analytics",
      "type": "analytics",
      "url": "https://www.google-analytics.com/collect",
      "permissions_requested": ["cookies", "tracking"]
    },
    {
      "name": "Facebook Pixel",
      "type": "marketing",
      "url": "https://connect.facebook.net/fbevents.js",
      "permissions_requested": ["tracking"]
    }
  ],
  "total_trackers": 2
}

Platform Examples
Web
python scan.py --target https://example.com


Detects third-party scripts, trackers, and cookies.

Outputs structured JSON.

Android
python scan.py --target com.example.app


Analyzes APK metadata and network connections.

Detects embedded trackers in SDKs.

iOS
python scan.py --target com.example.iosapp


Examines app network requests and embedded trackers.

Shows permissions and privacy risks.

Notes

Focuses on metadata and network analysis.

Combine with manual inspection or platform-specific tools for full coverage.

Contributions to extend detection are welcome—see CONTRIBUTING.md.

One-line description for GitHub:

Examples of running Ultra Privacy Scan on websites, Android, and iOS apps, with sample JSON output and usage instructions.
