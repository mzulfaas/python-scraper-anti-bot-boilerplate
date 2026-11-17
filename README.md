# 🛡️ Python Anti-Bot Web Scraper & Client Hints Engine (Lite)

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Production Kit: Gumroad](https://img.shields.io/badge/Gumroad-Production%20Kit%20%2429-green.svg)](https://mzulfaas.gumroad.com/l/xlxvnb)

A lightweight, zero-dependency Python boilerplate designed to navigate modern web bot protections (Cloudflare, Akamai, Datadome) using synchronized `Sec-CH-UA` Client Hints, randomized browser fingerprints, and jittered exponential retry backoff.

---

### 🚨 Why 90% of Python Scrapers Get Blocked in 2026

Most scrapers fail today not because their IP is flagged, but because their **HTTP headers are inconsistent**:
1. **Missing Sec-CH-UA**: Modern browsers send Structured Client Hints (`Sec-CH-UA`, `Sec-CH-UA-Mobile`, `Sec-CH-UA-Platform`). A scraper sending only a `User-Agent` string looks immediately robotic.
2. **Platform & Engine Mismatches**: Sending a Chrome on macOS `User-Agent` while omitting `Sec-CH-UA-Platform: "macOS"` triggers instant behavioral detection.
3. **Rigid Retry Intervals**: Fixed retry loops (`sleep(2)`) are trivially identified as machine automation.

This repository demonstrates the lightweight, zero-dependency approach to aligning your browser fingerprint with real user sessions.

---

### 📦 Features (Lite vs. Production)

| Feature | Lite (Open Source) | Production Kit (Gumroad $29) |
| :--- | :---: | :---: |
| **Zero External Dependencies** | ✅ | ✅ |
| **Synchronized Sec-CH-UA Client Hints** | ✅ | ✅ |
| **Jittered Exponential Backoff** | ✅ | ✅ |
| **Randomized Realistic Browser Fingerprints** | Basic (3 UAs) | Advanced (25+ Mapped Profiles) |
| **SQLite Persistence & Automatic Migrations** | ❌ | ✅ |
| **Automatic CSV Exporter & Schema Validation** | ❌ | ✅ |
| **Proxy & Session Pool Architecture** | ❌ | ✅ |
| **Async / Multi-Threaded Batch Scraper** | ❌ | ✅ |
| **Priority Support & Updates** | ❌ | ✅ |

👉 **[Unlock the Full Production Scraper Kit on Gumroad ($29)](https://mzulfaas.gumroad.com/l/xlxvnb)**

---

### 🚀 Quickstart

Run with 0 external packages (Standard Library only):

```bash
git clone https://github.com/mzulfaas/python-scraper-anti-bot-boilerplate.git
cd python-scraper-anti-bot-boilerplate
python3 lite_scraper.py
```

### 💻 Code Example

```python
from lite_scraper import AntiBotScraper

scraper = AntiBotScraper()
html = scraper.fetch("https://httpbin.org/headers")
print(html)
```

---

### 📄 License

MIT © [Muhamad Zulfa](https://github.com/mzulfaas). Built for developers, data engineers, and automation builders.
