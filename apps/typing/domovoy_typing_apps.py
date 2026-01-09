from domovoy.applications.registration import register_app
from domovoy_typing.apps import (
    HassSyntheticEntitiesStubUpdater,
    HassSyntheticEntitiesStubUpdaterConfig,
    HassSyntheticServiceStubUpdater,
    HassSyntheticServiceStubUpdaterConfig,
)

register_app(
    app_class=HassSyntheticServiceStubUpdater,
    app_name="synthetic_services_stub",
    config=HassSyntheticServiceStubUpdaterConfig(
        stub_path=("./typings/domovoy_typing/services.pyi"),    
    ),
)

register_app(
    app_class=HassSyntheticEntitiesStubUpdater,
    app_name="synthetic_entities_stub",
    config=HassSyntheticEntitiesStubUpdaterConfig(
        stub_path=("./typings/domovoy_typing/entities.pyi"),
    ),
)
