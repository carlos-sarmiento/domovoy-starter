from __future__ import annotations

from dataclasses import dataclass

from domovoy.applications import AppBase, AppConfigBase
from domovoy.applications.registration import register_app
from domovoy.plugins.hass.types import HassValue
from domovoy_typing.entities import entities


@dataclass(kw_only=True)
class MyFirstAppConfig(AppConfigBase):
    message: str


class MyFirstApp(AppBase[MyFirstAppConfig]):
    async def initialize(self) -> None:
        self.callbacks.run_minutely(self.minutely_callback)

        self.callbacks.listen_state(entities.sun.sun, self.on_sun_changed)

    async def minutely_callback(
        self,
    ) -> None:
        self.log.info("Tick tock! I get called every minute. Message: {message}", message=self.config.message)

    async def on_sun_changed(self, old: HassValue, new: HassValue) -> None:
        self.log.info("The sun has changed from {old} to {new}", old=old, new=new)


register_app(
    app_class=MyFirstApp,
    app_name="my_first_app",
    config=MyFirstAppConfig(message="Hello World!"),
    logging_config_name="ssh_monitoring",
)
