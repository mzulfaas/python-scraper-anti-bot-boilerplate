#!/usr/bin/env python3
"""
lite_scraper.py
===============
Lightweight, Zero-Dependency Anti-Bot Web Scraper Engine.
Demonstrates synchronized Sec-CH-UA client hints and jittered backoff.

Full Production Kit available at: https://mzulfaas.gumroad.com/l/xlxvnb
"""

import logging
import random
import time
import urllib.request
import urllib.error
from typing import Optional, Dict

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [LiteScraper] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("LiteScraper")

PROFILES = [
    {
        "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "ch_ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "platform": '"macOS"',
        "mobile": "?0",
    },
    {
        "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "ch_ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "platform": '"Windows"',
        "mobile": "?0",
    },
]

class AntiBotScraper:
    def __init__(self, timeout: int = 15):
        self.timeout = timeout

    def _build_headers(self) -> Dict[str, str]:
        profile = random.choice(PROFILES)
        return {
            "User-Agent": profile["ua"],
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Sec-Ch-Ua": profile["ch_ua"],
            "Sec-Ch-Ua-Mobile": profile["mobile"],
            "Sec-Ch-Ua-Platform": profile["platform"],
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
        }

    def fetch(self, url: str, max_retries: int = 3) -> Optional[str]:
        for attempt in range(1, max_retries + 1):
            headers = self._build_headers()
            req = urllib.request.Request(url, headers=headers)
            try:
                with urllib.request.urlopen(req, timeout=self.timeout) as response:
                    return response.read().decode("utf-8", errors="ignore")
            except Exception as e:
                backoff = (2 ** attempt) + random.uniform(0.5, 1.5)
                logger.warning(f"Request failed (attempt {attempt}/{max_retries}): {e}. Retrying in {backoff:.2f}s...")
                time.sleep(backoff)
        logger.error(f"Failed to fetch {url} after {max_retries} retries.")
        return None

if __name__ == "__main__":
    scraper = AntiBotScraper()
    test_url = "https://httpbin.org/headers"
    logger.info(f"Testing anti-bot headers against {test_url}...")
    res = scraper.fetch(test_url)
    if res:
        print("\n=== Response Headers Verified by Server ===")
        print(res)
