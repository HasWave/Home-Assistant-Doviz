"""Sensor platform for HasWave Döviz - Dolar, Euro, Altın, BIST."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity, DataUpdateCoordinator

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

SENSORS: list[tuple[str, str, str]] = [
    ("dolar", "Dolar", "mdi:currency-usd"),
    ("euro", "Euro", "mdi:currency-eur"),
    ("altin", "Altın", "mdi:gold"),
    ("bist", "BIST", "mdi:chart-line"),
]

KEY_MAP = {"dolar": "DOLAR", "euro": "EURO", "altin": "ALTIN", "bist": "BIST"}


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Sensor kurulumu."""
    coordinator: DataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]["coordinator"]
    device_info = DeviceInfo(
        identifiers={(DOMAIN, entry.entry_id)},
        name=entry.title or "HasWave Döviz",
        manufacturer="HasWave",
    )
    entities = [
        DovizSensor(coordinator, entry.entry_id, key, label, icon, device_info)
        for key, label, icon in SENSORS
    ]
    async_add_entities(entities)


class DovizSensor(CoordinatorEntity, SensorEntity):
    """Döviz / BIST sensörü."""

    def __init__(
        self,
        coordinator: DataUpdateCoordinator,
        entry_id: str,
        key: str,
        label: str,
        icon: str,
        device_info: DeviceInfo,
    ) -> None:
        super().__init__(coordinator)
        self._key = key
        self._label = label
        self._attr_unique_id = f"{DOMAIN}_{entry_id}_{key}"
        self._attr_name = f"Döviz - {label}"
        self._attr_icon = icon
        self._attr_device_info = device_info

    @property
    def native_value(self) -> str | None:
        """Değer (ör. 34,50)."""
        data = self.coordinator.data
        if not data:
            return None
        item = data.get(KEY_MAP[self._key], {})
        value = (item.get("value") or "").strip()
        return value if value else None

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Değişim yüzdesi ve yön."""
        data = self.coordinator.data or {}
        item = data.get(KEY_MAP[self._key], {})
        attrs: dict[str, Any] = {}
        change = (item.get("change") or "").strip()
        if change:
            attrs["değişim"] = change
        direction = (item.get("direction") or "").strip()
        if direction:
            attrs["yön"] = direction
        return attrs
