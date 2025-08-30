# Contributing to Ultra Privacy Scan

Thank you for your interest in contributing! Contributions are welcome but optional.

## How to Contribute

1. Fork the repository on GitHub.  
2. Make your changes, which can include:
   - Adding or updating tracker rules
   - Improving metadata analysis
   - Enhancing JSON reports
   - Addressing platform-specific issues on Android, iOS, or web browsers
3. Open a Pull Request on GitHub with a description of your changes.

## JSON Output Example

```json
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
