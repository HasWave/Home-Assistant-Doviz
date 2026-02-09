"""Config flow for HasWave Döviz."""
from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult
from homeassistant.exceptions import HomeAssistantError

from .const import (
    DEFAULT_UPDATE_INTERVAL,
    DOMAIN,
    UPDATE_INTERVAL_1_HOUR,
    UPDATE_INTERVAL_24_HOURS,
    UPDATE_INTERVAL_30_MIN,
    UPDATE_INTERVAL_4_HOURS,
)
from .api import fetch_rates

_LOGGER = logging.getLogger(__name__)


async def validate_connection(hass: HomeAssistant) -> None:
    """TRTHaber'e erişimi doğrula."""
    result = await hass.async_add_executor_job(fetch_rates)
    if result is None:
        raise CannotConnect


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """HasWave Döviz config flow."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Tek adım: bağlantıyı doğrula ve kur."""
        errors = {}
        if user_input is not None:
            try:
                await validate_connection(self.hass)
            except CannotConnect:
                errors["base"] = "cannot_connect"
            except Exception:
                _LOGGER.exception("Beklenmeyen hata")
                errors["base"] = "unknown"
            else:
                return self.async_create_entry(
                    title="HasWave Döviz",
                    data={"update_interval": DEFAULT_UPDATE_INTERVAL},
                )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
            errors=errors,
        )

    @staticmethod
    def async_get_options_flow(
        config_entry: config_entries.ConfigEntry,
    ) -> config_entries.OptionsFlow:
        return OptionsFlowHandler(config_entry)


class OptionsFlowHandler(config_entries.OptionsFlow):
    """Güncelleme sıklığı seçenekleri."""

    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        self._config_entry = config_entry

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)
        opt = self._config_entry.options or {}
        data = self._config_entry.data or {}
        current = opt.get("update_interval", data.get("update_interval", DEFAULT_UPDATE_INTERVAL))
        try:
            current = int(current)
        except (TypeError, ValueError):
            current = DEFAULT_UPDATE_INTERVAL
        if current not in (UPDATE_INTERVAL_30_MIN, UPDATE_INTERVAL_1_HOUR, UPDATE_INTERVAL_4_HOURS, UPDATE_INTERVAL_24_HOURS):
            current = DEFAULT_UPDATE_INTERVAL
        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Required(
                    "update_interval",
                    default=current,
                ): vol.In({
                    UPDATE_INTERVAL_30_MIN: "30 dakika",
                    UPDATE_INTERVAL_1_HOUR: "1 saat",
                    UPDATE_INTERVAL_4_HOURS: "4 saat",
                    UPDATE_INTERVAL_24_HOURS: "24 saat",
                }),
            }),
        )


class CannotConnect(HomeAssistantError):
    """Bağlantı hatası."""
