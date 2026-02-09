"""TRTHaber ekonomi çubuğundan dolar, euro, altın, BIST verisi çeker."""
from __future__ import annotations

import logging
from typing import Any

import requests
from bs4 import BeautifulSoup

from .const import TRTHABER_URL

_LOGGER = logging.getLogger(__name__)

USER_AGENT = "HasWave-Doviz/1.0"
LABELS = ("BIST", "EURO", "DOLAR", "ALTIN")


def fetch_rates() -> dict[str, dict[str, str]] | None:
    """
    TRTHaber ana sayfa ekonomi çubuğunu parse eder.
    Dönen format: {"DOLAR": {"value": "...", "change": "...", "direction": "up|down|"}, ...}
    """
    try:
        response = requests.get(
            TRTHABER_URL,
            timeout=10,
            headers={"User-Agent": USER_AGENT},
        )
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        economy_bar = soup.select(".homepage-economy-bar span")
        results: dict[str, dict[str, str]] = {}
        current_label: str | None = None

        for span in economy_bar:
            text = span.get_text(strip=True)
            classes = span.get("class", [])

            if text in LABELS:
                current_label = text
                results[current_label] = {"value": "", "change": "", "direction": ""}
            elif current_label and current_label in results:
                if any(c.isdigit() for c in text):
                    if "%" in text:
                        results[current_label]["change"] = text
                        if "up" in classes:
                            results[current_label]["direction"] = "up"
                        elif "down" in classes:
                            results[current_label]["direction"] = "down"
                    else:
                        results[current_label]["value"] = text

        if results:
            _LOGGER.debug("Kurlar alındı: %s", results)
        else:
            _LOGGER.warning("TRTHaber ekonomi çubuğunda veri bulunamadı")
        return results if results else None
    except Exception as e:
        _LOGGER.error("TRTHaber veri hatası: %s", e, exc_info=True)
        return None
